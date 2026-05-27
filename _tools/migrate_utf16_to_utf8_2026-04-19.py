#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-off: UTF-16 LE -> UTF-8 Korrektur der Canon-Extensions (2026-04-19).

Ablauf (zwei Durchgänge):
  PASS 1 (schon gelaufen): raw UTF-16 LE -> UTF-8. Ergebnis hatte
          cp850-Mojibake (z.B. "Prüfung" -> "Pr├╝fung"), weil die
          Original-Bytes cp850-Text repräsentierten, in UTF-16 LE verpackt.
  PASS 2 (hier): current UTF-8 -> encode('cp850') -> decode('utf-8')
          liefert den korrekten Text mit Umlauten.

Scope: die 5 Files die in PASS 1 migriert wurden.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

FILES_TO_FIX = [
    REPO / "06_CANON" / "06_framework_extensions_v1.0_SECJ.md",
    REPO / "06_CANON" / "08_extension_e11_hanf_universalanwendungen_v1.0.md",
    REPO / "06_CANON" / "09_extension_e12_urbane_transformation_v1.0.md",
    REPO / "06_CANON" / "10_extension_e13_governance_reform_v1.0.md",
    # (Legacy Gem-Folder wurde 2026-04-19 nach ARCHIVE/legacy_gem_folder_2026-04-19/ verschoben)
    # REPO / "ARCHIVE" / "legacy_gem_folder_2026-04-19" / "08_extension_e11_hanf_universalanwendungen_v1.0.md",
    REPO / "GEM_PROMPTS" / "knowledge_base" / "shared" / "08_extension_e11_hanf_universalanwendungen_v1.0.md",
]


def fix(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"[skip] nicht gefunden: {path.name}"

    text = path.read_text(encoding="utf-8")
    try:
        fixed = text.encode("cp850").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError) as e:
        return False, f"[skip] kein cp850-Mojibake-Muster: {path.name} -- {e}"

    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(fixed)

    # Umlaut-Sanity-Check
    umlauts = sum(fixed.count(c) for c in "äöüÄÖÜß")
    return True, f"[OK] {path.name}: {len(text)} -> {len(fixed)} chars, {umlauts} Umlaute"


def main():
    print("PASS 2: cp850-Mojibake-Fix - 2026-04-19")
    print("=" * 60)
    for p in FILES_TO_FIX:
        _, msg = fix(p)
        print(msg)
    print("=" * 60)
    print("Done.")


if __name__ == "__main__":
    main()
