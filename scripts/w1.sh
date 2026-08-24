#!/bin/sh
cd /home/user/g1
for i in 00 02 04 12 14 16 18 20 22; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/user/dp2g evalopts /home/user/evalin/f1C_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
