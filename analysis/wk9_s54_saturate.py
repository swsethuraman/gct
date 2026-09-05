#!/usr/bin/env python3
"""Saturation of union of im dPhi over reps of q=s5*det_3(N0): add richer reps
(upper+lower tri with r^T adj(N) c1=0, and GL_4xGL_4 conjugates that give new
tangents via non-block structure). Report union dim as #reps grows."""
import sys, random, itertools
sys.path.insert(0,'analysis')
from flint import nmod_mat
from wk9_s54_tangent import spmul,spadd,adjugate,det4,vecq,TqR5,QEXP,QIDX
P=2147483647; R,n=5,4
def imcols(M,p):
    adj=adjugate(M,p); cols=[]
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
def rank(v,p,nc=len(QEXP)):
    return nmod_mat(len(v),nc,[int(v[r][c]) for r in range(len(v)) for c in range(nc)],p).rank() if v else 0
def sform(vec):
    return {tuple(1 if i==k else 0 for i in range(R)):vec[k]%P for k in range(R) if vec[k]%P}
rng=random.Random(7)
N0=[[[rng.randint(0,P-1) for _ in range(3)] for _ in range(3)] for _ in range(R)]
def Nent(a,b): return sform([N0[k][a][b] for k in range(R)])
def block():
    M=[[{} for _ in range(n)] for _ in range(n)]
    M[0][0]={tuple(1 if i==4 else 0 for i in range(R)):1}
    for a in range(1,n):
        for b in range(1,n): M[a][b]=Nent(a-1,b-1)
    return M
# GL_4 x GL_4 conjugates of block: M -> P M Q (integer, det invertible mod P)
def randGL():
    import itertools as it
    while True:
        A=[[rng.randint(0,P-1) for _ in range(n)] for _ in range(n)]
        # det mod P nonzero check via flint
        d=nmod_mat(n,n,[A[i][j] for i in range(n) for j in range(n)],P).det()
        if d!=0: return A
def matmul_sform(Pm,M,Qm):
    # (P M Q)_{ab} = sum_{i,j} P[a][i] M[i][j] Q[j][b]; M entries are s-forms
    out=[[{} for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            acc={}
            for i in range(n):
                for j in range(n):
                    if Pm[a][i]%P==0 or Qm[j][b]%P==0: continue
                    coef=(Pm[a][i]*Qm[j][b])%P
                    for e,c in M[i][j].items():
                        acc[e]=(acc.get(e,0)+coef*c)%P
            out[a][b]={e:c for e,c in acc.items() if c%P}
    return out
reps=[block()]
for _ in range(3):
    M=block()
    for b in range(1,n): M[0][b]=sform([rng.randint(0,P-1) for _ in range(R)])
    reps.append(M)
for _ in range(3):
    M=block()
    for a in range(1,n): M[a][0]=sform([rng.randint(0,P-1) for _ in range(R)])
    reps.append(M)
# GL conjugates (these change det by scalar -> same projective q; new tangent dirs)
for _ in range(6):
    reps.append(matmul_sform(randGL(),block(),randGL()))
U=[]; q=det4(reps[0],P); TR=TqR5(q,P); rTR=rank(TR,P)
for i,M in enumerate(reps):
    U+=imcols(M,P)
    if i in (0,3,6,9,12,len(reps)-1):
        rU=rank(U,P); inter=rU+rTR-rank(U+TR,P)
        print(f"after {i+1} reps: dim(union)={rU}  dim(T_qR5 cap union)={inter} (T_qR5={rTR})",flush=True)
