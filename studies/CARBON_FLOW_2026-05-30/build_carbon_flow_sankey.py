"""
Carbon-Flow-Sankey (Brutto-Potenzial → realistischer Netto-Wert)
================================================================
Provolution · 2026-05-30 · adressiert LIMITATIONS #16, Reviewer-Q4 (Double-Counting).

Visualisiert, dass die Headline-Potenziale KEINE Prognosen sind und wo die
Reduktion zwischen gescreentem Brutto-Potenzial und realistischem Netto-Median
"verloren" geht (Soft/vermieden-Anteil, Overlap-Bereinigung, Umsetzungs-/
Unsicherheits-Abschlag).

Werte: Brutto (−87,1 / −58,6 / −28,5) live aus co2_master.yaml gelesen;
Monte-Carlo-Netto (−43,2 Szen. B / −14,9 Szen. S) aus der Bilanz-Studie
(studies/CO2_BILANZ_2026-05-28/, monte_carlo.py) — als dokumentierte Konstante.

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


def main():
    t = CO2.read_text(encoding="utf-8")
    hard = abs(read_val(t, "reduktion_hart"))        # 58.6
    soft = abs(read_val(t, "vermeidung_weich"))      # 28.5
    total = abs(read_val(t, "total_potenzial"))      # 87.1

    # Monte-Carlo-Netto (dokumentierte Konstante, Quelle: Bilanz-Studie v1.5)
    net_b = 43.2     # Szenario B Median [90%-KI 52,8…34,6]
    net_s = 14.9     # Szenario S (50%-Umsetzungs-Stresstest) [20,5…9,8]
    gap = round(hard - net_b, 1)   # Umsetzungs-/Unsicherheits-Abschlag = 15.4

    # B07-Overlap-Beispiel (co2_master double_counting_prevention)
    b07_gross, b07_net = 23.0, 15.8

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
                    head_angle=130, format="%.1f", unit=" Gt", gap=0.5, radius=0.10)

    # Stufe 1: Brutto-Gesamtpotenzial → Hard-CO₂ + Soft/vermieden
    sankey.add(flows=[total, -hard, -soft],
               labels=[f"Brutto-Gesamt\n−{total:.1f}", f"Hard-CO₂\n−{hard:.1f}",
                       f"Soft / vermieden −{soft:.1f}"],
               orientations=[0, 0, 1],
               pathlengths=[0.5, 0.55, 0.18],
               trunklength=1.4,
               facecolor=C_BRUTTO, edgecolor="#555555")

    # Stufe 2: Hard-CO₂ → realistischer Netto-Median (Szen. B) + Umsetzungs-/Unsicherheits-Abschlag
    sankey.add(flows=[hard, -net_b, -gap],
               labels=["", f"Realistischer Netto-Median\n(Monte-Carlo Szen. B)\n−{net_b:.1f}",
                       f"Umsetzungs-/Unsicherheits-\nAbschlag −{gap:.1f}"],
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
            f"Overlap-Beispiel B07: brutto −{b07_gross:.0f} → −{b07_net:.1f} Gt\n(Doppelzählung bereits entfernt)",
            transform=ax.transAxes, fontsize=8.5, color="#333333", va="top",
            bbox=dict(boxstyle="round,pad=0.4", fc="#f7f7f7", ec="#cccccc"))

    fig.text(0.5, 0.015,
             "Quelle: co2_master.yaml (Brutto) · Bilanz-Studie v1.5 monte_carlo.py (Netto). "
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
