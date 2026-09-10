#!/usr/bin/env bash
# B13-08 -- build the delivery bundle against the recorded base and its .md5.
#
#   git bundle create b13_08_cubic_remainder.bundle <base>..HEAD
#
# The bundle is delivered UNSPLIT (one part).  The .md5 names the BARE filename,
# never a path, so `md5sum -c` works on any machine, and carries the whole-file
# digest; if a future run has to split the file, the split parts are named
# part00, part01, ... contiguously and each gets its own line in the same file.
set -euo pipefail
cd "$(dirname "$0")/.."
BASE=00495110c62acfbbbc951e82cc218ed091563b3f
OUT=b13_08_cubic_remainder.bundle
SPLIT_AT=$((45 * 1024 * 1024))     # bytes; above this the bundle is split into part00, part01, ...

git bundle create "$OUT" "$BASE"..b13_08 b13_08
git bundle verify "$OUT" >/dev/null
SZ=$(stat -c%s "$OUT")
rm -f "$OUT.md5"
{
  echo "# B13-08 delivery.  Base $BASE, branch b13_08, HEAD $(git rev-parse HEAD)."
  echo "# Bundle size $SZ bytes.  Bare filenames only, for md5sum -c on any machine."
} > "$OUT.md5"
if [ "$SZ" -gt "$SPLIT_AT" ]; then
  split -b "$SPLIT_AT" -d -a 2 "$OUT" "$OUT.part"
  N=$(ls "$OUT".part* | wc -l)
  echo "# Total parts: $N, numbered from part00 contiguously.  Reassemble: cat $OUT.part* > $OUT" >> "$OUT.md5"
  md5sum "$OUT" "$OUT".part* | sed 's#.*/##' >> "$OUT.md5"
else
  echo "# Total parts: 1 -- the bundle is delivered unsplit; there are no part files." >> "$OUT.md5"
  md5sum "$OUT" | sed 's#.*/##' >> "$OUT.md5"
fi
echo "--- $OUT.md5 ---"; cat "$OUT.md5"
echo "--- verify ---"; md5sum -c "$OUT.md5" 2>/dev/null || md5sum -c <(grep -v '^#' "$OUT.md5")
