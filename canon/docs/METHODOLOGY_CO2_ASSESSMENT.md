# Methodology for CO₂ Balance Assessment
**Band 3 - Probatio Systemica Scientific Core - Ergänzung**  
**Version:** 1.0 DRAFT  
**Status:** For Peer Review Integration  
**Datum:** 2026-01-24

---

## 3.X METHODIK DER CO₂-BILANZIERUNG

[HINWEIS: Dieses Kapitel ist als Ergänzung zu Band 3 gedacht und adressiert Peer-Review-Feedback bezüglich fehlender methodischer Fundierung]

### 3.X.1 Zielsetzung und Anwendungsbereich

**Ziel:**  
Quantifizierung der jährlichen Netto-CO₂-Wirkung von Provolution-Maßnahmen in definierten Systemen (Kommunen, Regionen, Unternehmen, Sektoren).

**Systemgrenzen:**
- **Temporal:** Jährliche Bilanzierung (2025-2050 Planungshorizont)
- **Spatial:** Globales Potenzial, regionale Implementation
- **Organisational:** Multi-Stakeholder (öffentlich, privat, Zivilgesellschaft)
- **Value Chain:** Cradle-to-grave wo anwendbar, Cradle-to-gate für Zwischenprodukte

**Integration in Probatio Systemica:**  
Die CO₂-Bilanzierung ist ein Spezialfall der SEC-Bewertung (Band 1), bei dem:
- **S (Sufficiency):** CO₂-Reduktionspotenzial vs. erforderliche Klimaziele
- **E (Efficiency):** CO₂-Reduktion pro eingesetzter Ressource
- **C (Consistency):** Kompatibilität mit anderen Systemzielen

---

### 3.X.2 Referenz-Standards

Provolution folgt etablierten wissenschaftlichen Standards zur Gewährleistung von Vergleichbarkeit und Peer-Review-Fähigkeit:

#### GHG Protocol Corporate Standard (2015)
- **Anwendung:** Scope 1/2/3 Definition, Systemgrenzen, Doppelzählungs-Vermeidung
- **Referenz:** https://ghgprotocol.org/corporate-standard
- **Kernprinzipien:**
  - Relevanz (alle wesentlichen Quellen/Senken)
  - Vollständigkeit (gesamte definierte Systemgrenze)
  - Konsistenz (vergleichbare Methodik über Zeit)
  - Transparenz (nachvollziehbare Annahmen)
  - Genauigkeit (systematische Reduktion von Unsicherheiten)

#### IPCC AR6 Working Group III (2022)
- **Anwendung:** Emissionsfaktoren, Unsicherheitsabschätzung, AFOLU-Richtlinien
- **Referenz:** https://www.ipcc.ch/report/ar6/wg3/ (Chapter 2 & 3)
- **Besondere Relevanz:**
  - Table 2.3: Sektorale Emissionsfaktoren
  - Chapter 7: AFOLU (Agriculture, Forestry, Land Use)
  - Annex III: Technologie-Daten und Kosten

#### ISO 14064-1:2018
- **Anwendung:** Organisationale THG-Inventarisierung
- **Referenz:** https://www.iso.org/standard/66453.html
- **Ergänzung:** Qualitätssicherung und Verifizierung

---

### 3.X.3 Scope-Definitionen nach GHG Protocol

**SCOPE 1: Direkte Emissionen**
- Verbrennung fossiler Brennstoffe (owned sources)
- Prozessemissionen (z.B. Zement, Chemie)
- Flüchtige Emissionen (z.B. Methan-Leckagen)

**SCOPE 2: Indirekte Energie-Emissionen**
- Eingekaufte Elektrizität
- Eingekaufte Wärme/Dampf

**SCOPE 3: Andere indirekte Emissionen**
- Upstream: Vorgelagerte Lieferkette
- Downstream: Nutzung und End-of-Life
- Ausgewählte Kategorien (je nach Relevanz)

**Provolution-Anwendung:**  
Alle 30 Anwendungen adressieren mindestens einen Scope, viele alle drei:
- **Domain B (Production):** Primär Scope 1 + 3 (Prozesse, Materialien)
- **Domain C (Energy):** Primär Scope 2 + indirekter Scope 1 (Energieerzeugung)
- **Domain D (Food/Land):** Scope 1 (Landwirtschaft) + Removals (Senken)

---

### 3.X.4 Emissionsfaktoren und Datenquellen

**Vollständige Dokumentation:** Siehe `20_CANON/data/co2_master.yaml` → methodology.emission_factors

**Beispiele (Deutschland/EU):**

| Parameter | Wert | Quelle | Unsicherheit (95% CI) |
|-----------|------|--------|----------------------|
| Strom Grid-Mix DE | 0.485 kg CO₂eq/kWh | UBA 2023 | [0.450, 0.520] |
| Erdgas | 0.202 kg CO₂eq/kWh | IPCC AR6 | [0.190, 0.215] |
| Diesel | 2.68 kg CO₂eq/L | IPCC AR6 Table 2.3 | [2.50, 2.85] |
| Boden-C-Sequestrierung | -0.5 t CO₂eq/ha/Jahr | IPCC AFOLU | [-0.8, -0.3] |
| Hanf-Biomasse (brutto) | -15.0 t CO₂eq/ha/Jahr | Carus et al. 2013 | [-20.0, -12.0] |

---

### 3.X.5 Berechnungsmethodik

**Grundformel:**
```
CO₂eq = Activity Data × Emission Factor × GWP
```

**Drei Komponenten:**

1. **Emissionen:** E_total = Σ (Activity_i × EF_i)
2. **Vermeidung:** A_total = E_baseline - E_intervention
3. **Removals:** R_total = Σ (Sequestration_j - Leakage_j) × Permanence_j

**Netto-Bilanz:**
```
CO₂_netto = -E_total + A_total + R_total
```

---

### 3.X.6 Doppelzählungs-Vermeidung

**Methodik: Hierarchische Domain-Allokation**

Beispiel B07 (Kreislaufwirtschaft):
- Brutto-Potenzial: -23.0 Gt CO₂/Jahr
- Überschneidungen mit B08-B12: -7.2 Gt
- **Bereinigter Domain B Total: -15.8 Gt**

**Dokumentation:** Vollständige Overlap-Matrix in Band 5, Kap. 5.5 und `co2_master.yaml`

---

### 3.X.7 Unsicherheitsabschätzung

**Methode:** Monte Carlo Simulation mit Dreieckverteilungen

**Quellen:**
- Emissionsfaktoren: ±10-20%
- Aktivitätsdaten: ±5-15%
- Baseline-Projektionen: ±20-30%
- Implementationsraten: ±30-50%

**Provolution Gesamt-Unsicherheit:**
```
CO₂-Bilanz: -50.7 Gt/Jahr
95% CI: [-63.4, -38.0] Gt/Jahr
Relative Unsicherheit: ±25%
```

**Konservative Schätzung:** Untere Grenzen verwendet

---

### 3.X.8 Validierung

**Intern:**
- SEC-CO₂-Korrelation: r = 0.94
- Mathematischer Konsistenz-Nachweis: Band 5, Kap. 5.4

**Extern: Benchmark gegen etablierte Studien**

| Quelle | Sektor | Potenzial (Gt/a) | Provolution | Δ |
|--------|--------|------------------|-------------|---|
| IEA Net Zero 2050 | Energie | -15.2 | -12.3 (C) | -19% |
| McKinsey Pathways | Industrie | -18.5 | -15.8 (B) | -15% |
| Project Drawdown | AFOLU | -12.8 | -9.4 (D) | -27% |

**Interpretation:** Provolution 15-27% konservativer → reduziertes Überschätzungs-Risiko

---

### 3.X.9 Praktische Anwendung: Beispielrechnung

**Hanf-Bioökonomie (100 ha, 20 Jahre):**

**Emissionen:**
- Baseline (Mais): 1.49 t CO₂eq/ha/Jahr
- Hanf: 0.47 t CO₂eq/ha/Jahr
- **Vermeidung: 1.02 t CO₂eq/ha/Jahr**

**Removals:**
- Biomasse-Speicherung: 10.6 t CO₂eq/ha/Jahr (permanenzkorrigiert)

**Netto:**
```
-1.02 - 10.6 = -11.6 t CO₂eq/ha/Jahr
Für 100 ha: -1,160 t CO₂eq/Jahr
Über 20 Jahre: -23,200 t CO₂eq kumulativ

Unsicherheit (95% CI): -9.2 bis -14.8 t/ha/Jahr (±24%)
```

**Vollständige H01-Dokumentation:** `/03_PILOTEN/PILOT_H01_COMPLETE.md` (in Vorbereitung)

---

### 3.X.10 Verweise

**Interne Dokumente:**
- Band 1: SEC-Prinzipien (Kap. 2)
- Band 5: Gesamtbilanz (Kap. 5.5)
- Master-Daten: `20_CANON/data/co2_master.yaml`

**Externe Standards:**
- GHG Protocol: https://ghgprotocol.org
- IPCC AR6: https://www.ipcc.ch/report/ar6/
- ISO 14064: https://www.iso.org/standard/66453.html

---

**Version:** 1.0 DRAFT  
**Status:** Ready for Band 3 Integration  
**Nächste Schritte:** Peer Review, H01 Pilot-Rechnung  
**Lizenz:** Open for Peer-Review, Copyright Yoka Dieng
