# PROVOLUTION

## Band 5 – Steuerung & Score
### Hebel-Ebene (normativ, zielgerichtet, transformativ)

**Version:** 3.1
**Datum:** 2026-04-27
**Status:** Publication-Ready

> ⚠️ **Hinweis zu Kennzahlen:** Dieser Band enthält historische Headline-Werte (u.a. **−50,7 Gt/Jahr** als „100 % von Ziel"). Der **aktuelle autoritative CO₂-hart-Wert ist −58,6 Gt/Jahr** (`canon/data/co2_master.yaml` v1.5). Für alle gültigen Kennzahlen und das Werte-Glossar gilt [`canon/STATUS.md`](../STATUS.md) als Quelle. Fließtext-Werte hier sind Lesefassung, nicht Wertequelle.

---

## TEIL I: GRUNDLAGEN

### KAPITEL 1: EINFÜHRUNG & POSITIONIERUNG

#### 1.1 Was ist "Steuerung & Score"?

**Steuerung & Score** operationalisiert Probatio Systemica für Provolution.
Während Band 1-3 das mathematische Framework definieren, zeigt Band 5
wie es konkret zur Klimatransformation angewandt wird.

**Definition:**
> "Steuerung & Score ist die systematische Priorisierung, Allokation und
> Kontrolle aller kanonischen Provolution-Hebel (n, dynamisch wachsend),
> basierend auf SEC-Scores, mit dem Ziel der Kipppunkt-Kompensation bis 2035."

#### 1.2 Abgrenzung zu anderen Bändern

**Band 2 (Entscheidungskarte) vs. Band 5 (Steuerung):**

| Aspekt | Band 2 (Framework) | Band 5 (Anwendung) |
|--------|-------------------|-------------------|
| Ebene | Probatio Systemica | Provolution |
| Charakter | Neutral, deskriptiv | Normativ, zielgerichtet |
| Gewichtung | α=β=γ=1/3 | S=0.40, E=0.25, C=0.15, J=0.20 |
| Ziele | Keine | Kipppunkt-Kompensation |
| Kontext | Universal | Klimakrise |

**Analogie:**
- Band 2 = Schachregeln (wie Figuren ziehen)
- Band 5 = Gewinnstrategie (welche Züge führen zu Matt)

#### 1.3 Struktur dieses Bandes

**Teil I (Kap. 1-2):** Grundlagen & SEC-J-Score-System
**Teil II (Kap. 3-5):** Steuerung (Priorisierung, Allokation, Roadmap)
**Teil III (Kap. 6-8):** Monitoring & Korrektur
**Teil IV (Kap. 9-11):** Skalierung & Governance
**Teil V (Kap. 12-13):** Anwendung (Szenarien, Checklisten)

**Zielgruppen-spezifisches Lesen:**
- **Entscheider:** Kap. 1-3, 9-10 (Strategie)
- **Praktiker:** Kap. 4-5, 12-13 (Implementation)
- **Wissenschaftler:** Kap. 2, 6-8 (Methodik)

#### 1.4 Normative Anpassungen

**Warum S=0.40 und J=0.20 (Sufficiency und Justice priorisiert)?**

Die Klimakrise ist **zeitkritisch** und **gerechtigkeitspflichtig**. Kipppunkte nähern sich,
während ungerechte Maßnahmen gesellschaftlichen Widerstand erzeugen.
Daher wird **Wirksamkeit (S=0.40)** am höchsten gewichtet; **Gerechtigkeit (J=0.20)**
erhält als J-Veto-Dimension absolute Sperrwirkung: J < 0.50 → Maßnahme nicht zulässig,
unabhängig von S/E/C.

**Beispiel:**
Maßnahme A: S=0.95, E=0.70, C=1.0, J=0.80 (progressiv)
Maßnahme B: S=0.75, E=0.95, C=1.0, J=0.40 → **J-Veto** (regressiv)

Provolution (Band 5): SEC-J_A = 0.40·0.95 + 0.25·0.70 + 0.15·1.0 + 0.20·0.80 = **0.87**
Provolution (Band 5): SEC-J_B = **null** (J-Veto: J < 0.50 → nicht zulässig)

**Transparenz:** Diese Wertentscheidung ist explizit und diskutierbar.
Spec: `06_CANON/SECJ_SPEC_v1.0.md`

---

### KAPITEL 2: SEC-J-SCORE-SYSTEM (ERWEITERT)

#### 2.1 Score-Formel detailliert

```
SEC-J-Score(M) = 0.40·S(M) + 0.25·E(M) + 0.15·C(M) + 0.20·J(M)

J-Veto: Wenn J(M) < 0.50 → SEC-J-Score(M) = null  (Maßnahme nicht zulässig)

Wo:
S(M) = min( W(M) / W_min , 1.0 )    (Sufficiency: Wirkung vs. Minimum)

E(M) = Ressourcen-Optimalität, berechnet auf eine von zwei Weisen:

  (E-I)  Budget-Auslastung — wenn Maßnahme ein Budget-Limit hat:
           E(M) = 1 − R(M) / R_max(M)
         mit R(M) = Ressourcenverbrauch, R_max(M) = zugeteiltes Maximum.
         Gültig für: A-, H-Domäne (Governance-Apps mit Budget-Cap).

  (E-II) Portfolio-Normalisierung — für Impact-Maßnahmen (CO₂-Reduktion):
           cost_rate(M)       = R(M) / W(M)                          [€/Gt CO₂eq]
           cost_rate_benchmark = Median( cost_rate(M_i) ) über Portfolio
           E(M) = max( 0, min( 1, 1 − cost_rate(M) / cost_rate_benchmark ) )
         → Maßnahmen, die **günstiger als Portfolio-Median** sind, erhalten E > 0.
         → Extremwert-Clipping [0,1] verhindert Überschlagen bei Best-Performern.
         Gültig für: B-, C-, D-, I-, J-Domäne (Impact-Apps).

  Auswahl zwischen E-I und E-II wird pro Maßnahme-Typ festgelegt und im
  Scoring-Template dokumentiert.

C(M) = 1 wenn konsistent     (Consistency: Keine Widersprüche)
       0 sonst

J(M) = ( equity_score(M) + 1 ) / 2           (Justice: Verteilungsgerechtigkeit)
     equity_score(M) ∈ [−1, +1] aus Multi-Impact Dim. 3 (Social & Equity)
     J(M) ∈ [0, 1]
     J < 0.50 → J-Veto (progressive Mindestanforderung, unabhängig von S/E/C)
```

**Gewichte (SEC-J v1.0):** S=0.40, E=0.25, C=0.15, J=0.20
**Spec:** `06_CANON/SECJ_SPEC_v1.0.md`

**Parameter:**
- **W(M):** Tatsächliche Wirkung der Maßnahme M (Gt CO₂eq/Jahr)
- **W_min:** Minimal erforderliche Wirkung (Provolution-Zielanteil der Domäne)
- **R(M):** Ressourcenverbrauch von M (€/Jahr)
- **R_max(M):** Maximal zugeteilte Ressourcen (nur für E-I)
- **cost_rate(M):** Kosten pro Gt vermiedenem CO₂eq (für E-II)
- **cost_rate_benchmark:** Portfolio-Median der cost_rate — kalibriert quartalsweise
  (siehe Kapitel 2.4 Dynamische Anpassung)
  **Aktuell (Q1/2026): 26,0 €/t CO₂ (10y kumuliert)** — Median-App D16 (CO₂-Senken Boden).
  Quelle: `20_CANON/data/impact_master.yaml → portfolio_benchmark.current`.
  Kalibrierungs-Prozess: `20_CANON/docs/RUNBOOK_PORTFOLIO_BENCHMARK.md`.

#### 2.2 Berechnungsbeispiele

**Beispiel 1: B07 (Kreislaufwirtschaft) SEC-J = 0.92**

**Wirkung (S):**
- CO₂-Reduktion: 23 Gt/Jahr (tatsächlich)
- W_min: 24.2 Gt/Jahr (Provolution-Zielanteil für B07-Domäne)
- S(B07) = min(23/24.2, 1.0) = 0.95

**Effizienz (E — Portfolio-Normalisierung, E-II):**
- Ressourcen: R(B07) = €156 Mio/Jahr
- CO₂-Wirkung: W(B07) = 23 Gt/Jahr
- cost_rate(B07) = 156 / 23 ≈ **€6.78 Mio/Gt CO₂eq**
- cost_rate_benchmark (Portfolio-Median, Stand 2026-Q1) ≈ €67.8 Mio/Gt CO₂eq
- E(B07) = max(0, min(1, 1 − 6.78/67.8)) = max(0, min(1, 1 − 0.10)) = **0.90**
  → B07 ist ~10× günstiger als Portfolio-Median → hohe Kosteneffizienz-Score.

**Konsistenz (C):**
- Keine systemischen Widersprüche
- Kreislauf verstärkt andere Maßnahmen
- C(B07) = 1.0

**Gerechtigkeit (J):**
- equity_score(B07) = +0.68 (progressiv: Nutzen zu 42% bei niedrigen Einkommen)
- J(B07) = (0.68 + 1) / 2 = **0.84** (kein Veto)

**Gesamt:**
SEC-J(B07) = 0.40·0.95 + 0.25·0.90 + 0.15·1.0 + 0.20·0.84
           = 0.380 + 0.225 + 0.150 + 0.168 = **0.923 ≈ 0.92**

**Beispiel 2: C11 (Erneuerbare Integration) SEC-J = 0.94**

- S = 0.95 (15 Gt CO₂/Jahr, W_min = 12 Gt)
- E = 0.92 (sehr ressourceneffizient)
- C = 1.0 (keine Widersprüche)
- J = 0.90 (Beispielwert, equity_score = +0.80)
- SEC-J = 0.40·0.95 + 0.25·0.92 + 0.15·1.0 + 0.20·0.90
        = 0.380 + 0.230 + 0.150 + 0.180 = **0.940 ≈ 0.94**

**Beispiel 3: A01 (SEC-Priorisierung) SEC-J = 0.99**

- S = 1.0 (ermöglicht alle anderen Maßnahmen)
- E = 0.95 (minimaler Ressourcenverbrauch)
- C = 1.0 (konsistent per Definition)
- J = 1.0 (maximale Gerechtigkeit: universeller Zugang)
- SEC-J = 0.40·1.0 + 0.25·0.95 + 0.15·1.0 + 0.20·1.0
        = 0.400 + 0.238 + 0.150 + 0.200 = **0.988 ≈ 0.99**

#### 2.3 Score-Kategorien

| Score-Bereich | Kategorie | Empfehlung |
|--------------|-----------|------------|
| 0.90-1.00 | ⭐⭐⭐ Exzellent | Sofortige Implementierung |
| 0.80-0.89 | ⭐⭐ Sehr gut | Implementierung empfohlen |
| 0.70-0.79 | ⭐ Gut | Implementierung nach Ressourcen |
| 0.60-0.69 | ⚠️ Ausreichend | Verbesserung erforderlich |
| <0.60 | ❌ Unzureichend | Ablehnung oder Neukonzeption |

**Provolution-Status (n Hebel — wächst via SEC-Schwelle):**
- Durchschnitt: **0.914** (Exzellent)
- Minimum: 0.88 (Sehr gut)
- Maximum: 0.99 (Exzellent)

#### 2.4 Dynamische Anpassung

SEC-Scores sind **nicht statisch**. Sie werden re-evaluiert bei:

**Trigger für Re-Evaluation:**
1. Neue Technologie verfügbar (E verbessert sich)
2. Geänderte Rahmenbedingungen (Regulation, Preise)
3. Unerwartete Nebenwirkungen (C verschlechtert sich)
4. Bessere Daten verfügbar (S präzisiert sich)

**Beispiel:**
C11 (Erneuerbare) - Batterie-Technologie verbessert sich
- Vor: E = 0.85 (Speicher teuer)
- Nach: E = 0.92 (Speicher 40% günstiger)
- SEC steigt von 0.90 auf 0.94

**Frequenz:** Quartalsweise Review aller n kanonischen Hebel

**Spezifischer Prozess Portfolio-Benchmark (E-II):**
Die Kalibrierung des `cost_rate_benchmark` aus der E-II-Formel (Kapitel 2.1) ist ein eigenständiger quartalsweiser Prozess, dokumentiert in [`20_CANON/docs/RUNBOOK_PORTFOLIO_BENCHMARK.md`](../20_CANON/docs/RUNBOOK_PORTFOLIO_BENCHMARK.md). Der jeweils aktuelle Benchmark wird in `20_CANON/data/impact_master.yaml` unter `portfolio_benchmark.current` geführt.

---

## TEIL II: STEUERUNG

### KAPITEL 3: PRIORISIERUNGS-ALGORITHMUS

#### 3.1 Grundprinzip

**Naive Strategie:** Höchster SEC-Score zuerst
**Problem:** Ignoriert Abhängigkeiten

**Intelligente Strategie:**
1. Sort by SEC-Score (descending)
2. Identify dependencies
3. Topological sort (dependencies first)
4. Group by phases (feasibility)

#### 3.2 Dependency Graph

```
A01 (SEC-Priorisierung) → ENABLES → Alle anderen
  ↓
H30 (Finanzierung) → ENABLES → B, C, D, E, F
  ↓
G27 (Monitoring) → ENABLES → Feedback für alle
  ↓
High-Impact Trio:
  B07 (Kreislaufwirtschaft)
  C11 (Erneuerbare)
  D17 (Hanf-Ökosystem)
  ↓
Restliche Hebel
```

**Enabler (müssen zuerst):**
- A01: Ohne Priorisierungs-Tool → Chaos
- H30: Ohne Finanzierung → Keine Umsetzung
- G27: Ohne Monitoring → Blind flying

#### 3.3 Priorisierungs-Matrix

| Rank | ID | Name | J | SEC-J | Dependencies | Phase |
|------|----|-----------------------|------|-------|-------------|-------|
| 1 | A01 | SEC-Priorisierung | — | — | - | 1 |
| 2 | H30 | Finanzierung | — | — | A01 | 1 |
| 3 | G27 | Monitoring | — | — | A01 | 1 |
| 4 | B07 | Kreislaufwirtschaft | 0.84 | 0.92 | H30, G27 | 2 |
| 5 | C11 | Erneuerbare | — | — | H30, G27 | 2 |
| 6 | D17 | Hanf-Ökosystem | — | — | H30, G27 | 2 |
| 7 | B08 | Biopolymere | — | — | B07, D17 | 2 |
| 8 | A02 | Entscheidungskarte | — | — | A01 | 2 |
| 9 | C12 | Energie-Speicher | — | — | C11 | 2 |
| 10 | D15 | Regenerative Landwirt. | — | — | - | 2 |
| ... | ... | ... | ... | ... | ... | ... |

*J = — bedeutet: Bewertung ausstehend (Band-4-Schritt). SEC-J setzt vollständige J-Bewertung voraus.*

#### 3.4 Phasenmodell

**Phase 1: Foundation (Jahr 0-2)**
**Ziel:** Betriebssystem installieren
**Hebel:** A01, H30, G27 (Enabler)
**Budget:** €450 Mio/Jahr (10% von Gesamt)
**KPIs:**
- A01 operativ und genutzt
- H30 mobilisiert €4.5 Bio/Jahr
- G27 liefert Real-Time-Daten

**Phase 2: Demonstration (Jahr 2-5)**
**Ziel:** High-Impact-Hebel skalieren
**Hebel:** B07, C11, D17 + weitere 7
**Budget:** €2 Bio/Jahr (45% von Gesamt)
**KPIs:**
- CO₂-Reduktion: 25 Gt/Jahr erreicht
- 10 Pilot-Regionen erfolgreich
- Ökonomischer Break-Even erkennbar

**Phase 3: Scale-Up (Jahr 5-10)**
**Ziel:** Globale Adaption, Tipping Point
**Hebel:** Alle n (kanonisch qualifizierten)
**Budget:** €4.5 Bio/Jahr (100%)
**KPIs:**
- CO₂-Reduktion: 50.7 Gt/Jahr erreicht
- Kipppunkte kompensiert
- Selbstverstärkende Dynamik

#### 3.5 Algorithmus-Pseudocode

```python
def prioritize(applications):
    # 0. J-Veto-Filter: Maßnahmen mit J < 0.50 ausschließen
    eligible = [a for a in applications
                if a.justice_score is None or a.justice_score >= 0.50]
    
    # 1. Sort by SEC-J-Score
    sorted_apps = sorted(eligible,
                        key=lambda x: x.secj_score or 0,
                        reverse=True)
    
    # 2. Build dependency graph
    graph = build_dependency_graph(sorted_apps)
    
    # 3. Topological sort
    priority_order = topological_sort(graph)
    
    # 4. Group by phases
    phase1 = [a for a in priority_order if a.is_enabler]
    phase2 = [a for a in priority_order if a.is_high_impact]
    phase3 = [a for a in priority_order if a not in phase1+phase2]
    
    return {
        'phase1': phase1,
        'phase2': phase2,
        'phase3': phase3
    }
```

---

### KAPITEL 4: ALLOKATIONS-MODELL

#### 4.1 Ressourcen-Typen

**Finanzen:** €4.5 Bio/Jahr (siehe H30)
**Personal:** Geschätzt 500.000 FTE weltweit
**Infrastruktur:** Physische Assets (Fabriken, Netze, Sensoren)
**Zeit:** Projektlaufzeiten, Meilensteine

#### 4.2 Allokations-Formel

```
Budget(M) = Basis · SEC(M) · Complexity(M) · Impact(M)

Wo:
Basis = Total Budget / n
     = €4.5 Bio / n   (n = Anzahl kanonisch qualifizierter Hebel, SEC ≥ 0.82)

SEC(M) = Score der Maßnahme
Complexity(M) = 1.0 (einfach) bis 3.0 (sehr komplex)
Impact(M) = CO₂-Potential / Max CO₂-Potential
```

#### 4.3 Beispiel-Allokation

**B07 (Kreislaufwirtschaft):**
- SEC = 0.95
- Complexity = 2.5 (viele Stakeholder, Infrastruktur)
- Impact = 0.45 (23 Gt von 50.7 Gt)
- Budget = €150 Mio · 0.95 · 2.5 · 0.45 = **€160 Mio/Jahr**

**C11 (Erneuerbare):**
- SEC = 0.95
- Complexity = 2.0 (technisch, aber etabliert)
- Impact = 0.30 (15 Gt von 50.7 Gt)
- Budget = €150 Mio · 0.95 · 2.0 · 0.30 = **€86 Mio/Jahr**

**A01 (Priorisierung):**
- SEC = 0.99
- Complexity = 1.2 (Software, Tool)
- Impact = 1.0 (enabled alle anderen)
- Budget = €150 Mio · 0.99 · 1.2 · 1.0 = **€178 Mio/Jahr**

#### 4.4 Re-Allokation

**Trigger:**
- Quartalsweise Performance Review
- Over-/Underperformance >20%
- Externe Schocks (neue Tech, Regulation)

**Mechanismus:**
- Underperformer → Budget reduzieren oder Support erhöhen
- Overperformer → Budget erhöhen, schneller skalieren
- Failed → Budget streichen, Ressourcen umverteilen

---

### KAPITEL 5: ROADMAP-IMPLEMENTIERUNG

#### 5.1 Phase 1: Foundation (Jahr 0-2)

**Priorität 1: A01 (SEC-Priorisierung)**
- Monat 1-3: Tool-Design
- Monat 4-6: Development
- Monat 7-12: Pilot mit 5 Regionen
- Monat 13-18: Roll-Out
- Monat 19-24: Training & Adoption

**Priorität 2: H30 (Finanzierung)**
- Monat 1-6: Finanzierungs-Modell designen
- Monat 7-12: Erste Tranche mobilisieren (€500 Mio)
- Monat 13-18: Skalierung (€2 Bio)
- Monat 19-24: Full Scale (€4.5 Bio/Jahr)

**Priorität 3: G27 (Monitoring)**
- Monat 1-6: Sensor-Netzwerk Design
- Monat 7-12: Pilot-Deployment (10 Standorte)
- Monat 13-18: Dashboard Development
- Monat 19-24: Global-Deployment (1000 Standorte)

**Meilensteine:**
- M1 (Monat 6): A01 Tool Beta-Release
- M2 (Monat 12): H30 erste €500 Mio mobilisiert
- M3 (Monat 18): G27 Dashboard operativ
- M4 (Monat 24): Foundation komplett

#### 5.2 Phase 2: Demonstration (Jahr 2-5)

**High-Impact Trio:**

**B07 (Kreislaufwirtschaft):**
- Jahr 2: Pilot in 3 Städten (Hamburg, Rotterdam, Singapur)
- Jahr 3: Ausweitung auf 10 Städte
- Jahr 4: Ausweitung auf 50 Städte
- Jahr 5: 100 Städte, 10 Gt CO₂/Jahr Reduktion

**C11 (Erneuerbare):**
- Jahr 2: 5 Regions-Netze dekarbonisiert
- Jahr 3: 20 Regions-Netze
- Jahr 4: 50 Regions-Netze
- Jahr 5: 100 Regions-Netze, 8 Gt CO₂/Jahr

**D17 (Hanf-Ökosystem):**
- Jahr 2: 1 Mio Hektar Anbaufläche
- Jahr 3: 10 Mio Hektar
- Jahr 4: 40 Mio Hektar
- Jahr 5: 80 Mio Hektar, 4 Gt CO₂/Jahr

#### 5.3 Phase 3: Scale-Up (Jahr 5-10)

**Ziel:** Alle n kanonischen Hebel global implementiert

**Meilensteine:**
- M8 (Jahr 7): 50% globale Adaption erreicht
- M9 (Jahr 9): Tipping Point (Selbstverstärkung)
- M10 (Jahr 10): Kipppunkte kompensiert

**KPIs Jahr 10:**
- CO₂-Reduktion: 50.7 Gt/Jahr (100% von Ziel) <!-- HISTORISCH: aktueller autoritativer Wert −58,6 Gt/Jahr, siehe canon/STATUS.md §2 -->
- SEC-Durchschnitt: ≥0.85 (stabil)
- Kosten-Nutzen: Positiv (ROI >1.0)
- Soziale Akzeptanz: >70%

---

## TEIL III: MONITORING & KORREKTUR

**Monitoring & Korrektur (Kapitel 6-8):**
- **6. Mess-Infrastruktur:** Primäre und sekundäre Metriken auf globaler, domänen-, hebel- und projektbezogener Ebene. Dashboard-Spezifikation mit Executive, Hebel- und Geographic Views. Datenquellen von Remote Sensing bis Citizen Science. 
- **7. Feedback-Loops & Korrektur:** Wöchentliche, monatliche und quartalsweise Feedback-Zyklen. Detaillierter Korrektur-Algorithmus mit Ursachenanalyse und Maßnahmen von Zielanpassung bis Terminierung. Eskalations-Hierarchie bis hin zu externen Expertenreviews.
- **8. Risikomanagement:** Identifizierung von technischen, ökonomischen, politischen, sozialen und ökologischen Risiken. Top-5-Risiken mit Eintrittswahrscheinlichkeiten, Auswirkungen und Mitigationsstrategien. Risiko-Monitoring über Dashboards und Contingency-Pläne.

---

## TEIL IV: SKALIERUNG & GOVERNANCE

### KAPITEL 9: SKALIERUNGS-STRATEGIE

#### 9.1 Lokal → Global

**Stufe 1: Pilot (1-3 Orte, Jahr 1-2)**
- Test unter kontrollierten Bedingungen
- Lernen, Anpassen, Iterieren
- Budget: Klein (€10-50 Mio)
- Beispiel: B07 in Hamburg, Rotterdam, Singapur

**Stufe 2: Regional (10-50 Orte, Jahr 2-5)**
- Ausweitung auf diverse Kontexte
- Kulturelle Anpassungen
- Budget: Mittel (€100-500 Mio)
- Beispiel: B07 in EU, Nordamerika, Ostasien

**Stufe 3: Global (>100 Orte, Jahr 5-10)**
- Standards etabliert
- Ökonomischer Vorteil erkennbar
- Selbstverstärkende Dynamik
- Budget: Groß (€1+ Bio)
- Beispiel: B07 weltweit Standard

#### 9.2 Diffusions-Mechanismus

**Rogers Diffusion of Innovation:**

1. **Innovators (2.5%):** Risikofreudige Pioniere
   - Jahr 1-2: Erste Pilots
   - Motivation: Neugier, Prestige

2. **Early Adopters (13.5%):** Meinungsführer
   - Jahr 2-4: Erste Erfolge sichtbar
   - Motivation: Wettbewerbsvorteil

3. **Early Majority (34%):** Pragmatiker
   - Jahr 4-7: ROI bewiesen
   - Motivation: Ökonomischer Vorteil

4. **Late Majority (34%):** Skeptiker
   - Jahr 7-9: Peer Pressure
   - Motivation: Nicht zurückfallen

5. **Laggards (16%):** Konservative
   - Jahr 9+: Regulation erzwingt
   - Motivation: Compliance

#### 9.3 Tipping Point

**Kritische Masse: ~15-20% Marktadoption**

**Ab Tipping Point:**
- Selbstverstärkende Dynamik
- Nicht-Adaption wird teurer als Adaption
- Standards setzen sich durch
- "New Normal"

**Beschleuniger:**
- Netzwerk-Effekte (mehr Nutzer → mehr Wert)
- Skaleneffekte (höhere Produktion → niedrigere Kosten)
- Soziale Normen ("alle machen es")

#### 9.4 Kompetitive Kooperation

**Konzept:**
- Städte/Regionen konkurrieren um beste Implementation
- ABER: Teilen von Best Practices
- "Race to the top" statt "race to the bottom"

**Beispiel:**
- Hamburg erreicht 70% Recycling-Rate (B07)
- Rotterdam will übertreffen → 75%
- Hamburg teilt Methoden → Rotterdam lernt
- Hamburg verbessert auf 80%
- → Alle gewinnen

**Mechanismen:**
- Rankings (public Scoreboards)
- Awards (Best Practice Recognition)
- Konferenzen (Knowledge Sharing)

---

### KAPITEL 10: GOVERNANCE-STRUKTUR

#### 10.1 Multi-Level-Governance

**Level 1: Global (UN, Klima-Konventionen)**
- Rolle: Ziele setzen, Standards definieren
- Beispiel: "50.7 Gt CO₂-Reduktion bis 2035"
- KEINE operative Kontrolle

**Level 2: National/Regional (Regierungen)**
- Rolle: Gesetzgebung, Incentives, Budget
- Beispiel: CO₂-Steuer, Subventionen für B07
- Umsetzung der globalen Ziele

**Level 3: Lokal (Städte, Gemeinden)**
- Rolle: Implementation, Pilot-Projekte
- Beispiel: Hamburg implementiert B07
- Operative Ebene

**Level 4: Zivilgesellschaft (NGOs, Bürger)**
- Rolle: Monitoring, Druck, Innovation
- Beispiel: NGOs überwachen Fortschritt
- Bottom-Up-Kraft

#### 10.2 Entscheidungs-Prozesse

**NICHT:**
- Top-down Diktatur (ineffizient, undemokratisch)
- Bottom-up Anarchie (Chaos, keine Koordination)

**SONDERN:**
**Polyzentrisches System**
- Multiple Entscheidungs-Zentren
- Koordiniert aber nicht zentralisiert
- Subsidiarität (Entscheidung auf niedrigster sinnvoller Ebene)

#### 10.3 Rollen & Verantwortlichkeiten

**Wissenschaft:**
- SEC-Scores berechnen und validieren
- Monitoring-Daten interpretieren
- Neue Methoden entwickeln
- KEINE politischen Entscheidungen

**Politik:**
- Rahmenbedingungen schaffen
- Budget allokieren
- Konflikte moderieren
- KEINE technischen Detailentscheidungen

**Wirtschaft:**
- Implementieren und skalieren
- Innovation treiben
- Finanzierung bereitstellen
- KEINE regulatorischen Entscheidungen

**Zivilgesellschaft:**
- Monitoring und Feedback
- Druck auf alle Ebenen
- Grassroots-Innovation
- KEINE exekutive Macht

#### 10.4 Konflikt-Resolution

**Bei widersprüchlichen Interessen:**

**Schritt 1: Daten**
- SEC-Scores als objektive Basis
- CO₂-Reduktion messbar
- Kosten-Nutzen transparent

**Schritt 2: Dialog**
- Alle Stakeholder anhören
- Win-Win suchen

**Schritt 3: Kompromiss**
- Falls kein Win-Win: Kompromiss
- Transparente Begründung

**Schritt 4: Entscheidung**
- Menschen entscheiden (nicht Algorithmus)
- SEC-Score informiert, diktiert nicht

---

### KAPITEL 11: INTERNATIONALE KOORDINATION

#### 11.1 Warum Koordination?

**Klimawandel ist global:**
- CO₂ in Hamburg = CO₂ in Singapur (atmosphärisch)
- Keine lokale Lösung allein ausreichend
- Race to the bottom vermeiden (Trittbrettfahrer)

#### 11.2 Koordinations-Mechanismen

**Standards (ISO-style):**
- Gemeinsame SEC-Score-Berechnung
- Monitoring-Protokolle
- Reporting-Formate

**Best Practice Sharing:**
- Konferenzen, Workshops
- Online-Plattformen
- Peer-Learning

**Finanzierungs-Pools:**
- Gemeinsame Fonds für Entwicklungsländer
- Risk-Sharing-Mechanismen
- Technology Transfer Financing

**Technologie-Transfer:**
- Open-Source wo möglich
- Lizenz-Agreements
- Capacity Building

#### 11.3 Existierende Strukturen nutzen

**NICHT neue Institutionen schaffen (Overhead vermeiden)**

**STATTDESSEN bestehende erweitern:**
- Paris Agreement Framework
- SDGs (Sustainable Development Goals)
- Regional Trade Agreements
- IPCC (Intergovernmental Panel on Climate Change)

#### 11.4 Provolution als Add-On

**Provolution ersetzt NICHT:**
- UN-Prozesse
- Nationale Klimapolitik
- Bestehende Initiativen

**Provolution ERGÄNZT:**
- Systematische Methodik (SEC)
- Konkrete Hebel (n, dynamisch)
- Mess- und Steuerungssystem

**Metapher:** Provolution ist das Betriebssystem für Klimapolitik

---

## TEIL V: ANWENDUNG

### KAPITEL 12: BEISPIEL-SZENARIEN

#### 12.1 Szenario 1: Stadt Hamburg implementiert B07

**Kontext:**
- Einwohner: 1.9 Millionen
- Abfall: 850.000 Tonnen/Jahr
- Aktuelle Recycling-Rate: 42%
- Ziel: 80% Kreislaufwirtschaft

**Schritt 1: Analyse (Monat 1-3)**
- Abfallströme kartieren (Residual, Bio, Papier, Glas, Metall)
- Potentiale identifizieren: 650.000 t recyclebar
- SEC-Score berechnen (lokal): 0.91
- Budget schätzen: €120 Mio (einmalig) + €20 Mio/Jahr

**Schritt 2: Planung (Monat 4-6)**
- Infrastruktur-Design: 5 Sortier-Anlagen, 20 Recycling-Hubs
- Stakeholder-Engagement: Bürger, Industrie, Politik
- Kommunikations-Kampagne: "Hamburg wird zirkulär"
- Pilot-Gebiet: Altona (280.000 Einwohner)

**Schritt 3: Pilot (Monat 7-18)**
- Monat 7-9: Infrastruktur bauen (2 Sortier-Anlagen)
- Monat 10-12: Soft Launch (50% Altona)
- Monat 13-15: Full Roll-Out Altona
- Monat 16-18: Evaluation

**Pilot-Ergebnisse:**
- Recycling-Rate: 68% (Ziel: 80%)
- CO₂-Reduktion: 95.000 t/Jahr
- Bürgerzufriedenheit: 78%
- Lessons Learned: Bessere Sortierung nötig

**Schritt 4: Scale-Up (Monat 19-36)**
- Monat 19-24: Ausweitung auf ganze Stadt (Phase 1: Nord)
- Monat 25-30: Phase 2: Süd + Ost
- Monat 31-36: Phase 3: West + Zentrum

**Scale-Up-Ergebnisse (Jahr 3):**
- Recycling-Rate: 72% (stadtw eit)
- CO₂-Reduktion: 400.000 t/Jahr
- Jobs geschaffen: 2.500
- ROI: Break-Even Jahr 8

**Schritt 5: Evaluation & Verbreitung (Monat 37-42)**
- Best Practices dokumentieren
- Anderen Städten zur Verfügung stellen
- Hamburg als Vorbild (Konferenzen, Besuche)

---

#### 12.2 Szenario 2: Land Costa Rica implementiert C11

**Kontext:**
- Einwohner: 5 Millionen
- Strom: Bereits 99% erneuerbar (Hydro, Geothermie)
- Problem: Transport noch 85% fossil
- Ziel: 100% Erneuerbare Gesamt-Energie

**Herausforderungen:**
1. Transport-Sektor dekarbonisieren
2. Saisonale Volatilität (Regen/Trockenzeit)
3. Speicher-Bedarf (Batterie + H₂)

**Lösung (Jahr 1-5):**

**Jahr 1:**
- 100 MW Batterie-Speicher installieren
- 5.000 E-Busse beschaffen
- Ladeinfrastruktur (1.000 Stationen)

**Jahr 2:**
- 200 MW Batterie-Speicher (gesamt 300 MW)
- 10.000 E-Pkw Anreiz-Programm
- Smart Grid Roll-Out (50% Netz)

**Jahr 3:**
- 500 MW Batterie-Speicher (gesamt 800 MW)
- E-Mobilität: 30% Flotte
- Smart Grid: 100% Netz

**Jahr 4:**
- H₂-Pilotprojekt (schwere Trucks)
- E-Mobilität: 60% Flotte
- Export Expertise (Lateinamerika)

**Jahr 5:**
- E-Mobilität: 85% Flotte
- Gesamt-Erneuerbare: 95%
- CO₂-Reduktion: 2 Mio t/Jahr
- Costa Rica als Vorbild

**Kosten & Nutzen:**
- Investition: €3 Bio (über 5 Jahre)
- ROI: Positiv ab Jahr 7 (Öl-Import-Ersparnis)
- Co-Benefits: Luftqualität, Gesundheit, Jobs

---

#### 12.3 Szenario 3: Globale Koordination D17 (Hanf)

**Kontext:**
- Hanf: Schnellste CO₂-Senke (1 Hektar = 50 t CO₂/Jahr)
- Zusatznutzen: Baumaterial, Textilien, Papier
- Potential: 100 Mio Hektar weltweit
- Ziel: 5 Gt CO₂/Jahr Bindung
- **Struktureller Scope-3-Effekt:** Hanf ist in über 40 Ländern (gemäßigte und subtropische Zonen) anbaubar — bei globaler Adoption wird Rohstoff regional verfügbar. Konventionelle Baumwolle-Importwege (Usbekistan/Indien/China → Europa, ~8.000–12.000 km Seetransport) entfallen strukturell. Zusätzliche Einsparung: ~0.4 kg CO₂ pro kg Faser, bei 10 Mt/Jahr globaler Faserproduktion ~3–5 Mt CO₂/Jahr — als Scope-3-Minderung, nicht in der Anbau-Bilanz enthalten.

**Implementation (50 Länder koordiniert):**

**Jahr 1-2: Pilot (10 Länder)**
- 1 Mio Hektar Anbau
- Technologie-Transfer (EU → Afrika, Asien)
- Erste Verarbeitungs-Anlagen

**Jahr 2-5: Scale-Up (30 Länder)**
- 40 Mio Hektar Anbau
- Industrielle Verwertung etabliert
- Markt für Hanf-Baustoffe wächst

**Jahr 5-10: Global (50+ Länder)**
- 80 Mio Hektar Anbau
- 4 Gt CO₂/Jahr gebunden
- Hanf-Produkte Standard (20% Baumarkt)

**Koordinations-Mechanismen:**
- UN-koordinierter Standard (Anbau-Praktiken)
- Finanzierung via H30 (€200 Mio/Jahr Tech Transfer)
- Best Practice Sharing (Konferenzen)
- Gemeinsame Forschung (Züchtung, Verarbeitung)

**Ergebnis Jahr 10:**
- 80 Mio Hektar (80% von Potential)
- 4 Gt CO₂/Jahr (80% von Ziel)
- 5 Mio Jobs geschaffen
- Hanf-Industrie: €50 Bio/Jahr Umsatz

---

### KAPITEL 13: CHECKLISTEN FÜR PRAKTIKER

#### 13.1 Checklist: Neuen Hebel evaluieren

☐ **SEC-J-Score berechnen**
  - S-Wert: Wirkung vs. Minimum
  - E-Wert: Ressourcen-Effizienz
  - C-Wert: Systemische Konsistenz
  - J-Wert: Gerechtigkeit — equity_score aus Multi-Impact Dim. 3 → J = (equity_score + 1) / 2
  - J-Veto prüfen: J < 0.50 → Maßnahme nicht zulässig (unabhängig von S/E/C)

☐ **Dependencies identifizieren**
  - Welche Hebel müssen vorher?
  - Welche Infrastruktur benötigt?

☐ **Budget schätzen**
  - Einmalige Kosten
  - Operative Kosten/Jahr
  - ROI-Timeline

☐ **Risiken bewerten**
  - Top 3 Risiken identifizieren
  - Mitigation-Strategien entwickeln

☐ **Pilot-Region identifizieren**
  - Geeigneter Kontext?
  - Stakeholder-Support?
  - Infrastruktur vorhanden?

☐ **Stakeholder einbinden**
  - Politik, Wirtschaft, Zivilgesellschaft
  - Early Adopters finden

☐ **Monitoring-Plan erstellen**
  - KPIs definieren
  - Mess-Frequenz festlegen
  - Dashboard konfigurieren

☐ **Go/No-Go Entscheidung**
  - J-Veto geprüft? (J ≥ 0.50 Pflicht)
  - SEC-J-Score ≥ 0.70?
  - Budget verfügbar?
  - Stakeholder Support?
  - → GO oder zurück zu Planung

---

#### 13.2 Checklist: Pilot-Projekt starten

☐ **Projekt-Team aufstellen**
  - Projekt-Manager
  - Technische Leads
  - Stakeholder-Manager
  - Monitoring-Analyst

☐ **Budget allokieren**
  - Konto einrichten
  - Freigabe-Prozess definieren
  - Transparenz sicherstellen

☐ **Infrastruktur vorbereiten**
  - Physisch (Gebäude, Anlagen)
  - Digital (Software, Sensoren)

☐ **Baseline-Messung durchführen**
  - Vor-Zustand dokumentieren
  - KPIs messen (T0)

☐ **Kommunikations-Plan**
  - Intern (Team)
  - Extern (Stakeholder, Öffentlichkeit)
  - Krisenkommunikation

☐ **Kick-Off Event**
  - Team-Meeting
  - Stakeholder-Event
  - Presse-Mitteilung

☐ **Monitoring aktivieren**
  - Sensoren online
  - Dashboard live
  - Alerts konfiguriert

☐ **Weekly Reviews etablieren**
  - Jeden Montag 9:00
  - Status, Risiken, Next Steps
  - Dokumentation

---

#### 13.3 Checklist: Scale-Up entscheiden

☐ **Pilot erfolgreich?**
  - Ziele erreicht? (≥80%)
  - KPIs positiv?
  - Stakeholder zufrieden?

☐ **Lessons learned dokumentiert**
  - Was lief gut?
  - Was lief schlecht?
  - Was ändern für Scale-Up?

☐ **ROI positiv?**
  - Break-Even absehbar?
  - Langfristige Wirtschaftlichkeit?

☐ **Stakeholder Support?**
  - Politik unterstützt Ausbau?
  - Wirtschaft investiert?
  - Bürger akzeptieren?

☐ **Budget verfügbar?**
  - Scale-Up-Budget freigegeben?
  - Reserve für Unvorhergesehenes?

☐ **Scale-Up Plan erstellt**
  - Phase 1: 10x (wo, wann, wie)
  - Phase 2: 100x
  - Phase 3: 1000x

☐ **Go/No-Go Entscheidung**
  - Alle Punkte ✓?
  - → GO zu Scale-Up
  - Sonst: Iteration oder Abort

---

## ANHÄNGE

### ANHANG A: SCORE-BERECHNUNGS-TABELLEN

**Alle kanonischen Hebel mit SEC-J-Scores (n aktuell: 35 — wächst via AUTO-INTEGRATE):**

| ID | Name | S | E | C | J | SEC-J | Kategorie |
|----|---------------------------|------|------|------|------|-------|-----------|
| A01 | SEC-Priorisierung | 1.00 | 0.95 | 1.0 | — | — | ⭐⭐⭐ |
| A02 | Entscheidungskarte | 0.92 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| A03 | Risikoabschätzung | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| A04 | Szenario-Planung | 0.90 | 0.88 | 1.0 | — | — | ⭐⭐⭐ |
| A05 | Partizipation | 0.85 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| A06 | Skalierung | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| B07 | Kreislaufwirtschaft | 0.95 | 0.90 | 1.0 | 0.84 | 0.92 | ⭐⭐⭐ |
| B08 | Biopolymere | 0.90 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| B09 | Material-Tracking | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| B10 | Abfall-zu-Ressource | 0.90 | 0.88 | 1.0 | — | — | ⭐⭐⭐ |
| C11 | Erneuerbare Integration | 0.95 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| C12 | Energie-Speicher | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| C13 | Smart Grid | 0.90 | 0.88 | 1.0 | — | — | ⭐⭐⭐ |
| C14 | Dezentrale Erzeugung | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| D15 | Regenerative Landwirt. | 0.85 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| D16 | Boden-CO₂-Senken | 0.88 | 0.88 | 1.0 | — | — | ⭐⭐⭐ |
| D17 | Hanf-Ökosystem | 0.95 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| D18 | Urbane Landwirtschaft | 0.82 | 0.90 | 1.0 | — | — | ⭐⭐ |
| E19 | Bildung & Bewusstsein | 0.80 | 0.95 | 1.0 | — | — | ⭐⭐ |
| E20 | Verhaltens-Nudging | 0.82 | 0.92 | 1.0 | — | — | ⭐⭐ |
| E21 | Gerechtigkeit | 0.85 | 0.88 | 1.0 | — | — | ⭐⭐ |
| E22 | Partizipative Planung | 0.82 | 0.90 | 1.0 | — | — | ⭐⭐ |
| F23 | Forschung & Entwicklung | 0.88 | 0.88 | 1.0 | — | — | ⭐⭐⭐ |
| F24 | Open-Source Innovation | 0.85 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| F25 | Technologie-Transfer | 0.88 | 0.88 | 1.0 | — | — | ⭐⭐⭐ |
| F26 | Patent-Pools | 0.82 | 0.90 | 1.0 | — | — | ⭐⭐ |
| G27 | MRV-System | 0.90 | 0.95 | 1.0 | — | — | ⭐⭐⭐ |
| G28 | KI-Monitoring | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| G29 | Blockchain-Tracking | 0.82 | 0.90 | 1.0 | — | — | ⭐⭐ |
| H30 | Finanzierungs-Mechanismus | 0.95 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| H31 | Regulierungs-Framework | 0.88 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |
| H32 | Globale Koordination | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| I33 | Kreislauf-Auto | 0.95 | 0.98 | 0.90 | — | — | ⭐⭐⭐ |
| I34 | Kreislauf-LNF *(STUB)* | 0.88 | 0.90 | 1.0 | — | — | ⭐⭐⭐ |
| J01 | Kreislauf-Gebäude *(STUB)* | 0.90 | 0.92 | 1.0 | — | — | ⭐⭐⭐ |

**n = 35 (dynamisch) | SEC-J: ausstehend (J-Bewertung Band-4-Schritt) | B07: SEC-J = 0.92 (erste vollständige Bewertung)**

*J = — bedeutet: equity_score noch nicht bewertet. SEC-J = — bedeutet: Berechnung ausstehend bis J gesetzt.*

---

### ANHANG B: ALLOKATIONS-FORMELN

#### B.1 Budget-Formel

```
Budget(M) = Basis · SEC-J(M) · Complexity(M) · Impact(M)

Parameter:
- Basis = Total Budget / Anzahl Maßnahmen
- SEC-J(M) = 0.40·S + 0.25·E + 0.15·C + 0.20·J  (null wenn J-Veto)
- Complexity(M) ∈ [1.0, 3.0]
- Impact(M) = CO₂_Potential(M) / Max_CO₂_Potential
```

#### B.2 ROI-Berechnung

```
ROI = (Benefits - Costs) / Costs

Benefits:
- CO₂-Vermeidungskosten (€/t CO₂)
- Co-Benefits (Gesundheit, Jobs, etc.)

Costs:
- CAPEX (einmalig)
- OPEX (jährlich)
```

#### B.3 Payback-Period

```
Payback = CAPEX / (Annual_Benefits - OPEX)

Beispiel B07:
- CAPEX: €120 Mio
- OPEX: €20 Mio/Jahr
- Benefits: €40 Mio/Jahr
- Payback = 120 / (40 - 20) = 6 Jahre
```

---

### ANHANG C: MONITORING-DASHBOARD-SPEZIFIKATION

#### C.1 Technische Architektur

**Stack:**
- Frontend: React + D3.js (Visualisierung)
- Backend: Python FastAPI
- Database: PostgreSQL + TimescaleDB (Time-Series)
- Real-Time: Apache Kafka
- Hosting: Cloud (AWS/Azure/GCP)

#### C.2 Datenquellen

**API-Integrationen:**
1. Copernicus (Satellitenbilder)
2. IEA (Energie-Daten)
3. WMO (Klima-Daten)
4. Lokale IoT-Sensoren (MQTT)

#### C.3 Update-Frequenz

| Metrik | Frequenz | Latenz |
|-------------------------|----------|--------|
| Kipppunkt-Proxies | Täglich | 24h |
| CO₂-Emissionen (global) | Wöchentlich | 7 Tage |
| SEC-J-Scores | Wöchentlich | Real-Time |
| Budget-Verwendung | Monatlich | 1 Monat |
| Projekt-Status | Wöchentlich | Real-Time |

#### C.4 Visualisierungen

**Dashboard-Komponenten:**
1. **Score-Meter:** SEC-J-Durchschnitt (Gauge)
2. **CO₂-Graph:** Time-Series (Line Chart)
3. **Projekt-Map:** Geographic (Heat Map)
4. **Budget-Pie:** Allokation (Pie Chart)
5. **Risk-Matrix:** Risiko-Status (Matrix)

#### C.5 Alerts

**Trigger:**
- J-Veto ausgelöst (RED — sofortiger Ausschluss)
- SEC-J-Score < 0.70 (RED)
- CO₂-Ziel >10% verfehlt (ORANGE)
- Budget-Überschreitung >20% (ORANGE)
- Kipppunkt-Risiko erhöht (RED)

**Notification:**
- Email an Stakeholder
- SMS bei kritischen Alerts
- Dashboard-Badge

#### C.6 API-Endpunkte

```
GET /api/v1/secj-scores
GET /api/v1/co2-reduction
GET /api/v1/budget-status
GET /api/v1/projects
GET /api/v1/kipppunkte
POST /api/v1/alerts
```

---

## SCHLUSS & CROSS-REFERENZEN

**Framework-Referenzen:**
- Band 1: SEC-Kanon (Prinzipien)
- Band 2: Entscheidungskarte (SEC-Score-Grundlagen)
- Band 3: Scientific Core (Mathematik, Algorithmen)

**Provolution-Referenzen:**
- Band 4: Hebel (n kanonische Maßnahmen, dynamisch)
- MASTERDOKUMENT v2.0 (Gesamt-Überblick)
- GLOSSARY.md (Terminologie)

**Praktische Werkzeuge:**
- provolution_checkliste_anwendung_band_5_sec.md
- G27: Mess-Infrastruktur (Implementation-Details)
- H30: Finanzierungs-Mechanismus (Budget-Details)

---

**Version:** 3.1 | **Status:** Publication-Ready | **Datum:** 2026-04-27 | **SEC-J v1.0 integriert**

**Ende von Band 5 – Provolution Steuerung & Score**

---

## LICENSE

This work is released under:
- **CC0 1.0 Universal** (Public Domain)
- **Open Humanity License** (OHL)

See [LICENSE.md](../LICENSE.md) for full details.

You are free to use, modify, and distribute this work without restriction.

---
