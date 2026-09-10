#!/bin/bash
cd /home/claude/gct
( ulimit -v 3000000; exec timeout 900 python3 analysis/wk13_b10_fo_check.py ) > results/logs/b13_10_fo_check.log 2>&1
for id in B5 C4; do
  ( ulimit -v 7000000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids $id --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_recheck.log 2>&1
done
echo "FINAL DONE $(date -u)" >> results/logs/b13_10_recheck.log
