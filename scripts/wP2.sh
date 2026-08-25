#!/bin/sh
# P-grind worker 2: duplicate 07 first (pair gate vs 00), odd reps, then Phi18(h1gen) tail.
cd /home/claude/gct-run/p2
for i in 07 01 03 05 13 15 17 19 21 23; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/claude/gct/dp2g evalopts /home/claude/gct/inputs/evalin/f1P_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
cd /home/claude/gct-run/phi
until grep -q VALUE r_phi.out 2>/dev/null; do
  /home/claude/gct/dp2g evalfile /home/claude/gct/inputs/evalin/phi18_h1gen.txt > r_phi.out 2>> r_phi.log
  sleep 20
done
