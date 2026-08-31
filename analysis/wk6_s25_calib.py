#!/usr/bin/env python3
"""Session 25 -- the brief's calibration battery, reproduced from my own routines."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_core import *
from math import comb

ok = True
def ck(name, got, want):
    global ok
    good = got == want
    ok &= good
    print(("PASS " if good else "FAIL ") + name + "  got=%s want=%s" % (got, want))

# 1. Sym^2(Sym^3) = s_(6) + s_(4,2)  ->  a((2,2,2),2) = 0
ck("Sym^2(Sym^3) constituents", sorted(amb_row(2,3,9).items()), [((4,2),1),((6,),1)])
ck("a((2,2,2),2) [det_3 ambient]", a_of((2,2,2),2,3,9), 0)

# 2. stratification of the det_3 ambient
for delta, want in ((2,(11,9,2,0)), (3,(30,25,5,0)), (4,(73,61,12,0)),
                    (5,(157,129,27,1)), (6,(318,251,55,12))):
    A = amb_row(delta,3,9)
    tot = sum(1 for l in parts(3*delta) if len(l) <= 9)
    z  = sum(1 for l in parts(3*delta) if len(l) <= 9 and A.get(l,0)==0)
    o  = sum(1 for v in A.values() if v==1)
    t  = sum(1 for v in A.values() if v>=2)
    ck("det_3 ambient stratification delta=%d (tot,a=0,a=1,a>=2)"%delta, (tot,z,o,t), want)
A5 = amb_row(5,3,9)
ck("unique a>=2 weight at delta=5", [l for l,v in A5.items() if v>=2], [(9,4,2)])

# 3. Kronecker
ck("g((9,4,2),(5,5,5),(5,5,5))", kron((9,4,2),(5,5,5),(5,5,5)), 3)

# 4. m_det sums and supports at n=3
for delta, ssum, ssup in ((2,3,3),(3,11,10),(4,43,34)):
    vals = [m_det(l,3,delta) for l in parts(3*delta) if len(l)<=9]
    ck("m_det n=3 delta=%d (sum,support)"%delta, (sum(vals), sum(1 for v in vals if v)),
       (ssum, ssup))
row2 = {l:m_det(l,3,2) for l in parts(6) if len(l)<=9 and m_det(l,3,2)}
ck("m_det n=3 delta=2 row", sorted(row2.items()), [((2,2,2),1),((4,2),1),((6,),1)])

# 5. the ambient global identity: sum_lam a * dim S_lam = dim Sym^delta(Sym^d C^N)
for (delta,d,N) in ((2,3,9),(3,3,9),(4,3,9),(2,4,16),(3,4,16),(2,5,25),(4,4,2),(6,4,2)):
    D = comb(comb(N+d-1,d)+delta-1, delta)
    got = sum(v*dimS(l,N) for l,v in amb_row(delta,d,N).items())
    ck("ambient dimension identity (delta=%d,d=%d,N=%d)"%(delta,d,N), got, D)

# 6. World A ambient: a = Gaussian-binomial difference, two routes
def box(delta, b):
    """#partitions of b into at most 4 parts each <= delta (delta x 4 box)."""
    res = [0]*(4*delta+1)
    def rec(k, s, mx):
        if k == 4:
            res[s] += 1; return
        for p in range(0, mx+1):
            rec(k+1, s+p, p)
    rec(0, 0, delta)
    return res[b] if 0 <= b <= 4*delta else 0
badA=[]
for delta in range(1,15):
    A = amb_row(delta,4,2)
    for b in range(0,2*delta+1):
        r1 = a_of((4*delta-b,b),delta,4,2)
        r2 = box(delta,b) - (box(delta,b-1) if b else 0)
        if r1!=r2: badA.append((delta,b,r1,r2))
ck("World A: plethysm == Gaussian-binomial difference (delta<=14)", badA, [])

nz = [(d,b) for d in range(1,15) for b in range(0,2*d+1)
      if a_of((4*d-b,b),d,4,2)==0]
ge2= [(d,b) for d in range(1,15) for b in range(0,2*d+1)
      if a_of((4*d-b,b),d,4,2)>=2]
print("World A delta=1..14 : %d weights, a=0 in %d, a>=2 in %d"
      % (sum(2*d+1 for d in range(1,15)), len(nz), len(ge2)))
print("World A delta=2..14 : %d weights, a=0 in %d, a>=2 in %d   (brief: 221 / 27 / 134)"
      % (sum(2*d+1 for d in range(2,15)),
         len([x for x in nz if x[0]>=2]), len([x for x in ge2 if x[0]>=2])))
print()
print("ALL CALIBRATIONS PASSED" if ok else "*** SOME CALIBRATION FAILED ***")
