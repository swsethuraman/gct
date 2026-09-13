"""Bounded first entry benchmark; no stored arithmetic is an evaluation oracle."""
import json
import math
from pathlib import Path
import random
import sys
import time
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_eval as v

def main():
    rng=random.Random(7313);small=[]
    for n in range(4):
        f=dict(h=2,val=[4,4],C1=[0,1],C2=[1,0] if n%2 else [0,1],two=[],one=[0,0,1,1])
        table={4:{a:rng.randint(-5,5)*math.prod(math.factorial(i) for i in a) for a in v.exps(4,2)}}
        want=v.literal(f,table)
        for p in [0,2147483647]:
            vals,record=v.evaluate(f,[table],p,name=f'ci73_small_{n}_{p}')
            v.need(vals[0]==(want%p if p else want),'literal comparison failed')
            small.append(dict(case=n,prime=p,value=vals[0],expected=want))
    source=json.loads(Path('results/s74/source.json').read_text())
    points=json.loads(Path('results/b14_prep/points/P13.json').read_text())
    pts=[p for p in points['points'] if p['role']=='primary'][:4]
    ce=points['cubic_exponents'];symbols=[{4:v.quartic_symbols(pt,ce)} for pt in pts]
    f=v.native_source(source['entries'][15])
    vals,record=v.evaluate(f,symbols,name='ci73_source15_batch4')
    matrix=json.loads(Path('results/ci73/inputs/source_matrix.json').read_text())
    v.need(vals==[int(x) for x in matrix['A'][15][:4]],'source15 exact polynomial values disagree')
    targets=json.loads(Path('results/ci73/inputs/mixed.json').read_text())
    f=targets['members'][0]['filling']
    mv,mrecord=v.evaluate(f,[v.mixed_symbols(pt,ce) for pt in pts],2147483647,name='ci73_mixed0_batch4')
    v.need(mv==targets['rows_P1'][0][:4],'mixed0 polynomial values disagree')
    out={'status':'PASS','small':small,'source15':record,'mixed0':mrecord}
    Path('results/ci73/benchmark.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'source_seconds':record['seconds'],'source_transitions':record['transitions'],
                      'mixed_seconds':mrecord['seconds'],'mixed_transitions':mrecord['transitions'],
                      'source_values':vals,'mixed_values':mv}),flush=True)

if __name__=='__main__':main()
