"""B16-09 bounded geometric completion of the attributed B15-08 sources.

Run only under the inspected analysis/b15_bound.py (60 s / 512 MiB).
No workers, subprocesses, dense carriers, lease acquisition, or B15 writes.
"""
import sys
sys.dont_write_bytecode = True
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations_with_replacement, permutations
import json
from math import comb, factorial, prod
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[2]
SOURCE = ROOT.parent / 'B15-08'
BUNDLE = ROOT / 'delivery/b16_09/inputs'
OUT = ROOT / 'results/b16_09'
if BUNDLE.exists():
    sys.path.insert(0, str(BUNDLE / 'analysis'))
    sys.path.insert(0, str(BUNDLE / 'analysis/b14_04'))
else:
    sys.path.insert(0, str(SOURCE / 'analysis'))
    sys.path.insert(0, str(SOURCE / 'analysis/b14_04'))
from flint import fmpz_mat, fmpq_mat, nmod_mat
from b15_08_bracket import value, work_count, tensor_from_polynomials
from b15_08_points import from_parameters
from recount import exp_series, scalar
from wk8_s30_pleth import chi

H = 8
TAIL = (4, 3) + (2,) * 6
PRIMES = (2147483647, 2147483629)
SOURCES = (((2, 3),) * 7 + ((2, 4), (3, 7)),
           ((2, 3),) * 6 + ((3, 7), (4, 7)))


def save(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')


def pricing():
    # Each of 24 permutation products multiplies four <=9-term linear forms.
    # Supports after k factors are <=binom(8+k,k), so pair visits are bounded.
    visits = 24 * sum(comb(8+k, k) * 9 for k in range(4))
    result = dict(status='PRICED_SMALL_CONTROL', h=H, tail=TAIL,
        finite_degree=19, finite_weight=[57, *TAIL], conservative_range='delta>=19',
        source_letters=[len(b) for b in SOURCES],
        per_source_work=[work_count(b, H) for b in SOURCES],
        tensor_entries_per_point=sum(comb(H+d-1, d) for d in (2, 3, 4)),
        native_polynomial_support_upper=comb(12, 4),
        native_coefficient_pair_visits_per_point_upper=visits,
        one_prime_pilot_points=1, final_points=2,
        final_bracket_determinants_upper=2*3*sum(work_count(b,H)['determinants'] for b in SOURCES),
        final_bracket_order_max=8, matrix_size=[2,2],
        caps=dict(seconds=60, memory_mib=512, processes=1, blas_threads=1),
        heavy_lease_used=False,
        estimate='Small sparse products and <=528 order-eight determinants; no dense expansion.')
    save('pricing.json', result)
    print(json.dumps(result), flush=True)


def parameters(index):
    rng = random.Random(160900 + index)
    A = [[[rng.randrange(-2,3) for _ in range(4)] for _ in range(4)] for _ in range(H)]
    for a in A:
        a[3][3] = -sum(a[i][i] for i in range(3))
    return dict(family='DET', seed=160900+index, A=A)


def native_exact(params):
    """Independent integer 4x4 determinant expansion, ordinary coefficients."""
    A = params['A']
    assert len(A)==H and all(sum(a[i][i] for i in range(4))==0 for a in A)
    full = {}
    visits = 0
    for perm in permutations(range(4)):
        sign = (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = {():sign}
        for i,j in enumerate(perm):
            row = [int(i==j)] + [a[i][j] for a in A]
            nxt = {}
            for mon,coefficient in term.items():
                for k,v in enumerate(row):
                    if not v: continue
                    visits += 1
                    key = tuple(sorted(mon+(k,)))
                    nxt[key] = nxt.get(key,0)+coefficient*v
            term = {key:v for key,v in nxt.items() if v}
        for key,v in term.items():
            full[key] = full.get(key,0)+v
    full = {key:v for key,v in full.items() if v}
    assert full[(0,0,0,0)]==1
    assert not any(key.count(0)==3 for key in full)
    poly = {d:{} for d in (2,3,4)}
    for key,v in full.items():
        d=4-key.count(0)
        if d in poly:
            poly[d][tuple(k-1 for k in key if k)] = v
    # Multinomial denominators all divide 24. Both source row scales are saved.
    tensors = {d:{} for d in poly}
    for d in poly:
        for key in combinations_with_replacement(range(H),d):
            mult = factorial(d)//prod(factorial(v) for v in Counter(key).values())
            assert 24 % mult == 0
            tensors[d][key] = poly[d].get(key,0)*(24//mult)
    return full, poly, tensors, visits


def frame(params):
    """Complete the nine actual directions to an invertible 16-variable frame."""
    rows = [[int(i==j) for i in range(4) for j in range(4)]]
    rows += [[v for row in a for v in row] for a in params['A']]
    assert fmpq_mat(rows).rank()==9
    added=[]
    for j in range(16):
        unit=[int(i==j) for i in range(16)]
        if fmpq_mat(rows+[unit]).rank()>len(rows):
            rows.append(unit); added.append(j)
        if len(rows)==16: break
    determinant=int(fmpz_mat(rows).det())
    assert determinant
    return dict(rows=rows, added_matrix_unit_indices=added, integer_determinant=determinant)


def trace(M): return sum(M[i,i] for i in range(M.nrows()))


def alternate_values(T):
    """Independent adjugate/mixed-discriminant formula on invertible Q."""
    Q=fmpq_mat([[T[2][tuple(sorted((i,j)))] for j in range(H)] for i in range(H)])
    inv=Q.inv(); qdet=Q.det()
    C=[fmpq_mat([[T[3][tuple(sorted((i,j,k)))] for j in range(H)] for i in range(H)]) for k in (0,1)]
    E=[fmpq_mat([[T[4][tuple(sorted((i,j,k,0)))] for j in range(H)] for i in range(H)]) for k in (0,1)]
    u=[T[2][(0,k)] for k in (0,1)]
    B=factorial(7)*qdet*(u[0]*trace(inv*C[1])-u[1]*trace(inv*C[0]))
    def mixed(X,Y): return trace(inv*X)*trace(inv*Y)-trace(inv*X*inv*Y)
    F=factorial(6)*qdet*(mixed(C[0],E[1])-mixed(C[1],E[0]))
    assert B.denominator==F.denominator==1
    return [int(B),int(F)]


def pilot():
    t=time.perf_counter(); params=parameters(0)
    point,meta=from_parameters(params,H,PRIMES[0])
    construction=time.perf_counter()-t
    t=time.perf_counter(); vals=[value(b,point,H,PRIMES[0]) for b in SOURCES]
    elapsed=time.perf_counter()-t
    result=dict(status='MEASURED_PILOT', parameters=params, prime=PRIMES[0], values=vals,
                construction_seconds=construction, evaluation_seconds=elapsed,
                source_count=2, points=1, raw_support=len(meta['raw']), heavy_lease_used=False)
    save('pilot.json',result);print(json.dumps(result),flush=True)


def compute():
    start=time.perf_counter(); records=[]
    for index in range(2):
        params=parameters(index)
        t=time.perf_counter(); raw,polys,T,visits=native_exact(params)
        construction=time.perf_counter()-t
        t=time.perf_counter(); exact=[value(b,T,H) for b in SOURCES]
        evaluation=time.perf_counter()-t
        alternative=alternate_values(T)
        assert exact==alternative
        mods=[]
        for p in PRIMES:
            # Reconstruct using original B15-08 polynomial code, not saved tensors.
            point,meta=from_parameters(params,H,p)
            assert meta['c']==1 and not meta['g1']
            assert meta['raw']=={key:v%p for key,v in raw.items() if v%p}
            assert point==tensor_from_polynomials(polys,H,p)
            assert all(T[d][key]%p==24*entry%p for d,table in point.items() for key,entry in table.items())
            values=[value(b,point,H,p) for b in SOURCES]
            assert values==[v*pow(24**len(b),-1,p)%p for v,b in zip(exact,SOURCES)]
            mods.append(dict(prime=p, unscaled_values=values))
        # Independent direct evaluation of native matrix determinant at fixed arguments.
        controls=[]
        for s in (0,1,2):
            x=[s]+[((i+1)*(s+2))%7-3 for i in range(H)]
            direct=int(fmpz_mat([[x[0]*int(i==j)+sum(x[k+1]*a[i][j] for k,a in enumerate(params['A']))
                                   for j in range(4)] for i in range(4)]).det())
            expansion=sum(v*prod(x[j] for j in key) for key,v in raw.items())
            assert direct==expansion
            controls.append(dict(argument=x, direct_determinant=direct))
        records.append(dict(parameters=params, full_frame=frame(params),
            native_ordinary_coefficients=[[list(key),v] for key,v in sorted(raw.items())],
            scaled24_tensors={str(d):[[list(key),v] for key,v in sorted(table.items())] for d,table in T.items()},
            source_values_scaled24=exact, independent_trace_values_scaled24=alternative,
            modular_evaluations=mods, direct_polynomial_controls=controls,
            construction_seconds=construction, evaluation_seconds=evaluation,
            coefficient_pair_visits=visits))
    matrix=[[point['source_values_scaled24'][i] for point in records] for i in range(2)]
    minor=int(fmpz_mat(matrix).det()); assert minor!=0
    rational=Fraction(minor,24**sum(map(len,SOURCES)))
    modular_minors=[]
    for j,p in enumerate(PRIMES):
        M=[[point['modular_evaluations'][j]['unscaled_values'][i] for point in records] for i in range(2)]
        d=int(nmod_mat(M,p).det()); assert d and int(nmod_mat(M,p).rank())==2
        assert d==rational.numerator*pow(rational.denominator,-1,p)%p
        modular_minors.append(dict(prime=p,matrix=M,minor=d,rank=2))
    t=time.perf_counter(); F=exp_series(19)[19]; ambient=scalar(F,TAIL); assert ambient==2
    character_seconds=time.perf_counter()-t
    return dict(status='PASS_DETERMINANT_RANK_TWO',h=H,tail=TAIL,finite_degree=19,
        finite_weight=[57,*TAIL],stable_range='delta>=19, lambda=(4*delta-19,4,3,2^6)',
        sources=SOURCES,row_scaling=[24**len(b) for b in SOURCES],points=records,
        integer_scaled_matrix=matrix,integer_scaled_minor=minor,
        actual_rational_minor=[rational.numerator,rational.denominator],
        modular_minors=modular_minors,ambient=ambient,
        character_terms=[[list(rho),c.numerator,c.denominator,chi(TAIL,rho)] for rho,c in sorted(F.items())],
        character_seconds=character_seconds,seconds=time.perf_counter()-start,
        claims=dict(a=2,m_det=2,i_det=0,m_pad_upper=2,D_upper=0),
        inherited=['B15-08 source highest-weight and finite-difference proof',
                   'S57 Proposition S at delta>=19 and length-nine inheritance into 16 variables',
                   'B14-04 rational character recurrence and character implementation'],
        fresh=['integer determinant polynomials and full frames', 'two source evaluations by two algebraic formulas',
               'rank-two integer/rational/minors and both modular reconstructions','exact ambient character arithmetic'],
        padding='No padding evaluation or exact padding rank claimed; use only m_pad<=a.',
        heavy_lease_used=False)


def verify_saved(saved,fresh):
    assert len(saved['points'])==len(fresh['points'])==2
    for key in ('h','tail','finite_degree','finite_weight','sources','row_scaling',
                'integer_scaled_matrix','integer_scaled_minor','actual_rational_minor',
                'modular_minors','ambient','character_terms','claims'):
        assert json.loads(json.dumps(fresh[key]))==saved[key], key
    for a,b in zip(saved['points'],fresh['points']):
        for key in ('parameters','full_frame','native_ordinary_coefficients','scaled24_tensors',
                    'source_values_scaled24','independent_trace_values_scaled24','modular_evaluations',
                    'direct_polynomial_controls','coefficient_pair_visits'):
            assert a[key]==b[key], key


def verify_inputs():
    path=ROOT/'delivery/b16_09/input_manifest.json'
    if not path.exists():
        raise FileNotFoundError('Package the frozen input manifest before replay.')
    manifest=json.loads(path.read_text(encoding='utf-8-sig'))
    checks=[]
    for item in manifest['inputs']:
        snapshot=ROOT/'delivery/b16_09'/item['snapshot']
        actual=sha256(snapshot.read_bytes()).hexdigest()
        assert actual==item['sha256'], str(snapshot)
        checks.append(dict(snapshot=item['snapshot'],sha256=actual))
    # Bind executing local modules to the same byte-exact snapshots.
    imported=[]
    for name in ('b15_08_bracket','b15_08_points','recount','wk8_s30_pleth'):
        imported.append(dict(module=name,path=str(Path(sys.modules[name].__file__).resolve()),
            sha256=sha256(Path(sys.modules[name].__file__).read_bytes()).hexdigest()))
        assert imported[-1]['sha256'] in {item['sha256'] for item in manifest['inputs']}
    return dict(status='PASS',snapshot_checks=checks,imported_modules=imported)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['price','pilot','certify','replay'])
    mode=ap.parse_args().mode
    if mode=='price': pricing();return
    if mode=='pilot': pilot();return
    hashes=verify_inputs() if mode=='replay' else None
    fresh=compute()
    if mode=='certify':
        save('certificate.json',fresh)
    else:
        saved=json.loads((OUT/'certificate.json').read_text())
        verify_saved(saved,fresh)
        import copy
        bad=copy.deepcopy(saved);bad['integer_scaled_matrix'][0][0]+=1
        try: verify_saved(bad,fresh)
        except AssertionError: pass
        else: raise AssertionError('altered evaluation accepted')
        bad=copy.deepcopy(saved);bad['points'][0]['parameters']['A'][0][0][0]+=1
        try: verify_saved(bad,fresh)
        except AssertionError: pass
        else: raise AssertionError('altered native point accepted')
        save('replay.json',dict(status='PASS',fresh_certificate=fresh,
            input_verification=hashes,
            mutations_rejected=['source evaluation +1','native determinant entry +1']))
    print(json.dumps({key:fresh[key] for key in ('status','integer_scaled_matrix','actual_rational_minor','modular_minors','claims','seconds')}),flush=True)


if __name__=='__main__':main()
