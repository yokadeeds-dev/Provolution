# RUNBOOK: Portfolio-Benchmark-Kalibrierung (E-II)

**Version:** 1.0
**Datum:** 2026-04-18
**Status:** AKTIV — quartalsweiser Prozess
**Referenz:** Band 5, Kapitel 2.1 (E-II Portfolio-Normalisierung)
**Nachfolger-Kandidat:** Automatisierung via `build_portfolio_benchmark.py` oder n8n-Workflow (siehe Abschnitt 7)

---

## 1. Kontext

Die E-II-Formel in Band 5 Kapitel 2.1 definiert die Effizienz-Berechnung für Anwendungen (M) über die **Portfolio-Normalisierung**:

```
cost_rate(M)          = R(M) / W(M)          (Kosten-pro-Wirkung in €/Gt CO₂)
cost_rate_benchmark   = Median aller cost_rate(M_i) im Portfolio
E(M)                  = max(0, 1 − cost_rate(M) / cost_rate_benchmark)
```

**Warum Kalibrierung nötig:** `cost_rate_benchmark` ist **kein statischer Wert**. Er ändert sich, wenn:
- Neue Anwendungen via AUTO-INTEGRATE (SEC ≥ 0.82) aufgenommen werden
- Bestehende Ressourcen-Werte (R) oder Wirkungs-Werte (W) aktualisiert werden
- Apps deprecated werden

Ohne regelmäßige Neuberechnung werden E(M)-Scores **für alle Apps driftend falsch**. Für Peer-Review-Integrität muss der Benchmark daher **quartalsweise** neu berechnet und dokumentiert werden.

---

## 2. Zeitplan

| Quartal | Berechnungs-Fenster | Deadline Dokumentation |
|---|---|---|
| Q1 | März (Woche 1–2) | 31. März |
| Q2 | Juni (Woche 1–2) | 30. Juni |
| Q3 | September (Woche 1–2) | 30. September |
| Q4 | Dezember (Woche 1–2) | 31. Dezember |

**Verantwortliche Rolle:** Framework-Maintainer (aktuell: Tobias Yoka Dietz). Vertretung nach eigener Wahl.

**Trigger außerhalb des Quartals-Rhythmus (Ad-hoc-Kalibrierung nötig):**
- Neue App wird via AUTO-INTEGRATE aufgenommen → sofortige Re-Kalibrierung
- ≥ 3 Apps haben >20 % Änderung in R oder W → Re-Kalibrierung
- Peer-Review / Publikation ansteht → Re-Kalibrierung als Teil des Review-Package

---

## 3. Inputs

### 3.1 Datenquelle: `20_CANON/data/impact_master.yaml`

Pro App werden folgende Werte benötigt:

| Feld | Beschreibung | Beispiel |
|---|---|---|
| `R(M)` | Ressourcen-Aufwand (Kapital + laufend, 10-Jahres-Horizont) | €-Summe |
| `W(M)` | Primär-Wirkung (CO₂-Reduktion kumuliert über 10 Jahre) | Gt CO₂ |

**Quelle pro App in Band 4 v4.2:**
- R(M) ← Sektion 4 „RESSOURCEN" → `Finanziell: Initial + laufend × 10 Jahre`
- W(M) ← Sektion 3 „WIRKUNG" → `Primär: X Gt CO₂/Jahr × 10 Jahre`

**Hinweis:** Apps ohne direkte CO₂-Wirkung (Enabler wie A01, E19, E20, H32) werden **nicht in den Benchmark aufgenommen**, da sie kein cost_rate haben. Eine separate Benchmark-Klasse für Enabler kann zukünftig erwogen werden (out-of-scope für v1.0).

### 3.2 Apps-Liste

Aus `08_INDEX/MASTER_INDEX_ANWENDUNGEN.md` (Stand quartalsweise). Enthält die aktuell kanonisch qualifizierten n Apps.

---

## 4. Berechnungs-Ablauf

### 4.1 Extraktion

Für jede App M_i mit quantifizierter CO₂-Wirkung:

1. R(M_i) = `finanziell.initial + finanziell.laufend_pro_jahr × 10` (aus Band 4 Sektion 4)
2. W(M_i) = `co2_reduktion_gt_pro_jahr × 10` (aus Band 4 Sektion 3 / `impact_master.yaml`)
3. cost_rate(M_i) = R(M_i) / W(M_i)   *(Einheit: € / Gt CO₂ kumuliert über 10 Jahre)*

### 4.2 Median

Alle cost_rate(M_i) aufsteigend sortieren. Median:
- Bei ungerader Anzahl k: mittlerer Wert
- Bei gerader Anzahl k: arithmetisches Mittel der beiden mittleren Werte

**Ergebnis:** `cost_rate_benchmark_YYYYQN = [Wert] €/Gt CO₂`

### 4.3 E(M_i) pro App neu berechnen

`E(M_i) = max(0, 1 − cost_rate(M_i) / cost_rate_benchmark)`

Apps mit cost_rate < Benchmark → E > 0 (überdurchschnittlich effizient)
Apps mit cost_rate ≥ Benchmark → E = 0 (unter- oder gleich-durchschnittlich)

### 4.4 Ergebnis Q1/2026 (erste Kalibrierung nach Runbook v1.0)

Erfasst: 11 Impact-Apps (A, C12, E, F, G27, H-Domäne als Enabler separat). Werte aus Band 4 v4.2 Sektion 3+4:

| Rang | App | R(10y) [€] | W(10y) [Gt] | cost_rate [€/t] | E |
|---|---|---|---|---|---|
| 1 | B09 Materialfluss-Steuerung | 700 k | 0,2 | 0,0035 | 1,00 |
| 2 | B07 Kreislaufwirtschaft | 1,5 Mrd | 230 | 0,0065 | 1,00 |
| 3 | B08 Biopolymere (Hanf) | 15 Mrd | 15 | 1,00 | 0,962 |
| 4 | B10 Abfall-zu-Ressource | 30 Mrd | 20 | 1,50 | 0,942 |
| 5 | D15 Regen-Landwirtschaft | 700 Mrd | 40 | 17,5 | 0,327 |
| **6** | **D16 CO₂-Senken Boden** | **1,3 Bio** | **50** | **26,0** | **0,00 (Median)** |
| 7 | C11 Erneuerbare Integration | 4,0 Bio | 150 | 26,67 | 0,00 |
| 8 | D17 Hanf-Anbau | 150 Mrd | 1,85 | 81,08 | 0,00 |
| 9 | C13 Smart Grids | 600 Mrd | 5 | 120,0 | 0,00 |
| 10 | C14 Dezentrale Versorgung | 900 Mrd | 3 | 300,0 | 0,00 |
| 11 | D18 Urbane Landwirtschaft | 300 Mrd | 0,5 | 600,0 | 0,00 |

→ **`cost_rate_benchmark_2026Q1 = 26,0 €/t CO₂` (D16 stellt den Median)**

**Outlier-Befunde (plausibilisiert):**
- **B07, B09** unter 0,01 €/t — ultra-low, weil Low-Invest-Apps mit hoher Hebelwirkung (Kreislaufwirtschaft-Prinzip, IoT-Tooling). Realistisch.
- **D18** bei 600 €/t — Vertical Farming ist energie-intensiv, 23× Median. Plausibel, rechtfertigt E=0.

**Sanity-Check gegen Externes:**
- EU-ETS 2023: ~80 €/t. Unser Median 26 €/t liegt darunter — zu erwarten, da Provolution-Apps pro Definition günstiger sein sollen als Markt-Preis für Zertifikate.
- DAC (Direct Air Capture): 300–500 €/t. Unsere Outlier (C14, D18) liegen in dieser Region — Energie-/Gebäude-Apps sind strukturell teurer.

**Einheiten-Hinweis:** `cost_rate` hier in `EUR / t CO₂ (10y kumuliert)`. Für Verhältnisse mit EU-ETS-Preisen (jährlich) den Faktor ÷10 mental rechnen (grob: Provolution-Apps unter 2,6 €/t_CO₂_jährlich sind unter EU-ETS-Preis-Niveau und somit extrem kosteneffizient).

---

## 5. Outputs

### 5.1 Update `20_CANON/data/impact_master.yaml`

Neuer Abschnitt am Ende der Datei:

```yaml
# ============================================================================
# TEIL X: PORTFOLIO-BENCHMARK (quartalsweise kalibriert)
# ============================================================================

portfolio_benchmark:
  current:
    quartal: "2026Q1"         # ISO-Quartal
    cost_rate_benchmark: 26000
    einheit: "EUR_pro_t_CO2_10y"
    n_apps_eingerechnet: 7
    n_apps_enabler_excluded: 8  # nicht-CO₂-wirksame Apps
    berechnet_am: "2026-04-18"
    berechnet_von: "Framework-Maintainer"
    median_app_id: "D16"      # App deren cost_rate den Median stellt

  history:
    - quartal: "2026Q1"
      cost_rate_benchmark: 26000
      delta_zum_vorquartal: null  # Erste Kalibrierung
      trigger: "Initialberechnung"
```

### 5.2 Update `06_CANON/05_Band5_Steuerung_Score.md`

Im Kapitel 2.1 unter der E-II-Formel ergänzen:

```
**Aktueller Portfolio-Benchmark:** 26 000 €/t CO₂ (Q1/2026)
**Quelle:** 20_CANON/data/impact_master.yaml → portfolio_benchmark.current
**Update-Frequenz:** quartalsweise (siehe 20_CANON/docs/RUNBOOK_PORTFOLIO_BENCHMARK.md)
```

### 5.3 Changelog-Eintrag

In `impact_master.yaml` unter `meta.changelog`:

```yaml
v2_1_2026q1:
  - "Portfolio-Benchmark Q1/2026 initial kalibriert: 26 000 €/t CO₂"
  - "n=7 Apps mit quantifizierter CO₂-Wirkung eingerechnet"
  - "8 Enabler-Apps (A01, E19, etc.) separat behandelt, nicht im Benchmark"
```

---

## 6. Validation-Checkliste

Vor Abschluss der Kalibrierung prüfen:

- [ ] **Vollständigkeit:** Wurden alle aktuell kanonisch qualifizierten n Apps betrachtet (mit MASTER_INDEX abgeglichen)?
- [ ] **Enabler-Trennung:** Apps ohne quantifizierte CO₂-Wirkung korrekt als `enabler_excluded` markiert?
- [ ] **Einheiten-Konsistenz:** Alle R-Werte in €, alle W-Werte in Gt CO₂, Zeithorizont einheitlich 10 Jahre?
- [ ] **Outlier-Check:** Apps mit cost_rate > 10× Median manuell plausibilisiert (evtl. Datenfehler)?
- [ ] **Delta-Plausibilität:** Gegenüber Vorquartal Änderung ≤ 30 %? Falls >30 % — Ursache im Changelog dokumentieren.
- [ ] **Peer-Review-Readiness:** Die 7 obigen Punkte dokumentiert UND Commit-Message nennt Quartal + neuen Benchmark?

---

## 7. Automatisierungs-Pfad (zukünftig)

Dieses Runbook ist manuelle Baseline. Geplanter Automatisierungs-Pfad:

**Phase 2 (Kandidat 2026Q3):** `20_CANON/data/build_portfolio_benchmark.py`
- Liest `impact_master.yaml` + `MASTER_INDEX_ANWENDUNGEN.md`
- Berechnet cost_rate pro App und Median
- Schreibt `portfolio_benchmark`-Block in YAML
- Erzeugt Commit mit Default-Message

**Phase 3 (Kandidat 2026Q4):** n8n-Workflow
- Trigger: Cron quartalsweise + manuell
- Schritt 1: Script aus Phase 2 ausführen
- Schritt 2: PR in GitHub erstellen
- Schritt 3: Notification (E-Mail/Slack) an Maintainer

Solange Phase 2/3 nicht umgesetzt: **dieses Runbook manuell abarbeiten**.

---

## 8. Verantwortung & Dokumentations-Trail

- **Wer:** Framework-Maintainer
- **Wann:** 4× jährlich (März, Juni, September, Dezember), jeweils Woche 1–2
- **Dauer:** ca. 1–2 h (manuell), reduziert sich mit Automatisierung auf <10 min
- **Commit-Konvention:** `feat(portfolio-benchmark): Q[N]/YYYY kalibriert — [Wert] €/t CO₂`
- **Audit-Link:** Jede Kalibrierung wird referenziert in `08_INDEX/_AUDIT_YYYY-MM-DD_*.md`

---

*Runbook v1.0 · 2026-04-18 · Autor: Tobias Yoka Dietz · Nachgezogen durch Claude Code Session 2026-04-18*
*Nächste Erwartete Kalibrierung: Q2/2026 (bis 30. Juni 2026)*
