#!/bin/bash
ulimit -v 3200000
cd /home/claude/work/gct
timeout 5400 python3 analysis/wk9_s54_measure.py --delta 7 --out results/s54_cells_d7.jsonl --maxnb 5000 --padfirst 0 > results/logs/s54_d7.log 2>&1
echo "D7_DONE rc=$?" >> results/logs/s54_d7.log
