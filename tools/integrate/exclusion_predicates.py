"""Typed theorem application: a containment bound is not an empty-ideal claim."""
import argparse, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]

def validate_cell(c):
    if not isinstance(c,dict) or not {'n','ell','delta','lambda'}<=c.keys(): raise ValueError('missing cell fields')
    if any(type(c[k]) is not int or c[k]<1 for k in ('n','ell','delta')): raise ValueError('invalid cell dimensions')
    lam=c['lambda']
    if not isinstance(lam,list) or any(type(x) is not int or x<=0 for x in lam): raise ValueError('invalid partition')
    if len(lam)!=c['ell'] or lam!=sorted(lam,reverse=True) or sum(lam)!=c['n']*c['delta']: raise ValueError('cell degree/length mismatch')

def matches(pr,c,context):
    validate_cell(c)
    allowed={'n','r','r_min','r_max','delta','delta_min','delta_max','family','context','lambda_in'}
    if not isinstance(pr,dict) or not pr or set(pr)-allowed: raise ValueError('empty or unsupported predicate')
    if 'family' in pr and pr['family'] not in ('LMR_u_ladder','quartic_peaked_ladder'): raise ValueError('unknown family')
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
