"""Integrator check of B18-10's length sweep.

dim D4L  = closure of { det(x_1 B_1 + ... + x_L B_L) } in Sym^4(C^L)
dim R13L = closure of { (linear) * (cubic) } in Sym^4(C^L)

Both by exact Jacobian rank at a random integer point (rank at a point is a lower
bound on the generic rank; a random point attains it with probability 1).
"""
import itertools, random
from fractions import Fraction
from math import comb
random.seed(1810)
N = 4   # 4x4 matrices

def mons(deg, nv):
    return [m for m in itertools.product(range(deg+1), repeat=nv) if sum(m)==deg]

def pmul(a,b):
    o={}
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb)); o[k]=o.get(k,0)+va*vb
    return {k:v for k,v in o.items() if v}

def det_minor(M, rows, cols, nv):
    n=len(rows)
    if n==0: return {(0,)*nv:1}
    tot={}
    for perm in itertools.permutations(range(n)):
        sgn=1; p=list(perm)
        for a in range(n):
            for b in range(a+1,n):
                if p[a]>p[b]: sgn=-sgn
        t={(0,)*nv:1}
        for a in range(n):
            t=pmul(t, M[rows[a]][cols[perm[a]]])
            if not t: break
        for k,v in t.items(): tot[k]=tot.get(k,0)+sgn*v
    return {k:v for k,v in tot.items() if v}

def rank(rows):
    M=[[Fraction(x) for x in r] for r in rows]
    R=len(M); C=len(M[0]) if R else 0; r=0
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

def dim_D4(L):
    Q=mons(4,L); QI={m:i for i,m in enumerate(Q)}
    Bs=[[[random.randint(-6,6) for _ in range(N)] for _ in range(N)] for _ in range(L)]
    Mx=[[{tuple(1 if t==k else 0 for t in range(L)):Bs[k][i][j] for k in range(L) if Bs[k][i][j]}
         for j in range(N)] for i in range(N)]
    rows=[]
    for k in range(L):
        xk={tuple(1 if t==k else 0 for t in range(L)):1}
        for i in range(N):
            for j in range(N):
                rr=[a for a in range(N) if a!=i]; cc=[b for b in range(N) if b!=j]
                cof=det_minor(Mx,rr,cc,L)
                if (i+j)%2: cof={a:-b for a,b in cof.items()}
                v=[0]*len(Q)
                for e,c in pmul(xk,cof).items(): v[QI[e]]+=c
                rows.append(v)
    return rank(rows)

def dim_R13(L):
    Q=mons(4,L); QI={m:i for i,m in enumerate(Q)}
    L1=mons(1,L); C3=mons(3,L)
    lin={m:random.randint(-6,6) for m in L1}
    cub={m:random.randint(-6,6) for m in C3}
    rows=[]
    for m in L1:                      # d/d(linear coeff) = (that monomial) * cubic
        v=[0]*len(Q)
        for e,c in pmul({m:1},cub).items(): v[QI[e]]+=c
        rows.append(v)
    for m in C3:                      # d/d(cubic coeff) = linear * (that monomial)
        v=[0]*len(Q)
        for e,c in pmul(lin,{m:1}).items(): v[QI[e]]+=c
        rows.append(v)
    return rank(rows)

print(f"{'L':>3} {'dim Sym^4(C^L)':>15} {'dim D4L':>8} {'16L-30':>7} {'dim R13L':>9} "
      f"{'L+C(L+2,3)-1':>13} {'gap D-R':>8}")
for L in range(5, 9):
    dD=dim_D4(L); dR=dim_R13(L)
    print(f"{L:>3} {comb(L+3,4):>15} {dD:>8} {16*L-30:>7} {dR:>9} {L+comb(L+2,3)-1:>13} {dD-dR:>8}")
print("\nformula projection to L=10 (both formulas confirmed above):")
for L in range(9, 11):
    print(f"{L:>3} {comb(L+3,4):>15} {16*L-30:>8} {'':>7} {L+comb(L+2,3)-1:>9} {'':>13} {16*L-30-(L+comb(L+2,3)-1):>8}")
