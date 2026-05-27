#!/usr/bin/env python3
import yaml, json
from pathlib import Path

print("="*70)
print("PROVOLUTION VOLLSTAENDIGKEITSPRUEFUNG")
print("="*70 + "\n")

issues = []

# 1. YAML Konsistenz
print("[1/5] YAML-Konsistenz...")
try:
    co2 = yaml.safe_load(open("20_CANON/data/co2_master.yaml", encoding='utf-8'))
    impact = yaml.safe_load(open("20_CANON/data/impact_master.yaml", encoding='utf-8'))
    
    if abs(co2['gesamt']['reduktion_hart'] - impact['ghg_accounting']['co2']['gesamt']['reduktion_hart']) < 0.1:
        print("  OK: CO2-Werte konsistent")
    else:
        issues.append("CO2-Inkonsistenz zwischen Dateien")
except Exception as e:
    issues.append(f"YAML-Fehler: {e}")

# 2. Schema Vollstaendigkeit
print("[2/5] Schema-Vollstaendigkeit...")
try:
    schema = json.load(open("20_CANON/templates/PROJECT_IMPACT_SCHEMA.json", encoding='utf-8'))
    required = {'project_meta', 'ghg_accounting', 'environmental', 'social', 'governance'}
    if required.issubset(set(schema.get('required', []))):
        print("  OK: Schema komplett")
    else:
        issues.append("Schema fehlt Pflichtfelder")
except Exception as e:
    issues.append(f"Schema-Fehler: {e}")

# 3. H01 Vollstaendigkeit
print("[3/5] H01 Pilot...")
try:
    h01 = open("03_PILOTEN/PILOT_H01_COMPLETE.md", encoding='utf-8').read()
    required = ['GHG-Bilanz', 'Environmental', 'Social', 'SEC-Score', 'Oekonomie']
    missing = [s for s in required if s not in h01]
    if not missing:
        print("  OK: H01 vollstaendig")
    else:
        issues.append(f"H01 fehlt: {missing}")
except Exception as e:
    issues.append(f"H01-Fehler: {e}")

# 4. Dokumentation
print("[4/5] Dokumentations-Links...")
if Path("20_CANON/docs/METHODOLOGY_CO2_ASSESSMENT.md").exists():
    print("  OK: Methodik vorhanden")
else:
    issues.append("Methodik fehlt")

# 5. Build System
print("[5/5] Build-System...")
if Path("build_impact_references.py").exists():
    print("  OK: Build-System v2.0")
else:
    issues.append("Build-System fehlt")

print("\n" + "="*70)
if issues:
    print(f"WARNING: {len(issues)} Probleme:")
    for i in issues: print(f"  - {i}")
else:
    print("SUCCESS: ALLE PRUEFUNGEN BESTANDEN!")
print("="*70)
