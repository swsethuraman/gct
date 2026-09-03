#!/bin/bash
# restart-on-death wrapper for the last sweep cell
cd /home/claude/gct
export WIED_BIN=/home/claude/wied45 WIED_WORK=/home/claude/s45/work
if grep -q '"lam": \[6, 6, 6, 6, 2, 2\]' results/s45_cells.jsonl 2>/dev/null; then exit 0; fi
if pgrep -f "wk9_s45_bigcell.py 7 6 6 6 6 2 2" >/dev/null; then exit 0; fi
nohup timeout 39600 python3 analysis/wk9_s45_bigcell.py 7 6 6 6 6 2 2 --out results/s45_cells.jsonl >> results/logs/cell_7_6_6_6_6_2_2.log 2>&1 &
echo "(re)started $(date -u +%T)"
