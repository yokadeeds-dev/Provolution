# PS-U 2.0 · Provolution Framework Extension · SEC-J Canonical

**Status:** **Canonical** — aufgenommen ins Provolution-Canon 2026-05-10
**Stand:** 2026-05-10
**Vorgänger:** `06_framework_extensions_v1.0_SECJ.md` *(PS-U 1.x, J=0,15, keine J-Veto-Flag)*
**Anlass:** J-Audit 2026-05-10 — PS-U erkennt Ungerechtigkeit nur schwach im STANDARD-Modus + fehlt J-Modus für Achse-10-Maßnahmen

---

## §1 · Identität

**PS-U** *(Probatio Systemica Universal)* ist die framework-neutrale SEC-J-Bewertungs-Engine. Sie prüft eine Maßnahme oder ein System auf systemische Tragfähigkeit.

PS-U ist **nicht** an Provolution gebunden — sie ist universelle SEC-J-Anwendung, einsetzbar in jedem Kontext, der die SEC-J-Methodik adoptiert.

---

## §2 · Modi

PS-U 2.0 hat zwei methodisch unterschiedliche Modi:

| Modus | Aktivierung | Anwendungsfall |
|---|---|---|
| **PS-U:STANDARD** | Default | Maßnahmen auf Achsen 1–9 *(Wasser, Energie, …, Kultur)* |
| **PS-U:JUSTICE** | Achse 10 *(Gerechtigkeit)* primär | Maßnahmen, deren primäres Ziel Gerechtigkeit ist |

Aktivierung über zwei Pfade:

1. **Auto-Aktivierung:** im VFP-V4-Schritt erkennt das System die Primär-Achse. Achse 10 → JUSTICE-Modus. Achsen 1–9 → STANDARD.
2. **Manuell:** `PS-U:JUSTICE` oder `PS-U:STANDARD` als expliziter Modus-Aufruf, überschreibt Auto-Aktivierung.

---

## §3 · PS-U:STANDARD

### Formel

```
SEC-J(m) = (0,30 · S) + (0,25 · E) + (0,30 · C) + (0,15 · J)
```

| Dimension | Gewicht | Bedeutung |
|---|---|---|
| S | 0,30 | Sufficient — wirkt die Maßnahme hinreichend? |
| E | 0,25 | Efficient — ressourcen-effizient? |
| C | 0,30 | Consistent — kohärent mit anderen Maßnahmen + Skalen-invariant? |
| J | 0,15 | Just — gerechtigkeits-konform? |

### Veto- und Flag-Logik

```
S < 0,40   →  Flag UNZUREICHEND (Pflicht-Hinweis, kein Stop)
E < 0,40   →  Flag INEFFIZIENT (Pflicht-Hinweis, kein Stop)
C < 0,40   →  Flag STRUKTURELLER WIDERSPRUCH (Pflicht-Hinweis, kein Stop)
J < 0,40   →  Flag SOZIALE INKONSISTENZ (Pflicht-Hinweis + Empfehlung)   *** NEU in 2.0 ***
```

**Begründung der neuen J-Flag:** in PS-U 1.x fehlte die J-Veto-Flag, was Maßnahmen mit niedrigem J-Score einen unsichtbaren Pass gab, solange S/E/C hoch waren. Die SOZIALE-INKONSISTENZ-Flag schließt diese Lücke.

### Verdict-Schwellen *(unverändert gegenüber 1.x)*

| Score | Verdict | Plain |
|---|---|---|
| ≥ 0,80 | TRAGFÄHIG | TRAGFÄHIG |
| 0,60–0,79 | BEDINGT TRAGFÄHIG | TEILWEISE TRAGFÄHIG |
| 0,40–0,59 | DEFIZITÄR | NICHT TRAGFÄHIG |
| < 0,40 | NICHT TRAGFÄHIG | NICHT TRAGFÄHIG |

---

## §4 · PS-U:JUSTICE

### Formel *(neu)*

```
SEC-J(m, justice) = (0,25 · S) + (0,15 · E) + (0,20 · C) + (0,40 · J)
```

| Dimension | Gewicht | Bedeutung |
|---|---|---|
| S | 0,25 | Sufficient |
| E | 0,15 | Efficient |
| C | 0,20 | Consistent |
| J | **0,40** | Just — **dominant** |

### Begründung der J-Dominanz

Maßnahmen auf Achse 10 *(Gerechtigkeit)* haben Justice als **primären Zweck**, nicht als Eigenschaft. Eine Reparations-Maßnahme, die ressourcen-effizient ist, aber die Reparation falsch verteilt, verfehlt ihren Zweck — daher J=0,40 dominant.

Analog zu PN *(Probatio Narrativa, J=0,40)*, weil Mediendiskurs auch primär gerechtigkeits-distributiv-relevant ist.

### Veto- und Flag-Logik *(strenger als STANDARD)*

```
J < 0,50  →  J-VETO HARD STOP  (Verlustbegrenzungs-Komponente des Antifragility-Prinzips)
              Maßnahme blockiert, Score wird zwar angezeigt, aber Verdict = J-VETO
              Hinweis: warum geblockt + Empfehlung zur Korrektur

J 0,50–0,59  →  Flag JUSTICE-MARGINAL
                  Empfehlung zur Verstärkung der J-Wirkung

J ≥ 0,60  →  Pass (kein Flag)

C < 0,40   →  Flag STRUKTURELLER WIDERSPRUCH (wie STANDARD)
S < 0,40   →  Flag UNZUREICHEND (wie STANDARD)
E < 0,40   →  Flag INEFFIZIENT (wie STANDARD)
```

**Begründung der J<0,50-Hard-Stop-Schwelle:** das Antifragility-Prinzip *(siehe `canon/de/ANTIFRAGILITY_PRINCIPLE.md`)* legt J<0,50 als hartes Veto fest. PS-U:STANDARD nutzt eine weichere J<0,40-Flag, weil Justice dort Bewertungs-Filter ist; PS-U:JUSTICE setzt die Antifragility-Schwelle als Hard-Stop, weil hier Justice der Zweck ist.

### Verdict-Schwellen *(JUSTICE-Modus)*

| Score | Verdict | Plain |
|---|---|---|
| ≥ 0,80 | JUSTICE-TRAGFÄHIG | GERECHT WIRKSAM |
| 0,60–0,79 | BEDINGT JUSTICE-TRAGFÄHIG | TEILWEISE GERECHT |
| 0,40–0,59 | DEFIZITÄR | UNZUREICHEND GERECHT |
| < 0,40 oder J<0,50 | J-VETO | NICHT GERECHT |

---

## §5 · VFP-V4 Achsen-Erkennung *(neu)*

Erweiterung des Vorfilter-Protokolls um eine Achsen-Zuordnung.

```
[VFP V4] Achsen-Zuordnung

Frage 1: Auf welcher Achse sitzt die geprüfte Maßnahme primär?
  Optionen:
    1. Wasser           (Cluster I · Physisches Substrat)
    2. Energie          (Cluster I)
    3. Nahrung          (Cluster I)
    4. Wohnen           (Cluster II · Lebens-Räume)
    5. Gesundheit       (Cluster II)
    6. Mobilität        (Cluster II)
    7. Bildung          (Cluster III · Wissen & Bedeutung)
    8. Information      (Cluster III)
    9. Kultur           (Cluster III)
    10. Gerechtigkeit   (Cluster IV · Soziales Substrat)

Frage 2: Sekundär-Achsen (optional)?
  Liste weiterer betroffener Achsen.

Modus-Auto-Aktivierung:
  Primär = Achsen 1–9    →  PS-U:STANDARD
  Primär = Achse 10      →  PS-U:JUSTICE

Manueller Override:
  `PS-U:STANDARD` oder `PS-U:JUSTICE` überschreibt VFP-V4-Auto-Erkennung.
```

### VFP-Artefakt *(erweitert)*

```
[VFP-ARTEFAKT]
Eingangstyp     : ST-[1/2/3/4]
Primär-Achse    : [1–10] · [Achsen-Name] · [Cluster I/II/III/IV]
Sekundär-Achsen : [Liste]
Aktiver Modus   : PS-U:STANDARD | PS-U:JUSTICE
Modus-Quelle    : VFP-V4-Auto | Manueller Override
VFP-Status      : PASS | BLOCK
```

---

## §6 · Output-Format

### PS-U:FULL *(Vollständiger Begründungspfad)*

Reihenfolge wie etablierte Sub-Gem-Konvention: Fazit zuerst, Details darunter.

```
PS-U-REPORT v2.0 · [Datum] · ID: [UUID]

════════════════════════════════════════════
FAZIT
════════════════════════════════════════════

MAßNAHME: "[Originaltext]"
MODUS: PS-U:[STANDARD|JUSTICE]
PRIMÄR-ACHSE: [Achsen-Name]

VERDICT: [TRAGFÄHIG / BEDINGT TRAGFÄHIG / DEFIZITÄR / NICHT TRAGFÄHIG / J-VETO]
SCORE: [x]
[Flags: SOZIALE INKONSISTENZ | JUSTICE-MARGINAL | STRUKTURELLER WIDERSPRUCH | …]

KERN: [1-2 Sätze]

════════════════════════════════════════════
DETAILS
════════════════════════════════════════════

[VFP-ARTEFAKT]
SCORES:
  S = [x]  ·  E = [x]  ·  C = [x]  ·  J = [x]

AGGREGATION:
  STANDARD: 0,30·S + 0,25·E + 0,30·C + 0,15·J = [x]
  JUSTICE:  0,25·S + 0,15·E + 0,20·C + 0,40·J = [x]

BEGRÜNDUNG:
  S: [...]
  E: [...]
  C: [...]
  J: [...]

[Falls J-VETO:
J-VETO-BEGRÜNDUNG:
  J = [x] < 0,50 (JUSTICE-Modus, Antifragility-Prinzip)
  Korrektur-Empfehlung: [konkret]
]

EMPFEHLUNGEN: [...]
QUELLEN: [...]
EINSCHRÄNKUNGEN: [...]

────────────────────────────────────────────
Weitere Modi: `PS-U:FULL` · `PS-U:LITE` · `PS-U:PLAIN` · `PS-U:STANDARD` · `PS-U:JUSTICE` · `PS-U:J` · `PS-U:VFP` · `PS-U:STATUS`
```

### Weitere Modi

- `PS-U:LITE` — Verdict + 1 Satz
- `PS-U:PLAIN` — Laiensprache, max. 250 Wörter
- `PS-U:J` — nur J-Analyse
- `PS-U:VFP` — nur VFP-Artefakt *(inkl. neuem V4)*
- `PS-U:STATUS` — Prüfstand
- `PS-U:STANDARD` — manueller Standard-Override
- `PS-U:JUSTICE` — manueller Justice-Override

---

## §7 · Verhaltensregeln *(unverändert + ergänzt)*

Bestehende Verhaltensregeln aus PS-U 1.x bleiben gültig. **Neu:**

- **R-NEU-1:** VFP-V4 ist Pflicht — kein SEC-J ohne Achsen-Zuordnung
- **R-NEU-2:** SOZIALE-INKONSISTENZ-Flag *(STANDARD-Modus, J<0,40)* ist Pflicht-Hinweis, auch bei hohem Gesamt-Score
- **R-NEU-3:** J-VETO-Hard-Stop im JUSTICE-Modus ist nicht verhandelbar — Score-Anzeige ohne Verdict-Pass
- **R-NEU-4:** Modus-Wechsel transparent dokumentieren — wenn manueller Override, im Output ausweisen

---

## §8 · Bezug zu anderen Modulen

| Modul | Beziehung |
|---|---|
| **PS** *(Entry-Gem)* | routet zu PS-U bei framework-neutralen Maßnahmen-Tragfähigkeits-Fragen. Routing-Tabelle erweitern: bei Achse-10-Erkennung explizit `PS-U:JUSTICE` empfehlen |
| **PV** | bei faktischen Behauptungen über Justice-Wirkung *(distributive Aussagen)* — Veritatis prüft Wahrheits-Anspruch |
| **PD** | bei Politik-Entscheidungen, deren Inhalt Justice-relevant ist — PD prüft den Prozess |
| **PI** | bei Institutionen, die Justice umsetzen — PI prüft Institutional-Anspruch vs. Realität |
| **PN** | bei Mediendiskurs zu Justice-Themen — PN prüft Diskurs-Verteilung |
| **PP** | bei normativen Argumenten zu Justice — PP prüft Kohärenz |
| **PT** | bei Justice-Drift über Zeit |

---

## §9 · Migrations-Pfad

### Phase 1 *(diese Woche)*

- ✅ Diese Spec ist ins Canon migriert: `canon/de/06_framework_extensions_v2.0_SECJ.md` (clean-public, 2026-05-29; vorher nur in Pre-Split-`06_CANON/`)
- Erste Test-Anwendung mit konkreter Achse-10-Maßnahme *(z. B. „Bürger:innen-Rat mit Veto-Recht für Klima-Politik")*

### Phase 2 *(diese Woche oder nächste)*

- PS-Entry-Gem-Prompt *(`PS_3.0.md`)* wird zu **PS_4.0.md** aktualisiert:
  - Routing-Tabelle erweitert: Achse-10-Erkennung → `PS-U:JUSTICE`-Verweis
  - Modus-Hinweis im Quick-Start
- **Kein Update der Sub-Module *(PV/PD/PI/PN/PP/PT)*** — sie funktionieren unverändert

### Phase 3 *(post-NLnet, optional)*

- Prüfen, ob PS-U:JUSTICE in der Praxis ausreichend trennt
- Falls nicht: **PJ — Probatio Justitiae** als eigenständiges 7. Sub-Modul ausgliedern

---

## §10 · Falsifikations-Klausel auf diese Spec selbst

Diese Spec ist falsifizierbar:

- Wenn die JUSTICE-Modus-Gewichtung in der Praxis Justice-Maßnahmen falsch bewertet → Spec wird revidiert
- Wenn die J<0,50-Hard-Stop-Schwelle zu streng/zu lax ist → Schwelle wird angepasst
- Wenn die Achsen-Erkennung im VFP-V4 unsauber funktioniert → Mechanismus wird verbessert
- Wenn die SOZIALE-INKONSISTENZ-Flag im STANDARD-Modus zu viele False-Positives produziert → Schwelle wird justiert

Revisionen werden in der Versionierung dokumentiert.

---

## §11 · Versionierung

| Version | Datum | Änderungen |
|---|---|---|
| 1.x | bis 2026-05-09 | PS-U mit J=0,15, keine J-Veto-Flag, kein JUSTICE-Modus |
| **2.0** | **2026-05-10 *(Draft)*** | STANDARD-Modus mit J<0,40-Flag SOZIALE INKONSISTENZ; neuer JUSTICE-Modus mit J=0,40 + J<0,50-Hard-Stop; VFP-V4 Achsen-Erkennung |

---

**Ende der Spec.**

*Migriert ins Canon: 2026-05-10. Yoka-Approval erteilt. Spec ersetzt PS-U 1.x.*
