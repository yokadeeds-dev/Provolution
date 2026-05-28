# SEC-J Spezifikation v1.0

**Status:** ⚠️ **DEPRECATED seit 2026-05-10** — siehe `06_framework_extensions_v2.0_SECJ.md` für aktuelle PS-U 2.0 Formel mit STANDARD- und JUSTICE-Modi
**Datum:** 2026-04-27 (Original) · Deprecation-Markierung 2026-05-28
**Autor:** Yoka Dieng

---

## ⚠️ Wichtiger Hinweis (2026-05-28)

Diese v1.0-Spezifikation definierte eine einzige SEC-J-Aggregations-Formel mit den Gewichten **0,40·S + 0,25·E + 0,15·C + 0,20·J**.

Mit der PS-U 2.0 Extension am 2026-05-10 wurde diese auf **zwei differenzierte Modi** aufgespalten:

- **STANDARD-Modus** (für normale Maßnahmen-Audits): `SEC-J(m) = 0,30·S + 0,25·E + 0,30·C + 0,15·J`
- **JUSTICE-Modus** (für Gerechtigkeits-fokussierte Audits, z.B. E21): `SEC-J(m, justice) = 0,25·S + 0,15·E + 0,20·C + 0,40·J`

Plus: J<0,40 → Flag **SOZIALE INKONSISTENZ** (Pflicht-Hinweis + Empfehlung) als zusätzlicher Schwellenwert *** NEU in 2.0 ***.

**Maßgebliche Spec ist jetzt `06_framework_extensions_v2.0_SECJ.md`**. Diese v1.0-Datei bleibt zur historischen Nachvollziehbarkeit, ist aber für alle Berechnungen ab 2026-05-10 NICHT mehr autoritativ.

**Konsequenzen für SEC-J-Werte im Repo:**
- Alle SEC-J-Berechnungen in `canon/data/impact_master.yaml` v2.2 (PR #6) und `canon/de/04_Band4_Anwendungen_v4.2.md` (PR #7) verwenden korrekt die PS-U 2.0 STANDARD-Formel
- Der externe PF-Report-Bestätigung der v1.0-Formel (`studies/EXTERNAL_AUDIT_2026-05-28/CHATGPT_AUSSENLESER_2026-05-28.md` u.a.) bezog sich auf die FORMALE Korrektheit der v1.0-Definition, nicht auf die Aktualität gegenüber v2.0

---

## Zweck (HISTORISCH — siehe Hinweis oben)

Diese Spezifikation definiert SEC-J als die normative Bewertungstheorie des Provolution-Frameworks und ihre Operationalisierung über Multi-Impact-Indikatoren. Sie WAR Single Source of Truth für alle SEC-J-Berechnungen in den CANON-Bänden 1–5 bis zur PS-U 2.0 Extension (`06_framework_extensions_v2.0_SECJ.md`).

---

## 1. SEC-J Theorie-Ebene

SEC-J bewertet Systeme, Institutionen und Politiken anhand von vier normativen Dimensionen:

| Symbol | Dimension | Bedeutung | Wertebereich |
|--------|-----------|-----------|--------------|
| S | Sufficient | bedarfsgerecht | [0, 1] |
| E | Efficient | wirkungsstark | [0, 1] |
| C | Consistent | systemverträglich | [0, 1] |
| J | Justice | gerecht | [0, 1] |

---

## 2. Operationalisierung über Multi-Impact

Multi-Impact (siehe `20_CANON/data/README_MULTI_IMPACT.md`) ist die operationale Mess-Ebene des Frameworks. Die SEC-J-Dimensionen werden aus Multi-Impact-Indikatoren wie folgt abgeleitet:

| SEC-J | Träger-Indikator(en) | Multi-Impact Dim. |
|-------|---------------------|-------------------|
| Sufficient | Reduktion ggü. Baseline | D1 + D2 |
| Efficient | CO₂-Wirkungspfad pro €/kWh | D1 |
| Consistent | Lock-in-Risiko + Rebound | D6 (+ D4 optional) |
| Justice | equity_score | D3 |

---

## 3. J-Score Berechnung

Der Justice-Score wird direkt aus `social.equity_score` der Multi-Impact-Dimension 3 abgeleitet:

```
J = (equity_score + 1) / 2     [Wertebereich: 0..1]
```

Mathematische Eigenschaften:

| equity_score | J-Wert | Interpretation |
|-------------|--------|----------------|
| −1 | 0,00 | maximal regressiv |
| −0,5 | 0,25 | regressiv |
| 0 | 0,50 | neutral (Veto-Schwelle) |
| +0,5 | 0,75 | progressiv |
| +1 | 1,00 | maximal progressiv |

---

## 4. J-Veto

Bei J < 0,50 (entspricht `equity_score < 0`, also regressivem Effekt) gilt das **J-Veto**:

> Die bewertete Maßnahme ist nicht zulässig, unabhängig von ihren S-, E- oder C-Werten.

Das J-Veto ist absolut. Es kann nicht durch hohe Werte in anderen Dimensionen kompensiert werden.

---

## 5. SEC-J Aggregations-Formel (⚠️ DEPRECATED — siehe v2.0)

**HISTORISCH (v1.0, deprecated 2026-05-10):**

Wenn J ≥ 0,50 (kein Veto), wurde der aggregierte SEC-J-Score in v1.0 berechnet als:

```
SECJ = 0,40·S + 0,25·E + 0,15·C + 0,20·J   ← DEPRECATED v1.0
```

**AKTUELL (v2.0 PS-U Extension, `06_framework_extensions_v2.0_SECJ.md`):**

```
SEC-J(m) = 0,30·S + 0,25·E + 0,30·C + 0,15·J          ← STANDARD-Modus
SEC-J(m, justice) = 0,25·S + 0,15·E + 0,20·C + 0,40·J  ← JUSTICE-Modus
```

**Gewichte v1.0 und Begründung:**

| Dim. | Gewicht | Begründung |
|------|---------|------------|
| S | 0,40 | Suffizienz ist Vorbedingung — bedarfsgerechte Wirkung steht vor Optimierung |
| E | 0,25 | Effizienz zentral, aber sekundär zu Sufficient |
| C | 0,15 | Systemkonsistenz reduziert, da sie oft erst durch S+E erreicht wird |
| J | 0,20 | Justice substantiell verankert; Hauptwirkung bereits über den Veto-Mechanismus |
| **Σ** | **1,00** | |

Wertebereich: SECJ ∈ [0, 1]

---

## 6. Anwendungsbereich

**SEC-J** wird angewendet auf:
- Systembewertungen (Probatio Veritatis et al.)
- Politik- und Institutionen-Audits (Probatio Institutionalis)
- Einzelne Anwendungen / Apps in Band 4
- Aggregierte Framework-Bewertung in Band 5

**Multi-Impact** wird angewendet auf:
- Konkrete Projekt-Bewertungen
- Quantitative Wirkungsmessung
- CO₂-Bilanzierung und Co-Benefit-Tracking

---

## 7. Quellverweise

| Ressource | Pfad |
|-----------|------|
| Multi-Impact Definition | `20_CANON/data/README_MULTI_IMPACT.md` |
| Impact-Master-Daten | `20_CANON/data/impact_master.yaml` |
| Projekt-Schema | `20_CANON/templates/PROJECT_IMPACT_SCHEMA.json` |
| Theorie-Verankerung | `06_CANON/01_Band1_SEC_Kanon.md` |
| Score-Logik | `06_CANON/05_Band5_Steuerung_Score.md` |
| Probatio-Familie | `06_CANON/07_Probatio_Veritatis_v2.0.md` u. a. |

---

## 8. Methodische Begründung des J-Veto · Antifragilität

Das J-Veto bei J < 0,50 ist **operativer Antifragilitäts-Schalter**,
nicht ethische Verzierung.

Drei-achsige SEC-Frameworks (S/E/C) können intern konsistent sein und
gleichzeitig **fragil** gegen Legitimitätsstress. Sie überleben Stress
*(robust)*, profitieren aber nicht von Stress *(nicht antifragil)*, weil
ihnen das Sensorium für Verteilungs-Backlash fehlt.

**Empirische Evidenz:** Yellow Vests (FR 2018), USA-Coal-Transition,
EU-Taxonomie Gas/Atom — methodisch konsistente Maßnahmen, die an
fehlender J-Komponente politisch gekippt sind.

**Antifragilitäts-Bedingungen** (Taleb 2012) und ihre Operationalisierung
in SEC-J:

| Bedingung | Operationalisierung |
|---|---|
| Optionalität | Multi-Stakeholder-Berücksichtigung über J-Komponente |
| Verlustbegrenzung | J-Veto bei J < 0,50 *(verhindert kompensatorische Effizienz)* |
| Lernfähigkeit | J liefert Legitimitätsstress als measurable input |

**Mathematik:** Reine Gewichtung würde zulassen, dass hohe S/E/C-Werte
niedrige J-Werte kompensieren. Das Veto macht aus der Aggregation eine
lexikographische Bedingung — formal äquivalent zu Talebs
Verlustbegrenzungs-Prinzip.

**Konsequenz:** SEC ohne J ist maximal robust. SEC-J ist antifragil.

**Referenz:** `06_CANON/ANTIFRAGILITY_PRINCIPLE.md` (ausführliche
Begründung, vier empirische Fallstudien, vollständige Quellen).

---

## 9. Versionierung

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2026-04-27 | Erstdefinition: SEC-J als Theorie-Ebene, Multi-Impact als Operationalisierung, J-Score aus equity_score, J-Veto bei J < 0,50, Aggregationsformel mit Gewichten 0,40 / 0,25 / 0,15 / 0,20 |
| 1.1 | 2026-05-09 | § 8 Antifragilitäts-Begründung ergänzt; Cross-Referenz auf `ANTIFRAGILITY_PRINCIPLE.md`; J-Veto explizit als Antifragilitäts-Schalter formal verankert |
