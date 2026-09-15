"""Full polynomial point construction; no independently sampled jet entries.

Pad always starts with z*per3 and an invertible 10 by 10 integer substitution.
The h=8 evaluator uses its stated nine-variable restriction. A separate h=9
point check retains all ten variables and all ten independent linear forms.
"""
from collections import Counter
from itertools import permutations
from math import prod

from b15_08_bracket import det, evaluate_polynomial, sign, tensor_from_polynomials


def add(*polys,p):
    out={}
    for poly in polys:
        for mon,c in poly.items():out[mon]=(out.get(mon,0)+c)%p
    return {mon:c for mon,c in out.items() if c}


def scale(poly,s,p):return {mon:c*s%p for mon,c in poly.items() if c*s%p}


def mul(A,B,p):
    out={}
    for a,ca in A.items():
        for b,cb in B.items():
            k=tuple(sorted(a+b));out[k]=(out.get(k,0)+ca*cb)%p
    return {mon:c for mon,c in out.items() if c}


def linear(row,p):return {(i,):int(c)%p for i,c in enumerate(row) if c%p}


def matrix_polynomial(M,p,permanent=False):
    out={}
    for perm in permutations(range(len(M))):
        term={():1 if permanent else sign(perm)}
        for i,j in enumerate(perm):term=mul(term,M[i][j],p)
        out=add(out,term,p=p)
    return out


def normalize(F,h,p):
    raw=[{} for _ in range(5)]
    for mon,c in F.items():
        k=4-mon.count(0)
        tail=tuple(j-1 for j in mon if j)
        raw[k][tail]=c
    c=raw[0].get((),0)%p
    if not c:raise ValueError('point outside the nonzero leading-coefficient chart')
    g=[scale(q,pow(c,-1,p),p) for q in raw]
    g1,g2,g3,g4=g[1:]
    sq=mul(g1,g1,p)
    G2=add(g2,scale(sq,-3*pow(8,-1,p),p),p=p)
    G3=add(g3,scale(mul(g1,g2,p),-pow(2,-1,p),p),scale(mul(sq,g1,p),pow(8,-1,p),p),p=p)
    G4=add(g4,scale(mul(g1,g3,p),-pow(4,-1,p),p),scale(mul(sq,g2,p),pow(16,-1,p),p),
           scale(mul(sq,sq,p),-3*pow(256,-1,p),p),p=p)
    polys={2:G2,3:G3,4:G4}
    return tensor_from_polynomials(polys,h,p),dict(c=c,g1=g1,polys=polys,raw=F)


def det_parameters(h,rng):
    A=[[[rng.randrange(-3,4) for j in range(4)] for i in range(4)] for k in range(h)]
    for a in A:a[3][3]=-sum(a[i][i] for i in range(3))
    return dict(family='DET',A=A)


def pad_parameters(rng):
    while True:
        L=[[rng.randrange(-3,4) for j in range(10)] for i in range(10)]
        if det(L):return dict(family='PAD',L=L,independent_forms=10,integer_determinant=det(L))


def red_parameters(h,rng):
    from itertools import combinations_with_replacement
    return dict(family='RED',ell=[rng.randrange(-3,4) for _ in range(h+1)],
                cubic=[[list(idx),rng.randrange(-3,4)] for idx in combinations_with_replacement(range(h+1),3)])


def from_parameters(params,h,p):
    family=params['family']
    if family=='DET':
        A=params['A'];assert len(A)==h
        M=[[linear([int(i==j)]+[a[i][j] for a in A],p) for j in range(4)] for i in range(4)]
        F=matrix_polynomial(M,p)
    elif family=='PAD':
        L=params['L'];assert len(L)==10 and all(len(row)==10 for row in L)
        assert det(L)!=0 and h in (8,9)
        ls=[linear(row[:h+1],p) for row in L]
        F=mul(ls[0],matrix_polynomial([[ls[1+3*i+j] for j in range(3)] for i in range(3)],p,True),p)
    elif family=='RED':
        F=mul(linear(params['ell'],p),{tuple(idx):c%p for idx,c in params['cubic']},p)
    else:raise ValueError('unknown geometric family')
    return normalize(F,h,p)


def direct_value(params,x,p):
    if params['family']=='DET':
        A=params['A']
        return det([[x[0]*int(i==j)+sum(x[k+1]*a[i][j] for k,a in enumerate(A))
                     for j in range(4)] for i in range(4)],p)
    if params['family']=='PAD':
        ls=[sum(a*b for a,b in zip(row,x))%p for row in params['L']]
        return ls[0]*sum(prod(ls[1+3*i+perm[i]] for i in range(3)) for perm in permutations(range(3)))%p
    if params['family']=='RED':
        return sum(a*b for a,b in zip(params['ell'],x))*sum(c*prod(x[j] for j in idx) for idx,c in params['cubic'])%p
    raise ValueError('unknown family')


def verify_polynomial(params,meta,h,p,rng):
    for _ in range(3):
        x=[rng.randrange(-4,5) for _ in range(h+1)]
        assert evaluate_polynomial(meta['raw'],x,p)==direct_value(params,x,p)
        shift=evaluate_polynomial(meta['g1'],x[1:],p)*pow(4,-1,p)%p
        depressed=(pow(x[0],4,p)+sum(pow(x[0],4-d,p)*evaluate_polynomial(poly,x[1:],p)
                   for d,poly in meta['polys'].items()))%p
        shifted=[(x[0]-shift)%p]+x[1:]
        assert depressed==direct_value(params,shifted,p)*pow(meta['c'],-1,p)%p


def inherited_jet_control(params,point,h,p):
    """Compare genuinely regenerated B14-06 two-jets, using identical native inputs."""
    import numpy as np
    from b14_06_bracket import Jet,jet_point_list
    from b14_06_points import family_DET,_lin_jet,_per3,normalise_depress
    assert h==8
    if params['family']=='DET':
        A=np.asarray(params['A'],dtype=np.int64)[...,None]
        J,jets,_=family_DET(1,p,np.random.default_rng(1),A=A)
    elif params['family']=='PAD':
        J=Jet(h,p,1);L=np.asarray(params['L'],dtype=np.int64)[:,:9,None]
        per_s=[]
        for v in range(5):
            ls=[_lin_jet(L[t],J,v,p) for t in range(10)]
            per_s.append(J.mul(ls[0],_per3([[ls[1+3*i+j] for j in range(3)] for i in range(3)],J,p)))
        jets,c,defect,valid=normalise_depress(per_s,list(range(5)),p,J)
        assert defect==0 and valid[0]
    else:raise ValueError('unsupported inherited control family')
    old=jet_point_list(J,jets)[0]
    from b15_08_bracket import tensor_get
    for d,(s,u,N) in old.items():
        assert s==tensor_get(point,d,[])%p
        assert u==[tensor_get(point,d,[i])%p for i in range(h)]
        assert N==[[tensor_get(point,d,[i,j])%p for j in range(h)] for i in range(h)]
    return True
