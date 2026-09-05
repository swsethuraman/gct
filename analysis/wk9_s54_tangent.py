#!/usr/bin/env python3
"""
Session 54 -- the tangent test: R_5 subset D_5 ?

At an EXACT reducible determinantal point q = det M = s5.c (c in the dim-31
exact family, s32), compute:
  imdPhi = im dPhi_M = span{ tr(adj M(s) H(s)) : H pencil }   (subset T_q D_5)
  T_qR_5 = tangent to the reducible locus at q = s5.c
         = s5 . Sym^3 C^5  +  c . Sym^1 C^5    (dim 39 at a generic reducible pt)
and dim(T_qR_5 cap imdPhi).

Logic:
 * imdPhi subset T_q D_5, so  dim(T_qR_5 cap T_qD_5) >= dim(T_qR_5 cap imdPhi).
 * If, over the exact-reducible fiber, max rank(imdPhi) = 50, then q is a SMOOTH
   point of D_5 and T_qD_5 = imdPhi (dim 50). Then T_qR_5 subset T_qD_5 iff
   dim(T_qR_5 cap imdPhi) = 39; if < 39 at a smooth q, R_5 NOT subset D_5 (proved,
   since a subvariety's tangent lies in the ambient's tangent at a smooth common pt).
We report rank(imdPhi) (smoothness), dim T_qR_5, and the intersection, both primes,
several exact-reducible constructions, maximizing rank over the fiber by sampling.
"""
import sys, random, itertools, json
sys.path.insert(0,'analysis')
from flint import nmod_mat
P1,P2=2147483647,2147483629
R,n=5,4

def spmul(a,b,p):
    o={}
    for ea,ca in a.items():
        for eb,cb in b.items():
            e=tuple(ea[i]+eb[i] for i in range(R)); o[e]=(o.get(e,0)+ca*cb)%p
    return o
def spadd(acc,b,p,s=1):
    for e,c in b.items(): acc[e]=(acc.get(e,0)+s*c)%p
def det3(M,p):
    o={}
    for pm in itertools.permutations(range(3)):
        sg=1
        for i in range(3):
            for j in range(i+1,3):
                if pm[i]>pm[j]: sg=-sg
        pr={(0,)*R:sg%p}
        for i in range(3): pr=spmul(pr,M[i][pm[i]],p)
        spadd(o,pr,p)
    return o
def det4(M,p):
    o={}
    for pm in itertools.permutations(range(4)):
        sg=1
        for i in range(4):
            for j in range(i+1,4):
                if pm[i]>pm[j]: sg=-sg
        pr={(0,)*R:sg%p}
        for i in range(4): pr=spmul(pr,M[i][pm[i]],p)
        spadd(o,pr,p)
    return o
def adjugate(M,p):
    adj=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rs=[r for r in range(n) if r!=j]; cs=[c for c in range(n) if c!=i]
            sub=[[M[r][c] for c in cs] for r in rs]; m=det3(sub,p)
            s=1 if (i+j)%2==0 else -1
            adj[i][j]={e:(s*c)%p for e,c in m.items()}
    return adj

QEXP=[]
def _q(k,left,cur):
    if k==R-1: QEXP.append(tuple(cur+[left])); return
    for v in range(left+1): _q(k+1,left-v,cur+[v])
_q(0,4,[]); QIDX={e:i for i,e in enumerate(QEXP)}
CEXP=[]
def _c(k,left,cur):
    if k==R-1: CEXP.append(tuple(cur+[left])); return
    for v in range(left+1): _c(k+1,left-v,cur+[v])
_c(0,3,[])   # cubic exps
LEXP=[tuple(1 if i==k else 0 for i in range(R)) for k in range(R)]  # linear

def linf(mats,a,b,p):
    d={}
    for k in range(R):
        if mats[k][a][b]%p: d[tuple(1 if i==k else 0 for i in range(R))]=mats[k][a][b]%p
    return d
def entries(mats,p): return [[linf(mats,a,b,p) for b in range(n)] for a in range(n)]

def vecq(sp):
    v=[0]*len(QEXP)
    for e,c in sp.items(): v[QIDX[e]]=c
    return v

def imdPhi(Ment,p):
    adj=adjugate(Ment,p); cols=[]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                H=[[{} for _ in range(n)] for _ in range(n)]
                H[a][b]={tuple(1 if i==k else 0 for i in range(R)):1}
                f={}
                for i in range(n):
                    for j in range(n):
                        spadd(f,spmul(adj[i][j],H[j][i],p),p)
                cols.append(vecq(f))
    return cols  # 80 vectors in C^70

def TqR5(qsp,p):
    """q = s5.c. tangent to R_5 = s5.Sym^3 + c.Sym^1."""
    # c = q / s5
    c={}
    for e,co in qsp.items():
        assert e[4]>=1, "q not divisible by s5"
        e2=list(e); e2[4]-=1; c[tuple(e2)]=co
    vs=[]
    # s5 . (each cubic monomial)
    for ce in CEXP:
        e=list(ce); e[4]+=1; vs.append(vecq({tuple(e):1}))
    # c . (each linear monomial)
    for le in LEXP:
        prod={}
        for e,co in c.items():
            e2=tuple(e[i]+le[i] for i in range(R)); prod[e2]=(prod.get(e2,0)+co)%p
        vs.append(vecq(prod))
    return vs

def build_exact_reducible(kind,rng,p):
    """return pencil mats with det divisible by s5 (c in exact family)."""
    mats=[[[0]*n for _ in range(n)] for _ in range(R)]
    if kind=='block':               # diag(s5, N): c=det_3 N (dim 29)
        mats[4][0][0]=1
        for k in range(R):
            for a in range(1,n):
                for b in range(1,n): mats[k][a][b]=rng.randint(0,p-1)
    elif kind=='c21':               # richer: (2->1)-type; c up to dim 31
        mats[4][0][0]=1
        for k in range(R):
            for a in range(1,n):
                mats[k][a][0]=rng.randint(0,p-1)
                for b in range(1,n): mats[k][a][b]=rng.randint(0,p-1)
    elif kind=='genker':            # generic common-kernel pencil (col0=0): det=?
        # not automatically div by s5; skip
        pass
    return mats

def rankmod(vecs,p):
    if not vecs: return 0
    return nmod_mat(len(vecs),len(QEXP),
                    [int(vecs[r][c]) for r in range(len(vecs)) for c in range(len(QEXP))],p).rank()

def run():
    out={}
    for kind in ('block','c21'):
        rows=[]
        for p in (P1,P2):
            best_im=0; best_int=None; best_TR=None
            for seed in range(6):     # sample fiber, maximize im rank
                rng=random.Random(100*seed+7)
                mats=build_exact_reducible(kind,rng,p)
                Ment=entries(mats,p)
                q=det4(Ment,p)
                # check divisibility
                if any(e[4]==0 and co%p for e,co in q.items()):
                    continue
                im=imdPhi(Ment,p); rim=rankmod(im,p)
                TR=TqR5(q,p); rTR=rankmod(TR,p)
                rboth=rankmod(im+TR,p)
                inter=rim+rTR-rboth
                if rim>best_im:
                    best_im=rim; best_int=inter; best_TR=rTR
            rows.append(dict(prime=p,max_imdPhi=best_im,dim_TqR5=best_TR,
                             dim_TqR5_cap_imdPhi=best_int))
            print(f"[{kind}] p={p}: max rank(im dPhi)={best_im} (smooth iff 50), "
                  f"dim T_qR_5={best_TR}, dim(T_qR_5 cap im dPhi)={best_int} "
                  f"(=39 would allow containment)",flush=True)
        out[kind]=rows
    json.dump(out,open('results/s54_tangent.json','w'),indent=1)
    print("wrote results/s54_tangent.json")

if __name__=='__main__': run()
