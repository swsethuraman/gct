#!/bin/bash
cd /home/claude/gct
export S71_MEM_X=250000000
python3 analysis/wk12_s79_sweep6.py --queue results/s79_queue2.json --until 06:20 --no-fullrank --max-cost 1e7
