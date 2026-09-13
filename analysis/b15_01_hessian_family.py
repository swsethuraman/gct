"""A fixed36-member integral Hessian/transvectant family in N14.

This is a small exact construction control, not a numerical heavy job.
The cubic constituents have weights (26-s,2+s,2^7), 1<=s<=9.
"""
import json
import math
from pathlib import Path
import sys
import time

import b15_01_hessian as h
from flint import fmpq_mat,fmpz_mat,nmod_mat

PARAMS=[(r,s) for r in range(1,6) for s in range(1,min(3*r,9)+1)]


def falling(n,k):
    return math.factorial(n)//math.factorial(n-k) if n>=k>=0 else 0


def binary_derivative(f,D,dx,dy):
    return [falling(D-m,dx)*falling(m,dy)*f[m] for m in range(dy,len(f))]


def family(linear,T,p=h.P):
    def t(i,j,k):
        return T[tuple(sorted((i,j,k)))]
    vals=[]
    for x in range(10):
        M=[[t(i,j,0)+x*t(i,j,1) for j in range(9)] for i in range(9)]
        vals.append(int(nmod_mat(M,p).det() if p else fmpz_mat(M).det()))
    V=[[x**k for k in range(10)] for x in range(10)]
    g=(nmod_mat(V,p).inv()*nmod_mat([[x] for x in vals],p) if p else
       fmpq_mat(V).inv()*fmpq_mat([[x] for x in vals]))
    if not p and any(g[k,0].denominator!=1 for k in range(10)):
        raise ValueError("nonintegral determinant polynomial")
    G=[int(g[k,0]) for k in range(10)]
    A=[t(0,0,0),3*t(0,0,1),3*t(0,1,1),t(1,1,1)]
    powers=[[1]]
    for r in range(5):
        powers.append(h.mul(powers[-1],A,p))
    out=[]
    for r,s in PARAMS:
        terms=[]
        for k in range(s+1):
            term=h.mul(binary_derivative(powers[r],3*r,s-k,k),binary_derivative(G,9,k,s-k),p)
            terms.append([(-1)**k*math.comb(s,k)*v for v in term])
        Q=[sum(row[k] if k<len(row) else 0 for row in terms) for k in range(max(map(len,terms)))]
        Q=h.mul(Q,powers[5-r],p)
        L=24-2*s;j=15-s
        if any((v%p if p else v)!=0 for v in Q[L+1:]):
            raise ValueError("transvectant degree bound")
        Q += [0]*max(0,j+1-len(Q))
        value=sum((-1)**k*falling(j,k)*math.factorial(L-k)*linear[0]**(14-j+k)*linear[1]**(j-k)*Q[k]
                  for k in range(j+1))
        out.append(value%p if p else value)
    return out


def main():
    started=time.monotonic()
    pts=json.loads((h.ROOT/"results/b14_prep/points/P14.json").read_text())
    points=pts["points"][:192]
    tensors=[h.tensor(h.ev.mixed_symbols(pt,pts["cubic_exponents"])) for pt in points]
    cols=[family(pt["linear"],T) for pt,T in zip(points,tensors)]
    exact=family(points[0]["linear"],tensors[0],0)
    if [x%h.P for x in exact]!=cols[0]:
        raise ValueError("integer family control")
    for i in range(8):
        l,T=h.raised(points[0]["linear"],tensors[0],i,i+1,2)
        if family(l,T)!=cols[0]:
            raise ValueError("family raising control")
    rows=[list(x) for x in zip(*cols)]
    pilot=json.loads((h.OUT/"pilot.json").read_text())
    kept=[];current=pilot["rows_mod_p"][:]
    for i,row in enumerate(rows):
        rank=int(nmod_mat(current+[row],h.P).rank())
        if rank>len(current):
            kept.append(i);current.append(row)
    result=dict(status="CANDIDATE",parameters=PARAMS,rows_mod_p=rows,prime=h.P,
                rank_before=pilot["rank_mod_p"],rank_after=len(current),added_indices=kept,
                exact_point0_values=[str(x) for x in exact],raising_controls=8,
                definition="A^(5-r) times binary transvectant_s(A^r,det Hessian pencil), coupled to ell^14 by order15-s",
                seconds=time.monotonic()-started)
    (h.OUT/"hessian_family.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(rank_after=len(current),added_indices=kept,seconds=result["seconds"])),flush=True)


if __name__=="__main__":
    main()
