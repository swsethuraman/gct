#!/bin/bash
cd /home/claude/gct
for D in 11 12; do
  echo "$(date +%H:%M:%S) start delta=$D" >> results/orchestrator2.log
  python3 -u analysis/wk9_s38_screen.py big $D --csv results/screen_d${D}.csv >> results/screen_big_${D}.log 2>&1
  echo "$(date +%H:%M:%S) done delta=$D rc=$?" >> results/orchestrator2.log
done
echo "PHASE0_DONE" >> results/orchestrator2.log
