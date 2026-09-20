#!/usr/bin/env bash
# B24-10 seal step: hashing and listing only (not a numerical run under G19).
# Writes results/b24_10/MANIFEST.json and prints every count into results/b24_10/SEAL_LOG.txt.
# Does not bind its own outputs (MANIFEST.json, SEAL_LOG.txt).
# No external sources: this slot fetched nothing and used no network.
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=results/b24_10/MANIFEST.json
LOG=results/b24_10/SEAL_LOG.txt
: > "$LOG"
log() { echo "$*" | tee -a "$LOG"; }

log "B24-10 seal, $(date -u +%FT%TZ)"
log "reviewer model: Opus 5 (1M context), model id claude-opus-5[1m]"
log "HEAD $(git rev-parse HEAD)  tree $(git rev-parse 'HEAD^{tree}')"
log "tracked changes: $(git status --porcelain --untracked-files=no | wc -l)"

# Written by this slot, plus the two pre-existing files the brief requires be bound.
# preverdicts_formed_before_reading.md and _v2.md were NOT created or edited by this slot.
LOCAL=(
  docs/b24_10_review.md
  analysis/b24_10_p1_arith.py
  analysis/b24_10_seal.sh
  results/b24_10/preverdicts_formed_before_reading_v3.md
  results/b24_10/preverdicts_formed_before_reading_v2.md
  results/b24_10/preverdicts_formed_before_reading.md
  results/b24_10/p1_arith.json
  results/logs/b24_10_p1_arith_resources.json
  results/logs/b24_10_p1_arith.pid
)

# Every commit:path this review ruled on, at the commit the B24-10 brief pins.
PINNED=(
  bc7e62b714632c20d2405e54030224a2549c242d:paper/det3-conductor.tex
  bc7e62b714632c20d2405e54030224a2549c242d:CHANGES.md
  bc7e62b714632c20d2405e54030224a2549c242d:GAPS.md
  bc7e62b714632c20d2405e54030224a2549c242d:READINESS.md
  bc7e62b714632c20d2405e54030224a2549c242d:README.md
  bc7e62b714632c20d2405e54030224a2549c242d:ATTRIBUTION_PATCH.md
  f8273c3b5542fe085c596e3814c45621d3608ca7:docs/b24_02_report.md
  f8273c3b5542fe085c596e3814c45621d3608ca7:results/b24_02/MANIFEST.json
  f8273c3b5542fe085c596e3814c45621d3608ca7:results/b24_02/p1_n5_kleiman.json
  f8273c3b5542fe085c596e3814c45621d3608ca7:results/b24_02/p1_prereg.md
  f8273c3b5542fe085c596e3814c45621d3608ca7:analysis/b24_02_p1_n5_kleiman.py
  5a97317e7e28753261cf6e8dcece180a0e71b718:docs/b24_02b_report.md
  5a97317e7e28753261cf6e8dcece180a0e71b718:results/b24_02b/MANIFEST.json
  f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c:papers/det4-blindness/det4-blindness.tex
  f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c:papers/det4-blindness/CLAIMS.md
  f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c:papers/det4-blindness/GAPS.md
  f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c:papers/det4-blindness/BIB.md
  f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c:papers/det4-blindness/DIFF_NOTES.md
  aafcbb692375f0a968881dbf18963a74d62ab557:docs/b24_04_report.md
  aafcbb692375f0a968881dbf18963a74d62ab557:results/b24_04/MANIFEST.json
  5c5ba86edd318d349b858c5c99df27b6be9355c2:docs/b24_05_report.md
  5c5ba86edd318d349b858c5c99df27b6be9355c2:results/b24_05/MANIFEST.json
  0019b2e2359eeabe065dad4271b89f06e2553896:PAPER2_BLOCKERS.md
  0019b2e2359eeabe065dad4271b89f06e2553896:PAPER2_CLAIMS.md
  0019b2e2359eeabe065dad4271b89f06e2553896:PAPER2_GAPS.md
  0019b2e2359eeabe065dad4271b89f06e2553896:PAPER2_READINESS.md
  744eb77b70cbb237d26c945695b264d4a4b9b402:docs/b24_12_ledger.md
  744eb77b70cbb237d26c945695b264d4a4b9b402:docs/b23_12_ledger.md
  239dd6e84417ab04914a8d84cca02ddf754bf1fb:docs/b23_10_review.md
)

# Files whose ABSENCE is part of a ruling (11.4.1): B24-01 has no packet.
ABSENT=(
  "bc7e62b714632c20d2405e54030224a2549c242d|docs/b24_01_report.md"
  "bc7e62b714632c20d2405e54030224a2549c242d|results/b24_01/MANIFEST.json"
)

{
  echo "{"
  echo " \"slot\": \"B24-10\","
  echo " \"reviewer_model\": \"Opus 5 (1M context)\","
  echo " \"reviewer_model_id\": \"claude-opus-5[1m]\","
  echo " \"sealed_utc\": \"$(date -u +%FT%TZ)\","
  echo " \"head\": \"$(git rev-parse HEAD)\","
  echo " \"tree\": \"$(git rev-parse 'HEAD^{tree}')\","
  echo " \"git_mode\": \"read-only: no commit, no push, no fetch\","
  echo " \"pilots_used\": 1,"
  echo " \"pilots_allowed\": 3,"
  echo " \"external_sources\": \"none - this slot used no network\","
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
  echo " \"verified_absent\": ["
  a=0
  for s in "${ABSENT[@]}"; do
    c=${s%%|*}; p=${s#*|}
    if git cat-file -e "$c:$p" 2>/dev/null; then st="PRESENT - ruling 11.4.1 would be wrong"; else st="absent"; fi
    [ $a -gt 0 ] && echo ","
    printf '  {"commit": "%s", "path": "%s", "status": "%s"}' "$c" "$p" "$st"
    a=$((a+1))
  done
  echo ""
  echo " ]"
  echo "}"
} > "$OUT"

log ""
log "local files bound: ${#LOCAL[@]}"
for f in "${LOCAL[@]}"; do
  log "  $(sha256sum "$f" | cut -c1-64)  $(wc -c < "$f" | tr -d ' ')  $f"
done
log ""
log "pinned inputs bound: ${#PINNED[@]}"
for s in "${PINNED[@]}"; do
  c=${s%%:*}; p=${s#*:}
  log "  $(git show "$c:$p" | sha256sum | cut -c1-64)  $(git show "$c:$p" | wc -c | tr -d ' ')  ${c:0:8}:$p"
done
log ""
log "verified-absent paths: ${#ABSENT[@]}"
for s in "${ABSENT[@]}"; do
  c=${s%%|*}; p=${s#*|}
  if git cat-file -e "$c:$p" 2>/dev/null; then log "  PRESENT  ${c:0:8}:$p"; else log "  absent   ${c:0:8}:$p"; fi
done
log ""
log "the two files this slot bound but did NOT create or edit:"
for f in results/b24_10/preverdicts_formed_before_reading.md \
         results/b24_10/preverdicts_formed_before_reading_v2.md; do
  log "  $(sha256sum "$f" | cut -c1-64)  $(wc -c < "$f" | tr -d ' ')  $f"
done
log ""
IGN=$(git check-ignore results/logs/b24_10_*.pid 2>/dev/null | wc -l | tr -d ' ')
log "ignored receipts: $IGN"
if [ "$IGN" -gt 0 ]; then log "  negation missing for b24_10_"; fi
log ""
log "counts: local=${#LOCAL[@]} pinned=${#PINNED[@]} absent=${#ABSENT[@]} external=0 pilots=1 ignored_receipts=$IGN"
log "MANIFEST.json sha256 $(sha256sum "$OUT" | cut -c1-64) (not self-bound)"
