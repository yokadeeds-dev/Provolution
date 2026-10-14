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

Abhängigkeiten: `numpy`, `matplotlib` (getestet np 2.4.4 / mpl 3.10.8).

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
