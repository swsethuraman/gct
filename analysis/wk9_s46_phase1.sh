#!/bin/bash
# Session 46 -- Phase 1 validation V1 (three banked s45 rows), V2 (the
# discriminating pad-side drop cell) and V3 (level agreement).  One process per
# cell, so the recorded HWM is the cell's own peak.  Every run is bounded at
# launch and its process id is written to results/logs/.
set -u
cd "$(dirname "$0")"
OUT=../results/s46_v123.jsonl
LOG=../results/logs
run() {  # run <tag> <timeout> <args...>
  tag=$1; shift; tmo=$1; shift
  echo "=== $tag : $* ==="
  ( ulimit -v 6291456; exec timeout "$tmo" python3 wk9_s46_cell.py "$@" --out "$OUT" ) \
      > "$LOG/s46_$tag.out" 2> "$LOG/s46_$tag.err" &
  p=$!; echo $p > "$LOG/s46_$tag.pid"; wait $p
  echo "  exit $? (pid $p)"; tail -2 "$LOG/s46_$tag.err"
}
# V1 -- three banked mult_det = a rows of results/s45_ledger.md
run v1a 7200 7 8 8 5 5 1 1 --side det --levels cheap
run v1b 7200 7 9 9 6 2 1 1 --side det --levels cheap
run v1c 7200 8 12 12 3 3 1 1 --side det --levels cheap
# V2 -- the discriminating drop: (13,10,6,1,1,1)_8, pad side, a = 9, mult_pad = 8.
#       --kern exhibits the vector and checks it against the UNCOMPRESSED [E; ev].
run v2 7200 8 13 10 6 1 1 1 --side pad --levels cheap --kern
# V3 -- one mult_det = a row at both compression levels
run v3a 7200 7 12 9 3 2 1 1 --side det --levels cheap
run v3b 7200 7 12 9 3 2 1 1 --side det --levels s42
echo "PHASE 1 DONE"
