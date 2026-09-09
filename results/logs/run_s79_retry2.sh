#!/bin/bash
cd /home/claude/gct
ulimit -v 6500000
export S71_MEM_X=250000000
timeout 7200 python3 analysis/wk12_s79_cell6.py 9 13 9 9 3 1 1 --out results/s79_cells.jsonl --certs results/certs/s79_cells --sequential --no-fullrank > results/logs/s79_retry2_cell.log 2>&1
echo DONE rc=$?
