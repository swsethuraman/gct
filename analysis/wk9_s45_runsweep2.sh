#!/bin/bash
# Session 45 -- continuation of the pre-registered sweep for the two remaining
# cells, at the session-42 level set ((12,2), uncompressed).  Measured reason:
# the cheap level (3,2) samples 3 n_chi of the n_rows rows of E, and at cells
# with n_rows / n_chi >= 12 that loses rank (at (8,8,6,2,2,2)_7 the compressed
# matrix came out 57 short of full column rank), so the run is spent and then
# escalated.  Starting at (12,2) skips the wasted pass.  Both scripts are
# resumable: a cell already in results/s45_cells.jsonl is skipped.
cd /home/claude/gct
export WIED_BIN=/home/claude/wied45 WIED_WORK=/home/claude/s45/work
ulimit -v 6500000
CELLS=("8 9 9 9 3 1 1" "7 6 6 6 6 2 2")
for cell in "${CELLS[@]}"; do
  tag=$(echo "$cell" | tr ' ' '_')
  echo "=== CELL $cell (levels s42)  $(date -u +%FT%TZ) ==="
  timeout 39600 python3 analysis/wk9_s45_sweep.py $cell --levels s42 > results/logs/cell_$tag.log 2>&1 &
  pid=$!; echo $pid > results/logs/cell_$tag.pid
  wait $pid; rc=$?
  tail -6 results/logs/cell_$tag.log; echo "--- rc=$rc"
  if grep -q "the sweep HALTS here" results/logs/cell_$tag.log; then
    echo "*** HALT: determinant-side nullity > 0 at $cell ***"; break
  fi
  git add -A results/s45_cells.jsonl results/logs/cell_$tag.log results/logs/cell_$tag.pid 2>/dev/null
  git -c user.name="s45" -c user.email="s45@local" commit -q -m "s45 sweep: banked cell $cell

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" 2>/dev/null
done
echo "SWEEP2 LOOP DONE $(date -u +%FT%TZ)"
