# Provolution — Limitations & Anticipated Critiques

**Stand:** 2026-05-29 · **Charakter:** offene Selbst-Kritik (antifragil) · **Companion zu:** [`canon/STATUS.md`](STATUS.md)

Dieses Dokument benennt die **stärksten Einwände** gegen Provolution/Probatio Systemica — und beantwortet sie. Das ist Absicht, nicht Schwäche: Ein Framework, dessen Kern **Antifragilität** ist (Stress als Information, J-Veto), muss seine eigene Angriffsfläche **offen besitzen** statt verstecken. Wer hier eine Lücke findet, liefert genau den Input, den das System zum Stärkerwerden braucht.

Dies ist **kein** Versuch, die Komplexität für ein breites Publikum zu glätten. Zielpublikum sind Reviewer und Forschende. Wo ein Einwand berechtigt ist, wird er eingeräumt und verortet — nicht weggeredet.

> **Note for external readers (EN):** This file openly states the strongest critiques of the framework and our responses. It is deliberate, not defensive: a framework whose core is *antifragility* must surface its own attack surface. Concedes what is true, scopes each claim, and points to where it is handled. Authoritative values: [`canon/STATUS.md`](STATUS.md).

---

## 1. „Einzelautor, kein externes Peer Review"

**Einwand:** Das ist das Framework einer Einzelperson, nicht von der Fachgemeinschaft validiert.

**Antwort:** Eingeräumt und offen ausgewiesen — Preprint / living document, eingereicht bei *Earth System Governance*, **nicht extern peer-reviewed** (STATUS.md §4). Die internen Prüfläufe („Probatio Familia") sind als **selbst-administriert** gekennzeichnet, nicht als unabhängiges Review (§4). Gegengewicht: das Framework ist **explizit falsifizierbar**, vollständig dokumentiert, CC0/OHL-lizenziert und **forkbar zur unabhängigen Replikation**. Eine Reliabilitäts-Studie (Inter-Rater + Blind-Retest, N=10) existiert als Reproduzierbarkeits-Artefakt — innerhalb der Autoren-Infrastruktur, also kein externer Ersatz, aber ein prüfbarer Anfang. **Externe Replikation ist ausdrücklich erwünscht.**

## 2. „−58,6 / −87,1 Gt / 106,5 % — mehr als die globalen Emissionen, das ist Überclaiming"

**Einwand:** Ein Potenzial über 100 % der globalen Emissionen klingt nach „wir lösen mehr als das ganze Problem".

**Antwort:** Diese Werte sind **gescreente technisch/systemische Potenziale unter definierten Annahmen — keine Prognosen** und keine sofort realisierbaren Jahres-Reduktionen (STATUS.md §2). Sie enthalten Overlaps, Constraints und Unsicherheitsbänder. Die **realistische Netto-Größe** sind die Monte-Carlo-Mediane: **−43,2 Gt/Jahr** (Szenario B) bzw. **−14,9 Gt/Jahr** im 50 %-Umsetzungs-Stresstest — beide deutlich unter dem Potenzial-Ceiling. Die 106,5 % bezeichnen ein Potenzial-Maximum (inkl. aktiver Sequestrierung), nicht eine erwartete Realisierung. Der Wert ist als Potenzial markiert, nicht als Vorhersage.

## 3. „‚Scientific Framework' und ‚Mathematische Validierung' trotz fehlendem Peer Review = Selbstzertifizierung"

**Einwand:** Starke Begriffe ohne externe Bestätigung.

**Antwort:** „Scientific" bezieht sich auf die **Methode** (falsifizierbar, formalisiert, dokumentiert, an GHG Protocol / IPCC AR6 ausgerichtet — angewandt, nicht formal zertifiziert), nicht auf den Peer-Review-Status, der offen als ausstehend ausgewiesen ist. „Mathematische Validierung" meint die **interne** Theorie↔Praxis-Korrelation (r=0,94); `co2_master.yaml → validation_approach.internal` nennt sie ausdrücklich „internal", external = Vergleich mit Sektor-Studien (IEA, McKinsey, Drawdown). Kein Anspruch auf externe Validierung — diese ist eingeladen.

## 4. „Die internen ‚PF'-Audits laufen in der eigenen KI-Umgebung — das ist zirkulär"

**Einwand:** Selbst-administrierte Audits in eigenen Gemini-Gems prüfen sich selbst.

**Antwort:** Vollständig offengelegt (STATUS.md §4): die Probatio-Familia-Läufe sind **strukturierte Selbst-Prüfung, kein unabhängiges Review** — und werden nirgends als solches verkauft. Ihr Nutzen ist Disziplin (Annahmen-Offenlegung, Drift-Erkennung), nicht externe Legitimation. Die Trennung *neutrales Prüf-Framework (Probatio Systemica)* vs. *Anwendung (Provolution)* macht zudem Kritik an einer Ebene möglich, ohne die andere zu verwerfen.

## 5. „Die SEC-J-Gewichte sind willkürlich; warum zählt Gerechtigkeit nur 0,15?"

**Einwand:** Wer legt 0,30/0,25/0,30/0,15 fest, und warum ist J so niedrig?

**Antwort:** Die Gewichte sind eine **explizite, dokumentierte und diskutierbare Wertentscheidung** (`framework_extensions_v2.0_SECJ.md`), kein verstecktes Axiom. Entscheidend: **J wirkt primär über das harte Veto (J<0,50 → SEC-J=null), nicht über sein Komposit-Gewicht** — geringes Gewicht ≠ Abwertung, sondern Arbeitsteilung zwischen Feinabstufung (Gewicht) und Sperrschwelle (Veto). Für gerechtigkeits-primäre Maßnahmen existiert der **JUSTICE-Modus** (J=0,40). Sensitivität: ±20 %-Parametervariation ändert den Gesamtwert um <±15 % (`co2_master.yaml → validation_approach.sensitivity`).

## 6. „Consistency binär (1/0) ist methodisch zu grob"

**Einwand:** Eine 0/1-Konsistenz-Achse verliert Nuancen.

**Antwort:** Eingeräumt — die binäre C-Form ist eine **konservative Screening-Vereinfachung**. Die vollständige Formel ist `C = 1 − (K+U)/I_ges` (Konflikte K, unerfüllte Abhängigkeiten U über alle Interaktionen I_ges), dokumentiert in Band 5 §2 und der PS-U-2.0-Spec. Die durchgängige Anwendung der kontinuierlichen C-Form pro Hebel ist ein **offener Verfeinerungspunkt**.

## 7. „Living document = bewegliches Ziel / Methoden-Drift"

**Einwand:** Wenn sich Werte und Methode laufend ändern, worauf bezieht man sich?

**Antwort:** Drift ist **kontrolliert und versioniert**, nicht chaotisch: `canon/STATUS.md` als Single Source of Truth, Changelogs in den YAMLs, DEPRECATED/SUPERSEDED-Marker, und das Lint-Tool **Probatio Consistentia** (`_tools/spec_consistency_audit.py`) für Cross-File-Konsistenz. Versionierung ist auditierbar — das ist eine Stärke, kein Mangel, und antifragil-konsistent (das System lernt sichtbar). Wer eine Inkonsistenz findet, findet sie *wegen* dieser Offenlegung.

## 8. „Hanf-Lastigkeit — Single-Material-Bias"

**Einwand:** Hanf taucht in auffällig vielen Hebeln auf; wirkt wie Lieblings-Material.

**Antwort:** Hanf ist **nicht wegen Material-Überlegenheit** gewählt, sondern wegen **Kaskaden-Effekten** (Bodenregeneration, Biodiversität, Multi-Use über die Wertschöpfungskette), die generische Naturfasern nicht in gleicher Dichte liefern. Flachs/Kenaf werden als **technische Belege** für die Machbarkeit zitiert, nicht als gleichrangige Alternativen verworfen. Wo Hanf nur 1:1-Materialersatz wäre (ohne Kaskade), wird das benannt.

## 9. „Antifragilität / Taleb-Bezug ist rhetorisch, nicht rigoros"

**Einwand:** „Antifragil" klingt gut, ist aber schwer operationalisierbar.

**Antwort:** Der Bezug ist **konkret operationalisiert**, nicht nur metaphorisch: das **J-Veto** ist der harte Mechanismus (J<0,50 → nicht zulässig), der Legitimitätsstress in eine Steuerungs-Schranke übersetzt. Der Anspruch ist eng gefasst — „Verteilungs-Backlash als Systeminformation" — mit empirischen Ankern (Gelbwesten, US-Kohleausstieg ohne Just Transition). Keine Behauptung universeller Antifragilität über das hinaus, was das Veto leistet.

## 10. „AI-Agent-Enhancement (+8,7 % SEC) ist spekulativ"

**Einwand:** Der KI-Verbesserungs-Layer ist nicht empirisch belegt.

**Antwort:** Als **Potenzial** markiert, nicht als Messung — mit konservativen Automatisierungs-Konfidenzfaktoren (α ∈ [0,70, 0,95]). Wo Werte projiziert statt gemessen sind, ist das gekennzeichnet. Empirische Fundierung ist ein offener Punkt, kein behaupteter Stand.

## 11. „Potenzial ≠ Umsetzung — fehlende reale Pilotdaten"

**Einwand:** Technische Realisierbarkeit ist kein Umsetzungsnachweis.

**Antwort:** Eingeräumt. Provolution wertet **technische/systemische Realisierbarkeit** (Pilote, Forschung, Motorsport-Belege, historische Vorläufer) — bewusst, weil Großserien-Status kein Hebel-Kriterium sein soll. Der Schritt zu harter Umsetzung braucht **externe Fallstudien, Partner und reale Pilotdaten**; das ist als nächster Hebel benannt, nicht als bereits erbracht ausgegeben. Praxispiloten (H01, A01) sind Anwendungsbeispiele, keine abgeschlossenen Wirkungsnachweise.

---

## Offene Punkte (wissenschaftliche Vertiefung — noch nicht geschlossen)

Die folgenden Lücken sind durch adversariale Review-Pässe (siehe `studies/AI_AUDIT_2026-05-28/`) bestätigt und **noch nicht geschlossen**. Ihr Schließen ist echte wissenschaftliche Arbeit (Analyse, Vergleichstabelle, prädiktive Tests), kein Dokument-Edit — hier offen benannt, bevor ein Reviewer sie findet.

12. **Gewichts-Sensitivitätsanalyse (ausstehend).** Eine systematische Variation der SEC-J-Gewichte über plausible Bereiche — plus Abgleich mit etablierten MCDA-Verfahren (AHP, SMART) — als Manuskript-Anhang fehlt noch. Bis dahin gilt §5: dokumentierte Wertentscheidung, J wirkt über das Veto. Bekannt ist nur die grobe Robustheit (±20 % Parametervariation → <±15 % Gesamtwert, `co2_master.yaml`), nicht die volle Gewichts-Sensitivität.

13. **Out-of-sample-Falsifizierung (ausstehend).** Innere Konsistenz (§9) ist nicht dasselbe wie ein prädiktiver Test. Ein echter Falsifizierungs-Test — sagt SEC-J reale Maßnahmen-Erfolge bzw. -Misserfolge vorher? scheitert ein hoch bewerteter Hebel im Feld? — ist noch nicht definiert. Das ist die härtere Stufe und bleibt offen.

14. **Einordnung in MCDA / IAM / RDM (ausstehend).** Eine tabellarische Abgrenzung gegenüber AHP/ELECTRE/PROMETHEE, Integrated Assessment Models (DICE/FUND/PAGE) und Robust Decision Making (Lempert et al.) fehlt noch. Ohne sie bleibt die Frage „was ist neu gegenüber 30 Jahren MCDA?" unbeantwortet — wird für die Reviewer-Antwort vorbereitet.

15. **Auswahlbegründung der Hebel (ausstehend).** Warum genau diese 49 (nicht 39 oder 59)? Welche wurden bewusst ausgeschlossen (z. B. Kernkraft, BECCS/DAC, großskaliges Geoengineering) und nach welchem Kriterium? Die Selektions-Logik ist noch nicht systematisch dokumentiert; bis dahin ist die Hebel-Menge diskretionär begründet, nicht deduktiv.

16. **Double-Counting-Audit & Inter-Domain-Korrektur (teilweise offen).** Per-Domain-Overlap *ist* bereinigt (z. B. B07 Kreislauf „schluckt" B08–B12: −32 → ~−16 Gt), und der realistische Netto-Median (−43,2 Gt, Monte-Carlo) ist dokumentiert. Offen bleiben: eine **Sankey-Visualisierung** der Carbon-Flows, eine **Hebel-zu-Hebel-Konflikt-Matrix** (materialisiert die ⊥-Relation auditierbar), die **Inter-Domain-Rückkopplung** (dekarbonisiert die C-Domäne den Strom, ändert sich die B-Domänen-Materialvorkette — bisher nicht modelliert) und die **abschließende YAML-Domain-Zuordnungs-Bereinigung** (in Band 4 §8.2 selbst als ausstehend vermerkt). Lesart bis dahin: **−43,2 Gt = realistischer Netto-Wert, −58,6 Gt = gescreentes Potenzial-Ceiling** (beide in STATUS.md §2 getrennt geführt) — bei der Kommunikation gleichrangig nennen, nicht das Ceiling allein.

---

## Wie mit neuen Kritiken umgehen

Neue, hier nicht gelistete Einwände sind **willkommen** — als Issue, Fork oder Korrespondenz. Berechtigte Punkte werden eingeräumt und verortet (Spurensuche: prüfen, was stimmt, ändern); methodisch-belegte Aussagen werden präzisiert, aber nicht für ein breites Publikum weichgespült, wenn das gute Strukturen zerstören würde. Maßstab ist *unbelegt vs. methodisch-belegt*, nicht *klingt-stark*.

*Companion-Dokumente: [`canon/STATUS.md`](STATUS.md) (Werte/Methode/Status), `_tools/spec_consistency_audit.py` (Drift-Kontrolle).*
