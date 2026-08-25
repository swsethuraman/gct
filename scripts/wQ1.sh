#!/bin/sh
# Q-grind worker 1: reps 00 02 04 07 + post-dup 34, then f1D_00 negative-control tail.
cd /home/claude/gct-run/q1
for i in 00 02 04 07 34; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/claude/gct/dp2g evalopts /home/claude/gct/inputs/evalin/f1Q_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
cd /home/claude/gct-run/negD
until grep -q VALUE r_D00.out 2>/dev/null; do
  /home/claude/gct/dp2g evalopts /home/claude/gct/inputs/evalin/f1D_00.txt > r_D00.out 2>> r_D00.log
  sleep 20
done
