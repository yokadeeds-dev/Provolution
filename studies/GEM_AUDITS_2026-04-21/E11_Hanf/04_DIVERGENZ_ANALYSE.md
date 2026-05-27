# Doppel-Audit E11 — Divergenz-Analyse PS 3.0 vs. PS-U 1.1

**Datum:** 2026-04-21
**Prüfobjekt:** Extension E11 Hanf-Universalanwendungen (v1.0, 2026-02-06)
**Scope:** (a) 3,2-Gt-CO2-Einsparung bei 100-Mha-Szenario · (b) Konsistenz der I35-I38 · (c) Termination-Regel SEC-P < 0.60

---

## Kernbefund

| Gem | Verdict | Scope-Fidelität |
|---|---|---|
| **PS 3.0** | BESTANDEN / TRAGFÄHIG | ⚠️ **Scope-Fehler** — Gem hat auf **Hempcrete-Teilaspekt** verengt, nicht die E11-Extension als Ganzes geprüft |
| **PS-U 1.1** | **unentscheidbar** (MMM-BLOCK: W_min fehlt) | ✅ korrekt als Extension-Skalierungs-Prüfung behandelt |

---

## Problem bei PS 3.0

Die Eingabe fragte explizit nach Extension E11 (80 Hanfanwendungen, 4 neue I-Apps, aggregiertes 3,2-Gt-Szenario). Das PS 3.0 Gem antwortete mit einer Prüfung von "Hanfbeton als systemischer Ersatz für konventionellen Beton im urbanen Wohnungsbau zur Erreichung der Klimaneutralität" — das ist ein **Teilaspekt** der Extension (I33/Hempcrete-Spezifikation), nicht der Gesamtvorschlag.

**Mögliche Ursachen:**
1. Die Hempcrete-Zahlen (-130 kg/m³ CO₂, Dämmwert 0.07 W/mK) waren die konkretesten Claims im Prompt und wurden als Kernprüfobjekt interpretiert
2. PS 3.0 neigt bei komplexen Multi-Claim-Eingaben zur Reduktion auf den operationalisierbarsten Sub-Claim
3. Der Chat-Titel wurde automatisch auf "Hanfbeton: Klimaneutralität im Wohnungsbau" gesetzt — Gemini hat das Thema selbst geschnitten

**Konsequenz für künftige PS-3.0-Prüfungen:** Bei Extensions oder Multi-Claim-Dossiers **expliziten Scope-Anker** an den Anfang setzen (z.B. "PRÜFOBJEKT: Das Extension-Framework E11 als Ganzes, nicht einzelne Anwendungen").

---

## PS-U 1.1 Ergebnis (valide)

**MMM-BLOCK** — Mindestziel W_min nicht definiert. Ohne diesen Schwellenwert kann S (Sufficient) nicht mathematisch berechnet werden.

**Dennoch Vor-Prüfung der Teilfragen:**
- **(b) I35–I38 Konsistenz:** Hohe interne SEC-Werte (0.80–0.91) deuten auf Kohärenz hin. Aber: I35 hat Flächennutzungs-Konflikt (K=1 gegen Lebensmittel), I37 hängt an Marktdurchdringung (U=1). Systemische Einbettung erfordert explizite Zählung der Schnittstellen zum konventionellen Sektor.
- **(c) Termination-Regel SEC-P < 0.60:** **Methodisch sauber**. Ausschluss von Tumor/Alzheimer/Parkinson (0.52-0.58) ist zwingend, um statistische Integrität des Portfolios E11 nicht zu korrumpieren.

**Next Steps (PS-U empfohlen):**
1. Definition von W_min (z.B. 2,5 Gt CO2/Jahr)
2. R(M)-Angabe (Kosten pro Gt CO2) für E-Prüfung
3. Vergleichsalternativen R_min/R_max

---

## Handlungsfähige Befunde für den Canon

### Für E11-Extension direkt:
1. **W_min nachliefern** — aktuell fehlt im Extension-Dokument ein verbindliches Mindestziel, gegen das die 3,2-Gt-Behauptung testbar wäre. → Ergänzen in `08_extension_e11_hanf_universalanwendungen_v1.0.md` §9 Abschnitt 9.1 ("Aggregiertes Gesamtpotenzial")
2. **R(M)-Kennzahl ergänzen** — Kosten pro eingesparter Gt CO₂ (zur Vergleichbarkeit mit Aufforstung, DAC, BECCS). Für die 100-Mha-Skalierung fehlt eine Gesamt-Investitions-/Betriebskostenrechnung.
3. **I35-Flächenkonflikt explizit benennen** — PS-U hat Phytoremediation vs. Lebensmittelproduktion als K=1 zählbar gemacht. Gehört in §2.2 oder §6.2 als Einschränkung.
4. **I37-Marktdurchdringungs-Abhängigkeit** — U=1 "Zulassungen fehlen" sollte als Risiko-Pfad in §8 Statistik aufgenommen werden, nicht nur als "Break-Even 2027-2030".

### Für Prüfworkflow:
- **PS 3.0 Scope-Drift vermeiden:** Bei Multi-Claim-Eingaben expliziten Scope-Anker am Prompt-Anfang.
- **PS-U 1.1 ist robuster** für strukturell komplexe Eingaben — stoppt sauber mit MMM-BLOCK statt zu halluzinieren.

---

## Methodische Beobachtungen (Gem-Audit-Meta)

- **PS 3.0 E11-Scope-Drift** ist der erste echte Qualitätsbefund gegen das Gem: Es antwortet auf eine vereinfachte Variante der Frage statt der gestellten. Ähnliches Muster ist im Provolution-Audit-Log zu prüfen (`ARCHIVE/legacy_gem_folder_2026-04-19/_AUDIT_2026-04-17.md` — dort stand bereits, dass PS 2.0 kein Routing-Konzept hat; 3.0 hat eins, aber der Scope-Verengung-Bias scheint fortzubestehen).
- **PS-U 1.1 hielt die MMM-Regel ein** ("Niemals SEC-J starten ohne abgeschlossenes MMM-Artefakt" — Verhaltensregel #2). Das ist genau die Formalisierungs-Strenge, die den v1.0→v1.1-Update ausgemacht hat.
- **Chat-Management-Beobachtung:** Beide Gems erstellen jeden neuen Prompt als neue Chat-Instanz. Chat-Titel werden von Gemini auto-generiert basierend auf inferred topic — kann Scope-Drift sichtbar machen (hier: "Hanfbeton" statt "E11").

---

## Empfehlung für weitere Doppel-Audits

**Korrektur-Re-Run für PS 3.0 empfohlen** mit explizitem Scope-Anker — dann werden die E11-Gesamt-Claims statt Hempcrete-Sub-Claims geprüft. Alternativ: akzeptieren als "PS 3.0 bestätigt einen Sub-Aspekt (Hempcrete I33) als tragfähig, aber die Gesamt-Extension-Frage ist durch PS-U 1.1 als unentscheidbar markiert."

**Workflow-Hardening für die restlichen Kandidaten:**
- Prompts mit **klarem PRÜFOBJEKT-Satz** am Anfang beginnen
- Bei Mehrteiligem: **Teilprüfungen separat** durchführen statt alles im Block
