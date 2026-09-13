"""B15-03 leased primary pilot and native replay driver."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import random
import time
import numpy as np
from b15_03_engine import (ROOT, OUT, save, build, reduce, rank, eval_native,
    det_pencils, det_coeffs, pad_frames, pad_coeffs, diagonal_points, point_check, P1, P2)
from wk8_s30_core import exps
from wk13_b10_lean import best_cover_lean
from b15_bound import process_memory

LAM=(13,11,3,2,1,1,1)

def native_raise(arr,K,p,lam=LAM):
    """Fresh full raising check; no inherited raising/deduplication routine."""
    t=time.perf_counter()
    r=len(lam); alphas=np.array(exps(4,r),dtype=np.int16)
    idx={tuple(a):i for i,a in enumerate(alphas.tolist())}
    M=arr['M']; cols=arr['col_of']; signs=arr['sgn']
    assert np.all(alphas[M].sum(axis=1)==np.array(lam))
    assert np.all(np.diff(M,axis=1)>=0)
    sel=np.nonzero(cols>=0)[0]
    mon=M[sel]
    coeff=(K[cols[sel]]*signs[sel,None])%p
    tables=[np.array([math.comb(m+j,j+1) for m in range(len(alphas))],dtype=np.int64)
            for j in range(M.shape[1])]
    operators=[]
    for i in range(r-1):
        codes_parts=[]; value_parts=[]
        transform=np.full(len(alphas),-1,dtype=np.int32)
        for a,alpha in enumerate(alphas):
            if alpha[i+1]>0:
                changed=alpha.copy(); changed[i]+=1; changed[i+1]-=1
                transform[a]=idx[tuple(changed)]
        for slot in range(M.shape[1]):
            valid=transform[mon[:,slot]]>=0
            mons=mon[valid].copy()
            multiplier=alphas[mons[:,slot],i].astype(np.int64)+1
            mons[:,slot]=transform[mons[:,slot]]
            mons.sort(axis=1)
            codes=np.zeros(len(mons),dtype=np.int64)
            for j,tab in enumerate(tables):
                codes+=tab[mons[:,j]]
            codes_parts.append(codes)
            value_parts.append(coeff[valid]*multiplier[:,None])
        all_codes=np.concatenate(codes_parts)
        all_values=np.concatenate(value_parts)
        keys,inverse=np.unique(all_codes,return_inverse=True)
        sums=np.zeros((len(keys),K.shape[1]),dtype=np.int64)
        np.add.at(sums,inverse,all_values)
        assert not np.any(sums%p), ('full raising failure',i)
        operators.append({'i':i,'j':i+1,'image_terms':len(all_codes),'distinct_monomials':len(keys),'all_zero':True})
    return {'status':'EXACT','method':'full unquotiented simple raising, independently assembled from native monomials',
            'operators':operators,'seconds':time.perf_counter()-t}

def files_hash():
    names=['analysis/b15_03_engine.py','analysis/b15_03_run.py','analysis/b15_03_counts.py',
           'analysis/wk13_b10_lean.py','analysis/wk12_s79_cell6.py','analysis/wk8_s30_core.py',
           'analysis/wk9_s36_stabred.py','analysis/wk9_s45_build.py','analysis/wk9_s42_orbits.py',
           'analysis/wk10_s64_pad.py','analysis/b15_bound.py','results/b15_03/counts_primary.json']
    return {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}

def points():
    r=len(LAM)
    dp=det_pencils(4,11,3,r)
    pads=pad_frames(4,37,3,r)
    diag=diagonal_points(2,r)
    rng=random.Random(150304)
    gen=[{al:rng.randint(-3,3) for al in exps(4,r)} for _ in range(4)]
    # Native integer data retained before any source evaluation.
    rec={'det_pencils':dp,'pad_frames':pads,'diagonal_pencils':diag,
         'generic_quartics':[[[list(al),c] for al,c in co.items()] for co in gen],
         'seeds':{'det':11,'pad':37,'diagonal':150303,'generic':150304},'bound':3,
         'definitions':{'det':'det_4(sum_i x_i A_i), A_i integral 4x4',
                        'pad':'z*per_3 on independent integral 7x10 frame: z coordinate 0, per coordinates 1+3a+b',
                        'generic':'all 330 ordinary quartic coefficients independently uniform in [-3,3]',
                        'diagonal':'product of four linear forms from diagonal 4x4 pencils'},
         'ambient_variable_count':16,'pad_essential_variable_count':10,'restriction_variable_count':7}
    save('points.json',rec)
    return rec,{'det':[det_coeffs(x,r) for x in dp], 'pad':[pad_coeffs(x) for x in pads],
                'generic':gen,'diagonal':[det_coeffs(x,r) for x in diag]}

def pilot():
    lease_path=ROOT.parents[2]/'Batch15_Launch/native_20260913/LEASES.json'
    lease=json.loads(lease_path.read_text())
    assert '03' in lease['holders'],'B15-03 needs an integrator-granted heavy lease'
    save('lease_at_pilot.json',lease)
    rec={'status':'CANDIDATE','model':'gpt-6-astra','lambda':LAM,'n':4,'degree':8,
         'a_lb':2,'a_ub':2,'h_pad_lb':2,'h_pad_ub':2,'U_pad_ub':2,
         'source_orientation':'rows native chi monomials; columns highest-weight vectors',
         'ordinary_coefficients':True,'climbing_u_used':False,'input_sha256':files_hash()}
    t=time.perf_counter()
    B=build(LAM,8); E=B['E']; arr=B['arr']
    assert (arr['N_S'],arr['n_chi'])==(519879,43364)
    rec['construction']={'seconds':time.perf_counter()-t,'N_S':arr['N_S'],'n_chi':arr['n_chi'],
          'raising_shape':list(E.shape),'raising_nnz':int(E.nnz),
          'raising_csr_bytes':E.indptr.nbytes+E.indices.nbytes+E.data.nbytes,
          'monomial_dtype':str(arr['M'].dtype),'memory':process_memory()}
    print(json.dumps({'construction':rec['construction']}),flush=True)
    t=time.perf_counter(); cov=best_cover_lean(E,E.shape[1],verbose=False)
    rec['cover']={'seconds':time.perf_counter()-t,'rank_lb':cov['size'],'nU':len(cov['U']),
                  'order':cov['order'],'stats':cov['stats']}
    save('pilot.json',rec)
    print(json.dumps({'cover':rec['cover']}),flush=True)
    # Native source carrier below the single-file cap; it is also reconstructible.
    np.savez_compressed(OUT/'native_carrier.npz',M=arr['M'],col_of=arr['col_of'],sgn=arr['sgn'],n_chi=arr['n_chi'])
    assert (OUT/'native_carrier.npz').stat().st_size<5000000
    point_data, families=points()
    rec['per_prime']={}
    for p in [P1,P2]:
        tp=time.perf_counter()
        try: K,info=reduce(E,2,p,cov=cov)
        except MemoryError as exc:
            rec['status']='RESOURCE_STOP'; rec['allocation_stop']=str(exc); save('pilot.json',rec); return
        np.savez_compressed(OUT/f'kernel_{p}.npz',K=K,prime=p)
        rr=native_raise(arr,K,p)
        vals={}; floor={}; tev=time.perf_counter()
        for name,co in families.items():
            vals[name]=eval_native(arr,K,co,p,7)
            floor[name]=rank(vals[name],p)
        assert floor['generic']==2, 'source/evaluator independence control'
        assert floor['diagonal']==0
        assert all(point_check(pt,co,p) for pt,co in zip(point_data['det_pencils'],families['det']))
        assert all(rank(np.array(frame),p)==7 for frame in point_data['pad_frames'])
        assert all(rank(np.array(pen).reshape(7,16),p)==7 for pen in point_data['det_pencils'])
        det_minor=next(((i,j,(vals['det'][i][0]*vals['det'][j][1]-vals['det'][i][1]*vals['det'][j][0])%p)
                        for i in range(4) for j in range(i+1,4)
                        if (vals['det'][i][0]*vals['det'][j][1]-vals['det'][i][1]*vals['det'][j][0])%p),None)
        ent={'status':'REPLAYED_RANK_FLOOR','reduction':info,'full_raising':rr,'values':vals,
             'r_det_lb':floor['det'],'r_pad_lb':floor['pad'],'r_generic_lb':floor['generic'],
             'det_minor':det_minor,'diagonal_rank':floor['diagonal'],'evaluation_seconds':time.perf_counter()-tev,
             'seconds':time.perf_counter()-tp,'all_frames_rank_seven':True,'memory':process_memory()}
        rec['per_prime'][str(p)]=ent
        rec['r_det_lb']=max(e['r_det_lb'] for e in rec['per_prime'].values())
        rec['r_pad_lb']=max(e['r_pad_lb'] for e in rec['per_prime'].values())
        rec['i_det_ub']=2-rec['r_det_lb']; rec['i_pad_ub']=2-rec['r_pad_lb']
        rec['D_ub']=2-rec['r_det_lb']; rec['D_lb']=rec['r_pad_lb']-2
        rec['status']='REPLAYED_RANK_FLOOR' if rec['r_det_lb']==2 else 'CANDIDATE'
        save('pilot.json',rec)
        print(json.dumps({'prime':p,'r_det_lb':ent['r_det_lb'],'r_pad_lb':ent['r_pad_lb'],
                          'seconds':ent['seconds'],'det_minor':det_minor}),flush=True)
    rec['native_sha256']={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(OUT.glob('*.npz'))}
    rec['native_sha256']['points.json']=hashlib.sha256((OUT/'points.json').read_bytes()).hexdigest()
    save('pilot.json',rec)

if __name__=='__main__':
    pilot()
