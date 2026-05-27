# Probatio Veritatis (PV)
## Submodul von Probatio Systemica · Faktische Verifikation von Behauptungen
### CANON-Dokument · Version 1.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz  
**Status:** Entwurf · peer-review-vorbereitet  
**Einordnung:** PS-Submodul · anwendbar auf alle Domänen · Provolution-Klimamodul als Referenzimplementierung

---

## 0. PRÄAMBEL

**Probatio Veritatis (PV)** ist ein Submodul von Probatio Systemica (PS), das die SEC-J-Prüflogik auf die Verifikation faktischer Behauptungen überträgt. PV beantwortet nicht, *ob* eine Maßnahme sinnvoll ist, sondern *ob eine Behauptung über die Welt dem verfügbaren Evidenzstand standhält*.

PV ist:
- **Domänenunabhängig** durch modulare Quellenarchitektur (Klimamodul, Gesundheitsmodul, Politikmodul etc.)
- **Transparent** durch vollständigen Begründungspfad (Claim → Score → Quellen → Verdict)
- **Normativ erweiterbar** durch die J-Dimension: Framing, Perspektive und Machtasymmetrien werden explizit bewertet
- **Falsifizierbar**: alle Schwellenwerte, Formeln und Gewichtungen sind dokumentiert und anfechtbar

---

## 1. ABGRENZUNG ZU PS-U

| Merkmal | PS-U (Probatio Systemica Universal) | PV (Probatio Veritatis) |
|---|---|---|
| Prüfobjekt | Maßnahme / Intervention | Behauptung / Aussage |
| Eingabe | Beschreibung eines Vorhabens | Text, These, Zitat, Beleg |
| Kernfrage | Ist diese Maßnahme systemisch tragfähig? | Ist diese Behauptung faktisch haltbar? |
| Zeitlichkeit | Zukunftsorientiert (Wirkungsprognose) | Gegenwarts-/vergangenheitsbezogen (Evidenz) |
| Quellenlogik | Normativ (Zielwerte, Standards) | Empirisch (Studien, Statistiken, Primärquellen) |
| J-Veto-Logik | Gerechtigkeitsfolgen einer Maßnahme | Framing-Asymmetrien einer Aussage |

PV teilt mit PS-U: SEC-J-Dimensionen, Scoring-Logik (0–1), Veto-Mechanismus, MMM-Vorfilter (adaptiert).

---

## 2. CLAIM-TAXONOMIE

PV unterscheidet vier Claim-Typen, die unterschiedliche Verifikationspfade erfordern:

### CL-1 · Quantitativer Claim
Behauptung mit messbarer Größe.  
*Beispiel: „Deutschland hat seinen CO₂-Ausstoß seit 1990 um 40 % reduziert."*  
Verifikationspfad: Primärquelle (UBA, IPCC) → Zahlenwert prüfen → S-Score.

### CL-2 · Kausaler Claim
Behauptung über Ursache-Wirkung-Beziehung.  
*Beispiel: „Windkraftausbau senkt die Strompreise."*  
Verifikationspfad: Metaanalysen, kontrafaktische Studien → Effektgröße, Konfidenzintervall → E-Score.

### CL-3 · Normativer Claim (mit faktischer Basis)
Werturteil mit empirisch prüfbarer Komponente.  
*Beispiel: „Die Energiewende ist zu teuer."*  
Verifikationspfad: Kostendaten isolieren → faktische Teilaussage trennen → C-Score auf Faktenbasis; J-Score auf Framingbasis.

### CL-4 · Kompositer Claim
Mehrere Teilaussagen in einer Behauptung.  
Verifikationspfad: Claim in CL-1 bis CL-3 zerlegen → Teilscores → aggregieren (konservatives Minimum-Prinzip).

---

## 3. MMM-VORFILTER (ADAPTIERT FÜR PV)

### M1 · Claim-Einheitenklärung
- Welche Maßgröße wird behauptet? (Prozent, absolut, relativ, zeitlich befristet?)
- Welcher Bezugsraum? (national, global, sektoral?)
- Welcher Zeitraum? (Stichtag, Durchschnitt, Prognose?)
- Ergebnis: Operationalisierter Claim c(op)

### M2 · Prüfbarkeitsklärung

| Prüfbarkeit | Konsequenz |
|---|---|
| Vollständig prüfbar | → Weiter zu SEC-J |
| Teilweise prüfbar | → Nur prüfbare Teilaussagen bewerten; Rest als „nicht bewertbar" kennzeichnen |
| Nicht prüfbar (rein normativ) | → Abbruch; Ausgabe: „Kein faktischer Claim. PV nicht anwendbar." |

### M3 · Domänenzuweisung

| Domäne | Modul | Referenzquellen |
|---|---|---|
| Klimaschutz | PV-Klima | IPCC, UBA, Provolution-CANON |
| Gesundheit | PV-Gesundheit | WHO, Cochrane, AWMF |
| Wirtschaft | PV-Wirtschaft | Destatis, IWF, OECD |
| Politik/Recht | PV-Politik | Bundestag, EUR-Lex, Verfassungsgericht |
| Allgemein | PV-Default | Peer-reviewed Journals, offizielle Statistiken |

---

## 4. SEC-J-PRÜFUNG FÜR PV

### 4.1 S · Sufficient

| Evidenzgrad | Beschreibung | S-Wert |
|---|---|---|
| EG-1 | Mehrere unabhängige Metaanalysen / Primärquellen | 0,85–1,00 |
| EG-2 | Einzelne Primärstudie oder offizielle Statistik | 0,60–0,84 |
| EG-3 | Sekundärquelle, Medienbericht mit Quellenangabe | 0,35–0,59 |
| EG-4 | Keine nachprüfbare Quelle | 0,00–0,34 |

```
S(c) = EG(c) × Aktualitätsfaktor(c)

Aktualitätsfaktor:
  ≤ 2 Jahre → 1,00 | 3–5 Jahre → 0,85 | 6–10 Jahre → 0,70 | > 10 Jahre → 0,50
  (historische Fakten: immer 1,00)
```

### 4.2 E · Efficient

```
E(c) = 1 − (Anzahl_Abweichungen(c) × 0,25)   [Minimum: 0,00]

Abweichungstypen: Zahlenfehler, Bezugsraumfehler, Zeitfehler, Kausalitätssprung
```

### 4.3 C · Consistent

```
C(c) = 1 − (Anzahl_Widersprüche(c) / Anzahl_Vergleichsquellen(c))

Mindestens 3 domänenspezifische Vergleichsquellen erforderlich.
```

**Veto-Bedingung:** C(c) < 0,50 → automatisches Verdict: FALSE (unabhängig von S, E, J).

### 4.4 J · Justice

| Subdimension | Frage | Gewicht |
|---|---|---|
| J1 · Sprecherposition | Wessen Interesse bedient die Aussage? | 0,25 |
| J2 · Auslassung | Welche Betroffenen/Daten fehlen? | 0,30 |
| J3 · Vulnerabilität | Werden strukturell benachteiligte Gruppen korrekt dargestellt? | 0,25 |
| J4 · Partizipation | Haben betroffene Akteure zur Evidenz beigetragen? | 0,20 |

```
J(c) = Σ(Ji(c) × wi)   für i = 1..4

J-Veto: J(c) < 0,40 → Zusatzflag „HARMFUL FRAMING" (kein automatisches FALSE)
```

---

## 5. AGGREGATION UND VERDICT

### 5.1 PV-Gesamtscore

```
PV(c) = (wS × S(c)) + (wE × E(c)) + (wC × C(c)) + (wJ × J(c))

Standardgewichtung:
  wS = 0,30  (Evidenztiefe)
  wE = 0,20  (Quellennutzung ohne Überdehnung)
  wC = 0,35  (Widerspruchsfreiheit – höchstes Gewicht)
  wJ = 0,15  (Framing-Symmetrie)
```

**Begründung:** C erhält das höchste Gewicht, da Widerspruchsfreiheit mit gesichertem Wissen die härteste Bedingung faktischer Haltbarkeit ist. Ein Claim, der belegtem Konsens widerspricht, ist unabhängig von seiner Quellenbreite nicht haltbar.

### 5.2 Verdict-Schwellen

| PV(c) | Verdict |
|---|---|
| ≥ 0,80 | **VERIFIED** |
| 0,50–0,79 | **UNCERTAIN** |
| 0,20–0,49 | **FALSE** |
| < 0,20 | **FABRICATED** |
| C(c) < 0,50 | **FALSE** (C-Veto) |
| J(c) < 0,40 | Zusatzflag: **HARMFUL FRAMING** |

### 5.3 Composite-Claim-Aggregation (CL-4)

```
PV(c) = min(PV(ci))   [konservatives Prinzip]
Ausnahme: alle ci ≥ 0,80 → PV(c) = Durchschnitt(PV(ci))
```

---

## 6. BEGRÜNDUNGSPFAD (OUTPUT-STRUKTUR)

```
PV-REPORT · [Datum] · Claim-ID: [UUID]

INPUT:
  Originaler Claim: „[Text]"
  Claim-Typ: [CL-1 / CL-2 / CL-3 / CL-4]
  Operationalisiert: „[c(op)]"
  Domänenmodul: [PV-Klima / ...]

MMM-VORFILTER:
  M1 · Einheit: [Maßgröße, Bezugsraum, Zeitraum]
  M2 · Prüfbarkeit: [vollständig / teilweise / nicht prüfbar]
  M3 · Domäne: [zugewiesenes Modul]

SEC-J-SCORES:
  S(c) = [Wert] · EG: [EG-1..4] · Quellen: [n]
  E(c) = [Wert] · Abweichungen: [Liste]
  C(c) = [Wert] · Widersprüche: [n] / Vergleichsquellen: [n]
  J(c) = [Wert] · J1–J4: [Einzelwerte]

AGGREGATION:
  PV(c) = (0,30 × S) + (0,20 × E) + (0,35 × C) + (0,15 × J) = [Wert]

VERDICT: [VERIFIED / UNCERTAIN / FALSE / FABRICATED]
  [Ggf.] Zusatzflag: HARMFUL FRAMING

QUELLEN: [1] [Quelle · Datum] …
BEGRÜNDUNG: [Freitext]
EINSCHRÄNKUNGEN: [Was nicht geprüft werden konnte]
```

---

## 7. DOMÄNENMODUL: PV-KLIMA (REFERENZIMPLEMENTIERUNG)

### Referenzquellen (Hierarchie)

| Rang | Quellentyp | Beispiele |
|---|---|---|
| 1 | IPCC-Berichte (AR6) | Synthesis Report 2023, WG I–III |
| 2 | Provolution-CANON | 37 Anwendungen, −58,56 Gt/Jahr, SEC-J-Bewertungen |
| 3 | Nationale Umweltbehörden | UBA (DE), EPA (US), EEA (EU) |
| 4 | Peer-reviewed Klimajournale | Nature Climate Change, Science |
| 5 | Offizielle Statistiken | IEA, Eurostat, EDGAR |

### Klimaspezifischer Aktualitätsfaktor

| Alter | Faktor |
|---|---|
| ≤ 1 Jahr | 1,00 |
| 2–3 Jahre | 0,85 |
| 4–6 Jahre | 0,65 |
| > 6 Jahre | 0,45 |

### Klimaspezifische Veto-Bedingungen

- Direkter Widerspruch zum IPCC-Konsens → automatisch FABRICATED
- Behauptungen über Kipppunkte ohne Quellenangabe → S-Cap bei EG-3 (S ≤ 0,59)

---

## 8. FALSIFIZIERBARKEIT

| Parameter | Aktueller Wert | Anpassungsbedingung |
|---|---|---|
| wS | 0,30 | Wenn Evidenztiefe systematisch überbewertet |
| wC | 0,35 | Wenn Konsistenz zu restriktiv → senken |
| C-Veto-Schwelle | 0,50 | Durch Kalibrierungsstudie anpassbar |
| J-Veto-Schwelle | 0,40 | Durch normative Konsensfindung |
| EG-1 Untergrenze | 0,85 | Wenn Metaanalysenqualität variiert |

---

## 9. ANHANG: BEISPIEL-PRÜFUNG

**Claim:** „Offshore-Windkraft deckt bereits 10 % des deutschen Strombedarfs."

- M1: CL-1, Anteil Offshore-Wind an Bruttostromerzeugung DE, implizit „aktuell"
- M2: vollständig prüfbar · M3: PV-Klima

| Dim | Berechnung | Wert |
|---|---|---|
| S | EG-2 (BNetzA 2024) × Aktualitätsfaktor 1,00 | 0,70 |
| E | 1 Zahlenfehler (+1,8 PP Übertreibung) → 1 − 0,25 | 0,75 |
| C | 1 Widerspruch / 3 Quellen (IEA, Eurostat, UBA) | 0,67 |
| J | J1=0,80 / J2=0,70 / J3=0,90 / J4=0,80 | 0,79 |

**PV(c)** = (0,30 × 0,70) + (0,20 × 0,75) + (0,35 × 0,67) + (0,15 × 0,79) = 0,21 + 0,15 + 0,23 + 0,12 = **0,71**

**VERDICT: UNCERTAIN** – Claim überschätzt Offshore-Anteil um ~1,8 PP. Kernaussage faktisch gestützt; Präzision nicht ausreichend für VERIFIED.

---

## LICENSE

This work is released under:
- **CC0 1.0 Universal** (Public Domain)
- **Open Humanity License** (OHL)

See [LICENSE.md](../LICENSE.md) for full details.

---

*CANON-Referenz: 07_Probatio_Veritatis_v1.0.md · Version 1.0 · 2026-04-09 · Tobias Yoka Dietz*
