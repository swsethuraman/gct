#!/usr/bin/env python3
"""Which side carries the bigger deficit?  (Sign analysis for the recommendation.)"""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_worldA import *
tab = build(); D = DMAX
SUB = {'Gam': {'Gam','tau','Q','Iz','Jz','Ac','D'}, 'tau': {'tau','Iz','Jz','Ac','D'},
       'Q': {'Q','D'}, 'Iz': {'Iz'}, 'Jz': {'Jz'}, 'Ac': {'Ac'}, 'D': {'D'}}

# mean deficit per variety
print("mean deficit per closure over all weights delta<=%d (dim in brackets):" % D)
for X in NAMES:
    s = [tab[(X, d, b)][2] for d in range(1, D+1) for b in range(0, 2*d+1)]
    print("   %-4s [dim %d] : mean def = %7.3f   max = %d"
          % (X, DIMS[X], sum(s)/len(s), max(s)))
print()

# among cells carrying an obstruction, how does sign(Def) relate to dim?
buckets = {}
for A in NAMES:
    for B in NAMES:
        if A == B or A in SUB[B]:  continue
        for d in range(1, D+1):
            for b in range(0, 2*d+1):
                mA,uA,fA = tab[(A,d,b)]; mB,uB,fB = tab[(B,d,b)]
                Dob, Pw, Df = uB-uA, mB-mA, fB-fA
                key = ('dim B < dim A' if DIMS[B] < DIMS[A] else
                       'dim B > dim A' if DIMS[B] > DIMS[A] else 'dim B = dim A')
                s = buckets.setdefault(key, {'Def<0':0,'Def=0':0,'Def>0':0,
                                             'obs':0,'killed':0})
                s['Def<0' if Df<0 else ('Def=0' if Df==0 else 'Def>0')] += 1
                if Dob>0: s['obs'] += 1
                if Pw>0 and Dob<=0: s['killed'] += 1
for k in sorted(buckets):
    s = buckets[k]
    print("%-15s : Def<0 %5d | Def=0 %5d | Def>0 %5d || obstructions %4d, PW-obstructions killed %4d"
          % (k, s['Def<0'], s['Def=0'], s['Def>0'], s['obs'], s['killed']))
print()
print("reading: Def = def_B - def_A.  Def < 0 means the ambient-side closure A")
print("carries the larger deficit, which is the sign that FAVOURS an obstruction")
print("to B subset A.")

# --- how close does the deficit come to flipping a non-obstruction?
near = {}
best = None
for A in NAMES:
    for B in NAMES:
        if A == B or A in SUB[B]: continue
        for d in range(1, D+1):
            for b in range(0, 2*d+1):
                mA,uA,fA = tab[(A,d,b)]; mB,uB,fB = tab[(B,d,b)]
                Dob, Pw, Df = uB-uA, mB-mA, fB-fA
                if Pw <= 0 and Df < 0:            # deficit pushing the right way
                    near[Dob] = near.get(Dob, 0) + 1
                    if best is None or Dob > best[0]:
                        best = (Dob, A, B, d, 4*d-b, b, mA, uA, fA, mB, uB, fB, Pw, Df)
print()
print("cells with P <= 0 AND Def < 0 (deficit pushing towards an obstruction):")
print("   distribution of D = P - Def :",
      {k: near[k] for k in sorted(near, reverse=True)[:8]}, "...")
print("   best (largest D) case:", best)
print("   D > 0 would be a deficit-driven obstruction; the maximum attained is",
      max(near) if near else None)
