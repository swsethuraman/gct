"""Universal c-adic Schur-complement certificate, through c^3 after c^8.

Works over the open set det(M2_transverse)!=0, then uses polynomial density.
Trace and Gram symbols are treated as independent: a zero formal expression
is sufficient for a universal identity; nonzero expressions alone give no
rank assertion. Exact specialized minors supply the necessary rank bounds.
"""
from pathlib import Path
import json, time, itertools
from flint import fmpq_mpoly_ctx, fmpq
from b16_04_filtration import OUT, BASIS, nullspace, encode, dump

NAMES=['c','t','s2','s3','s4','alpha','beta','gamma','z',
       'trX','trY','trXX','trXY','trXXX']
for kind in ('G','GX','GY','GXX'):
    NAMES += [f'{kind}{i}{j}' for i in range(3) for j in range(i,3)]
CTX=fmpq_mpoly_ctx.get(tuple(NAMES)); GENS=CTX.gens()
VAR=dict(zip(NAMES,GENS)); globals().update(VAR)
ZERO=CTX.constant(0) if hasattr(CTX,'constant') else CTX.from_dict({})
ONE=ZERO+1
MAX_C=3
MAX_SUPPORT=100000
PEAK=0

def trunc(p):
    global PEAK
    d={k:v for k,v in p.to_dict().items() if k[0]<=MAX_C and k[8]<=1}
    PEAK=max(PEAK,len(d)); assert len(d)<=MAX_SUPPORT,'support preflight cap'
    return CTX.from_dict(d)

def mul(a,b): return trunc(a*b)

def coeff(p,index,power):
    d={}
    for k,v in p.to_dict().items():
        if k[index]==power:
            kk=list(k); kk[index]=0; d[tuple(kk)]=v
    return CTX.from_dict(d)

def substitute(p):
    args=list(GENS); args[5]=2*(t-1)**2; args[6]=6*(t-1); args[7]=ONE*12
    return trunc(p.compose(*args))

def scalar_matrix_det(M):
    n=len(M); result=ZERO
    for perm in itertools.permutations(range(n)):
        v=ONE*((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n): v=mul(v,M[i][perm[i]])
        result+=v
    return trunc(result)

DET_SERIES=(alpha**8+c*beta*alpha**7*trX
    +c**2*(gamma*alpha**7*trY+beta**2*alpha**6*(trX**2-trXX)/2)
    +c**3*(beta*gamma*alpha**6*(trX*trY-trXY)
            +beta**3*alpha**5*(trX**3-3*trX*trXX+2*trXXX)/6))

def gram(v,w):
    result=ZERO
    for i in range(3):
        for j in range(3):
            a,b=sorted((i,j)); suffix=str(a)+str(b)
            numerator=alpha**2*VAR['G'+suffix]-c*alpha*beta*VAR['GX'+suffix]+c**2*(beta**2*VAR['GXX'+suffix]-alpha*gamma*VAR['GY'+suffix])
            result+=mul(mul(v[i],w[j]),numerator)
    return trunc(result)

def block_det(X,V,W=None):
    """det(C0)*det(X-c V C0^-1 W^T), divided by det(M2).
    V and W are coefficient rows in the three raw transverse vectors.
    """
    if W is None: W=V
    n=len(X)
    Z=[[trunc(alpha**3*X[i][j]-c*gram(V[i],W[j])) for j in range(n)] for i in range(n)]
    numerator=mul(DET_SERIES,scalar_matrix_det(Z))
    data={}
    for key,val in numerator.to_dict().items():
        assert key[5]>=3*n,'uncancelled alpha denominator'
        kk=list(key); kk[5]-=3*n; data[tuple(kk)]=val
    return CTX.from_dict(data)

def remainder(poly,divisor):
    poly=trunc(poly); m=divisor.degrees()[1]
    # Monic division in t over the truncated polynomial coefficient ring.
    for k in range(poly.degrees()[1],m-1,-1):
        lead=coeff(poly,1,k)
        if lead: poly=trunc(poly-mul(lead*t**(k-m),divisor))
    assert poly.degrees()[1]<m
    return poly

def build():
    s2k=-6+c*s2; s3k=8-2*c*s2+c**2*s3; s4k=-3+c*s2-c**2*s3+c**3*s4
    h=12*t*t+2*s2k; v0=4*t*s2k+3*s3k
    bs=2*t*t*s2k+6*t*s3k+12*s4k
    v=[4*(t-1),3*c,ZERO]
    w=[2*(t-1)*(t-3),3*c*(2*t-3),12*c*c]
    u2=[ONE,ZERO,ZERO]; u3=[ONE*fmpq(-4,3),c,ZERO]
    u4=[ONE*fmpq(1,2),-3*c/4,c*c]
    A=substitute(block_det([[bs]],[w]))
    J2=substitute(block_det([[bs,v0],[s2k,ZERO]],[w,u2],[w,v]))
    J3=substitute(block_det([[bs,v0],[s3k,ZERO]],[w,u3],[w,v]))
    D=substitute(block_det([[h,v0],[v0,bs]],[v,w]))
    Q22=-substitute(block_det([[h,v0,ZERO],[v0,bs,s2k],[ZERO,s2k,ZERO]],[v,w,u2]))
    Ts=[]
    for sd,ud,ad,bd,gd in [(s2k,u2,1,0,0),(s3k,u3,fmpq(-2,3),1,0),(s4k,u4,fmpq(1,6),fmpq(-1,2),1)]:
        wz=[trunc(a+z*b) for a,b in zip(w,ud)]
        raw=block_det([[h,v0],[v0,bs+z*sd]],[v,wz])
        Td=raw.derivative('z').subs({'z':0})
        base=raw.subs({'z':0})
        Td+=ad*base.derivative('alpha')+bd*base.derivative('beta')+gd*base.derivative('gamma')
        Ts.append(substitute(Td))
    p=t**4+s2k*t*t+s3k*t+s4k
    R=[remainder(a,p) for a in (A,J2,J3,Q22)]
    S=remainder(D,trunc(p*p)); TR=[remainder(a,p) for a in Ts]
    r=lambda i,j:coeff(R[i],1,j)
    sj=lambda j:coeff(S,1,j)
    tr=lambda i,j:coeff(TR[i],1,j)
    all14=[r(0,1),mul(s2k,r(0,3)),r(1,2),r(2,3),r(3,3),sj(3),mul(s2k,sj(5)),mul(s3k,sj(6)),mul(s4k,sj(7)),mul(s2k*s2k,sj(7)),tr(0,1),mul(s2k,tr(0,3)),tr(1,2),tr(2,3)]
    return {19:[all14[i] for i in BASIS],17:[r(0,3),tr(0,3),sj(5),mul(s2k,sj(7))],15:[sj(7)]}

def main():
    started=time.perf_counter(); families=build()
    joint=json.loads((OUT/'joint_pole_constraints.json').read_text())
    result={'formal_symbols':NAMES,'truncation_after_c8':3,'scope':'complete polynomiality constraints on the declared families for degrees23..27, when matched to specialized rank bounds','families':{}}
    for tail,polys in families.items():
        records={}
        for d in range(23,28):
            cutoff=max(0,tail+8-d)
            assert cutoff<=MAX_C+1
            necessary=joint[str(tail)][str(d)]
            checks=[]
            for vector in necessary['kernel']:
                linear=sum((p*fmpq(v) for p,v in zip(polys,vector)),ZERO)
                checks.append(all(not coeff(linear,0,k) for k in range(cutoff)))
            records[d]={'necessary_dimension_upper':necessary['dimension_upper'],'all_kernel_vectors_universally_polynomial':all(checks),'individual_checks':checks,'kernel':necessary['kernel']}
        result['families'][tail]={'polynomial_supports':[len(p.to_dict()) for p in polys],
          'coefficients':[[[list(map(int,k)),str(v)] for k,v in sorted(p.to_dict().items())] for p in polys], 'filtration':records}
    result['max_intermediate_support']=PEAK; result['wall_seconds']=time.perf_counter()-started
    dump('universal_pole_certificate.json',result)
    print(json.dumps({'wall_seconds':result['wall_seconds'],'peak_support':PEAK,'filtration':{t:f['filtration'] for t,f in result['families'].items()}}))

if __name__=='__main__': main()
