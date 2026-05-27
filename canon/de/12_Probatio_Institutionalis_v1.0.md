# Probatio Institutionalis (PI)
## Submodul von Probatio Systemica · SEC-J-Audit von Institutionen
### CANON-Dokument · Version 1.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz  
**Status:** Entwurf · peer-review-vorbereitet  
**Einordnung:** PS-Submodul · Gap-Analyse zwischen institutionellem Anspruch und Realität

---

## 0. PRÄAMBEL

**Probatio Institutionalis (PI)** überträgt die SEC-J-Prüflogik auf Institutionen als Gesamtsystem. PI beantwortet nicht ob eine Maßnahme wirksam ist (PS-U), eine Behauptung wahr ist (PV) oder eine Entscheidung korrekt getroffen wurde (PD), sondern ob eine Institution ihre eigenen erklärten Ziele SEC-J-konform umsetzt.

Kernfrage: **Anspruch = Realität?**

PI ist prozessorientiert auf systemische Muster, nicht auf Einzelakte. Drei fehlerhafte Entscheidungen machen noch keine schlechte Institution – ein systemisches Muster schon.

---

## 1. ABGRENZUNG ZU PS-U, PV, PD

| Merkmal | PS-U | PV | PD | PI |
|---|---|---|---|---|
| Prüfobjekt | Maßnahme | Behauptung | Entscheidung | Institution |
| Kernfrage | Systemisch tragfähig? | Faktisch haltbar? | Prozessual konform? | Anspruch = Realität? |
| Zeitlichkeit | Zukunft | Vergangenheit | Beides | Systemisch (Muster) |
| Quellenlogik | Normativ | Empirisch | Deliberativ | Strukturell (Berichte, Bilanzen) |
| J-Gewicht | 0,15 | 0,15 | 0,25 | 0,25 |
| Abbruchlogik | S-Stop | C-Veto | Kein Stop | Kein Stop |

---

## 2. INSTITUTIONS-TAXONOMIE

### IT-1 · Staatliche Behörde
Ministerien, Bundesämter, Landesbehörden, Regulierungsbehörden.
Prüfpfad: Gesetzlicher Auftrag → Jahresbericht → Haushalt → Messindikatoren.

### IT-2 · Internationale Organisation
EU-Institutionen, UN-Agenturen, multilaterale Fonds.
Prüfpfad: Mandatsdokument → Aktivitätsbericht → Budget-Allokation → Outcome-Indikatoren.

### IT-3 · Zivilgesellschaftliche Organisation
NGOs, Verbände, Think Tanks, Stiftungen.
Prüfpfad: Satzung/Mission → Jahresbericht → Finanzierungsstruktur → Wirkungsmessung.

### IT-4 · Unternehmen mit öffentlichem Auftrag
Öffentliche Unternehmen, gemischtwirtschaftliche Gesellschaften, regulierte Märkte.
Prüfpfad: Unternehmensziele → Geschäftsbericht → ESG-Bericht → Regulierungsvorgaben.

---

## 3. MMM-VORFILTER (ADAPTIERT FÜR PI)

### M1 · Institutionsklärung
- Welche Institution wird geprüft?
- Was sind ihre erklärten Ziele? (Mission, gesetzlicher Auftrag, Leitbild)
- Welcher Beobachtungszeitraum? (mindestens 2 Jahre empfohlen)
- Ergebnis: Operationalisiertes Institutionsprofil i(op)

### M2 · Datenverfügbarkeit

| Datenlage | Konsequenz |
|---|---|
| Vollständig (Jahresbericht, Haushalt, Indikatoren) | → Weiter zu SEC-J |
| Teilweise (Lücken in Wirkungsmessung oder Finanzdaten) | → Prüfen was vorhanden, Lücken kennzeichnen |
| Minimal (nur Selbstdarstellung) | → S-Cap UG-3 (max. 0,59); Flag: Transparenzdefizit |

### M3 · Sektormodul

| Sektor | Modul | Referenzstandards |
|---|---|---|
| Klimaschutz / Umwelt | PI-Klima | IPCC, Provolution-CANON, KSG-Ziele |
| Soziales / Wohlfahrt | PI-Sozial | SDGs, SOEP, EU-Sozialindikatoren |
| Wirtschaft / Finanzen | PI-Wirtschaft | OECD, Bundesrechnungshof-Standards |
| Gesundheit | PI-Gesundheit | WHO-Qualitätsindikatoren, G-BA |
| Allgemein | PI-Default | GRI-Standards, OECD-Governance-Prinzipien |

---

## 4. SEC-J-PRÜFUNG FÜR PI

### 4.1 S · Sufficient

| Umsetzungsgrad | Beschreibung | S-Wert |
|---|---|---|
| UG-1 | Ziele messbar definiert + vollständig erreicht + dokumentiert | 0,85–1,00 |
| UG-2 | Ziele definiert + überwiegend erreicht (> 70%) | 0,60–0,84 |
| UG-3 | Ziele definiert + teilweise erreicht (30–70%) | 0,35–0,59 |
| UG-4 | Ziele nicht messbar definiert oder < 30% erreicht | 0,00–0,34 |

```
S(i) = UG(i) × Messbarkeitsfaktor(i)

Messbarkeitsfaktor:
  Quantitative Indikatoren mit externer Verifizierung  → 1,00
  Quantitative Indikatoren ohne externe Verifizierung  → 0,85
  Nur qualitative Selbsteinschätzung                   → 0,65
  Keine Wirkungsmessung dokumentiert                   → 0,40
```

### 4.2 E · Efficient

```
E(i) = 1 − (Anzahl_Effizienzdefizite × 0,20)   [Minimum: 0,00]

Effizienzdefizite (je −0,20):
  - Overhead > 30% des Gesamtbudgets ohne Begründung
  - Doppelstrukturen mit anderen Institutionen gleichen Auftrags
  - Ressourceneinsatz ohne nachweisbaren Wirkungsbezug
  - Signifikante Abweichung von Brancheneffizienzstandards
  - Systematische Mittelfehlallokation (Budget ≠ Prioritäten)
```

### 4.3 C · Consistent

```
C(i) = 1 − (Widersprüche / Referenzrahmen)

Referenzrahmen (mindestens 3):
  - Eigene Mission / Satzung / gesetzlicher Auftrag
  - Eigene Jahresplanung / Strategiepapiere
  - Übergeordnete Regulierung (national + EU)
  - Wissenschaftlicher Konsens im Wirkungsfeld
```

PI-Flag: C(i) < 0,40 → "STRUKTURELLE INKONSISTENZ" (Pflichthinweis, kein Stop)

Typische Inkonsistenzen: Klimaministerium finanziert fossile Projekte; Gesundheitsbehörde empfiehlt Maßnahmen ohne Evidenzgrundlage; NGO-Lobby widerspricht eigener Satzung.

### 4.4 J · Justice

J3 (Verteilung) erhält das höchste Gewicht, da Institutionen primär durch ihre Verteilungswirkung legitimiert werden.

```
J(i) = (0,20 × J1) + (0,25 × J2) + (0,30 × J3) + (0,25 × J4)

J1 · Zugang        : Sind Leistungen / Informationen für alle zugänglich?
J2 · Partizipation : Werden Betroffene in Entscheidungen einbezogen?
J3 · Verteilung    : Verteilen sich Nutzen und Lasten gerecht?
J4 · Vulnerabilität: Werden benachteiligte Gruppen aktiv berücksichtigt?
```

PI-Flag: J(i) < 0,40 → "EXKLUSIONSRISIKO" (Pflichthinweis + Empfehlung)

---

## 5. AGGREGATION UND VERDICT

```
PI(i) = (0,30 × S) + (0,20 × E) + (0,25 × C) + (0,25 × J)
```

### Verdict-Schwellen

| PI(i) | Verdict |
|---|---|
| ≥ 0,80 | INTEGER |
| 0,60–0,79 | BEDINGT INTEGER |
| 0,40–0,59 | DEFIZITÄR |
| < 0,40 | NICHT INTEGER |
| C(i) < 0,40 | Zusatzflag: STRUKTURELLE INKONSISTENZ |
| J(i) < 0,40 | Zusatzflag: EXKLUSIONSRISIKO |

---

## 6. BEGRÜNDUNGSPFAD (OUTPUT-STRUKTUR)

```
PI-REPORT · [Datum] · Institutions-ID: [UUID]

INPUT:
  Institution: "[Name]"
  Typ: [IT-1 / IT-2 / IT-3 / IT-4]
  i(op): "[Ziele + Beobachtungszeitraum]"
  Sektormodul: [PI-Klima / ...]

MMM-VORFILTER:
  M1 · i(op): [...]
  M2 · Datenverfügbarkeit: [vollständig / teilweise / minimal]
  M3 · Sektor: [Modul]

SEC-J-SCORES:
  S(i) = [Wert] · UG: [UG-1..4] · Messbarkeitsfaktor: [Wert]
  E(i) = [Wert] · Defizite: [Liste oder "keine"]
  C(i) = [Wert] · Widersprüche: [n] / Referenzrahmen: [n]
  J(i) = [Wert] · J1–J4: [Einzelwerte]

AGGREGATION:
  PI(i) = (0,30×S) + (0,20×E) + (0,25×C) + (0,25×J) = [Gesamt]

VERDICT: [INTEGER / BEDINGT INTEGER / DEFIZITÄR / NICHT INTEGER]
  [Ggf.] Flag: STRUKTURELLE INKONSISTENZ | EXKLUSIONSRISIKO

BEGRÜNDUNG: [S / E / C / J / Verdict je 1–2 Sätze]

VERBESSERUNGSEMPFEHLUNGEN:
  [Methodisch: Was würde welchen Score konkret erhöhen?]

QUELLEN: [1] [Quelle · Datum · Fundstelle]
EINSCHRÄNKUNGEN: [Datenlücken, Selbstberichte ohne externe Verifizierung]
```

---

## 7. SEKTORMODUL: PI-KLIMA

### Referenzstandards

| Rang | Standard | Quelle |
|---|---|---|
| 1 | IPCC AR6 Handlungsempfehlungen | IPCC 2023 |
| 2 | Nationales Klimaschutzziel (KSG) | BGBl. 2021 |
| 3 | Provolution-CANON Anwendungsmatrix | 37 Anwendungen, −58,56 Gt/Jahr |
| 4 | EU-Taxonomie | EUR-Lex |
| 5 | Science Based Targets (SBTi) | SBTi 2023 |

### Verbindung zu Provolution Deutschland

- PI-Audit von Klimabehörden → Legitimationsgrundlage für Provolution-Forderungen
- PI-J-Score → Input für Partizipationsanalyse
- PI-NICHT INTEGER-Verdicts → Reformbedarf-Evidenz für Provolution-Politikpapiere

---

## 8. ABGRENZUNGSREGEL (KANONISCH)

> "PS-U bewertet ob eine Maßnahme systemisch tragfähig ist.
> PV bewertet ob Behauptungen darüber faktisch haltbar sind.
> PD bewertet ob die Entscheidung dafür SEC-J-konform getroffen wurde.
> PI bewertet ob die Institution, die sie umsetzt, ihren eigenen Anspruch erfüllt."

Die vier Module bilden eine vollständige Prüfkette: Maßnahme → Behauptung → Entscheidung → Institution.

---

## 9. FALSIFIZIERBARKEIT

| Parameter | Wert | Anpassungsbedingung |
|---|---|---|
| wS | 0,30 | Wenn Zielerreichung überbewertet → senken |
| wC / wJ | je 0,25 | Wenn Institutionstyp andere Priorität erfordert |
| C-Flag-Schwelle | 0,40 | Durch Kalibrierungsstudie anpassbar |
| J-Flag-Schwelle | 0,40 | Durch normative Konsensfindung |
| Effizienzabzug E | 0,20 | Wenn zu restriktiv → auf 0,15 senken |

---

## ANHANG: BEISPIEL-PRÜFUNG

**Institution:** BMWK – Bundesministerium für Wirtschaft und Klimaschutz, 2022–2024

- M1: IT-1, Auftrag: Klimaneutralität 2045 + wirtschaftliche Prosperität
- M2: Vollständig
- M3: PI-Klima

| Dim | Berechnung | Wert |
|---|---|---|
| S | UG-3 (Sektorziele 2022 verfehlt) × Messbarkeitsfaktor 0,85 | 0,43 |
| E | 2 Defizite (fossile Subventionen ~12 Mrd./Jahr; Doppelstrukturen mit BAFA) | 0,60 |
| C | 3 Widersprüche (KSG vs. Gasinfrastrukturförderung, LNG, Dienstwagenprivileg) / 4 Rahmen | 0,25 |
| J | J1=0,60 / J2=0,55 / J3=0,50 / J4=0,55 | 0,55 |

**PI(i)** = (0,30×0,43) + (0,20×0,60) + (0,25×0,25) + (0,25×0,55) = 0,13+0,12+0,06+0,14 = **0,45**

**VERDICT: DEFIZITÄR** · Flag: STRUKTURELLE INKONSISTENZ (C=0,25)

Verbesserungsempfehlungen: Abschaffung kontraproduktiver Subventionen (C: 0,25 → ~0,60), Verteilungsfolgenabschätzung CO₂-Bepreisung (J3: 0,50 → ~0,75).

---

## LICENSE

This work is released under CC0 1.0 Universal + Open Humanity License.
See LICENSE.md for full details.

---

*CANON-Referenz: 12_Probatio_Institutionalis_v1.0.md · Version 1.0 · 2026-04-09 · Tobias Yoka Dietz*
