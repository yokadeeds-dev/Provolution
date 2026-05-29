# For Reviewers — Fachliche Lesereihenfolge

**Stand:** 2026-05-29

Dies ist ein **Fach-/Reviewer-Repository**, keine populäre Einführung. Die Dichte ist gewollt: Präzision und SSoT-Disziplin haben Vorrang vor Laienverständlichkeit. Diese Datei ist **keine** vereinfachte Fassung, sondern nur eine empfohlene **Lesereihenfolge**, um den Einstieg für Gutachter:innen effizient zu machen.

> **For external reviewers (EN):** This is a domain/reviewer repository, not a lay introduction. This file is a suggested *reading order* only — not a simplified version. Authoritative status & values live in `canon/STATUS.md`.

---

## Empfohlene Reihenfolge

| # | Datei | Warum |
|---|---|---|
| 1 | [`README.md`](README.md) | Positionierung, Status, Snapshot-Zahlen, Einstiegs-Navigation |
| 2 | [`canon/STATUS.md`](canon/STATUS.md) | **Autoritative Quelle**: gültige Methode (PS-U 2.0/SEC-J), Werte-Glossar, Peer-Review-Status, Dokument-Status. Bei jedem Zahlen-Konflikt gilt diese Datei. |
| 3 | [`canon/LIMITATIONS.md`](canon/LIMITATIONS.md) | Stärkste Einwände — offen benannt und beantwortet. Spart Gutachter:innen Arbeit und zeigt den Umgang mit Kritik. |
| 4 | [`canon/docs/METHODOLOGY_CO2_ASSESSMENT.md`](canon/docs/METHODOLOGY_CO2_ASSESSMENT.md) | CO₂-Bilanzierungs-Methodik (Scopes, Standards, Unsicherheit, Double-Counting) |
| 5 | [`canon/data/co2_master.yaml`](canon/data/co2_master.yaml) | CO₂-SSoT: Hebel-Werte, Aggregate, validation_approach, Changelog |
| 6 | [`canon/data/impact_master.yaml`](canon/data/impact_master.yaml) | Multi-Impact-SSoT: SEC-J-Scores, sechs Dimensionen, Warnschwellen |
| 7 | [`manuscript/MANUSCRIPT_DRAFT_v0.1_BLIND.md`](manuscript/MANUSCRIPT_DRAFT_v0.1_BLIND.md) | Eingereichte Blind-Fassung (mit Corrigenda-Annotation; siehe Header) |

**Tiefer (optional):** SEC-J-Spec [`canon/de/06_framework_extensions_v2.0_SECJ.md`](canon/de/06_framework_extensions_v2.0_SECJ.md) · Hebel-Index [`canon/de/HEBEL_KATALOG_v1.0.md`](canon/de/HEBEL_KATALOG_v1.0.md) · Anwendungs-Kanon [`canon/de/04_Band4_Anwendungen_v4.2.md`](canon/de/04_Band4_Anwendungen_v4.2.md) · Steuerung/Score [`canon/de/05_Band5_Steuerung_Score.md`](canon/de/05_Band5_Steuerung_Score.md).

---

## Wichtige Lesehinweise

- **Werte nur aus STATUS.md + `canon/data/*.yaml`.** Fließtext-Bände sind Lesefassung, nicht Wertequelle. Als DEPRECATED/SNAPSHOT/SUPERSEDED markierte Stände nicht zitieren.
- **Reduktions-Totale = gescreente Potenziale**, keine Prognosen. Realistische Netto-Größen: Monte-Carlo-Mediane −43,2 Gt/Jahr (Szenario B) bzw. −14,9 Gt/Jahr (50 %-Stresstest).
- **Status:** Preprint, eingereicht bei Earth System Governance, **nicht extern peer-reviewed**. Interne „Probatio-Familia"-Audits sind selbst-administriert, kein unabhängiges Review.
- **Drift-Kontrolle:** `_tools/spec_consistency_audit.py` (Probatio Consistentia) prüft Cross-File-Konsistenz.

*Kritik willkommen (Issue/Fork/Korrespondenz) — das Framework ist antifragil ausgelegt (siehe `canon/LIMITATIONS.md`).*
