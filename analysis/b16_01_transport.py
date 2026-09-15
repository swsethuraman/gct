"""Small exact coefficient/weight receiver for the B16-01 transport proof."""
from collections import defaultdict
import gzip
import hashlib
import json
import os
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b16_01'

def add(*polys):
    ans=defaultdict(int)
    for P in polys:
        for m,c in P.items():ans[m]+=c
    return {m:c for m,c in ans.items() if c}

def scale(P,a):return {m:c*a for m,c in P.items() if c*a}

def mul(P,Q):
    ans=defaultdict(int)
    for x,a in P.items():
        for y,b in Q.items():ans[tuple(u+v for u,v in zip(x,y))]+=a*b
    return {m:c for m,c in ans.items() if c}

def records(P):return [[list(m),c] for m,c in sorted(P.items())]

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    assert time.monotonic()+3<float(os.environ['CI73_DEADLINE'])
    start=time.monotonic()
    c,A,B,h=({tuple(int(i==j) for i in range(4)):1} for j in range(4))
    Ap=add(A,scale(mul(c,h),4))
    Bp=add(B,scale(mul(A,h),3),scale(mul(c,mul(h,h)),6))
    v=add(scale(mul(c,B),8),scale(mul(A,A),-3))
    vp=add(scale(mul(c,Bp),8),scale(mul(Ap,Ap),-3))
    difference=add(vp,scale(v,-1));assert difference=={}
    wrong=add(scale(mul(c,B),8),scale(mul(A,A),-2))
    wrongp=add(scale(mul(c,Bp),8),scale(mul(Ap,Ap),-2))
    assert add(wrongp,scale(wrong,-1)), 'A wrong coefficient must fail shear invariance'
    for m in v:
        assert sum(m[:3])==2 and m[3]==0
        assert (4*m[0]+3*m[1]+2*m[2],m[1]+2*m[2])==(6,2)
    certfile=OUT/'certificate.json.gz'
    cert=json.loads(gzip.decompress(certfile.read_bytes()))
    rows=[]
    for cell,q in zip(cert['cells'],(1,2,2,5)):
        d,t,U=cell['d'],cell['t'],cell['exact_source_dimension']
        k=(19-t)//2;j=35-d-2*k
        assert k>=0 and j>=0 and 2*k==19-t
        target=[cell['lam'][0]+4*j+6*k,t+2*k]+cell['lam'][2:]
        assert d+j+2*k==35 and target==[105,19]+[2]*8
        rows.append(dict(d=d,t=t,lam=cell['lam'],exact_source_dimension=U,padding_ceiling=U,
                         inherited_det_ideal_floor=q,transported_det_ideal_upper=11,
                         u_exponent=j,v_exponent=k,positive_certificate_requires_padding_rank='a-'+str(q)+'+1',
                         necessary_ambient_upper_using_this_floor=U+q-1,
                         sufficient_ambient_floor_for_exclusion=U+11))
    data=dict(status='PASS',monomial_order=['c','A','B','h'],v=records(v),v_after_shear=records(vp),
              exact_difference=records(difference),wrong_coefficient_difference=records(add(wrongp,scale(wrong,-1))),
              cells=rows,source_certificate_sha256=digest(certfile),
              proof_sha256=digest(ROOT/'docs/b16_01_proof.md'),script_sha256=digest(__file__),
              inherited_stable_det_ideal_dimension=11,finite_ambient_counts_computed=False,
              padding_image_ranks_computed=False,seconds=time.monotonic()-start)
    (OUT/'transport.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','cells':rows,'seconds':data['seconds']}))

if __name__=='__main__':main()
