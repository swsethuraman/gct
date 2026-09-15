"""Standalone B16-02 receiver: rational regeneration + connected rim hooks.

Uses no producer or inherited counting module. Run -B under b15_bound.py
with --seconds 60 --memory-mb 512. No numerical approximation or CRT.
"""
from collections import Counter, defaultdict
from functools import lru_cache
import copy
import gzip
import hashlib
import json
from math import factorial
from pathlib import Path
import time
from flint import fmpq

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b16_02'


def require(ok, message):
    if not ok:
        raise ValueError(message)


@lru_cache(None)
def partitions(n, largest=None):
    if n==0:
        return ((),)
    if largest is None:
        largest=n
    return tuple((a,)+b for a in range(min(n,largest),0,-1)
                 for b in partitions(n-a,a))


def centralizer(rho):
    z=1
    for a,m in Counter(rho).items():
        z*=a**m*factorial(m)
    return z


@lru_cache(None)
def border_strips(lam, k):
    """Enumerate contained partitions; test removed squares geometrically.

    This deliberately does not use the producer's beta-number hook move.
    """
    target=sum(lam)-k
    if target<0:
        return ()
    shapes=[]
    def descend(i, remaining, ceiling, prefix):
        if i==len(lam):
            if remaining==0:
                shapes.append(prefix)
            return
        for a in range(min(lam[i],ceiling,remaining),-1,-1):
            if remaining-a>sum(min(a,x) for x in lam[i+1:]):
                continue
            descend(i+1,remaining-a,a,prefix+(a,))
    descend(0,target,lam[0],())
    hooks=[]
    for mu in shapes:
        cells={(i,j) for i,a in enumerate(lam) for j in range(mu[i],a)}
        if len(cells)!=k:
            continue
        if any({(i+1,j),(i,j+1),(i+1,j+1)}<=cells for i,j in cells):
            continue
        seen={next(iter(cells))}
        todo=list(seen)
        while todo:
            i,j=todo.pop()
            for v in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if v in cells and v not in seen:
                    seen.add(v)
                    todo.append(v)
        if len(seen)==k:
            hooks.append((tuple(x for x in mu if x),(-1)**(len({i for i,j in cells})-1)))
    return tuple(hooks)


@lru_cache(None)
def character(lam,rho):
    if not rho:
        return int(not lam)
    return sum(sign*character(mu,rho[1:]) for mu,sign in border_strips(lam,rho[0]))


def regenerate(nmax):
    logarithm=[defaultdict(fmpq) for _ in range(nmax+1)]
    for degree in (2,3,4):
        for cycles in partitions(degree):
            for dilation in range(1,nmax//degree+1):
                logarithm[degree*dilation][tuple(x*dilation for x in cycles)]+=fmpq(degree,centralizer(cycles))
    F=[{():fmpq(1)}]
    for n in range(1,nmax+1):
        row=defaultdict(fmpq)
        for k in range(1,n+1):
            for x,a in logarithm[k].items():
                for y,b in F[n-k].items():
                    row[tuple(sorted(x+y,reverse=True))]+=a*b
        F.append({rho:a/n for rho,a in row.items() if a})
    return F


def read(name):
    raw=(OUT/name).read_bytes()
    if name.endswith('.gz'):
        raw=gzip.decompress(raw)
    return json.loads(raw)


def verify_certificate(cert,F):
    tail=tuple(cert['tail'])
    n=sum(tail)
    require(cert['weighted_degree']==n,'tail weight mismatch')
    require(cert['generator_degrees']==[2,3,4],'wrong generator degrees')
    rows=cert['rows_rho_numerator_denominator_character']
    keys=[tuple(row[0]) for row in rows]
    require(len(set(keys))==len(keys),'duplicate partition')
    require(set(keys)==set(F[n]),'missing or extra partition')
    total=fmpq(0)
    subtotals=defaultdict(fmpq)
    for rho,top,bottom,saved_character in rows:
        rho=tuple(rho)
        require(bottom>0,'nonpositive denominator')
        value=fmpq(top,bottom)
        require(value==F[n][rho],'coefficient mismatch')
        actual=character(tail,rho)
        require(saved_character==actual,'character mismatch')
        total+=value*actual
        subtotals[rho[0]]+=value*actual
        if character.cache_info().currsize>180000:
            character.cache_clear()
    require(total.denominator==1 and total>=0,'nonintegral/negative multiplicity')
    require(cert['a_inf']==int(total),'sum mismatch')
    expected=[[k,int(a.numerator),int(a.denominator)] for k,a in sorted(subtotals.items())]
    require(cert['signed_subtotals']==expected,'subtotal mismatch')
    return int(total)


def check_character_controls():
    for n in range(1,7):
        shapes=partitions(n)
        for lam in shapes:
            hook_product=1
            for i,width in enumerate(lam):
                for j in range(width):
                    hook_product*=width-j+sum(a>j for a in lam[i+1:])
            require(character(lam,(1,)*n)==factorial(n)//hook_product,'hook dimension')
            for mu in shapes:
                inner=sum((fmpq(character(lam,rho)*character(mu,rho),centralizer(rho))
                           for rho in shapes),fmpq(0))
                require(inner==int(lam==mu),'character orthogonality')


def main():
    start=time.perf_counter()
    inputs=read('input_hashes.json')
    for item in inputs['inputs']:
        path=Path(item['path'])
        require(hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'],
                'input hash mismatch: '+str(path))
    check_character_controls()
    F=regenerate(35)
    counts={}
    for t in (15,17,19):
        counts[t]=verify_certificate(read(f'count_t{t}.json.gz'),F)
        print(json.dumps({'receiver_tail':t,'a':counts[t]}),flush=True)
    expected_cells=[(23,15,1,158),(25,17,2,218),(26,17,2,218),(27,19,5,288)]
    summary=read('census.json')
    require(len(summary['rows'])==4,'wrong finite scope')
    for row,(d,t,q,h) in zip(summary['rows'],expected_cells):
        n=t+16
        require(2*d-n+2>t,'finite-stability hypothesis fails')
        require(row['degree']==d and row['lambda']==[4*d-n,t]+[2]*8,'wrong finite cell')
        a=counts[t]
        require(row['a']==a and row['finite_equals_stable'],'finite count mismatch')
        require(row['given_global_det_floor']==q and row['source_ceiling']==h,'premise changed')
        require(row['inherited_full_det_ideal_upper']==11,'ideal upper changed')
        require(row['padded_ideal_lower']==a-h,'padding ideal arithmetic')
        require(row['D_upper']==11+h-a<0,'exclusion arithmetic')
        require(row['r_needed_with_given_q']==a-q+1,'given q threshold')
        require(row['r_needed_even_at_q11']==a-10,'q11 threshold')
        require(row['q_needed_if_r_reached_source_ceiling']==a-h+1,'needed q threshold')
    # Certificate corruptions must be rejected without using saved conclusions.
    base=read('count_t15.json.gz')
    mutations=[]
    for kind in ('missing','duplicate','coefficient','character','sum'):
        bad=copy.deepcopy(base)
        rows=bad['rows_rho_numerator_denominator_character']
        if kind=='missing': rows.pop()
        if kind=='duplicate': rows.append(copy.deepcopy(rows[0]))
        if kind=='coefficient': rows[0][1]+=1
        if kind=='character': rows[0][3]+=1
        if kind=='sum': bad['a_inf']+=1
        try:
            verify_certificate(bad,F)
        except ValueError:
            mutations.append(kind)
        else:
            raise ValueError('mutation accepted: '+kind)
    result={'status':'PASS','fresh_exact_counts':counts,'finite_cells_checked':4,
            'character_method':'connected skew border strips, no beta-number moves',
            'arithmetic_backend':'python-flint fmpq, independently reconstructed recurrence',
            'character_controls':'hook dimensions and full orthogonality through6',
            'input_hashes_checked':len(inputs['inputs']),'mutation_rejections':mutations,
            'elapsed_seconds':time.perf_counter()-start,
            'inherited_geometry_recomputed':False,
            'finite_stability_proof':'docs/b16_02_proof.md; human argument plus producer direct controls',
            'independence_limit':'same mathematical exponential recurrence; different code/backend and rim-hook enumeration'}
    (OUT/'receiver.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
