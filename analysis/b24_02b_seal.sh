#!/usr/bin/env bash
# B24-02b seal step: hashing and listing only. No numerical run, no interpreter.
# Writes results/b24_02b/MANIFEST.json and results/b24_02b/SEAL_LOG.txt.
# Binds neither of its own outputs (MANIFEST.json, SEAL_LOG.txt).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=results/b24_02b/MANIFEST.json
LOG=results/b24_02b/SEAL_LOG.txt
SCR="${B24_02B_SCRATCH:?set B24_02B_SCRATCH to the scratchpad b24_02b directory}"
: > "$LOG"
log() { echo "$*" | tee -a "$LOG"; }

log "B24-02b seal, $(date -u +%FT%TZ)"
log "HEAD $(git rev-parse HEAD)  tree $(git rev-parse 'HEAD^{tree}')"
log "tracked changes: $(git status --porcelain --untracked-files=no | wc -l)"

LOCAL=(
  docs/b24_02b_report.md
  analysis/b24_02b_seal.sh
  results/b24_02b/lmr_quotes.md
)
PINNED=(
  82633a60893236fab4fbc317df416e1b8a349005:docs/equation_census.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/lmr_cell.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/s73_report.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/CLAIMS.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/GAPS.md
  feed104ea865ed5f76809f6d77455060af01433c:docs/b23_06_report.md
  feed104ea865ed5f76809f6d77455060af01433c:results/b23_06/MANIFEST.json
  239dd6e84417ab04914a8d84cca02ddf754bf1fb:docs/b23_10_review.md
)
# External sources: hashed here, kept in the scratchpad literature cache, not the delivery tree.
EXTERNAL=(
  "lmr_v1.pdf|arXiv:1004.4802v1 PDF (Landsberg-Manivel-Ressayre); v1 is the only version"
  "lmr_ar5iv.html|ar5iv rendering of arXiv:1004.4802 (the text actually read)"
  "lmr_text.txt|tag-stripped text of lmr_ar5iv.html (sed/tr)"
  "abs.html|arXiv abstract page, read for the version history"
)
# The hash B23-06 recorded for the same PDF, re-asserted here for byte comparison.
RECORDED_LMR=cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79

{
  echo "{"
  echo " \"slot\": \"B24-02b\","
  echo " \"sealed_utc\": \"$(date -u +%FT%TZ)\","
  echo " \"head\": \"$(git rev-parse HEAD)\","
  echo " \"tree\": \"$(git rev-parse 'HEAD^{tree}')\","
  echo " \"numerical_runs\": 0,"
  echo " \"interpreter_launches\": 0,"
  echo " \"receipts\": \"none produced; negation missing for b24_02b_\","
  echo " \"files\": ["
  n=0
  for f in "${LOCAL[@]}"; do
    h=$(sha256sum "$f" | cut -c1-64); b=$(wc -c < "$f" | tr -d ' ')
    [ $n -gt 0 ] && echo ","
    printf '  {"path": "%s", "sha256": "%s", "bytes": %s}' "$f" "$h" "$b"
    n=$((n+1))
  done
  echo ""
  echo " ],"
  echo " \"pinned_inputs\": ["
  m=0
  for s in "${PINNED[@]}"; do
    c=${s%%:*}; p=${s#*:}
    full=$(git rev-parse "$c^{commit}")
    h=$(git show "$full:$p" | sha256sum | cut -c1-64); b=$(git show "$full:$p" | wc -c | tr -d ' ')
    [ $m -gt 0 ] && echo ","
    printf '  {"commit": "%s", "path": "%s", "sha256": "%s", "bytes": %s}' "$full" "$p" "$h" "$b"
    m=$((m+1))
  done
  echo ""
  echo " ],"
  echo " \"external_sources\": ["
  e=0
  for s in "${EXTERNAL[@]}"; do
    f=${s%%|*}; d=${s#*|}
    h=$(sha256sum "$SCR/$f" | cut -c1-64); b=$(wc -c < "$SCR/$f" | tr -d ' ')
    [ $e -gt 0 ] && echo ","
    printf '  {"file": "%s", "what": "%s", "sha256": "%s", "bytes": %s, "location": "scratchpad literature cache, not the delivery tree"}' "$f" "$d" "$h" "$b"
    e=$((e+1))
  done
  echo ""
  echo " ],"
  LMRH=$(sha256sum "$SCR/lmr_v1.pdf" | cut -c1-64)
  echo " \"lmr_byte_verification\": {"
  echo "  \"recorded_by\": \"feed104ea865ed5f76809f6d77455060af01433c:results/b23_06/MANIFEST.json\","
  echo "  \"recorded_sha256\": \"$RECORDED_LMR\","
  echo "  \"fetched_sha256\": \"$LMRH\","
  echo "  \"match\": $([ "$LMRH" = "$RECORDED_LMR" ] && echo true || echo false)"
  echo " },"
  echo " \"read_status\": {"
  echo "  \"source\": \"arXiv:1004.4802v1 (Landsberg-Manivel-Ressayre)\","
  echo "  \"label\": \"PRIMARY\","
  echo "  \"sections_read\": [\"1 (Thm 1.0.2)\", \"2.3 (Thm 2.3.1 and scope)\", \"3.1 (Thm 3.1.1)\", \"3.2 (ideal statement and the n=3 example)\"],"
  echo "  \"proofs_audited\": false,"
  echo "  \"point_of_use\": \"C45 base rung i_det((19,7,2^5),12) >= 1; see docs/b24_02b_report.md section 3.2\""
  echo " }"
  echo "}"
} > "$OUT"

log "local files bound: ${#LOCAL[@]}"
for f in "${LOCAL[@]}"; do log "  $(sha256sum "$f" | cut -c1-64)  $f"; done
log "pinned inputs bound: ${#PINNED[@]}"
for s in "${PINNED[@]}"; do
  c=${s%%:*}; p=${s#*:}
  log "  $(git show "$(git rev-parse "$c^{commit}"):$p" | sha256sum | cut -c1-64)  $c:$p"
done
log "external sources bound: ${#EXTERNAL[@]}"
for s in "${EXTERNAL[@]}"; do f=${s%%|*}; log "  $(sha256sum "$SCR/$f" | cut -c1-64)  $f"; done
LMRH=$(sha256sum "$SCR/lmr_v1.pdf" | cut -c1-64)
log "LMR byte check vs B23-06 record: $([ "$LMRH" = "$RECORDED_LMR" ] && echo MATCH || echo MISMATCH)"
log "numerical runs: 0; interpreter launches: 0; receipts produced: 0 (negation missing for b24_02b_)"
log "B24-02 packet untouched: docs/b24_02_report.md $(sha256sum docs/b24_02_report.md | cut -c1-64)"
log "MANIFEST.json sha256 $(sha256sum "$OUT" | cut -c1-64) (not self-bound)"
