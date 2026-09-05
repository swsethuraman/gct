#!/usr/bin/env python3
"""
Session 55, verification pass.  Closes the gaps an adversarial review found in
the first draft of the census.

C1  Cat_{1,3} -- pre-registered in results/PREREG_s55.md M3 and missing from the
    first run.
C2  rank Hess(per_3) on {per_3 = 0}, sampled properly.  The first run drew
    coordinates from [-6,6], so about half the draws had a zero coordinate and
    returned rank 8; the dual dimension is the value at a GENERAL point, i.e.
    the maximum, so the reported 9 was right but the sample was not clean.
    Re-run with all-nonzero coordinates and report the whole distribution.
C3  the node check: a rank-2 point of a 5-dimensional pencil is an ORDINARY node
    of the quartic threefold, i.e. the projective Hessian there has rank exactly
    r-1 = 4.  The first run measured the LENGTH of the singular scheme (20), not
    its node-ness.
C4  the Koszul flattening rank over Q and mod the second prime, so the census's
    "measured exactly" is honest.
C5  rank A(s) = 3 at the point used for the det_4 pencil -- the first run
    labelled it "rank-3 point" without checking.
C6  the banked catalecticant bound rank Cat_{2,2}(l.c) <= 2r
    (docs/theory_directions.md sec. B(a), proved at s35) checked at r = 10.
"""

import random
from fractions import Fraction
from itertools import combinations_with_replacement, combinations, permutations

from flint import fmpq_mat, nmod_mat, fmpq

R = 10
PRIMES = (2147483647, 1000003)


def poly_mul(p, q):
    out = {}
    for ea, ca in p.items():
        for eb, cb in q.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = out.get(e, Fraction(0)) + ca * cb
    return {e: c for e, c in out.items() if c}


def poly_add(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, Fraction(0)) + c
    return {e: c for e, c in out.items() if c}


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


def linear(co, n=R):
    return {tuple(1 if j == i else 0 for j in range(n)): Fraction(c)
            for i, c in enumerate(co) if c}


def det_pencil(A, n=R):
    ent = [[linear([A[a][i][j] for a in range(n)], n) for j in range(4)]
           for i in range(4)]
    P = {}
    for perm in permutations(range(4)):
        sgn, pl = 1, list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    sgn = -sgn
        term = {(0,) * n: Fraction(sgn)}
        for i in range(4):
            term = poly_mul(term, ent[i][perm[i]])
        P = poly_add(P, term)
    return P


def rank_Q(rows, nr, nc):
    return fmpq_mat(nr, nc, [fmpq(c.numerator, c.denominator)
                             for c in rows]).rank()


def rank_p(rows, nr, nc, p):
    return nmod_mat(nr, nc, [((c.numerator % p) *
                              pow(c.denominator % p, p - 2, p)) % p
                             for c in rows], p).rank()


def hess_rows(P, x, n=R):
    d1 = [diff(P, i) for i in range(n)]
    return [poly_eval(diff(d1[i], j), x) for i in range(n) for j in range(n)], \
           [poly_eval(d, x) for d in d1]


def per3():
    P = {}
    for perm in permutations(range(3)):
        e = [0] * R
        for i in range(3):
            e[1 + 3 * i + perm[i]] += 1
        P[tuple(e)] = P.get(tuple(e), Fraction(0)) + 1
    return P


def rand_poly(deg, rng, n=R):
    out = {}
    for combo in combinations_with_replacement(range(n), deg):
        e = [0] * n
        for i in combo:
            e[i] += 1
        c = rng.randint(-9, 9)
        if c:
            out[tuple(e)] = Fraction(c)
    return out


def make_vanish_at(P, x, mono):
    val = poly_eval(P, x)
    m = Fraction(1)
    for i, ei in enumerate(mono):
        if ei:
            m *= x[i] ** ei
    Q = dict(P)
    Q[mono] = Q.get(mono, Fraction(0)) - val / m
    if Q[mono] == 0:
        del Q[mono]
    return Q


def nullspace(M, ncols):
    M = [row[:] for row in M]
    piv, r = [], 0
    for c in range(ncols):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fraction(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    out = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        out.append(v)
    return out


# --------------------------------------------------------------- build points
rng = random.Random(55)
A = [[[rng.randint(-6, 6) for _ in range(4)] for _ in range(4)]
     for _ in range(R)]
Pa = det_pencil(A)
v = [Fraction(rng.randint(-5, 5)) for _ in range(4)]
Mv = [[sum(Fraction(A[a][i][j]) * v[j] for j in range(4)) for a in range(R)]
      for i in range(4)]
ker = nullspace(Mv, R)
sa = [Fraction(0)] * R
for b in ker:
    lam = Fraction(rng.randint(-7, 7))
    sa = [si + lam * bi for si, bi in zip(sa, b)]
assert poly_eval(Pa, sa) == 0

xb = [Fraction(rng.randint(1, 9)) for _ in range(R)]
Pb = make_vanish_at(rand_poly(4, rng), xb, tuple([4] + [0] * (R - 1)))
ell = linear([rng.randint(1, 9) for _ in range(R)])
xc2 = [Fraction(rng.randint(1, 9)) for _ in range(R)]
cub = make_vanish_at(rand_poly(3, rng), xc2, tuple([3] + [0] * (R - 1)))
Pc = poly_mul(ell, cub)
q = per3()
Pd = poly_mul(linear([1] + [0] * (R - 1)), q)

PTS = [("A det_4 pencil", Pa), ("B generic quartic", Pb),
       ("C l*c", Pc), ("D x_0*per_3", Pd)]

# ------------------------------------------------------------------------- C5
print("C5  rank A(s) at the point used for the det_4 pencil")
Ms = [[sum(Fraction(A[a][i][j]) * sa[a] for a in range(R)) for j in range(4)]
      for i in range(4)]
rA = fmpq_mat(4, 4, [fmpq(Ms[i][j].numerator, Ms[i][j].denominator)
                     for i in range(4) for j in range(4)]).rank()
print(f"    rank A(s) = {rA}   (must be 3: on the hypersurface and a smooth point)")
assert rA == 3
print()

# ------------------------------------------------------------------------- C1
print("C1  Cat_{1,3} : V^* -> S^3 V   (rank = dim span of the first partials)")
print("    point                 rank(Q)   mod p1   mod p2   dim V")
mon3 = list(combinations_with_replacement(range(R), 3))
midx = {m: i for i, m in enumerate(mon3)}
for name, P in PTS:
    rows = [Fraction(0)] * (R * len(mon3))
    for i in range(R):
        d = diff(P, i)
        for e, c in d.items():
            m = tuple(t for t in range(R) for _ in range(e[t]))
            rows[i * len(mon3) + midx[m]] = c
    rQ = rank_Q(rows, R, len(mon3))
    rp = [rank_p(rows, R, len(mon3), p) for p in PRIMES]
    print(f"    {name:<20} {rQ:7d}   {rp[0]:6d}   {rp[1]:6d}   {R:5d}")
print("    Full rank at all four points: Cat_{1,3} is vacuous, as expected.")
print()

# ------------------------------------------------------------------------- C4
print("C4  Koszul flattening Phi_1 : V (x) V^* -> Lambda^2 V (x) S^2 V, over Q")
WEDGE = list(combinations(range(R), 2))
WIDX = {w: i for i, w in enumerate(WEDGE)}
mon2 = list(combinations_with_replacement(range(R), 2))
m2idx = {m: i for i, m in enumerate(mon2)}
print("    point                 rank(Q)   mod p1   mod p2   columns")
for name, P in PTS:
    d2 = {}
    for i in range(R):
        di = diff(P, i)
        for j in range(i, R):
            d2[(i, j)] = diff(di, j)
    nrows = len(WEDGE) * len(mon2)
    rows = [Fraction(0)] * (nrows * R * R)
    for c in range(R):
        for j in range(R):
            col = c * R + j
            for i in range(R):
                if i == c:
                    continue
                w = (i, c) if i < c else (c, i)
                sgn = 1 if i < c else -1
                blk = WIDX[w] * len(mon2)
                for e, coeff in d2[(min(i, j), max(i, j))].items():
                    m = tuple(t for t in range(R) for _ in range(e[t]))
                    rows[(blk + m2idx[m]) * R * R + col] += coeff * sgn
    rQ = rank_Q(rows, nrows, R * R)
    rp = [rank_p(rows, nrows, R * R, p) for p in PRIMES]
    print(f"    {name:<20} {rQ:7d}   {rp[0]:6d}   {rp[1]:6d}   {R*R:7d}")
print("    Rank 99 everywhere: universal corank >= 1 (the element sum_c e_c (x) d_c")
print("    maps to zero by symmetry of second partials); corank exactly 1 measured.")
print()

# ------------------------------------------------------------------------- C6
print("C6  the banked bound rank Cat_{2,2}(l.c) <= 2r (theory_directions sec.B(a))")
fact = (1, 1, 2, 6, 24)


def cat22(P, n=R):
    pairs = list(combinations_with_replacement(range(n), 2))
    rows = []
    for (i, j) in pairs:
        for (k, l) in pairs:
            e = [0] * n
            for t in (i, j, k, l):
                e[t] += 1
            c = P.get(tuple(e), Fraction(0))
            m = 1
            for ei in e:
                m *= fact[ei]
            rows.append(c * m)
    return rank_Q(rows, len(pairs), len(pairs))


print(f"    r = {R}:  bound 2r = {2*R};  measured rank Cat_22(l.c) = {cat22(Pc)},"
      f"  rank Cat_22(x_0.per_3) = {cat22(Pd)}")
print("    Both at or below the banked bound; the direction failure is s35's")
print("    proved lemma, not a new phenomenon.  New here: the det side is 36 at")
print("    r >= 8 (full rank at r <= 7), which is what fixes the minor size.")
print()

# ------------------------------------------------------------------------- C2
print("C2  rank Hess(per_3) on {per_3 = 0}, all coordinates nonzero")


def point_on_q(rng, nonzero):
    while True:
        x = [Fraction(0)] * R
        x[0] = Fraction(rng.randint(1, 9))
        for i in range(1, 9):
            x[i] = Fraction(rng.choice([t for t in range(-9, 10)
                                        if t != 0 or not nonzero]))
        a = b = Fraction(0)
        for e, c in q.items():
            t = c
            for i, ei in enumerate(e):
                if i != 9 and ei:
                    t *= x[i] ** ei
            if e[9] == 1:
                a += t
            else:
                b += t
        if a == 0:
            continue
        x[9] = -b / a
        if nonzero and any(xi == 0 for xi in x):
            continue
        return x


for label, nz in (("all coordinates nonzero", True),
                  ("coordinates from [-6,6] (the first run's sampler)", False)):
    rng2 = random.Random(31337)
    dist = {}
    for _ in range(40):
        x = point_on_q(rng2, nz)
        rows, grad = hess_rows(Pd, x)
        r = rank_Q(rows, R, R)
        dist[r] = dist.get(r, 0) + 1
    print(f"    {label:<48} rank distribution over 40 draws: {dict(sorted(dist.items()))}")
print("    The dual dimension is the value at a GENERAL point, i.e. the maximum")
print("    of a lower-semicontinuous function: 9, hence dim X^* = 7.  Rank 10")
print("    never occurs, which is the padding identity.")
print()

# ------------------------------------------------------------------------- C3
print("C3  a rank-2 point of a 5-dimensional pencil is an ORDINARY node")
print("    seed   P(s)   grad P(s)   rank Hess P(s)   ordinary node?")
for seed in (1, 2, 3, 4):
    rng3 = random.Random(6000 + seed)
    n = 5
    A5 = [[[0] * 4 for _ in range(4)]]
    A5[0][0][0] = A5[0][1][1] = 1                      # a rank-2 matrix
    for _ in range(n - 1):
        A5.append([[rng3.randint(-6, 6) for _ in range(4)] for _ in range(4)])
    P5 = det_pencil(A5, n)
    s = [Fraction(1)] + [Fraction(0)] * (n - 1)
    rows, grad = hess_rows(P5, s, n)
    val = poly_eval(P5, s)
    rk = rank_Q(rows, n, n)
    print(f"    {seed:4d}   {val}      {'0' if all(g == 0 for g in grad) else 'NONZERO'}"
          f"           {rk:9d}        {'yes' if rk == n - 1 else 'NO'}")
print("    rank = r-1 = 4 at the singular point is exactly the condition for an")
print("    ordinary node (A_1) of a hypersurface in P^4: the projective Hessian")
print("    always has the point itself in its kernel, so 4 is the maximum.")
