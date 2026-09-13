"""An explicit integral N14 member from a Hessian and binary transvectants.

For cubic factorial tensor T, put A(t)=T(0+t1,0+t1,0+t1),
G(t)=det(T(i,j,0)+t*T(i,j,1))_(0<=i,j<9), and
H(t)=A(t)^4*(3*A'(t)*G(t)-A(t)*G'(t)).
The output is sum_(k=0)^14 (-1)^k (14!/(14-k)!)(22-k)!
ell0^k ell1^(14-k) [t^k]H(t). All coefficients are integral.
"""
import argparse
from collections import Counter
import copy
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/b15_01"
sys.path.insert(0,str(ROOT/"tools/verify"))
import ci73_eval as ev
from flint import fmpq_mat, fmpz_mat, nmod_mat

P=2147483647


def mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return [v%p for v in out] if p else out


def derivative(a):
    return [k*a[k] for k in range(1,len(a))]


def tensor(symbols):
    return {a:symbols[3][tuple(a.count(i) for i in range(9))]
            for a in itertools.combinations_with_replacement(range(9),3)}


def value(linear,T,p=P):
    def t(i,j,k):
        v=T[tuple(sorted((i,j,k)))]
        return v%p if p else v
    M=[[t(i,j,0) for j in range(9)] for i in range(9)]
    N=[[t(i,j,1) for j in range(9)] for i in range(9)]
    vals=[]
    for x in range(10):
        mat=[[M[i][j]+x*N[i][j] for j in range(9)] for i in range(9)]
        vals.append(int(nmod_mat(mat,p).det() if p else fmpz_mat(mat).det()))
    vand=[[x**k for k in range(10)] for x in range(10)]
    if p:
        out=nmod_mat(vand,p).inv()*nmod_mat([[v] for v in vals],p)
    else:
        out=fmpq_mat(vand).inv()*fmpq_mat([[v] for v in vals])
    G=[]
    for k in range(10):
        v=out[k,0]
        if not p and v.denominator!=1:
            raise ValueError("determinant interpolation not integral")
        G.append(int(v))
    A=[t(0,0,0),3*t(0,0,1),3*t(0,1,1),t(1,1,1)]
    left=mul(derivative(A),G,p)
    right=mul(A,derivative(G),p)
    H0=[3*left[k]-right[k] for k in range(len(left))]
    A2=mul(A,A,p)
    H=mul(mul(A2,A2,p),H0,p)
    if (H[23]%p if p else H[23])!=0:
        raise ValueError("highest-weight degree23 cancellation")
    answer=sum((-1)**k*(math.factorial(14)//math.factorial(14-k))*math.factorial(22-k)
               *linear[0]**k*linear[1]**(14-k)*H[k] for k in range(15))
    return answer%p if p else answer


def raised(linear,T,i,j,s):
    l=linear[:]
    l[j]+=s*l[i]
    U={}
    for slots in T:
        total=0
        positions=[k for k,x in enumerate(slots) if x==j]
        for bits in range(1<<len(positions)):
            a=list(slots)
            power=0
            for q,pos in enumerate(positions):
                if bits&(1<<q):
                    a[pos]=i
                    power+=1
            total+=s**power*T[tuple(sorted(a))]
        U[slots]=total
    return l,U


def main():
    started=time.monotonic()
    points=json.loads((ROOT/"results/b14_prep/points/P14.json").read_text())
    ce=points["cubic_exponents"]
    records=[]
    for pt in points["points"][:3]:
        T=tensor(ev.mixed_symbols(pt,ce))
        exact=value(pt["linear"],T,0)
        for p in [P,2147483629]:
            if value(pt["linear"],T,p)!=exact%p:
                raise ValueError("integer/modular Hessian control")
        v=exact%P
        for i in range(8):
            l,U=raised(pt["linear"],T,i,i+1,2)
            if value(l,U,P)!=v:
                raise ValueError("highest-weight raising control")
        weights=[25,17]+[2]*7
        for i in range(9):
            l=[x*(2 if j==i else 1) for j,x in enumerate(pt["linear"])]
            U={a:x*2**a.count(i) for a,x in T.items()}
            if value(l,U,P)!=v*pow(2,weights[i],P)%P:
                raise ValueError("torus weight control")
        if value([2*x for x in pt["linear"]],{a:3*x for a,x in T.items()},P)!=v*pow(6,14,P)%P:
            raise ValueError("bidegree control")
        records.append(dict(point_id=pt["id"],integer_value=str(exact)))
    if not any(int(r["integer_value"]) for r in records):
        raise ValueError("Hessian member liveness zero")
    row=[value(pt["linear"],tensor(ev.mixed_symbols(pt,ce)),P) for pt in points["points"][:192]]
    pilot=json.loads((OUT/"pilot.json").read_text())
    rank=int(nmod_mat(pilot["rows_mod_p"]+[row],P).rank())
    rec=dict(status="CANDIDATE",kind="hessian_transvectant",prime=P,point_indices=list(range(192)),
             point_ids=[pt["id"] for pt in points["points"][:192]],row_mod_p=row,
             rank_before=pilot["rank_mod_p"],rank_with_member=rank,controls=records,
             formula="A^4(3 Aprime G-A Gprime); k coefficient (-1)^k(14!/(14-k)!)(22-k)! ell0^k ell1^(14-k)",
             degree=14,variables=9,partition=[25,17]+[2]*7,wall_seconds=time.monotonic()-started,
             program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (OUT/"hessian_member.json").write_text(json.dumps(rec,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(rank_before=rec["rank_before"],rank_with_member=rank,seconds=rec["wall_seconds"])),flush=True)


if __name__=="__main__":
    main()
