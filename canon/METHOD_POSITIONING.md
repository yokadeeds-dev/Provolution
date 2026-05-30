# Methodische Einordnung — SEC-J / Probatio Systemica gegenüber MCDA, IAM & RDM

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement (Entwurf) · **Companion zu:** [`canon/STATUS.md`](STATUS.md), [`canon/LIMITATIONS.md`](LIMITATIONS.md)

Dieses Dokument beantwortet den Reviewer-Einwand „Was ist neu gegenüber 30 Jahren Entscheidungswissenschaft?" ([`LIMITATIONS.md`](LIMITATIONS.md) #14). Es **formalisiert und erweitert** die bereits im Manuskript (§6.2, „Probatio Systemica vs. MCA/MCDA") angelegte Abgrenzung zu einer prüfbaren Vergleichstabelle. Es erhebt **keinen Neuheits-Alleinanspruch** auf Nicht-Kompensation oder Veto-Logik — diese existieren in der MCDA-Literatur (ELECTRE, lexikografische Verfahren). Der Beitrag liegt in der **Kombination** und der **Domänen-Anwendung**, nicht in einer einzelnen erfundenen Mechanik.

> **Note for external readers (EN):** This file positions SEC-J / Probatio Systemica relative to established decision-science families (MCDA, IAM, RDM). It does **not** claim sole novelty for non-compensatory or veto logic — those exist in MCDA (ELECTRE, lexicographic methods). The contribution is the *combination* and the *domain application*. Authoritative values: [`canon/STATUS.md`](STATUS.md).

---

## 1. Die drei Referenz-Familien

| Familie | Vertreter | Grundidee |
|---|---|---|
| **MCDA** (Multi-Criteria Decision Analysis) | AHP (Saaty), ELECTRE (Roy), PROMETHEE (Brans), SMART, TOPSIS, MAUT/MAVT | Alternativen anhand mehrerer, gewichteter Kriterien ordnen oder ausranken. Gewichte meist aus Stakeholder-Präferenzen (Befragung, Paarvergleich). |
| **IAM** (Integrated Assessment Models) | DICE/RICE (Nordhaus), FUND (Tol), PAGE (Hope) | Klima-Ökonomie-Kopplung; berechnen optimale Emissionspfade und den sozialen CO₂-Preis (SCC) über eine diskontierte Wohlfahrtsfunktion. |
| **RDM** (Robust Decision Making) | Lempert, Popper, Bankes (RAND) | Strategien über sehr viele Szenarien stress-testen; nicht eine „optimale", sondern eine **robust-satisficing** Strategie suchen (deep uncertainty). |

**Was Provolution / PS-U ist:** ein **Screening-/Prüf-Framework für die systemische Tragfähigkeit einzelner Maßnahmen** (SEC-J-Score + Verdict). Es ist **kein** Optimierer, **kein** IAM (berechnet weder SCC noch optimale Pfade) und **kein** Szenario-Explorer. Es ist damit eher **komplementär** zu diesen Familien als konkurrierend.

---

## 2. Vergleichstabelle

| Dimension | MCDA | IAM | RDM | **SEC-J / PS-U 2.0** |
|---|---|---|---|---|
| **Primärer Zweck** | Alternativen-Ranking nach Kriterien | Klima-Ökonomie-Optimierung | robuste Strategie bei tiefer Unsicherheit | Tragfähigkeits-Screening einzelner Maßnahmen |
| **Output** | Rangordnung / Outranking-Relation | optimaler Pfad, sozialer CO₂-Preis | robuste-satisficing Strategiemenge | SEC-J-Score + Verdict (TRAGFÄHIG … / J-VETO) |
| **Gewichts-Herkunft** | meist Stakeholder-Präferenzen (elicitiert) | implizit über Nutzenfunktion + Diskontrate | keine festen Kriteriengewichte | **fixe, offengelegte normative Gewichte** (0,30/0,25/0,30/0,15) |
| **Kompensation** | überwiegend kompensatorisch; ELECTRE & lexikografische Verfahren teils nicht-kompensatorisch (Veto-Schwellen) | kompensatorisch (Aggregation in Wohlfahrt) | n/a (Robustheit statt Aggregation) | **nicht-kompensatorisch an einer Stelle**: harter J-Veto (J<0,50 → SEC-J=null) ¹ |
| **Gerechtigkeit** | als ein Kriterium unter vielen — voll aufrechenbar | über Diskontierung / Schadensgewichtung (normativ umstritten) | meist nicht explizit | **eigene Achse J + harte Sperrschwelle** (nicht durch S/E/C aufrechenbar) |
| **Cross-Domain-Konsistenz** | nicht systematisch (pro Alternative bewertet) | endogen im Modellkern, aber rein ökonomisch | über Szenarien, nicht als eigenes Kriterium | **eigene gescorte Achse** C = 1 − (K+U)/I_ges ² |
| **Unsicherheits-Behandlung** | Sensitivitäts-/Robustheitsanalyse optional | probabilistisch / parametrische Monte-Carlo | **Kernstärke**: Exploration über Szenarienraum | Monte-Carlo-Bänder + 50 %-Umsetzungs-Stresstest (RDM-nah) |
| **Transparenz / Reproduzierbarkeit** | abhängig von Präferenz-Elicitation | hoch, aber annahmen-sensitiv (Diskontrate) | hoch | hoch: **eine** universelle Formel, offengelegte Gewichte, CC0/forkbar |

¹ Operativer Schwellenwert: `veto_threshold: 0.50` (`impact_master.yaml` → `sec_j_scores.meta`). Im **STANDARD**-Modus greift zusätzlich eine weichere J<0,40-Flag (SOZIALE INKONSISTENZ, kein Stopp); im **JUSTICE**-Modus ist J<0,50 ein harter Stopp (Spec §3/§4). „Nicht-kompensatorisch an einer Stelle" meint: ein Justice-Versagen unterhalb der Sperrschwelle kann **nicht** durch hohe S/E/C zurückgekauft werden.
² Konflikte K, unerfüllte Abhängigkeiten U über alle Interaktionen I_ges (Band 5 §2; binäre 0/1-Form als konservative Screening-Vereinfachung markiert — vgl. [`LIMITATIONS.md`](LIMITATIONS.md) #6).

---

## 3. Kern-Differenzierung (ehrlich, ohne Überclaiming)

Keine der folgenden Eigenschaften ist für sich genommen neu. Neu ist ihre **Bündelung in einem reproduzierbaren Maßnahmen-Screening** für die Klima-Transformation:

1. **Fixe, universelle Gewichte statt elicitierter Präferenzen.** Anders als die meisten MCDA-Anwendungen verzichtet PS-U bewusst auf maßnahmenspezifische Stakeholder-Gewichtung — weniger flexibel, dafür über alle Maßnahmen hinweg vergleichbar und reproduzierbar (so bereits im Manuskript §6.2 argumentiert).
2. **Eine normativ verankerte Gerechtigkeits-Sperrschwelle** statt eines pro-Paar-Vergleichs-Vetos (ELECTRE) oder einer rein kriterialen Gewichtung. Der J-Veto ist die Verlustbegrenzungs-Komponente des Antifragilitäts-Prinzips ([`canon/de/ANTIFRAGILITY_PRINCIPLE.md`](de/ANTIFRAGILITY_PRINCIPLE.md)), nicht ein technischer Outranking-Parameter.
3. **Cross-Domain-Konsistenz als first-class, gescorte Achse (C)** — nicht als nachgelagerte Plausibilitätsprüfung. Die C-Achse adressiert genau das im Manuskript benannte Problem #2 (Maßnahmen, die einzeln valide, gemeinsam widersprüchlich sind).
4. **Screening statt Optimierung.** PS-U ersetzt kein IAM und keinen SCC; es filtert Maßnahmen auf systemische Tragfähigkeit, bevor (und während) andere Verfahren Pfade oder Preise berechnen.

**Abgrenzung gegen ELECTRE explizit:** ELECTRE kennt Veto-Schwellen pro Kriterium im paarweisen Outranking. PS-U setzt stattdessen **eine** globale, normativ begründete Veto-Achse (Gerechtigkeit) auf den absoluten Maßnahmen-Score — kein paarweises Outranking. Das ist eine andere Konstruktion, kein „besseres ELECTRE".

---

## 4. Was PS-U *nicht* leistet (Grenzen)

- **Keine ökonomische Optimierung:** kein sozialer CO₂-Preis, kein optimaler Emissionspfad, keine Wohlfahrtsmaximierung. Wer das braucht, nutzt ein IAM — PS-U und IAM sind komplementär.
- **Keine Szenarienraum-Exploration im RDM-Sinn:** PS-U teilt RDMs Robustheits-Ethos (Stresstest, Monte-Carlo-Bänder), exploriert aber nicht systematisch den vollen Szenarienraum.
- **Volle Gewichts-Sensitivitätsanalyse steht aus:** ein systematischer Abgleich mit AHP/SMART über plausible Gewichtungsbereiche fehlt noch (siehe [`LIMITATIONS.md`](LIMITATIONS.md) #12). Bekannt ist nur die grobe Robustheit (±20 % Parametervariation → <±15 % Gesamtwert).

---

## 5. Anschluss an das Manuskript

Diese Datei vertieft den Absatz **„Probatio Systemica vs. MCA/MCDA"** in `manuscript/MANUSCRIPT_DRAFT_v0.1.md` §6.2. Für die finale ESG-Response-to-Reviewers ist der Inhalt ins Englische zu übertragen (vgl. [`manuscript/RESPONSE_TO_REVIEWERS_PREP.md`](../manuscript/RESPONSE_TO_REVIEWERS_PREP.md) Q6).

---

*Companion-Dokumente: [`canon/STATUS.md`](STATUS.md) · [`canon/LIMITATIONS.md`](LIMITATIONS.md) · [`canon/LEVER_SELECTION.md`](LEVER_SELECTION.md) · SEC-J-Spec [`canon/de/06_framework_extensions_v2.0_SECJ.md`](de/06_framework_extensions_v2.0_SECJ.md).*
