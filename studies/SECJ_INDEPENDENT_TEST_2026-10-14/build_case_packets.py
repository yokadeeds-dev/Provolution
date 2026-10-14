"""
SEC-J Independent Test · Fallauswahl + verblindete Fallmappen (Roadmap Paket 2)
==============================================================================

Datum: 2026-10-14 · Protokoll: PROTOCOL.md · Entscheidung: canon/decisions/DEC_2026-10-14_secj_independent_test.md

1. Fallauswahl (deterministisch, seed 42) aus den individuell SEC-J-bewerteten Hebeln
   (impact_master.yaml → sec_j_scores.individual_calculated), die einen Vollabschnitt in
   Band 4 v4.2 haben (STUB/yaml-only ausgeschlossen):
     - geschichtet nach Domäne (B 3 · C 2 · D 3 · K 2 · I 1 · J 1 = 12 Testfälle),
     - der Hebel mit dem niedrigsten J ist Pflicht (Spannweite der J-Achse),
     - 2 Trainingsfälle aus dem Rest (nur zur Kalibrierung, nicht ausgewertet).
2. Verblindete Fallmappe je Fall aus Band 4: behalten werden Definition, Problem, Zielgruppe,
   Wirkung, Ressourcen, Skalierung, Fallbeispiele, Synergien. Entfernt werden alle Autoren-
   Bewertungen: SEC-J-Score-Zeilen, Abschnitt „SEC-NACHWEIS“, Abschnitt „AGENTIC POTENZIAL“,
   Verweise auf Kanon/Archiv. Ein Leak-Check bricht ab, falls Score-Spuren übrig bleiben.
3. Ausgaben: cases.csv (Auswahl, OHNE Autoren-Scores), author_scores.csv (getrennt, erst bei der
   Auswertung öffnen), case_packets/*.md, score_sheet_template.csv.
"""

import csv
import os
import random
import re
import sys

import yaml

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
BAND4 = os.path.join(REPO, "canon", "de", "04_Band4_Anwendungen_v4.2.md")
IMPACT = os.path.join(REPO, "canon", "data", "impact_master.yaml")

QUOTA = {"B": 3, "C": 2, "D": 3, "K": 2, "I": 1, "J": 1}
N_TRAIN = 2
SEED = 42

with open(IMPACT, encoding="utf-8") as f:
    secj = yaml.safe_load(f)["sec_j_scores"]["individual_calculated"]
band4 = open(BAND4, encoding="utf-8").read()

# Band-4-Abschnitte: "### X99: TITEL" bis zum nächsten "### " oder "## "
sections = {}
for m in re.finditer(r"^### ([A-K]\d\d): (.+?)$(.*?)(?=^### |^## |\Z)", band4, re.M | re.S):
    sections[m.group(1)] = (m.group(2).strip(), m.group(3))

pool = []
for key, v in secj.items():
    lid = key.split("_")[0]
    if not isinstance(v, dict) or not all(k in v for k in ("s", "e", "c", "j", "sec_j")):
        continue
    if lid not in sections or "STUB" in sections[lid][0]:
        continue
    pool.append({"id": lid, "key": key, "title": sections[lid][0], "domain": lid[0],
                 "s": v["s"], "e": v["e"], "c": v["c"], "j": v["j"], "sec_j": v["sec_j"]})

rng = random.Random(SEED)
lowest_j = min(pool, key=lambda r: r["j"])
selected = [lowest_j]
for dom, q in QUOTA.items():
    cands = sorted([r for r in pool if r["domain"] == dom and r is not lowest_j], key=lambda r: r["id"])
    rng.shuffle(cands)
    need = q - sum(1 for r in selected if r["domain"] == dom)
    selected += cands[:max(need, 0)]
rest = sorted([r for r in pool if r not in selected], key=lambda r: r["id"])
rng.shuffle(rest)
training = rest[:N_TRAIN]
assert len(selected) == sum(QUOTA.values()), f"{len(selected)} Testfälle statt {sum(QUOTA.values())}"

# Reihenfolge für die Rater zufällig (seed), Fall-Codes ohne Hebel-ID → zusätzliche Verblindung
rng.shuffle(selected)
for i, r in enumerate(training, 1):
    r["code"] = f"T{i:02d}"
for i, r in enumerate(selected, 1):
    r["code"] = f"F{i:02d}"

DROP_SECTIONS = ("NACHWEIS", "AGENTIC", "OFFENE PUNKTE")  # NACHWEIS deckt SEC- und SEC-J-NACHWEIS ab
DROP_LINE = re.compile(r"SEC-J|SEC-Score|SEC:|\bSEC\b|Score|✅|⚠️|\bJ\s*=\s*0|\bW_min\b|\*\*CANON:\*\*|\*\*Archiv:\*\*|"
                       r"Band:\*\*|PS-U|PF-|Probatio", re.I)
LEAK = re.compile(r"SEC-|NACHWEIS|AGENTIC|\bS:\s*0[.,]\d|\bJ:\s*0[.,]\d|Score|✅|PS-U|Probatio|\bPR #", re.I)


def blind_text(body):
    out, skip = [], False
    for line in body.splitlines():
        h = re.match(r"^#### \d+\.\s*(.+)$", line)
        if h:
            skip = any(s in h.group(1).upper() for s in DROP_SECTIONS)
            if not skip:
                out.append(re.sub(r"^#### \d+\.\s*", "### ", line))
            continue
        if skip or DROP_LINE.search(line):
            continue
        out.append(line)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    text = re.sub(r"(\n-{3,})+\s*$", "", text).strip()  # abschließende Trennlinien
    return text


os.makedirs(os.path.join(HERE, "case_packets"), exist_ok=True)
for r in training + selected:
    title, body = sections[r["id"]]
    txt = blind_text(body)
    if LEAK.search(txt):
        raise SystemExit(f"Leak in Fallmappe {r['code']} ({r['id']}): {LEAK.search(txt).group(0)}")
    hdr = (f"# Fall {r['code']}{' (Training)' if r['code'].startswith('T') else ''}: {title.title()}\n\n"
           "> Verblindete Fallbeschreibung aus Provolution Band 4 v4.2. Alle Bewertungen der Autoren "
           "(Scores, Begründungen, Nachweise) sind entfernt. Bitte nur mit RUBRIC.md bewerten.\n\n")
    with open(os.path.join(HERE, "case_packets", f"{r['code']}.md"), "w", encoding="utf-8") as f:
        f.write(hdr + txt + "\n")

with open(os.path.join(HERE, "cases.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["code", "rolle", "domain", "titel"])
    for r in training + selected:
        w.writerow([r["code"], "training" if r["code"].startswith("T") else "test", r["domain"], r["title"].title()])

with open(os.path.join(HERE, "author_scores.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["code", "hebel", "s", "e", "c", "j", "sec_j"])
    for r in selected:
        w.writerow([r["code"], r["key"], r["s"], r["e"], r["c"], r["j"], r["sec_j"]])

with open(os.path.join(HERE, "score_sheet_template.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["rater_id", "runde", "code", "S", "E", "C", "J", "sicherheit_1_5", "minuten", "kommentar"])
    for r in training + selected:
        w.writerow(["R?", "1", r["code"], "", "", "", "", "", "", ""])

print(f"Pool: {len(pool)} Hebel mit Vollabschnitt · Test: {len(selected)} · Training: {len(training)}")
print("Pflichtfall (niedrigstes J):", lowest_j["id"], lowest_j["j"])
print("Testfälle:", ", ".join(f"{r['code']}={r['id']}" for r in sorted(selected, key=lambda r: r["code"])))
print("Training:", ", ".join(f"{r['code']}={r['id']}" for r in training))
js = [r["j"] for r in selected]
print(f"Spannweite Autoren-SEC-J im Test-Set: {min(r['sec_j'] for r in selected)} – {max(r['sec_j'] for r in selected)}; "
      f"J: {min(js)} – {max(js)}")
