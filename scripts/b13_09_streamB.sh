#!/bin/sh
# B13-09 stream B: the length-8 groups, (8,8) then (8,9) capped so two concurrent
# builds cannot exhaust the box (Addendum A.2).
set -e
cd "$(dirname "$0")/.."
export S71_SCHUR_SO=/home/claude/b13_09/schur.so
export S71_MEM_X=250000000
python3 analysis/b13_09_sweep.py 8 8 --run b13_09_B_r8_d8 --commit --max-nsd 1.8e8 || true
python3 analysis/b13_09_sweep.py 8 9 --run b13_09_B_r8_d9 --commit --max-nsd 5e7 || true
