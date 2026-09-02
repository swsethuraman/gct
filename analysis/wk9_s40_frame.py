#!/usr/bin/env python3
"""
Session 40, check 3 -- the six nodes of a determinantal cubic threefold are a
frame (six points of P^4 in linearly general position), and cubics singular
at the standard frame form a P^4.  Exact over Q throughout.

Construction of a pencil with all six nodes rational: choose five random
integer rank-one matrices p_i = u_i v_i^T (i = 1..5); their span L is a
generic 5-plane of M_3 (the map {5 Segre points} -> Gr(5, 9) is dominant,
both sides of dimension 20), and L meets the Segre in a sixth point, rational
because the other five are.  The sixth point is found as the extra solution
of the nine 2x2 minors on L (sympy Groebner over Q), verified exactly.

Frame test: the 6 x 5 coordinate matrix of the nodes (in the s-coordinates
of L) has all six 5x5 minors nonzero.  An open condition, so one exact
witness proves it for the generic pencil.

Also: rank of the 30 linear conditions "singular at e_1..e_5, e_1+..+e_5"
on the 35 coefficients of a quinary cubic (expect 30 -> a P^4 of cubics).
"""
import random, sys, itertools
import sympy as sp

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260902
rnd = random.Random(SEED)

def rank1(rnd):
    u = [rnd.randint(-5, 5) for _ in range(3)]
    v = [rnd.randint(-5, 5) for _ in range(3)]
    return sp.Matrix(3, 3, lambda i, j: u[i] * v[j])

# ---- (1) five rank-one matrices, their span, the sixth Segre point
while True:
    P = [rank1(rnd) for _ in range(5)]
    span = sp.Matrix([[m[i, j] for i in range(3) for j in range(3)] for m in P])
    if span.rank() == 5: break
t = sp.symbols('t1:6')
M = sum((t[i] * P[i] for i in range(5)), sp.zeros(3, 3))
minors = [sp.expand(M[a, b] * M[c, d] - M[a, d] * M[c, b])
          for (a, c) in itertools.combinations(range(3), 2)
          for (b, d) in itertools.combinations(range(3), 2)]
# dehomogenise on the chart t5 = 1 (the five known points e_1..e_4 have t5 = 0
# and e_5 has t5 = 1; the sixth point generically has t5 != 0)
eqs = [m.subs(t[4], 1) for m in minors]
G = sp.groebner(eqs, *t[:4], order='lex', domain='QQ')
print("Groebner basis (lex, chart t5=1):", len(G.exprs), "elements")
sols = sp.solve(list(G.exprs), t[:4], dict=True)
print("affine solutions on the chart:", sols)
pts = []
for s in sols:
    v = [sp.sympify(s.get(ti, ti)) for ti in t[:4]] + [sp.Integer(1)]
    assert all(x.is_rational for x in v), v
    pts.append([sp.Rational(x) for x in v])
# add the points e_1..e_4 (t5 = 0) which the chart misses
for i in range(4):
    pts.append([sp.Integer(1 if j == i else 0) for j in range(5)])
assert len(pts) == 6, ("expected six points", len(pts))
# exact verification: every point gives a rank-one matrix
for pt in pts:
    Mp = sum((pt[i] * P[i] for i in range(5)), sp.zeros(3, 3))
    assert Mp.rank() == 1, ("not rank one", pt)
print("six rank-one points on L, exact:")
for pt in pts: print("   ", pt)
# ---- (2) the frame test
C = sp.Matrix(pts)          # 6 x 5
dets = [C.extract(list(rows), list(range(5))).det() for rows in itertools.combinations(range(6), 5)]
print("the six 5x5 minors of the node matrix:", dets)
assert all(d != 0 for d in dets)
print("FRAME: every five of the six nodes span P^4 (exact over Q)")
# ---- (3) cubics singular at the standard frame
x = sp.symbols('x1:6')
E3 = [e for e in itertools.product(range(4), repeat=5) if sum(e) == 3]
coef = sp.symbols('c0:%d' % len(E3))
F = sum(coef[k] * sp.prod([x[i] ** e[i] for i in range(5)]) for k, e in enumerate(E3))
frame = [[1 if j == i else 0 for j in range(5)] for i in range(5)] + [[1] * 5]
conds = []
for pt in frame:
    for j in range(5):
        conds.append(sp.diff(F, x[j]).subs(dict(zip(x, pt))))
A = sp.Matrix([[sp.diff(c, ck) for ck in coef] for c in conds])
print("rank of the 30 node conditions at the standard frame on quinary cubics:", A.rank(), "of 30; cubics singular at the frame form a P^%d" % (35 - A.rank() - 1))
assert A.rank() == 30
