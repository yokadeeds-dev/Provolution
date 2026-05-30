# SEC-J Gewichts-Sensitivitätsanalyse

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement (Ergebnis-Report) · **Companion zu:** [`canon/STATUS.md`](../../canon/STATUS.md), [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md)
**Reproduzierbar:** `python studies/SENSITIVITY_2026-05-30/secj_weight_sensitivity.py` (seed=42, N_MC=20.000)

Antwort auf den Reviewer-Einwand „Die SEC-J-Gewichte (0,30/0,25/0,30/0,15) sind willkürlich — wo ist die Sensitivitätsanalyse?" ([`LIMITATIONS.md`](../../canon/LIMITATIONS.md) #5/#12, Reviewer-Q2). Geprüft wird, wie stark **Mittelwert, Hebel-Ranking, Verdict-Klassen und J-Veto** auf die Wahl der Gewichte reagieren.

> **Note for external readers (EN):** Weight-sensitivity analysis of the SEC-J composite. The script reads the 25 individually-scored levers from the SSoT (`canon/data/impact_master.yaml`), hardcodes nothing, and is reproducible (seed=42). This is **weight** sensitivity (how robust are results to the chosen weights), distinct from **input** sensitivity (varying the S/E/C/J scores themselves).

---

## 1. Methode

- **Datenbasis:** die **25** individuell kalkulierten Hebel aus `impact_master.yaml → sec_j_scores.individual_calculated` (S/E/C/J-Werte; die Domain-Batch-Ø sind nicht enthalten).
- **Baseline:** STANDARD-Gewichte `0,30·S + 0,25·E + 0,30·C + 0,15·J`.
- **Variiert:** der Gewichtsvektor (S,E,C,J), Summe = 1.
- **Gemessen:** (a) Ø SEC-J über die 25 Hebel, (b) **Spearman-Rangkorrelation** des Hebel-Rankings gegenüber der Baseline, (c) Anzahl Hebel mit **Verdict-Klassen-Wechsel** (TRAGFÄHIG ≥0,80 / BEDINGT 0,60–0,79 / DEFIZITÄR), (d) **J-Veto-Auslösungen** (J<0,50).
- **Drei Zugänge:** benannte Vergleichs-Gewichtungen · globales Monte-Carlo (uniformes Simplex, Dirichlet 1,1,1,1) · lokales Monte-Carlo (plausible Nachbarschaft Baseline ±0,10).

---

## 2. Ergebnisse

### 2.1 Integrität — die Scores sind formel-abgeleitet, nicht handgesetzt

Die mit der STANDARD-Formel neu berechneten Scores reproduzieren die in der SSoT **gespeicherten** `sec_j`-Werte **exakt**: maximale Abweichung **0,000** (auf 2 Nachkommastellen). Baseline-Ø SEC-J = **0,8984** (≈ 0,90, konsistent mit dem kanonischen Ø).

### 2.2 J-Veto ist gewichtsinvariant (Kernbefund)

`min(J)` über alle 25 Hebel = **0,72** (B09 Materialfluss) — deutlich über der Veto-Schwelle 0,50. **Kein Hebel kann durch irgendeine Gewichtswahl unter den J-Veto fallen**, weil der Veto auf die **J-Achse selbst** wirkt, nicht über das Komposit-Gewicht. → **0 Veto-Auslösungen für jede Gewichtung.** Das ist die quantitative Bestätigung des Kernarguments: *J wirkt über die Sperrschwelle, nicht über sein Gewicht (0,15)* — geringes Gewicht ≠ Abwertung.

### 2.3 Benannte Gewichtungs-Schemata

| Schema | Ø SEC-J | Spearman ρ vs. STANDARD | Verdict-Δ | Vetos |
|---|---:|---:|---:|---:|
| STANDARD (Baseline) | 0,8984 | 1,000 | 0 | 0 |
| JUSTICE (PS-U) | 0,8894 | 0,865 | 0 | 0 |
| Gleichgewicht (SMART-Default 0,25×4) | 0,8943 | 0,983 | 0 | 0 |
| DEPRECATED v1.0 (0,40/0,25/0,15/0,20) | 0,8962 | 0,927 | 0 | 0 |
| S-dominant (0,55/0,15/0,15/0,15) | 0,8995 | 0,877 | 0 | 0 |
| C-dominant (0,15/0,15/0,55/0,15) | 0,8998 | 0,880 | 0 | 0 |
| J-dominant (0,15/0,15/0,15/0,55) | 0,8833 | 0,692 | 2 | 0 |

Selbst über **radikal** unterschiedliche Gewichtungen bewegt sich der Mittelwert nur zwischen **0,883 und 0,900** (Spanne 1,7 Prozentpunkte); Verdict-Wechsel treten nur im J-dominant-Extrem auf (2 Hebel), Vetos nie.

### 2.4 Monte-Carlo (20.000 Gewichtsvektoren, seed=42)

| Größe | Global (uniformes Simplex) | Lokal (Baseline ±0,10) |
|---|---|---|
| Ø SEC-J (p5 / p50 / p95) | 0,880 / 0,895 / 0,904 | 0,895 / 0,898 / 0,902 |
| Ø SEC-J (min … max) | 0,868 … 0,908 | — |
| Spearman ρ (p5 / p50 / min) | 0,596 / 0,842 / 0,488 | 0,963 / 0,985 / 0,936 |
| Verdict-Δ (mittel / max von 25) | 0,52 / 3 | **0,00 / 0** |

**Lesart:** In der **plausiblen Nachbarschaft** (±0,10 um die Baseline) ist das Ergebnis nahezu invariant — das Ranking bleibt erhalten (ρ ≥ 0,94) und **kein einziges Verdict wechselt**. Selbst im **pathologischen** Fall völlig beliebiger Gewichte bleibt der Mittelwert in [0,868; 0,908] und höchstens 3 von 25 Verdicts kippen.

### 2.5 Verdict-Robustheit pro Hebel

Anteil der Gewichtsvektoren (globales MC), unter denen ein Hebel TRAGFÄHIG (≥0,80) bleibt:

| Hebel | TRAGFÄHIG-Anteil | STANDARD-Score |
|---|---:|---:|
| B12 Nachhaltige Biomasse | 80,6 % | 0,83 |
| B09 Materialfluss | 82,9 % | 0,85 |
| B11 Industrielle Transformation | 87,2 % | 0,86 |
| D19 Algen-Bioraffinerie | 98,0 % | 0,84 |
| *(übrige 21 Hebel)* | **≥ 99,9 %** | — |

**21 von 25 Hebeln sind unter praktisch jeder Gewichtung TRAGFÄHIG.** Die vier sensiblen Hebel sind **exakt die bereits im Kanon geflaggten Grenzfälle** (B09/B11/B12 tragen J<0,80-Warnschwellen mit Implementierungs-Auflagen; D19 ist der niedrigste Domain-D-Score). Die Sensitivität konzentriert sich also dort, wo der Kanon ohnehin schon Vorbehalte dokumentiert — kein verstecktes Risiko.

---

## 3. Antwort an Reviewer (Synthese)

1. **Die Gewichte sind nicht ergebnistreibend.** In der plausiblen Nachbarschaft ändert sich der Mittelwert um < 0,5 Prozentpunkte und **kein** Verdict; das Ranking ist stabil (ρ ≥ 0,94).
2. **Der Gerechtigkeits-Schutz hängt nicht am J-Gewicht.** Er wirkt über den harten Veto (J<0,50), der gewichtsinvariant ist — 0 Vetos unter jeder Gewichtung, weil min(J)=0,72.
3. **Wo Sensitivität existiert, ist sie offengelegt.** Die vier gewichtssensiblen Hebel sind die bereits dokumentierten Grenz-/Warnschwellen-Fälle, nicht überraschende Schwachstellen.
4. **Die Scores sind reproduzierbar formel-abgeleitet** (exakte Übereinstimmung Formel ↔ gespeicherte Werte), kein Hand-Tuning.

---

## 4. Grenzen

- Analysiert die **25 individuell kalkulierten** Hebel; die 5 batch-bewerteten Domains (A/E/F/G/H) sind nicht einzeln enthalten (Einzelhebel-J ausstehend, vgl. `HEBEL_KATALOG` Pending).
- Dies ist **Gewichts**-Sensitivität, nicht **Input**-Sensitivität (Variation der S/E/C/J-Scores selbst) — letztere ist ein separater, noch offener Test.
- Ein formaler Abgleich mit AHP/SMART-Elicitation-Verfahren (Herleitung *einer* präferenzbasierten Gewichtung) ersetzt diese Robustheits-Analyse **nicht**; beide sind komplementär (vgl. [`canon/METHOD_POSITIONING.md`](../../canon/METHOD_POSITIONING.md)).

---

## 5. Reproduktion

```
python studies/SENSITIVITY_2026-05-30/secj_weight_sensitivity.py
```

Liest live aus `canon/data/impact_master.yaml` (SSoT), seed=42, N_MC=20.000. Keine externen Abhängigkeiten (pure Python).

---

*Companion: [`canon/STATUS.md`](../../canon/STATUS.md) · [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #5/#12 · [`canon/METHOD_POSITIONING.md`](../../canon/METHOD_POSITIONING.md) · [`manuscript/RESPONSE_TO_REVIEWERS_PREP.md`](../../manuscript/RESPONSE_TO_REVIEWERS_PREP.md) Q2.*
