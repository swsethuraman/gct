#!/usr/bin/env bash
# B23-10 seal step: hashing and listing only (not a numerical run under G19).
# Writes results/b23_10/MANIFEST.json and prints every count into results/b23_10/SEAL_LOG.txt.
# Binds neither itself's outputs (MANIFEST.json, SEAL_LOG.txt).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=results/b23_10/MANIFEST.json
LOG=results/b23_10/SEAL_LOG.txt
SCR="${B23_10_SCRATCH:?set B23_10_SCRATCH to the scratchpad bi/ directory}"
: > "$LOG"
log() { echo "$*" | tee -a "$LOG"; }

log "B23-10 seal, $(date -u +%FT%TZ)"
log "HEAD $(git rev-parse HEAD)  tree $(git rev-parse 'HEAD^{tree}')"
log "tracked changes: $(git status --porcelain --untracked-files=no | wc -l)"

LOCAL=(
  docs/b23_10_review.md
  analysis/b23_10_p1_witness_tail_height.py
  analysis/b23_10_p2_washout_replay.py
  analysis/b23_10_p3_det_floor_replay.py
  analysis/b23_10_seal.sh
  results/b23_10/preverdicts_formed_before_reading.md
  results/b23_10/p3_prereg.md
  results/b23_10/p1_witness_tail_height.json
  results/b23_10/p2_washout_replay.json
  results/b23_10/p3_det_floor_replay.json
  results/logs/b23_10_p1_witness_tail_height_resources.json
  results/logs/b23_10_p1_witness_tail_height.pid
  results/logs/b23_10_p2_washout_replay_resources.json
  results/logs/b23_10_p2_washout_replay.pid
  results/logs/b23_10_p3_det_floor_replay_resources.json
  results/logs/b23_10_p3_det_floor_replay.pid
)
PINNED=(
  3bcad66601a586936ce5c76fdf72d9551700dab3:docs/b23_03_report.md
  3bcad66601a586936ce5c76fdf72d9551700dab3:results/b23_03/MANIFEST.json
  3bcad66601a586936ce5c76fdf72d9551700dab3:results/b23_03/p1_classification.json
  3bcad66601a586936ce5c76fdf72d9551700dab3:results/b23_03/p2_certificates_and_thresholds.json
  cc14e88cca7860b4a666ecf2bc18701ac8a05584:docs/b23_01_report.md
  cc14e88cca7860b4a666ecf2bc18701ac8a05584:results/b23_01/preregistration_snapshot.md
  cc14e88cca7860b4a666ecf2bc18701ac8a05584:results/b23_01/p1_secondprime.json
  cc14e88cca7860b4a666ecf2bc18701ac8a05584:results/b23_01/MANIFEST.json
  68866e6ddc4deb38ac1fa29ffc1294395178357a:docs/b23_02_report.md
  feed104ea865ed5f76809f6d77455060af01433c:docs/b23_06_report.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/CLAIMS.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/GAPS.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/BIB.md
  ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a:papers/det4-blindness/det4-blindness.tex
  bbd1d12e80ae162feb368f75c9c270ccf79747f8:READINESS.md
  bbd1d12e80ae162feb368f75c9c270ccf79747f8:GAPS.md
  bbd1d12e80ae162feb368f75c9c270ccf79747f8:CHANGES.md
  bbd1d12e80ae162feb368f75c9c270ccf79747f8:paper/det3-conductor.tex
  60a88025c7f6fd61f42af69df60832d6df4d8e35:docs/b23_12_ledger.md
  2efb7aaf1927e8d2785dfbbcc78b847592c204f5:docs/b22_10_review.md
  2efb7aaf1927e8d2785dfbbcc78b847592c204f5:analysis/b22_10_p2_D45_cap_P5.py
  2efb7aaf1927e8d2785dfbbcc78b847592c204f5:results/b22_10/p2_D45_cap_P5.json
  f7727cb7:docs/b21_10_review.md
  6915ae6f:docs/b20_10_review.md
  e22a41b1:docs/b22_02_report.md
  82633a60893236fab4fbc317df416e1b8a349005:paper/det3-conductor.tex
  82633a60893236fab4fbc317df416e1b8a349005:docs/washout_lemma.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/obstruction_power.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/lmr_cell.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/s62_report.md
  82633a60893236fab4fbc317df416e1b8a349005:PROJECT_NOTES.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/astra_gkz_degenerations_20260917/REPORT.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/CORRIGENDUM.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_source_vectors_20260917/routeA_signfilter_20260917/REPORT.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_source_vectors_20260917/routeA_signfilter_20260917/certificates/arc_rows_and_sampled_kernel_candidate.json
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_source_vectors_20260917/arc_target_dimension_followup/CORRIGENDUM.md
  82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_source_vectors_20260917/final_arc_diagnostic/CURRENT_DIAGNOSTIC_STATE.md
)
EXTERNAL=(
  "bi_v2.pdf|arXiv:1511.02927v2 PDF (Buergisser-Ikenmeyer)"
  "bi_v1.pdf|arXiv:1511.02927v1 PDF"
  "bi_ar5iv.html|ar5iv rendering of 1511.02927 (text read)"
  "bi_text.txt|tag-stripped text of bi_ar5iv.html"
  "lands_ar5iv.html|ar5iv rendering of Landsberg arXiv:1305.7387"
  "abv_ar5iv.html|ar5iv rendering of Alper-Bogart-Velasco arXiv:1505.02205"
)

{
  echo "{"
  echo " \"slot\": \"B23-10\","
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
  echo " \"external_sources\": ["
  e=0
  for s in "${EXTERNAL[@]}"; do
    f=${s%%|*}; d=${s#*|}
    h=$(sha256sum "$SCR/$f" | cut -c1-64); b=$(wc -c < "$SCR/$f" | tr -d ' ')
    [ $e -gt 0 ] && echo ","
    printf '  {"file": "%s", "what": "%s", "sha256": "%s", "bytes": %s}' "$f" "$d" "$h" "$b"
    e=$((e+1))
  done
  echo ""
  echo " ]"
  echo "}"
} > "$OUT"

log "local files bound: ${#LOCAL[@]}"
for f in "${LOCAL[@]}"; do log "  $(sha256sum "$f" | cut -c1-64)  $f"; done
log "pinned inputs bound: ${#PINNED[@]}"
log "external sources bound: ${#EXTERNAL[@]}"
for s in "${EXTERNAL[@]}"; do f=${s%%|*}; log "  $(sha256sum "$SCR/$f" | cut -c1-64)  $f"; done
log "ignored receipts (negation missing for b23_10_): $(git check-ignore results/logs/b23_10_*.pid | wc -l)"
log "MANIFEST.json sha256 $(sha256sum "$OUT" | cut -c1-64) (not self-bound)"
