"""s78: build the reduced (A5=I) system with a FAST dict-based determinant.

det(s5 I + sum_{k<=4} s_k B_k) = sum_a (s-monomial a) * (poly in 64 b-vars).
Group by the s-exponent a=(a1..a5):
  a5==4 (a'=0): anchor, coeff 1
  1<=|a'|<=3 : the 34 GOOD coords (coeffs of P1,P2,P3)
  a5==0      : the 35 W conditions (coeffs of P4 = det of the 4-pencil)

We expand det by Leibniz over the 4x4 matrix whose (i,j) entry is the sparse
poly  s5*delta_ij + sum_k s_k b_{k,i,j}  (<=5 terms). Polynomials are dicts
{ (svec, bkey) : int } where svec=(a1..a5) and bkey=sorted tuple of b-var ids.
"""
import json
from itertools import permutations

# b-vars: id = k*16 + i*4 + j, k=0..3, i,j=0..3  (64 total)
def bid(k, i, j): return k * 16 + i * 4 + j
BNAMES = [f'b{k}_{i}_{j}' for k in range(4) for i in range(4) for j in range(4)]

def entry(i, j):
    """sparse poly for M[i,j] = s5*delta + sum_k s_k b_{k,i,j}; dict (svec,bkey)->int."""
    d = {}
    if i == j:
        d[((0, 0, 0, 0, 1), ())] = 1               # s5
    for k in range(4):
        sv = [0, 0, 0, 0, 0]; sv[k] = 1
        d[(tuple(sv), (bid(k, i, j),))] = 1         # s_k * b_{k,i,j}
    return d

def pmul(A, B):
    out = {}
    for (sa, ba), ca in A.items():
        for (sb, bb), cb in B.items():
            sv = tuple(sa[t] + sb[t] for t in range(5))
            bk = tuple(sorted(ba + bb))
            key = (sv, bk)
            out[key] = out.get(key, 0) + ca * cb
    return out

# Leibniz expansion of the 4x4 determinant
det = {}
for perm in permutations(range(4)):
    sign = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if perm[a] > perm[b]: sign = -sign
    prod = {((0, 0, 0, 0, 0), ()): 1}
    for i in range(4):
        prod = pmul(prod, entry(i, perm[i]))
    for key, c in prod.items():
        det[key] = det.get(key, 0) + sign * c
det = {k: v for k, v in det.items() if v != 0}

# group by s-exponent -> b-polynomial (dict bkey->int)
from collections import defaultdict
byS = defaultdict(dict)
for (sv, bk), c in det.items():
    byS[sv][bk] = byS[sv].get(bk, 0) + c

good = {}    # sv (|a'| in 1..3) -> bpoly
p4 = {}      # sv (a5==0)       -> bpoly
for sv, bpoly in byS.items():
    a5 = sv[4]; dprime = sum(sv[:4])
    bpoly = {k: v for k, v in bpoly.items() if v != 0}
    if dprime == 0:
        assert list(bpoly.values()) == [1]      # anchor
    elif a5 == 0:
        p4[sv] = bpoly
    else:
        good[sv] = bpoly
assert len(p4) == 35 and len(good) == 34, (len(p4), len(good))

def bpoly_str(bpoly):
    terms = []
    for bk, c in sorted(bpoly.items()):
        mon = '*'.join(BNAMES[t] for t in bk) or '1'
        terms.append(('+' if c > 0 else '-') + (f'{abs(c)}*' if abs(c) != 1 else '') + mon)
    return ''.join(terms).lstrip('+') or '0'

# save exact polynomials
json.dump(
    dict(bnames=BNAMES,
         good={','.join(map(str, sv)): bpoly_str(bp) for sv, bp in good.items()},
         p4={','.join(map(str, sv)): bpoly_str(bp) for sv, bp in p4.items()}),
    open('results/s78_reduced_polys.json', 'w'), indent=1)

# ---- Singular: dimension of the source locus S = V(35 P4 coeffs) in 64 b-vars ----
p4list = ',\n  '.join(bpoly_str(bp) for bp in p4.values())
sing = f"""// dim of the singular 4-pencil source locus S in 64 B-variables (dp order).
ring r=0,({','.join(BNAMES)}),dp;
option(redSB);
ideal P4=
  {p4list};
ideal G=groebner(P4);
"dim S ="; dim(G);
"deg   ="; degree(G);
quit;
"""
open('results/astra/S2/cas/reduced_dimS.sing', 'w').write(sing)
print("det terms:", len(det), " good:", len(good), " P4:", len(p4))
print("wrote results/s78_reduced_polys.json and reduced_dimS.sing")
