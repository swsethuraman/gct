#!/usr/bin/env python3
"""
Session 25 -- core symmetric-function routines, written independently of
scripts/ambient_screen.py and of analysis/wk5_s24b_sf.py.

Provides:  partitions, z_rho, chi^lam(rho) (Murnaghan-Nakayama),
           column orthogonality self-check,
           Kronecker g(lam,mu,nu),
           m_det(lam,n,delta)     symmetric rectangular Kronecker,
           a(lam,delta,d,N)       ambient plethysm  Sym^delta(Sym^d C^N),
           dim S_lam(C^N)         Weyl dimension.
Exact integers / Fraction throughout.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

# ------------------------------------------------------------------ partitions
@lru_cache(maxsize=None)
def parts(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: return ((),)
    out = []
    for k in range(min(n, maxp), 0, -1):
        for r in parts(n - k, k):
            out.append((k,) + r)
    return tuple(out)

@lru_cache(maxsize=None)
def zrho(rho):
    z, c = 1, {}
    for p in rho: c[p] = c.get(p, 0) + 1
    for p, m in c.items(): z *= (p ** m) * factorial(m)
    return z

# ------------------------------- Murnaghan-Nakayama by RIM-HOOK REMOVAL on the
# diagram (hook lengths), deliberately NOT the beta-number formulation used by
# scripts/ambient_screen.py, so the two are independent code paths.
@lru_cache(maxsize=None)
def _hooks(lam):
    """hook length of every cell, as a dict (i,j) -> h."""
    L = len(lam)
    conj = [sum(1 for i in range(L) if lam[i] > j) for j in range(lam[0] if L else 0)]
    return {(i, j): (lam[i] - j) + (conj[j] - i) - 1
            for i in range(L) for j in range(lam[i])}

@lru_cache(maxsize=None)
def _remove_rim(lam, i, j):
    """remove the rim hook whose head is the cell (i,j); return (mu, height)."""
    L = len(lam)
    conj = [sum(1 for r in range(L) if lam[r] > c) for c in range(lam[0])]
    last = conj[j] - 1                      # bottom row the rim hook reaches
    mu = list(lam)
    # the rim hook from (i,j) walks down-left along the rim to row `last`
    for r in range(i, last + 1):
        mu[r] = (lam[r + 1] - 1) if r + 1 < L else (j - 1 + 1 - 1)
    mu[last] = j                            # the head column becomes the new length
    for r in range(i, last):
        mu[r] = lam[r + 1] - 1
    mu = tuple(x for x in mu if x > 0)
    return mu, last - i

@lru_cache(maxsize=None)
def chi(lam, rho):
    lam = tuple(x for x in lam if x)
    if not rho: return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    H = _hooks(lam)
    tot = 0
    for (i, j), h in H.items():
        if h != r: continue
        mu, ht = _remove_rim(lam, i, j)
        if sum(mu) != sum(lam) - r: continue
        if any(mu[k] < mu[k + 1] for k in range(len(mu) - 1)): continue
        tot += (-1) ** ht * chi(mu, rest)
    return tot

def orthogonality_ok(N):
    """column orthogonality: sum_lam chi^lam(rho) chi^lam(sig) = z_rho [rho=sig]."""
    P = parts(N)
    for a in P:
        for b in P:
            s = sum(chi(l, a) * chi(l, b) for l in P)
            if s != (zrho(a) if a == b else 0): return False, (a, b, s)
    return True, None

# ----------------------------------------------------------------- Kronecker
def kron(lam, mu, nu):
    N = sum(lam)
    tot = Fraction(0)
    for rho in parts(N):
        tot += Fraction(chi(lam, rho) * chi(mu, rho) * chi(nu, rho), zrho(rho))
    assert tot.denominator == 1
    return int(tot)

# ------------------------------------------------------- m_det (symmetric Kron)
def tau_split(rho):
    out = []
    for r in rho:
        if r % 2: out.append(r)
        else: out += [r // 2, r // 2]
    return tuple(sorted(out, reverse=True))

@lru_cache(maxsize=None)
def m_det(lam, n, delta):
    """dim (S_lam^*)^{Stab(det_n)},  Stab = {AXB: detA detB=1} |x <transpose>."""
    N = n * delta
    assert sum(lam) == N and len(lam) <= n * n
    rect = tuple([delta] * n)
    tot = Fraction(0)
    for rho in parts(N):
        tot += Fraction(chi(lam, rho), zrho(rho)) * (
            chi(rect, rho) ** 2 + chi(rect, tau_split(rho)))
    tot /= 2
    assert tot.denominator == 1, (lam, n, delta, tot)
    return int(tot)

# ------------------------------------------------------------ ambient plethysm
@lru_cache(maxsize=None)
def _sd_in_p(d):
    """s_d = sum_rho p_rho / z_rho."""
    return {rho: Fraction(1, zrho(rho)) for rho in parts(d)}

@lru_cache(maxsize=None)
def _pleth_p(delta, d):
    """Sym^delta(Sym^d) in the power-sum basis."""
    base = _sd_in_p(d)
    out = {}
    for rho in parts(delta):
        term = {(): Fraction(1)}
        for r in rho:
            pr = {}
            for sig, c in base.items():
                k = tuple(sorted([r * s for s in sig], reverse=True))
                pr[k] = pr.get(k, Fraction(0)) + c
            new = {}
            for x, cx in term.items():
                for y, cy in pr.items():
                    k = tuple(sorted(x + y, reverse=True))
                    new[k] = new.get(k, Fraction(0)) + cx * cy
            term = new
        for k, v in term.items():
            out[k] = out.get(k, Fraction(0)) + v / zrho(rho)
    return out

@lru_cache(maxsize=None)
def amb_row(delta, d, N):
    """dict lam -> a(lam,delta) for Sym^delta(Sym^d C^N), lam with <= N rows."""
    P = _pleth_p(delta, d)
    res = {}
    for lam in parts(d * delta):
        if len(lam) > N: continue
        v = sum(c * chi(lam, rho) for rho, c in P.items())
        assert v.denominator == 1
        if v: res[lam] = int(v)
    return res

def a_of(lam, delta, d, N):
    # NB keys are partitions with trailing zeros stripped; strip before lookup.
    return amb_row(delta, d, N).get(tuple(x for x in lam if x), 0)

def aA(delta, b):
    """World A ambient: a((4delta-b, b), delta) in Sym^delta(Sym^4 C^2)."""
    return a_of((4 * delta - b, b), delta, 4, 2)

# ------------------------------------------------------------- Weyl dimension
def dimS(lam, N):
    lam = tuple(x for x in lam if x)
    if len(lam) > N: return 0
    l = list(lam) + [0] * (N - len(lam))
    num = den = 1
    for i in range(N):
        for j in range(i + 1, N):
            num *= (l[i] - l[j] + j - i)
            den *= (j - i)
    return num // den
