#!/usr/bin/env python3
"""
Session 44 -- exact toolkit for forms in r variables, determinantal and
padded-permanent points, and Macaulay matrices of the Jacobian ideal.

Written r-general (the s40 toolkit is hardwired to five variables).  Forms are
dicts {exponent tuple of length r : integer coefficient}; every rank is a
python-flint nmod_mat rank at a house prime.

  M_d(F) : rows indexed by (i, m), i = 1..r, m a monomial of degree d-n+1,
           columns by monomials of degree d, entry the coefficient of the
           column monomial in m * dF/dx_i.
  rank M_d(F) = dim (J_F)_d ;  corank = dim (S/J_F)_d .

For smooth F the partials are a regular sequence and the corank is
  h_d(n,r) = [t^d] ((1 - t^{n-1})/(1 - t))^r ,
so the generic rank is rho_d = dim Sym^d C^r - h_d.
"""
import itertools
from functools import lru_cache
from math import comb
from flint import nmod_mat, fmpz_mat

P1, P2 = 2147483647, 2147483629
PRIMES = (P1, P2)
P3 = 2147483587                      # third prime, only for tie-breaking


# ------------------------------------------------------------- combinatorics
def dim_sym(d, r):
    return comb(d + r - 1, r - 1) if d >= 0 else 0


def h_smooth(d, n, r):
    """[t^d] ((1 - t^{n-1})/(1-t))^r -- Milnor algebra of a smooth degree-n form."""
    return sum((-1) ** j * comb(r, j) * dim_sym(d - j * (n - 1), r)
               for j in range(r + 1) if d - j * (n - 1) >= 0)


def rho_generic(d, n, r):
    """expected (generic) rank of M_d = dim Sym^d - h_d, also the Koszul count."""
    return dim_sym(d, r) - h_smooth(d, n, r)


def koszul_rank(d, n, r):
    """rows minus Koszul syzygies, alternating: sum_j (-1)^j C(r,j+1) dim S_{d-(j+1)(n-1)}."""
    return sum((-1) ** j * comb(r, j + 1) * dim_sym(d - (j + 1) * (n - 1), r)
               for j in range(r))


def H_GN(d, n, r):
    """Gulliksen-Negard Hilbert function of S/J, J = ideal of (n-1)-minors of a
    generic n x n matrix, specialised to grade 4."""
    num = {0: 1, n - 1: -n * n, n: 2 * n * n - 2, n + 1: -n * n, 2 * n: 1}
    return sum(c * dim_sym(d - j, r) for j, c in num.items() if d - j >= 0)


# ------------------------------------------------------------- monomials
@lru_cache(maxsize=None)
def monos(d, r):
    out = []
    def rec(pos, rem, cur):
        if pos == r - 1:
            out.append(tuple(cur + [rem])); return
        for k in range(rem + 1):
            rec(pos + 1, rem - k, cur + [k])
    rec(0, d, [])
    return tuple(sorted(out))


@lru_cache(maxsize=None)
def mono_index(d, r):
    return {e: i for i, e in enumerate(monos(d, r))}


# ------------------------------------------------------------- form algebra
def padd(f, g):
    h = dict(f)
    for e, c in g.items():
        v = h.get(e, 0) + c
        if v: h[e] = v
        elif e in h: del h[e]
    return h


def pmul(f, g):
    h = {}
    for ea, ca in f.items():
        for eb, cb in g.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            h[e] = h.get(e, 0) + ca * cb
    return {e: c for e, c in h.items() if c}


def pderiv(f, k):
    g = {}
    for e, c in f.items():
        if e[k]:
            ee = list(e); ee[k] -= 1
            g[tuple(ee)] = g.get(tuple(ee), 0) + c * e[k]
    return {e: c for e, c in g.items() if c}


def linform(coeffs, r):
    return {tuple(1 if j == i else 0 for j in range(r)): c
            for i, c in enumerate(coeffs) if c}


def randform(d, r, rnd, box):
    return {e: rnd.randint(-box, box) for e in monos(d, r)}


# ------------------------------------------------------- pencils and points
def rand_pencil(n, r, rnd, box):
    """r random integer n x n matrices A_1..A_r; M(s) = sum_i s_i A_i."""
    return [[[rnd.randint(-box, box) for _ in range(n)] for _ in range(n)]
            for _ in range(r)]


def pencil_entries(A, n, r):
    return [[linform([A[k][i][j] for k in range(r)], r) for j in range(n)]
            for i in range(n)]


def perm_sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s


def _expand(ent, rows, cols, signed):
    k = len(rows); F = {}
    r = len(next(iter(ent[0][0])))
    for perm in itertools.permutations(range(k)):
        sgn = perm_sign(perm) if signed else 1
        t = {tuple([0] * r): sgn}
        for a in range(k):
            t = pmul(t, ent[rows[a]][cols[perm[a]]])
            if not t: break
        F = padd(F, t)
    return F


def det_form(ent, n):
    return _expand(ent, list(range(n)), list(range(n)), True)


def per_form(ent, n):
    return _expand(ent, list(range(n)), list(range(n)), False)


def submax_minors(ent, n):
    """the n^2 (n-1)x(n-1) minors of M(s), forms of degree n-1."""
    out = []
    for i in range(n):
        for j in range(n):
            out.append(_expand(ent, [a for a in range(n) if a != i],
                               [b for b in range(n) if b != j], True))
    return out


def det_point(n, r, rnd, box):
    return det_form(pencil_entries(rand_pencil(n, r, rnd, box), n, r), n)


def pad_per_point(m, r, rnd, box, npad=1):
    """l_1...l_npad * per_m(A(s)) : a padded permanent of degree m + npad in r
    variables.  For the six-row programme: m = 3, npad = 1, r = 6, degree 4."""
    ent = pencil_entries(rand_pencil(m, r, rnd, box), m, r)
    F = per_form(ent, m)
    for _ in range(npad):
        F = pmul(F, linform([rnd.randint(-box, box) for _ in range(r)], r))
    return F


# --------------------------------------------------------------- matrices
def ideal_rows(gens, gdeg, d, r):
    """rows spanning (gens)_d: every generator times every monomial of degree d-gdeg."""
    idx = mono_index(d, r); rows = []
    if d < gdeg: return rows, len(idx)
    for g in gens:
        for m in monos(d - gdeg, r):
            row = {}
            for e, c in g.items():
                ee = tuple(x + y for x, y in zip(e, m))
                row[idx[ee]] = row.get(idx[ee], 0) + c
            rows.append(row)
    return rows, len(idx)


def rank_rows(rows, ncols, p):
    ent = [0] * (len(rows) * ncols)
    for i, row in enumerate(rows):
        base = i * ncols
        for c, v in row.items():
            ent[base + c] = v % p
    return nmod_mat(len(rows), ncols, ent, p).rank()


def rank_rows_exact(rows, ncols):
    ent = [0] * (len(rows) * ncols)
    for i, row in enumerate(rows):
        base = i * ncols
        for c, v in row.items():
            ent[base + c] = v
    return fmpz_mat(len(rows), ncols, ent).rank()


def macaulay_rank(F, n, d, r, p):
    """rank of the degree-d Macaulay matrix of the r partials of F."""
    grads = [pderiv(F, i) for i in range(r)]
    rows, nc = ideal_rows(grads, n - 1, d, r)
    return rank_rows(rows, nc, p) if rows else 0


def macaulay_rank_exact(F, n, d, r):
    grads = [pderiv(F, i) for i in range(r)]
    rows, nc = ideal_rows(grads, n - 1, d, r)
    return rank_rows_exact(rows, nc) if rows else 0


def ideal_dim(gens, gdeg, d, r, p):
    rows, nc = ideal_rows(gens, gdeg, d, r)
    return rank_rows(rows, nc, p) if rows else 0
