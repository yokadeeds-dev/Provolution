# PS-Familie – Kanonische Übersicht
## Probatio Systemica · Alle Module · Single Source of Truth
### CANON-Dokument · Version 1.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz
**Status:** Kanonisch · peer-review-vorbereitet

---

## 0. STRUKTURPRINZIP

Probatio Systemica (PS) ist ein modulares Framework. Jedes Modul
wendet die SEC-J-Logik auf einen anderen Prüfgegenstand an.
Alle Module teilen dieselbe mathematische Basis – sie unterscheiden
sich in Prüfobjekt, Gewichtung und Verdicts.

**Strikte Trennung:**
- **VFP (Vorfilter-Protokoll):** Eintrittscheck für alle Module.
  Klärt Einheit, Prüfbarkeit, Domäne. Immer aktiv.
- **MMM (Mikro-Makro-Matching):** Skalierungsprüfung.
  Ursprüngliche PS-Definition: prüft ob Logik auf Mikro genauso
  gilt wie auf Makro. In PV: aktiv bei n<3 ODER CL-2 ODER
  C_int-Kandidat. In PP: immer aktiv bei AT-1/2/3.
- **MMM ist Logik-Tool, kein Quellen-Tool.**

---

## 1. MODULÜBERSICHT

| Modul | Name | Prüfobjekt | Kernfrage |
|---|---|---|---|
| PS-U | Probatio Systemica Universal | Maßnahme / System | Systemisch tragfähig? |
| PV | Probatio Veritatis | Faktischer Claim | Empirisch haltbar? |
| PD | Probatio Deliberativa | Politische Entscheidung | Prozessual SEC-J-konform? |
| PI | Probatio Institutionalis | Institution | Anspruch = Realität? |
| PN | Probatio Narrativa | Mediendiskurs | Wer spricht, wer fehlt? |
| PP | Probatio Philosophica | Philosophisches Argument | Logisch konsistent? |
| PT | Probatio Temporalis | Zeit / Score-Drift | Hat sich die Lage verändert? |


---

## 2. FORMELN

```
PS-U: SEC-J(m) = (0,30×S) + (0,25×E) + (0,30×C) + (0,15×J)

PV:   PV(c)   = (0,30×S) + (0,20×E) + (0,20×C_ext) + (0,15×C_int) + (0,15×J)
      C gesamt = 0,35 (aufgespalten: C_ext=0,20 + C_int=0,15)

PD:   PD(d)   = (0,30×S) + (0,20×E) + (0,25×C) + (0,25×J)

PI:   PI(i)   = (0,30×S) + (0,20×E) + (0,25×C) + (0,25×J)

PN:   PN(n)   = (0,20×S) + (0,15×E) + (0,25×C) + (0,40×J)

PP:   PP(a)   = (0,25×S) + (0,25×E) + (0,35×C) + (0,15×J)

PT:   Keine eigene Formel – orchestriert andere Module über Zeit
      Drift: Delta(t0->tn) = Score(tn) - Score(t0)
```

---

## 3. GEWICHTUNGSLOGIK

| Modul | S | E | C | J | Dominante Dim. |
|---|---|---|---|---|---|
| PS-U | 0,30 | 0,25 | 0,30 | 0,15 | S/C gleichwertig |
| PV | 0,30 | 0,20 | 0,35* | 0,15 | C dominant |
| PD | 0,30 | 0,20 | 0,25 | 0,25 | S führend, J/C paritätisch |
| PI | 0,30 | 0,20 | 0,25 | 0,25 | S führend, J/C paritätisch |
| PN | 0,20 | 0,15 | 0,25 | 0,40 | J dominant |
| PP | 0,25 | 0,25 | 0,35 | 0,15 | C dominant |
| PT | – | – | – | – | Delta (Drift) |

*PV: C = C_ext (0,20) + C_int (0,15)

---

## 4. VETO-LOGIK

| Modul | Veto-Bedingung | Konsequenz |
|---|---|---|
| PV | C_ext < 0,50 | FALSE (automatisch) |
| PV | C_int = 0 | FALSE (Logik-Unmöglichkeit) |
| PV | J < 0,40 | Flag: HARMFUL FRAMING |
| PV | CANON_CONFLICT | Flag: PT-Übergabe |
| PD | C < 0,40 | Flag: STRUKTURELLER WIDERSPRUCH |
| PD | J < 0,40 | Flag: DEMOKRATIEDEFIZIT |
| PI | C < 0,40 | Flag: STRUKTURELLE INKONSISTENZ |
| PI | J < 0,40 | Flag: EXKLUSIONSRISIKO |
| PN | C < 0,40 | Flag: DISKURSINKONSISTENZ |
| PN | J < 0,40 | Flag: STRUKTURELLE AUSBLENDUNG |
| PP | Performativer Widerspruch | INKOHÄRENT (Veto, sofort) |
| PP | C_ext < 0,40 | Flag: TRADITIONSWIDERSPRUCH |
| PP | J < 0,40 | Flag: PERSPEKTIVMANGEL |
| PT | Volatilität > ±0,20 | Flag: INSTABIL |

**Veto-Transparenz-Regel:** Wenn Veto aktiv bei Score > 0,50:
VETO-GRUND + SCORE-HINWEIS ausgeben.
Veto-Logik hat immer Vorrang vor mathematischer Aggregation.


---

## 5. VERDICT-SYSTEME

### PV
| Score | Verdict | Plain (DE) |
|---|---|---|
| >= 0,80 | VERIFIED | BESTÄTIGT |
| 0,50-0,79 | UNCERTAIN | UNSICHER |
| 0,20-0,49 | FALSE | FALSCH |
| < 0,20 | FABRICATED | HALTLOS |
| Sonder | UNSUBSTANTIATED | UNBELEGT |

### PD
| Score | Verdict | Plain (DE) |
|---|---|---|
| >= 0,80 | KONFORM | ORDNUNGSGEMÄSS |
| 0,60-0,79 | BEDINGT KONFORM | MIT MÄNGELN |
| 0,40-0,59 | DEFIZITÄR | ERHEBLICH MANGELHAFT |
| < 0,40 | NICHT KONFORM | NICHT ORDNUNGSGEMÄSS |

### PI
| Score | Verdict | Plain (DE) |
|---|---|---|
| >= 0,80 | INTEGER | GLAUBWÜRDIG |
| 0,60-0,79 | BEDINGT INTEGER | BEDINGT GLAUBWÜRDIG |
| 0,40-0,59 | DEFIZITÄR | GROSSE LÜCKEN |
| < 0,40 | NICHT INTEGER | NICHT GLAUBWÜRDIG |

### PN
| Score | Profil | Plain (DE) |
|---|---|---|
| >= 0,75 | AUSGEWOGEN | AUSGEWOGEN |
| 0,55-0,74 | EINSEITIG | EINSEITIG |
| 0,35-0,54 | STARK VERZERRT | STARK EINSEITIG |
| < 0,35 | PROPAGANDISTISCH | IRREFÜHREND |

### PP
| Score | Verdict | Plain (DE) |
|---|---|---|
| >= 0,80 | KOHÄRENT | IN SICH STIMMIG |
| 0,60-0,79 | BEDINGT KOHÄRENT | ÜBERWIEGEND STIMMIG |
| 0,40-0,59 | KONTROVERS | WIDERSPRÜCHLICH |
| < 0,40 | INKOHÄRENT | IN SICH WIDERSPRÜCHLICH |

### PT
| Drift | Trend-Status | Plain (DE) |
|---|---|---|
| Delta > +0,15 | EMERGING | IN ENTWICKLUNG |
| Delta nahe Schwelle | CONVERGING | KURZ VOR ÄNDERUNG |
| Delta ±0,05 | STABLE | STABIL |
| Delta < -0,15 | DECLINING | VERSCHLECHTERT SICH |
| Verdictänderung | REVERSED | GEÄNDERT |
| Volatilität >±0,20 | INSTABIL | NOCH UNKLAR |


---

## 6. MODULKOPPLUNG

```
PV  --UNSUBSTANTIATED/CANON_CONFLICT-->  PT
PD  --STRUKTURELLER WIDERSPRUCH------->  PT
PI  --STRUKTURELLE INKONSISTENZ------->  PT
PN  --STRUKTURELLE AUSBLENDUNG-------->  PT
PP  --KONTROVERS/INKOHÄRENT----------->  PT
PT  --Kanonrevisions-Empfehlung------>  CANON (manuell bestätigt)

PV  --V0 Typ B/C------------------->  PP (philosophische Ebene)
PD  --normative Begründung----------->  PP
PI  --Leitbild-Kohärenz-------------->  PP
```

---

## 7. SYSTEMSTABILISIERUNGS-REGELN (KANONISCH)

**S1 – MMM ist Logik-Tool:**
MMM aktivieren bei: n<3 ODER CL-2 (kausal) ODER C_int-Kandidat.
NICHT: MMM inaktiv nur weil n>=3.

**S2 – Veto-Transparenz:**
Veto bei Score > 0,50 → VETO-GRUND + SCORE-HINWEIS Pflicht.

**S3 – C_int vs. C_ext Trennung:**
Skalenbruch (MMM) → immer C_int, nie C_ext.
C_int = deduktiv. C_ext = induktiv (Quellen nötig).

**S4 – PT empfiehlt, nie entscheidet:**
Alle Kanonrevisionen erfordern manuelle Bestätigung durch Yoka.

**S5 – PP ist kein Ethik-Schiedsrichter:**
PP urteilt nicht welche Ethik-Tradition richtig liegt.
PP prüft ob ein Argument die eigenen Regeln einhält.

---

## 8. ABGRENZUNGSREGEL (KANONISCH)

> "PS-U bewertet ob eine Maßnahme systemisch tragfähig ist.
> PV bewertet ob Behauptungen darüber faktisch haltbar sind.
> PD bewertet ob die Entscheidung dafür SEC-J-konform getroffen wurde.
> PI bewertet ob die Institution, die sie umsetzt, ihren Anspruch erfüllt.
> PN bewertet ob der Diskurs darüber alle Perspektiven abbildet.
> PP bewertet ob die philosophische Begründung dahinter konsistent ist.
> PT bewertet ob sich die Wahrheitslage über Zeit verändert hat."

**Routing nach Objekt-Typ — häufiger Mismatch:** Eine *Behauptung* gehört in **PV**, nicht in PS-U (Verführung: alles durch das Flaggschiff SEC-J jagen). Worked example + Entscheidungshilfe: [`studies/PV_DEMO_2026-05-30/`](../../studies/PV_DEMO_2026-05-30/PV_DEMO.md) (Blüm: PS-U-Lesart 0,33 vs. PV-korrekt FALSE via Logik-Veto).

---

## 9. CANON-DATEISTRUKTUR

| Datei | Modul |
|---|---|
| 00_PS_Familie_Uebersicht.md | Übersicht (dieses Dokument) |
| 01_Band1_SEC_Kanon.md | PS Grundlagen |
| 02_Entscheidungskarte.md | Band 2 |
| 03_Band3_Scientific_Core.md | Band 3 |
| 04_Band4_Anwendungen_v4.2.md | Provolution |
| 05_Band5_Steuerung_Score.md | Band 5 |
| 06_framework_extensions_v1.0_SECJ.md | PS-U |
| 07_Probatio_Veritatis_v2.0.md | PV v2.0 |
| 11_Probatio_Deliberativa_v1.0.md | PD |
| 12_Probatio_Institutionalis_v1.0.md | PI |
| 13_Probatio_Narrativa_v1.0.md | PN |
| 14_Probatio_Philosophica_v1.0.md | PP |
| 15_Probatio_Temporalis_v1.0.md | PT |

---

## LICENSE

CC0 1.0 Universal + Open Humanity License. See LICENSE.md.

---

*CANON-Referenz: 00_PS_Familie_Uebersicht.md · Version 1.0 · 2026-04-09*
*Tobias Yoka Dietz · Single Source of Truth für alle PS-Module*
