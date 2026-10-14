# DEC 2026-10-14: Input-Sensitivität (Roadmap Paket 1), Methodenwahl

**Status:** ✅ von Claude nach Repo-Konvention entschieden, User-Bestätigung über den PR-Merge · **Datum:** 2026-10-14
**Auftrag:** User 2026-10-14 „1“ (Paket 1 der Roadmap `DEC_2026-10-14_roadmap_external_validation.md`)
**Ergebnis:** [`studies/INPUT_SENSITIVITY_2026-10-14/INPUT_SENSITIVITY_REPORT.md`](../../studies/INPUT_SENSITIVITY_2026-10-14/INPUT_SENSITIVITY_REPORT.md)

## Getroffene Methoden-Entscheidungen

| Frage | Entscheidung | Begründung |
|---|---|---|
| Verfahren | Tornado (one-at-a-time) auf den Median von Szenario B, plus analytische Varianz-Zerlegung pro Hebel | Das Modell ist linear-additiv. Der Tornado ist dafür aussagekräftig, leicht zu prüfen und für Gutachter Standard |
| Zufallsziehungen | identisch zu `monte_carlo.py` (seed 42, A vor B) | Der Basiswert reproduziert die Headline exakt (`assert`). Unterschiede kommen damit nur vom Eingang, nicht vom Zufall |
| Bandbreite je Hebel | YAML-Bandbreite, sonst ±25 % | ±25 % ist die dokumentierte Gesamtunsicherheit in `co2_master.yaml` und wird hier nicht neu geschätzt |
| Overlap-Gruppen | anteiliger Faktor Netto/Brutto | Paar-Koeffizienten sind `not_sourced`, proportional ist die neutrale Annahme |
| Szenario-Parameter | Szenario A ↔ C | Bandbreite aus dem Repo selbst, keine neuen Werte |
| Basis-Unsicherheit ±10 % in `monte_carlo.py` | **unverändert** | Unabhängige Hebel-Bandbreiten ergeben nur ±2,9 %. Bei korrelierten Fehlern läge der Wert höher. ±10 % bleibt die konservative Wahl |

## Kernbefund für die Roadmap

Größte Treiber: Umsetzungsrate > Schicht 3 > Rebound > **Overlap B** > B07 > C11. Paket 3 beginnt deshalb mit Schicht 3 und Overlap B, Paket 4 mit Umsetzungsraten, B07 und C11.

## Prüfung

Check 12 in `_tools/spec_consistency_audit.py`: Die Ergebnis-CSVs enthalten genau die Hebel aus `co2_master.yaml`, und die Varianzanteile summieren sich auf 100 %. Kommt ein neuer Hebel ohne Neuberechnung dazu, scheitert der CI-Lauf.
