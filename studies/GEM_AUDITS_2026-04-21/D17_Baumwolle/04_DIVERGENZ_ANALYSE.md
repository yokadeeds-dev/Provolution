# Doppel-Audit D17 — Divergenz-Analyse PS 3.0 vs. PS-U 1.1

**Datum:** 2026-04-21
**Prüfobjekt:** D17 Hanf-Anbau (Nutzpflanze), Fokus Baumwolle-Substitutions-Sub-Argument
**Prüfer:** PS 3.0 Gem + PS-U 1.1 Gem (Google Gemini)
**Chat-URLs:**
- PS 3.0: `https://gemini.google.com/gem/dda4ee1e17c3/5ec3aa3b6297f77c`
- PS-U 1.1: `https://gemini.google.com/gem/905b325d7a92/f1572745e979286e`

---

## Kernverdict: Divergenz

| Dimension | PS 3.0 | PS-U 1.1 |
|---|---|---|
| **Verdict** | BESTANDEN / TRAGFÄHIG | nicht tragfähig (C) |
| **Prüflogik** | qualitativ (E1–E8, 8 ✅) | quantitativ (SEC-J Score) |
| **Gesamt-Score** | — (binär-qualitativ) | geo 0.71 · ari 0.76 |
| **Empfohlener Next Step** | PV-Verifikation Wasser-Zahlen | Harmonisierung Rechtsrahmen + Förderung Verarbeitungs-Cluster |

**Das ist genau die Art Triangulations-Divergenz, die wir uns erhofft haben:** Gleiche Faktenlage, gegensätzliches Urteil.

---

## Dimensions-Vergleich

### PS 3.0 Kaskade (alle ✅)
Alle 8 Ebenen BESTANDEN. E4 (Datenlage) explizit: *"Starke Evidenzbasis durch Canada/China-Beispiele. Substitutions-Daten konsistent mit E11."* E5 (Nebenwirkungen): *"Rebound-Effekt durch Billigtextilien wird indirekt durch Multi-Use minimiert."* E8 (Missbrauch): *"Dezentraler Anbau erschwert Monopolisierung. Gefahr Saatgut-Monopole, Gegenmaßnahme D15-Standardisierung."*

### PS-U 1.1 SEC-J
| Dim | Wert | Begründung |
|---|---|---|
| **S** | 1.00 | Ziel 100 Mt mit 185 Mt deutlich überschritten |
| **E** | 1.00 | Hanf = günstigste Alternative (vs. Flachs 12 Mrd, DAC 150 Mrd) |
| **C** | **0.40** | **Konflikte** (2): Betäubungsmittelrecht, Baumwoll-Subventionen. **Abhängigkeitslücken** (1): fehlende industrielle Verarbeitungskette. **C < 0.70 → Label `nicht tragfähig (C)`** |
| **J** | 0.63 | Zugang 0.80 / Verteilung 0.60 / Vulnerabilität 0.70 / **Partizipation 0.40** (Top-Down-Legalisierung) |

---

## Wo kommt die Divergenz her?

Die beiden Gems fragen **unterschiedliche Dinge**, die sich wie "ja" und "nein" anfühlen, es aber nicht sind:

1. **PS 3.0 fragt "Ist das System-Design tragfähig?"** — und das ist es (alle E1–E8 intern stimmig).
2. **PS-U 1.1 fragt "Ist die Maßnahme ressourceneffizient UND passt sie ohne Reibung ins bestehende System?"** — und letzteres ist sie nicht (Betäubungsmittelrecht, Subventions-Regimes, fehlende Verarbeitungsketten).

**Beide haben recht.** Die **Consistency-Dimension** von SEC-J ist strenger operationalisiert als E5/E8 bei PS 3.0 — sie zählt explizit Konflikte und Abhängigkeitslücken gegen Systembereiche und rechnet daraus einen Wert. PS 3.0 berücksichtigt Regulatorik intern in E3 (Annahmen) und E8 (Machtfrage), aber hat keine Schwelle dafür.

Das ist **kein Bug**, sondern der strukturelle Unterschied zwischen qualitativer SEC-Kaskade und quantitativer SEC-J-Metrik.

---

## Handlungsfähige Befunde für den Canon

Aus der Divergenz ergeben sich **konkrete Handlungspunkte** für D17:

1. **K1 — Betäubungsmittelrecht** (PS-U benannt): In der Canon-Anwendung wird "Hanf-Anbau illegal/stark reguliert" als Problem genannt, aber nicht als C-reduzierender strukturbruch quantifiziert. → **Empfehlung**: Explizite Risiko-Klausel in D17 §2 ergänzen.

2. **K2 — Baumwoll-Subventionen** (PS-U benannt, in D17 nicht erwähnt): Die globale Baumwoll-Subventionsarchitektur (USA/EU Farm Bills, Uzbekistan-Staatsquote) ist ein konkreter Gegenkraft-Faktor für die 10%-Substitutions-Annahme. → **Empfehlung**: D17 §3 Indikatoren um "Subventions-Parität" ergänzen.

3. **U1 — Verarbeitungs-Cluster-Lücke** (PS-U benannt): Fehlende Hanf-Entfasungsmaschinen in EU/Nordamerika. → **Empfehlung**: D17 §4 Material/Infrastruktur präzisieren (aktuelle Zahl Hanfentfaserer weltweit < 100).

4. **J-Dimension Partizipation 0.40** (PS-U benannt): Aktuelle Legalisierungs-Debatten sind Top-Down. → Verweist auf **E19/E20** (Bewusstseinsbildung, Partizipation) als flankierendes Instrument.

---

## Methodische Beobachtungen (Gem-Audit-Meta)

- **PS 3.0 aktivierte** ST-2 Claim-Taxonomie (Maßnahmen-Bündel / Strategie), zog Knowledge-Dateien Band 4/E11/Band 3, folgte Fazit-First-Format. Eingang-ID-Nummerierung sauber. Sub-Gem-Empfehlung an PV explizit.
- **PS-U 1.1 aktivierte** MMM M1→M2→M3 mit Artefakt, rechnete E/C mit Pflichtschritten (Alternativen A/B/C mit R-Werten, K/U/I_ges Zählung), gab JSON-Artefakt vollständig aus.
- **Bemerkenswert:** PS-U 1.1 wandte die Pflichtschritte der v1.1-Formeln korrekt an (siehe `GEM_SYSTEM_PROMPT_PS_Universal_v1.1.md` — "E-Formel mit Pflichtschritten und Minimalbeispiel" wurde im Output reproduziert).
- **Nebenbefund PS 3.0**: Ergebnis stark von der impliziten Lesart "System-Design" geprägt. Wäre die Eingabe als ST-3 (Einzelmaßnahme mit Wirkungsanspruch) klassifiziert worden, hätte PS 3.0 vermutlich stärker bei E4 differenziert.

---

## Gesamtbewertung Doppel-Audit-Methodik

Die Triangulation PS 3.0 + PS-U 1.1 liefert **genau das erwartete Muster**: System-Auditor sagt "tragfähig", Framework-Neutraler Numerik-Auditor sagt "strukturell zu reibungsvoll". Für Provolution-Kandidaten ist das ein wertvolles **Spannungs-Signal** — nicht Widerspruch, sondern unterschiedliche Prüfschärfen auf unterschiedlichen Dimensionen.

**Empfehlung für zukünftige Doppel-Audits:** Workflow beibehalten, PS-U-C-Befunde als konkrete Handlungspunkte in Canon-Einträge einspielen.
