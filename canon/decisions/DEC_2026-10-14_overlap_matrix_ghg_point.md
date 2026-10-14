# DEC 2026-10-14: Overlap-Matrix, all-GHG-Punktwert, Rebound ohne Senken

**Status:** ✅ von Claude nach Repo-Konvention entschieden, User-Bestätigung über den PR-Merge · **Datum:** 2026-10-14
**Fortgeschrieben:** 2026-10-14 durch [`DEC_2026-10-14_d18_band4_canonical.md`](DEC_2026-10-14_d18_band4_canonical.md): D18 auf band4-canonical (−0,05) korrigiert → Zahlen hier sind Vor-Korrektur-Stand (aktuell: CO₂ −57,05 / netto B −42,2; all-GHG −68,90 / netto B −51,2; D18-Annahme in der Overlap-Matrix entfallen).
**Auftrag:** User 2026-10-14 „das erledigen, was noch offen ist“ (offene Punkte aus PR #48 / Release v2.2)
**Betroffen:** neu `canon/data/overlap_matrix.yaml` v1.0 · `canon/data/impact_master.yaml` v2.8 · `studies/CO2_BILANZ_2026-05-28/monte_carlo.py` · `_tools/spec_consistency_audit.py` Check 11 · `canon/STATUS.md` §2/§5 · `canon/LIMITATIONS.md` #16

Grundsatz für alle drei Punkte: **keine erfundenen Koeffizienten**. Wo die Quellen nichts hergeben, steht es offen markiert in der Datei. Wo eine Annahme nötig war, ist sie die konservative, also die, die den Reduktionswert verkleinert.

## 1. Maschinenlesbare Overlap-Matrix (Domains B, C, D)

Die Quellen (Bilanz-Studie §2, `co2_master.yaml` methodology) dokumentieren die Bereinigung auf **Gruppen-Ebene**:

| Gruppe | Brutto | Netto | Overlap | Regel (Quelle) |
|---|---:|---:|---:|---|
| B07–B12 | 31,3 | 14,3 | 17,0 | B07 Kreislauf schluckt B08–B12; B13 additiv |
| C11–C14 | 20,1 | 12,3 | 7,8 | C11 schluckt C12–C14 teilweise |
| D15–D16 | 9,0 | 5,0 | 4,0 | Boden-Senken sind Mechanismus der Regen-LW; D17–D19 additiv |

**Entscheidung:** Paar-Koeffizienten gibt es nur dort, wo sie belegt sind. Das ist bei D der Fall, weil die Gruppe genau ein Paar ist (D15↔D16 = 4,0). Für B und C steht `pair_coefficients: not_sourced`. Eine Rückrechnung aus Domain-Differenzen auf einzelne Paare wäre geraten (Warnung im YAML-Review). Check 11 prüft die Gruppen-Arithmetik und dass jeder Hebel der Domain entweder in der Gruppe oder als additiv geführt ist. Ein neuer Hebel ohne Zuordnung schlägt also in der CI fehl.

## 2. all-GHG-Punktwert: −68,85 Gt CO₂eq/a

Jede CH₄-, N₂O- und F-Gas-Quelle ist der CO₂eq-Schicht zugeordnet (`overlap_matrix.yaml` → `gas_layer_overlaps`):

| Quelle | Gas | Overlap mit CO₂-Schicht | Beleg |
|---|---:|---:|---|
| CH₄ B (Deponie) | 2,70 | **2,0** | **belegt:** Band 4 B10 „CO₂: −2 Gt CO₂eq … Methan −2 Gt CO₂eq“. Der B10-Wert *ist* Deponie-Methan |
| CH₄ C (Erdgas-Leckagen) | 1,60 | 0 | belegt: C11 = Verbrennungs-CO₂ im Stromsektor, ohne flüchtiges CH₄ |
| CH₄ D (Landwirtschaft) | 3,09 | **1,6** | **Annahme (konservativ):** D18_ernaehrung (−1,6) kann die Tierhaltungs-Methan-Reduktion bereits enthalten; die Herleitung ist undokumentiert, deshalb wird volle Überlappung angenommen |
| N₂O D (Dünger) | 4,94 | 0 | belegt: D15 = Boden-Sequestrierung (CO₂); Dünger-Vorketten liegen in Schicht 2 |
| N₂O B (Industrie) | 0,82 | 0 | belegt: kein CO₂-Hebel deckt Prozess-N₂O |
| F-Gase | 0,70 | 0 | belegt: kein CO₂-Hebel deckt Kältemittel/SF₆ |

**Ergebnis:** −72,45 (keine Überlappung) + 3,6 = **−68,85** (`total_status: CURRENT`). Mit nur den belegten Overlaps wären es −70,45. Die Grenzfälle −58,6 … −72,45 bleiben in der Datei erhalten.

**Einordnung:** Das ist ein Brutto-Potenzial vor Umsetzungsrate und Rebound. Eine Monte-Carlo-Simulation existiert nur für die CO₂-Schicht (−43,2). all-GHG nach Rebound bleibt `null`, bis es Verteilungen für CH₄ und N₂O gibt.

**Nebenbefund (Tag-Drift):** Band 4 führt D18 als „Urbane Landwirtschaft“ (Transport −50 Mt/a), `co2_master.yaml` als `D18_ernaehrung` (−1,6 Gt). Das ist analog zum offenen F23/F24-Ownership-Punkt und total-neutral, aber zu klären. Es ist zugleich die einzige Annahme im Punktwert.

## 3. Rebound ohne Senken, als Sensitivität und nicht als Headline

`monte_carlo.py` rechnet zusätzlich eine Variante, in der Rebound nicht auf Senken wirkt: Boden D15∪D16 netto 5,0 plus Blue Carbon K 1,5, zusammen 6,5 Gt (11,1 % von Schicht 1, aus den YAML-Dateien gelesen). Die Zufallsziehungen sind identisch, nur der Rebound-Term unterscheidet sich.

| Szenario | Headline | ohne Senken | Δ |
|---|---:|---:|---:|
| A | −31,3 | −32,2 | −0,9 |
| **B** | **−43,2** | **−43,9** | −0,7 |
| C | −61,1 | −61,6 | −0,4 |
| S | −14,9 | −15,8 | −1,0 |

**Entscheidung:** Die Headline bleibt −43,2. Gründe:
- (a) Der Effekt liegt weit innerhalb des 90 %-Intervalls (B: −52,8 … −34,6).
- (b) Die Headline-Methodik ist dadurch konservativ, sie überschätzt den Rebound eher.
- (c) −43,2 steht in 21 Dateien, darunter im eingereichten Manuskript-Snapshot und im Release v2.2. Eine Änderung um 0,7 Gt rechtfertigt keine Neufassung.
- (d) Nur Senken auszunehmen ist belegt. Eine feinere Effizienz-/Suffizienz-Klassifikation aller 40 Hebel wäre wieder Ermessen.

**Umkehrbar:** Wenn die Headline auf die Senken-Variante umgestellt werden soll, reicht ein Parameter (`rebound_base_share`) plus ein Sync der Dokumente.

## Weiterhin offen

- all-GHG-Monte-Carlo (Verteilungen für CH₄ und N₂O)
- D18-Tag-Drift klären (Ernährung vs. Urbane Landwirtschaft), danach die einzige Annahme im Punktwert ersetzen
- Paar-Koeffizienten für B07↔B08–B12 und C11↔C12–C14, nur wenn neue Quellen sie hergeben
