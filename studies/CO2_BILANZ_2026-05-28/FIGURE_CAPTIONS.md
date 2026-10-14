# Provolution CO₂-Bilanz — Abbildungslegenden (submission-ready)

Monte-Carlo-Unsicherheitsstudie, n = 10 000 Iterationen pro Szenario, seed = 42.
Datengrundlage: `co2_master.yaml` v1.3 + Bilanz-Studie §6 (v1.5).
Globale Baseline: IPCC AR6 (2023) = 55,0 Gt CO₂eq/yr.

Szenarien:

| Kürzel | Szenario | impl | rebound | Median (Gt CO₂eq/yr) | 90 % KI | % Baseline |
|---|---|---|---|---|---|---|
| **S** | Stresstest 50 %-Umsetzung | 50 % | 30 % | −14,9 | [−20,5; −9,8] | 27,0 % |
| **A** | konservativ-realistisch | 70 % | 20 % | −31,3 | [−39,1; −24,2] | 56,9 % |
| **B** | mittel-realistisch (Erwartungswert) | 75 % | 15 % | −43,2 | [−52,8; −34,6] | 78,5 % |
| **C** | optimistisch-realistisch | 85 % | 8 % | −61,1 | [−73,1; −50,2] | 111,1 % |

Negative Werte = Netto-Reduktion. Alle Kennzahlen sind reproduzierbar aus
`monte_carlo.py` (Single Source of Truth); die Figuren-Skripte importieren das
Modul und hartkodieren keine Zahlen.

---

## Figure 1 — Szenario-Verteilungen
**Datei:** `Figure_MonteCarlo_CO2.png` / `.svg` · Skript: `figure_monte_carlo.py`

Violin-Darstellung der vollständigen Netto-CO₂-Bilanz-Verteilung (n = 10 000) für
die vier Szenarien S/A/B/C. Pro Szenario überlagert: Median (weißer Punkt),
50 %-Interquartilbereich (dicker Balken, p25–p75) und 90 %-Konfidenzintervall
(dünner Whisker, p5–p95). Die rote gestrichelte Linie markiert Net-Zero
(−55 Gt CO₂eq/yr = vollständige Kompensation der globalen Baseline). Median-
Beschriftungen geben den prozentualen Anteil an der Baseline an. Nur Szenario C
(optimistisch-realistisch) überschreitet im Median die Net-Zero-Schwelle
(111 % Baseline); Szenario B liegt mit 78 % auf dem Klima-positiv-Pfad.

## Figure 2 — Sensitivitätsanalyse
**Datei:** `Figure2_Sensitivity.png` / `.svg` · Daten: `variance_contributions.csv`

Fraktionaler Beitrag jeder Eingangsgröße zur Gesamtvarianz der Netto-Bilanz,
getrennt nach Szenario. Berechnet als First-Order-Kovarianz-Zerlegung
Var(netto) = Σᵢ Cov(Xᵢ, netto), gültig, weil die Netto-Bilanz die exakte Summe
ihrer Komponenten ist; die Anteile summieren sich pro Szenario auf 100 %
(`sum_check`-Spalte). Schicht 1 (direkte Hebelwirkung, gekoppelt an die
Umsetzungsrate) dominiert die Unsicherheit in allen Szenarien (67–117 %). Der
**negative** Rebound-Beitrag (−28 % bis 0 %) ist kein Artefakt: Rebound ist
antikorreliert zur Netto-Reduktion und **dämpft** daher die Varianz; sein Betrag
sinkt von Szenario S (hohe Rebound-Rate) zu C (niedrige Rate). Material-Engpässe
und klimatische Verschlechterung tragen durchweg < 5 % bei — die additive
Eingangsunsicherheit dieser Verlustterme ist gegenüber der multiplikativen
Umsetzungsunsicherheit vernachlässigbar.

## Figure 3 — Schicht-Herleitung (Waterfall)
**Datei:** `Figure3_Waterfall.png` / `.svg`

Additive Herleitung der Netto-CO₂-Bilanz aus den Modellschichten, Mittelwerte je
Schicht. Reduktionen (Schicht 1 direkt, Schicht 2 Kaskaden, Schicht 3
Folgewirkungen) wirken nach unten; Verlustterme (Rebound, Material-Engpässe,
klimatische Verschlechterung) nach oben. Der schwarze Endbalken zeigt die
Netto-Median-Bilanz; die rote Linie markiert Net-Zero. Sichtbar wird der
Strukturwandel über die Szenarien: in C (optimistisch) gewinnt Schicht 3
(Folgewirkungen, −12,6 Gt) deutlich an Gewicht und der Rebound-Verlust
schrumpft, während in S (Stresstest) der hohe Rebound einen großen Teil der
direkten Reduktion zunichtemacht.

## Figure 4 — Exceedance-Kurven
**Datei:** `Figure4_Exceedance.png` / `.svg`

Empirische kumulierte Verteilungsfunktionen P(X ≤ x) der Netto-Bilanz je
Szenario. Die Schwellen markieren Net-Zero (−55 Gt, rot gestrichelt) und den
Klima-positiv-Pfad (−33 Gt = 60 % Baseline, blau gepunktet). Die eingebettete
Tabelle gibt die Zielerreichungs-Wahrscheinlichkeiten an:

| Szenario | P(klima-positiv) | P(Net-Zero) |
|---|---|---|
| S · Stresstest 50 % | 0,0 % | 0,0 % |
| A · konservativ | 35,5 % | 0,0 % |
| B · Erwartungswert | 97,5 % | 2,4 % |
| C · optimistisch | 100,0 % | 81,4 % |

Diese Übersetzung der Verteilung in Entscheidungs-Wahrscheinlichkeiten adressiert
direkt die Frage der Robustheit: Selbst im Erwartungswert-Szenario B ist der
Klima-positiv-Pfad mit 97,5 % nahezu sicher, während vollständiges Net-Zero erst
unter optimistischen Annahmen (C: 81,4 %) wahrscheinlich wird.

## Figure 5 — Konvergenzdiagnose
**Datei:** `Figure5_Convergence.png` / `.svg`

Laufender Median (durchgezogen) und laufendes 90 %-Konfidenzintervall
(schattiert) als Funktion der Iterationszahl (log-Skala) je Szenario. Die
schwarze gestrichelte Linie zeigt den finalen Median bei n = 10 000. Median und
KI-Grenzen stabilisieren sich in allen Szenarien ab ca. 1 000–2 000 Iterationen;
die gewählte Stichprobengröße n = 10 000 liegt deutlich oberhalb der
Konvergenzschwelle und belegt die numerische Stabilität der berichteten
Kennzahlen (Reproduzierbarkeit über seed = 42).

---

### Reproduktion
```
cd studies/CO2_BILANZ_2026-05-28
python monte_carlo.py            # Kennzahlen-Report (Single Source of Truth)
python figure_monte_carlo.py     # Figure 1
python peer_review_figures.py    # Figures 2–5 + CSV-Tabellen
```
