"""Does the containment survive at length 5?

Question (session 27, successor item 2): is D_5^{per_3^pad} contained in
D_5^{det_4}?  Since per_3 is dense in 5-ary cubics, D_5^pad is the full
reducible locus {ell . c}.  So the question is: is s_1 . (generic cubic c)
a 4x4 determinant of linear forms in s_1..s_5?

det(sum s_i A_i) divisible by s_1  <=>  det(sum_{i>=2} s_i A_i) == 0
identically, i.e. span(A_2..A_5) is a vector space of singular matrices.
Those come in compression branches.  For each branch, parametrise, write
det M = s_1 . G, and measure the dimension of the reachable c-family as the
Jacobian rank of params -> coefficients of G.  Rank 35 = all cubics = containment.
"""
import random, itertools
P = (1 << 61) - 1
R = 5   # variables s_1..s_5

def pmul(a, b):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(e1[k]+e2[k] for k in range(R))
            o[e] = (o.get(e,0)+c1*c2) % P
    return {e:c for e,c in o.items() if c}
def padd(a, b):
    o = dict(a)
    for e,c in b.items(): o[e]=(o.get(e,0)+c)%P
    return {e:c for e,c in o.items() if c}
def det4(M):
    acc = {}
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for i in range(4):
            for j in range(i+1,4):
                if perm[i]>perm[j]: sgn=-sgn
        t = {tuple([0]*R):sgn % P}
        for p in range(4): t = pmul(t, M[p][perm[p]])
        acc = padd(acc, t)
    return acc
def cof(M, p, q):
    rows=[x for x in range(4) if x!=p]; cols=[x for x in range(4) if x!=q]
    acc={}
    for perm in itertools.permutations(range(3)):
        sgn=1
        for i in range(3):
            for j in range(i+1,3):
                if perm[i]>perm[j]: sgn=-sgn
        t={tuple([0]*R):sgn%P}
        for i in range(3): t=pmul(t,M[rows[i]][cols[perm[i]]])
        acc=padd(acc,t)
    s = 1 if (p+q)%2==0 else -1
    return {e:(c*s)%P for e,c in acc.items()}
def div_s1(poly):
    out={}
    for e,c in poly.items():
        assert e[0]>=1, "not divisible by s_1"
        out[tuple([e[0]-1]+list(e[1:]))]=c
    return out

MON3=[e for e in itertools.product(range(4),repeat=R) if sum(e)==3]
IDX={e:k for k,e in enumerate(MON3)}   # 35 of them

def branch_rank(freemask, seed):
    """freemask[p][q] True = entry free in A_2..A_5 (A_1 always fully free)."""
    rnd=random.Random(seed)
    A=[[[rnd.randint(-7,7) for _ in range(4)] for _ in range(4)]]
    for i in range(4):
        A.append([[rnd.randint(-7,7) if freemask[p][q] else 0 for q in range(4)] for p in range(4)])
    M=[[{} for _ in range(4)] for _ in range(4)]
    for p in range(4):
        for q in range(4):
            d={}
            for i in range(5):
                v=A[i][p][q]%P
                if v:
                    e=[0]*R; e[i]=1; d[tuple(e)]=v
            M[p][q]=d
    D=det4(M); G=div_s1(D)           # asserts divisibility = branch really singular
    rows=[]
    C=[[cof(M,p,q) for q in range(4)] for p in range(4)]
    for i in range(5):
        e_i=[0]*R; e_i[i]=1; e_i=tuple(e_i)
        for p in range(4):
            for q in range(4):
                if i>=1 and not freemask[p][q]: continue
                der=pmul({e_i:1},C[p][q])        # d(det)/d(A_i)_{pq}
                derG=div_s1(der)                 # asserts: deformation stays in branch
                row=[0]*35
                for e,c in derG.items(): row[IDX[e]]=(row[IDX[e]]+c)%P
                rows.append(row)
    rk=0
    for col in range(35):
        piv=next((k for k in range(rk,len(rows)) if rows[k][col]),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        inv=pow(rows[rk][col],P-2,P)
        rows[rk]=[(x*inv)%P for x in rows[rk]]
        for k in range(len(rows)):
            if k!=rk and rows[k][col]:
                f=rows[k][col]
                rows[k]=[(rows[k][c2]-f*rows[rk][c2])%P for c2 in range(35)]
        rk+=1
    return rk

full=[[True]*4 for _ in range(4)]
def mask(zero_rows, zero_cols):
    return [[not (p in zero_rows and q in zero_cols) for q in range(4)] for p in range(4)]

BRANCHES = {
 "k=1 common kernel   (col 4 = 0)          ": mask({0,1,2,3},{3}),
 "k=2 compression 2->1 (rows 2-4 x cols 3-4)": mask({1,2,3},{2,3}),
 "k=3 compression 3->2 (rows 3-4 x cols 2-4)": mask({2,3},{1,2,3}),
 "k=4 common cokernel (row 4 = 0)          ": mask({3},{0,1,2,3}),
}
print("target = 35 (all 5-ary cubics).  rank = dim of cubics c with s_1.c determinantal via this branch")
best=0
for name,fm in BRANCHES.items():
    r=max(branch_rank(fm,s) for s in (0,1,2))
    best=max(best,r)
    print("  %s rank %d %s"%(name,r,"  <-- DENSE, containment PROVED" if r==35 else ""))
print()
print("max over branches:", best, "of 35")
