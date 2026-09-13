"""Forced rank-zero control: ell times a product of three linear forms."""
from collections import defaultdict
import json,random,sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73,ci73_eval as ev,ci73_io as io

def main():
    rng=random.Random(137300);factors=[[rng.choice([-1,1]) for _ in range(9)] for _ in range(4)]
    polynomial={(0,)*9:1}
    for linear in factors[1:]:
        new=defaultdict(int)
        for alpha,value in polynomial.items():
            for i,v in enumerate(linear):
                beta=list(alpha);beta[i]+=1;new[tuple(beta)]+=value*v
        polynomial=new
    ce=ev.exps(3,9);point=dict(linear=factors[0],cubic_coefficients=[polynomial[a] for a in ce])
    c=io.load(Path('results/ci73/certificate.json'));s=io.read_reference(c['dependencies']['source'],Path('results/ci73'))
    session=ci73.Session();source=[];target=[]
    for i,e in enumerate(s['entries'][:39]):
        source+=session.row(ev.native_source(e),[{4:ev.quartic_symbols(point,ce)}],0,'chow_source_'+str(i))
    for i,m in enumerate(c['target_members'][:72]):
        target+=session.row(m['filling'],[ev.mixed_symbols(point,ce)],2147483647,'chow_target_'+str(i))
    if any(source+target):raise RuntimeError('forced Chow rank-zero control failed')
    result=dict(status='PASS',source_exact_zeros=len(source),mixed_modular_zeros=len(target),factors=factors,
        reason='A product of four linear forms has support dimension at most four; highest weights of length nine vanish. Mixed pullback on this Chow cubic has the same four-factor restriction.',
        fresh_backend_entries=session.entries,max_array_bytes=session.max_array_bytes)
    Path('results/ci73/chow_control.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
