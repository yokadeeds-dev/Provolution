# Out-of-sample-Validierung SEC-J — retrospektive Konkordanz-Probe

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement / Proof-of-Concept (N=3, Skala 0,19–0,94) · **Companion zu:** [`canon/STATUS.md`](../../canon/STATUS.md), [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #13

Antwort auf den Reviewer-Einwand „Innere Konsistenz ≠ prädiktiver Test — wo ist die Out-of-sample-Falsifizierung?" ([`LIMITATIONS.md`](../../canon/LIMITATIONS.md) #13). Getestet wird der Kern-Claim: *Markieren SEC-J — insbesondere die Achsen C (Konsistenz) und J (Gerechtigkeit) sowie der J-Veto — reale Maßnahmen-Fehlschläge bzw. -Erfolge, die eine reine Sufficiency/Efficiency-Prüfung unterschätzt?*

> **Note for external readers (EN):** Retrospective out-of-sample concordance probe across the full SEC-J range (failure → durable → reference). SEC-J is applied to the *ex-ante* information set of real measures with documented outcomes. This is a **proof-of-concept (N=3), not a powered validation**, scored by the framework author with outcome knowledge — see §7 Limitations. It does **not** claim error-free prediction.

---

## 1. Design

**Out-of-sample-Logik:** Eine Maßnahme wird mit SEC-J auf dem **Informationsstand *vor* dem bekannten Ausgang** bewertet; anschließend wird die Diagnose mit dem **tatsächlichen, dokumentierten Ausgang** verglichen. Falsifiziert wäre der Claim, wenn SEC-J einen real gescheiterten Fall hoch bewertete bzw. einen real durablen/erfolgreichen Fall als Veto/Totalschaden.

**Drei Fälle, volle Skala:**
1. **Negativ-Pol (Diskriminant-Paar, Teil 1):** Deutsche PKW-Maut — gerechtigkeits-/konsistenz-**brüchig**, gescheitert.
2. **Kontrast (Diskriminant-Paar, Teil 2):** Österreichisches ASFINAG-Maut-System — **diskriminierungsfrei**, durabel. *Gleicher Maßnahmentyp* (Straßen-Bepreisung), gegensätzliches C/J-Design → isoliert C/J als Diskriminator und zeigt: das Framework straft nicht „Maut", sondern den asymmetrischen Systemfehler.
3. **Positiv-Pol (Referenz-Modell):** Währungsreform 1948 — verankert das obere Skalen-Ende.

**Scope (ehrlich):** Diese Fälle testen SEC-J als **framework-neutrales Instrument** (Governance/Ökonomie — PS-U ist explizit nicht climate-gebunden, vgl. `06_framework_extensions_v2.0_SECJ.md §1`). Sie validieren die **allgemeine C/J-Diskriminationslogik**, *nicht* die climate-spezifischen Hebel-Scores; deren Feldvalidierung bleibt der härtere, domänenspezifische Test (§8).

**Formel (STANDARD):** `SEC-J = 0,30·S + 0,25·E + 0,30·C + 0,15·J`; Veto bei J<0,50; Flags bei S/E/C/J<0,40.

---

## 2. Negativ-Pol (Flaggschiff): Deutsche PKW-Maut / Infrastrukturabgabe

**Gegenstand (m₁):** Infrastrukturabgabe bei gleichzeitiger, betragsgenauer Entlastung **inländischer** Halter über die Kfz-Steuer (de facto „Ausländermaut"). Treiber: CSU / BMVI (Andreas Scheuer). **Ex-ante-Basis:** Gesetzentwürfe, Gutachten Wiss. Dienst Bundestag, Anhörungen (Stand Jan. 2019).

**PS-U-Audit** (Quelle: PS-U-Audit Yoka):

| Dim. | Gew. | Score | Sollbruchstelle |
|---|---:|---:|---|
| **S** | 0,30 | **0,20** | Starre Kopplung EU-Nutzerfinanzierung ↔ nationales Kfz-Steuersystem; bricht EU-Recht weg, kollabiert alles. |
| **E** | 0,25 | **0,30** | Erfassungs-/Systemkosten zehren die Transit-Einnahmen nahezu auf (vs. BMVI-Erwartung ~500 Mio. €/Jahr). |
| **C** | 0,30 | **0,10** | Genickbruch: „reine Nutzerfinanzierung (jeder zahlt)" **und** „Inländer netto 0 €" → 100 % Last bei Ausländern. Unauflösbar. |
| **J** | 0,15 | **0,15** | Diskriminierung nach Staatsangehörigkeit (Art. 18 AEUV), Behinderung der Grundfreiheiten. |

`SEC-J = 0,060 + 0,075 + 0,030 + 0,0225 =` **0,1875** → **NICHT TRAGFÄHIG** + dreifache Flag (S/C/J<0,40) + **J-Veto** (J 0,15 < 0,50). Interner „Totalschaden" (< 0,20). Audit-Verfügung: absolutes Stopp-Signal, keine Betreiberverträge vor juristischer Klärung.

**Realer Ausgang:** EuGH erklärt die Abgabe am **18.6.2019** (Rs. C-591/17) für unionsrechtswidrig — **diskriminierend**. Verträge waren *vor* dem Urteil unterzeichnet → dreistelliger Mio.-Schadenersatz (Schiedsverfahren) für eine nie in Betrieb gegangene Maut + Untersuchungsausschuss. Der Generalanwalt sah 2018 noch keine Diskriminierung (isolierte Normbetrachtung); der Gerichtshof entschied in der **Gesamtbetrachtung** gegenteilig.

**Konkordanz:** SEC-J kippt auf **C (0,10)** + **J (0,15)** — exakt die Achsen, an denen der EuGH die Maßnahme kassierte. Die holistische C-Prüfung nimmt dieselbe Gesamtschau vorweg.

---

## 3. Diskriminant-Kontrast: Österreichisches ASFINAG-Maut-System

**Gegenstand (m₂):** Zeitbezogene Pkw-Vignette + streckenbezogene Lkw-Maut (> 3,5 t) der **ASFINAG**. **Ex-ante-Basis:** Systemumstellung 1997 (Vignette) bis 2004 (Lkw-GO-Maut, DSRC-Mikrowellentechnologie, errichtet durch **Kapsch/Europpass**).

> *Korrektur ggü. Vorentwurf:* Die Lkw-Maut-Technik ist **DSRC-Mikrowelle (Kapsch/ASFINAG)** — **nicht** „DARS" (DARS d.d. ist die *slowenische* Autobahngesellschaft).

**SEC-J-Bewertung** *(illustratives Rubrik-Scoring dieses Audits — transparent als Schätzung gekennzeichnet)*:

| Dim. | Score | Ex-ante-Analyse |
|---|---:|---|
| **S** | 0,80 | Saubere Entflechtung: ASFINAG nutzerfinanziert, außerhalb Kernhaushalt, keine toxischen Steuerrechts-Kopplungen. |
| **E** | 0,85 | Tragfähige Datenbasis; Maut-Einnahmen decken Systemkosten empirisch, fließen in Infrastruktur. |
| **C** | 0,90 | Widerspruchsfrei: „Wer die Straße nutzt, zahlt — egal aus welchem Land." Keine nationalen Kompensationsschleifen. |
| **J** | 0,80 | Tarif symmetrisch für In- und Ausländer; europarechtliche Grundfreiheiten gewahrt. |

`SEC-J = 0,240 + 0,2125 + 0,270 + 0,120 =` **0,8425** → **STABIL / BESTANDEN**, kein Veto. **Realer Ausgang:** diskriminierungsfrei, rechtlich unangefochten, durabel im Betrieb.

---

## 4. Positiv-Pol (Referenz-Modell): Währungsreform 1948 (Trizone)

**Gegenstand (m₃):** Radikale Geldmengen-Verknappung (Reichsmark → D-Mark, Kern ~10:1, Sparguthaben effektiv ~100:6,5), **gekoppelt** an die gleichzeitige Aufhebung fast aller Preisbindungen/Rationierungen (Erhard, 20./21.6.1948). **Ex-ante-Basis:** ordoliberale Theorie + Mangelwirtschafts-Lagebild Frühjahr 1948.

**PS-U-Audit** (Quelle: PS-U-Audit Yoka):

| Dim. | Gew. | Score | Analyse |
|---|---:|---:|---|
| **S** | 0,30 | **0,95** | Erhard koppelt „Geld" starr an „freier Markt": knappes Geld trifft frei kalkulierte Preise → selbststabilisierender Regelkreis binnen 24 h. |
| **E** | 0,25 | **0,95** | Empirisches „Wunder": leere Schaufenster füllen sich schlagartig; Industrieproduktion Trizone H2/1948 ≈ +50 %. |
| **C** | 0,30 | **0,95** | Stringent + symmetrisch: keine Gruppen-Ausnahmen, kein Schönreden; für alle Marktteilnehmer berechenbar. |
| **J** | 0,15 | **0,85** | Materielle Basis für Freiheit/Würde (Soziale Marktwirtschaft). **Abzug:** Kleinsparer verlieren fast alles, Sachwertbesitzer bleiben verschont — reale distributive Härte. |

`SEC-J = 0,285 + 0,2375 + 0,285 + 0,1275 =` **0,935** → **EXZELLENT / REFERENZ-MODELL** (> 0,90). **Realer Ausgang:** Grundstein des „Wirtschaftswunders". Kein 1,00, weil die Spar-/Sachwert-Asymmetrie einen echten Gerechtigkeitspreis trägt — das Audit registriert ihn (J=0,85).

---

## 5. Ergebnis — volle Skala

| Fall | C | J | SEC-J | Verdict | Realer Ausgang | Konkordanz |
|---|---:|---:|---:|---|---|:---:|
| PKW-Maut (diskriminierend) | 0,10 | 0,15 | **0,19** | NICHT TRAGFÄHIG + J-Veto | vom EuGH gekippt, Schadenersatz | ✅ |
| ASFINAG (diskriminierungsfrei) | 0,90 | 0,80 | **0,84** | BESTANDEN | durabel, rechtl. unangefochten | ✅ |
| Währungsreform 1948 | 0,95 | 0,85 | **0,94** | REFERENZ-MODELL | „Wirtschaftswunder"-Grundstein | ✅ |

**Befund:** (a) **Diskriminanz** — bei identischem Maßnahmentyp trennt SEC-J PKW-Maut (0,19) und ASFINAG (0,84) scharf; der Diskriminator ist **C/J, nicht S/E** → das Framework straft nicht „Maut", sondern asymmetrisches Design. (b) **Skalen-Validität** — die Probe spannt Fehlschlag → durabel → Referenz (0,19/0,84/0,94), jeweils konkordant zum dokumentierten Ausgang.

---

## 6. Inter-Fall-Konsistenz der J-Achse (warum 0,15 vs 0,85 kein Widerspruch ist)

Ein scharfer Gutachter fragt: *Wie kann J die PKW-Maut mit **0,15** (Veto) bewerten, die Währungsreform aber mit **0,85** — obwohl letztere Kleinsparer real fast enteignete?* Das ist eine **prinzipielle Unterscheidung**, kein Ad-hoc-Urteil:

- **PKW-Maut (J=0,15):** ein **per Design eingebauter Gruppen-Ausschluss** entlang eines geschützten Merkmals (Staatsangehörigkeit) — die Regel *selbst* diskriminiert (Art. 18 AEUV). **Prozeduraler/rechtlicher Gleichheitsbruch** → kategorial Veto-Bereich.
- **Währungsreform (J=0,85):** eine **symmetrische Regel** (gleicher Umstellungsschlüssel für alle), deren *Inzidenz* wegen der **vorbestehenden** Vermögensverteilung regressiv ausfiel (das Pro-Kopf-„Kopfgeld" wirkte sogar progressiv). Die Härte ist eine distributive **Folge**, kein designter Ausnahme-Tatbestand — und wird **abgewertet** (0,85 statt 1,0).

Die J-Achse trennt also sauber: **diskriminierend-by-design / Rechtsbruch** (→ Veto) vs. **gleiche Regel mit regressiver Inzidenz** (→ Punktabzug, kein Veto). Diese Unterscheidung ist über beide Fälle **konsistent** angewandt und macht die J-Achse prüfbar statt beliebig.

---

## 7. Grenzen (kritisch, offen)

**Kein Beweis fehlerfreier Vorhersage.** Vier ernste Einschränkungen:

1. **Hindsight / Confirmation-Risiko:** Bewertung durch den Framework-Autor **mit** Outcome-Wissen. Gold-Standard wäre **verblindete, unabhängige** Bewertung ohne Ausgangs-Kenntnis.
2. **Anachronismus der Formel:** SEC-J (0,30/0,25/0,30/0,15) ist erst **2026-05-10** kanonisiert → **retrospektive Anwendung** auf den Ex-ante-Stand, **keine** real abgegebene Prognose.
3. **Kleines N + Single-Rater:** N=3, je N=1 Rater pro Fall; ein Kontrast-Score (ASFINAG) ist eine eigene illustrative Schätzung. Statistisch nicht powered.
4. **Framework-neutrale Fälle ≠ Climate-Lever-Validierung:** geprüft ist die allgemeine C/J-Logik (Governance/Ökonomie), *nicht* ob die climate-spezifischen Hebel im Feld erfolgreich sind — der domänenspezifische Out-of-sample-Test bleibt offen.

---

## 8. Was das zeigt — und was als Nächstes nötig ist

**Zeigt:** SEC-J trennt in dokumentierten Realfällen scharf und über die volle Skala; C/J markieren genau die Bruch- bzw. Tragfähigkeits-Stellen, die eine Effizienz-only-Prüfung unterschätzt — eine **nachvollziehbare Konkordanz** und ein belastbarer erster Out-of-sample-Ankerpunkt.

**Zeigt nicht:** prädiktive Treffsicherheit über viele Fälle; climate-Lever-Feldvalidierung.

**Roadmap:** N erhöhen (Gilets-Jaunes-CO₂-Steuer, BC/Schweden-CO₂-Steuer, Australien-Rücknahme 2014, dt. Kohleausstieg ± Just Transition) · **verblindete Rater** + **Präregistrierung** künftiger Maßnahmen · formale **Quellen-Zitate** für die empirischen Ausgangs-Aussagen (EuGH C-591/17 18.6.2019; Schadenersatz/Schiedsspruch; Währungsreform-Produktionsdaten H2/1948; ASFINAG-Strukturparameter) — in diesem Entwurf als gut dokumentierter Allgemeinstand geführt, Zitate ausstehend.

---

*Companion: [`canon/STATUS.md`](../../canon/STATUS.md) · [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #13 · [`canon/de/06_framework_extensions_v2.0_SECJ.md`](../../canon/de/06_framework_extensions_v2.0_SECJ.md) · [`manuscript/RESPONSE_TO_REVIEWERS_PREP.md`](../../manuscript/RESPONSE_TO_REVIEWERS_PREP.md) Q5.*
