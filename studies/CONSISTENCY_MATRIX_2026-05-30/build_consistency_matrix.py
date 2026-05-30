"""
Hebel-Konsistenz-/Konflikt-Matrix (C-Achse-Materialisierung)
============================================================
Provolution · 2026-05-30 · adressiert LIMITATIONS #16, Reviewer-Q1/Q4.

Materialisiert die ⊥-Relation (Konsistenz-Achse C) auditierbar: für jedes
Hebel-Paar eine Beziehung aus {SYN Synergie/Kohärenz, DEP Abhängigkeit,
CONF Konflikt/Konkurrenz, OVL Bilanz-Overlap, NEUTRAL}.

GROUNDED, nicht erfunden:
- SYN/DEP-Kanten werden aus den Band-4-"Consistent:"- und "Synergien:"-Zeilen
  der jeweiligen Hebel-Sektion geparst (= dort explizit behauptete Kohärenz).
- OVL/CONF/DEP-Kanten aus dokumentierten Quellen (co2_master double_counting,
  impact_master Warnschwellen-Notizen) — hand-codiert MIT Quelle.
- Inferierte (nicht kanon-belegte) Kanten sind separat als INFERRED markiert.

Pure Python (keine Abhängigkeiten). Liest live aus dem Repo.
Verwendung: python studies/CONSISTENCY_MATRIX_2026-05-30/build_consistency_matrix.py
"""

import re
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parents[2]
KATALOG = REPO / "canon" / "de" / "HEBEL_KATALOG_v1.0.md"
BAND4 = REPO / "canon" / "de" / "04_Band4_Anwendungen_v4.2.md"
OUT_CSV = Path(__file__).parent / "consistency_matrix.csv"

ID_RE = re.compile(r"\b([A-K])(\d{1,2})\b")
RANGE_RE = re.compile(r"\b([A-K])(\d{1,2})\s*[–-]\s*([A-K]?)(\d{1,2})\b")


def norm(letter, num):
    return f"{letter}{int(num):02d}"


def extract_ids(text, valid):
    """Extrahiert Hebel-IDs (inkl. einfacher Bereichs-Expansion) aus einer Textzeile."""
    found = set()
    for m in RANGE_RE.finditer(text):
        L, a, L2, b = m.group(1), int(m.group(2)), m.group(3) or m.group(1), int(m.group(4))
        if L2 == L and b >= a:
            for n in range(a, b + 1):
                cand = norm(L, n)
                if cand in valid:
                    found.add(cand)
    for m in ID_RE.finditer(text):
        cand = norm(m.group(1), m.group(2))
        if cand in valid:
            found.add(cand)
    return found


def load_levers():
    """44 A-K-Hebel-IDs aus den HEBEL_KATALOG-Tabellenzeilen."""
    text = KATALOG.read_text(encoding="utf-8")
    ids = []
    for m in re.finditer(r"^\|\s*([A-K]\d{1,2})\s*\|", text, re.M):
        if m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


def parse_band4_synergies(valid):
    """Parst pro Band-4-Hebelsektion die 'Consistent:'- und 'Synergien:'-Zeilen → SYN-Kanten."""
    text = BAND4.read_text(encoding="utf-8")
    headers = list(re.finditer(r"^###\s+([A-K]\d{1,2}):", text, re.M))
    edges = {}          # (a,b) -> set(sources)
    covered = set()
    for i, h in enumerate(headers):
        hid = h.group(1)
        if hid not in valid:
            continue
        covered.add(hid)
        start = h.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        section = text[start:end]
        for line in section.splitlines():
            if "**Consistent:**" in line or "Synergien:" in line:
                src = "Band4:Consistent" if "**Consistent:**" in line else "Band4:Synergien"
                for tid in extract_ids(line, valid):
                    if tid != hid:
                        key = tuple(sorted((hid, tid)))
                        edges.setdefault(key, {"type": "SYN", "sources": set()})["sources"].add(src)
    return edges, covered


# --- Dokumentierte Nicht-Synergie-Kanten (hand-codiert MIT Quelle) ---
# type: OVL=Bilanz-Overlap, CONF=Konflikt/Konkurrenz, DEP=Abhängigkeit(Auflage)
DOCUMENTED = [
    # Bilanz-Overlap B07 ⊃ B08–B13 (co2_master double_counting_prevention)
    ("B07", "B08", "OVL", "co2_master:double_counting_prevention", False),
    ("B07", "B09", "OVL", "co2_master:double_counting_prevention", False),
    ("B07", "B10", "OVL", "co2_master:double_counting_prevention", False),
    ("B07", "B11", "OVL", "co2_master:double_counting_prevention", False),
    ("B07", "B12", "OVL", "co2_master:double_counting_prevention", False),
    ("B07", "B13", "OVL", "co2_master:double_counting_prevention", False),
    # B12 Biomasse ↔ Ernährung/Landnutzung: Tank-oder-Teller (impact_master B12 warning)
    ("B12", "D15", "CONF", "impact_master:B12_warning (Tank-oder-Teller/Land)", False),
    ("B12", "D18", "CONF", "impact_master:B12_warning (Tank-oder-Teller/Land)", False),
    # C12 Speicher ↔ B09/H31: Lieferketten-Transparenz/Regulierung als Tragfähigkeits-Auflage
    ("C12", "B09", "DEP", "impact_master:C12_warning (Li/Co-Lieferkette → B09-Transparenz)", False),
    ("C12", "H31", "DEP", "impact_master:C12_warning (→ H31-Regulierung zwingend)", False),
    # D16 Boden-CO2 ↔ G27: Carbon-Payment-Monitoring zwingend (impact_master D16 note)
    ("D16", "G27", "DEP", "impact_master:D16_note (G27-Monitoring der Carbon-Payments)", False),
    # B09 Materialfluss ↔ E21/Mitbestimmung: algorithmisches Management (impact_master B09 warning)
    # (kein Hebel-Hebel-Paar mit klarer ID → ausgelassen)
    # --- INFERRED (nicht kanon-belegt, zur Review markiert) ---
    ("D17", "D15", "CONF", "INFERRED: Hanf-Anbaufläche ↔ Nahrungsfläche (Flächenkonkurrenz?)", True),
    ("D17", "D18", "CONF", "INFERRED: Hanf-Anbaufläche ↔ urbane LW-Fläche?", True),
    ("B12", "D17", "CONF", "INFERRED: Biomasse ↔ Hanf-Anbaufläche (Konkurrenz?)", True),
]

PRECEDENCE = {"CONF": 3, "OVL": 2, "DEP": 1, "SYN": 0}


def main():
    levers = load_levers()
    valid = set(levers)
    n = len(levers)

    syn_edges, covered = parse_band4_synergies(valid)

    # Merge: dokumentierte Kanten in die Matrix; INFERRED separat (überschreiben NICHTS,
    # zählen NICHT in C-Proxy — nur zur Review gelistet).
    edges = {}
    for key, d in syn_edges.items():
        edges[key] = {"type": "SYN", "sources": set(d["sources"])}
    inferred_edges = []
    for a, b, typ, src, inferred in DOCUMENTED:
        if a not in valid or b not in valid:
            continue
        key = tuple(sorted((a, b)))
        if inferred:
            inferred_edges.append((key, typ, src))
            continue
        if key in edges:
            if PRECEDENCE[typ] > PRECEDENCE[edges[key]["type"]]:
                edges[key]["type"] = typ
            edges[key]["sources"].add(src)
        else:
            edges[key] = {"type": typ, "sources": {src}}

    # --- CSV-Matrix (44×44) ---
    cell = {}
    for (a, b), d in edges.items():
        cell[(a, b)] = d["type"]
        cell[(b, a)] = d["type"]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        f.write("," + ",".join(levers) + "\n")
        for r in levers:
            row = [cell.get((r, c), "") if r != c else "—" for c in levers]
            f.write(r + "," + ",".join(row) + "\n")

    # --- Per-Hebel-Profil ---
    prof = {l: {"SYN": 0, "DEP": 0, "CONF": 0, "OVL": 0} for l in levers}
    for (a, b), d in edges.items():
        prof[a][d["type"]] += 1
        prof[b][d["type"]] += 1

    print("=" * 78)
    print("  HEBEL-KONSISTENZ-/KONFLIKT-MATRIX (C-Achse) · 2026-05-30")
    print("=" * 78)
    print(f"  Hebel (A–K): {n}   ·   Band-4-Sektionen geparst: {len(covered)}")
    nocov = [l for l in levers if l not in covered]
    print(f"  Ohne Band-4-Sektion (yaml-only/stub, keine Synergien geparst): {', '.join(nocov) or '—'}")
    print(f"  Kanten gesamt: {len(edges)}  "
          f"(SYN {sum(1 for d in edges.values() if d['type']=='SYN')}, "
          f"OVL {sum(1 for d in edges.values() if d['type']=='OVL')}, "
          f"CONF {sum(1 for d in edges.values() if d['type']=='CONF')}, "
          f"DEP {sum(1 for d in edges.values() if d['type']=='DEP')})")
    print()

    print("-" * 78)
    print("  NICHT-NEUTRALE KANTEN (Konflikt/Overlap/Abhängigkeit) — auditierbar")
    print("-" * 78)
    for (a, b), d in sorted(edges.items()):
        if d["type"] in ("CONF", "OVL", "DEP"):
            print(f"  {a}↔{b}  [{d['type']}]  ← {'; '.join(sorted(d['sources']))}")
    print()

    print("-" * 78)
    print("  C-PROXY pro Hebel:  C* = 1 − (CONF + DEP_unmet) / Interaktionen")
    print("  (Interaktionen = SYN+DEP+CONF+OVL; DEP hier als erfüllbar gewertet → U≈0;")
    print("   OVL = Bilanz-Accounting, NICHT als Viability-Konflikt gezählt)")
    print("-" * 78)
    rows = []
    for l in levers:
        p = prof[l]
        inter = p["SYN"] + p["DEP"] + p["CONF"] + p["OVL"]
        k = p["CONF"]
        cstar = 1 - (k / inter) if inter else 1.0
        rows.append((cstar, l, p, inter, k))
    for cstar, l, p, inter, k in sorted(rows):
        if k > 0 or inter >= 4:
            print(f"  {l}: C*={cstar:.2f}  (SYN {p['SYN']}, DEP {p['DEP']}, CONF {p['CONF']}, OVL {p['OVL']}; Σ{inter})")
    print()

    print("-" * 78)
    print("  ZUR REVIEW: inferierte Kanten — NICHT kanon-belegt, NICHT in Matrix/C-Proxy gezählt")
    print("-" * 78)
    for (key, typ, src) in sorted(inferred_edges):
        a, b = key
        print(f"  {a}↔{b}  [{typ}]  ← {src}")
    print()
    print(f"  CSV-Matrix geschrieben: {OUT_CSV.relative_to(REPO)}")
    print("=" * 78)


if __name__ == "__main__":
    main()
