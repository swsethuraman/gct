#!/bin/bash
cd /home/claude/gct
# 1. wait for d8a (small cells) and the screen to finish
while ps -p 2489 >/dev/null 2>&1; do sleep 20; done
echo "$(date +%H:%M:%S) d8a done" >> results/orchestrator.log
while ps -p 2374 >/dev/null 2>&1; do sleep 20; done
echo "$(date +%H:%M:%S) screen done" >> results/orchestrator.log
# 2. d8b: reachable delta=8 cells N_S 5000-9000, alone (full memory)
python3 -u analysis/wk9_s38_census.py measurecsv results/census_d8.csv 8 9000 --lo 5000 \
    >> results/s38_measure_d8b.log 2>&1
echo "$(date +%H:%M:%S) d8b done" >> results/orchestrator.log
echo "ALL_REMAINING_DONE" >> results/orchestrator.log
