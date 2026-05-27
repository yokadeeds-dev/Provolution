# STUB: J01 – Kreislauf-Gebäude

**Status:** STUB — SEC-Vorschätzung qualifiziert, Vollkonzept ausstehend
**App-ID:** J01
**Domain:** J – Konstruktion (neu)
**Version:** 0.1 (2026-04-17)

---

## Kern-Idee

Das Kreislauf-Kaskaden-Prinzip aus Domain I überträgt sich auf den Bausektor — mit dem größten CO₂-Hebeleffekt aller Domains: **Bauen & Betrieb von Gebäuden verursacht 38% der globalen Treibhausgasemissionen.** Die Kaskade funktioniert analog:

```
Upstream-Constraint:     Embodied-Carbon-Limit + Passivhaus-Standard (rechtlich bindend)
        ↓
Right-Sizing:            Kleinere Lasten → Tragwerk aus Holz/Hanfbeton statt Stahl/Beton
        ↓
Bio-Materialien möglich: Hempcrete (Hanfbeton), CLT (Brettsperrholz), Myzel-Dämmstoffe
        ↓
Carbon Sink:             Gebäude speichert CO₂ für 50–100+ Jahre im Tragwerk
```

---

## SEC-Vorschätzung

| Dimension | Wert | Begründung |
|-----------|------|------------|
| S (Suffizienz) | 0.90 | Passivhaus-Standard + Embodied-Carbon-Limit klar definierbar; politisch in EU bereits im Gang (EPBD 2024) |
| E (Effizienz) | 0.92 | Hempcrete und CLT industriell erprobt; Massivholzbau in Europa etabliert; CO₂-Speicherung wissenschaftlich belegt |
| C (Konsistenz) | 1.0 | Vollständig systemkonform: nutzt D17 (Hanf), B08 (Biopolymere), B07 (Kreislaufwirtschaft) |
| **SEC gesamt** | **0.93** | 0.5×0.90 + 0.3×0.92 + 0.2×1.0 = 0.45 + 0.276 + 0.20 |

→ **Qualifiziert für AUTO-INTEGRATE** (Schwelle: ≥ 0.82)

---

## CO₂-Potenzial (Schätzung)

- Gebäude & Bau: ~14 Gt CO₂/Jahr global (Betrieb + Embodied Carbon)
- Adressierbarer Anteil (Neubauten + Kernsanierungen): ~30% des Sektors
- Konservative Schätzung J01: **~3.0 Gt CO₂/Jahr** (Embodied Carbon Reduktion + Speicherung)
- Langfristig kumulativ deutlich höher durch 50–100-jährige Speicherung im Bestand

---

## Scope-Definition

**In Scope:**
- Neubauten mit Passivhaus-Standard + Embodied-Carbon-Limit
- Kernsanierungen mit Bio-Materialien (Hempcrete, CLT, Hanf-Dämmung)
- Tragwerk- und Hüllkonstruktionen aus nachwachsenden Rohstoffen
- Wohn- und Gewerbebauten bis ~8 Stockwerke (Holzmassivbau-Grenze technisch erprobt)

**Out of Scope:**
- Hochhäuser (> 8 Stockwerke) → Stahltragwerk physikalisch notwendig; eigene App denkbar
- Infrastruktur (Brücken, Tunnel) → andere Lasten und Normen
- Betriebsenergie → bereits in C11–C14 (Erneuerbare, Dezentral) adressiert

---

## Warum eigene Domain J (nicht unter B oder D)?

- **Andere Akteure:** Baubranche, Architekten, Baugenehmigungsbehörden, EU-Gebäuderichtlinie (EPBD)
- **Andere Standards:** EN-Normen für Baukonstruktion, Brandschutz, Statik
- **Andere Metriken:** Embodied Carbon (kgCO₂eq/m²), U-Werte, Lebenszyklusanalyse (LCA)
- **Systemische Eigendynamik:** Die Kaskade (Constraint → Right-Sizing → Bio-Material → Carbon Sink) rechtfertigt eine eigene Domain analog zu Domain I

---

## Offene Punkte (für Vollkonzept)

- [ ] Konkrete CO₂-Berechnungen: Hempcrete vs. Beton (kgCO₂eq/m³ Vergleich)
- [ ] Upstream-Constraint präzisieren: Welches EU-Gesetz? EPBD Art. X? CO₂-Grenzwert in kg/m²?
- [ ] Hochhaus-Frage: Ab wann neue App J02 (Hybrid-Hochbau)?
- [ ] Textilien in Gebäuden (Hanf-Dämmstoffe, Naturfaser-Teppiche) — Abgrenzung zu D17
- [ ] SEC-J-Score: Gerechtigkeitsdimension (Wer kann sich Passivhaus leisten? Sozialwohnungsbau?)
- [ ] Pilotprojekte recherchieren: Hempcrete-Bauten in DE/AT/CH (gibt es bereits?)

---

## Verknüpfungen

| App | Relation |
|-----|----------|
| D17 Hanf-Ökosystem | Rohstoffquelle: Hanfschäben → Hempcrete, Hanffaser → Dämmmatten |
| B07 Kreislaufwirtschaft | Baustoff-Kreislauf: Rückbau → Wiederverwendung CLT-Elemente |
| B08 Biopolymere | Upstream: Biopolymer-Folien, Dichtungen, Fensterrahmen |
| C11–C14 Energie | Komplementär: J01 adressiert Embodied Carbon, C-Domain adressiert Betriebsenergie |
| I33 Kreislauf-Auto | Schwester-Konzept: gleiche Kaskaden-Architektur, andere Physik |

---

*Stub erstellt: 2026-04-17 | Domain J „Konstruktion" — J01 als erste App | Nächster Schritt: Vollkonzept + Pilotprojekt-Recherche*
