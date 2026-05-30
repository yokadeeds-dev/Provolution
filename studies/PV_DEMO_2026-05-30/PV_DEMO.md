# PV-Demonstration — Claim-Detektion & Modul-Routing

**Stand:** 2026-05-30 · **Charakter:** Reviewer-Supplement / Methodik-Demo · **Companion zu:** [`canon/de/00_PS_Familie_Uebersicht.md`](../../canon/de/00_PS_Familie_Uebersicht.md) (Routing-SSoT), [`canon/de/07_Probatio_Veritatis_v2.0.md`](../../canon/de/07_Probatio_Veritatis_v2.0.md)

Zeigt zwei Dinge: (a) das **Routing-Prinzip** der PS-Familie — *der Prüfobjekt-Typ bestimmt das Modul* — und (b) **Probatio Veritatis (PV)** als Claim-Detektor an zwei realen Aussagen. Ergänzt die Out-of-sample-*Maßnahmen*-Studie um die *Behauptungs*-Ebene.

> **Note for external readers (EN):** Demonstrates module routing (object-type → module) and the Probatio Veritatis claim-checker. Scores for the Weidel case are this audit's proposal (author-confirmable); the Blüm case reproduces a prior PV run. Methodology demo, not a political statement — see §4.

---

## 1. Routing-Prinzip (warum nicht alles SEC-J ist)

Die PS-Familie routet **nach Prüfobjekt** (Kanon `00_PS_Familie_Uebersicht.md` §1 + §8 Abgrenzungsregel):

| Objekt-Typ | Modul | Kernfrage |
|---|---|---|
| Maßnahme / System | **PS-U** | systemisch tragfähig? |
| **faktische Behauptung** | **PV** | empirisch haltbar? |
| Mediendiskurs / Framing | **PN** | wer spricht, wer fehlt? |

> Kanon §8: *„PS-U bewertet ob eine Maßnahme systemisch tragfähig ist. **PV bewertet ob Behauptungen darüber faktisch haltbar sind.**"*

**Häufiger Mismatch:** Es ist verführerisch, das Flaggschiff **SEC-J (PS-U) auf alles** anzuwenden. Aber eine *Behauptung* gehört in **PV**, nicht in PS-U. Der Blüm-Fall (§2) zeigt das exemplarisch: dieselbe Aussage durch PS-U gejagt liefert „instabil 0,33", durch PV (korrekt) ein hartes **FALSE via Logik-Veto**. Beide landen rot — aber nur PV beantwortet die gestellte Frage („ist die Aussage *wahr*?").

**Wichtig — Achsen sind modul-spezifisch:** Gleiche Buchstaben messen je Modul Verschiedenes. In PS-U ist `S` = Systemica (System-Resilienz); in PV ist `S` = **Evidenzgüte** (wie gut belegt ist das Urteil). Roh-Scores sind daher **nicht** modulübergreifend vergleichbar — nur Verdikte.

**PV-Formel** (Kanon §2): `PV(c) = 0,30·S + 0,20·E + 0,20·C_ext + 0,15·C_int + 0,15·J`
**PV-Vetos** (§4): `C_ext<0,50 → FALSE` · `C_int=0 → FALSE (Logik-Unmöglichkeit)` · `J<0,40 → Flag HARMFUL FRAMING`.

---

## 2. Fall A — „Die Rente ist sicher" (Norbert Blüm, 1986)

**Claim (c):** unbedingte langfristige Stabilität des Umlageverfahrens ohne radikale Reform (Niveau *und* Beitragssatz stabil). **Ex-ante-Stand:** Pillenknick (ab 1965) + steigende Lebenserwartung waren 1986 bekannt.

| Achse | Score | Begründung |
|---|---:|---|
| S (Evidenzgüte) | 0,90 | offizielle Langfrist-Projektionen (BMF-Tragfähigkeit, StatBA-Kohorten) |
| E | 0,50 | Kausalitäts-/Bezugsraumfehler: Finanzsystem von seinen demografischen Variablen isoliert |
| C_ext | **0,20** | 4/5 Quellen widersprechen → **empirisches Veto** (C_ext<0,50) |
| C_int | **0,00** | Logikbruch: stabiles Niveau **und** stabiler Beitrag bei kippendem Altenquotienten ist arithmetisch unmöglich → **Logik-Veto** |
| J | 0,45 | systematische Auslassung der Lastenverschiebung auf jüngere Kohorten |

`PV = 0,27+0,10+0,04+0,00+0,0675 =` **0,4775** → **FALSE** (Verdict-Band 0,20–0,49) + **harter Logik-Veto** (C_int=0). **Realität 2026:** >110 Mrd. €/Jahr Steuerzuschuss + sinkendes Niveau = exakt der vorhergesagte Bruch.

*(PV-Audit reproduziert; kanon-treu — Formel + Veto decken sich mit `00_PS_Familie` §2/§4. Eine ältere PS-U-Lesart desselben Falls ergab SEC-J 0,33 „instabil" — richtige Richtung, aber falsches Modul für eine Behauptung; siehe §1.)*

---

## 3. Fall B — „Hitler war ein Linker / Kommunist" (A. Weidel ggü. E. Musk, 2025)

**Claim (c):** der historische Nationalsozialismus sei „links"/kommunistisch gewesen. **PV-Audit** *(Score-Vorschlag dieses Audits, zu bestätigen)*:

| Achse | Score | Begründung (Faktenlage — Zitate ausstehend) |
|---|---:|---|
| S (Evidenzgüte) | 0,95 | erdrückende, gut dokumentierte Quellenlage |
| E | 0,10 | isoliert das Wort „sozialistisch" im Parteinamen vom empirischen Befund |
| C_ext | **0,05** | widerspricht der Forschung: NS ließ Großindustrie-Eigentum (Krupp/IG Farben/Thyssen) intakt, zerschlug freie Gewerkschaften, KPD/SPD = erste KZ-Häftlinge (Dachau 1933), Feindbild „jüdischer Bolschewismus" → **empirisches Veto** |
| C_int | **0,00** | innerer Widerspruch: „Hitler = Kommunist", während Hitler den linken Straßer-Flügel 1934 liquidieren ließ → **Logik-Veto** |
| J | 0,20 | **HARMFUL FRAMING** (J<0,40): Geschichtsrevision, die den Faschismus-Vorwurf auf die Linke umlenkt |

`PV = 0,285+0,02+0,01+0,00+0,03 =` **0,345** → **FALSE** + Doppel-Veto (C_ext<0,50 **und** C_int=0) + Flag **HARMFUL FRAMING**.

**PN-Sekundärlinse (Diskursstrategie, qualitativ):** *warum* die falsche Aussage eingesetzt wird — formalistische Ausschlachtung des Namens „Nationalsozialismus", Umlenkung des Faschismus-Vorwurfs (Hufeisen-Manöver), Andocken an das vereinfachte US-Raster „links = viel Staat". PV stellt fest *dass* die Aussage falsch ist; PN erklärt die *Strategie* dahinter. (Routing: ein Claim mit Diskurs-Wirkung → PV-primär + PN-sekundär, nie PS-U.)

---

## 4. Neutralität (sichtbar gemacht)

Diese Demo ist **Methodik, keine politische Aussage.** Das Framework FALSE-flaggt **strukturell, seitenunabhängig** — belegt durch die Spannweite des Gesamt-Korpus:

| politische Verortung | Fall | Modul | Befund |
|---|---|---|---|
| weit links | Großer Sprung / Mao | PS-U | 0,085 Katastrophe |
| Mitte-rechts | PKW-Maut (CSU), Spahn (CDU), **Blüm (CDU)** | PS-U / PV | Veto / instabil / FALSE |
| weit rechts | **Weidel (AfD)** | PV/PN | FALSE + HARMFUL FRAMING |

Den AfD-Fall *auszusparen* wäre die eigentliche Selektivität; ihn mit **derselben** Logik zu prüfen wie Mao oder Blüm ist Neutralität *by construction* (sauberer Prozess → neutrales Ergebnis).

**Offen (zur Abrundung):** ein **links-codierter** falscher Fakten-Claim gleicher Struktur würde die Symmetrie *auf der Seite selbst* sichtbar machen. Kandidaten-Typen (vom User zu wählen/füllen): wirtschafts-/wissenschaftsbezogene Falschbehauptungen mit klarer Faktenlage. Bis dahin trägt die Spektrum-Tabelle die Neutralität.

---

## 5. Grenzen

- **Score-Vorschlag** (Weidel) ist Autor-bestätigungspflichtig; Blüm reproduziert einen früheren PV-Lauf.
- **Retrospektiv, Single-Rater**; empirische Aussagen (NS-Historie, Renten-Zuschuss-Höhe, Weidel/Musk-Gespräch) als gut dokumentierter Allgemeinstand geführt — **formale Zitate ausstehend**.
- PV ist **Detektion** (ist der Claim wahr?), nicht Prognose (vgl. die PS-U-Out-of-sample-Studie für Maßnahmen-Vorhersage).

---

*Companion: [`canon/de/00_PS_Familie_Uebersicht.md`](../../canon/de/00_PS_Familie_Uebersicht.md) · [`canon/de/07_Probatio_Veritatis_v2.0.md`](../../canon/de/07_Probatio_Veritatis_v2.0.md) · [`canon/de/13_Probatio_Narrativa_v1.0.md`](../../canon/de/13_Probatio_Narrativa_v1.0.md) · [`studies/OUT_OF_SAMPLE_2026-05-30/`](../OUT_OF_SAMPLE_2026-05-30/OUT_OF_SAMPLE_VALIDATION.md) (Maßnahmen-Ebene).*
