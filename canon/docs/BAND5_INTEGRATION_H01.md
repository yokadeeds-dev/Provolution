# Integration: H01 Hanf-Pilot in Band 5
**Provolution - Gesamtbilanz & Kontrolle**  
**Version:** 1.0 DRAFT  
**Datum:** 2026-01-24

> ⚠️ **SNAPSHOT 2026-01-24 (DRAFT).** Enthält historische Werte: **−50,7 Gt** (aktuell −58,6), **−64,5 Gt** all-GHG (laut `STATUS.md` §2 `PENDING v2.2`), **„30 Anwendungen"** (aktuell 49 Hebel / 11 Domänen / 38 band4-canonical). Autoritativ: [`canon/STATUS.md`](../STATUS.md) + `canon/data/*.yaml`. Nicht als aktuelle Werte zitieren.

---

## BAND 5 INTEGRATION - NEUE ABSCHNITTE

### Kapitel 5.5: Gesamtbilanz aller 30 Anwendungen <!-- HISTORISCH: aktuell 49 Hebel / 11 Domänen, siehe canon/STATUS.md §3 -->

**Bestehend:** CO₂-Bilanz-Tabellen  
**Neu hinzufügen:**

---

#### 5.5.6 Beispielrechnung: H01 Regenerativer Industriehanf (NEU)

**Zweck:** Vollständige Durchrechnung einer Anwendung als Peer-Review-Referenz

**Projekt-Überblick:**
- **ID:** H01 (Pilot) = D17 (Framework-Anwendung)
- **Fläche:** 50 ha (Pilotgröße)
- **Typ:** Landnutzung + Bioökonomie + Carbon Farming
- **Laufzeit:** 20 Jahre

**Vollständige Dokumentation:** `03_PILOTEN/PILOT_H01_COMPLETE.md`

---

##### 5.5.6.1 GHG-Bilanz (detailliert)

**Baseline-Szenario (BAU):**

| Parameter | Menge | Faktor | Emissionen |
|-----------|-------|--------|-----------|
| Diesel | 120 L/ha/Jahr | 2.68 kg CO₂eq/L | 322 kg CO₂eq/ha |
| N-Dünger | 180 kg N/ha | 6.5 kg CO₂eq/kg N | 1,170 kg CO₂eq/ha |
| Pestizide | - | - | 45 kg CO₂eq/ha |
| **Summe** | | | **1,537 kg CO₂eq/ha/Jahr** |
| SOC-Veränderung | | | -50 kg CO₂/ha (leichter Abbau) |
| **Netto Baseline** | | | **1,487 kg CO₂eq/ha/Jahr** |
| **50 ha gesamt** | | | **74.4 t CO₂eq/Jahr** |

**Projektszenario (Hanf):**

| Parameter | Menge | Faktor | Emissionen |
|-----------|-------|--------|-----------|
| Diesel | 80 L/ha | 2.68 kg CO₂eq/L | 214 kg CO₂eq/ha |
| N-Dünger | 40 kg N/ha | 6.5 kg CO₂eq/kg N | 260 kg CO₂eq/ha |
| Pestizide | - | - | 5 kg CO₂eq/ha |
| Verarbeitung | 150 kWh/ha | 0.485 kg CO₂eq/kWh | 73 kg CO₂eq/ha |
| **Summe Emissionen** | | | **552 kg CO₂eq/ha/Jahr** |

**Senken:**

| Senken-Typ | Berechnung | Wert |
|-----------|-----------|------|
| Biomasse-Bindung | 8 t/ha × 0.45 t C/t × 3.67 × 0.8 (Permanenz) | -10,600 kg CO₂/ha |
| SOC-Aufbau | 2.0 t CO₂/ha/Jahr (Tiefwurzler) | -2,000 kg CO₂/ha |
| **Summe Senken** | | **-12,600 kg CO₂/ha/Jahr** |

**Netto-Projektemissionen:**
```
-12,600 + 552 = -12,048 kg CO₂eq/ha/Jahr
Für 50 ha: -602.4 t CO₂eq/Jahr
```

**Substitution (Baustoffe):**
```
400 t Hanf-Dämmmaterial ersetzt:
- 320 t Steinwolle (1,200 kg CO₂eq/t) = -384 t CO₂eq
- 80 t XPS-Schaum (4,500 kg CO₂eq/t) = -360 t CO₂eq
Summe Substitution: -744 t CO₂eq/Jahr
```

**Weitere Treibhausgase:**

| Gas | Baseline | Projekt | Vermeidung | GWP | CO₂eq |
|-----|----------|---------|-----------|-----|-------|
| CH₄ | 12 kg/ha | 2 kg/ha | 10 kg/ha | 28 | 14 t CO₂eq/Jahr |
| N₂O | 1.8 kg/ha | 0.4 kg/ha | 1.4 kg/ha | 265 | 18.6 t CO₂eq/Jahr |

**GESAMT-GHG-BILANZ:**
```yaml
CO₂: -602.4 t/Jahr (inkl. Substitution)
CH₄: -14.0 t CO₂eq/Jahr
N₂O: -18.6 t CO₂eq/Jahr

TOTAL: -635.0 t CO₂eq/Jahr
Pro Hektar: -12.7 t CO₂eq/ha/Jahr

Unsicherheit (95% CI): [-810, -480] t CO₂eq/Jahr (±26%)
```

**Zeitlicher Verlauf:**

| Jahr | GHG-Impact (t CO₂eq) | Begründung |
|------|---------------------|-----------|
| 1 | -320 | Aufbauphase, noch nicht volle Wirkung |
| 3 | -580 | Hanf etabliert |
| 5 | -635 | Volle Wirkung erreicht |
| 10-20 | -635 | Stabil |
| **Kumulativ 20 Jahre** | **-11,890** | |

**Leakage & Adjustierung:**
- Leakage-Faktor: 15% (regional gebundene Kreisläufe)
- Konservativ adjustiert: -540 t CO₂eq/Jahr

---

##### 5.5.6.2 Multi-Impact Bilanz

**Environmental:**

| Dimension | Baseline | Projekt | Veränderung |
|-----------|----------|---------|------------|
| **Wasser** | 500 m³/ha | 250 m³/ha | **-12,500 m³/Jahr** (50 ha) |
| **Nitrat-Auswaschung** | 85 mg/L | 52 mg/L | **-38%** |
| **Pestizid-Einsatz** | 100% | 15% | **-85%** |
| **SOC** | 1.8% | 2.4% (nach 10 J) | **+33%** |
| **Erosion** | 5.8 t/ha | 2.0 t/ha | **-65%** |
| **Biodiversität (MSA)** | 0.42 | 0.54 | **+0.12 (+28%)** |

**Social:**

| Dimension | Wert | Interpretation |
|-----------|------|----------------|
| **Equity Score** | +0.68 | Stark progressiv |
| **Beneficiaries** | 45% untere, 38% mittlere, 17% obere | Gerechte Verteilung |
| **Jobs** | 15 (3 neu, 12 transformiert) | Lokale Beschäftigung |
| **Living Wage** | 85% | Existenzsichernde Löhne |
| **Gesundheit** | €12,000/Jahr | Vermiedene Kosten |
| **Klima-Literacy** | +8% | Bildungs-Effekt |

**Governance:**

| Check | Status | Details |
|-------|--------|---------|
| **FPIC** | ✅ | Alle 5 Landwirte konsultiert |
| **Additionality** | ✅ | Ohne Projekt würde Baseline weiterlaufen |
| **Permanence** | ✅ | Baustoffe 50+ Jahre, SOC langfristig |
| **Leakage** | ✅ | 15% konservativ eingepreist |
| **Double Counting** | ✅ | Klare Attribution, keine Überlappung |

---

##### 5.5.6.3 Ökonomische Bilanz

**Investment & Betrieb:**

| Kategorie | Jahr 0 (CAPEX) | Jahr 1-20 (OPEX/Jahr) |
|-----------|----------------|----------------------|
| Maschinen | €145,000 | €12,000 (Wartung) |
| Infrastruktur | €200,000 | - |
| Planung | €55,000 | €4,000 (Zertifizierung) |
| Working Capital | €50,000 | - |
| Saatgut | - | €20,000 |
| Betriebsmittel | - | €14,000 |
| Arbeit | - | €90,000 |
| Verwaltung | - | €20,000 |
| **SUMME** | **€450,000** | **€160,000** |

**Erlöse:**

| Produktlinie | Menge/Jahr | Preis | Erlös |
|-------------|-----------|-------|-------|
| Hanf-Faser | 300 t | €600/t | €180,000 |
| Hanf-Schäben | 100 t | €400/t | €40,000 |
| Biochar | 15 t | €800/t | €12,000 |
| Carbon Credits | 635 t CO₂eq | €45/t | €28,575 |
| **SUMME** | | | **€260,575** |

**Rentabilität:**

| Metrik | Wert | Interpretation |
|--------|------|----------------|
| EBITDA | €100,575/Jahr | Positiv ab Jahr 1 |
| Payback Period | 4.5 Jahre | Akzeptabel |
| NPV (20 Jahre, 5%) | €804,000 | Stark positiv |
| IRR | 21% | Attraktiv |
| CO₂-Kosten | -€1.59/t CO₂eq | Hocheffizient |

---

##### 5.5.6.4 SEC-Score

**Berechnung:**

| Dimension | Score | Gewichtung | Beitrag |
|-----------|-------|-----------|---------|
| **Sufficiency (S)** | 0.88 | 0.5 | 0.44 |
| **Efficiency (E)** | 0.92 | 0.3 | 0.276 |
| **Consistency (C)** | 0.95 | 0.2 | 0.19 |
| **SEC Total** | **0.90** | | **Exzellent** |

**Sufficiency:** Hohe Wirksamkeit pro Hektar (-12.7 t CO₂eq/ha), signifikantes Skalierungspotenzial

**Efficiency:** 2.94 kg CO₂eq/€ (überdurchschnittlich vs. 2.1 kg Benchmark)

**Consistency:** Hohe SDG-Alignment (SDG 8, 11, 13, 15), keine signifikanten Trade-offs

---

##### 5.5.6.5 Skalierungspotenzial

**Regional (NRW):**
- Geeignete Fläche: 105,000 ha (bei 50% Penetration)
- CO₂-Reduktion: -1.33 Mt CO₂eq/Jahr
- Jobs: 6,300
- Investment: €945 Mio

**National (Deutschland):**
- Geeignete Fläche: 498,000 ha (bei 30% Penetration)
- CO₂-Reduktion: -6.32 Mt CO₂eq/Jahr
- Anteil Landwirtschafts-Ziel: 2.5% (von -38 Mt bis 2030)
- Jobs: 30,000

**Global:**
- Potenzial: 5 Mio ha (bei 10% geeigneter Fläche)
- CO₂-Reduktion: -63.5 Mt CO₂eq/Jahr
- Vergleich Project Drawdown: -58 Mt (ähnlich!)
- Integration in D17: -2.8 Gt global (langfristig)

---

##### 5.5.6.6 Integration in Provolution Framework

**Domain-Zuordnung:**
```yaml
Primary: D17 (Hanf-Ökosystem in D_food_land)
Secondary:
  - B07 (Kreislaufwirtschaft - Reststoff-Nutzung)
  - C11 (Erneuerbare Energie - Biogas-Option)
  - A04 (Partizipation - Genossenschafts-Modell)
```

**Beitrag zu Gesamt-Bilanz:**
```yaml
H01_Pilot (50 ha):
  GHG: -0.000635 Mt CO₂eq/Jahr
  Anteil_D17_global: 0.00002% (Proof-of-Concept)

D17_Skaliert (global):
  GHG: -2.8 Gt CO₂eq/Jahr
  Anteil_Provolution_gesamt: 4.3% (von -64.5 Gt)
```

**Datenfluss:**
```
PILOT_H01_COMPLETE.md
    ↓
EXAMPLE_D17_HANF.json (PROJECT_IMPACT_SCHEMA)
    ↓
impact_master.yaml (D17 Entry)
    ↓
Band 5 Gesamtbilanz-Tabelle
```

---

##### 5.5.6.7 Lessons Learned & Best Practices

**Erfolgsfaktoren:**
1. Genossenschafts-Modell stärkt Ownership
2. Mehrjährige Abnahmeverträge reduzieren Markt-Risiko
3. Carbon Credits als Risikoabsicherung
4. Externe Verifizierung schafft Vertrauen

**Häufige Fehler vermeiden:**
1. Überschätzung Erträge Jahr 1 → Konservative Planung
2. Unterschätzung Verarbeitungs-Komplexität → Partnerschaften
3. Fehlende Markt-Absicherung → Diversifikation
4. Unzureichendes Monitoring → MRV von Anfang an

**Replikations-Template:**
- Übertragbar auf andere Faserpflanzen (Flachs, Brennnessel)
- Anpassung an lokale Klima-Bedingungen
- Genossenschafts-Struktur als Best Practice

---

## BAND 5 - Neue Struktur (erweitert)

```markdown
# Band 5: Provolution - Gesamtbilanz & Kontrolle

## Kapitel 5.1-5.4: [Bestehend]

## Kapitel 5.5: Gesamtbilanz aller 30 Anwendungen

### 5.5.1-5.5.5: [Bestehende CO₂-Tabellen]

### 5.5.6: Beispielrechnung H01 Regenerativer Industriehanf (NEU)
    5.5.6.1 GHG-Bilanz (detailliert)
    5.5.6.2 Multi-Impact Bilanz
    5.5.6.3 Ökonomische Bilanz
    5.5.6.4 SEC-Score
    5.5.6.5 Skalierungspotenzial
    5.5.6.6 Integration in Framework
    5.5.6.7 Lessons Learned

### 5.5.7: Multi-Impact Gesamt-Tabelle (NEU)

| Domain | CO₂ | CH₄ | N₂O | Wasser | Land | Bio | Equity | Jobs |
|--------|-----|-----|-----|--------|------|-----|--------|------|
| A | -8.2 | -0.5 | -0.3 | -50 | +5 | +0.02 | +0.45 | 2M |
| B | -15.8 | -2.8 | -0.8 | -280 | 0 | +0.05 | +0.58 | 12M |
| C | -12.3 | -1.5 | 0 | +45 | 0 | -0.01 | +0.42 | 18M |
| D | -9.4 | -3.2 | -4.8 | -850 | +420 | +0.14 | +0.72 | 8M |
| E-H | -5.0 | -0.2 | -0.2 | -50 | +15 | +0.01 | +0.55 | 2M |
| **TOTAL** | **-50.7** | **-7.5** | **-5.6** | **-1085** | **+420** | **+0.14** | **+0.68** | **42M** |

Einheiten: CO₂/CH₄/N₂O in Gt/Jahr, Wasser in km³/Jahr,  
Land in Mha, Bio = MSA-Verbesserung, Jobs in Millionen

## Kapitel 5.6-5.8: [Bestehend - Kontrolle, Scoring, etc.]
```

---

**Version:** 1.0 DRAFT  
**Status:** Ready for Band 5 Integration  
**Nächste Schritte:**
1. In Band 5 Hauptdokument einfügen (Kapitel 5.5.6)
2. Multi-Impact Tabelle 5.5.7 vervollständigen
3. Cross-Referenzen zu Band 3 (Methodik) aktualisieren

---

**Verweise:**
- Vollständige H01-Dokumentation: `03_PILOTEN/PILOT_H01_COMPLETE.md`
- Impact Schema: `20_CANON/templates/PROJECT_IMPACT_SCHEMA.json`
- Beispiel-Daten: `20_CANON/templates/EXAMPLE_D17_HANF.json`
- Master-Daten: `20_CANON/data/impact_master.yaml`
