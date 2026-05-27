# STUB: I34 – Kreislauf-LNF (Leichte Nutzfahrzeuge)

**Status:** STUB — SEC-Vorschätzung qualifiziert, Vollkonzept ausstehend
**App-ID:** I34
**Domain:** I – Mobilität
**Version:** 0.1 (2026-04-17)

---

## Kern-Idee

Die PKW-Kaskade aus I33 (Kreislauf-Auto) überträgt sich auf leichte Nutzfahrzeuge bis 3,5 t (Transporter, Kleintransporter, Lieferwagen). Diese Fahrzeugklasse teilt die wesentlichen physikalischen Voraussetzungen:

- Geschwindigkeit bereits auf 80–100 km/h beschränkt (Fahrphysik/Zulassung)
- Nutzlast-Anforderungen erlauben Bio-Composites für Karosserie-Außenhaut und Aufbau
- Hanf-Dämmung im Laderaum (Temperaturschutz + CO₂-Speicherung)
- Flottengröße DE: ~3 Mio. Fahrzeuge; global mehrere Hundert Millionen

---

## Kaskade (analog I33)

```
Upstream-Constraint:     Max. Nutzlast-Regulierung + Eco-Design-Mandat
        ↓
Right-Sizing:            Downsizing Antrieb (elektrisch/hybrid), Laderaum optimiert
        ↓
Bio-Materialien möglich: Hanf-Composit Außenhaut, Hanf-Dämmung Aufbau, Bio-Polymer-Ausstattung
        ↓
Carbon Sink:             Fahrzeugkarosserie speichert CO₂ für 10–15 Jahre Fahrzeuglebenszeit
```

---

## SEC-Vorschätzung

| Dimension | Wert | Begründung |
|-----------|------|------------|
| S (Suffizienz) | 0.88 | Kaskadenlogik greift fast identisch; etwas geringer als PKW wegen höherer Nutzlast-Variabilität |
| E (Effizienz) | 0.90 | Bio-Composites für Aufbauten nachgewiesen (Kühlfahrzeuge, Handwerkerausbau); Hanf-Dämmung etabliert |
| C (Konsistenz) | 1.0 | Vollständig systemkonform mit I33 und B08 (Biopolymere) |
| **SEC gesamt** | **0.91** | 0.5×0.88 + 0.3×0.90 + 0.2×1.0 = 0.44 + 0.27 + 0.20 |

→ **Qualifiziert für AUTO-INTEGRATE** (Schwelle: ≥ 0.82)

---

## CO₂-Potenzial (Schätzung)

- DE-Flotte: ~3 Mio. LNF, Ø-Emissions-Delta geringer als PKW (bereits niedrigere Geschwindigkeit)
- Global: ~10% der PKW-Effekte realistisch → ~0.3 Gt CO₂/Jahr
- Zusatz: Hanf-Aufbauten als Kurzzeit-Kohlenstoffspeicher (weniger als PKW-Karosserie, aber signifikant)

---

## Scope-Definition

**In Scope:**
- Fahrzeuge der Klasse N1 (≤ 3,5 t zGM): Transporter, Kleintransporter, Lieferwagen
- Karosserie-Außenhaut, Aufbauten, Innenausstattung aus Bio-Composites
- Elektrischer oder hybrider Antrieb als Voraussetzung (ohne Right-Sizing kein Gewichtsvorteil)

**Out of Scope:**
- Schwere Nutzfahrzeuge (> 3,5 t) → Hard-to-Abate, andere Physik
- Sonderfahrzeuge (Feuerwehr, Baumaschinen) → eigene Kategorie

---

## Offene Punkte (für Vollkonzept)

- [ ] Konkrete CO₂-Berechnungen für DE-Flotte (analog I33-Methodik)
- [ ] Hersteller-Referenzen für Bio-Composite-Aufbauten (gibt es bereits Piloten?)
- [ ] Regulatorischer Upstream-Constraint definieren (EU-Eco-Design-Verordnung LNF?)
- [ ] SEC-J-Score berechnen (J-Dimension: Wer profitiert? Handwerker, Lieferdienstfahrer)
- [ ] Abgrenzung zu E-Lieferwagen (I34 ist materialfokussiert, nicht antriebsfokussiert)

---

## Verknüpfungen

| App | Relation |
|-----|----------|
| I33 Kreislauf-Auto | Kaskaden-Vorlage — gleiche Logik, andere Fahrzeugklasse |
| B08 Biopolymere | Upstream-Materiallieferant für Composites und Dämmung |
| D17 Hanf-Ökosystem | Rohstoffquelle Hanf-Faser für Aufbauten und Dämmung |
| F23–F25 Technologie | Tech-Transfer Composite-Herstellung auf LNF-Aufbauten |

---

*Stub erstellt: 2026-04-17 | Nächster Schritt: Vollkonzept analog Kreislauf-Auto/Konzept_Kreislauf-Auto.md*
