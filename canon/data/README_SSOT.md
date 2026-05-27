> **⚠️ DEPRECATED (2026-04-28)**
>
> Dieses Dokument beschrieb das **CO2-only-SSOT-System (v1.1)** vom Februar 2026.
> Es wurde im April 2026 durch das **Multi-Impact-SSOT-System (v2.0)** abgelöst,
> welches sechs Impact-Dimensionen umfasst (GHG, environmental, social,
> energy_system, governance, transformation_pathways).
>
> **Aktuelle Dokumentation:** [`README_MULTI_IMPACT.md`](./README_MULTI_IMPACT.md)
>
> Diese Datei wird als historische Referenz erhalten. Die hier beschriebenen
> Skripte (`build_co2_references.py`, `migrate_co2_values.py`) wurden nach
> `ARCHIVE/obsolete_2026-04-27/` verschoben.

---

# CO₂-Bilanz Single Source of Truth (SSOT) System
**Provolution Framework - Zentrale Datenverwaltung**

Version: 1.1  
Datum: 2026-01-24  
Status: Production Ready

---

## Übersicht

Das CO₂-Bilanz SSOT-System gewährleistet **Konsistenz und Nachvollziehbarkeit** aller CO₂-Werte über das gesamte Provolution-Framework hinweg.

### Kernprinzip

**Single Source of Truth:**  
Alle CO₂-Werte werden **zentral** in `20_CANON/data/co2_master.yaml` gespeichert und **automatisch** in alle Dokumente propagiert.

### Vorteile

✅ **Konsistenz:** Änderung an einer Stelle → automatisches Update überall  
✅ **Nachvollziehbarkeit:** Klare Herkunft jedes Wertes  
✅ **Wissenschaftliche Rigorosität:** Emissionsfaktoren mit Quellen und Unsicherheitsbändern  
✅ **Peer-Review-Fähigkeit:** Transparente Methodik nach GHG Protocol & IPCC AR6

---

## Architektur

```
20_CANON/data/
├── co2_master.yaml          # SINGLE SOURCE OF TRUTH
│   ├── Gesamt-Bilanz (-50.7 Gt/Jahr)
│   ├── Domain-spezifisch (A-H)
│   ├── Einzelanwendungen (30 Apps)
│   ├── Methodik-Metadaten
│   └── Emissionsfaktoren

20_CANON/docs/
└── METHODOLOGY_CO2_ASSESSMENT.md   # Wissenschaftliche Methodik

Root/
├── build_co2_references.py    # Build-System (Platzhalter → Werte)
├── migrate_co2_values.py      # Migrations-Tool (Werte → Platzhalter)

06_CANON/                       # Kanonische Dokumente
├── Band 1-5 (mit Platzhaltern)
└── Automatisch aktualisiert via Build

10_ENGLISH/                     # Englische Versionen
└── Automatisch synchronisiert

_release/                       # Release-Versionen
└── Automatisch synchronisiert
```

---

## Workflow

### 1. Werte ändern

Bearbeite **nur** die Master-Datei:
```bash
nano 20_CANON/data/co2_master.yaml
```

Beispiel:
```yaml
gesamt:
  reduktion_hart: -52.3  # Geändert von -50.7
```

### 2. Build-System ausführen

**Preview (ohne Änderungen):**
```bash
python build_co2_references.py
```

**Anwenden (schreibt Dateien):**
```bash
python build_co2_references.py --apply
```

**Nur Validierung:**
```bash
python build_co2_references.py --validate
```

### 3. Ergebnis

Alle Platzhalter in allen Dokumenten werden automatisch aktualisiert:
```markdown
# Vorher (in Band 4):
**Klimawirkung:** -50.7 Gt CO₂eq/Jahr

# Nachher:
**Klimawirkung:** -52.3 Gt CO₂eq/Jahr
```

---

## Platzhalter-Referenz

### Gesamt-Werte

| Platzhalter | Wert (aktuell) | Beschreibung |
|-------------|----------------|--------------|
| `-50.7` | -50.7 | Harte Reduktionen (Gt/Jahr) |
| `-28.5` | -28.5 | Weiche Vermeidungen (Gt/Jahr) |
| `-79.2` | -79.2 | Total-Potenzial |
| `0.92` | 0.92 | Anteil globaler Emissionen (92%) |
| `0.94` | 0.94 | SEC-CO₂-Korrelation |

### Domain-Werte (A-H)

| Platzhalter | Wert | Domain |
|-------------|------|--------|
| `-8.2` | -8.2 | Governance |
| `-15.8` | -15.8 | Production |
| `-12.3` | -12.3 | Energy |
| `-9.4` | -9.4 | Food/Land |
| `-1.8` | -1.8 | Education |
| `-2.1` | -2.1 | Technology |
| `-0.6` | -0.6 | Monitoring |
| `-0.5` | -0.5 | Meta-Framework |

### Einzelanwendungen (Beispiele)

| Platzhalter | Wert | Anwendung |
|-------------|------|-----------|
| `-23.0` | -23.0 | Kreislaufwirtschaft |
| `-15.0` | -15.0 | Erneuerbare Energie |
| `-4.0` | -4.0 | Regenerative Landwirtschaft |
| `-5.0` | -5.0 | CO₂-Senken Boden |

### Metriken

| Platzhalter | Wert | Beschreibung |
|-------------|------|--------------|
| `0.895` | 0.895 | Durchschnittlicher SEC-Score |
| `55.0` | 55.0 | Globale Emissionen Baseline (Gt/Jahr) |

---

## Neue Platzhalter hinzufügen

### 1. Master-Datei erweitern

`20_CANON/data/co2_master.yaml`:
```yaml
domains:
  D_food_land:
    apps:
      D17_hanf_oekosystem: -2.8  # Neu
```

### 2. Platzhalter-Mapping ergänzen

`build_co2_references.py`:
```python
PLACEHOLDERS = {
    '{{CO2_D17}}': 'domains.D_food_land.apps.D17_hanf_oekosystem',  # Neu
    # ... existing placeholders
}
```

### 3. In Dokumenten verwenden

```markdown
**Hanf-Ökosystem:** {{CO2_D17}} Gt CO₂eq/Jahr
```

### 4. Build ausführen

```bash
python build_co2_references.py --apply
```

---

## Wissenschaftliche Methodik

### Standards

Das System folgt:
- **GHG Protocol Corporate Standard** (2015)
- **IPCC AR6 Guidelines** (2022)
- **ISO 14064-1:2018**

### Emissionsfaktoren

Alle Faktoren in `co2_master.yaml` mit:
- Wert (z.B. 0.485 kg CO₂eq/kWh)
- Quelle (z.B. UBA 2023)
- Unsicherheitsband (95% CI)
- Scope-Zuordnung (1/2/3)

**Beispiel:**
```yaml
emission_factors:
  electricity_grid_de:
    value: 0.485
    source: "Umweltbundesamt (UBA) 2023"
    uncertainty: [0.450, 0.520]
    scope: "Scope 2"
```

### Vollständige Dokumentation

Siehe: `20_CANON/docs/METHODOLOGY_CO2_ASSESSMENT.md`

---

## Migration bestehender Dokumente

### Schritt 1: Hardcoded Werte identifizieren

```bash
# Suche nach -50.7 in allen Markdown-Dateien
grep -r "\-50\.7" 06_CANON/*.md
```

### Schritt 2: Migrations-Script vorbereiten

`migrate_co2_values.py` erweitern:
```python
MIGRATIONS = [
    (r'-50\.7 Gt CO₂eq/Jahr', '-50.7 Gt CO₂eq/Jahr'),
    # ... weitere Werte
]
```

### Schritt 3: Migration ausführen

**Preview:**
```bash
python migrate_co2_values.py
```

**Anwenden:**
```bash
python migrate_co2_values.py --apply
```

**Automatische Backups** werden vor Änderungen erstellt!

---

## Wartung

### Regelmäßige Aufgaben

1. **Konsistenz prüfen:**
   ```bash
   python build_co2_references.py --validate
   ```

2. **Nach Werte-Änderung:**
   ```bash
   python build_co2_references.py --apply
   ```

3. **Version-Bump:**
   ```yaml
   # In co2_master.yaml
   meta:
     version: "1.2"  # Erhöhen
     last_updated: "2026-XX-XX"  # Aktualisieren
   ```

### Fehlerbehandlung

**Warnung: "Summe Apps ≠ Total"**
```
⚠️  C_energy: Summe Apps (-20.1) ≠ Total (-12.3)
```

**Ursache:** Überschneidungen zwischen Anwendungen (z.B. C12-C14 unterstützen C11)

**Lösung:** In `co2_master.yaml` dokumentieren:
```yaml
C_energy:
  hinweis: "Überschneidungen zwischen C11-C14 bereits bereinigt"
```

---

## Best Practices

### ✅ DO

- Ändere Werte **nur** in `co2_master.yaml`
- Führe Build-System nach **jeder** Änderung aus
- Dokumentiere Quellen und Unsicherheiten
- Verwende Platzhalter für **häufig referenzierte** Werte
- Validiere Konsistenz regelmäßig

### ❌ DON'T

- Hardcode keine CO₂-Werte in Dokumente
- Überspringe nicht das Build-System
- Vergiss nicht Backups zu prüfen
- Verändere keine Auto-generierten Abschnitte manuell

---

## Troubleshooting

### Problem: "Module 'yaml' not found"

**Lösung:**
```bash
pip install pyyaml --break-system-packages
```

### Problem: Unicode-Fehler (Windows PowerShell)

Das Build-Script hat automatischen UTF-8 Fix integriert.

### Problem: Platzhalter werden nicht ersetzt

**Checks:**
1. Ist Platzhalter in `PLACEHOLDERS` dict definiert?
2. Existiert der Pfad in `co2_master.yaml`?
3. Liegt die Datei in 06_CANON, 10_ENGLISH oder _release?

---

## Changelog

### v1.1 (2026-01-24)
- ✅ Methodik-Sektion hinzugefügt
- ✅ Emissionsfaktoren mit Quellen
- ✅ Unsicherheitsbänder
- ✅ Standards-Referenzen (GHG Protocol, IPCC AR6)

### v1.0 (2026-01-24)
- ✅ Initial Release
- ✅ Master-Datei (`co2_master.yaml`)
- ✅ Build-System (`build_co2_references.py`)
- ✅ Migrations-Tool (`migrate_co2_values.py`)
- ✅ Erste Migration (9 Werte in Band 4)

---

## Kontakt & Feedback

**Entwickler:** Claude (Anthropic) + Yoka Dieng  
**Repository:** https://github.com/yokadeeds-dev/Provolution  
**Issues:** GitHub Issues verwenden

---

**Lizenz:** Open for Peer-Review, Copyright Yoka Dieng
