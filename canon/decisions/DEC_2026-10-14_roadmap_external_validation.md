# DEC 2026-10-14: Roadmap, von „Framework reparieren“ zu „Framework extern beweisen“

**Status:** ✅ entschieden (User) · **Datum:** 2026-10-14
**Fortschritt:** Paket 1 ✅ 2026-10-14 → [`studies/INPUT_SENSITIVITY_2026-10-14/`](../../studies/INPUT_SENSITIVITY_2026-10-14/INPUT_SENSITIVITY_REPORT.md). Folge für Paket 3: Schicht 3 + Overlap B zuerst; für Paket 4: Umsetzungsraten, B07, C11.
**Ausgangsstand:** Release [v2.3 „Methodology preview (data consistency)“](https://github.com/yokadeeds-dev/Provolution/releases/tag/v2.3). Die internen Konsistenz- und Datenhygiene-Probleme sind geschlossen, die verbleibenden `not_sourced`-Overlaps (B07↔B08–B12, C11↔C12–C14) sind als Limitation dokumentiert.

## Release-Benennung (Klarstellung)

Ein separater Tag `v0.9-methodology-preview` wurde verworfen. Der Vorschlag war ein Versehen (User). v2.3 übernimmt die Rolle der Methodik-Vorschau, der Release-Titel wurde entsprechend angepasst. Tags folgen weiterhin der Version in `CITATION.cff`.

## Reihenfolge der nächsten Arbeitspakete

| # | Arbeitspaket | Ziel | Ausgangslage im Repo |
|---|---|---|---|
| 1 | **Input-Sensitivität** | Welche Hebel-Eingangswerte (CO₂ je Hebel, Overlap-Beträge, Gasmengen, Szenario-Parameter) treiben die Netto-Werte? Tornado bzw. Varianz-Zerlegung **pro Hebel**, nicht nur pro Schicht | vorhanden: Gewichts-Sensitivität SEC-J (`studies/SENSITIVITY_2026-05-30/`), Varianz-Zerlegung nach Schichten (F2). Fehlt: Sensitivität der CO₂-Eingangswerte pro Hebel |
| 2 | **Unabhängiger SEC-J-Test** | SEC-J-Bewertung durch Dritte (unabhängige Rater oder blind gerechnete Fälle), Vergleich mit den Autoren-Scores | vorhanden: illustrative Konkordanz-Probe N=7 (`studies/ILLUSTRATIVE_CASES_2026-05-30/`, ausdrücklich keine Validierung; dort §7 bereits ein Protokoll-Entwurf mit ≥ 3 verblindeten Ratern) und eine Divergenz-Analyse zweier Prüf-Versionen (`studies/GEM_AUDITS_2026-04-21/`). **Nicht vorhanden:** die in STATUS §4 früher genannte Reliabilitäts-Studie N=10. Das Artefakt ist nirgends auffindbar, die Aussage wurde am 2026-10-14 zurückgezogen. Paket 2 beginnt damit bei null |
| 3 | **Rückkopplungen zwischen Domänen** | z. B. C-Dekarbonisierung des Stroms → B-Material-Vorketten; bisher nicht modelliert (LIMITATIONS #16) | vorhanden: Konsistenz-Matrix 44×44 (qualitativ), `overlap_matrix.yaml` (nur innerhalb von Domänen) |
| 4 | **Pilotdaten** | gemessene Wirkung realer Pilotprojekte gegen die modellierten Werte | vorhanden: Pilot-Konzepte `applications/piloten/` (A01, H01), Pilot-Register K01–K04 (Band 4 Kap. 10b). Keine Messdaten |

**Begründung der Reihenfolge:** Erst wissen, welche Eingangswerte zählen (1). Dann zeigt die Prüfung durch Dritte (2), ob die Bewertung trägt, bevor das Modell um Wechselwirkungen erweitert wird (3). Pilotdaten (4) sind am teuersten und am langsamsten zu erheben und sollen gezielt die Hebel prüfen, die laut 1 am meisten Gewicht haben.

## Grundsätze für alle vier Pakete

- Neue Zahlen nur mit Quelle oder als ausdrücklich markierte Annahme. Alles reproduzierbar (Skript, Seed) und an `canon/data/*.yaml` angebunden.
- Jede neue Kennzahl bekommt einen Check im Prüfskript (`spec_consistency_audit.py`).
- „Extern“ heißt: Daten, Rater oder Prüfung außerhalb der Autoren-Infrastruktur. Interne KI-Audits zählen nicht als externe Validierung (siehe STATUS §4).
