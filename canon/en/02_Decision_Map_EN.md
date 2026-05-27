# PROBATIO SYSTEMICA

## Volume 2 – Decision Map
### Framework Level (neutral, mathematical, descriptive)

**Version:** 2.0
**Date:** 2026-01-18
**Status:** Canonical

---

## PREAMBLE

This document defines the **Decision Map** of Probatio Systemica – a systematic procedure for decision-making based on the SEC principle.

**The Decision Map is:**
- A neutral tool (W2 from the toolkit)
- Mathematically grounded (based on SEC logic)
- Context-independent (applicable to any domain)

**The Decision Map is NOT:**
- A normative program (does not dictate WHAT should be decided)
- Specific to any application
- A replacement for human judgment

**For application see:** PROVOLUTION (Volumes 4-5)

**Cross-reference:** Volume 1 (SEC Canon), MASTERDOCUMENT v2.0

---

## 1. PURPOSE OF THE DECISION MAP

### 1.1 Problem Statement

Complex systems require continuous decisions:
- Which measure should be implemented?
- Should an ongoing measure be continued?
- When should a measure be terminated?

**Challenge:**
Without systematic procedures, decisions become:
- Inconsistent (ad hoc)
- Subjective (based on intuition)
- Untraceable (why was this decided?)

---

### 1.2 Solution: Decision Map

The **Decision Map** provides:
- **Systematicity:** Clear criteria for every decision
- **Objectivity:** Based on SEC verification
- **Traceability:** Every decision is documented

**Core Principle:**
> Decisions are made exclusively based on passed SEC tests.

---

## 2. BASIC STRUCTURE

The Decision Map uses **3-state logic**:

### State 1: ADMISSIBLE ✅
Measure may be implemented.

**Condition:**
```
Probatio(M) = TRUE
```

This means:
- Sufficient(M) = TRUE (impact adequate)
- Efficient(M) = TRUE (resource-optimal)
- Consistent(M) = TRUE (no contradictions)

---

### State 2: CONTINUABLE 🔄
Ongoing measure may continue.

**Condition:**
```
W(M)_measured ≥ W_min ∧ Consistent(M) = TRUE
```

This means:
- Measure continues to achieve minimum impact
- Measure generates no new contradictions
- (Efficiency may change but is not a termination criterion)

---

### State 3: TO BE TERMINATED ⛔
Measure must be stopped.

**Conditions (at least one met):**
```
W(M)_measured < W_min  (impact insufficient)
OR
Consistent(M) = FALSE  (contradictions emerged)
OR
R(M) > R_max           (resource limit exceeded)
```

---

## 3. DECISION MATRIX

### 3.1 Implement New Measure?

**INPUT:** Proposed measure M

**PROCESS:**
1. Conduct Probatio(M)
2. Evaluate result

**OUTPUT:**

| Probatio(M) | Decision | Action |
|-------------|----------|--------|
| TRUE ✅ | ADMISSIBLE | Implement M |
| FALSE ⛔ | NOT ADMISSIBLE | Reject or modify M |

**Note:**
If FALSE, analyze which SEC test failed:
- Insufficient → Strengthen M or reduce target
- Inefficient → Optimize M
- Inconsistent → Redesign M or adjust other measures

---

### 3.2 Continue Ongoing Measure?

**INPUT:** Ongoing measure M with measured impact W(M)_measured

**PROCESS:**
1. W(M)_measured ≥ W_min?
2. Consistent(M) = TRUE?
3. R(M) ≤ R_max?

**OUTPUT:**

| W ≥ W_min | Consistent | R ≤ R_max | Decision | Action |
|-----------|------------|-----------|----------|--------|
| ✅ | ✅ | ✅ | CONTINUABLE | Let M continue |
| ❌ | - | - | TERMINATE | Stop M (impact too low) |
| ✅ | ❌ | - | TERMINATE | Stop M (contradictions) |
| ✅ | ✅ | ❌ | TERMINATE | Stop M (resource limit) |

---

### 3.3 Adjust Measure?

**INPUT:** Ongoing measure M that is CONTINUABLE but suboptimal

**PROCESS:**
1. Is M still optimal regarding Efficiency?
2. Does a better alternative M' exist?

**OUTPUT:**

| Efficiency optimal | Better alternative M' exists | Decision | Action |
|-------------------|------------------------------|----------|--------|
| ✅ | ❌ | MAINTAIN | Keep M unchanged |
| ❌ | ✅ with Probatio(M')=TRUE | REPLACE | Replace M with M' |
| ❌ | ❌ or Probatio(M')=FALSE | OPTIMIZE | Improve M, don't replace |

---

## 4. PRIORITY MATRIX

### 4.1 Prioritize Multiple Measures

**Problem:**
Several measures are ADMISSIBLE (Probatio = TRUE), but resources are limited. Which first?

**Solution: SEC Score**

Each measure M receives a score:

```
SEC-Score(M) = α·S(M) + β·E(M) + γ·C(M)
```

Where:
- S(M) = Sufficiency degree (W(M) / W_min, normalized 0-1)
- E(M) = Efficiency degree (1 - R(M)/R_max, normalized 0-1)
- C(M) = Consistency degree (1 if consistent, 0 otherwise)
- α, β, γ = Weighting factors (α + β + γ = 1)

**Standard weighting (neutral):**
α = β = γ = 1/3 (all equal)

**Prioritization:**
Sort measures by SEC score descending.
Implement those with highest score first.

---

### 4.2 Adjust Weighting (Application Context)

**In Framework (Probatio Systemica):**
Standard weighting α = β = γ = 1/3

**In Applications (e.g., Provolution):**
Weighting can be adjusted:
- Climate urgency → increase α (Sufficiency more important)
- Resource scarcity → increase β (Efficiency more important)
- System stability → increase γ (Consistency more important)

**Example:**
In Provolution could be: α = 0.5, β = 0.3, γ = 0.2
(Impact more important than efficiency, as time is pressing)

---

## 5. RISK ASSESSMENT

### 5.1 Accounting for Uncertainty

**Problem:**
Impact W(M) and resources R(M) are often estimates, not certainties.

**Solution: Confidence Intervals**

Instead of point estimate:
```
W(M) = 100 kg CO₂
```

Use interval:
```
W(M) = [80, 120] kg CO₂  (95% confidence)
```

**Decision rule:**
```
W(M)_worst_case ≥ W_min  (pessimistic case must suffice)
```

This means:
- For W(M) = [80, 120] and W_min = 100 → NOT sufficient
- For W(M) = [100, 140] and W_min = 100 → sufficient

---

### 5.2 Risk Categories

**Low Risk:**
- W(M) well known (small confidence intervals)
- R(M) well controllable
- Consistency assured

**Medium Risk:**
- W(M) with uncertainty (larger intervals)
- R(M) variable
- Consistency verified but side effects possible

**High Risk:**
- W(M) highly uncertain
- R(M) difficult to predict
- Consistency questionable

**Decision Rule:**
For High Risk: Start with pilot project (small, reversible), then scale.

---

## 6. SCENARIO COMPARISON

### 6.1 Compare Multiple Paths

**Problem:**
Different measure combinations lead to different future scenarios. Which is optimal?

**Solution: Scenario Analysis**

**Step 1: Define Scenarios**
- Scenario A: Measures M1, M2, M3
- Scenario B: Measures M4, M5
- Scenario C: Measures M1, M5, M6

**Step 2: Evaluate**
For each scenario:
```
W_total = Σ W(M_i)  (total impact)
R_total = Σ R(M_i)  (total resources)
Consistent = all M_i mutually consistent?
```

**Step 3: Compare**

| Scenario | W_total | R_total | Consistent | SEC-Score |
|----------|---------|---------|------------|-----------|
| A | 500 | 100 | ✅ | 0.85 |
| B | 400 | 60 | ✅ | 0.78 |
| C | 450 | 90 | ❌ | 0.00 |

**Decision:**
Choose scenario with highest SEC score (here: A).

---

### 6.2 Making Trade-offs Visible

Scenario comparison reveals trade-offs:
- Scenario A: More impact, more resources
- Scenario B: Less impact, fewer resources

**Decision depends on:**
- Is W_min achieved? (then B possible)
- Are resources limited? (then prefer B)
- Is urgency high? (then prefer A)

**Important:**
Decision Map provides structure, not the answer.
Context determines weighting.

---

## 7. CASE EXAMPLES (neutral)

### 7.1 New Measure

**Proposal:** M = "CO₂ storage through tree planting"

**Probatio Test:**
- W_min = 100 kg CO₂/year
- W(M)_estimated = 150 kg CO₂/year → Sufficient ✅
- R(M) = 50 EUR, minimal among alternatives → Efficient ✅
- No conflicts with other measures → Consistent ✅

**Decision:** ADMISSIBLE ✅ → Implement M

---

### 7.2 Ongoing Measure

**Measure:** M = "Operate wind turbine"

**Measurement after 1 year:**
- W(M)_measured = 80 kg CO₂ reduction/year
- W_min = 100 kg CO₂ reduction/year
- W(M) < W_min ❌

**Decision:** TERMINATE ⛔
(Or: Strengthen measure, e.g., add second turbine)

---

### 7.3 Prioritization

**Three measures, all ADMISSIBLE:**
- M1: W=200, R=100, SEC-Score=0.75
- M2: W=150, R=50, SEC-Score=0.85
- M3: W=180, R=80, SEC-Score=0.80

**Order (by SEC score):**
1. M2 (0.85) ← first
2. M3 (0.80)
3. M1 (0.75)

---

## 8. TOOLS & IMPLEMENTATION

### 8.1 Decision Checklist

**Before Implementation (new measure):**
- [ ] W_min defined?
- [ ] W(M) estimated?
- [ ] Sufficiency test passed? (W ≥ W_min)
- [ ] R(M) known?
- [ ] Efficiency test passed? (R minimal)
- [ ] Consistency checked? (no conflicts)
- [ ] Probatio(M) = TRUE?

**For Ongoing Measure (continuation):**
- [ ] W(M)_measured known?
- [ ] W(M) ≥ W_min? (still sufficient)
- [ ] Consistency still given? (no new conflicts)
- [ ] R(M) ≤ R_max? (resource limit not exceeded)

**See:** Provolution Checklist (Volume 5) for application-specific version.

---

### 8.2 Software Tools (optional)

The Decision Map can be implemented in software:

**Inputs:**
- Measure database (M, W(M), R(M))
- SEC criteria (W_min, R_max)
- Consistency rules

**Process:**
- Automatic Probatio test
- SEC score calculation
- Prioritization

**Output:**
- List of admissible measures (sorted by score)
- Termination recommendations for ongoing measures
- Scenario comparison

**Advantage:**
- Fast
- Consistent
- Scalable (many measures in parallel)

---

## 9. LIMITS OF THE DECISION MAP

### 9.1 What the Map Does NOT Provide

**No Goal Specification:**
The map does not say WHAT should be achieved (W_min).
This comes from the application context (e.g., Provolution).

**No Value Judgment:**
The map does not say WHICH goals are more important.
This is a normative decision (outside the framework).

**No Guarantee:**
The map can only assess whether measures theoretically work.
Practical implementation can fail (implementation errors).

---

### 9.2 Prerequisites

The Decision Map works only if:
- W(M) is measurable (impact quantifiable)
- R(M) is known (resources clear)
- Consistency is testable (interactions understood)

If these are missing: Map delivers no reliable results.

---

## 10. CROSS-REFERENCES

**CANON Modules:**
- Volume 1 (SEC Canon) – SEC principle in detail
- Volume 3 (Scientific Core) – Mathematical foundations

**MASTERDOCUMENT:**
- MASTERDOCUMENT_v2.0.md – Part II, Section 2.3 (Toolkit)

**Application:**
- Volume 5 (Provolution Governance & Score) – Application of Decision Map
- provolution_checkliste_anwendung_band_5_sec.md – Practical checklist

**Terminology:**
- TERMINOLOGY_CHANGELOG.md – Framework vs. Application
- GLOSSARY.md – Definitions

---

## 11. VERSION HISTORY

**v2.0 (2026-01-18):**
- Renaming: "Provolution" → "Probatio Systemica" (framework level)
- Complete elaboration (instead of placeholder)
- 3-state logic (Admissible, Continuable, To Be Terminated)
- SEC score system for prioritization
- Risk assessment integrated
- Scenario comparison
- Case examples (neutral)
- Cross-references

**v1.0 (original):**
- Placeholder document

---

## 12. CONCLUSION

The **Decision Map** is a systematic tool for decision-making based on the SEC principle.

It provides:
- **Clarity:** Every decision has clear criteria
- **Objectivity:** Based on Probatio verification
- **Traceability:** Every decision is documented

It does NOT replace:
- Human judgment
- Normative goal setting
- Practical implementation

**The Decision Map is neutral.**
**It says HOW to decide, not WHAT.**

The WHAT comes from the application (e.g., Provolution).

**On to the next volume.**

---

**Version:** 2.0
**Status:** Canonical
**Date:** 2026-01-18

**End of Volume 2 – Decision Map**

(Source: Consolidated from MASTERDOCUMENT v2.0, Volume 1 SEC Canon)


---

## LICENSE

This work is released under:
- **CC0 1.0 Universal** (Public Domain)
- **Open Humanity License** (OHL)

See [LICENSE.md](../LICENSE.md) for full details.

You are free to use, modify, and distribute this work without restriction.

---
