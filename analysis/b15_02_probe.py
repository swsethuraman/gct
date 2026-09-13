"""Bounded a=1 probes; integer source construction and checked modular lifting."""
import argparse
from fractions import Fraction
import gc
import hashlib
import json
from pathlib import Path
import sys
import time

import flint
import numpy as np
from scipy import sparse
import scipy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'tools/verify'))
from tools.integrate.exclusion_predicates import conclusions_for
from b14_11_sizes import burnside, controls as size_controls
from wk8_s30_pleth import pleth_p, chi
from wk8_s30_core import exps, build_R
from wk9_s45_build import build_cell
from wk11_s71_hybrid import best_cover
from wk12_s79_cell6 import det_pencils, det_coeffs, ev_rows_from_coeffs
from wk10_s64_pad import pad_frames, pad_coeffs, point_record_pad
from points import form_of_point
from hwv import is_highest_weight, evaluate

P = 65521
SEED = 20260913
OUT = ROOT / 'results/b15_02'


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def array_hash(a):
    a = np.asarray(a, dtype='<i8')
    return hashlib.sha256(a.tobytes()).hexdigest()


def exact_a(lam, d):
    v = sum((c * chi(tuple(lam), rho) for rho, c in pleth_p(d, 4).items()), Fraction())
    assert v.denominator == 1 and v >= 0
    chi.cache_clear()
    return int(v)


def solve_tri(T, B, p):
    """Integer modular back substitution, reducing each product before summing."""
    T = T.tocsr()
    X = np.asarray(B, dtype=np.int64).copy() % p
    for i in range(T.shape[0] - 1, -1, -1):
        lo, hi = T.indptr[i:i+2]
        cols, vals = T.indices[lo:hi], T.data[lo:hi]
        assert np.all(cols >= i)
        diag = int(vals[cols == i][0]) % p
        assert diag
        keep = cols > i
        cc, vv = cols[keep], vals[keep] % p
        assert len(cc) * (p - 1)**2 < 2**63
        if len(cc):
            X[i] = (X[i] - vv @ X[cc]) % p
        X[i] = X[i] * pow(diag, -1, p) % p
    return X


def dense_kernel(A, p):
    A = np.asarray(A, dtype=np.int64) % p
    Z, nullity = flint.nmod_mat(*A.shape, A.ravel().tolist(), p).nullspace()
    return np.array([[int(Z[i,j]) for j in range(nullity)] for i in range(A.shape[1])], dtype=np.int64)


def sparse_product(A, X, p):
    A = A.tocsr()
    maxsum = int(np.max(np.asarray(abs(A).sum(axis=1)), initial=0))
    assert maxsum * (p - 1) < 2**63
    return (A @ X) % p


def kernel(E, expected=1, p=P):
    """S71 cover proof, local integer NumPy/SciPy residual arithmetic."""
    begin = time.perf_counter()
    nc = E.shape[1]
    cov = best_cover(E, nc, seed=SEED)
    rows, S, U = cov['rows'], cov['S'], cov['U']
    ns, nu = len(S), len(U)
    print(json.dumps(dict(phase='cover', n_chi=nc, nS=ns, nU=nu)), flush=True)
    if nu > 2000 or 8 * ns * min(nu, 64) > 256 * 1024**2:
        raise MemoryError(f'Conservative residual cap: nS={ns}, nU={nu}')
    T = E[rows][:, S].tocsr()
    TU = E[rows][:, U].tocsr()
    mask = np.ones(E.shape[0], dtype=bool); mask[rows] = False
    other = np.flatnonzero(mask)
    Fo = E[other].tocsr()
    for attempt in range(2):
        m = nu + 32 * (attempt + 1)
        rng = np.random.default_rng(SEED + attempt)
        pr = rng.integers(0, m, size=(len(other), 2))
        ps = rng.choice(np.array([-1, 1], dtype=np.int64), size=(len(other), 2))
        Q = sparse.csr_matrix((ps.ravel(), (pr.ravel(), np.repeat(np.arange(len(other)), 2))), shape=(m, len(other)))
        H = (Q @ Fo).tocsr()
        HS = H[:, S].tocsr()
        G = H[:, U].toarray().astype(np.int64) % p
        for b in range(0, nu, 64):
            X = solve_tri(T, TU[:, b:b+64].toarray(), p)
            G[:, b:b+64] = (G[:, b:b+64] - sparse_product(HS, X, p)) % p
        YU = dense_kernel(G, p)
        if YU.shape[1] != expected:
            print(json.dumps(dict(phase='projection_retry', nullity=YU.shape[1])), flush=True)
            continue
        K = np.zeros((nc, expected), dtype=np.int64)
        K[U] = YU
        K[S] = solve_tri(T, -sparse_product(TU, YU, p), p)
        if np.any(sparse_product(E, K, p)):
            continue
        assert expected == 1 and np.any(K)
        pivot = int(np.flatnonzero(K[:, 0])[0])
        K = K * pow(int(K[pivot, 0]), -1, p) % p
        info = dict(method='integer triangular cover plus checked projected Schur kernel',
                    p=p, nS=ns, nU=nu, projected_rows=m, projected_rank_lb=nu-expected,
                    raising_rank_lb=nc-expected, raising_nullity=expected,
                    kernel_checked_on_all_rows=True, normalization_index=pivot,
                    cover_order=cov['order'], cover_stats=cov['stats'],
                    cover_rows=rows.tolist(), cover_columns=S.tolist(), free_columns=U.tolist(),
                    projection_seed=SEED+attempt, projection_entries_per_input_row=2,
                    projection_row_sha256=array_hash(pr), projection_sign_sha256=array_hash(ps),
                    schur_sha256=array_hash(G), kernel_sha256=array_hash(K),
                    seconds=time.perf_counter()-begin)
        return K[:,0], info
    raise ValueError('Projection did not produce a fully verified kernel')


def classify(value, a=1, h=1):
    return dict(status='REPLAYED_RANK_FLOOR' if value else 'CANDIDATE',
                m_det_lb=int(value != 0), m_pad_ub=min(a,h),
                D_ub=min(a,h)-1 if value else None)


def screen():
    index = json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    overlay = json.loads((ROOT/'results/b15_prep/transport_overlay.json').read_text())
    panel = json.loads((ROOT/'results/b15_prep/candidate_preflight.json').read_text())['a1_panel']
    out = []
    for c in panel + [dict(lam=[16,2,2,2,2,2,2],delta=7,a=1,h_pad_upper=1)]:
        cell = dict(n=4,ell=len(c['lam']),delta=c['delta'],**{'lambda':c['lam']})
        contracts=index['application_contract']['conclusions_by_id']
        contexts=sorted({ctx for item in contracts.values() for ctx in item})
        hits={ctx:conclusions_for(index,cell,ctx) for ctx in contexts}
        hits={ctx:v for ctx,v in hits.items() if v}
        oh=[x for x in overlay['targets'] if x['degree']==c['delta'] and x['lam']==c['lam']]
        out.append(dict(**c,typed_conclusions=hits,overlay_hits=oh))
    save(OUT/'screening.json',dict(status='EXACT', cells=out))
    return out[:-1]


def controls():
    t = time.perf_counter()
    sz = size_controls()
    lam=(6,2); B=build_cell(lam,2,verbose=False)
    K,info=kernel(B['E'])
    A=exps(4,2); vec=[]
    for idx,m in enumerate(B['arr']['M']):
        col=int(B['arr']['col_of'][idx])
        if col>=0:
            v=int(K[col]*B['arr']['sgn'][idx])%P
            if v:vec.append((tuple(A[k] for k in m),v))
    assert is_highest_weight(vec,2,P)[0]
    exact=[(((2,2),(4,0)),8),(((3,1),(3,1)),-3)]
    assert is_highest_weight(exact,2)[0]
    altered=[(exact[0][0],7),exact[1]]
    assert not is_highest_weight(altered,2)[0]
    factorial_bad=[(alphas,coef*np.prod([np.prod([__import__('math').factorial(v) for v in e]) for e in alphas])) for alphas,coef in exact]
    assert not is_highest_weight(factorial_bad,2)[0]
    I=np.eye(4,dtype=int).tolist(); D=np.diag([1,2,3,4]).tolist()
    pt=dict(type='det_pencil',pencil=[I,D])
    co=det_coeffs(pt['pencil'],2); independent=form_of_point(pt,2,4)
    assert {k:v for k,v in co.items() if v}==independent
    assert evaluate(exact,co)==-20
    assert evaluate(vec,co,P)!=0
    badpt=dict(type='det_pencil',pencil=[I,I])
    assert evaluate(exact,form_of_point(badpt,2),P)==0
    assert classify(0)['status']=='CANDIDATE' and classify(0)['D_ub'] is None
    assert exact_a(lam,2)==1
    # A planted kernel control exercises the residual rather than only cover rows.
    rng=np.random.default_rng(123)
    C=rng.integers(-5,6,size=(27,12),dtype=np.int64)
    C=np.column_stack([C,C[:,0]+2*C[:,1]])
    v,ki=kernel(sparse.csr_matrix(C))
    dk=dense_kernel(C,P); assert dk.shape==(13,1)
    assert np.all(C@v%P==0)
    # Full unreduced raising action agrees on the expanded small source.
    basis,R=build_R(4,2,2,lam)
    vd={tuple(A[k] for k in m):i for i,m in enumerate(basis)}
    x=np.zeros(len(basis),dtype=np.int64)
    for alphas,v in vec:x[vd[alphas]]=v
    assert all(sum(int(x[j])*c for j,c in row.items())%P==0 for row in R)
    result=dict(status='EXACT',control_pass=True,liveness_exact_value=-20,
                altered_source_rejected=True,factorial_change_rejected=True,
                altered_point_zero_detected=True,synthetic_zero_accepted=True,
                direct_raising_checked=True,schur_dense_control=ki,
                sizes=sz,versions=dict(numpy=np.__version__,scipy=scipy.__version__,flint=flint.__version__),
                seconds=time.perf_counter()-t)
    save(OUT/'controls.json',result)
    screen()
    print('CONTROLS PASS',flush=True)


def probe(c,index):
    start=time.perf_counter(); tag=f'cell_{index:02d}'
    assert not c['typed_conclusions'] and not c['overlay_hits'], 'New screen hit requires review'
    lam=tuple(c['lam']); d=c['delta']; r=len(lam)
    rec=dict(cell=dict(n=4,delta=d,lam=list(lam),working_variables=r,ambient_variables=16),
             model='gpt-6-astra',prime=P,source_convention='ordinary coefficients; signed orbit sums',
             status='CANDIDATE')
    save(OUT/f'{tag}.json',rec)
    size=burnside(lam,d); assert size['n_chi']==c['n_chi']
    rec['size']=size
    a=exact_a(lam,d); assert a==c['a']==1
    rec.update(a=a,h_pad_ub=c['h_pad_upper'],m_pad_ub=min(a,c['h_pad_upper']),
               ambient_check='exact rational power-sum plethysm with Murnaghan-Nakayama characters')
    B=build_cell(lam,d,verbose=True)
    assert (B['n_chi'],B['N_S'])==(size['n_chi'],size['N_S'])
    rec['construction']={k:B[k] for k in ['nrows','nnz','nfixed','mono_secs','orbit_secs','rows_secs','build_secs']}
    rec['carrier_hashes']={k:array_hash(B['arr'][k]) for k in ['M','col_of','sgn']}
    K,ki=kernel(B['E']); rec['reduction']=ki
    source=dict(cell=rec['cell'],prime=P,chi_coordinates=K.tolist(),
                carrier_hashes=rec['carrier_hashes'],coefficient_convention=rec['source_convention'],
                raising_rule='E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j)',
                construction='wk9_s45_build.build_cell(lam,delta,n=4); no source basis transformation',
                rational_lifting='rank_Q(E)=n_chi-a=n_chi-1; verified rank_Fp(E)=n_chi-1; unit maximal minor gives Z_(p) kernel base change')
    save(OUT/f'{tag}_source.json',source)
    rec['source_file']=f'results/b15_02/{tag}_source.json'
    rec['det_points']=[]; rec['pad_points']=[]
    save(OUT/f'{tag}.json',rec)
    te=time.perf_counter()
    for pencil in det_pencils(8,11,4,r):
        pt=dict(type='det_pencil',pencil=pencil)
        co=det_coeffs(pencil,r)
        ev=ev_rows_from_coeffs(B['arr'],[co],P,r)[0]
        assert len(ev)*(P-1)**2<2**63
        v=int(ev@K%P)
        # Independent polynomial construction, same explicit point.
        other=form_of_point(pt,r,4)
        assert {e:z for e,z in co.items() if z}==other
        rec['det_points'].append(dict(point=pt,value_mod_p=v))
        print(json.dumps(dict(phase='det_evaluation',index=index,value=v)),flush=True)
        if v:
            rec.update(classify(v,a,c['h_pad_upper']))
            rec.update(m_det_ub=a,i_det_lb=0,i_det_ub=0)
            break
    if not any(pt['value_mod_p'] for pt in rec['det_points']):
        for frame in pad_frames(4,37,4,r):
            pt=point_record_pad(frame); co=pad_coeffs(frame)
            assert {e:z for e,z in co.items() if z}==form_of_point(pt,r,4)
            row=ev_rows_from_coeffs(B['arr'],[co],P,r)[0]
            v=int(row@K%P)
            rec['pad_points'].append(dict(point=pt,value_mod_p=v))
            if v:break
        rec.update(classify(0,a,c['h_pad_upper']))
        rec['m_pad_lb']=int(any(x['value_mod_p'] for x in rec['pad_points']))
        rec['missing_witness']='global determinant vanishing proof or determinant nonzero'
    rec['evaluation_seconds']=time.perf_counter()-te
    rec['wall_seconds']=time.perf_counter()-start
    save(OUT/f'{tag}.json',rec)
    print(json.dumps(dict(phase='cell_complete',index=index,status=rec['status'],seconds=rec['wall_seconds'])),flush=True)
    del B,K
    gc.collect()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--controls',action='store_true')
    ap.add_argument('--first',type=int,default=1);ap.add_argument('--last',type=int,default=1)
    args=ap.parse_args()
    if args.controls:controls();return
    assert json.loads((OUT/'controls.json').read_text())['control_pass']
    panel=screen()
    for i in range(args.first,args.last+1):
        try:probe(panel[i-1],i)
        except MemoryError as exc:
            rec=json.loads((OUT/f'cell_{i:02d}.json').read_text())
            rec.update(status='RESOURCE_STOP',reason=str(exc))
            save(OUT/f'cell_{i:02d}.json',rec)
            print(json.dumps(dict(index=i,status='RESOURCE_STOP',reason=str(exc))),flush=True)
            break


if __name__=='__main__':main()
