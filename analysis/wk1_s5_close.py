"""Week 1, session 5 — closing computations.
(A) [b=1] law: independent rank verification of C[tangent-developable] in degrees <= 4.
(B) Construct the degree-6 invariant T of ternary cubics (pure-python exact),
    anchors + equivariance, then orbit dimensions of the deeper strata and the
    full stabilizer of the conic+tangent-line cubic.
"""
from fractions import Fraction
from itertools import combinations_with_replacement as cwr
import itertools, random

# ================= (A) tangent-developable image ranks =================
# e_j(u,v,p,q) = coeff of x^{4-j} y^j in (ux+vy)^3 (px+qy), j = 0..4
from math import comb
def eA(j):
    # returns dict monomial->coef, monomial = (beta, gamma) meaning u^{3-?}.. encode fully:
    # store as dict {(a_u, b_v, c_p, d_q): coef}
    out = {}
    if 0 <= j <= 3:
        out[(3-j, j, 1, 0)] = comb(3, j)
    if 1 <= j <= 4:
        out[(4-j, j-1, 0, 1)] = out.get((4-j, j-1, 0, 1), 0) + comb(3, j-1)
    return out

def pmul(P, Q):
    R = {}
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = tuple(a+b for a, b in zip(m1, m2))
            R[m] = R.get(m, 0) + c1*c2
    return R

E = [eA(j) for j in range(5)]
print("(A) tangent-developable image dimensions:")
for d in range(1, 5):
    rows = []
    basis_index = {}
    for combo in cwr(range(5), d):
        P = {(0,0,0,0): 1}
        for j in combo: P = pmul(P, E[j])
        rows.append(P)
        for m in P:
            if m not in basis_index: basis_index[m] = len(basis_index)
    # integer matrix -> rank via Fraction elimination
    M = [[Fraction(0)]*len(basis_index) for _ in rows]
    for i, P in enumerate(rows):
        for m, c in P.items(): M[i][basis_index[m]] = Fraction(c)
    # gaussian elimination
    rank = 0; ncols = len(basis_index)
    rowsm = M
    piv_col = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(rowsm)):
            if rowsm[r][col] != 0: piv = r; break
        if piv is None: continue
        rowsm[rank], rowsm[piv] = rowsm[piv], rowsm[rank]
        pr = rowsm[rank]; pc = pr[col]
        for r in range(len(rowsm)):
            if r != rank and rowsm[r][col] != 0:
                f = rowsm[r][col]/pc
                rowsm[r] = [a - f*b for a, b in zip(rowsm[r], pr)]
        rank += 1
    pred = (d+1)*(3*d+1) - (4*d - 1)
    full = (d+1)*(3*d+1)
    print(f"  delta={d}: rank {rank}, predicted {pred} (= full {full} minus the b=1 summand {4*d-1}):",
          "MATCH" if rank == pred else "MISMATCH")

# ================= (B) degree-6 invariant T =================
mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
midx = {m: i for i, m in enumerate(mons)}

def raise_monomial(mono, kind):
    """mono: sorted tuple of indices into mons (a product of c-vars).
    Returns dict {new_mono: coef} for V_kind, Leibniz over factors."""
    out = {}
    for pos in range(len(mono)):
        (i, j, k) = mons[mono[pos]]
        if kind == 1 and i+1 <= 3 and j >= 1:
            tgt = (i+1, j-1, k); coefsrc = None
        if kind == 1:
            if j >= 1:
                # c_{ijk} appears via derivative of c_{i+1,j-1,k}: the operator is
                # V1 = sum j * c_{ijk} d/dc_{i+1,j-1,k}; acting on a product means:
                # for each factor equal to c_{i+1,j-1,k}, replace it by j*c_{ijk}...
                pass
        # implement properly below
    return out

def apply_V(mono, kind):
    """V = sum_{(i,j,k)} w * c_{ijk} d/dc_{target}. Acting on product 'mono':
    for each factor F = c_{(I,J,K)}, if F is a 'target', replace by w * c_{source}."""
    out = {}
    for pos in range(len(mono)):
        I, J, K = mons[mono[pos]]
        if kind == 1:
            # target = c_{i+1, j-1, k} with source (i,j,k), weight j:
            # so F=(I,J,K) is target iff exists (i,j,k) with i+1=I, j-1=J, k=K -> (I-1, J+1, K), weight J+1
            if I >= 1 and J+1 <= 3:
                src = (I-1, J+1, K); w = J+1
            else: continue
        else:
            # V2: target = c_{i, j+1, k-1}, source (i,j,k), weight k:
            if J >= 1 and K+1 <= 3:
                src = (I, J-1, K+1); w = K+1
            else: continue
        if sum(src) != 3: continue
        new = list(mono); new[pos] = midx[src]; new.sort()
        t = tuple(new)
        out[t] = out.get(t, 0) + w
    return out

def build_invariant(degree, weight):
    cand = []
    for combo in cwr(range(10), degree):
        w = [0, 0, 0]
        for idx in combo:
            for t in range(3): w[t] += mons[idx][t]
        if tuple(w) == weight: cand.append(combo)
    cidx = {m: i for i, m in enumerate(cand)}
    eq_index = {}; triples = []
    for kind in (1, 2):
        for ci, combo in enumerate(cand):
            for tgt, w in apply_V(combo, kind).items():
                key = (kind, tgt)
                if key not in eq_index: eq_index[key] = len(eq_index)
                triples.append((eq_index[key], ci, w))
    nr, nc = len(eq_index), len(cand)
    M = [[Fraction(0)]*nc for _ in range(nr)]
    for r, ccol, w in triples: M[r][ccol] += w
    # nullspace via RREF
    rank = 0; pivots = []
    for col in range(nc):
        piv = None
        for r in range(rank, nr):
            if M[r][col] != 0: piv = r; break
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        pr = M[rank]; pc = pr[col]
        M[rank] = [a/pc for a in pr]; pr = M[rank]
        for r in range(nr):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f*b for a, b in zip(M[r], pr)]
        pivots.append(col); rank += 1
    free = [c for c in range(nc) if c not in pivots]
    if len(free) != 1:
        print("  nullspace dim:", len(free)); assert False
    sol = [Fraction(0)]*nc; sol[free[0]] = Fraction(1)
    for r, col in enumerate(pivots):
        sol[col] = -M[r][free[0]]
    # clear denominators
    from math import gcd
    den = 1
    for v in sol:
        den = den * v.denominator // gcd(den, v.denominator)
    ints = [int(v*den) for v in sol]
    g = 0
    for v in ints: g = gcd(g, abs(v))
    ints = [v//g for v in ints]
    return cand, ints

candT, Tco = build_invariant(6, (6, 6, 6))
print(f"\n(B) T constructed: ansatz {len(candT)} monomials, invariant has {sum(1 for v in Tco if v)} nonzero terms, nullspace dim 1")

def ev_inv(cand, co, assign):
    tot = 0
    for combo, cf in zip(cand, co):
        if cf == 0: continue
        p = cf
        for idx in combo:
            p *= assign.get(mons[idx], 0)
            if p == 0: break
        tot += p
    return tot

fermat  = {(3,0,0): 1, (0,3,0): 1, (0,0,3): 1}
cusp    = {(2,1,0): 1, (0,0,3): 1}
conitan = {(2,1,0): 1, (0,2,1): 1}      # x^2 y + y^2 z
dline   = {(2,1,0): 1}                  # x^2 y
tline   = {(3,0,0): 1}                  # x^3
tri     = {(1,1,1): 1}                  # xyz
for name, a in [("fermat", fermat), ("cusp", cusp), ("conic+tangent", conitan),
                ("x^2y", dline), ("x^3", tline), ("xyz", tri)]:
    print(f"  T({name}) = {ev_inv(candT, Tco, a)}")

# equivariance on a random integer g: T(f o g) == det(g)^6 T(f)
def cubic_from(assign):
    return dict(assign)
def compose_cubic(assign, g):
    # f o g where g is 3x3 integer matrix acting on variables: x_i -> sum_j g[i][j] x_j
    lin = [ {(1 if t==0 else 0, 1 if t==1 else 0, 1 if t==2 else 0): g[t][s] for t in range(3)} for s in range(3) ]
    # careful: we need images of x, y, z as linear forms: x -> sum_t? use substitution v_s -> sum_t g_{s,t} v_t
    def lform(s): return {(1,0,0): g[s][0], (0,1,0): g[s][1], (0,0,1): g[s][2]}
    def mulp(A, B):
        R = {}
        for m1, c1 in A.items():
            for m2, c2 in B.items():
                m = tuple(x+y for x, y in zip(m1, m2))
                R[m] = R.get(m, 0) + c1*c2
        return R
    out = {}
    for (i, j, k), cf in assign.items():
        term = {(0,0,0): cf}
        for _ in range(i): term = mulp(term, lform(0))
        for _ in range(j): term = mulp(term, lform(1))
        for _ in range(k): term = mulp(term, lform(2))
        for m, v in term.items(): out[m] = out.get(m, 0) + v
    return out
random.seed(11)
g = [[random.randint(-2, 2) for _ in range(3)] for _ in range(3)]
det = (g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1]) - g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])
       + g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0]))
while det == 0:
    g = [[random.randint(-2, 2) for _ in range(3)] for _ in range(3)]
    det = (g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1]) - g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])
           + g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0]))
frand = {m: random.randint(-3, 3) for m in mons}
lhs = ev_inv(candT, Tco, compose_cubic(frand, g))
rhs = det**6 * ev_inv(candT, Tco, frand)
print("  equivariance T(f o g) == det^6 T(f):", lhs == rhs)

# ---------- orbit dimensions via Lie algebra ----------
def orbit_dim(assign):
    # D_X f for X = E_{st}: v_s d/dv_t ... build 9 vectors in the 10-dim cubic space
    vecs = []
    for s in range(3):
        for t in range(3):
            out = {}
            for (i, j, k), cf in assign.items():
                e = (i, j, k)
                deg = e[t]
                if deg == 0: continue
                ne = list(e); ne[t] -= 1; ne[s] += 1
                ne = tuple(ne)
                out[ne] = out.get(ne, 0) + deg*cf
            vecs.append([out.get(m, 0) for m in mons])
    # rank
    M = [[Fraction(v) for v in row] for row in vecs]
    rank = 0
    for col in range(10):
        piv = None
        for r in range(rank, 9):
            if M[r][col] != 0: piv = r; break
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        pr = M[rank]; pc = pr[col]
        for r in range(9):
            if r != rank and M[r][col] != 0:
                f = M[r][col]/pc
                M[r] = [a - f*b for a, b in zip(M[r], pr)]
        rank += 1
    return rank
print("\norbit dimensions (cones):")
for name, a in [("fermat", fermat), ("cusp", cusp), ("conic+tangent", conitan),
                ("x^2y", dline), ("x^3", tline)]:
    print(f"  dim G.{name} = {orbit_dim(a)}")

# stabilizer Lie algebra of conic+tangent explicitly
import sympy as sp
X = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'x{i}{j}'))
xs, ys, zs = sp.symbols('x y z')
f1 = xs**2*ys + ys**2*zs
V = [xs, ys, zs]
Df = 0
for s in range(3):
    for t in range(3):
        Df += X[s, t] * V[s] * sp.diff(f1, V[t])
Pol = sp.Poly(sp.expand(Df), xs, ys, zs)
eqs = [cf for cf in Pol.coeffs()]
sol = sp.solve(eqs, list(X), dict=True)[0]
freesyms = sorted({s for v in sol.values() for s in v.free_symbols} |
                  {s for s in X if s not in sol}, key=str)
print("\nconic+tangent stabilizer Lie algebra: dim =", len(freesyms), "free params:", freesyms)
for fs in freesyms:
    Xi = X.subs({k: (1 if v == fs else v.subs(fs, 1).subs([(o, 0) for o in freesyms if o != fs]))
                 for k, v in sol.items()}, simultaneous=True)
    Xi = Xi.subs({fs: 1}).subs([(o, 0) for o in freesyms if o != fs])
    Xi = sp.Matrix(3, 3, lambda i, j: Xi[i, j] if not Xi[i, j].free_symbols else 0)
    print(f"  generator ({fs}):"); sp.pprint(Xi)
    print(f"    trace {sp.trace(Xi)}, nilpotent? {(Xi**3).is_zero_matrix}")
