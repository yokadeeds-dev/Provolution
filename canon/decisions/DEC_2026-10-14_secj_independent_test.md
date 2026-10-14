# DEC 2026-10-14: Unabhängiger SEC-J-Test (Roadmap Paket 2), Studiendesign

**Status:** ✅ Design von Claude nach Repo-Konvention festgelegt, Bestätigung über den PR-Merge · ⏳ vier Punkte warten auf den Autor (unten) · **Datum:** 2026-10-14
**Auftrag:** User 2026-10-14 „nach Empfehlung“ (Paket 2 planen)
**Studie:** [`studies/SECJ_INDEPENDENT_TEST_2026-10-14/PROTOCOL.md`](../../studies/SECJ_INDEPENDENT_TEST_2026-10-14/PROTOCOL.md)

## Befunde bei der Planung

1. **Die SEC-J-Scores sind Experten-Urteile, keine Formel-Ergebnisse.** Band 5 definiert C binär (0/1) und S, E, J als Formeln, die Daten enthalten aber abgestufte Werte (z. B. C = 0,82). Für einen Test durch Dritte war deshalb zuerst eine **Bewertungsskala mit festen Ankerpunkten** nötig (`RUBRIC.md`).
2. **Eingeschränkte Spannweite.** Die 12 Testfälle haben Autoren-SEC-J von 0,85 bis 0,93 (SD 0,024). Eine Simulation zeigt: Krippendorff-α fällt dann selbst bei fast perfekter Reproduktion niedrig aus (σ = 0,08 → α = 0,31 bei MAE 0,016). Die Entscheidungsregel stützt sich deshalb auf absolute Übereinstimmung und Streuung, α wird nur bei ausreichender Spannweite gewertet.
3. **Die illustrativen Fälle taugen nicht als Anker:** Ihr Ausgang ist bekannt, eine Verblindung damit unmöglich, und es sind keine Klima-Fälle.
4. **Verblindung über den Versand, nicht über das Repo:** Das Repo ist öffentlich und enthält die Autoren-Scores. Die Bewerter:innen erhalten nur das Fallmappen-Paket.

## Getroffene Design-Entscheidungen

| Frage | Entscheidung |
|---|---|
| Fälle Arm A | 12 Klima-Hebel mit Band-4-Vollabschnitt, geschichtet nach Domäne, B09 (niedrigstes J) Pflicht; 2 Trainingsfälle; deterministisch (seed 42) |
| Verblindung | Fallmappen ohne Scores, SEC-Nachweis und Agentic-Abschnitt; automatische Leak-Prüfung beim Erzeugen und als CI-Check 13 |
| Skala | 0–1 in 0,05-Schritten, Ankerpunkte je Achse; J mit Teilaspekten J1–J4 aus Probatio Deliberativa |
| Bewerter:innen | ≥ 3 (Ziel 5), extern, fachlich gemischt; KI-Systeme zählen nicht als externe Prüfung |
| Auswertung | `analyze.py` vorab festgelegt; Krippendorff-α am Referenzbeispiel geprüft (0,849); Bootstrap-KI |
| Entscheidungsregel | Reliabilität und Reproduktion getrennt, je Achse und gesamt, an Simulationen kalibriert (PROTOCOL §7) |
| Veröffentlichung | Ergebnisse unabhängig vom Ausgang |

## Offen, Entscheidung des Autors

1. **Arm B:** Sollen die 4 verworfenen Optionen (Biokraftstoffe, Kernkraft, BECCS/DAC, Solar-Geoengineering) als Kontrastfälle dazukommen? Voraussetzung: eigene Bewertung durch den Autor vorab (versiegelt) plus neutrale Fallmappen. Nutzen: größere Spannweite und Abschluss von LEVER_SELECTION §5.
2. **Rekrutierung:** Wer spricht die Bewerter:innen an? Vorlage: `RECRUITMENT_TEMPLATE.md`.
3. **Aufwandsentschädigung:** ja oder nein, Höhe.
4. **Vorab-Registrierung:** Plattform (Vorschlag: OSF) und Zeitpunkt (vor dem ersten Versand).
