"""Integral source certificate and independent native polynomial replay."""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from itertools import permutations
import argparse
import hashlib
import json
import math
import time
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_03'
LAM=(13,11,3,2,1,1,1)
P=2147483647

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n',encoding='utf-8')

def exponents(n,r):
    if r==1: return [(n,)]
    return [(j,)+x for j in range(n+1) for x in exponents(n-j,r-1)]

def reconstruct(x,p):
    if x==0: return Fraction(0)
    bound=math.isqrt(p//2)
    r0,r1,t0,t1=p,int(x),0,1
    while r1>bound:
        q=r0//r1; r0,r1=r1,r0-q*r1; t0,t1=t1,t0-q*t1
    if t1<0: r1,t1=-r1,-t1
    assert 0<t1<=bound and math.gcd(r1,t1)==1 and (r1-int(x)*t1)%p==0, ('reconstruction failed',x)
    return Fraction(r1,t1)

def carrier():
    z=np.load(OUT/'native_carrier.npz',allow_pickle=False)
    return z['M'],z['col_of'],z['sgn'],int(z['n_chi'])

def source_from_modular():
    M,col,sgn,nc=carrier()
    K=np.load(OUT/f'kernel_{P}.npz',allow_pickle=False)['K']
    mapping={int(x):reconstruct(int(x),P) for x in np.unique(K)}
    integral=np.zeros(K.shape,dtype=np.int64); scales=[]
    for j in range(2):
        den=math.lcm(*(mapping[int(x)].denominator for x in np.unique(K[:,j])))
        coeff=[int(mapping[int(x)]*den) for x in K[:,j]]
        content=math.gcd(*coeff)
        coeff=[x//content for x in coeff]
        integral[:,j]=coeff
        scales.append({'common_denominator':den,'content_divisor':content})
    rec={'status':'CANDIDATE','lambda':LAM,'degree':8,'n':4,'n_chi':nc,
         'construction':'single-prime rational reconstruction followed by exact integer verification; reconstruction alone proves nothing',
         'ordinary_coefficient_convention':'c_alpha=[x^alpha]f; E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j)',
         'source_orientation':'p_j=sum_m sign[m]*K[col[m],j]*product_k c_alpha(M[m,k])',
         'carrier':'native_carrier.npz','carrier_sha256':hashlib.sha256((OUT/'native_carrier.npz').read_bytes()).hexdigest(),
         'prime_used_for_discovery':P,'scales':scales,
         'nonzero_chi_rows':[[i,int(x),int(y)] for i,(x,y) in enumerate(integral) if x or y]}
    save('integral_source.json',rec)
    return rec,integral

def load_source():
    rec=json.loads((OUT/'integral_source.json').read_text())
    assert rec['lambda']==list(LAM) and rec['degree']==8 and rec['n']==4
    assert hashlib.sha256((OUT/rec['carrier']).read_bytes()).hexdigest()==rec['carrier_sha256']
    K=np.zeros((rec['n_chi'],2),dtype=np.int64)
    used=set()
    for i,x,y in rec['nonzero_chi_rows']:
        assert i not in used and 0<=i<len(K); used.add(i); K[i]=x,y
    return rec,K

def full_raise_Z(M,col,sgn,K):
    """All simple roots, no row quotient, modular arithmetic or inherited builder."""
    start=time.perf_counter(); r=len(LAM)
    A=np.array(exponents(4,r),dtype=np.int16); index={tuple(a):i for i,a in enumerate(A)}
    assert np.all(A[M].sum(axis=1)==np.array(LAM))
    assert np.all(np.diff(M,axis=1)>=0)
    active=np.nonzero((col>=0)&(np.any(K[np.maximum(col,0)]!=0,axis=1)))[0]
    mons=M[active]; coeff=K[col[active]]*sgn[active,None]
    assert np.all(np.isin(sgn,[-1,0,1]))
    # This bounds even a hypothetical sum of every generated contribution into one row.
    absolute_sum_bound=40*sum(abs(int(x)) for x in coeff.ravel())
    assert absolute_sum_bound<2**63
    tables=[np.array([math.comb(m+j,j+1) for m in range(len(A))],dtype=np.int64) for j in range(8)]
    assert math.comb(len(A)+7,8)<2**63
    outcomes=[]
    for i in range(r-1):
        move=np.full(len(A),-1,dtype=np.int16)
        for k,a in enumerate(A):
            if a[i+1]:
                b=a.copy(); b[i]+=1; b[i+1]-=1; move[k]=index[tuple(b)]
        code_parts=[]; value_parts=[]
        for slot in range(8):
            keep=move[mons[:,slot]]>=0
            image=mons[keep].copy()
            multiplier=(A[image[:,slot],i]+1).astype(np.int64)
            image[:,slot]=move[image[:,slot]]; image.sort(axis=1)
            codes=sum((tables[j][image[:,j]] for j in range(8)),np.zeros(len(image),dtype=np.int64))
            code_parts.append(codes); value_parts.append(coeff[keep]*multiplier[:,None])
        codes=np.concatenate(code_parts); vals=np.concatenate(value_parts)
        unique,inv=np.unique(codes,return_inverse=True)
        summed=np.zeros((len(unique),2),dtype=np.int64)
        np.add.at(summed,inv,vals)
        assert not np.any(summed),('integer raising nonzero',i)
        outcomes.append({'i':i,'j':i+1,'terms':len(codes),'image_monomials':len(unique),'exact_zero':True})
    return {'status':'EXACT','arithmetic':'Z; int64 accumulation proved safe by absolute sum bound',
            'absolute_accumulation_bound':absolute_sum_bound,'int64_signed_margin':2**63-1-absolute_sum_bound,
            'active_native_monomials':len(active),'operators':outcomes,'seconds':time.perf_counter()-start}

def product_linear(forms):
    r=len(forms[0]); co={(0,)*r:1}
    for linear in forms:
        new={}
        for al,c in co.items():
            for i,v in enumerate(linear):
                if v:
                    a=list(al); a[i]+=1; key=tuple(a)
                    new[key]=new.get(key,0)+c*v
        co=new
    return {al:c for al,c in co.items() if c}

def determinant_coefficients(pencil):
    r=len(pencil); co={}
    for perm in permutations(range(4)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        forms=[[pencil[k][i][perm[i]] for k in range(r)] for i in range(4)]
        for al,c in product_linear(forms).items(): co[al]=co.get(al,0)+sign*c
    return {al:c for al,c in co.items() if c}

def padded_coefficients(frame):
    r=len(frame); co={}
    for perm in permutations(range(3)):
        forms=[[frame[k][0] for k in range(r)]]
        forms += [[frame[k][1+3*i+perm[i]] for k in range(r)] for i in range(3)]
        for al,c in product_linear(forms).items(): co[al]=co.get(al,0)+c
    return {al:c for al,c in co.items() if c}

def evaluate_Z(M,col,sgn,K,co):
    A=exponents(4,7); cv=[co.get(a,0) for a in A]; values=[0,0]
    # Scalar Python integer multiplication, independent of the batched evaluator.
    active=np.nonzero((col>=0)&np.any(K[np.maximum(col,0)]!=0,axis=1))[0]
    for i in active:
        factors=M[i]; c=K[col[i]]
        value=int(sgn[i])
        for a in factors: value*=cv[int(a)]
        values[0]+=value*int(c[0]); values[1]+=value*int(c[1])
    return values

def minor(values):
    return values[0][0]*values[1][1]-values[0][1]*values[1][0]

def verify(mode):
    start=time.perf_counter()
    source,K=source_from_modular() if mode=='construct' else load_source()
    M,col,sgn,nc=carrier(); assert K.shape==(nc,2)
    raising=full_raise_Z(M,col,sgn,K)
    pts=json.loads((OUT/'points.json').read_text())
    values={}; minors={}
    for family,inputs,builder in [('det',pts['det_pencils'],determinant_coefficients),
                                 ('pad',pts['pad_frames'],padded_coefficients),
                                 ('diagonal',pts['diagonal_pencils'],determinant_coefficients)]:
        values[family]=[evaluate_Z(M,col,sgn,K,builder(pt)) for pt in inputs[:2]]
        minors[family]=minor(values[family])
    assert minors['det']!=0 and minors['pad']!=0
    assert values['diagonal']==[[0,0],[0,0]]
    # Exact defects: one source coefficient and one ordinary quartic coefficient.
    bad=K.copy(); first=source['nonzero_chi_rows'][0][0]; bad[first,0]+=1
    rejected=False
    try: full_raise_Z(M,col,sgn,bad)
    except AssertionError: rejected=True
    assert rejected
    c=determinant_coefficients(pts['det_pencils'][0]); altered=dict(c)
    detected=False; altered_alpha=None
    # Start with coefficient c4000000, then only letters within the weight budget.
    candidates=list(reversed([a for a in exponents(4,7) if all(x<=y for x,y in zip(a,LAM))]))
    for alpha in candidates:
        altered=dict(c); altered[alpha]=altered.get(alpha,0)+1
        if evaluate_Z(M,col,sgn,K,altered)!=values['det'][0]:
            detected=True; altered_alpha=alpha; break
    assert detected
    record={'status':'EXACT','model':'gpt-6-astra','lambda':LAM,'n':4,'degree':8,
            'source_membership':raising,'source_independence':'nonzero determinant 2x2 minor over Z',
            'values_Z':values,'minors_Z':minors,'r_det_lb':2,'r_pad_lb':2,
            'a_lb':2,'a_ub':2,'m_det_lb':2,'m_det_ub':2,'m_pad_lb':2,'m_pad_ub':2,
            'i_det_lb':0,'i_det_ub':0,'i_pad_lb':0,'i_pad_ub':0,'D_lb':0,'D_ub':0,
            'source_mutation_rejected':rejected,'point_coefficient_mutation_detected':detected,
            'altered_point_alpha':altered_alpha,'arithmetic':'Python integers for geometric evaluation and minors; no lifting premise needed',
            'seconds':time.perf_counter()-start,
            'input_sha256':{name:hashlib.sha256((OUT/name).read_bytes()).hexdigest() for name in ['integral_source.json','native_carrier.npz','points.json','counts_primary.json']},
            'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    save('exact_certificate.json' if mode=='construct' else 'standalone_replay.json',record)
    print(json.dumps({k:record[k] for k in ['status','r_det_lb','r_pad_lb','D_lb','D_ub','seconds','minors_Z']}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['construct','replay']); args=p.parse_args()
    verify(args.mode)
    if args.mode=='construct':
        verify('replay')
