#!/usr/bin/env python3
"""
Session 42 -- exact certificates at bite cells (nullity_p(E_red) = k > 0).

A mod-p nullity only gives mult_red >= a - k.  To PROVE mult_red <= a - k one
exhibits k independent RATIONAL highest-weight vectors supported on M_★
(then they lie in I(R_r) by Theorem (★), so dim(HWV_Q ∩ span M_★) >= k).

Route: at each of several primes, kernel vectors of E_red from the sparse
route (wk9_s42_sparse), put into reduced row echelon form (canonical for the
subspace ker_p(E_red)); pivot columns must agree across primes; CRT the
entries, rational reconstruction; the k reconstructed vectors are verified
over Z (python ints, no modular arithmetic) against every reduced raising-
operator row (E_red v = 0), and their independence is a flint rank.  Output:
results/s42_certs/<cell>.txt (the vectors in chi-coordinates of red orbits,
numerators/denominators), and the verdict line in the cell's JSON.

usage: python3 wk9_s42_lift.py delta lam1 lam2 ...
"""
import sys, os, time, json
from fractions import Fraction
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s42_redengine import build, csr_to_rows
from wk9_s42_sparse import nullity_sparse, log
from wk8_s30_pleth import a_of
from wk9_s36_stabred import P1, P2
from flint import nmod_mat

EXTRA_PRIMES = [2147483587, 2147483579, 2147483563, 2147483549, 2147483543, 2147483497]   # further primes in (2^30, 2^31)

def rref_mod(vectors, n, p):
    """canonical RREF basis of the span of `vectors` mod p; returns (pivots, rows)."""
    M = nmod_mat(len(vectors), n, [v for vec in vectors for v in vec], p)
    R, rk = M.rref()
    rows = [[int(R[i, j]) for j in range(n)] for i in range(rk)]
    piv = []
    for row in rows:
        piv.append(next(j for j, v in enumerate(row) if v))
    return tuple(piv), rows

def crt(residues, primes):
    x, m = 0, 1
    for r, p in zip(residues, primes):
        # solve x' = x mod m, x' = r mod p
        t = ((r - x) * pow(m, -1, p)) % p
        x = x + m * t; m *= p
    return x % m, m

def ratrec(x, m):
    """rational reconstruction: a/b with |a|, b <= sqrt(m/2); None if impossible."""
    import math
    bound = math.isqrt(m // 2)
    r0, r1 = m, x % m
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound: return None
    if s1 < 0: r1, s1 = -r1, -s1
    if gcd(r1, s1) != 1: return None
    return Fraction(r1, s1)

def lift(lam, delta, verbose=True):
    t0 = time.time()
    B = build(lam, delta, verbose=False)
    a = a_of(lam, delta, 4, len(lam))
    n = B['n_red']; rows = csr_to_rows(B['E_red'])
    primes = [P1, P2]
    per = {}
    for p in primes:
        k, kern = nullity_sparse(B['E_red'], n, p, want_kern=True, tag=f"lift{'_'.join(map(str, lam))}d{delta}", verbose=False)
        per[p] = rref_mod(kern, n, p) if k else ((), [])
        log(f"  p={p}: nullity {k}, pivots {per[p][0]}")
    k = len(per[P1][1])
    assert all(len(per[p][1]) == k for p in primes), "primes disagree on nullity"
    assert all(per[p][0] == per[P1][0] for p in primes), "pivot columns differ across primes"
    if k == 0:
        return dict(lam=list(lam), delta=delta, a=a, nullity=0, verdict='mult_red = a proved (nullity 0)')
    # rational reconstruction, adding primes until it succeeds (or the list is exhausted)
    extra = list(EXTRA_PRIMES)
    while True:
        m = 1
        for p in primes: m *= p
        vecs = []
        ok = True
        for i in range(k):
            vec = []
            for j in range(n):
                x, _ = crt([per[p][1][i][j] for p in primes], primes)
                q = ratrec(x, m)
                if q is None: ok = False; break
                vec.append(q)
            if not ok: break
            vecs.append(vec)
        if ok: break
        if not extra:
            return dict(lam=list(lam), delta=delta, a=a, nullity=k, verdict=f'mult_red >= {a-k} proved; = {a-k} measured (rational reconstruction failed with {len(primes)} primes)')
        p = extra.pop(0)
        kk, kern = nullity_sparse(B['E_red'], n, p, want_kern=True, tag=f"lift{'_'.join(map(str, lam))}d{delta}", verbose=False)
        assert kk == k, ("extra prime disagrees on nullity", p, kk, k)
        per[p] = rref_mod(kern, n, p)
        assert per[p][0] == per[P1][0]
        primes.append(p)
        log(f"  added prime {p}: nullity {kk}")
    # clear denominators, verify over Z against the reduced rows
    certs = []
    for vec in vecs:
        den = 1
        for q in vec: den = den * q.denominator // gcd(den, q.denominator)
        iv = [int(q * den) for q in vec]
        g = 0
        for v in iv: g = gcd(g, v)
        iv = [v // g for v in iv] if g else iv
        for d in rows:
            s = sum(v * iv[c] for c, v in d.items())
            assert s == 0, "exact verification E_red v = 0 FAILED"
        certs.append(iv)
    # independence over Q: rank mod P1 of the integer matrix
    rk = nmod_mat(k, n, [v % P1 for iv in certs for v in iv], P1).rank()
    assert rk == k
    os.makedirs(os.path.join(HERE, '..', 'results', 's42_certs'), exist_ok=True)
    fn = os.path.join(HERE, '..', 'results', 's42_certs', f"{'_'.join(map(str, lam))}_d{delta}.txt")
    with open(fn, 'w') as f:
        f.write(f"# lam={lam} delta={delta} a={a} nullity={k}: {k} integer highest-weight vectors in chi-coordinates of the red orbits\n")
        f.write(f"# red orbit index -> representative monomial (indices into exps(4,{len(lam)})): see build(); columns listed as red[j]\n")
        f.write(f"# red = {B['red']}\n")
        for iv in certs:
            f.write(' '.join(str(v) for v in iv) + "\n")
    maxc = max(abs(v) for iv in certs for v in iv)
    res = dict(lam=list(lam), delta=delta, a=a, nullity=k, primes=primes, max_coeff=maxc, file=os.path.relpath(fn, os.path.join(HERE, '..')),
               verdict=f'mult_red = {a-k} PROVED: {k} independent integer HWVs in I(R_r) exhibited (E v = 0 over Z, support in M_star), max |coeff| {maxc}; secs {time.time()-t0:.0f}')
    log(res['verdict'])
    return res

if __name__ == '__main__':
    delta = int(sys.argv[1]); lam = tuple(int(x) for x in sys.argv[2:])
    res = lift(lam, delta)
    print(json.dumps(res))
    with open(os.path.join(HERE, '..', 'results', 's42_lifts.jsonl'), 'a') as f: f.write(json.dumps(res) + "\n")
