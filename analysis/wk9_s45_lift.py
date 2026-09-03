#!/usr/bin/env python3
"""
Session 45 -- exact certificates for a measured nullity, on the lean build.

A mod-p nullity of [E; ev] only gives  mult >= a - k  (proved).  To promote
"mult = a - k" from measured to proved one exhibits k independent RATIONAL
highest-weight vectors annihilated by every evaluation:  kernel vectors at
several primes, canonical RREF (so the basis is intrinsic to the subspace),
pivot columns asserted equal across primes, CRT, rational reconstruction, and
then the exact integer verification E v = 0 (python ints, no modular
arithmetic) plus, where relevant, Theorem (★).

Same route as analysis/wk9_s42_lift.py, re-expressed on the array build of
wk9_s45_build (no `vecs` list) so it runs at the sizes this session reaches.

usage: python3 wk9_s45_lift.py delta lam1 lam2 ... [--side det|pad]
"""
import sys, os, time, json
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied45')
os.environ.setdefault('WIED_WORK', '/home/claude/s45/work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk8_s30_core import exps
from wk9_s45_build import build_cell, ev_rows_arr, log
from wk9_s45_cell import nullity_stacked, LEVELS, FORMS, SEEDS
from wk9_s36_stabred import P1, P2
from wk8_s30_pleth import a_of

EXTRA_PRIMES = [2147483587, 2147483579, 2147483563, 2147483549, 2147483543, 2147483497]

def rref_rows(vectors, n, p):
    M = nmod_mat(len(vectors), n, [int(v) % p for vec in vectors for v in vec], p)
    R, rk = M.rref()
    rows = [[int(R[i, j]) for j in range(n)] for i in range(rk)]
    piv = tuple(next(j for j, v in enumerate(row) if v) for row in rows)
    return piv, rows

def _ratrec(a, m):
    """rational reconstruction of a mod m: n/d with |n|,|d| <= sqrt(m/2)."""
    bound = int((m // 2) ** 0.5)
    r0, r1 = m, a % m; s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound: return None
    from math import gcd
    if gcd(abs(r1), abs(s1)) != 1: return None
    return Fraction(r1 if s1 > 0 else -r1, abs(s1))

def crt_rows(rows_by_prime, primes):
    """CRT + rational reconstruction of matching RREF bases."""
    Mprod = 1
    for p in primes: Mprod *= p
    k = len(rows_by_prime[primes[0]]); n = len(rows_by_prime[primes[0]][0])
    out = []
    for i in range(k):
        vec = []
        for j in range(n):
            x = 0; mm = 1
            for p in primes:
                r = rows_by_prime[p][i][j]
                # CRT step
                d = (r - x) % p
                x += mm * (d * pow(mm % p, p - 2, p) % p)
                mm *= p
            f = _ratrec(x % mm, mm)
            if f is None: return None
            vec.append(f)
        out.append(vec)
    return out

def clear_denoms(vec):
    from math import lcm, gcd
    L = 1
    for f in vec: L = lcm(L, f.denominator)
    ints = [int(f * L) for f in vec]
    g = 0
    for v in ints: g = gcd(g, abs(v))
    if g > 1: ints = [v // g for v in ints]
    return ints

def verify_exact(E, v):
    """E v = 0 over Z, python integers, no modular arithmetic."""
    E = sparse.csr_matrix(E)
    nz = [j for j, x in enumerate(v) if x]
    nzs = set(nz)
    for i in range(E.shape[0]):
        a, b = E.indptr[i], E.indptr[i + 1]
        s = 0
        for c, val in zip(E.indices[a:b], E.data[a:b]):
            c = int(c)
            if c in nzs: s += int(val) * v[c]
        if s != 0: return False, i
    return True, None

def star_flags(lam, delta, arr, n=4):
    """(★) per chi-column: for every constrained index i (lam_i >= delta) some
    factor of the monomial has alpha_i = 0.  Orbit-homogeneous (asserted)."""
    r = len(lam)
    A = np.array(exps(n, r), dtype=np.int32)
    cons = [i for i in range(r) if lam[i] >= delta]
    M = arr['M']; col_of = arr['col_of']; n_chi = arr['n_chi']
    st = np.ones(M.shape[0], dtype=bool)
    for i in cons:
        st &= (A[M, i] == 0).any(axis=1)
    kept = col_of >= 0
    tot = np.bincount(col_of[kept], minlength=n_chi)
    hit = np.bincount(col_of[kept], weights=st[kept].astype(np.float64), minlength=n_chi)
    assert np.all((hit == 0) | (hit == tot)), ("orbit not homogeneous for (★)", lam)
    return hit > 0, cons

def certify(lam, delta, side='det', primes=(P1, P2), extra=3, levels=LEVELS['cheap'],
            verbose=True, n=4):
    """measure the cell, and if the nullity is positive, lift the kernel to Q."""
    lam = tuple(lam); r = len(lam)
    B = build_cell(lam, delta, verbose=verbose)
    a = a_of(lam, delta, n, r); K = a + 8
    arr = B['arr']; E = B['E']; nc = B['n_chi']
    f, N = FORMS[side]
    allp = list(primes) + EXTRA_PRIMES[:extra]
    res = dict(lam=list(lam), delta=delta, a=a, side=side, n_chi=nc, nnz=int(E.nnz),
               nrows=int(E.shape[0]), K=K, primes={})
    rows_by_prime = {}; nuls = {}
    for p in allp:
        EV = ev_rows_arr(f, N, n, r, arr, K, SEEDS[side], 40, p)
        k, kern, lvl, _ = nullity_stacked(E, sparse.csr_matrix(EV), nc, p, want_kern=True,
                                          tag=f"lift_{'_'.join(map(str,lam))}d{delta}{side}",
                                          levels=levels, verbose=False)
        nuls[p] = k
        res['primes'][str(p)] = dict(nullity=k, level=lvl)
        if verbose: log(f"  p={p}: nullity_p([E; ev_{side}]) = {k} -> mult_{side} >= {a-k} (level {lvl})")
        if k: rows_by_prime[p] = rref_rows(kern, nc, p)
    assert len(set(nuls[p] for p in primes)) == 1, ("house primes disagree", lam, delta, nuls)
    k = nuls[primes[0]]
    res['nullity'] = k; res['mult'] = a - k
    if k == 0:
        res['status'] = 'proved (nullity 0): mult_%s = a = %d' % (side, a)
        return res, None
    good = [p for p in allp if nuls[p] == k]
    piv = {p: rows_by_prime[p][0] for p in good}
    assert len(set(piv.values())) == 1, ("pivot columns disagree across primes", lam, delta, piv)
    res['pivots'] = list(piv[good[0]])
    rec = crt_rows({p: rows_by_prime[p][1] for p in good}, good)
    assert rec is not None, ("rational reconstruction failed", lam, delta)
    vecs = [clear_denoms(v) for v in rec]
    for v in vecs:
        ok, bad = verify_exact(E, v)
        assert ok, ("exact verification E v = 0 failed", lam, delta, bad)
    rk = nmod_mat(len(vecs), nc, [x % P1 for v in vecs for x in v], P1).rank()
    assert rk == k, ("exhibited vectors dependent", lam, delta, rk, k)
    stars, cons = star_flags(lam, delta, arr)
    star_ok = all(all(stars[j] for j, x in enumerate(v) if x) for v in vecs)
    res.update(status='proved both ways: mult_%s = a - %d = %d' % (side, k, a - k),
               exact_vectors=k, max_abs=max(max(abs(x) for x in v) for v in vecs),
               support=[sum(1 for x in v if x) for v in vecs],
               star=bool(star_ok), constrained=cons, primes_used=good)
    if verbose:
        log(f"  {lam} d{delta} [{side}]: {k} exact rational vectors, E v = 0 over Z, "
            f"max |coeff| {res['max_abs']}, (★) {'holds' if star_ok else 'FAILS'} on every support monomial")
    return res, vecs

if __name__ == '__main__':
    args = sys.argv[1:]; side = 'det'; pos = []
    i = 0
    while i < len(args):
        if args[i] == '--side': side = args[i + 1]; i += 2
        else: pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res, vecs = certify(lam, delta, side=side)
    print(json.dumps(res))
