"""Independent exact arithmetic checks using 15-entry exponent monomials.

Does not import the producer. Rebuilds Casimir action and projected values
from coefficient definitions; FLINT is used for rational matrix arithmetic.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import factorial, prod
from pathlib import Path
import copy
import json
from flint import fmpq_mat

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'results/b15_07'
A = tuple((a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1))
AI = {a:i for i,a in enumerate(A)}


def check(ok, why):
    if not ok:
        raise ValueError(why)


def powers(indices):
    return tuple(indices.count(j) for j in range(15))


def unpack(terms):
    return {powers(indices): F(c) for indices,c in terms}


def plus(*polys):
    out = Counter()
    for p in polys:
        for m,c in p.items():
            out[m] += c
    return {m:c for m,c in out.items() if c}


def times(p,c):
    return {m:v*c for m,v in p.items() if v*c}


def derivative(p,i,j):
    out = Counter()
    for m,c in p.items():
        if i == j:
            out[m] += c*sum(m[k]*A[k][i] for k in range(15))
            continue
        for k,power in enumerate(m):
            if not power or not A[k][j]:
                continue
            beta=list(A[k]); beta[i]+=1; beta[j]-=1
            mm=list(m); mm[k]-=1; mm[AI[tuple(beta)]]+=1
            out[tuple(mm)] += c*power*(A[k][i]+1)
    return {m:c for m,c in out.items() if c}


def central(p):
    return plus(*(derivative(derivative(p,j,i),i,j) for i in range(3) for j in range(3)))


def matrix(polys,basis):
    return fmpq_mat([[str(p.get(m,0)) for p in polys] for m in basis])


def eye(n):
    return fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])


def fresh_projection(basis,spectrum,value):
    c=matrix([central({m:F(1)}) for m in basis],basis)
    unit=eye(len(basis)); p=unit
    for s in spectrum:
        if s != value:
            p=(c-unit*s)*p/(value-s)
    return c,p


def apply(p,basis,polynomial):
    v=p*matrix([polynomial],basis)
    return {m:F(str(v[i,0])) for i,m in enumerate(basis) if v[i,0]}


def value(p,point):
    return sum(c*prod(F(v)**k for v,k in zip(point,m)) for m,c in p.items())


def multiply(p,q):
    out=Counter()
    for m,c in p.items():
        for n,v in q.items():
            out[tuple(a+b for a,b in zip(m,n))]+=c*v
    return {m:c for m,c in out.items() if c}


def tensor_checks(d3):
    source=[unpack(p) for p in d3['source_basis']]
    rec=d3['normalized_pieri_tensor']
    pairs=[]
    for i,j in rec['labels']:
        m=[0]*15; m[j]=1; pairs.append((source[i],{tuple(m):F(1)}))
    def check_tensor(pairs,coeffs):
        for i,j in ((0,1),(1,2)):
            raised=Counter()
            for (p,q),t in zip(pairs,coeffs):
                for m,c in derivative(p,i,j).items():
                    for n,v in q.items():
                        raised[(m,n)]+=t*c*v
                for m,c in p.items():
                    for n,v in derivative(q,i,j).items():
                        raised[(m,n)]+=t*c*v
            check(not any(raised.values()),'tensor highest-weight equations')
        return plus(*(times(multiply(p,q),t) for (p,q),t in zip(pairs,coeffs)))
    coeffs=list(map(F,rec['coefficients']))
    check(next(v for v in coeffs if v)==1,'Pieri normalization')
    check(check_tensor(pairs,coeffs)==unpack(rec['image']),'Pieri multiplication image')
    mult=json.loads((OUT/'tensor_multiplicity.json').read_text())
    pairs4=[(source[i],source[j]) for i,j in mult['pairs']]
    coeff4=[[F(v) for v in row] for row in mult['tensor_hw_basis']]
    check(fmpq_mat(mult['tensor_hw_basis']).rank()==3,'three tensor directions')
    images=[check_tensor(pairs4,t) for t in coeff4]
    check(images==[unpack(p) for p in mult['image_polynomials']],'repeated tensor products')
    support=sorted(set().union(*(p.keys() for p in images)))
    check(matrix(images,support).rank()==2,'repeated tensor image rank')
    return dict(pieri_domain_hw_dimension=1,repeated_tensor_hw_dimension=3,
                repeated_product_hw_rank=2,repeated_multiplication_kernel_dimension=1)


def verify(d3,d4):
    check(d3['coefficient_variables']==[list(a) for a in A], 'coefficient indexing')
    source=[unpack(p) for p in d3['source_basis']]
    generator=unpack(d3['source_generator'])
    for word,s in zip(d3['source_lowering_words'],source):
        rebuilt=generator
        for i,j in word:
            rebuilt=derivative(rebuilt,i,j)
        check(s==rebuilt,'lowering word source definition')
    source_monomials=sorted(set().union(*(s.keys() for s in source)))
    check(matrix(source,source_monomials).rank()==60,'independent source module dimension')
    fresh={}; total=0
    for record in d3['projector_blocks']:
        basis=[powers(m) for m in record['basis']]
        c,p=fresh_projection(basis,d3['envelope_spectrum'],64)
        check(c==fmpq_mat(record['casimir']),'Casimir entries')
        check(p==fmpq_mat(record['projector']),'projection entries')
        check(p*p==p and c*p==p*64,'projector normalization')
        fresh[tuple(record['weight'])]=(basis,p)
        total+=p.rank()
    check(total==27,'projector rank')
    product_rank=0
    for record in d3['product_blocks']:
        basis,p=fresh[tuple(record['weight'])]; columns=[]
        for sj,vj in record['labels']:
            multiplied={}
            for m,c in source[sj].items():
                mm=list(m); mm[vj]+=1; multiplied[tuple(mm)]=c
            columns.append(multiplied)
        result=p*matrix(columns,basis)
        check(result==fmpq_mat(record['matrix']),'fresh product values')
        product_rank+=result.rank()
    check(product_rank==27,'product image rank')
    w=d3['witness']; sj,vj=w['source_index'],w['coefficient_index']
    multiplied={}
    for m,c in source[sj].items():
        mm=list(m); mm[vj]+=1; multiplied[tuple(mm)]=c
    image=apply(fresh[(6,4,2)][1],fresh[(6,4,2)][0],multiplied)
    check(image==unpack(w['polynomial']),'witness polynomial')
    check(value(image,w['point'])==F(w['value'])!=0,'fresh exact evaluation')
    hw=unpack(d3['highest_weight_polynomial'])
    check(not derivative(hw,0,1) and not derivative(hw,1,2),'three-row highest weight')
    # Full Lie algebra bracket identities on all 15 coefficient generators.
    for k in range(15):
        m=[0]*15; m[k]=1; f={tuple(m):F(1)}
        for i in range(3):
            for j in range(3):
                for a in range(3):
                    for b in range(3):
                        lhs=plus(derivative(derivative(f,a,b),i,j),times(derivative(derivative(f,i,j),a,b),-1))
                        rhs=plus(times(derivative(f,i,b),int(j==a)),times(derivative(f,a,j),-int(i==b)))
                        check(lhs==rhs,'Lie algebra representation convention')
    # An exact finite unipotent action, including both source and multiplier.
    def exponential(poly,i,j):
        terms=[]; cur=poly; k=0
        while cur:
            terms.append(times(cur,F(1,factorial(k))))
            cur=derivative(cur,i,j); k+=1
            check(k<30,'nilpotent action degree')
        return plus(*terms)
    shifted=exponential(multiplied,2,1); projected={}
    grouped={}
    for m,c in shifted.items():
        wt=tuple(sum(m[k]*A[k][i] for k in range(15)) for i in range(3))
        grouped.setdefault(wt,{})[m]=c
    for wt,poly in grouped.items():
        if wt in fresh:
            basis,p=fresh[wt]; projected=plus(projected,apply(p,basis,poly))
    check(projected==exponential(image,2,1),'finite GL shear equivariance')
    hs=[unpack(p) for p in d4['highest_weight_basis']]
    basis4=[powers(m) for m in d4['basis']]
    c4,p4=fresh_projection(basis4,d4['envelope_spectrum'],136)
    check(c4==fmpq_mat(d4['casimir']) and p4==fmpq_mat(d4['projector']),'degree-four projection')
    check(matrix(hs,basis4).rank()==2 and all(apply(p4,basis4,h)==h for h in hs),'two multiplicity copies')
    check(all(not derivative(h,0,1) and not derivative(h,1,2) for h in hs),'degree-four highest weights')
    veronese=[F(24,prod(factorial(v) for v in a)) for a in A]
    check(all(value(s,veronese)==0 for s in source),'source Veronese ideal')
    check(value(image,veronese)==0,'image Veronese ideal')
    return dict(source_dimension=60,projector_dimension=total,product_dimension=product_rank,
                repeated_multiplicity=2,coefficient_Lie_brackets=1215,finite_shear_checked=True)


def main():
    d3=json.loads((OUT/'degree3.json').read_text()); d4=json.loads((OUT/'degree4.json').read_text())
    summary=verify(d3,d4); summary['tensor_checks']=tensor_checks(d3); negatives=[]
    for name,mutate in [
        ('changed projector entry',lambda d: d['projector_blocks'][0]['projector'][0].__setitem__(0,'999')),
        ('changed polynomial source',lambda d: d['source_generator'][0].__setitem__(1,'999')),
        ('changed point',lambda d: d['witness']['point'].__setitem__(0,999)),
        ('changed product coefficient',lambda d: d['product_blocks'][0]['matrix'][0].__setitem__(0,'999'))]:
        changed=copy.deepcopy(d3); mutate(changed)
        try:
            verify(changed,d4)
        except ValueError as exc:
            negatives.append(dict(name=name,rejected=True,reason=str(exc)))
        else:
            raise ValueError('independent verifier accepted defect: '+name)
    result=dict(status='EXACT',checks='PASS',independent_representation='15-entry power monomials',
                fresh_checks=summary,negative_controls=negatives,
                scope='Fresh polynomial and operator replay; no determinant/padded geometric evaluation')
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':
    main()
