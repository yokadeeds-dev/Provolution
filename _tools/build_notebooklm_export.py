#!/usr/bin/env python3
"""
CANON Master-Export fuer NotebookLM
PS-Familie vollstaendig: PS-U / PV v2.0 / PD / PI / PN / PP / PT

Verwendung: python build_notebooklm_export.py
Output: _notebooklm_export/CANON_MASTER_EXPORT_<datum>.md
"""

import os
import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent

CANON_FILES = [
    "06_CANON/00_PS_Familie_Uebersicht.md",
    "06_CANON/01_Band1_SEC_Kanon.md",
    "06_CANON/02_Entscheidungskarte.md",
    "06_CANON/03_Band3_Scientific_Core.md",
    "06_CANON/04_Band4_Anwendungen_v4.2.md",
    "06_CANON/05_Band5_Steuerung_Score.md",
    "06_CANON/06_framework_extensions_v1.0_SECJ.md",
    "06_CANON/07_Probatio_Veritatis_v2.0.md",
    "06_CANON/11_Probatio_Deliberativa_v1.0.md",
    "06_CANON/12_Probatio_Institutionalis_v1.0.md",
    "06_CANON/13_Probatio_Narrativa_v1.0.md",
    "06_CANON/14_Probatio_Philosophica_v1.0.md",
    "06_CANON/15_Probatio_Temporalis_v1.0.md",
]

REFERENCE_FILES = [
    "07_SOURCE/co2_gesamtbilanz_referenzblatt.md",
    "08_INDEX/GLOSSARY.md",
    "08_INDEX/MASTER_INDEX_ANWENDUNGEN.md",
]

OUTPUT_DIR = REPO_ROOT / "_notebooklm_export"
NOTEBOOKLM_CHAR_LIMIT = 500_000


def read_file(path: Path) -> str:
    for enc in ("utf-8", "utf-16", "utf-8-sig", "cp1252"):
        try:
            return path.read_text(encoding=enc)
        except FileNotFoundError:
            print(f"  [WARNUNG] Nicht gefunden: {path}")
            return f"<!-- NICHT GEFUNDEN: {path.name} -->\n"
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception as e:
            print(f"  [FEHLER] {path}: {e}")
            return f"<!-- FEHLER: {path.name} -->\n"
    print(f"  [FEHLER] Kein Encoding: {path.name}")
    return f"<!-- ENCODING-FEHLER: {path.name} -->\n"


def strip_license_block(content: str) -> str:
    pattern = r"\n---\n\n## LICENSE\n.*?---\n?$"
    return re.sub(pattern, "", content, flags=re.DOTALL).rstrip()


def section_header(title: str, source_path: str) -> str:
    line = "=" * 70
    return f"\n\n{line}\n# {title}\n# Quelle: {source_path}\n{line}\n\n"


def build_toc(files: list) -> str:
    lines = ["## Inhaltsverzeichnis\n"]
    for i, (title, _) in enumerate(files, 1):
        lines.append(f"{i:2}. {title}")
    return "\n".join(lines)


def build_export():
    print("\n" + "=" * 60)
    print("CANON Master-Export fuer NotebookLM")
    print("PS-Familie: PS-U / PV v2.0 / PD / PI / PN / PP / PT")
    print("=" * 60)

    OUTPUT_DIR.mkdir(exist_ok=True)
    datum = datetime.now().strftime("%Y-%m-%d")
    output_path = OUTPUT_DIR / f"CANON_MASTER_EXPORT_{datum}.md"

    all_files = []

    print("\n[1/3] Kanonische Dokumente laden...")
    for rel_path in CANON_FILES:
        p = REPO_ROOT / rel_path
        content = read_file(p)
        first_line = content.strip().splitlines()[0] if content.strip() else p.stem
        title = re.sub(r"^#+\s*", "", first_line).strip()[:80]
        all_files.append((title, p, "CANON", content))
        print(f"  + {p.name} ({len(content):,} Zeichen)")

    print("\n[2/3] Referenzdokumente laden...")
    for rel_path in REFERENCE_FILES:
        p = REPO_ROOT / rel_path
        if p.exists():
            content = read_file(p)
            first_line = content.strip().splitlines()[0] if content.strip() else p.stem
            title = re.sub(r"^#+\s*", "", first_line).strip()[:80]
            all_files.append((title, p, "REFERENZ", content))
            print(f"  + {p.name} ({len(content):,} Zeichen)")
        else:
            print(f"  - {p.name} (nicht gefunden)")

    print("\n[3/3] Export zusammenstellen...")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"""# CANON MASTER EXPORT - Probatio Systemica & Provolution
**Exportiert:** {now}
**PS-Familie:** PS-U / PV v2.0 / PD / PI / PN / PP / PT (7 Module vollstaendig)
**Enthaelt:** {len(all_files)} Dokumente
**Lizenz:** CC0 1.0 Universal + Open Humanity License

"""

    toc_entries = [(t, p) for t, p, *_ in all_files]
    toc = build_toc(toc_entries)
    sections = [header, toc]

    for title, path, kategorie, content in all_files:
        rel = str(path.relative_to(REPO_ROOT))
        clean = strip_license_block(content)
        sec = section_header(f"[{kategorie}] {title}", rel)
        sections.append(sec + clean)

    footer = f"""

{"=" * 70}
# EXPORT-ENDE · {now}
# PS-Familie vollstaendig: PS-U / PV v2.0 / PD / PI / PN / PP / PT
{"=" * 70}
"""
    sections.append(footer)
    full_export = "\n".join(sections)
    output_path.write_text(full_export, encoding="utf-8")

    char_count = len(full_export)
    size_kb = output_path.stat().st_size / 1024
    print(f"\n  Gespeichert: {output_path}")
    print(f"  Zeichen: {char_count:,} | Groesse: {size_kb:.1f} KB")

    if char_count > NOTEBOOKLM_CHAR_LIMIT:
        print(f"  [WARNUNG] Limit ueberschritten um {char_count - NOTEBOOKLM_CHAR_LIMIT:,} Zeichen")
    else:
        rem = NOTEBOOKLM_CHAR_LIMIT - char_count
        print(f"  Kapazitaet: {char_count/NOTEBOOKLM_CHAR_LIMIT*100:.1f}% ({rem:,} frei)")

    print("\n" + "=" * 60)
    print("FERTIG")
    print(f"  In NotebookLM: alte Quelle loeschen, neue hochladen")
    print("=" * 60 + "\n")
    return output_path


if __name__ == "__main__":
    build_export()
