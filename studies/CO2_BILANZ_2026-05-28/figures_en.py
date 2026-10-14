#!/usr/bin/env python3
"""
PROVOLUTION CO2 BUDGET · ENGLISH FIGURE SET (F1-F5)
===================================================

English-labelled publication figures for the Monte-Carlo uncertainty study.
Mirrors the German set (figure_monte_carlo.py + peer_review_figures.py) but with
English captions/labels. Single Source of Truth: monte_carlo.py is imported and
re-run with identical seed=42 (anti-drift). No hard-coded figures.

Output: EN/Figure{1..5}_*.png (+ .svg), EN/percentiles_en.csv,
        EN/variance_contributions_en.csv
"""

import io
import os
import csv
import sys
import contextlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

_HERE = os.path.dirname(os.path.abspath(__file__))
_OUT = os.path.join(_HERE, "EN")
os.makedirs(_OUT, exist_ok=True)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


class _QuietBuf(io.StringIO):
    def reconfigure(self, *args, **kwargs):
        return None


with contextlib.redirect_stdout(_QuietBuf()):
    import monte_carlo as mc

GLOBAL_EMISSIONS = getattr(mc, "GLOBAL_EMISSIONS", 55.0)
NET_ZERO = -GLOBAL_EMISSIONS
CLIMATE_POS = -0.60 * GLOBAL_EMISSIONS

# ── reproduce distributions + components ──────────────────────────────────────
np.random.seed(42)
SIM = {}
for name, p in mc.szenarios.items():
    SIM[name] = mc.simulate_szenario(
        p["impl"], p["rebound"], p["s2"], p["s3"], p["engpaesse"], p["klima"]
    )

ORDER = [
    "S · Stresstest 50%-Umsetzung (PF-E7-Adressierung)",
    "A · konservativ-realistisch",
    "B · mittel-realistisch (Erwartungswert)",
    "C · optimistisch-realistisch",
]
SHORT = {
    ORDER[0]: "S · stress test 50%",
    ORDER[1]: "A · conservative",
    ORDER[2]: "B · expected value",
    ORDER[3]: "C · optimistic",
}
SHORT_ML = {  # multiline for x-tick labels
    ORDER[0]: "S\nstress test\n50% deployment",
    ORDER[1]: "A\nconservative-\nrealistic",
    ORDER[2]: "B\nexpected value\n(mid-realistic)",
    ORDER[3]: "C\noptimistic-\nrealistic",
}
SCEN_COLOR = {
    ORDER[0]: "#999999", ORDER[1]: "#0072B2",
    ORDER[2]: "#009E73", ORDER[3]: "#D55E00",
}

COMPONENTS = ["s1", "s2", "s3", "rebound", "engpaesse", "klima"]
COMP_SHORT = {
    "s1": "L1 direct", "s2": "L2 cascades", "s3": "L3 follow-on",
    "rebound": "Rebound", "engpaesse": "Bottlenecks", "klima": "Climate",
}
COMP_COLOR = {
    "s1": "#0072B2", "s2": "#56B4E9", "s3": "#009E73",
    "rebound": "#E69F00", "engpaesse": "#D55E00", "klima": "#CC79A7",
}

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.labelsize": 11, "axes.titlesize": 12, "figure.dpi": 300,
})
SRC_NOTE = ("Source: monte_carlo.py · co2_master.yaml v1.7 + balance study §6 "
            "· n=10,000 · seed=42")


def _src_footer(fig):
    fig.text(0.005, 0.004, SRC_NOTE, fontsize=7, color="#666666",
             ha="left", va="bottom")


def _save(fig, stem):
    png = os.path.join(_OUT, f"{stem}.png")
    svg = os.path.join(_OUT, f"{stem}.svg")
    fig.savefig(png, dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(svg, format="svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"[OK] {png}")
    print(f"[OK] {svg}")


# ── CSV tables (English headers) ──────────────────────────────────────────────
def write_csvs():
    p1 = os.path.join(_OUT, "percentiles_en.csv")
    with open(p1, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["scenario", "mean", "std", "p5", "p25", "p50_median",
                    "p75", "p95", "pct_baseline", "status"])
        for name in ORDER:
            netto = SIM[name]["netto"]
            p5, p25, p50, p75, p95 = np.percentile(netto, [5, 25, 50, 75, 95])
            anteil = -p50 / GLOBAL_EMISSIONS * 100
            status = ("net-zero reached" if anteil >= 95
                      else "climate-positive path" if anteil >= 60
                      else "partial reduction")
            w.writerow([SHORT[name], f"{np.mean(netto):.2f}", f"{np.std(netto):.2f}",
                        f"{p5:.2f}", f"{p25:.2f}", f"{p50:.2f}", f"{p75:.2f}",
                        f"{p95:.2f}", f"{anteil:.1f}", status])
    print(f"[OK] {p1}")

    p2 = os.path.join(_OUT, "variance_contributions_en.csv")
    with open(p2, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["scenario"] + [COMP_SHORT[c] for c in COMPONENTS] + ["sum_check"])
        for name in ORDER:
            netto = SIM[name]["netto"]
            var_net = np.var(netto)
            fracs = [np.cov(SIM[name][c], netto)[0, 1] / var_net for c in COMPONENTS]
            w.writerow([SHORT[name]] + [f"{x*100:.1f}" for x in fracs]
                       + [f"{sum(fracs)*100:.1f}"])
    print(f"[OK] {p2}")


# ── F1 violin ─────────────────────────────────────────────────────────────────
def figure1():
    data = [SIM[n]["netto"] for n in ORDER]
    pos = np.arange(1, len(ORDER) + 1)
    fig, ax = plt.subplots(figsize=(11, 7))
    parts = ax.violinplot(data, positions=pos, widths=0.8,
                          showmeans=False, showmedians=False, showextrema=False)
    for body, name in zip(parts["bodies"], ORDER):
        body.set_facecolor(SCEN_COLOR[name]); body.set_edgecolor("black")
        body.set_alpha(0.35); body.set_linewidth(1.0)
    for p, name in zip(pos, ORDER):
        netto = SIM[name]["netto"]
        p5, p25, p50, p75, p95 = np.percentile(netto, [5, 25, 50, 75, 95])
        col = SCEN_COLOR[name]
        ax.plot([p, p], [p5, p95], color="black", lw=1.5, zorder=3)
        ax.plot([p - 0.05, p + 0.05], [p5, p5], color="black", lw=1.5, zorder=3)
        ax.plot([p - 0.05, p + 0.05], [p95, p95], color="black", lw=1.5, zorder=3)
        ax.plot([p, p], [p25, p75], color=col, lw=9, solid_capstyle="round",
                zorder=4, alpha=0.9)
        ax.plot(p, p50, "o", color="white", markeredgecolor="black",
                markersize=9, markeredgewidth=1.5, zorder=5)
        anteil = -p50 / GLOBAL_EMISSIONS * 100
        ax.annotate(f"{p50:+.1f} Gt\n({anteil:.0f}% baseline)",
                    xy=(p, p50), xytext=(p + 0.34, p50), va="center", ha="left",
                    fontsize=9.5, fontweight="bold", color=col)
    ax.axhline(0, color="black", lw=1.0, alpha=0.6)
    ax.axhline(NET_ZERO, color="#E31A1C", lw=1.8, ls="--", zorder=2)
    ax.annotate(f"Net-zero (IPCC AR6 baseline: {GLOBAL_EMISSIONS:.0f} Gt CO₂eq/yr)",
                xy=(0.62, NET_ZERO), xytext=(0.62, NET_ZERO - 2.5),
                fontsize=9, color="#E31A1C", fontweight="bold", ha="left", va="top")
    ax.set_xticks(pos)
    ax.set_xticklabels([SHORT_ML[n] for n in ORDER], fontsize=10)
    ax.set_ylabel("Net CO₂ budget (Gt CO₂eq/yr)\n← more reduction", fontweight="bold")
    ax.set_xlabel("Scenario", fontweight="bold")
    ax.set_xlim(0.4, len(ORDER) + 0.9)
    ax.set_title("Provolution CO₂ budget — Monte-Carlo uncertainty "
                 "(n=10,000, seed=42)", fontweight="bold", pad=16)
    legend_elements = [
        Patch(facecolor="#cccccc", edgecolor="black", alpha=0.5, label="distribution (violin)"),
        plt.Line2D([0], [0], color="#444", lw=9, alpha=0.9, label="50% IQR (p25–p75)"),
        plt.Line2D([0], [0], color="black", lw=1.5, label="90% CI (p5–p95)"),
        plt.Line2D([0], [0], marker="o", color="white", markeredgecolor="black",
                   markersize=9, lw=0, label="median"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=9,
              frameon=True, framealpha=0.95, edgecolor="black")
    fig.tight_layout()
    _src_footer(fig)
    _save(fig, "Figure1_Scenarios")


# ── F2 sensitivity ────────────────────────────────────────────────────────────
def figure2():
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), sharex=True)
    axes = axes.ravel()
    for ax, name in zip(axes, ORDER):
        netto = SIM[name]["netto"]; var_net = np.var(netto)
        fracs = {c: np.cov(SIM[name][c], netto)[0, 1] / var_net for c in COMPONENTS}
        order_c = sorted(COMPONENTS, key=lambda c: fracs[c])
        vals = [fracs[c] * 100 for c in order_c]
        ax.barh(np.arange(len(order_c)), vals,
                color=[COMP_COLOR[c] for c in order_c],
                edgecolor="black", linewidth=1.0)
        for yi, v in enumerate(vals):
            ax.text(v + (0.6 if v >= 0 else -0.6), yi, f"{v:.1f}%",
                    va="center", ha="left" if v >= 0 else "right",
                    fontsize=8.5, fontweight="bold")
        ax.set_yticks(np.arange(len(order_c)))
        ax.set_yticklabels([COMP_SHORT[c] for c in order_c], fontsize=9)
        ax.axvline(0, color="black", lw=0.8)
        ax.set_title(SHORT[name], fontweight="bold", color=SCEN_COLOR[name], fontsize=11)
        ax.grid(axis="y", visible=False)
    for ax in axes[2:]:
        ax.set_xlabel("Contribution to total variance of the net budget (%)",
                      fontweight="bold")
    fig.suptitle("F2 · Sensitivity analysis — which assumptions drive the uncertainty?",
                 fontweight="bold", fontsize=14, y=0.98)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    _src_footer(fig)
    _save(fig, "Figure2_Sensitivity")


# ── F3 waterfall ──────────────────────────────────────────────────────────────
def figure3():
    fig, axes = plt.subplots(2, 2, figsize=(13, 9), sharey=True)
    axes = axes.ravel()
    lows = []
    seq = ["s1", "s2", "s3", "rebound", "engpaesse", "klima"]
    for ax, name in zip(axes, ORDER):
        means = {c: np.mean(SIM[name][c]) for c in COMPONENTS}
        running = 0.0
        for i, c in enumerate(seq):
            val = means[c]
            ax.bar(i, val, bottom=running, color=COMP_COLOR[c],
                   edgecolor="black", linewidth=1.0, width=0.7)
            ax.plot([i - 0.35, i + 0.35], [running + val, running + val],
                    color="black", lw=0.7, alpha=0.5)
            if i < len(seq) - 1:
                ax.plot([i + 0.35, i + 0.65], [running + val, running + val],
                        color="grey", lw=0.7, ls="--", alpha=0.6)
            running += val
            lows.append(running)
        ax.bar(len(seq), running, color="black", edgecolor="black",
               linewidth=1.0, width=0.7, alpha=0.85)
        ax.text(len(seq), running - 1.5, f"{running:+.1f}",
                ha="center", va="top", fontsize=9, fontweight="bold")
        ax.axhline(0, color="black", lw=0.8)
        ax.axhline(NET_ZERO, color="#E31A1C", lw=1.2, ls="--", alpha=0.8)
        ax.set_xticks(range(len(seq) + 1))
        ax.set_xticklabels([COMP_SHORT[c] for c in seq] + ["Net"],
                           rotation=40, ha="right", fontsize=8)
        ax.set_title(SHORT[name], fontweight="bold", color=SCEN_COLOR[name], fontsize=11)
    # gemeinsame y-Achse explizit: tiefster Zwischenstand aller Panels (vorher schnitt Panel C ab)
    axes[0].set_ylim(min(lows) * 1.08, 2)
    for ax in axes[::2]:
        ax.set_ylabel("Gt CO₂eq/yr", fontweight="bold")
    axes[0].text(0.02, NET_ZERO, "Net-zero", color="#E31A1C", fontsize=8,
                 va="bottom", ha="left", fontweight="bold")
    fig.suptitle("F3 · Layer attribution of the net CO₂ budget (per-layer means)",
                 fontweight="bold", fontsize=14, y=0.98)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    _src_footer(fig)
    _save(fig, "Figure3_Waterfall")


# ── F4 exceedance ─────────────────────────────────────────────────────────────
def figure4():
    fig, ax = plt.subplots(figsize=(11, 7))
    rows = []
    for name in ORDER:
        netto = np.sort(SIM[name]["netto"])
        cdf = np.arange(1, len(netto) + 1) / len(netto)
        ax.plot(netto, cdf, color=SCEN_COLOR[name], lw=2.2, label=SHORT[name])
        pz = np.mean(SIM[name]["netto"] <= NET_ZERO) * 100
        pc = np.mean(SIM[name]["netto"] <= CLIMATE_POS) * 100
        rows.append((SHORT[name], pc, pz))
    ax.axvline(NET_ZERO, color="#E31A1C", lw=1.6, ls="--")
    ax.axvline(CLIMATE_POS, color="#0072B2", lw=1.6, ls=":")
    ax.text(NET_ZERO, 1.01, "net-zero\n(−55 Gt)", color="#E31A1C",
            ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax.text(CLIMATE_POS, 1.01, "climate-positive\n(−33 Gt)", color="#0072B2",
            ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    tbl = "P(target reached)     clim-pos.   net-zero\n" + "─" * 44 + "\n"
    for sname, pc, pz in rows:
        tbl += f"{sname:<20} {pc:>7.1f}%   {pz:>7.1f}%\n"
    ax.text(0.015, 0.97, tbl, transform=ax.transAxes, va="top", ha="left",
            fontsize=8.5, family="monospace",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="black", alpha=0.92))
    ax.set_xlabel("Net CO₂ budget (Gt CO₂eq/yr) — left = more reduction", fontweight="bold")
    ax.set_ylabel("Cumulative probability  P(X ≤ x)", fontweight="bold")
    ax.set_ylim(0, 1.0)
    ax.legend(loc="lower right", fontsize=9, frameon=True, framealpha=0.95, edgecolor="black")
    ax.set_title("F4 · Exceedance curves — probability of reaching the target",
                 fontweight="bold", fontsize=14, pad=22)
    fig.tight_layout()
    _src_footer(fig)
    _save(fig, "Figure4_Exceedance")


# ── F5 convergence ────────────────────────────────────────────────────────────
def figure5():
    fig, axes = plt.subplots(2, 2, figsize=(12, 8.5), sharex=True)
    axes = axes.ravel()
    n_total = len(next(iter(SIM.values()))["netto"])
    steps = np.unique(np.logspace(np.log10(50), np.log10(n_total), 60).astype(int))
    for ax, name in zip(axes, ORDER):
        netto = SIM[name]["netto"]
        med = [np.median(netto[:k]) for k in steps]
        lo = [np.percentile(netto[:k], 5) for k in steps]
        hi = [np.percentile(netto[:k], 95) for k in steps]
        col = SCEN_COLOR[name]
        ax.fill_between(steps, lo, hi, color=col, alpha=0.18, label="90% CI")
        ax.plot(steps, med, color=col, lw=2.0, label="running median")
        fm = np.median(netto)
        ax.axhline(fm, color="black", lw=0.9, ls="--", alpha=0.7)
        ax.text(n_total, fm, f" {fm:+.1f}", va="center", ha="left",
                fontsize=8.5, fontweight="bold")
        ax.set_xscale("log")
        ax.set_title(SHORT[name], fontweight="bold", color=col, fontsize=11)
        ax.set_xlim(50, n_total * 1.25)
    for ax in axes[2:]:
        ax.set_xlabel("iterations (log)", fontweight="bold")
    for ax in axes[::2]:
        ax.set_ylabel("Gt CO₂eq/yr", fontweight="bold")
    axes[0].legend(loc="upper right", fontsize=8.5, frameon=True, framealpha=0.95)
    fig.suptitle("F5 · Convergence diagnostic — stability of median & 90% CI",
                 fontweight="bold", fontsize=14, y=0.98)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    _src_footer(fig)
    _save(fig, "Figure5_Convergence")


if __name__ == "__main__":
    print("=" * 70)
    print("PROVOLUTION · ENGLISH FIGURE SET (F1–F5 + tables)")
    print("=" * 70)
    write_csvs()
    figure1()
    figure2()
    figure3()
    figure4()
    figure5()
    print("=" * 70)
    print("[OK] English package complete -> EN/")
