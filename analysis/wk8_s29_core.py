#!/usr/bin/env python3
"""
Session 29 -- the isotypic rank machinery, rebuilt (s27's branch has not landed).

For a form f of degree n on C^N and a weight lam of length r:
    mult_lam C[closure(GL_N . f)]_delta = mult of S_lam(C^r) in C[D_r^f]_delta,
    D_r^f = closure{ (s_1..s_r) |-> f(sum s_i A_i) } in Sym^n C^r.
Basis: degree-delta monomials in the coefficient functionals c_alpha of weight
lam.  R = simple raising operators (a = dim ker R).  E = evaluations.
mult = rank([R;E]) - rank(R).  Kernel bases are extracted for the subspace test.
"""
import itertools, random
from fractions import Fraction
from functools import lru_cache

PRIMES = (2147483647, 2147483629)

@lru_cache(maxsize=None)
def exps(n, r):
    out = []
    def rec(k, left, cur):
        if k == r - 1: out.append(tuple(cur + [left])); return
        for v in range(left + 1): rec(k + 1, left - v, cur + [v])
    rec(0, n, [])
    return tuple(out)

@lru_cache(maxsize=None)
def monomials(n, r, delta, lam):
    A, L = exps(n, r), len(exps(n, r))
    lam = tuple(lam) + (0,) * (r - len(lam))
    if sum(lam) != delta * n: return ()
    out = []
    def rec(start, left, rem, cur):
        if left == 0:
            if not any(rem): out.append(tuple(cur))
            return
        if sum(rem) != left * n: return
        for i in range(start, L):
            al = A[i]
            if any(al[j] > rem[j] for j in range(r)): continue
            rec(i, left - 1, tuple(rem[j] - al[j] for j in range(r)), cur + [i])
    rec(0, delta, lam, [])
    return tuple(out)

def build_R(n, r, delta, lam):
    lam = tuple(lam) + (0,) * (r - len(lam))
    A = exps(n, r); idx = {a: k for k, a in enumerate(A)}
    basis = monomials(n, r, delta, lam); pos = {m: c for c, m in enumerate(basis)}
    rows = []
    for i in range(r - 1):
        j = i + 1
        tgt = tuple(lam[k] + (1 if k == i else (-1 if k == j else 0)) for k in range(r))
        if tgt[j] < 0: continue
        tb = monomials(n, r, delta, tgt); tp = {m: c for c, m in enumerate(tb)}
        acc = {}
        for m in basis:
            for p in range(len(m)):
                al = A[m[p]]
                if al[j] == 0: continue
                nb = list(al); nb[j] -= 1; nb[i] += 1
                nm = tuple(sorted(m[:p] + (idx[tuple(nb)],) + m[p + 1:]))
                d = acc.setdefault(tp[nm], {})
                # E_ij c_alpha = (alpha_i + 1) c_{alpha - e_j + e_i}.
                # NB the rule `alpha_j c_{...}` (used by session 26 and quoted in
                # docs/isotypic_rank.md) is the action on the MONOMIALS e^alpha of
                # Sym^n V, not on the COEFFICIENT functionals c_alpha, which are
                # e^alpha / alpha!.  The two differ by the diagonal rescaling
                # c_alpha -> alpha! c_alpha, so they give the same kernel
                # DIMENSION a but different kernel VECTORS -- and hence the same
                # `a` and a wrong `mult`.  See docs/visible_ideals.md section 1.
                d[pos[m]] = d.get(pos[m], 0) + al[i] + 1
        rows += list(acc.values())
    return basis, rows

def restrict(f, N, n, r, As):
    out = {}
    for beta, cf in f.items():
        cur = {tuple([0] * r): cf}
        for t in range(N):
            for _ in range(beta[t]):
                nxt = {}
                for al, c in cur.items():
                    for i in range(r):
                        v = As[i][t]
                        if v == 0: continue
                        k = list(al); k[i] += 1; k = tuple(k)
                        nxt[k] = nxt.get(k, 0) + c * v
                cur = nxt
        for al, c in cur.items(): out[al] = out.get(al, 0) + c
    return out

def eval_row(basis, coeffs, n, r):
    A = exps(n, r); row = []
    for m in basis:
        v = 1
        for k in m:
            v *= coeffs.get(A[k], 0)
            if v == 0: break
        row.append(v)
    return row

def _dense(rows, nc, p):
    M = []
    for rw in rows:
        if isinstance(rw, dict):
            v = [0] * nc
            for c, x in rw.items(): v[c] = x % p
            M.append(v)
        else: M.append([x % p for x in rw])
    return M

def rank_mod(rows, nc, p):
    M = _dense(rows, nc, p); rk, m = 0, len(M)
    for col in range(nc):
        piv = next((i for i in range(rk, m) if M[i][col]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][col], p - 2, p)
        for i in range(rk + 1, m):
            if M[i][col]:
                f = M[i][col] * inv % p; Mr, Mi = M[rk], M[i]
                for k in range(col, nc):
                    if Mr[k]: Mi[k] = (Mi[k] - f * Mr[k]) % p
        rk += 1
        if rk == m: break
    return rk

def kernel_mod(rows, nc, p):
    """basis of the null space, as a list of vectors mod p (RREF route)."""
    M = _dense(rows, nc, p); rk, m, piv_of = 0, len(M), {}
    for col in range(nc):
        piv = next((i for i in range(rk, m) if M[i][col]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][col], p - 2, p)
        M[rk] = [x * inv % p for x in M[rk]]
        for i in range(m):
            if i != rk and M[i][col]:
                f = M[i][col]; Mr, Mi = M[rk], M[i]
                for k in range(col, nc):
                    if Mr[k]: Mi[k] = (Mi[k] - f * Mr[k]) % p
        piv_of[col] = rk; rk += 1
        if rk == m: break
    free = [c for c in range(nc) if c not in piv_of]
    ker = []
    for fc in free:
        v = [0] * nc; v[fc] = 1
        for col, rw in piv_of.items(): v[col] = (-M[rw][fc]) % p
        ker.append(v)
    return ker

def measure(f, N, n, r, delta, lam, npts=None, seed=11, bound=40, want_U=False):
    """returns a, mult, and (optionally) a basis of U = the ideal slice."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    basis, R = build_R(n, r, delta, lam)
    nb = len(basis)
    if nb == 0: return dict(a=0, mult=0, nbasis=0)
    out = dict(nbasis=nb)
    rkR = {p: rank_mod(R, nb, p) for p in PRIMES}
    a = nb - rkR[PRIMES[0]]
    assert a == nb - rkR[PRIMES[1]], (lam, rkR)
    out['a'] = a
    if a == 0: out['mult'] = 0; return out
    rnd = random.Random(seed)
    K = npts if npts else a + 8
    ev = [eval_row(basis, restrict(f, N, n, r,
          [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]), n, r)
          for _ in range(K)]
    both = list(R) + ev
    ms = [rank_mod(both, nb, p) - rkR[p] for p in PRIMES]
    assert ms[0] == ms[1], (lam, ms)
    out['mult'] = ms[0]
    if want_U:
        # U = { u in ker R : sum u_k h_k vanishes on the orbit } expressed in the
        # coordinates of a fixed kernel basis of R.
        KB = kernel_mod(R, nb, PRIMES[0])          # a vectors, length nb
        p = PRIMES[0]
        rows = []
        for e in ev:
            rows.append([sum(e[i] * kb[i] for i in range(nb)) % p for kb in KB])
        out['U'] = kernel_mod(rows, a, p)          # subspace of C^a
        out['Udim'] = len(out['U'])
        assert out['Udim'] == a - out['mult'], (lam, out['Udim'], a, out['mult'])
    return out

# ------------------------------------------------------------------- forms
def det_form(k):
    out = {}
    for perm in itertools.permutations(range(k)):
        sgn, p = 1, list(perm)
        for i in range(k):
            for j in range(i + 1, k):
                if p[i] > p[j]: sgn = -sgn
        b = [0] * (k * k)
        for i in range(k): b[i * k + perm[i]] += 1
        out[tuple(b)] = out.get(tuple(b), 0) + sgn
    return out, k * k

def per_form(k):
    out = {}
    for perm in itertools.permutations(range(k)):
        b = [0] * (k * k)
        for i in range(k): b[i * k + perm[i]] += 1
        out[tuple(b)] = out.get(tuple(b), 0) + 1
    return out, k * k

def per_padded(m, n):
    """x_0^(n-m) . per_m on C^(1 + m*m); coordinate 0 is the padding variable."""
    base, nb = per_form(m); N = 1 + nb; out = {}
    for beta, c in base.items():
        b = [0] * N; b[0] = n - m
        for t in range(nb): b[1 + t] = beta[t]
        out[tuple(b)] = c
    return out, N
