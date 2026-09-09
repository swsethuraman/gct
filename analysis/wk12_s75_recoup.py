#!/usr/bin/env python3
"""s75 -- the local block-swap recoupling for the S5 one-block recursion.

The S5 recursion presents M(rho) = HWV_rho(Sym^m Sym^4) as the +1 space of the
block swap on a one-block precursor.  The single non-trivial local ingredient is
the block swap of the *last two* 4-blocks, with all earlier blocks a symmetric
spectator of shape rho^{--} (rho minus two horizontal-4-strips).  That swap acts
on

    X_{rho--,rho} := ( S^{rho/rho--} )^{S_4 x S_4}          (S_8 skew Specht module)

whose dimension is the number of intermediate shapes mu (rho-- < mu < rho, both
steps horizontal-4-strips) = number of SSYT of shape rho/rho-- and content (4,4).
The block swap w0 = (0 4)(1 5)(2 6)(3 7) has eigenvalues (-1)^j on the
W_{(8-j,j)} isotypic part, multiplicities c^rho_{rho--,(8-j,j)}.

This module builds S^{rho/rho--} concretely as polytabloids in the row-tabloid
permutation module (no straightening, no seminormal conventions -- integer/exact
rational arithmetic), extracts the (S_4 x S_4)-invariants in the intermediate-mu
basis, and returns the exact block-swap matrix in that basis.

Everything is cached by the skew shape theta = rho/rho-- (many DAG nodes share
one theta).
"""
import sys, os, itertools
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


# ---------- partitions, strips ----------
def horiz_strips_below(rho, k):
    """all mu with rho/mu a horizontal k-strip (mu interlaces rho)."""
    r = len(rho)
    out = []
    def rec(i, cur, left):
        if i == r:
            if left == 0:
                mu = tuple(cur)
                while mu and mu[-1] == 0:
                    mu = mu[:-1]
                out.append(mu)
            return
        lo = rho[i + 1] if i + 1 < r else 0
        hi = rho[i]
        for v in range(max(lo, rho[i] - left), hi + 1):
            rec(i + 1, cur + [v], left - (rho[i] - v))
    rec(0, [], k)
    return sorted(set(out), reverse=True)


def cells_of_skew(rho, rhomm):
    """cells (i,j) 0-indexed with rhomm_i <= j < rho_i."""
    r = len(rho)
    rr = list(rhomm) + [0] * (r - len(rhomm))
    cells = []
    for i in range(r):
        for j in range(rr[i], rho[i]):
            cells.append((i, j))
    return cells


# ---------- skew standard Young tableaux ----------
def skew_syt(cells):
    """all standard fillings of the skew shape (cells) with 0..n-1:
       increasing along rows and down columns."""
    n = len(cells)
    cellset = set(cells)
    # for each cell, its left neighbour and up neighbour if in the skew shape
    order = sorted(cells)
    res = []
    # place values 0..n-1; value v must be greater than left/up neighbour values
    # do a backtracking over an assignment cell->value that is a bijection
    # represent tableau as dict cell->value; fill values in increasing order into
    # cells s.t. partial is standard.  Easier: assign values 0..n-1 to cells one
    # value at a time, each new value into a cell whose left & up (if present)
    # are already filled.
    filled = {}
    def rec(v):
        if v == n:
            res.append(dict(filled)); return
        for c in cells:
            if c in filled:
                continue
            i, j = c
            left = (i, j - 1)
            up = (i - 1, j)
            if left in cellset and left not in filled:
                continue
            if up in cellset and up not in filled:
                continue
            filled[c] = v
            rec(v + 1)
            del filled[c]
    rec(0)
    return res


# ---------- row-tabloid permutation module ----------
def row_of(cells):
    """map cell-> row index."""
    return {c: c[0] for c in cells}


def tabloid_key(assign, rows_by_row):
    """canonical key of a row tabloid: for each row, the sorted tuple of values."""
    return tuple(tuple(sorted(assign[c] for c in rows_by_row[r])) for r in rows_by_row)


def build_local(rho, rhomm):
    """Return (mus, S) where mus = list of intermediate shapes (basis order) and
       S = block-swap matrix (list of lists of Fraction) in the mu-basis."""
    cells = cells_of_skew(rho, rhomm)
    n = len(cells)
    assert n == 8, f"expected 8 skew cells, got {n} for {rho}/{rhomm}"
    cellset = set(cells)
    # rows partition
    rowset = {}
    for c in cells:
        rowset.setdefault(c[0], []).append(c)
    rows_by_row = {r: rowset[r] for r in sorted(rowset)}
    colset = {}
    for c in cells:
        colset.setdefault(c[1], []).append(c)

    syts = skew_syt(cells)

    # polytabloid e_T = sum over column-stabiliser perms pi of sgn(pi) {pi.T}
    # {t} = row tabloid canonical key.  Represent vector as dict key->Fraction.
    def poly_tabloid(T):
        # column groups: cells sharing a column
        colgroups = [grp for grp in colset.values()]
        vec = {}
        # iterate over all products of permutations within each column group
        ranges = []
        for grp in colgroups:
            vals = [T[c] for c in grp]
            ranges.append((grp, vals))
        # generate all combinations of permutations per column
        def rec(gi, assign, sign):
            if gi == len(ranges):
                key = tabloid_key(assign, rows_by_row)
                vec[key] = vec.get(key, Fr(0)) + sign
                return
            grp, vals = ranges[gi]
            for perm in itertools.permutations(range(len(grp))):
                s = perm_sign(perm)
                a2 = dict(assign)
                for idx, c in enumerate(grp):
                    a2[c] = vals[perm[idx]]
                rec(gi + 1, a2, sign * s)
        rec(0, {}, 1)
        return vec

    basis_vecs = [poly_tabloid(T) for T in syts]

    # We need (S_4^A x S_4^B)-invariants where A-values={0,1,2,3}, B={4,5,6,7}.
    # Build these directly in the mu-intermediate basis:
    #   for intermediate mu (rhomm < mu < rho, both h4-strips), the A-block adds
    #   strip mu/rhomm (4 cells), the B-block adds rho/mu (4 cells).  The invariant
    #   vector u_mu = symmetrise over S_4^A x S_4^B of a polytabloid whose A-cells
    #   carry 0..3 and B-cells carry 4..7.  A tabloid is fixed by within-row value
    #   perms; symmetrising over S_4^A merges the A-values within each row, etc.
    mus = [mu for mu in horiz_strips_below(rho, 4) if is_h4_below(mu, rhomm)]
    mus = sorted(mus, reverse=True)

    # value-permutation action on a tabloid-vector
    def act_perm(vec, sigma):
        out = {}
        # sigma: dict value->value.  A tabloid key is tuple of sorted row-tuples;
        # to act we must map values then re-sort each row.
        for key, co in vec.items():
            newrows = tuple(tuple(sorted(sigma[v] for v in row)) for row in key)
            out[newrows] = out.get(newrows, Fr(0)) + co
        return out

    def symmetrise_AB(vec):
        # average over S_4^A x S_4^B
        accum = {}
        A = [0, 1, 2, 3]; B = [4, 5, 6, 7]
        cnt = 0
        for pa in itertools.permutations(A):
            sa = {A[i]: pa[i] for i in range(4)}
            for pb in itertools.permutations(B):
                sb = {B[i]: pb[i] for i in range(4)}
                sig = dict(sa); sig.update(sb)
                w = act_perm(vec, sig)
                for k, c in w.items():
                    accum[k] = accum.get(k, Fr(0)) + c
                cnt += 1
        return {k: c / cnt for k, c in accum.items() if c != 0}

    # build u_mu
    u = []
    for mu in mus:
        Acells = cells_of_skew(mu, rhomm)      # strip mu/rhomm  -> A
        Bcells = cells_of_skew(rho, mu)        # strip rho/mu    -> B
        # a standard-ish tableau: A-cells get 0..3 (row-major), B-cells 4..7
        T = {}
        for idx, c in enumerate(sorted(Acells)):
            T[c] = idx
        for idx, c in enumerate(sorted(Bcells)):
            T[c] = 4 + idx
        e = poly_tabloid(T)
        u.append(symmetrise_AB(e))
    return mus, u


def w0_matrix(mus, u):
    """block swap w0=(0 4)(1 5)(2 6)(3 7) in the mu-basis {u_mu}; exact rationals."""
    # w0 as value permutation
    sig = {0: 4, 1: 5, 2: 6, 3: 7, 4: 0, 5: 1, 6: 2, 7: 3}

    def act_perm(vec):
        out = {}
        for key, co in vec.items():
            newrows = tuple(tuple(sorted(sig[v] for v in row)) for row in key)
            out[newrows] = out.get(newrows, Fr(0)) + co
        return out

    # to express w0 u_mu in basis {u_nu}, solve linear system over the union of keys
    keys = set()
    for v in u:
        keys |= set(v.keys())
    for v in u:
        keys |= set(act_perm(v).keys())
    keys = sorted(keys)
    import_flint = False
    # build matrix U (keys x mus)
    from fractions import Fraction as F
    U = [[v.get(k, F(0)) for v in u] for k in keys]
    W = [[act_perm(v).get(k, F(0)) for v in u] for k in keys]
    # solve U * S = W  (least squares exact: U has full column rank)
    S = solve_exact(U, W)
    return S


# ---------- exact linear algebra over Q ----------
def perm_sign(perm):
    perm = list(perm); s = 1; seen = [False] * len(perm)
    for i in range(len(perm)):
        if seen[i]:
            continue
        j = i; l = 0
        while not seen[j]:
            seen[j] = True; j = perm[j]; l += 1
        if l % 2 == 0:
            s = -s
    return s


def is_h4_below(mu, rhomm):
    """is rhomm obtained from mu by removing a horizontal 4-strip, i.e. mu/rhomm h4."""
    r = max(len(mu), len(rhomm))
    m = list(mu) + [0] * (r - len(mu))
    b = list(rhomm) + [0] * (r - len(rhomm))
    tot = 0
    for i in range(r):
        if m[i] < b[i]:
            return False
        tot += m[i] - b[i]
        # interlacing: b[i] >= m[i+1]
        if i + 1 < r and b[i] < m[i + 1]:
            return False
    return tot == 4


def solve_exact(U, W):
    """solve U S = W for S, U (rows x c) full column rank, W (rows x d). Exact Q."""
    rows = len(U); c = len(U[0]); d = len(W[0])
    # augmented [U | W], row reduce, read pivots for the c columns
    M = [[U[i][j] for j in range(c)] + [W[i][j] for j in range(d)] for i in range(rows)]
    pivrow = 0; pivcols = []
    for col in range(c):
        # find pivot
        sel = None
        for rr in range(pivrow, rows):
            if M[rr][col] != 0:
                sel = rr; break
        if sel is None:
            continue
        M[pivrow], M[sel] = M[sel], M[pivrow]
        pv = M[pivrow][col]
        M[pivrow] = [x / pv for x in M[pivrow]]
        for rr in range(rows):
            if rr != pivrow and M[rr][col] != 0:
                f = M[rr][col]
                M[rr] = [M[rr][k] - f * M[pivrow][k] for k in range(c + d)]
        pivcols.append((col, pivrow)); pivrow += 1
    # S: c x d ; from pivot rows
    S = [[Fr(0)] * d for _ in range(c)]
    for col, prow in pivcols:
        for k in range(d):
            S[col][k] = M[prow][c + k]
    # consistency check: residual zero
    for i in range(rows):
        for k in range(d):
            val = sum(U[i][j] * S[j][k] for j in range(c))
            assert val == W[i][k], "inconsistent solve (U not full column rank?)"
    return S


if __name__ == "__main__":
    # quick self-test on a small case
    rho = (6, 2); rhomm = ()
    print("skew", rho, "/", rhomm, "cells", cells_of_skew(rho, rhomm))
