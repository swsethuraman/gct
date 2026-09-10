#!/bin/sh
# B13-09 stream A: the length-7 groups in the pre-registered order (Addendum A.2), each
# weight in its own bounded subprocess.  Bounds are inside analysis/b13_09_sweep.py.
set -e
cd "$(dirname "$0")/.."
export S71_SCHUR_SO=/home/claude/b13_09/schur.so
export S71_MEM_X=250000000
python3 analysis/b13_09_sweep.py 7 7 --run b13_09_A_r7_d7 --commit --max-nsd 1.8e8 || true
python3 analysis/b13_09_sweep.py 7 8 --run b13_09_A_r7_d8 --commit --max-nsd 1.8e8 || true
python3 analysis/b13_09_sweep.py 7 9 --run b13_09_A_r7_d9 --commit --max-nsd 1.8e8 || true
