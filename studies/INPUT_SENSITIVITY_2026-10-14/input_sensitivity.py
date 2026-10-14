"""
Provolution · Input-Sensitivität pro Hebel (Roadmap Paket 1)
============================================================

Datum: 2026-10-14 · Entscheidung: canon/decisions/DEC_2026-10-14_input_sensitivity.md
Frage: Welche Eingangswerte treiben die Netto-Werte (CO₂ und all-GHG, Szenario B) am stärksten?

Methode
  1. Tornado (one-at-a-time): jede Eingangsgröße einzeln auf ihren unteren/oberen Wert,
     alle anderen auf Basis; Monte-Carlo mit identischen Draws (seed 42) → Δ Median B.
     Eingangsgrößen:
       - 41 Hebel-Werte der CO₂-Schicht (co2_master.yaml, 40 apps + 1 community)
       - 3 Overlap-Beträge (overlap_matrix.yaml, Gruppen B/C/D)
       - 6 Szenario-Parameter (monte_carlo.py: Umsetzung, Rebound, S2, S3, Engpässe, Klima)
       - 3 Gasmengen (impact_master.yaml: CH₄, N₂O, F-Gase) — nur für all-GHG
  2. Varianz-Zerlegung der Schicht-1-Eingangsunsicherheit pro Hebel (analytisch, linear).

Bandbreiten (nichts neu geschätzt)
  - Hebel: „Bandbreite X bis Y“ aus dem YAML-Kommentar, sonst ±25 %
    (co2_master methodology.uncertainty_assessment.propagation: „Total uncertainty ~±25%“).
  - Overlap-Beträge: ±25 % (gleiche Quelle; Paar-Koeffizienten sind not_sourced).
  - Szenario-Parameter: Werte der Szenarien A (unten) und C (oben), Rest auf B.
  - Gasmengen: Unsicherheitsband aus impact_master.yaml.
Hebel in Overlap-Gruppen wirken anteilig (Faktor = Gruppen-Netto / Gruppen-Brutto), weil die
Aufteilung des Overlaps auf Paare nicht belegt ist (proportionale Annahme, dokumentiert).
"""

import contextlib
import csv
import io
import os
import re
import sys

import numpy as np
import yaml

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(REPO, "canon", "data")
MC_DIR = os.path.join(REPO, "studies", "CO2_BILANZ_2026-05-28")
sys.path.insert(0, MC_DIR)


class _Quiet(io.StringIO):
    def reconfigure(self, *a, **k):
        return None


with contextlib.redirect_stdout(_Quiet()):
    import monte_carlo as mc
    import ghg_monte_carlo as ghg

DEFAULT_REL = 0.25
N = 10000
B = "B · mittel-realistisch (Erwartungswert)"
A_ = "A · konservativ-realistisch"
C_ = "C · optimistisch-realistisch"


def _yaml(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return yaml.safe_load(f)


co2 = _yaml("co2_master.yaml")
ovl = _yaml("overlap_matrix.yaml")
raw_co2 = open(os.path.join(DATA, "co2_master.yaml"), encoding="utf-8").read()

# ── Hebel, Bandbreiten, Overlap-Faktoren ─────────────────────────────────────
group_factor = {}
for dkey, g in ovl["lever_overlaps"].items():
    for m in g["group"]:
        group_factor[m] = g["net"] / g["gross_sum"]

RANGE_RE = re.compile(r"Bandbreite\s+(-?\d+(?:\.\d+)?)\s+bis\s+(-?\d+(?:\.\d+)?)")
levers = []  # (key, domain, value, low, high, factor, range_source)
for dkey, d in co2["domains"].items():
    for key, val in (d.get("apps") or {}).items():
        line = next((l for l in raw_co2.splitlines() if l.strip().startswith(key + ":")), "")
        m = RANGE_RE.search(line)
        if m:
            lo, hi = sorted([abs(float(m.group(1))), abs(float(m.group(2)))])
            src = "YAML-Bandbreite"
        else:
            lo, hi = abs(val) * (1 - DEFAULT_REL), abs(val) * (1 + DEFAULT_REL)
            src = "Standard ±25 %"
        levers.append((key, dkey, abs(val), lo, hi, group_factor.get(key, 1.0), src))
for cid, c in co2["community_integrations"]["integrations"].items():
    v = abs(c["co2_impact_gt_per_year"])
    levers.append((cid, "Community", v, v * (1 - DEFAULT_REL), v * (1 + DEFAULT_REL), 1.0, "Standard ±25 %"))

S1_BASE = mc.S1_BRUTTO_MEAN
assert abs(sum(v * f for _, _, v, _, _, f, _ in levers) - abs(S1_BASE)) < 0.06, "Hebel-Summe ≠ reduktion_hart"


# ── Monte-Carlo-Helfer (identische Draws) ────────────────────────────────────
def median_b(s1=None, params=None):
    p = dict(mc.szenarios[B])
    if params:
        p.update(params)
    old = mc.S1_BRUTTO_MEAN
    mc.S1_BRUTTO_MEAN = S1_BASE if s1 is None else s1
    # Reihenfolge wie monte_carlo.py: erst A ziehen (verworfen), dann B → identische B-Draws
    np.random.seed(42)
    pa = mc.szenarios[A_]
    mc.simulate_szenario(pa["impl"], pa["rebound"], pa["s2"], pa["s3"], pa["engpaesse"], pa["klima"], n=N)
    r = mc.simulate_szenario(p["impl"], p["rebound"], p["s2"], p["s3"], p["engpaesse"], p["klima"], n=N)
    mc.S1_BRUTTO_MEAN = old
    return float(np.median(r["netto"]))


def ghg_median_b(gas_override=None, s1=None):
    """all-GHG-Median B; gas_override = {gas_block: neuer Punktwert (negativ)}."""
    saved = {}
    if gas_override:
        for gas, val in gas_override.items():
            blk = ghg.ga[gas]
            saved[gas] = (blk["gesamt"], list(blk["unsicherheit"]), {k: v["total"] for k, v in blk["domains"].items()})
            scale = val / blk["gesamt"]
            blk["gesamt"] = val
            blk["unsicherheit"] = [x * scale for x in blk["unsicherheit"]]
            for dk in blk["domains"]:
                blk["domains"][dk]["total"] *= scale
    old = mc.S1_BRUTTO_MEAN
    mc.S1_BRUTTO_MEAN = S1_BASE if s1 is None else s1
    out = float(np.median(ghg.run()[B]["ghg"]))
    mc.S1_BRUTTO_MEAN = old
    for gas, (g, u, doms) in saved.items():
        blk = ghg.ga[gas]
        blk["gesamt"], blk["unsicherheit"] = g, u
        for dk, v in doms.items():
            blk["domains"][dk]["total"] = v
    return out


base_co2 = median_b()
base_ghg = ghg_median_b()
assert np.isclose(base_co2, mc.results[B]["p50"]), "Basis weicht von monte_carlo.py ab"

rows = []  # (kategorie, name, low_input, high_input, d_co2_low, d_co2_high, d_ghg_low, d_ghg_high, quelle)


def add_s1_input(cat, name, lo_s1_delta, hi_s1_delta, lo_in, hi_in, src):
    # Δ Schicht 1 (positiv = mehr Reduktion) → S1 wird negativer
    c_lo = median_b(S1_BASE - lo_s1_delta) - base_co2
    c_hi = median_b(S1_BASE - hi_s1_delta) - base_co2
    g_lo = ghg_median_b(s1=S1_BASE - lo_s1_delta) - base_ghg
    g_hi = ghg_median_b(s1=S1_BASE - hi_s1_delta) - base_ghg
    rows.append((cat, name, lo_in, hi_in, c_lo, c_hi, g_lo, g_hi, src))


for key, dom, val, lo, hi, fac, src in levers:
    add_s1_input("Hebel", key, (lo - val) * fac, (hi - val) * fac, -lo, -hi,
                 src + (f", Overlap-Faktor {fac:.2f}" if fac != 1.0 else ""))

for dkey, g in ovl["lever_overlaps"].items():
    o = g["overlap"]
    # mehr Overlap = weniger Netto-Reduktion
    add_s1_input("Overlap", f"Overlap {dkey}", -(-o * DEFAULT_REL), -(o * DEFAULT_REL),
                 o * (1 - DEFAULT_REL), o * (1 + DEFAULT_REL), "Standard ±25 %")

PNAMES = {"impl": "Umsetzungsrate", "rebound": "Rebound-Rate", "s2": "Schicht 2 Kaskaden",
          "s3": "Schicht 3 Folgewirkungen", "engpaesse": "Material-Engpässe", "klima": "Klima-Verschlechterung"}
for k, label in PNAMES.items():
    lo_v, hi_v = mc.szenarios[A_][k], mc.szenarios[C_][k]
    c_lo = median_b(params={k: lo_v}) - base_co2
    c_hi = median_b(params={k: hi_v}) - base_co2
    # all-GHG: Parameter nur in Szenario B tauschen, ghg_monte_carlo.run() rechnet alle Szenarien neu
    g = []
    orig = mc.szenarios[B][k]
    for v in (lo_v, hi_v):
        mc.szenarios[B][k] = v
        g.append(float(np.median(ghg.run()[B]["ghg"])) - base_ghg)
    mc.szenarios[B][k] = orig
    rows.append(("Szenario-Parameter", label, lo_v, hi_v, c_lo, c_hi, g[0], g[1], "Szenario A ↔ C"))

for gas, label in (("methane_ch4", "CH₄-Menge"), ("nitrous_oxide_n2o", "N₂O-Menge"), ("f_gases", "F-Gas-Menge")):
    lo_b, hi_b = sorted(ghg.ga[gas]["unsicherheit"], key=abs)
    g_lo = ghg_median_b({gas: lo_b}) - base_ghg
    g_hi = ghg_median_b({gas: hi_b}) - base_ghg
    rows.append(("Gasmenge", label, lo_b, hi_b, None, None, g_lo, g_hi, "impact_master Unsicherheitsband"))


def swing(r, co2_=True):
    a, b = (r[4], r[5]) if co2_ else (r[6], r[7])
    return None if a is None else abs(b - a)


# ── Varianz-Zerlegung Schicht 1 (linear, unabhängige Dreiecksverteilungen) ──
var = []
for key, dom, val, lo, hi, fac, src in levers:
    v_tri = (lo**2 + val**2 + hi**2 - lo * val - lo * hi - val * hi) / 18.0
    var.append((key, (fac**2) * v_tri))
vtot = sum(v for _, v in var)
s1_sd_levers = vtot ** 0.5

# ── Ausgabe ──────────────────────────────────────────────────────────────────
with open(os.path.join(HERE, "tornado_co2_ghg.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["kategorie", "eingang", "wert_unten", "wert_oben", "d_co2_unten", "d_co2_oben",
                "swing_co2", "d_ghg_unten", "d_ghg_oben", "swing_ghg", "quelle_bandbreite"])
    for r in rows:
        fmt = lambda x: "" if x is None else f"{x:.3f}"
        w.writerow([r[0], r[1], fmt(r[2]), fmt(r[3]), fmt(r[4]), fmt(r[5]), fmt(swing(r)),
                    fmt(r[6]), fmt(r[7]), fmt(swing(r, False)), r[8]])
with open(os.path.join(HERE, "variance_levers.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["hebel", "varianz_anteil_pct"])
    for k, v in sorted(var, key=lambda x: -x[1]):
        w.writerow([k, f"{100 * v / vtot:.2f}"])

print("=" * 78)
print("INPUT-SENSITIVITÄT · Szenario B (Median, Gt/yr) · seed 42 · N =", N)
print("=" * 78)
print(f"Basis: CO₂ netto {base_co2:+.2f} · all-GHG netto {base_ghg:+.2f}")
print(f"Schicht 1 = {S1_BASE} = Σ Hebel × Overlap-Faktor (geprüft)")
print()
print("TOP 15 · CO₂-Netto (Swing = |Δ oben − Δ unten|)")
for r in sorted([r for r in rows if swing(r) is not None], key=lambda r: -swing(r))[:15]:
    print(f"  {r[0]:<19} {r[1]:<34} Swing {swing(r):5.2f}   ({r[4]:+.2f} … {r[5]:+.2f})")
print()
print("TOP 10 · all-GHG-Netto")
for r in sorted([r for r in rows if swing(r, False) is not None], key=lambda r: -swing(r, False))[:10]:
    print(f"  {r[0]:<19} {r[1]:<34} Swing {swing(r, False):5.2f}")
print()
print("Varianz-Zerlegung Schicht 1 (Eingangsunsicherheit der Hebel-Werte):")
for k, v in sorted(var, key=lambda x: -x[1])[:8]:
    print(f"  {k:<34} {100 * v / vtot:5.1f} %")
top3 = sum(v for _, v in sorted(var, key=lambda x: -x[1])[:3]) / vtot
print(f"  Top 3 zusammen: {100 * top3:.1f} %")
print()
print(f"Implizite Streuung von Schicht 1 aus Hebel-Bandbreiten (unabhängig): σ = {s1_sd_levers:.2f} Gt "
      f"= {100 * s1_sd_levers / abs(S1_BASE):.1f} % · monte_carlo.py nimmt pauschal 10 % an")


# ── Figur: Tornado CO₂ + all-GHG (DE/EN) ─────────────────────────────────────
def tornado_figure(lang="de"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    T = {
        "de": {"t": "Input-Sensitivität · Szenario B (Median): Δ bei unterem / oberem Eingangswert",
               "co2": f"CO₂ netto (Basis {base_co2:+.1f} Gt/yr)", "ghg": f"alle Treibhausgase netto (Basis {base_ghg:+.1f} Gt CO₂eq/yr)",
               "x": "Δ Netto-Median [Gt/yr]  (negativ = mehr Reduktion)", "lo": "unterer Wert", "hi": "oberer Wert",
               "src": "Quelle: input_sensitivity.py · co2_master v1.7 · overlap_matrix v1.1 · monte_carlo.py (seed 42) · "
                      "Bandbreiten: YAML oder Standard ±25 %; Szenario-Parameter A↔C",
               "cat": {"Hebel": "Hebel", "Overlap": "Overlap", "Szenario-Parameter": "Szenario", "Gasmenge": "Gas"}},
        "en": {"t": "Input sensitivity · scenario B (median): Δ at lower / upper input value",
               "co2": f"CO₂ net (base {base_co2:+.1f} Gt/yr)", "ghg": f"all greenhouse gases net (base {base_ghg:+.1f} Gt CO₂eq/yr)",
               "x": "Δ net median [Gt/yr]  (negative = more reduction)", "lo": "lower value", "hi": "upper value",
               "src": "Source: input_sensitivity.py · co2_master v1.7 · overlap_matrix v1.1 · monte_carlo.py (seed 42) · "
                      "ranges: YAML or default ±25 %; scenario parameters A↔C",
               "cat": {"Hebel": "lever", "Overlap": "overlap", "Szenario-Parameter": "scenario", "Gasmenge": "gas"}},
    }[lang]
    EN_P = {"Umsetzungsrate": "implementation rate", "Rebound-Rate": "rebound rate", "Schicht 2 Kaskaden": "layer 2 cascades",
            "Schicht 3 Folgewirkungen": "layer 3 follow-on", "Material-Engpässe": "material bottlenecks",
            "Klima-Verschlechterung": "climate deterioration", "CH₄-Menge": "CH₄ amount", "N₂O-Menge": "N₂O amount",
            "F-Gas-Menge": "F-gas amount"}
    fig, axes = plt.subplots(1, 2, figsize=(15, 8))
    for ax, is_co2, title in ((axes[0], True, T["co2"]), (axes[1], False, T["ghg"])):
        top = sorted([r for r in rows if swing(r, is_co2) is not None], key=lambda r: -swing(r, is_co2))[:15][::-1]
        for i, r in enumerate(top):
            lo, hi = (r[4], r[5]) if is_co2 else (r[6], r[7])
            ax.barh(i, lo, color="#9ecae1", edgecolor="black", lw=0.6, label=T["lo"] if i == 0 else None)
            ax.barh(i, hi, color="#3182bd", edgecolor="black", lw=0.6, label=T["hi"] if i == 0 else None)
        names = []
        for r in top:
            nm = r[1] if lang == "de" else EN_P.get(r[1], r[1])
            names.append(f"{nm}  [{T['cat'][r[0]]}]")
        ax.set_yticks(range(len(top)))
        ax.set_yticklabels(names, fontsize=8.5)
        ax.axvline(0, color="black", lw=0.8)
        ax.set_title(title, fontsize=11, fontweight="bold")
        ax.set_xlabel(T["x"], fontsize=9)
        ax.grid(axis="x", alpha=0.3)
        ax.legend(fontsize=8, loc="lower right")
    fig.suptitle(T["t"], fontsize=13, fontweight="bold")
    fig.text(0.01, 0.005, T["src"], fontsize=7, color="#666666")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    out = "Figure_Tornado" + ("" if lang == "de" else "_EN")
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(HERE, f"{out}.{ext}"), dpi=200 if ext == "png" else None,
                    bbox_inches="tight", facecolor="white")
    plt.close(fig)


tornado_figure("de")
tornado_figure("en")
