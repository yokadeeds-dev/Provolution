#!/usr/bin/env python3
"""Deep Checks - Zahlen-Konsistenz"""
import yaml

print("="*70)
print("DEEP CONSISTENCY CHECKS")
print("="*70 + "\n")

co2 = yaml.safe_load(open("20_CANON/data/co2_master.yaml", encoding='utf-8'))
impact = yaml.safe_load(open("20_CANON/data/impact_master.yaml", encoding='utf-8'))

issues = []

# Check 1: GHG Total Konsistenz
print("[1] GHG Totals...")
co2_total = co2['gesamt']['reduktion_hart']
ghg_co2 = impact['ghg_accounting']['co2']['gesamt']['reduktion_hart']
ghg_ch4 = impact['ghg_accounting']['methane_ch4']['gesamt']
ghg_n2o = impact['ghg_accounting']['nitrous_oxide_n2o']['gesamt']
ghg_fgas = impact['ghg_accounting']['f_gases']['gesamt']
ghg_total = impact['ghg_accounting']['ghg_total']['total']

calculated_total = ghg_co2 + ghg_ch4 + ghg_n2o + ghg_fgas

if abs(calculated_total - ghg_total) > 0.1:
    issues.append(f"GHG Total Inkonsistenz: {calculated_total} vs {ghg_total}")
else:
    print(f"  OK: GHG Total = {ghg_total} Gt CO2eq/Jahr")
    print(f"      (CO2: {ghg_co2}, CH4: {ghg_ch4}, N2O: {ghg_n2o}, F-Gase: {ghg_fgas})")

# Check 2: Domain Summen
print("\n[2] Domain Summen...")
domains = ['A_governance', 'B_production', 'C_energy', 'D_food_land',
           'E_education', 'F_technology', 'G_monitoring', 'H_meta']

domain_sum = 0
for d in domains:
    val = co2['domains'].get(d, {}).get('total', 0)
    domain_sum += val

if abs(domain_sum - co2_total) > 0.1:
    issues.append(f"Domain-Summe {domain_sum} != CO2-Total {co2_total}")
else:
    print(f"  OK: Domain-Summe = {domain_sum} Gt (= CO2 Total)")

# Check 3: Equity Score Range
print("\n[3] Equity Score Range...")
equity = impact['social']['equity']['distributional_impact']['net_equity_score']
if not (-1 <= equity <= 1):
    issues.append(f"Equity Score {equity} außerhalb [-1, 1]")
else:
    print(f"  OK: Equity Score = {equity} (in Range)")

# Check 4: Water Konsistenz
print("\n[4] Water Balance...")
water_saved = impact['environmental']['water']['gesamt']
water_domains = sum([
    impact['environmental']['water']['by_domain'].get(d, 0) 
    for d in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
])

if abs(water_saved - water_domains) > 1:
    issues.append(f"Water: Gesamt {water_saved} != Domains {water_domains}")
else:
    print(f"  OK: Water Balance = {water_saved} km³/Jahr")

# Check 5: Jobs plausibel?
print("\n[5] Employment Plausibility...")
jobs = impact['social']['co_benefits']['employment']['jobs_created']
if jobs < 1 or jobs > 100:
    issues.append(f"Jobs {jobs}M erscheint unrealistisch")
else:
    print(f"  OK: Jobs = {jobs}M (plausibel)")

# Check 6: Uncertainty Ranges
print("\n[6] Uncertainty Ranges...")
val_data = impact.get('validation', {}).get('uncertainty_ranges', {})
for key, unc in val_data.items():
    if '+' in str(unc) or '-' in str(unc):
        print(f"  OK: {key} = {unc}")

print("\n" + "="*70)
if issues:
    print(f"WARNUNG: {len(issues)} Inkonsistenzen:\n")
    for i in issues:
        print(f"  - {i}")
else:
    print("PERFEKT: Alle Zahlen konsistent!")
print("="*70)
