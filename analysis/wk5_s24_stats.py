#!/usr/bin/env python3
"""Session 24 -- what the deficit part actually DOES in World A."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_worldA import *

tab = build(); D = DMAX
SUB = {'Gam': {'Gam','tau','Q','Iz','Jz','Ac','D'}, 'tau': {'tau','Iz','Jz','Ac','D'},
       'Q': {'Q','D'}, 'Iz': {'Iz'}, 'Jz': {'Jz'}, 'Ac': {'Ac'}, 'D': {'D'}}

cnt = {'PW+real': 0, 'PW+killed': 0, 'deficit-driven': 0, 'neither': 0}
defsign = {'<0': 0, '=0': 0, '>0': 0}
killed_examples, helped_examples = [], []
maxneg = None
for A in NAMES:
    for B in NAMES:
        if A == B: continue
        for d in range(1, D + 1):
            for b in range(0, 2 * d + 1):
                mA, uA, fA = tab[(A, d, b)]; mB, uB, fB = tab[(B, d, b)]
                Dob, Pw, Df = uB - uA, mB - mA, fB - fA
                defsign['<0' if Df < 0 else ('=0' if Df == 0 else '>0')] += 1
                if Pw > 0 and Dob > 0:   cnt['PW+real'] += 1
                elif Pw > 0 and Dob <= 0:
                    cnt['PW+killed'] += 1
                    if len(killed_examples) < 6:
                        killed_examples.append((A,B,d,4*d-b,b,mA,uA,fA,mB,uB,fB,Pw,Df,Dob))
                elif Pw <= 0 and Dob > 0: cnt['deficit-driven'] += 1
                else: cnt['neither'] += 1
                if Df < 0 and Dob > 0:
                    if len(helped_examples) < 6:
                        helped_examples.append((A,B,d,4*d-b,b,Pw,Df,Dob))
                if Df < 0 and (maxneg is None or Df < maxneg[0]):
                    maxneg = (Df, A, B, d, 4*d-b, b, Pw, Dob)

tot = sum(cnt.values())
print("World A, delta <= %d, all 42 ordered pairs, %d (pair,weight) cells\n" % (D, tot))
print("  Peter-Weyl sees an obstruction AND it is real   (P>0, D>0):  %6d" % cnt['PW+real'])
print("  Peter-Weyl sees one but the deficit KILLS it    (P>0, D<=0): %6d" % cnt['PW+killed'])
print("  DEFICIT-DRIVEN: obstruction invisible classically(P<=0,D>0): %6d" % cnt['deficit-driven'])
print("  no obstruction either way                                  : %6d" % cnt['neither'])
print()
print("sign of the deficit part Def = def_B - def_A over all cells:")
print("   Def < 0 (deficit favours the obstruction): %6d" % defsign['<0'])
print("   Def = 0 (deficit inert)                  : %6d" % defsign['=0'])
print("   Def > 0 (deficit opposes the obstruction): %6d" % defsign['>0'])
print()
print("most negative Def anywhere (Def, A, B, delta, a, b, P, D):", maxneg)
print()
print("examples where the CLASSICAL side sees an obstruction that is NOT one")
print("(P>0 but mult_B <= mult_A -- the deficit destroys it):")
for e in killed_examples:
    print("   A=%-3s B=%-3s delta=%2d lam=(%d,%d): mA=%d uA=%d defA=%d | mB=%d uB=%d defB=%d | P=%d Def=%d D=%d" % e)
print()
print("examples where Def<0 (deficit strictly enlarges a real obstruction):")
for e in helped_examples:
    print("   A=%-3s B=%-3s delta=%2d lam=(%d,%d): P=%d Def=%d D=%d" % e)
