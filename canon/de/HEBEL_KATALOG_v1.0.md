# PROVOLUTION HEBEL-KATALOG v1.0

**Status:** Kanonische Index-Datei für alle Hebel im Provolution-Framework
**Version:** 1.0
**Datum:** 2026-05-09
**Erstellt in:** Phase 6D-D.4 (Resolution von G4-Block, siehe `01_STRATEGIE/DECISIONS/DEC_2026-05-09_hebel_set_canonical.md`)

---

## Zweck

Diese Datei ist die **konsolidierte Hebel-Liste** für Provolution. Sie löst die SET-Drift zwischen drei vorigen Quellen auf (Band 4 v4.2 = 30 Apps, YAML co2_master.yaml = 35 Einträge, MASTER_INDEX_ANWENDUNGEN.md = 40 Einträge in 17 IDs divergent).

**Architektur-Entscheidung (Option c aus DEC_2026-05-09):** Hebel-Katalog ist die SSoT für `was IST ein Hebel`. Detail-Inhalte bleiben in Band 4 v4.2 (kanonische Beschreibungen) bzw. STUB-Files; CO2-Werte bleiben in `20_CANON/data/co2_master.yaml`. Der Katalog **referenziert** beide, **dupliziert nicht**.

---

## Status-Klassen

| Status | Bedeutung |
|---|---|
| `band4-canonical` | In Band 4 v4.2 dokumentiert (Hauptkanon-Beschreibung) |
| `stub` | STUB-File existiert in eigenem Verzeichnis (I33/I34/J01); Band-4-Beschreibung ausstehend |
| `yaml-only` | In YAML mit quantifiziertem CO2-Wert, aber **noch nicht** in Band 4 (Aufnahme in Band 4 v4.3 = eigene Sub-Phase) |
| `community-integration` | Über AGENTIC_INTEGRATE-Pipeline akzeptiert; nicht Teil von A-J Hebel-Domains |

---

## Hebel-Liste (n=43 inkl. 5 Communities)

### Domain A — Governance & Steuerung (6)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| A01 | SEC-PRIORISIERUNG | sec_priorisierung | band4-canonical | -2.0 | konsistent |
| A02 | ENTSCHEIDUNGSKARTE | entscheidungskarte | band4-canonical | -1.5 | konsistent |
| A03 | RISIKOABSCHÄTZUNG | transparenz | band4-canonical | -1.8 | ⚠️ YAML-Tag-Drift (`transparenz` ≠ Band 4 Name) |
| A04 | SZENARIEN-VERGLEICH | partizipation | band4-canonical | -1.2 | ⚠️ YAML-Tag-Drift |
| A05 | PILOTPROJEKT-FRAMEWORK | konfliktloesung | band4-canonical | -0.9 | ⚠️ YAML-Tag-Drift |
| A06 | SKALIERUNGS-PROTOKOLL | kompetenz | band4-canonical | -0.8 | ⚠️ YAML-Tag-Drift |

### Domain B — Material/Produktion (6)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| B07 | KREISLAUFWIRTSCHAFT | kreislaufwirtschaft | band4-canonical | -23.0 | konsistent |
| B08 | BIOPOLYMERE (HANF) | bio_polymere | band4-canonical | -1.5 | konsistent |
| B09 | MATERIALFLUSS-STEUERUNG | wasserstoff | band4-canonical | -2.8 | ⚠️ **inhaltliche Drift** (YAML referenziert anderen Hebel) |
| B10 | ABFALL-ZU-RESSOURCE | ccs | band4-canonical | -1.2 | ⚠️ **inhaltliche Drift** (YAML referenziert anderen Hebel) |
| B11 | — | transformation | yaml-only | -1.8 | nicht in Band 4; YAML seit Commit 6bc312e |
| B12 | — | biomasse | yaml-only | -2.5 | nicht in Band 4; YAML seit Commit 6bc312e |

### Domain C — Energie & Infrastruktur (4)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| C11 | ERNEUERBARE INTEGRATION | erneuerbare | band4-canonical | -15.0 | konsistent |
| C12 | ENERGIE-SPEICHERUNG | speicher | band4-canonical | -2.1 | konsistent |
| C13 | SMART GRIDS | smart_grid | band4-canonical | -1.8 | konsistent |
| C14 | DEZENTRALE VERSORGUNG | dezentral | band4-canonical | -1.2 | konsistent |

### Domain D — Ernährung & Landnutzung (4)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| D15 | REGENERATIVE LANDWIRTSCHAFT | regen_landwirtschaft | band4-canonical | -4.0 | konsistent |
| D16 | CO₂-SENKEN (BODEN) | co2_senken_boden | band4-canonical | -5.0 | konsistent |
| D17 | HANF-ANBAU (NUTZPFLANZE) | hanf_oekosystem | band4-canonical | -2.8 | konsistent |
| D18 | URBANE LANDWIRTSCHAFT | ernaehrung | band4-canonical | -1.6 | konsistent |

### Domain E — Bildung & Bewusstsein (4)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| E19 | BEWUSSTSEINSBILDUNG | sec_literacy | band4-canonical | -0.8 | YAML-Tag mild abweichend |
| E20 | PARTIZIPATION | klima_bildung | band4-canonical | -0.6 | ⚠️ YAML-Tag-Drift |
| E21 | GERECHTIGKEITS-MECHANISMEN | erfahrungslernen | band4-canonical | -0.4 | ⚠️ YAML-Tag-Drift |
| E22 | KULTUR-TRANSFORMATION | (nicht in YAML) | band4-canonical | n/a | YAML hat E22 nicht; CO2-Wirkung nicht quantifiziert |

### Domain F — Technologie & Innovation (5)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| F22 | — | open_innovation | yaml-only | -1.2 | nicht in Band 4; YAML seit Commit 6bc312e |
| F23 | FORSCHUNGS-PRIORISIERUNG | tech_transfer | band4-canonical | -0.9 | ⚠️ YAML-Tag-Drift (`tech_transfer` ≠ Band 4 Name) |
| F24 | TECH-TRANSFER | (nicht in YAML) | band4-canonical | n/a | YAML hat F24 nicht; CO2-Wirkung nicht quantifiziert |
| F25 | OPEN-SOURCE-INFRASTRUKTUR | (nicht in YAML) | band4-canonical | n/a | YAML hat F25 nicht; CO2-Wirkung nicht quantifiziert |
| F26 | INNOVATION-BESCHLEUNIGUNG | (nicht in YAML) | band4-canonical | n/a | YAML hat F26 nicht; CO2-Wirkung nicht quantifiziert |

### Domain G — Monitoring & Kontrolle (3)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| G27 | MESS-INFRASTRUKTUR | mrv_system | band4-canonical | -0.3 | konsistent (MRV ≈ Mess-Infrastruktur) |
| G28 | — | ki_monitoring | yaml-only | -0.2 | nicht in Band 4; YAML seit Commit 6bc312e |
| G29 | — | blockchain_tracking | yaml-only | -0.1 | nicht in Band 4; YAML seit Commit 6bc312e |

### Domain H — Meta-Framework & Finanzierung (3)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| H30 | FINANZIERUNGS-MECHANISMEN | finanzierung | band4-canonical | -0.3 | konsistent |
| H31 | REGULIERUNGS-FRAMEWORK | regulierung | band4-canonical | -0.2 | konsistent |
| H32 | GLOBALE KOORDINATION | koordination | band4-canonical | 0.0 | konsistent |

### Domain I — Mobilität (2)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| I33 | — (in eigenem File) | kreislauf_auto | stub | -1.0 | STUB-File `Kreislauf-Auto/Konzept_Kreislauf-Auto.md`; nominell in 6D-A zu Band 4 hinzugefügt, aber nicht im File |
| I34 | — (in eigenem File) | kreislauf_lnf | stub | -0.3 | STUB-File `Kreislauf-LNF/STUB_I34_Kreislauf_LNF.md` |

### Domain J — Konstruktion (1)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| J01 | — (in eigenem File) | kreislauf_gebaeude | stub | -3.0 | STUB-File `Kreislauf-Gebaeude/STUB_J01_Kreislauf_Gebaeude.md` |

### Community-Integrations (5, außerhalb A-J)

| ID | Name (Registry) | Status | CO2 Gt/yr | Decision Date | Quelle |
|---|---|---|---:|---|---|
| C-2026-001 | Photovoltaik-basierte Wasserdesinfektion | community-integration | n/a | 2026-01-22 | `06_CANON/04_Band4_Community_Integrations.md` |
| C-2026-003 | Dezentrale Regenwasser-Speicherung (Silos) | community-integration | n/a | 2026-01-22 | `06_CANON/04_Band4_Community_Integrations.md` |
| C-2026-004 | Regenwasser-Speicherung mit Schwimmersystemen | community-integration | n/a | 2026-01-22 | `06_CANON/04_Band4_Community_Integrations.md` |
| C-2026-007 | Globale Energie-Effizienz als Querschnittsprinzip | community-integration | 0.0 (overlap C11-C14) | 2026-04-18 | `06_CANON/04_Band4_Community_Integrations.md` |
| C-2026-008 | Präzisionsfermentation + Hanf-Kaskade | community-integration | -3.0 | 2026-04-18 | `06_CANON/04_Band4_Community_Integrations.md` |

---

## Aggregierte Zahlen (kanonisch)

| Wert | Anzahl | Anmerkung |
|---|---:|---|
| **n_band4_canonical** | 30 | A01-A06, B07-B10, C11-C14, D15-D18, E19-E22, F23-F26, G27, H30-H32 |
| **n_stub** | 3 | I33, I34, J01 |
| **n_yaml_only** | 5 | B11, B12, F22, G28, G29 (echte Hebel laut DEC_2026-05-09 Q1=(a)) |
| **n_communities_integrated** | 5 | C-2026-001/003/004/007/008 |
| **n_total_kanonisch** | **43** | Hebel-Katalog v1.0 |
| **n_yaml_quantified** | 35 | YAML SSOT (34 A-J + 1 Community) — **Subset** des Katalogs |
| CO2-Reduktion (YAML, hart) | -58.0 Gt/yr | aus `co2_master.yaml gesamt.reduktion_hart` |

---

## Bekannte Drifts (Phase 6E nach Phase-6D-Abschluss)

1. **A03-A06 YAML-Tag-Drift** — Tags `transparenz/partizipation/konfliktloesung/kompetenz` widersprechen Band 4 Namen (Risikoabschätzung/Szenarien-Vergleich/Pilotprojekt-Framework/Skalierungs-Protokoll). Mögliche Erklärung: YAML wurde vor Band 4 v4.2 Konsolidierung erstellt. Auflösung: YAML-Tags umbenennen, CO2-Werte verifizieren.

2. **B09/B10 inhaltliche Drift** — YAML-Tags (`wasserstoff`, `ccs`) referenzieren ANDERE Hebel als Band 4-Inhalte (`Materialfluss-Steuerung`, `Abfall-zu-Ressource`). Möglicherweise: YAML hat alte B09=Wasserstoff/B10=CCS-Konzeption, Band 4 v4.2 hat finale B09=Materialfluss/B10=Abfall-zu-Ressource. Auflösung: User-Wissen erforderlich, welche CO2-Werte zu welchen Hebeln gehören.

3. **E20/E21/F23 YAML-Tag-Drift** — analog A03-A06.

4. **YAML-only Hebel (B11, B12, F22, G28, G29)** — Aufnahme in Band 4 v4.3 als eigene Sub-Phase. Inhaltliche Beschreibungen (Detail-Texte) zu schreiben.

5. **Band 4-only Hebel (E22, F24, F25, F26)** — CO2-Werte erheben oder explizit als "non-quantified" markieren. Bei Aufnahme in YAML: Q2-Konvention `co2_impact: 0` vermeiden (siehe DEC_2026-05-09).

6. **STUB-Hebel (I33, I34, J01)** — Aufnahme in Band 4 v4.3 als eigene Sub-Phase, basierend auf STUB-Files in `Kreislauf-Auto/`, `Kreislauf-LNF/`, `Kreislauf-Gebaeude/`.

---

## Cross-References

- **Band 4 v4.2 (Detail-Beschreibungen):** `06_CANON/04_Band4_Anwendungen_v4.2.md`
- **YAML CO2 SSOT:** `20_CANON/data/co2_master.yaml`
- **MASTER_INDEX (Übersichts-Tabelle):** `08_INDEX/MASTER_INDEX_ANWENDUNGEN.md` (Sync gegen diesen Katalog in Folge-Commit)
- **Community-Beschreibungen:** `06_CANON/04_Band4_Community_Integrations.md`
- **Community-Registry (CSV):** `08_INDEX/community_registry.csv`
- **STUB-Files:** `Kreislauf-Auto/Konzept_Kreislauf-Auto.md`, `Kreislauf-LNF/STUB_I34_Kreislauf_LNF.md`, `Kreislauf-Gebaeude/STUB_J01_Kreislauf_Gebaeude.md`
- **Decision-Doc:** `01_STRATEGIE/DECISIONS/DEC_2026-05-09_hebel_set_canonical.md`

---

## Versions-History

**v1.0 (2026-05-09):**
- Initial Release
- Konsoliert SET-Drift zwischen Band 4 / YAML / MASTER_INDEX
- Erstellt in Phase 6D-D.4 als Resolution von G4-Block
- 43 Hebel-Einträge: 30 band4-canonical + 3 stub + 5 yaml-only + 5 community-integration
- 6 Drift-Items für Phase 6E dokumentiert
