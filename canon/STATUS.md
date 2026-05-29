# Provolution — Autoritativer Status & Werte-Glossar

**Stand:** 2026-05-29 · **Charakter:** eingefrorener Status-Snapshot (living document)
**Zweck:** Eine einzige autoritative Quelle dafür, *welche* Methode, *welche* Kennzahlen und *welche* Dokumente aktuell gültig sind — und welche historisch/überholt sind.

> **Note for external readers (EN):** This file is the single authoritative status snapshot. Headline totals appearing elsewhere in this repository may be historical. Whenever a number conflicts, **this file and the CANON data files (`canon/data/*.yaml`) take precedence.** All mitigation totals are *screened technical/systemic potential under stated assumptions* — **not forecasts** and **not immediately realizable annual reductions.**

---

## 1. Methoden-Status

| Aspekt | Autoritativer Stand | Quelle |
|---|---|---|
| Methoden-Version | **PS-U 2.0 / SEC-J** (autoritativ seit 2026-05-10) | `canon/de/06_framework_extensions_v2.0_SECJ.md` |
| Formel STANDARD | `SEC-J = 0.30·S + 0.25·E + 0.30·C + 0.15·J` | impact_master.yaml `sec_j_scores.meta.formula_standard` |
| Formel JUSTICE | `SEC-J = 0.25·S + 0.15·E + 0.20·C + 0.40·J` (J-fokussierte Audits, z.B. E21) | impact_master.yaml `formula_justice` |
| J-Veto | `SEC-J = null`, wenn `J < 0.50` | s.o. `veto_threshold` |
| J-Flag „soziale Inkonsistenz" | `J < 0.40` | `flag_soziale_inkonsistenz_threshold` |
| J-Warnschwelle | `J < 0.80` (kein Veto, dokumentierte Implementierungs-Auflage) | `warning_threshold` |
| **DEPRECATED** | SECJ_SPEC v1.0 (alte Formel `0.40·S + 0.25·E + 0.15·C + 0.20·J`) | `canon/de/SECJ_SPEC_v1.0.md` (Deprecation-Header) |

Pre-v1.0-Manuskript-Formel (`0.5·S + 0.3·E + 0.1·C + 0.1·J`) ist ebenfalls überholt — siehe Corrigenda `canon/en/CORRIGENDUM_2026-04-27.md` + `CORRIGENDUM_2026-05-28.md`.

---

## 2. Werte-Glossar (Headline-Totale)

Das Repository führt **mehrere verschiedene Totale**, weil sie **verschiedene Metriken** messen. Sie sind kein Widerspruch — aber nur die als CURRENT markierten gelten. Domain-Level-Werte stehen ausschließlich in den YAML-SSoT-Dateien (diese Datei kopiert sie bewusst nicht, um keine Drift zu erzeugen).

| Wert | Bedeutung | Status | Quelle |
|---:|---|---|---|
| **−58,6 Gt/a** | CO₂-only, Schicht 1 (direkt, „reduktion_hart") | ✅ **CURRENT** | `canon/data/co2_master.yaml` v1.5 `gesamt.reduktion_hart` |
| **−87,1 Gt/a** | CO₂-Gesamtpotenzial (hart −58,6 + weich/vermieden −28,5) | ✅ **CURRENT** | co2_master.yaml `gesamt.total_potenzial` |
| **1,065 (106,5 %)** | Anteil an globaler Baseline (55 Gt) → netto-negativ möglich | ✅ **CURRENT** | co2_master.yaml `gesamt.anteil_global_emissions` |
| **−64,5 Gt/a** | **all-GHG** (CO₂+CH₄+N₂O+F-Gase), Overlap-bereinigt | ⏳ **PENDING v2.2** — auf alter CO₂-Basis gerechnet, Overlap-Re-Computation ausstehend; **nicht als final zitieren** | `canon/data/impact_master.yaml` `ghg_total.total` |
| **−43,2 Gt/a** | Realistischer **Netto-Erwartungswert** (Monte-Carlo Szenario B, Median) [90 %-KI −52,8…−34,6] | ✅ **CURRENT** (realistische Lesart) | Bilanz-Studie v1.5 `monte_carlo.py` |
| **−14,9 Gt/a** | Netto bei **50 %-Umsetzungs-Stresstest** (Szenario S, Median) [−20,5…−9,8] | ✅ **CURRENT** (konservativ) | Bilanz-Studie v1.5 |
| ~~−50,7 Gt/a~~ | Älterer „100 % von Ziel"-Snapshot | ❌ **DEPRECATED-SNAPSHOT** — abgelöst durch −58,6 | historische Stände in `canon/de/05_Band5_*`, `canon/docs/BAND5_INTEGRATION_H01.md` |
| ~~−58,0 Gt/a~~ | Vor-Drift-Resolution-Wert | ❌ **SUPERSEDED** — abgelöst durch −58,6 | alte README/GitHub-Description-Stände |

**Defensive Lesart aller Potenzial-Werte:** Es sind *gescreente technisch/systemische Potenziale unter definierten Annahmen* — keine Prognosen, keine sofort realisierbaren Jahres-Reduktionen. Sie enthalten Overlaps, Constraints und Unsicherheitsbänder. Die realistischen Netto-Größen sind die Monte-Carlo-Mediane (−43,2 Szenario B / −14,9 Stresstest S).

---

## 3. Hebel- & Domänen-Zählung

| Größe | Wert | Anmerkung |
|---|---:|---|
| Domänen | **11 (A–K)** | inkl. J Konstruktion + K Marine & Küste (v1.5 2026-05-29) |
| Hebel im Kanon gesamt | **49** | inkl. Communities, STUB, yaml-only |
| band4-canonical | **38** | Vollkonzept in Band 4 v4.2 |
| STUB | **1** | nur I34 (Kreislauf-LNF) |
| Gesamt-Ø SEC-J | **0,90** | 25 individuell + 5 Domain-Batch |
| J-Veto-Auslösungen | **0** | kein Hebel `J < 0.50` |
| J-Warnschwellen (`J < 0.80`) | **4** | B09 (0,72) · B11 (0,78) · B12 (0,75) · C12 (0,82) — Auflagen in impact_master.yaml |

> ⚠️ Veraltete Zählungen, die noch im Umlauf sind: **„43 levers / 10 domains"** (Vor-K/J-Stand) und **„30 Anwendungen"** (sehr alt). Aktuell gilt **49 / 11 / 38 band4-canonical**.

---

## 4. Peer-Review-Status (nüchtern)

- **Charakter:** Preprint / living research repository. **Noch nicht extern peer-reviewed.**
- **Eingereicht bei:** Earth System Governance (vormaliges Ziel Nature Climate Change ist **revidiert** — siehe `manuscript/JOURNAL_SUBMISSION_PACKAGE.md`).
- **Interne Methodik-Audits (Probatio Familia, „PF"):** Selbst-administrierte Prüfläufe in separater KI-Umgebung (Gemini Gems). Das sind **strukturierte Selbst-Prüfungen, kein unabhängiges Peer Review.** Berichte: `studies/EXTERNAL_AUDIT_2026-05-28/`.
- **Reliabilitäts-Studie:** Inter-Rater + Blind-Retest (N=10, seed=42) in `studies/RELIABILITY_2026-04-20/` — methodischer Reproduzierbarkeits-Beleg, aber innerhalb der Autoren-Infrastruktur, **nicht** extern.
- **Konsequenz:** Formulierungen wie „validated", „ready", „100 % gaps closed" beziehen sich auf **interne Checklisten**, nicht auf externe Begutachtung. Sie werden in den Manuskript-Paketen entsprechend nüchtern markiert (siehe §5).

---

## 5. Dokument-Status (was gilt, was ist historisch)

| Dokument | Status |
|---|---|
| `canon/data/co2_master.yaml` v1.5 | ✅ CURRENT — CO₂-SSoT |
| `canon/data/impact_master.yaml` v2.6 | ✅ CURRENT — Multi-Impact-SSoT (inkl. SEC-J-Scores) |
| `canon/de/04_Band4_Anwendungen_v4.2.md` | ✅ CURRENT — Anwendungs-Kanon |
| `canon/de/HEBEL_KATALOG_v1.0.md` (v1.10) | ✅ CURRENT — Hebel-Index |
| `canon/de/06_framework_extensions_v2.0_SECJ.md` | ✅ CURRENT — autoritative SEC-J-Spec |
| `canon/de/SECJ_SPEC_v1.0.md` | ❌ DEPRECATED (Header gesetzt) |
| `canon/data/README_MULTI_IMPACT.md` | ⚠️ SNAPSHOT 2026-01-24 — Metrik-Beschreibung gültig, Werte/Pfade historisch; −64,5 siehe §2 PENDING |
| `canon/de/05_Band5_*` / `canon/docs/BAND5_INTEGRATION_H01.md` | ⚠️ enthält −50,7-Snapshots (DEPRECATED, siehe §2) |
| `manuscript/MANUSCRIPT_DRAFT_v0.1*` | ⚠️ enthält Pre-SEC-J-Formel — nur mit Corrigenda-Annotation zitieren |
| `manuscript/JOURNAL_SUBMISSION_PACKAGE.md` | ⚠️ Ziel-Journal revidiert (Nature → ESG) |

---

## 6. Drift-Kontrolle

- **Probatio Consistentia v0.1** (`_tools/spec_consistency_audit.py`) prüft Cross-File-Konsistenz (SEC-J-Formel-Varianten, reduktion_hart-Sync, DEPRECATED-Marker, Band 4 ↔ YAML). Vor Releases laufen lassen.
- Diese STATUS-Datei ist bei jeder Headline-Wert- oder Methoden-Änderung **mit-zupflegen** (Anti-Drift-Konvention).

---

*Bei Konflikt zwischen dieser Datei und Fließtext-Dokumenten gewinnen diese Datei + die `canon/data/*.yaml`-SSoT. Fließtext-Bände sind Lesefassung, nicht Wertequelle.*
