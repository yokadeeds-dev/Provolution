# DEC 2026-10-14 — Rebound: eine einzige Rechenstelle (Monte-Carlo)

**Status:** ✅ entschieden (User, Option A) · **Datum:** 2026-10-14
**Anlass:** Externes YAML-Review (2026-10-14, 7,5/10), Befund „Rebound baut auf pending Wert auf"
**Betroffen:** `canon/data/impact_master.yaml` v2.7 (`energy_system.rebound_effects`), `canon/STATUS.md` §2

## Problem

Das Repo enthielt zwei widersprüchliche Rebound-Modelle:

| Ort | Rebound | Ergebnis |
|---|---|---|
| `impact_master.yaml` `rebound_effects` | Pauschal 50 % (direkt 25 + indirekt 15 + gesamtwirtschaftlich 10), auf PENDING-Wert −64,5 | −32,3 |
| `studies/CO2_BILANZ_2026-05-28/monte_carlo.py` (Schicht 4) | 8–30 % je Szenario (B: 15 %), ±3 %, auf Schicht 1+2 | −43,2 (B) · −14,9 (S) — CURRENT laut STATUS §2 |

Mängel des Pauschalfaktors:
1. 50 % liegt über dem eigenen Stresstest (30 %).
2. Er wurde auf alle Hebel angewendet, auch auf Senken (D16, K01–K04) und Suffizienz-Maßnahmen, die keinen Effizienz-Rebound haben.
3. Der Hinweis „bereits in −58,6 teilweise integriert" war falsch: −58,6 ist gescreentes Brutto-Potenzial ohne Rebound-Abzug.

## Entscheidung

- Rebound wird **ausschließlich** in der Monte-Carlo-Bilanz gerechnet.
- Berichtet wird zweistufig: **vor Rebound −58,6 Gt/a** · **nach Rebound −43,2 Gt/a** (Szenario B, Median), Spanne bis **−14,9 Gt/a** (Stresstest).
- `net_rebound_factor` und `adjusted_impact: -32.3` sind entfernt. Die Komponenten 25/15/10 % bleiben als Literatur-Belege der Bandbreite (`literature_sum_upper_bound: 0.50`, nicht anzuwenden).
- all-GHG nach Rebound (`ghg_total_rebound`) bleibt `null`, bis `ghg_total.total` overlap-neu gerechnet ist. Danach läuft er durch dieselbe Monte-Carlo-Logik, ohne eigenen Faktor.

## Bekannte Restschwäche (offen, nicht Teil dieser Entscheidung)

Auch `monte_carlo.py` wendet den Rebound auf die gesamte Schicht 1+2 an, also ebenfalls auf Senken. Präziser wäre ein Rebound nur auf Effizienz-Hebel. Das würde den Headline-Wert −43,2 leicht verbessern. Es ist bewusst **nicht** umgesetzt, weil es eine Hebel-Klassifikation (Effizienz / Suffizienz / Senke) voraussetzt und eine CURRENT-Zahl ändern würde. Kandidat für eine spätere Methodik-Runde.

## Nicht mehr zitieren

−32,3 Gt/a („rebound-adjusted"), u. a. in `canon/data/README_MULTI_IMPACT.md` und `canon/docs/BAND3_INTEGRATION_MULTI_IMPACT.md` (beides Snapshots vom 2026-01-24).
