#!/usr/bin/env python3
"""
Multi-Impact Build System v2.0 - Single Source of Truth
Ersetzt Platzhalter in Markdown-Dokumenten mit Werten aus master YAML-Dateien

Features v2.0:
- Dual-Source Support (co2_master.yaml + impact_master.yaml)
- Erweiterte Platzhalter für Multi-Impact Assessment
- Backward Compatible mit v1.x

Verwendung:
    python build_impact_references.py              # Preview Modus
    python build_impact_references.py --apply      # Tatsächlich ersetzen
    python build_impact_references.py --validate   # Nur Konsistenz prüfen
    python build_impact_references.py --update-n   # YAML: derived n persistieren
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple
import sys

# Konfiguration
MASTER_DATA_CO2 = Path(__file__).parent / "20_CANON" / "data" / "co2_master.yaml"
MASTER_DATA_IMPACT = Path(__file__).parent / "20_CANON" / "data" / "impact_master.yaml"
CANON_DIR = Path(__file__).parent / "06_CANON"
CANON_20_DIR = Path(__file__).parent / "20_CANON"
ENGLISH_DIR = Path(__file__).parent / "10_ENGLISH"
RELEASE_DIR = Path(__file__).parent / "_release"
PILOTEN_DIR = Path(__file__).parent / "03_PILOTEN"

# Platzhalter-Definitionen mit Source-Mapping
PLACEHOLDERS = {
    # === CO2-ONLY (aus co2_master.yaml) ===
    '{{CO2_TOTAL}}': ('co2', 'gesamt.reduktion_hart'),
    '{{CO2_TOTAL_SOFT}}': ('co2', 'gesamt.vermeidung_weich'),
    '{{CO2_POTENTIAL}}': ('co2', 'gesamt.total_potenzial'),
    '{{CO2_COVERAGE}}': ('co2', 'gesamt.anteil_global_emissions'),
    '{{CO2_CORRELATION}}': ('co2', 'gesamt.korrelation_theorie_praxis'),
    
    # Domain Totals (CO2-only)
    '{{CO2_DOMAIN_A}}': ('co2', 'domains.A_governance.total'),
    '{{CO2_DOMAIN_B}}': ('co2', 'domains.B_production.total'),
    '{{CO2_DOMAIN_C}}': ('co2', 'domains.C_energy.total'),
    '{{CO2_DOMAIN_D}}': ('co2', 'domains.D_food_land.total'),
    '{{CO2_DOMAIN_E}}': ('co2', 'domains.E_education.total'),
    '{{CO2_DOMAIN_F}}': ('co2', 'domains.F_technology.total'),
    '{{CO2_DOMAIN_G}}': ('co2', 'domains.G_monitoring.total'),
    '{{CO2_DOMAIN_H}}': ('co2', 'domains.H_meta.total'),
    
    # Einzelanwendungen
    '{{CO2_B07}}': ('co2', 'domains.B_production.apps.B07_kreislaufwirtschaft'),
    '{{CO2_C11}}': ('co2', 'domains.C_energy.apps.C11_erneuerbare'),
    '{{CO2_D15}}': ('co2', 'domains.D_food_land.apps.D15_regen_landwirtschaft'),
    '{{CO2_D16}}': ('co2', 'domains.D_food_land.apps.D16_co2_senken_boden'),
    
    # Metriken
    '{{SEC_SCORE_AVG}}': ('co2', 'metrics.durchschnitt_sec_score'),
    '{{EMISSIONS_BASELINE}}': ('co2', 'validation.global_emissions_baseline'),
    
    # === MULTI-IMPACT (aus impact_master.yaml) ===
    
    # GHG Extended
    '{{GHG_TOTAL}}': ('impact', 'ghg_accounting.ghg_total.total'),
    '{{GHG_CH4}}': ('impact', 'ghg_accounting.methane_ch4.gesamt'),
    '{{GHG_N2O}}': ('impact', 'ghg_accounting.nitrous_oxide_n2o.gesamt'),
    '{{GHG_F_GASES}}': ('impact', 'ghg_accounting.f_gases.gesamt'),
    
    # Environmental
    '{{WATER_SAVED}}': ('impact', 'environmental.water.gesamt'),
    '{{LAND_FREED}}': ('impact', 'environmental.land_use.land_use_change.freed_land'),
    '{{BIODIVERSITY_MSA}}': ('impact', 'environmental.biodiversity.msa_index.improvement'),
    '{{SOC_INCREASE}}': ('impact', 'environmental.land_use.soil_quality.soil_organic_carbon_increase'),
    
    # Social & Equity
    '{{EQUITY_SCORE}}': ('impact', 'social.equity.distributional_impact.net_equity_score'),
    '{{JOBS_CREATED}}': ('impact', 'social.co_benefits.employment.jobs_created'),
    '{{HEALTH_VALUE}}': ('impact', 'social.co_benefits.health.air_quality_improvement.economic_value'),
    '{{AVOIDED_DEATHS}}': ('impact', 'social.co_benefits.health.air_quality_improvement.avoided_deaths_per_year'),
    
    # Energy & Rebound
    '{{DIGITAL_FOOTPRINT}}': ('impact', 'energy_system.digitalization_footprint.components.total.emissions'),
    '{{REBOUND_FACTOR}}': ('impact', 'energy_system.rebound_effects.net_rebound_factor'),
    
    # Pathways
    '{{TEMP_HIGH_2050}}': ('impact', 'transformation_pathways.scenarios.provolution_high.temperature'),
    '{{CARBON_BUDGET}}': ('impact', 'transformation_pathways.carbon_budget.provolution_cumulative_reduction_to_2050'),
}


def load_master_data() -> Tuple[Dict, Dict]:
    """Lade Master-Daten aus beiden YAML-Dateien"""
    # CO2-Daten (Legacy, immer erforderlich)
    if not MASTER_DATA_CO2.exists():
        print(f"❌ FEHLER: {MASTER_DATA_CO2} nicht gefunden!")
        sys.exit(1)
    
    with open(MASTER_DATA_CO2, 'r', encoding='utf-8') as f:
        co2_data = yaml.safe_load(f)
    
    # Multi-Impact Daten (optional für Backward Compatibility)
    impact_data = {}
    if MASTER_DATA_IMPACT.exists():
        with open(MASTER_DATA_IMPACT, 'r', encoding='utf-8') as f:
            impact_data = yaml.safe_load(f)
        print(f"✅ impact_master.yaml geladen (v{impact_data.get('meta', {}).get('version', '?')})")
    else:
        print("ℹ️  impact_master.yaml nicht gefunden - nur CO2-Daten verfügbar")
    
    return co2_data, impact_data


def get_value_from_path(data: Dict, path: str) -> float:
    """Extrahiere Wert aus verschachteltem Dict mittels Pfad"""
    keys = path.split('.')
    value = data
    for key in keys:
        if isinstance(value, dict):
            value = value[key]
        else:
            raise KeyError(f"Cannot access '{key}' in non-dict value")
    return value


def derive_n(co2_data: Dict) -> Dict:
    """Berechne n (Hebel-Anzahl) dynamisch aus YAML-Struktur.

    Returns: dict mit n_aj_apps, n_communities, n_total, n_metrics_static
    Used by validate_consistency (Commit C) and YAML output (Commit D).
    """
    aj_apps = sum(
        len(d.get('apps', {}))
        for d in co2_data.get('domains', {}).values()
        if isinstance(d, dict)
    )
    communities = len(
        co2_data.get('community_integrations', {}).get('integrations', {})
    )
    return {
        'n_aj_apps': aj_apps,
        'n_communities': communities,
        'n_total': aj_apps + communities,
        'n_metrics_static': co2_data.get('metrics', {}).get('anzahl_anwendungen'),
    }


def update_n_in_yaml(filepath: Path, n_value: int) -> Tuple[bool, int]:
    """Schreibt metrics.anzahl_anwendungen via line-level regex.

    Erhält Inline-Kommentar + Formatierung (kein yaml.dump → kein
    Datei-Rewrite). Nur die einzelne Zahl wird ersetzt.

    Binary I/O: erhält Line-Endings (LF/CRLF) byte-exakt — Python's
    text-mode write konvertiert sonst auf Windows zu OS-default CRLF
    und erzeugt false positive diffs in jeder Zeile.

    Returns: (changed, old_value)
        changed = True wenn Zahl geändert
        changed = False wenn Pattern nicht gefunden ODER bereits aktuell
        old_value = vorgefundener Wert, oder -1 wenn Pattern nicht gefunden
    """
    raw = filepath.read_bytes()
    text = raw.decode('utf-8')
    pattern = re.compile(r'^(\s*anzahl_anwendungen:\s*)(\d+)(.*)$', re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return False, -1
    old_value = int(match.group(2))
    if old_value == n_value:
        return False, old_value
    new_text = pattern.sub(rf'\g<1>{n_value}\g<3>', text, count=1)
    filepath.write_bytes(new_text.encode('utf-8'))
    return True, old_value


def resolve_placeholder(placeholder: str, co2_data: Dict, impact_data: Dict) -> Tuple[bool, float]:
    """Löse Platzhalter auf
    
    Returns: (success: bool, value: float)
    """
    if placeholder not in PLACEHOLDERS:
        return False, 0.0
    
    source, path = PLACEHOLDERS[placeholder]
    
    try:
        if source == 'co2':
            value = get_value_from_path(co2_data, path)
        elif source == 'impact':
            if not impact_data:
                print(f"  ⚠️  {placeholder} erfordert impact_master.yaml")
                return False, 0.0
            value = get_value_from_path(impact_data, path)
        else:
            return False, 0.0
        
        return True, value
    except (KeyError, TypeError) as e:
        print(f"  ⚠️  Fehler bei {placeholder}: {e}")
        return False, 0.0


def find_and_replace_in_file(filepath: Path, co2_data: Dict, impact_data: Dict, apply: bool = False) -> int:
    """Finde und ersetze Platzhalter in einer Datei
    
    Returns: Anzahl der Ersetzungen
    """
    if not filepath.exists() or not filepath.suffix == '.md':
        return 0
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return 0
    
    original_content = content
    replacements = 0
    
    for placeholder in PLACEHOLDERS.keys():
        if placeholder in content:
            success, value = resolve_placeholder(placeholder, co2_data, impact_data)
            if success:
                # Ersetze Platzhalter mit Wert
                content = content.replace(placeholder, str(value))
                replacements += 1
    
    if replacements > 0 and apply:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return replacements


def scan_directory(directory: Path, co2_data: Dict, impact_data: Dict, apply: bool = False) -> int:
    """Scanne Verzeichnis nach Markdown-Dateien"""
    total = 0
    
    for md_file in directory.rglob('*.md'):
        count = find_and_replace_in_file(md_file, co2_data, impact_data, apply)
        if count > 0:
            rel_path = md_file.relative_to(directory.parent)
            action = "✅ Ersetzt" if apply else "🔍 Gefunden"
            print(f"  {action}: {rel_path} ({count} Platzhalter)")
            total += count
    
    return total


def validate_consistency(co2_data: Dict) -> List[str]:
    """Prüfe Konsistenz der CO2-Daten"""
    logs = []
    
    try:
        # Prüfe Domain-Summen
        for domain_key, domain_data in co2_data.get('domains', {}).items():
            if isinstance(domain_data, dict) and 'total' in domain_data:
                if 'apps' in domain_data:
                    if domain_key in ["B_production", "C_energy", "D_food_land"]:
                        logs.append(f"ℹ️  {domain_key}: Überschneidungen dokumentiert")
                    else:
                        app_sum = sum(domain_data['apps'].values())
                        if abs(app_sum - domain_data['total']) < 0.1:
                            logs.append(f"✓ {domain_key}: Konsistent")
                        else:
                            logs.append(f"⚠️  {domain_key}: Prüfen empfohlen")
        
        # Prüfe Gesamt (community-aware, Commit C)
        domain_sum = sum(d.get('total', 0) for d in co2_data.get('domains', {}).values() if isinstance(d, dict))
        community_total = co2_data.get('community_integrations', {}).get('total', 0)
        total_sum = domain_sum + community_total
        expected = co2_data.get('gesamt', {}).get('reduktion_hart', 0)

        if abs(total_sum - expected) < 0.1:
            if abs(community_total) > 0.001:
                logs.append(f"✓ Gesamt-Bilanz: Konsistent ({expected} Gt = Domains {domain_sum} + Communities {community_total})")
            else:
                logs.append(f"✓ Gesamt-Bilanz: Konsistent ({expected} Gt)")
        else:
            logs.append(f"⚠️  Gesamt: Domains {domain_sum} + Communities {community_total} = {total_sum} vs reduktion_hart {expected} Gt")

        # n-Derivation (Commit C: live anzeige; Commit D: persistierung in YAML)
        n_info = derive_n(co2_data)
        logs.append(f"ℹ️  n_derived = {n_info['n_total']} (A-J apps: {n_info['n_aj_apps']} + Communities: {n_info['n_communities']})")
        if n_info['n_metrics_static'] is not None and n_info['n_metrics_static'] != n_info['n_total']:
            logs.append(f"⚠️  n drift: metrics.anzahl_anwendungen={n_info['n_metrics_static']} vs derived={n_info['n_total']} (heilt in Commit D)")
    
    except Exception as e:
        logs.append(f"❌ Validierung fehlgeschlagen: {e}")
    
    return logs


def main():
    """Haupt-Workflow"""
    # Windows PowerShell UTF-8 Fix
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    apply = '--apply' in sys.argv
    validate_only = '--validate' in sys.argv
    update_n = '--update-n' in sys.argv
    
    print("=" * 70)
    print("Multi-Impact Build System v2.0 - Single Source of Truth")
    print("=" * 70)
    print()
    
    # Lade Master-Daten
    print(f"📂 Lade Master-Daten...")
    co2_data, impact_data = load_master_data()
    print(f"✅ co2_master.yaml v{co2_data['meta']['version']} ({co2_data['meta']['last_updated']})")
    print()
    
    # Validierung
    if validate_only or not apply:
        print("🔍 Validiere CO2-Konsistenz...")
        validation_logs = validate_consistency(co2_data)
        for log in validation_logs:
            print(f"  {log}")
        print()
    
    if validate_only:
        print("✅ Validierung abgeschlossen.")
        return

    if update_n:
        print("🔧 Update n in co2_master.yaml...")
        n_info = derive_n(co2_data)
        changed, old = update_n_in_yaml(MASTER_DATA_CO2, n_info['n_total'])
        if changed:
            print(f"  ✅ metrics.anzahl_anwendungen: {old} → {n_info['n_total']}")
        elif old == n_info['n_total']:
            print(f"  ℹ️  Bereits aktuell ({old})")
        else:
            print(f"  ❌ Pattern nicht gefunden")
        print()
        return
    
    # Verarbeite Verzeichnisse
    directories = [
        ("06_CANON (Kanonische Dokumente)", CANON_DIR),
        ("20_CANON (Daten & Dokumentation)", CANON_20_DIR),
        ("03_PILOTEN (Praxisprojekte)", PILOTEN_DIR),
        ("10_ENGLISH (Englische Versionen)", ENGLISH_DIR),
        ("_release (Releases)", RELEASE_DIR),
    ]
    
    total_replacements = 0
    
    for name, directory in directories:
        if not directory.exists():
            print(f"⏭️  {name}: Nicht gefunden - übersprungen")
            continue
        
        print(f"📁 {name}")
        count = scan_directory(directory, co2_data, impact_data, apply)
        
        if count > 0:
            total_replacements += count
            print(f"  → {count} Platzhalter {'ersetzt' if apply else 'gefunden'}")
        else:
            print(f"  → Keine Platzhalter gefunden")
        print()
    
    # Zusammenfassung
    print("=" * 70)
    if apply:
        print(f"✅ FERTIG: {total_replacements} Platzhalter ersetzt")
    else:
        print(f"🔍 PREVIEW: {total_replacements} Platzhalter gefunden")
        print()
        print("💡 Zum Anwenden: python build_impact_references.py --apply")
    print("=" * 70)


if __name__ == "__main__":
    main()
