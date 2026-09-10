"""Replay banked minors/transport; prove the padded n=3 variable-count control."""
from itertools import permutations
import json
from math import prod
from pathlib import Path
import sys
import time
from b13_11_ledger import ROOT,PRIMES,json_file
from wk12_int_s74_final import kernel,load,msym_u

OUT=ROOT/'results/b13_11'
checks=[]


def check(name,ok,**data):
    checks.append(dict(name=name,ok=bool(ok),**data))
    print(('PASS ' if ok else 'FAIL ')+name,flush=True)
    if not ok: raise ValueError(name)


def det_definition(matrix):
    n=len(matrix)
    return sum((-1)**sum(s[i]>s[j] for i in range(n) for j in range(i+1,n)) *
               prod(matrix[i][s[i]] for i in range(n)) for s in permutations(range(n)))


def main():
    start=time.monotonic(); n3=json_file('results/astra/S4/artifacts/n3_control.json')
    check('six integral n3 fillings have the correct seven-row degree-12 weight',
          len(n3['fillings'])==6 and all(f['n']==3 and f['delta']==12 and
             f['lam']==[19,7,2,2,2,2,2] for f in n3['fillings']))
    minors=[]
    for r in n3['results']:
        p=r['prime']; m=r['minor']; matrix=r['matrix']
        sub=[[matrix[i][j] for j in m['cols']] for i in m['rows']]
        value=det_definition(sub)%p
        check(f"n3 {r['family']} {p}: exact Leibniz minor agrees",value==m['det']!=0,
              rank_floor=m['rank'],minor_residue=value)
        if r['family']=='det':
            v=n3['ideal_source_coordinates']
            check(f'n3 determinant candidate vanishes on banked matrix at {p}',
                  all(sum(v[i]*matrix[i][j] for i in range(6))%p==0 for j in range(7)))
        minors.append(dict(family=r['family'],prime=p,rank_floor=m['rank'],
                           rows=m['rows'],cols=m['cols'],det_mod_p=value,
                           status='CERTIFIED',scope='banked matrix arithmetic; source evaluations inherited'))
    check('n3 controls cover both house primes and both families',
          {(r['family'],r['prime']) for r in minors}==
          {(f,p) for f in ('det','unpadded_per3') for p in PRIMES})
    # f=z*(a*d+b*c): derivatives have distinct monomial supports.
    f={(1,1,0,0,1):1,(1,0,1,1,0):1}
    derivatives=[]
    for i in range(5):
        q={}
        for e,c in f.items():
            if e[i]:
                t=list(e); t[i]-=1; q[tuple(t)]=c*e[i]
        derivatives.append(q)
    mons=sorted({m for q in derivatives for m in q})
    matrix=[[q.get(m,0) for m in mons] for q in derivatives]
    # Disjoint nonempty supports prove independence over Q without rank heuristics.
    check('ell*per2 has exactly five essential variables',all(derivatives) and
          all(set(derivatives[i]).isdisjoint(derivatives[j]) for i in range(5) for j in range(i+1,5)))
    n3out=dict(board_numbering='batch13',session_id='B13-11',minors=minors,
        source='results/astra/S4/artifacts/n3_control.json',
        unpadded_comparison=dict(status='ADOPTED',mult_per3=6,mult_det=5,gap=1,
            dependencies=['docs/s63_report.md section 3: LMR upper bound',
                'results/certs/19_7_2_2_2_2_2_d12_n3_permanent_pencil_p2147483647.json.gz',
                'results/certs/19_7_2_2_2_2_2_d12_n3_permanent_pencil_p2147483629.json.gz']),
        padded_control=dict(status='PROVED',essential_variables=5,weight_length=7,
            a=6,mult_pad=0,i_pad=6,D=-5,
            argument='Pullbacks and their closures lie in Sub_5. Its coordinate ring contains no Schur constituent of length >5. Therefore a seven-row weight has zero padded multiplicity.',
            derivative_monomials=mons,values_are='integer coefficients of first partial derivatives of z*(a*d+b*c)',
            derivative_matrix=matrix),
        source_defect='s63_n3control.json reverses the modular rank inequality in its note; the correct upper bound comes from LMR, as stated in docs/s63_report.md')
    (OUT/'n3_control.json').write_text(json.dumps(n3out,indent=1)+'\n')
    source=json_file('results/s74/source.json'); entries=source['entries']; keys=[str(e['key']) for e in entries]
    check('LMR source has 273 earlier rows and one degree-24 birth',len(entries)==274 and
          sum(e['rung']<24 for e in entries)==273 and sum(e['rung']==24 for e in entries)==1)
    result=[]
    for p in PRIMES:
        for fam,expected in (('det',273),('pad',269),('gen',274)):
            col=load(fam,p)
            us=[msym_u(fam,q)%p for q in col['points']]
            check(f'LMR {fam} {p}: exact point data reproduce every u value',
                  us==[v%p for v in col['u_symbol']])
            check(f'LMR {fam} {p}: no u-zero column',all(us))
            matrix=[[col['rows_native'][keys[i]][j]*pow(us[j],24-e['rung'],p)%p
                     for j in range(col['K'])] for i,e in enumerate(entries)]
            rank,ker=kernel(matrix,p)
            check(f'LMR {fam} {p}: transported rank {rank}',rank==expected,
                  rank=rank,nullity=len(ker))
            result.append(dict(family=fam,prime=p,rank=rank,columns=col['K'],
                values_are='rows_native[i,j]*msym_u(point_j)^(24-rung_i) mod p',
                u_values_mod_p=us,point_source=f'results/s74/columns_{fam}_{p}.json'+('.gz' if fam=='gen' else ''),
                status='CERTIFIED',scope='matrix rank and point u arithmetic; native filling evaluations inherited'))
    report=dict(board_numbering='batch13',session_id='B13-11',checks=checks,
                LMR=result,det_exact_rank=273,padded_rank_floor=269,D_interval=[-4,1],
                D_formula='D=mult_pad-mult_det=1-i_pad(24)',
                epsilon_pad_status='rational lift unresolved',
                elapsed_seconds=round(time.monotonic()-start,3))
    (OUT/'controls.json').write_text(json.dumps(report,indent=1)+'\n')
    print(json.dumps({'checks':len(checks),'all_pass':all(c['ok'] for c in checks),
                      'seconds':report['elapsed_seconds']}),flush=True)


if __name__=='__main__': main()
