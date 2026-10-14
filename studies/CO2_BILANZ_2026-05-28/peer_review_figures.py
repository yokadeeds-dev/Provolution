#!/usr/bin/env python3
"""
PROVOLUTION CO2-BILANZ · PEER-REVIEW-FIGURENPAKET
=================================================

Erzeugt die ergaenzenden Figuren F2-F5 und die maschinenlesbaren
Reproduktions-Tabellen fuer die Monte-Carlo-Unsicherheitsstudie.
F1 (Szenario-Violin) liegt separat in figure_monte_carlo.py.

Single Source of Truth: monte_carlo.py wird importiert und mit
identischem seed=42 re-ausgefuehrt (Anti-Drift). Es werden KEINE
Kennzahlen hartkodiert.

F2  Sensitivitaet   — Varianz-Beitrag jedes Eingangs (2x2)
F3  Schicht-Waterfall — additive Herleitung der Netto-Bilanz (2x2)
F4  Exceedance/CDF  — P(Net-Zero), P(klima-positiv) je Szenario
F5  Konvergenz      — laufender Median + 90% KI vs. Iterationen

Datentabellen:
  percentiles.csv              — p5/p25/p50/p75/p95, Mean, Std je Szenario
  variance_contributions.csv   — fraktionaler Varianz-Beitrag je Input

Methodik Varianz-Zerlegung:
  netto = s1 + s2 + s3 + rebound + engpaesse + klima  (exakte Summe)
  => Var(netto) = sum_i Cov(X_i, netto)
  Anteil_i = Cov(X_i, netto) / Var(netto),  sum_i Anteil_i = 1
  Defensible First-Order-Beitragszerlegung (kein Sobol noetig, da additiv).
"""

import io
import os
import csv
import sys
import contextlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ── monte_carlo.py importieren (Single Source of Truth), Report-Print schlucken ──
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


class _QuietBuf(io.StringIO):
    def reconfigure(self, *args, **kwargs):
        return None


with contextlib.redirect_stdout(_QuietBuf()):
    import monte_carlo as mc

GLOBAL_EMISSIONS = getattr(mc, "GLOBAL_EMISSIONS", 55.0)

# Schwellen (aus monte_carlo.py Status-Logik abgeleitet)
NET_ZERO = -GLOBAL_EMISSIONS                 # 100% Baseline kompensiert
CLIMATE_POS = -0.60 * GLOBAL_EMISSIONS       # >= 60% Baseline = "Klima-positiv-Pfad"

# ── Verteilungen + alle Komponenten reproduzierbar erzeugen ───────────────────
np.random.seed(42)
SIM = {}  # name -> dict mit netto + komponenten-arrays
for name, p in mc.szenarios.items():
    SIM[name] = mc.simulate_szenario(
        p["impl"], p["rebound"], p["s2"], p["s3"], p["engpaesse"], p["klima"]
    )

# Szenario-Reihenfolge schwach -> stark, konsistent ueber alle Figuren
ORDER = [
    "S · Stresstest 50%-Umsetzung (PF-E7-Adressierung)",
    "A · konservativ-realistisch",
    "B · mittel-realistisch (Erwartungswert)",
    "C · optimistisch-realistisch",
]
SHORT = {
    ORDER[0]: "S · Stresstest 50%",
    ORDER[1]: "A · konservativ",
    ORDER[2]: "B · Erwartungswert",
    ORDER[3]: "C · optimistisch",
}
# Okabe-Ito (colorblind-safe), konsistent mit F1
SCEN_COLOR = {
    ORDER[0]: "#999999",
    ORDER[1]: "#0072B2",
    ORDER[2]: "#009E73",
    ORDER[3]: "#D55E00",
}

# Komponenten (Schichten + Verluste), feste Farben + Labels
COMPONENTS = ["s1", "s2", "s3", "rebound", "engpaesse", "klima"]
COMP_LABEL = {
    "s1": "Schicht 1\n(direkte Hebel)",
    "s2": "Schicht 2\n(Kaskaden)",
    "s3": "Schicht 3\n(Folgewirkungen)",
    "rebound": "Rebound\n(Verlust)",
    "engpaesse": "Material-\nEngpässe",
    "klima": "Klima-\nVerschlechterung",
}
COMP_LABEL_SHORT = {
    "s1": "S1 direkt", "s2": "S2 Kaskaden", "s3": "S3 Folge",
    "rebound": "Rebound", "engpaesse": "Engpässe", "klima": "Klima",
}
# Reduktionen gruen-blau, Verluste rot-toene (Okabe-Ito-nah)
COMP_COLOR = {
    "s1": "#0072B2", "s2": "#56B4E9", "s3": "#009E73",
    "rebound": "#E69F00", "engpaesse": "#D55E00", "klima": "#CC79A7",
}

# ── Globales Styling ──────────────────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "figure.dpi": 300,
})

SRC_NOTE = "Quelle: monte_carlo.py · co2_master.yaml v1.3 + Bilanz-Studie §6 (v1.5) · n=10 000 · seed=42"


def _src_footer(fig):
    fig.text(0.005, 0.004, SRC_NOTE, fontsize=7, color="#666666", ha="left", va="bottom")


# ── Percentile-Tabelle (CSV) ──────────────────────────────────────────────────
def write_percentiles_csv():
    path = os.path.join(_HERE, "percentiles.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["scenario", "mean", "std", "p5", "p25",
                    "p50_median", "p75", "p95", "pct_baseline", "status"])
        for name in ORDER:
            netto = SIM[name]["netto"]
            p5, p25, p50, p75, p95 = np.percentile(netto, [5, 25, 50, 75, 95])
            anteil = -p50 / GLOBAL_EMISSIONS * 100
            status = ("Net-Zero erreicht" if anteil >= 95
                      else "Klima-positiv-Pfad" if anteil >= 60
                      else "Teil-Reduktion")
            w.writerow([SHORT[name], f"{np.mean(netto):.2f}", f"{np.std(netto):.2f}",
                        f"{p5:.2f}", f"{p25:.2f}", f"{p50:.2f}", f"{p75:.2f}",
                        f"{p95:.2f}", f"{anteil:.1f}", status])
    print(f"[OK] {path}")


def write_variance_csv():
    path = os.path.join(_HERE, "variance_contributions.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["scenario"] + [COMP_LABEL_SHORT[c] for c in COMPONENTS]
                   + ["sum_check"])
        for name in ORDER:
            netto = SIM[name]["netto"]
            var_net = np.var(netto)
            fracs = []
            for c in COMPONENTS:
                cov = np.cov(SIM[name][c], netto)[0, 1]
                fracs.append(cov / var_net)
            w.writerow([SHORT[name]] + [f"{x*100:.1f}" for x in fracs]
                       + [f"{sum(fracs)*100:.1f}"])
    print(f"[OK] {path}")


# ── F2 Sensitivitaet: Varianz-Beitrag je Input (2x2) ──────────────────────────
def figure2_sensitivity():
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), sharex=True)
    axes = axes.ravel()
    for ax, name in zip(axes, ORDER):
        netto = SIM[name]["netto"]
        var_net = np.var(netto)
        fracs = {c: np.cov(SIM[name][c], netto)[0, 1] / var_net for c in COMPONENTS}
        order_c = sorted(COMPONENTS, key=lambda c: fracs[c])  # klein -> gross
        vals = [fracs[c] * 100 for c in order_c]
        colors = [COMP_COLOR[c] for c in order_c]
        y = np.arange(len(order_c))
        ax.barh(y, vals, color=colors, edgecolor="black", linewidth=1.0)
        for yi, v in zip(y, vals):
            ax.text(v + (0.6 if v >= 0 else -0.6), yi, f"{v:.1f}%",
                    va="center", ha="left" if v >= 0 else "right",
                    fontsize=8.5, fontweight="bold")
        ax.set_yticks(y)
        ax.set_yticklabels([COMP_LABEL_SHORT[c] for c in order_c], fontsize=9)
        ax.axvline(0, color="black", lw=0.8)
        ax.set_title(SHORT[name], fontweight="bold",
                     color=SCEN_COLOR[name], fontsize=11)
        ax.grid(axis="y", visible=False)
    for ax in axes[2:]:
        ax.set_xlabel("Beitrag zur Gesamt-Varianz der Netto-Bilanz (%)",
                      fontweight="bold")
    fig.suptitle("F2 · Sensitivitätsanalyse — welche Annahmen treiben die Unsicherheit?",
                 fontweight="bold", fontsize=14, y=0.98)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    _src_footer(fig)
    _save(fig, "Figure2_Sensitivity")


# ── F3 Schicht-Waterfall: additive Herleitung (2x2) ───────────────────────────
def figure3_waterfall():
    fig, axes = plt.subplots(2, 2, figsize=(13, 9), sharey=True)
    axes = axes.ravel()
    for ax, name in zip(axes, ORDER):
        means = {c: np.mean(SIM[name][c]) for c in COMPONENTS}
        net = np.median(SIM[name]["netto"])
        # additive Reihenfolge: Reduktionen zuerst, dann Verluste
        seq = ["s1", "s2", "s3", "rebound", "engpaesse", "klima"]
        running = 0.0
        for i, c in enumerate(seq):
            val = means[c]
            ax.bar(i, val, bottom=running, color=COMP_COLOR[c],
                   edgecolor="black", linewidth=1.0, width=0.7)
            # Verbindungslinie
            ax.plot([i - 0.35, i + 0.35], [running + val, running + val],
                    color="black", lw=0.7, ls="-", alpha=0.5)
            if i < len(seq) - 1:
                ax.plot([i + 0.35, i + 0.65], [running + val, running + val],
                        color="grey", lw=0.7, ls="--", alpha=0.6)
            running += val
        # Netto-Balken
        ax.bar(len(seq), running, color="black", edgecolor="black",
               linewidth=1.0, width=0.7, alpha=0.85)
        ax.text(len(seq), running - 1.5, f"{running:+.1f}",
                ha="center", va="top", fontsize=9, fontweight="bold")
        ax.axhline(0, color="black", lw=0.8)
        ax.axhline(NET_ZERO, color="#E31A1C", lw=1.2, ls="--", alpha=0.8)
        ax.set_xticks(range(len(seq) + 1))
        ax.set_xticklabels([COMP_LABEL_SHORT[c] for c in seq] + ["Netto"],
                           rotation=40, ha="right", fontsize=8)
        ax.set_title(SHORT[name], fontweight="bold",
                     color=SCEN_COLOR[name], fontsize=11)
    for ax in axes[::2]:
        ax.set_ylabel("Gt CO₂eq/yr", fontweight="bold")
    fig.suptitle("F3 · Schicht-Herleitung der Netto-CO₂-Bilanz (Mittelwerte je Schicht)",
                 fontweight="bold", fontsize=14, y=0.98)
    # gemeinsame Net-Zero-Annotation
    axes[0].text(0.02, NET_ZERO, "Net-Zero", color="#E31A1C", fontsize=8,
                 va="bottom", ha="left", fontweight="bold")
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    _src_footer(fig)
    _save(fig, "Figure3_Waterfall")


# ── F4 Exceedance / CDF mit Wahrscheinlichkeiten ──────────────────────────────
def figure4_exceedance():
    fig, ax = plt.subplots(figsize=(11, 7))
    rows = []
    for name in ORDER:
        netto = np.sort(SIM[name]["netto"])
        cdf = np.arange(1, len(netto) + 1) / len(netto)  # P(X <= x)
        ax.plot(netto, cdf, color=SCEN_COLOR[name], lw=2.2, label=SHORT[name])
        p_netzero = np.mean(SIM[name]["netto"] <= NET_ZERO) * 100
        p_climpos = np.mean(SIM[name]["netto"] <= CLIMATE_POS) * 100
        rows.append((SHORT[name], p_climpos, p_netzero))

    ax.axvline(NET_ZERO, color="#E31A1C", lw=1.6, ls="--")
    ax.axvline(CLIMATE_POS, color="#0072B2", lw=1.6, ls=":")
    ax.text(NET_ZERO, 1.01, "Net-Zero\n(−55 Gt)", color="#E31A1C",
            ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax.text(CLIMATE_POS, 1.01, "Klima-positiv\n(−33 Gt)", color="#0072B2",
            ha="center", va="bottom", fontsize=8.5, fontweight="bold")

    # Wahrscheinlichkeits-Tabelle im Plot
    tbl = "P(Ziel erreicht)        klima-pos.   Net-Zero\n"
    tbl += "─" * 44 + "\n"
    for sname, pc, pz in rows:
        tbl += f"{sname:<20} {pc:>7.1f}%   {pz:>7.1f}%\n"
    ax.text(0.015, 0.97, tbl, transform=ax.transAxes, va="top", ha="left",
            fontsize=8.5, family="monospace",
            bbox=dict(boxstyle="round", facecolor="white",
                      edgecolor="black", alpha=0.92))

    ax.set_xlabel("Netto-CO₂-Bilanz (Gt CO₂eq/yr) — links = mehr Reduktion",
                  fontweight="bold")
    ax.set_ylabel("Kumulierte Wahrscheinlichkeit  P(X ≤ x)", fontweight="bold")
    ax.set_ylim(0, 1.0)
    ax.legend(loc="lower right", fontsize=9, frameon=True, framealpha=0.95,
              edgecolor="black")
    ax.set_title("F4 · Exceedance-Kurven — Wahrscheinlichkeit der Zielerreichung",
                 fontweight="bold", fontsize=14, pad=22)
    fig.tight_layout()
    _src_footer(fig)
    _save(fig, "Figure4_Exceedance")


# ── F5 Konvergenz: laufender Median + 90% KI vs. n ────────────────────────────
def figure5_convergence():
    fig, axes = plt.subplots(2, 2, figsize=(12, 8.5), sharex=True)
    axes = axes.ravel()
    # Stuetzstellen logarithmisch
    n_total = len(next(iter(SIM.values()))["netto"])
    steps = np.unique(np.logspace(np.log10(50), np.log10(n_total), 60).astype(int))
    for ax, name in zip(axes, ORDER):
        netto = SIM[name]["netto"]  # bereits zufaellige Reihenfolge
        med, lo, hi = [], [], []
        for k in steps:
            sub = netto[:k]
            med.append(np.median(sub))
            lo.append(np.percentile(sub, 5))
            hi.append(np.percentile(sub, 95))
        col = SCEN_COLOR[name]
        ax.fill_between(steps, lo, hi, color=col, alpha=0.18, label="90% KI")
        ax.plot(steps, med, color=col, lw=2.0, label="laufender Median")
        final_med = np.median(netto)
        ax.axhline(final_med, color="black", lw=0.9, ls="--", alpha=0.7)
        ax.text(n_total, final_med, f" {final_med:+.1f}", va="center",
                ha="left", fontsize=8.5, fontweight="bold")
        ax.set_xscale("log")
        ax.set_title(SHORT[name], fontweight="bold", color=col, fontsize=11)
        ax.set_xlim(50, n_total * 1.25)
    for ax in axes[2:]:
        ax.set_xlabel("Iterationen (log)", fontweight="bold")
    for ax in axes[::2]:
        ax.set_ylabel("Gt CO₂eq/yr", fontweight="bold")
    axes[0].legend(loc="upper right", fontsize=8.5, frameon=True, framealpha=0.95)
    fig.suptitle("F5 · Konvergenzdiagnose — Stabilität von Median & 90% KI",
                 fontweight="bold", fontsize=14, y=0.98)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    _src_footer(fig)
    _save(fig, "Figure5_Convergence")


# ── Speichern (PNG 300 dpi + SVG) ─────────────────────────────────────────────
def _save(fig, stem):
    png = os.path.join(_HERE, f"{stem}.png")
    svg = os.path.join(_HERE, f"{stem}.svg")
    fig.savefig(png, dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(svg, format="svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"[OK] {png}")
    print(f"[OK] {svg}")


if __name__ == "__main__":
    print("=" * 70)
    print("PROVOLUTION · PEER-REVIEW-FIGURENPAKET (F2–F5 + Tabellen)")
    print("=" * 70)
    write_percentiles_csv()
    write_variance_csv()
    figure2_sensitivity()
    figure3_waterfall()
    figure4_exceedance()
    figure5_convergence()
    print("=" * 70)
    print("[OK] Paket vollständig.")
