"""
Provolution Repo Spec-Consistency Audit Tool
==============================================
"Probatio Consistentia" v0.3 · 2026-10-14 (v0.1: 2026-05-28)

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
  --- v0.2 (2026-10-14, YAML-geparst, deterministisch) ---
  5. CO₂-Aggregate: Domain-Summen, App-Summen, Gesamt, Potenzial, Anteil
  6. Abgeleitete Zähler: metrics.anzahl_anwendungen / anzahl_domains, ID-Eindeutigkeit
  7. Cross-File-Sync co2_master.yaml ↔ impact_master.yaml (Gesamt, Domains, Communities)
  8. GHG: GWP100 = IPCC AR6, Gas-Summen, ghg_total-Komponenten + Spanne (RANGE/CURRENT), Rebound-Kette
  9. SEC-J: STANDARD-Formel, J-Veto, J-Warnschwelle mit Auflage
 10. Quellen: Repo-Pfade existieren, Hashes im SHA-256-Format
 11. Overlap-Matrix (canon/data/overlap_matrix.yaml): Gruppen-Arithmetik B/C/D,
     Gas-Schicht-Zuordnung, all-GHG-Punktwert = naive Summe + Σ Overlap,
     all-GHG-Monte-Carlo-Werte = ghg_percentiles.csv

Verwendung:
    python _tools/spec_consistency_audit.py          # alle Checks, Exit = Summe aller Befunde
    python _tools/spec_consistency_audit.py --ci     # CI-Modus: blockierend nur Checks 2 + 5-11;
                                                     # heuristische Checks 1/3/4 nur als Hinweis

Exit-Code: 0 wenn keine (blockierenden) Konflikte, sonst Anzahl Befunde (max. 127).
Abhängigkeit Checks 5-10: PyYAML (pip install pyyaml).

Geplante Erweiterungen (v0.3+):
  - Pfad-Drift legacy → clean (06_CANON/ vs canon/de/) in Markdown
  - JSON-Output
  - maschinenlesbare Overlap-Matrix (B/C/D) statt Ungleichungs-Check
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


# ═════════════════════════════════════════════════════════════════════════════
# v0.2 — YAML-geparste Daten-Checks (deterministisch, CI-blockierend)
# ═════════════════════════════════════════════════════════════════════════════

TOL = 0.05  # Gt — Rundungstoleranz für Summen aus 1-2-Nachkommastellen-Werten

# IPCC AR6 WG1 (2021) Table 7.15, GWP100
GWP_AR6 = {"ch4_fossil": 29.8, "ch4_non_fossil": 27.0, "n2o": 273}

# Domains, deren Total bewusst overlap-bereinigt ist (|total| < |Summe apps|)
OVERLAP_DOMAINS = {"B_production", "C_energy", "D_food_land"}


def _load_yamls(repo: Path):
    import yaml
    data = repo / "canon" / "data"
    with open(data / "co2_master.yaml", encoding="utf-8") as f:
        co2 = yaml.safe_load(f)
    with open(data / "impact_master.yaml", encoding="utf-8") as f:
        imp = yaml.safe_load(f)
    return co2, imp


def _load_overlap(repo: Path):
    import yaml
    with open(repo / "canon" / "data" / "overlap_matrix.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _close(a, b, tol=TOL):
    return a is not None and b is not None and abs(float(a) - float(b)) <= tol


def _fail(msg):
    print(f"  ❌ {msg}")
    return 1


def check_co2_aggregates(co2) -> int:
    banner("CHECK 5: CO₂-Aggregate (co2_master.yaml)")
    issues = 0
    domains = co2["domains"]
    for key, d in domains.items():
        s = sum((d.get("apps") or {}).values())
        if key in OVERLAP_DOMAINS:
            if abs(d["total"]) > abs(s) + TOL:
                issues += _fail(f"{key}: overlap-bereinigtes total {d['total']} größer als Summe apps {s:.2f}")
        elif not _close(s, d["total"]):
            issues += _fail(f"{key}: Summe apps {s:.2f} ≠ total {d['total']}")
    dom_sum = sum(d["total"] for d in domains.values())
    comm = co2["community_integrations"]
    comm_sum = sum(i["co2_impact_gt_per_year"] for i in comm["integrations"].values())
    if not _close(comm_sum, comm["total"]):
        issues += _fail(f"community_integrations: Summe {comm_sum} ≠ total {comm['total']}")
    g = co2["gesamt"]
    if not _close(dom_sum + comm["total"], g["reduktion_hart"]):
        issues += _fail(f"Domains {dom_sum:.2f} + Communities {comm['total']} ≠ reduktion_hart {g['reduktion_hart']}")
    if not _close(g["reduktion_hart"] + g["vermeidung_weich"], g["total_potenzial"]):
        issues += _fail(f"reduktion_hart + vermeidung_weich ≠ total_potenzial {g['total_potenzial']}")
    base = co2["validation"]["global_emissions_baseline"]
    if not _close(abs(g["reduktion_hart"]) / base, g["anteil_global_emissions"], 0.005):
        issues += _fail(f"anteil_global_emissions {g['anteil_global_emissions']} ≠ |reduktion_hart|/{base}")
    if issues == 0:
        print(f"  ✅ Domains {dom_sum:.1f} + Communities {comm['total']} = {g['reduktion_hart']} Gt; "
              f"Potenzial {g['total_potenzial']}; Anteil {g['anteil_global_emissions']}")
    return issues


def check_derived_counters(co2) -> int:
    banner("CHECK 6: Abgeleitete Zähler + ID-Eindeutigkeit")
    issues = 0
    domains = co2["domains"]
    apps = {k: v for d in domains.values() for k, v in (d.get("apps") or {}).items()}
    n_comm = len(co2["community_integrations"]["integrations"])
    n_apps = len(apps) + n_comm
    m = co2["metrics"]
    if m["anzahl_anwendungen"] != n_apps:
        issues += _fail(f"metrics.anzahl_anwendungen={m['anzahl_anwendungen']}, abgeleitet {n_apps} "
                        f"({len(apps)} apps + {n_comm} communities)")
    if m["anzahl_domains"] != len(domains):
        issues += _fail(f"metrics.anzahl_domains={m['anzahl_domains']}, abgeleitet {len(domains)}")
    ids = [k.split("_")[0] for k in apps]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        issues += _fail(f"doppelte Hebel-IDs: {dupes}")
    top_key, top_val = min(apps.items(), key=lambda x: x[1])
    h = m["hoechste_einzelanwendung"]
    if h["wert"] != top_val or not top_key.startswith(h["id"]):
        issues += _fail(f"hoechste_einzelanwendung {h['id']} ({h['wert']}) ≠ {top_key} ({top_val})")
    if issues == 0:
        print(f"  ✅ {n_apps} Anwendungen ({len(apps)} apps + {n_comm} communities), "
              f"{len(domains)} Domains, IDs eindeutig")
    return issues


def check_cross_file_sync(co2, imp) -> int:
    banner("CHECK 7: Cross-File-Sync co2_master.yaml ↔ impact_master.yaml")
    issues = 0
    ic = imp["ghg_accounting"]["co2"]
    for k, v in co2["gesamt"].items():
        if k in ic["gesamt"] and ic["gesamt"][k] != v:
            issues += _fail(f"gesamt.{k}: co2 {v} ≠ impact {ic['gesamt'][k]}")
    for k, d in co2["domains"].items():
        if ic["domains"].get(k) != d["total"]:
            issues += _fail(f"domains.{k}: co2 {d['total']} ≠ impact {ic['domains'].get(k)}")
    extra = set(ic["domains"]) - set(co2["domains"])
    if extra:
        issues += _fail(f"Domains nur in impact_master: {sorted(extra)}")
    ca, cb = co2["community_integrations"], imp["community_integrations"]
    if ca["total"] != cb["total"]:
        issues += _fail(f"community total: {ca['total']} ≠ {cb['total']}")
    for cid, a in ca["integrations"].items():
        b = cb["integrations"].get(cid)
        if b is None:
            issues += _fail(f"{cid} fehlt in impact_master")
            continue
        for fld in ("hash", "source_ref", "co2_impact_gt_per_year", "decision_date", "dossier"):
            if a.get(fld) != b.get(fld):
                issues += _fail(f"{cid}.{fld}: {a.get(fld)} ≠ {b.get(fld)}")
    if imp["ghg_accounting"]["ghg_total"]["co2"] != co2["gesamt"]["reduktion_hart"]:
        issues += _fail("ghg_total.co2 ≠ co2_master gesamt.reduktion_hart")
    if issues == 0:
        print("  ✅ Gesamt, Domain-Totals, Community-Integrationen und ghg_total.co2 synchron")
    return issues


def check_ghg(imp) -> int:
    banner("CHECK 8: GHG — GWP100 (IPCC AR6), Gas-Summen, Spanne, Rebound-Kette")
    issues = 0
    ga = imp["ghg_accounting"]
    ch4, n2o, fg = ga["methane_ch4"], ga["nitrous_oxide_n2o"], ga["f_gases"]
    if (ch4.get("gwp_factor_fossil") != GWP_AR6["ch4_fossil"]
            or ch4.get("gwp_factor_non_fossil") != GWP_AR6["ch4_non_fossil"]):
        issues += _fail(f"CH₄-GWP ≠ AR6 ({GWP_AR6['ch4_fossil']} fossil / {GWP_AR6['ch4_non_fossil']} non-fossil)")
    if n2o.get("gwp_factor") != GWP_AR6["n2o"]:
        issues += _fail(f"N₂O-GWP {n2o.get('gwp_factor')} ≠ AR6 {GWP_AR6['n2o']}")
    for key, d in ch4["domains"].items():
        if d.get("gwp_basis") not in ("fossil", "non_fossil"):
            issues += _fail(f"methane_ch4.{key}: gwp_basis fehlt/ungültig")
    for name, gas in (("methane_ch4", ch4), ("nitrous_oxide_n2o", n2o), ("f_gases", fg)):
        s = sum(d["total"] for d in gas["domains"].values())
        if not _close(s, gas["gesamt"], 0.02):
            issues += _fail(f"{name}: Summe Domains {s:.2f} ≠ gesamt {gas['gesamt']}")
        lo, hi = gas["unsicherheit"]
        if not (lo <= gas["gesamt"] <= hi):
            issues += _fail(f"{name}: gesamt {gas['gesamt']} außerhalb Unsicherheit [{lo}, {hi}]")
    gt = ga["ghg_total"]
    for comp, gas in (("ch4_co2eq", ch4), ("n2o_co2eq", n2o), ("f_gases_co2eq", fg)):
        if gt[comp] != gas["gesamt"]:
            issues += _fail(f"ghg_total.{comp} {gt[comp]} ≠ {gas['gesamt']}")
    # ghg_total: RANGE (Spanne volle ↔ keine Überlappung, total = null) oder CURRENT (Punktwert
    # innerhalb der Spanne) — siehe canon/decisions/DEC_2026-10-14_ghg_total_range.md
    status = gt.get("total_status")
    naive = gt["co2"] + gt["ch4_co2eq"] + gt["n2o_co2eq"] + gt["f_gases_co2eq"]
    if status == "RANGE":
        if gt.get("total") is not None:
            issues += _fail(f"ghg_total.total = {gt['total']}, bei total_status RANGE muss es null sein")
        if gt.get("range_lower_full_overlap") != gt["co2"]:
            issues += _fail(f"range_lower_full_overlap {gt.get('range_lower_full_overlap')} ≠ co2 {gt['co2']}")
        if not _close(gt.get("range_upper_no_overlap"), naive, 0.01):
            issues += _fail(f"range_upper_no_overlap {gt.get('range_upper_no_overlap')} ≠ naive Summe {naive:.2f}")
    elif status == "CURRENT":
        t = gt.get("total")
        if t is None or not (naive - TOL <= t <= gt["co2"] + TOL):
            issues += _fail(f"ghg_total.total {t} außerhalb der Spanne [{naive:.2f}, {gt['co2']}]")
    else:
        issues += _fail(f"ghg_total.total_status fehlt/ungültig: {status} (erlaubt: RANGE, CURRENT)")
    rb = imp["energy_system"]["rebound_effects"]
    if "adjusted_impact" in rb or "net_rebound_factor" in rb:
        issues += _fail("rebound_effects: Pauschalfaktor/adjusted_impact wieder vorhanden "
                        "(siehe canon/decisions/DEC_2026-10-14_rebound_single_source.md)")
    if status != "CURRENT" and rb.get("ghg_total_rebound") is not None:
        issues += _fail("rebound_effects.ghg_total_rebound gesetzt, obwohl ghg_total keinen Punktwert hat")
    if (rb.get("reporting") or {}).get("vor_rebound") != gt["co2"]:
        issues += _fail("rebound_effects.reporting.vor_rebound ≠ reduktion_hart")
    if issues == 0:
        shown = f"Spanne {naive:.2f} … {gt['co2']}" if status == "RANGE" else f"{gt['total']}"
        print(f"  ✅ GWP AR6, Gas-Summen konsistent; ghg_total [{status}] {shown}")
    return issues


def check_secj(imp) -> int:
    banner("CHECK 9: SEC-J — Formel, Veto, Warnschwelle")
    issues = 0
    s = imp["sec_j_scores"]
    veto, warn = s["meta"]["veto_threshold"], s["meta"]["warning_threshold"]
    constraints = s.get("implementation_constraints") or {}
    n = 0
    for key, v in s["individual_calculated"].items():
        if not isinstance(v, dict) or not all(x in v for x in ("s", "e", "c", "j", "sec_j")):
            continue
        n += 1
        j = v["j"]
        if j is not None and j < veto:
            if v["sec_j"] is not None:
                issues += _fail(f"{key}: J={j} < {veto} → SEC-J muss null sein (Veto), ist {v['sec_j']}")
            continue
        calc = 0.30 * v["s"] + 0.25 * v["e"] + 0.30 * v["c"] + 0.15 * v["j"]
        if abs(calc - v["sec_j"]) > 0.011:
            issues += _fail(f"{key}: SEC-J {v['sec_j']} ≠ STANDARD-Formel {calc:.3f}")
        if j is not None and j < warn and "warning" not in v and key.split("_")[0] not in constraints:
            issues += _fail(f"{key}: J={j} < {warn} ohne warning/implementation_constraint")
    if issues == 0:
        print(f"  ✅ {n} individuell berechnete Hebel: Formel, Veto und Warnschwelle konsistent")
    return issues


def check_sources(repo: Path, co2, imp) -> int:
    banner("CHECK 10: Quellen — Pfade + Hashes")
    issues = 0
    hex64 = re.compile(r"^[0-9a-f]{64}$")
    for label, data in (("co2", co2), ("impact", imp)):
        for cid, c in data["community_integrations"]["integrations"].items():
            h = c.get("hash")
            if not isinstance(h, str) or not hex64.match(h):
                issues += _fail(f"{label}:{cid}.hash kein SHA-256: {h}")
            for fld in ("dossier", "quelle"):
                path = c.get(fld)
                if path and not (repo / path).exists():
                    issues += _fail(f"{label}:{cid}.{fld} existiert nicht: {path}")
    single = imp["energy_system"]["rebound_effects"].get("single_source")
    if single and not (repo / single).exists():
        issues += _fail(f"rebound_effects.single_source existiert nicht: {single}")
    for rp in imp["sec_j_scores"]["meta"].get("audit_reports", []):
        if not (repo / rp).exists():
            issues += _fail(f"sec_j_scores.meta.audit_reports: {rp} existiert nicht")
    if issues == 0:
        print("  ✅ Alle referenzierten Repo-Pfade existieren, Hashes im SHA-256-Format")
    return issues


# Gas-Quelle in overlap_matrix.yaml → (Gas-Block in impact_master, Domain oder None = gesamt)
GAS_SOURCES = {
    "ch4_B_production": ("methane_ch4", "B_production"),
    "ch4_C_energy": ("methane_ch4", "C_energy"),
    "ch4_D_food_land": ("methane_ch4", "D_food_land"),
    "n2o_D_food_land": ("nitrous_oxide_n2o", "D_food_land"),
    "n2o_B_production": ("nitrous_oxide_n2o", "B_production"),
    "f_gases": ("f_gases", None),
}


def check_overlap_matrix(co2, imp, ovl) -> int:
    banner("CHECK 11: Overlap-Matrix — Hebel-Gruppen + Gas-Schicht + all-GHG-Punktwert")
    issues = 0
    # Teil 1: Hebel ↔ Hebel
    for dkey, g in ovl["lever_overlaps"].items():
        apps = (co2["domains"].get(dkey) or {}).get("apps") or {}
        missing = [m for m in g["group"] + g["additive"] if m not in apps]
        if missing:
            issues += _fail(f"{dkey}: unbekannte Hebel {missing}")
            continue
        if set(g["group"]) | set(g["additive"]) != set(apps):
            issues += _fail(f"{dkey}: group + additive decken nicht alle apps ab")
        gross = sum(abs(apps[m]) for m in g["group"])
        if not _close(gross, g["gross_sum"], 0.01):
            issues += _fail(f"{dkey}: gross_sum {g['gross_sum']} ≠ Summe group {gross:.2f}")
        if not _close(g["gross_sum"] - g["overlap"], g["net"], 0.01):
            issues += _fail(f"{dkey}: gross_sum − overlap ≠ net")
        domain_total = abs(co2["domains"][dkey]["total"])
        if not _close(g["net"] + sum(abs(apps[m]) for m in g["additive"]), domain_total, 0.01):
            issues += _fail(f"{dkey}: net + additive ≠ Domain-total {domain_total}")
        pc = g["pair_coefficients"]
        if pc != "not_sourced" and (not isinstance(pc, dict) or not _close(sum(pc.values()), g["overlap"], 0.01)):
            issues += _fail(f"{dkey}: pair_coefficients weder 'not_sourced' noch Summe = overlap")
    # Teil 2: CO₂eq-Schicht ↔ Gas-Schicht
    ga = imp["ghg_accounting"]
    gl = ovl["gas_layer_overlaps"]
    tot = belegt = 0.0
    for skey, (gas, dom) in GAS_SOURCES.items():
        s = gl.get(skey)
        if s is None:
            issues += _fail(f"gas_layer_overlaps.{skey} fehlt")
            continue
        val = abs(ga[gas]["gesamt"] if dom is None else ga[gas]["domains"][dom]["total"])
        if not _close(s["gas_total"], val, 0.01):
            issues += _fail(f"{skey}: gas_total {s['gas_total']} ≠ impact_master {val}")
        o = s["overlap_with_co2_layer"]
        if not (0 <= o <= s["gas_total"] + 0.01):
            issues += _fail(f"{skey}: overlap {o} außerhalb [0, gas_total]")
        lever = s.get("co2_lever")
        if o > 0:
            lever_val = next((abs(d["apps"][lever]) for d in co2["domains"].values()
                              if lever in (d.get("apps") or {})), None)
            if lever_val is None or o > lever_val + 0.01:
                issues += _fail(f"{skey}: overlap {o} > CO₂-Schicht-Wert von {lever}")
        tot += o
        if s["evidence"] == "belegt":
            belegt += o
    sm = gl["summary"]
    if not (_close(sm["overlap_total"], tot, 0.01) and _close(sm["overlap_belegt"], belegt, 0.01)
            and _close(sm["overlap_angenommen"], tot - belegt, 0.01)):
        issues += _fail("gas_layer_overlaps.summary passt nicht zu den Einzelquellen")
    gt = ga["ghg_total"]
    naive = gt["co2"] + gt["ch4_co2eq"] + gt["n2o_co2eq"] + gt["f_gases_co2eq"]
    if gt.get("total_status") == "CURRENT":
        if not _close(gt["total"], naive + tot, 0.01):
            issues += _fail(f"ghg_total.total {gt['total']} ≠ naive {naive:.2f} + Overlap {tot:.2f}")
        if not _close(gt.get("total_evidence_only"), naive + belegt, 0.01):
            issues += _fail(f"ghg_total.total_evidence_only ≠ naive + belegter Overlap ({naive + belegt:.2f})")
    # Teil 3: all-GHG-Monte-Carlo — YAML-Werte = Skript-Output (ghg_percentiles.csv)
    mcn = gt.get("monte_carlo_net")
    if mcn:
        import csv
        with open(REPO_ROOT / mcn["source"], encoding="utf-8") as f:
            rows = {r["scenario"][0]: r for r in csv.DictReader(f)}
        b = rows["B"]
        pairs = [("A_median", rows["A"]["ghg_p50"]), ("B_median", b["ghg_p50"]),
                 ("C_median", rows["C"]["ghg_p50"]), ("S_median", rows["S"]["ghg_p50"]),
                 ("B_median_rebound_on_gases", b["ghg_p50_rebound_on_gases"])]
        for k, v in pairs:
            if not _close(mcn.get(k), float(v), 0.05):
                issues += _fail(f"monte_carlo_net.{k} {mcn.get(k)} ≠ CSV {v}")
        if not (_close(mcn["B_ci90"][0], float(b["ghg_p5"]), 0.05) and _close(mcn["B_ci90"][1], float(b["ghg_p95"]), 0.05)):
            issues += _fail("monte_carlo_net.B_ci90 ≠ CSV p5/p95")
        if imp["energy_system"]["rebound_effects"].get("ghg_total_rebound") != mcn["B_median"]:
            issues += _fail("rebound_effects.ghg_total_rebound ≠ monte_carlo_net.B_median")
    if issues == 0:
        print(f"  ✅ Gruppen B/C/D arithmetisch konsistent; Gas-Overlap {tot:.1f} Gt "
              f"(belegt {belegt:.1f}); all-GHG {naive + tot:.2f}"
              + (f"; Monte-Carlo B {mcn['B_median']}" if mcn else ""))
    return issues


def main() -> int:
    print()
    print("═" * 78)
    print("  PROVOLUTION REPO SPEC-CONSISTENCY AUDIT")
    print("  'Probatio Consistentia' v0.3 · 2026-10-14")
    print("═" * 78)
    print(f"  Repo-Root: {REPO_ROOT}")

    ci = "--ci" in sys.argv

    advisory = 0
    advisory += check_secj_formulas(REPO_ROOT)
    advisory += check_deprecated_markers(REPO_ROOT)
    advisory += check_band4_secj_sync(REPO_ROOT)

    total = check_reduktion_hart_sync(REPO_ROOT)
    co2, imp = _load_yamls(REPO_ROOT)
    total += check_co2_aggregates(co2)
    total += check_derived_counters(co2)
    total += check_cross_file_sync(co2, imp)
    total += check_ghg(imp)
    total += check_secj(imp)
    total += check_sources(REPO_ROOT, co2, imp)
    total += check_overlap_matrix(co2, imp, _load_overlap(REPO_ROOT))

    if ci:
        if advisory:
            print()
            print(f"  ℹ️  {advisory} heuristische Hinweise (Checks 1/3/4) — im CI-Modus nicht blockierend")
    else:
        total += advisory

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
