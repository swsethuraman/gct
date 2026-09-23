"""B27-03 run: explicit nonsymmetric actual-padding witness T' and its 65 retained coefficients.

Exact integer arithmetic (sympy Poly over ZZ).  Smoothness certificates are Groebner bases
over GF(p), p = 32003; smoothness over the algebraic closure of GF(p) implies smoothness over
Qbar (HAND lemma in docs/b27_03_report.md, section 3a).  Output: results/b27_03/witness.json.
"""
import json, itertools, sys, time
from sympy import symbols, Poly, ZZ, groebner, Matrix, expand

t0 = time.time()
X = symbols('x1:6')
x1, x2, x3, x4, x5 = X
P = 32003

# ---- the substitution T' (rows z, y11..y33), fixed before any evaluation ----
L = x1 + x2 + x3 + x4 + x5
A = [[x1 + x3,   x2 - x4,   x5 + 2*x1],
     [x3 + x4,   x1 - x5,   x2 + x3],
     [x2 + 2*x5, x4 + x1,   x3 - x2]]

def perm3(M):
    s = 0
    for p in itertools.permutations(range(3)):
        s += M[0][p[0]] * M[1][p[1]] * M[2][p[2]]
    return expand(s)

C = perm3(A)
F = expand(L * C)
Fp = Poly(F, *X, domain=ZZ)
Cp = Poly(C, *X, domain=ZZ)

# T' as a 10x5 integer matrix, rows (z, y11, y12, y13, y21, ..., y33)
rows = [L] + [A[r][c] for r in range(3) for c in range(3)]
T = [[int(Poly(e, *X).coeff_monomial(v)) for v in X] for e in rows]

# ---- nonsymmetry of the block (literal) ----
asym = [(r, c) for r in range(3) for c in range(3) if expand(A[r][c] - A[c][r]) != 0]

def zero_dim_gf(polys, gens):
    G = groebner(polys, *gens, modulus=P, order='grevlex')
    lms = [Poly(g, *gens).monoms(order='grevlex')[0] for g in G.exprs]
    ok = all(any(m[i] > 0 and sum(m) == m[i] for m in lms) for i in range(len(gens)))
    return ok, len(G.exprs)

# ---- smoothness of C in P^4 (common zeros of the five partials only at 0) ----
partials = [Cp.diff(v).as_expr() for v in X]
smooth_C, gbC = zero_dim_gf(partials, X)

# ---- ten coordinate 3-planes: C restricted is a smooth plane cubic ----
planes = []
for keep in itertools.combinations(range(5), 3):
    kill = {X[i]: 0 for i in range(5) if i not in keep}
    Cv = expand(C.subs(kill))
    gens = [X[i] for i in keep]
    pv = [Poly(Cv, *gens).diff(g).as_expr() for g in gens]
    ok, n = zero_dim_gf(pv, gens) if Cv != 0 else (False, 0)
    planes.append({"plane": [f"x{i+1}" for i in keep], "C_restricted": str(Cv), "smooth": ok})

# ---- the 70 quartic coefficients; the 65 retained (max exponent >= 2) ----
def exps4():
    out = []
    for a in itertools.product(range(5), repeat=5):
        if sum(a) == 4:
            out.append(a)
    return sorted(out, reverse=True)          # descending lexicographic (A25-05 convention)
E70 = exps4()
E65 = [a for a in E70 if max(a) >= 2]
K5 = [a for a in E70 if max(a) <= 1]
coef = {a: int(Fp.coeff_monomial(a)) for a in E70}
out = {
    "script": "analysis/b27_03_witness.py",
    "l": str(L),
    "A_prime": [[str(e) for e in row] for row in A],
    "T_prime_10x5_rows_z_y11_to_y33": T,
    "block_asymmetric_positions": asym,
    "l_coefficients_all_nonzero": all(Poly(L, *X).coeff_monomial(v) != 0 for v in X),
    "C": str(C),
    "C_smooth_in_P4_over_GFp_closure": smooth_C, "C_gb_size": gbC, "p": P,
    "ternary_restrictions": planes,
    "all_ternary_restrictions_smooth": all(q["smooth"] for q in planes),
    "E65_order": "descending lexicographic exponent order, max exponent >= 2",
    "pi_PT_65": [[list(a), coef[a]] for a in E65],
    "omitted_K5_coefficients": [[list(a), coef[a]] for a in K5],
    "wall_s": round(time.time() - t0, 2),
}
json.dump(out, open(sys.argv[1], "w"), indent=1)
print({k: out[k] for k in ["block_asymmetric_positions", "l_coefficients_all_nonzero",
       "C_smooth_in_P4_over_GFp_closure", "all_ternary_restrictions_smooth", "wall_s"]})
print("C =", C)
