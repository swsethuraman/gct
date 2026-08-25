#!/bin/sh
# P-grind worker 1: even reps, then f1D_00 negative-control tail.
cd /home/claude/gct-run/p1
for i in 00 02 04 12 14 16 18 20 22; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/claude/gct/dp2g evalopts /home/claude/gct/inputs/evalin/f1P_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
cd /home/claude/gct-run/negD
until grep -q VALUE r_D00.out 2>/dev/null; do
  /home/claude/gct/dp2g evalopts /home/claude/gct/inputs/evalin/f1D_00.txt > r_D00.out 2>> r_D00.log
  sleep 20
done
