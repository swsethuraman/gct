#!/bin/bash
cd /home/claude/gct
ulimit -v 6500000
export S71_MEM_X=250000000
for cell in "8 11 7 6 6 1 1" "9 13 9 9 3 1 1"; do
  timeout 7200 python3 analysis/wk12_s79_cell6.py $cell --out results/s79_cells.jsonl --certs results/certs/s79_cells --sequential --no-fullrank 2>&1 | grep -E "RESULT \(|hybrid\[|Traceback|Error|Killed" | cut -c1-300
done
echo DONE
