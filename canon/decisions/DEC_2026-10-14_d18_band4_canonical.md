# DEC 2026-10-14: D18-Drift-Resolution, Band 4 ist autoritativ

**Status:** ✅ entschieden (User, Option A) · **Datum:** 2026-10-14
**Präzedenz:** B09/B10-Drift-Resolution (co2_master v1.3, 2026-05-28): Tag und Wert auf band4-canonical korrigiert
**Betroffen:** `canon/data/co2_master.yaml` v1.7 · `canon/data/impact_master.yaml` v2.10 · `canon/data/overlap_matrix.yaml` v1.1 · `studies/CO2_BILANZ_2026-05-28/` (Monte-Carlo, Figuren, CSVs, Bildunterschriften) · `studies/CARBON_FLOW_2026-05-30/` · `canon/STATUS.md` · `README.md` · `CITATION.cff` (v2.3) · `canon/LIMITATIONS.md` · `canon/de/HEBEL_KATALOG_v1.0.md` · Band 4/5 · neu `canon/en/CORRIGENDUM_2026-10-14.md`

## Befund

| Quelle | D18 |
|---|---|
| Band 4 v4.2, Band 5, HEBEL_KATALOG | **Urbane Landwirtschaft**, „Transport-CO₂ −50 Mt/Jahr“ (= −0,05 Gt) |
| `co2_master.yaml` bis v1.6 | `D18_ernaehrung: -1.6`, erstmals v1.1 (Commit `6bc312e`, 2026-01-24), **ohne Herleitung** |
| Legacy-Repo (Stand 24.01.2026), ChatGPT-Archiv | −1,6 kommt nirgends sonst vor |

Die Größenordnung −1,6 passt zu einem Ernährungswandel (weniger Tierhaltung), nicht zu urbaner Landwirtschaft. Dieser Effekt steht bereits in der CH₄-Schicht (`impact_master.yaml` → `methane_ch4.D_food_land`, „reduzierte Tierhaltung“). Die −1,6 waren damit sehr wahrscheinlich eine Doppelzählung desselben Methan-Effekts.

## Entscheidung (Option A)

`D18_urbane_landwirtschaft: -0.05` (band4-canonical). Damit entfällt die D18-Annahme in der Overlap-Matrix. Der all-GHG-Punktwert beruht jetzt nur noch auf belegten Overlaps.

| Wert | vorher | **neu** |
|---|---:|---:|
| Domain D | −9,7 | **−8,15** |
| CO₂-Potenzial (reduktion_hart) | −58,6 | **−57,05** |
| CO₂-Gesamtpotenzial | −87,1 | **−85,55** |
| Anteil 55-Gt-Baseline | 106,5 % | **103,7 %** |
| CO₂ netto B (Monte-Carlo) | −43,2 [−52,8 … −34,6] | **−42,2 [−51,6 … −33,8]** |
| CO₂ netto A / C / S | −31,3 / −61,1 / −14,9 | **−30,4 / −59,9 / −14,3** |
| all-GHG brutto | −68,85 (mit D18-Annahme) | **−68,90** (nur belegte Overlaps) |
| all-GHG netto B | −51,6 | **−51,2 [−60,9 … −42,7]** |

Bei allen Treibhausgasen zusammen ändert sich praktisch nichts, nur bei der reinen CO₂-Zahl. Das bestätigt die Doppelzählungs-These.

## Mitgezogen (Anti-Drift)

- `monte_carlo.py` liest Schicht 1 jetzt **live** aus `co2_master.yaml`, statt sie fest einzutragen (vorher stand dort −58,6).
- Die Carbon-Flow-Sankey liest die Netto-Werte live aus `percentiles.csv` und das Overlap-Beispiel aus `overlap_matrix.yaml`.
- Figuren: Fußzeilen v1.3 → v1.7; die y-Achse der F3-Waterfall schneidet Panel C nicht mehr ab (älterer Darstellungsfehler).
- Bildunterschriften (DE/EN) mit den neuen Perzentilen, Zielerreichungs-Wahrscheinlichkeiten und Varianzanteilen.
- Unverändert und mit Hinweis versehen: das eingereichte Manuskript, das Anschreiben, die Corrigenda vom 2026-05-30, die Snapshots und die Decision-Dateien (dort stehen datierte Werte).

## Nebenwirkung

Wasser-Schicht in `impact_master.yaml`: Die Bezeichnung „D18 Ernährungswandel“ (−380 km³) ist jetzt „Ernährungswandel (kein eigener Hebel)“. Der Wert ist unverändert. Ein eigener Ernährungswandel-Hebel wäre eine inhaltliche Erweiterung und ist hier bewusst nicht angelegt.
