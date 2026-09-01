#!/usr/bin/env python3
"""
Session 34 -- Phase 1: the census at (n, delta) = (4, 7), |lam| = 28.

Gate (two conditions, must_have_room semantics, need=2): ell(lam) >= 5 and
a(lam, 7) >= 2.  Per cell: a by TWO independent plethysm routes
(wk8_s30_pleth.amb and scripts/ambient_screen.stratify -- distinct
implementations; they must agree), N_S (weight-space dimension), balance
lam_1 - lam_ell, predicted memory 5.6e-8 * N_S^2 GB.

N_S is computed by an exact numpy knapsack DP (multisets of delta degree-4
exponent vectors summing to lam) and CROSS-CHECKED against
len(wk8_s30_core.monomials(...)) -- the definition the sweep uses -- on every
cell with DP count <= CHECK_CAP.  The DP and the enumeration are independent
codes for the same number.

Writes results/d7_census.md and results/d7_cells.json.  Also asserts that no
weight of ell >= 8 carries a > 0 (structural: Sym^7(Sym^4) has <= 7 rows).
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))
import numpy as np
from wk8_s30_pleth import amb
from wk8_s30_core import exps, monomials
import ambient_screen

DELTA, N = 7, 4
MEM_PER = 5.6e-8
BUDGET_S34 = 7.2          # this container (prereg section 3)
BUDGET_S30 = 6.5          # s30 reference budget
CHECK_CAP = 30000

def ns_dp(lam):
    """multisets of DELTA vectors from exps(N, r) summing to lam, exactly."""
    r = len(lam)
    A = exps(N, r)
    shape = tuple(x + 1 for x in lam)
    arr = [np.zeros(shape, dtype=np.int64) for _ in range(DELTA + 1)]
    arr[0][(0,) * r] = 1
    for v in A:
        if any(v[i] > lam[i] for i in range(r)):
            continue
        sl_to = tuple(slice(v[i], lam[i] + 1) for i in range(r))
        sl_from = tuple(slice(0, lam[i] + 1 - v[i]) for i in range(r))
        for c in range(1, DELTA + 1):        # ascending c: repetition allowed
            arr[c][sl_to] += arr[c - 1][sl_from]
    n = int(arr[DELTA][tuple(lam)])
    assert n >= 0
    return n

if __name__ == '__main__':
    t0 = time.time()
    print("plethysm route 1: wk8_s30_pleth.amb(7, 4, 16) ..."); sys.stdout.flush()
    A7 = amb(DELTA, N, 16)
    print("   %d weights with a > 0  [%.0fs]" % (len(A7), time.time() - t0)); sys.stdout.flush()

    # structural check: nothing at ell >= 8
    long_ = [lam for lam in A7 if len(lam) >= 8]
    assert not long_, ("ell>=8 weight with a>0 -- impossible", long_[:5])
    print("   asserted: no weight with ell >= 8 has a > 0")

    t1 = time.time()
    print("plethysm route 2: ambient_screen.stratify(4, 7, d=4) ..."); sys.stdout.flush()
    sys.setrecursionlimit(20000)
    S = {lam: v for lam, v in ambient_screen.stratify(4, DELTA, 4) if v}
    assert S == A7, ("plethysm routes disagree",
                     {k: (A7.get(k), S.get(k)) for k in set(A7) ^ set(S) or
                      [k for k in A7 if A7[k] != S.get(k)]})
    print("   routes agree on all %d weights  [%.0fs]" % (len(S), time.time() - t1))
    sys.stdout.flush()

    gate = sorted([(lam, av) for lam, av in A7.items()
                   if av >= 2 and len(lam) >= 5],
                  key=lambda c: tuple(-x for x in c[0]))
    print("gate (ell >= 5, a >= 2): %d cells" % len(gate)); sys.stdout.flush()

    cells = []
    for lam, av in gate:
        t = time.time()
        ns = ns_dp(lam)
        checked = False
        if ns <= CHECK_CAP:
            ne = len(monomials(N, len(lam), DELTA, lam))
            monomials.cache_clear()
            assert ne == ns, ("N_S routes disagree", lam, ns, ne)
            checked = True
        cells.append(dict(lam=list(lam), ell=len(lam), a=av,
                          balance=lam[0] - lam[-1], ns=ns,
                          gb=MEM_PER * ns * ns, ns_checked=checked))
        print("   %-26s ell=%d a=%-2d bal=%-2d N_S=%-8d %.2f GB%s [%.0fs]"
              % (str(lam), len(lam), av, lam[0] - lam[-1], ns,
                 MEM_PER * ns * ns, " (enum-checked)" if checked else "",
                 time.time() - t))
        sys.stdout.flush()

    cells.sort(key=lambda c: (c['ns'], tuple(-x for x in c['lam'])))
    for c in cells:
        c['feas_s34'] = c['gb'] <= BUDGET_S34
        c['feas_s30ref'] = c['gb'] <= BUDGET_S30
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           'results', 'd7_cells.json'), 'w') as fh:
        json.dump(dict(delta=DELTA, n=N, mem_per=MEM_PER,
                       budget_s34=BUDGET_S34, budget_s30ref=BUDGET_S30,
                       cells=cells), fh, indent=1)
    print("\n%d cells; %d feasible at %.1f GB (this container), %d at %.1f GB (s30 ref)"
          % (len(cells), sum(c['feas_s34'] for c in cells), BUDGET_S34,
             sum(c['feas_s30ref'] for c in cells), BUDGET_S30))
    print("total %.0fs" % (time.time() - t0))
