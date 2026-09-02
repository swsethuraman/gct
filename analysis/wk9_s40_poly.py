#!/usr/bin/env python3
"""
Session 40 -- small exact toolkit for quinary forms, determinantal pencils,
minor ideals and Macaulay matrices.  Shares no code with wk9_s35_daytests.py.

Forms are dicts {exponent tuple (length NV) : integer coefficient}; all ranks
are python-flint nmod_mat ranks at the two house primes.
"""
import itertools, random
from functools import lru_cache
from math import comb
from flint import nmod_mat

P1, P2 = 2147483647, 2147483629
NV = 5                                   # quinary throughout

# ------------------------------------------------------------- monomials
@lru_cache(maxsize=None)
def monos(d, nv=NV):
    """all exponent tuples of degree d in nv variables, sorted."""
    out = []
    def rec(pos, rem, cur):
        if pos == nv - 1:
            out.append(tuple(cur + [rem])); return
        for k in range(rem + 1):
            rec(pos + 1, rem - k, cur + [k])
    rec(0, d, [])
    return tuple(sorted(out))

@lru_cache(maxsize=None)
def mono_index(d, nv=NV):
    return {e: i for i, e in enumerate(monos(d, nv))}

# ------------------------------------------------------------- arithmetic
def padd(f, g):
    h = dict(f)
    for e, c in g.items():
        v = h.get(e, 0) + c
        if v: h[e] = v
        elif e in h: del h[e]
    return h

def pscale(f, c):
    return {e: c * v for e, v in f.items()} if c else {}

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
            ee = list(e); ee[k] -= 1; ee = tuple(ee)
            g[ee] = g.get(ee, 0) + c * e[k]
    return {e: c for e, c in g.items() if c}

def linform(coeffs):
    return {tuple(1 if j == i else 0 for j in range(NV)): c
            for i, c in enumerate(coeffs) if c}

def randform(d, rnd, box):
    return {e: rnd.randint(-box, box) for e in monos(d)}

# ----------------------------------------------------- determinantal pencils
def rand_pencil(n, rnd, box):
    """5 random integer n x n matrices A_1..A_5; M(s) = sum s_i A_i."""
    return [[[rnd.randint(-box, box) for _ in range(n)] for _ in range(n)]
            for _ in range(NV)]

def pencil_entries(A, n):
    """M(s) as an n x n array of linear forms in s_1..s_5."""
    return [[linform([A[k][i][j] for k in range(NV)]) for j in range(n)]
            for i in range(n)]

def perm_sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s

def det_of(ent, rows, cols):
    """determinant of the submatrix ent[rows][cols] (lists of indices), by
    permutation expansion; entries are forms."""
    k = len(rows); F = {}
    for perm in itertools.permutations(range(k)):
        sgn = perm_sign(perm)
        t = {tuple([0] * NV): sgn}
        for a in range(k):
            t = pmul(t, ent[rows[a]][cols[perm[a]]])
            if not t: break
        F = padd(F, t)
    return F

def det_form(ent, n):
    return det_of(ent, list(range(n)), list(range(n)))

def submax_minors(ent, n):
    """the n^2 (n-1)x(n-1) minors of M(s), as forms of degree n-1."""
    out = []
    for i in range(n):
        for j in range(n):
            rows = [a for a in range(n) if a != i]
            cols = [b for b in range(n) if b != j]
            out.append(det_of(ent, rows, cols))
    return out

# --------------------------------------------------------------- matrices
def rank_rows(rows, ncols, p):
    """rows: list of dict {col: int}; rank mod p via flint."""
    ent = [0] * (len(rows) * ncols)
    for r, row in enumerate(rows):
        base = r * ncols
        for c, v in row.items():
            ent[base + c] = v % p
    return nmod_mat(len(rows), ncols, ent, p).rank()

def ideal_degree_rows(gens, gdeg, k):
    """rows spanning the degree-k part of the ideal (gens) : every generator
    (degree gdeg) times every monomial of degree k - gdeg."""
    idx = mono_index(k); rows = []
    if k < gdeg: return rows, len(idx)
    for g in gens:
        for m in monos(k - gdeg):
            row = {}
            for e, c in g.items():
                ee = tuple(x + y for x, y in zip(e, m))
                row[idx[ee]] = row.get(idx[ee], 0) + c
            rows.append(row)
    return rows, len(idx)

def dim_ideal(gens, gdeg, k, p):
    rows, nc = ideal_degree_rows(gens, gdeg, k)
    return rank_rows(rows, nc, p) if rows else 0

def hilbert_quotient(gens, gdeg, k, p):
    """dim (S/(gens))_k mod p."""
    return comb(k + NV - 1, NV - 1) - dim_ideal(gens, gdeg, k, p)

def macaulay_corank(F, n, k, p):
    """corank of the degree-k Macaulay matrix of the five partials of the
    degree-n form F, i.e. dim (S/J_F)_k mod p."""
    grads = [pderiv(F, i) for i in range(NV)]
    return hilbert_quotient(grads, n - 1, k, p)

def saturated_dim(gens, gdeg, k, e, p):
    """dim of {G in S_k : G * m in (gens)_{k+e} for every monomial m of degree
    e} -- the degree-k part of the e-th quotient (gens):m^e.  For e beyond the
    saturation index this is h^0(I_Z(k)) for the scheme Z cut by gens."""
    K = comb(k + NV - 1, NV - 1)
    Jrows, nc = ideal_degree_rows(gens, gdeg, k + e)
    # basis of (S/J)_{k+e}: reduce columns mod the row space of J
    p_int = p
    M = nmod_mat(len(Jrows), nc, [0] * (len(Jrows) * nc), p_int)
    for r, row in enumerate(Jrows):
        for c, v in row.items(): M[r, c] = v % p_int
    R = M.rref()[0]
    rk = M.rank()
    # pivot columns of the rref
    piv = []
    r = 0
    for c in range(nc):
        if r < rk and int(R[r, c]) != 0:
            piv.append(c); r += 1
    pivset = set(piv); nonpiv = [c for c in range(nc) if c not in pivset]
    # a vector w in S_{k+e} is in J_{k+e} iff after reducing by R it vanishes;
    # reduction: w -> w - sum_r w[piv_r] * R[r].  The reduced vector is
    # supported on nonpivot columns; its coordinates are linear in w.
    # Build for each monomial m of degree e the map S_k -> S_{k+e}/J, then
    # stack: G must be in the joint kernel.
    idx_k = mono_index(k); idx_ke = mono_index(k + e)
    conds = []      # rows indexed by (m, nonpivot col); columns = S_k basis
    for m in monos(e):
        # the image of basis monomial b of S_k is the monomial b+m in S_{k+e}
        # reduced: coordinate at nonpivot column c is
        #   [b+m == c] - sum_r [b+m == piv_r] * R[r, c]
        col_of = {}
        for bi, b in enumerate(monos(k)):
            col_of[bi] = idx_ke[tuple(x + y for x, y in zip(b, m))]
        # rows: one per nonpivot column c
        rows_c = {c: {} for c in nonpiv}
        pivpos = {c: r for r, c in enumerate(piv)}
        for bi, c0 in col_of.items():
            if c0 in pivpos:
                rr = pivpos[c0]
                for c in nonpiv:
                    v = int(R[rr, c])
                    if v: rows_c[c][bi] = (rows_c[c].get(bi, 0) - v) % p_int
            else:
                rows_c[c0][bi] = (rows_c[c0].get(bi, 0) + 1) % p_int
        conds += [d for d in rows_c.values() if d]
    rk2 = rank_rows(conds, K, p_int) if conds else 0
    return K - rk2
