#!/usr/bin/env bash
# B24-04 seal step: hashing and listing only (not a numerical run under G19).
# Writes results/b24_04/MANIFEST.json and results/b24_04/SEAL_LOG.txt.
# Binds neither of its own outputs (MANIFEST.json, SEAL_LOG.txt).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=results/b24_04/MANIFEST.json
LOG=results/b24_04/SEAL_LOG.txt
: > "$LOG"
log() { echo "$*" | tee -a "$LOG"; }

log "B24-04 seal, $(date -u +%FT%TZ)"
log "HEAD $(git rev-parse HEAD)  tree $(git rev-parse 'HEAD^{tree}')"
log "tracked changes: $(git status --porcelain --untracked-files=no | wc -l)"

FILES=(
  docs/b24_04_report.md
  analysis/b24_04_p1_patterns.py
  analysis/b24_04_p2_saturate.py
  analysis/b24_04_p3_close.py
  analysis/b24_04_seal.sh
  results/b24_04/PREREG_b24_04_p1.md
  results/b24_04/PREREG_b24_04_p2.md
  results/b24_04/PREREG_b24_04_p3.md
  results/b24_04/p1_patterns.json
  results/b24_04/p2_saturate.json
  results/b24_04/p3_close.json
  results/logs/b24_04_p1_patterns_resources.json
  results/logs/b24_04_p2_saturate_resources.json
  results/logs/b24_04_p3_close_resources.json
  results/logs/b24_04_p1_patterns.pid
  results/logs/b24_04_p2_saturate.pid
  results/logs/b24_04_p3_close.pid
)

{
  echo '{'
  echo '  "packet": "b24_04",'
  echo "  \"generated_utc\": \"$(date -u +%FT%TZ)\","
  echo '  "worktree": "work/batch15_workers/B15-02",'
  echo "  \"branch\": \"$(git rev-parse --abbrev-ref HEAD)\","
  echo "  \"head\": \"$(git rev-parse HEAD)\","
  echo '  "algorithm": "sha256",'
  echo '  "excluded_from_manifest": ["results/b24_04/MANIFEST.json", "results/b24_04/SEAL_LOG.txt"],'
  echo '  "excluded_reason": "a manifest cannot bind itself or the log written beside it",'
  echo '  "gitignore_note": "negation missing for b24_04_ (results/logs/*.pid is ignored)",'
  echo '  "files": {'
  first=1
  for f in "${FILES[@]}"; do
    [ -f "$f" ] || { echo "MISSING $f" >> "$LOG"; continue; }
    h=$(sha256sum "$f" | cut -d' ' -f1)
    b=$(wc -c < "$f" | tr -d ' ')
    [ $first -eq 1 ] || echo '    ,'
    first=0
    echo "    \"$f\": {\"sha256\": \"$h\", \"bytes\": $b}"
    echo "  $h  $b  $f" >> "$LOG"
  done
  echo '  },'
  echo '  "pinned_inputs": {'
  echo '    "analysis/b22_01_typed_v2.py": {"sha256": "93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc", "bytes": 13226, "bound_by": "results/b22_01/MANIFEST.json at 53bdb31e3042acae9464f9025be355ae699a2485"},'
  echo '    "results/b22_01/p2_basis.json": {"sha256": "7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79", "bytes": 293596, "bound_by": "results/b22_01/MANIFEST.json at 53bdb31e3042acae9464f9025be355ae699a2485"},'
  echo '    "analysis/b15_bound.py": {"sha256": "'"$(sha256sum analysis/b15_bound.py | cut -d' ' -f1)"'", "note": "the wrapper (G19)"},'
  echo '    "lit/bdi_2002.11594v2.pdf": {"sha256": "5371f3b62964f221b248334bec54d453a5bdcca4f2980c854cee41183f1317b6", "bytes": 513636, "note": "session scratchpad, not in the tree; https://arxiv.org/pdf/2002.11594v2"},'
  echo '    "lit/bdi_ar5iv.html": {"sha256": "31c8a74500d961b8e60e29daf8a780917700a1ad2fa1f2a5f383b1b454cde23b", "bytes": 1630516, "note": "session scratchpad, not in the tree; https://ar5iv.labs.arxiv.org/html/2002.11594"}'
  echo '  },'
  echo '  "generator": "analysis/b24_04_seal.sh"'
  echo '}'
} > "$OUT"

log "manifest written to $OUT"
log "HEAD after $(git rev-parse HEAD)"
