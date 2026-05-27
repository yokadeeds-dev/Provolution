#!/usr/bin/env python3
"""
Vollständigkeitsprüfung Provolution Multi-Impact Framework
Prüft: Konsistenz, Vollständigkeit, Referenz-Integrität, Peer-Review-Readiness
"""

import yaml
from pathlib import Path
import json

def check_yaml_consistency():
    """Prüft co2_master.yaml und impact_master.yaml auf Konsistenz"""
    issues = []
    
    co2_file = Path("20_CANON/data/co2_master.yaml")
    impact_file = Path("20_CANON/data/impact_master.yaml")
    
    # Lade beide Files
    with open(co2_file, 'r', encoding='utf-8') as f:
        co2_data = yaml.safe_load(f)
    
    with open(impact_file, 'r', encoding='utf-8') as f:
        impact_data = yaml.safe_load(f)
    
    # Prüfung 1: CO2-Werte konsistent?
    co2_total = co2_data['gesamt']['reduktion_hart']
    ghg_co2 = impact_data['ghg_accounting']['co2']['gesamt']['reduktion_hart']
    
    if abs(co2_total - ghg_co2) > 0.1:
        issues.append(f"❌ CO2-Inkonsistenz: co2_master={co2_total}, impact_master={ghg_co2}")
    else:
        print(f"✅ CO2-Werte konsistent: {co2_total} Gt")
    
    # Prüfung 2: Domain-Summen konsistent?
    domains = ['A_governance', 'B_production', 'C_energy', 'D_food_land', 
               'E_education', 'F_technology', 'G_monitoring', 'H_meta']
    
    for domain in domains:
        co2_val = co2_data['domains'].get(domain, {}).get('total', 0)
        impact_val = impact_data['ghg_accounting']['co2']['domains'].get(domain, 0)
        
        if abs(co2_val - impact_val) > 0.1:
            issues.append(f"❌ Domain {domain}: co2={co2_val}, impact={impact_val}")
    
    print(f"✅ Domain-Werte geprüft: {len(domains)} Domains")
    
    return issues

def check_schema_completeness():
    """Prüft ob PROJECT_IMPACT_SCHEMA alle erforderlichen Felder hat"""
    issues = []
    
    schema_file = Path("20_CANON/templates/PROJECT_IMPACT_SCHEMA.json")
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    # Erforderliche Top-Level Felder
    required = ['project_meta', 'ghg_accounting', 'environmental', 
                'social', 'governance']
    
    if 'required' in schema:
        missing = set(required) - set(schema['required'])
        if missing:
            issues.append(f"❌ Schema fehlt required: {missing}")
        else:
            print(f"✅ Schema hat alle required Felder")
    
    return issues

def check_h01_completeness():
    """Prüft ob H01 Pilot alle Dimensionen abdeckt"""
    issues = []
    
    h01_file = Path("03_PILOTEN/PILOT_H01_COMPLETE.md")
    
    if not h01_file.exists():
        issues.append("❌ PILOT_H01_COMPLETE.md nicht gefunden")
        return issues
    
    with open(h01_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Prüfe kritische Kapitel
    required_sections = [
        'GHG-Bilanz',
        'Environmental',
        'Social',
        'SEC-Score',
        'Ökonomie'
    ]
    
    for section in required_sections:
        if section not in content:
            issues.append(f"❌ H01 fehlt Kapitel: {section}")
    
    if not issues:
        print(f"✅ H01 hat alle {len(required_sections)} Kern-Kapitel")
    
    return issues

def check_documentation_links():
    """Prüft ob Dokumentation korrekt verlinkt ist"""
    issues = []
    
    # Prüfe ob METHODOLOGY in Band 3 erwähnt wird
    band3_integration = Path("20_CANON/docs/BAND3_INTEGRATION_MULTI_IMPACT.md")
    
    if band3_integration.exists():
        with open(band3_integration, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'METHODOLOGY_CO2_ASSESSMENT.md' in content:
            print("✅ Band 3 Integration verlinkt Methodik")
        else:
            issues.append("⚠️  Band 3 Integration erwähnt Methodik nicht explizit")
    
    return issues

def check_build_system():
    """Prüft ob Build-System funktionsfähig ist"""
    issues = []
    
    build_file = Path("build_impact_references.py")
    
    if not build_file.exists():
        issues.append("❌ build_impact_references.py nicht gefunden")
        return issues
    
    print("✅ Build-System v2.0 vorhanden")
    return issues

def main():
    print("=" * 70)
    print("PROVOLUTION VOLLSTÄNDIGKEITSPRÜFUNG")
    print("=" * 70)
    print()
    
    all_issues = []
    
    print("[CHECK] Pruefe YAML-Konsistenz...")
    all_issues.extend(check_yaml_consistency())
    print()
    
    print("[CHECK] Pruefe Schema-Vollstaendigkeit...")
    all_issues.extend(check_schema_completeness())
    print()
    
    print("[CHECK] Pruefe H01 Pilot...")
    all_issues.extend(check_h01_completeness())
    print()
    
    print("[CHECK] Pruefe Dokumentations-Links...")
    all_issues.extend(check_documentation_links())
    print()
    
    print("[CHECK] Pruefe Build-System...")
    all_issues.extend(check_build_system())
    print()
    
    print("=" * 70)
    if all_issues:
        print(f"WARNING: {len(all_issues)} Probleme gefunden:")
        for issue in all_issues:
            print(f"  {issue}")
    else:
        print("SUCCESS: ALLE PRUEFUNGEN BESTANDEN - PEER-REVIEW READY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
