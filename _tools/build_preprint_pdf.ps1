# Build a submission-ready PDF from a manuscript markdown source.
# Windows PowerShell wrapper for build_preprint_pdf.sh logic.
#
# Usage:
#   .\_tools\build_preprint_pdf.ps1               # blind version (default)
#   .\_tools\build_preprint_pdf.ps1 -Target attributed
#
# Requirements:
#   - pandoc in PATH (winget install JohnMacFarlane.Pandoc)
#   - xelatex via MiKTeX in PATH

param(
    [ValidateSet('blind', 'attributed')]
    [string]$Target = 'blind'
)

$ErrorActionPreference = 'Stop'

$repoRoot     = (Resolve-Path "$PSScriptRoot\..").Path
$manuscriptDir = Join-Path $repoRoot 'manuscript'
$outDir       = Join-Path $repoRoot '_build_outputs'
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

switch ($Target) {
    'blind'      { $srcName = 'MANUSCRIPT_DRAFT_v0.1_BLIND.md'; $outName = 'MANUSCRIPT_DRAFT_v0.1_BLIND.pdf' }
    'attributed' { $srcName = 'MANUSCRIPT_DRAFT_v0.1.md';       $outName = 'MANUSCRIPT_DRAFT_v0.1.pdf' }
}

$src = Join-Path $manuscriptDir $srcName
$out = Join-Path $outDir $outName

if (-not (Test-Path $src)) {
    Write-Error "Source not found: $src"
    exit 2
}

# Detect PDF engine
$pdfEngine = 'xelatex'
if (-not (Get-Command xelatex -ErrorAction SilentlyContinue)) {
    if (Get-Command pdflatex -ErrorAction SilentlyContinue) {
        $pdfEngine = 'pdflatex'
    } else {
        Write-Error "Neither xelatex nor pdflatex found in PATH."
        exit 3
    }
}

Write-Host "[build] source: $src"
Write-Host "[build] target: $out"
Write-Host "[build] engine: $pdfEngine"

$resourcePath = "$manuscriptDir;$(Join-Path $manuscriptDir 'figures');$repoRoot"

$pandocArgs = @(
    '--from=markdown+yaml_metadata_block+raw_tex',
    '--to=pdf',
    "--pdf-engine=$pdfEngine",
    "--resource-path=$resourcePath",
    '-V', 'geometry:margin=2.5cm',
    '-V', 'fontsize=11pt',
    '-V', 'linestretch=1.25',
    '-V', 'documentclass=article',
    '-V', 'papersize=a4',
    '-V', 'colorlinks=true',
    '-V', 'linkcolor=black',
    '-V', 'urlcolor=black',
    '--toc',
    '--toc-depth=2',
    '--number-sections'
)

# By default no mainfont is set — xelatex falls back to Latin Modern Roman,
# which carries full Unicode math coverage (∈, ∀, ≥, ⊥, ∧, subscripts, Greek).
# To override with a serif font, set $env:MAINFONT = 'Times New Roman' first.
if ($env:MAINFONT -and $pdfEngine -eq 'xelatex') {
    $pandocArgs += @('-V', "mainfont=$($env:MAINFONT)")
}

& pandoc $src @pandocArgs -o $out

Write-Host "[build] OK: $out"
Get-Item $out | Select-Object Name, Length, LastWriteTime | Format-Table -AutoSize
