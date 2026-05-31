# Corrigendum: Headline Figures, Lever & Domain Count — Submission Snapshot → Canon v1.5

**Date:** 2026-05-30
**Affected documents:**
- `manuscript/MANUSCRIPT_DRAFT_v0.1.md` (EN) + `manuscript/MANUSCRIPT_DRAFT_v0.1_BLIND.md` (blind submission)
- `canon/de/MANUSKRIPT_DRAFT_v0.1.md` (DE version)
- `manuscript/COVER_LETTER_EarthSystemGovernance.md`
**Affected sections:** Abstract; §1.3 Contribution; §4.2 Domain Classification; §4.3 Dynamic Application Set; §5.1 Table 1; §5.2 Table 2; §7 Conclusion

> **Companion to the formula corrigenda.** `CORRIGENDUM_2026-04-27.md` and `CORRIGENDUM_2026-05-28.md` correct the **SEC-J formula** (Discussion §5). The present corrigendum corrects the **quantitative and structural figures** that changed as a consequence of moving to PS-U 2.0 / SEC-J and of canon growth between the 2026-04-18 submission snapshot and Canon v1.5 (2026-05-29). It does **not** modify the submitted manuscript body, which is deliberately preserved as a frozen submission snapshot.

---

## Issue

The submitted manuscript (Draft v0.1, 2026-04-18) reports an application count, domain count, aggregate scoring statistic, and CO₂ headline that have all been superseded by the current canon. The submitted figures remain in the frozen body; the authoritative current values are maintained in [`canon/STATUS.md`](../STATUS.md) and the SSoT data files (`canon/data/co2_master.yaml` v1.5, `canon/data/impact_master.yaml` v2.6).

---

## Corrections (submitted snapshot → current canonical)

| Item | Submitted v0.1 | Current canonical | Source |
|---|---|---|---|
| Lever count *n* | 40 | **49** (38 band4-canonical · 1 STUB [I34] · plus yaml-only + community integrations) | STATUS.md §3 |
| Domains | 10 (A–J) | **11 (A–K)** — adds **Domain K Marine & Coastal** | STATUS.md §3 |
| Scoring method | 3-axis SEC = `0.5·S + 0.3·E + 0.2·C` | 4-axis **SEC-J STANDARD** = `0.30·S + 0.25·E + 0.30·C + 0.15·J` (PS-U 2.0) | STATUS.md §1; CORRIGENDUM_2026-05-28 |
| Mean score | 0.914 (3-axis; now historical) | **SEC-J Ø = 0.90** (25 individual + 5 domain-batch) | STATUS.md §3 |
| CO₂ headline (hard, Layer 1) | −58.0 Gt/yr (105%) | **−58.6 Gt/yr** (106.5% of 55 Gt baseline); total potential −87.1 Gt/yr | STATUS.md §2; co2_master.yaml `gesamt` |
| Realistic **net** expectation | *(absent)* | **−43.2 Gt/yr** (Monte-Carlo Scenario B median; 90% CI −52.8…−34.6); 50%-implementation stress test **−14.9 Gt/yr** | STATUS.md §2; balance study v1.5 `monte_carlo.py` |

### Deprecated / superseded totals (for citation hygiene)

- **−58.0 Gt/yr** → SUPERSEDED by −58.6 (post drift-resolution).
- **−50.7 Gt/yr** ("100% of target" snapshot) → DEPRECATED.
- **−64.5 Gt/yr** (all-GHG; CO₂+CH₄+N₂O+F-gases) → PENDING v2.2 (overlap re-computation outstanding); **do not cite as final**.

---

## New canonical levers since submission

- **Domain K — Marine & Coastal** (Blue Carbon, −1.5 Gt/yr mean; range −0.9…−2.1): K01 Mangrove restoration, K02 Seagrass restoration, K03 Kelp forest recovery, K04 Salt-marsh protection & restoration.
- **D19 Algae Biorefinery** (−0.3 Gt/yr; SEC-J 0.83), promoted into Domain D.
- **B11–B13** (industrial transformation / biomass / local on-demand manufacturing) added to Domain B.

---

## Interpretation guard (applies to every potential figure)

All mitigation totals above (−58.6, −87.1, the −26.5/−15.8-type domain figures in the submitted tables) are **screened technical/systemic potential under stated assumptions** — **not forecasts** and **not immediately realizable annual reductions**. They contain overlaps, constraints, and uncertainty bands. The realistic net magnitudes are the Monte-Carlo medians (−43.2 Gt/yr Scenario B; −14.9 Gt/yr 50%-implementation stress test). This framing supersedes any reading of the submitted headline as a near-term forecast.

---

## Not re-validated under PS-U 2.0 (open item)

The submitted agentic-integration figures (average **+8.7% SEC improvement**, α ∈ [0.70, 0.95]) were computed against the 3-axis SEC and have **not** been re-computed under SEC-J / PS-U 2.0. Treat as historical pending re-validation.

---

## Supplementary methodological studies (added since submission)

Four openly auditable supplements have been published in `studies/` since the 2026-04-19 submission. They support reviewer evaluation of methodological robustness and are **not** part of the frozen manuscript body:

- **`studies/SENSITIVITY_2026-05-30/`** — weight-sensitivity analysis (20,000 Monte-Carlo weight vectors, seed=42): in the plausible neighbourhood (±0.10) mean SEC-J shifts < 0.5 pp, no verdict flips, ranking stable (Spearman ρ ≥ 0.94); the J-veto is weight-invariant (min J = 0.72 → 0 vetoes).
- **`studies/CARBON_FLOW_2026-05-30/`** — Sankey decomposition gross −87.1 → screened −58.6 → realistic net −43.2 Gt/yr, with explicit domain-level double-counting controls.
- **`studies/CONSISTENCY_MATRIX_2026-05-30/`** — first-draft 44×44 lever-interaction matrix (121 source-traceable edges) operationalizing the consistency (⊥) relation; systematic conflict elicitation is flagged as future work.
- **`studies/ILLUSTRATIVE_CASES_2026-05-30/`** — **illustrative proof-of-concept, explicitly NOT a validation study:** retrospective concordance probe over N=7 historical decision cases (non-blind, unpowered, some cases beyond climate). Reported as *structural* consistency with documented outcomes, **not** predictive validity; a powered/blinded validation roadmap is included in the report.

These are reported with their stated limitations; none is claimed as external peer review or predictive validation.

---

## Action

- Filed in `canon/en/` alongside the two formula corrigenda (2026-04-27, 2026-05-28).
- Manuscript STATUS banners (EN + blind) updated to reference this corrigendum.
- `canon/STATUS.md` (§1 footnote, §5 manuscript row) updated to reference this corrigendum.
- External corrigendum to journal: pending author decision (per workflow in `CORRIGENDUM_2026-04-27.md`).
- Submitted manuscript body unchanged (frozen submission snapshot).

---

*Authoritative values live in `canon/STATUS.md` + `canon/data/*.yaml`. On any conflict, those files take precedence over manuscript prose.*
