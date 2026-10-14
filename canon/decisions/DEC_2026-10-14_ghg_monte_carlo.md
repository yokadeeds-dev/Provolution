# DEC 2026-10-14: all-GHG-Monte-Carlo, Recherche D18 und Paar-Koeffizienten

**Status:** ✅ von Claude nach Repo-Konvention entschieden, User-Bestätigung über den PR-Merge; D18 → offene User-Entscheidung · **Datum:** 2026-10-14
**Fortgeschrieben:** 2026-10-14 durch [`DEC_2026-10-14_d18_band4_canonical.md`](DEC_2026-10-14_d18_band4_canonical.md): D18 auf band4-canonical (−0,05) korrigiert → Zahlen hier sind Vor-Korrektur-Stand (aktuell: CO₂ −57,05 / netto B −42,2; all-GHG −68,90 / netto B −51,2; D18-Annahme in der Overlap-Matrix entfallen).
**Auftrag:** User 2026-10-14 „dann gehen wir die offenen Punkte an“ (offene Punkte aus #50)
**Betroffen:** neu `studies/CO2_BILANZ_2026-05-28/ghg_monte_carlo.py` (+ `ghg_monte_carlo_results.txt`, `ghg_percentiles.csv`) · `canon/data/impact_master.yaml` v2.9 · `canon/data/overlap_matrix.yaml` (Recherche-Vermerke) · `_tools/spec_consistency_audit.py` v0.3 · `canon/STATUS.md` §2

## 1. all-GHG-Monte-Carlo

**Ergebnis (Median, Gt CO₂eq/a):**

| Szenario | CO₂ (Headline) | all-GHG | 90 %-KI all-GHG | Anteil 55-Gt-Baseline |
|---|---:|---:|---|---:|
| A | −31,3 | −39,2 | −47,2 … −32,0 | 71 % |
| **B** | **−43,2** | **−51,6** | **−61,4 … −43,0** | **94 %** |
| C | −61,1 | −70,7 | −82,9 … −59,6 | 129 % |
| S | −14,9 | −20,5 | −26,3 … −15,2 | 37 % |

Die Baseline von 55 Gt CO₂eq/a ist all-GHG. Der Vergleich all-GHG ↔ Baseline ist daher der methodisch passende. Der bisherige CO₂-gegen-Baseline-Vergleich unterschätzt den Anteil.

**Annahmen (konservativ bzw. aus vorhandenen Daten, nichts neu geschätzt):**

| Baustein | Annahme | Begründung |
|---|---|---|
| CO₂-Schicht | identische Draws wie `monte_carlo.py` | Anti-Drift. Ein `assert` erzwingt, dass die CO₂-Mediane exakt der Headline entsprechen |
| Gasmengen | Dreieck (Min/Max = Unsicherheitsband aus `impact_master.yaml`, Modus = AR6-Punktwert); Domain-Anteile proportional | Nutzt die vorhandenen Bänder, keine neuen Zahlen |
| Overlap mit CO₂-Schicht | belegte Werte fest (B10: 2,0); angenommene Werte (D18: 1,6) gleichverteilt 0…1,6 | Die D18-Unsicherheit wird damit ehrlich als Spanne propagiert, statt als fester Wert |
| Umsetzungsrate Gase | Szenario-Mittelwert wie CO₂, ±5 %, eigene Ziehung | Gleiche Szenario-Logik |
| Rebound auf Gase | **keiner** in der Headline. Sensitivität: wie CO₂ (B: −50,4, Δ +1,3) | Deponie, Leckagen, Dünger, Prozess-N₂O und Kältemittel sind regulatorische bzw. prozesstechnische Maßnahmen ohne preisgetriebenen Mehrverbrauch |

`rebound_effects.ghg_total_rebound` ist jetzt −51,6 (vorher `null`). Check 11 prüft, dass die YAML-Werte dem Skript-Output (`ghg_percentiles.csv`) entsprechen.

## 2. D18: Recherche abgeschlossen, Entscheidung offen

| Quelle | Befund |
|---|---|
| Band 4 v4.2 / Band 5 / HEBEL_KATALOG | D18 = **Urbane Landwirtschaft**, Wirkung „Transport-CO₂ −50 Mt/Jahr“ (= −0,05 Gt) |
| `co2_master.yaml` | `D18_ernaehrung: -1.6`, erstmals in v1.1 (Commit `6bc312e`, 2026-01-24), ohne Herleitung |
| Legacy-Repo, gesamter Stand vom 24.01.2026 | −1,6 kommt **nur** in der YAML-Datei vor |
| ChatGPT-Archiv (semantische Suche + Volltext) | kein Treffer zu −1,6 Gt für Ernährung, Tierhaltung oder urbane Landwirtschaft |

Die Größenordnung −1,6 Gt CO₂eq passt zu einem **Ernährungswandel** (IPCC AR6 WGIII nennt für Ernährungsumstellung eine breite Spanne von 0,7–8 Gt CO₂eq/a). Sie passt nicht zu urbaner Landwirtschaft (−0,05). Der Wert ist vermutlich beim Anlegen der YAML-Datei einem falschen Hebel zugeordnet worden.

→ **Offene Entscheidung (User)**, siehe PR-Beschreibung. Die Repo-Konvention (Präzedenz B09/B10, v1.3) wäre „Band 4 ist autoritativ, Wert auf band4-canonical korrigieren“. Das würde allerdings die Headline-Werte ändern.

## 3. Paar-Koeffizienten B und C: abgeschlossen als „nicht belegbar“

Band 4 nennt bei B07 nur „kompatibel mit B08, B09, B10“ und bei C11–C14 nur „kompatibel mit …“. Eine Mengenaufteilung gibt es nirgends, auch nicht in Historie oder Archiv. Die Koeffizienten bleiben `not_sourced`, mit Recherche-Vermerk in `overlap_matrix.yaml`. Ohne externe Studie (z. B. Material-Flow-Analyse für B, Energiesystem-Modell für C) ist keine belegte Aufteilung möglich. Das ist kein offener Arbeitspunkt mehr, sondern eine dokumentierte Grenze.
