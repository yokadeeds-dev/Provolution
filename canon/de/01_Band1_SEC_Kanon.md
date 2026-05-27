# PROBATIO SYSTEMICA

## Band 1 – SEC-J-Kanon
### Framework-Ebene (neutral, mathematisch, deskriptiv)

**Version:** 2.2
**Datum:** 2026-05-09
**Status:** Kanonisch

---

## VORBEMERKUNG

Dieses Dokument definiert **Probatio Systemica** – das mathematisch fundierte Framework zur systemischen Verifikation. Es ist die **Framework-Ebene** des Gesamtprojekts und bleibt bewusst neutral, objektiv und wertfrei.

**Probatio Systemica ist:**
- Ein dauerhaft justierbares System, das sich selbst begrenzt, selbst verbessert und selbst überprüft
- Ein Werkzeugkasten aus Prinzipien, Regeln und Anwendungen
- Mathematisch fundiert, kulturunabhängig, universell anwendbar

**Probatio Systemica ist NICHT:**
- Eine Ideologie oder Heilsversprechen
- Ein Zielzustand oder normatives Programm
- Spezifisch für eine Anwendung

**Anwendung siehe:** PROVOLUTION (Band 4-5) – die konkrete, zielgerichtete Implementierung für Klimatransformation.

**Cross-Referenz:** MASTERDOKUMENT v2.0, TERMINOLOGY_CHANGELOG.md

---

## 1. DEFINITION: PROBATIO SYSTEMICA

### 1.1 Kernkonzept

**Probatio Systemica** (von lat. *probatio* = Beweis, Prüfung; *systemica* = systemisch) ist ein Framework zur **Verifikation systemischer Maßnahmen** durch das SEC-J-Prinzip.

**Aus Kipppunkt-Analyse (Msg #1964):**
> "Kein Zielzustand, sondern ein dauerhaft justierbares System, das sich selbst begrenzt, selbst verbessert und selbst überprüft."

**Erweiterte Definition:**
> "Der Weg dorthin. Kein Versprechen, keine Ideologie, sondern ein Werkzeugkasten aus Prinzipien, Regeln und Anwendungen."

---

### 1.2 Charakteristika

**Neutral & Deskriptiv:**
- Keine Werturteile oder Zielvorgaben
- Beschreibt WAS möglich ist, nicht WAS sein SOLL
- Objektiv messbar und verifizierbar

**Mathematisch Fundiert:**
- SEC-J-Prinzip formalisiert (∀, ∃, Logik)
- Probatio-Logik als Verifikationsverfahren
- Vorhersagekraft durch Präzision

**Universell Anwendbar:**
- Nicht kulturgebunden
- Basiert auf physikalischen Realitäten
- Für verschiedene Kontexte nutzbar

---

## 2. SEC-J-PRINZIP (Super Ebenen Check)

Das **SEC-J-Prinzip** ist das Herzstück von Probatio Systemica. Es definiert vier Bedingungen, die jede Maßnahme erfüllen muss.

### 2.1 S – SUFFICIENT (Ausreichend)

**Definition:**
Jede Maßnahme muss hinreichend sein, um die definierte Wirkung zu erzielen.

**Mathematisch:**
```
∀ M ∈ Maßnahmen: W(M) ≥ W_min
```

Wo:
- M = Maßnahme
- W(M) = Wirkung der Maßnahme M
- W_min = Minimale erforderliche Wirkung

**Bedeutung:**
Eine Maßnahme, die das Ziel nicht erreicht, ist nutzlos – egal wie effizient oder konsistent sie ist.

**Beispiel (neutral):**
- Maßnahme: "10kg CO₂ speichern"
- W_min: "100kg CO₂ speichern"
- → Maßnahme ist NICHT sufficient (W(M) < W_min)

---

### 2.2 E – EFFICIENT (Effizient)

**Definition:**
Jede Maßnahme minimiert Ressourcenverbrauch bei gegebener Wirkung.

**Mathematisch:**
```
min(R(M)) unter der Nebenbedingung W(M) ≥ W_min
```

Wo:
- R(M) = Ressourcenverbrauch der Maßnahme M
- Optimierung erfolgt nur bei ausreichender Wirkung

**Bedeutung:**
Von allen Maßnahmen, die ausreichend sind (S), wähle die ressourcen-sparsamste.

**Beispiel (neutral):**
- Maßnahme A: 100kg CO₂ speichern mit 10 Einheiten Ressource
- Maßnahme B: 100kg CO₂ speichern mit 5 Einheiten Ressource
- → B ist effizienter (weniger R bei gleichem W)

---

### 2.3 C – CONSISTENT (Konsistent)

**Definition:**
Keine Maßnahme darf systemische Widersprüche erzeugen oder mit anderen Maßnahmen kollidieren.

**Mathematisch:**
```
∀ M_i, M_j ∈ Maßnahmen: ¬(M_i ⊥ M_j)
```

Wo:
- M_i ⊥ M_j = Maßnahmen widersprechen sich
- System bleibt in sich widerspruchsfrei

**Bedeutung:**
Eine Maßnahme darf nicht zerstören, was andere aufbauen. Das Gesamtsystem muss kohärent bleiben.

**Beispiel (neutral):**
- Maßnahme A: "Wald aufforsten" (CO₂-Speicherung)
- Maßnahme B: "Selben Wald für Bauholz nutzen"
- → Widerspruch (M_A ⊥ M_B), nicht konsistent

---

### 2.4 J – JUST (Gerecht)

**Definition:**
Jede Maßnahme muss eine verteilungsgerechte Wirkung erzielen. Maßnahmen,
die bestehende Ungleichheiten strukturell verstärken, erfüllen das J-Kriterium nicht.

**Mathematisch:**
```
∀ M ∈ Maßnahmen: J(M) ≥ J_min
```

Wo:
- J(M) = Distributiver Gerechtigkeitsscore der Maßnahme M ∈ [0, 1]
- J(M) = ( equity_score(M) + 1 ) / 2,  equity_score(M) ∈ [−1, +1]
- J_min = Anwendungsspezifischer Mindestwert (in Provolution: J_min = 0.50)

**Bedeutung:**
Eine Maßnahme, die Ungleichheit strukturell verstärkt (J(M) < J_min), kann nicht
probiert werden – unabhängig davon, ob sie sufficient, efficient und consistent ist.

**Beispiel (formal):**
- Maßnahme A: Lasten und Nutzen gleichmäßig über alle Gruppen verteilt
  → equity_score(A) > 0  →  J(A) > 0.50  ✅
- Maßnahme B: Lasten bei einkommensschwachen, Nutzen bei einkommensstarken Gruppen
  → equity_score(B) < 0  →  J(B) < 0.50  ❌

Der equity_score wird empirisch gemessen. Operationalisierung und
Mess-Methode siehe `20_CANON/data/README_MULTI_IMPACT.md`.

**Anwendungsspezifisch:**
J_min wird vom Anwender festgelegt.
Provolution setzt J_min = 0.50 (J-Veto-Regel).
Siehe: `06_CANON/SECJ_SPEC_v1.0.md`

---

## 3. PROBATIO-LOGIK (Verifikation)

### 3.1 Definition

**Probatio** ist das Verfahren zur Verifikation, dass eine Maßnahme SEC-J-konform ist.

**Formalisierung:**
```
Probatio(M) = Sufficient(M) ∧ Efficient(M) ∧ Consistent(M) ∧ Just(M)

Wenn Probatio(M) = TRUE → M ist probiert (verifiziert)
Wenn Probatio(M) = FALSE → M wird verworfen oder modifiziert
```

---

### 3.2 Prozess

**Schritt 1: Hypothese**
Eine Maßnahme M wird vorgeschlagen.

**Schritt 2: Sufficiency-Test**
- Frage: Erreicht M die Mindest-Wirkung W_min?
- Test: W(M) ≥ W_min?
- Ergebnis: JA → weiter zu Schritt 3 | NEIN → M verwerfen

**Schritt 3: Efficiency-Test**
- Frage: Ist M ressourcen-optimal?
- Test: R(M) minimal unter allen M mit W(M) ≥ W_min?
- Ergebnis: JA → weiter zu Schritt 4 | NEIN → M optimieren

**Schritt 4: Consistency-Test**
- Frage: Erzeugt M Widersprüche mit anderen Maßnahmen?
- Test: ∃ M_j: M ⊥ M_j?
- Ergebnis: NEIN → weiter zu Schritt 5 | JA → M modifizieren

**Schritt 5: Justice-Test**
- Frage: Ist die Verteilungswirkung von M gerecht?
- Test: J(M) ≥ J_min?
- Ergebnis: JA → M probiert ✅ | NEIN → M verwerfen oder grundlegend neu konzipieren (J-Versagen ist strukturell)

**Schritt 6: Resultat**
- M ist **probiert** (verifiziert) → kann implementiert werden
- M ist **nicht probiert** → zurück zu Schritt 1 (modifizieren)

---

### 3.3 Gültigkeitsregel

**Kanonische Regel:**
> Jede Aussage oder Maßnahme ist nur gültig, wenn sie einen expliziten SEC-J-Nachweis enthält.

**Das bedeutet:**
- Keine Maßnahme ohne Probatio
- Kein "Hoffen", sondern "Wissen"
- Mathematische Präzision = Vorhersagekraft

---

## 4. NULLPUNKT-PRINZIP

### 4.1 Definition

Das **Nullpunkt-Prinzip** besagt:
> Jede Veränderung beginnt beim IST-Zustand (Nullpunkt), nicht bei einem idealisierten Wunschzustand.

**Bedeutung:**
- Wahrnehmen, was IST (nicht, was sein sollte)
- Realistische Ausgangslage
- Keine Utopien als Startpunkt

---

### 4.2 Anwendung

**Schritt 1: IST-Analyse**
Unverzerrte Beobachtung des aktuellen Systemzustands.

**Schritt 2: Abweichung messen**
Differenz zwischen IST und SOLL (falls SOLL definiert ist in Anwendungskontext).

**Schritt 3: Maßnahmen ableiten**
Von IST ausgehend, nicht von idealem Zielzustand.

**Wichtig:** Im Framework selbst gibt es kein SOLL – das kommt erst in der Anwendung (z.B. Provolution).

---

## 5. FALSIFIKATION & SELBSTKORREKTUR

### 5.1 Falsifikationsprinzip

Probatio Systemica ist **falsifizierbar**:
- Jede Aussage kann widerlegt werden
- Widerlegung führt zu Revision
- Keine dogmatischen Wahrheiten

**Kriterium:**
> Wenn Maßnahme M implementiert wird und W(M) < W_min (trotz Probatio), dann war Probatio(M) falsch.

---

### 5.2 Selbstkorrektur

**Mechanismus:**
1. Maßnahme M wird implementiert
2. Wirkung W(M) wird gemessen
3. Wenn W(M) ≠ W_erwartet → Analyse warum
4. Probatio-Prozess wird angepasst
5. M wird modifiziert oder verworfen

**Lernendes System:**
Probatio Systemica verbessert sich durch Rückkopplung.

---

## 6. MISSBRAUCHSRESISTENZ

### 6.1 Schutz vor Manipulation

**Problem:**
Systeme können manipuliert werden, um vorgegebene Ergebnisse zu rechtfertigen.

**Lösung in Probatio Systemica:**

**Transparenz:**
- Alle Annahmen explizit
- Alle Berechnungen nachvollziehbar
- Alle Entscheidungen dokumentiert

**Objektivität:**
- Messbare Kriterien (W, R)
- Mathematisch prüfbar
- Nicht verhandelbar (TRUE or FALSE)

**Falsifikation:**
- Jede Aussage kann widerlegt werden
- Widerlegung ist erwünscht (verbessert System)
- Keine Immunisierung gegen Kritik

---

### 6.2 Grenzen

**Probatio Systemica schützt NICHT vor:**
- Bewusster Datenfälschung (W(M) falsch messen)
- Manipulation der Zielvorgaben (W_min willkürlich setzen)
- Politischem Missbrauch (System ignorieren)

**Das erfordert:**
- Integrität der Anwender
- Unabhängige Verifikation
- Offenheit der Daten

---

## 7. WERKZEUGKASTEN-KOMPONENTEN

Probatio Systemica stellt modulare Werkzeuge bereit:

### W1: Analysewerkzeuge
- Systemzustands-Erfassung (IST)
- Wirkungsketten-Analyse
- Abhängigkeiten identifizieren

### W2: Entscheidungswerkzeuge
- Prioritätsmatrix (nach SEC-J-Score)
- Risikoabschätzung
- Szenarien-Vergleich

### W3: Implementierungswerkzeuge
- Schrittweise Einführung (Pilotprojekte)
- Rückkopplungs-Messung
- Fehlerkorrektur-Prozeduren

### W4: Verifikationswerkzeuge
- SEC-J-Konformitäts-Test
- Konsistenz-Prüfung (keine Widersprüche)
- Wirksamkeits-Nachweis (W(M) messen)

**Siehe:** Band 2 (Entscheidungskarte) für Details.

---

## 8. ANWENDUNG: PROVOLUTION

**Probatio Systemica ist neutral.**
**Es kann für verschiedene Anwendungen genutzt werden.**

**Die erste und wichtigste Anwendung ist PROVOLUTION:**
- Konkrete Implementierung für Klimatransformation
- Normativ, zielgerichtet (Kipppunkt-Kompensation)
- Basiert auf diesem Framework

**Siehe:**
- Band 4: Provolution – Hebel
- Band 5: Provolution – Steuerung & Score
- MASTERDOKUMENT v2.0, Teil II

**Wichtig:**
Provolution ist EINE Anwendung. Probatio Systemica könnte auch für andere Kontexte genutzt werden (z.B. Stadtplanung, Unternehmensführung, Gesundheitssysteme).

---

## 9. CROSS-REFERENZEN

**Terminologie:**
- TERMINOLOGY_CHANGELOG.md – Trennung Probatio Systemica / Provolution
- GLOSSARY.md – Definitionen aller Begriffe

**CANON-Module:**
- 02_probatio_systemica_entscheidungskarte.md – Werkzeuge W2
- 03_probatio_systemica_scientific_core.md – Mathematische Grundlagen

**MASTERDOKUMENT:**
- MASTERDOKUMENT_v2.0.md – Teil II, Abschnitt 2 (Probatio Systemica)

**Anwendung:**
- 04_provolution_band4_anwendungen.md – Konkrete Umsetzung
- 05_provolution_band5_steuerung_und_score.md – SEC-Score-System

**Historischer Kontext:**
- KIPPPUNKT_ANALYSE.md – Nachweis des Wechsels bei Msg #1977
- Chat "Provolution Definition" – Ursprung der Konzepte

---

## 10. VERSIONSGESCHICHTE

**v2.2 (2026-05-09):**
- Notation `J(M)` / `J_min` konsolidiert mit SEC-J-Spec
  (vorher `D(M)` / `D_min` in Abschnitt 2.4 + 3.2 — Buchstaben-Drift
  gegen `06_CANON/SECJ_SPEC_v1.0.md`, Phase 6D-D.3+.a Drift-Harmonization)
- Versionsgeschichte v2.1 retrospektiv auf neue Notation aktualisiert

**v2.1 (2026-04-27):**
- SEC erweitert zu SEC-J: Justice als vierte Framework-Dimension
- Neuer Abschnitt 2.4 J – JUST (Gerecht) mit formaler Definition
- Probatio-Formel erweitert: ∧ Just(M)
- Probatio-Prozess: neuer Schritt 5 Justice-Test, Resultat → Schritt 6
- J-Versagen führt zu Verwerfung oder grundlegender Neukonzeption
- J(M) = (equity_score + 1) / 2, J_min anwendungsspezifisch
- Provolution: J_min = 0.50 (siehe `06_CANON/SECJ_SPEC_v1.0.md`)
- Alle SEC-Bezeichnungen → SEC-J

**v2.0 (2026-01-18):**
- Umbenennung: "Provolution" → "Probatio Systemica" (Framework-Ebene)
- Definition aus Kipppunkt-Analyse integriert
- SEC-Prinzip mathematisch formalisiert
- Probatio-Logik als Verifikationsverfahren
- Cross-Referenzen zu MASTERDOKUMENT v2.0
- Klarstellung: Framework vs. Anwendung (Provolution)

**v1.0 (ursprünglich):**
- Platzhalter-Dokument
- Verweis auf Canvas-Dokument

---

## 11. SCHLUSS

Probatio Systemica ist ein **mathematisch fundiertes, neutrales Framework** zur Verifikation systemischer Maßnahmen.

Es ist kein Zielzustand, sondern ein **Werkzeugkasten**.
Es ist keine Ideologie, sondern ein **Prüfverfahren**.
Es ist nicht dogmatisch, sondern **lernfähig**.

Die **Probatio-Logik** garantiert:
- Sufficient: Maßnahmen erreichen ihre Wirkung
- Efficient: Ressourcen werden optimal genutzt
- Consistent: Keine Widersprüche entstehen
- Just: Verteilungsgerechtigkeit ist gewährleistet

**Mathematische Präzision = Vorhersagekraft.**

Das Framework ist universell.
Die Anwendung (Provolution) ist spezifisch.

**Auf zum nächsten Band.**

---

**Version:** 2.2
**Status:** Kanonisch
**Datum:** 2026-05-09

**Ende von Band 1 – SEC-J-Kanon**

(Quelle: Konsolidiert aus MASTERDOKUMENT v2.0, TERMINOLOGY_CHANGELOG.md, Kipppunkt-Analyse)


---

## LICENSE

This work is released under:
- **CC0 1.0 Universal** (Public Domain)
- **Open Humanity License** (OHL)

See [LICENSE.md](../LICENSE.md) for full details.

You are free to use, modify, and distribute this work without restriction.

---
