#!/bin/bash
# session 79 part 2 calibration at length 6 (both primes each): the s47 reducible-drop cells, two s43 det-full cells,
# and the cross-instrument cells of the (5,3,2,2,1) tail
cd /home/claude/gct
ulimit -v 6500000
OUT=results/s79_calibration6.jsonl
for cell in "8 19 6 2 2 2 1" "8 14 8 7 1 1 1" "9 17 12 4 1 1 1" "9 16 13 4 1 1 1" "9 19 9 5 1 1 1" "9 22 6 2 2 2 2" "8 12 9 8 1 1 1" "8 19 5 3 2 2 1" "9 23 5 3 2 2 1" "10 27 5 3 2 2 1"; do
  timeout 7200 python3 analysis/wk12_s79_cell6.py $cell --out $OUT --certs results/certs/s79_calib6 --sequential 2>&1 | grep -E "RESULT \(|sieve|hybrid\[|Traceback|Error" | cut -c1-400
done
echo DONE
