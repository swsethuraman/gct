import os, pathlib
ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))
WORK = pathlib.Path(os.environ.get('GCT_WORK', ROOT / 'results' / 'integrate' / 'b14_11_replay'))
WORK.mkdir(parents=True, exist_ok=True)
import json, sys, collections
sys.path.insert(0, str(ROOT / 'tools' / 'integrate'))
import exclusion_predicates as EP
R=str(ROOT)+'/'
idx=json.load(open(R+'results/integrate/inherited_exclusions.json'))
def q(n,delta,lam,ctx='quartic_padded_gap'):
    return EP.conclusions_for(idx, dict(n=n,ell=len(lam),delta=delta,**{'lambda':list(lam)}), ctx)

cq=json.load(open(R+'results/b14_11/cost_queue.json'))
cands = cq['candidates'] if isinstance(cq,dict) and 'candidates' in cq else (cq if isinstance(cq,list) else cq[list(cq)[-1]])
print("candidate queue entries:", len(cands))
hits=collections.Counter(); rows=[]
for c in cands:
    r=q(4,c['delta'],c['lam'])
    if r:
        for x in r: hits[x['id']]+=1
        rows.append({'delta':c['delta'],'lam':c['lam'],'ids':[x['id'] for x in r],
                     'concl':[x['conclusion'] for x in r]})
print("queue cells the banked ledger already closes:", len(rows))
for k,v in hits.items(): print(f"   {k}: {v}")
for r in sorted(rows, key=lambda z:(z['delta'],z['lam']))[:40]:
    print("   ", tuple(r['lam']), r['delta'], r['ids'], r['concl'])

# The honest question is what the ledger closed BEFORE B14-11's own two rules
# were appended.  Asking it of the full ledger returns 153 of 153 by construction,
# which is a check that cannot fail; see check_must_be_able_to_fail in PROVED.md.
NEW={'quartic_length_and_eligibility','quartic_pullback_zero'}
pre=dict(idx); pre['exclusions']=[e for e in idx['exclusions'] if e['id'] not in NEW]
def qpre(delta,lam,ctx='quartic_padded_gap'):
    return EP.conclusions_for(pre, dict(n=4,ell=len(lam),delta=delta,**{'lambda':list(lam)}), ctx)

exc=json.load(open(R+'results/b14_11/exact_exclusions.json'))['cells']
overlap=sum(1 for e in exc if qpre(e['delta'],e['lam']))
print(f"of the {len(exc)} new exclusions, {overlap} were already closed by the "
      f"PRE-B14-11 ledger; net new: {len(exc)-overlap}")

cen=[json.loads(l) for l in open(str(WORK / 'census_all.jsonl'))]
pos=[c for c in cen if c['a']>0]
closed=[c for c in pos if qpre(c['delta'],tuple(c['lam']))]
print(f"of the {len(pos)} positive census labels, the PRE-B14-11 ledger closes {len(closed)}")
print(f"of the {len(pos)} positive census labels, the ledger closes "
      f"{sum(1 for c in pos if q(4,c['delta'],tuple(c['lam'])))} after this merge")
assert len(closed)==10, f"expected the ten peaked shapes, got {len(closed)}"
assert overlap==0, f"expected no overlap, got {overlap}"
json.dump({'queue_closed':rows,'queue_total':len(cands),'exc_overlap':overlap,
           'positive_closed':len(closed)}, open(str(WORK / 'ledger_join.json'),'w'), indent=1)
