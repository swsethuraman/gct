#!/bin/bash
cd /home/claude/gct
for id in B5 D1 C4; do
  ( ulimit -v 2500000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids $id --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteA.log 2>&1
done
echo "LOOP A1 DONE $(date -u)" >> results/logs/b13_10_suiteA.log
