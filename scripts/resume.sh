#!/bin/sh
for w in 1 2; do
  if pgrep -f "^sh /home/user/w$w.sh" > /dev/null; then echo "w$w alive"
  else setsid nohup sh /home/user/w$w.sh < /dev/null > /dev/null 2>&1 & echo "w$w restarted"
  fi
done
