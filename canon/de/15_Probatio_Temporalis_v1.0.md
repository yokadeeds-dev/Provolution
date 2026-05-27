# Probatio Temporalis (PT)
## Submodul von Probatio Systemica · Zeitreihen-Tracking und Score-Drift-Analyse
### CANON-Dokument · Version 1.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz
**Einordnung:** PS-Meta-Modul · orchestriert PV, PD, PI, PN, PP über Zeit
**Besonderheit:** PT hat keine eigene Prüflogik – es misst Score-Drift

---

## 0. PRÄAMBEL

**Probatio Temporalis (PT)** ist das Meta-Modul von Probatio Systemica.
PT prüft nicht selbst – es beobachtet wie sich Scores anderer Module
über Zeit verändern.

Kernfrage: **Hat sich die Evidenz-, Konsistenz- oder Framlage verändert?
Wann ist eine Revision des Verdicts gerechtfertigt?**

PT ist:
- **Nicht-prüfend** – PT führt keine eigene SEC-J-Analyse durch
- **Drift-sensitiv** – misst Veränderungen, nicht absolute Werte
- **Kanonrevisions-Anker** – definiert wann ein CANON-Update gerechtfertigt ist
- **Kopernikus-Schutz** – verhindert dass innovative Low-n-Claims dauerhaft
  als UNSUBSTANTIATED verschwinden

PT schließt den Kreis der PS-Familie:
PS-U → PV → PD → PI → PN → PP → PT

---

## 1. ABGRENZUNG

| Merkmal | Alle anderen Module | PT |
|---|---|---|
| Prüflogik | Eigene SEC-J-Analyse | Keine – beobachtet andere |
| Zeitpunkt | Einzelmoment (t0) | Mehrere (t0...tn) |
| Eingabe | Claim/Entscheidung/etc. | Vorherige Modulergebnisse |
| Ausgabe | Verdict | Trendlinie + Revisionsempfehlung |
| Aktivierung | Direkt | Automatisch + manuell |
| Kanonrevision | Nicht zuständig | Primäres Instrument |

---

## 2. PT-AKTIVIERUNG

### Automatische Trigger
```
PV:  UNSUBSTANTIATED | CANON_CONFLICT_FLAG | n=1+EG-1
PD:  STRUKTURELLER WIDERSPRUCH
PI:  STRUKTURELLE INKONSISTENZ
PN:  STRUKTURELLE AUSBLENDUNG
PP:  KONTROVERS | INKOHÄRENT (bei etabliertem Argument)
```

### Manuelle Aktivierung (PT:CHECK)
```
PT:CHECK [Claim/Objekt]
→ Vorgänger im Register? → Drift messen
→ Kein Vorgänger? → Neues Tracking starten
   Hinweis: "Kein Vorgänger. PT beginnt Tracking ab jetzt."
```

---

## 3. INTERVALLKLASSEN (THEMEN-ADAPTIV)

| Klasse | Domänen | Intervall | Trigger-Beispiel |
|---|---|---|---|
| A (schnell) | PV-Gesundheit, PV-Technik | 30/90/180 Tage | neue Studie |
| B (mittel) | PV-Klima, PV-Wirtschaft, PD, PI | 90/180/365 Tage | Jahresbericht, Wahl |
| C (langsam) | PN, PP | 180/365/730 Tage | Paradigmenwechsel |
| D (reaktiv) | alle | sofort | CANON_CONFLICT, Rückzug |

D immer zusätzlich zu A/B/C. Automatische Zuweisung aus VFP-Domäne.

```
PV-Klima (Tech)  → A + D
PV-Klima (Politik) → B + D
PV-Gesundheit    → A + D
PD / PI          → B + D
PN / PP          → C + D
```


---

## 4. PRÜFPROZESS

```
1. Register-Eintrag (t0 + Score + Verdict + n)
2. Intervallklasse zuweisen
3. Bei Folgemessung: Quellmodul erneut ausführen → neuer Score
4. Drift: Delta = Score(tn) - Score(t0)
5. Trend-Status bestimmen
6. Revisionsschwellen prüfen
```

### Drift-Berechnung
```
Delta > +0,15    → Signifikanter Aufwärtstrend
Delta +0,05-0,15 → Moderater Aufwärtstrend
Delta ±0,05      → Stabil
Delta -0,05-0,15 → Moderater Abwärtstrend
Delta < -0,15    → Signifikanter Abwärtstrend

Volatilität >±0,20 zwischen Messungen → Flag: INSTABIL
```

### Trend-Status
```
EMERGING   : Score steigt, noch unter Zielschwelle
CONVERGING : Score < 0,10 von Revisionsschwelle
STABLE     : Score ±0,05 über mehrere Messungen
DECLINING  : Score fällt signifikant
REVERSED   : Verdict hat sich geändert
INSTABIL   : Hohe Volatilität, kein klarer Trend
```

---

## 5. REVISIONSSCHWELLEN UND KANONREVISION

```
Aufwärtsrevision:
  UNSUBSTANTIATED → UNCERTAIN : Score >= 0,50, n >= 2
  UNCERTAIN → VERIFIED        : Score >= 0,80, n >= 3
  KONTROVERS → BEDINGT KOHÄRENT: PP-Score >= 0,60, n >= 2

Abwärtsrevision:
  VERIFIED → UNCERTAIN        : Score < 0,75 (zwei Messungen)
  UNCERTAIN → FALSE           : Score < 0,45

Kanonrevision empfohlen wenn:
  n >= 3 EG-1-Quellen widersprechen CANON-Eintrag
  Verdict-Revision stabil >= 2 Messungen

PT empfiehlt immer – entscheidet nie.
Manuelle Bestätigung durch Yoka erforderlich.
```

### Prognose (SCHÄTZUNG)
```
Nur wenn >= 3 Datenpunkte + Trend EMERGING oder CONVERGING

Methode: Lineare Extrapolation
PFLICHT: "SCHÄTZUNG – keine Garantie. Externe Ereignisse
          können Trend jederzeit ändern."
```

---

## 6. OUTPUT-STRUKTUR

```
PT-REPORT v1.0 · [Datum]

OBJEKT: "[Claim/Entscheidung/Argument]"
Quellmodul: [PV/PD/PI/PN/PP] | Klasse: [A/B/C+D]
Aktivierung: automatisch ([Trigger]) | manuell (PT:CHECK)

ZEITREIHE:
  t0 [Datum]: Score=[x] | Verdict=[x] | n=[x]
  t1 [Datum]: Score=[x] | Verdict=[x] | n=[x] | Delta=[x]
  t2 [Datum]: Score=[x] | Verdict=[x] | n=[x] | Delta=[x]

DRIFT:
  Gesamt-Delta (t0→tn): [x]
  Trend-Status: [...]
  Wendepunkte: [Datum + auslösendes Ereignis]

[Falls >= 3 Datenpunkte:]
PROGNOSE (SCHÄTZUNG):
  Nächste Messung: [Datum]
  Erwarteter Score: [x] (wenn Trend anhält)
  SCHÄTZUNG – keine Garantie.

REVISIONSSTATUS:
  Empfohlen: ja | nein | ausstehend
  Schwelle: [aktuell] / [Ziel]

[Falls Revision empfohlen:]
REVISIONSEMPFEHLUNG:
  Alt: "[Verdict]" → Neu: "[Verdict]"
  Begründung: [Trendlinie + n-Entwicklung]
  Manuelle Bestätigung erforderlich.

NÄCHSTE MESSUNG: [Datum] | [Intervall/Ereignis]
```


---

## 7. PRÜFMODI

| Befehl | Funktion |
|---|---|
| PT:CHECK | Manueller Re-Check eines Objekts |
| PT:TREND | Nur Trendlinie und Drift |
| PT:STATUS | Alle aktiven Trackings |
| PT:REVISION | Ausstehende Revisionsempfehlungen |
| PT:PLAIN | Fließtext für Laien, max. 250 Wörter |

Plain-Verdicts: EMERGING→IN ENTWICKLUNG | CONVERGING→KURZ VOR ÄNDERUNG |
STABLE→STABIL | DECLINING→VERSCHLECHTERT SICH | REVERSED→GEÄNDERT | INSTABIL→NOCH UNKLAR

---

## 8. VERBINDUNG ZU ANDEREN MODULEN

| Von | Trigger | PT-Ausgabe |
|---|---|---|
| PV | UNSUBSTANTIATED, CANON_CONFLICT | Score-Entwicklung des Claims |
| PD | STRUKTURELLER WIDERSPRUCH | Hat sich Datenlage verändert? |
| PI | STRUKTURELLE INKONSISTENZ | Institution besser/schlechter? |
| PN | STRUKTURELLE AUSBLENDUNG | Framing-Muster im Wandel? |
| PP | KONTROVERS/INKOHÄRENT | Philosophischer Konsens im Wandel? |

---

## 9. ABGRENZUNGSREGEL (KANONISCH)

> "PT ist das einzige Modul das keine eigene Prüflogik hat.
> Es misst nicht ob etwas wahr ist – sondern ob sich die
> Wahrheitslage verändert hat."

---

## 10. BEISPIEL-TRACKING

**Claim:** "Offshore-Wind deckt 10% des deutschen Strombedarfs."
Trigger: UNCERTAIN (PV-Score 0,71) | Klasse: B + D

```
t0 2026-01-01: 0,71 UNCERTAIN n=3
t1 2026-04-01: 0,74 UNCERTAIN n=4  Delta=+0,03 (BNetzA Q1)
t2 2026-07-01: 0,77 UNCERTAIN n=4  Delta=+0,03
t3 2027-01-01: 0,82 VERIFIED  n=5  Delta=+0,05 (IEA Metaanalyse)
Wendepunkt t3: IEA EG-1-Studie

REVISIONSEMPFEHLUNG: UNCERTAIN → VERIFIED
Schwelle erreicht: 0,82 >= 0,80 bei n=5
Manuelle Bestätigung erforderlich.
```

---

## 11. FALSIFIZIERBARKEIT

| Parameter | Wert | Anpassungsbedingung |
|---|---|---|
| Signifikanter Drift | ±0,15 | Empirisch kalibrierbar |
| Klasse A | 30/90/180 Tage | Domänen-spezifisch |
| Klasse B | 90/180/365 Tage | Domänen-spezifisch |
| Klasse C | 180/365/730 Tage | Domänen-spezifisch |
| Kanonrevisions-n | 3 EG-1-Quellen | Kalibrierungsstudie |

---

## LICENSE

CC0 1.0 Universal + Open Humanity License. See LICENSE.md.

---

*CANON-Referenz: 15_Probatio_Temporalis_v1.0.md · Version 1.0 · 2026-04-09*
*Tobias Yoka Dietz · Meta-Modul von Probatio Systemica*
