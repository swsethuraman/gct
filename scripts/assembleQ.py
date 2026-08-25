#!/usr/bin/env python3
"""Assemble TOTAL_Q from the 11-run extended-orbit grind at point
Q = (x4+=x0, x6+=x1)  [rank-2, sources {x0,x1}, targets (r1,c1),(r2,c0)].
Point symmetry rho = (0 1); scheme automorphisms swap + post-omega, omega=(0 2).
Orbits computed here, not hardcoded. Structural zeros (VALUE 0, states 0) accepted.
"""
import re, glob, sys, itertools

perms = list(itertools.permutations((0,1,2)))
ix = {p: i for i, p in enumerate(perms)}
def comp(a,b): return tuple(a[b[i]] for i in range(3))
RHO, OM = (1,0,2), (2,1,0)
def pre(s):  return (comp(RHO,s[0]), comp(RHO,s[1]))
def post(s): return (comp(s[0],OM), comp(s[1],OM))
def swap(s): return (s[1], s[0])

seen, orbits = set(), []
for s6 in perms:
    for s7 in perms:
        if (s6,s7) in seen: continue
        orb, st = set(), [(s6,s7)]
        while st:
            x = st.pop()
            if x in orb: continue
            orb.add(x)
            for f in (pre, post, swap): st.append(f(x))
        seen |= orb; orbits.append(sorted(orb))

def n_of(s): return 6*ix[s[0]] + ix[s[1]]
WEIGHTS = {}
for orb in orbits:
    rep = min(n_of(s) for s in orb)
    WEIGHTS[f"{rep:02d}"] = len(orb)
DUPS = [("14", "00", "pre"), ("06", "01", "swap"), ("34", "02", "post")]
ALL = sorted(WEIGHTS) + [d[0] for d in DUPS]
assert sorted(WEIGHTS) == ["00","01","02","03","04","05","07","09"], sorted(WEIGHTS)

vals = {}
for d in ("q1","q2"):
    for f in glob.glob(f"/home/claude/gct-run/{d}/r_*.out"):
        xx = f[-6:-4]
        m = re.search(r"VALUE (-?\d+) \(final states (\d+)\)", open(f).read())
        if m: vals[xx] = (int(m.group(1)), int(m.group(2)))

missing = [x for x in ALL if x not in vals]
if missing:
    print(f"INCOMPLETE: missing {missing} ({len(vals)}/11 done)")
    sys.exit(1)
bad = [x for x,(v,ns) in vals.items() if not (ns == 1 or (ns == 0 and v == 0))]
if bad:
    print(f"ERROR: invalid (VALUE, states) for {bad}")
    sys.exit(2)
sz = sorted(x for x,(v,ns) in vals.items() if ns == 0 and v == 0)
if sz: print(f"structural/cancelled zeros: {sz}")

fail = False
for dup, rep, name in DUPS:
    ok = vals[dup][0] == vals[rep][0]
    print(f"gate {name}: V({dup})={vals[dup][0]:+d} vs V({rep})={vals[rep][0]:+d} -> {'MATCH' if ok else 'MISMATCH!!'}")
    fail = fail or not ok
if fail:
    print("GATE FAILURE — do not assemble."); sys.exit(3)

for x in sorted(WEIGHTS):
    print(f"  {x}: {vals[x][0]:+d}  (weight {WEIGHTS[x]})")
total = sum(WEIGHTS[x]*vals[x][0] for x in WEIGHTS)
print(f"TOTAL_Q = {total}")
print("NONZERO -> independent second-point k=1 certificate" if total != 0
      else "ZERO -> h1 vanishes at Q too; report before interpreting")
