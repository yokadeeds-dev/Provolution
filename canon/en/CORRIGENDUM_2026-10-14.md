# Corrigendum: CO₂ Headline after D18 Drift Resolution, GWP100 to IPCC AR6, all-GHG Figures (Canon v1.5 → v2.3)

**Date:** 2026-10-14
**Affected documents:**
- `manuscript/MANUSCRIPT_DRAFT_v0.1.md` (EN) + `manuscript/MANUSCRIPT_DRAFT_v0.1_BLIND.md` (blind submission)
- `canon/de/MANUSKRIPT_DRAFT_v0.1.md` (DE version)
- `manuscript/COVER_LETTER_EarthSystemGovernance.md`
- `canon/en/CORRIGENDUM_2026-05-30.md` (its "current canonical" column is superseded by this document)

> **Companion to `CORRIGENDUM_2026-05-30.md`.** That corrigendum mapped the submission snapshot to Canon v1.5. The present corrigendum records the changes from Canon v1.5 to **v2.3** (release 2026-10-14). The submitted manuscript body stays a frozen snapshot; authoritative values are maintained in [`canon/STATUS.md`](../STATUS.md) and `canon/data/*.yaml`.

---

## 1. D18 drift resolution (CO₂ layer)

The data file listed `D18_ernaehrung: −1.6 Gt CO₂eq/yr` ("diet change"). An audit on 2026-10-14 found **no derivation for this value anywhere**: it first appears in `co2_master.yaml` v1.1 (2026-01-24) and is absent from Volumes 4 and 5, from the full repository history and from the authors' working-chat archive. Canonical lever D18 in Volume 4 v4.2 is **Urban Agriculture**, with a stated effect of −50 Mt CO₂/yr (transport). Following the established precedent (B09/B10 drift resolution, Canon v1.3), the data file was corrected to the Volume 4 value. Rationale: [`canon/decisions/DEC_2026-10-14_d18_band4_canonical.md`](../decisions/DEC_2026-10-14_d18_band4_canonical.md).

| Item | Canon v1.5 | **Canon v2.3** |
|---|---|---|
| D18 value (CO₂ layer) | −1.6 (tag "diet change") | **−0.05** (Urban Agriculture, Volume 4) |
| Domain D total | −9.7 | **−8.15** |
| CO₂ headline (hard, Layer 1) | −58.6 Gt/yr (106.5%) | **−57.05 Gt/yr** (103.7% of the 55 Gt baseline) |
| Total CO₂ potential (hard + avoided) | −87.1 | **−85.55** |
| Realistic **net**, Scenario B (Monte-Carlo median) | −43.2 [90% CI −52.8…−34.6] | **−42.2 [−51.6…−33.8]** |
| Scenario A / C | −31.3 / −61.1 | **−30.4 / −59.9** |
| 50%-implementation stress test (S) | −14.9 | **−14.3** |
| Lever count / domains | 49 / 11 | 49 / 11 (unchanged) |

The diet-change effect (reduced livestock) is accounted for in the CH₄ layer of the multi-impact data. The all-greenhouse-gas totals below are therefore practically unchanged by this correction. This indicates that the former −1.6 largely double-counted that methane effect.

## 2. GWP100 corrected to IPCC AR6

The multi-impact data used AR5 factors (CH₄ 28, N₂O 265) while labelling them "AR6". They now use IPCC AR6 WG1 Table 7.15: CH₄ 29.8 (fossil) / 27.0 (non-fossil), N₂O 273. CH₄ −7.5 → **−7.38**, N₂O −5.6 → **−5.77** Gt CO₂eq/yr (deterministic rescaling).

## 3. All-greenhouse-gas figures

| Item | Before | **Canon v2.3** |
|---|---|---|
| all-GHG gross potential | −64.5 (never overlap-adjusted: naive sum on the v2.0 CO₂ basis) | **−68.90 Gt CO₂eq/yr** after source-by-source overlap assignment (`canon/data/overlap_matrix.yaml`); bounds −57.05 (full overlap) … −70.90 (no overlap) |
| all-GHG **net**, Scenario B | *(absent)* | **−51.2 Gt CO₂eq/yr [90% CI −60.9…−42.7]** ≈ 93% of the (all-GHG) 55 Gt baseline (`ghg_monte_carlo.py`) |
| "rebound-adjusted" −32.3 | flat 50% factor on −64.5 | **withdrawn**; rebound is modelled only inside the Monte-Carlo balance |

### Superseded totals (citation hygiene)

- **−58.6 / −87.1 / 106.5% / −43.2 / −14.9** → superseded by the v2.3 values above.
- **−64.5** (all-GHG) and **−32.3** (rebound-adjusted) → deprecated.
- All totals are *screened technical/systemic potentials under stated assumptions*, **not forecasts**.
