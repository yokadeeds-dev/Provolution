# Provolution CO₂ Budget — Figure Captions (submission-ready, EN)

Monte-Carlo uncertainty study, n = 10,000 iterations per scenario, seed = 42.
Data basis: `co2_master.yaml` v1.7 (layer 1 = −57.05 Gt, read live) + balance study §6. As of 2026-10-14 (D18 drift resolution).
Global baseline: IPCC AR6 (2023) = 55.0 Gt CO₂eq/yr.

Scenarios:

| Code | Scenario | impl | rebound | Median (Gt CO₂eq/yr) | 90% CI | % baseline |
|---|---|---|---|---|---|---|
| **S** | stress test, 50% deployment | 50% | 30% | −14.3 | [−19.8, −9.4] | 26.0% |
| **A** | conservative-realistic | 70% | 20% | −30.4 | [−38.1, −23.5] | 55.3% |
| **B** | expected value (mid-realistic) | 75% | 15% | −42.2 | [−51.6, −33.8] | 76.7% |
| **C** | optimistic-realistic | 85% | 8% | −59.9 | [−71.7, −49.2] | 108.9% |

Negative values denote net reduction. All figures are reproducible from
`monte_carlo.py` (single source of truth); the figure scripts import that module
and hard-code no values.

---

## Figure 1 — Scenario distributions
**File:** `Figure1_Scenarios.png` / `.svg`

Violin plot of the full net-CO₂-budget distribution (n = 10,000) for the four
scenarios S/A/B/C. Overlaid per scenario: median (white dot), 50% interquartile
range (thick bar, p25–p75), and 90% confidence interval (thin whisker, p5–p95).
The red dashed line marks net-zero (−55 Gt CO₂eq/yr, full compensation of the
global baseline). Median labels give the share of the baseline. Only scenario C
(optimistic-realistic) crosses the net-zero threshold at the median (109% of
baseline); scenario B sits on the climate-positive path at 77%.

## Figure 2 — Sensitivity analysis
**File:** `Figure2_Sensitivity.png` / `.svg` · Data: `variance_contributions_en.csv`

Fractional contribution of each input to the total variance of the net budget,
by scenario. Computed as a first-order covariance decomposition
Var(net) = Σᵢ Cov(Xᵢ, net), valid because the net budget is the exact sum of its
components; contributions sum to 100% per scenario (`sum_check` column). Layer 1
(direct leverage, coupled to the deployment rate) dominates the uncertainty in
all scenarios (66–117%). The **negative** rebound contribution (−28% to 0%) is
not an artefact: rebound is anti-correlated with net reduction and therefore
**dampens** the variance; its magnitude declines from scenario S (high rebound
rate) to C (low rate). Material bottlenecks and climate deterioration each
contribute < 5% — their additive input uncertainty is negligible against the
multiplicative deployment uncertainty.

## Figure 3 — Layer attribution (waterfall)
**File:** `Figure3_Waterfall.png` / `.svg`

Additive attribution of the net CO₂ budget across the model layers, per-layer
means. Reductions (Layer 1 direct, Layer 2 cascades, Layer 3 follow-on effects)
act downward; loss terms (rebound, material bottlenecks, climate deterioration)
act upward. The black terminal bar shows the net median budget; the red line
marks net-zero. The structural shift across scenarios is visible: in C
(optimistic) Layer 3 (follow-on effects, −12.6 Gt) gains substantial weight and
the rebound loss shrinks, whereas in S (stress test) the high rebound cancels a
large share of the direct reduction.

## Figure 4 — Exceedance curves
**File:** `Figure4_Exceedance.png` / `.svg`

Empirical cumulative distribution functions P(X ≤ x) of the net budget by
scenario. Thresholds mark net-zero (−55 Gt, red dashed) and the climate-positive
path (−33 Gt = 60% baseline, blue dotted). The embedded table reports the
target-attainment probabilities:

| Scenario | P(climate-positive) | P(net-zero) |
|---|---|---|
| S · stress test 50% | 0.0% | 0.0% |
| A · conservative | 28.1% | 0.0% |
| B · expected value | 96.3% | 1.4% |
| C · optimistic | 100.0% | 76.8% |

Translating the distribution into decision probabilities directly addresses
robustness: even in the expected-value scenario B the climate-positive path is
near-certain (96.3%), while full net-zero becomes likely only under optimistic
assumptions (C: 76.8%).

## Figure 5 — Convergence diagnostic
**File:** `Figure5_Convergence.png` / `.svg`

Running median (solid) and running 90% confidence interval (shaded) as a function
of iteration count (log scale), by scenario. The black dashed line shows the
final median at n = 10,000. Median and CI bounds stabilise in all scenarios from
roughly 1,000–2,000 iterations; the chosen sample size n = 10,000 lies well above
the convergence threshold, confirming the numerical stability of the reported
statistics (reproducible via seed = 42).

---

### Reproduction
```
cd studies/CO2_BILANZ_2026-05-28
python monte_carlo.py     # citable statistics (single source of truth)
python figures_en.py      # English Figures 1–5 + CSV tables → EN/
```
