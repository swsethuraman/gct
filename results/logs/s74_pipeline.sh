#!/bin/bash
# Session 74 pipeline: wait for the birth streams, then build the source and run the
# evaluation columns in the pre-registered order, banking each unit with a commit.
# Every step is bounded (timeout, ulimit -v); the pid of this driver is in s74_pipeline.pid.
cd /home/claude/gct || exit 1
ulimit -v 6500000
LOG=results/logs/s74_pipeline.log
echo "[$(date -u +%FT%TZ)] pipeline start" >> $LOG
BPID=$(cat results/logs/s74_births_1319b.pid 2>/dev/null)
while [ -n "$BPID" ] && kill -0 "$BPID" 2>/dev/null; do sleep 60; done
echo "[$(date -u +%FT%TZ)] births finished" >> $LOG
bank () {  # bank <message>
  git add -A results/s74 results/logs results/certs 2>/dev/null
  git commit -q -m "$1

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && echo "[$(date -u +%FT%TZ)] committed: $1" >> $LOG
}
run () {  # run <label> <timeout-secs> <command...>
  local label=$1; local tmo=$2; shift 2
  echo "[$(date -u +%FT%TZ)] start $label: $*" >> $LOG
  timeout "$tmo" "$@" >> results/logs/s74_${label}.log 2>&1
  echo "[$(date -u +%FT%TZ)] end $label (exit $?)" >> $LOG
}
P1=2147483647; P2=2147483629
run build     600   python3 analysis/wk12_s74_columns.py --build
run rowcheck  3600  python3 analysis/wk12_s74_columns.py --check-rows --workers 2
bank "s74: source assembled from the birth bases; row-system identity check banked."
run det_P1    14400 python3 analysis/wk12_s74_columns.py --family det --prime $P1 --workers 2
run decide1   1200  python3 analysis/wk12_s74_decide.py --prime $P1 --families det
bank "s74: determinant column at P1 (i_det(23), i_det(24)) banked."
run pad_P1    14400 python3 analysis/wk12_s74_columns.py --family pad --prime $P1 --workers 2
run decide2   1200  python3 analysis/wk12_s74_decide.py --prime $P1 --families det,pad
bank "s74: padded-permanent column at P1 banked; decision at P1 read."
run rest_P1   28800 python3 analysis/wk12_s74_columns.py --family gen,red,per4 --prime $P1 --workers 2
run decide3   1200  python3 analysis/wk12_s74_decide.py --prime $P1 --families gen,det,pad,red,per4
bank "s74: generic, reducible and per_4 columns at P1 banked."
run det_P2    14400 python3 analysis/wk12_s74_columns.py --family det --prime $P2 --workers 2
run pad_P2    14400 python3 analysis/wk12_s74_columns.py --family pad --prime $P2 --workers 2
run decide4   1200  python3 analysis/wk12_s74_decide.py --prime $P2 --families det,pad
bank "s74: determinant and padded columns at P2 banked."
run rest_P2   28800 python3 analysis/wk12_s74_columns.py --family gen,red,per4 --prime $P2 --workers 2
run decide5   1200  python3 analysis/wk12_s74_decide.py --prime $P2 --families gen,det,pad,red,per4
bank "s74: all five columns at both primes banked."
echo "[$(date -u +%FT%TZ)] pipeline done" >> $LOG
