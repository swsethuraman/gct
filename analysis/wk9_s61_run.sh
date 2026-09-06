#!/bin/bash
# Session 61 launcher: bound a run by wall clock and memory, record its pid.
#   usage: wk9_s61_run.sh <runname> <timeout_seconds> <mem_kb> -- <command...>
# Log: results/logs/s61_<runname>.log ; pid: results/logs/s61_<runname>.pid
# A run is ended only by the pid in that file, never by name.
set -u
NAME="$1"; TMO="$2"; MEM="$3"; shift 3
[ "$1" = "--" ] && shift
cd "$(dirname "$0")/.." || exit 1
mkdir -p results/logs
ulimit -v "$MEM"
nohup timeout "$TMO" "$@" > "results/logs/s61_$NAME.driver.log" 2>&1 &
echo $! > "results/logs/s61_$NAME.driver.pid"
echo "launched $NAME pid $(cat results/logs/s61_$NAME.driver.pid) timeout ${TMO}s mem ${MEM}kB"
