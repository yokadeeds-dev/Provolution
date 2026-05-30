# Hebel-Selektion — Aufnahme- und Ausschluss-Kriterien

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement (Entwurf) · **Companion zu:** [`canon/STATUS.md`](STATUS.md), [`canon/LIMITATIONS.md`](LIMITATIONS.md)

Dieses Dokument beantwortet den Reviewer-Einwand „Warum genau diese 49 Hebel — nicht 39 oder 59? Was wurde nach welchem Kriterium ausgeschlossen?" ([`LIMITATIONS.md`](LIMITATIONS.md) #15). Es macht die **bislang diskretionär begründete** Hebel-Menge in ihrer Selektions-Logik **explizit**. Es ist ehrlich: die Menge ist **historisch gewachsen und konsolidiert**, nicht aus einem Axiomensatz **deduziert** — die hier dokumentierten Kriterien sind die *erklärte* Aufnahme-Logik, keine nachträgliche Rationalisierung einer geschlossenen Liste.

> **Note for external readers (EN):** This file states the inclusion/exclusion criteria behind the 49-lever set. The set is **historically grown and consolidated**, not deductively derived; the criteria here are the *stated* selection logic, and exclusions are documented value+method decisions open to challenge. Authoritative counts: [`canon/STATUS.md`](STATUS.md) §3.

---

## 1. Provenienz der Hebel-Menge (ehrlich)

Die 49 Hebel sind **nicht** aus einem geschlossenen Ableitungs-Schema entstanden, sondern über mehrere Iterationen gewachsen und 2026-05-09 konsolidiert. Der [`canon/de/HEBEL_KATALOG_v1.0.md`](de/HEBEL_KATALOG_v1.0.md) (SSoT für „was *ist* ein Hebel") löste damals eine SET-Drift zwischen drei divergierenden Quellen auf (Band 4 = 30 Apps, `co2_master.yaml` = 35 Einträge, MASTER_INDEX = 40). Die Menge ist **offen und erweiterbar**, nicht abgeschlossen — neue Hebel treten über die Kandidaten-Pipeline ein (§5).

Genau diese Provenienz ist der Grund, dass die Selektion bis hierher als „diskretionär begründet, nicht deduktiv" markiert war ([`LIMITATIONS.md`](LIMITATIONS.md) #15). Dieses Dokument schließt die *Dokumentations*-Lücke; die vollständige *deduktive* Herleitung bleibt offen (§6).

---

## 2. Aufnahme-Kriterien

Ein Kandidat wird als Hebel aufgenommen, wenn er **alle** folgenden Bedingungen erfüllt:

| # | Kriterium | Operationalisierung |
|---|---|---|
| **K1** | **Technisch/systemisch realisierbar** | Belegbar durch Pilote, Forschung, Motorsport, industrielle Vorläufer **oder** historische Beispiele. **Großserien-/Status-quo-Reife ist *kein* Kriterium** (sonst würde das Framework nur den Ist-Zustand fortschreiben). |
| **K2** | **SEC-J-tragfähig** | Verdict ≥ 0,80 (TRAGFÄHIG) im PS-U-2.0-Audit — oder bedingt tragfähig mit **dokumentierter Implementierungs-Auflage**. **Kein** ausgelöster J-Veto (J ≥ 0,50). |
| **K3** | **Keine ungelösten Gerechtigkeits-/Konsistenz-Konflikte** | J < 0,80 ist als **Warnschwelle** mit Auflage zulässig (z. B. B09, B11, B12, C12); J < 0,50 sperrt hart (Antifragilitäts-Veto). C-Konflikte mit anderen Hebeln müssen benannt und auflösbar sein. |
| **K4** | **Systemwirkung benennbar** | Entweder quantifiziert (Gt CO₂eq/Jahr in `co2_master.yaml`) **oder** klar qualitativ als Enabler (Domains A/E/F/G/H — Governance, Bildung, Technologie, Monitoring, Meta). Eine reine „0-Wirkung ohne Funktion" wird nicht aufgenommen. |
| **K5** | **Status-Klasse transparent** | Jeder Hebel trägt eine Reife-Klasse (§3), damit Vollkonzept, Stub und nur-quantifizierte Einträge unterscheidbar bleiben. |

**Kernpunkt zu K2/K3:** Aufnahme heißt **nicht** „technisch möglich", sondern „technisch möglich **und** SEC-J-tragfähig **und** ohne ungelösten Justice-/Konsistenz-Konflikt". K1 öffnet das Feld weit (nicht nur Status quo), K2/K3 sind das eigentliche Filter.

---

## 3. Status-Klassen (Reifegrade)

| Klasse | Bedeutung | Anzahl (Stand v1.5) |
|---|---|---:|
| `band4-canonical` | Vollkonzept in Band 4 v4.2 dokumentiert | 38 |
| `stub` | STUB-File vorhanden, Band-4-Beschreibung ausstehend | 1 (I34) |
| `yaml-only` | quantifiziert in YAML, noch nicht in Band 4 | 5 (B11, B12, F22, G28, G29) |
| `community-integration` | über AGENTIC-INTEGRATE-Pipeline akzeptiert, außerhalb A–K | 5 |
| **Gesamt** | | **49** (11 Domänen A–K) |

Quelle: [`canon/de/HEBEL_KATALOG_v1.0.md`](de/HEBEL_KATALOG_v1.0.md) (autoritative Zählung) · [`canon/STATUS.md`](STATUS.md) §3.

---

## 4. Bewusst (noch) nicht im Portfolio

Die folgenden, in der Klimadebatte prominenten Optionen sind **nicht** als Hebel aufgenommen. Die Begründung ist jeweils **kriteriengeleitet** (K1–K3) und als **dokumentierte Wert- und Methoden-Entscheidung markiert — challenge-bar**, nicht als bewiesene Unterlegenheit. Wo kein formales PS-U-Audit vorliegt, ist das ausgewiesen.

| Option | Status | Kriteriengeleitete Begründung |
|---|---|---|
| **Biokraftstoffe (für Fahrzeug-Antrieb)** | ✅ **explizit ausgeschlossen** (im Kanon belegt) | Band 4 v4.2, Hebel I33 §12: „Wirkungsgrad-Kollaps". Scheitert an **K2 (E)** — Flächen-/Energie-Effizienz gegenüber BEV. (Stoffliche Hanf-/Rest-Biomasse-Nutzung bleibt über B08/B12 erhalten — der Ausschluss betrifft die **Verbrennung zum Antrieb**.) |
| **Kernkraft** | 🔶 zurückgestellt (nicht formal auditiert) | Diskretionäre Wertung über **K2/K3**: Bauzeit-/Kosten-Effizienz (E), Endlager- und intergenerationale Gerechtigkeit (J), Konsistenz mit der dezentral-erneuerbaren Linie C11–C14 (C). **Kein** Per-se-Verbot — sondern (noch) nicht als SEC-J-tragfähiger Hebel aufgenommen. Ein formales PS-U-Audit ist möglich und willkommen (§6). |
| **BECCS / DAC** | 🔶 als Benchmark referenziert, nicht als Hebel | DAC erscheint im Kanon als **Kosten-Vergleichsanker** (D16: ~€10–50/t boden­basiert vs. ~€300/t DAC), nicht als eigener Hebel — Begründung **K2 (E, Kosten/Energie)**. BECCS-nahe Biomasse-Risiken (Landkonkurrenz, Tank-oder-Teller) sind über die **B12-Warnschwelle** (J=0,75, FPIC-Auflage) abgebildet statt als unkonditionierter Hebel. |
| **Großskaliges Solar-Geoengineering (SRM)** | 🔶 zurückgestellt (nicht formal auditiert) | Scheitert an **K3**: Termination-Shock / Reversibilitäts-Risiko, globale Verteilungs-Asymmetrie (J), Governance-Lücke — unvereinbar mit dem **Antifragilitäts-Prinzip** (katastrophaler Tail statt Verlustbegrenzung). |

**Lesart:** K1 (technische Möglichkeit) genügt für keine dieser Optionen zur Aufnahme — es sind **K2/K3** (Effizienz, Gerechtigkeit, Konsistenz, Antifragilität), an denen sie zurückgestellt oder ausgeschlossen werden. Das ist konsistent mit dem Framework-Prinzip „technische Realisierbarkeit reicht für die *Prüfung*, nicht für die *Aufnahme*".

---

## 5. Kandidaten-Pipeline (das Set ist offen)

Neue Hebel treten nicht ad hoc ein, sondern über die **AUTO-INTEGRATE-Pipeline** mit PS-U-Audit:

- **Kategorie A** (audit-reif) → Promotion bei Verdict ≥ 0,82 und bestandenen kritischen E-Ebenen. Beispiel: **I35** (Aktive Geschwindigkeits-Regulation, SEC 0,84) promoted; **D19** (Algen-Bioraffinerie) Kategorie B → A.
- **Kategorie B** (vielversprechend, Daten offen) → bleibt in der Pipeline bis empirische Fundierung steht. Beispiel: **I36** (Schwere-Nfz) — hinter I34 zurückgestellt, weil Materialbelastbarkeit/Antriebs-Roadmap noch offen.

Das belegt: die Menge ist **erweiterbar und revidierbar**, nicht willkürlich fix. Belege: [`studies/AUTO_INTEGRATE_AUDIT_2026-05-28/`](../studies/AUTO_INTEGRATE_AUDIT_2026-05-28/), `canon/de/HEBEL_KATALOG_v1.0.md` Drift-Items #14, #18.

---

## 6. Offene Punkte

- **Systematisches kriteriengeleitetes Scoring der ausgeschlossenen Optionen** (eigene PS-U-Audits für Kernkraft, BECCS, SRM, statt qualitativer Begründung) steht aus. Bis dahin sind die Ausschlüsse in §4 **dokumentierte, challenge-bare Wertungen**, keine auditierten Verdikte.
- **Vollständige deduktive Herleitung** der Hebel-Menge (statt historisch-konsolidiert + Kriterien-Filter) bleibt künftige Arbeit (vgl. [`LIMITATIONS.md`](LIMITATIONS.md) #15).
- Für die finale ESG-Response ins Englische zu übertragen (vgl. [`manuscript/RESPONSE_TO_REVIEWERS_PREP.md`](../manuscript/RESPONSE_TO_REVIEWERS_PREP.md) Q7).

---

*Companion-Dokumente: [`canon/STATUS.md`](STATUS.md) · [`canon/LIMITATIONS.md`](LIMITATIONS.md) · [`canon/METHOD_POSITIONING.md`](METHOD_POSITIONING.md) · Hebel-Index [`canon/de/HEBEL_KATALOG_v1.0.md`](de/HEBEL_KATALOG_v1.0.md).*
