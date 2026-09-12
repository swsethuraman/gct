"""Typed theorem application: a containment bound is not an empty-ideal claim."""
import argparse, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]

def validate_cell(c):
    if not isinstance(c,dict) or not {'n','ell','delta','lambda'}<=c.keys(): raise ValueError('missing cell fields')
    if any(type(c[k]) is not int or c[k]<1 for k in ('n','ell','delta')): raise ValueError('invalid cell dimensions')
    lam=c['lambda']
    if not isinstance(lam,list) or any(type(x) is not int or x<=0 for x in lam): raise ValueError('invalid partition')
    if len(lam)!=c['ell'] or lam!=sorted(lam,reverse=True) or sum(lam)!=c['n']*c['delta']: raise ValueError('cell degree/length mismatch')

_KEYCAT={}

def _explicit_keys(path):
    """(n,delta,tuple(lambda)) set from a named certificate catalog.  Fails closed:
    a missing or malformed catalog raises rather than matching nothing silently."""
    if path in _KEYCAT: return _KEYCAT[path]
    if not isinstance(path,str) or not path: raise ValueError('explicit_cell_keys needs a path')
    f=ROOT/path
    if not f.exists(): raise ValueError('explicit key catalog not found: '+path)
    d=json.loads(f.read_text())
    cells=d.get('cells')
    if not isinstance(cells,list) or not cells: raise ValueError('empty explicit key catalog: '+path)
    out=set()
    for e in cells:
        if not {'n','delta','lam'}<=e.keys(): raise ValueError('bad key entry in '+path)
        out.add((e['n'],e['delta'],tuple(e['lam'])))
    _KEYCAT[path]=out
    return out


def matches(pr,c,context):
    validate_cell(c)
    # B14-11 appended two predicate SHAPES the range-only matcher did not know:
    # a relational partition bound (any_of over length/first-row conditions) and an
    # explicit-key certificate catalog.  It expected the legacy join to skip them;
    # in fact the unsupported-key branch RAISED, so after that merge every query
    # failed.  Implemented here rather than skipped, keeping the fail-closed policy:
    # an unknown key is still an error, never a silent match and never "all n=4".
    allowed={'n','r','r_min','r_max','delta','delta_min','delta_max','family','context',
             'lambda_in','any_of','lambda_length_gt_delta','lambda_1_lt_delta',
             'explicit_cell_keys'}
    if not isinstance(pr,dict) or not pr or set(pr)-allowed: raise ValueError('empty or unsupported predicate')
    if 'family' in pr and pr['family'] not in ('LMR_u_ladder','quartic_peaked_ladder'): raise ValueError('unknown family')
    if 'any_of' in pr:
        alts=pr['any_of']
        if not isinstance(alts,list) or not alts: raise ValueError('empty any_of')
        rest={k:v for k,v in pr.items() if k!='any_of'}
        if rest and not matches(rest,c,context): return False
        return any(matches(a,c,context) for a in alts)
    if 'lambda_length_gt_delta' in pr:
        if pr['lambda_length_gt_delta'] is not True: raise ValueError('lambda_length_gt_delta must be true')
        if not c['ell']>c['delta']: return False
    if 'lambda_1_lt_delta' in pr:
        if pr['lambda_1_lt_delta'] is not True: raise ValueError('lambda_1_lt_delta must be true')
        if not c['lambda'][0]<c['delta']: return False
    if 'explicit_cell_keys' in pr:
        if (c['n'],c['delta'],tuple(c['lambda'])) not in _explicit_keys(pr['explicit_cell_keys']):
            return False
    for field,slot in [('n','n'),('r','ell'),('delta','delta')]:
        if field in pr and c[slot]!=pr[field]: return False
        if field+'_min' in pr and c[slot]<pr[field+'_min']: return False
        if field+'_max' in pr and c[slot]>pr[field+'_max']: return False
    if 'context' in pr and context!=pr['context']: return False
    if 'lambda_in' in pr and c['lambda'] not in pr['lambda_in']: return False
    if pr.get('family')=='LMR_u_ladder':
        k=c['delta']-24
        return c['n']==4 and k>=0 and c['lambda']==[65+4*k,17]+[2]*7
    if pr.get('family')=='quartic_peaked_ladder':
        ell=c['ell'];d=c['delta']
        return c['n']==4 and 2<=ell<=16 and d>=ell and c['lambda']==[4*d-2*(ell-1)]+[2]*(ell-1)
    return True

def conclusions_for(index,c,context):
    validate_cell(c)
    if not isinstance(context,str) or not context: raise ValueError('explicit context required')
    contracts=index.get('application_contract',{}).get('conclusions_by_id')
    if not contracts: raise ValueError('missing theorem application contract')
    entries=index.get('exclusions')
    if not entries: raise ValueError('empty theorem index')
    out=[]
    for ex in entries:
        if ex['id'] not in contracts: raise ValueError('rule lacks typed application contract: '+ex['id'])
        hit=matches(ex['predicate'],c,context)
        claim=contracts[ex['id']].get(context)
        if hit and claim: out.append(dict(id=ex['id'],conclusion=claim,status=ex['status'],source=ex['source']))
    return out

def stable_full_rank_closure(*,ambient_at_witness,stable_ambient,rank_lower_bound,dimension_verified,witness_verified):
    if not dimension_verified or not witness_verified: return False
    if any(type(x) is not int or x<1 for x in (ambient_at_witness,stable_ambient,rank_lower_bound)): return False
    return ambient_at_witness==stable_ambient==rank_lower_bound

def main():
    p=argparse.ArgumentParser();p.add_argument('--context',required=True);p.add_argument('--n',type=int,required=True)
    p.add_argument('--delta',type=int,required=True);p.add_argument('--lambda',dest='lam',type=int,nargs='+',required=True)
    a=p.parse_args();index=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    print(json.dumps(conclusions_for(index,dict(n=a.n,ell=len(a.lam),delta=a.delta,**{'lambda':a.lam}),a.context),indent=2))

if __name__=='__main__':main()
