"""Exact lift + independent verification at an unused fifth prime, with controls."""
import sys,json,time
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad')
from harness import *
from red import gen_RED
from flint import nmod_mat, fmpz
from math import gcd
LIFT_P=[2147483647,2147483629,2147482951,2147482949]
VERIFY_P=2147482943
while not fmpz(VERIFY_P).is_prime(): VERIFY_P-=1
bs=enumerate_brackets(W,COL); NB=len(bs)
def rows_of(fam,p,ev,seed):
    reds = gen_RED(p,480,seed) if fam=='RED' else gen_points(fam,p,480,seed,uniform=(fam!='GEN'))[0]
    return evalmat(ev,reds)
def basis_rows(G,p):
    T,rr=nmod_mat(len(G[0]),NB,[int(G[i][j])%p for j in range(len(G[0])) for i in range(NB)],p).rref()
    return [next(j for j in range(NB) if T[i,j]) for i in range(rr)]
def kern(M,R,p):
    S=nmod_mat(429,len(M[0]),[int(M[i][j])%p for i in R for j in range(len(M[0]))],p)
    X,n=S.transpose().nullspace()
    K,k=nmod_mat(n,429,[int(X[i,j]) for j in range(n) for i in range(429)],p).rref()
    assert k==n
    return n,[[int(K[i,j]) for j in range(429)] for i in range(n)]
R=None; store={'RED':[],'DET':[]}
for p in LIFT_P:
    ev=Evaluator(bs,COL,p)
    r=basis_rows(rows_of('GEN',p,ev,900+p%101),p); assert len(r)==429
    if R is None: R=r
    assert r==R
    for fam in ('RED','DET'):
        n,K=kern(rows_of(fam,p,ev,950+p%101),R,p); store[fam].append((p,n,K))
    print('lift prime',p,'ok',flush=True)
def crt(vs,ms):
    x=0;M=1
    for v,m in zip(vs,ms): x=x+M*(((v-x)*pow(M,-1,m))%m); M*=m
    return x%M,M
def ratrec(a,m):
    u,v=(m,0),(a,1)
    while v[0]*v[0]*2>m:
        q=u[0]//v[0]; u,v=v,(u[0]-q*v[0],u[1]-q*v[1])
    return (v[0],v[1]) if v[1]>0 else (-v[0],-v[1])
exact={}
for fam in ('RED','DET'):
    recs=store[fam]; n=recs[0][1]; rows=[]
    for i in range(n):
        num=[];den=[]
        for j in range(429):
            x,M=crt([r[2][i][j] for r in recs],[r[0] for r in recs]); a,b=ratrec(x,M)
            g=gcd(abs(a),b); num.append(a//g); den.append(b//g)
        L=1
        for b in den: L=L*b//gcd(L,b)
        rows.append([num[j]*(L//den[j]) for j in range(429)])
    # primitive integer rows
    rows=[[v//g for v in r] for r in rows for g in [max(1,__import__('math').gcd(*[abs(x) for x in r if x]) if any(r) else 1)]]
    exact[fam]=rows
    print(fam,'dim',n,'max entry',max(abs(v) for r in rows for v in r),flush=True)
json.dump({'basis_bracket_indices':R,'brackets':[list(map(list,b)) for b in bs],
           'I_red':exact['RED'],'I_det':exact['DET'],
           'note':'rows are exact integer HWV combinations in the 429-bracket basis basis_bracket_indices'},
          open('exact_ideals.json','w'))
# ---- verification at an unused prime, fresh points ----
p=VERIFY_P; ev=Evaluator(bs,COL,p)
mats={f:rows_of(f,p,ev,7000+ord(f[0])) for f in ('GEN','DET','PAD','RED')}
print('verify prime',p,'ranks',{f:rank_mod(m,p) for f,m in mats.items()},flush=True)
def apply(K,M):
    S=nmod_mat(429,len(M[0]),[int(M[i][j])%p for i in R for j in range(len(M[0]))],p)
    A=nmod_mat(len(K),429,[int(v)%p for r in K for v in r],p)
    Pd=A*S
    return max(int(Pd[i,j]) for i in range(Pd.nrows()) for j in range(Pd.ncols()))
print('CONTROLS at unused prime',p)
for kn in ('I_red','I_det'):
    K=exact[kn[2:].upper()]
    for f in ('RED','DET','PAD','GEN'):
        m=apply(K,mats[f])
        print(f'  {kn} applied to {f}: max |value| = {m}  -> {"VANISHES" if m==0 else "nonzero (as required)"}',flush=True)
