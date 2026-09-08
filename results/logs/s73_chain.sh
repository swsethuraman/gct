#!/bin/bash
cd /root/gct
for d in 11 10 9; do
  timeout 7200 python3 analysis/wk11_s73_cell.py $d --fullE > results/logs/s73_d$d.log 2>&1
done
for d in 15 16; do
  timeout 7200 python3 analysis/wk11_s73_cell.py $d > results/logs/s73_d$d.log 2>&1
done
