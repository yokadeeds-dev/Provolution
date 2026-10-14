# Protokoll: Unabhängiger SEC-J-Test (Roadmap Paket 2)

**Version:** 1.0 (Entwurf zur Vorab-Registrierung) · **Datum:** 2026-10-14 · **Status:** ⏳ geplant, noch keine Datenerhebung
**Entscheidung:** [`canon/decisions/DEC_2026-10-14_secj_independent_test.md`](../../canon/decisions/DEC_2026-10-14_secj_independent_test.md)
**Dateien:** `build_case_packets.py` (Fallauswahl + Fallmappen) · `case_packets/` · `RUBRIC.md` · `score_sheet_template.csv` · `analyze.py` · `author_scores.csv` (versiegelt bis zur Auswertung) · `RECRUITMENT_TEMPLATE.md`

> **Note for external readers (EN):** Pre-registration draft for an independent inter-rater test of the SEC-J scores. External raters score 12 blinded lever descriptions with an anchored rubric; reliability (Krippendorff's α, ICC) and agreement with the authors' scores (MAE) are evaluated by a pre-specified script with pre-specified decision thresholds. No data have been collected yet.

---

## 1. Fragen und Hypothesen

| # | Frage | Hypothese | Kennzahl |
|---|---|---|---|
| F1 | Bewerten unabhängige Fachleute mit derselben Skala übereinstimmend? | Streuung zwischen Bewerter:innen ≤ 0,10 auf jeder Achse (bei ausreichender Spannweite: α ≥ 0,667) | mittlere SD je Fall, Krippendorff-α (Intervall), ICC(2,1) |
| F2 | Reproduzieren sie die Autoren-Scores? | MAE(SEC-J) ≤ 0,10 und jede Achse ≤ 0,15 | MAE Bewerter-Mittel ↔ Autoren, Anteil \|Δ\| ≤ 0,10 |
| F3 | Stimmt die Rangfolge? | ρ > 0 | Spearman-ρ |
| F4 | Erkennen sie dieselben Gerechtigkeits-Warnungen? | Übereinstimmung J < 0,80 | Cohen-κ; Zahl der J-Vetos (J < 0,50) |

## 2. Design

- **Arm A (Kern, startbereit):** 12 Klima-Hebel aus dem Kanon, verblindet, mit einer Bewertungsskala mit festen Ankerpunkten (`RUBRIC.md`).
- **Arm B (optional, braucht Autoren-Input):** 4 bewusst verworfene Optionen aus `canon/LEVER_SELECTION.md` §4 (Biokraftstoffe, Kernkraft, BECCS/DAC, Solar-Geoengineering) als Kontrastfälle. Voraussetzung: Die Autoren bewerten sie **vorher** und versiegeln die Werte (Hash im Repo), und für jede Option liegt eine neutrale Fallmappe vor. Nutzen: größere Spannweite (siehe §5) und Abschluss des offenen Punkts aus LEVER_SELECTION §5.
- Kein Test der Vorhersagekraft (dazu: `studies/ILLUSTRATIVE_CASES_2026-05-30/` §7). Hier geht es um Reliabilität und Reproduzierbarkeit.

## 3. Fälle

Deterministische Auswahl (`build_case_packets.py`, seed 42) aus den 20 individuell bewerteten Hebeln mit Vollabschnitt in Band 4 v4.2:

- **12 Testfälle**, geschichtet nach Domäne (B 3 · C 2 · D 3 · K 2 · I 1 · J 1). Der Hebel mit dem niedrigsten J (B09, J = 0,72) ist Pflicht.
- **2 Trainingsfälle** (T01, T02) nur zur Kalibrierung, nicht ausgewertet.
- Fall-Codes F01–F12 ohne Hebel-ID, Reihenfolge zufällig.
- **Fallmappen** = Band-4-Abschnitt ohne alle Autoren-Bewertungen (Scores, SEC-Nachweis, Agentic-Abschnitt, Kanon- und Archiv-Verweise). Eine automatische Leak-Prüfung bricht ab, falls Score-Spuren übrig bleiben (zusätzlich Check 13 in der CI).

## 4. Bewerterinnen und Bewerter

- **Anzahl:** mindestens 3, Ziel 5.
- **Unabhängigkeit:** keine Mitautorschaft, keine Beteiligung an Provolution, keine Kenntnis der Autoren-Scores.
- **Fachliche Mischung:** Klimapolitik oder Governance · Energiesysteme, Ökobilanz oder Technik · Sozialwissenschaft oder Klimagerechtigkeit.
- **KI-Systeme** sind keine Bewerter im Sinne dieses Tests. Ein KI-Durchlauf darf als getrennt berichteter Vergleich laufen, zählt aber nicht als externe Prüfung (STATUS §4).

## 5. Ablauf

1. **Vorab-Registrierung** (z. B. OSF): Dieses Protokoll, `RUBRIC.md`, die Fallmappen und `analyze.py` werden mit Commit-Hash eingefroren, **bevor** Bewertungen eingehen.
2. **Versand:** Die Bewerter erhalten **nur** das Paket aus `case_packets/`, `RUBRIC.md` und `score_sheet_template.csv`, **keinen Link zum Repo**. Das Repo ist öffentlich und enthält die Autoren-Scores.
3. **Einführung** (30 min): Skala erklären, Trainingsfälle T01 und T02 bewerten, nur über die Skala sprechen, nie über Werte der Autoren.
4. **Bewertung:** 12 Fälle, unabhängig, ohne Austausch untereinander, etwa 2–3 Stunden.
5. **Wiederholung:** 6 zufällig gewählte Fälle nach mindestens 14 Tagen erneut (Test-Retest, `runde = 2`).
6. **Auswertung:** `python analyze.py`, erst nachdem alle Bewertungen vorliegen.

**Bekannte Einschränkung, eingeschränkte Spannweite:** Die Autoren-Werte im Test-Set liegen eng beieinander (SEC-J 0,85–0,93). Reliabilitätsmaße wie α und ICC fallen dann auch bei guter Übereinstimmung niedrig aus. Deshalb ist F2 (MAE, absolute Übereinstimmung) die Hauptaussage, und die Streuung der Autoren-Werte wird mitberichtet. Arm B würde die Spannweite erweitern.

## 6. Auswertung (vorab festgelegt)

`analyze.py` berechnet je Achse und für SEC-J: Krippendorff-α (Intervall), ICC(2,1) und ICC(2,k), MAE und Anteil |Δ| ≤ 0,10 (Bewerter-Mittel ↔ Autoren), Spearman-ρ, κ für die J-Warnschwelle sowie die Zahl der J-Vetos. Selbsttest mit synthetischen Daten und dem Referenzbeispiel aus Krippendorff (2011): `python analyze.py --selftest`.

## 7. Entscheidungsregeln (vorab festgelegt, umgesetzt in `analyze.py → verdict()`)

**Reliabilität** (stimmen die Bewerter:innen untereinander überein?):

- Streuen die Fälle ausreichend (SD der Autoren-SEC-J ≥ 0,10, z. B. mit Arm B): Krippendorff-α(SEC-J) ≥ 0,80 zuverlässig · 0,667–0,80 vorläufig · darunter nicht zuverlässig. Zusätzlich ist es nicht zuverlässig, wenn auf einer Achse die Streuung zwischen den Bewerter:innen 0,20 übersteigt.
- Bei eingeschränkter Spannweite (nur Arm A: SD = 0,024) ist α **nicht interpretierbar** und wird nur berichtet. Maßgeblich ist dann die größte mittlere Streuung zwischen den Bewerter:innen auf einer Achse: ≤ 0,10 zuverlässig · ≤ 0,20 vorläufig · darüber nicht zuverlässig.

**Reproduktion** (trifft das Mittel der Bewerter:innen die Autoren-Werte?):

- reproduziert: MAE(SEC-J) ≤ 0,10 **und** MAE jeder Achse ≤ 0,15
- teilweise reproduziert: MAE(SEC-J) ≤ 0,20 und jede Achse ≤ 0,25
- sonst nicht reproduziert

**Kalibrierung der Regel** (Simulation mit 5 synthetischen Bewerter:innen auf den echten 12 Testfällen):

| Szenario | Reliabilität | Reproduktion |
|---|---|---|
| Rauschen σ = 0,05 je Achse | zuverlässig | reproduziert |
| Rauschen σ = 0,30 je Achse | **nicht zuverlässig** | reproduziert (das Mittel trifft) |
| J systematisch −0,20 | zuverlässig | **teilweise** |
| J systematisch −0,40 | zuverlässig | **nicht reproduziert** |

Die Simulation zeigt auch, warum α allein nicht reicht. Bei realistischer Streuung (σ = 0,08) liegt α nur bei 0,31, obwohl die Bewerter:innen die Autoren-Werte fast exakt treffen (MAE 0,016). Der Grund ist die enge Spannweite der Fälle, nicht schlechte Übereinstimmung.

| Ergebnis | Folge im Repo |
|---|---|
| zuverlässig und reproduziert | Scores gelten als **unabhängig reproduziert**. STATUS §4 und LIMITATIONS werden entsprechend aktualisiert |
| vorläufig oder teilweise | betroffene Achsen benennen, Skala oder Scores überarbeiten, erneut testen |
| nicht zuverlässig oder nicht reproduziert | Die Scores werden als „Autoren-Urteil, nicht unabhängig bestätigt“ gekennzeichnet. LIMITATIONS bekommt einen neuen Punkt |

Zusätzlich berichtet: 90 %-Konfidenzintervalle per Bootstrap über die Fälle (α, MAE), ICC(2,1)/(2,k), Spearman-ρ, κ der J-Warnschwelle.

Die Ergebnisse werden **unabhängig vom Ausgang** im Repo veröffentlicht.

## 8. Daten und Datenschutz

- Bewerter erscheinen nur unter Pseudonym (R01 …). Die Zuordnung zu Personen liegt außerhalb des Repos.
- Es werden keine personenbezogenen Daten erhoben außer Fachgebiet und Jahren an Erfahrung (Angabe freiwillig).
- Einwilligung per Rekrutierungs-Mail (`RECRUITMENT_TEMPLATE.md`).

## 9. Offen (Entscheidungen des Autors, siehe Decision-Datei)

Wer rekrutiert, ob es eine Aufwandsentschädigung gibt, die Plattform für die Vorab-Registrierung und ob Arm B stattfindet.
