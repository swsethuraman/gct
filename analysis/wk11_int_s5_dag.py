"""The memoised shape DAG behind Sol S5's one-block recursion (batch 11).

S5 proves the exact recursion

    (S^{lam_delta})^{K_delta} = sum over lam_delta/mu a horizontal 4-strip of
                                (S^mu)^{H_{delta-1}},
    M_{lam_delta} = ker(tau - I) on that precursor,

and nominates B_delta = sum of the predecessor multiplicities as the decisive
economic number.  B_delta measures ONE level.  A real implementation is
recursive, so what it actually pays is the size of the memoised DAG of distinct
(shape, delta) pairs reachable from the top rung down to delta = 1 -- every node
of which needs its own multiplicity space before the level above it can be
formed.  This counts that DAG.  Pure combinatorics: no plethysm, seconds to run.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk11_int_bdelta import lam_of, horiz_strips

for top in (12, 24):
    lam = lam_of(top)
    level = {lam}
    tot = 0
    print(f'--- from lambda_{top} = {lam} ---', flush=True)
    for d in range(top, 1, -1):
        nxt = set()
        for mu in level:
            nxt |= set(horiz_strips(mu, 4))
        print(f'  delta={d-1:2d}: {len(nxt):6d} distinct shapes  (from {len(level)} at delta={d})', flush=True)
        tot += len(nxt)
        level = nxt
        if len(level) > 400000:
            print('  ... exceeded 400k distinct shapes, stopping'); break
    print(f'  total distinct (shape, delta) nodes below the top: {tot}\n', flush=True)
