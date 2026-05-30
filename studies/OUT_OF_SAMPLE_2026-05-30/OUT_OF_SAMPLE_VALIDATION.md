# Out-of-sample-Validierung SEC-J — retrospektive Konkordanz-Probe

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement / Proof-of-Concept (N=2) · **Companion zu:** [`canon/STATUS.md`](../../canon/STATUS.md), [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #13

Antwort auf den Reviewer-Einwand „Innere Konsistenz ≠ prädiktiver Test — wo ist die Out-of-sample-Falsifizierung?" ([`LIMITATIONS.md`](../../canon/LIMITATIONS.md) #13). Getestet wird der Kern-Claim: *Markieren SEC-J — insbesondere die Achsen C (Konsistenz) und J (Gerechtigkeit) sowie der J-Veto — reale Maßnahmen-Fehlschläge, die eine reine Sufficiency/Efficiency-Prüfung unterschätzt?*

> **Note for external readers (EN):** Retrospective out-of-sample concordance probe. SEC-J is applied to the *ex-ante* information set of real measures with documented outcomes. This is a **proof-of-concept (N=2 contrast pair), not a powered validation**, and is scored by the framework author with outcome knowledge — see §5 Limitations. It does **not** claim error-free prediction.

---

## 1. Design

**Out-of-sample-Logik:** Eine Maßnahme wird mit SEC-J auf dem **Informationsstand *vor* dem bekannten Ausgang** bewertet; anschließend wird die SEC-J-Diagnose mit dem **tatsächlichen, dokumentierten Ausgang** verglichen. Falsifiziert wäre der Claim, wenn SEC-J einen real gescheiterten Fall hoch (TRAGFÄHIG) bzw. einen real durablen Fall als Veto/Totalschaden bewertet.

**Kontrast-Paar statt Einzelfall:** Um Bestätigungs-Auswahl zu vermeiden, wird **derselbe Maßnahmentyp** (Straßen-/Infrastruktur-Bepreisung) in zwei Ausprägungen geprüft — einmal mit gerechtigkeits-/konsistenz-**brüchigem** Design (gescheitert), einmal **diskriminierungsfrei** (durabel). Wenn SEC-J die beiden trennt, ist gezeigt, dass nicht „Maut = schlecht", sondern das **C/J-Design** der Diskriminator ist.

**Formel (STANDARD):** `SEC-J = 0,30·S + 0,25·E + 0,30·C + 0,15·J`; Veto bei J<0,50; Flags bei S/E/C/J<0,40.

---

## 2. Flaggschiff-Fall (Negativ-Kontrolle): Deutsche PKW-Maut / Infrastrukturabgabe

**Gegenstand (m):** Gesetzliche Einführung einer Infrastrukturabgabe bei gleichzeitiger, betragsgenauer Entlastung **inländischer** Fahrzeughalter über die Kfz-Steuer (de facto „Ausländermaut"). Treiber: CSU / BMVI (Andreas Scheuer).

**PS-U-Audit-Protokoll** (Quelle: PS-U-Audit Yoka; bewertet auf dem Ex-ante-Informationsstand Anfang 2019, *vor* dem EuGH-Urteil):

| Dimension | Gewicht | Score | Systemische Sollbruchstelle |
|---|---:|---:|---|
| **S** Systemica | 0,30 | **0,20** | Starre Interdependenz: Nutzerfinanzierung (EU-Subsystem) starr an nationales Kfz-Steuersystem gekoppelt; bricht das EU-Recht weg, kollabiert das Gesamtkonstrukt — keine Resilienz. |
| **E** Empirica | 0,25 | **0,30** | Datendivergenz: BMVI rechnete mit ~500 Mio. €/Jahr netto; unabhängige Gutachten zeigten vorab, dass System-/Erfassungskosten die Transit-Einnahmen nahezu aufzehren. |
| **C** Consistentia | 0,30 | **0,10** | Logischer Genickbruch: zwei sich ausschließende Maximen — „reine Nutzerfinanzierung (jeder zahlt)" **und** „Inländer zahlen netto 0 €" → 100 % der Last bei Ausländern. Unauflösbarer Widerspruch. |
| **J** Justitia | 0,15 | **0,15** | Normativer Verstoß: Diskriminierung nach Staatsangehörigkeit (Art. 18 AEUV), Behinderung des freien Waren-/Dienstleistungsverkehrs. |

**Berechnung:** `(0,30·0,20) + (0,25·0,30) + (0,30·0,10) + (0,15·0,15) = 0,060 + 0,075 + 0,030 + 0,0225 =` **0,1875**

**SEC-J-Verdict:** **NICHT TRAGFÄHIG** (Score 0,19 < 0,40) — zusätzlich **dreifache Flag** (S, C, J je < 0,40: UNZUREICHEND · STRUKTURELLER WIDERSPRUCH · SOZIALE INKONSISTENZ) und **J-Veto** (J 0,15 < 0,50 → operativ SEC-J = null). In der internen Lesart der niedrigste je vergebene Score („Totalschaden", < 0,20). Audit-Verfügung: **absolutes Stopp-Signal** — insbesondere keine langfristigen privatrechtlichen Betreiberverträge vor juristischer Klärung.

**Realer Ausgang:** Der EuGH erklärte die Abgabe am **18. Juni 2019** (Rs. C-591/17, Österreich ./. Deutschland) für **unionsrechtswidrig — diskriminierend** nach Staatsangehörigkeit. Die Verträge waren **vor** dem Urteil unterzeichnet → die nie in Betrieb gegangene Maut endete in einem **dreistelligen Millionen-Schadenersatz** (Schiedsverfahren) und einem Bundestags-Untersuchungsausschuss. Der Generalanwalt hatte 2018 noch **keine** Diskriminierung gesehen (isolierte Normbetrachtung); der Gerichtshof entschied in der **Gesamtbetrachtung** gegenteilig.

**Konkordanz:** SEC-J markiert den Kollaps auf **C** (0,10) und **J** (0,15) — exakt die Achsen, an denen der EuGH die Maßnahme kippte. Die holistische Konsistenz-Prüfung (C) nimmt dieselbe Gesamtschau vorweg, die der Gerichtshof dem isolierten Blick des Generalanwalts entgegensetzte. **Eine reine S/E-Prüfung (Machbarkeit + Einnahmen) hätte den Bruch unterschätzt.**

---

## 3. Kontrast-Fall (Diskriminant): diskriminierungsfreie Straßen-Bepreisung

**Gegenstand:** Pauschale, nutzerunabhängige Autobahn-Vignette (Muster Schweiz/Österreich): gilt **gleich für alle Nutzer** (In- und Ausländer), keine nationale Entlastungs-Kopplung.

**SEC-J-Bewertung** *(illustrativ, Rubrik-Scoring dieses Audits — nicht user-geliefert; transparent als Schätzung gekennzeichnet)*:

| Dimension | Score | Begründung |
|---|---:|---|
| S | 0,70 | Infrastruktur-Finanzierung + milder Nachfrage-/Lenkungseffekt |
| E | 0,85 | sehr niedrige Erfassungskosten (Pauschale), hohe Netto-Quote |
| C | 0,85 | EU-rechtskonform, diskriminierungsfrei, kohärent mit Infrastruktur-Finanzierung |
| J | 0,70 | gleiche Last für alle Nutzer; **keine** Staatsangehörigkeits-Diskriminierung (mild regressiv durch Pauschale) |

**Berechnung:** `(0,30·0,70)+(0,25·0,85)+(0,30·0,85)+(0,15·0,70) = 0,210+0,2125+0,255+0,105 =` **0,7825 ≈ 0,78**

**SEC-J-Verdict:** **BEDINGT TRAGFÄHIG** (0,60–0,79), **kein** Veto (J ≥ 0,50), keine Flag. **Realer Ausgang:** diskriminierungsfreie Vignetten-/Maut-Modelle (CH/AT-Vignette, dt. LKW-Maut) sind **rechtlich unangefochten und durabel** im Betrieb.

---

## 4. Ergebnis

| Fall | C | J | SEC-J | Verdict | Realer Ausgang | Konkordanz |
|---|---:|---:|---:|---|---|:---:|
| PKW-Maut (diskriminierend) | 0,10 | 0,15 | **0,19** | NICHT TRAGFÄHIG + J-Veto | vom EuGH gekippt, Schadenersatz | ✅ |
| Vignette (diskriminierungsfrei) | 0,85 | 0,70 | **0,78** | BEDINGT TRAGFÄHIG | durabel, rechtl. unangefochten | ✅ |

**Befund:** Bei identischem Maßnahmentyp trennt SEC-J die beiden Ausprägungen scharf — und der Diskriminator sind **C und J**, nicht S/E. Das ist konsistent mit dem Kern-Claim (distributiver/legaler Bruch als Systeminformation) und mit dem realen Ausgang in beiden Fällen.

---

## 5. Grenzen (kritisch, offen)

Diese Probe ist **kein Beweis fehlerfreier Vorhersage**. Sie hat vier ernste Einschränkungen, die ein belastbares Verständnis erfordern:

1. **Hindsight / Confirmation-Risiko:** Die Bewertung erfolgt durch den Framework-Autor **mit Kenntnis des Ausgangs**. Auch bei Disziplin auf den Ex-ante-Informationsstand ist unbewusste Rückprojektion nicht ausgeschlossen. Gold-Standard wäre eine **verblindete, unabhängige** Bewertung ohne Outcome-Wissen.
2. **Anachronismus der Formel:** Die SEC-J-Formel (0,30/0,25/0,30/0,15) ist erst **2026-05-10** kanonisiert. Der Fall ist daher eine **retrospektive Anwendung** auf den Ex-ante-Stand — **keine** real abgegebene Prognose von 2019.
3. **Kleines N (Proof-of-Concept):** N=2 (ein Kontrast-Paar). Das illustriert die diskriminierende Logik, ist aber **statistisch nicht powered**. Ein Kontrast-Score (Vignette) ist zudem eine *eigene* illustrative Schätzung, kein unabhängig validierter Wert.
4. **Single-Rater:** keine Inter-Rater-Prüfung dieser konkreten Fälle (anders als die Reliabilitäts-Studie N=10, die SEC-Scoring generell prüft).

---

## 6. Was das zeigt — und was als Nächstes nötig ist

**Zeigt:** Die SEC-J-Achsen C und J markieren in einem gerichtlich dokumentierten Realfall genau die Bruchstelle, die eine Effizienz-only-Prüfung unterschätzt hätte — eine **scharfe, nachvollziehbare Konkordanz** und ein erster Out-of-sample-Ankerpunkt.

**Zeigt nicht:** prädiktive Treffsicherheit über viele Fälle; das bleibt offen.

**Roadmap zur Härtung** (echte wissenschaftliche Vertiefung):
- **N erhöhen:** weitere dokumentierte Fälle, balanciert (Erfolge + Fehlschläge), u. a. Gilets-Jaunes-CO₂-Steuer (J-Backlash), BC/Schweden-CO₂-Steuer (durabel), Australien-CO₂-Steuer-Rücknahme 2014, dt. Kohleausstieg mit Strukturhilfe (gerechte Transition) vs. Kohleregion-Kollaps ohne sie.
- **Verblindung + Präregistrierung:** unabhängige Rater scoren ohne Outcome-Wissen; künftige Maßnahmen *vor* dem Ausgang pre-registrieren (stärkste Falsifizierungs-Stufe).
- **Belege/Quellen:** die empirischen Ausgangs-Aussagen (EuGH C-591/17 vom 18.6.2019; Schadenersatz-Höhe/Schiedsspruch; AG-Stellungnahme 2018; Vignetten-Durabilität) sind vor externer Verwendung **formal zu zitieren** (in diesem Entwurf als gut dokumentierter Allgemeinstand geführt, Quellen-Ergänzung ausstehend).

---

*Companion: [`canon/STATUS.md`](../../canon/STATUS.md) · [`canon/LIMITATIONS.md`](../../canon/LIMITATIONS.md) #13 · [`canon/de/06_framework_extensions_v2.0_SECJ.md`](../../canon/de/06_framework_extensions_v2.0_SECJ.md) (Veto-/Flag-Logik) · [`manuscript/RESPONSE_TO_REVIEWERS_PREP.md`](../../manuscript/RESPONSE_TO_REVIEWERS_PREP.md) Q5.*
