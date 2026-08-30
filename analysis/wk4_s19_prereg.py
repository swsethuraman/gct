"""Step 5 groundwork (uses NO I6 data): what are the a-priori possible answers?

I6 is a degree-6 SL3^3 invariant, hence a GL3^3 semi-invariant with character
det^2 in each factor (scaling a factor by lambda*I multiplies I6 by lambda^6 =
det(lambda I)^2).  Restricted to slabs (I,A,B), the slab-group equivariance is
exactly session 18's condition  D_A f + 2 tr(A) f = 0  (and A<->B), and that
condition is BIDEGREE-PRESERVING (D_A raises the A-degree by one, as does
tr(A)*f).  Therefore the bidegree-(2,2) component of I6|_(I,A,B) is FORCED to
lie in the 2-dimensional equivariant subspace of the 10-dim bidegree-(2,2)
simultaneous-conjugation space.  This script computes that 2-dim space and a
complement generator X to Psi, so the outcome space can be pre-registered as a
single number: the X-coefficient.
"""
import sympy as sp
from itertools import product

A = sp.Matrix(3,3, lambda i,j: sp.Symbol('a%d%d'%(i,j)))
B = sp.Matrix(3,3, lambda i,j: sp.Symbol('b%d%d'%(i,j)))
t = sp.trace

def basis(A,B):
    return [t(A*A*B*B), t(A*B*A*B),
            t(A*A*B)*t(B), t(A*B*B)*t(A),
            t(A*A)*t(B*B), t(A*B)**2,
            t(A*A)*t(B)**2, t(B*B)*t(A)**2, t(A*B)*t(A)*t(B),
            t(A)**2*t(B)**2]
NAMES = ['tr(AABB)','tr(ABAB)','tr(AAB)tr(B)','tr(ABB)tr(A)','tr(AA)tr(BB)',
         'tr(AB)^2','tr(AA)tr(B)^2','tr(BB)tr(A)^2','tr(AB)tr(A)tr(B)','tr(A)^2tr(B)^2']
BAS = [sp.expand(x) for x in basis(A,B)]

def deriv(f, dA, dB):
    s = 0
    for i,j in product(range(3),repeat=2):
        s += sp.diff(f, A[i,j])*dA[i,j] + sp.diff(f, B[i,j])*dB[i,j]
    return sp.expand(s)

c = sp.symbols('c0:10')
f = sum(ci*bi for ci,bi in zip(c, BAS))
eqs = []
for (dA,dB,tr_) in [(-A*A, -A*B, t(A)), (-B*A, -B*B, t(B))]:
    E = sp.expand(deriv(f, dA, dB) + 2*tr_*f)
    P = sp.Poly(E, *[A[i,j] for i,j in product(range(3),repeat=2)],
                   *[B[i,j] for i,j in product(range(3),repeat=2)])
    eqs += [sp.expand(co) for co in P.coeffs()]
sol = sp.linsolve(eqs, c)
print("equivariance solution set:", sol)
Msys, _ = sp.linear_eq_to_matrix(eqs, c)
ns = Msys.nullspace()
print("dim of equivariant subspace of the 10-dim (2,2) space:", len(ns))
for v in ns: print("   ", [sp.nsimplify(x) for x in v.T])

# Psi = 2 u1 - 4 u2 - D in the same basis
u1 = t(A*A)*t(B*B) - t(A*B)**2
u2 = t(A*A*B*B) - t(A*B*A*B)
D  = (t(A)*t(B)-t(A*B))**2 - (t(A)**2-t(A*A))*(t(B)**2-t(B*B))
PSI = sp.expand(2*u1 - 4*u2 - D)
coef, _ = sp.linear_eq_to_matrix([sp.expand(PSI - sum(ci*bi for ci,bi in zip(c,BAS)))], c)
# solve for the coordinates of PSI directly
vs = sp.symbols('v0:10')
sysm = sp.Matrix([sp.expand(PSI - sum(vi*bi for vi,bi in zip(vs,BAS)))])
Mm, bb = sp.linear_eq_to_matrix(
    sp.Poly(sp.expand(PSI - sum(vi*bi for vi,bi in zip(vs,BAS))),
            *[A[i,j] for i,j in product(range(3),repeat=2)],
            *[B[i,j] for i,j in product(range(3),repeat=2)]).coeffs(), vs)
psic = sp.Matrix(list(sp.linsolve((Mm, bb), vs))[0])
print("\nPsi coordinates:", [sp.nsimplify(x) for x in psic.T], "  (doc says (-4,4,0,0,3,-3,-1,-1,2,0))")

N = sp.Matrix.hstack(*ns)
lam = N.solve_least_squares(psic) if N.rows != N.cols else None
# exact: solve N * z = psic
z = sp.linsolve((N, psic), sp.symbols('z0:%d'%len(ns)))
print("Psi lies in the equivariant space:", z)
# complement generator X: any nullspace vector independent of Psi
Xv = None
for v in ns:
    if sp.Matrix.hstack(psic, v).rank() == 2: Xv = v; break
print("complement generator X =", [sp.nsimplify(x) for x in Xv.T])
print("     X in words:", " + ".join("%s*%s"%(sp.nsimplify(Xv[i]), NAMES[i]) for i in range(10) if Xv[i]!=0))
sp.pprint(sp.factor(sp.expand(sum(Xv[i]*BAS[i] for i in range(10)))))
import pickle
pickle.dump({'psic':psic, 'ns':[list(v) for v in ns], 'X':list(Xv)}, open('/home/claude/prereg.pkl','wb'))
