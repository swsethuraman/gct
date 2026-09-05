#!/usr/bin/env bash
# One-pass history rewrite.  Run on a FRESH clone, never on a working repo.
#
#   git clone --no-local <repo> gct-rewrite && cd gct-rewrite
#   bash tools/rewrite/run_rewrite.sh
#
# Then inspect, and only then force-push.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"

git filter-repo --force \
  --commit-callback "$(cat "$here/message_callback.py")" \
  --strip-blobs-bigger-than 5M

echo
echo "=== post-rewrite checks ==="
echo -n "commits with a byte-order mark : "; git log --all --format='%s' | grep -cP '\xef\xbb\xbf' || true
echo -n "commits with 'h_pad >= 19'     : "; git log --all --format='%B' | grep -c 'h_pad >= 19' || true
echo -n "commits with a session link    : "; git log --all --format='%B' | grep -c 'claude.ai' || true
echo -n "blobs over 5 MB in history     : "
git rev-list --objects --all \
  | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' 2>/dev/null \
  | awk '$1=="blob" && $3>5242880' | wc -l
echo -n "commits total                  : "; git rev-list --count --all
