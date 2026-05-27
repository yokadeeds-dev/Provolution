# PROBATIO SYSTEMICA

## Volume 1 – SEC-J Canon
### Framework Level (neutral, mathematical, descriptive)

**Version:** 2.2
**Date:** 2026-05-09
**Status:** Canonical

---

## PREFACE

This document defines **Probatio Systemica** – the mathematically grounded framework for systemic verification. It represents the **framework level** of the overall project and remains deliberately neutral, objective, and value-free.

**Probatio Systemica is:**
- A permanently adjustable system that self-limits, self-improves, and self-verifies
- A toolbox of principles, rules, and applications
- Mathematically grounded, culture-independent, universally applicable

**Probatio Systemica is NOT:**
- An ideology or promise of salvation
- A target state or normative program
- Specific to any single application

**For application see:** PROVOLUTION (Volumes 4-5) – the concrete, goal-oriented implementation for climate transformation.

**Cross-Reference:** MASTERDOCUMENT v2.0, TERMINOLOGY_CHANGELOG.md

---

## 1. DEFINITION: PROBATIO SYSTEMICA

### 1.1 Core Concept

**Probatio Systemica** (from Latin *probatio* = proof, verification; *systemica* = systemic) is a framework for **verification of systemic measures** through the SEC Principle.

**From Tipping Point Analysis (Msg #1964):**
> "Not a target state, but a permanently adjustable system that self-limits, self-improves, and self-verifies."

**Extended Definition:**
> "The path to get there. No promise, no ideology, but a toolbox of principles, rules, and applications."

---

### 1.2 Characteristics

**Neutral & Descriptive:**
- No value judgments or target specifications
- Describes WHAT is possible, not WHAT ought to be
- Objectively measurable and verifiable

**Mathematically Grounded:**
- SEC Principle formalized (∀, ∃, logic)
- Probatio Logic as verification procedure
- Predictive power through precision

**Universally Applicable:**
- Not culture-bound
- Based on physical realities
- Usable for various contexts

---

## 2. SEC-J PRINCIPLE (Super Level Check)

The **SEC-J Principle** is the heart of Probatio Systemica. It defines four conditions that every measure must fulfill.

### 2.1 S – SUFFICIENT

**Definition:**
Every measure must be sufficient to achieve the defined effect.

**Mathematical:**
```
∀ M ∈ Measures: W(M) ≥ W_min
```

Where:
- M = Measure
- W(M) = Effect of measure M
- W_min = Minimum required effect

**Meaning:**
A measure that fails to achieve the goal is useless – regardless of how efficient or consistent it is.

**Example (neutral):**
- Measure: "Store 10kg CO₂"
- W_min: "Store 100kg CO₂"
- → Measure is NOT sufficient (W(M) < W_min)

---

### 2.2 E – EFFICIENT

**Definition:**
Every measure minimizes resource consumption for a given effect.

**Mathematical:**
```
min(R(M)) subject to W(M) ≥ W_min
```

Where:
- R(M) = Resource consumption of measure M
- Optimization occurs only when effect is sufficient

**Meaning:**
From all measures that are sufficient (S), choose the most resource-efficient.

**Example (neutral):**
- Measure A: Store 100kg CO₂ with 10 resource units
- Measure B: Store 100kg CO₂ with 5 resource units
- → B is more efficient (less R for same W)

---

### 2.3 C – CONSISTENT

**Definition:**
No measure may create systemic contradictions or collide with other measures.

**Mathematical:**
```
∀ M_i, M_j ∈ Measures: ¬(M_i ⊥ M_j)
```

Where:
- M_i ⊥ M_j = Measures contradict each other
- System remains internally consistent

**Meaning:**
A measure must not destroy what others build. The overall system must remain coherent.

**Example (neutral):**
- Measure A: "Reforest woodland" (CO₂ storage)
- Measure B: "Use same woodland for timber"
- → Contradiction (M_A ⊥ M_B), not consistent

---

### 2.4 J – JUST

**Definition:**
Every measure must achieve a distributively just effect. Measures
that structurally amplify existing inequalities do not fulfill the J criterion.

**Mathematical:**
```
∀ M ∈ Measures: J(M) ≥ J_min
```

Where:
- J(M) = Justice score of measure M ∈ [0, 1]
- J(M) = ( equity_score(M) + 1 ) / 2,  equity_score(M) ∈ [−1, +1]
- J_min = Application-specific minimum value (in Provolution: J_min = 0.50)

**Meaning:**
A measure that structurally amplifies inequality (J(M) < J_min) cannot be
probated – regardless of whether it is sufficient, efficient, and consistent.

**Example (formal):**
- Measure A: Burdens and benefits evenly distributed across all groups
  → equity_score(A) > 0  →  J(A) > 0.50  ✅
- Measure B: Burdens on low-income groups, benefits to high-income groups
  → equity_score(B) < 0  →  J(B) < 0.50  ❌

The equity_score is measured empirically. Operationalization and
measurement method see `20_CANON/data/README_MULTI_IMPACT.md`.

**Application-specific:**
J_min is set by the application user.
Provolution sets J_min = 0.50 (J-Veto rule).
See: `06_CANON/SECJ_SPEC_v1.0.md`

---

## 3. PROBATIO LOGIC (Verification)

### 3.1 Definition

**Probatio** is the procedure for verifying that a measure is SEC-J-compliant.

**Formalization:**
```
Probatio(M) = Sufficient(M) ∧ Efficient(M) ∧ Consistent(M) ∧ Just(M)

If Probatio(M) = TRUE → M is verified (probated)
If Probatio(M) = FALSE → M is rejected or modified
```

---

### 3.2 Process

**Step 1: Hypothesis**
A measure M is proposed.

**Step 2: Sufficiency Test**
- Question: Does M achieve the minimum effect W_min?
- Test: W(M) ≥ W_min?
- Result: YES → proceed to Step 3 | NO → reject M

**Step 3: Efficiency Test**
- Question: Is M resource-optimal?
- Test: R(M) minimal among all M with W(M) ≥ W_min?
- Result: YES → proceed to Step 4 | NO → optimize M

**Step 4: Consistency Test**
- Question: Does M create contradictions with other measures?
- Test: ∃ M_j: M ⊥ M_j?
- Result: NO → proceed to Step 5 | YES → modify M

**Step 5: Justice Test**
- Question: Is the distributional effect of M just?
- Test: J(M) ≥ J_min?
- Result: YES → M probated ✅ | NO → reject M or fundamentally redesign (J failure is structural)

**Step 6: Result**
- M is **probated** (verified) → can be implemented
- M is **not probated** → return to Step 1 (modify)

---

### 3.3 Validity Rule

**Canonical Rule:**
> Every statement or measure is only valid if it contains an explicit SEC-J proof.

**This means:**
- No measure without Probatio
- No "hoping", but "knowing"
- Mathematical precision = predictive power

---

## 4. ZERO-POINT PRINCIPLE

### 4.1 Definition

The **Zero-Point Principle** states:
> Every change begins at the current state (zero point), not at an idealized desired state.

**Meaning:**
- Perceive what IS (not what should be)
- Realistic starting position
- No utopias as starting point

---

### 4.2 Application

**Step 1: Current State Analysis**
Undistorted observation of the current system state.

**Step 2: Measure Deviation**
Difference between current state and target (if target is defined in application context).

**Step 3: Derive Measures**
Starting from current state, not from ideal target state.

**Important:** In the framework itself there is no target – that comes only in the application (e.g., Provolution).

---

## 5. FALSIFICATION & SELF-CORRECTION

### 5.1 Falsification Principle

Probatio Systemica is **falsifiable**:
- Every statement can be refuted
- Refutation leads to revision
- No dogmatic truths

**Criterion:**
> If measure M is implemented and W(M) < W_min (despite Probatio), then Probatio(M) was false.

---

### 5.2 Self-Correction

**Mechanism:**
1. Measure M is implemented
2. Effect W(M) is measured
3. If W(M) ≠ W_expected → analyze why
4. Probatio process is adjusted
5. M is modified or rejected

**Learning System:**
Probatio Systemica improves through feedback.

---

## 6. ABUSE RESISTANCE

### 6.1 Protection Against Manipulation

**Problem:**
Systems can be manipulated to justify predetermined results.

**Solution in Probatio Systemica:**

**Transparency:**
- All assumptions explicit
- All calculations traceable
- All decisions documented

**Objectivity:**
- Measurable criteria (W, R)
- Mathematically verifiable
- Non-negotiable (TRUE or FALSE)

**Falsification:**
- Every statement can be refuted
- Refutation is welcome (improves system)
- No immunization against criticism

---

### 6.2 Limitations

**Probatio Systemica does NOT protect against:**
- Deliberate data falsification (measuring W(M) incorrectly)
- Manipulation of targets (setting W_min arbitrarily)
- Political misuse (ignoring the system)

**This requires:**
- Integrity of users
- Independent verification
- Data openness

---

## 7. TOOLBOX COMPONENTS

Probatio Systemica provides modular tools:

### W1: Analysis Tools
- System state capture (current state)
- Effect chain analysis
- Identify dependencies

### W2: Decision Tools
- Priority matrix (by SEC score)
- Risk assessment
- Scenario comparison

### W3: Implementation Tools
- Gradual introduction (pilot projects)
- Feedback measurement
- Error correction procedures

### W4: Verification Tools
- SEC-J compliance test
- Consistency check (no contradictions)
- Effectiveness proof (measure W(M))

**See:** Volume 2 (Decision Map) for details.

---

## 8. APPLICATION: PROVOLUTION

**Probatio Systemica is neutral.**
**It can be used for various applications.**

**The first and most important application is PROVOLUTION:**
- Concrete implementation for climate transformation
- Normative, goal-oriented (tipping point compensation)
- Based on this framework

**See:**
- Volume 4: Provolution – Applications
- Volume 5: Provolution – Control & Score
- MASTERDOCUMENT v2.0, Part II

**Important:**
Provolution is ONE application. Probatio Systemica could also be used for other contexts (e.g., urban planning, business management, healthcare systems).

---

## 9. CROSS-REFERENCES

**Terminology:**
- TERMINOLOGY_CHANGELOG.md – Separation Probatio Systemica / Provolution
- GLOSSARY.md – Definitions of all terms

**CANON Modules:**
- 02_probatio_systemica_decision_map.md – Tools W2
- 03_probatio_systemica_scientific_core.md – Mathematical foundations

**MASTERDOCUMENT:**
- MASTERDOCUMENT_v2.0.md – Part II, Section 2 (Probatio Systemica)

**Application:**
- 04_provolution_volume4_applications.md – Concrete implementation
- 05_provolution_volume5_control_and_score.md – SEC Score system

**Historical Context:**
- TIPPING_POINT_ANALYSIS.md – Evidence of transition at Msg #1977
- Chat "Provolution Definition" – Origin of concepts

---

## 10. VERSION HISTORY

**v2.2 (2026-05-09):**
- Notation `J(M)` / `J_min` consolidated with SEC-J Spec
  (was `D(M)` / `D_min` letter drift against `06_CANON/SECJ_SPEC_v1.0.md`,
  Phase 6D-D.3+.a Drift-Harmonization)
- Version history v2.1 retroactively updated to new notation
- EN translation of SEC-J extension (Phase 6D-F.a, 2026-05-09)

**v2.1 (2026-04-27):**
- SEC extended to SEC-J: Justice as fourth framework dimension
- New section 2.4 J – JUST with formal definition
- Probatio formula extended: ∧ Just(M)
- Probatio process: new Step 5 Justice Test, Result → Step 6
- J failure leads to rejection or fundamental redesign
- J(M) = (equity_score + 1) / 2, J_min application-specific
- Provolution: J_min = 0.50 (see `06_CANON/SECJ_SPEC_v1.0.md`)
- All SEC labels → SEC-J

**v2.0 (2026-01-18):**
- Renaming: "Provolution" → "Probatio Systemica" (framework level)
- Definition from Tipping Point Analysis integrated
- SEC Principle mathematically formalized
- Probatio Logic as verification procedure
- Cross-references to MASTERDOCUMENT v2.0
- Clarification: Framework vs. Application (Provolution)

**v1.0 (original):**
- Placeholder document
- Reference to Canvas document

---

## 11. CONCLUSION

Probatio Systemica is a **mathematically grounded, neutral framework** for verification of systemic measures.

It is not a target state, but a **toolbox**.
It is not an ideology, but a **verification procedure**.
It is not dogmatic, but **capable of learning**.

The **Probatio Logic** guarantees:
- Sufficient: Measures achieve their effect
- Efficient: Resources are optimally used
- Consistent: No contradictions arise
- Just: Distributive justice is ensured

**Mathematical precision = predictive power.**

The framework is universal.
The application (Provolution) is specific.

**On to the next volume.**

---

**Version:** 2.2
**Status:** Canonical
**Date:** 2026-05-09

**End of Volume 1 – SEC-J Canon**

(Source: Consolidated from MASTERDOCUMENT v2.0, TERMINOLOGY_CHANGELOG.md, Tipping Point Analysis; SEC-J extension synced from German Band 1 v2.2 in Phase 6D-F.a)


---

## LICENSE

This work is released under:
- **CC0 1.0 Universal** (Public Domain)
- **Open Humanity License** (OHL)

See [LICENSE.md](../LICENSE.md) for full details.

You are free to use, modify, and distribute this work without restriction.

---
