"""
SEC-J Independent Test · Auswertung (vorab festgelegt, PROTOCOL.md §6)
=====================================================================

Liest ratings/*.csv (eine Datei pro Bewerter:in, Format score_sheet_template.csv) und
author_scores.csv. Erst nach Abschluss aller Bewertungen ausführen.

Kennzahlen je Achse (S, E, C, J) und für den Gesamtwert SEC-J (STANDARD-Formel):
  - Krippendorff-α (Intervallskala) über alle Bewerter:innen       → Reliabilität
  - ICC(2,1) und ICC(2,k), absolute Übereinstimmung                 → Reliabilität
  - MAE und Anteil |Δ| ≤ 0,10 zwischen Bewerter-Mittel und Autoren  → Reproduktion
  - Spearman-ρ Bewerter-Mittel ↔ Autoren                            → Rangfolge
  - Übereinstimmung der J-Warnschwelle (J < 0,80) und des J-Vetos (J < 0,50)
  - Streuung der Autoren-Werte (Hinweis auf eingeschränkte Spannweite)
Selbsttest mit synthetischen Daten: python analyze.py --selftest
"""

import csv
import glob
import os
import sys

import numpy as np

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
AXES = ["S", "E", "C", "J"]
W = {"S": 0.30, "E": 0.25, "C": 0.30, "J": 0.15}


def krippendorff_alpha_interval(m):
    """m: Bewerter × Fälle, np.nan = fehlend. Intervall-Metrik."""
    m = np.asarray(m, dtype=float)
    vals, d_o_num, n_pairable = [], 0.0, 0
    for col in m.T:
        v = col[~np.isnan(col)]
        if len(v) < 2:
            continue
        vals.append(v)
        diffs = (v[:, None] - v[None, :]) ** 2
        d_o_num += diffs.sum() / (len(v) - 1)
        n_pairable += len(v)
    if n_pairable < 2:
        return np.nan
    allv = np.concatenate(vals)
    d_e = ((allv[:, None] - allv[None, :]) ** 2).sum() / (n_pairable * (n_pairable - 1))
    d_o = d_o_num / n_pairable
    return np.nan if d_e == 0 else 1 - d_o / d_e


def icc2(m):
    """ICC(2,1) und ICC(2,k) nach Shrout & Fleiss; m: Fälle × Bewerter, vollständig."""
    m = np.asarray(m, dtype=float)
    n, k = m.shape
    grand = m.mean()
    msr = k * ((m.mean(1) - grand) ** 2).sum() / (n - 1)
    msc = n * ((m.mean(0) - grand) ** 2).sum() / (k - 1)
    sse = ((m - m.mean(1, keepdims=True) - m.mean(0, keepdims=True) + grand) ** 2).sum()
    mse = sse / ((n - 1) * (k - 1))
    icc1 = (msr - mse) / (msr + (k - 1) * mse + k * (msc - mse) / n)
    icck = (msr - mse) / (msr + (msc - mse) / n)
    return icc1, icck


def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])


def cohen_kappa(x, y):
    x, y = np.asarray(x, bool), np.asarray(y, bool)
    po = np.mean(x == y)
    pe = np.mean(x) * np.mean(y) + np.mean(~x) * np.mean(~y)
    return np.nan if pe == 1 else (po - pe) / (1 - pe)


def secj(s, e, c, j):
    return W["S"] * s + W["E"] * e + W["C"] * c + W["J"] * j


def evaluate(ratings, author, verbose=True):
    """ratings: {rater: {code: {axis: wert}}}, author: {code: {axis: wert}}"""
    codes = sorted(author)
    raters = sorted(ratings)
    res = {}
    for ax in AXES + ["SECJ"]:
        if ax == "SECJ":
            m = np.array([[secj(*(ratings[r][c][a] for a in AXES)) for c in codes] for r in raters])
            auth = np.array([secj(*(author[c][a] for a in AXES)) for c in codes])
        else:
            m = np.array([[ratings[r][c][ax] for c in codes] for r in raters])
            auth = np.array([author[c][ax] for c in codes])
        mean_r = m.mean(0)
        i1, ik = icc2(m.T)
        res[ax] = {
            "alpha": krippendorff_alpha_interval(m), "icc21": i1, "icc2k": ik,
            "mae": float(np.mean(np.abs(mean_r - auth))),
            "within_010": float(np.mean(np.abs(mean_r - auth) <= 0.10 + 1e-9)),
            "spearman": spearman(mean_r, auth), "sd_author": float(np.std(auth, ddof=1)),
            "rater_sd": float(np.mean(np.std(m, axis=0, ddof=1))),  # mittlere Streuung zwischen Bewerter:innen je Fall
        }
    # Bootstrap über Fälle (2000 Ziehungen, seed 42): 90 %-KI für α und MAE von SEC-J
    m = np.array([[secj(*(ratings[r][c][a] for a in AXES)) for c in codes] for r in raters])
    auth = np.array([secj(*(author[c][a] for a in AXES)) for c in codes])
    rng = np.random.default_rng(42)
    boots_a, boots_m = [], []
    for _ in range(2000):
        idx = rng.integers(0, len(codes), len(codes))
        boots_a.append(krippendorff_alpha_interval(m[:, idx]))
        boots_m.append(float(np.mean(np.abs(m[:, idx].mean(0) - auth[idx]))))
    res["SECJ"]["alpha_ci90"] = tuple(np.nanpercentile(boots_a, [5, 95]))
    res["SECJ"]["mae_ci90"] = tuple(np.percentile(boots_m, [5, 95]))
    jm = np.array([[ratings[r][c]["J"] for c in codes] for r in raters]).mean(0)
    ja = np.array([author[c]["J"] for c in codes])
    res["J_warn_kappa"] = cohen_kappa(jm < 0.80, ja < 0.80)
    res["J_veto_rater"] = int(np.sum(jm < 0.50))
    res["J_veto_author"] = int(np.sum(ja < 0.50))
    if verbose:
        print(f"Bewerter:innen: {len(raters)} · Fälle: {len(codes)}")
        print(f"{'Achse':<6}{'α':>7}{'ICC21':>8}{'ICC2k':>8}{'MAE':>7}{'≤0,10':>8}{'ρ':>7}{'SD Aut.':>9}")
        for ax in AXES + ["SECJ"]:
            r = res[ax]
            print(f"{ax:<6}{r['alpha']:7.2f}{r['icc21']:8.2f}{r['icc2k']:8.2f}{r['mae']:7.3f}"
                  f"{100 * r['within_010']:7.0f}%{r['spearman']:7.2f}{r['sd_author']:9.3f}")
        s = res["SECJ"]
        print(f"SEC-J 90 %-KI (Bootstrap über Fälle): α {s['alpha_ci90'][0]:.2f} … {s['alpha_ci90'][1]:.2f} · "
              f"MAE {s['mae_ci90'][0]:.3f} … {s['mae_ci90'][1]:.3f}")
        print(f"J-Warnschwelle (<0,80) κ Bewerter↔Autoren: {res['J_warn_kappa']:.2f} · "
              f"J-Veto Bewerter {res['J_veto_rater']} / Autoren {res['J_veto_author']}")
        print(verdict(res))
    return res


MIN_SD_FOR_ALPHA = 0.10  # unterhalb dieser Streuung der Autoren-SEC-J ist α nicht interpretierbar (PROTOCOL.md §7)


def verdict(res):
    """Vorab festgelegte Entscheidungsregel (PROTOCOL.md §7).

    Reliabilität: Krippendorff-α nur, wenn die Fälle genug streuen (SD Autoren-SEC-J ≥ 0,10).
    Sonst (eingeschränkte Spannweite) zählt die absolute Streuung zwischen den Bewerter:innen
    (mittlere SD je Fall). Reproduktion: MAE Bewerter-Mittel ↔ Autoren.
    """
    s = res["SECJ"]
    mae = s["mae"]
    if s["sd_author"] >= MIN_SD_FOR_ALPHA:
        a = s["alpha"]
        rel = "zuverlässig" if a >= 0.80 else "vorläufig zuverlässig" if a >= 0.667 else "NICHT zuverlässig"
        rel_txt = f"{rel} (α = {a:.2f})"
    else:
        # ungünstigste Achse entscheidet (das Komposit mittelt Uneinigkeit weg)
        sd = max(res[ax]["rater_sd"] for ax in AXES)
        rel = "zuverlässig" if sd <= 0.10 else "vorläufig zuverlässig" if sd <= 0.20 else "NICHT zuverlässig"
        rel_txt = (f"{rel} (größte Streuung zwischen Bewerter:innen auf einer Achse {sd:.3f}; α = {s['alpha']:.2f} "
                   f"nicht interpretierbar, Autoren-SD {s['sd_author']:.3f} < {MIN_SD_FOR_ALPHA})")
    # Achsen-Bedingung: das Komposit mittelt Fehler weg, deshalb muss jede Achse einzeln passen
    ax_mae = {ax: res[ax]["mae"] for ax in AXES}
    ax_sd = {ax: res[ax]["rater_sd"] for ax in AXES}
    worst_mae, worst_sd = max(ax_mae.values()), max(ax_sd.values())
    if mae <= 0.10 and worst_mae <= 0.15:
        rep = "reproduziert"
    elif mae <= 0.20 and worst_mae <= 0.25:
        rep = "teilweise reproduziert"
    else:
        rep = "NICHT reproduziert"
    if s["sd_author"] >= MIN_SD_FOR_ALPHA and worst_sd > 0.20 and rel != "NICHT zuverlässig":
        rel_txt += f"; Achsen-Streuung bis {worst_sd:.2f} → NICHT zuverlässig"
        rel_txt = "NICHT zuverlässig" + rel_txt[len(rel):]
    axes_txt = ", ".join(f"{ax} {ax_mae[ax]:.2f}" for ax in AXES)
    return (f"Ergebnis (vorab festgelegte Regel): Bewertung {rel_txt}; Autoren-Scores {rep} "
            f"(MAE SEC-J = {mae:.3f}; je Achse {axes_txt}).")


def load():
    author = {}
    with open(os.path.join(HERE, "author_scores.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            author[r["code"]] = {a: float(r[a.lower()]) for a in AXES}
    ratings = {}
    for path in sorted(glob.glob(os.path.join(HERE, "ratings", "*.csv"))):
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["code"] not in author or r.get("runde", "1") != "1":
                    continue
                ratings.setdefault(r["rater_id"], {})[r["code"]] = {a: float(r[a].replace(",", ".")) for a in AXES}
    return ratings, author


def selftest():
    """Synthetische Bewerter:innen = Autoren-Wert + Rauschen. Prüft, dass die Kennzahlen
    bei kleinem Rauschen hoch und bei großem Rauschen niedrig ausfallen."""
    rng = np.random.default_rng(42)
    codes = [f"F{i:02d}" for i in range(1, 13)]
    author = {c: {a: float(rng.uniform(0.3, 1.0)) for a in AXES} for c in codes}
    out = {}
    for noise in (0.02, 0.30):
        ratings = {f"R{k}": {c: {a: float(np.clip(author[c][a] + rng.normal(0, noise), 0, 1)) for a in AXES}
                             for c in codes} for k in range(1, 6)}
        out[noise] = evaluate(ratings, author, verbose=False)
    lo, hi = out[0.02]["SECJ"], out[0.30]["SECJ"]
    assert lo["alpha"] > 0.9 and lo["mae"] < 0.03, lo
    assert hi["alpha"] < lo["alpha"] and hi["mae"] > lo["mae"], (lo, hi)
    # Krippendorff-α-Referenz: perfekte Übereinstimmung = 1
    assert abs(krippendorff_alpha_interval([[0.2, 0.5, 0.9], [0.2, 0.5, 0.9]]) - 1) < 1e-12
    # Referenzbeispiel Krippendorff (2011) „Computing Krippendorff's Alpha-Reliability“, 4 × 12, Intervall-α = 0,849
    n = np.nan
    ref = [[1, 2, 3, 3, 2, 1, 4, 1, 2, n, n, n], [1, 2, 3, 3, 2, 2, 4, 1, 2, 5, n, 3],
           [n, 3, 3, 3, 2, 3, 4, 2, 2, 5, 1, n], [1, 2, 3, 3, 2, 4, 4, 1, 2, 5, 1, n]]
    assert abs(krippendorff_alpha_interval(ref) - 0.849) < 0.0005, krippendorff_alpha_interval(ref)
    print(f"Selbsttest OK · Rauschen 0,02: α = {lo['alpha']:.2f}, MAE = {lo['mae']:.3f} · "
          f"Rauschen 0,30: α = {hi['alpha']:.2f}, MAE = {hi['mae']:.3f}")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        ratings, author = load()
        if len(ratings) < 3:
            sys.exit(f"Nur {len(ratings)} vollständige Bewertungssätze in ratings/ — mindestens 3 nötig (PROTOCOL.md §4).")
        evaluate(ratings, author)
