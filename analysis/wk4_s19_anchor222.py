"""ANCHOR (step 2): does the complete-epsilon-contraction machinery reproduce
Cayley's 2x2x2 hyperdeterminant exactly?

Reference definitions used (two independent ones):
  (Ref A) explicit Cayley polynomial (12 terms, coefficients 1,-2,4);
  (Ref B) Det(T) = discriminant of the binary quadratic det(x*S0 + y*S1),
          S0,S1 the two 2x2 slabs.
Ref A == Ref B is checked symbolically first, so the reference is itself
cross-validated before it is used to judge the machinery.
"""
import sympy as sp, numpy as np, itertools, sys
sys.path.insert(0, 'analysis')
from wk4_s19_eps import contract, all_patterns

# ---------- symbolic references ----------
a = {k: sp.Symbol('a%d%d%d' % k) for k in itertools.product(range(2), repeat=3)}
def A(i,j,k): return a[(i,j,k)]

refA = (A(0,0,0)**2*A(1,1,1)**2 + A(0,0,1)**2*A(1,1,0)**2
      + A(0,1,0)**2*A(1,0,1)**2 + A(0,1,1)**2*A(1,0,0)**2
      - 2*(A(0,0,0)*A(0,0,1)*A(1,1,0)*A(1,1,1) + A(0,0,0)*A(0,1,0)*A(1,0,1)*A(1,1,1)
         + A(0,0,0)*A(0,1,1)*A(1,0,0)*A(1,1,1) + A(0,0,1)*A(0,1,0)*A(1,0,1)*A(1,1,0)
         + A(0,0,1)*A(0,1,1)*A(1,0,0)*A(1,1,0) + A(0,1,0)*A(0,1,1)*A(1,0,0)*A(1,0,1))
      + 4*(A(0,0,0)*A(0,1,1)*A(1,0,1)*A(1,1,0) + A(0,0,1)*A(0,1,0)*A(1,0,0)*A(1,1,1)))

x, y = sp.symbols('x y')
S0 = sp.Matrix(2,2, lambda p,q: A(0,p,q))
S1 = sp.Matrix(2,2, lambda p,q: A(1,p,q))
q = sp.Poly(sp.expand((x*S0 + y*S1).det()), x, y)
c2, c1, c0 = q.coeff_monomial(x**2), q.coeff_monomial(x*y), q.coeff_monomial(y**2)
refB = sp.expand(c1**2 - 4*c0*c2)

print("Ref A == Ref B :", sp.simplify(refA - refB) == 0)

# ---------- the machinery ----------
pats = all_patterns(2)
print("patterns (3^3):", len(pats))

rng = np.random.default_rng(20260830)
TESTS = [rng.integers(-6, 7, size=(2,2,2)).astype(np.int64) for _ in range(30)]
def refval(T):
    sub = {a[k]: int(T[k]) for k in a}
    return int(refA.subs(sub))

rows = np.array([[contract(T, p, 2) for p in pats] for T in TESTS], dtype=object)
rvals = [refval(T) for T in TESTS]

M = sp.Matrix(rows.tolist())
print("rank of the pattern-evaluation matrix (dim of degree-4 invariant span):", M.rank())

# every pattern must be an integer multiple of the reference
ratios = set()
for j, p in enumerate(pats):
    col = [rows[i][j] for i in range(len(TESTS))]
    nz = [(c, r) for c, r in zip(col, rvals) if r != 0]
    if all(c == 0 for c in col):
        ratios.add(sp.Integer(0)); continue
    rs = {sp.Rational(c, r) for c, r in nz}
    assert len(rs) == 1, ("pattern %d not proportional to Cayley" % j, rs)
    ratios.add(rs.pop())
print("distinct pattern/Cayley ratios:", sorted(ratios))

# pick a nonzero pattern and check it symbolically term-by-term
j0 = next(j for j in range(len(pats)) if any(rows[i][j] for i in range(len(TESTS))))
lam = [sp.Rational(rows[i][j0], rvals[i]) for i in range(len(TESTS)) if rvals[i]][0]
print("chosen pattern", pats[j0], "ratio", lam)

# exact symbolic identity on the generic tensor: brute-force the contraction
from wk4_s19_eps import eps
E = eps(2)
def sym_contract(pattern):
    tot = 0
    for idx in itertools.product(range(2), repeat=12):
        # idx[3c+s]
        s = 1
        for slot in range(3):
            for blk in pattern[slot]:
                s = s * E[tuple(idx[3*c+slot] for c in blk)]
                if s == 0: break
            if s == 0: break
        if s == 0: continue
        term = sp.Integer(int(s))
        for c in range(4):
            term *= A(idx[3*c], idx[3*c+1], idx[3*c+2])
        tot += term
    return sp.expand(tot)

sym = sym_contract(pats[j0])
print("SYMBOLIC IDENTITY  contraction == %s * Cayley :" % lam, sp.expand(sym - lam*refA) == 0)

# ---------- anchor evaluations ----------
def T_of(terms):
    T = np.zeros((2,2,2), dtype=np.int64)
    for coef, u, v, w in terms:
        T += coef*np.einsum('i,j,k->ijk', np.array(u), np.array(v), np.array(w))
    return T
def D(T): return sp.Rational(contract(T, pats[j0], 2), lam)

anchors = {
 'rank1 e0(x)e0(x)e0'      : T_of([(1,[1,0],[1,0],[1,0])]),
 'rank1 generic'           : T_of([(1,[2,3],[-1,4],[5,1])]),
 'GHZ e000+e111 (rank2)'   : T_of([(1,[1,0],[1,0],[1,0]),(1,[0,1],[0,1],[0,1])]),
 'rank2 generic'           : T_of([(1,[2,3],[-1,4],[5,1]),(1,[1,-2],[3,1],[1,7])]),
 'W-state (rank3, tangent)': np.array([[[0,1],[1,0]],[[1,0],[0,0]]], dtype=np.int64),
 'zero tensor'             : np.zeros((2,2,2), dtype=np.int64),
}
print("\n--- 2x2x2 anchor table (Det via the contraction machinery) ---")
for k, T in anchors.items():
    print("  %-26s Det = %s" % (k, D(T)))
