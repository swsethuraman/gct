#!/bin/sh
cd /home/claude/g1
for i in 01 03 07 09 05 00; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/claude/gct2/dp2g evalopts /home/claude/gct2/inputs/evalin/f1Xm3_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
