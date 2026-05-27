# Probatio Philosophica (PP)
## Submodul von Probatio Systemica · SEC-J-Prüfung philosophischer Argumente
### CANON-Dokument · Version 1.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz · **Basis:** PS-U

---

## 0. PRÄAMBEL

**Probatio Philosophica (PP)** prüft ob ein philosophisches Argument intern
konsistent, argumentationseffizient und perspektivgerecht ist. PP ist nicht PV –
es prüft keine empirischen Fakten, sondern logische Struktur.

PP schließt die Lücke wenn PV Typ-B/C-Input meldet (philosophisch/normativ).

Kernfrage: **Ist dieses Argument logisch konsistent und normativ vertretbar?**

PP ist kein Ethik-Schiedsrichter. PP prüft ob ein Argument die eigenen Regeln einhält.

---

## 1. ABGRENZUNG

| Merkmal | PV | PS-U | PP |
|---|---|---|---|
| Prüfobjekt | Faktischer Claim | Maßnahme | Philosophisches Argument |
| Kernfrage | Empirisch haltbar? | Systemisch tragfähig? | Logisch konsistent? |
| S | Evidenzbreite | Wirkungsausmaß | Prämissenstärke |
| E | Quellennutzung | Ressourceneffizienz | Argumentationseffizienz |
| C | Empirische Konsistenz | Systemkonsistenz | Interne Logikkonsistenz |
| J | Framing-Symmetrie | Gerechtigkeitsfolgen | Perspektivgerechtigkeit |
| Verdicts | VERIFIED/FALSE | PROBIERT/NICHT | KOHÄRENT/INKOHÄRENT |
| FABRICATED | möglich | n/a | nicht anwendbar |

---

## 2. ARGUMENT-TAXONOMIE

| Typ | Tradition | MMM-Test |
|---|---|---|
| AT-1 | Deontologie (Kant, Ross) | Kategorischer Imperativ |
| AT-2 | Konsequentialismus (Mill, Singer) | Nutzenkalkulation Mikro/Makro |
| AT-3 | Tugendethik (Aristoteles) | Soziale Praktizierbarkeit |
| AT-4 | Metaethik (Moore, Mackie) | Objekt-/Metaebene konsistent? |
| AT-5 | Hybrid/Systemisch | fallabhängig |

---

## 3. VFP – VORFILTER-PROTOKOLL

### V0 · Zuständigkeit
- Philosophisch/normativ → PP zuständig
- Faktisch → PV zuständig
- Hybrid → PP für normative Ebene

### V1 · Argumentklärung
Prämissen P1..Pn + Schlussfolgerung K → a(op)

### V2 · Prüfbarkeit
- Vollständig formuliert → weiter
- Teilweise → Prämissen explizieren
- Nicht formalisierbar → BLOCK

### V3 · Traditionszuweisung
Deontologie | Utilitarismus | Tugendethik | Diskursethik |
Pluralismus | Feministische Ethik | Nicht-westlich

### V4 · Performativer Widerspruchs-Check
```
Widerspricht das Argument den Bedingungen seiner eigenen Äußerung?
Beispiel: "Es gibt keine allgemeinen Wahrheiten"
→ JA: sofortiges INKOHÄRENT (Veto) – keine weiteren Scores
→ NEIN: weiter zu SEC-J
```

VFP-Artefakt:
```
[VFP-ARTEFAKT]
Argument-Typ      : AT-[1/2/3/4/5]
a(op)             : "[operationalisiert]"
Prämissen         : P1=[...] P2=[...] K=[...]
Tradition(en)     : [...]
Perf. Widerspruch : ja (→ INKOHÄRENT) | nein
VFP-Status        : PASS | BLOCK
```


---

## 4. SEC-J-PRÜFUNG

### S · Sufficient (Prämissenstärke)
```
S(a) = PG(a) × Explizitheitsfaktor

PG-1 (breiter Konsens):         0,85-1,00
PG-2 (etablierte Schule):       0,60-0,84
PG-3 (kontrovers, begründet):   0,35-0,59
PG-4 (implizit/unbegründet):    0,00-0,34

Explizitheitsfaktor:
  Alle explizit + begründet   → 1,00
  Hauptprämissen explizit     → 0,85
  Kernprämisse rekonstruierbar→ 0,65
  Mehrere implizit            → 0,40
```

### E · Efficient (Argumentationseffizienz)
```
E(a) = 1 - (Fehlschlüsse × 0,20)   [min: 0,00]

Fehlschluss-Typen (je -0,20):
  Strohmann | Zirkelschluss | Ad hominem | False Dichotomy
  Appeal to Authority | Slippery Slope | Äquivokation
```

### C_ext · Consistent (extern)
```
C_ext(a) = 1 - (Traditionswidersprüche / Referenzrahmen)
Referenzrahmen: mind. 3 Ethiktraditionen
Flag: C_ext < 0,40 → TRADITIONSWIDERSPRUCH
```

### C_int · Consistent (intern) mit MMM – Kant-MMM-Test
```
MMM IMMER AKTIV bei AT-1, AT-2, AT-3 (unabhängig von n)
MMM ist Logik-Tool, kein Quellen-Tool.

Kant-MMM-Test: Ist die Maxime universalisierbar?
  Mikro: Gilt das Prinzip im Einzelfall?
  Makro: Gilt es wenn alle so handeln?

Partieller Bruch (Mikro ok, Makro fragwürdig)  → -0,10
Systemischer Bruch (Universalisierung kollabiert) → -0,35
Performativer Bruch → INKOHÄRENT (Veto)

C_int(a) = 1,00 - Malus   [min: 0,00]
```

### J · Justice (Perspektivgerechtigkeit)
```
J(a) = (0,20×J1) + (0,25×J2) + (0,30×J3) + (0,25×J4)

J1 Traditionszugang | J2 Auslassung | J3 Machtperspektive (höchstes Gew.) | J4 Vulnerabilität

Flag: J < 0,40 → PERSPEKTIVMANGEL
```

---

## 5. AGGREGATION UND VERDICT

```
PP(a) = (0,25×S) + (0,25×E) + (0,35×C) + (0,15×J)

C dominant (0,35): interne Konsistenz härteste Bedingung
S = E = 0,25: gleichwertig
J = 0,15: Perspektiven-Check, kein Ethik-Schiedsrichter
```

| PP(a) | Verdict | Plain (DE) |
|---|---|---|
| >= 0,80 | KOHÄRENT | IN SICH STIMMIG |
| 0,60-0,79 | BEDINGT KOHÄRENT | ÜBERWIEGEND STIMMIG |
| 0,40-0,59 | KONTROVERS | WIDERSPRÜCHLICH |
| < 0,40 | INKOHÄRENT | IN SICH WIDERSPRÜCHLICH |
| Perf. Widerspruch | INKOHÄRENT (Veto) | – |
| C_ext < 0,40 | + Flag: TRADITIONSWIDERSPRUCH | – |
| J < 0,40 | + Flag: PERSPEKTIVMANGEL | – |

Veto-Transparenz: Wenn Veto bei PP > 0,50 → VETO-GRUND + SCORE-HINWEIS Pflicht.

---

## 6. OUTPUT-STRUKTUR

```
PP-REPORT v1.0 · [Datum]
ARGUMENT: "[Kernthese]" | Typ: AT-[x] | a(op): "[...]"
Prämissen: P1=[...] P2=[...] | K=[...]
[VFP-ARTEFAKT]

SCORES:
  S = [x] · PG:[x] · Explizitheit:[x]
  E = [x] · Fehlschlüsse: [Liste oder "keine"]
  C_ext = [x] · Widersprüche:[n]/[Rahmen]
  C_int = [x] · MMM-Befund:[Typ] · Malus:[x]
  J = [x] · J1-J4: [x,x,x,x]

[MMM-KANT-TEST:]
  Mikro: [Befund] | Makro: [Befund]
  Universalisierung: möglich | partiell | kollabiert

PP = (0,25×S)+(0,25×E)+(0,35×C)+(0,15×J) = [x]
VERDICT: [...]
[Flags wenn aktiv]
BEGRÜNDUNG: [je 1-2 Sätze]
FEHLENDE PERSPEKTIVEN: [konkret]
STÄRKSTE GEGENARGUMENTE: [Top 2-3]
```


---

## 7. PRÜFMODI

| Befehl | Funktion |
|---|---|
| PP:EXPERT | Vollständiger Begründungspfad (Standard) |
| PP:PLAIN | Fließtext für Laien, max. 300 Wörter |
| PP:KANT | Nur MMM/Kant-Universalisierungstest |
| PP:J | Nur Perspektivgerechtigkeit |
| PP:STATUS | Prüfstand ausgeben |

---

## 8. BEISPIEL

**Argument:** "Ich verspreche feierlich zu lügen, weil es moralisch richtig ist."

VFP: AT-5 | Performativer Widerspruch: JA → INKOHÄRENT (Veto)

Begründung: Versprechen = Akt der Wahrhaftigkeit. Inhalt (Lüge) widerspricht
Form (Versprechen). Selbsthebend.

MMM zur Illustration: Mikro möglich. Makro: universalisiert kollabiert
Institution des Versprechens → systemischer Bruch bestätigt Veto.

---

## 9. ABGRENZUNGSREGEL (KANONISCH)

> "PV bewertet ob eine Behauptung faktisch haltbar ist.
> PP bewertet ob ein philosophisches Argument intern konsistent
> und normativ vertretbar ist.
> PP fällt kein Urteil darüber welche Ethik-Tradition richtig liegt."

---

## 10. INTEGRATION IN PS-FAMILIE

| Modul | PP-Schnittstelle |
|---|---|
| PV | V0 verweist bei Typ B/C an PP |
| PD | PP prüft normative Begründung |
| PI | PP prüft Leitbild-Kohärenz |
| PN | PP prüft normative Rahmenargumente |
| PT | PP-Scores über Zeit trackbar |

---

## LICENSE

CC0 1.0 Universal + Open Humanity License. See LICENSE.md.

---

*CANON-Referenz: 14_Probatio_Philosophica_v1.0.md · Version 1.0 · 2026-04-09*
*Tobias Yoka Dietz · Submodul von Probatio Systemica · Basis: PS-U*
