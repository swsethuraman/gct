#!/bin/bash
ulimit -v 6000000
cd /home/claude/work/gct
timeout 3000 python3 analysis/wk9_s54_census.py 8 9 > results/logs/s54_census89.log 2>&1
echo "CENSUS_DONE rc=$?" >> results/logs/s54_census89.log
