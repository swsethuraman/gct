"""s78: EXACT image dimension of the common-kernel component of D5 cap W.

On the common-kernel component each B_k = [[0,r_k^T],[0,C_k]], and the r_k do not
affect det(s5 I4 + sum s_k B_k) = s5 * det(s5 I3 + sum_{k<=4} s_k C_k). So the
component image is rho_ker: M3^4 -> A^34, (C1..C4) |-> the 34 non-leading coeffs
of det(s5 I3 + sum s_k C_k).

EXACT dimension by matching bounds, both rigorous:
  UPPER: rho_ker is invariant under C_k -> g C_k g^{-1}. The centralizer of a
    3x3 tuple always contains the scalar line (dim>=1). Observing centralizer dim
    = 1 at ANY point proves the generic centralizer dim = 1 (1 is the minimum),
    so the generic conjugation orbit has dim 9-1 = 8; orbit is contained in the
    generic fibre, so image <= 36 - 8 = 28.
  LOWER: rank of the 34x36 Jacobian at an integer point is <= generic rank
    (lower-semicontinuity); computing it (even mod a house prime) is a certified
    lower bound on the generic rank = image dim.
If lower = upper the image dimension is pinned EXACTLY.
"""
import json, random
import flint

P1, P2 = 2147483647, 2147483629
NC = 36  # c-vars: index = k*9 + i*3 + j, k=0..3, i,j=0..2

def cid(k, i, j): return k * 9 + i * 3 + j

# ---- multilinear expansion of det(s5 I3 + sum s_k C_k) ----
# entry(i,j) = s5*delta + sum_k s_k c_{k,i,j}; represent polynomials as
# dict{ (svec, cvarset) : int }, svec=(a1..a5), cvarset=sorted tuple of c-ids.
def entry(i, j):
    d = {}
    if i == j:
        d[((0, 0, 0, 0, 1), ())] = 1
    for k in range(4):
        sv = [0, 0, 0, 0, 0]; sv[k] = 1
        d[(tuple(sv), (cid(k, i, j),))] = 1
    return d

def pmul(A, B):
    out = {}
    for (sa, ca), va in A.items():
        for (sb, cb), vb in B.items():
            key = (tuple(sa[t] + sb[t] for t in range(5)), tuple(sorted(ca + cb)))
            out[key] = out.get(key, 0) + va * vb
    return out

from itertools import permutations
det = {}
for perm in permutations(range(3)):
    sign = 1
    for a in range(3):
        for b in range(a + 1, 3):
            if perm[a] > perm[b]: sign = -sign
    prod = {((0, 0, 0, 0, 0), ()): 1}
    for i in range(3):
        prod = pmul(prod, entry(i, perm[i]))
    for key, c in prod.items():
        det[key] = det.get(key, 0) + sign * c

# group by s-monomial; keep the 34 good coords (s5-power < 3, i.e. |a'| in 1..3)
from collections import defaultdict
coords = []   # each is a dict{ cvarset : int }
for (sv, cset), c in det.items():
    if c == 0: continue
    coords_key = sv
# rebuild grouped
byS = defaultdict(dict)
for (sv, cset), c in det.items():
    if c: byS[sv][cset] = byS[sv].get(cset, 0) + c
good = []
for sv, poly in byS.items():
    if sum(sv[:4]) >= 1:   # exclude s5^3 anchor
        good.append({k: v for k, v in poly.items() if v})
assert len(good) == 34, len(good)

# ---- LOWER bound: Jacobian rank at an integer point, mod both house primes ----
rng = random.Random(2024)
Pt = [rng.randint(-5, 5) for _ in range(NC)]
def evalmon(cset):
    r = 1
    for v in cset: r *= Pt[v]
    return r
# Jacobian J[m][v] = d(good[m])/d(c_v) at Pt = sum over monomials containing v of coeff*prod(others)
def jac_rows():
    rows = []
    for poly in good:
        row = [0] * NC
        for cset, coeff in poly.items():
            for v in cset:
                rest = tuple(x for x in cset if x != v)  # multilinear: v appears once
                row[v] += coeff * evalmon(rest)
        rows.append(row)
    return rows
J = jac_rows()
def rank_mod(rows, p):
    ctx = flint.fmpz_mod_ctx(p)
    return flint.fmpz_mod_mat([[int(x) % p for x in r] for r in rows], ctx).rank()
lower = max(rank_mod(J, P1), rank_mod(J, P2))

# ---- UPPER bound: centralizer dim of the tuple at Pt ----
# C_k as integer 3x3 at Pt: C_k[i][j] = Pt[cid(k,i,j)]
Cmats = [[[Pt[cid(k, i, j)] for j in range(3)] for i in range(3)] for k in range(4)]
# unknown Z (3x3, 9 vars z_{ab}); rows from [Z,C_k]_{ij}=0
zrows = []
for k in range(4):
    Ck = Cmats[k]
    for i in range(3):
        for j in range(3):
            # (Z C_k - C_k Z)_{ij} = sum_a Z[i][a] Ck[a][j] - sum_a Ck[i][a] Z[a][j]
            row = [0] * 9
            for a in range(3):
                row[i * 3 + a] += Ck[a][j]
                row[a * 3 + j] -= Ck[i][a]
            zrows.append(row)
cent_rank = max(rank_mod(zrows, P1), rank_mod(zrows, P2))
stab_dim = 9 - cent_rank
orbit_dim = 9 - stab_dim
upper = 36 - orbit_dim

result = dict(
    component="common kernel (=coker by transpose)",
    source_dim=36,
    lower_bound_generic_rank=int(lower),
    generic_stabilizer_dim=int(stab_dim),
    conjugation_orbit_dim=int(orbit_dim),
    upper_bound_image_dim=int(upper),
    exact_image_dim=int(lower) if lower == upper else None,
    primes=[P1, P2],
)
print(json.dumps(result, indent=2))
json.dump(result, open('results/s78_ker_dim.json', 'w'), indent=2)
assert stab_dim == 1, f"stab {stab_dim}"
assert lower == upper == 28, f"lower {lower} upper {upper}"
print("\nker-component image dimension = 28 EXACTLY  (<= 34 required bound).")
