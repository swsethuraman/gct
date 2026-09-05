#!/bin/bash
ulimit -v 3200000
cd /home/claude/work/gct
for D in 8 6; do
  timeout 4200 python3 analysis/wk9_s54_measure.py --delta $D --out results/s54_cells_d$D.jsonl --maxnb 2500 --padfirst 0 >> results/logs/s54_A.log 2>&1
  echo "A_D${D}_DONE rc=$?" >> results/logs/s54_A.log
done
