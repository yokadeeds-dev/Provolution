# B11 Definitions-Korrektur: Hanf-Bio-Reduktionsmittel-Spur wiederhergestellt

**Datum:** 2026-05-29 (intern, kein PF-Audit-Run)
**Anlass:** User-Hinweis nach PR #13 — die ursprüngliche Provolutions-Planung für B11 "Industrielle Transformation" enthielt eine **Hanf-Bio-Reduktionsmittel-Spur** als primären Pfad. Diese ist bei der Domain-B-yaml-only-Definition (vor 2026-05-28) und im PR #13 SEC-J-Audit verloren gegangen.
**Status:** Definitions-Korrektur dokumentiert; **SEC-J-Re-Audit beim nächsten Gem-Lauf ausstehend**

---

## Was war verloren gegangen

| Stand | B11-Definition | SEC-J |
|---|---|---|
| **Ursprüngliche Provolutions-Planung** (vor v0.1) | Hanf-Biokohle/Pyrolyse als Reduktionsmittel-Ersatz für Koks in Hochöfen — Drop-in für bestehende Anlagen | (damals nicht formal kalkuliert) |
| **AUTO_INTEGRATE-Kandidat-Beschreibung** (2026-04-17) | "Schwerindustrie (Stahl, Zement, Chemie) auf grüne Prozesse: H₂-Direktreduktion, Elektrolichtbogenöfen, CCS" — Hanf-Spur fehlt | SEC 0,71 (geschätzt) |
| **PR #13 PS-U:STANDARD-Audit** (2026-05-29) | "H₂-Direktreduktion (Stahl)" — als alleiniger Pfad bewertet | SEC-J 0,86 mit ⚠️ Just-Transition-Warnschwelle |
| **PR #14 Korrektur** (diese Datei) | Hanf-Bio-Reduktionsmittel als **primärer Pfad**, H₂ als Alternative | Re-Audit ausstehend; erwartet ~0,91 (J ~0,90) |

## Warum die Korrektur methodisch zwingend ist

### 1. Konsistenz mit D17-Hanf-Kaskade

Die Provolution-Architektur baut auf der D17-Hanf-Kaskade auf (Boden → Faser → Material → Bau → Biopolymer → 3D-Filament → Lagerblock). Hanf-Reststoffe (Schäben aus der Faser-Verarbeitung) als Pyrolyse-Input für Bio-Reduktionsmittel ist der **siebte Pfad** dieser Kaskade — und genau der Pfad, der bei der yaml-only-Bewertung verschwunden ist.

### 2. Industrie-Realität (Best Practice 2026)

Char Technologies (Kanada) liefert CleanFyre Biokohle (>85 % C-Gehalt) seit Jahren an ArcelorMittal Dofasco. thyssenkrupp plant ab 2025 250.000 t/yr Bio-Kohlenstoff-Drop-in. EU CBAM macht biogenen Kohlenstoff bis 2030 zwingend. Das ist **kein Hypothese-Pfad**, sondern industrie-realer Best Practice.

### 3. Just-Transition-Problem löst sich auf

Die Hauptbegründung für die PR #13-Warnschwelle (J=0,78) war:
> "Extrem kapitalintensive Transformation. Risiko massiver Verwerfungen auf dem Arbeitsmarkt (Stahlindustrie), wenn alte Anlagen unrentabel werden."

Genau dieses Risiko verschwindet beim **Drop-in-Pfad**: keine Anlagen-Umbauten, keine Belegschafts-Verwerfungen, sofort wirtschaftlich (CBAM-getrieben).

## SEC-J-Re-Audit-Erwartung

Aktuelle PR #13-Werte: S 0,95 · E 0,75 · C 0,90 · J 0,78 → SEC-J 0,86

Erwartete korrigierte Werte (Schätzung, Re-Audit erforderlich):

| Dimension | PR #13 | erwartet PR #14 | Begründung |
|---|:---:|:---:|---|
| **S** Sufficient | 0,95 | **0,95** | unverändert — Stahlsektor ~7-9% globaler CO₂-Emissionen |
| **E** Efficient | 0,75 | **~0,88** | Drop-in nutzt bestehende Hochöfen (kapitalsparend); EBC-Zertifizierung vorhanden; ETS-Einsparung sofort |
| **C** Consistent | 0,90 | **0,90** | unverändert; vollständig systemkonform mit D17-Hanf-Kaskade |
| **J** Just | 0,78 | **~0,90** | Drop-in löst Just-Transition-Problem; dezentralisiert Wertschöpfung (Landwirte werden Stahl-Lieferanten); kein Konzern-Monopol mehr |
| **SEC-J** | 0,86 | **~0,91** | PS-U 2.0 STANDARD: 0,30·0,95 + 0,25·0,88 + 0,30·0,90 + 0,15·0,90 = 0,91 |

**Warnschwelle entfällt:** J 0,90 > 0,80, daher keine J-Auflage mehr erforderlich. Die alte Just-Transition-Auflage bleibt nur für den H₂-Alternativ-Pfad relevant.

## Implementierungs-Implikation

Die in PR #13 dokumentierte Implementierungs-Auflage:
> "Staatliche Subventionen für H₂-Direktreduktion zwingend an Standortgarantien, 'Just Transition'-Umschulungsprogramme..."

bleibt nur für **Pfad B (H₂-Direktreduktion)** relevant. Für **Pfad A (Hanf-Bio-Reduktionsmittel)** entfallen diese Auflagen — der Pfad ist konstruktiv just (Drop-in + dezentrale Wertschöpfung).

## Quellen

- **User-Recherche** (industrienahe Best-Practice-Tabellen): `studies/SOURCES_2026-05-29/B11_HANF_STAHL_RECHERCHE.md`
- Char Technologies CleanFyre Biokohle (>85% C-Gehalt, EBC-zertifiziert)
- ArcelorMittal Dofasco Partnerschaft Char Tech
- thyssenkrupp 250.000 t/yr Bio-Kohlenstoff ab 2025
- EU CBAM / ETS-Preise 2026-2030
- ChatGPT-Archiv 2025-11-09 (`01_Tech/Buch_Provolution/69104c78... Stahlersatz mit Carbon und Hanf.md`)

## Folge-Aktion

Beim nächsten PF-Lauf (Gem aktuell PR #11 + KB-Update 2026-05-28 23:59):
- B11 mit korrigierter Definition erneut bewerten
- Erwartung: SEC-J ~0,91 (statt 0,86), J ~0,90 (statt 0,78)
- Warnschwelle entfällt für Pfad A; nur für Pfad B (H₂) bleibt sie
- impact_master.yaml v2.5 sec_j_scores.B11 `pending_re_audit` auf `false` setzen + finale Werte eintragen

---

*Audit-Datei angelegt 2026-05-29 mittags · interne Definitions-Korrektur (kein neuer PF-Lauf) · Re-Audit beim nächsten Gem-Lauf*
