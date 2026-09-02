#!/usr/bin/env python3
"""
Session 37, check 4 -- first-order jets of the reducible determinantal
quartics, branch by branch (docs/blindness_slab.md section 4).

For s_1 . c = det(sum s_i A_i) on a compression branch (span(A_2..A_5)
singular), the reachable cubics c form a family of dimension <= 31 < 35
(docs/l5_containment.md, docs/singular_spaces.md).  The lam_5 = 1 sub-slab
sees only the first-order jet in one variable, here s_5:

    jet(c) = ( c|_{s_5 = 0} ,  d c / d s_5 |_{s_5 = 0} )  in  Sym^3 C^4 x Sym^2 C^4  (20 + 10 = 30).

If the reachable c-family maps DOMINANTLY onto the 30-dimensional jet space,
every pad first-order jet is a det first-order jet and D <= 0 holds at every
lam_5 = 1 weight, at every degree.  Jacobian rank of params -> jet(c),
exact over Q (fmpz_mat) and modulo the two house primes, three random points per branch; the
divisibility assertions of analysis/l5contain.py are kept (the branch is
really singular and the deformation stays in it).  rank at a point <= generic
rank; rank 30 at a point proves dominance.
"""
import random, itertools, sys
from flint import nmod_mat, fmpz_mat

P1, P2 = 2147483647, 2147483629
R = 5
BOX = 10**6

def _red(x, P): return x % P if P else x
def pmul(a, b, P):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(e1[k] + e2[k] for k in range(R))
            o[e] = _red(o.get(e, 0) + c1 * c2, P)
    return {e: c for e, c in o.items() if c}
def padd(a, b, P):
    o = dict(a)
    for e, c in b.items(): o[e] = _red(o.get(e, 0) + c, P)
    return {e: c for e, c in o.items() if c}
def cof(M, p, q, P):
    rows = [x for x in range(4) if x != p]; cols = [x for x in range(4) if x != q]
    acc = {}
    for perm in itertools.permutations(range(3)):
        sgn = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if perm[i] > perm[j]: sgn = -sgn
        t = {tuple([0] * R): _red(sgn, P)}
        for i in range(3): t = pmul(t, M[rows[i]][cols[perm[i]]], P)
        acc = padd(acc, t, P)
    s = 1 if (p + q) % 2 == 0 else -1
    return {e: _red(c * s, P) for e, c in acc.items()}
def det4(M, P):
    acc = {}
    for q in range(4):
        acc = padd(acc, pmul(M[0][q], cof(M, 0, q, P), P), P)
    return acc
def div_s1(poly):
    out = {}
    for e, c in poly.items():
        assert e[0] >= 1, "not divisible by s_1"
        out[tuple([e[0] - 1] + list(e[1:]))] = c
    return out

MON3_4 = [e for e in itertools.product(range(4), repeat=4) if sum(e) == 3]   # cubics in s_1..s_4
MON2_4 = [e for e in itertools.product(range(3), repeat=4) if sum(e) == 2]   # quadrics in s_1..s_4
J3 = {e: k for k, e in enumerate(MON3_4)}
J2 = {e: 20 + k for k, e in enumerate(MON2_4)}

def jet_row(G):
    """G a cubic in s_1..s_5 -> its 30-vector (G|_{s5=0}, dG/ds5|_{s5=0})."""
    row = [0] * 30
    for e, c in G.items():
        if e[4] == 0: row[J3[e[:4]]] = c
        elif e[4] == 1: row[J2[e[:4]]] = c
    return row

def branch_rank(freemask, seed, P):
    rnd = random.Random(seed)
    A = [[[rnd.randint(-BOX, BOX) for _ in range(4)] for _ in range(4)]]
    for i in range(4):
        A.append([[rnd.randint(-BOX, BOX) if freemask[p][q] else 0 for q in range(4)] for p in range(4)])
    M = [[{} for _ in range(4)] for _ in range(4)]
    for p in range(4):
        for q in range(4):
            d = {}
            for i in range(5):
                v = _red(A[i][p][q], P)
                if v:
                    e = [0] * R; e[i] = 1; d[tuple(e)] = v
            M[p][q] = d
    div_s1(det4(M, P))                       # branch really singular
    C = [[cof(M, p, q, P) for q in range(4)] for p in range(4)]
    rows = []
    for i in range(5):
        e_i = [0] * R; e_i[i] = 1; e_i = tuple(e_i)
        for p in range(4):
            for q in range(4):
                if i >= 1 and not freemask[p][q]: continue
                derG = div_s1(pmul({e_i: 1}, C[p][q], P))   # deformation stays in branch
                rows.append(jet_row(derG))
    def rk(rows):
        if P: return nmod_mat(len(rows), 30, [x for r in rows for x in r], P).rank()
        return fmpz_mat(len(rows), 30, [x for r in rows for x in r]).rank()   # exact over Z, i.e. over Q
    r_branch = rk(rows)
    # the s_1-shear  s_1 -> s_1 + a s_5  (the only element of the jet-preserving
    # parabolic not already inside the branch's own GL(s_2..s_5)) moves the jet
    # by  a . (0, d c_0 / d s_1):  append that direction.
    G = div_s1(det4(M, P))
    d1 = {}
    for e, c in G.items():
        if e[0] >= 1:
            e2 = (e[0] - 1,) + e[1:]
            d1[e2] = _red(d1.get(e2, 0) + c * e[0], P)
    shear = [0] * 30
    for e, c in d1.items():
        if e[4] == 0: shear[J2[e[:4]]] = c        # dc_0/ds_1 is a quadric in s_1..s_4
    rows.append(shear)
    r_shear = rk(rows)
    return r_branch, r_shear

def mask(zero_rows, zero_cols):
    return [[not (p in zero_rows and q in zero_cols) for q in range(4)] for p in range(4)]

BRANCHES = {
 "k=1 common kernel   (col 4 = 0)          ": mask({0, 1, 2, 3}, {3}),
 "k=2 compression 2->1 (rows 2-4 x cols 3-4)": mask({1, 2, 3}, {2, 3}),
 "k=3 compression 3->2 (rows 3-4 x cols 2-4)": mask({2, 3}, {1, 2, 3}),
 "k=4 common cokernel (row 4 = 0)          ": mask({3}, {0, 1, 2, 3}),
}
if __name__ == "__main__":
    print("target = 30 (all first-order jets (c_0, q)); rank = dim of reachable jets via this branch")
    best = 0
    for name, fm in BRANCHES.items():
        rs = {P: max(branch_rank(fm, s, P) for s in (0, 1, 2)) for P in (P1, P2, 0)}   # 0 = exact over Q
        r, r2 = rs[0]; assert rs[P1] == rs[P2] == rs[0], rs
        best = max(best, r2)
        print("  %s rank %d/30, with the s_1-shear %d/30 %s" % (name, r, r2,
              "  <-- DOMINANT: every pad jet is a det jet" if r2 == 30 else ""))
    print("max over compression branches (with shear):", best, "of 30")
