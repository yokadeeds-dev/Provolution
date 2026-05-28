"""
Provolution Repo Spec-Consistency Audit Tool
==============================================
"Probatio Consistentia" v0.1 · 2026-05-28

Scannt das Provolution clean-Public-Repo nach **stillen Inkonsistenzen** —
Konflikten zwischen Dateien, die durch Diff-orientierte Reviews (PR-Audits,
/ultrareview), inhaltliche PF-Audits (E1-E8), oder Außenleser-Sichten
typischerweise NICHT erkannt werden.

Hintergrund (2026-05-28 spät-Nacht):
Vier parallele externe Audit-Schichten (PF E1-E8 Kaskade, ChatGPT-Außenleser,
/ultrareview Multi-Agent, Claude Code) haben den Konflikt zwischen
canon/de/SECJ_SPEC_v1.0.md (Formel 0,40·S + 0,25·E + 0,15·C + 0,20·J) und
canon/de/06_framework_extensions_v2.0_SECJ.md (Formel 0,30·S + 0,25·E + 0,30·C
+ 0,15·J) übersehen — alle prüfen Inhalts-Tragfähigkeit, keiner prüft
systematisch Cross-File-Konsistenz von Spec-Definitionen.

Dieses Tool ist die erste Iteration eines Konsistenz-Linters für Spec-Repos.

Checks:
  1. SEC-J-Formel-Varianten in Markdown
  2. reduktion_hart Cross-File-Sync zwischen den beiden zentralen YAMLs
  3. DEPRECATED-Marker bei vN.0/vM.0-Spec-Paaren
  4. SEC-J-Werte pro Hebel: Band 4 ↔ impact_master.yaml

Verwendung:
    python _tools/spec_consistency_audit.py

Exit-Code: 0 wenn keine Konflikte, sonst Anzahl gefundener Konflikt-Befunde.

Geplante Erweiterungen (v0.2+):
  - Domain-Totals B/C/D/.../K Cross-Sync
  - ghg_total.* interne Konsistenz
  - Pfad-Drift legacy → clean (06_CANON/ vs canon/de/)
  - JSON-Output für CI-Integration
  - --strict für Warnings → Failure
"""

import re
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).parent.parent.resolve()


def banner(text):
    print()
    print("─" * 78)
    print(f"  {text}")
    print("─" * 78)


def iter_repo_files(repo: Path, suffix: str):
    """Iteriert alle Files mit gegebener Endung, ignoriert .git und Build-Verzeichnisse."""
    skip_dirs = {".git", "node_modules", ".claude", "__pycache__"}
    for p in repo.rglob(f"*{suffix}"):
        # Skip nur wenn ein Pfad-Teil im skip-set ist (nicht der Repo-Root selbst)
        rel = p.relative_to(repo)
        if any(part in skip_dirs for part in rel.parts):
            continue
        yield p


def check_secj_formulas(repo: Path) -> int:
    """Sucht SEC-J-Formel-Varianten und meldet Konflikte (in .md UND .yaml)."""
    banner("CHECK 1: SEC-J-Formel-Konsistenz (·- und *-Notation, .md + .yaml)")

    pattern = re.compile(
        r"(\d+[,.]\d+)\s*[·*]\s*S\s*\+\s*"
        r"(\d+[,.]\d+)\s*[·*]\s*E\s*\+\s*"
        r"(\d+[,.]\d+)\s*[·*]\s*C\s*\+\s*"
        r"(\d+[,.]\d+)\s*[·*]\s*J"
    )

    findings: dict = {}
    for ext in (".md", ".yaml"):
        for f in iter_repo_files(repo, ext):
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            for match in pattern.finditer(text):
                coeffs = tuple(c.replace(",", ".") for c in match.groups())
                findings.setdefault(coeffs, set()).add(str(f.relative_to(repo)))

    if not findings:
        print("  ℹ️  Keine SEC-J-Formel-Definitionen gefunden.")
        return 0

    if len(findings) == 1:
        coeffs = next(iter(findings.keys()))
        files = findings[coeffs]
        print(f"  ✅ Eine einzige Formel-Variante: {coeffs[0]}·S + {coeffs[1]}·E + {coeffs[2]}·C + {coeffs[3]}·J")
        print(f"     Definiert in {len(files)} File(s)")
        return 0

    print(f"  ⚠️  {len(findings)} verschiedene SEC-J-Formel-Varianten:")
    for coeffs, files in findings.items():
        print(f"  → {coeffs[0]}·S + {coeffs[1]}·E + {coeffs[2]}·C + {coeffs[3]}·J  ({len(files)} File(s))")
        for f in sorted(files):
            print(f"       {f}")
    print()
    print("  Hinweis: mehrere Formel-Varianten können legitim sein")
    print("  (z.B. STANDARD + JUSTICE Modus, oder DEPRECATED v1.0 + aktuell v2.0).")
    print("  Prüfe ob DEPRECATED-Marker bei den älteren Varianten gesetzt sind (CHECK 3).")
    return len(findings) - 1


def check_reduktion_hart_sync(repo: Path) -> int:
    """Vergleicht reduktion_hart zwischen co2_master.yaml und impact_master.yaml."""
    banner("CHECK 2: reduktion_hart Cross-File-Sync")

    yaml_files = [
        repo / "canon" / "data" / "co2_master.yaml",
        repo / "canon" / "data" / "impact_master.yaml",
    ]

    # YAML-Feld (nicht im changelog-String): am Anfang einer Zeile,
    # nur Whitespace davor (kein Anführungszeichen), gefolgt von Wert.
    pattern = re.compile(r"^\s*reduktion_hart\s*:\s*(-?\d+\.?\d*)", re.MULTILINE)

    values: dict = {}
    for yf in yaml_files:
        if not yf.exists():
            continue
        text = yf.read_text(encoding="utf-8", errors="ignore")
        m = pattern.search(text)
        if m:
            values[str(yf.relative_to(repo))] = m.group(1)

    if not values:
        print("  ℹ️  Kein reduktion_hart in den YAMLs gefunden.")
        return 0

    distinct = set(values.values())
    if len(distinct) == 1:
        v = next(iter(distinct))
        print(f"  ✅ reduktion_hart konsistent: {v} Gt CO₂eq/Jahr")
        for f, val in values.items():
            print(f"     {f}: {val}")
        return 0

    print(f"  ❌ reduktion_hart NICHT synchron — {len(distinct)} unterschiedliche Werte:")
    for f, v in values.items():
        print(f"  → {v}  in {f}")
    return 1


def check_deprecated_markers(repo: Path) -> int:
    """Findet vN.0/vM.0-Paare und prüft DEPRECATED-Markierung."""
    banner("CHECK 3: DEPRECATED-Markierung bei v1.0/v2.0-Spec-Paaren")

    # Heuristik: Files mit version-suffix _vN.M
    spec_files = sorted(repo.rglob("*_v*.md"))
    seen: dict = {}
    for sf in spec_files:
        if any(skip in sf.parts for skip in [".git", "_provolution_clean_temp",
                                              ".claude", "_GEM_DEPLOY",
                                              "ARCHIVE", "node_modules"]):
            continue
        m = re.match(r"(.+)_v(\d+)\.(\d+)", sf.stem)
        if m:
            base = m.group(1)
            ver = (int(m.group(2)), int(m.group(3)))
            seen.setdefault(base, []).append((ver, sf))

    issues = 0
    paare = 0
    for base, versions in seen.items():
        if len(versions) < 2:
            continue
        versions.sort(key=lambda x: x[0])
        oldest_ver, oldest_file = versions[0]
        newest_ver, newest_file = versions[-1]

        # Skip when same major version (e.g. v1.0 and v1.1 — kein Pair-Problem)
        if oldest_ver[0] == newest_ver[0]:
            continue

        paare += 1
        text = oldest_file.read_text(encoding="utf-8", errors="ignore")
        first_part = text[:1000]
        if "DEPRECATED" in first_part.upper():
            print(f"  ✅ {oldest_file.name} (v{oldest_ver[0]}.{oldest_ver[1]}) korrekt als DEPRECATED markiert")
            print(f"     → aktuell: {newest_file.name} (v{newest_ver[0]}.{newest_ver[1]})")
        else:
            print(f"  ⚠️  {oldest_file.name} (v{oldest_ver[0]}.{oldest_ver[1]}) NICHT als DEPRECATED markiert")
            print(f"     → sollte verweisen auf {newest_file.name} (v{newest_ver[0]}.{newest_ver[1]})")
            issues += 1

    if paare == 0:
        print("  ℹ️  Keine Major-Version-Spec-Paare im Repo (v1.0/v2.0).")

    return issues


def check_band4_secj_sync(repo: Path) -> int:
    """Vergleicht SEC-J-Werte pro Hebel zwischen Band 4 und impact_master.yaml."""
    banner("CHECK 4: SEC-J-Werte Band 4 ↔ impact_master.yaml")

    band4 = repo / "canon" / "de" / "04_Band4_Anwendungen_v4.2.md"
    yaml_file = repo / "canon" / "data" / "impact_master.yaml"

    if not band4.exists():
        print(f"  ⚠️  {band4.name} nicht gefunden — Check übersprungen.")
        return 0
    if not yaml_file.exists():
        print(f"  ⚠️  {yaml_file.name} nicht gefunden — Check übersprungen.")
        return 0

    band4_text = band4.read_text(encoding="utf-8", errors="ignore")
    yaml_text = yaml_file.read_text(encoding="utf-8", errors="ignore")

    # Tolerant gegenüber Markdown-fett (**SEC-J-Score: 0.93**)
    band4_pattern = re.compile(
        r"SEC-J-Score:\s*(\d+[.,]\d+)\s*\*{0,2}\s*"
        r"\(S:\s*(\d+[.,]\d+),\s*E:\s*(\d+[.,]\d+),"
        r"\s*C:\s*(\d+[.,]\d+),\s*J:\s*(\d+[.,]\d+)"
    )

    band4_values = set()
    for match in band4_pattern.finditer(band4_text):
        secj, s, e, c, j = [float(x.replace(",", ".")) for x in match.groups()]
        band4_values.add((s, e, c, j, secj))

    yaml_pattern = re.compile(
        r"s:\s*(\d\.\d+),\s*e:\s*(\d\.\d+),\s*c:\s*(\d\.\d+),"
        r"\s*j:\s*(\d\.\d+),\s*sec_j:\s*(\d\.\d+)"
    )

    yaml_values = set()
    for match in yaml_pattern.finditer(yaml_text):
        s, e, c, j, sec_j = [float(x) for x in match.groups()]
        yaml_values.add((s, e, c, j, sec_j))

    print(f"  Band 4: {len(band4_values)} Hebel mit SEC-J-Score-Zeile")
    print(f"  impact_master.yaml: {len(yaml_values)} Hebel in sec_j_scores.individual_calculated")

    if not band4_values and not yaml_values:
        print("  ℹ️  Keine SEC-J-Werte gefunden — möglicherweise vor Integration.")
        return 0

    only_b4 = band4_values - yaml_values
    only_y = yaml_values - band4_values

    issues = 0
    if only_b4:
        print(f"  ⚠️  Tupel nur in Band 4 ({len(only_b4)}):")
        for t in sorted(only_b4):
            print(f"     {t}")
        issues += len(only_b4)
    if only_y:
        print(f"  ⚠️  Tupel nur in impact_master.yaml ({len(only_y)}):")
        for t in sorted(only_y):
            print(f"     {t}")
        issues += len(only_y)

    if not only_b4 and not only_y:
        print(f"  ✅ Alle {len(band4_values)} (S,E,C,J,SEC-J)-Tupel konsistent zwischen Band 4 und YAML")

    return issues


def main() -> int:
    print()
    print("═" * 78)
    print("  PROVOLUTION REPO SPEC-CONSISTENCY AUDIT")
    print("  'Probatio Consistentia' v0.1 · 2026-05-28")
    print("═" * 78)
    print(f"  Repo-Root: {REPO_ROOT}")

    total = 0
    total += check_secj_formulas(REPO_ROOT)
    total += check_reduktion_hart_sync(REPO_ROOT)
    total += check_deprecated_markers(REPO_ROOT)
    total += check_band4_secj_sync(REPO_ROOT)

    print()
    print("═" * 78)
    if total == 0:
        print("  ✅ ALLE CHECKS BESTANDEN — Repo-Konsistenz OK")
    else:
        print(f"  ⚠️  {total} Konsistenz-Befunde — siehe Details oben")
    print("═" * 78)
    print()

    return 0 if total == 0 else min(total, 127)


if __name__ == "__main__":
    sys.exit(main())
