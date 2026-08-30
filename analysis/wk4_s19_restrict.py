"""Step 5/6: restrict I6 to slabs (I, A, B), extract the bidegree components,
identify the (2,2) part, cross-check at the banked nets.  Exact integers."""
import numpy as np, sympy as sp, sys
sys.path.insert(0,'analysis')
from wk4_s19_fast import all_values, PARTS
from fractions import Fraction

PAT = (1,5)   # a nonvanishing canonical pattern; I6 := this contraction

def I6(T): return all_values(np.array(T, dtype=np.int64))[PAT]

def slabT(A, B, x=1, y=1):
    T = np.zeros((3,3,3), dtype=np.int64)
    T[0] = np.eye(3, dtype=np.int64)
    T[1] = x*np.array(A, dtype=np.int64)
    T[2] = y*np.array(B, dtype=np.int64)
    return T

def bidegree(A, B):
    """exact coefficients c_ab of I6(I, xA, yB) = sum_ab c_ab x^a y^b."""
    XS = list(range(7))
    vals = {(x,y): I6(slabT(A,B,x,y)) for x in XS for y in XS}
    # interpolate in x for each y, then in y
    rows, rhs = [], []
    mons = [(a,b) for a in range(7) for b in range(7) if a+b <= 6]
    for x in XS:
        for y in XS:
            rows.append([x**a * y**b for (a,b) in mons]); rhs.append(vals[(x,y)])
    M = sp.Matrix(rows); v = sp.Matrix(rhs)
    sol = M.solve_least_squares(v) if M.rows != M.cols else M.solve(v)
    # exact solve via the normal equations on an invertible square subsystem
    sol = (M.T*M).solve(M.T*v)
    assert sp.simplify(M*sol - v) == sp.zeros(len(rows),1), "interpolation not exact"
    return {mons[i]: sp.nsimplify(sol[i]) for i in range(len(mons))}

E = lambda i,j: [[1 if (r,c)==(i,j) else 0 for c in range(3)] for r in range(3)]
def diag(*d): return [[d[i] if i==j else 0 for j in range(3)] for i in range(3)]
POINTS = {
  'C ':(E(2,1), E(1,2)), 'R ':(E(0,0), E(1,1)),
  'T4':(diag(1,1,0), diag(0,1,1)), 'Q ':(E(1,0), E(0,1)),
  'X4':(E(0,0), [[0,0,0],[0,0,1],[0,1,0]]), 'P ':(E(0,0), E(0,0)),
}

def psi(A,B):
    A, B = sp.Matrix(A), sp.Matrix(B); t = sp.trace
    u1 = t(A*A)*t(B*B) - t(A*B)**2
    u2 = t(A*A*B*B) - t(A*B*A*B)
    D  = (t(A)*t(B)-t(A*B))**2 - (t(A)**2-t(A*A))*(t(B)**2-t(B*B))
    return sp.expand(2*u1 - 4*u2 - D)

print("=== bidegree support of I6|(I,A,B) ===")
rng = np.random.default_rng(31337)
supp = {}
for trial in range(4):
    A = rng.integers(-3,4,size=(3,3)); B = rng.integers(-3,4,size=(3,3))
    cs = bidegree(A,B)
    for k,v in cs.items():
        if v != 0: supp[k] = supp.get(k,0)+1
print("bidegrees with a nonzero coefficient at >=1 of 4 random pencils:")
print("   ", sorted(supp))

print("\n=== (2,2) component vs Psi ===")
rows = []
for trial in range(40):
    A = rng.integers(-4,5,size=(3,3)); B = rng.integers(-4,5,size=(3,3))
    c22 = bidegree(A,B)[(2,2)]
    p = psi(A,B)
    rows.append((c22, p))
rats = {sp.Rational(c,p) for c,p in rows if p != 0}
print("distinct c22/Psi over 40 random pencils:", rats)
print("zeros of Psi that are not zeros of c22:", [(c,p) for c,p in rows if p==0 and c!=0])

print("\n=== step 6: banked cross-check ===")
print(" point   Psi    c22          c22/Psi")
for k,(A,B) in POINTS.items():
    cs = bidegree(A,B); p = psi(A,B)
    r = sp.Rational(cs[(2,2)], p) if p != 0 else '--'
    print("  %s   %4s  %12s   %s" % (k, p, cs[(2,2)], r))
    print("        full bidegree profile:", {kk:vv for kk,vv in cs.items() if vv != 0})
