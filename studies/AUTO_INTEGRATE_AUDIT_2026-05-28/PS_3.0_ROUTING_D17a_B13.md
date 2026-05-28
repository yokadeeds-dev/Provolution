# PS 3.0 Routing — D17a + B-neu/B13 SEC-J-Vollberechnung

**Datum:** 2026-05-28 spät-Nacht
**Routed an:** Gemini PS 3.0 (Probatio Systemica 3.0)
**Anlass:** PF-Report v1.0.1 (AUTO-INTEGRATE) E4 — vier Kandidaten mit ausstehender SEC-Score-Vollberechnung; I35/I36 werden vom User selbst gesichtet, D17a + B-neu/B13 werden hiermit geroutet
**Worker-Session-Verantwortlich:** Tobias mit Claude Opus 4.7 (Code-Session, 1M-Kontext)
**Erwarteter Rückkanal:** SEC-J-Berechnung (S/E/C/J einzeln + Aggregation + Promotion-Empfehlung) zurück ins Repo via Re-Import

---

## Routing-Trace

| Schritt | Status | Notiz |
|---|---|---|
| 1. PF-Audit-Befund identifiziert | ✅ 2026-05-28 | Drift-Item #14 in HEBEL_KATALOG |
| 2. User-Direktive "gerne routen" | ✅ 2026-05-28 spät | I35/36 bleibt beim User, D17a + B-neu zu PS 3.0 |
| 3. Routing-Prompt formuliert | ✅ 2026-05-28 spät | Paste-fertiger Block (siehe unten) |
| 4. Ins Clipboard geschrieben | siehe Worker-Session-Bestätigung | via `mcp__computer-use__write_clipboard` |
| 5. Gemini-Rückkanal eingearbeitet | ⏳ ausstehend | nach Eingang in AUTO_INTEGRATE_KANDIDATEN.md + HEBEL_KATALOG |

---

## Paste-fertiger Routing-Block (für Gemini PS 3.0)

```
PS 3.0 · Provolution-Kandidaten SEC-J-Vollberechnung
Datum: 2026-05-28
Trigger: PF-Report v1.0.1 (AUTO-INTEGRATE) E4 Datenlage

KONTEXT
Probatio-Familia-Methodik-Audit hat das Provolution-AUTO-INTEGRATE-Bündel am 2026-05-28 als TEILBESTANDEN klassifiziert; alle kritischen Ebenen E1/E3/E6/E8 ✅, drei nicht-kritische ⚠️ in E2/E4/E7. In E4 wurden vier Hebel-Kandidaten mit "SEC-Score: geschätzt"-Markierung identifiziert: D17a (Hanf-Mehrfachernte), B-neu (Lokale On-Demand-Fertigung — inzwischen als B13 promoviert), I35 (Aktive Geschwindigkeits-Regulation), I36 (Kreislauf-Schwere-Nfz). I35 und I36 werden vom Framework-Inhaber direkt gesichtet. D17a und B-neu/B13 werden hiermit an PS 3.0 zur SEC-J-Vollberechnung geroutet.

Bestehende geschätzte SEC-Scores: D17a 0.85, B-neu/B13 0.83.
B-neu wurde 2026-05-27 als B13 LOKALE ON-DEMAND-FERTIGUNG in Band 4 v4.2 promoviert (band4-canonical). Die SEC-Berechnung dient hier zur Validierung des bestehenden 0.83-Werts.
D17a ist als Sub-Notiz innerhalb D17 dokumentiert; die SEC-Berechnung soll die Promotion-Empfehlung (eigener Hebel vs. Sub-Notiz) abschließen.

ANFRAGE
Für beide Kandidaten:
1. SEC-S (Sufficient) — Score 0..1 + 1 Satz Begründung (Beitrag zur Hinreichendheit)
2. SEC-E (Efficient) — Score 0..1 + 1 Satz Begründung (Ressourcen-Effizienz, ROI)
3. SEC-C (Consistent) — Score 0..1 + 1 Satz Begründung (Konsistenz mit anderen Hebeln, kein Doppel-Counting)
4. SEC-J (Just) — Score 0..1 + 1 Satz Begründung (Verteilung Lasten/Nutzen, Eigentumsstruktur, Risiken)
5. SEC-Total: arithmetisches Mittel + Methodik-Notiz, falls Gewichtung
6. Promotion-Empfehlung: D17a eigener Hebel vs. Sub-Notiz; B13 SEC-Validierung des bestehenden 0.83 (bestätigt/korrigiert/Bandbreite)

Output paste-fertig für Re-Import ins Provolution-Repo. Bitte deutsche Sprache.

──────────────────────────────────
KANDIDAT 1 — D17a · Hanf-Mehrfachernte
──────────────────────────────────

Bisher geschätzt: SEC 0.85 | CO₂: Multiplikator zu D17, ×2–3 pro Hektar/Jahr

Industriehanf hat einen Wachstumszyklus von 90–120 Tagen. In milden Klimazonen sind dadurch 2 bis 3 Ernten pro Jahr auf derselben Fläche möglich. Die CO₂-Bindung skaliert annähernd linear: aus den 9–15 t CO₂/ha/Ernte werden 18–45 t CO₂/ha/Jahr. Dadurch sinkt der globale Flächenbedarf für vollständigen Plastik-Ersatz drastisch — von 110–256 Mio. ha (1 Ernte/Jahr) auf 37–85 Mio. ha (3 Ernten/Jahr).

Abgrenzung zu D17 (Hanf-Anbau): D17 ist der Anbau-Hebel generell; D17a wäre die Anbau-Intensivierung über Mehrfachernten in geeigneten Klimazonen. Kein eigenständiger Hebel im klassischen Sinn, sondern ein Multiplikator-Faktor.

SEC-J-relevante offene Punkte:
- Klima-Beschränkung: in welchen Vegetationszonen sind 2–3 Ernten realistisch?
- Wasser- und Bodenbilanz bei Intensivierung — vermeidet die Mehrfachernte den Bodenregenerations-Effekt von D17?
- Eigentumsstruktur: Intensiv-Mehrfachernte könnte industrielle Großbetriebe gegenüber Kleinbauern bevorzugen
- Pestizid-/Düngerzwang bei 2–3 Ernten? Bisher D17 als Regen-LW-Komplement gerechnet — wenn Intensivierung Pestizide nötig macht, kollidiert das mit der C-Dimension

Bisherige Empfehlung im Repo: Sub-Notiz in D17 ergänzen, nicht eigener Hebel.

──────────────────────────────────
KANDIDAT 2 — B-neu / B13 · Lokale On-Demand-Fertigung mit Bio-Filamenten
──────────────────────────────────

Bisher geschätzt: SEC 0.83 | CO₂: −0.2 bis −0.5 Gt/Jahr (konservativ −0.3 als YAML-Wert)
Status: 2026-05-27 als B13 LOKALE ON-DEMAND-FERTIGUNG in Band 4 v4.2 promoviert (band4-canonical), YAML v1.3 ergänzt.

Hanf-basierte Biopolymere werden zu 3D-Druck-Filamenten verarbeitet und in regionalen Cluster-Fabriken vorgehalten. Produkte werden bedarfsgerecht und lokal hergestellt, statt zentral massenproduziert und global verschifft. Drei Effekte greifen ineinander:
1. Vermeidung globaler Container-Schifffahrt (Containersektor 2024: ca. 240 Mio. t CO₂/Jahr) für einen Teil der Massen-Standardware
2. Vermeidung von Überproduktion und Lagerhaltung durch On-Demand-Fertigung
3. Verkürzung der Material-Wege vom Hanf-Acker zur Fertigung zum Endverbraucher

Abgrenzung zu B07 (Kreislaufwirtschaft) und B08 (Biopolymere): B07 = Kreislauffähigkeit eines Materials. B08 = Hanf-Cellulose als Kunststoff-Ersatz. B13 adressiert die Fertigungs-Geografie und -Zeitlichkeit — nicht *was* das Material ist, sondern *wo* und *wann* es zum Produkt wird. Komplement zu B07/B08, kein Overlap.

SEC-J-relevante offene Punkte:
- Eigentumsstruktur regionaler Cluster-Fabriken: Genossenschaft / Privat / Öffentlich-Privat-Partnerschaft?
- 3D-Druck-Reife: für welche Produktklassen heute praxistauglich? (Bewertung der E-Dimension)
- Übergang aus globaler Container-Schifffahrt: Just-Transition für die heutigen Wertschöpfungs-Akteure (Hafen-Arbeitsplätze etc.)?
- Material-Pfad Hanf-Acker → Cluster: braucht es regionale Aufbereitungs-Infrastruktur (regionaler J-Aspekt)?

──────────────────────────────────
QUELLEN ZUM CROSSCHECK
──────────────────────────────────
- SEC-J-Spec: `06_CANON/SECJ_SPEC_v1.0.md` und `06_CANON/01_Band1_SEC_Kanon.md`
- Band 4 v4.2 D-Domain (D17 mit D17a Sub-Notiz Sektion 9) + B-Domain (B13)
- HEBEL_KATALOG v1.5 (Drift-Item #14 zum PF-Audit)
- AUTO_INTEGRATE_KANDIDATEN.md Kategorie D ✅ INTEGRIERT 2026-05-27
```

---

## Re-Import-Plan (für Worker-Session bei Rückkanal)

Wenn die Gemini-PS-3.0-Berechnung zurückkommt:

1. SEC-J-Werte in `08_INDEX/AUTO_INTEGRATE_KANDIDATEN.md` Kategorie D einpflegen — "geschätzt"-Markierungen durch ✅ vollberechnet ersetzen
2. Bei D17a: Promotion-Empfehlung der PS 3.0 dokumentieren (Sub-Notiz vs. eigener Hebel) — wenn eigener Hebel-Vorschlag, in HEBEL_KATALOG D-Domain ergänzen
3. Bei B13: SEC 0.83 validieren — bei Abweichung > 0.05 ggf. in `co2_master.yaml` Wert anpassen
4. PF-Report-Adressierung E4 als ✅ adressiert markieren in HEBEL_KATALOG Drift-Item #14
5. Cross-Refs: B13/D17a in Band 4 v4.2 mit Validierungs-Hinweis ergänzen

---

*Routing-Trace angelegt 2026-05-28 spät-Nacht — Cross-Session-Kommunikations-Pattern via Repo (Multi-Session-Rollen-Trennung)*
