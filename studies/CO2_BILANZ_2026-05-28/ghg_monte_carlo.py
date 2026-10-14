"""
Provolution all-GHG-Bilanz · Monte-Carlo (CO₂ + CH₄ + N₂O + F-Gase)
====================================================================

Datum: 2026-10-14 · Entscheidung: canon/decisions/DEC_2026-10-14_ghg_monte_carlo.md
Erweitert monte_carlo.py (CO₂-Schicht, Single Source of Truth) um die Gas-Schicht.

Aufbau je Iteration und Szenario:
  netto_ghg = netto_co2 (aus monte_carlo.py, identische Draws, seed=42)
            + Σ_Quellen (gas_i − overlap_i) × impl_gas
Annahmen (alle in der Decision-Datei begründet):
  - Gasmengen: Dreiecksverteilung je Gas, Grenzen = Unsicherheitsband aus impact_master.yaml,
    Modus = Punktwert (AR6). Domain-Anteile proportional zum Punktwert.
  - Overlap mit der CO₂-Schicht aus overlap_matrix.yaml: belegte Overlaps fest,
    angenommene Overlaps (D18) gleichverteilt zwischen 0 und dem Punktwert.
  - Umsetzungsrate der Gas-Maßnahmen: gleicher Szenario-Mittelwert wie CO₂, ±5 %, eigene Ziehung.
  - Kein Rebound auf die Gas-Schicht (Deponie, Leckagen, Dünger, Prozess-N₂O, Kältemittel sind
    regulatorische/prozesstechnische Maßnahmen ohne preisgetriebenen Mehrverbrauch).
    Sensitivität: Rebound wie CO₂-Schicht → separat ausgewiesen.
Liest alle Mengen aus canon/data/*.yaml — keine hartkodierten Gas- oder Overlap-Werte.
"""

import contextlib
import io
import os
import sys

import numpy as np
import yaml

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

_HERE = os.path.dirname(os.path.abspath(__file__))
_DATA = os.path.join(_HERE, "..", "..", "canon", "data")
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


class _QuietBuf(io.StringIO):
    def reconfigure(self, *args, **kwargs):
        return None


with contextlib.redirect_stdout(_QuietBuf()):
    import monte_carlo as mc


def _yaml(name):
    with open(os.path.join(_DATA, name), encoding="utf-8") as f:
        return yaml.safe_load(f)


imp = _yaml("impact_master.yaml")
ovl = _yaml("overlap_matrix.yaml")
ga = imp["ghg_accounting"]

# Gas-Quelle → (Block in impact_master, Domain oder None)
SOURCES = {
    "ch4_B_production": ("methane_ch4", "B_production"),
    "ch4_C_energy": ("methane_ch4", "C_energy"),
    "ch4_D_food_land": ("methane_ch4", "D_food_land"),
    "n2o_D_food_land": ("nitrous_oxide_n2o", "D_food_land"),
    "n2o_B_production": ("nitrous_oxide_n2o", "B_production"),
    "f_gases": ("f_gases", None),
}

N = 10000


def draw_gas_layer(n):
    """Netto-Gas-Schicht (positiv = Reduktion) vor Umsetzungsrate, je Iteration."""
    totals = {}
    for gas in ("methane_ch4", "nitrous_oxide_n2o", "f_gases"):
        g = ga[gas]
        lo, hi = sorted(abs(x) for x in g["unsicherheit"])
        totals[gas] = np.random.triangular(lo, abs(g["gesamt"]), hi, n)
    net = np.zeros(n)
    for key, (gas, dom) in SOURCES.items():
        src = ovl["gas_layer_overlaps"][key]
        point_gas = abs(ga[gas]["gesamt"])
        share = (abs(ga[gas]["domains"][dom]["total"]) / point_gas) if dom else 1.0
        amount = totals[gas] * share
        o = src["overlap_with_co2_layer"]
        if o > 0 and src["evidence"] != "belegt":
            o = np.random.uniform(0.0, o, n)
        net += np.maximum(amount - o, 0.0)
    return net


def run(rebound_on_gases=False):
    # Erst alle CO₂-Szenarien in derselben Reihenfolge wie monte_carlo.py (seed 42) →
    # CO₂-Draws identisch zur Headline; die Gas-Schicht zieht danach.
    np.random.seed(42)
    co2_net = {name: mc.simulate_szenario(p["impl"], p["rebound"], p["s2"], p["s3"],
                                          p["engpaesse"], p["klima"], n=N)["netto"]
               for name, p in mc.szenarios.items()}
    out = {}
    for name, p in mc.szenarios.items():
        co2 = co2_net[name]
        gas = draw_gas_layer(N)
        impl = np.clip(np.random.normal(p["impl"], 0.05, N), 0, 1)
        gas_eff = gas * impl
        if rebound_on_gases:
            rb = np.clip(np.random.normal(p["rebound"], 0.03, N), 0, 0.5)
            gas_eff = gas_eff * (1 - rb)
        out[name] = {"co2": co2, "ghg": co2 - gas_eff}
    return out


res = run()
res_rb = run(rebound_on_gases=True)

# Anti-Drift: CO₂-Schicht muss exakt die Headline aus monte_carlo.py reproduzieren
for _name, _r in res.items():
    assert np.isclose(np.percentile(_r["co2"], 50), mc.results[_name]["p50"]), \
        f"CO₂-Median weicht von monte_carlo.py ab: {_name}"

print("=" * 78)
print("PROVOLUTION ALL-GHG-BILANZ · MONTE-CARLO (CO₂ + CH₄ + N₂O + F-Gase)")
print("=" * 78)
print(f"N={N} je Szenario · seed=42 · CO₂-Schicht = monte_carlo.py (identische Draws)")
print(f"Gas-Punktwerte (AR6): CH₄ {ga['methane_ch4']['gesamt']} · N₂O {ga['nitrous_oxide_n2o']['gesamt']} · "
      f"F-Gase {ga['f_gases']['gesamt']} Gt CO₂eq/yr; Overlap lt. overlap_matrix.yaml")
print()
print(f"{'Szenario':<48} {'CO₂ Median':>11} {'GHG Median':>11} {'GHG 90% KI':>18}")
print("─" * 78)
rows = []
for name in mc.szenarios:
    c50 = np.percentile(res[name]["co2"], 50)
    g5, g50, g95 = np.percentile(res[name]["ghg"], [5, 50, 95])
    rb50 = np.percentile(res_rb[name]["ghg"], 50)
    rows.append((name, c50, g50, g5, g95, rb50))
    print(f"{name:<48} {c50:+11.1f} {g50:+11.1f} {f'[{g5:+.1f}, {g95:+.1f}]':>18}")
print()
print("Sensitivität · Rebound auch auf Gas-Schicht:")
for name, c50, g50, g5, g95, rb50 in rows:
    print(f"  {name:<46} GHG-Median {rb50:+.1f} (Δ {rb50 - g50:+.1f})")
print()
GLOBAL = 55.0
print(f"Anteil an globaler Baseline ({GLOBAL} Gt CO₂eq/yr), GHG-Median:")
for name, c50, g50, *_ in rows:
    print(f"  {name:<46} {-g50 / GLOBAL * 100:5.1f} %")

# CSV für Doku/Figuren
with open(os.path.join(_HERE, "ghg_percentiles.csv"), "w", encoding="utf-8", newline="") as f:
    f.write("scenario,co2_p50,ghg_p5,ghg_p50,ghg_p95,ghg_p50_rebound_on_gases\n")
    for name, c50, g50, g5, g95, rb50 in rows:
        f.write(f"{name.split('(')[0].strip()},{c50:.2f},{g5:.2f},{g50:.2f},{g95:.2f},{rb50:.2f}\n")
