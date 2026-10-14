"""
Carbon-Flow-Sankey (Brutto-Potenzial → realistischer Netto-Wert)
================================================================
Provolution · 2026-05-30 · adressiert LIMITATIONS #16, Reviewer-Q4 (Double-Counting).

Visualisiert, dass die Headline-Potenziale KEINE Prognosen sind und wo die
Reduktion zwischen gescreentem Brutto-Potenzial und realistischem Netto-Median
"verloren" geht (Soft/vermieden-Anteil, Overlap-Bereinigung, Umsetzungs-/
Unsicherheits-Abschlag).

Werte (alle live gelesen, seit 2026-10-14 keine Konstanten mehr):
Brutto aus canon/data/co2_master.yaml; Monte-Carlo-Netto (Szen. B / S) aus
studies/CO2_BILANZ_2026-05-28/percentiles.csv; Overlap-Beispiel aus
canon/data/overlap_matrix.yaml.

Verwendung: python studies/CARBON_FLOW_2026-05-30/build_carbon_flow_sankey.py
Output: carbon_flow_sankey.png + .svg
"""

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parents[2]
CO2 = REPO / "canon" / "data" / "co2_master.yaml"
OUTDIR = Path(__file__).parent


def read_val(text, key):
    m = re.search(rf"^\s*{key}\s*:\s*(-?\d+\.?\d*)", text, re.M)
    return float(m.group(1)) if m else None


def _fmt(v):
    """Gt-Werte ohne Rundungsverlust: 57.05 bleibt 57.05, 28.5 bleibt 28.5."""
    return f"{round(abs(v), 2):g}"


def main():
    t = CO2.read_text(encoding="utf-8")
    hard = abs(read_val(t, "reduktion_hart"))
    soft = abs(read_val(t, "vermeidung_weich"))
    total = abs(read_val(t, "total_potenzial"))

    # Monte-Carlo-Netto (Szen. B / S Median) aus percentiles.csv — Anti-Drift
    import csv
    with open(REPO / "studies" / "CO2_BILANZ_2026-05-28" / "percentiles.csv", encoding="utf-8") as f:
        med = {r["scenario"][0]: abs(float(r["p50_median"])) for r in csv.DictReader(f)}
    net_b, net_s = round(med["B"], 1), round(med["S"], 1)  # MC-Mediane wie überall mit 1 Nachkommastelle
    gap = round(hard - net_b, 1)   # Umsetzungs-/Unsicherheits-Abschlag

    # Overlap-Beispiel Domain B (overlap_matrix.yaml lever_overlaps.B_production)
    ovl = (REPO / "canon" / "data" / "overlap_matrix.yaml").read_text(encoding="utf-8")
    b_block = ovl.split("  B_production:", 1)[1]
    b07_gross, b07_net = read_val(b_block, "gross_sum"), read_val(b_block, "net")

    print(f"co2_master: hard={hard}  soft={soft}  total={total}")
    print(f"MC: Szen.B={net_b}  Szen.S={net_s}  gap(hard-netB)={gap}")

    C_BRUTTO = "#9ecae1"
    C_HARD = "#3182bd"
    C_SOFT = "#c6dbef"
    C_NET = "#238b45"
    C_GAP = "#fdae6b"

    fig = plt.figure(figsize=(12, 6.5))
    ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])
    ax.set_title("Provolution — Carbon-Flow: gescreentes Potenzial → realistischer Netto-Wert",
                 fontsize=12.5, pad=14)

    sankey = Sankey(ax=ax, scale=1.0 / total, offset=0.30,
                    head_angle=130, format=lambda v: _fmt(v) + " Gt", unit="", gap=0.5, radius=0.10)

    # Stufe 1: Brutto-Gesamtpotenzial → Hard-CO₂ + Soft/vermieden
    sankey.add(flows=[total, -hard, -soft],
               labels=[f"Brutto-Gesamt\n−{_fmt(total)}", f"Hard-CO₂\n−{_fmt(hard)}",
                       f"Soft / vermieden −{_fmt(soft)}"],
               orientations=[0, 0, 1],
               pathlengths=[0.5, 0.55, 0.18],
               trunklength=1.4,
               facecolor=C_BRUTTO, edgecolor="#555555")

    # Stufe 2: Hard-CO₂ → realistischer Netto-Median (Szen. B) + Umsetzungs-/Unsicherheits-Abschlag
    sankey.add(flows=[hard, -net_b, -gap],
               labels=["", f"Realistischer Netto-Median\n(Monte-Carlo Szen. B)\n−{_fmt(net_b)}",
                       f"Umsetzungs-/Unsicherheits-\nAbschlag −{_fmt(gap)}"],
               orientations=[0, 0, -1],
               prior=0, connect=(1, 0),
               pathlengths=[0.5, 0.7, 0.28],
               trunklength=1.4,
               facecolor=C_HARD, edgecolor="#555555")

    diagrams = sankey.finish()
    for d in diagrams:
        for txt in d.texts:
            txt.set_fontsize(9)
    diagrams[1].patch.set_facecolor(C_HARD)

    # Annotationen in leere Zonen (oben-links / unten, mit Figur-Rand)
    ax.text(0.01, 0.90,
            f"50 %-Umsetzungs-Stresstest (Szen. S):\nNetto −{net_s:.1f} Gt\n\n"
            f"Overlap-Beispiel B07–B12: brutto −{b07_gross:.1f} → −{b07_net:.1f} Gt\n(Doppelzählung bereits entfernt)",
            transform=ax.transAxes, fontsize=8.5, color="#333333", va="top",
            bbox=dict(boxstyle="round,pad=0.4", fc="#f7f7f7", ec="#cccccc"))

    fig.text(0.5, 0.015,
             "Quelle: co2_master.yaml (Brutto) · monte_carlo.py / percentiles.csv (Netto) · overlap_matrix.yaml. "
             "Werte = gescreente Potenziale unter Annahmen — keine Prognosen.",
             fontsize=7.5, color="#777777", ha="center")

    ax.axis("off")
    fig.subplots_adjust(left=0.03, right=0.97, top=0.84, bottom=0.10)
    for ext in ("png", "svg"):
        out = OUTDIR / f"carbon_flow_sankey.{ext}"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print(f"geschrieben: {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
