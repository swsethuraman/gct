#!/bin/bash
cd /home/claude/gct
for D in 11 12; do
  echo "$(date +%H:%M:%S) start delta=$D" >> results/orchestrator3.log
  python3 -u analysis/wk9_s38_screen.py $D --clear 2 --csv results/screen_d${D}.csv >> results/screen_p0b_${D}.log 2>&1
  echo "$(date +%H:%M:%S) done delta=$D rc=$?" >> results/orchestrator3.log
done
echo "P0B_DONE" >> results/orchestrator3.log
