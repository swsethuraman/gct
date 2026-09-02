#!/bin/bash
# Session 34 -- drive the remaining feasible cells, one fresh process per cell,
# in the pre-registered master order (results/s34_finish_order.txt).
# Gate: census constant 5.6e-8 vs 0.85*free, encoded as 5.93e-8 vs the
# wrapper's 0.90*free (identical inequality).  The two marginal cells run last
# under the observed constant 3.5e-8 (PREREG_s34.md section 4 admission),
# after every other feasible cell is done.
cd "$(dirname "$0")/.."
while read -r line; do
  case "$line" in
    MARGINAL\ *) lam="${line#MARGINAL }"; c="3.5e-8" ;;
    *) lam="$line"; c="5.93e-8" ;;
  esac
  echo "=== $(date -u +%H:%M) finish $lam (constant $c) ==="
  python3 analysis/wk9_s34_finish.py "$lam" "$c"
  rc=$?
  if [ $rc -eq 3 ]; then echo "*** D>0 -- STOP-EVERYTHING ***"; exit 3; fi
  if [ $rc -eq 2 ]; then echo "cell $lam did not fit -- recorded, continuing"; fi
done < results/s34_finish_order.txt
echo "=== finish driver complete ==="
