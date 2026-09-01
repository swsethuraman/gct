#!/usr/bin/env python3
"""
Session 29 -- the cheapest detector: the whole Hilbert function.

dim C[D_r^f]_delta = rank of the evaluation matrix on ALL degree-delta monomials
in the coefficient functionals (no weight restriction).  If that is less than
dim Sym^delta(Sym^n C^r) the ideal is nonzero at that degree, and only then is
it worth localising by weight.  One rank per degree instead of one per weight.
"""
import sys, random, time, itertools
from math import comb
sys.path.insert(0, '/root/gct/analysis')
from wk8_s29_core import exps, restrict, rank_mod, det_form, per_padded, PRIMES

def hilb(f, N, n, r, delta, npts=None, seed=5, bound=30):
    A = exps(n, r); nA = len(A)
    mons = list(itertools.combinations_with_replacement(range(nA), delta))
    nc = len(mons)
    K = npts if npts else nc + 20
    rnd = random.Random(seed)
    rows = []
    for _ in range(K):
        As = [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]
        co = restrict(f, N, n, r, As)
        v = []
        for m in mons:
            x = 1
            for k in m:
                x *= co.get(A[k], 0)
                if x == 0: break
            v.append(x)
        rows.append(v)
    rk = [rank_mod(rows, nc, p) for p in PRIMES]
    assert rk[0] == rk[1], (delta, rk)
    return rk[0], nc

if __name__ == '__main__':
    r = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    d4, N4 = det_form(4); p3, Np3 = per_padded(3, 4); p2, Np2 = per_padded(2, 4)
    print("r = %d.  ambient dim = C(%d+delta-1, delta) with C(r+3,4) = %d symbols"
          % (r, comb(r + 3, 4), comb(r + 3, 4)))
    print("delta | ambient |  det_4  | per_3^pad | per_2^pad |  ideal codims")
    for delta in range(2, dmax + 1):
        t0 = time.time()
        row = []
        for f, N in ((d4, N4), (p3, Np3), (p2, Np2)):
            rk, nc = hilb(f, N, 4, r, delta)
            row.append((rk, nc))
        nc = row[0][1]
        print("  %2d  | %7d | %7d | %9d | %9d |  %d / %d / %d   [%.0fs]"
              % (delta, nc, row[0][0], row[1][0], row[2][0],
                 nc - row[0][0], nc - row[1][0], nc - row[2][0], time.time() - t0))
        sys.stdout.flush()
