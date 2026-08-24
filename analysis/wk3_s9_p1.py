"""Week 3 session 9, stage 2 — transport data for P1 (traceless determinant).
Coordinates x0..x8, z0 = det(M) with entry (2,2) = -x0-x4; x8 dead.
Stabilizer torus (3-dim): conj-diag (a = d0-d1, b = d0-d2) + dead-scaling w8:
  weights W(a,b,w8) = (0, a, b, -a, 0, b-a, -b, a-b, w8)  on (x0..x8).
Pipeline: verify torus in stab; T_P = g.z0 (64); T-hat = image of d(A -> det3 o A)
at the chart matrix A0 (rank? want 65); N = T-hat/T_P: multi-weight (alpha,beta,gamma).
Then: m1 = vanishing order of Phi18 on P1 from 6*Sum(W) = m1*w_N."""
import itertools
import sympy as sp
from sympy import Rational

X = sp.symbols('x0:9')
Y = sp.symbols('y0:9')
det3y = sp.expand(sp.Matrix(3, 3, lambda i, j: Y[3*i+j]).det())

# chart: y_k = x_k (k<=7), y8 = -x0-x4
chart = {Y[k]: X[k] for k in range(8)}
chart[Y[8]] = -X[0]-X[4]
z0 = sp.expand(det3y.subs(chart))

mons165 = list(itertools.combinations_with_replacement(range(9), 3))
mix = {m: i for i, m in enumerate(mons165)}
def to_vec(f):
    P = sp.Poly(sp.expand(f), *X)
    v = [Rational(0)]*165
    for mono, cf in P.terms():
        if cf == 0: continue
        idx = tuple(sorted([i for i in range(9) for _ in range(mono[i])]))
        v[mix[idx]] = Rational(cf)
    return v

def act(Wdiag, f):
    """diagonal torus derivation: sum w_i x_i d/dx_i"""
    return sp.expand(sum(w*X[i]*sp.diff(f, X[i]) for i, w in enumerate(Wdiag)))

a, b, w8 = sp.symbols('a b w8')
Wgen = [0, a, b, -a, 0, b-a, -b, a-b, w8]
res = act(Wgen, z0)
print("torus kills z0 for all (a,b,w8):", sp.simplify(res) == 0)

# T_P = span of E_ij . z0  (E_ij: x_i -> x_i + t x_j derivation: x_j d/dx_i? convention consistent)
rows = []
for i in range(9):
    for j in range(9):
        rows.append(to_vec(sp.expand(X[j]*sp.diff(z0, X[i]))))
TP = sp.Matrix(rows)
rTP = TP.rank()
print("dim T_P = g.z0:", rTP, "(expect 64)")

# T-hat: d/dt det3((A0 + tB) x) = sum_k (d det3/d y_k)(A0 x) * (B x)_k
grad_at = [sp.expand(sp.diff(det3y, Y[k]).subs(chart)) for k in range(9)]
rows2 = []
for k in range(9):
    for j in range(9):
        rows2.append(to_vec(sp.expand(grad_at[k]*X[j])))
TH = sp.Matrix(rows2)
rTH = TH.rank()
print("dim T-hat (parametrization tangent):", rTH, "(want 65)")

# N: weight-graded search for a T-hat direction outside T_P
# grade by (a-deg, b-deg, w8-deg): each monomial has weight alpha*a+beta*b+gamma*w8
wts = {}
for m in mons165:
    wa = sum({1:1, 3:-1, 5:-1, 7:1}.get(v, 0) for v in m)
    wb = sum({2:1, 5:1, 6:-1, 7:-1}.get(v, 0) for v in m)
    w8d = sum(1 for v in m if v == 8)
    wts[m] = (wa, wb, w8d)
# group T-hat generators' spans by weight? monomials of z0-related spaces mix weights;
# instead: find any vector in T-hat not in T_P, then project to weight components
# (T-hat and T_P are torus-stable, so the quotient is spanned by weight vectors).
TPr = TP.rowspace()
THr = TH.rowspace()
TPmat = sp.Matrix([list(r) for r in TPr])
found = []
for r in THr:
    aug = TPmat.col_join(sp.Matrix([list(r)]))
    if aug.rank() > TPmat.rank():
        # decompose r into weight components; find the component outside T_P
        comps = {}
        for idx, val in enumerate(r):
            if val == 0: continue
            w = wts[mons165[idx]]
            comps.setdefault(w, [Rational(0)]*165)[idx] = val
        for w, vec in comps.items():
            aug2 = TPmat.col_join(sp.Matrix([vec]))
            if aug2.rank() > TPmat.rank():
                found.append((w, [mons165[i] for i, v in enumerate(vec) if v != 0]))
        break
for w, support in found:
    print(f"NORMAL weight component: (alpha,beta,gamma) = {w}; support sample: {support[:5]}")
