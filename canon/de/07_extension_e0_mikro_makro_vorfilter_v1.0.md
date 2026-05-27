# EXTENSION E0: MIKRO-MAKRO-MASCHINE (VORFILTER)

**Version:** 1.0
**Datum:** 2026-02-04
**Status:** KANONISCH
**Priorität:** HÖCHSTE (vorgeschaltet vor SEC)
**Ursprung:** Entwickelt vor Probatio Systemica, chronologisch älteste Komponente

---

## ZUSAMMENFASSUNG

Die **Mikro-Makro-Maschine** ist der obligatorische **Vorfilter** für alle Klimamaßnahmen, bevor diese in die SEC-Bewertung (Sufficient-Efficient-Consistent) eingehen. Sie prüft, ob eine Maßnahme auf beiden fundamentalen Analyse-Ebenen überhaupt funktioniert.

**Kernprinzip:** Fällt eine Maßnahme bereits bei der Mikro-Makro-Prüfung durch, wird keine SEC-Bewertung durchgeführt → Ressourcenersparnis.

---

## 1. SYSTEMARCHITEKTUR

### 1.1 Position im Provolution-Workflow

```
EINGABE (Klimamaßnahme/Konzept)
              ↓
┌─────────────────────────────────────┐
│  STUFE 0: MIKRO-MAKRO-PRÜFUNG       │
│  ├── Mikroebene (konkrete Wirkung)  │
│  ├── Makroebene (systemische Wirk.) │
│  └── 14 Bewertungskriterien         │
└─────────────────────────────────────┘
              ↓
         BESTANDEN?
         ├── NEIN → ABGELEHNT (Begründung)
         │          Keine weitere Prüfung
         └── JA ↓
┌─────────────────────────────────────┐
│  STUFE 1: SEC-PRÜFUNG               │
│  ├── Sufficient (S ≥ 0.6)           │
│  ├── Efficient (E ≥ 0.5)            │
│  └── Consistent (C ≥ 0.7)           │
└─────────────────────────────────────┘
              ↓
         SEC-SCORE → Aufnahme ins Framework
```

### 1.2 Begründung der Vorschaltung

| Aspekt | Ohne Vorfilter | Mit Vorfilter |
|--------|----------------|---------------|
| Rechenaufwand | SEC für ALLE Maßnahmen | SEC nur für vorgeprüfte |
| Qualität | Viele Fehlbewertungen | Saubere Eingabe |
| Effizienz | Niedrig | Hoch |
| Fehlervermeidung | Systemisch unpassende Maßnahmen können hohe SEC-Scores bekommen | Vorab gefiltert |

---

## 2. MIKROEBENE

### 2.1 Definition

Die **Mikroebene** analysiert die **konkrete, lokale, unmittelbare Wirkung** einer Einzelmaßnahme.

### 2.2 Prüfdimensionen

| Dimension | Prüffrage | Beispiel |
|-----------|-----------|----------|
| **Ressourcen** | Welche Inputs werden benötigt? | Material, Energie, Arbeit |
| **Emissionen** | Welche direkten Outputs entstehen? | CO₂, Abfall, Wärme |
| **Kosten** | Was kostet eine Einzelinstanz? | €/Einheit, Zeitaufwand |
| **Wirkung** | Was bewirkt eine Einzelinstanz? | kg CO₂ gespart, kWh erzeugt |
| **Risiken** | Welche lokalen Risiken bestehen? | Unfälle, Fehlfunktionen |
| **Reversibilität** | Ist die Maßnahme rückgängig machbar? | Ja/Nein/Teilweise |

### 2.3 Mikro-Prüflogik

```
MIKRO_PASS = TRUE wenn:
  (1) Wirkung > 0 (messbar positiv)
  UND (2) Ressourcen verfügbar
  UND (3) Kosten ≤ akzeptabler Schwellenwert
  UND (4) Risiken beherrschbar
```

**Mikro-Durchfallgründe:**
- Keine messbare positive Wirkung
- Benötigte Ressourcen nicht verfügbar
- Kosten prohibitiv hoch
- Unkontrollierbare lokale Risiken

---

## 3. MAKROEBENE

### 3.1 Definition

Die **Makroebene** analysiert die **systemische, strukturelle, langfristige Einbettung** einer Maßnahme.

### 3.2 Prüfdimensionen

| Dimension | Prüffrage | Beispiel |
|-----------|-----------|----------|
| **Systemkompatibilität** | Passt es ins bestehende System? | Energienetz, Marktstruktur |
| **Kulturelle Akzeptanz** | Wird es gesellschaftlich akzeptiert? | Verhaltensänderung nötig? |
| **Politische Machbarkeit** | Gibt es regulatorische Hürden? | Gesetze, Genehmigungen |
| **Marktdynamik** | Wie reagiert der Markt? | Verdrängung, Konkurrenz |
| **Infrastruktur** | Welche Infrastruktur wird benötigt? | Netze, Logistik, Ausbildung |
| **Wechselwirkungen** | Welche anderen Systeme werden beeinflusst? | Kaskaden, Nebeneffekte |

### 3.3 Makro-Prüflogik

```
MAKRO_PASS = TRUE wenn:
  (1) Systemkompatibilität gegeben ODER Umbau realistisch
  UND (2) Kulturelle Barrieren überwindbar
  UND (3) Politische Machbarkeit ≥ 50%
  UND (4) Infrastruktur vorhanden ODER aufbaubar
  UND (5) Wechselwirkungen beherrschbar
```

**Makro-Durchfallgründe:**
- Fundamentaler Systemkonflikt (z.B. widerspricht Grundinfrastruktur)
- Kulturelle Unüberwindbarkeit (z.B. erfordert unrealistische Verhaltensänderung)
- Politisch blockiert ohne Aussicht auf Änderung
- Infrastruktur nicht herstellbar in relevantem Zeitraum
- Unkontrollierbare negative Kaskaden

---

## 4. DIE 14 BEWERTUNGSKRITERIEN

### 4.1 Herkunft

Diese Kriterien wurden in der ursprünglichen Mikro-Makro-Maschine entwickelt und sind **domänenunabhängig** anwendbar.

### 4.2 Kriterienliste

| Nr | Kriterium | Ebene | Beschreibung |
|----|-----------|-------|--------------|
| 1 | **Wirkungsklarheit** | Mikro | Ist die Wirkung eindeutig messbar? |
| 2 | **Ressourcenverfügbarkeit** | Mikro | Sind benötigte Ressourcen zugänglich? |
| 3 | **Kosteneffizienz** | Mikro | Verhältnis Kosten zu Wirkung |
| 4 | **Risikokontrolle** | Mikro | Sind Risiken beherrschbar? |
| 5 | **Reversibilität** | Mikro | Kann die Maßnahme rückgängig gemacht werden? |
| 6 | **Vorhersehbarkeit** | Mikro | Ist das Ergebnis vorhersagbar? |
| 7 | **Systemkompatibilität** | Makro | Passt es ins bestehende System? |
| 8 | **Kulturelle Akzeptanz** | Makro | Gesellschaftliche Bereitschaft |
| 9 | **Politische Machbarkeit** | Makro | Regulatorische Umsetzbarkeit |
| 10 | **Infrastrukturabhängigkeit** | Makro | Welche Infrastruktur wird benötigt? |
| 11 | **Wechselwirkungen** | Makro | Interaktion mit anderen Systemen |
| 12 | **Skalierbarkeit** | Beide | Funktioniert es bei Massenanwendung? |
| 13 | **Zeitrahmen** | Beide | Wann tritt Wirkung ein? |
| 14 | **Prävention** | Beide | Verhindert es künftige Probleme? |

### 4.3 Bewertungsskala

Jedes Kriterium wird auf einer Skala von **0-3** bewertet:

| Wert | Bedeutung |
|------|-----------|
| 0 | Nicht erfüllt / Durchfall |
| 1 | Schwach erfüllt / Nachbesserung nötig |
| 2 | Ausreichend erfüllt |
| 3 | Vollständig erfüllt |

### 4.4 Durchfallschwellen

```
MIKRO-MAKRO_PASS = TRUE wenn:
  (1) Kein Kriterium = 0 (hartes Durchfallen)
  UND (2) Durchschnitt aller Kriterien ≥ 1.5
  UND (3) Mikro-Durchschnitt ≥ 1.5
  UND (4) Makro-Durchschnitt ≥ 1.5
```

---

## 5. BETRIEBSMODI

### 5.1 Auto-Modus (Standard)

Das System entscheidet automatisch über die Prüftiefe basierend auf:
- Komplexität der Maßnahme
- Erkannte Risikoindikatoren
- Verfügbare Informationen

### 5.2 Voll-Modus (MM:FULL)

Aktiviert durch: `MM:FULL` oder `Mikro-Makro-Vollprüfung`

- Alle 14 Kriterien werden explizit bewertet
- Detaillierte Begründung für jedes Kriterium
- Warnmatrix für Grenzfälle
- Explizite Empfehlung

### 5.3 Lite-Modus (MM:LITE)

Aktiviert durch: `MM:LITE` oder `Mikro-Makro-Schnellprüfung`

- Nur kritische Kriterien (1, 4, 7, 11, 12)
- Kurzurteil: PASS/FAIL/UNSICHER
- Maximal 5 Zeilen Begründung

---

## 6. PHASENMODELL

### 6.1 Phase S (Start)

**Erstanalyse** bei jeder neuen Maßnahme:
- IST-Zustand erfassen
- SOLL-Zustand definieren
- Erste Mikro-Makro-Einschätzung
- Warnungen identifizieren

### 6.2 Phase A (Analyse)

**Vertiefung** ohne neuen Full-Scan:
- Diskussion offener Fragen
- Nachrecherche zu Unsicherheiten
- Iteration der Bewertung

### 6.3 Phase B (Bewertung)

**Neuer vollständiger Scan** nur auf expliziten Befehl:
- `Starte Mikro-Makro-Prüfung` oder `MM:AN`
- Komplette Neubewertung aller 14 Kriterien
- Finales Urteil: PASS/FAIL

---

## 7. AKTIVIERUNGSBEFEHLE

| Befehl | Funktion |
|--------|----------|
| `MM:AN` | Starte Mikro-Makro-Analyse (Auto-Modus) |
| `MM:FULL` | Starte Vollprüfung (alle 14 Kriterien) |
| `MM:LITE` | Starte Schnellprüfung (5 kritische Kriterien) |
| `MM:EX` | Erkläre Mikro-Makro-Logik an diesem Beispiel |
| `MM:STATUS` | Zeige aktuellen Prüfstatus |

---

## 8. INTEGRATION IN PROVOLUTION

### 8.1 Änderungen an bestehenden Dokumenten

**Band 1 (Grundlagen):**
- Kapitel 2: Ergänze "Stufe 0: Mikro-Makro-Vorfilter" vor SEC-Definition
- Axiom 0 (neu): "Keine SEC-Bewertung ohne Mikro-Makro-PASS"

**Band 3 (Mathematische Grundlagen):**
- Kapitel 2: Ergänze formale Definition der 14 Kriterien
- Appendix: Mikro-Makro-Prüfmatrix

**Band 4 (Anwendungen):**
- Jede Anwendung erhält Abschnitt "Mikro-Makro-Vorprüfung"
- Dokumentation der PASS/FAIL-Entscheidung

### 8.2 Neue Metriken

| Metrik | Definition | Zielwert |
|--------|------------|----------|
| **MM-Score** | Durchschnitt aller 14 Kriterien (0-3) | ≥ 1.5 |
| **MM-Mikro** | Durchschnitt Kriterien 1-6 | ≥ 1.5 |
| **MM-Makro** | Durchschnitt Kriterien 7-11 | ≥ 1.5 |
| **MM-Bridge** | Durchschnitt Kriterien 12-14 | ≥ 1.5 |

### 8.3 Workflow-Update

**Bisheriger Workflow:**
```
Maßnahme → SEC-Bewertung → Aufnahme/Ablehnung
```

**Neuer Workflow:**
```
Maßnahme → MM-Vorprüfung → [PASS] → SEC-Bewertung → Aufnahme/Ablehnung
                        → [FAIL] → Ablehnung (kein SEC)
```

---

## 9. ANWENDUNGSBEISPIELE

### 9.1 Beispiel: Aufforstungsprojekt

**Mikro-Prüfung:**
| Kriterium | Wert | Begründung |
|-----------|------|------------|
| Wirkungsklarheit | 3 | CO₂-Bindung pro Baum messbar |
| Ressourcenverfügbarkeit | 2 | Land begrenzt, Setzlinge verfügbar |
| Kosteneffizienz | 2 | ~10-50€ pro t CO₂ |
| Risikokontrolle | 2 | Waldbrände, Schädlinge beherrschbar |
| Reversibilität | 1 | Wald kann abholzt werden, aber langsam |
| Vorhersehbarkeit | 2 | Wachstum kalkulierbar |
**Mikro-Durchschnitt: 2.0** ✓

**Makro-Prüfung:**
| Kriterium | Wert | Begründung |
|-----------|------|------------|
| Systemkompatibilität | 3 | Passt in Ökosystem |
| Kulturelle Akzeptanz | 3 | Hohe gesellschaftliche Zustimmung |
| Politische Machbarkeit | 2 | Förderprogramme existieren |
| Infrastrukturabhängigkeit | 2 | Minimale Infrastruktur nötig |
| Wechselwirkungen | 2 | Positive Nebeneffekte (Biodiversität) |
**Makro-Durchschnitt: 2.4** ✓

**Bridge-Prüfung:**
| Kriterium | Wert | Begründung |
|-----------|------|------------|
| Skalierbarkeit | 1 | Flächenbegrenzung |
| Zeitrahmen | 1 | Jahrzehnte bis volle Wirkung |
| Prävention | 2 | Langfristige CO₂-Senke |
**Bridge-Durchschnitt: 1.33** ⚠️

**MM-Gesamturteil:** PASS mit Warnung
→ Weiter zu SEC-Bewertung, aber Skalierungsgrenzen beachten

### 9.2 Beispiel: Perpetuum Mobile (Extremfall)

**Mikro-Prüfung:**
| Kriterium | Wert | Begründung |
|-----------|------|------------|
| Wirkungsklarheit | 0 | Physikalisch unmöglich |
| Ressourcenverfügbarkeit | 0 | Nicht existent |
| ... | ... | ... |

**MM-Gesamturteil:** FAIL (hartes Durchfallen bei Kriterium = 0)
→ Keine SEC-Bewertung nötig

---

## 10. HISTORISCHE EINORDNUNG

### 10.1 Chronologie

| Zeitpunkt | Entwicklung |
|-----------|-------------|
| **Vor Nov 2024** | Erste Mikro-Makro-Konzepte |
| **Nov 2024** | Formalisierung der 14 Kriterien |
| **Nov 2025** | SEC-2.0 Integration |
| **Dez 2025** | Phasenmodell (S/A/B) |
| **Feb 2026** | Formale Integration als E0 in Provolution |

### 10.2 Verhältnis zu SEC

| Aspekt | Mikro-Makro (E0) | SEC (Probatio Systemica) |
|--------|------------------|--------------------------|
| Typ | Vorfilter (qualitativ) | Bewertung (quantitativ) |
| Skala | 0-3 pro Kriterium | 0.0-1.0 Score |
| Ergebnis | PASS/FAIL | Numerischer Score |
| Zeitpunkt | Zuerst | Nach MM-PASS |
| Aufwand | Gering | Höher |
| Funktion | Ausschluss ungeeigneter Maßnahmen | Priorisierung geeigneter Maßnahmen |

---

## 11. CO₂-BILANZ-AUSWIRKUNGEN

### 11.1 Keine direkten Änderungen

Die Mikro-Makro-Maschine ist ein **Prozess-Tool**, keine neue Anwendung. Sie ändert nicht die CO₂-Potenziale der bestehenden 34 Anwendungen.

### 11.2 Indirekte Auswirkungen

- **Qualitätssicherung:** Nur geprüfte Maßnahmen in SEC
- **Effizienzsteigerung:** Weniger Fehlbewertungen
- **Konsistenz:** Einheitlicher Prüfstandard

### 11.3 Framework-Metriken

| Metrik | Vor E0 | Nach E0 |
|--------|--------|---------|
| Anwendungen | 34 | 34 (unverändert) |
| Domänen | 9 | 9 (unverändert) |
| CO₂-Potenzial | -54.2 Gt/Jahr | -54.2 Gt/Jahr (unverändert) |
| **Prüfstufen** | **1 (SEC)** | **2 (MM → SEC)** |
| Qualitätssicherung | Mittel | Hoch |

---

## 12. OFFENE PUNKTE FÜR BAND-1-INTEGRATION

**Zu dokumentieren:**
- [ ] Axiom 0 formulieren
- [ ] Kapitel 2 erweitern
- [ ] Verhältnis zu SEC-Axiomen klären
- [ ] Beispielhafte Durchläufe für alle 34 Anwendungen

**Zu entscheiden:**
- [ ] Soll MM-Score in Gesamt-Score einfließen?
- [ ] Gewichtung von MM vs. SEC?
- [ ] Automatische vs. manuelle MM-Prüfung?

---

## ÄNDERUNGSHISTORIE

| Version | Datum | Änderung |
|---------|-------|----------|
| 1.0 | 2026-02-04 | Erstfassung aus Archiv-Rekonstruktion |

---

**ENDE EXTENSION E0**
