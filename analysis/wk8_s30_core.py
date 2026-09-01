#!/usr/bin/env python3
"""
Session 30 -- isotypic rank machinery with the CORRECTED raising rule, on
python-flint.

    E_ij . c_alpha = (alpha_i + 1) . c_{alpha + e_i - e_j}

NOT `alpha_j . c_{...}` (the rule in docs/isotypic_rank.md section 1, which is
the action on the monomials e^alpha of Sym^n V; the coefficient functionals are
c_alpha = e^alpha / alpha! and carry the reciprocal factorials).  The two differ
by a diagonal rescaling: same kernel DIMENSION a, different kernel VECTORS, so
`a` is unaffected and `mult` is not.  No `mult = a` calibration can tell them
apart -- see the witness in wk8_s30_calib.py.

mult_lam C[closure(GL_N . f)]_delta = mult of S_lam(C^r) in C[D_r^f]_delta,
    D_r^f = closure{ (s_1..s_r) |-> f(sum s_i A_i) } in Sym^n C^r.
Ranks by flint nmod_mat over two word-size primes.
"""
import itertools, random
from functools import lru_cache
from flint import nmod_mat

P1, P2 = 2147483647, 2147483629

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
    A = exps(n, r); L = len(A)
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
    """rows of the simple raising operators on the weight-lam monomial basis."""
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
                d[pos[m]] = d.get(pos[m], 0) + al[i] + 1     # <-- corrected rule
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

def _mat(rows, nc, p):
    ent = [0] * (len(rows) * nc)
    for i, rw in enumerate(rows):
        base = i * nc
        if isinstance(rw, dict):
            for c, v in rw.items(): ent[base + c] = int(v) % p
        else:
            for c, v in enumerate(rw): ent[base + c] = int(v) % p
    return nmod_mat(len(rows), nc, ent, p)

def rank_of(rows, nc, p):
    return _mat(rows, nc, p).rank()

def nullspace(rows, nc, p):
    """basis of the null space as a list of python int vectors."""
    M = _mat(rows, nc, p)
    X, nul = M.nullspace()
    return [[int(X[i, j]) for i in range(nc)] for j in range(nul)]

def measure(f, N, n, r, delta, lam, npts=None, seed=11, bound=40, want_U=False,
            primes=(P1, P2), a_expect=None):
    lam = tuple(lam) + (0,) * (r - len(lam))
    basis, R = build_R(n, r, delta, lam)
    nb = len(basis)
    if nb == 0: return dict(a=0, mult=0, nbasis=0)
    out = dict(nbasis=nb)
    rkR = {p: rank_of(R, nb, p) for p in primes}
    a = nb - rkR[primes[0]]
    assert all(nb - rkR[p] == a for p in primes), (lam, rkR)
    if a_expect is not None:
        assert a == a_expect, ("a mismatch vs plethysm", lam, a, a_expect)
    out['a'] = a
    if a == 0: out['mult'] = 0; return out
    rnd = random.Random(seed)
    K = npts if npts else a + 8
    ev = [eval_row(basis, restrict(f, N, n, r,
          [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]), n, r)
          for _ in range(K)]
    both = list(R) + ev
    ms = {p: rank_of(both, nb, p) - rkR[p] for p in primes}
    assert len(set(ms.values())) == 1, (lam, ms)
    out['mult'] = ms[primes[0]]
    if want_U:
        p = primes[0]
        KB = nullspace(R, nb, p)
        rows = [[sum(e[i] * kb[i] for i in range(nb)) % p for kb in KB] for e in ev]
        out['U'] = nullspace(rows, a, p) if rows else [[1 if i == j else 0
                                                       for i in range(a)] for j in range(a)]
        out['Udim'] = len(out['U'])
        assert out['Udim'] == a - out['mult'], (lam, out['Udim'], a, out['mult'])
    return out

# ------------------------------------------------------------------- forms
def det_form(k):
    out = {}
    for perm in itertools.permutations(range(k)):
        sgn, pl = 1, list(perm)
        for i in range(k):
            for j in range(i + 1, k):
                if pl[i] > pl[j]: sgn = -sgn
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
    base, nb = per_form(m); N = 1 + nb; out = {}
    for beta, c in base.items():
        b = [0] * N; b[0] = n - m
        for t in range(nb): b[1 + t] = beta[t]
        out[tuple(b)] = c
    return out, N
