#!/usr/bin/env python3
"""
Session 37, check 3 -- the lam_5 = 1 sub-slab probe (docs/blindness_slab.md
section 4): does the pad first-order jet variety lie in the closure of the
det first-order jet variety?

Setting (4 variables s = s_1..s_4 on the hyperplane x_5 = 0):
  jet(F) = (F_0, G),  F_0 = F|_{x5=0} in Sym^4 C^4,  G = dF/dx5|_{x5=0} in Sym^3 C^4.
  det jets:  F = det(M_0(s) + x_5 A),  G = tr(adj M_0(s) . A) -- as A ranges
             over M_4 the G's span V_{M_0} = span of the 16 ENTRIES of adj M_0.
  pad jets:  F = l.c,  F_0 = l_0 c_0,  G = a c_0 + l_0 q, q ANY quadric (washout).
Over F_0 = l_0 c_0 the pad jets form W = C c_0 + l_0 . Sym^2 (dim 11).

Block representation M_0 = diag(l_0, M), c_0 = det M: adj M_0 = diag(c_0, l_0 adj M),
so V_{M_0} = C c_0 + l_0 . span(entries of adj M): dim 10 -- one quadric short.
The probe: take the limit plane  L_B = lim_{t->0} V_{M_0 + tB}  (a 16-plane, a
point of the CLOSURE of the det jet variety over F_0) and test  W subset L_B.
All arithmetic exact modulo the two house primes, parameters uniform in F_p:
a false 'contained' reading has probability <= deg/p per prime (Schwartz-Zippel).
"""
import random, sys, itertools
from flint import nmod_mat, nmod_poly

P1, P2 = 2147483647, 2147483629
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 37

def exps(n, r=4):
    out = []
    def rec(k, left, cur):
        if k == r - 1: out.append(tuple(cur + [left])); return
        for v in range(left + 1): rec(k + 1, left - v, cur + [v])
    rec(0, n, [])
    return out
E1, E2, E3, E4 = exps(1), exps(2), exps(3), exps(4)
I3 = {e: k for k, e in enumerate(E3)}

# polynomials in s with coefficients in F_p[t]: dict exp -> nmod_poly
def pmul(a, b, p):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = out.get(e, nmod_poly([], p)) + ca * cb
    return out
def padd(a, b, p, sign=1):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, nmod_poly([], p)) + (c if sign == 1 else -c)
    return out
def const(c, p): return {(0, 0, 0, 0): nmod_poly([c], p)}
def linform(coeffs, p, tcoeffs=None):
    out = {}
    for k, e in enumerate(E1):
        out[e] = nmod_poly([coeffs[k]] + ([tcoeffs[k]] if tcoeffs else []), p)
    return out
def det3(m, p):
    tot = {}
    for perm in itertools.permutations(range(3)):
        sg = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if perm[i] > perm[j]: sg = -sg
        term = const(1, p)
        for i in range(3): term = pmul(term, m[i][perm[i]], p)
        tot = padd(tot, term, p, sg)
    return tot
def adj4(m, p):
    """adjugate entries adj[j][i] = (-1)^{i+j} det(minor removing row i, col j)."""
    adj = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            rows = [r for r in range(4) if r != i]; cols = [c for c in range(4) if c != j]
            minor = [[m[r][c] for c in cols] for r in rows]
            d = det3(minor, p)
            if (i + j) % 2: d = {e: -c for e, c in d.items()}
            adj[j][i] = d
    return adj
def cubic_vec(poly):
    """poly (deg 3 in s) -> list of 20 nmod_poly in t."""
    return [poly.get(e, None) for e in E3]

def limit_plane(vecs, p):
    """vecs: list of vectors in F_p[t]^20 (entries nmod_poly or None).
    Returns basis (list of int lists) of lim_{t->0} of their F_p(t)-span."""
    vecs = [[(v if v is not None else nmod_poly([], p)) for v in vec] for vec in vecs]
    n = len(vecs[0])
    while True:
        C = [[int(v[0]) if v.degree() >= 0 else 0 for v in vec] for vec in vecs]
        M = nmod_mat(len(vecs), n, [x for row in C for x in row], p)
        # left nullspace: solve c M = 0  <=>  M^T c^T = 0
        X, nul = M.transpose().nullspace()
        if nul == 0:
            return C
        c = [int(X[i, 0]) for i in range(len(vecs))]
        k = max(i for i in range(len(vecs)) if c[i] != 0)
        comb = [nmod_poly([], p) for _ in range(n)]
        for i in range(len(vecs)):
            if c[i]:
                for j in range(n): comb[j] += vecs[i][j] * c[i]
        t = nmod_poly([0, 1], p)
        new = []
        for j in range(n):
            q, r = divmod(comb[j], t)
            assert r.degree() < 0, "not divisible by t"
            new.append(q)
        vecs[k] = new

def rank_rows(rows, p):
    if not rows: return 0
    n = len(rows[0])
    return nmod_mat(len(rows), n, [x % p for r in rows for x in r], p).rank()

def run(p, rnd, nB=3):
    rint = lambda: rnd.randrange(p)
    l0 = [rint() for _ in range(4)]
    L0 = linform(l0, p)
    M = [[linform([rint() for _ in range(4)], p) for _ in range(3)] for _ in range(3)]
    c0 = det3(M, p)
    # block M_0 = diag(l_0, M)
    M0 = [[None] * 4 for _ in range(4)]
    M0[0][0] = L0
    for i in range(3):
        for j in range(3): M0[i + 1][j + 1] = M[i][j]
    zero = {}
    for i in range(4):
        for j in range(4):
            if M0[i][j] is None: M0[i][j] = zero
    # W = C c0 + l0 . Sym^2
    W = [[int(v[0]) if v is not None and v.degree() >= 0 else 0 for v in cubic_vec(c0)]]
    for e in E2:
        q = {e: nmod_poly([1], p)}
        W.append([int(v[0]) if v is not None and v.degree() >= 0 else 0
                  for v in cubic_vec(pmul(L0, q, p))])
    assert rank_rows(W, p) == 11
    # V_{M_0}
    A0 = adj4(M0, p)
    V0 = [[int(v[0]) if v is not None and v.degree() >= 0 else 0
           for v in cubic_vec(A0[i][j])] for i in range(4) for j in range(4)]
    print(f"  p={p}: dim V_(M_0) = {rank_rows(V0, p)} (block, expect 10); "
          f"rank[V_(M_0); W] = {rank_rows(V0 + W, p)} (expect 11: V_(M_0) is a hyperplane of W)")
    results = []
    for b in range(nB):
        # M_t = M_0 + t B, B a random 4x4 of linear forms
        Mt = [[None] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                Bij = {e: nmod_poly([0, rint()], p) for e in E1}
                Mt[i][j] = padd(M0[i][j], Bij, p)
        At = adj4(Mt, p)
        vecs = [cubic_vec(At[i][j]) for i in range(4) for j in range(4)]
        # generic rank check at t = random
        tv = rint()
        gen = [[int(v(tv)) if v is not None else 0 for v in vec] for vec in vecs]
        rg = rank_rows(gen, p)
        L = limit_plane(vecs, p)
        rL = rank_rows(L, p)
        rLW = rank_rows(L + W, p)
        rLV0 = rank_rows(L + V0, p)
        print(f"  p={p}: B#{b}: generic dim V_(M_t) = {rg}; dim L_B = {rL}; "
              f"rank[L_B; V_(M_0)] = {rLV0} (expect {rL}: L_B contains V_(M_0)); "
              f"rank[L_B; W] = {rLW}  -> W subset L_B: {rLW == rL}")
        results.append(rLW == rL)
    return results

if __name__ == "__main__":
    for p in (P1, P2):
        rnd = random.Random(SEED)
        run(p, rnd)
