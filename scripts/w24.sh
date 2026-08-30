#!/bin/sh
# retry-until-VALUE worker (rule 3): never advance past an unfinished run
SPEC=$1; LG=$2; DIR=$3; OUT=$4
while true; do
  /home/claude/gct/br2 "$SPEC" "$LG" "$DIR" > "$OUT.tmp" 2>> "$OUT.err"
  if grep -q VALUE "$OUT.tmp"; then mv "$OUT.tmp" "$OUT"; break; fi
  echo "=== restart $(date -u +%H:%M:%S) ===" >> "$OUT.err"
  sleep 5
done
