#!/usr/bin/env python3
"""
Session 42 -- census of the obstruction-eligible region for the reducible engine:

    n = 4,  6 <= ell(lam) <= ELL_MAX,  lam_1 >= delta,  a(lam, delta) >= 1,  delta in DELTAS.

Per cell: a (plethysm, wk8_s30_pleth.amb -- symmetric-function route, no r),
N_S (weight-space dimension by the TAIL DP: a monomial of weight lam is a
multiset of delta quartic exponents alpha; since |alpha| = 4 the x_1-exponent
is determined by the tail (alpha_2..alpha_r), so N_S = number of delta-multisets
of tails beta, |beta| <= 4, with sum = (lam_2..lam_r) -- a numpy DP on an array
of shape (delta+1, lam_2+1, ..., lam_r+1)), |Stab_W(lam)|, the lower bound
n_chi >= N_S/|Stab| (exact n_chi needs the orbit enumeration and is left to
the sweep), h_pad (wk9_s42_hpad: the normalisation bound), and the h_pad < a
flag (a pad-forced ideal, proved without any rank).

usage: python3 wk9_s42_census.py [--deltas 7,8] [--ellmax 8] [--out results/s42_census.json]
"""
import sys, os, time, json
from math import factorial
from collections import Counter
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import amb
from wk9_s42_hpad import h_pad

def tails(r, n=4):
    """all beta in N^{r-1} with |beta| <= n."""
    out = []
    def rec(k, left, cur):
        if k == r - 1: out.append(tuple(cur)); return
        for v in range(left + 1): rec(k + 1, left - v, cur + [v])
    rec(0, n, [])
    return out

def N_S_tail(lam, delta, n=4):
    """weight-space dimension by the tail DP (numpy)."""
    lam = tuple(lam); r = len(lam)
    if sum(lam) != n * delta: return 0
    tail = lam[1:]
    shape = (delta + 1,) + tuple(t + 1 for t in tail)
    F = np.zeros(shape, dtype=object)
    F[(0,) * len(shape)] = 1
    for beta in tails(r, n):
        if any(beta[i] > tail[i] for i in range(r - 1)): continue
        # multiply by 1/(1 - t x^beta):  F[d, w] += F[d-1, w-beta]  for d = 1..delta (in increasing d)
        src = tuple(slice(0, tail[i] + 1 - beta[i]) for i in range(r - 1))
        dst = tuple(slice(beta[i], tail[i] + 1) for i in range(r - 1))
        for d in range(1, delta + 1):
            F[(d,) + dst] += F[(d - 1,) + src]
    return int(F[(delta,) + tail])

def stab_order(lam):
    o = 1
    for v, k in Counter(lam).items(): o *= factorial(k)
    return o

def census(deltas, ellmax, ellmin=6, n=4, verbose=True):
    rows = []
    for delta in deltas:
        t0 = time.time()
        A = amb(delta, n, ellmax)
        if verbose: print(f"delta {delta}: plethysm done ({time.time()-t0:.0f}s), {len(A)} weights with <= {ellmax} rows", flush=True)
        for lam, a in sorted(A.items()):
            r = len(lam)
            if r < ellmin or r > ellmax or lam[0] < delta or a < 1: continue
            ns = N_S_tail(lam, delta, n)
            so = stab_order(lam)
            hp = h_pad(lam, delta)
            rows.append(dict(lam=list(lam), delta=delta, ell=r, a=a, N_S=ns, stab=so,
                             nchi_lb=(ns + so - 1) // so, h_pad=hp, hpad_lt_a=(hp < a), bal=lam[0] - lam[-1]))
        if verbose: print(f"delta {delta}: {sum(1 for x in rows if x['delta'] == delta)} region cells ({time.time()-t0:.0f}s)", flush=True)
    return rows

if __name__ == '__main__':
    args = sys.argv[1:]
    deltas = [7, 8]; ellmax = 8; out = os.path.join(HERE, '..', 'results', 's42_census.json')
    i = 0
    while i < len(args):
        if args[i] == '--deltas': deltas = [int(x) for x in args[i + 1].split(',')]; i += 2
        elif args[i] == '--ellmax': ellmax = int(args[i + 1]); i += 2
        elif args[i] == '--out': out = args[i + 1]; i += 2
        else: i += 1
    rows = census(deltas, ellmax)
    prev = []
    if os.path.exists(out):
        prev = [x for x in json.load(open(out)) if x['delta'] not in deltas]
    json.dump(prev + rows, open(out, 'w'))
    print("wrote", out, len(prev + rows))
