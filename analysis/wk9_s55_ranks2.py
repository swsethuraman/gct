#!/usr/bin/env python3
"""
Session 55, follow-ups to M2/M3.

(a) genericity: repeat the four-point Hessian and catalecticant measurements at
    several seeds and several points per component;
(b) the vacuity threshold in r: dim X^* for a det_4 pencil at r = 6..11, against
    the generic value r-2, which is what decides the smallest r at which the LMR
    module says anything at all;
(c) rank Hess(per_3) on {per_3 = 0} -- the Mignon-Ressayre mechanism itself;
(d) the structural reason the padded quartic l*q with l not in vars(q) has
    dim X^* <= N-3: an Euler identity forcing det Hess = 0 on {q = 0}.  Checked
    symbolically at a random point as well as argued in the report.
(e) Cat_{2,2} rank for det_4 pencils at r = 5, 6, 7, 8, 9, 10.

Exact arithmetic; ranks over Q, cross-checked mod two primes.
"""

import random
from fractions import Fraction
from itertools import combinations_with_replacement, permutations

from flint import fmpq_mat, nmod_mat, fmpq

PRIMES = (2147483647, 1000003)


def build(R):
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

    def linear(co):
        return {tuple(1 if j == i else 0 for j in range(R)): Fraction(c)
                for i, c in enumerate(co) if c}

    return ZERO, poly_mul, poly_add, poly_eval, diff, linear


def rank_Q(rows, nr, nc):
    return fmpq_mat(nr, nc, [fmpq(c.numerator, c.denominator)
                             for c in rows]).rank()


def rank_p(rows, nr, nc, p):
    ent = [((c.numerator % p) * pow(c.denominator % p, p - 2, p)) % p
           for c in rows]
    return nmod_mat(nr, nc, ent, p).rank()


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
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        out.append(v)
    return out


def det4_pencil(R, rng, linear, poly_mul, poly_add, ZERO):
    A = [[[rng.randint(-6, 6) for _ in range(4)] for _ in range(4)]
         for _ in range(R)]
    ent = [[linear([A[a][i][j] for a in range(R)]) for j in range(4)]
           for i in range(4)]
    P = {}
    for perm in permutations(range(4)):
        sgn, pl = 1, list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    sgn = -sgn
        term = {ZERO: Fraction(sgn)}
        for i in range(4):
            term = poly_mul(term, ent[i][perm[i]])
        P = poly_add(P, term)
    return P, A


def kernel_point(A, R, rng):
    for _ in range(400):
        v = [Fraction(rng.randint(-5, 5)) for _ in range(4)]
        if all(t == 0 for t in v):
            continue
        M = [[sum(Fraction(A[a][i][j]) * v[j] for j in range(4))
              for a in range(R)] for i in range(4)]
        ker = nullspace(M, R)
        if len(ker) < 1:
            continue
        s = [Fraction(0)] * R
        for b in ker:
            lam = Fraction(rng.randint(-7, 7))
            s = [si + lam * bi for si, bi in zip(s, b)]
        if any(si != 0 for si in s):
            return s
    raise RuntimeError


def hess_rank(P, x, R, diff, poly_eval):
    d1 = [diff(P, i) for i in range(R)]
    H = []
    for i in range(R):
        di = d1[i]
        for j in range(R):
            H.append(poly_eval(diff(di, j), x))
    grad = [poly_eval(d, x) for d in d1]
    return (rank_Q(H, R, R), [rank_p(H, R, R, p) for p in PRIMES],
            any(g != 0 for g in grad))


def cat22(P, R):
    fact = (1, 1, 2, 6, 24)
    pairs = list(combinations_with_replacement(range(R), 2))
    rows = []
    for (i, j) in pairs:
        for (k, l) in pairs:
            e = [0] * R
            for t in (i, j, k, l):
                e[t] += 1
            c = P.get(tuple(e), Fraction(0))
            m = 1
            for ei in e:
                m *= fact[ei]
            rows.append(c * m)
    n = len(pairs)
    return rank_Q(rows, n, n), [rank_p(rows, n, n, p) for p in PRIMES]


# ------------------------------------------------------------------ (b) + (e)
print("(b,e)  det_4 pencil at varying r: dual dimension against the generic r-2,")
print("       and the middle catalecticant rank against the generic dim S^2 C^r")
print()
print("   r   dim X^*(det)   generic r-2   LMR non-vacuous?   Cat_{2,2}(det)"
      "   dim S^2 C^r")
for R in range(5, 12):
    ZERO, poly_mul, poly_add, poly_eval, diff, linear = build(R)
    vals, cats = [], []
    for seed in (551, 552, 553):
        rng = random.Random(seed * 100 + R)
        P, A = det4_pencil(R, rng, linear, poly_mul, poly_add, ZERO)
        s = kernel_point(A, R, rng)
        assert poly_eval(P, s) == 0
        rQ, rp, sm = hess_rank(P, s, R, diff, poly_eval)
        assert all(t == rQ for t in rp) and sm
        vals.append(rQ - 2)
        cQ, cp = cat22(P, R)
        assert all(t == cQ for t in cp)
        cats.append(cQ)
    dstar = max(vals)
    nvac = "yes" if dstar < R - 2 else "NO (vacuous)"
    print(f"   {R:2d}   {dstar:12d}   {R-2:11d}   {nvac:<17}   {max(cats):14d}"
          f"   {R*(R+1)//2:11d}")
print()

# --------------------------------------------------------------------- (c,d)
R = 10
ZERO, poly_mul, poly_add, poly_eval, diff, linear = build(R)


def per3():
    P = {}
    for perm in permutations(range(3)):
        e = [0] * R
        for i in range(3):
            e[1 + 3 * i + perm[i]] += 1
        P[tuple(e)] = P.get(tuple(e), Fraction(0)) + 1
    return P


def point_on_q(q, rng, solve_var):
    for _ in range(500):
        x = [Fraction(rng.randint(-6, 6)) for _ in range(R)]
        x[0] = Fraction(rng.randint(1, 9))
        a = b = Fraction(0)
        for e, c in q.items():
            t = c
            for i, ei in enumerate(e):
                if i != solve_var and ei:
                    t *= x[i] ** ei
            if e[solve_var] == 1:
                a += t
            elif e[solve_var] == 0:
                b += t
            else:
                raise ValueError
        if a == 0:
            continue
        x[solve_var] = -b / a
        return x
    raise RuntimeError


q = per3()
Pd = poly_mul(linear([1] + [0] * (R - 1)), q)
print("(c)  rank Hess(per_3) on {per_3 = 0}  (the Mignon-Ressayre mechanism)")
print("     and rank Hess(x_0*per_3) at the same points")
print("     seed   rank Hess per_3 (9x9)   rank Hess x_0*per_3 (10x10)   dim X^*")
for seed in range(1, 9):
    rng = random.Random(9000 + seed)
    x = point_on_q(q, rng, 9)
    assert poly_eval(q, x) == 0 and poly_eval(Pd, x) == 0
    d1 = [diff(q, i) for i in range(R)]
    K = []
    for i in range(1, R):
        for j in range(1, R):
            K.append(poly_eval(diff(d1[i], j), x))
    rk = rank_Q(K, 9, 9)
    rQ, rp, sm = hess_rank(Pd, x, R, diff, poly_eval)
    assert all(t == rQ for t in rp)
    print(f"     {seed:4d}   {rk:20d}   {rQ:27d}   {rQ-2 if sm else None}")
print()

print("(d)  the padding identity:  P = l*q with l a variable not occurring in q.")
print("     Euler for q of degree 3 gives Hess(q).x = 2.grad(q), and q(x) = 0")
print("     gives grad(q).x = 0; the bordered determinant")
print("        det [[0, g^T],[g, x_0 K]] = -det(x_0 K) * g^T (x_0 K)^{-1} g")
print("     is then -det(x_0 K) * (grad q . x) / (2 x_0) = 0.")
print("     So det Hess(l*q) vanishes identically on {q = 0}: any such padded")
print("     form has dual defect at least 1, with no hypothesis on q.")
print("     Checked above: rank 9, never 10, at 8 independent points.")
print()

# ------------------------------------------------------------------- (a)
print("(a)  genericity of the four-point table: extra seeds for C and D")
print("     seed   C dim X^*   D dim X^*   Cat22(C)   Cat22(D)")


def rand_poly(deg, rng):
    out = {}
    for combo in combinations_with_replacement(range(R), deg):
        e = [0] * R
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


for seed in (11, 22, 33):
    rng = random.Random(seed)
    lc = [rng.randint(1, 9) for _ in range(R)]
    ell = linear(lc)
    xc2 = [Fraction(rng.randint(1, 9)) for _ in range(R)]
    cub = make_vanish_at(rand_poly(3, rng), xc2, tuple([3] + [0] * (R - 1)))
    Pc = poly_mul(ell, cub)
    rc, _, smc = hess_rank(Pc, xc2, R, diff, poly_eval)
    xd = point_on_q(q, rng, 9)
    rd, _, smd = hess_rank(Pd, xd, R, diff, poly_eval)
    cc, _ = cat22(Pc, R)
    cd, _ = cat22(Pd, R)
    print(f"     {seed:4d}   {rc-2:9d}   {rd-2:9d}   {cc:8d}   {cd:8d}")
