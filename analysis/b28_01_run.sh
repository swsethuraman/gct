#!/bin/bash
# B28-01 run wrapper: one numerical process, one BLAS thread, OS memory cap.
# usage: b28_01_run.sh LABEL MEMMAX TIMEOUT_SECONDS cmd args...
#   MEMMAX as systemd accepts it (e.g. 8G); the cap is a transient user scope
#   with MemoryMax=MEMMAX and MemorySwapMax=0; GNU time -v records wall time
#   and maximum RSS; `timeout` enforces the wall limit.
set -u
LABEL=$1; MEM=$2; TO=$3; shift 3
RUNS=${B28_RUNS:-$HOME/b28_01/runs}
mkdir -p "$RUNS"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
T0=$(date -u +%Y-%m-%dT%H:%M:%SZ)
systemd-run --user --scope --quiet -p MemoryMax="$MEM" -p MemorySwapMax=0 \
  /usr/bin/time -v -o "$RUNS/$LABEL.time" timeout "$TO" "$@" > "$RUNS/$LABEL.out" 2> "$RUNS/$LABEL.log"
RC=$?
T1=$(date -u +%Y-%m-%dT%H:%M:%SZ)
WALL=$(grep 'Elapsed (wall clock)' "$RUNS/$LABEL.time" | awk '{print $NF}')
RSS=$(grep 'Maximum resident set size' "$RUNS/$LABEL.time" | awk '{print $NF}')
printf '{"label":"%s","start":"%s","end":"%s","rc":%d,"wall":"%s","maxrss_kb":%s,"memmax":"%s","timeout_s":%s,"cmd":"%s"}\n' \
  "$LABEL" "$T0" "$T1" "$RC" "$WALL" "${RSS:-null}" "$MEM" "$TO" "$*" >> "$RUNS/runlog.jsonl"
echo "$LABEL rc=$RC wall=$WALL maxrss_kb=$RSS"
exit $RC
