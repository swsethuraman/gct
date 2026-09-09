"""s78: independent EXACT reproduction of S2 Theorem 5.1's image bound <= 29.

S2 report sec 5: every order-two fixed-factor leading form on the integral-cubic
ker/coker locus is s5 times a 3x3 linear determinant (eqn 5.1). The set of 3x3
linear determinants det(L(s)), L a 3x3 matrix of linear forms in 5 variables, is
the image of a 45-dim parameter space under the determinant-preserving group
G = {(P,Q) in GL3 x GL3 : det P det Q = 1}, dim G = 17, acting by L -> P L Q.
S2 claims the generic stabilizer is 1-dimensional (the scalars (aI, a^-1 I)),
so orbits are 16-dim and the image closure has dim <= 45 - 16 = 29.

We verify EXACTLY (not by sampling an image dimension): at a random rational L,
the Lie-algebra stabilizer {(X,Y) in gl3+gl3 : XL + LY = 0, tr X + tr Y = 0}
has dimension exactly 1. This is a finite exact linear-algebra fact; a random L
gives the generic value as a LOWER bound on the true stabilizer only if the map
rank could drop, but stabilizer dim is upper-semicontinuous, so the generic
(minimum) stabilizer dim <= dim at any specific point. We therefore compute at
several random L and take the MINIMUM observed dimension; that minimum is an
upper bound for the generic stabilizer...

CORRECT LOGIC: orbit dim = dim G - dim Stab(L). We want a LOWER bound on the
generic orbit dim to get an UPPER bound on image = param - orbit? No:
image closure dim = dim of generic orbit's parameter-family = 45 - (fibre dim).
The fibre of L -> det(L) that is an ORBIT has dim = orbit dim = 17 - dimStab.
Two L with same determinant need not be in one orbit, but the orbit is contained
in the fibre, so fibre dim >= orbit dim, hence image dim <= 45 - orbit dim
<= 45 - (17 - dimStab). To bound image <= 29 we need orbit dim >= 16, i.e.
dimStab <= 1 GENERICALLY. Generic (=minimum) stabilizer dim is <= dimStab at any
sampled point, so a sample giving dimStab = 1 shows generic dimStab <= 1; and
dimStab >= 1 always (scalars). Hence generic dimStab = 1 EXACTLY, orbit dim = 16,
image dim <= 45 - 16 = 29. This is S2's bound, reproduced.
"""
import sympy as sp, random, json

s = sp.symbols('s1 s2 s3 s4 s5')
rng = random.Random(529)

def random_linear_matrix():
    return sp.Matrix(3, 3, lambda i, j: sum(rng.randint(-3, 3) * sk for sk in s))

def stab_dim(L):
    # unknowns X (3x3), Y (3x3): 18 entries
    Xs = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'X{i}{j}'))
    Ys = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'Y{i}{j}'))
    unknowns = list(Xs) + list(Ys)
    Eq = Xs * L + L * Ys          # 3x3 matrix of linear forms in s, linear in unknowns
    rows = []
    # each entry is a linear form in s1..s5; every s-coefficient must vanish
    for ent in Eq:
        p = sp.Poly(sp.expand(ent), *s)
        for co in p.coeffs():
            rows.append([sp.diff(co, u) for u in unknowns])
    # add trace condition tr X + tr Y = 0
    tr = sum(Xs[i, i] for i in range(3)) + sum(Ys[i, i] for i in range(3))
    rows.append([sp.diff(tr, u) for u in unknowns])
    A = sp.Matrix(rows)
    return len(unknowns) - A.rank()

dims = []
for _ in range(4):
    L = random_linear_matrix()
    while sp.Poly(L.det(), *s).total_degree() < 3:   # ensure det is a genuine cubic
        L = random_linear_matrix()
    dims.append(int(stab_dim(L)))

generic_stab = min(dims)   # upper-semicontinuous: min over samples >= true generic (min) dim
# scalars (aI, -aI... ) always in stabilizer with the trace constraint: (aI, -aI) has
# X L + L Y = aL - aL = 0 and tr = 3a - 3a = 0 -> dim >= 1 always.
result = dict(
    sampled_stabilizer_dims=dims,
    generic_stabilizer_dim=generic_stab,
    group_dim=17, param_dim=45,
    generic_orbit_dim=17 - generic_stab,
    image_dim_upper_bound=45 - (17 - generic_stab),
)
print(json.dumps(result, indent=2))
assert generic_stab == 1, f"expected generic stabilizer dim 1, got {generic_stab}"
assert result["image_dim_upper_bound"] == 29
print("\nS2 Theorem 5.1 bound reproduced EXACTLY: 3x3 linear-determinant image dim <= 29.")
print("(<= 34 required global bound is satisfied on the integral-cubic ker/coker locus.)")
