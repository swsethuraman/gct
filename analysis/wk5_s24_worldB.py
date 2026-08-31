#!/usr/bin/env python3
"""
Session 24 -- World B (ternary cubics, W = Sym^3 C^3).

Exact GL_3 plethysm  Sym^delta(Sym^3 C^3)  by weight counting + Weyl
alternation, then the two hypersurface orbit closures

   Fer  = closure(GL_3 . Fermat) = {S = 0},        deg 4, weight det^4
   Hes  = closure(GL_3 . f_m), generic Hesse member
        = {alpha S^3 + beta T^2 = 0},              deg 12, weight det^12

with m obtained by the RAY route (validated twice in World A):
   boundary of {S=0} is cut by T   (deg 6, det^6)
   boundary of {aS^3+bT^2=0} is cut by S (deg 4, det^4).
"""
from functools import lru_cache
import itertools, sys

RHO = (2, 1, 0)
MONS = [(i, j, 3 - i - j) for i in range(4) for j in range(4 - i) ]  # exps of x^i y^j z^k

@lru_cache(maxsize=None)
def wtcount(delta):
    """dict weight-triple -> #monomials of degree delta in the 10 coefficients."""
    dp = {(0, 0, 0, 0): 1}
    for mo in MONS:
        nd = {}
        for (n, a, b, c), v in dp.items():
            k = 0
            while n + k <= delta:
                key = (n + k, a + mo[0]*k, b + mo[1]*k, c + mo[2]*k)
                nd[key] = nd.get(key, 0) + v
                k += 1
        dp = nd
    out = {}
    for (n, a, b, c), v in dp.items():
        if n == delta:
            out[(a, b, c)] = out.get((a, b, c), 0) + v
    return out

PERMS = [((0,1,2),1), ((1,0,2),-1), ((0,2,1),-1), ((2,0,1),1), ((1,2,0),1), ((2,1,0),-1)]

def P3(delta, lam):
    if delta < 0 or min(lam) < 0: return 0
    if sum(lam) != 3 * delta: return 0
    W = wtcount(delta); tot = 0
    for p, sg in PERMS:
        mu = tuple(lam[i] + RHO[i] - RHO[p[i]] for i in range(3))
        if min(mu) < 0: continue
        tot += sg * W.get(mu, 0)
    return tot

def mult_hyp3(delta, lam, e, w):
    return P3(delta, lam) - P3(delta - e, tuple(x - w for x in lam))

MULT3 = {'Fer': lambda d, l: mult_hyp3(d, l, 4, 4),
         'Hes': lambda d, l: mult_hyp3(d, l, 12, 12)}
RAY   = {'Fer': (6, 6), 'Hes': (4, 4)}          # (e, w) of the boundary cutter

def m3(name, delta, lam, kmax=30):
    e, w = RAY[name]; seen = []
    for k in range(kmax):
        seen.append(MULT3[name](delta + k*e, tuple(x + k*w for x in lam)))
        if len(seen) >= 5 and len(set(seen[-4:])) == 1:
            return seen[-1]
    raise RuntimeError('ray did not stabilise')

def partitions_of(n, parts=3):
    for a in range(n, -1, -1):
        for b in range(min(a, n-a), -1, -1):
            c = n - a - b
            if 0 <= c <= b:
                yield (a, b, c)

if __name__ == '__main__':
    DM = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    # --- calibration against the paper: 254 deficit-positive weights, delta<=10
    tot = 0; per = {}
    for d in range(1, DM + 1):
        c = 0
        for lam in partitions_of(3*d):
            df = m3('Fer', d, lam) - MULT3['Fer'](d, lam)
            assert df >= 0, (d, lam, df)
            if df > 0: c += 1
        per[d] = c; tot += c
    print("World B: deficit-positive weights for {S=0} by delta:", per)
    print("total through delta = %d : %d   (paper: 254 through delta = 10)" % (DM, tot))
    print()
    # --- the pair (Fer, Hes)
    ddr = 0; obs = 0; killed = 0
    for d in range(1, min(DM, 8) + 1):
        for lam in partitions_of(3*d):
            mA, uA = m3('Fer', d, lam), MULT3['Fer'](d, lam)
            mB, uB = m3('Hes', d, lam), MULT3['Hes'](d, lam)
            for (A, B) in (((mA, uA), (mB, uB)), ((mB, uB), (mA, uA))):
                Dob = B[1] - A[1]; Pw = B[0] - A[0]
                if Dob > 0:
                    obs += 1
                    if Pw <= 0:
                        ddr += 1
                        print("   DEFICIT-DRIVEN:", d, lam, A, B)
                elif Pw > 0:
                    killed += 1
    print("pair {S=0} vs generic Hesse, delta <= %d:" % min(DM, 8))
    print("   multiplicity obstructions : %d" % obs)
    print("   deficit-driven            : %d" % ddr)
    print("   Peter-Weyl obstructions killed by the deficit : %d" % killed)
