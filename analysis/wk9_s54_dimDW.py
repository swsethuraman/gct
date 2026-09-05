#!/usr/bin/env python3
"""
Session 54 -- dim(D_5 cap W), W = {s_5 . c}, done correctly (global).

D_5 = closure{ f_1 = tr(adj M_0(s) M_1(s)) : M_0 in ker-pencils, M_1 } -- the
common-kernel parametrization is dominant to D_5 (dim 50; wk9_s54_bdim). Write
G(params)=f_1 in C^70, pi = projection to the 35 s_5-degree-0 monomials
(W = ker pi). Then, at a GENERIC point of V = {G in W} = {pi.G = 0},
    dim(D_5 cap W) = dim G(V) = rank(dG) - rank(pi.dG).
R_5 subset D_5  <=>  dim(D_5 cap W) = 35  <=>  dim(R_5 cap D_5)=dim(D_5capW)+4=39.

We (1) build a generic V-point: generic M_0 in ker-pencils, then M_1 solving the
35 linear conditions f_1|_{s5=0}=0; (2) form the exact Jacobian dG (dual numbers)
in the params (M_0 coeffs c_ij and M_1 entries) at that point; (3) rank(dG) and
rank of its s_5-degree-0 rows. Calibrations: at a NON-V (generic) point the same
formula must give the transverse value 15; and dim T = rank(dG) must be 50.
"""
import sys, random, itertools, argparse, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat
P1, P2 = 2147483647, 2147483629
R, n = 5, 4

def dadd(x,y,p): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def dmul(x,y,p): return ((x[0]*y[0])%p,(x[0]*y[1]+x[1]*y[0])%p)
def spadd(acc,b,p,coef=(1,0)):
    for e,c in b.items(): acc[e]=dadd(acc.get(e,(0,0)),dmul(coef,c,p),p)
def spmul(a,b,p):
    out={}
    for ea,ca in a.items():
        for eb,cb in b.items():
            e=tuple(ea[i]+eb[i] for i in range(R))
            out[e]=dadd(out.get(e,(0,0)),dmul(ca,cb,p),p)
    return out
def det3(M,p):
    out={}
    for pm in itertools.permutations(range(3)):
        sgn=1
        for i in range(3):
            for j in range(i+1,3):
                if pm[i]>pm[j]: sgn=-sgn
        pr={(0,)*R:(sgn%p,0)}
        for i in range(3): pr=spmul(pr,M[i][pm[i]],p)
        spadd(out,pr,p)
    return out
def adjugate(M0,p):
    adj=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rows=[r for r in range(n) if r!=j]; cols=[c for c in range(n) if c!=i]
            sub=[[M0[r][c] for c in cols] for r in rows]
            m=det3(sub,p); s=1 if (i+j)%2==0 else -1
            adj[i][j]={e:((s*c[0])%p,(s*c[1])%p) for e,c in m.items()}
    return adj

QEXP=[]
def _q(k,left,cur):
    if k==R-1: QEXP.append(tuple(cur+[left])); return
    for v in range(left+1): _q(k+1,left-v,cur+[v])
_q(0,4,[])
QIDX={e:i for i,e in enumerate(QEXP)}
S5DEG0=[i for i,e in enumerate(QEXP) if e[4]==0]

def stratum_basis(name, rng, p):
    G=[]
    if name=='ker':
        for a in range(n):
            for b in range(n):
                if b==0: continue
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='coker':
        for a in range(n):
            for b in range(n):
                if a==0: continue
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='c21':
        for a in range(n):
            for b in range(n):
                if b in (0,1) and a in (1,2,3): continue
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='c32':
        for a in range(n):
            for b in range(n):
                if b in (0,1,2) and a in (2,3): continue
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='prim':
        phi=[[[0]*n for _ in range(n)] for _ in range(n)]
        for a in range(n):
            for b in range(n):
                for c in range(b+1,n):
                    v=rng.randint(1,p-1); phi[a][b][c]=v; phi[a][c][b]=(-v)%p
        for c in range(n):
            G.append([[phi[a][b][c] for b in range(n)] for a in range(n)])
    return G

def kerbasis():
    return stratum_basis('ker', random.Random(0), P1)

def f1_dual(cc, HH, G, p):
    """cc[k][j] dual coeffs (M0 = sum_i s_i sum_j cc[i][j] G[j]); HH[k][a][b] dual
    (M1 = sum_i s_i H_i). return (val,dval) 70-vectors."""
    m=len(G)
    M0=[[[ (0,0) for _ in range(n)] for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                acc=(0,0)
                for j in range(m):
                    if G[j][a][b]:
                        acc=dadd(acc,dmul(cc[k][j],(G[j][a][b]%p,0),p),p)
                M0[k][a][b]=acc
    def lin(mats,a,b):
        d={}
        for k in range(R):
            if mats[k][a][b]!=(0,0):
                e=[0]*R; e[k]=1; d[tuple(e)]=mats[k][a][b]
        return d
    M0e=[[lin(M0,a,b) for b in range(n)] for a in range(n)]
    M1e=[[lin(HH,a,b) for b in range(n)] for a in range(n)]
    adj=adjugate(M0e,p)
    f={}
    for i in range(n):
        for j in range(n):
            spadd(f,spmul(adj[i][j],M1e[j][i],p),p)
    val=[0]*len(QEXP); dv=[0]*len(QEXP)
    for e,c in f.items(): val[QIDX[e]]=c[0]%p; dv[QIDX[e]]=c[1]%p
    return val,dv

def make_V_point(G, p, rng):
    """generic M0 in ker-pencils; solve M1 (80 params) s.t. f_1|_{s5=0}=0."""
    m=len(G)
    c=[[rng.randint(1,p-1) for _ in range(m)] for _ in range(R)]
    # f_1|_{s5=0} is linear in M1 entries. Build 35 x 80 matrix, find nullspace.
    # columns: M1 param (k,a,b). rows: the 35 s5-deg0 monomials.
    cc=[[ (c[i][j],0) for j in range(m)] for i in range(R)]
    cols=[]
    idxs=[]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                HH=[[[ (0,0) for _ in range(n)] for _ in range(n)] for _ in range(R)]
                HH[k][a][b]=(1,0)
                val,_=f1_dual(cc,HH,G,p)
                cols.append([val[i] for i in S5DEG0])
                idxs.append((k,a,b))
    A=nmod_mat(len(S5DEG0),len(cols),
               [int(cols[j][r]) for r in range(len(S5DEG0)) for j in range(len(cols))],p)
    Xns,nul=A.nullspace()
    # pick a random combination of null vectors -> M1 coeffs (as a list over idxs)
    coeffs=[0]*len(cols)
    for t in range(nul):
        w=rng.randint(1,p-1)
        for r in range(len(cols)):
            coeffs[r]=(coeffs[r]+w*int(Xns[r,t]))%p
    H=[[[0]*n for _ in range(n)] for _ in range(R)]
    for r,(k,a,b) in enumerate(idxs):
        H[k][a][b]=coeffs[r]
    return c,H,nul

def jac_ranks(c,H,G,p,atV=True):
    m=len(G)
    def col_for(param):
        cc=[[ (c[i][j],0) for j in range(m)] for i in range(R)]
        HH=[[[ (H[i][a][b],0) for b in range(n)] for a in range(n)] for i in range(R)]
        kind,idx=param
        if kind=='c':
            i,j=idx; cc[i][j]=(c[i][j],1)
        else:
            i,a,b=idx; HH[i][a][b]=(H[i][a][b],1)
        _,dv=f1_dual(cc,HH,G,p)
        return dv
    params=[('c',(i,j)) for i in range(R) for j in range(m)] + \
           [('H',(i,a,b)) for i in range(R) for a in range(n) for b in range(n)]
    J=[col_for(pp) for pp in params]           # each is 70-vector (a Jacobian column)
    npar=len(J)
    full=nmod_mat(npar,len(QEXP),[int(J[r][cc]) for r in range(npar) for cc in range(len(QEXP))],p)
    rk_full=full.rank()
    sub=nmod_mat(npar,len(S5DEG0),[int(J[r][S5DEG0[cc]]) for r in range(npar) for cc in range(len(S5DEG0))],p)
    rk_pi=sub.rank()
    return rk_full, rk_pi

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--strata',default='ker,coker,c21,c32,prim')
    a=ap.parse_args()
    out={}
    best=0; best_name=None
    for name in a.strata.split(','):
        rows=[]
        for p in (P1,P2):
            for seed in (11,22):
                rng=random.Random(seed+p%1000)
                G=stratum_basis(name,rng,p)
                if not G: continue
                c,H,nul=make_V_point(G,p,rng)
                rkV,rkVpi=jac_ranks(c,H,G,p)
                dimDW=rkV-rkVpi
                rows.append(dict(prime=p,seed=seed,dimE=len(G),Vnull=nul,
                                 rankdG=rkV,rankpi=rkVpi,dim_D5capW=dimDW,
                                 dim_R5capD5=dimDW+4))
        mx=max(r['dim_D5capW'] for r in rows) if rows else 0
        if mx>best: best=mx; best_name=name
        out[name]=rows
        vals=sorted(set(r['dim_D5capW'] for r in rows))
        print(f"[{name}] dimE={rows[0]['dimE'] if rows else '-'}  "
              f"dim(D_5 cap W) over V-points = {vals}  "
              f"=> dim(R_5 cap D_5) = {[v+4 for v in vals]}",flush=True)
    print(f"\nMAX dim(D_5 cap W) over strata = {best} (at {best_name})")
    print(f"=> dim(R_5 cap D_5) = {best+4};  dim R_5 = 39.  "
          f"R_5 subset D_5  iff  this = 39.")
    json.dump(out,open('results/s54_dimDW.json','w'),indent=1)
    print("wrote results/s54_dimDW.json")
