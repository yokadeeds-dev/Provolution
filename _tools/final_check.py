#!/usr/bin/env python3
"""Finale Konsistenz-Pruefung vor Peer-Review"""
import yaml, json
from pathlib import Path

issues = []

print("="*70)
print("FINALE KONSISTENZ-PRUEFUNG")
print("="*70 + "\n")

# 1. Cross-References zwischen Dokumenten
print("[1] Cross-Reference Checks...")

# H01 in impact_master erwähnt?
impact = yaml.safe_load(open("20_CANON/data/impact_master.yaml", encoding='utf-8'))
h01_mentioned = False
for section in str(impact).lower().split():
    if 'h01' in section or 'hanf' in section or 'hemp' in section:
        h01_mentioned = True
        break

if not h01_mentioned:
    issues.append("WARN: H01 nicht explizit in impact_master.yaml referenziert")
else:
    print("  OK: H01 in impact_master.yaml erwähnt")

# 2. Alle Bände referenzieren neue Methodik?
print("\n[2] Band-Integration Checks...")

band3_files = list(Path("06_CANON").glob("*Band3*.md"))
if band3_files:
    band3 = open(band3_files[0], encoding='utf-8').read()
    if 'METHODOLOGY' not in band3 and 'Methodik' not in band3:
        issues.append("WARN: Band 3 verlinkt nicht zur neuen Methodik")
    else:
        print("  OK: Band 3 erwähnt Methodik")

# 3. Alle Quellen haben Jahr?
print("\n[3] Quellen-Vollständigkeit...")

sources_incomplete = []
for key, val in impact.get('validation', {}).get('external_comparison', {}).items():
    if isinstance(val, str) and not any(year in val for year in ['2020', '2021', '2022', '2023', '2024', '2025']):
        sources_incomplete.append(key)

if sources_incomplete:
    issues.append(f"WARN: Quellen ohne Jahr: {sources_incomplete}")
else:
    print("  OK: Alle Quellen haben Jahreszahlen")

# 4. README verlinkt alles Wichtige?
print("\n[4] README Vollständigkeit...")

readme = open("README.md", encoding='utf-8').read()
critical_links = [
    ('METHODOLOGY_CO2_ASSESSMENT', 'Methodik'),
    ('impact_master.yaml', 'Impact Data'),
    ('PILOT_H01_COMPLETE', 'H01 Pilot'),
    ('PROJECT_IMPACT_SCHEMA', 'Schema')
]

for link, name in critical_links:
    if link not in readme:
        issues.append(f"WARN: README fehlt Link zu {name}")
    else:
        print(f"  OK: README verlinkt {name}")

# 5. Figures vorhanden und referenziert?
print("\n[5] Figures Check...")

figures_dir = Path("20_CANON/docs/figures")
if not figures_dir.exists():
    issues.append("ERROR: figures/ Verzeichnis fehlt")
else:
    figures = list(figures_dir.glob("*.png"))
    print(f"  OK: {len(figures)} Figuren gefunden")
    
    # Werden sie irgendwo referenziert?
    all_docs = list(Path("20_CANON/docs").glob("*.md"))
    referenced = False
    for doc in all_docs:
        if 'systemgrenzen' in open(doc, encoding='utf-8').read().lower():
            referenced = True
            break
    
    if not referenced:
        issues.append("WARN: Systemgrenzen-Diagramm nirgends referenziert")

# 6. CITATION.cff aktuell?
print("\n[6] Citation Check...")

if Path("CITATION.cff").exists():
    citation = open("CITATION.cff", encoding='utf-8').read()
    if '2026' in citation and 'v2.0' in citation:
        print("  OK: CITATION.cff aktuell")
    else:
        issues.append("WARN: CITATION.cff ggf. veraltet (prüfen: Jahr, Version)")
else:
    issues.append("WARN: CITATION.cff fehlt (optional aber empfohlen)")

# 7. Alle JSONs valide?
print("\n[7] JSON Validation...")

json_files = list(Path("20_CANON/templates").glob("*.json"))
for jf in json_files:
    try:
        json.load(open(jf, encoding='utf-8'))
        print(f"  OK: {jf.name} valide")
    except json.JSONDecodeError as e:
        issues.append(f"ERROR: {jf.name} invalid JSON: {e}")

# 8. YAMLs valide?
print("\n[8] YAML Validation...")

yaml_files = list(Path("20_CANON/data").glob("*.yaml"))
for yf in yaml_files:
    try:
        yaml.safe_load(open(yf, encoding='utf-8'))
        print(f"  OK: {yf.name} valide")
    except yaml.YAMLError as e:
        issues.append(f"ERROR: {yf.name} invalid YAML: {e}")

# 9. Keine TODO/FIXME im Code?
print("\n[9] TODO/FIXME Check...")

todos_found = []
for md_file in Path("20_CANON").rglob("*.md"):
    content = open(md_file, encoding='utf-8').read().upper()
    if 'TODO' in content or 'FIXME' in content or 'XXX' in content:
        todos_found.append(md_file.name)

if todos_found:
    issues.append(f"INFO: TODO/FIXME gefunden in: {todos_found[:3]}...")
else:
    print("  OK: Keine TODOs gefunden")

# 10. License Files vorhanden?
print("\n[10] License Check...")

if Path("LICENSE").exists() or Path("LICENSE.md").exists():
    print("  OK: LICENSE vorhanden")
else:
    issues.append("WARN: LICENSE Datei fehlt (CC0+OHL sollte dokumentiert sein)")

# SUMMARY
print("\n" + "="*70)
if issues:
    print(f"ACHTUNG: {len(issues)} potenzielle Probleme gefunden:\n")
    for i, issue in enumerate(issues, 1):
        print(f"  {i}. {issue}")
    print("\nEmpfehlung: Prüfen vor PR-Merge")
else:
    print("PERFEKT: Alle Checks bestanden!")
    print("Status: READY FOR PEER-REVIEW SUBMISSION")
print("="*70)
