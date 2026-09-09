#!/usr/bin/env python3
"""s76 -- Young's seminormal form on skew diagrams, strip invariants, and the
block-swap recoupling matrices of the S5 one-block recursion.

Conventions (recorded in results/PREREG_s76.md section 2):

  * cells are (row, col), 1-based inside a partition, content c = col - row;
  * a skew diagram is a frozenset of cells, normalised by translation
    (min row -> 0, min col -> 0) -- the seminormal matrices depend only on
    same-row / same-column incidences and content differences, so the
    normalised diagram determines them;
  * seminormal form, uniform rule: for i, i+1 not in the same row or column of
    the standard tableau T, with rho = 1/(c(i+1) - c(i)),
        s_i e_T = rho e_T + (1 - rho) e_{s_i T};
    same row: s_i e_T = e_T;  same column: s_i e_T = -e_T.
    (s_i^2 = 1 and the braid relations are checked in selftest().)
  * the trivial vector of S_4 on a horizontal 4-strip is the intersection of
    ker(s_i - 1), i = 1, 2, 3, normalised to coefficient 1 on the
    lexicographically first standard filling (fillings are sorted as tuples
    of cells in the order 1..4);
  * for a two-strip skew diagram D = nu/eta the block swap
    tau = (1 5)(2 6)(3 7)(4 8) is restricted to the (S_4 x S_4)-invariants
    in the basis u_xi = c^{xi/eta} (x) c^{nu/xi}, xi running over the
    intermediate shapes; R^D is defined by tau u_xi = sum_xi' R[xi', xi] u_xi'.

Everything here is exact over Q (fractions.Fraction); reduction mod p is done
by the caller.
"""
import itertools
import sys
from fractions import Fraction
from functools import lru_cache

sys.setrecursionlimit(10000)


# ----------------------------------------------------------------- diagrams
def cells_of(nu):
    return frozenset((i + 1, j + 1) for i, r in enumerate(nu) for j in range(r))


def skew_cells(nu, eta):
    """cells of nu/eta (eta padded with zeros)."""
    eta = tuple(eta) + (0,) * (len(nu) - len(eta))
    return frozenset((i + 1, j + 1) for i, r in enumerate(nu)
                     for j in range(eta[i], r))


def normalise(cells):
    r0 = min(r for r, _ in cells)
    c0 = min(c for _, c in cells)
    return frozenset((r - r0, c - c0) for r, c in cells)


# ------------------------------------------------- standard skew tableaux
@lru_cache(maxsize=256)
def standard_fillings(D):
    """all standard fillings of the (normalised) skew diagram D with 1..|D|,
    as tuples cell_1, ..., cell_m (cell_k = position of entry k); sorted."""
    D = frozenset(D)
    m = len(D)
    out = []

    def rec(placed, cur):
        if len(cur) == m:
            out.append(tuple(cur))
            return
        for cell in D:
            if cell in placed:
                continue
            r, c = cell
            # entry k goes to `cell`: every cell of D to its left in the row
            # and above it in the column must already hold a smaller entry
            if (r, c - 1) in D and (r, c - 1) not in placed:
                continue
            if (r - 1, c) in D and (r - 1, c) not in placed:
                continue
            placed.add(cell)
            cur.append(cell)
            rec(placed, cur)
            cur.pop()
            placed.remove(cell)

    rec(set(), [])
    out.sort()
    return tuple(out)


def _s_action(D, i):
    """matrix of s_i = (i, i+1) on the seminormal basis of S^D as a dict
    {(row_index, col_index): Fraction}; columns index e_T, rows index the
    output basis vectors."""
    fills = standard_fillings(D)
    index = {T: k for k, T in enumerate(fills)}
    M = {}
    for k, T in enumerate(fills):
        a, b = T[i - 1], T[i]            # cells of i and i+1
        if a[0] == b[0]:                 # same row
            M[(k, k)] = Fraction(1)
        elif a[1] == b[1]:               # same column
            M[(k, k)] = Fraction(-1)
        else:
            d = (b[1] - b[0]) - (a[1] - a[0])
            rho = Fraction(1, d)
            Tp = list(T)
            Tp[i - 1], Tp[i] = b, a
            kp = index[tuple(Tp)]
            M[(k, k)] = rho
            M[(kp, k)] = 1 - rho
    return M


@lru_cache(maxsize=64)
def s_columns(D, i):
    """sparse columns of s_i on S^D: list over basis index k of
    [(row_index, Fraction), ...] -- the image of e_{T_k}."""
    n = len(standard_fillings(D))
    cols = [[] for _ in range(n)]
    for (r, c), v in _s_action(D, i).items():
        cols[c].append((r, v))
    return cols


def apply_s(D, i, vec):
    """s_i applied to a dense list vector."""
    cols = s_columns(D, i)
    out = [Fraction(0)] * len(vec)
    for k, x in enumerate(vec):
        if x:
            for r, v in cols[k]:
                out[r] += v * x
    return out


def apply_perm(D, perm, vec):
    """perm (tuple, perm[k] = image of k+1) applied to vec, as a product of
    adjacent transpositions (bubble-sort word)."""
    word = []
    p = list(perm)
    changed = True
    while changed:
        changed = False
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i + 1)
                changed = True
    # perm = s_{word[-1]} ... s_{word[0]}: apply s_{word[0]} first
    for i in word:
        vec = apply_s(D, i, vec)
    return vec


def s_matrix(D, i):
    """dense list-of-rows Fraction matrix of s_i on S^D (small diagrams only)."""
    n = len(standard_fillings(D))
    M = [[Fraction(0)] * n for _ in range(n)]
    for (r, c), v in _s_action(D, i).items():
        M[r][c] = v
    return M


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[Fraction(0)] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        oi = out[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        oi[j] += a * Bt[j]
    return out


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def nullspace(A):
    """basis (list of Fraction row vectors) of {x : A x = 0}, A a list of rows."""
    if not A:
        return []
    m = len(A[0])
    R = [row[:] for row in A]
    pivots = []
    r = 0
    for c in range(m):
        piv = None
        for i in range(r, len(R)):
            if R[i][c]:
                piv = i
                break
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        inv = 1 / R[r][c]
        R[r] = [v * inv for v in R[r]]
        for i in range(len(R)):
            if i != r and R[i][c]:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        pivots.append(c)
        r += 1
        if r == len(R):
            break
    free = [c for c in range(m) if c not in pivots]
    basis = []
    for fcol in free:
        x = [Fraction(0)] * m
        x[fcol] = Fraction(1)
        for i, pc in enumerate(pivots):
            x[pc] = -R[i][fcol]
        basis.append(x)
    return basis


def invariants(D, gens):
    """basis of the joint fixed space of s_i, i in gens, on S^D (small D)."""
    n = len(standard_fillings(D))
    rows = []
    for i in gens:
        M = s_matrix(D, i)
        for r in range(n):
            row = M[r][:]
            row[r] -= 1
            rows.append(row)
    return nullspace(rows)


# --------------------------------------------------------- strip invariant
@lru_cache(maxsize=None)
def strip_invariant(D):
    """the S_4-invariant vector of a horizontal 4-strip D (normalised), as a
    dict filling -> Fraction, normalised to 1 on the lexicographically first
    standard filling."""
    assert len(D) == 4
    fills = standard_fillings(D)
    basis = invariants(D, (1, 2, 3))
    assert len(basis) == 1, (D, len(basis))
    v = basis[0]
    k0 = min(k for k in range(len(fills)) if v[k])
    v = [x / v[k0] for x in v]
    assert k0 == 0 or all(v[k] == 0 for k in range(k0))
    return {fills[k]: v[k] for k in range(len(fills)) if v[k]}


# ------------------------------------------------------------ recoupling
def intermediate_shapes(nu, eta):
    """xi with nu/xi and xi/eta horizontal 4-strips, in the canonical order
    used everywhere (horiz_strips order: sorted descending)."""
    from wk11_int_bdelta import horiz_strips
    xs = [xi for xi in horiz_strips(nu, 4) if eta in horiz_strips(xi, 4)]
    return xs


def _shift_filling(fill, cells_D):
    """re-express a filling given in absolute cells in the normalised cells."""
    return fill


def _rowcounts(S, nrows):
    v = [0] * nrows
    for r, _ in S:
        v[r] += 1
    return tuple(v)


def _is_hstrip(S):
    cols = [c for _, c in S]
    return len(cols) == len(set(cols))


@lru_cache(maxsize=None)
def recoupling_D(D):
    """the block-swap recoupling on a normalised two-strip skew diagram D:
    returns (subsets, R) where subsets are the intermediate 4-cell subsets S
    of D (xi/eta = S, nu/xi = D - S, both horizontal strips, S an order ideal of
    D) in the canonical order -- row-count vector descending, which is the
    order sorted(xis, reverse=True) of the actual shapes -- and R the matrix
    with tau u_S = sum_S' R[S'][S] u_S'."""
    D = frozenset(D)
    assert len(D) == 8
    nrows = max(r for r, _ in D) + 1
    subsets = []
    for S in itertools.combinations(sorted(D), 4):
        S = frozenset(S)
        T = D - S
        if not (_is_hstrip(S) and _is_hstrip(T)):
            continue
        ok = all(((r, c - 1) not in D or (r, c - 1) in S) and
                 ((r - 1, c) not in D or (r - 1, c) in S) for r, c in S)
        if ok:
            subsets.append(S)
    subsets.sort(key=lambda S: _rowcounts(S, nrows), reverse=True)
    fills = standard_fillings(D)
    index = {T: k for k, T in enumerate(fills)}
    n = len(fills)
    U, first = [], []
    for S in subsets:
        T = D - S
        ra, ca = min(r for r, _ in S), min(c for _, c in S)
        rb, cb = min(r for r, _ in T), min(c for _, c in T)
        cA = strip_invariant(frozenset((r - ra, c - ca) for r, c in S))
        cB = strip_invariant(frozenset((r - rb, c - cb) for r, c in T))
        u = [Fraction(0)] * n
        for TA, va in cA.items():
            TAabs = tuple((r + ra, c + ca) for r, c in TA)
            for TB, vb in cB.items():
                TBabs = tuple((r + rb, c + cb) for r, c in TB)
                u[index[TAabs + TBabs]] += va * vb
        supp = [k for k in range(n) if u[k]]
        k0 = min(supp)
        assert u[k0] == 1
        U.append(u)
        first.append(k0)
    m = len(subsets)
    shape_of = {}
    for j in range(m):
        for k in range(n):
            if U[j][k]:
                assert k not in shape_of
                shape_of[k] = j
    R = [[Fraction(0)] * m for _ in range(m)]
    tau = (5, 6, 7, 8, 1, 2, 3, 4)
    for i in range(m):
        t = apply_perm(D, tau, U[i])
        for j in range(m):
            R[j][i] = t[first[j]]
        for k in range(n):
            j = shape_of.get(k)
            expect = R[j][i] * U[j][k] if j is not None else Fraction(0)
            assert t[k] == expect, (D, "tau u not in the span of the u", k)
    assert matmul(R, R) == identity(m), (D, "R^2 != I")
    return tuple(subsets), R


def recoupling(nu, eta):
    """R^{nu/eta} in the basis u_xi, xi over intermediate_shapes(nu, eta)
    (sorted descending).  Computed once per normalised skew diagram."""
    nu = tuple(nu)
    eta = tuple(eta)
    xis = intermediate_shapes(nu, eta)
    cells = skew_cells(nu, eta)
    r0 = min(r for r, _ in cells)
    c0 = min(c for _, c in cells)
    D = frozenset((r - r0, c - c0) for r, c in cells)
    subsets, R = recoupling_D(D)
    pos = {S: k for k, S in enumerate(subsets)}
    order = []
    for xi in xis:
        S = frozenset((r - r0, c - c0) for r, c in skew_cells(xi, eta))
        order.append(pos[S])
    assert order == list(range(len(subsets))), (nu, eta, order)
    return xis, R


# ------------------------------------------------ the same thing mod p, fast
def _tau_word(n=8):
    word = []
    perm = list(range(n // 2 + 1, n + 1)) + list(range(1, n // 2 + 1))
    changed = True
    while changed:
        changed = False
        for i in range(len(perm) - 1):
            if perm[i] > perm[i + 1]:
                perm[i], perm[i + 1] = perm[i + 1], perm[i]
                word.append(i + 1)
                changed = True
    return word


TAU_WORD = _tau_word()


def intermediate_subsets(D):
    """the intermediate 4-cell subsets S of the normalised two-strip diagram D
    (xi/eta = S and nu/xi = D - S horizontal strips, S an order ideal of D), in
    the canonical order (row-count vector descending)."""
    D = frozenset(D)
    nrows = max(r for r, _ in D) + 1
    subsets = []
    for S in itertools.combinations(sorted(D), 4):
        S = frozenset(S)
        T = D - S
        if not (_is_hstrip(S) and _is_hstrip(T)):
            continue
        ok = all(((r, c - 1) not in D or (r, c - 1) in S) and
                 ((r - 1, c) not in D or (r - 1, c) in S) for r, c in S)
        if ok:
            subsets.append(S)
    subsets.sort(key=lambda S: _rowcounts(S, nrows), reverse=True)
    return tuple(subsets)


def recoupling_modp(D, p):
    """(subsets, R mod p) for the normalised two-strip diagram D: the block-swap
    recoupling matrix reduced mod p, computed in F_p from the start with numpy
    (the seminormal coefficients rho = 1/d are inverted mod p; p > every axial
    distance).  Verified in F_p: tau u_S lies in the span of the u_S (entry by
    entry on the disjoint supports) and R^2 = I."""
    import numpy as np
    D = frozenset(D)
    assert len(D) == 8
    fills = standard_fillings(D)
    index = {T: k for k, T in enumerate(fills)}
    n = len(fills)
    diag, off, offc = [], [], []
    for i in range(1, 8):
        dg = np.zeros(n, dtype=np.int64)
        of = np.full(n, -1, dtype=np.int64)
        oc = np.zeros(n, dtype=np.int64)
        for k, T in enumerate(fills):
            a, b = T[i - 1], T[i]
            if a[0] == b[0]:
                dg[k] = 1
            elif a[1] == b[1]:
                dg[k] = p - 1
            else:
                d = (b[1] - b[0]) - (a[1] - a[0])
                rho = pow(d % p, -1, p)
                Tp = list(T)
                Tp[i - 1], Tp[i] = b, a
                dg[k] = rho
                of[k] = index[tuple(Tp)]
                oc[k] = (1 - rho) % p
        diag.append(dg)
        off.append(of)
        offc.append(oc)
    masks = [of >= 0 for of in off]
    targets = [of[mk] for of, mk in zip(off, masks)]

    def apply(i, v):
        out = (diag[i - 1] * v) % p
        mk = masks[i - 1]
        out[targets[i - 1]] = (out[targets[i - 1]] + offc[i - 1][mk] * v[mk]) % p
        return out

    subsets = intermediate_subsets(D)
    U, first = [], []
    for S in subsets:
        T = D - S
        ra, ca = min(r for r, _ in S), min(c for _, c in S)
        rb, cb = min(r for r, _ in T), min(c for _, c in T)
        cA = strip_invariant(frozenset((r - ra, c - ca) for r, c in S))
        cB = strip_invariant(frozenset((r - rb, c - cb) for r, c in T))
        u = np.zeros(n, dtype=np.int64)
        for TA, va in cA.items():
            TAabs = tuple((r + ra, c + ca) for r, c in TA)
            va_p = (va.numerator % p) * pow(va.denominator % p, -1, p) % p
            for TB, vb in cB.items():
                TBabs = tuple((r + rb, c + cb) for r, c in TB)
                vb_p = (vb.numerator % p) * pow(vb.denominator % p, -1, p) % p
                k = index[TAabs + TBabs]
                u[k] = (u[k] + va_p * vb_p) % p
        supp = np.nonzero(u)[0]
        k0 = int(supp.min())
        assert u[k0] == 1
        U.append(u)
        first.append(k0)
    m = len(subsets)
    owner = np.full(n, -1, dtype=np.int64)
    for j in range(m):
        supp = np.nonzero(U[j])[0]
        assert np.all(owner[supp] == -1)
        owner[supp] = j
    R = [[0] * m for _ in range(m)]
    for i in range(m):
        t = U[i].copy()
        for w in TAU_WORD:
            t = apply(w, t)
        expect = np.zeros(n, dtype=np.int64)
        for j in range(m):
            R[j][i] = int(t[first[j]])
            expect = (expect + R[j][i] * U[j]) % p
        assert np.array_equal(t, expect), (D, "tau u not in the span of the u (mod p)")
    RR = [[sum(R[i][k] * R[k][j] for k in range(m)) % p for j in range(m)] for i in range(m)]
    assert RR == [[int(i == j) for j in range(m)] for i in range(m)], (D, "R^2 != I mod p")
    return subsets, R


# ------------------------------------------------------------- selftest
def selftest(verbose=True):
    import random
    random.seed(76)
    ok = 0
    # Coxeter relations on assorted skew diagrams of size <= 8
    shapes = [((4,), ()), ((3, 1), ()), ((2, 2), ()), ((5, 3), (1,)),
              ((6, 2), (2,)), ((4, 4), ()), ((8,), ()), ((7, 1), ()),
              ((5, 3, 2, 2), (3, 1, 1)), ((6, 4, 2, 2, 2), (4, 2, 2, 2)),
              ((9, 5, 2, 2), (5, 3, 2)), ((6, 6, 2, 2, 2, 2), (4, 4, 2, 2, 2)),
              ((7, 3, 2, 2, 1), (4, 2, 1)), ((5, 4, 3), (3, 2, 1)), ((4, 3, 2, 1), (2, 1))]
    shapes = [sh for sh in shapes if len(standard_fillings(normalise(skew_cells(*sh)))) <= 120]
    for nu, eta in shapes:
        cells = skew_cells(nu, eta)
        D = normalise(cells)
        m = len(D)
        n = len(standard_fillings(D))
        I = identity(n)
        for i in range(1, m):
            S = s_matrix(D, i)
            assert matmul(S, S) == I, ("s_i^2", nu, eta, i)
            if i + 1 < m:
                T = s_matrix(D, i + 1)
                assert matmul(matmul(S, T), S) == matmul(matmul(T, S), T), ("braid", nu, eta, i)
            for j in range(i + 2, m):
                T = s_matrix(D, j)
                assert matmul(S, T) == matmul(T, S), ("commute", nu, eta, i, j)
        ok += 1
    if verbose:
        print(f"seminormal: Coxeter relations hold on {ok} skew diagrams")
    # base cases delta = 2: the sign of tau on the one-dimensional channel
    signs = {}
    for nu in [(8,), (7, 1), (6, 2), (5, 3), (4, 4)]:
        xis, R = recoupling(nu, ())
        assert xis == [(4,)] and len(R) == 1
        signs[nu] = R[0][0]
    assert signs == {(8,): 1, (7, 1): -1, (6, 2): 1, (5, 3): -1, (4, 4): 1}, signs
    if verbose:
        print("recoupling: delta = 2 signs", {k: int(v) for k, v in signs.items()},
              "(h_2[h_4] = s_8 + s_62 + s_44)")
    # the mod-p route agrees with the exact route on every goal-cell diagram
    from wk11_int_cdelta import two_strip_paths
    from wk11_int_bdelta import lam_of
    lam = lam_of(24)
    p = 2147483647
    nD = 0
    for eta in sorted({nu for _, nu in two_strip_paths(24)}):
        xis, R = recoupling(lam, eta)
        cells = skew_cells(lam, eta)
        r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
        D = frozenset((r - r0, c - c0) for r, c in cells)
        subsets, Rp = recoupling_modp(D, p)
        assert len(subsets) == len(xis)
        for i in range(len(xis)):
            for j in range(len(xis)):
                x = R[i][j]
                assert Rp[i][j] == (x.numerator % p) * pow(x.denominator % p, -1, p) % p
        nD += 1
    if verbose:
        print(f"recoupling mod p agrees with the exact recoupling on all {nD} goal-cell diagrams")
    return True


if __name__ == "__main__":
    selftest()
