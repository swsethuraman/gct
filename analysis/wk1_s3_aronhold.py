"""Week 1, session 3 — construct the Aronhold invariant S of ternary cubics from
scratch (exact linear algebra), then the boundary geometry at the cusp point
w0 = x^2 y + z^3 of sigma_3 = {S = 0}.

Cubic: f = sum c[(i,j,k)] x^i y^j z^k over i+j+k = 3 (plain monomial coefficients).
S = the unique (up to scale) degree-4 polynomial in c of torus weight (4,4,4)
killed by the raising operators V1 (y -> y + eps x) and V2 (z -> z + eps y).
Cusp stabilizer torus: h_t = diag(t, t^-2, 1) via f(tx, t^-2 y, z); monomial
x^i y^j z^k has T1-weight i - 2j.
"""
import sympy as sp
import itertools

mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
assert len(mons) == 10
c = {m: sp.Symbol('c_%d%d%d' % m) for m in mons}

# degree-4 monomials in the c's with total weight (4,4,4)
cand = []
for combo in itertools.combinations_with_replacement(mons, 4):
    w = tuple(sum(m[t] for m in combo) for t in range(3))
    if w == (4, 4, 4):
        cand.append(combo)
print("ansatz monomials of weight (4,4,4):", len(cand))

coeffs = sp.symbols('u0:%d' % len(cand))
P = sum(u * sp.prod(c[m] for m in combo) for u, combo in zip(coeffs, cand))

def raise_op(P, kind):
    # kind 1: y -> y + eps x  : (i,j,k) -> (i+1, j-1, k), factor j
    # kind 2: z -> z + eps y  : (i,j,k) -> (i, j+1, k-1), factor k
    out = 0
    for (i, j, k) in mons:
        if kind == 1 and j >= 1:
            out += j * c[(i, j, k)] * sp.diff(P, c[(i+1, j-1, k)])
        if kind == 2 and k >= 1:
            out += k * c[(i, j, k)] * sp.diff(P, c[(i, j+1, k-1)])
    return sp.expand(out)

eqs = []
for kind in (1, 2):
    E = raise_op(P, kind)
    poly = sp.Poly(E, *[c[m] for m in mons])
    for mono, cf in poly.terms():
        eqs.append(cf)
sol = sp.linsolve(eqs, coeffs)
sol = list(sol)[0]
free = [s for s in sol.free_symbols if s in coeffs]
print("solution space dimension:", len(free))
assert len(free) == 1
S = sp.expand(P.subs(dict(zip(coeffs, sol))).subs({free[0]: sp.Integer(24)}))
nterm = len(sp.Poly(S, *[c[m] for m in mons]).terms())
print("Aronhold S constructed:", nterm, "terms")

def ev(S, assign):
    subs = {c[m]: assign.get(m, 0) for m in mons}
    return sp.simplify(S.subs(subs))

fermat = {(3,0,0): 1, (0,3,0): 1, (0,0,3): 1}
triangle = {(1,1,1): 1}
cusp = {(2,1,0): 1, (0,0,3): 1}
import random
random.seed(7)
rnd = {m: random.randint(-3, 3) for m in mons}
print("S(fermat)   =", ev(S, fermat))
print("S(xyz)      =", ev(S, triangle))
print("S(cusp)     =", ev(S, cusp))
print("S(random)   =", ev(S, rnd))

# scale-check the invariance numerically: S(g.f) = det(g)^4 S(f) for a random g
g = sp.Matrix(3, 3, lambda i, j: sp.Rational(random.randint(-2, 2), 1))
while g.det() == 0:
    g = sp.Matrix(3, 3, lambda i, j: sp.Rational(random.randint(-2, 2), 1))
x, y, z = sp.symbols('x y z')
f_rnd = sum(rnd[m] * x**m[0] * y**m[1] * z**m[2] for m in mons)
gx, gy, gz = (g.row(0).dot(sp.Matrix([x,y,z])), g.row(1).dot(sp.Matrix([x,y,z])), g.row(2).dot(sp.Matrix([x,y,z])))
fg = sp.expand(f_rnd.subs({x: gx, y: gy, z: gz}, simultaneous=True))
Pg = sp.Poly(fg, x, y, z)
assign_g = {m: Pg.coeff_monomial(x**m[0]*y**m[1]*z**m[2]) for m in mons}
lhs = ev(S, assign_g); rhs = g.det()**4 * ev(S, rnd)
print("equivariance S(g.f) == det(g)^4 S(f):", sp.simplify(lhs - rhs) == 0)

# ---------- gradient of S at the cusp point ----------
grad = {m: ev(sp.diff(S, c[m]), cusp) for m in mons}
nz = {m: v for m, v in grad.items() if v != 0}
print("\ngrad S at cusp (nonzero components):", nz if nz else "ALL ZERO -> cusp is a SINGULAR point of sigma_3")

# ---------- tangent space of the orbit G.w0 and T1-weights ----------
w0 = cusp
V = sp.Matrix([w0.get(m, 0) for m in mons])
def act_vec(u, v):
    # infinitesimal substitution var_v -> var_v + eps var_u applied to w0; diagonal u==v allowed
    varlist = [x, y, z]
    f0 = sum(w0.get(m, 0) * x**m[0] * y**m[1] * z**m[2] for m in mons)
    eps = sp.Symbol('eps')
    sub = {varlist[v]: varlist[v] + eps*varlist[u]} if u != v else {varlist[v]: (1+eps)*varlist[v]}
    fe = sp.expand(f0.subs(sub, simultaneous=True))
    d = sp.expand(sp.diff(fe, eps).subs(eps, 0))
    Pd = sp.Poly(d, x, y, z)
    return sp.Matrix([Pd.coeff_monomial(x**m[0]*y**m[1]*z**m[2]) for m in mons])

vecs = [act_vec(u, v) for u in range(3) for v in range(3)]
Mspan = sp.Matrix.hstack(*vecs)
rk = Mspan.rank()
print("dim g.w0 =", rk, "(stabilizer dim =", 9 - rk, ")")

def weight_of_index(idx):
    i, j, k = mons[idx]
    return i - 2*j

def weight_dims(basis_matrix):
    # basis_matrix: 10 x r, T1-stable span; return dict weight -> dim
    cols = [basis_matrix.col(t) for t in range(basis_matrix.shape[1])]
    out = {}
    for w in sorted(set(weight_of_index(i) for i in range(10))):
        idxs = [i for i in range(10) if weight_of_index(i) == w]
        proj = sp.Matrix.hstack(*[sp.Matrix([col[i] for i in idxs]) for col in cols]) if cols else sp.zeros(len(idxs), 0)
        out[w] = proj.rank()
    return out

orb_w = weight_dims(Mspan)
print("T1-weight dims of g.w0:", {w: d for w, d in orb_w.items() if d})
if nz:
    # tangent of sigma_3 at cusp = ker(dS); compute its weight dims
    gvec = sp.Matrix([[grad[m] for m in mons]])
    ker = gvec.nullspace()
    K = sp.Matrix.hstack(*ker)
    print("dim ker dS =", K.shape[1])
    ker_w = weight_dims(K)
    print("T1-weight dims of T_w0 sigma_3:", {w: d for w, d in ker_w.items() if d})
    diff = {w: ker_w.get(w, 0) - orb_w.get(w, 0) for w in set(ker_w) | set(orb_w)}
    print("NORMAL weight(s):", {w: d for w, d in diff.items() if d})
else:
    print("(singular case: normal space ill-defined at the naive level; record and stop)")
