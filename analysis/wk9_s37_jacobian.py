#!/usr/bin/env python3
"""
Session 37, check 1 -- fresh-point Jacobian ranks for the washout lemma.

For f in {per_3 (9 vars, cubic), det_4 (16 vars, quartic), pad = x_0.per_3
(10 vars, quartic)} and r = 2..6, the parametrisation

    Phi_r : M^r -> Sym^n C^r,   (A_1..A_r) |-> f(sum_i s_i A_i)

has Jacobian rank at a random integer point computed exactly modulo the two
house primes.  rank at a point <= generic rank = dim D_r^f (char 0), so each
number is a LOWER bound on dim D_r^f, and equality with the ambient dimension
C(r+n-1, n) is a PROOF of dominance (washout).  Upper bounds come from the
finite-stabiliser page in docs/washout_lemma.md.

Derivatives are exact: the form is expanded symbolically as a polynomial in
the parameters via dual numbers (a + eps b, eps^2 = 0), one parameter at a
time, sharing nothing with analysis/wk8_s30_dims.py except the idea.
"""
import random, sys, itertools
from math import comb
from flint import nmod_mat

P1, P2 = 2147483647, 2147483629
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260902
BOX = 10**6

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

# a form is a dict {exponent tuple over N variables : coefficient}
def per_form(k):
    out = {}
    for p in itertools.permutations(range(k)):
        b = [0] * (k * k)
        for i in range(k): b[i * k + p[i]] += 1
        out[tuple(b)] = out.get(tuple(b), 0) + 1
    return out, k * k, k

def det_form(k):
    out = {}
    for p in itertools.permutations(range(k)):
        b = [0] * (k * k)
        for i in range(k): b[i * k + p[i]] += 1
        out[tuple(b)] = out.get(tuple(b), 0) + perm_sign(p)
    return out, k * k, k

def pad_form():
    base, N, n = per_form(3)
    out = {}
    for b, c in base.items(): out[(1,) + b] = c
    return out, N + 1, n + 1

def exps(n, r):
    out = []
    def rec(k, left, cur):
        if k == r - 1: out.append(tuple(cur + [left])); return
        for v in range(left + 1): rec(k + 1, left - v, cur + [v])
    rec(0, n, [])
    return out

def restrict_dual(f, N, n, r, A, dparam, p):
    """coefficients of f(sum s_i A_i) in Sym^n C^r with A[i][t] replaced by
    A[i][t] + eps * [ (i,t) == dparam ]; returns the eps-part as a dict."""
    out = {}
    for beta, cf in f.items():
        # product over variables t of (sum_i s_i A[i][t])^{beta_t}
        cur = {tuple([0] * r): (cf % p, 0)}
        for t in range(N):
            for _ in range(beta[t]):
                nxt = {}
                for al, (c0, c1) in cur.items():
                    for i in range(r):
                        a0 = A[i][t] % p
                        a1 = 1 if (i, t) == dparam else 0
                        if a0 == 0 and a1 == 0: continue
                        k = list(al); k[i] += 1; k = tuple(k)
                        d0, d1 = nxt.get(k, (0, 0))
                        nxt[k] = ((d0 + c0 * a0) % p, (d1 + c0 * a1 + c1 * a0) % p)
                cur = nxt
        for al, (c0, c1) in cur.items():
            out[al] = (out.get(al, 0) + c1) % p
    return out

def jac_rank(f, N, n, r, p, rnd):
    A = [[rnd.randint(-BOX, BOX) for _ in range(N)] for _ in range(r)]
    E = exps(n, r); idx = {e: k for k, e in enumerate(E)}
    rows = []
    for i in range(r):
        for t in range(N):
            d = restrict_dual(f, N, n, r, A, (i, t), p)
            row = [0] * len(E)
            for al, c in d.items(): row[idx[al]] = c
            rows.append(row)
    M = nmod_mat(len(rows), len(E), [v for row in rows for v in row], p)
    return M.rank(), len(E)

if __name__ == "__main__":
    forms = [("per_3", per_form(3), range(2, 7)),
             ("det_4", det_form(4), range(2, 7)),
             ("pad x0.per_3", pad_form(), range(3, 7))]
    print(f"seed {SEED}, box +-{BOX}")
    for name, (f, N, n), rs in forms:
        for r in rs:
            res = []
            for p in (P1, P2):
                rnd = random.Random(SEED * 1000 + r)
                rk, amb = jac_rank(f, N, n, r, p, rnd)
                res.append(rk)
            amb = comb(r + n - 1, n)
            print(f"{name:14s} r={r}  rank={res[0]},{res[1]}  ambient={amb}  "
                  f"{'DENSE' if res[0] == amb else ''}")
