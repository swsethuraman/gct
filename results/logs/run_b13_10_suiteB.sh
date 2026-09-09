#!/bin/bash
# B13-10 suite, loop B: the small cells
cd /home/claude/gct
for id in A1 A2 A3 A4 B1 B2 B3 B4 C1 C2 C3; do
  ( ulimit -v 7000000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids $id --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteB.log 2>&1
done
echo "LOOP B DONE $(date -u)" >> results/logs/b13_10_suiteB.log
