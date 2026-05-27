# Submission Preparation — Zenodo + EarthArXiv

Vorbereitete Pipeline für die zwei nächsten Publikations-Schritte.

## 1. Zenodo-DOI (für CANON-Bände + Daten)

### Vorgehen über die GitHub-Zenodo-Integration

1. Bei https://zenodo.org/account/settings/github/ anmelden (mit GitHub-Account `yokadeeds-dev`).
2. Repository `yokadeeds-dev/Provolution` aktivieren (Toggle auf "ON").
3. Auf GitHub einen neuen Release erstellen:
   - Tag-Name: `v1.0.0` (Semantic Versioning empfohlen)
   - Title: "Provolution v1.0.0 — Initial CANON Release"
   - Description: Kurzfassung der Inhalte und Versions-Notiz
4. Zenodo greift den Release automatisch ab und vergibt eine DOI.
5. DOI in `CITATION.cff` und im README eintragen.

### `.zenodo.json` (im Repo-Root)

Die Datei steuert die Metadaten, die Zenodo beim automatischen Import verwendet
— Titel, Beschreibung, Autoren mit ORCID, Lizenz, Keywords, Communities. Vor
dem ersten Release einmal prüfen, dass Werte aktuell sind.

**Keine harten Zahlen in der Description** — Provolution ist living document.
Aktuelle quantitative Werte stehen in `canon/data/*.yaml` und werden mit dem
Release-Snapshot mitversioniert.

### Communities

`climate-change-mitigation` und `open-science` sind als Vorschlag eingetragen.
Beide existieren auf Zenodo; weitere Communities können auf der Zenodo-Web-UI
nach dem Upload angefragt werden.

---

## 2. EarthArXiv-Preprint (Manuskript-PDF)

### Build

```bash
# Bash / Git-Bash
./_tools/build_preprint_pdf.sh blind         # für Submission
./_tools/build_preprint_pdf.sh attributed    # mit Autorennamen

# PowerShell
.\_tools\build_preprint_pdf.ps1 -Target blind
.\_tools\build_preprint_pdf.ps1 -Target attributed
```

**Voraussetzungen:**

- Pandoc 3.x in `PATH` (`winget install JohnMacFarlane.Pandoc` auf Windows)
- `xelatex` (über MiKTeX auf Windows, TeX Live auf Linux/Mac)

**Output:** `_build_outputs/MANUSCRIPT_DRAFT_v0.1[_BLIND].pdf`

### Konfiguration

Voreingestellt:

- A4, 11&nbsp;pt, 2,5&nbsp;cm Rand
- Mainfont: Latin Modern Roman (xelatex-Default — keine Custom-Fonts gesetzt,
  damit der Build auf jeder TeX-Distribution durchläuft)
- 1,25 Zeilenabstand
- Linkfarben schwarz (Submission-tauglich)
- Inhaltsverzeichnis bis Tiefe 2, nummerierte Sections

Falls EarthArXiv andere Vorgaben hat (Letter-Papier, Doppelspalte, spezifisches
LaTeX-Template), die Pandoc-Variablen in `build_preprint_pdf.sh/.ps1`
entsprechend anpassen.

### Bekanntes Limit: Mathe-Sonderzeichen

Das Manuskript enthält Unicode-Mathe-Zeichen direkt im Fließtext (∈, ∀, ≥,
⊥, ∧, ₂, ₙ, α …). Weder Times New Roman noch Latin Modern Roman deckt alle
ab — solche Zeichen erscheinen im aktuellen Build als leere Boxen.

**Lösungen für die finale Submission** (eines davon, nicht alles):

1. **STIX Two Text** als Mainfont — Open Source, deckt Unicode-Mathe-Bereich
   ab. In MiKTeX ggf. nachinstallieren oder über die Schriftartenverwaltung.
   ```bash
   MAINFONT="STIX Two Text" ./_tools/build_preprint_pdf.sh blind
   ```

2. **Cambria** (Windows-only) als Mainfont — hat Mathe-Symbole standardmäßig.
   ```bash
   MAINFONT="Cambria" ./_tools/build_preprint_pdf.sh blind
   ```

3. Math-Passagen im Manuskript in echte LaTeX-Math-Syntax umstellen
   (`$\forall x \in X$` statt direkter Unicode-Zeichen). Dann rendert
   xelatex die Symbole mit Latin Modern Math sauber, unabhängig vom Body-
   Font.

Vor der echten Submission einmal die Markdown-Quellen scannen und entscheiden,
welcher Weg sinnvoll ist.

### Submission

1. PDF lokal builden (siehe oben).
2. Auf https://eartharxiv.org/ einloggen, "Submit a preprint".
3. PDF hochladen, Metadata-Form ausfüllen (Title, Abstract, Keywords, Authors).
4. Submission absenden — Moderation 1–3 Werktage.
5. Vergebene EarthArXiv-DOI in `CITATION.cff` und README eintragen.

### Anhängende Dateien

Wenn EarthArXiv Supplementary Material zulässt:

- `manuscript/figures/Figure1-5.png/svg`
- `manuscript/PEER_REVIEW_PACKAGE.md`
- Link auf das Provolution-Repo

---

## 3. Nach DOI-Vergabe — `CITATION.cff` aktualisieren

```yaml
# Beispiel, mit echter DOI ersetzen:
identifiers:
  - description: "Concept DOI for the latest version"
    type: doi
    value: 10.5281/zenodo.XXXXXXX
  - description: "EarthArXiv Preprint"
    type: doi
    value: 10.31223/X5XXXX
```

Anschließend Release-Tag erhöhen (`v1.0.1` oder `v1.1.0` je nach Scope) und im
Repo committen.
