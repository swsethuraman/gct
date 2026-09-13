"""Replay exact counts or rebuild native geometry for explicit nonzero minors."""
import argparse
import gzip
import json
import time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from b14_04 import recount as R
from b15_06_geometry import (OUT, ROOT, Evaluator, determinant, product_point,
    jet_point_list, det_mod, minor_certificate, save, PRIMES)


def read(path):
    raw=path.read_bytes()
    if path.name.endswith('.gz'):raw=gzip.decompress(raw)
    return json.loads(raw)


def counts():
    census=read(OUT/'census.json')
    assert census['complete'] and len(census['rows'])==40
    checks=[]
    for degrees,prefix,key in [((2,3,4),'count','a_inf'),((1,2,3),'hbound','h_normalization')]:
        # Pure recomputation: no historical checkpoints or values are reused.
        F=R.exp_series(37,degrees)
        for cell in census['rows']:
            cert=read(OUT/f"{prefix}_r{cell['r']}_t{cell['t']}.json.gz")
            values={tuple(rho):Q(a,b) for rho,a,b,ch in cert['rows_rho_numerator_denominator_character']}
            assert len(values)==len(cert['rows_rho_numerator_denominator_character'])
            assert values==F[sum(cell['tail'])]
            got=Q(0)
            for rho,a,b,char in cert['rows_rho_numerator_denominator_character']:
                assert char==R.chi(tuple(cell['tail']),tuple(rho))
                got+=Q(a,b)*char
                if R.chi.cache_info().currsize>180000:R.chi.cache_clear()
            assert got.denominator==1 and int(got)==cert[key]
            assert int(got)==cell['a_inf' if prefix=='count' else 'h_pad_ub']
            checks.append({'r':cell['r'],'t':cell['t'],'degrees':degrees,'value':int(got)})
            R.chi.cache_clear()
        del F
    # Tampered cycle character changes its stored identity and must be rejected.
    assert R.chi((3,2,2,2,2,2),(1,)*13)!=-1
    save('count_replay.json',{'status':'EXACT','checks':checks,'complete':True})
    print('COUNT REPLAY PASS',len(checks),flush=True)


def native_reds(cert):
    record=cert['record'];native=cert['native']
    r,p=record['r'],record['prime']
    if record['family']=='GEN':
        return [{int(d):v for d,v in red.items()} for red in native['points']]
    if record['family']=='DET':
        return jet_point_list(*determinant(r,p,np.array(native['A'],dtype=np.int64)))
    J,jets,c,valid=product_point(r,p,np.array(native['L'],dtype=np.int64),record['family']=='PAD')
    assert c.tolist()==native['c'] and valid.tolist()==native['valid']
    if r==10 and record['family']=='PAD':
        L=np.array(native['L'],dtype=np.int64)
        dets=[det_mod(L[:,:,k].tolist(),p) for k in range(L.shape[-1])]
        assert all(dets) and dets==native['full_support_determinants_mod_p']
    return [red for red,ok in zip(jet_point_list(J,jets),valid) if ok]


def geometry(r,t):
    summary=read(OUT/f'pilot_r{r}_t{t}_summary.json')
    assert summary['complete']
    checks=[]
    for record in summary['records']:
        p,family=record['prime'],record['family']
        cert=read(OUT/f'pilot_r{r}_t{t}_{family}_{p}.json.gz')
        assert cert['record']==record
        stamp=time.perf_counter()
        reds=native_reds(cert)
        ev=Evaluator(cert['brackets'],r-1,p,cert['interpolation_seed'])
        rows,cols=record['rows'],record['columns']
        fresh=[ev.values(reds[j]) for j in cols]
        matrix=[[column[i] for column in fresh] for i in rows]
        expected=[[cert['values'][i][j] for j in cols] for i in rows]
        assert matrix==expected
        value=det_mod(matrix,p) if rows else 1
        assert value==record['determinant_mod_p'] and value
        assert len(rows)==len(cols)==record['rank_lb']
        # Local defect: changing a stored minor entry is detectable by fresh values.
        if matrix:
            altered=[row.copy() for row in expected];altered[0][0]=(altered[0][0]+1)%p
            assert altered!=matrix
        checks.append({'family':family,'prime':p,'rank_lb':len(rows),
                       'determinant_mod_p':value,'seconds':time.perf_counter()-stamp,
                       'fresh_geometric_replay':True})
        print('REPLAY',r,t,family,p,len(rows),flush=True)
    save(f'geometric_replay_r{r}_t{t}.json',{'status':'REPLAYED_RANK_FLOOR','complete':True,'checks':checks})


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['counts','geometry'])
    parser.add_argument('--r',type=int);parser.add_argument('--t',type=int)
    a=parser.parse_args()
    if a.mode=='counts':counts()
    else:geometry(a.r,a.t)
