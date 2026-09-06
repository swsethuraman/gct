#!/usr/bin/env python3
"""
Session 57 -- the stable value of a along a ladder, and the stability threshold.

Developed after the pre-registration (it sharpens Lemma L; nothing pre-registered
depends on it).  Statement (proved in docs/s57_report.md, Proposition S):

  For a tail lam_bar = (lam_2, ..., lam_ell) with all parts > 0 and V' = C^{ell-1},

      a((4 delta - |lam_bar|, lam_bar), delta)  =  a_inf(lam_bar)   for every delta >= |lam_bar|,

  where a_inf(lam_bar) is the multiplicity of S_{lam_bar}(V') in the polynomial
  GL(V')-module Sym(Sym^2 V' (+) Sym^3 V' (+) Sym^4 V'), and a(., delta) <= a_inf for all delta.

Reason: a highest-weight vector of weight (4 delta - |lam_bar|, lam_bar) is
c^delta . phi(f / c) for a function phi on the chart {c = 1} of tail weight
lam_bar that is invariant under the unipotent radical (the substitutions
s_1 -> s_1 + t s_j, which act freely with quotient the slice {g_1 = 0}) and a
highest-weight vector for GL(V'); the chart has coordinate ring
Sym(V' (+) Sym^2 V' (+) Sym^3 V' (+) Sym^4 V') and the slice has coordinate ring
Sym(Sym^2 V' (+) Sym^3 V' (+) Sym^4 V'); phi has degree <= |lam_bar| because every
chart coordinate has tail weight >= 1; and phi lifts to degree delta iff
delta >= deg phi.

Computation: a_inf = sum_w sgn(w) K_inf(w(lam_bar + rho') - rho') over S_{ell-1},
with K_inf(mu) the number of multisets of monomials of degree 2, 3 or 4 in
ell - 1 variables with exponent sum mu (a box DP, no degree index), mod two
primes with CRT.  The same applies to h_pad's cubic side and to sk (which also
stabilise) but only a is needed here.

usage: python3 wk9_s57_stable.py --tails "2,2,2,2,2;17,2,2,2,2,2,2,2"
       python3 wk9_s57_stable.py --record        (every ladder through the six-row record)
       python3 wk9_s57_stable.py --region-l6     (every ladder of the ell = 6 region at delta 10-12)
"""
import sys, os, json, time, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (weyl_terms, sort_desc, crt2, negative_record, tail_of, load_s39, log,
                         P1, P2, ROOT)

CELLS = os.path.join(ROOT, 'results/s57_cells')

def monomials_deg(r, dmin, dmax):
    out = []
    def rec(k, left, cur):
        if k == r:
            if dmin <= sum(cur) <= dmax: out.append(tuple(cur))
            return
        for v in range(left + 1): rec(k + 1, left - v, cur + [v])
    rec(0, dmax, [])
    return out

_MON = {}
def K_inf_mod(mu, p, dmin=2, dmax=4):
    """number of multisets of monomials of degree dmin..dmax in len(mu) variables
    with exponent sum mu, mod p.  DP over the box of mu."""
    mu = tuple(int(x) for x in mu); r = len(mu)
    if any(x < 0 for x in mu): return 0
    key = (r, dmin, dmax)
    if key not in _MON: _MON[key] = monomials_deg(r, dmin, dmax)
    shape = tuple(m + 1 for m in mu)
    F = np.zeros(shape, dtype=np.uint64); F[(0,) * r] = 1
    pp = np.uint64(p)
    for al in _MON[key]:
        if any(al[i] > mu[i] for i in range(r)): continue
        src = tuple(slice(0, mu[i] + 1 - al[i]) for i in range(r))
        dst = tuple(slice(al[i], mu[i] + 1) for i in range(r))
        # unbounded: iterate along the first axis where al is nonzero so repeats accumulate
        ax = next(i for i in range(r) if al[i] > 0)
        for s in range(al[ax], mu[ax] + 1):
            si = list(src); di = list(dst)
            si[ax] = s - al[ax]; di[ax] = s
            blk = F[tuple(di)]; blk += F[tuple(si)]; blk %= pp
    return int(F[tuple(mu)])

def a_inf(tail, cache=None):
    tail = tuple(int(x) for x in tail)
    acc = [0, 0]; seen = {}
    for sgn, mu in weyl_terms(tail):
        key = sort_desc(mu)
        if key not in seen:
            if cache is not None and key in cache: seen[key] = cache[key]
            else:
                seen[key] = (K_inf_mod(key, P1), K_inf_mod(key, P2))
                if cache is not None: cache[key] = seen[key]
        v = seen[key]
        acc[0] = (acc[0] + sgn * v[0]) % P1; acc[1] = (acc[1] + sgn * v[1]) % P2
    v = crt2(acc[0], acc[1]); assert v >= 0
    return v

if __name__ == '__main__':
    args = sys.argv[1:]
    tails = []
    if '--tails' in args:
        tails = [tuple(int(x) for x in t.split(',')) for t in args[args.index('--tails') + 1].split(';')]
    if '--record' in args:
        rec = negative_record()
        tails += sorted({tail_of(lam) for (lam, d) in rec if len(lam) == 6})
    if '--region-l6' in args:
        for p in glob.glob(os.path.join(CELLS, 'bank_d*_l6.jsonl')):
            for ln in open(p):
                r = json.loads(ln)
                if r['a'] >= 1: tails.append(tuple(r['tail']))
        tails = sorted(set(tails))
    out_path = os.path.join(CELLS, 'stable_a.jsonl')
    done = {}
    if os.path.exists(out_path):
        for ln in open(out_path):
            r = json.loads(ln); done[tuple(r['tail'])] = r['a_inf']
    fh = open(out_path, 'a'); cache = {}
    t0 = time.time()
    for i, t in enumerate(tails):
        if t in done: continue
        t1 = time.time(); v = a_inf(t, cache)
        fh.write(json.dumps(dict(tail=list(t), size=sum(t), ell=len(t) + 1, a_inf=v, threshold=sum(t), secs=round(time.time() - t1, 2))) + "\n"); fh.flush()
        done[t] = v
        if (i + 1) % 50 == 0: log(f"{i+1}/{len(tails)} tails [{time.time()-t0:.0f}s]")
    fh.close()
    for t in tails: print(t, "a_inf =", done[t], "threshold delta >=", sum(t))
