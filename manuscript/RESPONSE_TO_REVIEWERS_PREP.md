# Response-to-Reviewers — Vorbereitung (INTERN / Arbeitsdokument)

**Stand:** 2026-05-29 · **Status:** INTERNES Vorbereitungs-Dokument — **nicht Teil der Einreichung**
**Zweck:** Die wahrscheinlichsten ESG-Reviewer-Einwände vorab durchschreiben, damit auf jeden eine belegte Antwort bereitliegt. Konsolidiert aus [`canon/LIMITATIONS.md`](../canon/LIMITATIONS.md) + adversarialen KI-Pässen ([`studies/AI_AUDIT_2026-05-28/`](../studies/AI_AUDIT_2026-05-28/)).

> **Hinweis:** Die *finale* Response-to-Reviewers an ESG ist auf **Englisch** zu verfassen. Dies ist die deutsche Arbeitsfassung der Argumente; bei den Reviews adaptieren/übersetzen.

**Status-Legende:** ✅ adressiert (im Repo belegt) · ⏳ offen, geplant (echte wissenschaftliche Arbeit) · 📋 wird in der Revision/Corrigendum geliefert

---

## 1. „Operationalisieren Sie die Konsistenz-Relation (⊥)."

**Vorbereitete Antwort:** Die Consistency-Achse ist nicht binär-undefiniert. Die kontinuierliche Form ist `C = 1 − (K+U)/I_ges` (Konflikte K, unerfüllte Abhängigkeiten U über alle Interaktionen I_ges; Band 5 §2). Die binäre 0/1-Variante ist als **konservative Screening-Vereinfachung** markiert. Die reproduzierbare Bestimmung von K/U pro Hebel — als auditierbare **Hebel-zu-Hebel-Konflikt-Matrix (49×49)** mit operationalen Kriterien (Ressourcen-Konkurrenz, gegenläufige Anreize, Rebound-Typ) — wird als Supplement nachgereicht.
**Status:** ✅ Formel vorhanden · 📋 49×49-Matrix als Supplement · **Beleg:** LIMITATIONS #6, #16.

## 2. „Begründen Sie die SEC-J-Gewichte. Sensitivitätsanalyse?"

**Vorbereitete Antwort:** Die Gewichte (0,30·S + 0,25·E + 0,30·C + 0,15·J) sind eine **explizite, dokumentierte und diskutierbare Wertentscheidung** (`framework_extensions_v2.0_SECJ.md`), kein verstecktes Axiom. Entscheidend: **J wirkt primär über das harte Veto (J<0,50 → SEC-J=null), nicht über sein Komposit-Gewicht.** Für gerechtigkeits-primäre Maßnahmen existiert der JUSTICE-Modus (J=0,40). Grobe Robustheit ist belegt (±20 % Parametervariation → <±15 % Gesamtwert); eine vollständige Sensitivitätsanalyse über plausible Gewichtungsbereiche (+ Abgleich AHP/SMART) folgt als Anhang.
**Status:** ✅ dokumentiert · 📋 Sensitivitäts-Anhang · **Beleg:** LIMITATIONS #5, #12.

## 3. „Wo ist die Justice-Dimension? Das Manuskript sagt ‚under development'."

**Vorbereitete Antwort:** SEC-J ist seit 2026-05-10 **kanonisch** (PS-U 2.0): fixe Formel, J-Veto bei J<0,50, J-Flag bei <0,40 (`canon/STATUS.md` §1). Die „under development"-Phrase stammt aus einem **älteren eingereichten Manuskript-Stand**; ein Corrigendum dokumentiert die SEC→SEC-J-Migration und wird ESG nachgereicht, sobald der Repo-Stand review-ready ist.
**Status:** ✅ im Canon · 📋 Corrigendum an ESG · **Beleg:** STATUS.md §1, `framework_extensions_v2.0_SECJ.md`.

## 4. „−58,6 Gt = Überclaiming. Double-Counting-Audit?"

**Vorbereitete Antwort:** −58,6 Gt ist ein **gescreentes Potenzial, keine Prognose**. Der realistische Netto-Erwartungswert ist der Monte-Carlo-Median **−43,2 Gt/Jahr** [90 %-KI −52,8…−34,6], im 50 %-Umsetzungs-Stresstest **−14,9 Gt/Jahr**. Per-Domain-Overlap ist bereinigt (z. B. B07 schluckt B08–B12: −32 → ~−16 Gt). **Offen:** Sankey-Visualisierung der Carbon-Flows, Inter-Domain-Rückkopplung, abschließende YAML-Domain-Zuordnungs-Bereinigung. Beide Werte werden in README/STATUS gleichrangig kommuniziert.
**Status:** ✅ MC-Median + Per-Domain-Overlap · ⏳ Sankey/Inter-Domain/YAML-Bereinigung · **Beleg:** STATUS.md §2, LIMITATIONS #2, #16.

## 5. „Falsifizierbarkeit — oder nur innere Konsistenz?"

**Vorbereitete Antwort:** Eingeräumt: innere Konsistenz ist **nicht** dasselbe wie ein prädiktiver Test. Das J-Veto ist konkret operationalisiert (harte Sperrschwelle), aber ein echter **Out-of-sample-Vorhersagetest** (sagt SEC-J reale Erfolge/Misserfolge vorher? scheitert ein hoch bewerteter Hebel im Feld?) ist noch nicht definiert. Das ist offen benannt und als nächste Falsifizierungs-Stufe priorisiert.
**Status:** ⏳ offen · **Beleg:** LIMITATIONS #9, #13.

## 6. „Abgrenzung zu MCDA / IAM / Robust Decision Making?"

**Vorbereitete Antwort:** Eine tabellarische Einordnung gegenüber AHP/ELECTRE/PROMETHEE (MCDA), DICE/FUND/PAGE (IAM) und Lempert et al. (RDM) wird als Supplement vorbereitet. Kern-Differenzierung, die zu prüfen ist: das **J-Veto als lexikographische Sperrschwelle** (nicht additiv kompensierbar — anders als gewichtete MCDA-Summen) und **Cross-Domain-Konsistenz als First-Class-Kriterium** statt nachgelagerter Prüfung.
**Status:** 📋 Vergleichstabelle in Revision · **Beleg:** LIMITATIONS #14.

## 7. „Warum genau diese 49 Hebel? Was wurde ausgeschlossen?"

**Vorbereitete Antwort:** Die Selektions-Logik (Aufnahme- und Ausschluss-Kriterien) ist noch nicht systematisch dokumentiert — bis dahin ist die Hebel-Menge diskretionär begründet. Bewusst (noch) nicht im Portfolio: u. a. Kernkraft, BECCS/DAC, großskaliges Geoengineering; die Begründung (Kriterium: technisch/systemisch realisierbar + SEC-J-tragfähig + keine ungelösten Just-/Konsistenz-Konflikte) wird nachgeliefert.
**Status:** ⏳ offen · **Beleg:** LIMITATIONS #15.

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
1. **§8.2 YAML-Domain-Zuordnungs-Bereinigung** (Double-Counting endgültig sauber) — #4
2. **Sankey + 49×49-Konflikt-Matrix** (materialisiert Konsistenz auditierbar) — #1, #4
3. **Out-of-sample-Test definieren** — #5
4. **MCDA/IAM/RDM-Vergleichstabelle** (📋, schreibbar ohne neue Daten) — #6
5. **Hebel-Selektions-Logik dokumentieren** (📋, schreibbar) — #7

Die 📋-Punkte (4, 5, 6, 10) sind ohne neue Daten erstellbar; die ⏳-Punkte (1, 5, 7) brauchen echte Analyse-Arbeit.
