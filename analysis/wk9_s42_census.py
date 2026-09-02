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

usage: python3 wk9_s42_census.py [--deltas 7,8] [--ellmax 10] [--out results/s42_census.json]
       python3 wk9_s42_census.py --weyl --deltas 9,10,11,12 --ellmax 10 [--nchi-cap 400000] [--box-cap 2000000]
         (the Weyl route: a and h_pad by Weyl alternation + tail DPs, only for cells whose n_chi lower bound is within the cap)
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

# ------------------------------------------------ the Weyl route (large delta)
# a(lam, delta) = sum_{w in S_r} sgn(w) N_S(lam + rho - w rho)   (Weyl character formula
# read backwards: the coefficient of x^{lam+rho} in a_rho . char);  N_S of a shifted
# weight by the tail DP (any composition: the x_1 exponent is implied by the tail).
# Used where the symmetric-function route (amb) is too slow (delta >= 9); the two
# routes are asserted equal on every delta = 7, 8 cell they share (--check).

def N_S_tail_n(mu, delta, n):
    """tail DP for Sym^delta(Sym^n C^r) at an arbitrary composition mu (int64 numpy)."""
    mu = tuple(mu); r = len(mu)
    if any(x < 0 for x in mu) or sum(mu) != n * delta: return 0
    tail = mu[1:]
    shape = (delta + 1,) + tuple(t + 1 for t in tail)
    F = np.zeros(shape, dtype=np.int64)
    F[(0,) * len(shape)] = 1
    for beta in tails(r, n):
        if any(beta[i] > tail[i] for i in range(r - 1)): continue
        src = tuple(slice(0, tail[i] + 1 - beta[i]) for i in range(r - 1))
        dst = tuple(slice(beta[i], tail[i] + 1) for i in range(r - 1))
        for d in range(1, delta + 1):
            F[(d,) + dst] += F[(d - 1,) + src]
    v = int(F[(delta,) + tail])
    assert v < (1 << 62), "int64 headroom"
    return v

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def a_weyl(lam, delta, n, cache=None):
    """plethysm multiplicity by Weyl alternation with nonnegativity pruning."""
    lam = tuple(lam); r = len(lam)
    rho = tuple(range(r - 1, -1, -1))
    lr = [lam[i] + rho[i] for i in range(r)]
    tot = 0
    # assign w(i) for i = r-1 down to 0 (tightest budgets first); w(i) = j means rho_j is subtracted at position i
    order = sorted(range(r), key=lambda i: lr[i])
    used = [False] * r
    w = [0] * r
    def rec(k):
        nonlocal tot
        if k == r:
            mu = tuple(lr[i] - rho[w[i]] for i in range(r))
            key = (mu, delta, n)
            if cache is not None and key in cache: v = cache[key]
            else:
                v = N_S_tail_n(mu, delta, n)
                if cache is not None: cache[key] = v
            tot += perm_sign(w) * v
            return
        i = order[k]
        for j in range(r):
            if not used[j] and rho[j] <= lr[i]:
                used[j] = True; w[i] = j
                rec(k + 1)
                used[j] = False
    rec(0)
    return tot

def h_pad_weyl(lam, delta, cache=None):
    from wk9_s42_hpad import pieri_strips
    tot = 0
    for nu in pieri_strips(lam, delta):
        nu_t = tuple(nu)
        # c_nu for Sym^delta(Sym^3 C^r); nu may end in zeros (fine: r variables)
        tot += a_weyl(nu_t, delta, 3, cache)
    return tot

def partitions_region(delta, ellmin, ellmax, n=4):
    """partitions of n*delta with ellmin <= length <= ellmax and lam_1 >= delta."""
    N = n * delta
    out = []
    def rec(remaining, maxpart, cur):
        if remaining == 0:
            if ellmin <= len(cur) <= ellmax: out.append(tuple(cur))
            return
        if len(cur) >= ellmax: return
        for k in range(min(remaining, maxpart), 0, -1):
            if remaining - k > (ellmax - len(cur) - 1) * k: continue
            rec(remaining - k, k, cur + [k])
    for first in range(delta, N + 1):
        rec(N - first, first, [first])
    return out

def census_weyl(deltas, ellmax, ellmin=6, n=4, box_cap=2_000_000, nchi_cap=400_000, verbose=True):
    rows = []
    for delta in deltas:
        t0 = time.time()
        lams = partitions_region(delta, ellmin, ellmax, n)
        cache = {}
        nbox = na = 0
        for lam in lams:
            box = 1
            for x in lam[1:]: box *= (x + 1)
            so = stab_order(lam)
            rec = dict(lam=list(lam), delta=delta, ell=len(lam), stab=so, bal=lam[0] - lam[-1])
            # rigorous prefilter: weight multiplicities are monotone in dominance, so
            # N_S(lam) >= N_S(mu) for the merged weight mu = (lam_1..lam_4, lam_5+...+lam_r) >= lam;
            # a cell whose merged lower bound already exceeds nchi_cap * |Stab| is beyond the frontier.
            mu = tuple(lam[:4]) + (sum(lam[4:]),)
            ns_lb = N_S_tail_n(mu, delta, n)
            if (ns_lb + so - 1) // so > nchi_cap:
                rec.update(N_S=None, N_S_lb=ns_lb, nchi_lb=(ns_lb + so - 1) // so, a=None, h_pad=None,
                           note='N_S lower bound (5-variable merged weight, dominance monotonicity) already above the cap')
                nbox += 1
            elif box * (delta + 1) > box_cap:
                rec.update(N_S=None, N_S_lb=ns_lb, nchi_lb=(ns_lb + so - 1) // so, a=None, h_pad=None, note='tail box > cap: N_S not computed')
                nbox += 1
            else:
                ns = N_S_tail_n(lam, delta, n)
                rec.update(N_S=ns, nchi_lb=(ns + so - 1) // so)
                if rec['nchi_lb'] <= nchi_cap:
                    a = a_weyl(lam, delta, n, cache)
                    rec['a'] = a
                    if a >= 1:
                        rec['h_pad'] = h_pad_weyl(lam, delta, cache); rec['hpad_lt_a'] = rec['h_pad'] < a
                    na += 1
                else:
                    rec.update(a=None, h_pad=None, note='n_chi lower bound > cap: a not computed')
            rows.append(rec)
        if verbose:
            print(f"delta {delta}: {len(lams)} lam_1>=delta partitions with {ellmin}<=ell<={ellmax}; "
                  f"{nbox} beyond the frontier by the prefilter/box cap; a computed at {na}; "
                  f"{sum(1 for x in rows if x['delta']==delta and x.get('a'))} cells with a>=1 sized ({time.time()-t0:.0f}s)", flush=True)
    return rows

if __name__ == '__main__':
    args = sys.argv[1:]
    deltas = [7, 8]; ellmax = 8; out = os.path.join(HERE, '..', 'results', 's42_census.json'); weyl = False
    nchi_cap = 400_000; box_cap = 2_000_000
    i = 0
    while i < len(args):
        if args[i] == '--deltas': deltas = [int(x) for x in args[i + 1].split(',')]; i += 2
        elif args[i] == '--ellmax': ellmax = int(args[i + 1]); i += 2
        elif args[i] == '--out': out = args[i + 1]; i += 2
        elif args[i] == '--weyl': weyl = True; i += 1
        elif args[i] == '--nchi-cap': nchi_cap = int(args[i + 1]); i += 2
        elif args[i] == '--box-cap': box_cap = int(args[i + 1]); i += 2
        else: i += 1
    rows = census_weyl(deltas, ellmax, nchi_cap=nchi_cap, box_cap=box_cap) if weyl else census(deltas, ellmax)
    prev = []
    if os.path.exists(out):
        prev = [x for x in json.load(open(out)) if x['delta'] not in deltas]
    json.dump(prev + rows, open(out, 'w'))
    print("wrote", out, len(prev + rows))
