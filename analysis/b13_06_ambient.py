"""Bounded exact Weyl alternation, with overflow checks before accepting counts."""
import argparse
from collections import Counter
from itertools import permutations
import json
from math import prod
from pathlib import Path
import time
import numpy as np
from b13_06_decompose import exps, schur_character


def weyl_weights(lam):
    r=len(lam); rho=list(range(r-1,-1,-1)); shifted=[lam[i]+rho[i] for i in range(r)]
    terms=Counter(); used=[False]*r; perm=[]; raw=0
    def rec(i,sign):
        nonlocal raw
        if i==r:
            mu=tuple(sorted((shifted[perm[t]]-rho[t] for t in range(r)),reverse=True))
            terms[mu]+=sign; raw+=1; return
        for j in range(r):
            if not used[j] and shifted[j]>=rho[i]:
                inversions=sum(q>j for q in perm)
                used[j]=True; perm.append(j)
                rec(i+1,sign*(-1 if inversions%2 else 1))
                perm.pop(); used[j]=False
    rec(0,1)
    return {mu:c for mu,c in terms.items() if c},raw,len(terms)


def weight_count(mu,degree):
    tail=mu[1:]; shape=(degree+1,)+tuple(v+1 for v in tail)
    entries=prod(shape)
    if entries>8_000_000: raise MemoryError('preallocation DP cap: '+str(entries))
    dp=np.zeros(shape,dtype=np.int64); dp[(0,)*len(shape)]=1
    betas=[x[1:] for x in exps(4,len(mu)) if all(x[i+1]<=tail[i] for i in range(len(tail)))]
    additions=0; max_value=1
    for beta in betas:
        src=tuple(slice(0,tail[i]+1-beta[i]) for i in range(len(tail)))
        dst=tuple(slice(beta[i],tail[i]+1) for i in range(len(tail)))
        for d in range(1,degree+1):
            block=dp[(d,)+dst]
            block+=dp[(d-1,)+src]
            # Every summand is nonnegative and <=INT64_MAX. A single sum can
            # overflow at most once and must then be negative. Fail before
            # any further use, rather than inspecting just the final entry.
            if np.any(block<0): raise OverflowError(('int64',mu,degree,beta,d))
            additions+=block.size
        max_value=max(max_value,int(dp.max()))
    return int(dp[(degree,)+tail]),dict(entries=entries,scalar_additions=additions,
                                      maximum_intermediate=max_value,overflow_checks_passed=True)


def small_controls():
    out=[]
    for r in (2,3):
        expected=Counter()
        for shape in ((8,),(6,2),(4,4)):
            expected[shape]=1
        # All partitions of 8 having at most r parts, constructed separately.
        def parts(n,maxpart,cur):
            if not n: yield tuple(cur); return
            if len(cur)==r:return
            for a in range(min(n,maxpart),0,-1): yield from parts(n-a,a,cur+[a])
        for sh in parts(8,8,[]):
            lam=sh+(0,)*(r-len(sh)); terms,_,_=weyl_weights(lam)
            a=sum(sign*weight_count(mu,2)[0] for mu,sign in terms.items())
            assert a==expected[sh],(r,sh,a)
            out.append(dict(r=r,partition=list(sh),a=a))
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--degree',type=int,required=True)
    ap.add_argument('--weight',required=True); args=ap.parse_args()
    lam=tuple(map(int,args.weight.split(','))); assert sum(lam)==4*args.degree
    root=Path('results/b13_06'); root.mkdir(parents=True,exist_ok=True)
    label=str(args.degree)+'_'+'_'.join(map(str,lam))
    path=root/('ambient_'+label+'.json'); start=time.monotonic()
    controls=small_controls(); terms,raw,distinct=weyl_weights(lam)
    record=dict(board_numbering='batch13',session_id='B13-06',partition=list(lam),degree=args.degree,
                method='integer Weyl alternation with checked int64 tail DP; Python-int signed sum',
                source_convention='ordinary coefficient c_alpha=[s^alpha]F',
                raw_weyl_terms=raw,distinct_sorted_weights=distinct,nonzero_aggregated_weights=len(terms),
                controls=controls,terms=[],complete=False)
    print(json.dumps({k:v for k,v in record.items() if k not in ('controls','terms')}),flush=True)
    acc=0
    for j,(mu,c) in enumerate(sorted(terms.items(),reverse=True)):
        value,stats=weight_count(mu,args.degree); acc+=c*value
        record['terms'].append(dict(weight=list(mu),coefficient=c,value=value,**stats))
        if j%25==0:
            record['elapsed_seconds']=time.monotonic()-start
            path.write_text(json.dumps(record,indent=2)+'\n')
            print('terms',j+1,'/',len(terms),'seconds',round(time.monotonic()-start,2),flush=True)
    assert acc>=0
    if lam[1:]==(17,)+(2,)*7: assert acc==274,(lam,acc)
    record.update(a=acc,complete=True,elapsed_seconds=time.monotonic()-start)
    path.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(partition=lam,degree=args.degree,a=acc,seconds=record['elapsed_seconds'],
                         max_dp_entries=max(t['entries'] for t in record['terms']))),flush=True)


if __name__=='__main__': main()
