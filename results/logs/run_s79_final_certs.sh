#!/bin/bash
cd /home/claude/gct
export S71_MEM_X=250000000
for cell in "8 19 6 2 2 2 1" "8 14 8 7 1 1 1" "9 17 12 4 1 1 1" "9 16 13 4 1 1 1" "9 19 9 5 1 1 1" "9 22 6 2 2 2 2" "8 12 9 8 1 1 1" "8 19 5 3 2 2 1" "9 23 5 3 2 2 1" "10 27 5 3 2 2 1"; do
  timeout 3600 python3 analysis/wk12_s79_cell6.py $cell --out /tmp/claude-0/-home-claude/6f74b5c9-a9d4-535c-9901-ec92ff53b8ee/scratchpad/calib6_recert.jsonl --certs results/certs/s79_calib6 --sequential 2>&1 | grep -E "RESULT \(|Traceback|Error" | cut -c1-200
done
echo DONE
