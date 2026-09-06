#!/bin/bash
# Session 61: msolve sweep over forms / primes / seeds / slots (third engine, Rabinowitsch form).
#   usage: wk9_s61_msolve_sweep.sh <tag> <spec>...   spec = form:prime:seed:k1,k2,...
cd "$(dirname "$0")/.." || exit 1
TAG="$1"; shift
echo $$ > "results/logs/s61_msolve_sweep_$TAG.pid"
for spec in "$@"; do
  IFS=: read -r form prime seed ks <<< "$spec"
  for k in ${ks//,/ }; do
    python3 analysis/wk9_s61_msolve.py --form "$form" --prime "$prime" --seed "$seed" --k "$k" --timeout 3600 >> "results/logs/s61_msolve_sweep_$TAG.log" 2>&1
  done
done
echo "sweep $TAG finished" >> "results/logs/s61_msolve_sweep_$TAG.log"
