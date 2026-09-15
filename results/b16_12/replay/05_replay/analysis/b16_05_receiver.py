"""B16-05 bounded split-cubic/permanent residual receiver.

Run via this worktree's inspected b15_bound.py, -B, 60 seconds / 512 MiB.
Banked bracket/Jet/normalization code: B14-06, Claude Opus 5 attribution.
Dimension adapter: B15-06. New comparison and direct derivatives: B16-05.
No imported producer or save function is called. All writes use B16-05 paths.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import importlib
import itertools as it
import json
import math
import os
import sys
import time

HERE = Path('C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-05')
ROOT = HERE.parents[2]
W6 = ROOT / 'work/batch15_workers/B15-06'
REVIEW = ROOT / 'Batch15_Launch/native_20260913/reviews_filesystem'
OUT = Path('C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/results/b16_12/replay/05_replay/results/b16_05')
P = 2147483647
POINTS = 4
SEED = 16051301


def digest(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def inputs():
    paths = [ROOT/'Batch16/BOARD.md', ROOT/'Batch16/launch/INPUT_MANIFEST.json',
             ROOT/'Batch16/launch/B16-05.md', ROOT/'Batch15_Launch/native_20260913/INTAKE.json',
             HERE/'analysis/b15_bound.py', HERE/'.venv/python.exe',
             HERE/'analysis/b14_06_bracket.py', HERE/'analysis/b14_06_points.py',
             W6/'analysis/b15_06_geometry.py', W6/'analysis/b14_06_bracket.py',
             W6/'analysis/b14_06_points.py', W6/'docs/b15_06_report.md',
             W6/'results/b15_06/pilot_r10_t19_summary.json']
    paths += [REVIEW/'Dream_Upper288'/x for x in
              ['DREAM_REPORT.md', 'integrator_review.json', 'tiny_controls.py', 'DELIVERY_MANIFEST.json']]
    paths += [REVIEW/'Hessian11_1631'/x for x in
              ['REPORT.md', 'verify_small.py', 'integrator_review.json']]
    paths += [REVIEW/'Slot05_Hessian_1530/integrator_review.json']
    paths += [W6/f'results/b15_06/pilot_r10_t19_{f}_{P}.json.gz' for f in ['GEN', 'PAD']]
    return {str(x.relative_to(ROOT)): digest(x) for x in paths}


def save(name, data):
    OUT.mkdir(exist_ok=True, parents=True)
    (OUT/name).write_text(json.dumps(data, indent=2) + '\n', encoding='utf8')


def read(name):
    return json.loads((OUT/name).read_text(encoding='utf8'))


def modules():
    assert sys.dont_write_bytecode, 'Use -B; inherited caches must remain untouched'
    for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS']:
        assert os.environ.get(key) == '1', (key, 'use the bounded wrapper')
    assert 'CI73_DEADLINE' in os.environ
    sys.path.insert(0, str(W6/'analysis'))
    import numpy as np
    import flint
    geo = importlib.import_module('b15_06_geometry')
    bracket = importlib.import_module('b14_06_bracket')
    points = importlib.import_module('b14_06_points')
    assert Path(geo.__file__).resolve() == W6/'analysis/b15_06_geometry.py'
    assert Path(bracket.__file__).resolve() == W6/'analysis/b14_06_bracket.py'
    return np, flint, geo, bracket, points


def retained():
    out = {}
    for family in ['GEN', 'PAD']:
        path = W6/f'results/b15_06/pilot_r10_t19_{family}_{P}.json.gz'
        assert path.stat().st_size < 4_000_000
        raw = gzip.decompress(path.read_bytes())
        assert len(raw) < 8_000_000
        out[family] = json.loads(raw)
    assert out['GEN']['brackets'] == out['PAD']['brackets']
    assert len(out['GEN']['brackets']) == 1019
    assert out['GEN']['record']['rank_lb'] == 429
    assert out['PAD']['record']['rank_lb'] == 243
    return out


def preflight():
    np, flint, geo, br, pts = modules()
    ins = inputs()
    frozen = json.loads((ROOT/'Batch16/launch/INPUT_MANIFEST.json').read_text())
    checks = []
    for item in frozen['inputs']:
        actual = digest(Path(item['path']))
        assert actual['sha256'] == item['sha256'], item['path']
        checks.append(actual)
    data = retained()
    bs = br.enumerate_brackets(35, 9)
    assert [[list(g) for g in b] for b in bs] == data['GEN']['brackets']
    basis = data['GEN']['record']['rows']
    ev = geo.Evaluator([bs[i] for i in basis], 9, P, seed=SEED)
    dets_per_point = sum(len(ev._interp[x['m']][0]) for x in ev.patterns.values())
    record = {
        'status': 'PRICED_SMALL_CONTROL', 'prime': P, 'points_each': POINTS,
        'input_hashes': ins, 'frozen_input_checks': checks,
        'frozen_slot05_head': next(w['head'] for w in frozen['worktrees'] if w['slot']=='05'),
        'source_brackets': len(bs), 'ambient_basis_size': len(basis),
        'inherited_padding_pivot': 243, 'residual_size': 186,
        'split_cubic_monomials': math.comb(11, 3),
        'jet_coefficients_each': 1+9+45, 'quartic_interpolation_nodes': 5,
        'bracket_determinants_per_point': dets_per_point,
        'bracket_max_matrix_order': max(9+sum(b[0]) for b in ev.brackets),
        'residual_projection_entries': 186*243,
        'stored_old_matrix_entries': 1019*(480+462),
        'conservative_memory_estimate_bytes': 160*1024**2,
        'estimate_rationale': 'Two <8MB decoded JSONs and <1M Python integers, plus <0.5M matrix entries; budget160MiB, enforced512MiB separately.',
        'hard_cap': {'seconds': 60, 'memory_mib': 512, 'workers': 1, 'blas_threads': 1},
        'no_dense_coefficient_expansion': True,
        'module_versions': {'numpy': np.__version__, 'python_flint': flint.__version__}}
    save('preflight.json', record)
    print(json.dumps({k: record[k] for k in ['status','source_brackets','ambient_basis_size','residual_size','split_cubic_monomials','bracket_determinants_per_point']}))


def matrix_rows(M):
    return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]


def cubic_terms(family, coeffs=None):
    if family == 'PAD':
        return [(1, tuple(3*i+q[i] for i in range(3))) for q in it.permutations(range(3))]
    return [(int(c), m) for c,m in zip(coeffs, it.combinations_with_replacement(range(9),3)) if c]


def family_jets(L, terms_by_point, np, geo, br, pts):
    J = br.Jet(9, P, POINTS)
    per_s0 = []
    # Each point may have a different cubic. Fixed monomial union avoids padding C
    # with dependence on z; the ten source forms remain independent.
    union = sorted(set(m for ts in terms_by_point for c,m in ts))
    coeff = {m: np.array([dict((mm,c) for c,mm in ts).get(m,0) for ts in terms_by_point], dtype=np.int64) for m in union}
    for t in range(5):
        ls = [geo.linear_jet(L[i], J, t) for i in range(10)]
        C = J.zero()
        for mon in union:
            a,b,c = mon
            term = J.mul(J.mul(ls[1+a],ls[1+b]),ls[1+c])
            C = (C + term*(coeff[mon]%P))%P
        per_s0.append(J.mul(ls[0],C))
    raw_g = pts._interp_s1(per_s0,list(range(5)),P,J)
    jets,c,defect,valid = pts.normalise_depress(per_s0,list(range(5)),P,J)
    assert defect == 0 and all(valid), 'Do not silently replace rejected points'
    shifts = [[int(raw_g[1][1+i,k])*pow(int(c[k]),P-2,P)*pow(4,P-2,P)%P for i in range(9)] for k in range(POINTS)]
    reds = br.jet_point_list(J,jets)
    assert all(br.consistency_defect(red,9,P)==0 for red in reds)
    return reds, list(map(int,c)), shifts


def cubic_derivatives(x, terms):
    C = 0
    g = [0]*9
    H = [[0]*9 for _ in range(9)]
    for coef,mon in terms:
        C += coef*math.prod(x[i] for i in mon)
        for a in range(3):
            g[mon[a]] += coef*math.prod(x[mon[b]] for b in range(3) if b!=a)
            for b in range(3):
                if a!=b:
                    H[mon[a]][mon[b]] += coef*x[mon[3-a-b]]
    return C%P, [v%P for v in g], [[v%P for v in row] for row in H]


def multiply(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] = (out[i+j]+x*y)%P
    return out


def remainder(a,p):
    out = list(a)
    inv = pow(p[-1],P-2,P)
    for k in range(len(out)-1,len(p)-2,-1):
        v = out[k]*inv%P
        for j,x in enumerate(p): out[k-len(p)+1+j] = (out[k-len(p)+1+j]-v*x)%P
    return out[:len(p)-1]


def hessian_control(red,L,c,shift,terms,br):
    # Compute the original z*C Hessian by direct monomial differentiation, then
    # transform by the exact normalization/depression matrix. Compare every
    # entry against the independently generated quartic slice jets at21 nodes.
    Q = [[int(i==j) for j in range(10)] for i in range(10)]
    Q[0][1:] = [(-x)%P for x in shift]
    A = br._fl(L,P)*br._fl(Q,P)
    Ar = matrix_rows(A)
    cinv = pow(c,P-2,P)
    s2,s3,s4 = [red[d][0] for d in (2,3,4)]
    p = [s4,s3,s2,0,1]
    dvals = []
    for t in range(21):
        y = [(row[0]*t+row[1])%P for row in Ar]
        z,x = y[0],y[1:]
        C,g,HC = cubic_derivatives(x,terms)
        assert all(sum(HC[i][j]*x[j] for j in range(9))%P == 2*g[i]%P for i in range(9))
        assert sum(g[i]*x[i] for i in range(9))%P == 3*C%P
        native = [[0]+g]+[[g[i]]+[z*v%P for v in HC[i]] for i in range(9)]
        dn = br.det_mod(native,P)
        assert dn == -3*pow(2,P-2,P)*pow(z,8,P)*C*br.det_mod(HC,P)%P
        H = A.transpose()*br._fl(native,P)*A
        direct = [[int(H[i,j])*cinv%P for j in range(10)] for i in range(10)]
        v = [(4*t*red[2][1][i]+3*red[3][1][i])%P for i in range(9)]
        B = [[(2*t*t*red[2][2][i][j]+6*t*red[3][2][i][j]+12*red[4][2][i][j])%P for j in range(9)] for i in range(9)]
        expected = [[(12*t*t+2*s2)%P]+v]+[[v[i]]+B[i] for i in range(9)]
        assert direct == expected
        assert c*sum(p[i]*pow(t,i,P) for i in range(5))%P == z*C%P
        dvals.append(br.det_mod(direct,P))
    V = br._fl([[pow(t,j,P) for j in range(21)] for t in range(21)],P)
    D = [r[0] for r in matrix_rows(V.inv()*br._fl([[x] for x in dvals],P))]
    S = remainder(D,multiply(p,p))
    Es = [
        S[0]-s4*S[4]+s2*s4*S[6]+s3*s4*S[7],
        S[1]-s3*S[4]-s4*S[5]+s2*s3*S[6]+(s2*s4+s3*s3)*S[7],
        S[2]-s2*S[4]-s3*S[5]+(s2*s2-s4)*S[6]+2*s2*s3*S[7],
        S[3]-s2*S[5]-s3*S[6]+(s2*s2-s4)*S[7]]
    assert [e%P for e in Es] == remainder(S,p) == remainder(D,p) == [0]*4
    # A changed S3 coefficient must fail the requested relation.
    mutated = S.copy(); mutated[3]=(mutated[3]+1)%P
    assert remainder(mutated,p) == [0,0,0,1]
    return {'s':[s2,s3,s4], 'D_coefficients':D, 'S_coefficients':S,
            'p_remainder':[0]*4, 'shared_relations':[0]*4,
            'S_weight35':[S[3],s2*S[5]%P,s3*S[6]%P,s4*S[7]%P,s2*s2*S[7]%P],
            'direct_hessian_nodes':21, 'entry_checks':2100,
            'mutation_rejected':True}


def control():
    np,flint,geo,br,pts = modules()
    start=time.perf_counter()
    before=inputs()
    assert before == read('preflight.json')['input_hashes']
    data=retained()
    basis=data['GEN']['record']['rows']
    bs=data['GEN']['brackets']
    pad=data['PAD']; record=pad['record']
    pivot_original=record['rows']; old_cols=record['columns']
    assert pivot_original==list(range(243)) and all(i in basis for i in pivot_original)
    pivot=[basis.index(i) for i in pivot_original]
    comp=[i for i in range(429) if i not in pivot]
    old=[[pad['values'][b][j] for j in old_cols] for b in basis]
    M=br._fl([old[i] for i in pivot],P)
    assert int(M.det())==record['determinant_mod_p']!=0
    projection=br._fl([old[i] for i in comp],P)*M.inv()
    def residual(vals):
        W=br._fl([vals[i] for i in comp],P)-projection*br._fl([vals[i] for i in pivot],P)
        return W
    assert not any(v for row in matrix_rows(residual(old)) for v in row)
    # Saved generic witness is an inherited positive control for the receiver.
    gen=[[data['GEN']['values'][b][j] for j in range(429)] for b in basis]
    assert int(residual(gen).rank())==186
    timings={'old_basis_and_projection':time.perf_counter()-start}
    rng=np.random.default_rng(SEED)
    L=rng.integers(-8,9,(10,10,POINTS),dtype=np.int64)
    L[0,0]=np.array([2,3,4,5],dtype=np.int64)
    dets=[int(flint.fmpz_mat(L[:,:,k].tolist()).det()) for k in range(POINTS)]
    assert all(d%P for d in dets)
    cubic_coeff=rng.integers(-3,4,(POINTS,165),dtype=np.int64)
    ev=geo.Evaluator([bs[i] for i in basis],9,P,seed=SEED)
    out={'prime':P,'seed':SEED,'L':L.tolist(),'full_support_integer_determinants':dets,
         'split_coefficients':cubic_coeff.tolist(),
         'split_monomial_order':'combinations_with_replacement(range(9),3)',
         'basis_source_indices':basis, 'pivot_basis_indices':pivot,
         'residual_basis_indices':comp, 'old_point_columns':old_cols,
         'old_minor_mod_p':int(M.det()),'projection':matrix_rows(projection),
         'inherited_generic_residual_rank':186,'families':{}}
    for family in ['SPLIT','PAD']:
        stamp=time.perf_counter()
        terms=[cubic_terms(family,cubic_coeff[k]) for k in range(POINTS)]
        reds,cs,shifts=family_jets(L,terms,np,geo,br,pts)
        point_seconds=time.perf_counter()-stamp
        stamp=time.perf_counter()
        vals=list(map(list,zip(*(ev.values(red) for red in reds))))
        R=residual(vals)
        minor=geo.minor_certificate(matrix_rows(R),P)
        eval_seconds=time.perf_counter()-stamp
        stamp=time.perf_counter()
        hs=[hessian_control(reds[k],L[:,:,k].tolist(),cs[k],shifts[k],terms[k],br) for k in range(POINTS)]
        hessian_seconds=time.perf_counter()-stamp
        out['families'][family]={'points':POINTS,'c':cs,'depression_shift':shifts,
             'values':vals,'residual_values':matrix_rows(R), 'residual_minor':minor,
             'augmented_rank':243+minor['rank_lb'],'hessian':hs,
             'S5_sample_rank':br.rank_mod([h['S_weight35'] for h in hs],P),
             'timings':{'point_seconds':point_seconds,'evaluation_and_residual_seconds':eval_seconds,'hessian_seconds':hessian_seconds}}
        print(family,'residual rank',minor['rank_lb'],'augmented',243+minor['rank_lb'],flush=True)
    out['timings']=timings
    out['total_seconds']=time.perf_counter()-start
    assert inputs()==before
    out['input_hashes']=before
    out['status']='BOUNDED_COMPARISON_COMPLETE'
    save('control.json',out)


def replay():
    np,flint,geo,br,pts=modules()
    result=read('control.json')
    assert inputs()==result['input_hashes']
    data=retained()
    basis=result['basis_source_indices']
    cols=result['old_point_columns']
    old=[[data['PAD']['values'][b][j] for j in cols] for b in basis]
    piv=result['pivot_basis_indices']; comp=result['residual_basis_indices']
    M=br._fl([old[i] for i in piv],P)
    projection=br._fl([old[i] for i in comp],P)*M.inv()
    assert matrix_rows(projection)==result['projection']
    L=np.array(result['L'],dtype=np.int64)
    # Same eight saved geometric points, different bracket interpolation nodes.
    ev=geo.Evaluator([data['GEN']['brackets'][i] for i in basis],9,P,seed=SEED+77)
    checks={}
    for family in ['SPLIT','PAD']:
        ts=[cubic_terms(family,result['split_coefficients'][k]) for k in range(POINTS)]
        reds,cs,shifts=family_jets(L,ts,np,geo,br,pts)
        vals=list(map(list,zip(*(ev.values(red) for red in reds))))
        rec=result['families'][family]
        assert vals==rec['values'] and cs==rec['c'] and shifts==rec['depression_shift']
        R=br._fl([vals[i] for i in comp],P)-projection*br._fl([vals[i] for i in piv],P)
        assert matrix_rows(R)==rec['residual_values']
        m=geo.minor_certificate(matrix_rows(R),P)
        assert m==rec['residual_minor']
        mutated=[row.copy() for row in vals]
        mutated[comp[0]][0]=(mutated[comp[0]][0]+1)%P
        MR=br._fl([mutated[i] for i in comp],P)-projection*br._fl([mutated[i] for i in piv],P)
        assert MR!=R
        checks[family]={'points_replayed':POINTS,'entries_rebuilt':429*POINTS,
                        'residual_rank':m['rank_lb'],'changed_entry_rejected':True}
    save('replay.json',{'status':'PASS','changed_interpolation_seed':SEED+77,
                      'input_hashes_match':True,'checks':checks})
    print(json.dumps(checks))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['preflight','control','replay'])
    args=parser.parse_args()
    globals()[args.mode]()
