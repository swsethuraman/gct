#!/bin/bash
cd /home/claude/gct
export S71_MEM_X=250000000
python3 analysis/wk12_s79_sweep_per6.py 10 --until 06:20 --max-ns 2e6 --no-certs
