#!/usr/bin/env python3
"""Assemble TOTAL_P from the 19 P-grind outputs (session 12).
Pairing derived from the col-swap symmetry rho=(1 2): V(rho.s6, rho.s7) = +V(s6,s7).
Pairs: (0,7),(1,6),(2,10),(3,11),(4,8),(5,9),(12,25),(13,24),(14,28),(15,29),
(16,26),(17,27),(18,31),(19,30),(20,34),(21,35),(22,32),(23,33).
TOTAL_P = 2 * sum over the 18 representatives (dup 07 is validation only).
"""
import re, glob, sys

REPS = ["00","02","04","12","14","16","18","20","22",
        "01","03","05","13","15","17","19","21","23"]
DUP = "07"

vals = {}
for d in ("p1","p2"):
    for f in glob.glob(f"/home/claude/gct-run/{d}/r_*.out"):
        xx = f[-6:-4]
        m = re.search(r"VALUE (-?\d+) \(final states (\d+)\)", open(f).read())
        if m:
            vals[xx] = (int(m.group(1)), int(m.group(2)))

missing = [x for x in REPS + [DUP] if x not in vals]
if missing:
    print(f"INCOMPLETE: missing {missing} ({len(vals)}/19 done)")
    sys.exit(1)

bad = [x for x, (_, ns) in vals.items() if ns != 1]
if bad:
    print(f"ERROR: final states != 1 for {bad}")
    sys.exit(2)

v00, v07 = vals["00"][0], vals[DUP][0]
pair_ok = (v00 == v07)
print(f"pair gate: VALUE(00)={v00}  VALUE(07)={v07}  -> {'MATCH' if pair_ok else 'MISMATCH!!'}")
if not pair_ok:
    sys.exit(3)

for x in REPS:
    print(f"  {x}: {vals[x][0]:+d}")
srep = sum(vals[x][0] for x in REPS)
total = 2 * srep
print(f"sum over 18 reps = {srep}")
print(f"TOTAL_P = 2 * {srep} = {total}")
print("NONZERO -> independent second-point k=1 certificate" if total != 0
      else "ZERO -> investigate before any interpretation")
