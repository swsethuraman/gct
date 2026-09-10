"""Semantic regressions for the reconciled record and the frozen computations."""
import ast
from collections import Counter
import json
from b13_11_ledger import (ROOT,Ledger,LMR,N3,PRIMES,partition,cell_key,load_record,
                          negative_record,quartic_closed_tails)
from b13_11_inventory import inherited_gap_exclusion
from b13_11_reconcile import save
from wk9_s57_lib import legacy_negative_record

checks=[]
def check(name,ok):
    checks.append(dict(name=name,ok=bool(ok)))
    if not ok: raise AssertionError(name)
def raises(name,fn):
    try:fn()
    except ValueError:check(name,True)
    else:check(name,False)

bank=load_record(); rec=negative_record(); old=legacy_negative_record()
check('legacy snapshot contains 326 cells',len(old)==326)
check('all legacy exclusions retained without changing dimensions/ranks',
      all(k in rec and rec[k][:2]==v[:2] for k,v in old.items()))
check('full-rank compatibility view has 1521 cells',len(rec)==1521)
check('two explicitly omitted s60 cells included',
      all((p,8) in rec for p in [(19,6,3,3,1),(19,4,4,3,2)]))
check('LMR excluded from full-rank-only API',(LMR,24) not in rec)
check('all compatibility rows are full rank',all(a==md for a,md,_ in rec.values()))
check('no ambient dimension conflicts',not bank.conflicts)
check('polynomial degree is part of cell identity',cell_key(3,[6,3],3)!=cell_key(1,[6,3],9))
raises('invalid partition fails loudly',lambda:partition([1,3]))
raises('incorrect cell size fails loudly',lambda:cell_key(4,[19,6,3,3,1],9))
toy=Ledger();toy.add(4,[8],2,3,'synthetic',ranks={'det':2},per_prime={'det':{p:2 for p in PRIMES}})
r=toy.finish().cells[(4,(8,),2)]
check('sampled deficiency never becomes membership',r['sides']['det']['ideal_dimension_interval']==[0,1]
      and not r['sides']['det']['full_rank'] and 'exact_rank' not in r['sides']['det'])
toy.add(4,[8],2,4,'synthetic_conflict',ranks={'det':4})
check('conflicting dimensions recorded and cannot close',bool(toy.conflicts) and
      not toy.finish().cells[(4,(8,),2)]['sides']['det']['full_rank'])
vals={(6,3,3,1,0):4}; fake={((19,6,3,3,1),8):(4,4,'control')}
check('zero-padded and short tails join while preserving caller key',
      quartic_closed_tails(vals,fake)==set(vals))
check('deficient row does not close stable tail',not quartic_closed_tails(vals,{((19,6,3,3,1),8):(4,3,'control')}))
check('unequal ambient and stable dimensions do not close tail',not quartic_closed_tails(vals,{((19,6,3,3,1),8):(3,3,'control')}))
lmr=bank.cells[(4,LMR,24)]
check('LMR rank and interval preserved',lmr['sides']['det']['exact_rank']==273 and
      lmr['sides']['pad']['rank_floor']==269 and lmr['D_interval']==[-4,1])
check('n3 padded weight vanishes without conflating unpadded control',
      bank.cells[(3,N3,12)]['sides']['pad']['exact_rank']==0 and
      bank.cells[(3,N3,12)]['sides']['per3']['exact_rank']==6)
check('length4 containment stops before length5',
      bool(inherited_gap_exclusion(4,[5,4,4,3])) and not inherited_gap_exclusion(4,[5,4,3,3,1]))
census=json.loads((ROOT/'results/b13_11/weight13_census.json').read_text())
check('exact census complete',census['shapes']==57 and census['a_inf_positive']==47 and census['a_inf_zero']==10)
check('census dimensions match the frozen independent historical census',
      census['a_inf_by_shape']==json.loads((ROOT/'results/wk12_int_w13_census.json').read_text())['a_inf_by_shape'])
check('rank openness remains distinct from containment exclusion',
      len(census['open_on_both_instruments'])==19 and not census['open_on_all_instruments'])
inventory=json.loads((ROOT/'results/b13_11/inventory_summary.json').read_text())
check('cubic remainder matches board cutoff',inventory['cubic_degree10']==
      dict(candidates=402,open=106,open_NS_below_10m=95,open_NS_at_least_10m=11))
seen=set();counts=Counter()
for name in inventory['candidate_parts']:
    for line in (ROOT/'results/b13_11'/name).read_text().splitlines():
        c=json.loads(line)
        check_id=c['id']
        if check_id in seen:raise AssertionError('duplicate candidate id')
        seen.add(check_id);counts[c['n']]+=1
        if c['n']==4 and c['open_on_all_instruments'] and c['closures']:
            raise AssertionError('closed candidate marked open')
check('inventory cell keys unique and complete',len(seen)==inventory['candidate_cells'])
for name,n in [('stable_replay.json',192),('controls.json',28)]:
    x=json.loads((ROOT/'results/b13_11'/name).read_text())
    check(name+' complete and passing',len(x['checks'])==n and all(c['ok'] for c in x['checks']))
save('validation.json',dict(board_numbering='batch13',session_id='B13-11',checks=checks,
                           passed=sum(c['ok'] for c in checks),total=len(checks)))
print(json.dumps(dict(passed=len(checks),total=len(checks),legacy=len(old),full_rank=len(rec))),flush=True)
