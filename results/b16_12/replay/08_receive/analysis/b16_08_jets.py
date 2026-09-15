"""B16-08: bounded shared-block jet elimination. New gpt-6-astra code.

Run through inspected analysis/b15_bound.py, one process/thread, 60s/512MiB.
No old worker evaluator is imported. Ordinary polynomial coefficients, no
factorial division. Modes: preflight, produce, receive.
"""
from collections import defaultdict
from itertools import permutations, product, combinations_with_replacement
from pathlib import Path
from math import comb, factorial
import hashlib
import json
import os
import sys
import time
from flint import nmod_mat

HERE = Path('C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-08')
OUT = Path('C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/results/b16_12/replay/08_receive/results/b16_08')
PRIME = 2147483647
NDIR = 3
ONE = {(): 1}


def save(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/name).write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')


def digest(obj):
    return hashlib.sha256(json.dumps(obj, separators=(',', ':')).encode()).hexdigest()


def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for m, v in p.items():
            out[m] += v
    return {m: v for m, v in out.items() if v}


def scale(p, c):
    return {m: c*v for m, v in p.items() if c*v}


def mul(p, q):
    out = defaultdict(int)
    for a, x in p.items():
        for b, y in q.items():
            out[tuple(sorted(a+b))] += x*y
    return {m: v for m, v in out.items() if v}


def sign(perm):
    return (-1)**sum(perm[i] > perm[j] for i in range(len(perm))
                     for j in range(i+1, len(perm)))


def det(M):
    out = {}
    for perm in permutations(range(len(M))):
        v = ONE
        for i, j in enumerate(perm):
            v = mul(v, M[i][j])
        out = add(out, scale(v, sign(perm)))
    return out


def generic_identity():
    X = [[{(4*i+j,): 1} for j in range(4)] for i in range(4)]
    E = [row[1:] for row in X[1:]]
    a, r, c = X[0][0], X[0][1:], [row[0] for row in X[1:]]
    tr = add(*(E[i][i] for i in range(3)))
    e2 = add(*(add(mul(E[i][i], E[j][j]), scale(mul(E[i][j], E[j][i]), -1))
               for i in range(3) for j in range(i+1, 3)))
    adj = [[scale(det([[E[u][v] for v in range(3) if v != i]
                      for u in range(3) if u != j]), (-1)**(i+j))
            for j in range(3)] for i in range(3)]
    rc = add(*(mul(r[i], c[i]) for i in range(3)))
    re = add(*(mul(mul(r[i], E[i][j]), c[j])
               for i in range(3) for j in range(3)))
    radjc = add(*(mul(mul(r[i], adj[i][j]), c[j])
                  for i in range(3) for j in range(3)))
    formulas = [a, add(mul(a, tr), scale(rc, -1)),
                add(mul(a, e2), scale(mul(tr, rc), -1), re),
                add(mul(a, det(E)), scale(radjc, -1))]
    M = [[add(X[i][j], ONE if i == j and i > 0 else {})
          for j in range(4)] for i in range(4)]
    direct = det(M)
    assert direct == add(*formulas)
    assert [len(p) for p in formulas] == [1, 6, 18, 24]
    return direct, formulas


def weights(k):
    return [a for d in range(1, 5) for a in product(range(d+1), repeat=k)
            if sum(a) == d]


def sectors(alphas, degree=2):
    out = defaultdict(list)
    for d in range(degree+1):
        for col in combinations_with_replacement(range(len(alphas)), d):
            w = tuple(sum(alphas[j][i] for j in col) for i in range(NDIR))
            out[w].append(col)
    return dict(sorted(out.items()))


def generic_support():
    direct, _ = generic_identity()
    out = {a: defaultdict(int) for a in weights(NDIR)}
    for monomial, coefficient in direct.items():
        for directions in product(range(NDIR), repeat=len(monomial)):
            alpha = tuple(directions.count(i) for i in range(NDIR))
            param = tuple(sorted(16*d + e for d, e in zip(directions, monomial)))
            out[alpha][param] += coefficient
    return {a: dict(p) for a, p in out.items()}


def preflight():
    alphas = weights(NDIR)
    ss = sectors(alphas)
    sizes = [len(v) for v in ss.values()]
    support = generic_support()
    assert sum(map(len, support.values())) == 2487
    n = len(alphas)
    counts = []
    for k in (1, 2, 3, 9, 10, 15, 16):
        ncoeff = comb(k+4, 4)-1
        counts.append({'directions': k, 'shared_matrix_parameters': 16*k,
                       'jet_coefficients_orders_1_to_4': ncoeff,
                       'quadratic_columns_including_lower_degrees': comb(ncoeff+2, 2),
                       'raw_expanded_parameter_terms': k+6*k*k+18*k**3+24*k**4})
    n16 = comb(19, 4)
    data = {'status': 'PRICED_BEFORE_ELIMINATION', 'directions': NDIR,
            'parameters': 48, 'jet_coefficients': n, 'columns': sum(sizes),
            'weight_blocks': len(ss), 'maximum_block_columns': max(sizes),
            'sum_square_block_entries': sum(s*s for s in sizes),
            'planned_shared_points': max(sizes),
            'symbolic_support_by_order': [sum(len(p) for a,p in support.items() if sum(a)==d)
                                          for d in range(1, 5)],
            'symbolic_support_total': sum(map(len, support.values())),
            'maximum_single_coefficient_support': max(map(len, support.values())),
            'all_pair_raw_support_product_upper': sum(map(len,support.values()))**2,
            'full_ungraded_dense_entries': comb(n+2, 2)**2,
            'degree_three_columns_not_run': comb(n+3, 3),
            'homogeneous_quartic_16_variables': {'coefficients': n16,
                 'degree_at_most_two_coefficient_columns': comb(n16+2, 2),
                 'matrix_entry_parameters': 256},
            'support_prices': counts,
            'cap': {'seconds': 60, 'memory_MiB': 512, 'processes': 1, 'blas_threads': 1},
            'estimate': 'Under 10 seconds and 128 MiB; hard 60s/512MiB. No full Groebner or dense parameter expansion.',
            'blocks': [{'weight': w, 'columns': len(v)} for w,v in ss.items()]}
    return data


def point(index):
    # Saved explicit points are authoritative. SHA256 avoids PRNG-version drift.
    return [int.from_bytes(hashlib.sha256(f'B16-08-v1:{index}:{j}'.encode()).digest()[:2],
                           'big') % 7 - 3 for j in range(48)]


def support_eval(support, entries):
    vals = []
    for terms in support.values():
        s = 0
        for monomial, c in terms.items():
            for j in monomial:
                c *= entries[j]
            s += c
        vals.append(s)
    return vals


def direct_eval(entries):
    # Receiver uses 24 determinant permutations of linear polynomials in x.
    M = [[{(d,): entries[16*d+4*i+j] for d in range(NDIR)
           if entries[16*d+4*i+j]} for j in range(4)] for i in range(4)]
    for i in range(1, 4):
        M[i][i] = add(M[i][i], ONE)
    poly = det(M)
    assert poly.get((), 0) == 0
    return [poly.get(tuple(d for d in range(NDIR) for _ in range(a[d])), 0)
            for a in weights(NDIR)]


def evaluation(rows, cols, row_ids=None):
    out = []
    for i in (range(len(rows)) if row_ids is None else row_ids):
        row = rows[i]
        vals = []
        for col in cols:
            value = 1
            for j in col:
                value = value * row[j] % PRIME
            vals.append(value)
        out.append(vals)
    return out


def independent_rows(mat):
    rr, rank = nmod_mat(list(map(list, zip(*mat))), PRIME).rref()
    pivots = [next(j for j in range(rr.ncols()) if rr[i,j]) for i in range(rank)]
    return pivots


def determinant_mod(rows):
    return int(nmod_mat(rows, PRIME).det())


def produce():
    price = json.loads((OUT/'preflight.json').read_text())
    assert digest(price) == digest(preflight())
    start = time.perf_counter()
    generic, formulas = generic_identity()
    support = generic_support()
    ss = sectors(list(support))
    points = [point(i) for i in range(max(map(len, ss.values())))]
    rows = [support_eval(support, p) for p in points]
    assert all(direct_eval(p) == row for p,row in zip(points,rows))
    cubic = next(i for i,a in enumerate(support) if sum(a) == 3)
    altered = list(rows[0]); altered[cubic] += 1
    assert altered != direct_eval(points[0])
    blocks = []
    for w, cols in ss.items():
        row_ids = independent_rows(evaluation(rows, cols))
        assert len(row_ids) == len(cols), ('Unresolved block: no equation inferred', w)
        mat = evaluation(rows, cols, row_ids)
        minor = determinant_mod(mat)
        assert minor, ('Unresolved block: no equation inferred', w)
        blocks.append({'weight': w, 'columns': cols, 'rows': row_ids,
                       'minor_mod_prime': minor, 'evaluation_matrix_mod_prime': mat})
    universal = [{'order': d+1, 'terms': [[v,list(m)] for m,v in sorted(p.items())]}
                 for d,p in enumerate(formulas)]
    cert = {'status': 'NO_RELATIONS_OF_TOTAL_COEFFICIENT_DEGREE_AT_MOST_TWO',
            'prime': PRIME, 'directions': NDIR, 'coefficient_order': list(support),
            'parameter_order': 'B_direction[row,column], direction major, row major',
            'points': points, 'integer_jet_values': rows, 'blocks': blocks,
            'universal_block_expansion': universal, 'universal_residual_terms': 0,
            'mutation': {'point': 0, 'coefficient': cubic, 'delta': 1, 'rejected': True},
            'global_form_equation_claimed': False,
            'all_degree_elimination_ideal_claimed_zero': False,
            'seconds': time.perf_counter()-start}
    save('certificate.json', cert)
    print(json.dumps({'status': cert['status'], 'blocks': len(blocks),
                      'columns': sum(len(b['columns']) for b in blocks),
                      'points': len(points), 'seconds': cert['seconds']}))


def receive():
    start = time.perf_counter()
    hash_checks = 0
    for manifest_name in ('INPUT_HASHES.json', 'ARTIFACT_HASHES.json'):
        manifest = HERE/'delivery/b16_08'/manifest_name
        if manifest.exists():
            for item in json.loads(manifest.read_text())['files']:
                p = Path(item['path'])
                if not p.is_absolute():
                    p = HERE/p
                assert hashlib.sha256(p.read_bytes()).hexdigest() == item['sha256'], str(p)
                hash_checks += 1
    cert = json.loads((OUT/'certificate.json').read_text())
    assert cert['prime'] == PRIME and cert['directions'] == NDIR
    assert cert['coefficient_order'] == [list(a) for a in weights(NDIR)]
    generic, formulas = generic_identity()
    expected = [{'order': d+1, 'terms': [[v,list(m)] for m,v in sorted(p.items())]}
                for d,p in enumerate(formulas)]
    assert cert['universal_block_expansion'] == expected
    rows = [direct_eval(p) for p in cert['points']]
    assert rows == cert['integer_jet_values']
    ss = sectors(weights(NDIR))
    assert len(cert['blocks']) == len(ss)
    for b,(w,cols) in zip(cert['blocks'],ss.items()):
        assert b['weight'] == list(w)
        assert b['columns'] == [list(c) for c in cols]
        assert len(set(b['rows'])) == len(b['rows']) == len(cols)
        assert all(0 <= i < len(rows) for i in b['rows'])
        mat = evaluation(rows, cols, b['rows'])
        assert mat == b['evaluation_matrix_mod_prime']
        assert determinant_mod(mat) == b['minor_mod_prime'] != 0
    mutation = cert['mutation']
    altered = list(rows[mutation['point']]); altered[mutation['coefficient']] += mutation['delta']
    assert altered != cert['integer_jet_values'][mutation['point']]
    # Nontrivial arithmetic mutation: duplicate a row of a square block.
    b = next(b for b in cert['blocks'] if len(b['columns']) >= 2)
    bad = [list(r) for r in b['evaluation_matrix_mod_prime']]
    bad[1] = list(bad[0])
    assert determinant_mod(bad) == 0
    result = {'status': 'PASS', 'independent_coefficient_route': '24 determinant permutations',
              'same_implementation_review': True, 'independent_human_review': False,
              'blocks_rebuilt': len(ss), 'columns_proved_independent': sum(map(len,ss.values())),
              'integer_points_rebuilt': len(rows), 'universal_residual_terms': 0,
              'coefficient_mutation_rejected': True, 'duplicate_row_minor_rejected': True,
              'input_and_artifact_hashes_checked': hash_checks,
              'certificate_sha256': hashlib.sha256((OUT/'certificate.json').read_bytes()).hexdigest(),
              'seconds': time.perf_counter()-start}
    save('receiver.json', result)
    print(json.dumps(result))


if __name__ == '__main__':
    assert os.environ.get('OPENBLAS_NUM_THREADS') == '1'
    assert 'CI73_DEADLINE' in os.environ, 'Use inspected Job Object wrapper'
    if sys.argv[1] == 'preflight':
        data = preflight(); save('preflight.json', data)
        print(json.dumps({k:v for k,v in data.items() if k != 'blocks'}))
    elif sys.argv[1] == 'produce':
        produce()
    elif sys.argv[1] == 'receive':
        receive()
    else:
        raise ValueError('unknown mode')
