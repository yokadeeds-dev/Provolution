# Nature Climate Change - Peer Review Erwartungen
**Basierend auf Journal Guidelines & typischen Reviewer-Kommentaren**

> **STATUS:** INTERNAL — Vorbereitungs-Notizen. Das Nature-Climate-Change-Ziel wurde **abgelöst** (tatsächlich eingereicht bei Earth System Governance, 2026-04-19). Zählungen hier (30 Anwendungen, Domains A–H) sind Vor-Kanon-Stand. Aktuell & autoritativ: [`canon/STATUS.md`](../canon/STATUS.md).

---

## 1. SCIENTIFIC NOVELTY & SIGNIFICANCE

### Was Reviewer prüfen:
- **Neuartigkeit:** Gibt es bereits ähnliche Multi-Impact Frameworks?
- **Advance over prior work:** Was ist besser als z.B. IPCC, Project Drawdown?
- **Significance:** Ist -64.5 Gt CO₂eq/Jahr realistic und impactful genug?

### Unsere Stärken:
✅ Erste systematische Integration von 6 Dimensionen (GHG, Environmental, Social, Energy, Governance, Pathways)
✅ SEC-Prinzip als mathematische Grundlage (neuartig)
✅ Empirische Validierung: r=0.94 über 180+ Implementierungen
✅ Vollständiges Beispiel (H01) mit Implementation-Plan

### Potenzielle Reviewer-Fragen:
❓ "Wie unterscheidet sich dies von IPCC Mitigation Pathways?"
   → ANTWORT: IPCC = Szenarien, wir = konkrete Anwendungen mit Implementierungsdetails
   
❓ "Warum ist euer Framework besser als bestehende Frameworks?"
   → ANTWORT: Multi-dimensional (nicht nur CO₂), SEC-validiert, empirisch getestet
   
❓ "Ist -64.5 Gt realistisch erreichbar?"
   → ANTWORT: Ja, mit Skalierung + konservative Annahmen dokumentiert

---

## 2. METHODOLOGY RIGOR

### Was Reviewer prüfen:
- **GHG Accounting:** GHG Protocol compliant?
- **Data Quality:** Tier 1/2/3 klar getrennt?
- **Uncertainty:** Monte Carlo korrekt angewendet?
- **Baseline:** Credible counterfactual scenario?
- **Double-counting:** Vermieden?

### Unsere Stärken:
✅ GHG Protocol Corporate Standard konform
✅ IPCC AR6 Guidelines integriert
✅ Scope 1/2/3 explizit definiert + Systemgrenzen-Diagramm
✅ Emissionsfaktoren mit Quellen + Jahr
✅ Monte Carlo Unsicherheit: ±25%
✅ IPCC Tier System dokumentiert
✅ Hierarchical Allocation gegen Double-Counting

### Potenzielle Reviewer-Fragen:
❓ "Wie habt ihr Scope 3 Kategorien 4, 5, 11, 12 quantifiziert?"
   → ANTWORT: METHODOLOGY_CO2_ASSESSMENT.md Kapitel 3.3, mit Quellen
   
❓ "Warum ±25% Unsicherheit? Zu niedrig?"
   → ANTWORT: Monte Carlo über 3 Parameter-Typen, konservativ nach IPCC Tier 2
   
❓ "H01 Baseline plausibel? Könnte optimistisch sein?"
   → ANTWORT: Baseline = konventionelle Praxis dokumentiert, konservative Annahmen

---

## 3. DATA TRANSPARENCY & REPRODUCIBILITY

### Was Reviewer prüfen:
- **Open Data:** Sind Rohdaten verfügbar?
- **Code/Scripts:** Können Berechnungen nachvollzogen werden?
- **Methods Detail:** Kann jemand H01 replizieren?

### Unsere Stärken:
✅ Alle Daten in YAML (impact_master.yaml, co2_master.yaml)
✅ Build-System öffentlich (build_impact_references.py)
✅ JSON Schema für Standardisierung (PROJECT_IMPACT_SCHEMA.json)
✅ H01 mit allen Berechnungsschritten (1,391 Zeilen)
✅ CC0 License (maximale Offenheit)
✅ GitHub Repository öffentlich

### Potenzielle Reviewer-Fragen:
❓ "Können wir die Berechnungen verifizieren?"
   → ANTWORT: Ja, alle Formeln in METHODOLOGY, Daten in YAML, H01 als Worked Example
   
❓ "Wie wurden die 180+ Implementierungen validiert?"
   → ANTWORT: Korrelationsanalyse dokumentiert, aber Details fehlen noch
   
❓ "Wo sind die Rohdaten für die Korrelation r=0.94?"
   → ⚠️  LÜCKE: Wir haben nur aggregierte Werte, nicht die 180 Einzelprojekte

---

## 4. STATISTICAL ANALYSIS

### Was Reviewer prüfen:
- **Sample Size:** N=180 ausreichend für r=0.94?
- **Correlation vs Causation:** Wurde verwechselt?
- **Confounders:** Kontrolliert?
- **P-values:** Statistisch signifikant?

### Unsere Stärken:
✅ N=180+ ist robust für Korrelation
✅ Konservative Schätzungen dokumentiert
✅ Multiple Validierungsquellen (IPCC, IEA, Drawdown)

### Potenzielle Reviewer-Fragen:
❓ "Was ist der p-value für r=0.94?"
   → ⚠️  LÜCKE: Nicht explizit berechnet
   
❓ "Wie wurden die 180 Projekte ausgewählt? Selection bias?"
   → ⚠️  LÜCKE: Auswahlkriterien nicht dokumentiert
   
❓ "Confidence intervals für die -64.5 Gt?"
   → ANTWORT: ±25% = [-80.6, -48.4] Gt, Monte Carlo basiert

---

## 5. FIGURES & TABLES QUALITY

### Was Reviewer prüfen:
- **Clarity:** Selbsterklärend?
- **Publication Quality:** Mindestens 300 DPI?
- **Captions:** Informativ?
- **Color-blind friendly:** Barrierefreiheit?

### Unsere Stärken:
✅ Systemgrenzen-Diagramm: 300 DPI, klar beschriftet
✅ Tabellen in H01: Comprehensive

### Potenzielle Reviewer-Fragen:
❓ "Fehlt Abbildung: Domain-Breakdown als Sankey?"
   → ⚠️  EMPFEHLUNG: Zusätzliche Visualisierung würde helfen
   
❓ "Fehlt Abbildung: SEC-Score Distribution?"
   → ⚠️  EMPFEHLUNG: Zeigt Qualität der 30 Anwendungen
   
❓ "Fehlt Abbildung: Pathway-Szenarien über Zeit?"
   → ⚠️  EMPFEHLUNG: BAU vs. Provolution Low/Medium/High

---

## 6. IMPACT PATHWAYS PLAUSIBILITY

### Was Reviewer prüfen:
- **Technology Readiness:** Sind die 30 Anwendungen bereits verfügbar?
- **Scaling Barriers:** Dokumentiert?
- **Timeframe:** Bis wann -64.5 Gt erreichbar?
- **Lock-ins:** Adressiert?

### Unsere Stärken:
✅ H01 zeigt Implementation-Ready Projekt
✅ Lock-in Assessment dokumentiert
✅ Transformation Pathways mit 3 Szenarien
✅ Scaling Potential quantifiziert (NRW → Deutschland → Global)

### Potenzielle Reviewer-Fragen:
❓ "Ist H01 repräsentativ für alle 30 Anwendungen?"
   → ⚠️  SCHWÄCHE: Nur 1 Beispiel vollständig dokumentiert
   
❓ "Was ist der zeitliche Horizont? 2030? 2050?"
   → ANTWORT: H01 = 20 Jahre, Framework = 2050 (in Pathways dokumentiert)
   
❓ "Wie werden politische Barrieren adressiert?"
   → ANTWORT: Governance-Dimension, aber könnte detaillierter sein

---

## 7. SOCIAL & EQUITY DIMENSIONS

### Was Reviewer prüfen:
- **Justice:** Sind vulnerable Gruppen geschützt?
- **Distributional Effects:** Wer trägt Kosten? Wer profitiert?
- **FPIC:** Free, Prior, Informed Consent dokumentiert?

### Unsere Stärken:
✅ Equity Score: +0.68 (stark progressiv)
✅ Beneficiary-Analyse: 45% low-income
✅ FPIC in H01 dokumentiert
✅ Co-Benefits quantifiziert (Jobs, Health)

### Potenzielle Reviewer-Fragen:
❓ "Wie wurde Equity Score +0.68 berechnet?"
   → ANTWORT: Formel in impact_master.yaml, aber könnte in Paper klarer erklärt sein
   
❓ "Gibt es Trade-offs zwischen Klima und sozialen Zielen?"
   → ANTWORT: H01 zeigt keine, aber sollte systematisch für alle 30 geprüft werden
   
❓ "Wie wird sichergestellt, dass keine Menschenrechtsverletzungen?"
   → ANTWORT: Governance-Framework mit Red Flags, FPIC

---

## 8. COMPARABILITY & BENCHMARKING

### Was Reviewer prüfen:
- **Vs. IPCC:** Wie vergleicht sich -64.5 Gt mit IPCC Pathways?
- **Vs. Project Drawdown:** -64.5 vs. -58 Gt - warum Unterschied?
- **Vs. IEA Net Zero:** 95% Overlap - was sind die 5%?

### Unsere Stärken:
✅ Externe Validierung dokumentiert (IPCC, IEA, Drawdown)
✅ Konservativ: -15% vs. IPCC
✅ 95% Overlap mit IEA

### Potenzielle Reviewer-Fragen:
❓ "Warum -64.5 Gt höher als Drawdown -58 Gt?"
   → ANTWORT: Wir inkludieren alle Gase (CH₄, N₂O), Drawdown nur CO₂
   
❓ "Ist Provolution kompatibel mit 1.5°C Pathways?"
   → ANTWORT: Ja, Provolution High = 1.5°C kompatibel (dokumentiert)
   
❓ "Wie vergleicht sich SEC mit anderen Multi-Criteria Frameworks?"
   → ⚠️  LÜCKE: Direkter Vergleich mit MCDA, AHP fehlt

---

## 9. LIMITATIONS & CAVEATS

### Was Reviewer prüfen:
- **Acknowledged Limitations:** Transparent über Schwächen?
- **Caveats:** Wo sind größte Unsicherheiten?
- **Future Work:** Was fehlt noch?

### Unsere Stärken:
✅ Unsicherheitsbänder dokumentiert
✅ Datenqualität Tier-System
✅ Leakage berücksichtigt (15% in H01)

### Was wir ergänzen sollten:
⚠️  "Nur 1 von 30 Anwendungen vollständig dokumentiert"
⚠️  "Rebound-Effekte könnten höher sein als 50%"
⚠️  "Politische Umsetzbarkeit nicht quantifiziert"
⚠️  "Biodiversität MSA mit höchster Unsicherheit (±35%)"

---

## 10. LANGUAGE & PRESENTATION

### Was Reviewer prüfen:
- **Clarity:** Verständlich für breites Publikum?
- **Conciseness:** Nature hat strenge Wortlimits!
- **Structure:** Abstract, Methods, Results, Discussion klar getrennt?

### Unsere Herausforderungen:
⚠️  Framework ist komplex (6 Dimensionen, 30 Anwendungen)
⚠️  Viel Methodik-Detail → Supplementary Material nutzen
⚠️  Main Paper: Max 3000 Wörter (Nature Climate Change)

---

## CRITICAL GAPS - Was fehlt noch?

### 🔴 HIGH PRIORITY (vor Submission fixen):

1. **P-value für r=0.94 Korrelation**
   - Benötigt: Statistische Signifikanz-Test
   - Action: Berechnen und dokumentieren

2. **Rohdaten für 180 Validierungen**
   - Benötigt: Liste der Projekte oder aggregierte Anonymisierung
   - Action: Supplementary Table erstellen

3. **Zusätzliche Figures:**
   - Domain-Breakdown (Sankey oder Bar Chart)
   - Pathway-Szenarien (Timeline 2025-2050)
   - SEC-Distribution (Box Plot über 30 Anwendungen)

4. **Limitations Section schreiben**
   - Nur 1/30 Beispiele vollständig
   - Politische Barrieren nicht quantifiziert
   - Rebound-Unsicherheit

### 🟡 MEDIUM PRIORITY (nützlich, aber nicht kritisch):

5. **Direkter MCDA-Vergleich**
   - SEC vs. AHP, TOPSIS, ELECTRE
   - Warum ist SEC besser?

6. **Mehr Beispiele** (mindestens 2-3 weitere)
   - Z.B. C11 (Erneuerbare), D15 (Regen Agriculture)
   - Zeigt Diversität der Anwendungen

7. **Sensitivity Analysis**
   - Was passiert wenn Rebound 70% statt 50%?
   - Was bei pessimistischeren Annahmen?

### 🟢 LOW PRIORITY (nice to have):

8. **Zenodo DOI** für Langzeit-Archivierung
9. **Preprint** (z.B. EarthArxiv) für Community-Feedback
10. **Excel-Template** für andere Forscher

---

## TYPISCHE REVIEWER-KOMMENTARE (aus Nature Papern)

### Major Revision Triggers:
- ❌ "Insufficient statistical rigor" → p-values fehlen
- ❌ "Methods not reproducible" → Code/Daten unklar
- ❌ "Novelty unclear" → Nicht klar abgegrenzt von Prior Work
- ❌ "Figures insufficient" → Zu wenig Visualisierungen
- ❌ "Limitations not discussed" → Fehlende Selbstkritik

### Minor Revision Triggers:
- ⚠️  "Clarify assumptions" → Detaillierter erklären
- ⚠️  "Expand discussion" → Mehr Kontext geben
- ⚠️  "Update references" → Neuere Papers zitieren
- ⚠️  "Improve figure captions" → Mehr Info in Captions

### Rejection Triggers:
- 🚫 "Not novel enough" → Zu ähnlich zu existierendem Work
- 🚫 "Fatal methodological flaw" → Grundlegender Fehler
- 🚫 "Not significant enough" → Impact zu klein
- 🚫 "Out of scope" → Passt nicht zu Journal

---

## UNSER RISIKO-ASSESSMENT

### ✅ STRONG (wenig Risiko):
- Methodological Rigor (GHG Protocol compliant)
- Data Transparency (Open Source)
- Novelty (SEC + Multi-Impact neu)
- Significance (-64.5 Gt ist major)

### ⚠️  MEDIUM (adressierbar):
- Statistical Analysis (p-value fehlt)
- Figures (mehr Visualisierungen nötig)
- Validation Data (180 Projekte nicht dokumentiert)
- Limitations (sollte expliziter sein)

### 🔴 WEAK (könnte kritisiert werden):
- Nur 1 vollständiges Beispiel (H01)
- Kein direkter MCDA-Vergleich
- Politische Umsetzbarkeit nicht quantifiziert
- Biodiversität-Metrik unsicher (±35%)

---

## EMPFOHLENE PRE-SUBMISSION ACTIONS

### Must-Do (1-2 Tage):
1. ✅ P-value für r=0.94 berechnen und dokumentieren
2. ✅ Supplementary Table: 180 Validierungsprojekte (anonymisiert)
3. ✅ 2-3 zusätzliche Figures erstellen
4. ✅ Limitations Section schreiben

### Should-Do (3-5 Tage):
5. ✅ Mindestens 1 weiteres vollständiges Beispiel (z.B. C11)
6. ✅ Sensitivity Analysis durchführen
7. ✅ MCDA-Vergleich ergänzen

### Nice-to-Have (optional):
8. Preprint auf EarthArxiv
9. Zenodo DOI
10. Community-Feedback vor Submission

---

## FAZIT

**Current State:** 
- 70% publication-ready
- Methodik: Excellent
- Daten: Very Good
- Statistik: Needs Work (p-values)
- Figures: Needs More
- Validation: Needs Documentation

**Recommendation:**
Vor Submission 1-2 Wochen investieren für:
- Statistische Tests
- Zusätzliche Figures
- Limitations Section
- Optional: 1-2 weitere Beispiele

**Dann:** Strong Case für Nature Climate Change! 🎯
