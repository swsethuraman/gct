"""Exact n-degree-two flag harmonic projector; bounded B16-06 control."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parents[1]/'results/b16_06'
A,B,N=63,15,10
# (powers u,v,C,D_a,D_b), C=b.d_a, applied right to left to F.
BASIS=[(0,0,0,0,0)]
for q in (1,2):
    for i in range(q+1):
        j=q-i
        for l in range(q+1):
            m=q-l;k=i-l
            if k>=0:BASIS.append((i,j,k,l,m))

def derivative(key,which):
    i,j,k,l,m=key; out=defaultdict(int)
    def add(v,c):
        if min(v)>=0 and v[3]+v[4]<=2:out[v]+=c
    if which=='a':
        add((i,j,k,l+1,m),1)
        add((i-1,j,k,l,m),i*(N+i+j-1+A-l-k+2-l-m))
        add((i,j-1,k+1,l,m),j)
    else:
        add((i,j,k,l,m+1),1)
        add((i,j,k-1,l+1,m),k)
        add((i,j-1,k,l,m),j*(N+i+j-1+B-m+k+2-l-m))
        add((i-1,j,k,l-1,m+1),-i*l)
        add((i-1,j,k-1,l,m),i*k*(A-B-l+m-k+1))
    return {v:c for v,c in out.items() if c}

def solve():
    equations=[]
    for which in ('a','b'):
        cols=[derivative(x,which) for x in BASIS]
        keys=sorted(set().union(*cols))
        equations += [[d.get(k,0) for d in cols] for k in keys]
    mat=sp.Matrix(equations)
    ns=mat.nullspace();assert len(ns)==1
    coeff=[Q(x/ns[0][0]) for x in ns[0]]
    assert coeff[0]==1
    # Actual contraction G(a,a,d_n,d_n) on c=1, depressed chart.
    # coordinates A_R3,T2_R3,S5,s2*S7; trace formulas proved in report.
    v={
      (0,0,0,0,0):[2,Q(1,3),0,0],
      (1,0,0,1,0):[256,0,Q(-4,3),Q(8,3)],
      (1,0,1,0,1):[0,0,-20,40],
      (0,1,0,0,1):[0,0,0,Q(-2,9)],
      (2,0,0,2,0):[16128,128,-200,400],
      (2,0,1,1,1):[0,0,-1720,Q(10192,3)],
      (2,0,2,0,2):[0,0,-6160,Q(34144,3)],
      (1,1,0,1,1):[0,0,0,0],
      (1,1,1,0,2):[0,0,0,0],
      (0,2,0,0,2):[0,0,0,Q(-44,9)],
    }
    image=[sum(c*v[k][j] for k,c in zip(BASIS,coeff)) for j in range(4)]
    return dict(status='EXACT_FORMAL_PROJECTOR_REQUIRES_TRACE_PROOF',dimension=N,
        degrees_a_b_n=[A,B,2],basis=[list(k) for k in BASIS],coefficients=list(map(str,coeff)),
        harmonic_matrix=equations,rank=mat.rank(),
        contraction_labels=['A_R3','T2_R3','S5','s2_S7'],
        contraction_columns=[[str(t) for t in v[k]] for k in BASIS],
        contraction_image=list(map(str,image)))

def small_polynomial_control():
    """Independent differentiation of the harmonic projector, dimension 3.

    This builds ordinary polynomials, with no use of derivative() for checking.
    Includes incidence representatives and a deliberately corrupted coefficient.
    """
    global A,B,N
    old=A,B,N;A,B,N=4,2,3
    try: co=list(map(Q,solve()['coefficients']))
    finally:A,B,N=old
    a=sp.symbols('a0:3');b=sp.symbols('b0:3');n=sp.symbols('n0:3')
    u=sum(x*y for x,y in zip(a,n));v=sum(x*y for x,y in zip(b,n))
    base=(a[0]*b[1]-a[1]*b[0])**2*a[0]**2
    F=sp.expand(base*(n[0]+2*n[1]+3*n[2])**2)
    da=lambda z:sp.expand(sum(sp.diff(z,a[i],n[i]) for i in range(3)))
    db=lambda z:sp.expand(sum(sp.diff(z,b[i],n[i]) for i in range(3)))
    cc=lambda z:sp.expand(sum(b[i]*sp.diff(z,a[i]) for i in range(3)))
    raising=lambda z:sp.expand(sum(a[i]*sp.diff(z,b[i]) for i in range(3)))
    terms=[]
    for i,j,k,l,m in BASIS:
        z=F
        for _ in range(m):z=db(z)
        for _ in range(l):z=da(z)
        for _ in range(k):z=cc(z)
        terms.append(sp.expand(u**i*v**j*z))
    H=sp.expand(sum(sp.Rational(x.numerator,x.denominator)*z for x,z in zip(co,terms)))
    assert da(H)==db(H)==raising(H)==0
    assert H!=0
    assert da(H+terms[1])!=0 or db(H+terms[1])!=0
    assert sp.expand((H-F).subs(dict(zip(n,(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])))))==0
    return dict(dimension=3,degrees=[4,2,2],input_terms=len(sp.Poly(F).terms()),
        output_terms=len(sp.Poly(H).terms()),ordinary_derivatives_zero=True,
        incidence_class_preserved=True,changed_coefficient_rejected=True)

if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    out=solve();(OUT/'projector.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('basis','coefficients','contraction_image')}))
