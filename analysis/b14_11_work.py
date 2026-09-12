"""Exact bounded quartic census. No rank claims are inferred from census records."""
from b14_11_run import memory_limit, peak_memory
memory_limit()
import argparse, csv, hashlib, itertools, json, math, re, subprocess, time
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from wk8_s30_pleth import parts, pleth_p, chi

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'results/b14_11'; OUT.mkdir(exist_ok=True)
PRIMES=[2147483647,2147483629]
BASE='9898e56941a7665f231873481dae956f08509995'

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def key(r): return (int(r.get('n',4)),int(r['delta']),tuple(r['lam']))

def eligible(r):
    lam=r['lam']; d=r['delta']
    return (r.get('n',4)==4 and isinstance(d,int) and 1<=d<=8 and
            all(isinstance(x,int) and x>0 for x in lam) and lam==sorted(lam,reverse=True)
            and sum(lam)==4*d and 5<=len(lam)<=d and lam[0]>=d and r['a']>0)

def exact_a(lam,d,n=4):
    v=sum((c*chi(tuple(lam),rho) for rho,c in pleth_p(d,n).items()),Fraction())
    if v.denominator!=1 or v<0: raise ValueError(('invalid multiplicity',lam,d,v))
    return int(v)

def census(d,ell):
    lams=[lam for lam in parts(4*d) if len(lam)==ell and lam[0]>=d]
    assert lams
    p=pleth_p(d,4); den=math.lcm(*(c.denominator for c in p.values()))
    rows=[]; start=time.time()
    path=OUT/f'census_d{d}_l{ell}.jsonl'
    with path.open('w',encoding='utf-8') as f:
        for i,lam in enumerate(lams):
            a=exact_a(lam,d)
            row=dict(n=4,delta=d,lam=list(lam),ell=ell,a=a,status='CERTIFIED_EXACT_COMBINATORICS')
            f.write(json.dumps(row)+'\n'); rows.append(row)
            if i%32==31: chi.cache_clear(); f.flush()
    info=dict(delta=d,ell=ell,partitions=len(lams),positive=sum(r['a']>0 for r in rows),
              a1=sum(r['a']==1 for r in rows),sum_a=sum(r['a'] for r in rows),
              power_sum_terms=len(p),common_denominator=str(den),
              denominator_gcd_with_primes={str(q):math.gcd(den,q) for q in PRIMES},
              wall_seconds=round(time.time()-start,4),peak_working_set_bytes=peak_memory(),complete=True)
    save(f'census_d{d}_l{ell}_summary.json',info); print(json.dumps(info))

@lru_cache(maxsize=None)
def exponents(n,r):
    if r==1:return ((n,),)
    return tuple((i,)+t for i in range(n+1) for t in exponents(n-i,r-1))

def weight_count(lam,d,n=4):
    """Independent integer generating function DP; sparse dictionaries, no int64."""
    if any(x<0 for x in lam) or sum(lam)!=d*n:return 0
    E=[x for x in exponents(n,len(lam)) if all(a<=b for a,b in zip(x,lam))]
    F=[{} for _ in range(d+1)]; F[0][(0,)*len(lam)]=1
    for e in E:
        for k in range(1,d+1):
            for w,c in list(F[k-1].items()):
                v=tuple(a+b for a,b in zip(w,e))
                if all(a<=b for a,b in zip(v,lam)):F[k][v]=F[k].get(v,0)+c
    return F[d].get(tuple(lam),0)

def weyl_small(lam,d,n):
    r=len(lam); rho=tuple(range(r-1,-1,-1)); total=0
    for perm in itertools.permutations(range(r)):
        mu=tuple(lam[i]+rho[i]-rho[perm[i]] for i in range(r))
        if min(mu)<0:continue
        sign=(-1)**sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
        total+=sign*weight_count(mu,d,n)
    return total

def require(ok,msg):
    if not ok:raise ValueError(msg)

def validate_rows(rows):
    require(bool(rows),'empty census')
    require(len({key(r) for r in rows})==len(rows),'duplicate')
    require(all(eligible(r) for r in rows),'invalid eligibility')

def validate_rules(rules):
    require(bool(rules),'missing exclusions')
    for rule in rules:
        p=rule['predicate']
        require(not any(re.search(r'occurrence|bip|^a$|ambient',s,re.I) for s in p),'occurrence rule')
    require(any(r['id']=='n4_gate_containment' and r['predicate']=={'n':4,'r_max':4} for r in rules),'containment missing')

def controls():
    result=[]
    for n,d,lam in [(4,2,(8,)),(4,2,(6,2)),(4,2,(5,3)),(4,3,(4,4,4)),(4,3,(6,4,2))]:
        a=exact_a(lam,d,n); b=weyl_small(lam,d,n)
        require(a==b,'independent count')
        try:require(a==b+1,'corrupt independent count')
        except ValueError: rejected=True
        else: raise AssertionError('corrupt count accepted')
        result.append(dict(n=n,delta=d,lam=lam,character=a,weyl=b,corruption_rejected=rejected))
    rules=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())['exclusions'];validate_rules(rules)
    good=dict(n=4,delta=6,lam=[14,2,2,2,2,2],a=1);validate_rows([good])
    bads=[('empty',lambda:validate_rows([])),('duplicate',lambda:validate_rows([good,good])),
          ('A0',lambda:validate_rows([{**good,'a':0}])),
          ('short',lambda:validate_rows([{**good,'lam':[18,2,2,2]}])),
          ('wrong_sum',lambda:validate_rows([{**good,'lam':[15,2,2,2,2,2]}])),
          ('long',lambda:validate_rows([{**good,'lam':[12,2,2,2,2,2,2]}])),
          ('first_row',lambda:validate_rows([dict(n=4,delta=8,lam=[7,7,7,7,4],a=1)])),
          ('nonpartition',lambda:validate_rows([{**good,'lam':[2,14,2,2,2,2]}])),
          ('occurrence_rule',lambda:validate_rules(rules+[dict(predicate={'a':1})])),
          ('missing_rules',lambda:validate_rules([]))]
    rejected=[]
    for name,fn in bads:
        try:fn()
        except ValueError:rejected.append(name)
        else:raise AssertionError(name+' accepted')
    # A coefficient functional of weight (3,1) is not an HWV:
    # coefficient of x^3 y in (x+y)^4 = 4, despite essential span one.
    span=dict(form='(x+y)^4',ordinary_weight=[3,1],span=1,value=math.comb(4,1),
              false_arbitrary_weight_lemma_rejected=math.comb(4,1)!=0)
    # Correct row extension adds to first row, not a new row.
    rectangle=[dict(k=1,l=2,delta=1,lam=[4],a=exact_a((4,),1)),
               dict(k=1,l=4,delta=1,lam=[4],a=exact_a((4,),1)),
               dict(k=2,l=2,delta=2,lam=[6,2],a=exact_a((6,2),2))]
    require(exact_a((2,2),1)==0,'false s52 generator not rejected')
    save('controls.json',dict(status='PASS',independent_counts=result,A1_preserved=True,
         rejected_mutations=rejected,span_counterexample=span,rectangle_generators=rectangle,
         wrong_s52_generator_rejected=True,peak_working_set_bytes=peak_memory()))
    print('controls PASS',len(rejected),'mutations; independent Weyl and span/rectangle controls')

def inspect():
    out=[]
    for f in sorted(ROOT.joinpath('results').glob('*.jsonl')):
        if not any(s in f.name for s in ['cells','sweep','ledger']):continue
        try: rows=[json.loads(s) for s in f.read_text(encoding='utf-8').splitlines() if s]
        except (ValueError,UnicodeError):continue
        r=next((r for r in rows if isinstance(r,dict) and r.get('lam') and r.get('delta',99)<=8 and sum(r['lam'])==4*r['delta']),None)
        if r:out.append(dict(path=f.relative_to(ROOT).as_posix(),count=len(rows),keys=list(r),sample=str(r)[:1400]))
    save('historical_schemas.json',out)
    print(json.dumps([{k:v for k,v in x.items() if k!='sample'} for x in out]))

def strips(lam,d):
    """Fresh interlacing enumeration with residual-sum bounds."""
    lo=tuple(lam[1:])+(0,); out=[]
    def rec(i,left,cur):
        if i==len(lam):
            if left==0:out.append(tuple(x for x in cur if x))
            return
        for x in range(max(lo[i],left-sum(lam[i+1:])),min(lam[i],left-sum(lo[i+1:]))+1):
            rec(i+1,left-x,cur+(x,))
    rec(0,3*d,());return out

def all_census():
    rows=[]
    for d in range(5,9):
        for ell in range(5,d+1):
            summary=json.loads((OUT/f'census_d{d}_l{ell}_summary.json').read_text())
            require(summary['complete'],'incomplete census')
            group=[json.loads(s) for s in (OUT/f'census_d{d}_l{ell}.jsonl').read_text().splitlines()]
            require(len(group)==summary['partitions'],'truncated census')
            expected={lam for lam in parts(4*d) if len(lam)==ell and lam[0]>=d}
            require({tuple(r['lam']) for r in group}==expected,'census coverage')
            rows.extend(r for r in group if r['a']>0)
    validate_rows(rows);return rows

def hpad_census(d):
    start=time.time();rows=[r for r in all_census() if r['delta']==d]
    channels={tuple(r['lam']):strips(r['lam'],d) for r in rows}
    union=sorted(set(nu for v in channels.values() for nu in v))
    cubic={}
    for i,nu in enumerate(union):
        cubic[nu]=exact_a(nu,d,3)
        if i%32==31:chi.cache_clear()
    result=[dict(n=4,delta=d,lam=r['lam'],h_pad=sum(cubic[nu] for nu in channels[tuple(r['lam'])]),
                 channels=[dict(nu=nu,a3=cubic[nu]) for nu in channels[tuple(r['lam'])]],
                 status='CERTIFIED_EXACT_COMBINATORICS') for r in rows]
    (OUT/f'hpad_d{d}.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    info=dict(delta=d,rows=len(rows),distinct_cubic_labels=len(union),
              hpad_zero=sum(x['h_pad']==0 for x in result),wall_seconds=round(time.time()-start,4),
              peak_working_set_bytes=peak_memory(),complete=True)
    save(f'hpad_d{d}_summary.json',info);print(json.dumps(info))

def inventory():
    rows=all_census(); bykey={key(r):r for r in rows}; consumed=set()
    for r in rows:r.update(recorded_evidence=[],recorded_sizes=[],historical_rank_status='NOT_FOUND')
    for d in range(5,9):
        hp=json.loads((OUT/f'hpad_d{d}.json').read_text())
        require(len(hp)==sum(r['delta']==d for r in rows),'missing hpad input')
        for x in hp:bykey[key(x)]['h_pad']=x['h_pad']
    # Cross-check every overlapping ambient coefficient in the named frozen censuses.
    comparisons=[]
    for path in ['results/s42_census.json','results/s54_length5_census.json']:
        consumed.add(path);data=json.loads((ROOT/path).read_text())
        if isinstance(data,dict):data=[dict(delta=int(d),lam=lam,a=a) for d,rs in data.items() for lam,a in rs]
        count=0
        for x in data:
            if key(x) not in bykey:continue
            r=bykey[key(x)];require(r['a']==x['a'],'frozen coefficient disagreement')
            if 'h_pad' in x:require(r['h_pad']==x['h_pad'],'frozen hpad disagreement')
            if x.get('N_S') is not None:r['recorded_sizes'].append(dict(path=path,N_S=x['N_S']))
            count+=1
        require(count>0,'vacuous frozen comparison');comparisons.append(dict(path=path,matched=count))
    # Producer rank records are deduplication evidence only, not certificates.
    for path in sorted(ROOT.joinpath('results').glob('*.jsonl')):
        if not any(s in path.name for s in ['cells','sweep','ledger']):continue
        used=False
        for line,s in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
            if not s:continue
            x=json.loads(s)
            if not isinstance(x,dict) or not isinstance(x.get('delta'),int) or not x.get('lam'):continue
            if key(x) not in bykey:continue
            r=bykey[key(x)];used=True;src=path.relative_to(ROOT).as_posix()
            ns=x.get('N_S',x.get('nb'))
            if isinstance(ns,int) and ns>0:r['recorded_sizes'].append(dict(path=src,line=line,N_S=ns,n_chi=x.get('n_chi')))
            md=x.get('mult_det')
            if isinstance(md,int) and md>=0:
                require(md<=r['a'],'rank record exceeds exact ambient')
                r['recorded_evidence'].append(dict(path=src,line=line,mult_det=md,a=x.get('a'),
                     status='RECORDED_NOT_REPLAYED',certs=x.get('certs')))
        if used:consumed.add(path.relative_to(ROOT).as_posix())
    # s36's onset and A1 tables are headerless; columns are stated in s36 report.
    for name in ['s36_onset5.md','s36_aone.md']:
        path='results/'+name;consumed.add(path)
        for line,s in enumerate((ROOT/path).read_text().splitlines(),1):
            cols=[x.strip() for x in s.strip('|').split('|')]
            if len(cols)<9 or not cols[0].isdigit():continue
            lam=[int(x) for x in re.findall(r'\d+',cols[2])]
            x=dict(n=4,delta=int(cols[1]),lam=lam)
            if key(x) not in bykey:continue
            r=bykey[key(x)];md=int(cols[6]);require(md<=r['a'],'markdown rank exceeds ambient')
            r['recorded_evidence'].append(dict(path=path,line=line,mult_det=md,a=int(cols[3]),status='RECORDED_NOT_REPLAYED'))
            r['recorded_sizes'].append(dict(path=path,line=line,N_S=int(cols[4]),n_chi=int(cols[5])))
    # B13-11 normalised the earlier markdown ledgers and later JSONL runs.
    # Preserve its own replay flags and original source addresses.
    for path in sorted((ROOT/'results/b13_11').glob('ledger.part*.jsonl')):
        consumed.add(path.relative_to(ROOT).as_posix())
        for line,s in enumerate(path.read_text().splitlines(),1):
            x=json.loads(s)
            if key(x) not in bykey:continue
            r=bykey[key(x)];require(x['a']==r['a'],'B13 ambient mismatch')
            det=x.get('sides',{}).get('det',{})
            md=det.get('rank_floor')
            if isinstance(md,int):
                require(0<=md<=r['a'],'B13 rank bound')
                r['recorded_evidence'].append(dict(path=path.relative_to(ROOT).as_posix(),line=line,
                    mult_det=md,a=x['a'],status='RECORDED_NOT_REPLAYED',original_sources=det.get('evidence',[])))
            for obs in x.get('observations',[]):
                ns=obs.get('resources',{}).get('N_S')
                if isinstance(ns,int):r['recorded_sizes'].append(dict(path=obs['source'],N_S=ns,n_chi=obs['resources'].get('n_chi')))
    inherited={}
    for path in sorted((ROOT/'results/b13_11').glob('inherited_tail_closures.part*.jsonl')):
        consumed.add(path.relative_to(ROOT).as_posix())
        for line,s in enumerate(path.read_text().splitlines(),1):
            x=json.loads(s)
            if x['n']==4:inherited[tuple(x['tail'])]=dict(path=path.relative_to(ROOT).as_posix(),line=line,record=x,status='RECORDED_NOT_REPLAYED')
    # Fill remaining cost data from the reconciled queue; these fields prove no rank.
    for path in sorted((ROOT/'results/b13_11').glob('candidate_inventory.part*.jsonl')):
        consumed.add(path.relative_to(ROOT).as_posix())
        for s in path.read_text().splitlines():
            x=json.loads(s)
            if key(x) not in bykey:continue
            for res in x.get('resources',[]):
                if isinstance(res.get('N_S'),int):bykey[key(x)]['recorded_sizes'].append(dict(path=res['source'],N_S=res['N_S'],n_chi=res.get('n_chi')))
    for r in rows:
        vals={s['N_S'] for s in r['recorded_sizes']}
        # 'nb' may be a build-limited sentinel in old files; only unambiguous values price selection.
        r['recorded_N_S']=next(iter(vals)) if len(vals)==1 else None
        r['size_record_conflict']=len(vals)>1
        r['recorded_full_det']=any(e['mult_det']==r['a'] for e in r['recorded_evidence'])
        r['recorded_tail_closure']=inherited.get(tuple(r['lam'][1:]))
        r['historical_rank_status']='RECORDED_FULL_DET_NOT_REPLAYED' if r['recorded_full_det'] else ('RECORDED_PARTIAL' if r['recorded_evidence'] else 'NOT_FOUND')
        r['mathematical_status']='PROVED_D_NONPOSITIVE_HPAD_ZERO' if r['h_pad']==0 else 'OPEN_IN_THIS_AUDIT'
        r['selection_status']='EXCLUDED_HPAD_ZERO' if r['h_pad']==0 else ('DEFER_RECORDED_FULL_DET' if r['recorded_full_det'] else ('DEFER_RECORDED_TAIL_CLOSURE' if r['recorded_tail_closure'] else 'CANDIDATE'))
        r['tail_box']=(r['delta']+1)*math.prod(x+1 for x in r['lam'][1:])
    save('inventory.json',rows)
    counts=Counter(r['selection_status'] for r in rows)
    save('inventory_summary.json',dict(total=len(rows),a1=sum(r['a']==1 for r in rows),by_selection=dict(counts),
         frozen_comparisons=comparisons,consumed_historical_files=sorted(consumed),
         size_conflicts=sum(r['size_record_conflict'] for r in rows),
         status='PASS',missing_certificate_policy='retained as RECORDED; never promoted to a mathematical closure'))
    candidates=[r for r in rows if r['selection_status']=='CANDIDATE']
    candidates.sort(key=lambda r:(r['recorded_N_S'] if r['recorded_N_S'] else 10**20,r['tail_box'],key(r)))
    save('cost_queue.json',candidates)
    print('inventory',len(rows),dict(counts),'A1',sum(r['a']==1 for r in rows),'size conflicts',sum(r['size_record_conflict'] for r in rows))
    print('first queue',[(r['delta'],r['lam'],r['a'],r['h_pad'],r['recorded_N_S'],r['tail_box']) for r in candidates[:15]])

def main():
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['census','controls','inspect','hpad','inventory','sizecontrols','size','verify']);p.add_argument('--delta',type=int);p.add_argument('--ell',type=int);p.add_argument('--index',type=int)
    a=p.parse_args()
    if a.mode=='census':census(a.delta,a.ell)
    elif a.mode=='controls':controls()
    elif a.mode=='inspect':inspect()
    elif a.mode=='hpad':hpad_census(a.delta)
    elif a.mode=='inventory':inventory()
    elif a.mode=='sizecontrols':
        from b14_11_sizes import controls as size_controls
        obj=size_controls();obj['peak_working_set_bytes']=peak_memory();save('size_controls.json',obj);print(json.dumps(obj))
    elif a.mode=='verify':
        from b14_11_finish import verify
        verify(limit=False)
    else:
        from b14_11_sizes import burnside
        queue=json.loads((OUT/'cost_queue.json').read_text());selected=[];tails=set()
        for r in queue:
            tail=tuple(r['lam'][1:])
            if tail in tails:continue
            tails.add(tail);selected.append(r)
            if len(selected)==10:break
        r=selected[a.index];require(eligible(r),'invalid shortlist label')
        obj=burnside(r['lam'],r['delta']);require(obj['N_S']==r['recorded_N_S'],'N_S replay mismatch')
        obj.update(a=r['a'],h_pad=r['h_pad'],selection_index=a.index,peak_working_set_bytes=peak_memory(),
                   status='CERTIFIED_EXACT_COMBINATORICS',gap_status='OPEN',recorded_evidence=r['recorded_evidence'])
        obj['costs']=dict(dense_square_int64_bytes=8*obj['n_chi']**2,
                         dense_square_status='storage for one square only; not a process peak',
                         reduced_HWB_int64_bytes=8*obj['n_chi']*r['a'],
                         expanded_monomial_int32_bytes=4*obj['N_S']*r['delta'],
                         build_seconds_model=round(3.06e-6*obj['N_S']*r['delta']+1.07e-6*obj['stabilizer_order']*obj['N_S'],4),
                         build_model_status='EXTRAPOLATED s79/B13-09 builder only; not measured here; kernel/evaluation excluded',
                         source='docs/PROVED.md:cost_model',next_run_wall_limit_seconds=300,next_run_memory_limit_bytes=1536*1024**2,
                         kernel_runtime='UNMEASURED')
        save(f'shortlist_size_{a.index:02d}.json',obj)
        print(json.dumps({k:v for k,v in obj.items() if k not in ['classes','recorded_evidence']}))
if __name__=='__main__':main()
