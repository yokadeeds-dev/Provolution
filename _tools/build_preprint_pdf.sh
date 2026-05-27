#!/usr/bin/env bash
# Build a submission-ready PDF from a manuscript markdown source.
# Default target: EarthArXiv (single-column, 11pt, generous margins).
#
# Usage:
#   ./_tools/build_preprint_pdf.sh                  # builds default (BLIND draft)
#   ./_tools/build_preprint_pdf.sh attributed       # builds version with author names
#   ./_tools/build_preprint_pdf.sh blind            # explicit blind version
#
# Requirements:
#   - pandoc (tested with 3.x)
#   - a LaTeX engine (xelatex preferred; falls back to pdflatex)
#
# Output: _build_outputs/MANUSCRIPT_DRAFT_v0.1[_BLIND].pdf
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANUSCRIPT_DIR="$REPO_ROOT/manuscript"
OUT_DIR="$REPO_ROOT/_build_outputs"
mkdir -p "$OUT_DIR"

# Pick source
TARGET="${1:-blind}"
case "$TARGET" in
  blind)
    SRC="$MANUSCRIPT_DIR/MANUSCRIPT_DRAFT_v0.1_BLIND.md"
    OUT="$OUT_DIR/MANUSCRIPT_DRAFT_v0.1_BLIND.pdf"
    ;;
  attributed|named|signed)
    SRC="$MANUSCRIPT_DIR/MANUSCRIPT_DRAFT_v0.1.md"
    OUT="$OUT_DIR/MANUSCRIPT_DRAFT_v0.1.pdf"
    ;;
  *)
    echo "Unknown target: $TARGET. Use 'blind' or 'attributed'." >&2
    exit 1
    ;;
esac

if [ ! -f "$SRC" ]; then
  echo "Source not found: $SRC" >&2
  exit 2
fi

# Detect PDF engine
PDF_ENGINE="xelatex"
if ! command -v xelatex >/dev/null 2>&1; then
  if command -v pdflatex >/dev/null 2>&1; then
    PDF_ENGINE="pdflatex"
  else
    echo "Neither xelatex nor pdflatex found in PATH." >&2
    exit 3
  fi
fi

echo "[build] source:   $SRC"
echo "[build] target:   $OUT"
echo "[build] engine:   $PDF_ENGINE"

# Build flags
PANDOC_FLAGS=(
  --from=markdown+yaml_metadata_block+raw_tex
  --to=pdf
  --pdf-engine="$PDF_ENGINE"
  --resource-path="$MANUSCRIPT_DIR:$MANUSCRIPT_DIR/figures:$REPO_ROOT"
  -V geometry:margin=2.5cm
  -V fontsize=11pt
  -V linestretch=1.25
  -V documentclass=article
  -V papersize=a4
  -V colorlinks=true
  -V linkcolor=black
  -V urlcolor=black
  --toc
  --toc-depth=2
  --number-sections
)

# Font: by default no mainfont is set, so xelatex uses Latin Modern Roman —
# which has full Unicode math coverage (∈, ∀, ≥, ⊥, ∧, subscripts, Greek).
# Override with a serif font (e.g. "Times New Roman") via env if the journal
# requires it; be aware that math glyphs may then fall back or print as boxes.
#   MAINFONT="Times New Roman" ./_tools/build_preprint_pdf.sh
if [ -n "${MAINFONT:-}" ] && [ "$PDF_ENGINE" = "xelatex" ]; then
  PANDOC_FLAGS+=(-V mainfont="$MAINFONT")
fi

pandoc "$SRC" "${PANDOC_FLAGS[@]}" -o "$OUT"

echo "[build] OK: $OUT"
ls -lh "$OUT"
