#!/bin/bash
cd /home/claude/gct
( ulimit -v 7800000; exec timeout 14400 python3 analysis/wk13_b10_pilot.py --stage all ) > results/logs/b13_10_pilot.log 2>&1
echo "PILOT LOOP DONE $(date -u)" >> results/logs/b13_10_pilot.log
