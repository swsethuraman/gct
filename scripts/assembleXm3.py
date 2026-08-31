#!/usr/bin/env python3
"""Assemble TOTAL(X_-3) from the 12-run point-independent grind.

NOTE: the arithmetic signature is 75,600, not 151,200 -- see results_Xm3.md;
f1Xm3_03 and f1Xm3_08 are both odd multiples of 75,600.

X_-3 = (x3+=x2, x4+=x1, x7+=x1, x8+=x0);  A = E(0,2)+E(1,1), B = E(1,1)+E(2,0);
Psi = -3, so the totals law predicts TOTAL = -3 x 1,152,144,000 = -3,456,432,000.

The 12 representatives are the orbits of the POINT-INDEPENDENT scheme
automorphisms only (swap and post-omega, proved in session 12); no point
symmetry is used in the assembly.  The point symmetry rho = (0 2) is checked
separately as four blind gates.  Orbits are computed here, not hardcoded.
"""
import re, glob, sys, itertools

perms = list(itertools.permutations((0,1,2)))
ix = {p:i for i,p in enumerate(perms)}
def comp(a,b): return tuple(a[b[i]] for i in range(3))
OM  = (2,1,0)          # scheme automorphism: post-composition by omega = (0 2)
RHO = (2,1,0)          # X_-3 point symmetry: pre-composition by rho = (0 2)

def orbits(gens):
    seen, out = set(), []
    for a in perms:
        for b in perms:
            if (a,b) in seen: continue
            orb, st = set(), [(a,b)]
            while st:
                x = st.pop()
                if x in orb: continue
                orb.add(x)
                for f in gens: st.append(f(x))
            seen |= orb; out.append(orb)
    return out

def post(s): return (comp(s[0],OM), comp(s[1],OM))
def swap(s): return (s[1], s[0])
def pre(s):  return (comp(RHO,s[0]), comp(RHO,s[1]))

def n_of(s): return 6*ix[s[0]] + ix[s[1]]
WEIGHTS = {}
for orb in orbits((post, swap)):
    WEIGHTS["%02d" % min(n_of(s) for s in orb)] = len(orb)
assert sum(WEIGHTS.values()) == 36
# the four gates the point symmetry predicts
GATES = []
for orb in orbits((post, swap, pre)):
    reps = sorted({"%02d" % min(n_of(t) for t in o)
                   for o in orbits((post, swap)) for s in o if s in orb})
    if len(reps) > 1: GATES.append(tuple(reps))
GATES = sorted(set(GATES))

vals = {}
for d in ("g1","g2"):
    for f in glob.glob(f"/home/claude/{d}/r_*.out"):
        xx = f[-6:-4]
        m = re.search(r"VALUE (-?\d+) \(final states (\d+)\)", open(f).read())
        if m: vals[xx] = (int(m.group(1)), int(m.group(2)))

need = sorted(WEIGHTS)
missing = [x for x in need if x not in vals]
print("reps:", need)
print("weights:", [WEIGHTS[x] for x in need], "sum", sum(WEIGHTS.values()))
for x in need:
    if x in vals:
        v, ns = vals[x]
        c = v/75600
        print(f"  {x}: {v:+15d}  weight {WEIGHTS[x]}  states {ns}"
              f"  cofactor(75600) {int(c) if v % 75600 == 0 else 'NOT 75600 x int: %s' % c}")
    else:
        print(f"  {x}: (pending)")
if missing:
    print(f"INCOMPLETE: missing {missing} ({len(need)-len(missing)}/{len(need)} done)")
bad = [x for x,(v,ns) in vals.items() if not (ns == 1 or (ns == 0 and v == 0))]
if bad: print("ERROR: invalid (VALUE, states) for", bad)

print("\npoint-symmetry gates (rho = (0 2)) -- blind, pre-registered:")
for g in GATES:
    have = [x for x in g if x in vals]
    if len(have) == len(g):
        ok = len({vals[x][0] for x in g}) == 1
        print(f"  {' = '.join(g)} : {[vals[x][0] for x in g]} -> {'MATCH' if ok else 'MISMATCH!!'}")
    else:
        print(f"  {' = '.join(g)} : pending")

if not missing and not bad:
    total = sum(WEIGHTS[x]*vals[x][0] for x in need)
    pred = -3456432000
    print(f"\nTOTAL(X_-3) = {total:+d}")
    print(f"predicted   = {pred:+d}   (Psi = -3 times TOTAL_C = 1,152,144,000)")
    print("ratio to TOTAL_C =", total/1152144000)
    print("VERDICT:", "CONFIRMED" if total == pred else "*** MISS -- REFUTATION, do not adjust anything ***")
    if total % 75600 == 0:
        print("cofactor units (75600):", total//75600, "(predicted -45720)")
else:
    known = sum(WEIGHTS[x]*vals[x][0] for x in need if x in vals)
    print(f"\npartial weighted sum so far: {known:+d}"
          f"   ({known/75600:+.0f} units of 75600, of a predicted -45720)")
