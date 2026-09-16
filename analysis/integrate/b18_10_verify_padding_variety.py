"""Check slot 10's correction: the padding variety at length L is
   P_L = closure{ (z.per3) o T : T in Hom(C^L, C^10) },
not R13L = all linear x cubic.

Jacobian rank of the parametrisation T |-> (u0)*per3(u1..u9), u_a = sum_k T[a][k] x_k.
"""
import itertools, random
from fractions import Fraction
from math import comb
random.seed(1810)

def mons(deg, nv): return [m for m in itertools.product(range(deg+1), repeat=nv) if sum(m)==deg]
def pmul(a,b):
    o={}
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb)); o[k]=o.get(k,0)+va*vb
    return {k:v for k,v in o.items() if v}
def padd(a,b):
    o=dict(a)
    for k,v in b.items(): o[k]=o.get(k,0)+v
    return {k:v for k,v in o.items() if v}
def rank(rows):
    M=[[Fraction(x) for x in r] for r in rows]; R=len(M); C=len(M[0]); r=0
    for c in range(C):
        p=next((i for i in range(r,R) if M[i][c]!=0), None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(r+1,R):
            if M[i][c]!=0:
                f=M[i][c]/M[r][c]
                for j in range(c,C): M[i][j]-=f*M[r][j]
        r+=1
        if r==R: break
    return r

PERMS = list(itertools.permutations(range(3)))
def per3(U):  # U[i][j] are polynomial dicts; permanent = sum over perms, all +
    tot={}
    for p in PERMS:
        t={None:1}; t={k:v for k,v in [((0,)*0,1)]} if False else None
        t=None
        acc=None
        for i in range(3):
            acc = U[i][p[i]] if acc is None else pmul(acc, U[i][p[i]])
        tot=padd(tot, acc)
    return tot

def dim_P(L):
    Q=mons(4,L); QI={m:i for i,m in enumerate(Q)}
    T=[[random.randint(-6,6) for _ in range(L)] for _ in range(10)]
    def lin(a): return {tuple(1 if t==k else 0 for t in range(L)):T[a][k] for k in range(L) if T[a][k]}
    u=[lin(a) for a in range(10)]
    rows=[]
    for a in range(10):
        for k in range(L):
            e=tuple(1 if t==k else 0 for t in range(L))
            # dF/dT[a][k]: product rule on F = u0 * per3(u1..u9)
            U=[[u[1+3*i+j] for j in range(3)] for i in range(3)]
            if a==0:
                d=pmul({e:1}, per3(U))
            else:
                idx=a-1; i,j=divmod(idx,3)
                dper={}
                for p in PERMS:
                    if p[i]!=j: continue
                    acc=None
                    for r2 in range(3):
                        f = {e:1} if r2==i else U[r2][p[r2]]
                        acc = f if acc is None else pmul(acc,f)
                    dper=padd(dper,acc)
                d=pmul(u[0], dper)
            v=[0]*len(Q)
            for mm,c in d.items(): v[QI[mm]]+=c
            rows.append(v)
    return rank(rows)

print(f"{'L':>3} {'dim P_L (mine)':>15} {'10L-5':>7} {'slot 10':>8} {'dim D4L':>8} {'gap':>5}")
claim={5:39,6:55,7:65,8:75}
for L in (5,6,7,8):
    d=dim_P(L)
    print(f"{L:>3} {d:>15} {10*L-5:>7} {claim[L]:>8} {16*L-30:>8} {16*L-30-d:>5}")
print("\nfrom L=6 on, if dim P_L = 10L-5 and dim D4L = 16L-30, gap = 6L-25:")
for L in range(5,11): print(f"   L={L}: 6L-25 = {6*L-25}")
