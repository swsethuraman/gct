#!/bin/bash
cd /home/claude/gct
export S71_MEM_X=250000000
for mu in "9 6 6 6 5 2 2" "9 7 7 4 4 3 2"; do
  timeout 5400 python3 analysis/wk12_s79_per6.py $mu --out results/s79_per6.jsonl --certs results/certs/s79_per6 2>&1 | grep -E "PER6 RESULT|Killed|Error" | cut -c1-250
done
timeout 7200 python3 analysis/wk12_s79_cell6.py 9 13 9 9 3 1 1 --out results/s79_cells.jsonl --certs results/certs/s79_cells --sequential --no-fullrank > results/logs/s79_retry3_cell.log 2>&1
echo DONE rc=$?
