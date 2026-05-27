# CO₂-Bilanz Fundstellen - Mapping für Platzhalter-Ersetzung
# Generiert: 2026-01-24
# Basis: Suche nach "-50.7" in allen Markdown-Dateien

## Fundstellen "-50.7 Gt CO₂/Jahr" (Gesamtbilanz)

### 06_CANON/04_Band4_v4.2_COMPLETE.md
- Zeile 38: "**Klimawirkung:** -50.7 Gt CO₂eq/Jahr (-28.5 Gt additional avoidance)"
  → Ersetze durch: "**Klimawirkung:** -50.7 Gt CO₂eq/Jahr (-28.5 Gt additional avoidance)"

- Zeile 1230: "- ✅ CO₂-Impact quantifiziert (-50.7 Gt/Jahr gesamt)"
  → Ersetze durch: "- ✅ CO₂-Impact quantifiziert (-50.7 Gt/Jahr gesamt)"

- Zeile 1304: "**CO₂-Reduktion:** -50.7 Gt/Jahr"
  → Ersetze durch: "**CO₂-Reduktion:** -50.7 Gt/Jahr"

### 06_CANON/04_Band4_Anwendungen_v4.2.md
- Zeile 13: "**Klimawirkung:** -50.7 Gt CO₂eq/Jahr (-28.5 Gt additional avoidance)"
  → Ersetze durch: "**Klimawirkung:** -50.7 Gt CO₂eq/Jahr (-28.5 Gt additional avoidance)"

- Zeile 2030: "**Total Impact (bei voller Skalierung):** -50.7 Gt/Jahr"
  → Ersetze durch: "**Total Impact (bei voller Skalierung):** -50.7 Gt/Jahr"

- Zeile 2060: "**Total Provolution Impact:** -50.7 Gt/Jahr"
  → Ersetze durch: "**Total Provolution Impact:** -50.7 Gt/Jahr"

- Zeile 2090: "| **CO₂-Potential** | -50.7 Gt/Jahr |"
  → Ersetze durch: "| **CO₂-Potential** | -50.7 Gt/Jahr |"

- Zeile 2196: "-50.7 Gt/Jahr Reduktion mathematisch nachgewiesen"
  → Ersetze durch: "-50.7 Gt/Jahr Reduktion mathematisch nachgewiesen"

- Zeile 2219: "- CO₂-Reduktion: -50.7 Gt/Jahr"
  → Ersetze durch: "- CO₂-Reduktion: -50.7 Gt/Jahr"

## Weitere zu identifizierende Werte

### Domain-spezifische Werte
- Domain A (Governance): -8.2 Gt → -8.2
- Domain B (Production): -15.8 Gt → -15.8
- Domain C (Energy): -12.3 Gt → -12.3
- Domain D (Food/Land): -9.4 Gt → -9.4
- Domain E-H: Analog

### Einzelanwendungen
- B07 (Kreislaufwirtschaft): -23.0 Gt → -23.0
- C11 (Erneuerbare): -15.0 Gt → -15.0
- D15 (Regen-Landwirtschaft): -4.0 Gt → -4.0
- D16 (CO₂-Senken Boden): -5.0 Gt → -5.0

## Nächste Schritte

1. **Manuelle Ersetzung vorbereiten**: Erstelle Skript für sichere Batch-Ersetzung
2. **Band 5 ergänzen**: Füge fehlende Gesamtbilanz-Tabelle ein (Kapitel 5.5)
3. **Englische Versionen**: Synchronisiere Platzhalter auch in 10_ENGLISH/
4. **Release-Versionen**: Update auch _release/ Dateien

## Implementierungs-Strategie

**Phase 1: Core-Ersetzung (JETZT)**
- Ersetze -50.7 mit -50.7 in allen Fundstellen
- Teste Build-System

**Phase 2: Domain-Werte (später)**
- Suche alle Domain-spezifischen Werte
- Erstelle erweiterte Platzhalter

**Phase 3: Einzelanwendungen (später)**
- Nur wo sinnvoll (häufig referenziert)
- Nicht jede Erwähnung muss Platzhalter sein
