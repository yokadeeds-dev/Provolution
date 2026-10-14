#!/usr/bin/env python3
"""
PROVOLUTION CO2-BILANZ · MONTE-CARLO-FIGUR
==========================================

Publikationsreife Visualisierung der 4 Szenarien (A/B/C/S) aus der
Monte-Carlo-Simulation. Single Source of Truth: monte_carlo.py wird
importiert und mit identischem seed=42 re-ausgefuehrt, damit die Figur
nicht von den Kennzahlen driftet (Anti-Drift-Konvention).

Darstellung pro Szenario:
  - Violin (volle Netto-Verteilung, n=10000)
  - Median-Punkt
  - 50%-IQR-Box (p25-p75)
  - 90%-KI-Whisker (p5-p95)
Referenzlinien: IPCC-AR6-Baseline (55 Gt) und Net-Zero.

Ausgabe: Figure_MonteCarlo_CO2.png (300 dpi) + .svg
"""

import io
import os
import sys
import contextlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ── Simulationslogik aus monte_carlo.py importieren (Single Source of Truth) ──
# Der Modul-Import fuehrt das Skript aus und druckt den Report; stdout schlucken.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

class _QuietBuf(io.StringIO):
    # monte_carlo.py ruft sys.stdout.reconfigure(); StringIO kennt das nicht.
    def reconfigure(self, *args, **kwargs):
        return None

with contextlib.redirect_stdout(_QuietBuf()):
    import monte_carlo as mc

# ── Verteilungen reproduzierbar re-erzeugen (gleicher seed, gleiche Reihenfolge) ──
np.random.seed(42)
distributions = {}
for name, p in mc.szenarios.items():
    r = mc.simulate_szenario(
        p["impl"], p["rebound"], p["s2"], p["s3"], p["engpaesse"], p["klima"]
    )
    distributions[name] = r["netto"]

GLOBAL_EMISSIONS = mc.GLOBAL_EMISSIONS if hasattr(mc, "GLOBAL_EMISSIONS") else 55.0

# ── Plot-Styling (publikationsreif, colorblind-freundlich) ────────────────────
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "figure.dpi": 300,
})

# Szenario-Reihenfolge S < A < B < C (von schwach nach stark) fuer monotone Optik
order = [
    "S · Stresstest 50%-Umsetzung (PF-E7-Adressierung)",
    "A · konservativ-realistisch",
    "B · mittel-realistisch (Erwartungswert)",
    "C · optimistisch-realistisch",
]
short_labels = {
    order[0]: "S\nStresstest\n50%-Umsetzung",
    order[1]: "A\nkonservativ-\nrealistisch",
    order[2]: "B\nmittel-realistisch\n(Erwartungswert)",
    order[3]: "C\noptimistisch-\nrealistisch",
}
# Okabe-Ito (colorblind-safe)
scenario_color = {
    order[0]: "#999999",  # grau
    order[1]: "#0072B2",  # blau
    order[2]: "#009E73",  # gruen
    order[3]: "#D55E00",  # orange-rot
}

data = [distributions[n] for n in order]
positions = np.arange(1, len(order) + 1)

fig, ax = plt.subplots(figsize=(11, 7))

# Violin
parts = ax.violinplot(
    data, positions=positions, widths=0.8,
    showmeans=False, showmedians=False, showextrema=False,
)
for body, name in zip(parts["bodies"], order):
    body.set_facecolor(scenario_color[name])
    body.set_edgecolor("black")
    body.set_alpha(0.35)
    body.set_linewidth(1.0)

# Pro Szenario: 90%-KI-Whisker, 50%-IQR-Box, Median-Punkt
for pos, name in zip(positions, order):
    netto = distributions[name]
    p5, p25, p50, p75, p95 = np.percentile(netto, [5, 25, 50, 75, 95])
    col = scenario_color[name]

    # 90%-KI als duenner Whisker
    ax.plot([pos, pos], [p5, p95], color="black", lw=1.5, zorder=3)
    ax.plot([pos - 0.05, pos + 0.05], [p5, p5], color="black", lw=1.5, zorder=3)
    ax.plot([pos - 0.05, pos + 0.05], [p95, p95], color="black", lw=1.5, zorder=3)
    # 50%-IQR als dicker Balken
    ax.plot([pos, pos], [p25, p75], color=col, lw=9, solid_capstyle="round",
            zorder=4, alpha=0.9)
    # Median-Punkt
    ax.plot(pos, p50, "o", color="white", markeredgecolor="black",
            markersize=9, markeredgewidth=1.5, zorder=5)

    # Median-Label + %-Baseline
    anteil = -p50 / GLOBAL_EMISSIONS * 100
    ax.annotate(
        f"{p50:+.1f} Gt\n({anteil:.0f}% Baseline)",
        xy=(pos, p50), xytext=(pos + 0.34, p50),
        va="center", ha="left", fontsize=9.5, fontweight="bold",
        color=col,
    )

# Referenzlinien
ax.axhline(0, color="black", lw=1.0, ls="-", alpha=0.6)
ax.axhline(-GLOBAL_EMISSIONS, color="#E31A1C", lw=1.8, ls="--", zorder=2)
ax.annotate(
    f"Net-Zero (IPCC AR6 Baseline: {GLOBAL_EMISSIONS:.0f} Gt CO₂eq/yr)",
    xy=(0.62, -GLOBAL_EMISSIONS), xytext=(0.62, -GLOBAL_EMISSIONS - 2.5),
    fontsize=9, color="#E31A1C", fontweight="bold", ha="left", va="top",
)

# Achsen
ax.set_xticks(positions)
ax.set_xticklabels([short_labels[n] for n in order], fontsize=10)
ax.set_ylabel("Netto-CO₂-Bilanz (Gt CO₂eq/yr)\n← mehr Reduktion", fontweight="bold")
ax.set_xlabel("Szenario", fontweight="bold")
ax.set_xlim(0.4, len(order) + 0.9)
ax.set_title(
    "Provolution CO₂-Bilanz — Monte-Carlo-Unsicherheit (n=10 000, seed=42)",
    fontweight="bold", pad=16,
)

# Legende (Glyph-Erklaerung)
legend_elements = [
    Patch(facecolor="#cccccc", edgecolor="black", alpha=0.5, label="Verteilung (Violin)"),
    plt.Line2D([0], [0], color="#444", lw=9, alpha=0.9, label="50% IQR (p25–p75)"),
    plt.Line2D([0], [0], color="black", lw=1.5, label="90% KI (p5–p95)"),
    plt.Line2D([0], [0], marker="o", color="white", markeredgecolor="black",
               markersize=9, lw=0, label="Median"),
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=9, frameon=True,
          framealpha=0.95, edgecolor="black")

ax.text(
    0.01, 0.01,
    "Quelle: monte_carlo.py · co2_master.yaml v1.7 + Bilanz-Studie §6",
    transform=ax.transAxes, fontsize=7.5, color="#666666", ha="left", va="bottom",
)

fig.tight_layout()

out_png = os.path.join(_HERE, "Figure_MonteCarlo_CO2.png")
out_svg = os.path.join(_HERE, "Figure_MonteCarlo_CO2.svg")
fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"[OK] gespeichert: {out_png}")
print(f"[OK] gespeichert: {out_svg}")
