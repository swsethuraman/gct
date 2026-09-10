#!/bin/bash
# re-run every cheap cell under the FIXED rank comparator (a check that cannot place
# its targets now fails instead of reporting PASS on nothing)
cd /home/claude/gct
for id in D1 A1 A2 A3 A4 B1 B2 B3 B4 C1 C2 C3 X1 X2; do
  ( ulimit -v 2500000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids $id --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_recheck.log 2>&1
done
echo "RECHECK DONE $(date -u)" >> results/logs/b13_10_recheck.log
