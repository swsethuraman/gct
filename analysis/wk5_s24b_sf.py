#!/usr/bin/env python3
"""
Session 24b -- exact symmetric-function / character core.

  partitions, S_N character table by Murnaghan-Nakayama (exact integers),
  Kronecker coefficients, plethysm s_delta[s_n] in the Schur basis,
  and the two Peter-Weyl counts

     m_det_n(lam)       determinant stabiliser {AXB : detA detB = 1} |x <transpose>
     m_mon(lam, group)  any MONOMIAL stabiliser (permanent, padded permanent)

Everything is exact: Python ints and Fraction.
"""
from functools import lru_cache
from fractions import Fraction
import itertools

# ---------------------------------------------------------------- partitions
@lru_cache(maxsize=None)
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: return ((),)
    out = []
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            out.append((k,) + rest)
    return tuple(out)

@lru_cache(maxsize=None)
def zee(rho):
    from math import factorial
    z, cnt = 1, {}
    for p in rho:
        cnt[p] = cnt.get(p, 0) + 1
    for p, c in cnt.items():
        z *= (p ** c) * factorial(c)
    return z

@lru_cache(maxsize=None)
def classsize(rho):
    from math import factorial
    return factorial(sum(rho)) // zee(rho)

# ------------------------------------------- Murnaghan-Nakayama: chi^lam(rho)
@lru_cache(maxsize=None)
def mn(lam, rho):
    """character of S_n irreducible lam at cycle type rho (both tuples)."""
    lam = tuple(x for x in lam if x)
    if not rho:
        return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    total = 0
    # remove every border strip of size r from lam
    for (newlam, ht) in border_strips(lam, r):
        total += (-1) ** ht * mn(newlam, rest)
    return total

@lru_cache(maxsize=None)
def border_strips(lam, r):
    """all (lam minus a border strip of size r, height) pairs."""
    res = []
    k = len(lam)
    beta = [lam[i] + (k - 1 - i) for i in range(k)]        # distinct betas
    bset = set(beta)
    for b in beta:
        nb = b - r
        if nb < 0 or nb in bset:
            continue
        nbeta = sorted([x for x in beta if x != b] + [nb], reverse=True)
        # height = number of rows the strip spans - 1 = number of betas jumped
        ht = sum(1 for x in beta if nb < x < b)
        newlam = tuple(nbeta[i] - (k - 1 - i) for i in range(k))
        newlam = tuple(x for x in newlam if x)
        if any(newlam[i] < newlam[i+1] for i in range(len(newlam)-1)):
            continue
        res.append((newlam, ht))
    return tuple(res)

def kronecker(lam, mu, nu):
    n = sum(lam)
    assert sum(mu) == n and sum(nu) == n
    tot = 0
    for rho in partitions(n):
        tot += classsize(rho) * mn(lam, rho) * mn(mu, rho) * mn(nu, rho)
    from math import factorial
    assert tot % factorial(n) == 0
    return tot // factorial(n)

# -------------------------------------------------- m for the determinant
def rho_tilde(rho):
    """odd parts kept; each even part r replaced by two parts r/2."""
    out = []
    for r in rho:
        if r % 2: out.append(r)
        else: out.extend([r // 2, r // 2])
    return tuple(sorted(out, reverse=True))

@lru_cache(maxsize=None)
def m_det(lam, n, delta):
    """dim (S_lam^*)^{Stab(det_n)},  |lam| = n*delta, at most n^2 rows."""
    from math import factorial
    N = n * delta
    assert sum(lam) == N
    rect = tuple([delta] * n)
    g = kronecker(lam, rect, rect)
    tw = 0
    for rho in partitions(N):
        tw += classsize(rho) * mn(lam, rho) * mn(rect, rho_tilde(rho))
    assert tw % factorial(N) == 0
    tw //= factorial(N)
    assert (g + tw) % 2 == 0, (lam, n, delta, g, tw)
    return (g + tw) // 2

# --------------------------------- m for a MONOMIAL stabiliser (route 1)
# polynomials as dict: exponent tuple -> int
def pmul(p, q, nv):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(e1[i] + e2[i] for i in range(nv))
            r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}

def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c}

def pscal(p, s):
    return {e: c * s for e, c in p.items()} if s else {}

def h_series(perm, nv, kmax):
    """h_0..h_kmax of the monomial matrix diag(x) * perm, as polynomials."""
    # cycles of perm (a tuple: perm[i] = image of i)
    seen, cycles = [False] * nv, []
    for i in range(nv):
        if seen[i]: continue
        c, j = [], i
        while not seen[j]:
            seen[j] = True; c.append(j); j = perm[j]
        cycles.append(c)
    h = [dict() for _ in range(kmax + 1)]
    h[0] = {tuple([0] * nv): 1}
    for c in cycles:
        L = len(c)
        Xc = [0] * nv
        for i in c: Xc[i] += 1
        Xc = tuple(Xc)
        # multiply by 1/(1 - z^L X_c) = sum_e z^{L e} X_c^e
        nh = [dict() for _ in range(kmax + 1)]
        for k in range(kmax + 1):
            if not h[k]: continue
            e, kk = 0, k
            cur = {tuple([0] * nv): 1}
            while kk <= kmax:
                nh[kk] = padd(nh[kk], pmul(h[k], cur, nv))
                e += 1; kk += L
                cur = pmul(cur, {Xc: 1}, nv)
        h = nh
    return h

def chi_monomial(lam, perm, nv):
    """chi_{S_lam}(diag(x) . perm) as a polynomial in nv variables (Jacobi-Trudi)."""
    lam = tuple(x for x in lam if x)
    L = len(lam)
    N = sum(lam)
    H = h_series(perm, nv, N + L)
    M = [[H[lam[i] - i + j] if 0 <= lam[i] - i + j <= N + L else dict()
          for j in range(L)] for i in range(L)]
    # exact determinant by cofactor expansion with memo on column subsets
    from functools import lru_cache as _lc
    def det(rows, cols):
        if not rows: return {tuple([0] * nv): 1}
        i = rows[0]
        acc = {}
        for idx, j in enumerate(cols):
            if not M[i][j]: continue
            sub = det(rows[1:], cols[:idx] + cols[idx+1:])
            if not sub: continue
            term = pmul(M[i][j], sub, nv)
            acc = padd(acc, pscal(term, (-1) ** idx))
        return acc
    return det(tuple(range(L)), tuple(range(L)))

def m_monomial(lam, perms, nv, weight_ok):
    """dim (S_lam^*)^H for H = (torus) |x (perms), torus-invariance encoded by
    weight_ok(mu) on exponent tuples."""
    tot = 0
    for perm in perms:
        chi = chi_monomial(lam, perm, nv)
        tot += sum(c for e, c in chi.items() if weight_ok(e))
    assert tot % len(perms) == 0, (lam, tot, len(perms))
    return tot // len(perms)

# ------------------------------------------------ plethysm s_delta[s_n]
@lru_cache(maxsize=None)
def schur_in_p(n):
    """s_n = sum_rho p_rho / z_rho  ->  dict rho -> Fraction."""
    return {rho: Fraction(1, zee(rho)) for rho in partitions(n)}

@lru_cache(maxsize=None)
def plethysm_p(delta, n):
    """s_delta[s_n] in the power-sum basis: dict rho -> Fraction."""
    base = schur_in_p(n)
    acc = {(): Fraction(1)}
    out = {}
    for rho in partitions(delta):
        term = {(): Fraction(1)}
        for r in rho:
            # p_r[s_n] = sum_sigma p_{r*sigma} / z_sigma
            pr = {}
            for sigma, c in base.items():
                key = tuple(sorted([r * s for s in sigma], reverse=True))
                pr[key] = pr.get(key, Fraction(0)) + c
            new = {}
            for a, ca in term.items():
                for b, cb in pr.items():
                    key = tuple(sorted(a + b, reverse=True))
                    new[key] = new.get(key, Fraction(0)) + ca * cb
            term = new
        for k, v in term.items():
            out[k] = out.get(k, Fraction(0)) + v / zee(rho)
    return out

@lru_cache(maxsize=None)
def plethysm_schur(delta, n, maxrows):
    """mult of S_lam in Sym^delta(Sym^n C^maxrows): dict lam -> int."""
    P = plethysm_p(delta, n)
    res = {}
    for lam in partitions(n * delta):
        if len(lam) > maxrows: continue
        v = sum(c * mn(lam, rho) for rho, c in P.items())
        assert v.denominator == 1, (lam, v)
        if v: res[lam] = int(v)
    return res
