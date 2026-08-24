#!/bin/sh
cd /home/user/g2
for i in 01 03 07 05 13 15 17 19 21 23; do
  until grep -q VALUE r_$i.out 2>/dev/null; do
    /home/user/dp2g evalopts /home/user/evalin/f1C_$i.txt > r_$i.out 2>> r_$i.log
    sleep 20
  done
done
