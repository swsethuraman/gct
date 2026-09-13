"""B15-03 exact counts; fresh integer Weyl DP, inherited character cross-check."""
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import math
import sys
import time
import numpy as np
from wk8_s30_pleth import pleth_p, chi
from b14_11_sizes import burnside, controls as burnside_controls

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b15_03'
OUT.mkdir(exist_ok=True)
CELLS = {'primary': (13,11,3,2,1,1,1), 'secondary': (11,8,8,2,1,1,1)}

def save(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')

@lru_cache(None)
def comps(n, r):
    if r == 1:
        return ((n,),)
    return tuple((k,)+v for k in range(n+1) for v in comps(n-k,r-1))

@lru_cache(None)
def weight(mu, d, n):
    """Unbounded multiset generating function, Python integers throughout."""
    if min(mu) < 0 or sum(mu) != d*n:
        return 0
    tail = mu[1:]
    shape = (d+1,) + tuple(v+1 for v in tail)
    f = np.zeros(shape, dtype=object)
    f[(0,)*len(shape)] = 1
    for al in comps(n, len(mu)):
        if any(x>y for x,y in zip(al,mu)):
            continue
        src = tuple(slice(0,b+1-a) for a,b in zip(al[1:],tail))
        dst = tuple(slice(a,b+1) for a,b in zip(al[1:],tail))
        for k in range(1,d+1):
            f[(k,)+dst] += f[(k-1,)+src]
    return int(f[(d,)+tail])

def exact_weyl(lam, d, n):
    r = len(lam)
    grouped = Counter()
    for perm in permutations(range(r)):
        mu = tuple(lam[i]+perm[i]-i for i in range(r))
        if min(mu) < 0:
            continue
        sign = (-1)**sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
        grouped[tuple(sorted(mu, reverse=True))] += sign
    terms = [(mu,s) for mu,s in grouped.items() if s]
    values = [(mu,s,weight(mu,d,n)) for mu,s in terms]
    result = sum(s*v for mu,s,v in values)
    assert result >= 0
    return result, {'method':'integer Weyl alternation; object-array weight DP',
                    'nonzero_grouped_terms':len(values), 'terms':values}

def exact_character(lam,d,n):
    a = sum((c*chi(lam,rho) for rho,c in pleth_p(d,n).items()), Fraction())
    assert a.denominator == 1 and a>=0
    return int(a)

def strips(lam,d):
    return [tuple(x for x in nu if x) for nu in product(*(
        range(lam[i+1] if i+1<len(lam) else 0, lam[i]+1) for i in range(len(lam))))
        if sum(nu)==sum(lam)-d]

def count(name):
    start=time.perf_counter()
    lam=CELLS[name]; d=8
    a, route = exact_weyl(lam,d,4)
    achar=exact_character(lam,d,4)
    assert a==achar
    print(json.dumps({'cell':name,'a_exact':a,'seconds':time.perf_counter()-start}),flush=True)
    channels=[]
    for nu in strips(lam,d):
        av, detail=exact_weyl(nu,d,3)
        ac=exact_character(nu,d,3)
        assert av==ac
        channels.append({'nu':nu,'cubic_multiplicity_exact':av,'weyl_grouped_terms':detail['nonzero_grouped_terms']})
    hp=sum(x['cubic_multiplicity_exact'] for x in channels)
    sizes=burnside(lam,d)
    bank=json.loads((ROOT/'results/b15_prep/small_panel_sizing.json').read_text())
    entry=next(x for x in bank['cells'] if tuple(x['target']['lam'])==lam)
    assert (a,hp,sizes['N_S'],sizes['n_chi']) == (entry['target']['a'],entry['target']['h_pad'],entry['sizing']['N_S'],entry['sizing']['n_chi'])
    sys.path.insert(0,str(ROOT/'tools/integrate'))
    from exclusion_predicates import conclusions_for
    ledger=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    hits=conclusions_for(ledger,{'n':4,'ell':len(lam),'delta':d,'lambda':list(lam)},'quartic_padded_gap')
    overlay=json.loads((ROOT/'results/b15_prep/transport_overlay.json').read_text())
    overlay_hits=[x for x in overlay.get('closed_records',[]) if x['degree']==d and tuple(x['lam'])==lam]
    overlay_hits += [x for x in overlay.get('family_extensions',[]) if tuple(x['tail'])==lam[1:] and d>=x['from_degree']]
    record={'status':'EXACT','model':'gpt-6-astra','cell':name,'n':4,'degree':d,
        'ambient_variable_count':16,'restriction_variable_count':len(lam),'lambda':lam,
        'a_exact':a,'a_lb':a,'a_ub':a,'h_pad_exact':hp,'h_pad_lb':hp,'h_pad_ub':hp,
        'i_pad_lb':0,'U_pad_ub':min(a,hp),'ambient_weyl':route,'ambient_character_exact':achar,
        'pieri_channels':channels,'signed_burnside':sizes,'scoped_ledger_hits':hits,
        'accepted_overlay_hits':overlay_hits,'wall_seconds':time.perf_counter()-start,
        'costs':{'dense_int64_square_bytes':8*sizes['n_chi']**2,
                 'expanded_monomial_int16_bytes':2*sizes['N_S']*d,
                 'kernel_uint32_bytes':4*sizes['n_chi']*a,
                 'construction_reduction_evaluation':'must be separately measured'}}
    save('counts_'+name+'.json',record)
    print(json.dumps({k:record[k] for k in ['cell','status','a_exact','h_pad_exact','U_pad_ub','wall_seconds']}),flush=True)

def controls():
    out=[]
    for d,n,lam in [(2,4,(6,2)),(2,4,(5,3)),(3,4,(6,4,2))]:
        a,_=exact_weyl(lam,d,n)
        ac=exact_character(lam,d,n)
        assert a==ac
        out.append({'lambda':lam,'degree':d,'a_exact':a,'character_agrees':True,'altered_count_rejected':a!=ac+1})
    assert out[0]['a_exact']==1 and out[1]['a_exact']==0
    save('count_controls.json',{'status':'EXACT','controls':out,'signed_burnside_controls':burnside_controls()})
    print('count controls PASS',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['controls','primary','secondary'])
    args=ap.parse_args()
    controls() if args.mode=='controls' else count(args.mode)
