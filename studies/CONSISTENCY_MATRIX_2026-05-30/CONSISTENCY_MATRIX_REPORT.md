# Hebel-Konsistenz-/Konflikt-Matrix — C-Achse materialisiert

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement / Erst-Entwurf (Hälfte 1 von Punkt 4) · **Companion zu:** [`canon/STATUS.md`](../../canon/STATUS.md), [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #16
**Reproduzierbar:** `python studies/CONSISTENCY_MATRIX_2026-05-30/build_consistency_matrix.py` → `consistency_matrix.csv` (44×44)

Antwort auf den Reviewer-Einwand „Operationalisieren Sie die Konsistenz-Relation (⊥) — eine auditierbare Hebel-zu-Hebel-Matrix fehlt" ([`LIMITATIONS.md`](../../canon/LIMITATIONS.md) #16, Reviewer-Q1/Q4). Macht die C-Achse aus einer Behauptung zu einem **prüfbaren Artefakt**: jede Hebel-Beziehung ist mit Quelle hinterlegt und einzeln widerlegbar.

> **Note for external readers (EN):** Materializes the consistency (⊥) relation as an auditable 44×44 lever-interaction matrix. Edges are **extracted from the canon's own documented relations** (Band 4 "Consistent:"/"Synergien:" lines, co2_master overlaps, impact_master warning notes) — not invented; inferred edges are listed separately and excluded from the matrix. The synergy assertions are the authors' and now **checkable**, not externally proven (§5).

---

## 1. Methode (grounded, nicht erfunden)

Für jedes der 44 A–K-Hebel-Paare wird eine Beziehung bestimmt:

| Typ | Bedeutung | Quelle |
|---|---|---|
| **SYN** | Synergie / Kohärenz | geparst aus den Band-4-„**Consistent:**"- und „**Synergien:**"-Zeilen der Hebelsektion (= dort *explizit behauptete* Kohärenz) |
| **OVL** | Bilanz-Overlap (Doppelzählung im CO₂-Accounting) | `co2_master.yaml → double_counting_prevention` |
| **CONF** | Konflikt / Ressourcen-Konkurrenz | `impact_master.yaml` Warnschwellen-Notizen (dokumentiert) |
| **DEP** | Abhängigkeit / Implementierungs-Auflage | `impact_master.yaml` Notizen (dokumentiert) |
| **INFERRED** | eigene Hypothese, **nicht** kanon-belegt | **separat gelistet, NICHT in Matrix/C-Proxy** (§5) |

**C-Proxy:** `C* = 1 − (CONF + unerfüllte DEP) / Interaktionen` (Interaktionen = SYN+DEP+CONF+OVL). DEP gelten hier als erfüllbar (Auflagen dokumentiert → U≈0); OVL ist Accounting, kein Viability-Konflikt → nicht im Zähler. Das ist eine **strukturelle Annäherung** an die kanonische Form `C = 1 − (K+U)/I_ges` (Band 5 §2), nicht deren Ersatz.

---

## 2. Ergebnis-Übersicht

- **44** A–K-Hebel · **39** Band-4-Sektionen geparst · **5 ohne** Band-4-Sektion (B11, B12, F22, G28, G29 = yaml-only → keine Synergien geparst).
- **121 dokumentierte Kanten:** **110 SYN**, **6 OVL**, **2 CONF**, **3 DEP**.
- Die Matrix ist dicht an Synergien und arm an dokumentierten Konflikten — was die framework-interne Kohärenz-Behauptung **strukturell stützt** (mit der Einschränkung §5, dass die Synergien selbst-behauptet sind).

---

## 3. Die auditierbaren Nicht-Synergie-Kanten (das Kernstück)

Jede dieser Kanten ist einzeln prüf- und widerlegbar:

| Paar | Typ | Beleg |
|---|---|---|
| B07 ↔ B08/B09/B10/B11/B12/B13 | **OVL** | co2_master `double_counting_prevention` (B07 −23 → −15,8 nach Overlap-Abzug) |
| B12 ↔ D15 | **CONF** | impact_master B12-Warnung: Tank-oder-Teller / Flächenkonkurrenz |
| B12 ↔ D18 | **CONF** | impact_master B12-Warnung: Tank-oder-Teller / Flächenkonkurrenz |
| B09 ↔ C12 | **DEP** | impact_master C12-Warnung: Li/Co-Lieferkette → B09-Transparenz zwingend |
| C12 ↔ H31 | **DEP** | impact_master C12-Warnung: → H31-Regulierung zwingend |
| D16 ↔ G27 | **DEP** | impact_master D16-Notiz: G27-Monitoring der Carbon-Payments zwingend |

Die 6 OVL-Kanten sind **Accounting-Overlaps** (in der CO₂-Aggregation bereits bereinigt, Netto-Median −43,2 Gt) — keine Viability-Konflikte. Die 3 DEP-Kanten sind **dokumentierte Implementierungs-Auflagen** (erfüllbar). Echte **Viability-Konflikte: nur 2**, beide an B12.

---

## 4. C-Proxy + Konkordanz

| Hebel | C* | Profil | Anmerkung |
|---|---:|---|---|
| **B12** Nachhaltige Biomasse | **0,50** | SYN 1, CONF 2, OVL 1 | beide dokumentierten Konflikte; **niedrigster** struktureller C* |
| **D18** Urbane LW | 0,80 | SYN 4, CONF 1 | trägt eine B12-Konfliktseite |
| **D15** Regen-LW | 0,88 | SYN 7, CONF 1 | trägt eine B12-Konfliktseite |
| *(übrige 41 Hebel)* | **1,00** | nur SYN/DEP/OVL | keine dokumentierten Konflikte |

**Konkordanz-Befund:** Der einzige Hebel mit deutlich niedrigem strukturellem C\* (**B12 = 0,50**) ist **exakt** der Hebel, den das Framework unabhängig als Warnschwelle führt (B12: J=0,75, C=0,80, FPIC-Auflage). Die *strukturelle* Konflikt-Zählung und das *bewertete* C/J zeigen also auf denselben Hebel — ein Hinweis, dass die C-Achse nicht beliebig vergeben ist, sondern reale Interaktions-Spannungen einfängt.

**Nicht überinterpretieren:** Die meisten C\*=1,00 spiegeln *fehlende dokumentierte Konflikte*, nicht *bewiesene Konfliktfreiheit* (Konflikte sind konservativ/untererfasst — §5).

---

## 5. Grenzen (kritisch, offen)

1. **Synergien sind selbst-behauptet.** Die 110 SYN-Kanten stammen aus den „Consistent:"-Zeilen des Kanons — also der Aussage der Autoren, dass diese Hebel kohärent seien. Der Wert der Matrix ist **Auditierbarkeit** (jede Behauptung ist jetzt einzeln prüf-/widerlegbar), **nicht** ein externer Beweis von Konsistenz.
2. **Konflikte sind untererfasst (konservativ).** Erfasst sind nur *dokumentierte* Konflikte (2). Eine systematische Paar-für-Paar-Konflikt-Elicitation (Ressourcen-Konkurrenz, gegenläufige Anreize, Rebound, Reihenfolge) durch Domänen-Expert:innen würde mit hoher Wahrscheinlichkeit weitere Konflikte finden → die C\* sind **optimistisch**.
3. **Abdeckungslücke.** 5 yaml-only-Hebel (B11/B12/F22/G28/G29) haben keine Band-4-Sektion → ihre Synergien sind nicht geparst (B12 erscheint nur über seine dokumentierten Konflikte/Overlaps).
4. **Parsing-Kanten:** Bereiche („C11–C14") werden endpunkt-basiert expandiert; seltene Prosa-Treffer möglich. Erst-Entwurf, zur Review.

---

## 6. Zur Review: inferierte Kanten (deine Entscheidung)

Diese Konflikte habe ich **hypothetisch** ergänzt — sie sind **nicht** kanon-belegt und **nicht** in Matrix/C-Proxy gezählt:

| Paar | Hypothese | Auditor-Einschätzung |
|---|---|---|
| D15 ↔ D17 | Hanf-Anbaufläche ↔ Nahrungsfläche | **Wahrscheinlich kein Konflikt:** der Kanon listet D15/D17 als **Synergie** (Hanf in Fruchtfolge regeneriert Boden; Multi-Use-Kaskade statt simpler Flächen-Konkurrenz). Empfehlung: **streichen**, außer es gibt einen konkreten Flächen-Trade-off-Beleg. |
| D17 ↔ D18 | Hanf-Anbaufläche ↔ urbane LW | dito — vermutlich kein realer Konflikt |
| B12 ↔ D17 | Biomasse ↔ Hanf-Anbaufläche | plausibler als die D17-D15/D18-Paare (beide flächenintensiv), aber unbelegt → deine Entscheidung |

---

## 7. Was als Nächstes

- **Hälfte 2 von Punkt 4 — Carbon-Flow-Sankey:** Visualisierung der OVL-Bereinigung (Brutto-Potenzial −87,1/−58,6 → Overlap-Abzug → realistischer Netto-Median −43,2). matplotlib ist verfügbar (3.10.8) → als Figur + Skript machbar. **Folge-PR.**
- **Härtung:** systematische Paar-für-Paar-Konflikt-Elicitation (Domänen-Review), Adjudikation der inferierten Kanten (§6), Synergie-Stichproben extern prüfen lassen.

---

*Companion: [`canon/STATUS.md`](../../canon/STATUS.md) · [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #16 · `consistency_matrix.csv` (44×44) · [`manuscript/RESPONSE_TO_REVIEWERS_PREP.md`](../../manuscript/RESPONSE_TO_REVIEWERS_PREP.md) Q1/Q4.*
