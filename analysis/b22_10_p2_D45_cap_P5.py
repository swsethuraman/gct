"""B22-10 pilot 2 — is D45 ∩ P5 = {l·C : C ∈ D35}?  And the n = 3 cap-minor clause of Lemma 1.6.
Imports no project code.  Exact integer polynomial arithmetic in five variables.

  E1. The (2,1)-compression template
        A = [[a11 a12 a13 a14], [l 0 D11 D12], [0 l D21 D22], [0 0 D31 D32]]   (all entries linear)
      has det A = l · C with C = D32·Q1 − D31·Q2, Q1 = −a11 D11 − a12 D21 + l a13,
      Q2 = −a11 D12 − a12 D22 + l a14: a cubic containing the plane {D31 = D32 = 0}.  Checked
      as a polynomial identity at a random integer point.
  E2. Dimensions, certified in the safe direction.
      - lower bound: rank of the Jacobian of the template family (55 parameters -> 70 coefficients)
        at a random point, mod p (a modular rank is a floor on the rank over Q, and the rank at one
        point is a floor on the dimension of the image);
      - upper bound for {l·det_3 M}: the 18-dimensional group {(s, g, h) : s det g det h = 1} acts
        on (l, M) preserving l·det M; the rank of its infinitesimal action at one point is a floor on
        the generic orbit dimension, so dim{l·C : C ∈ D35} <= 50 − that rank;
      - the matching lower bound, and sanity ranks for D45 (50) and P5 (39).
  E3. rank M_4(C) (the 70 x 75 degree-4 Macaulay matrix of the five partials of a quinary cubic),
      EXACT over Q (fraction-free elimination): a random point of D35, a random cubic through a
      plane, a random cubic.  MEASURED at single points.
"""
import json
import random
import sys
from itertools import combinations_with_replacement, permutations
from pathlib import Path

NV = 5
p_mod = 2147483647
rng = random.Random(20260918)
out = {"pilot": "b22_10_p2_D45_cap_P5", "seed": 20260918, "modulus_for_floors": p_mod}


def mono(d):
    res = []
    for c in combinations_with_replacement(range(NV), d):
        e = [0] * NV
        for i in c:
            e[i] += 1
        res.append(tuple(e))
    return res


M2, M3, M4 = mono(2), mono(3), mono(4)


def lin(v):
    return {tuple(1 if j == i else 0 for j in range(NV)): v[i] for i in range(NV) if v[i]}


def add(p, q, s=1):
    r = dict(p)
    for e, v in q.items():
        r[e] = r.get(e, 0) + s * v
        if r[e] == 0:
            del r[e]
    return r


def mul(p, q):
    r = {}
    for e1, v1 in p.items():
        for e2, v2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            r[e] = r.get(e, 0) + v1 * v2
    return {e: v for e, v in r.items() if v}


def sgn(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s


def det(Mx):
    n = len(Mx)
    tot = {}
    for perm in permutations(range(n)):
        t = {tuple([0] * NV): sgn(perm)}
        for i in range(n):
            t = mul(t, Mx[i][perm[i]])
            if not t:
                break
        tot = add(tot, t)
    return tot


def minor(Mx, i, j):
    return [[Mx[a][b] for b in range(len(Mx)) if b != j] for a in range(len(Mx)) if a != i]


def cof(Mx, i, j):
    d = det(minor(Mx, i, j))
    return d if (i + j) % 2 == 0 else {e: -v for e, v in d.items()}


def rvec():
    return [rng.randint(-3, 3) for _ in range(NV)]


def rlin():
    v = rvec()
    while not any(v):
        v = rvec()
    return lin(v)


def coeffs(p, basis):
    return [p.get(e, 0) for e in basis]


def xk(k):
    return lin([1 if j == k else 0 for j in range(NV)])


def rank_mod(rows, pm=p_mod):
    A = [[x % pm for x in r] for r in rows]
    rk = 0
    ncol = len(A[0]) if A else 0
    for col in range(ncol):
        piv = next((i for i in range(rk, len(A)) if A[i][col]), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = pow(A[rk][col], pm - 2, pm)
        for i in range(rk + 1, len(A)):
            if A[i][col]:
                f = A[i][col] * inv % pm
                A[i] = [(x - f * y) % pm for x, y in zip(A[i], A[rk])]
        rk += 1
    return rk


def rank_exact(rows):
    """Exact rank over Q by fraction-free (Bareiss) elimination."""
    A = [list(r) for r in rows]
    m, n = len(A), len(A[0])
    rk, prev = 0, 1
    for col in range(n):
        piv = next((i for i in range(rk, m) if A[i][col]), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for i in range(rk + 1, m):
            A[i] = [(A[rk][col] * A[i][j] - A[i][col] * A[rk][j]) // prev for j in range(n)]
        prev = A[rk][col]
        rk += 1
        if rk == m:
            break
    return rk


# ------------------------------------------------------------------ E1: the template identity
ZERO = {}
l = rlin()
a = [rlin() for _ in range(4)]
Dm = [[rlin(), rlin()] for _ in range(3)]
A = [[a[0], a[1], a[2], a[3]],
     [l, ZERO, Dm[0][0], Dm[0][1]],
     [ZERO, l, Dm[1][0], Dm[1][1]],
     [ZERO, ZERO, Dm[2][0], Dm[2][1]]]
detA = det(A)
neg = lambda p: {e: -v for e, v in p.items()}
Q1 = add(add(neg(mul(a[0], Dm[0][0])), neg(mul(a[1], Dm[1][0]))), mul(l, a[2]))
Q2 = add(add(neg(mul(a[0], Dm[0][1])), neg(mul(a[1], Dm[1][1]))), mul(l, a[3]))
C = add(mul(Dm[2][1], Q1), neg(mul(Dm[2][0], Q2)))
out["E1"] = {"detA_equals_l_times_C": detA == mul(l, C), "detA_nonzero": bool(detA),
             "C_nonzero": bool(C), "C_is_D32*Q1 - D31*Q2 (in the ideal of the plane D31 = D32 = 0)": True}

# ------------------------------------------------------------------ E2: dimensions
# template family: free entries are a11..a14, D (6), and l (tied in two entries)
cols = []
for (i, j) in [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]:
    cf = cof(A, i, j)
    for k in range(NV):
        cols.append(coeffs(mul(xk(k), cf), M4))
cl = add(cof(A, 1, 0), cof(A, 2, 1))
for k in range(NV):
    cols.append(coeffs(mul(xk(k), cl), M4))
jt = [list(r) for r in zip(*cols)]                                   # 70 x 55
rank_template = rank_mod(jt)

# {l · det_3 M}: parameters (l, M), 5 + 45
l2 = rlin()
M = [[rlin() for _ in range(3)] for _ in range(3)]
dM = det(M)
cols = [coeffs(mul(xk(k), dM), M4) for k in range(NV)]
for i in range(3):
    for j in range(3):
        cf = mul(l2, cof(M, i, j))
        for k in range(NV):
            cols.append(coeffs(mul(xk(k), cf), M4))
rank_D35fam = rank_mod([list(r) for r in zip(*cols)])


# infinitesimal action of {(s, g, h): s det g det h = 1} at (l2, M): tangent (s l, X M + M Y),
# s + tr X + tr Y = 0; coordinates of (l, M) as 50 numbers (the linear forms' coefficients)
def lin_vec(p):
    return [p.get(tuple(1 if j == k else 0 for j in range(NV)), 0) for k in range(NV)]


Mv = [[lin_vec(M[i][j]) for j in range(3)] for i in range(3)]
lv = lin_vec(l2)
gens = []
for which in ("X", "Y"):
    for u in range(3):
        for v in range(3):
            E = [[1 if (r, c) == (u, v) else 0 for c in range(3)] for r in range(3)]
            dMv = [[[0] * NV for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for t in range(3):
                        if which == "X" and E[i][t]:
                            dMv[i][j] = [x + E[i][t] * y for x, y in zip(dMv[i][j], Mv[t][j])]
                        if which == "Y" and E[t][j]:
                            dMv[i][j] = [x + E[t][j] * y for x, y in zip(dMv[i][j], Mv[i][t])]
            s = -1 if u == v else 0                                   # keep s + tr X + tr Y = 0
            gens.append([s * x for x in lv] + [x for i in range(3) for j in range(3) for x in dMv[i][j]])
orbit_rank = rank_mod(gens)

# sanity: D45 and P5 dimensions by the same machinery
As = [[[rvec() for _ in range(4)] for _ in range(4)] for _ in range(1)][0]
Ax = [[lin(As[i][j]) for j in range(4)] for i in range(4)]            # not used below
Ai = [[[rng.randint(-3, 3) for _ in range(4)] for _ in range(4)] for _ in range(NV)]
Apen = [[{tuple(1 if t == k else 0 for t in range(NV)): Ai[k][i][j] for k in range(NV) if Ai[k][i][j]}
         for j in range(4)] for i in range(4)]
cols = []
for i in range(4):
    for j in range(4):
        cf = cof(Apen, i, j)
        for k in range(NV):
            cols.append(coeffs(mul(xk(k), cf), M4))
rank_D45 = rank_mod([list(r) for r in zip(*cols)])
l3 = rlin()
C3 = {e: rng.randint(-3, 3) for e in M3}
cols = [coeffs(mul(xk(k), C3), M4) for k in range(NV)] + [coeffs(mul(l3, {e: 1}), M4) for e in M3]
rank_P5 = rank_mod([list(r) for r in zip(*cols)])

out["E2"] = {
    "template_family_jacobian_rank_floor": rank_template,
    "D35_family_jacobian_rank_floor": rank_D35fam,
    "D35_family_orbit_rank_floor": orbit_rank,
    "D35_family_dimension_upper_bound": 50 - orbit_rank,
    "D35_family_dimension_exact": rank_D35fam if rank_D35fam == 50 - orbit_rank else None,
    "sanity_D45_rank": rank_D45, "sanity_P5_rank": rank_P5,
    "template_family_strictly_larger": rank_template > 50 - orbit_rank,
}


# ------------------------------------------------------------------ E3: rank M_4(C), exact
def partial(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + v * e[i]
    return r


def macaulay4(C):
    parts = [partial(C, i) for i in range(NV)]
    cols = [coeffs(mul(parts[i], {m: 1}), M4) for i in range(NV) for m in M2]
    return [list(r) for r in zip(*cols)]                             # 70 x 75


Mr = [[rlin() for _ in range(3)] for _ in range(3)]
C_det = det(Mr)
L1, L2 = rlin(), rlin()
Qa = {e: rng.randint(-3, 3) for e in M2}
Qb = {e: rng.randint(-3, 3) for e in M2}
C_plane = add(mul(L1, Qa), neg(mul(L2, Qb)))
C_gen = {e: rng.randint(-3, 3) for e in M3}
out["E3"] = {
    "rank_M4_random_D35_point": rank_exact(macaulay4(C_det)),
    "rank_M4_random_cubic_through_a_plane": rank_exact(macaulay4(C_plane)),
    "rank_M4_random_template_cubic_C": rank_exact(macaulay4(C)),
    "rank_M4_random_cubic": rank_exact(macaulay4(C_gen)),
    "shape": [70, 75],
}
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
