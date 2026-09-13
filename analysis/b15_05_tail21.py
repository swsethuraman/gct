"""B15-05 bounded tail-21 controls, measurement and geometric replay.

New orchestration: gpt-6-astra. The imported B14-06 bracket and jet
implementations retain Claude Opus 5 attribution. No shared files changed.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
import flint
from flint import nmod_mat

from b14_06_bracket import (BracketEvaluator, CONVENTIONS, DEGS, PRIMES,
    brute_value, consistency_defect, det_mod, enumerate_brackets,
    jet_point_list, random_point)
from b14_06_points import family_DET, family_DETQ

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b15_05'
TAIL = [21] + [2] * 7
LEASE = ROOT.parents[2] / 'Batch15_Launch/native_20260913/LEASES.json'
INPUTS = ['analysis/b14_06_bracket.py', 'analysis/b14_06_points.py',
          'results/b14_04/stable_summary.json', 'results/b14_08/witnesses.json',
          'results/b15_prep/transport_overlay.json',
          'results/integrate/inherited_exclusions.json',
          'results/b15_prep/ci73_acceptance.json', 'docs/s57_report.md',
          'docs/b14_05_transport.md', 'docs/b14_06_review.md']


def save(name, value):
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


def seed(family):
    return int.from_bytes(hashlib.sha256(('B15-05-v1:' + family).encode()).digest()[:8], 'little')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def mat(a, p):
    a = np.asarray(a)
    need(a.ndim == 2 and min(a.shape) > 0, 'empty/nonmatrix input')
    return nmod_mat(a.shape[0], a.shape[1], [int(x) % p for x in a.flat], p)


def guard(rank, ambient=533):
    need(0 <= rank <= ambient, 'rank outside ambient dimension')


def pivots(a, p):
    rr, rank = mat(a, p).rref()
    result = []
    for i in range(rank):
        result.append(next(j for j in range(rr.ncols()) if rr[i, j]))
    return result


def red_guard(red, col, p):
    need(consistency_defect(red, col, p) == 0, 'Euler jet disagreement')
    need(all(red[d][2][i][j] % p == red[d][2][j][i] % p
             for d in DEGS for i in range(col) for j in range(col)), 'nonsymmetric Hessian')


def explicit_points(family, npts):
    rng = np.random.default_rng(seed(family))
    if family == 'DET':
        a = rng.integers(-50, 51, (8, 4, 4, npts), dtype=np.int64)
        a[:, 3, 3] = -(a[:, 0, 0] + a[:, 1, 1] + a[:, 2, 2])
        return a
    a = rng.integers(-50, 51, (npts, 3, 8, 8), dtype=np.int64)
    return a + a.transpose(0, 1, 3, 2)


def points_to_red(family, data, p):
    if family == 'DET':
        j, jets, aux = family_DET(data.shape[-1], p, np.random.default_rng(0), A=data)
        need(bool(np.all(aux['valid'])), 'unexpected invalid traceless pencil')
        red = jet_point_list(j, jets)
    else:
        red = []
        for triple in data:
            r = {}
            for k, d in enumerate(DEGS):
                n = (triple[k] % p).tolist()
                r[d] = (n[0][0], [n[i][0] for i in range(8)], n)
            red.append(r)
    for r in red:
        red_guard(r, 8, p)
    return red


def controls():
    start = time.perf_counter()
    tests = []
    def check(name, truth):
        need(bool(truth), name)
        tests.append(name)
    def rejects(name, fn):
        try:
            fn()
        except ValueError:
            tests.append(name)
        else:
            raise ValueError('defect was not rejected: ' + name)
    from b14_06_run import control_C2, _c8
    for p in PRIMES:
        data = explicit_points('DET', 3)
        red = points_to_red('DET', data, p)
        br = enumerate_brackets(16, 8)
        ev = BracketEvaluator(br, 8, p)
        check(f'{p}: independent liveness', len(br) == 1 and all(
            ev.values(r)[0] == 40320 * det_mod(r[2][2], p) % p != 0 for r in red))
        check(f'{p}: brute formula and factorial/nonsymmetry defects', control_C2(p))
        ok, twin, _ = _c8(p, 3)
        check(f'{p}: DETQ shifted jets and changed pencil', ok and twin)
        rr = copy.deepcopy(red[0]); rr[2][1][0] += 1
        rejects(f'{p}: Euler defect', lambda: red_guard(rr, 8, p))
        bs = enumerate_brackets(13, 3)
        re = random_point(3, p, np.random.default_rng(89))
        vals = BracketEvaluator(bs, 3, p).values(re)
        check(f'{p}: sign defect', any(v and sum(b[0]) % 2 and
              (-v) % p != brute_value(b, re, 3, p) for b, v in zip(bs, vals)))
    rejects('empty matrix', lambda: mat([], PRIMES[0]))
    rejects('ambient rank defect', lambda: guard(534))
    check('research zero rank is allowed', guard(0) is None)
    check('fixed seed repeats', np.array_equal(explicit_points('DET', 3), explicit_points('DET', 3)))
    check('family seeds differ', seed('DET') != seed('GEN'))
    import sympy as s
    c = s.symbols('c0:5')
    q = 12*c[0]*c[4] - 3*c[1]*c[3] + c[2]**2
    dq = s.expand(sum((5-j)*c[j-1]*s.diff(q, c[j]) for j in range(1, 5)))
    check('q44 exact raising derivative', dq == 0 and q != 0)
    qbad = q - c[2]**2
    check('q44 altered coefficient detected', s.expand(sum(
        (5-j)*c[j-1]*s.diff(qbad, c[j]) for j in range(1, 5))) != 0)
    w = json.loads((ROOT / INPUTS[3]).read_text())['witnesses']
    w = next(v for v in w if v['weight'] == [4, 4])
    check('q44 banked terms', [v['coefficient'] for v in w['terms']] == [12, -3, 1])
    br = enumerate_brackets(35, 8)
    counts = dict(brackets=len(br), before_swap_dedupe=len(enumerate_brackets(35, 8, dedupe=False)),
                  patterns=len(set((b[0], b[1]) for b in br)),
                  matrix_bytes_per_prime_600_points_uint32=600*len(br)*4,
                  pencil_bytes_600_points_int64=8*4*4*600*8)
    ev = BracketEvaluator(br, 8, PRIMES[0]); t = time.perf_counter()
    reds = points_to_red('DET', explicit_points('DET', 3), PRIMES[0])
    construction = time.perf_counter()-t; t = time.perf_counter()
    values = [ev.values(r) for r in reds]
    evaluation = time.perf_counter()-t; t = time.perf_counter()
    small_rank = int(mat(values, PRIMES[0]).rank()); guard(small_rank)
    reduction = time.perf_counter()-t
    result = dict(status='EXACT', controls=tests, versions=dict(numpy=np.__version__, flint=flint.__version__),
        counts=counts, timing=dict(construction_3_points=construction,
        evaluation_3_points=evaluation, reduction_3_points=reduction), small_rank_lb=small_rank,
        wall_seconds=time.perf_counter()-start, source_conventions=CONVENTIONS,
        input_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in INPUTS},
        seed_method='first eight SHA256 bytes of B15-05-v1:FAMILY, little endian',
        seeds={f:seed(f) for f in ['DET','GEN']})
    save('controls.json', result)
    save('source.json', dict(tail=TAIL, weighted_degree=35, stable_ambient=533,
        finite_degree26_ambient=531, brackets=br, conventions=CONVENTIONS,
        generic_integral_form='N00*x0^d + d*sum_i>0 N0i*x0^(d-1)*xi + binom(d,2)*sum_i,j>0 Nij*x0^(d-2)*xi*xj',
        determinant_form='det(s0*I4 + sum_k=0..7 xk*Ak); each Ak integral traceless',
        lifting='rational symmetric tensors with denominators dividing d(d-1); house primes are units; brackets are epsilon contractions over Q'))
    print(json.dumps(result), flush=True)


def lease_check():
    data = json.loads(LEASE.read_text(encoding='utf-8'))
    need('05' in data['holders'], 'B15-05 has no heavy lease')
    return data


def transport():
    """Finite transport checks, independent of the stable rank measurement."""
    sys.path.insert(0, str(ROOT/'tools/integrate'))
    from exclusion_predicates import conclusions_for, validate_cell
    ledger = json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    overlay = json.loads((ROOT/'results/b15_prep/transport_overlay.json').read_text())
    selected = [r for r in overlay['targets'] if r['lam'][1:] == TAIL]
    need(len(selected) == 2 and all(r['status']=='OPEN' and r['padded_ideal_floor']==3
         for r in selected), 'accepted overlay disagreement')
    checks = []
    for degree in [15,16,24,25,26,35,100]:
        lam = [4*degree-35] + TAIL
        cell = dict(n=4,ell=9,delta=degree,**{'lambda':lam})
        validate_cell(cell)
        conclusions = conclusions_for(ledger,cell,'quartic_padded_gap')
        need(not conclusions, 'cell already excluded in scoped ledger')
        product_weight = [21+4+4*(degree-15),17+4]+[2]*7
        need(product_weight == lam and 13+2+degree-15==degree, 'finite transport weight/degree')
        checks.append(dict(degree=degree,partition=lam,matched_exclusions=conclusions,padded_ideal_lb=3))
    save('transport.json',dict(status='EXACT',scope='arithmetic, ledger predicates and symbolic q44 only',
        checks=checks,overlay_records=selected,source_weight=[21,17]+[2]*7,
        multiplier_weight=[4,4],multiplier_degree=2,
        formula='q44*u^(d-15); u=24*c0; 12*c0*c4-3*c1*c3+c2^2',
        generic_parameter_argument='For all integers d>=15, degree=d, partition=(4d-35,21,2^7), ordered with nine rows.',
        finite_ideal_argument='Restriction to c=1 followed by depression injects each finite highest-weight ideal into the stable ideal; this does not require a(d)=a_inf.',
        inherited_premises=['three exact degree13 reducible equations, hence padded equations',
            'polynomial ring is an integral domain; product preserves highest weight and ideal membership',
            'S57 Proposition S identifies determinant stable locus with traceless-pencil coefficients',
            'a_inf=533 and a26=531'],
        bound_formula='i_det(d)<=533-r_det_inf; i_pad(d)>=3; D(d)<=530-r_det_inf',
        finite26=dict(a=531,padded_ideal_lb=3,padded_coordinate_ub=528),
        no_finite_coordinate_rank_substitution=True))
    print('Finite transport and scoped ledger checks passed',flush=True)


def defect():
    """Intentional nonzero control: altered stored value must be rejected."""
    p = PRIMES[0]
    ev = BracketEvaluator(enumerate_brackets(16,8),8,p)
    red = points_to_red('DET',explicit_points('DET',1),p)[0]
    correct = ev.values(red)[0]
    altered = (correct+1)%p
    need(correct==altered,'EXPECTED DEFECT: altered stored bracket value disagrees')


def evaluate(family, p, ev, npts):
    data = explicit_points(family, npts)
    np.savez_compressed(OUT / f'{family.lower()}_points.npz', data=data)
    all_values = []; growth = []; construction = evaluation = reduction = 0.0
    for lo in range(0, npts, 40):
        hi = min(lo+40, npts)
        selected = data[..., lo:hi] if family == 'DET' else data[lo:hi]
        t = time.perf_counter(); red = points_to_red(family, selected, p)
        construction += time.perf_counter()-t
        t = time.perf_counter(); all_values.extend(ev.values(r) for r in red)
        evaluation += time.perf_counter()-t
        t = time.perf_counter(); rank = int(mat(all_values, p).rank()); guard(rank)
        reduction += time.perf_counter()-t
        growth.append(dict(points=hi, rank_lb=rank))
        save(f'{family.lower()}_{p}_progress.json', dict(status='RECORDED',
             family=family,prime=p,completed_points=hi,requested_points=npts,
             rank_lb=rank,growth=growth,
             timing=dict(construction=construction,evaluation=evaluation,reduction=reduction),
             replay='First completed_points entries of the explicit point file; use source.json brackets.'))
        print(json.dumps(dict(family=family, prime=p, **growth[-1])), flush=True)
    values = np.asarray(all_values, dtype=np.uint32)
    np.savez_compressed(OUT / f'{family.lower()}_{p}_values.npz', values=values)
    t = time.perf_counter()
    cols = pivots(values, p); rows = pivots(values[:, cols].T, p)
    minor = values[np.ix_(rows, cols)]
    determinant = int(mat(minor, p).det())
    need(determinant != 0 and len(cols) == rank, 'exported minor disagreement')
    np.savez_compressed(OUT / f'{family.lower()}_{p}_minor.npz', values=minor)
    reduction += time.perf_counter()-t
    record = dict(status='REPLAYED_RANK_FLOOR', family=family, prime=p, rank_lb=rank,
        points=npts, minor_rows=rows, minor_columns=cols, minor_determinant=determinant,
        growth=growth, timing=dict(construction=construction, evaluation=evaluation, reduction=reduction),
        values_are='exact residues; source columns, geometric point rows; actual exported minor')
    save(f'{family.lower()}_{p}_certificate.json', record)
    return record, values


def pilot():
    lease = lease_check(); start = time.perf_counter()
    controls_record = json.loads((OUT/'controls.json').read_text())
    need(controls_record['status'] == 'EXACT', 'controls not passed')
    save('lease_at_pilot.json', lease)
    brackets = enumerate_brackets(35, 8)
    records = []
    for p in PRIMES:
        ev = BracketEvaluator(brackets, 8, p)
        gen, generic = evaluate('GEN', p, ev, 560)
        need(gen['rank_lb'] == 533, 'generic ambient completeness disagreement')
        det, determinant = evaluate('DET', p, ev, 600)
        cols = gen['minor_columns']
        d = determinant[:, cols]
        rank = int(mat(d, p).rank())
        need(rank == det['rank_lb'], 'generic basis lost determinant rank')
        rr, r = mat(d, p).rref()
        pc = [next(j for j in range(rr.ncols()) if rr[i,j]) for i in range(r)]
        free = [j for j in range(533) if j not in pc]
        kernel = []
        for j in free:
            v = [0]*533; v[j] = 1
            for i,k in enumerate(pc): v[k] = -int(rr[i,j]) % p
            kernel.append(v)
        if kernel:
            product = mat(d,p)*mat(np.asarray(kernel).T,p)
            need(all(product[i,j] == 0 for i in range(product.nrows())
                     for j in range(product.ncols())), 'candidate kernel residual')
        save(f'kernel_{p}.json', dict(status='CANDIDATE', prime=p,
             basis_bracket_columns=cols, sampled_kernel_vectors=kernel,
             qualification='modular sampled relations only; no global ideal lower bound'))
        records.extend([gen, det])
    ranks = [r['rank_lb'] for r in records if r['family']=='DET']
    need(len(set(ranks)) == 1, 'cross-prime rank disagreement')
    save('pilot.json', dict(status='REPLAYED_RANK_FLOOR', records=records,
        det_rank_lb=ranks[0], det_ideal_stable_ub=533-ranks[0], D_ub=530-ranks[0],
        threshold_met=ranks[0]>=530, wall_seconds=time.perf_counter()-start,
        stop='fixed 600 determinant / 560 generic point cap per prime',
        model='gpt-6-astra', inherited=['a_inf=533', 'degree13 three global padded equations', 'Proposition S finite ideal injection']))


def replay():
    lease_check(); results = []; start = time.perf_counter()
    source = json.loads((OUT/'source.json').read_text())
    brackets = [tuple(tuple(x) for x in b) for b in source['brackets']]
    for p in PRIMES:
        for family in ['GEN','DET']:
            record = json.loads((OUT/f'{family.lower()}_{p}_certificate.json').read_text())
            rows, cols = record['minor_rows'], record['minor_columns']
            data = np.load(OUT/f'{family.lower()}_points.npz')['data']
            selected = data[..., rows] if family == 'DET' else data[rows]
            ev = BracketEvaluator([brackets[i] for i in cols], 8, p, seed=20260913)
            red = points_to_red(family, selected, p)
            values = np.array([ev.values(r) for r in red], dtype=np.uint32)
            stored = np.load(OUT/f'{family.lower()}_{p}_minor.npz')['values']
            need(np.array_equal(values, stored), 'fresh geometric minor disagreement')
            determinant = int(mat(values,p).det())
            need(determinant == record['minor_determinant'] != 0, 'fresh minor determinant disagreement')
            results.append(dict(family=family,prime=p,rank_lb=len(rows),
                entries_checked=values.size,minor_determinant=determinant))
            print(json.dumps(results[-1]), flush=True)
    save('replay.json',dict(status='REPLAYED_RANK_FLOOR',fresh_geometry=True,
         interpolation_seed=20260913, records=results,wall_seconds=time.perf_counter()-start))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('mode',choices=['controls','transport','defect','pilot','replay'])
    args = parser.parse_args()
    {'controls':controls,'transport':transport,'defect':defect,'pilot':pilot,'replay':replay}[args.mode]()
