#!/usr/bin/env python3
"""Assemble total_f1C from the 19 grind outputs (per ASSEMBLY.md)."""
import re, glob, sys

REPS = ["00","02","04","12","14","16","18","20","22",
        "01","03","05","13","15","17","19","21","23"]
DUP = "07"   # partner of 00; validation only

vals = {}
for d in ("g1","g2"):
    for f in glob.glob(f"/home/user/{d}/r_*.out"):
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
print(f"validation pair: VALUE(00)={v00}  VALUE(07)={v07}  -> {'MATCH' if pair_ok else 'MISMATCH!!'}")
if not pair_ok:
    sys.exit(3)

srep = sum(vals[x][0] for x in REPS)
total = 2 * srep
print(f"sum over 18 reps = {srep}")
print(f"TOTAL_f1C = 2 * {srep} = {total}")
