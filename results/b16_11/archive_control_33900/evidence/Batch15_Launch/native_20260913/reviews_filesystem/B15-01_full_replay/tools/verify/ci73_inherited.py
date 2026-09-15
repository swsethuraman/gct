"""Separate replay of INHERITED S74 minor arithmetic, with freshly rebuilt u.

Native degree-24-family values and the a24/LMR theorems remain inherited.
This module does not call their producers or claim fresh polynomial evaluation.
"""
import itertools,json,math
from pathlib import Path
import ci73_io as io
import ci73_linear as la


def need(ok,why):
    if not ok:raise ValueError(why)


def verify(root):
    root=Path(root);source=io.load(root/'results/s74/source.json')
    cert=io.load(root/'results/s74/certified.json');records=[]
    need(source['cell']==cert['cell']==dict(n=4,r=9,lam=[65,17]+[2]*7,delta=24,a=274),'inherited cell')
    for p in [2147483647,2147483629]:
        for family,name,degree,rank in [('det','det_minor_delta23',23,273),('pad','pad_minor',24,269)]:
            path=root/f'results/s74/columns_{family}_{p}.json';data=io.load(path)
            need(data['family']==family and data['prime']==p,'inherited family/prime')
            witness=cert['primes'][str(p)][name]
            rows=[e for e in source['entries'] if e['rung']<=degree]
            need(len(rows)==witness['rows'],'inherited row count')
            us=[]
            for q in data['points']:
                if family=='det':u=24*la.determinant(q['pencil'][0])
                else:
                    lf=q['linear_forms'];B=[[lf[1+3*i+j][0] for j in range(3)] for i in range(3)]
                    u=24*lf[0][0]*sum(math.prod(B[i][perm[i]] for i in range(3)) for perm in itertools.permutations(range(3)))
                need(u%p!=0,'inherited point u=0');us.append(u%p)
            need(us==[v%p for v in data['u_symbol']],'fresh inherited u disagrees')
            lookup={io.digest(json.loads(k)):v for k,v in data['rows_native'].items()}
            rs,cs=witness['row_set'],witness['col_set']
            need(len(rs)==len(cs)==rank and len(set(rs))==rank and len(set(cs))==rank,'inherited minor indices')
            need(witness['point_index']==[data['point_index'][j] for j in cs],'inherited point order')
            A=[]
            for i in rs:
                e=rows[i];native=lookup[io.digest(e['key'])]
                A.append([native[j]*pow(us[j],degree-e['rung'],p)%p for j in cs])
            determinant=la.determinant(A,p)
            need(determinant!=0 and determinant==witness['det_mod_p'],'inherited determinant mismatch')
            records.append(dict(family=family,degree=degree,rank_floor=rank,prime=p,determinant=determinant,
                points_with_fresh_u=len(us),native_values='INHERITED; not freshly contracted',
                source_canonical_sha256=io.digest(source),column_canonical_sha256=io.digest(data)))
    return dict(status='PASS_ARITHMETIC_REPLAY',records=records,
                a24='274 INHERITED from S57/S63 and S74 full source',
                determinant_upper_bound='273 ADOPTED LMR theorem as in frozen S74',
                interpretation='Together with new i_pad24>=3: i_pad24 in [3,5], D in [-4,-2]; D=-4 open')
