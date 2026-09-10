#!/bin/bash
while pgrep -f "run_b13_10_suiteA1.sh" > /dev/null; do sleep 10; done
/home/claude/gct/results/logs/run_b13_10_suiteA2.sh
