#!/bin/sh
# Q-grind worker 2: reps 01 03 05 09 + pre-dup 14 + swap-dup 06, then Phi18(h1gen) tail.
cd /home/claude/gct-run/q2
for i in 01 03 05 09 14 06; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/claude/gct/dp2g evalopts /home/claude/gct/inputs/evalin/f1Q_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
cd /home/claude/gct-run/phi
until grep -q VALUE r_phi.out 2>/dev/null; do
  /home/claude/gct/dp2g evalfile /home/claude/gct/inputs/evalin/phi18_h1gen.txt > r_phi.out 2>> r_phi.log
  sleep 20
done
