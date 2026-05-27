# PROBATIO SYSTEMICA

## Band 2 – Entscheidungskarte
### Framework-Ebene (neutral, mathematisch, deskriptiv)

**Version:** 2.0
**Datum:** 2026-01-18
**Status:** Kanonisch

---

## VORBEMERKUNG

Dieses Dokument definiert die **Entscheidungskarte** von Probatio Systemica – ein systematisches Verfahren zur Entscheidungsfindung basierend auf dem SEC-Prinzip.

**Die Entscheidungskarte ist:**
- Ein neutrales Werkzeug (W2 aus dem Werkzeugkasten)
- Mathematisch fundiert (basiert auf SEC-Logik)
- Kontextunabhängig (für beliebige Anwendungen nutzbar)

**Die Entscheidungskarte ist NICHT:**
- Ein normatives Programm (sagt nicht WAS entschieden werden soll)
- Spezifisch für eine Anwendung
- Ein Ersatz für menschliches Urteilsvermögen

**Anwendung siehe:** PROVOLUTION (Band 4-5)

**Cross-Referenz:** Band 1 (SEC-Kanon), MASTERDOKUMENT v2.0

---

## 1. ZWECK DER ENTSCHEIDUNGSKARTE

### 1.1 Problemstellung

Komplexe Systeme erfordern kontinuierliche Entscheidungen:
- Welche Maßnahme soll implementiert werden?
- Soll eine laufende Maßnahme fortgeführt werden?
- Wann soll eine Maßnahme abgebrochen werden?

**Herausforderung:**
Ohne systematisches Verfahren werden Entscheidungen:
- Inkonsistent (mal so, mal so)
- Subjektiv (nach Bauchgefühl)
- Nicht nachvollziehbar (warum wurde so entschieden?)

---

### 1.2 Lösung: Entscheidungskarte

Die **Entscheidungskarte** bietet:
- **Systematik:** Klare Kriterien für jede Entscheidung
- **Objektivität:** Basierend auf SEC-Verifikation
- **Nachvollziehbarkeit:** Jede Entscheidung ist dokumentiert

**Kernprinzip:**
> Entscheidungen werden ausschließlich auf Basis bestandener SEC-Tests getroffen.

---

## 2. GRUNDSTRUKTUR

Die Entscheidungskarte verwendet eine **3-Zustands-Logik**:

### Zustand 1: ZULÄSSIG ✅
Maßnahme darf implementiert werden.

**Bedingung:**
```
Probatio(M) = TRUE
```

Das bedeutet:
- Sufficient(M) = TRUE (Wirkung ausreichend)
- Efficient(M) = TRUE (Ressourcen-optimal)
- Consistent(M) = TRUE (keine Widersprüche)

---

### Zustand 2: FORTFÜHRBAR 🔄
Laufende Maßnahme darf weiterlaufen.

**Bedingung:**
```
W(M)_gemessen ≥ W_min ∧ Consistent(M) = TRUE
```

Das bedeutet:
- Maßnahme erreicht weiterhin Mindestwirkung
- Maßnahme erzeugt keine neuen Widersprüche
- (Efficiency kann sich verändern, ist aber nicht Abbruchkriterium)

---

### Zustand 3: ABZUBRECHEN ⛔
Maßnahme muss gestoppt werden.

**Bedingungen (mindestens eine erfüllt):**
```
W(M)_gemessen < W_min  (Wirkung unzureichend)
ODER
Consistent(M) = FALSE  (Widersprüche entstanden)
ODER
R(M) > R_max           (Ressourcen-Grenze überschritten)
```

---

## 3. ENTSCHEIDUNGSMATRIX

### 3.1 Neue Maßnahme implementieren?

**INPUT:** Vorgeschlagene Maßnahme M

**PROZESS:**
1. Probatio(M) durchführen
2. Ergebnis auswerten

**OUTPUT:**

| Probatio(M) | Entscheidung | Aktion |
|-------------|--------------|--------|
| TRUE ✅ | ZULÄSSIG | M implementieren |
| FALSE ⛔ | NICHT ZULÄSSIG | M verwerfen oder modifizieren |

**Hinweis:**
Bei FALSE analysieren, welcher SEC-Test fehlgeschlagen ist:
- Insufficient → M verstärken oder Ziel reduzieren
- Inefficient → M optimieren
- Inconsistent → M umgestalten oder andere Maßnahmen anpassen

---

### 3.2 Laufende Maßnahme fortführen?

**INPUT:** Laufende Maßnahme M mit gemessener Wirkung W(M)_gemessen

**PROZESS:**
1. W(M)_gemessen ≥ W_min?
2. Consistent(M) = TRUE?
3. R(M) ≤ R_max?

**OUTPUT:**

| W ≥ W_min | Consistent | R ≤ R_max | Entscheidung | Aktion |
|-----------|------------|-----------|--------------|--------|
| ✅ | ✅ | ✅ | FORTFÜHRBAR | M weiterlaufen lassen |
| ❌ | - | - | ABBRECHEN | M stoppen (Wirkung zu gering) |
| ✅ | ❌ | - | ABBRECHEN | M stoppen (Widersprüche) |
| ✅ | ✅ | ❌ | ABBRECHEN | M stoppen (Ressourcen-Limit) |

---

### 3.3 Maßnahme anpassen?

**INPUT:** Laufende Maßnahme M, die FORTFÜHRBAR ist, aber suboptimal

**PROZESS:**
1. Ist M noch optimal bezüglich Efficiency?
2. Gibt es bessere Alternative M'?

**OUTPUT:**

| Efficiency optimal | Bessere Alternative M' existiert | Entscheidung | Aktion |
|-------------------|----------------------------------|--------------|--------|
| ✅ | ❌ | BEIBEHALTEN | M unverändert lassen |
| ❌ | ✅ mit Probatio(M')=TRUE | ERSETZEN | M durch M' ersetzen |
| ❌ | ❌ oder Probatio(M')=FALSE | OPTIMIEREN | M verbessern, nicht ersetzen |

---

## 4. PRIORITÄTSMATRIX

### 4.1 Multiple Maßnahmen priorisieren

**Problem:**
Mehrere Maßnahmen sind ZULÄSSIG (Probatio = TRUE), aber Ressourcen sind begrenzt. Welche zuerst?

**Lösung: SEC-Score**

Jede Maßnahme M erhält einen Score:

```
SEC-Score(M) = α·S(M) + β·E(M) + γ·C(M)
```

Wo:
- S(M) = Sufficiency-Grad (W(M) / W_min, normiert 0-1)
- E(M) = Efficiency-Grad (1 - R(M)/R_max, normiert 0-1)
- C(M) = Consistency-Grad (1 wenn konsistent, 0 sonst)
- α, β, γ = Gewichtungsfaktoren (α + β + γ = 1)

**Standard-Gewichtung (neutral):**
α = β = γ = 1/3 (alle gleichwertig)

**Priorisierung:**
Sortiere Maßnahmen nach SEC-Score absteigend.
Implementiere zuerst die mit höchstem Score.

---

### 4.2 Gewichtung anpassen (Anwendungskontext)

**Im Framework (Probatio Systemica):**
Standardgewichtung α = β = γ = 1/3

**In Anwendungen (z.B. Provolution):**
Gewichtung kann angepasst werden:
- Klima-Dringlichkeit → α erhöhen (Sufficiency wichtiger)
- Ressourcen-Knappheit → β erhöhen (Efficiency wichtiger)
- Systemstabilität → γ erhöhen (Consistency wichtiger)

**Beispiel:**
In Provolution könnte gelten: α = 0.5, β = 0.3, γ = 0.2
(Wirkung wichtiger als Effizienz, da Zeit drängt)

---

## 5. RISIKOABSCHÄTZUNG

### 5.1 Unsicherheit berücksichtigen

**Problem:**
Wirkung W(M) und Ressourcen R(M) sind oft nur Schätzungen, keine Sicherheiten.

**Lösung: Konfidenzintervalle**

Statt Punktschätzung:
```
W(M) = 100 kg CO₂
```

Verwende Intervall:
```
W(M) = [80, 120] kg CO₂  (95% Konfidenz)
```

**Entscheidungsregel:**
```
W(M)_worst_case ≥ W_min  (pessimistischer Fall muss ausreichen)
```

Das bedeutet:
- Bei W(M) = [80, 120] und W_min = 100 → NICHT ausreichend
- Bei W(M) = [100, 140] und W_min = 100 → ausreichend

---

### 5.2 Risiko-Kategorien

**Niedrig-Risiko:**
- W(M) gut bekannt (kleine Konfidenzintervalle)
- R(M) gut kontrollierbar
- Consistent sicher

**Mittel-Risiko:**
- W(M) mit Unsicherheit (größere Intervalle)
- R(M) variabel
- Consistency geprüft, aber Nebenwirkungen möglich

**Hoch-Risiko:**
- W(M) sehr unsicher
- R(M) schwer vorhersagbar
- Consistency fraglich

**Entscheidungsregel:**
Bei Hoch-Risiko: Erst Pilotprojekt (klein, reversibel), dann skalieren.

---

## 6. SZENARIEN-VERGLEICH

### 6.1 Mehrere Pfade vergleichen

**Problem:**
Verschiedene Maßnahmen-Kombinationen führen zu verschiedenen Zukunftsszenarien. Welches ist optimal?

**Lösung: Szenario-Analyse**

**Schritt 1: Szenarien definieren**
- Szenario A: Maßnahmen M1, M2, M3
- Szenario B: Maßnahmen M4, M5
- Szenario C: Maßnahmen M1, M5, M6

**Schritt 2: Bewerten**
Für jedes Szenario:
```
W_total = Σ W(M_i)  (Gesamtwirkung)
R_total = Σ R(M_i)  (Gesamtressourcen)
Consistent = alle M_i konsistent untereinander?
```

**Schritt 3: Vergleichen**

| Szenario | W_total | R_total | Consistent | SEC-Score |
|----------|---------|---------|------------|-----------|
| A | 500 | 100 | ✅ | 0.85 |
| B | 400 | 60 | ✅ | 0.78 |
| C | 450 | 90 | ❌ | 0.00 |

**Entscheidung:**
Wähle Szenario mit höchstem SEC-Score (hier: A).

---

### 6.2 Trade-offs sichtbar machen

Szenarien-Vergleich zeigt Trade-offs:
- Szenario A: Mehr Wirkung, mehr Ressourcen
- Szenario B: Weniger Wirkung, weniger Ressourcen

**Entscheidung hängt ab von:**
- Ist W_min erreicht? (dann B möglich)
- Sind Ressourcen begrenzt? (dann B bevorzugen)
- Ist Dringlichkeit hoch? (dann A bevorzugen)

**Wichtig:**
Entscheidungskarte gibt Struktur, nicht die Antwort.
Kontext bestimmt Gewichtung.

---

## 7. FALLBEISPIELE (neutral)

### 7.1 Neue Maßnahme

**Vorschlag:** M = "CO₂-Speicherung durch Baumpflanzung"

**Probatio-Test:**
- W_min = 100 kg CO₂/Jahr
- W(M)_geschätzt = 150 kg CO₂/Jahr → Sufficient ✅
- R(M) = 50 EUR, minimal unter Alternativen → Efficient ✅
- Keine Konflikte mit anderen Maßnahmen → Consistent ✅

**Entscheidung:** ZULÄSSIG ✅ → M implementieren

---

### 7.2 Laufende Maßnahme

**Maßnahme:** M = "Windkraftwerk betreiben"

**Messung nach 1 Jahr:**
- W(M)_gemessen = 80 kg CO₂-Einsparung/Jahr
- W_min = 100 kg CO₂-Einsparung/Jahr
- W(M) < W_min ❌

**Entscheidung:** ABBRECHEN ⛔
(Oder: Maßnahme verstärken, z.B. zweites Windrad hinzufügen)

---

### 7.3 Priorisierung

**Drei Maßnahmen, alle ZULÄSSIG:**
- M1: W=200, R=100, SEC-Score=0.75
- M2: W=150, R=50, SEC-Score=0.85
- M3: W=180, R=80, SEC-Score=0.80

**Reihenfolge (nach SEC-Score):**
1. M2 (0.85) ← zuerst
2. M3 (0.80)
3. M1 (0.75)

---

## 8. WERKZEUGE & IMPLEMENTATION

### 8.1 Checkliste für Entscheidungen

**Vor Implementation (neue Maßnahme):**
- [ ] W_min definiert?
- [ ] W(M) geschätzt?
- [ ] Sufficiency-Test bestanden? (W ≥ W_min)
- [ ] R(M) bekannt?
- [ ] Efficiency-Test bestanden? (R minimal)
- [ ] Konsistenz geprüft? (keine Konflikte)
- [ ] Probatio(M) = TRUE?

**Bei laufender Maßnahme (Fortführung):**
- [ ] W(M)_gemessen bekannt?
- [ ] W(M) ≥ W_min? (noch ausreichend)
- [ ] Consistency noch gegeben? (keine neuen Konflikte)
- [ ] R(M) ≤ R_max? (Ressourcen-Limit nicht überschritten)

**Siehe:** Provolution-Checkliste (Band 5) für anwendungsspezifische Version.

---

### 8.2 Software-Tools (optional)

Die Entscheidungskarte kann in Software implementiert werden:

**Eingaben:**
- Maßnahmen-Datenbank (M, W(M), R(M))
- SEC-Kriterien (W_min, R_max)
- Konsistenz-Regeln

**Prozess:**
- Automatischer Probatio-Test
- SEC-Score-Berechnung
- Priorisierung

**Ausgabe:**
- Liste zulässiger Maßnahmen (sortiert nach Score)
- Abbruch-Empfehlungen für laufende Maßnahmen
- Szenarien-Vergleich

**Vorteil:**
- Schnell
- Konsistent
- Skalierbar (viele Maßnahmen parallel)

---

## 9. GRENZEN DER ENTSCHEIDUNGSKARTE

### 9.1 Was die Karte NICHT leistet

**Keine Zielvorgabe:**
Die Karte sagt nicht, WAS erreicht werden soll (W_min).
Das kommt aus dem Anwendungskontext (z.B. Provolution).

**Keine Wertentscheidung:**
Die Karte sagt nicht, WELCHE Ziele wichtiger sind.
Das ist eine normative Entscheidung (außerhalb des Frameworks).

**Keine Garantie:**
Die Karte kann nur bewerten, ob Maßnahmen theoretisch funktionieren.
Praktische Umsetzung kann scheitern (Implementierungsfehler).

---

### 9.2 Voraussetzungen

Die Entscheidungskarte funktioniert nur, wenn:
- W(M) messbar ist (Wirkung quantifizierbar)
- R(M) bekannt ist (Ressourcen klar)
- Konsistenz prüfbar ist (Wechselwirkungen verstanden)

Fehlen diese: Karte liefert keine verlässlichen Ergebnisse.

---

## 10. CROSS-REFERENZEN

**CANON-Module:**
- Band 1 (SEC-Kanon) – SEC-Prinzip im Detail
- Band 3 (Scientific Core) – Mathematische Grundlagen

**MASTERDOKUMENT:**
- MASTERDOKUMENT_v2.0.md – Teil II, Abschnitt 2.3 (Werkzeugkasten)

**Anwendung:**
- Band 5 (Provolution Steuerung & Score) – Anwendung der Entscheidungskarte
- provolution_checkliste_anwendung_band_5_sec.md – Praktische Checkliste

**Terminologie:**
- TERMINOLOGY_CHANGELOG.md – Framework vs. Anwendung
- GLOSSARY.md – Definitionen

---

## 11. VERSIONSGESCHICHTE

**v2.0 (2026-01-18):**
- Umbenennung: "Provolution" → "Probatio Systemica" (Framework-Ebene)
- Vollständige Ausarbeitung (statt Platzhalter)
- 3-Zustands-Logik (Zulässig, Fortführbar, Abzubrechen)
- SEC-Score-System für Priorisierung
- Risikoabschätzung integriert
- Szenarien-Vergleich
- Fallbeispiele (neutral)
- Cross-Referenzen

**v1.0 (ursprünglich):**
- Platzhalter-Dokument

---

## 12. SCHLUSS

Die **Entscheidungskarte** ist ein systematisches Werkzeug zur Entscheidungsfindung auf Basis des SEC-Prinzips.

Sie bietet:
- **Klarheit:** Jede Entscheidung hat klare Kriterien
- **Objektivität:** Basierend auf Probatio-Verifikation
- **Nachvollziehbarkeit:** Jede Entscheidung ist dokumentiert

Sie ersetzt NICHT:
- Menschliches Urteilsvermögen
- Normative Zielvorgaben
- Praktische Implementation

**Die Entscheidungskarte ist neutral.**
**Sie sagt WIE entschieden wird, nicht WAS.**

Das WAS kommt aus der Anwendung (z.B. Provolution).

**Auf zum nächsten Band.**

---

---

## SUBMODUL: Probatio Veritatis (PV)

Die SEC-J-Prüflogik ist nicht auf Maßnahmen beschränkt. Als Submodul **Probatio Veritatis (PV)** wird dasselbe Framework auf die Verifikation faktischer Behauptungen angewendet. PV übernimmt die vier Dimensionen S, E, C, J sowie den Veto-Mechanismus unverändert; es adaptiert lediglich die Eingabeoperationalisierung (Claim-Taxonomie CL-1 bis CL-4) und die Quellenlogik (empirisch statt normativ).

**Kernunterschied:** PS-U bewertet Maßnahmen. PV bewertet Behauptungen über die Welt.

**Gewichtungsformel:** `PV(c) = (0,30 × S) + (0,20 × E) + (0,35 × C) + (0,15 × J)`

C erhält das höchste Gewicht (0,35), da Widerspruchsfreiheit mit gesichertem Wissen die härteste Bedingung faktischer Haltbarkeit ist.

→ Vollständige Spezifikation: `06_CANON/07_Probatio_Veritatis_v1.0.md`

---

**Version:** 2.0
**Status:** Kanonisch
**Datum:** 2026-01-18

**Ende von Band 2 – Entscheidungskarte**

(Quelle: Konsolidiert aus MASTERDOKUMENT v2.0, Band 1 SEC-Kanon)

---

## SUBMODUL: Probatio Institutionalis (PI)

**Probatio Institutionalis (PI)** überträgt die SEC-J-Logik auf Institutionen. PI beantwortet nicht ob eine Maßnahme wirksam oder eine Behauptung wahr ist, sondern: **Tut diese Institution was sie sagt?**

**Kernwerkzeug:** Gap-Analyse zwischen erklärtem Anspruch (S) und nachweisbarem Output (C).

**Gewichtungsformel:** `PI(i) = (0,25 × S) + (0,20 × E) + (0,25 × C) + (0,30 × J)`

J erhält das höchste Gewicht der PS-Familie (0,30), da institutionelle Macht strukturell Ungleichheit produziert. Keine Abbruchlogik – alle Dimensionen werden immer bewertet.

Flags: C < 0,40 → STRUKTURELLES UMSETZUNGSDEFIZIT · J < 0,40 → STRUKTURELLE UNGERECHTIGKEIT

Verdict-Sprache: INTEGER / BEDINGT INTEGER / DEFIZITÄR / NICHT INTEGER

→ Vollständige Spezifikation: `06_CANON/12_Probatio_Institutionalis_v1.0.md`