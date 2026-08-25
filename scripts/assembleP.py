#!/usr/bin/env python3
"""Assemble TOTAL_P from the 11-run extended-orbit P-grind (session 12).

Extended orbit structure (LEMMA, validated 36/36 on banked C values):
group = <pre-rho, swap theta_b, post-omega theta_d>, 8 orbits:
  orbit 0 (size 4): {00,07,21,35}   rep 00   dup 07 validates PRE
  orbit 1 (size 4): {01,06,23,33}   rep 01   dup 06 validates SWAP
  orbit 2 (size 8): {02,10,12,15,20,25,29,34} rep 02  dup 34 validates POST
  orbit 3 (size 4): {03,11,18,31}   rep 03
  orbit 4 (size 8): {04,08,13,17,22,24,27,32} rep 04
  orbit 5 (size 4): {05,09,19,30}   rep 05
  orbit 6 (size 2): {14,28}         rep 14
  orbit 7 (size 2): {16,26}         rep 16

TOTAL_P = 4*V00 + 4*V01 + 8*V02 + 4*V03 + 8*V04 + 4*V05 + 2*V14 + 2*V16

Blind predictions (rel-only law, logged before values existed):
V00=V14, V05=V16, V01=V02, V03=V04.
"""
import re, glob, sys

WEIGHTS = {"00": 4, "01": 4, "02": 8, "03": 4, "04": 8, "05": 4, "14": 2, "16": 2}
DUPS = [("07", "00", "pre"), ("06", "01", "swap"), ("34", "02", "post")]
ALL = list(WEIGHTS) + [d[0] for d in DUPS]

vals = {}
for d in ("p1", "p2"):
    for f in glob.glob(f"/home/claude/gct-run/{d}/r_*.out"):
        xx = f[-6:-4]
        m = re.search(r"VALUE (-?\d+) \(final states (\d+)\)", open(f).read())
        if m:
            vals[xx] = (int(m.group(1)), int(m.group(2)))

missing = [x for x in ALL if x not in vals]
if missing:
    print(f"INCOMPLETE: missing {missing} ({len(vals)}/11 done)")
    sys.exit(1)

bad = [x for x, (v, ns) in vals.items() if not (ns == 1 or (ns == 0 and v == 0))]
if bad:
    print(f"ERROR: invalid (VALUE, final states) for {bad} — need states 1, or structural zero (0, 0)")
    sys.exit(2)
szero = [x for x, (v, ns) in vals.items() if ns == 0 and v == 0]
if szero:
    print(f"structural zeros (final states 0): {sorted(szero)}")

gate_fail = False
for dup, rep, name in DUPS:
    ok = vals[dup][0] == vals[rep][0]
    print(f"gate {name}: V({dup}) = {vals[dup][0]:+d}  vs  V({rep}) = {vals[rep][0]:+d}  -> {'MATCH' if ok else 'MISMATCH!!'}")
    gate_fail = gate_fail or not ok
if gate_fail:
    print("GATE FAILURE: do not assemble; fall back to full-36 grind.")
    sys.exit(3)

print("\nblind predictions (rel-only law at P):")
for a, b in [("00","14"), ("05","16"), ("01","02"), ("03","04")]:
    print(f"  V({a}) {'==' if vals[a][0]==vals[b][0] else '!='} V({b})   [{vals[a][0]:+d} vs {vals[b][0]:+d}]")

for x in WEIGHTS:
    print(f"  {x}: {vals[x][0]:+d}  (weight {WEIGHTS[x]})")
total = sum(WEIGHTS[x] * vals[x][0] for x in WEIGHTS)
print(f"TOTAL_P = {total}")
print("NONZERO -> independent second-point k=1 certificate" if total != 0
      else "ZERO -> stop; investigate before any interpretation")
