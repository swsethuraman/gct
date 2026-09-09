"""s78: image dimensions of the compression components (C21, C32) of D5 cap W.

A 4-tuple (B1..B4) spans a SINGULAR matrix space iff det(sum s_k B_k) == 0 (every
matrix in the span is singular). The named families are compression spaces:
  ker  : B_k(U1) = 0            (common kernel)             flag (1,3)  -> done, 28
  coker: B_k(C4) in W3          (common cokernel)           transpose of ker, 28
  C21  : B_k(U2) in W1          (dim 2 -> dim 1)            flag W1 c U2 c C4, (1,1,2)
  C32  : B_k(U3) in W2          (dim 3 -> dim 2)            flag W2 c U3 c C4, (2,1,1)
With A5 = I (chart y0!=0). Image = 34 non-leading coeffs of det(s5 I + sum s_k B_k).

Bounds (both rigorous when the stabilizer hits its floor):
  LOWER: Jacobian rank at an integer point, mod both house primes (<= generic rank).
  UPPER: source_free - generic_orbit_dim, orbit = dim(P) - stab, P the flag-
    preserving conjugation parabolic; scalars give stab>=1, so observing stab=1
    certifies generic orbit = dim(P)-1 and hence the upper bound.
"""
import json, random
from itertools import permutations
import flint

P1, P2 = 2147483647, 2147483629
rng = random.Random(77)

def rank_mod(rows, p):
    if not rows or not rows[0]:
        return 0
    ctx = flint.fmpz_mod_ctx(p)
    return flint.fmpz_mod_mat([[int(x) % p for x in r] for r in rows], ctx).rank()

def det_coeffs_good(free_mask):
    """Multilinear expansion of det(s5 I4 + sum_{k<=4} s_k B_k) with B_k[i][j] a
    free var only where free_mask[i][j]; returns list of 34 good coeffs as
    dict{ varset : int }, where var id = k*16 + i*4 + j (only free ones used)."""
    def vid(k, i, j): return k * 16 + i * 4 + j
    def entry(i, j):
        d = {}
        if i == j:
            d[((0,0,0,0,1), ())] = 1
        for k in range(4):
            if free_mask[i][j]:
                sv=[0,0,0,0,0]; sv[k]=1
                d[(tuple(sv), (vid(k,i,j),))] = 1
        return d
    def pmul(A,B):
        out={}
        for (sa,ca),va in A.items():
            for (sb,cb),vb in B.items():
                key=(tuple(sa[t]+sb[t] for t in range(5)), tuple(sorted(ca+cb)))
                out[key]=out.get(key,0)+va*vb
        return out
    det={}
    for perm in permutations(range(4)):
        sign=1
        for a in range(4):
            for b in range(a+1,4):
                if perm[a]>perm[b]: sign=-sign
        prod={((0,0,0,0,0),()):1}
        for i in range(4):
            prod=pmul(prod, entry(i,perm[i]))
        for key,c in prod.items():
            det[key]=det.get(key,0)+sign*c
    from collections import defaultdict
    byS=defaultdict(dict)
    for (sv,vs),c in det.items():
        if c: byS[sv][vs]=byS[sv].get(vs,0)+c
    good=[]
    for sv,poly in byS.items():
        if sum(sv[:4])>=1:
            good.append({k:v for k,v in poly.items() if v})
    return good

def analyze(name, free_mask, flag_block):
    """flag_block[i] = block index of coordinate i (0 highest in flag).
    Parabolic (flag-preserving conjugation) Lie algebra: Z[a][b] free iff
    block(a) <= block(b)."""
    def vid(k,i,j): return k*16+i*4+j
    free_ids = [vid(k,i,j) for k in range(4) for i in range(4) for j in range(4) if free_mask[i][j]]
    source_free = len(free_ids)
    good = det_coeffs_good(free_mask)
    assert len(good)==34, (name, len(good))
    nonzero_good = sum(1 for poly in good if poly)
    idpos = {v: t for t, v in enumerate(free_ids)}
    # LOWER: Jacobian rank at several integer points (rank is lower-semicontinuous;
    # the max over points is a certified lower bound approaching the generic rank).
    def jac_rank_at(Pt):
        def evalmon(vs):
            r = 1
            for v in vs: r *= Pt[v]
            return r
        rows = []
        for poly in good:
            row = [0]*source_free
            for vs, coeff in poly.items():
                for v in vs:
                    rest = tuple(x for x in vs if x != v)
                    row[idpos[v]] += coeff*evalmon(rest)
            rows.append(row)
        return max(rank_mod(rows, P1), rank_mod(rows, P2)), rows
    lower = 0; last_rows = None
    for _ in range(8):
        Pt = {vid: 0 for vid in range(64)}
        for vid_ in free_ids: Pt[vid_] = rng.randint(-9, 9)
        r, last_rows = jac_rank_at(Pt)
        lower = max(lower, r)
    Bmats_Pt = Pt  # reuse last point for the orbit computation
    Pt = Bmats_Pt
    # UPPER: flag-preserving parabolic orbit. B_k matrices at Pt.
    Bmats=[[[Pt[vid(k,i,j)] for j in range(4)] for i in range(4)] for k in range(4)]
    # parabolic mask: allowed Z[a][b] iff block(a)<=block(b)
    zids=[(a,b) for a in range(4) for b in range(4) if flag_block[a]<=flag_block[b]]
    zindex={ab:t for t,ab in enumerate(zids)}
    parab_dim=len(zids)
    # stabilizer: [Z,B_k]=0, Z restricted to parabolic. (ZB - BZ)_{ij}=0
    srows=[]
    for k in range(4):
        Bk=Bmats[k]
        for i in range(4):
            for j in range(4):
                row=[0]*parab_dim
                for a in range(4):
                    if (i,a) in zindex: row[zindex[(i,a)]] += Bk[a][j]
                    if (a,j) in zindex: row[zindex[(a,j)]] -= Bk[i][a]
                srows.append(row)
    stab = parab_dim - max(rank_mod(srows,P1), rank_mod(srows,P2))
    orbit = parab_dim - stab
    upper = source_free - orbit
    return dict(component=name, source_free=source_free, nonzero_good_coords=nonzero_good,
                parabolic_dim=parab_dim, stabilizer_dim=stab, orbit_dim=orbit,
                lower_bound=lower, upper_bound=upper,
                exact=(lower if lower==upper else None),
                affine_upper=upper+1, note="upper is projective (chart); affine cone = upper+1")

# C21: rows 1,2,3 (idx1,2,3), cols 0,1 -> zero (B_k(U2=<e0,e1>) in W1=<e0>)
mC21=[[1]*4 for _ in range(4)]
for i in (1,2,3):
    for j in (0,1): mC21[i][j]=0
fbC21=[0,1,2,2]   # flag W1={e0} c U2={e0,e1} c C4 : blocks (1,1,2)

# C32: rows 2,3 (idx2,3), cols 0,1,2 -> zero (B_k(U3=<e0,e1,e2>) in W2=<e0,e1>)
mC32=[[1]*4 for _ in range(4)]
for i in (2,3):
    for j in (0,1,2): mC32[i][j]=0
fbC32=[0,0,1,2]   # flag W2={e0,e1} c U3={e0,e1,e2} c C4 : blocks (2,1,1)

res=[analyze("C21",mC21,fbC21), analyze("C32",mC32,fbC32)]
print(json.dumps(res, indent=2))
json.dump(res, open('results/s78_compression_dim.json','w'), indent=2)
