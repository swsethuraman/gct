#!/usr/bin/env python3
"""Sum im dPhi over several determinantal reps of a FIXED reducible q = s5*det_3(N0),
to approximate T_q(image) from below, and intersect with T_q R_5."""
import sys, random, itertools
sys.path.insert(0,'analysis')
from flint import nmod_mat
from wk9_s54_tangent import (spmul,spadd,adjugate,det4,entries,vecq,TqR5,QEXP,QIDX,linf)
P1,P2=2147483647,2147483629
R,n=5,4
def imdPhi_cols(Ment,p):
    adj=adjugate(Ment,p); cols=[]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                H=[[{} for _ in range(n)] for _ in range(n)]
                H[a][b]={tuple(1 if i==k else 0 for i in range(R)):1}
                f={}
                for i in range(n):
                    for j in range(n): spadd(f,spmul(adj[i][j],H[j][i],p),p)
                cols.append(vecq(f))
    return cols
def rank(vecs,p,ncol=len(QEXP)):
    if not vecs: return 0
    return nmod_mat(len(vecs),ncol,[int(vecs[r][c]) for r in range(len(vecs)) for c in range(ncol)],p).rank()
def run():
    for p in (P1,P2):
        rng=random.Random(2026+p%97)
        # fixed N0 (3x3 pencil in 5 vars) => c0=det_3 N0, q = s5*c0
        N0=[[[rng.randint(0,p-1) for _ in range(3)] for _ in range(3)] for _ in range(R)]
        def Nent(a,b): 
            d={}
            for k in range(R):
                if N0[k][a][b]%p: d[tuple(1 if i==k else 0 for i in range(R))]=N0[k][a][b]%p
            return d
        reps=[]
        # block diag(s5, N0)
        def block():
            M=[[{} for _ in range(n)] for _ in range(n)]
            M[0][0]={tuple(1 if i==4 else 0 for i in range(R)):1}
            for a in range(1,n):
                for b in range(1,n): M[a][b]=Nent(a-1,b-1)
            return M
        reps.append(block())
        # upper-tri [[s5, r^T],[0,N0]], several r
        for _ in range(4):
            M=block()
            for b in range(1,n):
                r_=[rng.randint(0,p-1) for _ in range(R)]
                M[0][b]={tuple(1 if i==k else 0 for i in range(R)):r_[k] for k in range(R) if r_[k]%p}
            reps.append(M)
        # lower-tri [[s5,0],[c1,N0]], several c1
        for _ in range(4):
            M=block()
            for a in range(1,n):
                c_=[rng.randint(0,p-1) for _ in range(R)]
                M[a][0]={tuple(1 if i==k else 0 for i in range(R)):c_[k] for k in range(R) if c_[k]%p}
            reps.append(M)
        # verify all reps have det = q (same up to nonzero scalar? here exactly s5*det N0)
        q=det4(reps[0],p)
        allsame=all(det4(M,p)==q for M in reps)
        # union of im dPhi
        U=[]
        for M in reps: U+=imdPhi_cols(M,p)
        rU=rank(U,p)
        TR=TqR5(q,p); rTR=rank(TR,p)
        rboth=rank(U+TR,p)
        inter=rU+rTR-rboth
        print(f"p={p}: reps={len(reps)} dets_equal={allsame}  "
              f"dim(union im dPhi)={rU} (>=50 => T_qD5 looks >=50)  "
              f"dim T_qR5={rTR}  dim(T_qR5 cap union)={inter}",flush=True)
run()
