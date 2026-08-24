"""Week 3 session 9, stage 1 — rebuild World B's transport ingredients through
one code path, to validate conventions before applying it to det_3.
z0 = x^2 y + z^3 (cusp), Omega = sigma_3 = {S = 0} (cone, dim 9).
Expect: stab dim 2 (torus (1,-2,0) + unipotent), T_P = g.z0 dim 8,
T = ker dS(z0) dim 9, N = T/T_P 1-dim with COEFFICIENT-weight +6 under (1,-2,0)."""
import itertools
import sympy as sp
from sympy import Rational

x, y, z = sp.symbols('x y z')
V = (x, y, z)
mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
def to_vec(f):
    P = sp.Poly(sp.expand(f), *V)
    vec = [Rational(0)]*10
    for mono, cf in P.terms():
        if cf == 0: continue
        vec[mons.index(mono)] = Rational(cf)
    return sp.Matrix(1, 10, vec)

z0 = x**2*y + z**3
z0v = to_vec(z0)

# --- stabilizer Lie algebra in gl_3: A acts as derivation -sum (A v)_i d/dv_i? use A.f = d/dt f((I+tA)^{-1}x)?
# convention: (A.f)(v) = d/dt|_0 f(v + t A v) (infinitesimal substitution v -> v + tAv).
E = [[sp.zeros(3,3) for _ in range(3)] for _ in range(3)]
def act(A, f):
    subs = {V[i]: V[i] + sum(A[i,j]*V[j] for j in range(3)) for i in range(3)}
    t = sp.Symbol('t')
    g = f.subs({V[i]: V[i] + t*sum(A[i, j]*V[j] for j in range(3)) for i in range(3)})
    return sp.expand(sp.diff(sp.expand(g), t).subs(t, 0))

basisA = []
rows = []
for i in range(3):
    for j in range(3):
        A = sp.zeros(3, 3); A[i, j] = 1
        basisA.append(A)
        rows.append(to_vec(act(A, z0)))
M = sp.Matrix.vstack(*rows)   # 9 x 10, rows = action of E_ij on z0
ns = M.T.nullspace()          # wrong direction; we need left null: combinations of E_ij killing z0
K = M.nullspace()             # combinations c with sum c_ij E_ij . z0 = 0 : M^T? careful:
# rows indexed by (i,j); we want c (9-vector) with c^T M = 0  => nullspace of M^T
KT = M.T.nullspace()
print("stab dim (point):", len(KT), "(expect 2)")

# torus element (1,-2,0) diag: check in stab
D = sp.diag(1, -2, 0)
print("diag(1,-2,0) kills z0:", act(D, z0) == 0)

# tangent to orbit: span of rows of M (+ z0 itself via Euler: included)
TP = M.rank()
print("dim T_P = g.z0:", TP, "(expect 8)")

# S invariant (rebuild quickly, degree 4 weight (4,4,4) killed by raising ops)
c = {m: sp.Symbol('c_%d%d%d' % m) for m in mons}
cand = [combo for combo in itertools.combinations_with_replacement(mons, 4)
        if tuple(sum(m[t] for m in combo) for t in range(3)) == (4, 4, 4)]
coeffs = sp.symbols('u0:%d' % len(cand))
P = sum(u * sp.prod(c[m] for m in combo) for u, combo in zip(coeffs, cand))
def raise_op(P, kind):
    out = 0
    for (i, j, k) in mons:
        if kind == 1 and j >= 1: out += j * c[(i,j,k)] * sp.diff(P, c[(i+1,j-1,k)])
        if kind == 2 and k >= 1: out += k * c[(i,j,k)] * sp.diff(P, c[(i,j+1,k-1)])
    return sp.expand(out)
eqs = []
for kind in (1, 2):
    poly = sp.Poly(raise_op(P, kind), *[c[m] for m in mons])
    eqs += [cf for _, cf in poly.terms()]
sol = list(sp.linsolve(eqs, coeffs))[0]
free = [s for s in sol.free_symbols if s in coeffs]
S = sp.expand(P.subs(dict(zip(coeffs, sol))).subs({free[0]: sp.Integer(24)}))
print("S rebuilt")

# dS at z0: gradient wrt the 10 coefficients, evaluated at z0's coefficients
subs0 = {c[m]: z0v[mons.index(m)] for m in mons}
grad = [sp.simplify(sp.diff(S, c[m]).subs(subs0)) for m in mons]
gv = sp.Matrix(1, 10, grad)
print("dS(z0) nonzero:", any(g != 0 for g in grad))
# T = ker dS : 9-dim subspace of coefficient space... as FORM deformations: directions w with grad.w = 0
Tdirs = sp.Matrix(grad).T.nullspace()   # 10-vectors w
print("dim ker dS:", len(Tdirs), "(expect 9)")

# N = ker dS / T_P: find weight vector spanning the quotient under D-grading
# D-weight of FORM monomial (i,j,k): i - 2j; coefficient function weight is the negative.
# Work with form-direction weights; report both signs at the end.
wt = {m: m[0] - 2*m[1] for m in mons}
# build T_P row space; test each weight-graded piece of ker dS for a vector not in T_P
TPmat = M
import itertools as it
found = None
for w in sorted(set(wt.values())):
    idxs = [k for k, m in enumerate(mons) if wt[m] == w]
    # graded component of ker dS: solve within span of e_idx
    for d in Tdirs:
        # project direction onto this weight component
        proj = sp.zeros(10, 1)
        for k in idxs: proj[k] = d[k]
        if proj == sp.zeros(10, 1): continue
        aug = sp.Matrix.vstack(TPmat, proj.T)
        if aug.rank() > TPmat.rank():
            found = (w, proj)
            print(f"normal direction found at FORM-weight {w}: monomial support",
                  [mons[k] for k in idxs if proj[k] != 0])
            break
    if found: break
w_form, nvec = found
print(f"=> normal FORM-weight {w_form}; COEFFICIENT (function) weight {-w_form}")
print(f"   World B formula divisor 6: match = {abs(w_form) == 6}")
