# Probatio Narrativa (PN)
## Submodul von Probatio Systemica · SEC-J-Analyse von Mediendiskursen
### CANON-Dokument · Version 1.0 · 2026-04-09
**Autor:** Tobias Yoka Dietz
**Status:** Entwurf · peer-review-vorbereitet
**Einordnung:** PS-Submodul · Kein numerisches Verdict – erzeugt qualitative Framing-Karte

---

## 0. PRÄAMBEL

**Probatio Narrativa (PN)** überträgt die SEC-J-Prüflogik auf Narrative und Mediendiskurse. PN prüft nicht einzelne Behauptungen (PV), Entscheidungen (PD) oder Institutionen (PI), sondern **systemische Framing-Muster** über mehrere Quellen und Zeiträume.

Kernfrage: **Welche Perspektiven werden systematisch verstärkt, welche systematisch ausgeblendet?**

PN hat drei Besonderheiten gegenüber allen anderen PS-Modulen:
- **Kein numerisches Verdict** – PN erzeugt eine qualitative Framing-Karte
- **J-dominant** – J erhält Gewicht 0,40 (höchstes aller PS-Module)
- **Multiperspektivisch** – mindestens 3 Quellen zum gleichen Thema erforderlich

---

## 1. ABGRENZUNG

| Merkmal | PV | PD | PI | PN |
|---|---|---|---|---|
| Prüfobjekt | Einzelbehauptung | Einzelentscheidung | Institution | Diskursmuster |
| Kernfrage | Faktisch haltbar? | Prozessual konform? | Anspruch = Realität? | Wer spricht, wer fehlt? |
| Ausgabe | Numerisches Verdict | Numerisches Verdict | Numerisches Verdict | Framing-Karte |
| J-Gewicht | 0,15 | 0,25 | 0,25 | 0,40 |
| Quellenanzahl | 1 Claim | 1 Entscheidung | 1 Institution | mind. 3 Quellen |

---

## 2. NARRATIV-TAXONOMIE

### NT-1 · Mediendiskurs
Berichterstattungsmuster zu einem Thema über mehrere Medien.
Prüfpfad: Artikel-Sampling → Framing-Identifikation → Auslassungsanalyse.

### NT-2 · Politischer Diskurs
Argumentative Muster in Parlamentsdebatten, Wahlprogrammen.
Prüfpfad: Plenarprotokolle → Schlüsselwörter → Sprecherverteilung → fehlende Positionen.

### NT-3 · Wissenschaftskommunikations-Diskurs
Wie wissenschaftliche Erkenntnisse in Öffentlichkeit übersetzt werden.
Prüfpfad: Original (z.B. IPCC) → Medienberichte → Abweichungsanalyse.

### NT-4 · Kampagnen-Narrativ
Gezielt konstruierte Kommunikation von Organisationen oder Lobbygruppen.
Prüfpfad: Kampagnenmaterialien → Schlüsselbotschaften → Interessenstruktur.

---

## 3. MMM-VORFILTER

### M1 · Diskursklärung
- Welches Thema / welcher Diskurs?
- Zeitraum? (mind. 3 Monate für Muster, mind. 2 Jahre für Trends)
- Quellen? (mind. 3, möglichst unterschiedliche Perspektiven)
- Ergebnis: n(op) = operationalisierter Diskursrahmen

### M2 · Quellenverfügbarkeit

| Datenlage | Konsequenz |
|---|---|
| Vollständig (mind. 5 Quellen, unterschiedliche Träger) | → Weiter zu SEC-J |
| Teilweise (3–4 Quellen, begrenzter Zeitraum) | → Prüfen mit Einschränkungshinweis |
| Minimal (1–2 Quellen) | → BLOCK: mind. 3 Quellen erforderlich |

### M3 · Diskursdomäne

| Domäne | Modul | Referenzrahmen |
|---|---|---|
| Klimakommunikation | PN-Klima | IPCC AR6, Provolution-CANON, UBA |
| Sozialpolitik | PN-Sozial | Armutsberichte, SOEP |
| Gesundheit | PN-Gesundheit | WHO-Standards, RKI |
| Wirtschaft | PN-Wirtschaft | Wirtschaftswiss. Fachliteratur |
| Allgemein | PN-Default | Entman 1993, Scheufele 1999 |

---

## 4. SEC-J-PRÜFUNG

### S · Sufficient – Evidenzbasis des Diskurses

```
S(n) = Anteil faktisch belegter Kernaussagen

> 80% belegt      → HOCH    (0,80–1,00)
60–80% belegt     → MITTEL  (0,60–0,79)
40–60% belegt     → NIEDRIG (0,40–0,59)
< 40% belegt      → KRITISCH (0,00–0,39)

× Quellenvielfalt-Faktor:
  > 3 unabhängige Primärquellen → 1,00
  1–2 Primärquellen dominant    → 0,80
  Zirkuläre Quellenstruktur     → 0,60
```

### E · Efficient – Verzerrungsmuster

```
E(n) = 1 − (Anzahl_Verzerrungsmuster × 0,15)   [Minimum: 0,00]

Verzerrungsmuster (je −0,15):
  - Cherrypicking (selektive Datenzitierung)
  - Kontextentfernung (Zahlen ohne Bezugsrahmen)
  - Zeitliche Verzerrung (veraltete Daten)
  - Maßstabsverzerrung (lokal → global generalisiert)
  - Kausalitätsersatz (Korrelation als Ursache)
  - Expertenselektion (nur gleichgerichtete Stimmen)
```

### C · Consistent – Diskurskohärenz

```
C(n) = 1 − (Anteil_widersprüchlicher_Kernaussagen / Gesamtaussagen)

Widerspruchstypen:
  - Quelle widerspricht sich im Zeitverlauf
  - Diskurs widerspricht wissenschaftlichem Konsens
  - Implizite Annahmen vs. explizite Aussagen
  - Strukturelle Lücken: bekannte Gegenargumente ignoriert
```

PN-Flag: C(n) < 0,40 → "DISKURSINKONSISTENZ"

### J · Justice – Framing-Analyse (Kerndimension)

```
J(n) = (0,25×J1) + (0,35×J2) + (0,25×J3) + (0,15×J4)

J1 · Sprecherstruktur : Wer hat Zugang zum Diskurs?
J2 · Auslassung       : Welche Perspektiven/Gruppen/Daten fehlen systematisch?
J3 · Rahmung          : Wie wird das Problem definiert? Wer trägt Verantwortung?
J4 · Lösungsraum      : Welche Lösungen erscheinen möglich / werden ausgeblendet?
```

J2 (Auslassung) erhält das höchste Gewicht – systematische Auslassung ist das wirksamste Framing-Instrument.

PN-Flag: J(n) < 0,40 → "STRUKTURELLE AUSBLENDUNG"

---

## 5. AGGREGATION UND FRAMING-KARTE

```
PN(n) = (0,20×S) + (0,15×E) + (0,25×C) + (0,40×J)
```

### Profil-Typen (statt Verdict)

| PN(n) | Profil |
|---|---|
| ≥ 0,75 | AUSGEWOGEN |
| 0,55–0,74 | EINSEITIG |
| 0,35–0,54 | STARK VERZERRT |
| < 0,35 | PROPAGANDISTISCH |

---

## 6. OUTPUT-STRUKTUR

```
PN-REPORT · [Datum]

DISKURS: "[Thema]"
Typ: NT-[1/2/3/4] | n(op): "[Zeitraum + Quellenset]"
Domäne: PN-[...]

[MMM-ARTEFAKT]
  Quellenverfügbarkeit: [vollständig / teilweise / zu wenige]

SEC-J-PROFIL:
  S(n) = [Wert] · Niveau: [HOCH/MITTEL/NIEDRIG/KRITISCH]
  E(n) = [Wert] · Verzerrungsmuster: [Liste]
  C(n) = [Wert] · Widersprüche: [n]
  J(n) = [Wert] · J1=[x] J2=[x] J3=[x] J4=[x]

AGGREGATION:
  PN = (0,20×S) + (0,15×E) + (0,25×C) + (0,40×J) = [Gesamt]

PROFIL: [AUSGEWOGEN / EINSEITIG / STARK VERZERRT / PROPAGANDISTISCH]
[Ggf.] Flags: DISKURSINKONSISTENZ | STRUKTURELLE AUSBLENDUNG

FRAMING-KARTE:
  Evidenzbasis: [S-Niveau + dominante Quellen + Quellenvielfalt]
  Verzerrungen: [stärkste Muster mit Beispielen]
  Kohärenz: [Widersprüche + Lücken]
  J1 Sprecherstruktur: [wer dominiert]
  J2 Auslassungen: [systematisch fehlende Perspektiven]
  J3 Problemrahmung: [wie wird Problem definiert]
  J4 Lösungsraum: [was erscheint möglich / unmöglich]

ALTERNATIVE NARRATIVE:
  [Welche Gegennarrative existieren? Warum marginal?]

EMPFEHLUNGEN:
  [Welche Quellen/Perspektiven würden J2 erhöhen?]

QUELLEN: [1] [Medium · Datum]
EINSCHRÄNKUNGEN: [Sampling-Bias, Zeitraum-Limitation]
```

---

## 7. DOMÄNENMODUL: PN-KLIMA

### Referenzrahmen

| Rang | Quelle | Zweck |
|---|---|---|
| 1 | IPCC AR6 (Original) | S-Referenz: Was sagt die Wissenschaft? |
| 2 | Provolution-CANON | J4-Referenz: Welche Lösungen existieren? |
| 3 | UBA-Kommunikationsleitfäden | Kommunikationsstandards |
| 4 | Boykoff & Boykoff 2004 | Framing-Theorie Klimamedien |

### Typische PN-Klima-Muster

J2-Auslassungen (häufig): Globaler Süden, Einkommensschwache Haushalte, Systemlösungen, Kipppunkte.
J3-Rahmungen: Klimaschutz als Wirtschaftsrisiko statt -chance; "Wir alle" statt strukturelle Akteure.
J4-Verengungen: Erneuerbare als utopisch vs. fossile als pragmatisch; Provolution-Anwendungen unsichtbar.

### Verbindung zu Provolution

- PN-Klimaanalysen erklären, warum Provolution-Maßnahmen im Diskurs unsichtbar sind
- J4-Analyse liefert Kommunikationsstrategie-Input für Provolution Deutschland
- PN-Reports als Peer-Review-Evidenz für Wissenschaftskommunikationsdefizite

---

## 8. ABGRENZUNGSREGEL (KANONISCH)

> "PS-U → Maßnahme · PV → Behauptung · PD → Entscheidung · PI → Institution · PN → Diskurs.
> Die fünf Module bilden eine vollständige Prüfkette."

---

## 9. FALSIFIZIERBARKEIT

| Parameter | Wert | Anpassungsbedingung |
|---|---|---|
| wJ | 0,40 | Wenn J überbewertet → senken |
| wC | 0,25 | Wenn Kohärenz weniger relevant → senken |
| J2-Gewicht | 0,35 | Empirisch anpassbar |
| Verzerrungsabzug E | 0,15 | Moderater als andere Module (Vereinfachungen normal) |

---

## ANHANG: BEISPIEL-ANALYSE

**Diskurs:** CO₂-Bepreisung in deutschen Leitmedien 2021–2023 (FAZ, Spiegel, taz, BILD)

| Dim | Berechnung | Wert |
|---|---|---|
| S | ~70% belegt × Quellenvielfalt 0,80 (zirkulär) | 0,56 |
| E | 3 Muster (Cherrypicking, Kontextentfernung, Expertenselektion) | 0,55 |
| C | 2 Widersprüche (Technologieoptimismus vs. Dringlichkeit) | 0,60 |
| J | J1=0,55 / J2=0,40 / J3=0,50 / J4=0,45 | 0,47 |

**PN(n)** = (0,20×0,56)+(0,15×0,55)+(0,25×0,60)+(0,40×0,47) = 0,11+0,08+0,15+0,19 = **0,53**

**PROFIL: STARK VERZERRT** · Flag: STRUKTURELLE AUSBLENDUNG

Auslassungen: Global South, Niedrigeinkommensgruppen, Systemlösungen, Kipppunkte.

---

## LICENSE

This work is released under CC0 1.0 Universal + Open Humanity License.

*CANON-Referenz: 13_Probatio_Narrativa_v1.0.md · Version 1.0 · 2026-04-09 · Tobias Yoka Dietz*
