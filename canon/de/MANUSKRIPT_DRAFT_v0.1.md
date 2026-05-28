# Probatio Systemica & Provolution: Ein systematisches, quantifiziertes Framework zur Klimatransformation

**Entwurf v0.1 — 2026-04-18**

---

**Autor:**
Yoka Tobias Dietz¹
ORCID: 0009-0006-2349-9002
Kontakt: yokadeeds-dev@provolution.org

¹ Independent Researcher, Hamm (Westfalen), Deutschland

**Interessenkonflikte:** Keine.
**Finanzierung:** Eigenfinanziert / unabhängige Forschung.
**Datenverfügbarkeit:** Alle Daten, Formeln und Anwendungs-Templates verfügbar unter https://github.com/yokadeeds-dev/Provolution (CC0 1.0).

---

## Zusammenfassung

Aktuelle Klimaschutzstrategien leiden unter Fragmentierung, Inkonsistenz und dem Fehlen systematischer, domänenübergreifender Verifikation. Wir präsentieren **Probatio Systemica**, ein mathematisch fundiertes Framework zur systemischen Verifikation von Klimamaßnahmen, und seine normative Anwendung **Provolution**, bestehend aus n = 40 quantifizierten Klimatransformations-Anwendungen in zehn Domänen. Das Framework basiert auf dem **SEC-Prinzip** — jede Maßnahme muss Sufficient (W(M) ≥ W_min), Efficient (min R(M) unter der Nebenbedingung W(M) ≥ W_min) und Consistent (¬∃ M_i ⊥ M_j) sein — formalisiert durch einen gewichteten Komposit-Score SEC(M) = 0,5·S(M) + 0,3·E(M) + 0,2·C(M). Angewandt auf 40 Klimamaßnahmen aus den Bereichen Governance, Kreislaufwirtschaft, Energie, Ernährung, Bildung, Technologie, Monitoring, Meta-Framework, Mobilität und Konstruktion ergibt das Framework einen durchschnittlichen SEC-Score von 0,914 (Bereich 0,88–1,00) und ein aggregiertes CO₂-Minderungspotenzial von −58,0 Gt/Jahr, das die globalen Emissionen von 55 Gt/Jahr übersteigt (105 %) — mit Netto-Negativ-Potenzial durch aktive Kohlenstoffsequestrierung. Eine integrierte agentische Schicht quantifiziert das KI-Verbesserungspotenzial mit durchschnittlich +8,7 % SEC-Steigerung über alle Anwendungen, unter Verwendung konservativer Automatisierungs-Konfidenzfaktoren (α ∈ [0,70, 0,95]). Das Framework ist explizit falsifizierbar, vollständig dokumentiert und als Open-Source verfügbar. Es bietet die erste einheitliche, domänenübergreifende, mathematisch konsistente Methodik zur Priorisierung, Validierung und Skalierung von Klimamaßnahmen unter Ressourcenrestriktionen.

**Schlüsselwörter:** Klimatransformation, SEC-Prinzip, Systemframework, Klimapolitik, Entscheidungsunterstützung, Kreislaufwirtschaft, Erneuerbare Energien, agentische KI, quantifizierter Klimaschutz

---

## 1. Einleitung

### 1.1 Das Problem: Fragmentierter Klimaschutz

Die globale Klimaherausforderung ist durch Dringlichkeit, Komplexität und Koordinationsversagen gekennzeichnet. Im Jahr 2025 belaufen sich die globalen CO₂-Äquivalent-Emissionen auf ca. 55 Gt/Jahr [1], während die aktuellen nationalen Klimaschutzbeiträge (NDCs) im Rahmen des Pariser Abkommens [5] für das Jahr 2100 eine Erwärmung von etwa 2,5–2,9 °C prognostizieren — weit über dem 1,5-°C-Schwellenwert, ab dem wesentliche Kipppunkte des Erdsystems aktiviert werden [3,4].

Das dominierende Merkmal des aktuellen Klimaschutzes ist Fragmentierung. Tausende von Einzelmaßnahmen, Technologien und Initiativen laufen parallel, ohne gemeinsamen Verifikationsstandard, ohne systematische domänenübergreifende Koordination und ohne ein einheitliches Framework zur Bewertung von Zielkonflikten unter Ressourcenrestriktionen. Das Ergebnis ist Allokationsineffizienz: Ressourcen fließen zu politisch sichtbaren oder kommerziell attraktiven Maßnahmen, statt zu jenen mit dem höchsten nachweisbaren Wirkungsgrad pro Ressourceneinheit.

Drei strukturelle Probleme liegen dieser Fragmentierung zugrunde:

**1. Fehlen eines universellen Verifikationsstandards.** Klimamaßnahmen werden mit heterogenen Methoden bewertet — Lebenszyklusanalyse (LCA), Kosten-Nutzen-Analyse (KNA), Multikriterienanalyse (MCA) oder narrative Politikevaluation — die nicht miteinander vergleichbar sind. Eine Maßnahme, die nach einer Methodik als „wirksam" gilt, kann nach einer anderen scheitern.

**2. Domänenübergreifende Inkonsistenz.** Maßnahmen, die einzeln valide sind, können bei gleichzeitiger Implementierung systemische Widersprüche erzeugen. Aufforstungsprogramme können mit der Bioenergie-Landnutzung kollidieren; CO₂-Bepreisung kann Just-Transition-Ziele untergraben; Smart-Grid-Investitionen können fossile Backup-Infrastruktur verfrüht entwerten. Kein bestehendes Framework prüft solche Widersprüche systematisch über Domänen hinweg.

**3. Fehlende Falsifizierbarkeit.** Die meisten Klima-Frameworks — einschließlich prominenter Szenariopfade wie IEA Net Zero 2050 [2] und IPCC-Minderungsszenarien [1] — sind nicht als falsifizierbare wissenschaftliche Theorien im Popperschen Sinne konzipiert [6]. Sie liefern Projektionen, keine verifizierbaren Vorhersagen, und spezifizieren nicht die Bedingungen, unter denen das Framework selbst revidiert oder aufgegeben werden müsste.

### 1.2 Bestehende Ansätze und ihre Grenzen

Zur Bewertung von Klimamaßnahmen im großen Maßstab existieren mehrere Frameworks. Der Sechste Sachstandsbericht des IPCC (AR6) [1] liefert maßgebliche Szenarioanalysen zu Minderungspfaden, schreibt jedoch keine spezifischen Maßnahmen vor und erstellt kein Ranking; seine Ergebnisse sind probabilistische Projektionen, keine handlungsorientierten Entscheidungswerkzeuge. Die IEA-Roadmap „Net Zero by 2050" [2] identifiziert 400 Meilensteine, bietet jedoch keine einheitliche Scoring-Methodik und keine domänenübergreifende Konsistenzprüfung. Project Drawdown [7] quantifiziert den CO₂-Impact einzelner Lösungen, behandelt diese jedoch als unabhängig und additiv, ohne Wechselwirkungseffekte zu berücksichtigen.

Auf Organisationsebene liefern Ansätze wie Science-Based Targets (SBTi) [11] und das GHG Protocol [9] Messstandards für bestimmte Emissionsscopes, adressieren aber nicht die Herausforderung der Priorisierung von Maßnahmen über Domänen hinweg unter gemeinsamen Ressourcenrestriktionen.

### 1.3 Beitrag dieser Arbeit

Diese Arbeit präsentiert zwei ineinandergreifende Beiträge:

**Probatio Systemica** — eine Framework-Ebene, mathematisch neutrale Methodik zur Verifikation systemischer Maßnahmen. Probatio Systemica ist nicht klimaspezifisch; es stellt ein universelles Verifikationsverfahren bereit, das auf beliebige multidimensionale Interventionsprobleme anwendbar ist.

**Provolution** — die normative, klimaspezifische Anwendung von Probatio Systemica, bestehend aus 40 quantifizierten Anwendungen in 10 Domänen, mit expliziten SEC-Scores, CO₂-Impact-Schätzungen, Ressourcenbedarfen, Skalierungs-Roadmaps und Fallstudienbasis.

Das kombinierte Framework adressiert die drei oben identifizierten Strukturprobleme: Es liefert einen universellen Verifikationsstandard (das SEC-Prinzip und seine mathematische Formalisierung), prüft domänenübergreifende Konsistenz systematisch als erstrangiges Kriterium und ist explizit durch definierte Falsifizierungsszenarien falsifizierbar.

---

## 2. Theoretisches Framework: Probatio Systemica

### 2.1 Grundlagen

**Probatio Systemica** (aus dem Lateinischen: *probatio* — Beweis, Verifikation; *systemica* — systemisch) ist definiert als ein permanent selbstjustierendes, selbstlimitierendes Verifikations-Framework, das:

- **Neutral und deskriptiv** ist: Es spezifiziert Bedingungen, die Maßnahmen erfüllen müssen, ohne vorzuschreiben, welche Maßnahmen wünschenswert sind.
- **Mathematisch fundiert** ist: Alle Verifikationskriterien sind durch quantitative Bedingungen formalisiert.
- **Universell anwendbar** ist: Es ist nicht kulturgebunden oder domänenspezifisch.
- **Falsifizierbar by design** ist: Das Framework spezifiziert die genauen Bedingungen, unter denen es falsifiziert würde.

Das Kernelement ist das **SEC-Prinzip**, das drei notwendige Bedingungen definiert, die eine Maßnahme M erfüllen muss, um verifiziert (probiert) zu werden.

### 2.2 Das SEC-Prinzip

#### 2.2.1 S — Sufficient (Ausreichend)

**Definition:** Eine Maßnahme M ist sufficient, genau dann wenn ihre Wirkung W(M) die minimal erforderliche Wirkung W_min erreicht oder überschreitet.

**Formalisierung:**
```
∀ M ∈ Maßnahmen: Probatio(M) → W(M) ≥ W_min
```

Dabei ist W(M) der Wirkungsvektor der Maßnahme M und W_min der kontextspezifische Mindest-Wirkungsschwellenwert. In multidimensionalen Kontexten ist W(M) ein Vektor; Suffizienz wird dimensionsweise oder durch ein normiertes Aggregat bewertet.

**Begründung:** Eine Maßnahme, die die minimal erforderliche Wirkung nicht erzielt, ist nutzlos — unabhängig davon, wie effizient oder konsistent sie ist. Suffizienz ist eine notwendige, aber nicht hinreichende Bedingung für die Verifikation.

#### 2.2.2 E — Efficient (Effizient)

**Definition:** Eine Maßnahme M ist efficient, wenn sie den Ressourcenverbrauch R(M) minimiert und dabei die Suffizienz-Bedingung einhält.

**Formalisierung:**
```
min R(M) unter der Nebenbedingung W(M) ≥ W_min
```

Effizienz wird nur unter Maßnahmen bewertet, die bereits sufficient sind. Die optimale Maßnahme ist jene, die W_min mit minimalem Ressourceneinsatz erreicht.

**Begründung:** Angesichts der Klimadringlichkeit und begrenzten globalen Kapitals (geschätzter Bedarf €3–5 Billionen/Jahr [2]) stellt das Effizienzkriterium sicher, dass Ressourcen zu Maßnahmen mit dem höchsten Wirkungs-Ressourcen-Verhältnis fließen.

#### 2.2.3 C — Consistent (Konsistent)

**Definition:** Eine Maßnahme M ist consistent, wenn sie keine systemischen Widersprüche mit anderen Maßnahmen im Implementierungsset erzeugt.

**Formalisierung:**
```
∀ M_i, M_j ∈ Maßnahmen: ¬(M_i ⊥ M_j)
```

Dabei bezeichnet M_i ⊥ M_j einen systemischen Widerspruch — einen Zustand, in dem die Implementierung von M_i die Wirksamkeit von M_j unter akzeptable Grenzen reduziert oder umgekehrt.

**Begründung:** Klimatransformation erfordert die simultane Implementierung von Maßnahmen über Domänen hinweg. Konsistenz als erstrangiges Verifikationskriterium verhindert systemische Widersprüche, die fragmentierte Ansätze plagen (z. B. Aufforstungs-Bioenergie-Landkonflikt, CO₂-Bepreisung-Gerechtigkeitskonflikte).

### 2.3 Die Probatio-Logik (Verifikationsverfahren)

Verifikation (Probatio) ist das Verfahren, das bestimmt, ob eine vorgeschlagene Maßnahme die SEC-Bedingungen erfüllt:

```
Probatio(M) = Sufficient(M) ∧ Efficient(M) ∧ Consistent(M)

Wenn Probatio(M) = WAHR  → M ist verifiziert; zur Implementierung freigegeben
Wenn Probatio(M) = FALSCH → M wird abgelehnt oder zur Überarbeitung zurückgegeben
```

Das Verfahren läuft sequenziell ab: Eine Maßnahme, die den Suffizienztest nicht besteht, wird sofort abgelehnt, ohne Effizienz oder Konsistenz zu prüfen. Diese Reihenfolge spiegelt die logische Priorität von Wirkung gegenüber Optimierung wider.

### 2.4 Das Nullpunkt-Prinzip

Das **Nullpunkt-Prinzip** definiert den Referenzzustand, gegenüber dem Maßnahmen bewertet werden: den Zustand des Systems ohne Intervention (die kontrafaktische Baseline). Alle Wirkungsschätzungen W(M) werden relativ zu diesem Nullpunkt-Pfad gemessen, was Vergleichbarkeit zwischen Maßnahmen sicherstellt und Doppelzählung verhindert.

In der Provolution-Anwendung ist der Nullpunkt als Business-as-usual-Emissionspfad von ~55 Gt CO₂eq/Jahr ohne strukturellen Politikwandel definiert.

### 2.5 Unterscheidung: Framework vs. Anwendung

Ein zentrales Designmerkmal von Probatio Systemica ist seine Trennung in zwei Ebenen:

| Ebene | Komponente | Charakter |
|-------|-----------|-----------|
| Framework | Probatio Systemica (Bände 1–3) | Neutral, deskriptiv, mathematisch |
| Anwendung | Provolution (Bände 4–5) | Normativ, zielgerichtet, klimaspezifisch |

Diese Trennung ermöglicht die Anwendung des Frameworks auf andere Domänen ohne Modifikation, während die Anwendungsebene explizite normative Verpflichtungen trägt (z. B. das 1,5-°C-Ziel, Gerechtigkeitsprinzipien). Die Gewichtung des SEC-Scores (Abschnitt 3) spiegelt diese normativen Verpflichtungen auf Anwendungsebene wider und ist explizit diskutierbar.

---

## 3. Mathematische Formalisierung

### 3.1 Der SEC-Score

Der SEC-Score operationalisiert das SEC-Prinzip als skalare Größe für Ranking und Vergleich. In der Provolution-Anwendung ist der Score definiert als:

```
SEC(M) = 0,5 · S(M) + 0,3 · E(M) + 0,2 · C(M)
```

Die Gewichte spiegeln die normativen Prioritäten der Provolution-Anwendung wider: Unter Klimadringlichkeit wird Wirkung (S) am höchsten gewichtet; Effizienz (E) folgt; Konsistenz (C) wird als binäre Bedingung behandelt, die zu einem skalaren Gewicht normiert wird.

**Komponentendefinitionen:**

```
S(M) = W(M) / W_min          [Suffizienz-Verhältnis; für das Scoring auf 1,0 begrenzt]
E(M) = 1 − R(M) / R_max      [Effizienz: inverse Ressourcenfraktion]
C(M) = 1  wenn keine Widersprüche
       0  andernfalls          [Konsistenz: binär, dimensionsspezifisch]
```

**Interpretationsschwellen:**

| SEC-Score | Klassifikation |
|-----------|---------------|
| ≥ 0,90 | Exzellent |
| 0,80–0,89 | Gut |
| 0,70–0,79 | Akzeptabel |
| < 0,70 | Unzureichend (nicht probiert) |

**AUTO-INTEGRATE-Schwellenwert:** Anwendungen, die im Community-Einreichungsverfahren SEC_total ≥ 0,82 erreichen, sind zur automatischen Integration in den kanonischen Anwendungssatz berechtigt, vorbehaltlich menschlicher Überprüfung.

### 3.2 Multidimensionale Wirkungsvektoren

Klimamaßnahmen erzeugen gleichzeitig Wirkungen in mehreren Dimensionen — CO₂-Reduktion, Ressourcenverbrauch, Beschäftigung, Biodiversität, Gerechtigkeit. Der Wirkungsvektor ist:

```
W(M) = (W₁(M), W₂(M), ..., Wₙ(M))
```

wobei jede Dimension Wᵢ in ihrer natürlichen Einheit gemessen wird (Gt CO₂eq/Jahr, €/Jahr, geschaffene Arbeitsplätze usw.) und gegen ein dimensionsspezifisches W_min normiert wird. In Provolution ist die primäre Wirkungsdimension die CO₂-Äquivalent-Reduktion; sekundäre Dimensionen (wirtschaftlich, sozial, ökologisch) fließen in die Konsistenzprüfung ein.

### 3.3 Messstandards

Probatio Systemica übernimmt etablierte Messstandards zur Sicherstellung der Replizierbarkeit:

- **Treibhausgase:** GHG Protocol Scope 1–3 [9]; IPCC-AR6-100-Jahres-GWP-Faktoren [1]
- **Kosten:** Nettobarwert (NPV) mit 3 % sozialem Diskontierungssatz
- **Zeithorizonte:** PMI-Projektphasen; IPCC-Kurzziel (2030), mittelfristig (2035), langfristig (2050)
- **Fehlerbereiche:** Alle Schätzungen mit ±5 % Toleranzband; konservative α-Faktoren (Abschnitt 3.4)

### 3.4 Agentische Erweiterung: Automatisierungs-Konfidenzfaktoren

Die agentische Integrationsschicht quantifiziert die SEC-Score-Verbesserung, die durch KI-Agentenautomatisierung spezifischer Teilprozesse innerhalb jeder Anwendung erreichbar ist. Jedem automatisierbaren Teilprozess k in Anwendung M wird ein Automatisierungs-Konfidenzfaktor αₖ ∈ [0, 1] zugewiesen:

```
SEC_agentisch(M) = SEC(M) + Σₖ αₖ · Δ_SEC_k(M)
```

wobei Δ_SEC_k die marginale SEC-Verbesserung durch Automatisierung des Teilprozesses k ist und αₖ den aktuellen Stand der Technologiereife dieser Automatisierung widerspiegelt. Alle αₖ-Werte sind konservativ gesetzt (Bereich 0,70–0,95 über alle Anwendungen) auf Basis publizierter KI-Leistungsbenchmarks und sind explizit zitierbar.

Diese Schicht ist explizit optional: Das Kern-Framework und seine CO₂-Impact-Schätzungen hängen nicht von agentischer Verstärkung ab.

### 3.5 Falsifizierungskriterien

Probatio Systemica wird unter einer von drei Bedingungen falsifiziert:

**Falsifizierung 1 (Wirkung-Score-Inkonsistenz):** Wenn eine Anwendung M mit SEC(M) ≥ 0,70 in einer Realwelt-Implementierung nachweislich W(M) < W_min erzielt, ist die Suffizienz-Formel falsifiziert.

**Falsifizierung 2 (Effizienz-Pareto-Verletzung):** Wenn eine Maßnahme N existiert mit geringerem Ressourcenverbrauch R(N) < R(M) und gleicher oder höherer Wirkung W(N) ≥ W(M), aber SEC(N) < SEC(M), ist die Effizienz-Formel falsifiziert.

**Falsifizierung 3 (Konsistenz-Zirkularität):** Wenn Probatio(M | Kontext mit M) ≠ Probatio(M | Kontext ohne M), weist das System eine Zirkelabhängigkeit auf und das Framework ist falsifiziert.

Diese Falsifizierungsbedingungen sind bewusst konservativ gesetzt: Jede einzelne davon macht das Framework ungültig und erfordert Revision.

---

## 4. Methodik: Das Provolution-Anwendungs-Framework

### 4.1 Anwendungs-Template

Jede Provolution-Anwendung ist durch ein standardisiertes 7-Abschnitte-Template dokumentiert:

1. **Definition:** Problembeschreibung, Zielgruppe, Scope-Grenzen
2. **SEC-Nachweis:** Explizite Berechnung der S-, E-, C-Komponenten mit zitierten Quellen
3. **Wirkung (W):** Primäre und sekundäre quantifizierte Wirkungen mit Indikatoren und Zeithorizonten
4. **Ressourcen (R):** Finanziell (initial + laufend), Personal (FTE), Material, Zeit
5. **Skalierung:** Drei-Phasen-Modell (Pilot → Regional → Global) mit Gate-Kriterien
6. **Fallbeispiele:** Mindestens 2 pro Anwendung — 1 erfolgreiche Implementierung, 1 gescheiterter Versuch (Lerneffekt)
7. **Cross-Referenzen:** Synergien, CANON-Band-Links, Archiv-Quellen

Die Anforderung eines gescheiterten Fallbeispiels ist eine bewusste methodische Entscheidung: Sie erzwingt die Anerkennung der Bedingungen, unter denen die Maßnahme scheitert, und erhöht die epistemische Qualität der Aussage.

### 4.2 Domänen-Klassifikation

Die 40 kanonischen Anwendungen sind in 10 funktionale Domänen gegliedert:

| Domäne | Label | Anwendungen | Primärfunktion |
|--------|-------|-------------|----------------|
| A | Governance & Steuerung | 6 (A01–A06) | Evidenzbasierte Entscheidungsinfrastruktur |
| B | Produktion & Material | 4 (B07–B10) | Kreislaufwirtschaft, Materialtransformation |
| C | Energie & Infrastruktur | 4 (C11–C14) | Grid-Dekarbonisierung |
| D | Ernährung & Landnutzung | 4 (D15–D18) | Regenerative Landsysteme |
| E | Bildung & Soziales | 4 (E19–E22) | Bewusstsein, Gerechtigkeit, Kulturtransformation |
| F | Technologie & Innovation | 4 (F23–F26) | Forschung, Transfer, Beschleunigung |
| G | Monitoring & Korrektur | 3 (G27–G29) | Echtzeit-Systemsteuerung |
| H | Meta-Framework | 3 (H30–H32) | Finanzierung, Regulation, globale Koordination |
| I | Mobilität & Transport | 2 (I33–I34) | Kreislaufwirtschaft Fahrzeuge |
| J | Konstruktion & Gebäude | 1 (J01) | Gebäude als Kohlenstoffspeicher |
| Community | Offene Einreichungen | ≥1 (C-2026-*) | AUTO-INTEGRATE-verifizierte Maßnahmen |

Die Domänenstruktur folgt einer funktionalen Dekompositionslogik: Domänen A, G und H sind **Enabler** (sie schaffen die Bedingungen, unter denen B–F, I und J wirksam operieren können); Domänen B–F, I und J sind **Implementierung** (sie erzeugen direkten CO₂-Impact); diese Architektur spiegelt Enabler-Implementer-Muster aus dem Systems Engineering wider.

### 4.3 Dynamischer Anwendungssatz

Der Anwendungssatz ist nicht festgelegt. Neue Anwendungen treten über den AUTO-INTEGRATE-Mechanismus in den kanonischen Satz ein, wenn sie SEC_total ≥ 0,82 im Community-Einreichungsverfahren erreichen. Derzeit umfasst der kanonische Satz n = 40 Anwendungen in den Domänen A–J sowie Community-validierte Einreichungen (C-2026-*). Der Anwendungssatz wächst dynamisch mit jeder Einreichung, die den AUTO-INTEGRATE-Schwellenwert erreicht.

### 4.4 Validierungsansatz

Der SEC-Score jeder Anwendung leitet sich ab aus:

1. **Primärliteratur:** IPCC AR6, IEA-Szenarien, peer-reviewte Sektorstudien
2. **Realwelt-Implementierungen:** Die Fallstudienpflicht stellt sicher, dass jede Aussage in mindestens einem Realwelt-Präzedenzfall verankert ist
3. **Konservative Schätzung:** Bei unsicherer Datenlage werden Schätzungen bewusst an der unteren Grenze des plausiblen Bereichs angesetzt
4. **Kreuz-Validierung:** Alle Anwendungen werden auf gegenseitige Konsistenz (C-Kriterium) über den gesamten Domänensatz geprüft

Die Validierung ist kein kontrolliertes Experiment, sondern eine strukturierte Expertensynthese. Dies ist eine Limitation (Abschnitt 6.1).

---

## 5. Ergebnisse

### 5.1 Anwendungs-Scores und CO₂-Impact

Tabelle 1 präsentiert alle 40 kanonischen Anwendungen mit ihren SEC-Scores und geschätztem CO₂-Impact.

**Tabelle 1: Provolution-Anwendungen — SEC-Scores und CO₂-Impact**

| ID | Anwendung | Domäne | SEC-Score | CO₂-Impact (Gt/Jahr) |
|----|-----------|--------|-----------|----------------------|
| A01 | SEC-Priorisierung | Governance | 0,99 | Enabler |
| A02 | Entscheidungskarte | Governance | 0,94 | Enabler |
| A03 | Risikoabschätzung | Governance | 0,91 | Enabler |
| A04 | Szenarien-Vergleich | Governance | 0,91 | Enabler |
| A05 | Pilotprojekt-Framework | Governance | 0,90 | Enabler |
| A06 | Skalierungs-Protokoll | Governance | 0,91 | Enabler |
| B07 | Kreislaufwirtschaft | Material | 0,95 | −23,0 |
| B08 | Biopolymere (Hanf) | Material | 0,93 | −1,5 |
| B09 | Materialfluss-Steuerung | Material | 0,91 | −0,02 |
| B10 | Abfall-zu-Ressource | Material | 0,91 | −2,0 |
| C11 | Erneuerbare Integration | Energie | 0,95 | −15,0 |
| C12 | Energie-Speicherung | Energie | 0,91 | Enabler |
| C13 | Smart Grids | Energie | 0,91 | −0,5 |
| C14 | Dezentrale Versorgung | Energie | 0,91 | −0,3 |
| D15 | Regenerative Landwirtschaft | Ernährung/Land | 0,90 | −4,0 |
| D16 | CO₂-Senken (Boden) | Ernährung/Land | 0,90 | −5,0 |
| D17 | Hanf-Anbau | Ernährung/Land | 0,95 | −0,2 |
| D18 | Urbane Landwirtschaft | Ernährung/Land | 0,88 | −0,05 |
| E19 | Bewusstseinsbildung | Soziales | 0,89 | Enabler |
| E20 | Partizipation | Soziales | 0,89 | Enabler |
| E21 | Gerechtigkeits-Mechanismen | Soziales | 0,89 | Enabler |
| E22 | Kultur-Transformation | Soziales | 0,88 | Enabler |
| F23 | Forschungs-Priorisierung | Innovation | 0,90 | Enabler |
| F24 | Tech-Transfer | Innovation | 0,90 | Enabler |
| F25 | Open-Source-Infrastruktur | Innovation | 0,90 | Enabler |
| F26 | Innovation-Beschleunigung | Innovation | 0,88 | Enabler |
| G27 | MRV-System | Monitoring | 0,94 | Enabler |
| G28 | KI-Monitoring | Monitoring | 0,91 | Enabler |
| G29 | Blockchain-Tracking | Monitoring | 0,88 | Enabler |
| H30 | Finanzierungs-Mechanismen | Meta | 0,95 | Enabler |
| H31 | Regulierungs-Framework | Meta | 0,92 | Enabler |
| H32 | Globale Koordination | Meta | 0,91 | Enabler |
| I33 | Kreislauf-Auto | Mobilität | 0,95 | −1,0 |
| I34 | Kreislauf-LNF | Mobilität | 0,91 | −0,3 |
| J01 | Kreislauf-Gebäude | Konstruktion | 0,93 | −3,0 |
| C-2026-008 | Präzisionsfermentation + Hanf-Kaskade | Community | 1,00 | −3,0 |

*Enabler: kein direkter CO₂-Impact, aber erforderlich für die Implementierung wirkungsgenerierender Anwendungen.*

**Aggregierte Statistiken:**
- Mittlerer SEC-Score: **0,914** (SD = 0,028)
- Bereich: 0,88 (D18/E22/F26/G29) – 1,00 (C-2026-008)
- Anwendungen im Bereich „Exzellent" (≥ 0,90): 29 von 40 (72 %)
- Gesamt-CO₂-Minderungspotenzial: **−58,0 Gt/Jahr** (105 % der Baseline von 55 Gt — Netto-Negativ durch aktive Sequestration)

### 5.2 Analyse auf Domänenebene

**Tabelle 2: Zusammenfassung auf Domänenebene**

| Domäne | n | Ø SEC | CO₂-Impact (Gt/Jahr) | Primärhebel |
|--------|---|-------|----------------------|-------------|
| A — Governance | 6 | 0,94 | — | Entscheidungsqualität +55 % |
| B — Material | 4 | 0,93 | −26,5 | Kreislaufwirtschaft |
| C — Energie | 4 | 0,92 | −15,8 | Erneuerbare Integration |
| D — Ernährung/Land | 4 | 0,91 | −9,2 | Bodenkohlenstoff + Regeneration |
| E — Soziales | 4 | 0,89 | — | Akzeptanz +50 Pp. |
| F — Innovation | 4 | 0,90 | — | Time-to-Market −50 % |
| G — Monitoring | 3 | 0,91 | — | Echtzeit-Steuerung |
| H — Meta | 3 | 0,93 | — | €4,5 Bio./Jahr Finanzierung |
| I — Mobilität | 2 | 0,93 | −1,3 | Kreislaufwirtschaft Fahrzeuge |
| J — Konstruktion | 1 | 0,93 | −3,0 | Gebäude als Kohlenstoffspeicher |
| Community | ≥1 | 1,00 | −3,0 | Präzisionsfermentation + Hanf-Kaskade |

Der höchste direkte CO₂-Impact liegt in Domäne B (Kreislaufwirtschaft: −26,5 Gt/Jahr), getrieben hauptsächlich durch B07 Kreislaufwirtschaft (−23 Gt/Jahr), das auf die 45 % der globalen Emissionen abzielt, die mit linearen Produktionssystemen verbunden sind [10]. Domäne C (Energie: −15,8 Gt/Jahr) repräsentiert die konventionelle Energiewende [12]. Domänen I (Mobilität: −1,3 Gt/Jahr) und J (Konstruktion: −3,0 Gt/Jahr) erweitern die Kreislaufwirtschaftslogik auf Fahrzeugsysteme und die gebaute Umwelt, aus der 38 % der globalen Emissionen stammen. Die vergleichsweise moderaten Scores in Domäne E (Soziales, Ø 0,89) spiegeln die inhärente Schwierigkeit wider, Verhaltens- und Kulturwandel zu quantifizieren — diese Anwendungen werden als essentielle Enabler für die politische Akzeptanz des Implementierungs-Fahrplans behandelt.

### 5.3 Systemarchitektur und kritische Abhängigkeiten

Die 40 Anwendungen bilden ein strukturiertes, geschichtetes System mit drei Architekturebenen:

**Ebene 1 — Foundation (A01–A06):** Governance-Werkzeuge, die die Entscheidungsinfrastruktur bereitstellen. Ohne funktionale Governance ist die Identifikation und Priorisierung wirkungsstarker Maßnahmen beeinträchtigt.

**Ebene 2 — Implementierung (B07–F26):** Zwanzig Maßnahmen, die direkten CO₂-Impact generieren oder rasche Technologiediffusion ermöglichen.

**Ebene 3 — Meta-Framework (G27–H32):** Vier Enabler-Maßnahmen, die die systemischen Voraussetzungen bereitstellen. H30 (Finanzierung: +€4,5 Bio./Jahr) ist eine kritische Abhängigkeit — ohne Klimafinanzierung in der erforderlichen Größenordnung ist die Implementierung aller Ebene-2-Maßnahmen blockiert. G27 (Monitoring) liefert die Echtzeit-Rückkopplungsschleife, ohne die adaptive Korrektur unmöglich ist.

Diese Architektur impliziert eine sequenzierte Implementierungspriorität: Ebene 3 (Meta-Framework und Monitoring) muss aktiviert werden, bevor Ebene 2 wirksam skalieren kann. Diese Sequenzierung ist im Drei-Phasen-Skalierungs-Fahrplan formalisiert.

### 5.4 Skalierungs-Fahrplan

Der Implementierungs-Fahrplan ist in drei Phasen gegliedert, die den IPCC-Kurzzeit- und Mittelfrist-Horizonten entsprechen:

**Phase 1: Foundation (2025–2027)**
Meta-Framework-Anwendungen (H30–H32) und Monitoring-Infrastruktur (G27) aktivieren. Ziel: CO₂-Bepreisung bei €50/t in 10 Ländern; Green Bonds €200 Mrd./Jahr; MRV-Protokolle für 100 Projekte; Governance-Werkzeuge (A01–A06) ausgerollt.
*Impact: €500 Mrd./Jahr Klimafinanzierung erschlossen; Monitoring für 100 Projekte operativ.*

**Phase 2: Demonstration (2027–2035)**
Hochimpakt-Anwendungen in Prioritätsreihenfolge skalieren: B07 (10 % → 40 % Recyclingquote), C11 (20 % → 60 % Erneuerbare), D15 (2 % → 30 % regenerative Landwirtschaftsfläche), F25 (Open-Source-Klimatech), E19–E22 (soziale Enablement-Programme).
*Impact: −22 Gt CO₂/Jahr; €3 Bio./Jahr Investment fließend; Bewusstsein 70 %.*

**Phase 3: Vollständige Dekarbonisierung (2035–2050)**
Alle n kanonischen Anwendungen bei 80–100 % Skalierung. Net-Zero-Ziel: 2040–2050.
*Impact: −50,7 Gt CO₂/Jahr; System vollständig implementiert.*

### 5.5 Agentische Integrationsergebnisse

Die optionale agentische Integrationsschicht quantifiziert KI-Verbesserungspotenzial über alle 40 Anwendungen. Wesentliche Befunde:

- **Durchschnittliche SEC-Verbesserung:** +8,7 % (Bereich: +5,3 % bis +8,4 %)
- **Durchschnittlicher Automatisierungs-Konfidenz:** α_mean = 0,82
- **Höchste Verbesserung:** A03 Risikoabschätzung (+7,9 %), A04 Szenarien-Vergleich (+8,0 %), A05/A06 Pilot/Skalierung (+8,2 %, +8,4 %)
- **Stärkst eingeschränkt:** A01 (begrenzt auf +5,3 % durch die Human-only-Entscheidungsrestriktion an der SEC-Obergrenze)

Die Governance-Anwendungen (Domäne A) zeigen das höchste relative agentische Verbesserungspotenzial, was widerspiegelt, dass Governance-Prozesse erhebliche Informationsverarbeitungs- und Dokumentenanalyseaufgaben umfassen, die gut für Automatisierung geeignet sind. Implementierungs-Anwendungen (B–D) zeigen moderatere Verbesserungen, da physikalische Restriktionen (Materialflüsse, Energiesysteme) den marginalen Beitrag von KI-Agenten auf Prozessoptimierung statt auf Designveränderung begrenzen.

Human-in-the-Loop-Restriktionen sind für alle 40 Anwendungen definiert: Keine Anwendung erlaubt KI-autonome Entscheidungen oberhalb definierter Finanzschwellen (typischerweise €500k–€10 Mio.), bei ethischen Zielkonflikten oder in sicherheitskritischen Operationen.

### 5.6 Business Case

Ein repräsentativer Fünfjahres-Business-Case für ein Portfolio von drei Einstiegs-Anwendungen (A01, C11, F23) ergibt:

```
Anfangsinvestition:       €500 Mio.
Jährliche Kosteneinsparung: €84 Mio.
Netto-ROI (5 Jahre):      +78 %
Amortisationszeitraum:    2,4 Jahre
```

Die Meta-Anwendung H30 (CO₂-Bepreisung bei €80/t, EU-ETS-Maßstab) generiert ca. €80 Mrd./Jahr Einnahmen, was ausreicht, um die vollständige Phase-1-Implementierung der übrigen 29 Anwendungen unter dem €4,5-Bio./Jahr-Finanzierungsziel selbst zu finanzieren.

---

## 6. Diskussion

### 6.1 Limitationen

**1. Validierungsmethodik.** Die in dieser Arbeit berichteten SEC-Scores sind aus strukturierter Literatursynthese und Expertenwissen abgeleitet, nicht aus kontrollierten Experimenten oder randomisierten Vergleichen. Die in jeder Anwendung zitierten Realwelt-Fallstudien liefern empirische Verankerung, stellen jedoch keine randomisierte Evidenz dar. Unabhängige Replikation der SEC-Berechnung für eine Teilmenge von Anwendungen durch nicht affiliierte Forschungsteams ist ein notwendiger nächster Schritt zur wissenschaftlichen Validierung.

**2. Wechselwirkungseffekte.** Während das Konsistenzkriterium (C) explizit auf paarweise Widersprüche zwischen Maßnahmen prüft, ist die vollständige Wechselwirkungslandschaft von 40 simultanen Anwendungen nicht erschöpfend kartiert. Emergente systemische Effekte — zum Beispiel zwischen großflächiger Landnutzungsänderung (D15–D17) und lokaler Energiesystemtransformation (C14) — erfordern detaillierte regionale Modellierung, die über den Rahmen dieser Framework-Arbeit hinausgeht.

**3. Regionale Heterogenität.** Alle Impact-Schätzungen sind globale Durchschnittswerte. Regionale Variation in Klimabedingungen, institutioneller Kapazität, Infrastruktur-Baselines und politischer Ökonomie wird zu erheblichen Abweichungen vom globalen Mittelwert führen. Das Framework liefert regionalspezifische Anpassungshinweise in den Skalierungs-Templates, generiert jedoch keine regionalspezifischen quantitativen Projektionen.

**4. Unsicherheit bei agentischer Integration.** Die Automatisierungs-Konfidenzfaktoren (αₖ) basieren auf KI-Fähigkeitsbewertungen des Jahres 2025. Rasche Fortschritte bei KI-Fähigkeiten könnten diese Schätzungen innerhalb von 2–3 Jahren konservativ erscheinen lassen; umgekehrt könnten KI-Stagnation oder sicherheitsgetriebene Einsatzbeschränkungen sie optimistisch erscheinen lassen.

**5. Normative Transparenz.** Die Provolution-Gewichtung (0,5·S + 0,3·E + 0,2·C) kodiert eine normative Priorität — Wirkung vor Effizienz — die unter Klimadringlichkeit angemessen, aber diskutierbar ist. Alternative Gewichtungen würden Ranking-Ergebnisse und Implementierungsprioritäten verändern. Diese Transparenz über die normative Struktur betrachten wir als Feature, nicht als Limitation.

### 6.2 Vergleich mit bestehenden Frameworks

**Probatio Systemica vs. IPCC-Szenariopfade:** IPCC-Pfade liefern maßgebliche probabilistische Projektionen für Emissionspfade unter verschiedenen politischen Annahmen. Sie sind keine Entscheidungsunterstützungswerkzeuge im hier verwendeten Sinne — sie ranken keine Einzelmaßnahmen, spezifizieren keine domänenübergreifenden Konsistenzbedingungen und liefern keine standardisierten Ressourcentemplates. Provolution ist komplementär: Es operiert auf Ebene der Maßnahmenauswahl und -priorisierung und verwendet IPCC-Daten als Input für W_min-Schwellenwerte und Impact-Schätzungen.

**Provolution vs. Project Drawdown:** Project Drawdown [7,8] ist der nächste bestehende Präzedenzfall für die Quantifizierung von Klimalösungspotenzial über mehrere Domänen hinweg. Die wesentlichen methodischen Unterschiede sind: (a) Provolution prüft domänenübergreifende Konsistenz explizit als erstrangiges Kriterium; (b) der SEC-Score liefert einen einheitlichen Verifikationsstandard über Domänen hinweg, der Ranking ermöglicht; (c) die agentische Integrationsschicht quantifiziert KI-Verbesserungspotenzial, das zur Zeit der Entwicklung von Project Drawdown nicht verfügbar war; (d) Provolution ist vollständig Open-Source und enthält Community-Einreichungspfade. Ein systematischer Vergleich von SEC-Scores vs. Drawdown-Impact-Rankings für überlappende Maßnahmen wäre eine wertvolle Folgestudie.

**Probatio Systemica vs. MCA/MCDA:** Multikriterien-Entscheidungsanalyse (MCDA)-Frameworks teilen die multidimensionale Aggregationsstruktur des SEC-Scores. Der wesentliche Unterschied: MCDA gewichtet Kriterien typischerweise nach Stakeholder-Präferenzen (oft durch Befragungen erhoben), während Probatio Systemica eine einzige universelle Score-Formel mit explizit angegebenen normativen Gewichten verwendet. Dies macht Probatio Systemica weniger flexibel, aber transparenter und reproduzierbarer.

### 6.3 Ethische Überlegungen

**Gerechtigkeit und Verteilung.** Die explizite Aufnahme von E21 (Gerechtigkeits-Mechanismen) als kanonische Anwendung spiegelt die Erkenntnis wider, dass Klimatransformation, die eine ungerechte Lastenverteilung nicht adressiert, politischen Backlash und Implementierungsversagen erleben wird — wie der Zusammenbruch der US-amerikanischen Kohleregionen und die Gelbwesten-Proteste in Frankreich belegen. Die globale Jobbilanz der Energiewende (+40 Mio. neue Arbeitsplätze vs. −15 Mio. Arbeitsplätze in der fossilen Industrie [1,2]) ist aggregiert positiv, aber regional konzentriert, was aktive Just-Transition-Programme als politische Voraussetzung erfordert.

**Agentische Systeme und menschliche Autonomie.** Die Human-in-the-Loop-Restriktionen, die für alle 40 agentischen Anwendungen spezifiziert sind, reflektieren ein Designprinzip: KI-Agenten in Klimagovernance-Kontexten können Informationsverarbeitung und Optimierung automatisieren, aber Entscheidungen mit normativen, sicherheitsrelevanten oder finanziell hochvolumigen Implikationen erfordern menschliche Autorisierung. Dieses Prinzip ist nicht nur ethisch, sondern auch praktisch: Verantwortlichkeit für Klimagovernance-Entscheidungen kann nicht an autonome Systeme delegiert werden.

**Open Science und CC0-Lizenzierung.** Die vollständige Veröffentlichung des Frameworks, der Daten und der Templates unter CC0 1.0 (Public Domain) ist eine bewusste Entscheidung zur Maximierung der Zugänglichkeit, insbesondere für Forscher und Praktiker im Globalen Süden, die dem größten Klimarisiko und den schwersten Ressourcenrestriktionen ausgesetzt sind.

### 6.4 Zukünftige Forschung

**1. Ausbau Domäne I & J.** Domäne I (Kreislaufwirtschaft — Fahrzeuge und LNF) und Domäne J (Kreislaufwirtschaft — Gebäude) befinden sich derzeit als Stub-Anwendungen in Entwicklung mit geschätzten SEC-Scores von 0,91 bzw. 0,93 und kombiniertem CO₂-Potenzial von ca. −3,3 Gt/Jahr.

**2. Unabhängige Replikationsstudie.** Prioritärer wissenschaftlicher Validierungsschritt: Unabhängige Forschungsteams sollten das Probatio-Verfahren auf eine Stichprobe von 5 Anwendungen anwenden und berichten, ob sie SEC-Scores innerhalb des ±0,05-Toleranzbands erhalten.

**3. Regionale Parametrisierung.** Entwicklung regionalspezifischer W_min-Schwellenwerte und Ressourcenkostenparameter für klimakritische Regionen (Subsahara-Afrika, Südostasien, Südamerika) ist erforderlich, um globale Schätzungen in regionale Aktionspläne zu übersetzen.

**4. Longitudinale Validierung.** Wenn Provolution-Anwendungen in Realwelt-Implementierung eintreten, sollten empirische SEC-Scores verfolgt und mit den Pre-Implementierungsschätzungen verglichen werden. Dies ermöglicht iterative Rekalibrierung der Vorhersagegenauigkeit des Frameworks.

**5. SEC-J-Dimension.** [Corrigendum 2026-04-27: Die im Manuskript-Entwurf v0.1 angegebene Formel SEC-J = 0,5·S + 0,3·E + 0,1·C + 0,1·J entsprach einer frühen Entwicklungsversion. SECJ_SPEC v1.0 (2026-04-27) korrigierte sie zu SEC-J = 0,40·S + 0,25·E + 0,15·C + 0,20·J mit J-Veto bei J < 0,50. Siehe `canon/en/CORRIGENDUM_2026-04-27.md`.] [Corrigendum 2026-05-28: SECJ_SPEC v1.0 ist seit der PS-U 2.0 Extension (2026-05-10) selbst DEPRECATED. Aktuelle autoritative Formeln sind STANDARD-Modus `SEC-J(m) = 0,30·S + 0,25·E + 0,30·C + 0,15·J` und JUSTICE-Modus `SEC-J(m, justice) = 0,25·S + 0,15·E + 0,20·C + 0,40·J`. Siehe `canon/de/06_framework_extensions_v2.0_SECJ.md` und `canon/en/CORRIGENDUM_2026-05-28.md`.] Eine Gerechtigkeitserweiterung des SEC-Scores (SEC-J = 0,5·S + 0,3·E + 0,1·C + 0,1·J) befindet sich in Entwicklung, um Verteilungsgerechtigkeit formal als vierte Komponente des Verifikationsstandards einzubeziehen, statt sie ausschließlich über die Konsistenzprüfung zu behandeln.

---

## 7. Schlussfolgerung

Die Klimakrise erfordert nicht bessere Einzelmaßnahmen, sondern bessere systematische Koordination von Maßnahmen unter Ressourcenrestriktionen. Diese Arbeit hat Probatio Systemica präsentiert — ein mathematisch fundiertes, falsifizierbares und universell anwendbares Framework zur systematischen Verifikation von Klimamaßnahmen — sowie Provolution, seine Anwendung auf 40 quantifizierte Klimatransformations-Maßnahmen in 10 Domänen.

Die wesentlichen Befunde sind:

1. Ein einheitlicher Verifikationsstandard — das SEC-Prinzip und sein Komposit-Score — ermöglicht domänenübergreifenden Vergleich und das Ranking von Klimamaßnahmen auf reproduzierbare, falsifizierbare Weise.

2. Bei vollständiger Implementierung ergeben die 40 kanonischen Provolution-Anwendungen ein geschätztes CO₂-Minderungspotenzial von −58,0 Gt/Jahr, das die aktuellen globalen Emissionen von 55 Gt/Jahr übersteigt (105 %), bei einem mittleren SEC-Score von 0,914 — mit Netto-Negativ-Potenzial durch aktive Kohlenstoffsequestrierung.

3. Die Systemarchitektur — mit Governance, Monitoring und Finanzierung als Enabler-Schichten für Implementierungs-Anwendungen — impliziert eine sequenzierte Implementierungspriorität, die sich wesentlich von politisch getriebenen, sektorweisen Ansätzen unterscheidet.

4. Eine integrierte agentische Schicht quantifiziert KI-Verbesserungspotenzial bei durchschnittlich +8,7 % SEC-Steigerung, während explizite Human-in-the-Loop-Restriktionen menschliche Verantwortlichkeit für normative Entscheidungen wahren.

5. Das Framework ist vollständig als Open-Source unter CC0 1.0 verfügbar und ermöglicht unabhängige Verifikation, Replikation und Adaptation.

Klimatransformation ist aus dieser Perspektive primär kein technologisches, sondern ein epistemologisches Problem: das Fehlen eines gemeinsamen, mathematisch konsistenten Standards dafür, was als ausreichende, effiziente und konsistente Maßnahme gilt. Probatio Systemica schlägt einen solchen Standard vor. Wir laden die wissenschaftliche Gemeinschaft ein, ihn zu testen, herauszufordern und zu verbessern.

---

## Literaturverzeichnis

1. IPCC. *Klimawandel 2022: Minderung des Klimawandels*. Beitrag der Arbeitsgruppe III zum Sechsten Sachstandsbericht des IPCC (Hrsg. Shukla, P.R. et al.) (Cambridge University Press, 2022). https://doi.org/10.1017/9781009157926

2. IEA. *Net Zero by 2050: A Roadmap for the Global Energy Sector* (Internationale Energieagentur, 2021). https://www.iea.org/reports/net-zero-by-2050

3. Lenton, T.M. et al. Climate tipping points — too risky to bet against. *Nature* **575**, 592–595 (2019). https://doi.org/10.1038/d41586-019-03595-0

4. Rockström, J. et al. Safe and just Earth system boundaries. *Nature* **619**, 102–111 (2023). https://doi.org/10.1038/s41586-023-06083-8

5. UNFCCC. *Pariser Abkommen* (Rahmenübereinkommen der Vereinten Nationen über Klimaänderungen, 2015). https://unfccc.int/sites/default/files/english_paris_agreement.pdf

6. Popper, K.R. *Logik der Forschung* (Mohr Siebeck, 1934; Neuausgabe Hutchinson & Co., 1959; repr. Routledge, 2002). ISBN 978-0415278447.

7. Hawken, P. (Hrsg.) *Drawdown: The Most Comprehensive Plan Ever Proposed to Reverse Global Warming* (Penguin Books, 2017). ISBN 978-0143130444.

8. Project Drawdown. *The Drawdown Review: Climate Solutions for a New Decade* (Project Drawdown, 2020). https://drawdown.org/drawdown-framework/drawdown-review

9. World Resources Institute & WBCSD. *The Greenhouse Gas Protocol: A Corporate Accounting and Reporting Standard* (WRI/WBCSD, 2004). https://ghgprotocol.org/corporate-standard

10. Ellen MacArthur Foundation. *Completing the Picture: How the Circular Economy Tackles Climate Change* (Ellen MacArthur Foundation, 2019). https://www.ellenmacarthurfoundation.org/completing-the-picture

11. Science Based Targets initiative. *SBTi Corporate Manual v2.0* (SBTi, 2023). https://sciencebasedtargets.org/resources/files/SBTi-manual.pdf

12. IRENA. *Renewable Power Generation Costs in 2022* (Internationale Energieagentur für Erneuerbare Energien, 2023). https://www.irena.org/publications/2023/Aug/Renewable-Power-Generation-Costs-in-2022

13. Lazard. *Lazard's Levelized Cost of Energy Analysis — Version 16.0* (Lazard, 2023). https://www.lazard.com/research-insights/2023-levelized-cost-of-energyplus/

*Sektorspezifische Referenzen und weitere anwendungsspezifische Zitate sind im Ergänzenden Material (Band 4 Anwendungsdokumentation) aufgeführt.*

---

## Ergänzendes Material

**Supplement 1:** Vollständige Anwendungsdokumentation (40 Anwendungen × 7 Abschnitte) — verfügbar in `06_CANON/04_Band4_Anwendungen_v4.2.md`

**Supplement 2:** Mathematische Ableitungen (SEC-Formeln, α-Faktor-Ableitungen) — verfügbar in `06_CANON/03_Band3_Scientific_Core.md`

**Supplement 3:** Governance- und Score-Methodik — verfügbar in `06_CANON/05_Band5_Steuerung_Score.md`

**Supplement 4:** Community-Submission-Pipeline und AUTO-INTEGRATE-Protokoll — verfügbar in `04_CONTENT_LEVERS/community_pipeline.py`

**Alle Materialien:** https://github.com/yokadeeds-dev/Provolution (CC0 1.0)

---

*Entwurf v0.1 — 2026-04-18 — Zur internen Prüfung vor Einreichung*
*Wortanzahl (Haupttext): ca. 4.600 Wörter*
