#!/bin/bash
cd /home/claude/gct
( ulimit -v 6000000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids B6 --variants --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteA.log 2>&1
( ulimit -v 6000000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids C6 --variants --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteA.log 2>&1
( ulimit -v 6000000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids B7 --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteA.log 2>&1
( ulimit -v 6000000; exec timeout 3600 python3 analysis/wk13_b10_suite.py --ids C5 --out results/b13_10/suite.jsonl ) >> results/logs/b13_10_suiteA.log 2>&1
echo "LOOP A2 DONE $(date -u)" >> results/logs/b13_10_suiteA.log
