#!/bin/sh
# B13-09 stream A: the length-7 groups.  (7,7) and (7,8) completed in the
# pre-registered N_S order; (7,9) runs in the refitted-cost order of Addendum C.
set -e
cd "$(dirname "$0")/.."
export S71_SCHUR_SO=/home/claude/b13_09/schur.so
export S71_MEM_X=250000000
python3 analysis/b13_09_sweep.py 7 9 --run b13_09_A_r7_d9 --commit --order cost --max-cost 900 --max-nsd 1.8e8 || true
python3 analysis/b13_09_sweep.py 7 9 --run b13_09_A_r7_d9_tail --commit --order cost --max-nsd 1.8e8 || true
