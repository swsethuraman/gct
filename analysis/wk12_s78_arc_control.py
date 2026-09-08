"""s78 mandatory control: independent reproduction of S2's rank-3 arc.

Independent of results/astra/S2 code. Uses sympy for the symbolic determinant
identity and python-flint for the reduced-matrix rank at both house primes.

The arc (S2 report section 6), coordinates (x,y,z,w,v) = (s1,s2,s3,s4,s5):

    B(s) = [[x+v, w, 0],
            [0,   y+v, v],
            [0,   0,   z+v]]
    M0 = diag(B, 0)  (4x4, common kernel/cokernel e4)
    b = (w,0,0)^T,  c = (x,0,0)^T
    M(t) = [[B, t b],[t c^T, t^2 w]]

Claim: det M(t) = t^2 * (w det B - c^T adj(B) b) = t^2 * v w (y+v)(z+v),
i.e. leading fixed-factor form in W = s5 * s4 * (s2+s5)(s3+s5); reduced rank 3.
"""
import sympy as sp
import json, sys

x, y, z, w, v, t = sp.symbols('x y z w v t')
s = [x, y, z, w, v]  # s1..s5

# ---- 1. Base pencil, and cross-check against the JSON base_pencil matrices ----
B = sp.Matrix([[x+v, w, 0], [0, y+v, v], [0, 0, z+v]])
M0 = sp.zeros(4, 4)
M0[:3, :3] = B

arc = json.load(open('results/astra/S2/intermediate_rank3_arc.json'))
# base_pencil[k] is the 4x4 integer matrix A_{k+1}; M0(s) = sum_k s_k A_k.
A = [sp.Matrix(mat) for mat in arc['base_pencil']]
assert len(A) == 5
M0_from_json = sum((s[k] * A[k] for k in range(5)), sp.zeros(4, 4))
assert sp.simplify(M0_from_json - M0) == sp.zeros(4, 4), "base_pencil != diag(B,0)"

# base span: the 5 coefficient matrices linearly independent (as 16-vectors)
span = sp.Matrix([[A[k][i, j] for i in range(4) for j in range(4)] for k in range(5)])
base_span = span.rank()

# ---- 2. The arc determinant, order by order in t ----
b = sp.Matrix([w, 0, 0])
c = sp.Matrix([x, 0, 0])
M = sp.zeros(4, 4)
M[:3, :3] = B
M[:3, 3] = t * b
M[3, :3] = (t * c).T
M[3, 3] = t**2 * w

detM = sp.expand(M.det())
detM_poly = sp.Poly(detM, t)
coeff = {k: sp.expand(detM_poly.coeff_monomial(t**k)) for k in range(0, 5)}

leading_expected = sp.expand(v * w * (y + v) * (z + v))
g2 = coeff[2]

# block-determinant identity: det M(t) = t^2 (w det B - c^T adj(B) b)
block_form = sp.expand(t**2 * (w * B.det() - (c.T * B.adjugate() * b)[0, 0]))

# ---- 3. Reduced map rank: L_b(c') = c'^T adj(B') b'  in S4/(f S1), f=det B' ----
# B' = B|_{v=0}; b' = (w,0,0). Following report sec 6: rank of the reduced map = 3.
Bp = B.subs(v, 0)
f = sp.expand(Bp.det())            # = xyz (reducible)
bp = sp.Matrix([w, 0, 0])
# c' = (c1,c2,c3), each a linear form in (x,y,z,w); build the map to S4/(f S1).
c1, c2, c3 = sp.symbols('c1 c2 c3')
# We test the specific structural claim: image of c'->c'^T adj(B') b' has dim 3.
# Parametrize c' by its 4 linear coeffs each (x,y,z,w): 12-dim domain.
lin = [x, y, z, w]
cc = []
csyms = []
for name in ('c1', 'c2', 'c3'):
    row = []
    for L in lin:
        sym = sp.symbols(f'{name}_{L}')
        csyms.append(sym); row.append(sym * L)
    cc.append(sum(row))
cprime = sp.Matrix([cc[0], cc[1], cc[2]])
val = sp.expand((cprime.T * Bp.adjugate() * bp)[0, 0])   # in S; reduce mod f*S1 below

# Target S_4 = homogeneous degree-4 forms in (x,y,z,w). Quotient by f*S_1
# with f = xyz, i.e. by the 4 forms {xyz*x, xyz*y, xyz*z, xyz*w}.
# Build a fixed monomial basis of degree-4 forms in x,y,z,w robustly.
gens4 = sp.polys.monomials.itermonomials([x, y, z, w], 4)
mons4 = sorted([m for m in gens4 if sp.total_degree(m) == 4], key=lambda m: sp.Poly(m, x, y, z, w).monoms()[0], reverse=True)
idx4 = {tuple(sp.Poly(m, x, y, z, w).monoms()[0]): i for i, m in enumerate(mons4)}
def vec4(expr):
    expr = sp.expand(expr)
    out = [0] * len(mons4)
    if expr == 0:
        return out
    p = sp.Poly(expr, x, y, z, w)
    for monom, co in zip(p.monoms(), p.coeffs()):
        assert sum(monom) == 4, f"non-degree-4 term {monom} in {expr}"
        out[idx4[tuple(monom)]] = co
    return out
# f*S_1 basis vectors (the quotient relations)
Q = sp.Matrix([vec4(f * L) for L in lin])            # 4 x 35
# domain->target matrix: coefficient of each csym in val (val is csym-linear)
Mmap = sp.Matrix([vec4(val.coeff(sym)) for sym in csyms])  # 12 x 35
# rank in the quotient target = rank([Mmap ; Q]) - rank(Q)
reduced_rank = Mmap.col_join(Q).rank() - Q.rank()

result = {
    "base_span_dimension": int(base_span),
    "detM_t0_is_zero": coeff[0] == 0,
    "detM_t1_is_zero": coeff[1] == 0,
    "leading_form_g2": str(g2),
    "leading_form_expected_s5_s4_s2ps5_s3ps5": str(leading_expected),
    "g2_matches_expected": sp.expand(g2 - leading_expected) == 0,
    "g2_matches_block_identity": sp.expand(detM - block_form) == 0,
    "reduced_map_rank": int(reduced_rank),
    "restricted_det_f": str(f),
}
print(json.dumps(result, indent=2))
assert result["g2_matches_expected"], "leading form mismatch"
assert result["g2_matches_block_identity"], "block identity mismatch"
assert result["detM_t0_is_zero"] and result["detM_t1_is_zero"], "not order 2"
assert result["reduced_map_rank"] == 3, "reduced rank != 3"
assert result["base_span_dimension"] == 5, "base span != 5"

# ---- 4. Two-prime confirmation (house primes) via python-flint ----
import flint
P1, P2 = 2147483647, 2147483629
def rank_mod(rows, p):
    if not rows or not rows[0]:
        return 0
    ctx = flint.fmpz_mod_ctx(p)
    m = flint.fmpz_mod_mat([[int(v) % p for v in r] for r in rows], ctx)
    return m.rank()
stacked_rows = Mmap.tolist() + Q.tolist()
q_rows = Q.tolist()
rr = {}
for p in (P1, P2):
    rr[p] = rank_mod(stacked_rows, p) - rank_mod(q_rows, p)
result["reduced_map_rank_mod_primes"] = {str(p): int(rr[p]) for p in (P1, P2)}
assert rr[P1] == 3 and rr[P2] == 3, "reduced rank != 3 mod a house prime"

import os
os.makedirs('results', exist_ok=True)
json.dump(result, open('results/s78_arc_control.json', 'w'), indent=2)
print("\nALL ARC CONTROL CHECKS PASS (independent of S2 code); both house primes agree.")
print("wrote results/s78_arc_control.json")
