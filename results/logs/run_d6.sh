#!/bin/bash
ulimit -v 3200000
cd /home/claude/work/gct
timeout 5400 python3 analysis/wk9_s54_measure.py --delta 6 --out results/s54_cells_d6.jsonl --maxnb 6000 --padfirst 0 > results/logs/s54_d6.log 2>&1
echo "D6_DONE rc=$?" >> results/logs/s54_d6.log
