# Corrigendum: SEC-J Formula Weights

**Date:** 2026-04-27
**Affected document:** MANUSCRIPT_DRAFT_v0.1_BLIND.md (submitted)
**Affected section:** Discussion, paragraph 5 (SEC-J dimension)

---

## Issue

The submitted manuscript states the SEC-J aggregation formula as:

    SEC-J = 0.5·S + 0.3·E + 0.1·C + 0.1·J     [INCORRECT]

This does not match the canonical specification.

---

## Correct Formula (per SECJ_SPEC v1.0, 2026-04-27)

    SEC-J = 0.40·S + 0.25·E + 0.15·C + 0.20·J
    J-veto: SEC-J = null if J < 0.50

Where J = (equity_score + 1) / 2, equity_score ∈ [−1, +1] (Multi-Impact Dim. 3).

---

## Weight Comparison

| Component | Submitted (incorrect) | Canonical (SECJ_SPEC v1.0) |
|-----------|----------------------|---------------------------|
| S (Sufficient)  | 0.50 | 0.40 |
| E (Efficient)   | 0.30 | 0.25 |
| C (Consistent)  | 0.10 | 0.15 |
| J (Just)        | 0.10 | 0.20 |
| Sum             | 1.00 | 1.00 |

---

## Source

See `06_CANON/SECJ_SPEC_v1.0.md` for full specification and rationale.

---

## Action

- Internal manuscript (`MANUSCRIPT_DRAFT_v0.1_BLIND.md`) updated with corrigendum
  annotation at the affected paragraph (2026-04-27)
- External corrigendum to journal: pending author decision
- All future versions use corrected weights

---

## Path Update: Supplement 4

**Date:** 2026-04-27
**Affected document:** MANUSCRIPT_DRAFT_v0.1_BLIND.md (submitted)
**Affected section:** Data and Code Availability, Supplement 4 reference (line 503)

### Original path (in submitted version)

```
04_CONTENT_30_APPS/community_pipeline.py
```

### Updated path (canonical, post-2026-04-27)

```
04_CONTENT_LEVERS/community_pipeline.py
```

### Reason

The folder was renamed to reflect the canonical terminology
(*Lever* / *Hebel*) and to remove the misleading hardcoded "30"
(n is a dynamic value, not fixed at 30).

### Action for reviewers

When inspecting the supplementary code repository, please use
the updated path `04_CONTENT_LEVERS/community_pipeline.py`.
The file content is unchanged; only the directory name was
updated.

---

## Note on Terminology

The original filename and headers used "Erratum" prior to terminology
review. Per COPE and Elsevier convention, this document is properly
classified as a **corrigendum**: the affected paths and weights were
introduced by the authors, not by production or typesetting. The
filename `ERRATUM_2026-04-27.md` is retained to preserve referential
integrity with the submission record (`MANUSCRIPT_DRAFT_v0.1_BLIND.md`,
line 439). All in-document terminology has been migrated to "Corrigendum".

**References:**
- COPE Guidelines: https://publicationethics.org/guidance/Guideline
- Elsevier Editorial Policy on Corrections: https://www.elsevier.com/about/policies/article-withdrawal

---

## Forward Reference (added 2026-05-28)

**SECJ_SPEC v1.0** referenced as "canonical" in this 2026-04-27 corrigendum is itself **DEPRECATED** since the PS-U 2.0 Extension (`canon/de/06_framework_extensions_v2.0_SECJ.md`) on 2026-05-10.

A second-stage corrigendum (`canon/en/CORRIGENDUM_2026-05-28.md`) updates the formula reference from v1.0 to PS-U 2.0 (STANDARD + JUSTICE modes). All future external corrections should cite the v2.0 spec, not v1.0.

The submitted manuscript's Discussion §5 (referenced here, line 439 in `MANUSCRIPT_DRAFT_v0.1_BLIND.md`) now carries inline annotations for both corrigenda.
