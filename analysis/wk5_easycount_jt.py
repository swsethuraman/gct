#!/usr/bin/env python3
"""
Growth of the two Peter-Weyl ("easy") counts with n.

  m_det_n(lam)  = dim (S_lam^*)^{Stab(det_n)}   -- sparse rectangular Kroneckers
  m_per_n(lam)  = dim (S_lam^*)^{Stab(per_n)}   -- monomial stabiliser

Reuses session 24b's exact core (wk5_s24b_sf.py) for m_det and for the
Murnaghan-Nakayama machinery.  The permanent side is rewritten for general n
with two changes that make n = 4, 5 feasible:

  (1) MARGIN PRUNING.  Only exponent vectors whose n x n exponent matrix has
      every row and column sum <= delta can survive to the torus-invariant
      part, so prune every intermediate polynomial to that cone.  Without this
      the Jacobi-Trudi h-series at n = 4 carries C(31,15) ~ 3e8 monomials.
  (2) CONJUGACY REDUCTION.  m_monomial averages chi over all 2(n!)^2 monomial
      permutations; conjugate ones contribute equally, so average over class
      representatives with multiplicities instead.
"""
import sys, itertools, time
sys.path.insert(0, '/root/gctrepo/analysis')
from wk5_s24b_sf import partitions, m_det

# ------------------------------------------------------------------ pruning
def make_ok(n, delta):
    """exact torus-invariance: every row sum and column sum equals delta."""
    def ok(e):
        for i in range(n):
            if sum(e[n*i+j] for j in range(n)) != delta: return False
        for j in range(n):
            if sum(e[n*i+j] for i in range(n)) != delta: return False
        return True
    return ok

def make_feasible(n, delta):
    """necessary condition for a monomial to be extendable: all margins <= delta."""
    def feas(e):
        for i in range(n):
            if sum(e[n*i+j] for j in range(n)) > delta: return False
        for j in range(n):
            if sum(e[n*i+j] for i in range(n)) > delta: return False
        return True
    return feas

# ------------------------------------------- pruned polynomial arithmetic
def pmul(p, q, nv, feas):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(e1[i] + e2[i] for i in range(nv))
            if not feas(e): continue
            r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}

def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c}

def pscal(p, s):
    return {e: c * s for e, c in p.items()} if s else {}

def h_series(perm, nv, kmax, feas):
    seen, cycles = [False]*nv, []
    for i in range(nv):
        if seen[i]: continue
        c, j = [], i
        while not seen[j]:
            seen[j] = True; c.append(j); j = perm[j]
        cycles.append(c)
    h = [dict() for _ in range(kmax+1)]
    h[0] = {tuple([0]*nv): 1}
    for c in cycles:
        L = len(c)
        Xc = [0]*nv
        for i in c: Xc[i] += 1
        Xc = tuple(Xc)
        if not feas(Xc):        # a whole cycle already breaks a margin
            nh = [dict() for _ in range(kmax+1)]
            for k in range(kmax+1): nh[k] = dict(h[k])
            h = nh; continue
        nh = [dict() for _ in range(kmax+1)]
        for k in range(kmax+1):
            if not h[k]: continue
            kk = k
            cur = {tuple([0]*nv): 1}
            while kk <= kmax:
                if cur:
                    nh[kk] = padd(nh[kk], pmul(h[k], cur, nv, feas))
                kk += L
                cur = pmul(cur, {Xc: 1}, nv, feas)
                if not cur: break
        h = nh
    return h

def chi_monomial(lam, perm, nv, feas, kmax):
    lam = tuple(x for x in lam if x)
    L = len(lam); N = sum(lam)
    H = h_series(perm, nv, kmax, feas)
    M = [[H[lam[i]-i+j] if 0 <= lam[i]-i+j <= kmax else dict()
          for j in range(L)] for i in range(L)]
    memo = {}
    def det(rows, cols):
        if not rows: return {tuple([0]*nv): 1}
        key = (rows, cols)
        if key in memo: return memo[key]
        i = rows[0]; acc = {}
        for idx, j in enumerate(cols):
            if not M[i][j]: continue
            sub = det(rows[1:], cols[:idx]+cols[idx+1:])
            if not sub: continue
            acc = padd(acc, pscal(pmul(M[i][j], sub, nv, feas), (-1)**idx))
        memo[key] = acc
        return acc
    return det(tuple(range(L)), tuple(range(L)))

# ------------------------------------------- the permanent's stabiliser
def perms_per(n):
    """the 2 (n!)^2 coordinate permutations of {(i,j)}: (P,Q) and (P,Q).T"""
    Sn = list(itertools.permutations(range(n)))
    out = set()
    for P in Sn:
        for Q in Sn:
            for t in (0, 1):
                pm = [0]*(n*n)
                for i in range(n):
                    for j in range(n):
                        ii, jj = (i, j) if t == 0 else (j, i)
                        pm[n*i+j] = n*P[ii] + Q[jj]
                out.add(tuple(pm))
    return sorted(out)

def classes(perms):
    """group perms into conjugacy classes under the group they generate."""
    S = set(perms); nv = len(perms[0])
    def conj(g, h):  # g h g^{-1}
        gi = [0]*nv
        for i, v in enumerate(g): gi[v] = i
        return tuple(g[h[gi[i]]] for i in range(nv))
    seen, reps = set(), []
    for p in perms:
        if p in seen: continue
        orb = set()
        stack = [p]
        while stack:
            x = stack.pop()
            if x in orb: continue
            orb.add(x)
            for g in perms:
                y = conj(g, x)
                if y not in orb: stack.append(y)
        seen |= orb
        reps.append((p, len(orb)))
    assert sum(c for _, c in reps) == len(perms)
    return reps

_CACHE = {}
def per_reps(n):
    if n not in _CACHE:
        _CACHE[n] = classes(perms_per(n))
    return _CACHE[n]

def m_per(lam, n, delta):
    nv = n*n
    ok, feas = make_ok(n, delta), make_feasible(n, delta)
    L = len([x for x in lam if x])
    kmax = sum(lam) + L
    tot = 0; tally = 0
    for rep, size in per_reps(n):
        chi = chi_monomial(lam, rep, nv, feas, kmax)
        tot += size * sum(c for e, c in chi.items() if ok(e))
        tally += size
    assert tot % tally == 0, (lam, n, delta, tot, tally)
    return tot // tally
