# Corrigendum: SEC-J Formula — Update to PS-U 2.0 Standard

**Date:** 2026-05-28
**Affected documents:**
- `MANUSCRIPT_DRAFT_v0.1.md` (DE + EN versions in `canon/de/`, `manuscript/`)
- `MANUSCRIPT_DRAFT_v0.1_BLIND.md` (blind-review submission)
- `CORRIGENDUM_2026-04-27.md` (predecessor — itself now superseded)
**Affected section:** Discussion, paragraph 5 (SEC-J dimension)

---

## Issue

The first corrigendum (2026-04-27, this folder) corrected the manuscript SEC-J formula:

    SEC-J = 0.5·S + 0.3·E + 0.1·C + 0.1·J     [INCORRECT, original submission]
    →
    SEC-J = 0.40·S + 0.25·E + 0.15·C + 0.20·J  [per SECJ_SPEC v1.0, 2026-04-27]

On 2026-05-10, the **PS-U 2.0 Extension** (`06_framework_extensions_v2.0_SECJ.md`) superseded SECJ_SPEC v1.0 by splitting the formula into two distinguished modes:

- **STANDARD Mode** (for measure-by-measure audits on Axes 1–9)
- **JUSTICE Mode** (for justice-focused audits, e.g. dedicated equity policies)

`canon/de/SECJ_SPEC_v1.0.md` is now formally marked **DEPRECATED** (see header note added 2026-05-28).

The 2026-04-27 corrigendum referenced the v1.0 formula as canonical — that reference is itself now historical.

---

## Current Canonical Formulas (per `06_framework_extensions_v2.0_SECJ.md`, PS-U 2.0)

### STANDARD Mode (default for general measure audits)

    SEC-J(m) = 0.30·S + 0.25·E + 0.30·C + 0.15·J
    J-veto:                SEC-J = null if J < 0.50
    Soziale Inkonsistenz flag: J < 0.40 (mandatory note + recommendation, no hard stop)

### JUSTICE Mode (for justice-focused audits, e.g. E21 Justice Mechanisms)

    SEC-J(m, justice) = 0.25·S + 0.15·E + 0.20·C + 0.40·J

### J derivation (unchanged)

    J = (equity_score + 1) / 2,     equity_score ∈ [−1, +1]

---

## Three-Stage Formula History

| Stage | Formula | Status |
|---|---|---|
| **Pre-v1.0** (submitted manuscript Discussion §5) | 0.5·S + 0.3·E + 0.1·C + 0.1·J | INCORRECT (early development version) |
| **v1.0** (SECJ_SPEC, 2026-04-27) | 0.40·S + 0.25·E + 0.15·C + 0.20·J | DEPRECATED since 2026-05-10 |
| **v2.0 STANDARD** (PS-U 2.0, 2026-05-10) | 0.30·S + 0.25·E + 0.30·C + 0.15·J | **AUTHORITATIVE** for standard audits |
| **v2.0 JUSTICE** (PS-U 2.0, 2026-05-10) | 0.25·S + 0.15·E + 0.20·C + 0.40·J | **AUTHORITATIVE** for justice audits |

---

## Why two modes?

The PS-U 2.0 update reflects the methodological insight that a single weighting cannot serve both purposes equally well:

- **STANDARD** balances S/E/C/J such that systemic coherence (C = 0.30) and Sufficient (S = 0.30) carry the most weight, while J = 0.15 remains substantive but does not dominate — appropriate for measures whose primary purpose is climate mitigation with distributional concerns as a guard rail.
- **JUSTICE** elevates J = 0.40 for measures whose primary purpose IS distributional (e.g. E21 Justice Mechanisms in the Provolution canon, with J = 0.95 functioning as the system-wide justice anchor).

The **J-veto** (J < 0.50 → SEC-J = null) is preserved in both modes as an absolute fail-safe.

---

## Action

- This corrigendum is filed alongside the 2026-04-27 predecessor in `canon/en/`
- Inline annotations added to `MANUSCRIPT_DRAFT_v0.1.md` (DE + EN) and `MANUSCRIPT_DRAFT_v0.1_BLIND.md` at the affected paragraph (Discussion §5)
- `canon/de/SECJ_SPEC_v1.0.md` formally marked DEPRECATED (header note 2026-05-28)
- `canon/data/impact_master.yaml` v2.3 `sec_j_scores.meta` references PS-U 2.0 as `spec_reference`
- External corrigendum to journal: pending author decision (per workflow in `CORRIGENDUM_2026-04-27.md`)

---

## Source

- Current authoritative spec: `canon/de/06_framework_extensions_v2.0_SECJ.md` (PS-U 2.0 Extension)
- Predecessor corrigendum: `canon/en/CORRIGENDUM_2026-04-27.md`
- Deprecated v1.0: `canon/de/SECJ_SPEC_v1.0.md` (with DEPRECATED header)
- Audit trail: `studies/EXTERNAL_AUDIT_2026-05-28/PF_SEC-J_NACHRUESTUNG_2026-05-28.md`
- Tool that detected the residual pre-v1.0 formula in manuscripts: `_tools/spec_consistency_audit.py`
