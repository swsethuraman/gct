#!/usr/bin/env python3
"""
Fast route to m_per_n(lam), via power sums instead of Jacobi-Trudi.

    dim (S_lam)^H = sum_rho (|C_rho|/N!) chi^lam(rho) E(rho),
    E(rho)        = <prod_i tr(h^{rho_i})>_H .

E(rho) does not depend on lam, so the expensive part is paid once per (n,delta)
rather than once per weight.  Each E(rho) is a DP over exponent matrices pruned
to margins <= delta.
"""
import sys, itertools
from fractions import Fraction
sys.path.insert(0, '/root/gctrepo/analysis')
from wk5_s24b_sf import partitions, classsize, mn

def coord_perm(n, P, Q, t):
    pm = [0]*(n*n)
    for i in range(n):
        for j in range(n):
            ii, jj = (i, j) if t == 0 else (j, i)
            pm[n*i+j] = n*P[ii] + Q[jj]
    return tuple(pm)

def cycle_type(p):
    n = len(p); seen = [False]*n; ct = []
    for i in range(n):
        if seen[i]: continue
        L, j = 0, i
        while not seen[j]:
            seen[j] = True; L += 1; j = p[j]
        ct.append(L)
    return tuple(sorted(ct, reverse=True))

def compose(a, b):          # (a o b)(i) = a[b[i]]
    return tuple(a[b[i]] for i in range(len(a)))

def per_classes(n):
    """conjugacy classes of the permanent's finite stabiliser, by structure:
       t=0 -> unordered pair of cycle types; t=1 -> cycle type of P o Q."""
    Sn = list(itertools.permutations(range(n)))
    lab = {}
    for P in Sn:
        for Q in Sn:
            for t in (0, 1):
                key = (('t0', tuple(sorted([cycle_type(P), cycle_type(Q)])))
                       if t == 0 else ('t1', cycle_type(compose(P, Q))))
                lab.setdefault(key, []).append(coord_perm(n, P, Q, t))
    return [(v[0], len(v)) for v in lab.values()], sum(len(v) for v in lab.values())

def cycles_of(p):
    n = len(p); seen = [False]*n; out = []
    for i in range(n):
        if seen[i]: continue
        c, j = [], i
        while not seen[j]:
            seen[j] = True; c.append(j); j = p[j]
        out.append(c)
    return out

def E_table(n, delta):
    """E(rho) for every rho |- n*delta, exact Fractions."""
    N = n*delta; nv = n*n
    reps, total = per_classes(n)
    def margins_ok(e, strict):
        for i in range(n):
            s = sum(e[n*i+j] for j in range(n))
            if (s != delta) if strict else (s > delta): return False
        for j in range(n):
            s = sum(e[n*i+j] for i in range(n))
            if (s != delta) if strict else (s > delta): return False
        return True
    # per-class cycle data
    cyc = []
    for rep, size in reps:
        cs = []
        for c in cycles_of(rep):
            X = [0]*nv
            for i in c: X[i] += 1
            cs.append((len(c), tuple(X)))
        cyc.append((cs, size))
    out = {}
    for rho in partitions(N):
        acc = 0
        for cs, size in cyc:
            state = {tuple([0]*nv): 1}
            for r in rho:
                terms = [(L, tuple(x*(r//L) for x in X)) for L, X in cs if r % L == 0]
                nxt = {}
                for e, c0 in state.items():
                    for L, dX in terms:
                        e2 = tuple(e[k]+dX[k] for k in range(nv))
                        if not margins_ok(e2, False): continue
                        nxt[e2] = nxt.get(e2, 0) + c0*L
                state = nxt
                if not state: break
            acc += size * sum(c for e, c in state.items() if margins_ok(e, True))
        assert acc % total == 0, (rho, acc, total)
        out[rho] = acc // total
    return out

def m_per_fast(lam, n, delta, Etab):
    from math import factorial
    N = n*delta
    s = 0
    for rho, E in Etab.items():
        if E: s += classsize(rho) * mn(lam, rho) * E
    assert s % factorial(N) == 0, (lam, s)
    return s // factorial(N)
