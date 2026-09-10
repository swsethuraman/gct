#!/bin/bash
# B13-10 delivery: one bundle against the recorded base, with an md5 naming bare filenames.
set -e
cd /home/claude/gct
BASE=00495110c62acfbbbc951e82cc218ed091563b3f
OUT=/home/claude/b13_10_delivery
rm -rf "$OUT"; mkdir -p "$OUT"
git bundle create "$OUT/b13_10_lean_rows.bundle" $BASE..HEAD
git -C /home/claude/gct bundle verify "$OUT/b13_10_lean_rows.bundle"
cd "$OUT"
SZ=$(stat -c%s b13_10_lean_rows.bundle)
echo "bundle bytes: $SZ"
{
  echo "# B13-10 delivery digests.  Bare filenames; md5sum -c works from the directory holding the files."
  echo "# One part only: the bundle is a single file, so there is no partNN split and no part digest to reconcile."
  echo "# base = $BASE ; branch b13-10-lean-rows ; total parts = 1"
  md5sum b13_10_lean_rows.bundle
} > b13_10_lean_rows.bundle.md5
md5sum -c b13_10_lean_rows.bundle.md5
ls -l
