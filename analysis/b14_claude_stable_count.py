#!/usr/bin/env python3
"""Batch-14 strategy session (Claude) -- the stable-slice counter.

Proposition S (docs/s57_report.md, load-bearing part audited by B13-07) localises
a ladder at the leading quartic coefficient `u` and removes the cubic-in-s_1 term,
leaving

    Z = Sym^2 V' + Sym^3 V' + Sym^4 V',        V' = C^(ell-1)

with `a_inf(tail)` = the multiplicity of S_tail in Sym(Sym^2 + Sym^3 + Sym^4)(V').
This module computes, for any tail and any set of generator degrees:

  * `count_fast(w, degs)` -- the RAW weight space: the number of multisets of
    generators y_(d,alpha), d in degs, |alpha| = d, whose exponents sum to w.
    (Same object as `raw_weight_space` in analysis/wk12_s79_stable.py, which is
    hard-wired to 5 tail variables and degrees (2,3,4).)
  * `mult(lam, degs)` -- the multiplicity of S_lam, by Weyl alternation
        m_lam = sum_{w in S_n} sgn(w) * K(w(lam+rho) - rho),
    K = the raw weight-space count above (which is S_n-symmetric, so only the
    sorted key is memoised).

Two readings of `degs`:
  * `degs = (2,3,4)` -- the stable ambient multiplicity `a_inf(tail)` (Prop. S).
  * `degs = (1,2,3)` -- the stable REDUCIBLE-NORMALISATION target.  In the slice
    the reducible locus is {Q_4 = a Q_3 - a^2 Q_2 - a^4}, whose parametrisation
    (a, Q_2, Q_3) is birational onto it, so C[R'] embeds in
    C[V' + Sym^2 V' + Sym^3 V'].  At the LMR tail this returns 521, matching the
    banked h_pad(65,17,2^7; 24) = 521.  That agreement is evidence for the
    identification, not a proof of it.

CALIBRATION (run `--selftest`; all seven checks must pass):
  raw sizes at 5 tails vs the `raw_weight_space` field of results/s79_stable/*.json
      (4,4,3,2,0) 3716 | (5,2,2,2,2) 9166 | (5,3,2,2,1) 6922
      (6,2,2,2,1) 4636 | (6,3,3,1,0) 1668
  a_inf = 4 at (6,3,3,1,0) and (5,2,2,2,2)   [s79 part 1]

VALUES USED IN THE BATCH-14 MEMO (each ~70-95 s on 2 cores):
    python3 analysis/b14_claude_stable_count.py --mult 17,2,2,2,2,2,2,2              ->  274   (= banked a at the LMR cell)
    python3 analysis/b14_claude_stable_count.py --mult 17,2,2,2,2,2,2,2 --degs 1,2,3 ->  521   (= banked h_pad(24))
    python3 analysis/b14_claude_stable_count.py --mult 19,2,2,2,2,2,2,2              ->  392   (= banked a at (71,19,2^7)_26, so that cell is stable)
    python3 analysis/b14_claude_stable_count.py --mult 21,2,2,2,2,2,2,2              ->  533   (banked a at (69,21,2^7)_26 is 531, so that cell is NOT stable)
    python3 analysis/b14_claude_stable_count.py --raw 17,2,2,2,2,2,2,2               ->  7,212,907,703
        (= 1.43e6 x |Stab| = 5040; s57 sizes the same slice at ~1.4e6 orbit classes)

STATUS: scratch, single implementation, written for a strategy session; the
calibration above is the only cross-check it carries.  Anything load-bearing
should be recounted by a different method (see the batch-14 memo, slot 04).

usage:
    python3 analysis/b14_claude_stable_count.py --selftest
    python3 analysis/b14_claude_stable_count.py --raw  W [--degs D,D,D]
    python3 analysis/b14_claude_stable_count.py --mult W [--degs D,D,D]
where W is a comma-separated weight, e.g. 17,2,2,2,2,2,2,2.
"""
import argparse, functools, itertools, sys, time

import numpy as np

DEFAULT_DEGS = (2, 3, 4)


def gens(nv, degs=DEFAULT_DEGS):
    """every exponent vector alpha in Z^nv_{>=0} with |alpha| in degs."""
    return [a for d in degs
            for a in itertools.product(range(d + 1), repeat=nv) if sum(a) == d]


def count_fast(w, degs=DEFAULT_DEGS):
    """#multisets of generators with exponent sum exactly w.

    Unbounded knapsack over the generators, one array pass per generator; a
    float64 shadow array carries the same recursion and raises before int64
    silently overflows.  Returns (exact_count, float_shadow)."""
    w = tuple(int(x) for x in w)
    nv = len(w)
    dims = tuple(x + 1 for x in w)
    f = np.zeros(dims, dtype=np.int64); f[(0,) * nv] = 1
    g = np.zeros(dims, dtype=np.float64); g[(0,) * nv] = 1.0
    for a in gens(nv, degs):
        if any(a[k] > w[k] for k in range(nv)):
            continue
        src = tuple(slice(0, dims[k] - a[k]) for k in range(nv))
        dst = tuple(slice(a[k], dims[k]) for k in range(nv))
        maxm = min(w[k] // a[k] for k in range(nv) if a[k] > 0)
        acc, accg = f.copy(), g.copy()
        cur, curg = f, g
        for _ in range(1, maxm + 1):
            sh = np.zeros_like(cur); shg = np.zeros_like(curg)
            sh[dst] = cur[src]; shg[dst] = curg[src]
            cur, curg = sh, shg
            acc += cur; accg += curg
        f, g = acc, accg
        if g.max() > 9e18:
            raise OverflowError('int64 range exceeded; rerun with dtype=object')
    return int(f[tuple(w)]), float(g[tuple(w)])


@functools.lru_cache(maxsize=None)
def _K(mu, degs):
    """weight multiplicity, memoised on the sorted key (the count is symmetric)."""
    mu = tuple(sorted(mu, reverse=True))
    if min(mu) < 0:
        return 0
    return count_fast(mu, degs)[0]


def mult(lam, degs=DEFAULT_DEGS):
    """multiplicity of S_lam in Sym(sum_{d in degs} Sym^d V'), V' = C^len(lam)."""
    lam = tuple(int(x) for x in lam)
    n = len(lam)
    rho = list(range(n - 1, -1, -1))
    lr = [lam[i] + rho[i] for i in range(n)]
    total = 0
    for p in itertools.permutations(range(n)):
        mu = [lr[p[i]] - rho[i] for i in range(n)]
        if min(mu) < 0:
            continue
        sign, seen = 1, [False] * n
        for i in range(n):
            if not seen[i]:
                j, ln = i, 0
                while not seen[j]:
                    seen[j] = True; j = p[j]; ln += 1
                if ln % 2 == 0:
                    sign = -sign
        total += sign * _K(tuple(mu), degs)
    return total


SELFTEST_RAW = {(4, 4, 3, 2, 0): 3716, (5, 2, 2, 2, 2): 9166, (5, 3, 2, 2, 1): 6922,
                (6, 2, 2, 2, 1): 4636, (6, 3, 3, 1, 0): 1668}
SELFTEST_MULT = {(6, 3, 3, 1, 0): 4, (5, 2, 2, 2, 2): 4}


def selftest():
    ok = True
    for w, want in SELFTEST_RAW.items():
        got = count_fast(w)[0]
        ok &= got == want
        print(f'raw  {w}: {got} (s79: {want}) {"PASS" if got == want else "FAIL"}')
    for w, want in SELFTEST_MULT.items():
        got = mult(w)
        ok &= got == want
        print(f'a_inf {w}: {got} (s79: {want}) {"PASS" if got == want else "FAIL"}')
    print('SELFTEST', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--raw')
    ap.add_argument('--mult')
    ap.add_argument('--degs', default='2,3,4')
    args = ap.parse_args()
    degs = tuple(int(x) for x in args.degs.split(','))
    if args.selftest:
        return selftest()
    if args.raw:
        w = tuple(int(x) for x in args.raw.split(','))
        t = time.time(); n, shadow = count_fast(w, degs)
        print(f'raw {w} degs={degs}: {n} ({n:.3e}), {time.time() - t:.1f}s')
        return 0
    if args.mult:
        w = tuple(int(x) for x in args.mult.split(','))
        t = time.time(); m = mult(w, degs)
        print(f'mult {w} degs={degs}: {m}, {time.time() - t:.1f}s')
        return 0
    ap.print_help()
    return 2


if __name__ == '__main__':
    sys.exit(main())
