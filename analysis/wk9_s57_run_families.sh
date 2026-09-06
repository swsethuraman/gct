#!/bin/bash
# Session 57 -- the family runs, sequential, each bounded by timeout and ulimit -v,
# each with its process id recorded under results/logs/.  Ended only by that id.
cd "$(dirname "$0")/.."
export S39_BUILD=/tmp/s39_build
ulimit -v 6300000
run () {  # name, timeout seconds, args...
  local name=$1; local tmo=$2; shift 2
  timeout "$tmo" python3 analysis/wk9_s57_families.py "$@" > "results/logs/s57_${name}.log" 2>&1 &
  echo $! > "results/logs/s57_${name}.pid"
  wait $!
  echo "rc=$?" >> "results/logs/s57_${name}.log"
}
run families_A_d13_16 7200  --families F1,F2,F3 --deltas 13,14,15,16
run families_C_d17_24 10800 --families F1,F2,F3 --deltas 17,18,19,20,21,22,23,24
run families_B_d13_16 14400 --families F5 --deltas 13,14,15,16
run families_D_d13_16 10800 --families F4 --deltas 13,14,15,16
