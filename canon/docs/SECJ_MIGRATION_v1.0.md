# SEC-J Schema-Migration v1.0

**Datum:** 2026-04-27
**Branch:** `feat/secj-integration`
**Spezifikation:** `06_CANON/SECJ_SPEC_v1.0.md`

---

## Was wurde geändert

### Umbenannt: `sec_integration` → `secj_integration`

Das optionale Feld `sec_integration` im `PROJECT_IMPACT_SCHEMA.json` wurde in `secj_integration` umbenannt und um die J-Dimension (Justice) erweitert.

**Betroffene Dateien:**

| Datei | Art der Änderung |
|-------|-----------------|
| `20_CANON/templates/PROJECT_IMPACT_SCHEMA.json` | Feld umbenannt, `justice_score`, `veto_triggered`, `secj_total` ergänzt, Formel aktualisiert |
| `20_CANON/templates/EXAMPLE_D17_HANF.json` | Daten migriert, `justice_score = null` (noch nicht bewertet) |
| `20_CANON/data/README_MULTI_IMPACT.md` | Dokumentationszeile aktualisiert |
| `20_CANON/data/impact_master.yaml` | Migrations-Annotation im `project_impact_schema:`-Abschnitt ergänzt |

---

## Neue Feldstruktur

```json
"secj_integration": {
  "sufficiency_score": 0.0–1.0,
  "efficiency_score":  0.0–1.0,
  "consistency_score": 0.0–1.0,
  "justice_score":     0.0–1.0  oder  null (ausstehend),
  "veto_triggered":    true / false / null,
  "secj_total":        0.0–1.0  oder  null,
  "calculation_method": "secj = 0.40*S + 0.25*E + 0.15*C + 0.20*J"
}
```

---

## Formel-Änderung

| Version | Formel | Gewichte |
|---------|--------|----------|
| Legacy (`sec_integration`) | `sec = 0.5·S + 0.3·E + 0.2·C` | S=0,50 E=0,30 C=0,20 |
| Neu (`secj_integration`) | `secj = 0.40·S + 0.25·E + 0.15·C + 0.20·J` | S=0,40 E=0,25 C=0,15 J=0,20 |

---

## J-Veto-Regel

Wenn `justice_score < 0,50` (entspricht `equity_score < 0` in Multi-Impact Dim. 3):

- `veto_triggered = true`
- `secj_total = null`
- Die Maßnahme ist **nicht zulässig**, unabhängig von S/E/C

---

## Migration bestehender Werte

| Altes Feld | Neues Feld | Migrations-Logik |
|-----------|-----------|-----------------|
| `sec_total` | `secj_total` | **Kein direktes Mapping.** Alte Werte (Formel `0.5S+0.3E+0.2C`) sind nicht kompatibel mit neuer Formel. `secj_total = null` bis `justice_score` explizit gesetzt wird. |
| `sufficiency_score` | `sufficiency_score` | 1:1 übernommen |
| `efficiency_score` | `efficiency_score` | 1:1 übernommen |
| `consistency_score` | `consistency_score` | 1:1 übernommen |
| — | `justice_score` | Neu: `J = (equity_score + 1) / 2` aus Multi-Impact Dim. 3 |

---

## Noch ausstehend (defer → Band-4-Schritt)

Diese Dateien nutzen eine eigene SEC-Implementierung und werden im Band-4-Schritt aktualisiert:

| Datei | Was zu tun ist |
|-------|---------------|
| `04_CONTENT_LEVERS/community_pipeline.py` | `Result`-Datenklasse um `j`, `j_veto` erweitern; Formel auf `0.40S+0.25E+0.15C+0.20J` aktualisieren; Veto-Logik einbauen |
| `04_CONTENT_LEVERS/manual_classify_2026-04-19.py` | Abhängig von `community_pipeline.Result` |
| `08_INDEX/community_registry.csv` | Neue Spalte `score_j` in CSV-Header; historische Zeilen bleiben unverändert |
| `03_PILOTEN/PILOT_H01_COMPLETE.md` | `sec_total: 0.90` → inhaltliche Einordnung im Band-4/5-Kontext |

---

*Migrations-Dokument. Kein eigener Commit-Inhalt — wird mit Schema-Commit eingecheckt.*
