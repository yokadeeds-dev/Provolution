# Response-to-Reviewers — Vorbereitung (INTERN / Arbeitsdokument)

**Stand:** 2026-05-29 · **Status:** INTERNES Vorbereitungs-Dokument — **nicht Teil der Einreichung**
**Zweck:** Die wahrscheinlichsten ESG-Reviewer-Einwände vorab durchschreiben, damit auf jeden eine belegte Antwort bereitliegt. Konsolidiert aus [`canon/LIMITATIONS.md`](../canon/LIMITATIONS.md) + adversarialen KI-Pässen ([`studies/AI_AUDIT_2026-05-28/`](../studies/AI_AUDIT_2026-05-28/)).

> **Hinweis:** Die *finale* Response-to-Reviewers an ESG ist auf **Englisch** zu verfassen. Dies ist die deutsche Arbeitsfassung der Argumente; bei den Reviews adaptieren/übersetzen.

**Status-Legende:** ✅ adressiert (im Repo belegt) · ⏳ offen, geplant (echte wissenschaftliche Arbeit) · 📋 wird in der Revision/Corrigendum geliefert

---

## 1. „Operationalisieren Sie die Konsistenz-Relation (⊥)."

**Vorbereitete Antwort:** Die Consistency-Achse ist nicht binär-undefiniert. Die kontinuierliche Form ist `C = 1 − (K+U)/I_ges` (Konflikte K, unerfüllte Abhängigkeiten U über alle Interaktionen I_ges; Band 5 §2). Die binäre 0/1-Variante ist als **konservative Screening-Vereinfachung** markiert. Die reproduzierbare Bestimmung von K/U pro Hebel — als auditierbare **Hebel-zu-Hebel-Konflikt-Matrix (44×44)** — liegt als **Erst-Entwurf** vor (`studies/CONSISTENCY_MATRIX_2026-05-30/`, 121 dokumentierte Kanten, jede quellen-rückführbar; nur B12 mit niedrigem C\*=0,50 = der Warnschwellen-Hebel). Operationale Kriterien (Ressourcen-Konkurrenz, gegenläufige Anreize, Rebound) + systematische Paar-für-Paar-Elicitation der restlichen Konflikte folgen.
**Status:** ✅ Formel vorhanden · ✅ 44×44-Matrix-Erst-Entwurf (`studies/CONSISTENCY_MATRIX_2026-05-30/`) · 📋 systematische Konflikt-Elicitation offen · **Beleg:** LIMITATIONS #6, #16.

## 2. „Begründen Sie die SEC-J-Gewichte. Sensitivitätsanalyse?"

**Vorbereitete Antwort:** Die Gewichte (0,30·S + 0,25·E + 0,30·C + 0,15·J) sind eine **explizite, dokumentierte und diskutierbare Wertentscheidung** (`framework_extensions_v2.0_SECJ.md`), kein verstecktes Axiom — und sie sind **nicht ergebnistreibend**: die Gewichts-Sensitivitätsanalyse (`studies/SENSITIVITY_2026-05-30/`, 20.000 Monte-Carlo-Gewichtsvektoren, seed=42) zeigt, dass in der plausiblen Nachbarschaft (±0,10) der Ø SEC-J um < 0,5 Prozentpunkte schwankt, **kein** Verdict wechselt und das Ranking stabil bleibt (Spearman ρ ≥ 0,94). Entscheidend: **J wirkt primär über das harte Veto (J<0,50 → SEC-J=null), nicht über sein Komposit-Gewicht** — quantitativ bestätigt: min(J)=0,72 → 0 Vetos unter *jeder* Gewichtung. Die vier gewichtssensiblen Hebel sind exakt die bereits geflaggten Grenzfälle (B09/B11/B12/D19). Für gerechtigkeits-primäre Maßnahmen existiert der JUSTICE-Modus (J=0,40).
**Status:** ✅ Sensitivitätsanalyse durchgeführt (`studies/SENSITIVITY_2026-05-30/`) · 📋 AHP/SMART-Elicitation-Abgleich + Input-Sensitivität (≠ Gewichts-S.) offen · **Beleg:** LIMITATIONS #5, #12.

## 3. „Wo ist die Justice-Dimension? Das Manuskript sagt ‚under development'."

**Vorbereitete Antwort:** SEC-J ist seit 2026-05-10 **kanonisch** (PS-U 2.0): fixe Formel, J-Veto bei J<0,50, J-Flag bei <0,40 (`canon/STATUS.md` §1). Die „under development"-Phrase stammt aus einem **älteren eingereichten Manuskript-Stand**; ein Corrigendum dokumentiert die SEC→SEC-J-Migration und wird ESG nachgereicht, sobald der Repo-Stand review-ready ist.
**Status:** ✅ im Canon · 📋 Corrigendum an ESG · **Beleg:** STATUS.md §1, `framework_extensions_v2.0_SECJ.md`.

## 4. „−58,6 Gt = Überclaiming. Double-Counting-Audit?"

**Vorbereitete Antwort:** −58,6 Gt ist ein **gescreentes Potenzial, keine Prognose**. Der realistische Netto-Erwartungswert ist der Monte-Carlo-Median **−43,2 Gt/Jahr** [90 %-KI −52,8…−34,6], im 50 %-Umsetzungs-Stresstest **−14,9 Gt/Jahr**. Per-Domain-Overlap ist bereinigt (z. B. B07 schluckt B08–B12: −32 → ~−16 Gt). **Offen:** Sankey-Visualisierung der Carbon-Flows, Inter-Domain-Rückkopplung, abschließende YAML-Domain-Zuordnungs-Bereinigung. Beide Werte werden in README/STATUS gleichrangig kommuniziert.
**Status:** ✅ MC-Median + Per-Domain-Overlap + YAML-Tag-Zuordnung + Konflikt-Matrix-Erst-Entwurf (2026-05-30) · ⏳ Sankey + Inter-Domain-Rückkopplung · **Beleg:** STATUS.md §2, LIMITATIONS #2, #16.

## 5. „Falsifizierbarkeit — oder nur innere Konsistenz?"

**Vorbereitete Antwort:** Eingeräumt: innere Konsistenz ist **nicht** dasselbe wie ein prädiktiver Test. Das J-Veto ist konkret operationalisiert (harte Sperrschwelle). Eine erste **retrospektive Out-of-sample-Probe** liegt jetzt vor (`studies/OUT_OF_SAMPLE_2026-05-30/`, N=3, volle Skala): PKW-Maut SEC-J = 0,19 (J-Veto auf C+J → vom EuGH 2019 als diskriminierend gekippt, Art. 18 AEUV) vs. diskriminierungsfreies ASFINAG-System 0,84 (durabel) vs. Währungsreform 1948 als Positiv-Pol 0,94. SEC-J trennt scharf — Diskriminator C/J, nicht S/E; inkl. Inter-Fall-J-Konsistenz-Begründung (0,15-Veto vs. 0,85). Offen ausgewiesen: Hindsight-/Single-Rater-Risiko, N=3, retrospektive Anwendung, framework-neutrale Fälle ≠ Climate-Lever-Feldtest.
**Status:** ✅ erste Probe (`studies/OUT_OF_SAMPLE_2026-05-30/`) · ⏳ powered/verblindet/prä-registriert + Climate-Lever-Feldtest offen · **Beleg:** LIMITATIONS #9, #13.

## 6. „Abgrenzung zu MCDA / IAM / Robust Decision Making?"

**Vorbereitete Antwort:** Die tabellarische Einordnung gegenüber AHP/ELECTRE/PROMETHEE (MCDA), DICE/FUND/PAGE (IAM) und Lempert et al. (RDM) liegt als Supplement vor: `canon/METHOD_POSITIONING.md`. Kern-Differenzierung — **ohne Neuheits-Alleinanspruch** (ELECTRE und lexikografische Verfahren kennen Veto-Schwellen): nicht die Existenz eines Vetos, sondern die **Kombination** ist neu — fixe universelle Gewichte (statt elicitierter Präferenzen), **eine** normativ verankerte Gerechtigkeits-Sperrschwelle (J-Veto aus dem Antifragilitäts-Prinzip, nicht paarweises Outranking), **Cross-Domain-Konsistenz als gescorte First-Class-Achse** und Screening statt Optimierung (komplementär zu IAM).
**Status:** ✅ Entwurf vorhanden (`canon/METHOD_POSITIONING.md`) · 📋 volle Gewichts-Sensitivität + EN-Übertragung offen · **Beleg:** LIMITATIONS #14.

## 7. „Warum genau diese 49 Hebel? Was wurde ausgeschlossen?"

**Vorbereitete Antwort:** Die Selektions-Logik (Aufnahme-Kriterien K1–K5, Ausschluss-Begründungen) ist jetzt dokumentiert: `canon/LEVER_SELECTION.md`. Kern: K1 (technisch/systemisch realisierbar, Großserien-Reife *kein* Kriterium) öffnet das Feld; K2/K3 (SEC-J-tragfähig + kein J-Veto + keine ungelösten Just-/Konsistenz-Konflikte) filtern. Bewusst zurückgestellt: Kernkraft, BECCS/DAC, SRM-Geoengineering — kriteriengeleitet begründet (E/J/C), als challenge-bare Wertung markiert; Biokraftstoffe (Antrieb) sind im Kanon bereits explizit ausgeschlossen (Band 4 I33 §12). Die Menge ist offen/erweiterbar (AUTO-INTEGRATE-Pipeline).
**Status:** ✅ Entwurf vorhanden (`canon/LEVER_SELECTION.md`) · ⏳ systematisches PS-U-Scoring der Ausschlüsse + deduktive Herleitung offen · **Beleg:** LIMITATIONS #15.

## 8. „Einzelautor, interne KI-Audits — Qualitätssicherung?"

**Vorbereitete Antwort:** Offen ausgewiesen (STATUS.md §4): Preprint, **nicht extern peer-reviewed**. Die „Probatio Familia"-Läufe sind **selbst-administriert** (eigene Gemini-Gems), KI-Außenleser-Pässe sind als solche gelabelt (`studies/AI_AUDIT_2026-05-28/_README.md` + Provenance-Disclaimer in der Datei). Gegengewicht: explizit falsifizierbar, CC0/OHL, **forkbar zur unabhängigen Replikation**; Reliabilitäts-Studie (Inter-Rater + Blind-Retest, N=10) als Reproduzierbarkeits-Anfang. Externe Replikation ist ausdrücklich erwünscht.
**Status:** ✅ transparent · **Beleg:** STATUS.md §4, LIMITATIONS #1, #4, AI_AUDIT/_README.

## 9. „Manuskript-Text ≠ Repo-Canon (veraltete Formel/Werte)."

**Vorbereitete Antwort:** Bewusster Zustand: eingereicht wurde ein älterer Stand; der aktuelle Canon (STATUS.md, YAMLs) ist neuer. Ein **Corrigendum** liegt im Repo und wird ESG nachgereicht, sobald der Repo-Stand vollständig review-ready ist (offene Punkte §4–§7 dieses Dokuments). STATUS.md ist die Brücke, die jederzeit den gültigen Stand ausweist.
**Status:** 📋 Corrigendum-Versand · **Beleg:** STATUS.md §5, Corrigenda in `canon/en/`.

## 10. „Starke Begriffe (‚first', ‚validated', ‚konform')."

**Vorbereitete Antwort:** Bereits entschärft: „a unified … methodology" statt „the first"; „ausgerichtet an GHG Protocol/IPCC AR6 (angewandt, nicht formal zertifiziert)" statt „konform"; „Mathematische Validierung (intern, r=0,94; keine externe Begutachtung)". Maßstab: *unbelegt vs. methodisch-belegt*, nicht *klingt-stark*.
**Status:** ✅ adressiert (PR #19/#21) · **Beleg:** README, co2_master `validation_approach`.

---

## Priorisierung vor Corrigendum-Versand (kritischer Pfad)

Die mit ⏳ markierten Punkte sind die echten review-ready-Gates (wissenschaftliche Arbeit, keine Doku-Edits):
1. ~~**§8.2 YAML-Domain-Zuordnungs-Bereinigung**~~ ✅ **erledigt 2026-05-30** — Befund: Tag-Drift war in `co2_master` v1.3 (2026-05-28) bereits bereinigt, nur Doku stale; nachgezogen (HEBEL_KATALOG v1.12). Double-Counting/Overlap bereits auf Domain-Total-Ebene sauber. Rest: F23/F24-Wert-Ownership (total-neutral) — #4
2. **49×49-Konflikt-Matrix** ✅ **Erst-Entwurf 2026-05-30** (`studies/CONSISTENCY_MATRIX_2026-05-30/`, 44×44, C-Achse auditierbar); ⏳ **Sankey** + systematische Konflikt-Elicitation — #1, #4
3. **Out-of-sample-Test** — ✅ **erste Probe 2026-05-30** (`studies/OUT_OF_SAMPLE_2026-05-30/`, N=3, Skala 0,19–0,94: PKW-Maut ↔ ASFINAG ↔ Währungsreform); ⏳ powered/verblindet/prä-registriert offen — #5
4. ~~**MCDA/IAM/RDM-Vergleichstabelle**~~ ✅ **erledigt 2026-05-30** → `canon/METHOD_POSITIONING.md` — #6
5. ~~**Hebel-Selektions-Logik dokumentieren**~~ ✅ **erledigt 2026-05-30** → `canon/LEVER_SELECTION.md` — #7

Erledigt: die doku-schreibbaren 📋-Punkte (Q6, Q7, Q10), die Gewichts-Sensitivität (Q2, `studies/SENSITIVITY_2026-05-30/`), §8.2 (Item 1 — war stale-Doku) und der Out-of-sample-Test (Item 3, Q5 — erste Probe `studies/OUT_OF_SAMPLE_2026-05-30/`; powered/verblindet bleibt offen). **Verbleibend:** von Item 2 ist die 49×49-Matrix als Erst-Entwurf erledigt — offen nur noch die **Sankey-Visualisierung** + die systematische Paar-für-Paar-Konflikt-Elicitation (Q1/Q4).
