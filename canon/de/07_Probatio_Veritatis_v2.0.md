# Probatio Veritatis (PV)
## Submodul von Probatio Systemica · Faktische Verifikation von Behauptungen
### CANON-Dokument · Version 2.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz
**Vorgänger:** 07_Probatio_Veritatis_v1.0.md
**Änderungen v1.0 → v2.0:**
- C aufgespalten: C_ext (empirisch) + C_int (logisch)
- Dynamic Source Rule mit n-Skalierung
- Fünftes Verdict: UNSUBSTANTIATED
- VFP ersetzt MMM-Vorfilter (Terminologie bereinigt)
- MMM neu: nur aktiv wenn n < 3
- CANON_CONFLICT_FLAG als PT-Trigger
- PT-Brücke für Low-n-Claims

---

## 0. PRÄAMBEL

**Probatio Veritatis (PV) v2.0** erweitert v1.0 um logische Konsistenzprüfung, Quellenskalierung und PT-Kopplung. PV beantwortet ob eine Behauptung dem verfügbaren Evidenzstand UND der logischen Konsistenz standhält.

---

## 1. TERMINOLOGIE (NEU IN V2.0)

**VFP – Vorfilter-Protokoll**
Ersetzt "MMM-Vorfilter" in PV. Klärt Einheit, Prüfbarkeit, Domäne. Immer aktiv.

**MMM – Mikro-Makro-Matching**
Ursprüngliche PS-Definition: prüft ob Logik auf Mikro genauso gilt wie auf Makro.
In PV v2.0: nur aktiv wenn n < 3 Quellen. Skalierungsanker für C_int.
Ursprüngliche PS-Definition: prüft ob Logik auf Mikro genauso gilt wie auf Makro.
In PV v2.0: nur aktiv wenn n < 3 Quellen. Skalierungsanker für C_int.

Strikte Trennung:
- VFP = immer aktiv (Eintrittscheck)
- MMM = bedingt aktiv (n < 3, Skalierungsprüfung)

---

## 2. CLAIM-TAXONOMIE

| Typ | Beschreibung | MMM-Relevanz |
|---|---|---|
| CL-1 | Quantitativer Claim | gering |
| CL-2 | Kausaler Claim | hoch (Skalenbrüche häufig) |
| CL-3 | Normativer Claim mit faktischer Basis | mittel |
| CL-4 | Kompositer Claim | fallabhängig |

---

## 3. VFP – VORFILTER-PROTOKOLL

### V0 · Zuständigkeits-Check
Bestimmt ob der Input für PV prüfbar ist.

```
Typ A – Faktischer Claim (CL-1 bis CL-4)
  Empirisch prüfbar, quantifizierbar, kausal oder komposit
  → PV zuständig, weiter zu V1

Typ B – Philosophisch/normativer Input
  Rein wertend, logisch-analytisch, kein empirischer Kern
  → PV nicht zuständig
  → Ausgabe: "Primär philosophisch/normativer Input.
     PV prüft nur extrahierbare faktische Teilclaims.
     Für normative Analyse: Probatio Philosophica (PP) empfohlen."
  → Optional: faktische Teilclaims extrahieren und als CL-1/2/3/4 weiterführen

Typ C – Hybrid (philosophisch + faktische Teilclaims)
  Dokument enthält beide Ebenen
  → PV teilweise zuständig
  → Ausgabe: "Hybrides Dokument. PV extrahiert und prüft
     nur die faktischen Teilclaims. Normative Argumente
     liegen außerhalb des PV-Prüfrahmens."
  → Weiter zu V1 mit extrahierten Claims
```

V0-Artefakt (bei Typ B und C ausgeben):
```
[V0-ZUSTÄNDIGKEIT]
Input-Typ   : A (faktisch) | B (philosophisch) | C (hybrid)
PV-Zuständig: vollständig | teilweise | nicht
Extrahierte Claims: [n] faktische Teilclaims identifiziert
```

### V1 · Einheitenklärung
import pathlib, sys

# Restliche Chunks 03-18 der PV v2.0 Datei
target = pathlib.Path(r'D:\Yoka\Workspace\Provolution-main\06_CANON\07_Probatio_Veritatis_v2.0.md')

chunks = [
r"""Maßgröße, Bezugsraum, Zeitraum → c(op)

### V2 · Prüfbarkeitsklärung
- Vollständig → weiter
- Teilweise → prüfbare Teile, Rest kennzeichnen
- Nicht prüfbar → BLOCK

### V3 · Domänenzuweisung
PV-Klima (IPCC, UBA, Provolution-CANON) | PV-Gesundheit (WHO, Cochrane) |
PV-Wirtschaft (Destatis, IWF) | PV-Politik (Bundestag, EUR-Lex) | PV-Default

### V4 · Quellenerhebung und n-Bestimmung
```
n >= 3  ->  MMM inaktiv
n <  3  ->  MMM aktiv
n =  0  ->  BLOCK
```

VFP-Artefakt (immer ausgeben):
```
[VFP-ARTEFAKT]
Claim-Typ   : CL-[1/2/3/4]
c(op)       : "[operationalisiert]"
Prüfbarkeit : vollständig | teilweise | nicht prüfbar
Domäne      : PV-[...]
n (Quellen) : [Anzahl]
MMM-Status  : aktiv (n<3) | inaktiv (n>=3)
VFP-Status  : PASS | BLOCK
```
""",
r"""
---

## 4. SEC-J-PRÜFUNG V2.0

### S · Sufficient
```
S(c) = EG(c) × Aktualitätsfaktor × n-Faktor

EG-1 (Metaanalysen):           0,85-1,00
EG-2 (Primärstudie/Statistik): 0,60-0,84
EG-3 (Sekundärquelle):         0,35-0,59
EG-4 (keine Quelle):           0,00-0,34

Aktualitätsfaktor Standard:
  <=2J->1,00 | 3-5J->0,85 | 6-10J->0,70 | >10J->0,50
  Historische Fakten: immer 1,00

Aktualitätsfaktor PV-Klima (verschärft):
  <=1J->1,00 | 2-3J->0,85 | 4-6J->0,65 | >6J->0,45

n-Faktor (Dynamic Source Rule):
  n >= 3 -> 1,00
  n =  2 -> 0,80
  n =  1 -> 0,55
```
""",
r"""Anti-Halluzinations-Regel: System nutzt exakt n vorhandene Quellen.
Vertrauen sinkt mathematisch durch n-Faktor – keine Quellenerfindung.

### E · Efficient
```
E(c) = 1 - (Abweichungen × 0,25)   [min: 0,00]

Abweichungstypen (je -0,25):
  Zahlenfehler | Bezugsraumfehler | Zeitfehler | Kausalitätssprung
```

### C_ext · Consistent (empirisch)
```
C_ext(c) = 1 - (Widersprüche / Vergleichsquellen)
mind. 3 Vergleichsquellen (n-Faktor wenn n < 3)

C_ext-Veto: C_ext < 0,50 -> FALSE (automatisch)
```

CANON_CONFLICT_FLAG:
Neue EG-1-Quelle widerspricht Kanon ->
  kein sofortiger Override
  -> PT-Übergabe: "Mögliche Kanonrevision"
  -> Kanonrevision erst bei n >= 3 unabhängigen EG-1-Quellen

### C_int · Consistent (logisch)
```
Stufe 1 – Unmöglichkeits-Veto:
""",
r"""  Verstößt gegen formale Logik oder Naturgesetze
  -> sofortiges FALSE (kein Score, kein Override)

Stufe 2 – Konsistenz-Malus:

  MMM inaktiv (n >= 3):
    Partieller Logikfehler   -> C_int-Malus: -0,10
    Systemischer Logikfehler -> C_int-Malus: -0,35
    Unmöglichkeit            -> FALSE (Veto)

  MMM aktiv (n < 3):
    Partieller Bruch (Mikro):
      "Logik gilt nur unter spezifischen Randbedingungen"
      -> C_int-Malus: -0,10

    Systemischer Bruch (Makro):
      "Logik kollabiert auf Gesamtsystemebene"
      -> C_int-Malus: -0,35

    Universeller Bruch:
      "Mathematisch/physikalisch unmöglich auf allen Skalen"
      -> FALSE (Veto, unabhängig von n)

C_int(c) = 1,00 - C_int-Malus   [min: 0,00]
```

Veto-Klarstellung:
  C_ext-Veto = empirisch: Claim widerspricht Vergleichsquellen (externe Evidenz)
  C_int-Veto = logisch: Claim verstößt gegen Logik/Naturgesetze (intern, quellenunabhängig)
  MMM-Veto   = Skalenbruch: Logik kollabiert auf Makro (nur wenn n<3, Teil von C_int)
""",
r"""Sparparadoxon-Beispiel (CL-2, MMM-Demonstration):
  Mikro: "Haushalt spart 500 EUR -> gut für den Haushalt" -> C_int hoch
  Makro: "Alle sparen -> Nachfrageeinbruch -> BIP sinkt"
  -> MMM: systemischer Bruch -> C_int-Malus -0,35

### J · Justice
```
J(c) = (0,25×J1) + (0,30×J2) + (0,25×J3) + (0,20×J4)

J1 Sprecherposition | J2 Auslassung | J3 Vulnerabilität | J4 Partizipation

J-Veto: J < 0,40 -> HARMFUL FRAMING (Flag, kein automatisches FALSE)
```

---

## 5. AGGREGATION UND VERDICT

### PV v2.0 Gesamtformel
```
PV(c) = (0,30×S) + (0,20×E) + (0,20×C_ext) + (0,15×C_int) + (0,15×J)

Gewichtung:
  S     = 0,30  (Evidenztiefe)
  E     = 0,20  (Quellennutzung)
  C_ext = 0,20  (empirische Konsistenz)
  C_int = 0,15  (logische Konsistenz)
  J     = 0,15  (Framing-Symmetrie)
  Summe = 1,00
""",
r"""C gesamt = 0,35 (identisch zu v1.0 – nur aufgespalten für Transparenz)
```

### Verdict-Schwellen
| PV(c) | Verdict |
|---|---|
| >= 0,80 | VERIFIED |
| 0,50-0,79 | UNCERTAIN |
| 0,20-0,49 | FALSE |
| < 0,20 | FABRICATED |
| C_ext < 0,50 | FALSE (C_ext-Veto: empirischer Widerspruch) |
| C_int = 0 | FALSE (C_int-Veto: logische Unmöglichkeit) |
| J < 0,40 | + Flag: HARMFUL FRAMING |
| CANON_CONFLICT | + Flag: PT-Übergabe |

Veto-Klarstellung:
  C_ext-Veto = empirisch: Claim widerspricht Vergleichsquellen
  C_int-Veto = logisch: Claim verstößt gegen Logik/Naturgesetze
  MMM-Veto   = Skalenbruch: Teil von C_int, Logik kollabiert auf Makro

### UNSUBSTANTIATED (neu in v2.0)
```
Bedingungen (alle drei müssen gelten):
  C_int > 0    (logisch möglich)
  S < EG-3     (empirisch unbelegt)
  C_ext intakt (nicht widerlegt)

-> Verdict: UNSUBSTANTIATED
-> Bedeutung: logisch möglich, Beweislast nicht erfüllt
-> Automatische PT-Übergabe zur Trendbeobachtung
```
""",
r"""### PT-Brücke
```
PT-Übergabe wird ausgelöst bei:
  UNSUBSTANTIATED-Verdict
  CANON_CONFLICT_FLAG
  n = 1 mit EG-1 (starke Einzelquelle)

PT beobachtet:
  Score-Drift über Zeit (wird n größer?)
  Kanonrevisions-Schwelle: n >= 3 EG-1-Quellen
  Trend-Status: EMERGING | STABLE | DECLINING
```

---

## 6. OUTPUT-STRUKTUR V2.0

```
PV-REPORT v2.0 · [Datum] · Claim-ID: [UUID]

INPUT:
  Claim: "[Text]"
  Typ: CL-[1/2/3/4]
  c(op): "[operationalisiert]"

[VFP-ARTEFAKT]
  n: [x] | MMM: aktiv/inaktiv

SCORES:
  S      = [x] · EG:[x] · Aktual.:[x] · n-Faktor:[x]
  E      = [x] · Abweichungen: [...]
""",
r"""  C_ext  = [x] · Widersprüche:[x] / Quellen:[x]
  C_int  = [x] · Malus:[x] · MMM:[aktiv/inaktiv]
  J      = [x] · J1-J4: [x,x,x,x]

[Falls MMM aktiv:]
  MMM-SKALIERUNG:
    Mikro: [Befund]
    Makro: [Befund]
    Bruch: partiell | systemisch | universell

AGGREGATION:
  PV = (0,30×S)+(0,20×E)+(0,20×C_ext)+(0,15×C_int)+(0,15×J) = [x]

VERDICT: [VERIFIED / UNCERTAIN / FALSE / FABRICATED / UNSUBSTANTIATED]
[Flags: HARMFUL FRAMING | CANON_CONFLICT+PT]

BEGRÜNDUNG: [S/E/C_ext/C_int/J/Verdict je 1-2 Sätze]
QUELLEN: [1][...] [2][...] [3][...]
EINSCHRÄNKUNGEN: [...]

[Falls PT-Übergabe:]
  PT-STATUS: EMERGING
  n aktuell: [x] / Ziel: 3 EG-1-Quellen
```

---

## 7. VERGLEICH V1.0 -> V2.0

| Merkmal | v1.0 | v2.0 |
|---|---|---|
| Formel | 0,30S+0,20E+0,35C+0,15J | 0,30S+0,20E+0,20C_ext+0,15C_int+0,15J |
| C-Dimension | einfach | aufgespalten |
""",
r"""| Quellenregel | mind. 3 (starr) | n-Skalierung (flexibel) |
| Verdicts | 4 | 5 (+UNSUBSTANTIATED) |
| Vorfilter | MMM-Vorfilter | VFP |
| MMM | immer aktiv | nur n < 3 |
| PT-Kopplung | keine | UNSUBSTANTIATED + CANON_CONFLICT |
| C-Gesamtgewicht | 0,35 | 0,35 (rückwärtskompatibel) |

---

## 8. FALSIFIZIERBARKEIT

| Parameter | Wert | Anpassungsbedingung |
|---|---|---|
| n-Faktor n=2 | 0,80 | Empirisch kalibrierbar |
| n-Faktor n=1 | 0,55 | Empirisch kalibrierbar |
| C_int-Malus partiell | -0,10 | Kalibrierungsstudie |
| C_int-Malus systemisch | -0,35 | Kalibrierungsstudie |
| C_ext-Veto | 0,50 | Anpassbar |
| UNSUBSTANTIATED-Schwelle | EG-3 | Anpassbar |

---

## LICENSE

CC0 1.0 Universal + Open Humanity License. See LICENSE.md.

---

*CANON-Referenz: 07_Probatio_Veritatis_v2.0.md · Version 2.0 · 2026-04-09 · Tobias Yoka Dietz*
*Vorgänger: 07_Probatio_Veritatis_v1.0.md*

---

## 9. AUSGABEMODI (NEU IN V2.0)

PV v2.0 unterstützt zwei Ausgabemodi.

### Modus A: EXPERT (Standard)
Vollständiger Begründungspfad mit allen Scores, Formeln und Flags.
Befehl: `PV:EXPERT` oder kein Befehl (Standard)
""",
r"""### Modus B: PLAIN (Laiensprache)

Fließtext, keine Formeln, keine Scores, kein Fachjargon.
Befehl: `PV:PLAIN`

```
PV-BERICHT · [Datum]

BEHAUPTUNG:
"[Originaltext des Claims]"

WAS WURDE GEPRÜFT:
[1-2 Sätze: Was genau analysiert, welcher Zeitraum, welcher Bezug.]

ERGEBNIS: [BESTÄTIGT / UNSICHER / FALSCH / HALTLOS / UNBELEGT]

WAS DAS BEDEUTET:
[2-3 Sätze in einfacher Sprache. Keine Fachbegriffe. Analogien erlaubt.]

WIE SICHER SIND WIR?
[1-2 Sätze über Quellenlage und Vertrauen ins Ergebnis.]

WAS SPRICHT DAFÜR, WAS DAGEGEN?
[2-3 Sätze. Stärkste Evidenz beider Seiten.]

WICHTIGE EINSCHRÄNKUNG:
[1 Satz: Was nicht geprüft werden konnte.]

[Nur wenn HARMFUL FRAMING:]
ACHTUNG – EINSEITIGE DARSTELLUNG:
[1-2 Sätze: Welche Perspektive fehlt, keine politische Wertung.]

[Nur wenn PT-Übergabe:]
BEOBACHTUNG LÄUFT:
[1 Satz: Behauptung wird weiter beobachtet, Datenlage noch dünn.]
```

Übersetzungstabelle Verdicts:
| Expert | Plain | Bedeutung |
|---|---|---|
| VERIFIED | BESTÄTIGT | Durch mehrere Quellen belegt |
| UNCERTAIN | UNSICHER | Hinweise vorhanden, Beleglage nicht stark genug |
| FALSE | FALSCH | Widerspricht Studien und Daten |
| FABRICATED | HALTLOS | Keine Grundlage, widerspricht gesichertem Wissen |
| UNSUBSTANTIATED | UNBELEGT | Logisch möglich, aber nicht belegt |
""",
r"""Verhaltensregeln Modus B:
1. Keine Scores im Text
2. Keine Fachbegriffe (EG-1, C_int, VFP)
3. Analogien erlaubt und erwünscht
4. Max. 250 Wörter Fließtext
5. Ton: sachlich und zugänglich
6. UNSUBSTANTIATED nicht alarmistisch
7. HARMFUL FRAMING nie als politische Aussage

---

## 10. SYSTEMSTABILISIERUNGS-REGELN (NEU IN V2.0 POST-TEST)

### Regel S1: MMM ist Logik-Tool, nicht Quellen-Tool
```
FALSCH: MMM inaktiv weil n >= 3
RICHTIG: MMM aktivieren wenn:
  (1) n < 3  ODER
  (2) Claim-Typ = CL-2 (kausal)  ODER
  (3) C_int-Analyse identifiziert Skalenbruch-Kandidaten

Begründung: Das Sparparadoxon (CL-2, n=5) braucht MMM
unabhängig von der Quellenanzahl.
```

### Regel S2: Veto-Transparenz bei Score-Veto-Divergenz
```
Wenn Veto aktiv UND PV(c) > 0,50:
  → VETO-GRUND explizit ausgeben
  → SCORE-HINWEIS ausgeben
  → "Veto-Logik hat Vorrang vor Aggregation" erklären
```

### Regel S3: C_int-Veto vs. C_ext-Veto – strikte Trennung
```
C_int-Veto = deduktiv (Logik/Naturgesetze/Skalenbruch)
  → kein empirisches Quellenmaterial nötig

C_ext-Veto = induktiv (empirischer Widerspruch zu Quellen)
  → Vergleichsquellen müssen benannt werden

FEHLER: Skalenbruch (C_int) als C_ext-Veto deklarieren
→ macht System "leseabhängig" statt "denkfähig"
```

---

*Systemstabilisierungs-Regeln hinzugefügt nach Test-Vergleich v2.0 vs. v2.1 · 2026-04-09*
