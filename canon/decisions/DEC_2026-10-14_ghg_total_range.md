# DEC 2026-10-14 — all-GHG-Total: Spanne statt Punktwert

**Status:** ✅ entschieden (User, Empfehlung A) · **Datum:** 2026-10-14
**Fortgeschrieben:** 2026-10-14 durch [`DEC_2026-10-14_overlap_matrix_ghg_point.md`](DEC_2026-10-14_overlap_matrix_ghg_point.md): quellenweise Zuordnung erledigt → Punktwert −68,85 (CURRENT); die Spanne bleibt als Grenzfälle erhalten.
**Anlass:** Externes YAML-Review (2026-10-14), Befund „GHG-Gesamtwert noch nicht konsistent (PENDING)“
**Betroffen:** `canon/data/impact_master.yaml` v2.7 (`ghg_accounting.ghg_total`, `uncertainty_overall.ghg_total`), `canon/STATUS.md` §2, `_tools/spec_consistency_audit.py` Check 8

## Befund

Der Wert **−64,5 Gt CO₂eq/a war nie um Doppelzählungen bereinigt.** Beim Anlegen (Commit `1b683b2`, 2026-01-24, Legacy-Repo) war er die einfache Summe auf der damaligen CO₂-Basis:

−50,7 (CO₂) − 7,5 (CH₄) − 5,6 (N₂O) − 0,7 (F-Gase) = **−64,5**

Der spätere Kommentar „enthält Overlap-Bereinigung gegenüber naiver Summe −72,4“ (2026-05-28) war eine nachträgliche Erklärung und keine Rechnung. Eine Bereinigung, die man „neu rechnen“ könnte, gab es nicht. Auch das 95 %-Intervall [−81,2; −48,6] war nur pauschal ±25 % um −64,5 und keine Simulation.

## Methodisches Problem

Die CO₂-Schicht (`co2_master.yaml`) rechnet mit **CO₂eq**-Emissionsfaktoren (Strom, Diesel, Hanf-Biomasse; siehe `canon/docs/METHODOLOGY_CO2_ASSESSMENT.md`). Ob die CH₄- und N₂O-Wirkungen der separaten Gas-Schicht darin schon enthalten sind, ist pro Quelle nicht dokumentiert. Am stärksten betrifft das Domäne D (CO₂-Werte D15/D18 neben CH₄ −3,09 und N₂O −4,94 Gt CO₂eq/a). Die Überlappung kann irgendwo zwischen 0 % und 100 % liegen.

## Entscheidung

- **Spanne statt Punktwert:**
  - **−58,6 Gt CO₂eq/a**: volle Überlappung (CH₄/N₂O stecken schon in den CO₂eq-Werten)
  - **−72,45 Gt CO₂eq/a**: keine Überlappung (einfache Summe, mit GWP100 nach IPCC AR6)
- `ghg_total.total = null`, `total_status = RANGE`. **Kein erfundener Überlappungsfaktor.**
- −64,5 ist **DEPRECATED** (`deprecated_total`, nicht zitieren). Das pauschale Intervall und die Punktwerte in `uncertainty_overall.ghg_total` sind entfernt.
- all-GHG nach Rebound bleibt `null`, bis es einen Punktwert gibt (siehe `DEC_2026-10-14_rebound_single_source.md`).
- Check 8 erzwingt das maschinell: Bei RANGE muss `total` null sein und die Grenzen müssen der CO₂-Schicht bzw. der einfachen Summe entsprechen. Bei CURRENT muss der Punktwert innerhalb der Spanne liegen.

## Weg zu einem Punktwert (offen)

Jede CH₄- und N₂O-Quelle wird zugeordnet, ob sie „in der CO₂eq-Schicht enthalten“ oder „zusätzlich“ ist: B10/B12 Deponie, C Erdgas-Leckagen, D15 Gülle, D18 Tierhaltung, D Düngung (N₂O), B Industrie-N₂O. Danach `total_status: CURRENT` mit Punktwert und Begründung pro Quelle.

## Nicht mehr zitieren

−64,5 Gt CO₂eq/a, u. a. in `manuscript/PEER_REVIEW_PACKAGE.md`, `manuscript/NATURE_REVIEWER_EXPECTATIONS.md` (beide intern, mit Status-Banner) und in den Snapshots vom 2026-01-24.
