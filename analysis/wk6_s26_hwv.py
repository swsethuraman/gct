"""Session 26 -- highest-weight vectors, and the isotypic rank.

ROUTE 2 for the ambient room a(lam,delta): build the weight-lam subspace of
C[W]_delta explicitly and take the kernel of the raising operators.  This
shares no code and no identity with the symmetric-function routes.

THE MEASUREMENT.  By the short-weight reduction (docs/isotypic_rank.md), a
highest-weight vector h of weight lam with ell(lam) = r involves only the
coefficients c_alpha with alpha supported on the first r coordinates, so

    h(g.det_3) = h( det(s_1 A_1 + ... + s_r A_r) ),    A_i = g^{-1} e_i,

an arbitrary r-tuple of 3x3 matrices.  Then

    mult_lam C[closure]_delta = a - dim{ u : sum_k u_k h_k vanishes on the orbit }
                              = rank [ h_k( det(sum s_i A_i^{(j)}) ) ]_{k,j}
                                for generic tuples (a lower bound for any finite
                                set of tuples, and equal to a once it reaches a).

Everything is exact: integer matrices, integer coefficients, exact rank over Q
and over a large prime.
"""

import random
from fractions import Fraction
from itertools import combinations_with_replacement as cwr
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import cubic_exponents, partitions

BIGP = (1 << 61) - 1          # 2^61 - 1, prime


# ------------------------------------------------------------ the graded piece
def mono_weight(mono, exps, r):
    w = [0] * r
    for i in mono:
        for t in range(r):
            w[t] += exps[i][t]
    return tuple(w)


def weight_basis(delta, r, lam):
    """The degree-delta monomials in the c_alpha of weight exactly lam,
    enumerated directly (never generated and filtered)."""
    exps = cubic_exponents(r)
    lam = tuple(lam) + (0,) * (r - len(lam))
    ne = len(exps)
    out = []
    # choose multiplicities for exps[idx..] summing to `left` slots with
    # remaining weight `need`; prune on the per-coordinate budget.
    def rec(idx, left, need, acc):
        if left == 0:
            if all(x == 0 for x in need):
                out.append(tuple(acc))
            return
        if idx == ne:
            return
        # prune: the largest weight still reachable in any coordinate is 3*left
        if sum(need) != 3 * left:
            return
        a = exps[idx]
        kmax = left
        for t in range(r):
            if a[t]:
                kmax = min(kmax, need[t] // a[t])
        for k in range(kmax, -1, -1):
            nn = tuple(need[t] - k * a[t] for t in range(r))
            rec(idx + 1, left - k, nn, acc + [idx] * k)
    rec(0, delta, lam, [])
    out.sort()
    return out, exps


def raise_op(mono, coeff, i, j, exps, eidx):
    """E_ij applied to the monomial (a derivation):  c_alpha -> alpha_j
    c_{alpha - eps_j + eps_i}.  Returns {monomial: coeff}."""
    out = {}
    for pos in range(len(mono)):
        al = exps[mono[pos]]
        if al[j] == 0:
            continue
        new = list(al)
        new[j] -= 1
        new[i] += 1
        k = eidx.get(tuple(new))
        if k is None:
            continue
        nm = list(mono)
        nm[pos] = k
        nm = tuple(sorted(nm))
        out[nm] = out.get(nm, 0) + coeff * al[j]
    return out


def hwv_basis(delta, r, lam):
    """Basis of highest-weight vectors of weight lam in C[W]_delta, as integer
    vectors over the weight-lam monomial basis.  Its length is a(lam,delta)."""
    src, exps = weight_basis(delta, r, lam)
    if not src:
        return [], [], exps
    eidx = {a: i for i, a in enumerate(exps)}
    sidx = {m: i for i, m in enumerate(src)}
    rows = []                       # equations: E_{i,i+1} h = 0
    tgt_index = {}
    for i in range(r - 1):
        j = i + 1
        for col, m in enumerate(src):
            for nm, c in raise_op(m, 1, i, j, exps, eidx).items():
                key = (i, nm)
                if key not in tgt_index:
                    tgt_index[key] = len(tgt_index)
                rows.append((tgt_index[key], col, c))
    nrow, ncol = len(tgt_index), len(src)
    M = [[Fraction(0)] * ncol for _ in range(nrow)]
    for rr, cc, v in rows:
        M[rr][cc] += v
    ker = nullspace(M, ncol)
    return ker, src, exps


def nullspace(M, ncol):
    """Exact nullspace of a list-of-lists Fraction matrix; integer basis out."""
    M = [row[:] for row in M]
    nrow = len(M)
    pivots = []
    rank = 0
    for col in range(ncol):
        piv = None
        for rr in range(rank, nrow):
            if M[rr][col] != 0:
                piv = rr
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pr = M[rank]
        pc = pr[col]
        M[rank] = [x / pc for x in pr]
        pr = M[rank]
        for rr in range(nrow):
            if rr != rank and M[rr][col] != 0:
                f = M[rr][col]
                M[rr] = [x - f * y for x, y in zip(M[rr], pr)]
        pivots.append(col)
        rank += 1
    free = [c for c in range(ncol) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0)] * ncol
        v[f] = Fraction(1)
        for rr, col in enumerate(pivots):
            v[col] = -M[rr][f]
        den = 1
        for x in v:
            den = den * x.denominator // _gcd(den, x.denominator)
        iv = [int(x * den) for x in v]
        g = 0
        for x in iv:
            g = _gcd(g, abs(x))
        if g:
            iv = [x // g for x in iv]
        basis.append(iv)
    return basis


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ------------------------------------------------------------- the evaluation
def det3(Mx):
    return (Mx[0][0] * (Mx[1][1] * Mx[2][2] - Mx[1][2] * Mx[2][1])
            - Mx[0][1] * (Mx[1][0] * Mx[2][2] - Mx[1][2] * Mx[2][0])
            + Mx[0][2] * (Mx[1][0] * Mx[2][1] - Mx[1][1] * Mx[2][0]))


def per3(Mx):
    return (Mx[0][0] * (Mx[1][1] * Mx[2][2] + Mx[1][2] * Mx[2][1])
            + Mx[0][1] * (Mx[1][0] * Mx[2][2] + Mx[1][2] * Mx[2][0])
            + Mx[0][2] * (Mx[1][0] * Mx[2][1] + Mx[1][1] * Mx[2][0]))


def form_coeffs(As, exps, kind='det'):
    """Coefficients c_alpha of  f(s_1 A_1 + ... + s_r A_r)  as a cubic in s.

    Expanded by multilinearity: the coefficient of s^alpha is the sum over
    ordered choices of rows consistent with alpha of the corresponding 3x3
    'mixed' determinant/permanent.  Implemented by brute-force polynomial
    expansion in the s_i, exactly.
    """
    r = len(As)
    f = det3 if kind == 'det' else per3
    # symbolic-free expansion: build the 3x3 matrix of linear forms as
    # dictionaries {monomial in s : coeff}, then run f over that ring.
    def lin(i, j):
        return {(0,) * k + (1,) + (0,) * (r - 1 - k): As[k][i][j]
                for k in range(r) if As[k][i][j]}

    def mul(p, q):
        out = {}
        for a, ca in p.items():
            for b, cb in q.items():
                key = tuple(x + y for x, y in zip(a, b))
                out[key] = out.get(key, 0) + ca * cb
        return {k: v for k, v in out.items() if v}

    def add(p, q, sign=1):
        out = dict(p)
        for k, v in q.items():
            out[k] = out.get(k, 0) + sign * v
        return {k: v for k, v in out.items() if v}

    Mx = [[lin(i, j) for j in range(3)] for i in range(3)]
    if kind == 'det':
        t1 = mul(Mx[0][0], add(mul(Mx[1][1], Mx[2][2]), mul(Mx[1][2], Mx[2][1]), -1))
        t2 = mul(Mx[0][1], add(mul(Mx[1][0], Mx[2][2]), mul(Mx[1][2], Mx[2][0]), -1))
        t3 = mul(Mx[0][2], add(mul(Mx[1][0], Mx[2][1]), mul(Mx[1][1], Mx[2][0]), -1))
        F = add(add(t1, t2, -1), t3, 1)
    else:
        t1 = mul(Mx[0][0], add(mul(Mx[1][1], Mx[2][2]), mul(Mx[1][2], Mx[2][1])))
        t2 = mul(Mx[0][1], add(mul(Mx[1][0], Mx[2][2]), mul(Mx[1][2], Mx[2][0])))
        t3 = mul(Mx[0][2], add(mul(Mx[1][0], Mx[2][1]), mul(Mx[1][1], Mx[2][0])))
        F = add(add(t1, t2), t3)
    return [F.get(a, 0) for a in exps]


def eval_hwv(vec, src, coeffs, mod=None):
    """Evaluate an integer combination of weight-lam monomials at a point."""
    tot = 0
    for c, m in zip(vec, src):
        if not c:
            continue
        p = c
        for i in m:
            p *= coeffs[i]
            if mod:
                p %= mod
        tot += p
        if mod:
            tot %= mod
    return tot


# ------------------------------------------------------------------ the rank
def rank_int(rows, mod=None):
    """Exact rank of a list of integer row-vectors (over Q, or mod a prime)."""
    if not rows:
        return 0
    if mod:
        M = [[x % mod for x in r] for r in rows]
        n, m, rk = len(M), len(M[0]), 0
        for col in range(m):
            piv = next((i for i in range(rk, n) if M[i][col]), None)
            if piv is None:
                continue
            M[rk], M[piv] = M[piv], M[rk]
            inv = pow(M[rk][col], mod - 2, mod)
            M[rk] = [(x * inv) % mod for x in M[rk]]
            for i in range(n):
                if i != rk and M[i][col]:
                    f = M[i][col]
                    M[i] = [(x - f * y) % mod for x, y in zip(M[i], M[rk])]
            rk += 1
        return rk
    M = [[Fraction(x) for x in r] for r in rows]
    n, m, rk = len(M), len(M[0]), 0
    for col in range(m):
        piv = next((i for i in range(rk, n) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pc = M[rk][col]
        M[rk] = [x / pc for x in M[rk]]
        for i in range(n):
            if i != rk and M[i][col] != 0:
                f = M[i][col]
                M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk


def measure(lam, delta, kind='det', npts=12, seed=26, spread=6, verbose=False):
    """mult_lam C[closure(f_3)]_delta for ell(lam) = r <= 4.

    Returns (a, rank, ranks_by_prefix, hwvs, points)."""
    lam = tuple(x for x in lam if x)
    r = len(lam)
    ker, src, exps = hwv_basis(delta, r, lam)
    a = len(ker)
    if a == 0:
        return 0, 0, [], [], []
    rng = random.Random(seed)
    cols = []
    for _ in range(npts):
        As = [[[rng.randint(-spread, spread) for _ in range(3)] for _ in range(3)]
              for _ in range(r)]
        co = form_coeffs(As, exps, kind)
        cols.append([eval_hwv(v, src, co) for v in ker])
    rows = [[cols[j][k] for j in range(npts)] for k in range(a)]
    ranks = [rank_int([row[:t] for row in rows]) for t in range(1, npts + 1)]
    rk = ranks[-1]
    rkp = rank_int(rows, mod=BIGP)
    assert rk == rkp, ("rank over Q and mod p disagree", lam, delta, rk, rkp)
    if verbose:
        print("  lam=%s delta=%d %s: a=%d rank=%d (by #points: %s)"
              % (lam, delta, kind, a, rk, ranks))
    return a, rk, ranks, ker, src


# ---------------------------------------------------------------------------
# The same measurement without ever forming a kernel basis.
#
#   HWV_lam = ker R  (R = the raising operators restricted to weight lam), so
#       a    = N_S - rank(R)
#       mult = dim ker R - dim(ker R ^ ker E) = rank([R;E]) - rank(R)
# with E the evaluation matrix (rows = orbit points, cols = weight-lam
# monomials).  Ranks over GF(p) for speed, cross-checked over Q and at a
# second prime on everything small enough.
# ---------------------------------------------------------------------------

P1 = (1 << 61) - 1
P2 = (1 << 31) - 1


def _rank_mod(rows, ncol, mod):
    M = [r[:] for r in rows]
    n, rk = len(M), 0
    for col in range(ncol):
        piv = None
        for i in range(rk, n):
            if M[i][col] % mod:
                piv = i
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][col] % mod, mod - 2, mod)
        M[rk] = [(x * inv) % mod for x in M[rk]]
        for i in range(n):
            if i != rk and M[i][col] % mod:
                f = M[i][col] % mod
                M[i] = [(x - f * y) % mod for x, y in zip(M[i], M[rk])]
        rk += 1
        if rk == n:
            break
    return rk


def raise_matrix(delta, r, lam):
    """Rows of the raising operators E_{i,i+1} on the weight-lam monomials."""
    src, exps = weight_basis(delta, r, lam)
    eidx = {a: i for i, a in enumerate(exps)}
    sidx = {m: i for i, m in enumerate(src)}
    tgt = {}
    ent = []
    for i in range(r - 1):
        for col, m in enumerate(src):
            for nm, c in raise_op(m, 1, i, i + 1, exps, eidx).items():
                key = (i, nm)
                if key not in tgt:
                    tgt[key] = len(tgt)
                ent.append((tgt[key], col, c))
    R = [[0] * len(src) for _ in range(len(tgt))]
    for rr, cc, v in ent:
        R[rr][cc] += v
    return R, src, exps


def measure_fast(lam, delta, kind='det', npts=None, seed=26, spread=6,
                 mods=(P1,), check_q=False):
    """(a, mult) for lam of any length, via rank([R;E]) - rank(R)."""
    lam = tuple(x for x in lam if x)
    r = len(lam)
    R, src, exps = raise_matrix(delta, r, lam)
    ns = len(src)
    if ns == 0:
        return 0, 0, 0
    res = []
    for mod in mods:
        rr = _rank_mod([[x % mod for x in row] for row in R], ns, mod)
        a = ns - rr
        if a == 0:
            res.append((0, 0))
            continue
        k = npts or (a + 4)
        rng = random.Random(seed)
        E = []
        for _ in range(k):
            As = [[[rng.randint(-spread, spread) for _ in range(3)] for _ in range(3)]
                  for _ in range(r)]
            co = form_coeffs(As, exps, kind)
            row = []
            for m in src:
                p = 1
                for i in m:
                    p = (p * co[i]) % mod
                row.append(p)
            E.append(row)
        rre = _rank_mod([[x % mod for x in row] for row in R] + E, ns, mod)
        res.append((a, rre - rr))
    assert len(set(res)) == 1, ("modular disagreement", lam, delta, res)
    a, mult = res[0]
    if check_q and ns <= 400:
        rr = rank_int(R) if R else 0
        rng = random.Random(seed)
        E = []
        for _ in range((npts or (a + 4))):
            As = [[[rng.randint(-spread, spread) for _ in range(3)] for _ in range(3)]
                  for _ in range(r)]
            co = form_coeffs(As, exps, kind)
            E.append([_prod(co, m) for m in src])
        rre = rank_int((R if R else []) + E)
        assert (ns - rr, rre - rr) == (a, mult), ("Q disagrees", lam, delta,
                                                  (ns - rr, rre - rr), (a, mult))
    return a, mult, ns


def _prod(co, m):
    p = 1
    for i in m:
        p *= co[i]
    return p


# ---------------------------------------------------------------------------
# numpy modular rank, for the long weights where the weight space runs to
# thousands of monomials.  Two primes, both small enough that p*p*ncol fits in
# int64, so every intermediate is exact.
# ---------------------------------------------------------------------------
NP1, NP2 = 46337, 46309


def rank_np(rows, ncol, mod):
    import numpy as np
    if not rows:
        return 0
    M = np.array(rows, dtype=np.int64) % mod
    n, rk = M.shape[0], 0
    for col in range(ncol):
        nz = np.nonzero(M[rk:, col])[0]
        if nz.size == 0:
            continue
        p = rk + int(nz[0])
        if p != rk:
            M[[rk, p]] = M[[p, rk]]
        inv = pow(int(M[rk, col]), mod - 2, mod)
        M[rk] = (M[rk] * inv) % mod
        colv = M[:, col].copy()
        colv[rk] = 0
        nzr = np.nonzero(colv)[0]
        if nzr.size:
            M[nzr] = (M[nzr] - np.outer(colv[nzr], M[rk])) % mod
        rk += 1
        if rk == n:
            break
    return rk


def measure_np(lam, delta, kind='det', npts=None, seed=26, spread=6,
               mods=(NP1, NP2), a_known=None):
    """(a, mult) via rank([R;E]) - rank(R), with numpy modular elimination."""
    lam = tuple(x for x in lam if x)
    r = len(lam)
    R, src, exps = raise_matrix(delta, r, lam)
    ns = len(src)
    if ns == 0:
        return 0, 0, 0
    out = []
    for mod in mods:
        rr = rank_np(R, ns, mod) if R else 0
        a = ns - rr
        if a_known is not None and a != a_known:
            raise AssertionError(("a mismatch", lam, delta, a, a_known, mod))
        if a == 0:
            out.append((0, 0))
            continue
        k = npts or (a + 4)
        rng = random.Random(seed)
        E = []
        for _ in range(k):
            As = [[[rng.randint(-spread, spread) for _ in range(3)] for _ in range(3)]
                  for _ in range(r)]
            co = form_coeffs(As, exps, kind)
            row = []
            for m in src:
                p = 1
                for i in m:
                    p = (p * co[i]) % mod
                row.append(p)
            E.append(row)
        rre = rank_np(R + E, ns, mod)
        out.append((a, rre - rr))
    assert len(set(out)) == 1, ("two primes disagree", lam, delta, out)
    return out[0][0], out[0][1], ns
