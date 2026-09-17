"""Check a = 1 for lambda = (4^6) in Sym^6(Sym^4 C^6).
S_(4^6)(C^6) = det^4 is one-dimensional, so a is the count of degree-6 SL_6 invariants
of a quartic form in six variables. Computed by monomial DP + the Weyl alternant."""
import itertools, time
NV, DEG, D = 6, 4, 6
RHO = (5,4,3,2,1,0)

def mons(deg, n):
    if n == 1: return [(deg,)]
    out = []
    for k in range(deg+1):
        for r in mons(deg-k, n-1): out.append((k,)+r)
    return out

t0 = time.time()
base = mons(DEG, NV)
print(f"degree-{DEG} monomials in {NV} vars: {len(base)}")

dp = [dict() for _ in range(D+1)]
dp[0][(0,)*NV] = 1
for m in base:                       # unbounded repeats: ascend c, update in place
    for c in range(D):
        src = dp[c]
        if not src: continue
        tgt = dp[c+1]
        for vec, cnt in list(src.items()):
            nv = tuple(a+b for a, b in zip(vec, m))
            tgt[nv] = tgt.get(nv, 0) + cnt
M = dp[D]
print(f"states at size {D}: {len(M)}   ({time.time()-t0:.1f}s)")

def alternant(lam):
    tot = 0
    for perm in itertools.permutations(range(NV)):
        sgn = 1; p = list(perm)
        for a in range(NV):
            for b in range(a+1, NV):
                if p[a] > p[b]: sgn = -sgn
        al = tuple(lam[i] + RHO[i] - RHO[perm[i]] for i in range(NV))
        if min(al) < 0: continue
        tot += sgn * M.get(al, 0)
    return tot

LAM = (4,)*6
print(f"\na(d={D}, lambda={LAM}) = {alternant(LAM)}        (B19-01 claims 1)")

# control: sum over all lambda of a * dim S_lambda(C^6) must equal C(125+D, D)
from math import comb
def dim_schur(lam):
    num = den = 1
    for i in range(NV):
        for j in range(i+1, NV):
            num *= (lam[i]-lam[j]+j-i); den *= (j-i)
    return num//den
def parts_at_most(n, k, maxp=None):
    if maxp is None: maxp = n
    if k == 0:
        if n == 0: yield ()
        return
    for f in range(min(n, maxp), -1, -1):
        for r in parts_at_most(n-f, k-1, f): yield (f,)+r
tot = sum(alternant(l)*dim_schur(l) for l in parts_at_most(DEG*D, NV))
exp = comb(len(base)-1+D, D)
print(f"control: sum a*dim S_lambda(C^6) = {tot}")
print(f"         C(125+{D},{D})            = {exp}   {'OK' if tot==exp else 'FAIL'}")
print(f"\ntotal {time.time()-t0:.1f}s")
