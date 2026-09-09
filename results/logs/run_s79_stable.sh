#!/bin/bash
# session 79 part 1: calibration (the eight remaining closed blocks, size order) then the five a_inf = 4 blocks (cost order)
cd /home/claude/gct
ulimit -v 6500000
timeout 14400 python3 analysis/wk12_s79_stable.py 7,2,2,1,1 5,5,1,1,1 5,3,3,2 6,3,2,1,1 5,4,2,1,1 5,3,3,1,1 4,4,2,2,1 4,3,2,2,2 --out results/s79_stable/calibration
timeout 14400 python3 analysis/wk12_s79_stable.py 6,3,3,1 4,4,3,2 6,2,2,2,1 5,3,2,2,1 5,2,2,2,2 --out results/s79_stable --partial-control
echo DONE
