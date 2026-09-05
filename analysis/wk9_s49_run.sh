#!/bin/bash
# Session 49 launcher: bound a run by wall clock and memory, record its pid.
#   usage: wk9_s49_run.sh <runname> <timeout_seconds> <mem_kb> -- <command...>
# Log: results/logs/<runname>.log ; pid: results/logs/<runname>.pid
# A run is ended only by the pid in that file (kill <pid>), never by name.
set -u
NAME="$1"; TMO="$2"; MEM="$3"; shift 3
[ "$1" = "--" ] && shift
cd "$(dirname "$0")/.." || exit 1
mkdir -p results/logs
ulimit -v "$MEM"
nohup timeout "$TMO" "$@" > "results/logs/$NAME.log" 2>&1 &
echo $! > "results/logs/$NAME.pid"
echo "launched $NAME pid $(cat results/logs/$NAME.pid) timeout ${TMO}s mem ${MEM}kB"
