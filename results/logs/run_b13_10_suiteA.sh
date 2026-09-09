#!/bin/bash
# B13-10 suite, loop A: the large cells, one driver process per cell (clean per-cell consumer peak)
cd /home/claude/gct
for id in B5 B6 B7 C4 C5 C6 D1 X1 X2; do
  V=""; case $id in B6|B7|C5|C6) V="--variants";; esac
  ( ulimit -v 7000000; exec timeout 7200 python3 analysis/wk13_b10_suite.py --ids $id $V --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteA.log 2>&1
done
echo "LOOP A DONE $(date -u)" >> results/logs/b13_10_suiteA.log
