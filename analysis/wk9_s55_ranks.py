#!/usr/bin/env python3
"""
Session 55, measurements M2 and M3.

M2  Hessian rank on the hypersurface, hence the exact dual dimension, at the
    committed degeneracy-direction test set of docs/brief_wording.md section 5:
    a det_4 pencil, a generic quartic, a reducible l*c, and the full
    ten-variable l*per_3.  This is simultaneously
      (a) the pre-check for the whole dual-degeneracy family, and
      (b) the entire content of "is 24 the floor of the LMR family at n = 4",
          since the LMR degree is 3(k+2) with k the dual dimension, monotone
          increasing in k, and the smallest admissible k is dim X^*(det).

    Fact used (proved in the report): at a smooth point x of a hypersurface
    X = {P = 0} in P(V),  dim X^* = rank Hess_x(P) - 2.

M3  The flattening family: rank of the middle catalecticant Cat_{2,2} and of
    the Koszul-Young flattening Phi_1 at the same four points.  The smallest
    minor of a flattening that vanishes on D_r has size rank(det pencil) + 1,
    which is that row's degree.

Exact arithmetic throughout: ranks over Q with fmpq_mat, cross-checked mod two
primes with nmod_mat.  No floating point.
"""

import sys
import random
from fractions import Fraction
from itertools import combinations_with_replacement, permutations, combinations

from flint import fmpq_mat, nmod_mat, fmpq

R = 10                       # number of variables x_0 .. x_9
PRIMES = (2147483647, 1000003)

# --------------------------------------------------------------- polynomials
# A polynomial is a dict: exponent tuple (length R) -> Fraction.

ZERO = (0,) * R


def mono_mul(a, b):
    return tuple(x + y for x, y in zip(a, b))


def poly_mul(p, q):
    out = {}
    for ea, ca in p.items():
        for eb, cb in q.items():
            e = mono_mul(ea, eb)
            out[e] = out.get(e, Fraction(0)) + ca * cb
    return {e: c for e, c in out.items() if c}


def poly_add(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, Fraction(0)) + c
    return {e: c for e, c in out.items() if c}


def poly_scale(p, s):
    s = Fraction(s)
    return {} if s == 0 else {e: c * s for e, c in p.items()}


def poly_eval(p, x):
    tot = Fraction(0)
    for e, c in p.items():
        t = c
        for i, ei in enumerate(e):
            if ei:
                t *= x[i] ** ei
        tot += t
    return tot


def diff(p, i):
    out = {}
    for e, c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c * e[i]
    return out


def linear(coeffs):
    return {tuple(1 if j == i else 0 for j in range(R)): Fraction(c)
            for i, c in enumerate(coeffs) if c}


def rand_poly(deg, rng, lo=-9, hi=9, vars_=None):
    vs = range(R) if vars_ is None else vars_
    out = {}
    for combo in combinations_with_replacement(vs, deg):
        e = [0] * R
        for i in combo:
            e[i] += 1
        c = rng.randint(lo, hi)
        if c:
            out[tuple(e)] = Fraction(c)
    return out


# --------------------------------------------------------------- test points
def det4_pencil(rng):
    """P(s) = det_4(sum_a s_a A_a), A_a random integer 4x4, a = 0..9."""
    A = [[[rng.randint(-6, 6) for _ in range(4)] for _ in range(4)]
         for _ in range(R)]
    ent = [[linear([A[a][i][j] for a in range(R)]) for j in range(4)]
           for i in range(4)]
    P = {}
    for perm in permutations(range(4)):
        sgn = 1
        pl = list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    sgn = -sgn
        term = {ZERO: Fraction(sgn)}
        for i in range(4):
            term = poly_mul(term, ent[i][perm[i]])
        P = poly_add(P, term)
    return P, A


def kernel_point(A, rng):
    """A rational s with A(s)v = 0 for a random v, hence det A(s) = 0."""
    for _ in range(200):
        v = [Fraction(rng.randint(-5, 5)) for _ in range(4)]
        if all(t == 0 for t in v):
            continue
        # rows: sum_a s_a (A_a v)_i = 0  for i = 0..3
        M = [[sum(Fraction(A[a][i][j]) * v[j] for j in range(4))
              for a in range(R)] for i in range(4)]
        ker = nullspace(M, R)
        if len(ker) < 2:
            continue
        s = [Fraction(0)] * R
        for b in ker:
            lam = Fraction(rng.randint(-7, 7))
            s = [si + lam * bi for si, bi in zip(s, b)]
        if any(si != 0 for si in s):
            return s, v
    raise RuntimeError("no kernel point")


def nullspace(M, ncols):
    """Exact nullspace basis of a list-of-rows rational matrix."""
    M = [row[:] for row in M]
    nrows = len(M)
    piv, r = [], 0
    for c in range(ncols):
        p = None
        for i in range(r, nrows):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fraction(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == nrows:
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis


def per3(rng=None):
    """per_3 in x_1..x_9, laid out as the 3x3 matrix [[x1,x2,x3],[x4..],[x7..]]."""
    P = {}
    for perm in permutations(range(3)):
        e = [0] * R
        for i in range(3):
            e[1 + 3 * i + perm[i]] += 1
        P[tuple(e)] = P.get(tuple(e), Fraction(0)) + 1
    return P


def point_on(P, rng, forced=None, solve_var=None):
    """A rational point with P(x) = 0, by solving for x[solve_var] (P linear in it)."""
    for _ in range(400):
        x = [Fraction(rng.randint(-6, 6)) for _ in range(R)]
        if forced:
            for i, val in forced.items():
                x[i] = Fraction(val)
        a = Fraction(0)   # coefficient of x[solve_var]
        b = Fraction(0)   # rest
        ok = True
        for e, c in P.items():
            if e[solve_var] > 1:
                ok = False
                break
            t = c
            for i, ei in enumerate(e):
                if i != solve_var and ei:
                    t *= x[i] ** ei
            if e[solve_var] == 1:
                a += t
            else:
                b += t
        if not ok:
            raise ValueError("not linear in the solve variable")
        if a == 0:
            continue
        x[solve_var] = -b / a
        if any(xi != 0 for xi in x):
            return x
    raise RuntimeError("no point found")


def make_vanish_at(P, x, mono):
    """Shift one coefficient so that P(x) = 0; mono must not vanish at x."""
    val = poly_eval(P, x)
    m = Fraction(1)
    for i, ei in enumerate(mono):
        if ei:
            m *= x[i] ** ei
    assert m != 0
    Q = dict(P)
    Q[mono] = Q.get(mono, Fraction(0)) - val / m
    if Q[mono] == 0:
        del Q[mono]
    assert poly_eval(Q, x) == 0
    return Q


# --------------------------------------------------------------------- ranks
def rank_Q(rows, nr, nc):
    M = fmpq_mat(nr, nc, [fmpq(c.numerator, c.denominator) for c in rows])
    return M.rank()


def rank_p(rows, nr, nc, p):
    ent = []
    for c in rows:
        num = c.numerator % p
        den = c.denominator % p
        ent.append((num * pow(den, p - 2, p)) % p)
    return nmod_mat(nr, nc, ent, p).rank()


def hess_rank(P, x):
    d1 = [diff(P, i) for i in range(R)]
    H = []
    for i in range(R):
        di = d1[i]
        for j in range(R):
            H.append(poly_eval(diff(di, j), x))
    grad = [poly_eval(d, x) for d in d1]
    rQ = rank_Q(H, R, R)
    rp = [rank_p(H, R, R, p) for p in PRIMES]
    return rQ, rp, any(g != 0 for g in grad)


PAIRS = list(combinations_with_replacement(range(R), 2))       # 55


def cat22_rank(P):
    """rank of the middle catalecticant = dim span of the second partials."""
    fact = (1, 1, 2, 6, 24)
    rows = []
    for (i, j) in PAIRS:
        for (k, l) in PAIRS:
            e = [0] * R
            for t in (i, j, k, l):
                e[t] += 1
            c = P.get(tuple(e), Fraction(0))
            m = 1
            for ei in e:
                m *= fact[ei]
            rows.append(c * m)
    n = len(PAIRS)
    return rank_Q(rows, n, n), [rank_p(rows, n, n, p) for p in PRIMES]


WEDGE = list(combinations(range(R), 2))                        # 45
WIDX = {w: i for i, w in enumerate(WEDGE)}


def koszul_rank(P, p):
    """Koszul-Young flattening Phi : V (x) V^* -> Lambda^2 V (x) S^2 V,
       e_c (x) d_j  |->  sum_i (e_i ^ e_c) (x) d_i d_j P .   (rows mod p)"""
    d2 = {}
    for i in range(R):
        di = diff(P, i)
        for j in range(i, R):
            d2[(i, j)] = diff(di, j)
    mon2 = PAIRS
    midx = {m: t for t, m in enumerate(mon2)}
    nrows = len(WEDGE) * len(mon2)
    ncols = R * R
    ent = [0] * (nrows * ncols)
    for c in range(R):
        for j in range(R):
            col = c * R + j
            for i in range(R):
                if i == c:
                    continue
                w = (i, c) if i < c else (c, i)
                sgn = 1 if i < c else -1
                q = d2[(min(i, j), max(i, j))]
                blk = WIDX[w] * len(mon2)
                for e, coeff in q.items():
                    m = tuple(t for t in range(R) for _ in range(e[t]))
                    v = coeff * sgn
                    val = (v.numerator % p) * pow(v.denominator % p, p - 2, p) % p
                    idx = (blk + midx[m]) * ncols + col
                    ent[idx] = (ent[idx] + val) % p
    return nmod_mat(nrows, ncols, ent, p).rank()


# ---------------------------------------------------------------------- main
def main(seed):
    rng = random.Random(seed)
    print(f"=== seed {seed} ===")

    pts = []

    # A: det_4 pencil, r = 10
    Pa, A = det4_pencil(rng)
    sa, _ = kernel_point(A, rng)
    assert poly_eval(Pa, sa) == 0
    pts.append(("A  det_4 pencil (r=10)", Pa, [("rank-3 point", sa)]))

    # B: generic quartic
    xb = [Fraction(rng.randint(1, 9)) for _ in range(R)]
    Pb = make_vanish_at(rand_poly(4, rng), xb, tuple([4] + [0] * (R - 1)))
    pts.append(("B  generic quartic", Pb, [("generic point", xb)]))

    # C: l * c, l linear, c generic cubic
    lc = [rng.randint(1, 9) for _ in range(R)]
    ell = linear(lc)
    xc1 = point_on(ell, rng, solve_var=0)
    xc2 = [Fraction(rng.randint(1, 9)) for _ in range(R)]
    cub = make_vanish_at(rand_poly(3, rng), xc2, tuple([3] + [0] * (R - 1)))
    Pc = poly_mul(ell, cub)
    assert poly_eval(Pc, xc1) == 0 and poly_eval(Pc, xc2) == 0
    pts.append(("C  l * c  (c generic cubic)", Pc,
                [("on {l=0}", xc1), ("on {c=0}", xc2)]))

    # D: x_0 * per_3(x_1..x_9)  -- the full ten-variable padded permanent
    q = per3()
    Pd = poly_mul(linear([1] + [0] * (R - 1)), q)
    xd1 = [Fraction(0)] + [Fraction(rng.randint(-6, 6)) for _ in range(R - 1)]
    xd2 = point_on(q, rng, forced={0: rng.randint(1, 9)}, solve_var=9)
    assert poly_eval(Pd, xd1) == 0 and poly_eval(Pd, xd2) == 0
    pts.append(("D  x_0 * per_3 (ten variables)", Pd,
                [("on {x_0=0}", xd1), ("on {per_3=0}", xd2)]))

    print()
    print("M2  Hessian rank on the hypersurface, and dim X^* = rank - 2")
    print("    point                            component        rank(Q)  "
          "mod p1  mod p2  smooth  dim X^*")
    duals = {}
    for name, P, plist in pts:
        best = -1
        for cname, x in plist:
            rQ, rp, smooth = hess_rank(P, x)
            dstar = rQ - 2 if smooth else None
            if smooth:
                best = max(best, dstar)
            print(f"    {name:<32} {cname:<16} {rQ:5d}  {rp[0]:6d}  {rp[1]:6d}"
                  f"   {str(smooth):<6} {dstar}")
        duals[name] = best
        print(f"    {'':32} {'--> dim X^* =':<16} {best}")
    print()

    print("M3  flattening ranks")
    print("    point                            Cat_{2,2}(Q)  mod p1  mod p2"
          "   Koszul Phi_1 (mod p1)")
    for name, P, _ in pts:
        cQ, cp = cat22_rank(P)
        kz = koszul_rank(P, PRIMES[0])
        print(f"    {name:<32} {cQ:12d}  {cp[0]:6d}  {cp[1]:6d}   {kz:6d}")
    print()
    return duals


if __name__ == "__main__":
    seeds = [int(a) for a in sys.argv[1:]] or [55]
    for s in seeds:
        main(s)
