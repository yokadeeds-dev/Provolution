"""
Provolution CO2-Bilanz · Monte-Carlo-Simulation
================================================

Aktion: PF-Report v1.0.1 E4-Datenlage-Adressierung
        (Monte-Carlo-Unsicherheits-Propagation auf 3 Szenarien + 50%-Stresstest)

Datum: 2026-05-28
Methodik: 10000 Iterationen, seed=42 für Reproduzierbarkeit
Quelle der Eingangsverteilungen: co2_master.yaml v1.2 + Bilanz-Studie §6
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import numpy as np

np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# EINGANGS-VERTEILUNGEN
# ─────────────────────────────────────────────────────────────────────────────

# Schicht 1: Direkte Hebel-Wirkung (Brutto, nach Domain-K-Integration + D19-Promotion + B09/B10-Drift-Resolution)
# Quelle: co2_master.yaml v1.3 gesamt.reduktion_hart
# v1.3 Änderungen gegenüber v1.2: B09/B10 Drift-Resolution (+1.5 weniger Reduktion);
# D19 Algen-Bioraffinerie Promotion (-0.3 mehr Reduktion); Netto -1.2 weniger Reduktion
S1_BRUTTO_MEAN = -58.6  # Gt CO2eq/yr (v1.3, Domain A-K + Communities inkl. D19)
S1_BRUTTO_UNCERTAINTY = 0.10  # ±10% Methodik-Unsicherheit (YAML validation_approach)

# Schicht 2: Kaskaden (Vermeidung Material-Vorketten, Klimaanlagen etc.)
# Quelle: Bilanz-Studie §3.10 (konservativ / mittel / optimistisch)
S2_KONSERV = -3.2
S2_MITTEL = -6.0
S2_OPTIMIST = -8.0

# Schicht 3: Folgewirkungen (Wald, Mikroklima, Gesundheit, Verhalten)
# Quelle: Bilanz-Studie §4.6
S3_KONSERV = -2.7
S3_MITTEL = -7.6
S3_OPTIMIST = -12.6

# Verluste-Parameter (positiv = entgegen Reduktion)
# Quelle: Bilanz-Studie §5
ENGPAESSE_KONSERV = 3.0
ENGPAESSE_MITTEL = 2.0
ENGPAESSE_OPTIMIST = 1.0

KLIMA_VERSCHL_KONSERV = 2.0
KLIMA_VERSCHL_MITTEL = 1.5
KLIMA_VERSCHL_OPTIMIST = 0.5

# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION
# ─────────────────────────────────────────────────────────────────────────────


def simulate_szenario(impl_mean, rebound_mean, s2_mean, s3_mean,
                      engpaesse_mean, klima_verschl_mean, n=10000):
    """Monte-Carlo-Simulation eines Szenarios.

    Parameter:
        impl_mean: erwartete Umsetzungsrate (0..1)
        rebound_mean: erwartete Rebound-Rate (0..1)
        s2_mean: erwarteter Schicht-2-Wert (Gt, negativ)
        s3_mean: erwarteter Schicht-3-Wert (Gt, negativ)
        engpaesse_mean: erwartete Material-Engpässe (Gt, positiv = Verlust)
        klima_verschl_mean: erwartete klimatische Verschlechterung (Gt, positiv)
        n: Anzahl Iterationen
    """
    # Implementations-Rate: Normalverteilung um Mean, ±5%
    impl = np.clip(np.random.normal(impl_mean, 0.05, n), 0, 1)

    # Schicht 1: Brutto-Reduktion ±10%, skaliert mit impl
    s1 = np.random.normal(S1_BRUTTO_MEAN,
                          abs(S1_BRUTTO_MEAN * S1_BRUTTO_UNCERTAINTY),
                          n) * impl

    # Schicht 2: Bandbreite konservativ-optimistisch, zentriert um s2_mean
    s2 = np.random.normal(s2_mean, abs(s2_mean) * 0.20, n) * impl

    # Schicht 3: ähnlich, aber mit mehr Unsicherheit
    s3 = np.random.normal(s3_mean, abs(s3_mean) * 0.30, n) * impl

    # Rebound: ±3%, Skalierung auf S1+S2
    rebound = np.clip(np.random.normal(rebound_mean, 0.03, n), 0, 0.5)
    verluste_rebound = -(s1 + s2) * rebound  # positiv (Verlust)

    # Material-Engpässe: ±0.5 Gt um mean
    verluste_engpaesse = np.random.normal(engpaesse_mean, 0.5, n)

    # Klimatische Verschlechterung: ±0.3 Gt um mean
    verluste_klima = np.random.normal(klima_verschl_mean, 0.3, n)

    # Netto-Bilanz
    netto = s1 + s2 + s3 + verluste_rebound + verluste_engpaesse + verluste_klima

    return {
        "netto": netto,
        "s1": s1, "s2": s2, "s3": s3,
        "rebound": verluste_rebound,
        "engpaesse": verluste_engpaesse,
        "klima": verluste_klima,
    }


# ─────────────────────────────────────────────────────────────────────────────
# SZENARIEN
# ─────────────────────────────────────────────────────────────────────────────

szenarios = {
    "A · konservativ-realistisch": {
        "impl": 0.70, "rebound": 0.20,
        "s2": S2_KONSERV, "s3": S3_KONSERV,
        "engpaesse": ENGPAESSE_KONSERV, "klima": KLIMA_VERSCHL_KONSERV,
    },
    "B · mittel-realistisch (Erwartungswert)": {
        "impl": 0.75, "rebound": 0.15,
        "s2": S2_MITTEL, "s3": S3_MITTEL,
        "engpaesse": ENGPAESSE_MITTEL, "klima": KLIMA_VERSCHL_MITTEL,
    },
    "C · optimistisch-realistisch": {
        "impl": 0.85, "rebound": 0.08,
        "s2": S2_OPTIMIST, "s3": S3_OPTIMIST,
        "engpaesse": ENGPAESSE_OPTIMIST, "klima": KLIMA_VERSCHL_OPTIMIST,
    },
    "S · Stresstest 50%-Umsetzung (PF-E7-Adressierung)": {
        "impl": 0.50, "rebound": 0.30,
        "s2": S2_KONSERV, "s3": S3_KONSERV,
        "engpaesse": 5.0, "klima": 3.0,
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# AUSFÜHRUNG + AUSGABE
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 78)
print("PROVOLUTION CO2-BILANZ · MONTE-CARLO-SIMULATION")
print("=" * 78)
print(f"N=10000 Iterationen pro Szenario · seed=42")
print(f"Brutto Schicht 1: {S1_BRUTTO_MEAN} ±{abs(S1_BRUTTO_MEAN*S1_BRUTTO_UNCERTAINTY):.1f} Gt CO2eq/yr")
print(f"Quelle: co2_master.yaml v1.3 + Bilanz-Studie §6 (v1.5 update)")
print()

results = {}
for name, params in szenarios.items():
    r = simulate_szenario(
        params["impl"], params["rebound"],
        params["s2"], params["s3"],
        params["engpaesse"], params["klima"],
    )
    netto = r["netto"]
    p5, p25, p50, p75, p95 = np.percentile(netto, [5, 25, 50, 75, 95])
    mean = np.mean(netto)
    std = np.std(netto)

    results[name] = {
        "mean": mean, "std": std,
        "p5": p5, "p25": p25, "p50": p50, "p75": p75, "p95": p95,
    }

    print("─" * 78)
    print(f"{name}")
    print(f"  Parameter: impl={params['impl']:.0%}, rebound={params['rebound']:.0%}, "
          f"engpässe={params['engpaesse']:.1f} Gt, klima={params['klima']:.1f} Gt")
    print(f"  Mittelwert: {mean:+.1f} Gt CO2eq/yr (Standardabweichung ±{std:.1f})")
    print(f"  Median:     {p50:+.1f} Gt CO2eq/yr")
    print(f"  90% KI:     [{p5:+.1f}, {p95:+.1f}] Gt CO2eq/yr")
    print(f"  50% IQR:    [{p25:+.1f}, {p75:+.1f}] Gt CO2eq/yr")
    print()

# ─────────────────────────────────────────────────────────────────────────────
# ZUSAMMENFASSUNG
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 78)
print("ZUSAMMENFASSUNG · ZITIERBARE KERNZAHLEN")
print("=" * 78)
print()
print(f"{'Szenario':<48} {'Median':>10} {'90% KI':>22}")
print("─" * 78)
for name, r in results.items():
    short_name = name.split("·")[0].strip()
    ki = f"[{r['p5']:+.1f}, {r['p95']:+.1f}]"
    print(f"{name:<48} {r['p50']:+10.1f} {ki:>22}")
print()

# Globaler Kontext
GLOBAL_EMISSIONS = 55.0  # Gt CO2eq/yr 2023 baseline
print(f"Globale Baseline (IPCC AR6, 2023): {GLOBAL_EMISSIONS} Gt CO2eq/yr")
print()
print(f"{'Szenario':<48} {'% Baseline':>12}")
print("─" * 78)
for name, r in results.items():
    anteil = -r["p50"] / GLOBAL_EMISSIONS * 100
    status = "Net-Zero erreicht" if anteil >= 95 else "Klima-positiv-Pfad" if anteil >= 60 else "Teil-Reduktion"
    print(f"{name:<48} {anteil:>10.1f}%  ({status})")
print()
print(f"PF-Report E4-Adressierung: Monte-Carlo-Propagation auf 3 Hauptszenarien + Stresstest ✓")
print(f"PF-Report E7-Adressierung: Stresstest 50%-Umsetzung als 4. Szenario ✓")
