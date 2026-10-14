# CO₂-Bilanz · Figuren- und Reproduktionspaket

Peer-Review-Begleitmaterial zur Monte-Carlo-Unsicherheitsstudie der Provolution-
CO₂-Bilanz (Stand v1.5, 2026-05-28).

## Inhalt

| Datei | Typ | Beschreibung |
|---|---|---|
| `monte_carlo.py` | Skript | **Single Source of Truth** — Simulation, Kennzahlen-Report |
| `monte_carlo_results.txt` | Output | zitierbare Kernzahlen (Median, 90 % KI, % Baseline) |
| `figure_monte_carlo.py` | Skript | erzeugt Figure 1 (Szenario-Violin) |
| `peer_review_figures.py` | Skript | erzeugt Figures 2–5 + CSV-Tabellen |
| `Figure_MonteCarlo_CO2.{png,svg}` | Figur | F1 Szenario-Verteilungen |
| `Figure2_Sensitivity.{png,svg}` | Figur | F2 Varianz-Beitrag je Input |
| `Figure3_Waterfall.{png,svg}` | Figur | F3 Schicht-Herleitung |
| `Figure4_Exceedance.{png,svg}` | Figur | F4 Zielerreichungs-Wahrscheinlichkeiten |
| `Figure5_Convergence.{png,svg}` | Figur | F5 Konvergenzdiagnose |
| `percentiles.csv` | Daten | p5/p25/p50/p75/p95, Mean, Std, % Baseline, Status |
| `variance_contributions.csv` | Daten | fraktionaler Varianz-Beitrag je Input (Σ = 100 %) |
| `FIGURE_CAPTIONS.md` | Doku | submission-fertige Abbildungslegenden F1–F5 |
| `figures_en.py` | Skript | erzeugt das englische Figurenpaket → `EN/` |
| `EN/` | Ordner | englische F1–F5 (PNG+SVG), CSV-Tabellen, `FIGURE_CAPTIONS_EN.md` |

## Reproduktion (vollständig)

```bash
cd studies/CO2_BILANZ_2026-05-28
python monte_carlo.py            # Konsolen-Report → monte_carlo_results.txt
python figure_monte_carlo.py     # F1
python peer_review_figures.py    # F2–F5, percentiles.csv, variance_contributions.csv
```

Abhängigkeiten: `numpy`, `matplotlib`, `pyyaml` (getestet np 2.4.4 / mpl 3.10.8). `pyyaml` seit 2026-10-14 für die Senken-Sensitivität in `monte_carlo.py` (liest `canon/data/`).

## all-GHG-Monte-Carlo (2026-10-14)

`ghg_monte_carlo.py` erweitert die CO₂-Simulation um CH₄, N₂O und F-Gase (Mengen aus `impact_master.yaml`, Overlaps aus `overlap_matrix.yaml`). Die CO₂-Schicht reproduziert die Headline exakt (assert). Ergebnis: `ghg_monte_carlo_results.txt`, `ghg_percentiles.csv`. Szenario B: **−51,6 Gt CO₂eq/a** [90 % KI −61,4 … −43,0]. Begründung der Verteilungsannahmen: `canon/decisions/DEC_2026-10-14_ghg_monte_carlo.md`.

```bash
python ghg_monte_carlo.py > ghg_monte_carlo_results.txt
```

## Senken-Sensitivität (2026-10-14)

`monte_carlo.py` rechnet zusätzlich eine Variante, in der Rebound nicht auf Senken wirkt (Boden D15∪D16 netto 5,0 + Blue Carbon K 1,5 = 6,5 Gt = 11,1 % von Schicht 1, aus den YAML-Dateien gelesen). Gleiche Zufallsziehungen, nur der Rebound-Term unterscheidet sich. Effekt auf den Median: A −0,9 · **B −0,7 (−43,2 → −43,9)** · C −0,4 · S −1,0 Gt. Die Headline-Werte bleiben bei der konservativen Methodik (Rebound auf ganze Schicht 1); siehe `canon/decisions/DEC_2026-10-14_overlap_matrix_ghg_point.md`. Figuren und CSV-Tabellen sind davon unberührt (byte-identisch reproduziert).

## Anti-Drift-Garantie

`figure_monte_carlo.py` und `peer_review_figures.py` **importieren**
`monte_carlo.py` und führen die Simulation mit identischem `seed = 42` erneut
aus. Sie enthalten **keine** hartkodierten Kennzahlen. Ändert sich eine
Eingangsverteilung in `monte_carlo.py` oder `co2_master.yaml`, propagiert die
Änderung automatisch in alle Figuren und Tabellen — die Figuren können nicht von
den berichteten Kennzahlen abweichen.

Validierung: `percentiles.csv` reproduziert die Werte aus
`monte_carlo_results.txt` exakt (Median, 90 % KI, % Baseline, Status).

## Methodische Eckpunkte für Gutachter

- **Unsicherheits-Propagation** (PF-Report E4): Monte-Carlo über die drei
  Hauptszenarien A/B/C; multiplikative Umsetzungsunsicherheit (impl ± 5 %) plus
  schichtspezifische Methodikunsicherheit (S1 ± 10 %, S2 ± 20 %, S3 ± 30 %).
- **Stresstest** (PF-Report E7): Szenario S mit 50 % Umsetzung, 30 % Rebound,
  erhöhten Verlusttermen als adversariale Untergrenze.
- **Varianz-Zerlegung** (F2): exakte First-Order-Kovarianz-Zerlegung statt
  Sobol-Indizes — zulässig, da die Netto-Bilanz die exakte Summe ihrer
  Komponenten ist (kein Interaktionsterm). Negative Beiträge kennzeichnen
  varianz-dämpfende, antikorrelierte Terme (Rebound).
- **Konvergenz** (F5): Median- und KI-Stabilität ab ~1 000–2 000 Iterationen;
  n = 10 000 mit komfortablem Sicherheitsabstand.
- **Determinismus**: `seed = 42`, feste Aufrufreihenfolge A→B→C→S.

## Offene Anschluss-Optionen (nicht ausgeführt)

- Englische Caption-/Beschriftungsvariante für internationale Submission.
- Einbindung als Figures 6–9 in `generate_publication_figures.py` (Haupt-Paper).
- Sobol-Sensitivität als Robustheits-Gegencheck zur Kovarianz-Zerlegung
  (erwartbar konsistent, da additiv).
