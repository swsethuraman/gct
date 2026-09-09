"""s78: the dominance / reversal test.

Reduction (PROVED): W subset D5  <=>  the good-coordinate map
  G: {B in M4^4 : det(sum_{k<=4} s_k B_k) == 0} = S  ->  A^34
is DOMINANT (its image fills the y0=1 chart of P(W)), i.e. the generic rank of
dG restricted to the tangent space T_B S equals 34.

A single point B in S with rank(dG|_{T_B S}) = 34 would PROVE W subset D5
(the reversal). Sub-maximal rank at generic points is consistent with W not
subset D5 but does not prove it (an exact image equation is needed for that).

At B in S, image-dim of G = rank(dPsi_B) - rank(d bad_B), where Psi = (34 good,
35 bad) is the full reduced coefficient map and bad = the 35 P4 coefficients
(whose vanishing defines S). We evaluate this at generic points of the named
singular families.
"""
import json, random
from itertools import permutations
import flint

P1, P2 = 2147483647, 2147483629
rng = random.Random(909)

def vid(k, i, j): return k * 16 + i * 4 + j

def build_maps():
    """Return (good_polys, bad_polys), each a list of dict{varset:int}, for the
    FULL 64-var reduced map (no compression mask)."""
    def entry(i, j):
        d = {}
        if i == j: d[((0,0,0,0,1), ())] = 1
        for k in range(4):
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
        for i in range(4): prod=pmul(prod, entry(i,perm[i]))
        for key,c in prod.items(): det[key]=det.get(key,0)+sign*c
    from collections import defaultdict
    byS=defaultdict(dict)
    for (sv,vs),c in det.items():
        if c: byS[sv][vs]=byS[sv].get(vs,0)+c
    good, bad = [], []
    for sv,poly in byS.items():
        p={k:v for k,v in poly.items() if v}
        if sum(sv[:4])==0: continue          # anchor s5^4
        if sv[4]==0: bad.append(p)            # P4 coeffs (a5=0)
        else: good.append(p)
    return good, bad

GOOD, BAD = build_maps()
assert len(GOOD)==34 and len(BAD)==35

def jac_rows(polys, Pt):
    def evalmon(vs):
        r=1
        for v in vs: r*=Pt[v]
        return r
    rows=[]
    for poly in polys:
        row=[0]*64
        for vs,coeff in poly.items():
            for v in vs:
                rest=tuple(x for x in vs if x!=v)
                row[v]+=coeff*evalmon(rest)
        rows.append(row)
    return rows

def rank_mod(rows,p):
    ctx=flint.fmpz_mod_ctx(p)
    return flint.fmpz_mod_mat([[int(x)%p for x in r] for r in rows], ctx).rank()

def image_dim_at(Pt):
    # rank(dPsi) - rank(d bad), both at Pt; use max over primes for each
    dpsi = jac_rows(GOOD+BAD, Pt)
    dbad = jac_rows(BAD, Pt)
    rp = max(rank_mod(dpsi,P1), rank_mod(dpsi,P2))
    rb = max(rank_mod(dbad,P1), rank_mod(dbad,P2))
    return rp - rb, rp, rb

# --- generators of named singular families (as B-tuples, A5=I implicit) ---
def zero(): return {vid(k,i,j):0 for k in range(4) for i in range(4) for j in range(4)}
def rand_ker():
    # common kernel e3 (index 3): column 3 of every B_k is zero
    Pt=zero()
    for k in range(4):
        for i in range(4):
            for j in range(3):   # cols 0,1,2 free; col 3 = 0
                Pt[vid(k,i,j)]=rng.randint(-6,6)
    return Pt
def rand_coker():
    # common cokernel: row 3 of every B_k is zero
    Pt=zero()
    for k in range(4):
        for i in range(3):
            for j in range(4):
                Pt[vid(k,i,j)]=rng.randint(-6,6)
    return Pt
def rand_C32():
    # B_k(U3=<e0,e1,e2>) in W2=<e0,e1>: rows 2,3 nonzero only in col 3
    Pt=zero()
    for k in range(4):
        for i in range(4):
            for j in range(4):
                if i in (2,3) and j in (0,1,2): continue
                Pt[vid(k,i,j)]=rng.randint(-6,6)
    return Pt

tests={}
for name,gen in [("ker",rand_ker),("coker",rand_coker),("C32",rand_C32)]:
    best=(-1,None)
    for _ in range(5):
        Pt=gen()
        # sanity: this point is in S (all bad polys vanish)
        assert all(sum(c*(1 if not vs else __import__('math').prod(Pt[v] for v in vs)) for vs,c in bp.items())==0 for bp in BAD)
        d,rp,rb=image_dim_at(Pt)
        if d>best[0]: best=(d,(rp,rb))
    tests[name]=dict(image_dim=best[0], rank_dPsi=best[1][0], rank_dbad=best[1][1])

maxdim=max(t["image_dim"] for t in tests.values())
result=dict(target_chart_dim=34, tests=tests, max_image_dim_over_tested_families=maxdim,
            dominant=(maxdim==34),
            reversal_W_subset_D5=(maxdim==34),
            note=("A single family reaching 34 would PROVE W subset D5. Max over tested "
                  "families is a LOWER bound on dim(D5 cap W); it does not prove <=33."))
print(json.dumps(result,indent=2))
json.dump(result, open('results/s78_dominance.json','w'), indent=2)
if maxdim<34:
    print(f"\nNo reversal: every tested family has naive image dim <= {maxdim} < 34.")
    print("This is EVIDENCE for W not subset D5, NOT a proof (needs an exact image equation).")
else:
    print("\nREVERSAL: a family fills the chart -> W subset D5. Trigger the verification protocol.")
