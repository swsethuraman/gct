#!/usr/bin/env bash
# B24-02 seal step: hashing and listing only (not a numerical run under G19).
# Writes results/b24_02/MANIFEST.json and prints every count into results/b24_02/SEAL_LOG.txt.
# Binds neither of its own outputs (MANIFEST.json, SEAL_LOG.txt).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=results/b24_02/MANIFEST.json
LOG=results/b24_02/SEAL_LOG.txt
: > "$LOG"
log() { echo "$*" | tee -a "$LOG"; }

log "B24-02 seal, $(date -u +%FT%TZ)"
log "HEAD $(git rev-parse HEAD)  tree $(git rev-parse 'HEAD^{tree}')"
log "tracked changes: $(git status --porcelain --untracked-files=no | wc -l)"

LOCAL=(
  docs/b24_02_report.md
  analysis/b24_02_p1_n5_kleiman.py
  analysis/b24_02_seal.sh
  results/b24_02/p1_prereg.md
  results/b24_02/p1_n5_kleiman.json
  results/logs/b24_02_p1_n5_kleiman_resources.json
  results/logs/b24_02_p1_n5_kleiman.pid
)
PINNED=(
  239dd6e84417ab04914a8d84cca02ddf754bf1fb:docs/b23_10_review.md
  3bcad66601a586936ce5c76fdf72d9551700dab3:docs/b23_03_report.md
  3bcad66601a586936ce5c76fdf72d9551700dab3:results/b23_03/p2_certificates_and_thresholds.json
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/CLAIMS.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/GAPS.md
  feed104ea865ed5f76809f6d77455060af01433c:docs/b23_06_report.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/s73_report.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/lmr_cell.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/equation_census.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/s62_report.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/s63_report.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/astra_gkz_degenerations_20260917/REPORT.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/CORRIGENDUM.md
)

{
  echo "{"
  echo " \"slot\": \"B24-02\","
  echo " \"sealed_utc\": \"$(date -u +%FT%TZ)\","
  echo " \"head\": \"$(git rev-parse HEAD)\","
  echo " \"tree\": \"$(git rev-parse 'HEAD^{tree}')\","
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
  echo " \"external_sources\": [],"
  echo " \"external_sources_note\": \"None reached in this slot. The LMR read-status finding of section 2 is a statement about the record, not a new reading; no PDF or HTML was fetched.\""
  echo "}"
} > "$OUT"

log "local files bound: ${#LOCAL[@]}"
for f in "${LOCAL[@]}"; do log "  $(sha256sum "$f" | cut -c1-64)  $f"; done
log "pinned inputs bound: ${#PINNED[@]}"
for s in "${PINNED[@]}"; do
  c=${s%%:*}; p=${s#*:}
  log "  $(git show "$(git rev-parse "$c^{commit}"):$p" | sha256sum | cut -c1-64)  $c:$p"
done
log "external sources bound: 0"
log "receipts ignored (negation missing for b24_02_): $(git check-ignore results/logs/b24_02_*.pid | wc -l)"
log "MANIFEST.json sha256 $(sha256sum "$OUT" | cut -c1-64) (not self-bound)"
