"""Session 16: recovery fit — identify the TRUE quartic functional.

The session-13 slot theorem said V_00 lies in span{u1,u2,D} (3-dim, det^2
GL2-covariants). The X4 engine value (-308,145,600) is inconsistent with
that span given the C/R/T4 values, so the receiving space is larger.

This fits V_00 over the FULL space of bidegree-(2,2) simultaneous
conjugation invariants of a pencil (A,B) in gl3 x gl3 (10 spanning trace
words), using every banked engine datum plus the structural zeros implied
by the displacement-cancellation lemma (infeasible support => value 0).
"""
import sympy as sp
from itertools import product

def E(i, j):
    M = sp.zeros(3, 3); M[i, j] = 1; return M

def invs(A, B):
    t = sp.trace
    return [t(A*A*B*B), t(A*B*A*B),
            t(A*A*B)*t(B), t(A*B*B)*t(A),
            t(A*A)*t(B*B), t(A*B)**2,
            t(A*A)*t(B)**2, t(B*B)*t(A)**2, t(A*B)*t(A)*t(B),
            t(A)**2*t(B)**2]
NAMES = ['tr(AABB)','tr(ABAB)','tr(AAB)tr(B)','tr(ABB)tr(A)','tr(AA)tr(BB)',
         'tr(AB)^2','tr(AA)tr(B)^2','tr(BB)tr(A)^2','tr(AB)tr(A)tr(B)','tr(A)^2tr(B)^2']

W_ID = 108712800
# engine data for sigma = 00, scheme 1 (pencil (A,B), value)
ENGINE = [
    ('C',   (E(2,1), E(1,2)),                  W_ID),
    ('R',   (E(0,0), E(1,1)),                  W_ID),
    ('T4',  (sp.diag(1,1,0), sp.diag(0,1,1)),  W_ID),
    ('Q',   (E(1,0), E(0,1)),                  W_ID),
    ('P',   (E(0,0), E(0,0)),                  0),
    ('X4',  (E(0,0), E(1,2)+E(2,1)),           -308145600),
]

def structural_zeros():
    """single-transvection pairs whose displacement cannot cancel => infeasible."""
    out = []
    for (j1, a1) in product(range(3), repeat=2):
        for (j2, a2) in product(range(3), repeat=2):
            d = [0, 0, 0]
            d[j1] += 1; d[a1] -= 1; d[j2] += 1; d[a2] -= 1
            if any(d):
                out.append(((E(j1, a1), E(j2, a2)), 0))
    return out

def build():
    rows, vals, tags = [], [], []
    for tag, (A, B), v in ENGINE:
        rows.append([sp.expand(x) for x in invs(A, B)]); vals.append(v); tags.append(tag)
    for (A, B), v in structural_zeros():
        rows.append([sp.expand(x) for x in invs(A, B)]); vals.append(v); tags.append('zero')
    return sp.Matrix(rows), sp.Matrix(vals), tags

if __name__ == '__main__':
    M, b, tags = build()
    aug = M.row_join(b)
    print(f"equations {M.rows}, unknowns 10, rank(M) = {M.rank()}, rank(aug) = {aug.rank()}")
    print("consistent:", M.rank() == aug.rank())
    res = M.gauss_jordan_solve(b)
    sol, params = res[0], res[1]
    print("free parameters:", len(params))
    print("\nparticular/general solution:")
    for n, c in zip(NAMES, sol):
        print(f"  {n:>18}: {sp.simplify(c)}")
    # predictions for the pending points, as functions of free params
    PEND = {
      'Xm3 (Psi=-3)': (E(0,2)+E(1,1), E(1,1)+E(2,0)),
      'G':            (E(2,1)+E(0,0), E(1,2)),
      'X4_scaled2':   (E(0,0), 2*(E(1,2)+E(2,1))),
    }
    print("\npredictions from the fit:")
    for k, (A, B) in PEND.items():
        val = sp.expand((sp.Matrix([invs(A, B)]) * sol)[0])
        print(f"  {k:>14}: {sp.simplify(val)}")
