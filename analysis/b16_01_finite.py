"""B16-01: exact finite cubic source dimensions, never padding image ranks.

Run with -B through inspected analysis/b15_bound.py (60 s, 512 MiB).
Pure standard library, no imported producer, no children or numerical threads.
Attribution: symmetric-function Newton recurrence and Murnaghan--Nakayama
are standard; retained Dream_Upper288 and B15-01 dimension code informed the
audit. The finite branching/hook correction proof is in docs/b16_01_proof.md.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import json
from math import factorial
import os
from pathlib import Path
import time

WORK = Path(__file__).resolve().parents[1]
OUT = WORK / 'results/b16_01'
CELLS = ((23,15),(25,17),(26,17),(27,19))

def guard():
    if 'CI73_DEADLINE' not in os.environ:
        raise RuntimeError('Use the inspected bounded wrapper')
    if time.monotonic()+3 >= float(os.environ['CI73_DEADLINE']):
        raise RuntimeError('Incomplete: stopping before wrapper deadline')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, obj):
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(path).write_bytes(gzip.compress(raw,mtime=0) if str(path).endswith('.gz') else raw)

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)

@lru_cache(maxsize=10000)
def parts(n, cap=None):
    if n==0: return ((),)
    return tuple((a,)+tail for a in range(min(n,n if cap is None else cap),0,-1)
                 for tail in parts(n-a,a))

def z(rho):
    v=1
    for a,n in Counter(rho).items(): v*=a**n*factorial(n)
    return v

@lru_cache(maxsize=20000)
def rim(lam,k):
    if not lam:return ()
    boundary=[]; i=0; j=lam[0]-1
    while True:
        boundary.append((i,j))
        if i==len(lam)-1 and j==0:break
        if i+1<len(lam) and lam[i+1]>j:i+=1
        else:j-=1
    ans=[]
    for t in range(len(boundary)-k+1):
        segment=boundary[t:t+k]
        counts=Counter(i for i,j in segment)
        mu=tuple(a-counts[i] for i,a in enumerate(lam))
        if any(a<b for a,b in zip(mu,mu[1:])):continue
        if any(j<mu[i] for i,j in segment):continue
        ans.append((tuple(a for a in mu if a),(-1)**(len(counts)-1)))
    return tuple(ans)

@lru_cache(maxsize=100000)
def character(lam,rho):
    if not rho:return int(not lam)
    return sum(s*character(mu,rho[1:]) for mu,s in rim(lam,rho[0]))

@lru_cache(maxsize=100000)
def beta_character(lam,rho):
    if not rho:return int(not lam)
    length=len(lam); beads=[a+length-1-i for i,a in enumerate(lam)]
    answer=0
    for a in beads:
        b=a-rho[0]
        if b<0 or b in beads:continue
        moved=sorted([x for x in beads if x!=a]+[b],reverse=True)
        mu=tuple(x-(length-1-i) for i,x in enumerate(moved))
        answer+=(-1)**sum(b<x<a for x in beads)*beta_character(tuple(x for x in mu if x),rho[1:])
    return answer

def multiply(A,B):
    C=defaultdict(Q)
    for a,x in A.items():
        for b,y in B.items(): C[tuple(sorted(a+b,reverse=True))]+=x*y
    return {rho:x for rho,x in C.items() if x}

@lru_cache(maxsize=100)
def hpleth(k,j):
    """Independent outer-partition definition of h_k[h_j]."""
    C=defaultdict(Q)
    for outer in parts(k):
        term={():Q(1)}
        for r in outer:
            term=multiply(term,{tuple(r*x for x in inner):Q(1,z(inner)) for inner in parts(j)})
        for rho,x in term.items():C[rho]+=x/z(outer)
    return dict(C)

def series(nmax):
    """Weight-graded exponential Newton recurrence for Sym(Sym2+Sym3)."""
    L=[defaultdict(Q) for _ in range(nmax+1)]
    for j in (2,3):
        for r in range(1,nmax//j+1):
            for rho in parts(j):L[j*r][tuple(r*x for x in rho)]+=Q(j,z(rho))
    F=[{():Q(1)}]
    for n in range(1,nmax+1):
        guard(); row=defaultdict(Q)
        for m in range(1,n+1):
            for rho,x in L[m].items():
                for tau,y in F[n-m].items():row[tuple(sorted(rho+tau,reverse=True))]+=x*y
        F.append({rho:x/n for rho,x in row.items() if x})
    return F

def inner(A,beta):
    return sum((v*character(beta,rho) for rho,v in A.items()),Q(0))

@lru_cache(maxsize=200)
def finite_branch(d,w):
    """Full finite branching and first-row Weyl factor, controls only."""
    result=defaultdict(Q)
    for k2 in range(min(d,w//2)+1):
        for k3 in range(min(d-k2,w//3)+1):
            v=2*k2+3*k3
            if v>w:continue
            for k1 in range(min(d-k2-k3,w-v)+1):
                j=w-v-k1
                E={rho:Q((-1)**(j-len(rho)),z(rho)) for rho in parts(j)}
                term=multiply(multiply(hpleth(k1,1),E),multiply(hpleth(k2,2),hpleth(k3,3)))
                for rho,c in term.items():result[rho]+=(-1)**j*c
    return {rho:c for rho,c in result.items() if c}

def controls(F):
    records=[]
    for w in range(13):
        direct=defaultdict(Q)
        for k2 in range(w//2+1):
            if (w-2*k2)%3:continue
            for rho,c in multiply(hpleth(k2,2),hpleth((w-2*k2)//3,3)).items():direct[rho]+=c
        assert dict(direct)==F[w]
    for n in range(1,7):
        for lam in parts(n):
            for mu in parts(n):
                assert sum(Q(character(lam,r)*character(mu,r),z(r)) for r in parts(n))==int(lam==mu)
    for d in range(1,7):
        direct=hpleth(d,3)
        for w in range(min(8,3*d)+1):
            guard()
            for beta in parts(w):
                if beta and 3*d-w<beta[0]:continue
                lam=tuple(x for x in (3*d-w,)+beta if x)
                a=inner(direct,lam); b=inner(finite_branch(d,w),beta)
                assert a==b and a.denominator==1 and a>=0,(d,beta,a,b)
                stable=inner(F[w],beta)
                threshold=(w+(beta[0] if beta else 0))//2
                if d>=threshold:assert a==stable,(d,beta,a,stable)
                records.append(dict(d=d,beta=beta,finite=int(a),chart=int(stable),threshold=threshold))
    assert any(r['finite']!=r['chart'] for r in records),'Need a nonstable control'
    return records

def pieri(d,t):
    lam=(4*d-t-16,t)+(2,)*8
    ans=[]
    def walk(mu,remaining):
        i=len(mu)
        if i==10:
            if remaining==0 and mu[-1]==0:ans.append(tuple(v for v in mu if v))
            return
        lo=lam[i+1] if i<9 else 0
        for v in range(lo,min(lam[i],remaining)+1):walk(mu+(v,),remaining-v)
    walk((),3*d)
    expected=[(3*d-14-b,b)+(2,)*7 for b in range(2,t+1)]
    assert sorted(ans)==sorted(expected)
    return expected

def preflight():
    p=[len(parts(n)) for n in range(34)]
    l=[sum(len(parts(j)) for j in (2,3) if n and n%j==0) for n in range(34)]
    ops=sum(l[m]*p[n-m] for n in range(1,34) for m in range(1,n+1))
    estimate=2048*sum(p)
    assert ops<400000 and estimate<128*1024**2
    return dict(max_tail_weight=33,recurrence_pair_upper=ops,partition_counts=p,
                estimated_series_bytes=estimate,estimate_is_not_bound=True,
                character_cache_limits=[100000,100000,20000],
                control_full_cubic_degree_max=6,control_full_power_sum_weight_max=18,
                control_tail_weight_max=8,dense_representation_allocation=False,
                hard_memory_MiB=512,hard_wall_seconds=60,workers=1,blas_threads=1)

def produce():
    F=series(33); small=controls(F); rows=[]; terms=[]
    for b in range(2,20):
        guard(); beta=(b,)+(2,)*7; total=Q(0); arithmetic=[]
        for rho,c in sorted(F[b+14].items(),reverse=True):
            x=character(beta,rho); y=beta_character(beta,rho)
            assert x==y
            total+=c*x
            arithmetic.append([list(rho),c.numerator,c.denominator,x])
        assert total.denominator==1 and total>=0
        rows.append(dict(b=b,beta=list(beta),value=int(total),sufficient_degree=b+7,terms=len(arithmetic)))
        terms.append(dict(b=b,power_sum_and_character=arithmetic))
        character.cache_clear(); beta_character.cache_clear()
    cells=[]; checks=[]
    for d,t in CELLS:
        shapes=pieri(d,t); channel_rows=[]
        for mu in shapes:
            b=mu[1]; w=b+14; threshold=(w+b)//2; assert d>=threshold
            # Full finite correction support enumeration BEFORE any character work.
            survivors=[]; excluded=[]
            for k2 in range(w//2+1):
                for k3 in range(w//3+1):
                    v=2*k2+3*k3; k=k2+k3
                    if v>w:continue
                    assert k<=d
                    s=w-v; D=d-k
                    if s<=D:continue
                    hook=[D+1]+[1]*(s-D-1)
                    reason='first_row_exceeds_beta' if D+1>b else 'hook_not_contained'
                    if len(hook)<=8 and all(x<=y for x,y in zip(hook,(b,)+(2,)*7)):
                        survivors.append([k2,k3,hook])
                    else:excluded.append([k2,k3,hook,reason])
            assert not survivors
            channel_rows.append(dict(mu=list(mu),finite_cubic_multiplicity=rows[b-2]['value']))
            checks.append(dict(d=d,b=b,threshold=threshold,correction_survivors=survivors,excluded_hooks=excluded))
        U=sum(r['finite_cubic_multiplicity'] for r in channel_rows)
        cells.append(dict(d=d,t=t,lam=[4*d-t-16,t]+[2]*8,channels=channel_rows,
                          exact_source_dimension=U,padding_upper=U,padding_rank_claim=False))
    return dict(schema='b16_01_exact_cubic_sources_v1',preflight=preflight(),rows=rows,cells=cells,
                arithmetic=terms,finite_correction_checks=checks,small_controls=small)

def validate_certificate(actual,expected):
    if actual!=json.loads(json.dumps(expected)):
        raise ValueError('Fresh arithmetic disagrees with certificate')

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('mode',choices=('preflight','produce','verify'))
    args=parser.parse_args(); guard(); start=time.monotonic(); OUT.mkdir(exist_ok=True)
    if args.mode=='preflight':
        obj=preflight();save(OUT/'preflight.json',obj);print(json.dumps(obj));return
    manifest=read(OUT/'input_hashes.json')
    for r in manifest['files']:assert sha(r['path'])==r['sha256'],r['path']
    obj=produce(); file=OUT/'certificate.json.gz'
    if args.mode=='produce':save(file,obj)
    else:
        validate_certificate(read(file),obj)
        # A consistent digest is insufficient: edited numeric claims must fail.
        for mutation in ('source_total','character','missing_channel','image_rank'):
            altered=json.loads(json.dumps(obj))
            if mutation=='source_total':altered['cells'][0]['exact_source_dimension']+=1
            if mutation=='character':altered['arithmetic'][0]['power_sum_and_character'][0][-1]+=1
            if mutation=='missing_channel':altered['cells'][0]['channels'].pop()
            if mutation=='image_rank':altered['cells'][0]['padding_rank_claim']=True
            try:validate_certificate(altered,obj)
            except ValueError:pass
            else:raise AssertionError('Accepted altered '+mutation)
    for r in manifest['files']:assert sha(r['path'])==r['sha256'],r['path']
    report=dict(status='PASS',mode=args.mode,certificate_sha256=sha(file),
                input_hashes_sha256=sha(OUT/'input_hashes.json'),script_sha256=sha(__file__),
                seconds=time.monotonic()-start,full_plethysm_controls=len(obj['small_controls']),
                finite_source_dimensions=[c['exact_source_dimension'] for c in obj['cells']],
                padding_image_rank_proved=False,heavy_lease_used=False,
                rejected_mutations=4 if args.mode=='verify' else 0)
    save(OUT/(args.mode+'_receipt.json'),report);print(json.dumps(report),flush=True)

if __name__=='__main__':main()
