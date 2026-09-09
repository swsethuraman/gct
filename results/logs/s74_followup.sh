#!/bin/bash
# Session 74 follow-up: the verification runs after the two decisive columns at both primes.
cd /home/claude/gct || exit 1
ulimit -v 6500000
LOG=results/logs/s74_followup.log
P1=2147483647; P2=2147483629
bank () { git add -A results/s74 results/logs results/certs 2>/dev/null; git commit -q -m "$1

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && echo "[$(date -u +%FT%TZ)] committed: $1" >> $LOG; }
run () { local label=$1; local tmo=$2; shift 2; echo "[$(date -u +%FT%TZ)] start $label: $*" >> $LOG; timeout "$tmo" "$@" >> results/logs/s74_${label}.log 2>&1; echo "[$(date -u +%FT%TZ)] end $label (exit $?)" >> $LOG; }
echo "[$(date -u +%FT%TZ)] follow-up start" >> $LOG
run verify_pad_P1 7200 python3 analysis/wk12_s74_verify.py --families pad --prime $P1 --K 294 --workers 2
bank "s74: padded column re-derived at fresh box-1000 points (P1)."
run rest_P1 14400 python3 analysis/wk12_s74_columns.py --family gen,red,per4 --prime $P1 --workers 2
run decide3 1200 python3 analysis/wk12_s74_decide.py --prime $P1 --families gen,det,pad,red,per4
bank "s74: generic, reducible and per_4 columns at P1 banked."
run verify_det_P1 7200 python3 analysis/wk12_s74_verify.py --families det --prime $P1 --K 294 --workers 2
bank "s74: determinant column re-derived at fresh box-1000 points (P1)."
run rest_P2 14400 python3 analysis/wk12_s74_columns.py --family gen,red,per4 --prime $P2 --workers 2
run decide5 1200 python3 analysis/wk12_s74_decide.py --prime $P2 --families gen,det,pad,red,per4
bank "s74: all five columns at both primes banked."
run verify_pad_P2 7200 python3 analysis/wk12_s74_verify.py --families pad --prime $P2 --K 294 --workers 2
run countns 1800 python3 analysis/wk12_s74_verify.py --count-ns 23,24
run spot 3600 python3 analysis/wk12_s74_verify.py --spot 4
bank "s74: fresh-point padded re-derivation at P2, the N_S recount and the evaluator spot check banked."
echo "[$(date -u +%FT%TZ)] follow-up done" >> $LOG
