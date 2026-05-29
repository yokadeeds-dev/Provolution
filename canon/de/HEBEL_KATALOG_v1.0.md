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

### Domain B — Material/Produktion (7)

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| B07 | KREISLAUFWIRTSCHAFT | kreislaufwirtschaft | band4-canonical | -23.0 | konsistent |
| B08 | BIOPOLYMERE (HANF) | bio_polymere | band4-canonical | -1.5 | konsistent |
| B09 | MATERIALFLUSS-STEUERUNG | materialfluss_steuerung | band4-canonical | -0.5 | ✅ konsistent (v1.5 Drift-Resolution 2026-05-28: Tag wasserstoff/-2.8 → materialfluss_steuerung/-0.5 nach band4-canonical) |
| B10 | ABFALL-ZU-RESSOURCE | abfall_zu_ressource | band4-canonical | -2.0 | ✅ konsistent (v1.5 Drift-Resolution 2026-05-28: Tag ccs/-1.2 → abfall_zu_ressource/-2.0 nach band4-canonical) |
| B11 | — | transformation | yaml-only | -1.8 | nicht in Band 4; YAML seit Commit 6bc312e |
| B12 | — | biomasse | yaml-only | -2.5 | nicht in Band 4; YAML seit Commit 6bc312e |
| B13 | LOKALE ON-DEMAND-FERTIGUNG | (noch nicht in YAML) | band4-canonical | -0.2 bis -0.5 | neu 2026-05-27 (aus Lesbare-Form integriert) — YAML-Eintrag ausstehend |

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
| D19 | ALGEN-BIORAFFINERIE | algen_bioraffinerie | band4-canonical | -0.3 | ✅ NEU v1.5 2026-05-28: Promotion Kategorie B → A (SEC 0.83 > 0.82); vollintegriert Band 4 v4.2 §5 D-Domain; D-bleibt-Entscheidung (kategoriell anders als K: Bioreaktor vs Ökosystem-Restoration) |

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
| I33 | KREISLAUF-AUTO | kreislauf_auto | band4-canonical | -1.0 | Promoted 2026-05-28 stub→band4-canonical (Kap. 10 Domäne I in Band 4 v4.2); STUB-File `Kreislauf-Auto/Konzept_Kreislauf-Auto.md` bleibt als ausführliche Konzept-Historie |
| I34 | — (in eigenem File) | kreislauf_lnf | stub | -0.3 | STUB-File `Kreislauf-LNF/STUB_I34_Kreislauf_LNF.md`; Promotion zu band4-canonical analog I33 als Folge-Aufgabe |

### Domain J — Konstruktion (1) · band4-canonical seit 2026-05-29

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| J01 | KREISLAUF-GEBÄUDE | kreislauf_gebaeude | band4-canonical | -3.0 | ✅ v1.5 STUB → band4-canonical: Vollkonzept Band 4 v4.2 KAPITEL 10c mit 13-Sektionen-Format (Embodied-Carbon-Limit + Hempcrete + Hanfbast-Bewehrung + Hanffaser-Dämmung + Material-Pässe); SEC-J 0,93 (PR #13) |

### Domain K — Marine & Küste (4) · neu 2026-05-28

| ID | Band 4 v4.2 Name | YAML Tag | Status | CO2 Gt/yr | Drift-Note |
|---|---|---|---|---:|---|
| K01 | MANGROVEN-WIEDERHERSTELLUNG | mangroven | band4-canonical | -0.75 | ✅ v1.5 STUB → band4-canonical: Vollkonzept Band 4 v4.2 KAPITEL 10b mit 8-Sektionen-Format (~5–10 t CO₂/ha/yr; ~14 Mio ha global heute; Restoration-Potenzial 7–10 Mio ha über 30 Jahre) |
| K02 | SEEGRAS-RESTAURATION | seegras | band4-canonical | -0.35 | ✅ v1.5 STUB → band4-canonical: Vollkonzept Band 4 v4.2 KAPITEL 10b (~2–3 t CO₂/ha/yr; ~30 Mio ha global; Restoration sehr arbeitsintensiv aber realisierbar) |
| K03 | KELP-WÄLDER-WIEDERAUFBAU | kelp | band4-canonical | -0.20 | ✅ v1.5 STUB → band4-canonical: Vollkonzept Band 4 v4.2 KAPITEL 10b (~1–2 t CO₂/ha/yr + Tiefsee-C-Export; massive Verluste Kalifornien/Tasmanien; Seeigel-Ernte als Voraussetzung) |
| K04 | SALZMARSCHEN-SCHUTZ UND RESTORATION | salzmarschen | band4-canonical | -0.20 | ✅ v1.5 STUB → band4-canonical: Vollkonzept Band 4 v4.2 KAPITEL 10b (~6–8 t CO₂/ha/yr — höchste Effizienz pro ha; Schutz > Restoration; UNESCO-Welterbe Wattenmeer als Vorbild) |

**Domain K Total (Stub-Schätzung):** -0.9 bis -2.1 Gt CO₂eq/yr (Mittelwert ~-1.5)

**Querschnitts-Notiz Marine-Wirkung:** Die direkten Marine-Hebel K01–K04 wirken zusammen mit indirekten Effekten anderer Domains auf das Meer:
- B07 Kreislauf + B08 Hanf-Biopolymere → Mikroplastik-Reduktion in Ozeanen
- D15 Regen-LW + D17 Hanf → Pestizid-/Düngerschwemmen-Reduktion → Meeres-Todeszone-Reduktion
- B13 Lokale On-Demand-Fertigung → reduzierte Container-Schifffahrt → weniger Verschmutzung/Lärm
- C11 Erneuerbare → schrumpfende Erdöl-Förderung → weniger Tanker-Spills

Plus verwandter Hebel **D19 Algen-Bioraffinerie** (AUTO_INTEGRATE Kategorie B Kandidat): industriell-Bioreaktor-basiert, deshalb in D-Domain belassen, nicht in K verschoben. Bei Promotion zusätzlich -0.3 bis -0.5 Gt/yr.

**Marine-Domain Reserve-Potenzial bei Voll-Ausbau:** ~-2 bis -3 Gt CO₂eq/yr (inkl. D19), plus qualitative Co-Benefits (Versauerungs-Stopp, biologische Pumpe, Phytoplankton-Stabilisierung — siehe Bilanz-Studie §11).

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
| **n_band4_canonical** | 38 | A01-A06, B07-B10, B13, C11-C14, D15-D19, E19-E22, F23-F26, G27, H30-H32, I33, J01, K01-K04 (v1.5: +D19 +K01-K04 +J01) |
| **n_stub** | 1 | I34 (v1.5: K01-K04 + J01 zu band4-canonical promoted) |
| **n_yaml_only** | 5 | B11, B12, F22, G28, G29 (echte Hebel laut DEC_2026-05-09 Q1=(a)) |
| **n_communities_integrated** | 5 | C-2026-001/003/004/007/008 |
| **n_total_kanonisch** | **49** | Hebel-Katalog v1.5: +D19 (=48+1) |
| **n_domains** | **11** | A–K (Domain K voll-integriert 2026-05-28 v1.5) |
| **n_yaml_quantified** | 36 | YAML SSOT (v1.3: 35+1 mit D19) — **Subset** des Katalogs |
| CO2-Reduktion (YAML, hart) | -58.6 Gt/yr | v1.3 nach B09/B10-Drift-Resolution + D19-Promotion (vorher v1.2 -59.8) |

---

## Bekannte Drifts (Phase 6E nach Phase-6D-Abschluss)

1. **A03-A06 YAML-Tag-Drift** — Tags `transparenz/partizipation/konfliktloesung/kompetenz` widersprechen Band 4 Namen (Risikoabschätzung/Szenarien-Vergleich/Pilotprojekt-Framework/Skalierungs-Protokoll). Mögliche Erklärung: YAML wurde vor Band 4 v4.2 Konsolidierung erstellt. Auflösung: YAML-Tags umbenennen, CO2-Werte verifizieren.

2. **B09/B10 inhaltliche Drift** — ✅ **RESOLVED v1.5 2026-05-28**. Auflösung: YAML auf band4-canonical-Inhalte korrigiert (B09 = materialfluss_steuerung -0.5; B10 = abfall_zu_ressource -2.0). Vormals zugeordnete Wasserstoff (-2.8) und CCS (-1.2) zurückgestellt als separate zukünftige Hebel-Kandidaten — H2 partial in B11_transformation -1.8 abgedeckt (enthält H2-Direktreduktion), CCS bekommt eigenen Slot bei späterer Promotion. Netto-Effekt auf Bilanz: +1.5 Gt (weniger Reduktion) → reduktion_hart -59.8 → -58.6 (kombiniert mit D19 -0.3).

3. **E20/E21/F23 YAML-Tag-Drift** — analog A03-A06.

4. **YAML-only Hebel (B11, B12, F22, G28, G29)** — Aufnahme in Band 4 v4.3 als eigene Sub-Phase. Inhaltliche Beschreibungen (Detail-Texte) zu schreiben.

5. **Band 4-only Hebel (E22, F24, F25, F26)** — CO2-Werte erheben oder explizit als "non-quantified" markieren. Bei Aufnahme in YAML: Q2-Konvention `co2_impact: 0` vermeiden (siehe DEC_2026-05-09).

6. **STUB-Hebel (I33, I34, J01)** — Aufnahme in Band 4 v4.3 als eigene Sub-Phase, basierend auf STUB-Files in `Kreislauf-Auto/`, `Kreislauf-LNF/`, `Kreislauf-Gebaeude/`.

7. **B13 YAML-Eintrag ausstehend (neu 2026-05-27)** — `LOKALE ON-DEMAND-FERTIGUNG` ist in Band 4 v4.2 voll ausgeschrieben (band4-canonical), aber noch nicht in `20_CANON/data/co2_master.yaml` ergänzt. CO2-Wert: -0.2 bis -0.5 Gt/Jahr (Bandbreite, konservativ).

8. **D17a Multiplikator-Aspekt (neu 2026-05-27)** — `Mehrfachernte` ist als Sektion 9 innerhalb des D17-Eintrags dokumentiert, nicht als eigener Hebel. Falls künftig als eigenständiger Slot benötigt, ID D17a reserviert. SEC-Implikation: positive S/E, bedingt C (Boden-Regenerations-Trade-off).

9. **D17b Strategie-Differenzierung (neu 2026-05-27)** — `Faser-/Regen-/Phyto-Gleis` als Anbau-Strategie-Differenzierung in D17 Sektion 10 dokumentiert, nicht als eigener Hebel. ID D17b reserviert. Verlust-Bilanz beim Regen-Gleis: nur 10–30% des Pflanzen-C stabilisiert als Humus, Rest aerob veratmet (für höhere Stabilisierungsraten siehe D16/Biochar). Phyto-Caveat: Biomasse auf kontaminierten Böden muss separat entsorgt werden, sonst kehren Schadstoffe in den Boden zurück.

10. **I33 Promotion stub→band4-canonical (neu 2026-05-28)** — Kreislauf-Auto-Konzept aus Probatio-Systemica-2.0-Analyse voll im Band-4-Format ausgeschrieben in Kapitel 10 "Domäne I — Mobilität" mit 13 Sektionen. Korrigiert gegenüber ursprünglichem STUB: Bausteine sind modular einführbar, nicht physikalisch zwingend voneinander abhängig (Motorsport-Belege: F1/Super Formula/FIA-Crash-Box). Tempolimit und Vmax-Drosselung haben eigenständige Begründungen (Auslegung↔Nutzung, Straftaten-Anreiz, Sicherheit). YAML-Eintrag in `co2_master.yaml` ausstehend.

11. **Band-4-Kapitel-Umnummerierung (2026-05-28)** — Bei I33-Promotion neu eingefügtes "Kapitel 10: Domäne I" hat alte Kapitel 10/11/12 (Integration/Cross-References/Fallbeispiele-Index) zu 11/12/13 verschoben, inkl. Sub-Sektionen 10.x→11.x und 11.x→12.x. Backup vor Umnummerierung: `04_Band4_Anwendungen_v4.2.md.bak_2026-05-28_pre-I33`.

12. **Domain K Marine & Küste neu (2026-05-28)** — ✅ **RESOLVED v1.5 2026-05-28**. STUB-File `Marine-Kueste/STUB_K_Marine_Kueste.md` angelegt; K01-K04 als band4-canonical promoviert, Vollkonzepte in Band 4 v4.2 KAPITEL 10b mit 8-Sektionen-Format (Definition / SEC-Nachweis / Wirkung / Ressourcen / Skalierung+Fallbeispiele / Cross-Refs). Pilot-Projekt-Register angelegt für alle 4 Sub-Hebel. Re-Numbering der nachfolgenden Kapitel in Band 4 v4.3 vorgesehen (pragmatisches Workaround "KAPITEL 10b" vermeidet Cross-Reference-Drift).

13. **PF-Report v1.0.1 externe Methodik-Prüfung CO₂-Bilanz (2026-05-28)** — CO₂-Bilanz-Studie v1.1 durch Probatio-Systemica-Modul der Probatio Familia geprüft. Verdict: TEILBESTANDEN — alle vier kritischen Ebenen E1/E3/E6/E8 bestanden; E4 Datenlage und E7 Skalierung als ⚠️ markiert wegen YAML-Drifts (siehe Drift-Items 1–3), fehlender Monte-Carlo-Unsicherheits-Propagation und ausstehender Sensitivitätsanalyse bei 50 %-Umsetzung. ✅ **E4 und E7 in v1.4/v1.5 adressiert** durch Monte-Carlo-Skript + Stresstest-Szenario S. Dokumentation in `STUDIES/CO2_BILANZ_2026-05-28/PF_REPORT_v1.0.1_2026-05-28.md`.

14. **PF-Report v1.0.1 externe Methodik-Prüfung AUTO-INTEGRATE (2026-05-28 spät)** — Kandidaten-Bündel `08_INDEX/AUTO_INTEGRATE_KANDIDATEN.md` durch Probatio-Systemica-Modul der Probatio Familia geprüft. Verdict: TEILBESTANDEN — alle vier kritischen Ebenen E1/E3/E6/E8 bestanden; drei ⚠️ in nicht-kritischen Ebenen: (E2) G26 Resiliente Städte braucht klarere Adaptation-Wirkungsmetrik (statt CO₂-Reduktion); (E4) SEC-Scores ausstehend bei D17a, B-neu, I35, I36; (E7) B11 Industrielle Transformation H₂-abhängig, Re-Bewertung ~2028 (bereits in Kategorie C dokumentiert). Vollständiger Report: `STUDIES/AUTO_INTEGRATE_AUDIT_2026-05-28/PF_REPORT_v1.0.1_2026-05-28.md`.

**Adressierungs-Status E4 (Stand 2026-05-28 spät-Nacht):**
- ✅ **I35 PS-U-vollberechnet (2026-05-28):** Verdict TRAGFÄHIG, SEC 0,84 (S 0,85 / E 0,90 / C 0,80 / J 0,80) — Promotion-fähig (> 0,82 Schwelle). Report: `STUDIES/AUTO_INTEGRATE_AUDIT_2026-05-28/PS_U_REPORT_I35_2026-05-28.md`
- ⚠️ **I36 PS:FULL-bewertet (2026-05-28):** Verdict TEILBESTANDEN, SEC 0,85-Schätzung bestätigt aber empirische Fundierung (Materialbelastbarkeit + Antriebs-Roadmap) noch ausstehend. **Empfehlung: hinter I34-Promotion zurückstellen.** Report: `STUDIES/AUTO_INTEGRATE_AUDIT_2026-05-28/PS_REPORT_I36_2026-05-28.md`. **Zusatz-Befund:** PS:FULL bewertete neben I36 auch die Gesamt-Roadmap und bestätigte alle vier kritischen Ebenen (E1/E3/E6/E8) — die Integrations-Strategie selbst ist methodisch validiert (über die Einzel-Hebel-Bewertung hinaus).
- ⏳ **D17a + B-neu/B13 zu PS 3.0 Gemini geroutet (2026-05-28):** Routing-Trace `STUDIES/AUTO_INTEGRATE_AUDIT_2026-05-28/PS_3.0_ROUTING_D17a_B13.md`, Rückkanal ausstehend.

15. **PS-U 2.0 SEC-J-Nachrüstung des kompletten Kanons (2026-05-28 spät-Nacht)** — User-PF-Sitzung hat die architektonische Lücke geschlossen: Band 4 v4.2 hatte vor 2026-05-10 (Verankerung der PS-U 2.0 SEC-J-Spec) nur SEC-Werte, kein J. PF-Audit-Sitzung 2026-05-28 (PS-U:STANDARD + PS-U:JUSTICE in Gemini) hat alle Hebel der Domains B, C, D **individuell** mit J-Scores + SEC-J nachgerüstet (13 Hebel kalkuliert) und Domains A, E, F, G, H **batch-bewertet** (Domain-Ø). Verdict: **KANON VOLLSTÄNDIG AUF SEC-J v2.0 AKTUALISIERT** — Gesamt-Ø SEC-J = 0,91; kein J<0,50-Veto ausgelöst; **B09 J=0,72 + C12 J=0,82 als Warnschwellen** dokumentiert mit Implementierungs-Auflagen. **Zentralisiert in:** `canon/data/impact_master.yaml` v2.3 TEIL 6.5 `sec_j_scores`. Vollständiger Audit-Bericht: `studies/EXTERNAL_AUDIT_2026-05-28/PF_SEC-J_NACHRUESTUNG_2026-05-28.md`. **Folge-Sub-Phasen:** Einzelhebel-J-Berechnung für A/E/F/G/H, sowie I33-I36, J01, K01-K04, B11/B12/B13, Kategorie-A-AUTO_INTEGRATE-Kandidaten, Communities. Band 4 §2.SEC-NACHWEIS-Updates für alle 30+ Hebel als eigener Folge-PR.

16. **SECJ_SPEC v1.0 ↔ PS-U 2.0 Spec-Konflikt aufgelöst (2026-05-28 spät-Nacht)** — ✅ **RESOLVED**. ChatGPT-Außenleser-Audit und 4. PF-Report (`SEC-J Multi.md` aus User-Sitzung) haben offengelegt, dass das Repo **zwei nicht-synchrone SEC-J-Spezifikationen** enthielt: (1) `canon/de/SECJ_SPEC_v1.0.md` mit alter Formel `SECJ = 0,40·S + 0,25·E + 0,15·C + 0,20·J` und (2) `canon/de/06_framework_extensions_v2.0_SECJ.md` mit der PS-U 2.0 Erweiterung — `SEC-J(m) = 0,30·S + 0,25·E + 0,30·C + 0,15·J` (STANDARD) und `SEC-J(m, justice) = 0,25·S + 0,15·E + 0,20·C + 0,40·J` (JUSTICE). Die User-PF-Sitzungen nutzten korrekt PS-U 2.0 STANDARD. Auflösung: **SECJ_SPEC_v1.0.md mit DEPRECATED-Markierung** + Verweis auf v2.0 als autoritative Spec; `impact_master.yaml` v2.2 → v2.3 mit `spec_reference` + getrennten `formula_standard` und `formula_justice` Feldern. PR #6/#7-Werte bleiben methodisch korrekt (sie wurden nach PS-U 2.0 STANDARD berechnet). **5. PF-Report (PS:FULL Batch-Domains A/E/F/G/H, 2026-05-28 spät-Nacht):** würdigt diesen Schritt explizit als "Musterbeispiel für E3" (Annahmen-Offenlegung); siehe `studies/EXTERNAL_AUDIT_2026-05-28/PF_BATCH_DOMAINS_AEFGH_2026-05-28.md`.

17. **PF-Batch-Audit Domains A/E/F/G/H ✅ TRAGFÄHIG (2026-05-28 spät-Nacht)** — 5. konvergenter externer Audit der Sitzung. Bestätigt das Batch-Bündel der 19 Hebel aus Governance, Bildung/Soziales, Innovation, Monitoring und Meta-Framework mit allen 8 E-Ebenen ✅ (inkl. alle 4 kritischen). Wichtige methodische Bestätigung: (a) die heute Abend vollzogene Spec-Auflösung (Drift-Item #16) wird als "Musterbeispiel für E3" gewürdigt; (b) die Domain-Architektur als Enabler-Schicht ist systemisch unverzichtbar; (c) **die Batch-Bewertung (Domain-Ø-J statt Einzelhebel-J) ist methodisch konsistent** — Einzelhebel-J-Erweiterung künftiger Folge-Sub-Phasen wird durch die Tragfähigkeit der Batch-Bewertung **nicht** zur Pflicht, sondern zur sukzessiven Vertiefung. Audit-Bericht: `studies/EXTERNAL_AUDIT_2026-05-28/PF_BATCH_DOMAINS_AEFGH_2026-05-28.md`.

18. **PF-Batch-Audit Rest-Hebel I/J/K/B SEC-J berechnet (2026-05-29 mittags)** — 6. konvergenter externer Audit nach Gem-Knowledge-Update (2026-05-28 23:59). PS-U:STANDARD-Batch berechnet SEC-J für I33–I36, J01, K01–K04, B11–B13 (12 Hebel) mit den korrekten Repo-Definitionen. Verdict: **TRAGFÄHIG mit punktuellen Auflagen** — kein J<0,50-Veto; 2 neue Warnschwellen: **B11 J=0,78** (Industrielle H2-Transformation — Just-Transition-Auflage) und **B12 J=0,75** (Nachhaltige Biomasse — Tank-oder-Teller / FPIC-Auflage). I33 Kreislauf-Auto, J01 Kreislauf-Gebäude und K01 Mangroven erreichen SEC-J 0,93 (Spitzenwerte). Konsequenz: **individual_calculated wächst von 13 auf 25 Hebel**; Domain-Ø-J neu: I 0,913 · J 0,93 · K 0,913 · B 0,884 (Vollkalkulation Domain B). Audit-Bericht: `studies/EXTERNAL_AUDIT_2026-05-28/PF_BATCH_RESTHEBEL_SEC-J_2026-05-29.md`. Daten in `canon/data/impact_master.yaml` v2.4 `sec_j_scores`.

19. **B11 Definitions-Korrektur — Hanf-Bio-Reduktionsmittel-Spur wiederhergestellt (PR #14, 2026-05-29 mittags)** — User-Hinweis nach PR #13: die ursprüngliche Provolutions-Planung für B11 enthielt eine Hanf-Bio-Reduktionsmittel-Spur als primären Pfad (Hanf-Biokohle/Pyrolyse als Koks-Ersatz in bestehenden Hochöfen — Drop-in). Diese ist bei der yaml-only-Definition und im PR #13-Audit verloren gegangen. **Industrie-real:** Char Technologies CleanFyre (>85% C-Gehalt, EBC-zertifiziert), Pilotprojekte ArcelorMittal Dofasco + thyssenkrupp 250.000 t/yr ab 2025; EU CBAM macht biogenen Kohlenstoff bis 2030 zwingend. **Methodische Folge:** Drop-in löst das Just-Transition-Problem (PR #13-Warnschwelle J=0,78 entfällt für Pfad A); J steigt erwartet auf ~0,90, SEC-J auf ~0,91. **Status:** B11 in `impact_master.yaml` v2.5 als `pending_re_audit: true` markiert mit `legacy_values_pr13` + `expected_corrected_values`; finale Werte beim nächsten PF-Lauf. Quellen: `studies/SOURCES_2026-05-29/B11_HANF_STAHL_RECHERCHE.md` + `studies/EXTERNAL_AUDIT_2026-05-28/B11_HANF_KORREKTUR_2026-05-29.md`. **Bonus:** J01 Kreislauf-Gebäude (STUB) hat ebenfalls Hanf-Stahl-Bauspur (Hanfbast-Bewehrung BasEcoCrete, Hempcrete 110 kg CO₂/m³ netto-negativ, Hanffaser-Dämmung) — gleiche Quelle liefert Best-Practice für J01-Promotion zu band4-canonical.

20. **J01 Kreislauf-Gebäude Promotion STUB → band4-canonical (PR #15, 2026-05-29 abends)** — ✅ **RESOLVED**. Direkte Folge von PR #14 + PR #13 (J01 SEC-J 0,93 mit S 0,90 / E 0,92 / C 1,00 / J 0,85 bereits validiert). Vollkonzept Band 4 v4.2 KAPITEL 10c mit 13-Sektionen-Format eingefügt zwischen Domain K (10b) und KAPITEL 11. **Hebel-Inhalte:** fünf modulare Bausteine — Embodied-Carbon-Limit + Passivhaus-Standard / Hempcrete (netto-negativ ~110 kg CO₂/m³) / Hanfbast-Bewehrung (BasEcoCrete-Pfad, Beton-CO₂-Reduktion ~64 %) / Hanffaser-Dämmung (U-Wert ~0,038 W/(m·K), -1,6 kg CO₂/kg) / Material-Pässe + Urban Mining. **Skalierungs-Daten** mit konkreten Lieferanten (IsoHemp, Thermo-Hanf, HempFlax, BasEcoCrete, Stora Enso/KLH) und Fallbeispielen (Marks & Spencer Distribution Centre, École Issy-les-Moulineaux, Mjøstårnet, HoHo Wien). **Regulatorischer Anker:** EU EPBD-Recast 2024 (Whole-Life-Carbon-Reporting ab 2030) und FR RE2020 (Embodied-Carbon-Limit gesetzlich seit 2022) als Pilotstaaten-Spur. Aggregate: n_band4_canonical 37 → 38; n_stub 2 → 1 (nur noch I34); §11.4 "J STUB Konstruktion" → "J band4-canonical Konstruktion v1.5"; Hebel im Kanon insgesamt unverändert 49.

---

## SEC-J-Master-Übersicht (PS-U 2.0)

Individuell kalkulierte SEC-J-Werte (Audit 2026-05-28):

| ID | S | E | C | J | SEC-J | Note |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **B07** Kreislauf | 0,95 | 0,92 | 0,92 | 0,90 | **0,93** | |
| **B08** Biopolymere Hanf | 0,92 | 0,87 | 0,92 | 0,85 | **0,90** | Zertifizierungs-Barriere für Kleinbauern beachten |
| **B09** Materialfluss | 0,85 | 0,95 | 0,82 | **0,72** | **0,85** | ⚠️ Warnschwelle J<0,80 — Algorithmisches-Management-Risiko |
| **B10** Abfall-Ressource | 0,93 | 0,90 | 0,90 | 0,88 | **0,91** | |
| **C11** Erneuerbare | 0,95 | 0,95 | 0,92 | 0,85 | **0,93** | |
| **C12** Speicher | 0,88 | 0,90 | 0,90 | 0,82 | **0,88** | ⚠️ Li/Co-Abbau — H31 + Lieferketten-Transparenz zwingend |
| **C13** Smart Grid | 0,90 | 0,93 | 0,90 | 0,88 | **0,90** | |
| **C14** Dezentral | 0,90 | 0,88 | 0,86 | **0,95** | **0,89** | |
| **D15** Regen-LW | 0,93 | 0,92 | 0,91 | 0,90 | **0,92** | |
| **D16** Boden-CO₂ | 0,92 | 0,92 | 0,86 | 0,88 | **0,90** | G27-Monitoring der Carbon-Payments zwingend |
| **D17** Hanf-Anbau | 0,95 | 0,93 | 0,91 | 0,92 | **0,93** | |
| **D18** Urbane LW | 0,85 | 0,82 | 0,92 | **0,94** | **0,88** | |
| **D19** Algen-Bioraffinerie | 0,85 | 0,78 | 0,86 | 0,85 | **0,84** | |

Batch-bewertete Domain-Durchschnitte (Einzelhebel-Berechnung ausstehend):

| Domäne | Ø J | Ø SEC-J | Note |
|---|:---:|:---:|---|
| **A** Governance | 0,92 | 0,92 | A01/A02 demokratisieren Entscheidungs-Zugang |
| **E** Bildung & Soziales | 0,93 | 0,93 | E21 PS-U:JUSTICE J=0,95 als Justice-Anker |
| **F** Technologie | 0,90 | 0,90 | F25 bricht Patentmonopole |
| **G** Monitoring | 0,90 | 0,90 | |
| **H** Meta-Framework | 0,90 | 0,90 | H31 Internalisierung Externalitäten |

**Gesamt-Ø SEC-J: 0,90** (25 individuell + 5 batch) · **J-Veto-Auslösungen: 0** · **J-Warnschwellen <0,80: 4** (B09 J=0,72 · C12 J=0,82 · B11 J=0,78 · B12 J=0,75)

### NEU PR #13: Domain I/J/K + Domain B vollständig (PS-U 2.0 STANDARD, 2026-05-29)

| ID | S | E | C | J | SEC-J | Note |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **I33** Kreislauf-Auto | 0,95 | 0,98 | 0,90 | 0,88 | **0,93** | TCO-Demokratisierung; Reparierbarkeit |
| **I34** Kreislauf-LNF | 0,88 | 0,90 | 1,00 | 0,85 | **0,92** | Schutz Handwerk/Kleinflotten vor Entwertung |
| **I35** Aktive Geschwindigkeits-Regulation | 0,90 | 0,95 | 0,90 | 0,82 | **0,90** | J4 vulnerable Verkehrsteilnehmer (Fußgänger/Radfahrer/Kinder) |
| **I36** Kreislauf-Schwere-Nfz | 0,92 | 0,88 | 0,90 | 0,88 | **0,90** | Leistbarer ÖPNV-Ausbau für finanzschwache Kommunen |
| **J01** Kreislauf-Gebäude | 0,90 | 0,92 | 1,00 | 0,85 | **0,93** | Urban Mining → leistbarer Wohnraum |
| **K01** Mangroven | 0,95 | 0,90 | 0,95 | 0,92 | **0,93** | Küstenschutz Globaler Süden; Fischerei-Einkommen |
| **K02** Seegras | 0,92 | 0,88 | 0,95 | 0,90 | **0,92** | Maritime Kinderstuben → Ernährungssouveränität |
| **K03** Kelp | 0,90 | 0,92 | 0,90 | 0,88 | **0,90** | Dezentrale Aquakultur-Jobs |
| **K04** Salzmarschen | 0,90 | 0,85 | 0,95 | 0,90 | **0,90** | Hochwasserschutz Küsteninfrastruktur |
| **B11** Industrielle Transformation | 0,95 | 0,75 | 0,90 | **0,78** | **0,86** | ⚠️ Warnschwelle — Just-Transition-Auflage |
| **B12** Nachhaltige Biomasse | 0,85 | 0,88 | 0,80 | **0,75** | **0,83** | ⚠️ Warnschwelle — FPIC + Anbauflächen-Ausschluss |
| **B13** Lokale On-Demand-Fertigung | 0,88 | 0,90 | 0,95 | 0,92 | **0,91** | Demokratisiert Produktionsmittel |

**Domain-Ø SEC-J (individuell):** B 0,884 (vollständig 7 Hebel) · C 0,90 · D 0,894 · I 0,913 · J 0,93 · K 0,913

**Pending:** Einzelhebel-Werte innerhalb A/E/F/G/H (Batch tragfähig laut PR #11), F22/F27/G25/G26/G30/H33/E23 (AUTO_INTEGRATE Kategorien A/B), Communities C-2026-001/003/004/007/008

**Formel STANDARD:** `SEC-J(m) = 0,30·S + 0,25·E + 0,30·C + 0,15·J` (PS-U 2.0, für normale Maßnahmen-Audits)
**Formel JUSTICE:** `SEC-J(m, justice) = 0,25·S + 0,15·E + 0,20·C + 0,40·J` (PS-U 2.0, für Gerechtigkeits-fokussierte Audits, z.B. E21)
**J-Veto:** J<0,50 → SEC-J=null · **J-Flag SOZIALE INKONSISTENZ:** J<0,40 → Pflicht-Hinweis · **Warnschwelle:** J<0,80 → Implementierungs-Auflagen
**Quelle (autoritativ):** `canon/de/06_framework_extensions_v2.0_SECJ.md` (PS-U 2.0 Extension)
**Daten-SSoT:** `canon/data/impact_master.yaml` v2.3 TEIL 6.5 + `studies/EXTERNAL_AUDIT_2026-05-28/PF_SEC-J_NACHRUESTUNG_2026-05-28.md`
**Deprecated:** `canon/de/SECJ_SPEC_v1.0.md` (alte Single-Formel 0,40·S + 0,25·E + 0,15·C + 0,20·J)

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

**v1.10 (2026-05-29 abends, Promotion):**
- ✅ **J01 Kreislauf-Gebäude Promotion STUB → band4-canonical** (Drift-Item #20): Vollkonzept in Band 4 v4.2 KAPITEL 10c mit 13-Sektionen-Format. Fünf modulare Bausteine inkl. Hempcrete, Hanfbast-Bewehrung (BasEcoCrete), Hanffaser-Dämmung, Embodied-Carbon-Limit und Material-Pässe. SEC-J 0,93 aus PR #13. Aggregate: n_band4_canonical 37 → 38; n_stub 2 → 1; §11.4 "J STUB Konstruktion" → "J band4-canonical Konstruktion v1.5". Hanf-Recherche aus PR #14 als Quelle für die hanfbasierten Bausteine in J01.

**v1.9 (2026-05-29 mittags, korrigierend):**
- ✅ **B11 Definitions-Korrektur** (Drift-Item #19): Hanf-Bio-Reduktionsmittel-Spur wiederhergestellt nach User-Hinweis. Industrie-Best-Practice dokumentiert (Char Tech, ArcelorMittal, thyssenkrupp). Erwartete SEC-J-Anhebung auf ~0,91; Warnschwelle entfällt für Pfad A.
- impact_master.yaml v2.4 → v2.5 mit B11 `pending_re_audit` + Korrektur-Begründung
- Bonus-Befund: J01 Kreislauf-Gebäude STUB sollte Hanfbast-Bewehrung + Hempcrete + Hanffaser-Dämmung als konkrete Bausteine erhalten

**v1.8 (2026-05-29 mittags):**
- ✅ **PF-Batch-Audit Rest-Hebel I/J/K/B** (Drift-Item #18): 6. konvergenter externer Audit nach Gem-Knowledge-Update. SEC-J für 12 Hebel kalkuliert (I33–I36, J01, K01–K04, B11–B13).
- impact_master.yaml v2.3 → v2.4: individual_calculated 13 → 25 Hebel
- 2 neue Warnschwellen J<0.80: B11 (Just-Transition) + B12 (FPIC) mit Auflagen in implementation_constraints
- HEBEL_KATALOG SEC-J-Master-Übersicht erweitert um Domain I/J/K + vervollständigte Domain B (jetzt alle 7 Hebel individuell)
- Domain-Ø-J neu: I 0,913 · J 0,93 · K 0,913 · B 0,884 (volle 7 Hebel)
- Gesamt-Ø SEC-J: 0,91 → 0,90 (durch 12 neue Werte, B11 0,86 + B12 0,83 ziehen leicht nach unten)
- Pending-Liste reduziert auf A/E/F/G/H-Einzelhebel + AUTO_INTEGRATE-Kategorien + Communities
- Band 4 Header für 6 voll-band4-canonical Hebel umgestellt (B13, I33, K01-K04)

**v1.7 (2026-05-28, spät-Nacht):**
- ✅ **Spec-Konflikt SECJ_SPEC v1.0 vs PS-U 2.0 aufgelöst** (Drift-Item #16): SECJ_SPEC_v1.0.md als DEPRECATED markiert; `06_framework_extensions_v2.0_SECJ.md` ist autoritativ
- impact_master.yaml v2.2 → v2.3 mit korrektem Spec-Verweis + formula_standard + formula_justice
- PR #6/#7-Werte verifiziert als methodisch korrekt nach PS-U 2.0 STANDARD-Modus
- Hinweis in SEC-J-Master-Übersicht: Formeln beide dokumentiert, Modi klar getrennt

**v1.6 (2026-05-28, spät-Nacht):**
- ✅ **PS-U 2.0 SEC-J-Nachrüstung des kompletten Kanons** (Drift-Item #15): User-PF-Sitzung hat die architektonische Lücke (Band 4 v4.2 SEC-only, kein J) geschlossen. 13 Hebel individuell kalkuliert (Domains B/C/D), 5 Domains batch-bewertet (A/E/F/G/H). Werte zentralisiert in `canon/data/impact_master.yaml` v2.2 TEIL 6.5 sec_j_scores.
- Neue SEC-J-Master-Übersichtstabelle in diesem Dokument
- Gesamt-Ø SEC-J = 0,91; kein J<0,50-Veto; B09 J=0,72 + C12 J=0,82 als Warnschwellen mit Implementierungs-Auflagen dokumentiert
- ChatGPT-Außenleser-Audit-Befund "SEC vs SEC-J historische Trennung" damit adressiert

**v1.5 (2026-05-28, spät):**
- ✅ **Drift-Resolution B09/B10** (Drift-Item #2): YAML-Tags `wasserstoff/ccs` → `materialfluss_steuerung/abfall_zu_ressource` mit band4-konformen Werten (B09 -0.5, B10 -2.0). H2/CCS-Werte als zukünftige separate Hebel zurückgestellt
- ✅ **D19 Algen-Bioraffinerie Promotion** Kategorie B → A: vollintegriert als 5. Hebel der D-Domain in Band 4 v4.2 §5 (8-Sektionen-Format, SEC 0.83, CO₂ -0.3 Gt). D-bleibt-Entscheidung (kategoriell anders als K)
- ✅ **K01-K04 Promotion stub→band4-canonical** (Drift-Item #12): Vollkonzepte in Band 4 v4.2 KAPITEL 10b (Mangroven/Seegras/Kelp/Salzmarschen mit 8-Sektionen-Format + Pilot-Projekt-Register)
- Aggregate Änderungen: n_band4_canonical 32 → 37 (+D19 +K01-K04); n_stub 6 → 2 (nur I34, J01); n_total 48 → 49; reduktion_hart -59.8 → -58.6 (B09/B10 +1.5 weniger Reduktion + D19 -0.3 mehr); Domain B Total -16.1 → -14.6; Domain D Total -9.4 → -9.7
- Drift-Items #2 + #12 als RESOLVED markiert

**v1.4 (2026-05-28, abends):**
- Domain K Marine & Küste neu angelegt mit 4 Stub-Hebeln (K01 Mangroven, K02 Seegras, K03 Kelp, K04 Salzmarschen) — systematische Erweiterung um Blue-Carbon-Senken-Ökosysteme
- Domain-Total konservativ -0.9 bis -2.1 Gt/yr; Reserve-Potenzial bis -2 bis -3 Gt/yr mit D19 Algen-Bioraffinerie
- Aggregate: n_stub 2→6, n_total 44→48, n_domains 10→11 (A–K)
- Zwei neue Drift-Items: #12 Domain K angelegt, STUB-File-Anlage ausstehend; #13 PF-Report v1.0.1 externe Methodik-Prüfung mit Verdict TEILBESTANDEN
- Quelle: Bilanz-Studie v1.2 §11 (Ozean-Wechselwirkung) hat Blue-Carbon-Hebel-Klasse als systemische Lücke identifiziert; User-Entscheidung 2026-05-28 zur Domain-K-Einrichtung

**v1.3 (2026-05-28):**
- I33 KREISLAUF-AUTO als band4-canonical promoted (Kapitel 10 Domäne I in Band 4 v4.2 neu eingefügt mit 13 Sektionen)
- Domain-I-Stand: I33 band4-canonical + I34 stub (war zuvor: beide stub)
- Aggregate: n_band4_canonical 31→32, n_stub 3→2 (n_total bleibt 44)
- Kapitel-Umnummerierung Band 4: alte 10/11/12 (Integration/Cross-Refs/Fallbeispiele-Index) → 11/12/13
- Zwei neue Drift-Items (10: I33-Promotion + YAML-Eintrag ausstehend; 11: Umnummerierung mit Backup-Hinweis)
- Workflow-Memorien etabliert: `feedback_hemp_cascade_priority` (Hanf wegen Kaskaden, nicht Material-Eigenschaft), `feedback_provolution_not_status_quo` (Großserien-Status kein Hebel-Kriterium)
- Korrekturen im I33-Konzept: Modularität statt physikalischer Zwingung; Tempolimit/Vmax mit vier eigenständigen Begründungen
- Quelle: Wissenschaftliche Begutachtung im Konzept-Workflow 2026-05-28 (Motorsport-Recherche: Bcomp/F1/Super Formula/F3rst/Ycom-FIA-Crash-Box; UBA-Tempolimit-Studie 2024)

**v1.2 (2026-05-27):**
- D17 Sektion 10 ergänzt: D17b Anbau-Strategie-Differenzierung (Faser-/Regen-/Phyto-Gleis)
- Drift-Item 9 hinzugefügt
- Quelle: Wissenschaftliche Klärung im Lesefassungs-Workflow 2026-05-27 (User-Frage "Zwei Gleise", verfeinert zu Drei-Gleis-Modell)

**v1.1 (2026-05-27):**
- B13 LOKALE ON-DEMAND-FERTIGUNG als neuer band4-canonical Hebel hinzugefügt (Domain B: 6→7 Hebel)
- D17a Mehrfachernte als Sub-Notiz innerhalb D17-Eintrag dokumentiert (kein eigener Hebel)
- n_band4_canonical: 30→31, n_total_kanonisch: 43→44
- 2 neue Drift-Items (B13 YAML-Eintrag ausstehend; D17a-Status)
- Quelle: Lesbare-Form-Erzählarbeit `12_LESBARE_FORM/00_Der_Kern.md`; Perplexity-Dialog 2026-05-27
- Workflow-Prinzip "Kanon vor Lesefassung" etabliert (Memory-Eintrag)

**v1.0 (2026-05-09):**
- Initial Release
- Konsoliert SET-Drift zwischen Band 4 / YAML / MASTER_INDEX
- Erstellt in Phase 6D-D.4 als Resolution von G4-Block
- 43 Hebel-Einträge: 30 band4-canonical + 3 stub + 5 yaml-only + 5 community-integration
- 6 Drift-Items für Phase 6E dokumentiert
