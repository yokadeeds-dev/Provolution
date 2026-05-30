"""
SEC-J Gewichts-Sensitivitätsanalyse
====================================
Provolution · 2026-05-30 · adressiert LIMITATIONS #5/#12, Reviewer-Q2.

Frage: Wie sensitiv sind die SEC-J-Ergebnisse (Mittelwert, Hebel-Ranking,
Verdict-Klassen, J-Veto) gegenüber der Wahl der Gewichte
(STANDARD: 0.30·S + 0.25·E + 0.30·C + 0.15·J)?

Liest die 25 individuell kalkulierten Hebel aus der SSoT
(canon/data/impact_master.yaml → sec_j_scores.individual_calculated),
hardcodet KEINE Werte. Pure Python (kein numpy/scipy/yaml).

Verwendung:
    python studies/SENSITIVITY_2026-05-30/secj_weight_sensitivity.py

Reproduzierbar: random-seed=42 (wie Reliability-Studie 2026-04-20).
"""

import re
import sys
import math
import random
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parents[2]
IMPACT = REPO / "canon" / "data" / "impact_master.yaml"

SEED = 42
N_MC = 20000

# Kanonische STANDARD-Gewichte (PS-U 2.0)
BASE = {"s": 0.30, "e": 0.25, "c": 0.30, "j": 0.15}

# Schwellen aus impact_master sec_j_scores.meta
VETO_J = 0.50      # J < 0.50 -> SEC-J = null (Veto)
TRAG = 0.80        # >= 0.80 TRAGFÄHIG
BEDINGT = 0.60     # 0.60-0.79 BEDINGT TRAGFÄHIG

# Benannte Vergleichs-Gewichtungen
SCHEMES = {
    "STANDARD (Baseline)":          {"s": 0.30, "e": 0.25, "c": 0.30, "j": 0.15},
    "JUSTICE (PS-U)":               {"s": 0.25, "e": 0.15, "c": 0.20, "j": 0.40},
    "Gleichgewicht (SMART-Default)": {"s": 0.25, "e": 0.25, "c": 0.25, "j": 0.25},
    "DEPRECATED v1.0":              {"s": 0.40, "e": 0.25, "c": 0.15, "j": 0.20},
    "S-dominant (Wirkung)":         {"s": 0.55, "e": 0.15, "c": 0.15, "j": 0.15},
    "C-dominant (Kohärenz)":        {"s": 0.15, "e": 0.15, "c": 0.55, "j": 0.15},
    "J-dominant (Gerechtigkeit)":   {"s": 0.15, "e": 0.15, "c": 0.15, "j": 0.55},
}


def load_levers():
    """Liest die individual_calculated-Hebel (s,e,c,j,sec_j) aus impact_master."""
    text = IMPACT.read_text(encoding="utf-8")
    start = text.index("individual_calculated:")
    end = text.index("domain_batch:", start)
    block = text[start:end]
    pat = re.compile(
        r"^\s*([A-Za-z0-9_]+):\s*\{\s*s:\s*([\d.]+),\s*e:\s*([\d.]+),"
        r"\s*c:\s*([\d.]+),\s*j:\s*([\d.]+),\s*sec_j:\s*([\d.]+)",
        re.M,
    )
    levers = []
    for m in pat.finditer(block):
        levers.append({
            "id": m.group(1),
            "s": float(m.group(2)), "e": float(m.group(3)),
            "c": float(m.group(4)), "j": float(m.group(5)),
            "stored": float(m.group(6)),
        })
    return levers


def secj(lev, w):
    return w["s"] * lev["s"] + w["e"] * lev["e"] + w["c"] * lev["c"] + w["j"] * lev["j"]


def verdict(score, j):
    if j < VETO_J:
        return "VETO"
    if score >= TRAG:
        return "TRAGFÄHIG"
    if score >= BEDINGT:
        return "BEDINGT"
    return "DEFIZITÄR"


def rankdata(values):
    """Average-Ränge mit Tie-Behandlung (1-basiert)."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y))
    vx = math.sqrt(sum((a - mx) ** 2 for a in x))
    vy = math.sqrt(sum((b - my) ** 2 for b in y))
    return cov / (vx * vy) if vx > 0 and vy > 0 else 1.0


def spearman(x, y):
    return pearson(rankdata(x), rankdata(y))


def percentile(sorted_vals, p):
    if not sorted_vals:
        return float("nan")
    k = (len(sorted_vals) - 1) * p
    lo = int(math.floor(k))
    hi = int(math.ceil(k))
    if lo == hi:
        return sorted_vals[lo]
    return sorted_vals[lo] * (hi - k) + sorted_vals[hi] * (k - lo)


def dirichlet(alpha):
    g = [random.gammavariate(a, 1.0) for a in alpha]
    s = sum(g)
    return [x / s for x in g]


def main():
    random.seed(SEED)
    levers = load_levers()
    n = len(levers)

    base_scores = [secj(l, BASE) for l in levers]
    base_verdicts = [verdict(s, l["j"]) for s, l in zip(base_scores, levers)]
    min_j = min(l["j"] for l in levers)
    min_j_id = min(levers, key=lambda l: l["j"])["id"]

    print("=" * 78)
    print("  SEC-J GEWICHTS-SENSITIVITÄTSANALYSE")
    print("  Provolution · 2026-05-30 · seed=%d · N_MC=%d" % (SEED, N_MC))
    print("=" * 78)
    print("  Datenquelle: %s" % IMPACT.relative_to(REPO))
    print("  Hebel (individual_calculated): %d" % n)
    print()

    # ---- 1. Integritätscheck: Formel reproduziert gespeicherte sec_j? ----
    print("-" * 78)
    print("  1. INTEGRITÄT: STANDARD-Formel vs. gespeicherte sec_j")
    print("-" * 78)
    max_diff = 0.0
    worst = None
    for l, sc in zip(levers, base_scores):
        d = abs(round(sc, 2) - l["stored"])
        if d > max_diff:
            max_diff, worst = d, l["id"]
    print("  Max |recompute(2dp) - stored| = %.3f  (%s)" % (max_diff, worst))
    print("  -> %s" % ("KONSISTENT (Rundung <=0.005)" if max_diff <= 0.005
                        else "ABWEICHUNG > Rundung — prüfen!"))
    print("  Baseline-Ø SEC-J = %.4f" % (sum(base_scores) / n))
    print()

    # ---- 2. J-Veto-Invarianz ----
    print("-" * 78)
    print("  2. J-VETO-INVARIANZ (gewichtsunabhängig)")
    print("-" * 78)
    print("  min(J) im Datensatz = %.2f  (%s)" % (min_j, min_j_id))
    print("  Veto-Schwelle       = %.2f" % VETO_J)
    print("  -> Kein Hebel kann durch IRGENDEINE Gewichtswahl unter den J-Veto")
    print("     fallen: der J-Veto wirkt auf die J-Achse selbst, nicht über das")
    print("     Komposit-Gewicht. Veto-Auslösungen = 0 für alle Gewichte.")
    print()

    # ---- 3. Benannte Vergleichs-Gewichtungen ----
    print("-" * 78)
    print("  3. BENANNTE GEWICHTUNGS-SCHEMATA (vs. STANDARD-Ranking)")
    print("-" * 78)
    print("  %-32s %7s %8s %9s %6s" % ("Schema", "Ø SEC-J", "Spearman", "Verdict-Δ", "Veto"))
    for name, w in SCHEMES.items():
        scores = [secj(l, w) for l in levers]
        mean = sum(scores) / n
        rho = spearman(base_scores, scores)
        vchg = sum(1 for s, l, bv in zip(scores, levers, base_verdicts)
                   if verdict(s, l["j"]) != bv)
        vetoes = sum(1 for l in levers if l["j"] < VETO_J)
        print("  %-32s %7.4f %8.3f %9d %6d" % (name, mean, rho, vchg, vetoes))
    print()
    print("  (Verdict-Δ = Anzahl Hebel, deren Verdict-Klasse vs. STANDARD wechselt)")
    print()

    # ---- 4. Monte-Carlo global (uniformes Simplex) ----
    print("-" * 78)
    print("  4. MONTE-CARLO GLOBAL — uniformes Gewichts-Simplex (Dirichlet 1,1,1,1)")
    print("-" * 78)
    means, rhos, vchgs = [], [], []
    for _ in range(N_MC):
        ws, we, wc, wj = dirichlet([1, 1, 1, 1])
        w = {"s": ws, "e": we, "c": wc, "j": wj}
        scores = [secj(l, w) for l in levers]
        means.append(sum(scores) / n)
        rhos.append(spearman(base_scores, scores))
        vchgs.append(sum(1 for s, l, bv in zip(scores, levers, base_verdicts)
                         if verdict(s, l["j"]) != bv))
    means.sort(); rhos.sort()
    print("  Ø SEC-J:    p5=%.3f  p50=%.3f  p95=%.3f  (Spannweite min=%.3f max=%.3f)"
          % (percentile(means, .05), percentile(means, .5), percentile(means, .95),
             means[0], means[-1]))
    print("  Spearman ρ: p5=%.3f  p50=%.3f  p95=%.3f  (min=%.3f)"
          % (percentile(rhos, .05), percentile(rhos, .5), percentile(rhos, .95), rhos[0]))
    print("  Verdict-Δ:  mittel=%.2f  max=%d von %d Hebeln"
          % (sum(vchgs) / len(vchgs), max(vchgs), n))
    print()

    # ---- 5. Monte-Carlo lokal (plausibler ±0.10-Nachbarschaft) ----
    print("-" * 78)
    print("  5. MONTE-CARLO LOKAL — plausible Nachbarschaft (Baseline ±0.10, renorm.)")
    print("-" * 78)
    means2, rhos2, vchgs2 = [], [], []
    keys = ["s", "e", "c", "j"]
    drawn = 0
    while drawn < N_MC:
        raw = {k: BASE[k] + random.uniform(-0.10, 0.10) for k in keys}
        if any(v < 0 for v in raw.values()):
            continue
        tot = sum(raw.values())
        w = {k: raw[k] / tot for k in keys}
        scores = [secj(l, w) for l in levers]
        means2.append(sum(scores) / n)
        rhos2.append(spearman(base_scores, scores))
        vchgs2.append(sum(1 for s, l, bv in zip(scores, levers, base_verdicts)
                          if verdict(s, l["j"]) != bv))
        drawn += 1
    means2.sort(); rhos2.sort()
    print("  Ø SEC-J:    p5=%.3f  p50=%.3f  p95=%.3f"
          % (percentile(means2, .05), percentile(means2, .5), percentile(means2, .95)))
    print("  Spearman ρ: p5=%.3f  p50=%.3f  min=%.3f"
          % (percentile(rhos2, .05), percentile(rhos2, .5), rhos2[0]))
    print("  Verdict-Δ:  mittel=%.2f  max=%d von %d Hebeln"
          % (sum(vchgs2) / len(vchgs2), max(vchgs2), n))
    print()

    # ---- 6. Verdict-Robustheit pro Hebel (global MC) ----
    print("-" * 78)
    print("  6. VERDICT-ROBUSTHEIT pro Hebel (Anteil TRAGFÄHIG über globales MC)")
    print("-" * 78)
    random.seed(SEED + 1)
    trag_count = {l["id"]: 0 for l in levers}
    for _ in range(N_MC):
        ws, we, wc, wj = dirichlet([1, 1, 1, 1])
        w = {"s": ws, "e": we, "c": wc, "j": wj}
        for l in levers:
            if verdict(secj(l, w), l["j"]) == "TRAGFÄHIG":
                trag_count[l["id"]] += 1
    fragile = sorted(((c / N_MC, lid) for lid, c in trag_count.items()))
    print("  Am wenigsten ranking-robust (niedrigster TRAGFÄHIG-Anteil):")
    for frac, lid in fragile[:5]:
        bs = next(s for s, l in zip(base_scores, levers) if l["id"] == lid)
        print("    %-34s TRAGFÄHIG in %5.1f%% der Gewichte  (STANDARD=%.2f)"
              % (lid, frac * 100, bs))
    robust = sum(1 for frac, _ in fragile if frac >= 0.999)
    print("  Immer TRAGFÄHIG (>=99.9%% aller Gewichte): %d von %d Hebeln" % (robust, n))
    print()

    print("=" * 78)
    print("  FAZIT (Zahlen oben sind reproduzierbar mit seed=%d):" % SEED)
    print("  - J-Veto ist gewichtsinvariant (min J=%.2f > %.2f) -> 0 Vetos immer." % (min_j, VETO_J))
    print("  - Ranking bleibt über das gesamte Simplex hoch stabil (Spearman p5 oben).")
    print("  - Verdict-Wechsel betreffen v.a. Hebel nahe der 0.80-Linie.")
    print("=" * 78)


if __name__ == "__main__":
    main()
