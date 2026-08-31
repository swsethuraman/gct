#!/usr/bin/env python3
"""Session 24 -- the search: deficit-driven obstructions in World A."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_worldA import *

tab = build()
D = DMAX

# containment poset (X below Y  <=>  X subset of Y), verified by invariants
SUB = {
 'Gam': {'Gam','tau','Q','Iz','Jz','Ac','D'},
 'tau': {'tau','Iz','Jz','Ac','D'},
 'Q'  : {'Q','D'},
 'Iz' : {'Iz'}, 'Jz': {'Jz'}, 'Ac': {'Ac'}, 'D': {'D'},
}

rows_all, rows_def = [], []
for A in NAMES:
    for B in NAMES:
        if A == B:
            continue
        contained = A in SUB[B] and False  # B subset of A ?
        Bsub = A in SUB[B]                  # SUB[B] = things B is contained in
        for d in range(1, D + 1):
            for b in range(0, 2 * d + 1):
                mA, uA, fA = tab[(A, d, b)]
                mB, uB, fB = tab[(B, d, b)]
                Dob = uB - uA                 # obstruction to  B subset A
                Pw  = mB - mA                 # Peter-Weyl part
                Df  = fB - fA                 # deficit part
                assert Dob == Pw - Df
                if Dob > 0:
                    rows_all.append((A, B, d, b, mA, uA, fA, mB, uB, fB, Pw, Df, Dob, Bsub))
                    if Pw <= 0:
                        rows_def.append(rows_all[-1])

print("ordered pairs searched: %d ; weights per pair: %d ; delta <= %d"
      % (len(NAMES) * (len(NAMES) - 1),
         sum(1 for d in range(1, D + 1) for b in range(0, 2 * d + 1)), D))
print("total multiplicity obstructions found (mult_B > mult_A): %d" % len(rows_all))
print("of which DEFICIT-DRIVEN (P <= 0):                        %d" % len(rows_def))
print()

# how many obstruction pairs occur, and is the containment poset respected?
seen = {}
for r in rows_all:
    seen.setdefault((r[0], r[1]), 0)
    seen[(r[0], r[1])] += 1
print("pairs (A,B) admitting an obstruction to B subset A, with count:")
for k in sorted(seen, key=lambda k: -seen[k]):
    print("   A=%-4s B=%-4s : %4d weights   (B subset A? %s)"
          % (k[0], k[1], seen[k], k[0] in SUB[k[1]]))
print()
# sanity: no obstruction may exist when B IS contained in A
viol = [r for r in rows_all if r[13]]
print("obstructions violating a true containment (must be 0):", len(viol))
print()

# which pairs are incomparable yet admit NO obstruction at all?
print("incomparable ordered pairs with NO multiplicity obstruction at delta<=%d:" % D)
for A in NAMES:
    for B in NAMES:
        if A == B: continue
        if A in SUB[B]:   continue   # B really is inside A
        if (A, B) not in seen:
            print("   A=%-4s B=%-4s  (B not subset A, yet mult_B <= mult_A everywhere)" % (A, B))
print()
if rows_def:
    print("DEFICIT-DRIVEN OBSTRUCTIONS:")
    for r in rows_def[:40]:
        print("   A=%s B=%s delta=%d lam=(%d,%d) mA=%d uA=%d fA=%d | mB=%d uB=%d fB=%d | P=%d Def=%d D=%d"
              % (r[0], r[1], r[2], 4*r[2]-r[3], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12]))
else:
    print("NO deficit-driven obstruction exists in World A for delta <= %d." % D)
    print("Equivalently: every multiplicity obstruction in Sym^4 C^2 is already")
    print("a Peter-Weyl obstruction (m_B > m_A).")
