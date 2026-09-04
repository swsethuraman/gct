#!/bin/bash
# Session 45 -- the pre-registered sweep, one heavy cell at a time.
# Each cell: `timeout` + `ulimit -v`, pid recorded, result appended to
# results/s45_cells.jsonl.  Halts on any determinant-side nullity > 0
# (pre-registered stopping rule 3).
cd /home/claude/gct
export WIED_BIN=/home/claude/wied45 WIED_WORK=/home/claude/s45/work
ulimit -v 6500000
# "delta lam... | extra flags"
CELLS=(
 "8 12 12 3 3 1 1|--full-check"
 "7 9 9 4 4 1 1|--full-check"
 "7 9 9 6 2 1 1|--full-check"
 "7 8 8 5 5 1 1|"
 "7 8 8 7 3 1 1|"
 "7 7 7 6 6 1 1|"
 "7 8 8 6 2 2 2|"
 "8 9 9 9 3 1 1|"
 "7 6 6 6 6 2 2|"
)
for spec in "${CELLS[@]}"; do
  cell="${spec%%|*}"; flags="${spec##*|}"
  tag=$(echo "$cell" | tr ' ' '_')
  echo "=== CELL $cell $flags  $(date -u +%FT%TZ) ==="
  timeout 39600 python3 analysis/wk9_s45_sweep.py $cell $flags > results/logs/cell_$tag.log 2>&1 &
  pid=$!; echo $pid > results/logs/cell_$tag.pid
  wait $pid; rc=$?
  tail -40 results/logs/cell_$tag.log
  echo "--- rc=$rc"
  if grep -q "the sweep HALTS here" results/logs/cell_$tag.log; then
    echo "*** HALT: determinant-side nullity > 0 at $cell ***"; break
  fi
  git add -A results/s45_cells.jsonl results/logs/cell_$tag.log results/logs/cell_$tag.pid 2>/dev/null
  git -c user.name="s45" -c user.email="s45@local" commit -q -m "s45 sweep: banked cell $cell

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" 2>/dev/null
done
echo "SWEEP LOOP DONE $(date -u +%FT%TZ)"
