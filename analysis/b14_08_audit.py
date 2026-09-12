"""Independent exact B14-08 transport census. Python stdlib; no house counters.

Counts coefficient monomials then extracts Schur multiplicities by alternation.
Positive witnesses are independently solved from actual raising matrices over Q.
All output paths are session-owned. See results/PREREG_b14_08.md and replay.md.
"""
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
import csv
import hashlib
import json
from math import comb, gcd, lcm
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b14_08'
BASE = '9898e56941a7665f231873481dae956f08509995'
PRIMES = (2147483647, 2147483629)
SOURCES = {'rung13': (13, (21, 17) + (2,) * 7),
           'rung14': (14, (25, 17) + (2,) * 7),
           'lmr': (24, (65, 17) + (2,) * 7)}
CONTROLS = {(25, (69, 17) + (2,) * 7), (26, (73, 17) + (2,) * 7),
            (26, (71, 19) + (2,) * 7), (26, (69, 21) + (2,) * 7)}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')


def key(row):
    return row['degree'], tuple(row.get('partition', row.get('nu', [])))


def read_targets(document):
    require('rows' in document, 'missing rows')
    rows = []
    all_keys = []
    for row in document['rows']:
        d, nu = key(row)
        require(type(d) is int and d in (25, 26), 'unexpected degree')
        require(nu and all(type(x) is int and x > 0 for x in nu), 'invalid partition')
        require(tuple(sorted(nu, reverse=True)) == nu and sum(nu) == 4*d,
                'partition shape/weight')
        require(row['length'] == len(nu), 'length mismatch')
        require(row['tensor_multiplicity'] > 0, 'nonpositive tensor multiplicity')
        all_keys.append((d, nu))
        if len(nu) <= 10:
            rows.append(row)
    require(len(all_keys) == len(set(all_keys)), 'duplicated census key')
    keys = set(map(key, rows))
    require(Counter(d for d, _ in keys) == {25: 31, 26: 208}, 'incomplete target counts')
    require(CONTROLS <= keys, 'missing named control')
    require(Counter((r['degree'], r['length']) for r in rows) ==
            {(25, 9): 15, (25, 10): 16, (26, 9): 89, (26, 10): 119}, 'length census')
    # Ten-row degree-25 cases first, as requested; remainder deterministic.
    return sorted(rows, key=lambda r: (not (r['degree'] == 25 and r['length'] == 10),
                                      r['degree'], tuple(-x for x in r['partition'])))


def validate_reference(reference, rows):
    expected = {name: {'lam': list(lam), 'delta': d} for name, (d, lam) in SOURCES.items()}
    require(reference.get('sources') == expected, 'wrong/missing reference source')
    targets = reference.get('targets', [])
    require(len(targets) == 239 and len({key(r) for r in targets}) == 239,
            'missing/duplicate reference target')
    require({key(r) for r in targets} == {key(r) for r in rows}, 'reference key mismatch')
    for row in targets:
        require(row['length'] == len(row['nu']), 'reference length mismatch')
        require(set(row['reached_by']) == set(SOURCES), 'missing reference flag')
        require(all(type(v) is bool for v in row['reached_by'].values()), 'flag must be boolean')
    return {key(r): r for r in targets}


def validate_flags(rows):
    by_key = {key(r): r for r in rows}
    require(len(rows) == len(by_key) == 239, 'incomplete flag census')
    require(CONTROLS <= set(by_key), 'missing flag controls')
    require(all(by_key[k]['reached_by']['lmr'] for k in CONTROLS), 'LMR-specific control')
    require(not any(any(r['reached_by'].values()) for r in rows if r['length'] == 10),
            'ten-row source scope control')


@lru_cache(None)
def tail_letters(tail):
    return tuple(t for t in product(*(range(min(4, x)+1) for x in tail)) if 1 <= sum(t) <= 4)


@lru_cache(None)
def weight_count(degree, weight):
    """Unordered monomials in quartic coefficient letters; arbitrary-precision Z."""
    if degree < 0 or any(x < 0 for x in weight) or sum(weight) != 4*degree:
        return 0
    weight = tuple(x for x in sorted(weight, reverse=True) if x)
    if len(weight) <= 1:
        return 1
    tail = weight[1:]
    letters = tail_letters(tail)

    @lru_cache(None)
    def count(index, left, target):
        if not any(target):
            return 1  # remaining factors are u; first weight is forced
        if index == len(letters) or left <= 0 or sum(target) > 4*left:
            return 0
        letter = letters[index]
        high = min([left] + [b//a for a, b in zip(letter, target) if a])
        return sum(count(index+1, left-m, tuple(b-m*a for a, b in zip(letter, target)))
                   for m in range(high+1))
    return count(0, degree, tail)


@lru_cache(None)
def multiplicity(degree, mu):
    """[x^mu] char(A_degree)*prod_(i<j)(1-x_j/x_i)."""
    terms = Counter()
    r = len(mu)
    for perm in permutations(range(r)):
        beta = tuple(mu[i]-i+perm[i] for i in range(r))
        if min(beta) < 0:
            continue
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(r) for j in range(i+1, r))
        terms[tuple(sorted(beta, reverse=True))] += sign
    certificate = []
    result = 0
    for beta, sign in sorted(terms.items(), reverse=True):
        if sign:
            count = weight_count(degree, beta)
            result += sign*count
            certificate.append({'weight': list(beta), 'alternant_coefficient': sign,
                                'weight_monomials': count})
    require(result >= 0, 'negative character multiplicity')
    return result, certificate


def difference_test(d, nu, source):
    ds, lam = SOURCES[source]
    width = max(len(nu), len(lam))
    diff = tuple((nu[i] if i < len(nu) else 0) - (lam[i] if i < len(lam) else 0)
                 for i in range(width))
    require(sum(diff) == 4*(d-ds), 'difference degree mismatch')
    result = {'source': source, 'degree_difference': d-ds, 'difference': list(diff),
              'reached': False, 'witness_id': None}
    for i, x in enumerate(diff):
        if x < 0:
            return dict(result, reason='negative_coordinate', failure_row=i+1)
    for i in range(width-1):
        if diff[i] < diff[i+1]:
            return dict(result, reason='not_dominant', failure_rows=[i+1, i+2])
    mu = tuple(x for x in diff if x)
    mult, terms = multiplicity(d-ds, mu)
    return dict(result, reached=bool(mult), reason='positive_multiplicity' if mult else 'zero_multiplicity',
                multiplicity=mult, character_terms=terms,
                witness_id=('w_%d_%s' % (d-ds, '_'.join(map(str, mu)))) if mult else None)


def source_monomials(degree, mu):
    """Fresh generator, distinct from the coin DP used for weight counts."""
    r = len(mu)
    tail = mu[1:]
    letters = sorted(tail_letters(tail), reverse=True)
    u = (4,) + (0,)*(r-1)
    answer = []

    def walk(start, left, target, factors):
        if not any(target):
            answer.append(tuple(sorted(factors + [u]*left)))
            require(len(answer) <= 400, 'registered 400-monomial witness cap')
            return
        if left == 0 or sum(target) > 4*left:
            return
        for j in range(start, len(letters)):
            t = letters[j]
            if all(a <= b for a, b in zip(t, target)):
                walk(j, left-1, tuple(b-a for a, b in zip(t, target)), factors+[(4-sum(t),)+t])
    walk(0, degree, tail, [])
    return sorted(answer)


def raised_monomial(monomial, root):
    result = Counter()
    for alpha, power in Counter(monomial).items():
        if alpha[root+1]:
            beta = list(alpha); beta[root] += 1; beta[root+1] -= 1
            new = list(monomial); new.remove(alpha); new.append(tuple(beta))
            result[tuple(sorted(new))] += power*(alpha[root]+1)
    return result


def solve_witness(degree, mu, expected_mult, witness_id):
    start = time.monotonic()
    monomials = source_monomials(degree, mu)
    require(len(monomials) == weight_count(degree, mu), 'independent weight count disagreement')
    rows = {}
    for col, mon in enumerate(monomials):
        for root in range(len(mu)-1):
            for raised, value in raised_monomial(mon, root).items():
                rows.setdefault((root, raised), {})[col] = Fraction(value)
    require(len(rows) <= 1200, 'registered 1200-row witness cap')
    pivots = {}
    for _, raw in sorted(rows.items()):
        row = dict(raw)
        while row:
            p = min(row)
            if p not in pivots:
                scale = row[p]
                pivots[p] = {j: v/scale for j, v in row.items()}
                break
            scale = row[p]
            for j, v in pivots[p].items():
                row[j] = row.get(j, Fraction(0)) - scale*v
                if not row[j]:
                    del row[j]
    nullity = len(monomials)-len(pivots)
    require(nullity == expected_mult and nullity > 0, 'raising nullity versus character multiplicity')
    free = next(j for j in range(len(monomials)) if j not in pivots)
    vector = [Fraction(int(j == free)) for j in range(len(monomials))]
    for p, row in sorted(pivots.items(), reverse=True):
        vector[p] = -sum(value*vector[j] for j, value in row.items() if j != p)
    denominators = sorted({v.denominator for v in vector})
    scale = lcm(*denominators)
    integers = [int(v*scale) for v in vector]
    content = gcd(*integers)
    sign = 1 if next(v for v in integers if v) > 0 else -1
    integers = [v//content*sign for v in integers]
    terms = [{'coefficient': v, 'factors': [{'alpha': list(a), 'power': m}
               for a, m in sorted(Counter(mon).items())]}
             for mon, v in zip(monomials, integers) if v]
    return {'id': witness_id, 'degree': degree, 'weight': list(mu),
            'values_are': 'primitive integer coefficients in ordinary c_alpha monomials',
            'coefficient_convention': 'c_alpha(F)=[s^alpha]F',
            'terms': terms, 'normalization': {'rational_denominators': denominators,
             'cleared_lcm': scale, 'integer_content_removed': content, 'sign': sign,
             'denominators_coprime_to_house_primes': all(gcd(scale, p) == 1 for p in PRIMES)},
            'construction': {'matrix_orientation': 'raised monomial rows; source monomial columns; right kernel',
             'rows': len(rows), 'columns': len(monomials), 'rational_rank': len(pivots),
             'nullity': nullity, 'character_multiplicity': expected_mult,
             'values_are': 'ordinary coefficient-basis raising map entries over Q',
             'seconds': time.monotonic()-start}}


@lru_cache(None)
def scalar_tail_bound(r, degree, tail_weight):
    # Exact coefficient [z^degree t^tail_weight] in the non-u scalar-tail character.
    state = {(0, 0): 1}
    for j in range(1, 5):
        count = comb(r+j-2, j)
        after = Counter()
        for (d, s), value in state.items():
            for m in range(min(degree-d, (tail_weight-s)//j)+1):
                after[d+m, s+j*m] += value*comb(count+m-1, m)
        state = after
    return state.get((degree, tail_weight), 0)


def ambient_inputs():
    result = {}
    for row in json.loads((ROOT/'results/b13_06/run_summary.json').read_text())['ambient_counts']:
        result[row['degree'], tuple(row['partition'])] = (row['a'], 'B13-06 exact ambient count, ADOPTED')
    for row in json.loads((ROOT/'results/b14_prep/ladder_recount.json').read_text())['values']:
        head = row['cell'].strip('()').split(',')
        nu = (int(head[0]), int(head[1]))+(2,)*7
        result.setdefault((row['delta'], nu), (row['a'], 'frozen single-method recount, RECORDED'))
    return result


def attach_bounds(row, tests, ambient):
    d, nu = key(row)
    predecessor = (nu[0]-4,)+nu[1:]
    require(predecessor[0] >= predecessor[1], 'nonpartition u-predecessor')
    a, a_source = ambient.get((d, nu), (None, None))
    ap, ap_source = ambient.get((d-1, predecessor), (None, None))
    delta = a-ap if a is not None and ap is not None else None
    reached = [t['source'] for t in tests if t['reached']]
    p_names = ['p13' if s == 'rung13' else 'p14' if s == 'rung14' else 'p24' for s in reached]
    ladder = nu[1:] == (17,)+(2,)*7
    upper = 1 if ladder else None
    floor = 'max(0' + ''.join(', '+p for p in p_names) + ')'
    raw_bound = scalar_tail_bound(len(nu), d, sum(nu[1:]))
    return {'lemma_T': {'status': 'CONDITIONAL' if reached else 'NOT REACHED',
             'reached_sources': reached, 'conditional_padded_ideal_floor': floor,
             'certified_padded_ideal_floor': 0, 'source_floor_certificates': None,
             'determinant_ideal_upper_bound': upper,
             'determinant_upper_provenance': 'cartan_ladder_invariance + lmr_ranks, ADOPTED' if ladder else None,
             'D_upper_bound_if_source_floors_certified': str(upper if upper is not None else 'U_det')+' - '+floor,
             'exclusion_condition': 'compatible certified U_det <= '+floor,
             'exclusion_status': 'OPEN',
             'missing': ['positive certified padded source floor'] + ([] if ladder else ['sufficient certified determinant ideal upper bound']),
             'tensor_product_image_upper_is_not_det_ideal_upper': row['tensor_multiplicity']},
            'lemma_B': {'status': 'PROVED formula; inherited numeric inputs labelled separately',
             'predecessor_degree': d-1, 'predecessor_weight': list(predecessor),
             'inequality': '0 <= i_X(target)-i_X(predecessor) <= a(target)-a(predecessor)',
             'applies_to': ['determinant', 'padded', 'reducible'],
             'ambient_target': a, 'ambient_target_provenance': a_source,
             'ambient_predecessor': ap, 'ambient_predecessor_provenance': ap_source,
             'ambient_increment': delta,
             'ambient_increment_status': 'inherited counts, ADOPTED/RECORDED' if delta is not None else 'OPEN exact numeric increment',
             'scalar_tail_birth_upper_bound': raw_bound,
             'birth_upper_bound': delta if delta is not None else raw_bound,
             'bound_kind': 'exact inherited ambient increment' if delta is not None else 'coarse exact monomial upper bound',
             'values_are': 'integer bounds on births; not measured ranks or equations'},
            'ambient_a': a,
            'gap_status': 'OPEN; same frozen [-4,+1] interval as LMR' if ladder else 'OPEN'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, default=OUT)
    args = ap.parse_args()
    start = time.monotonic()
    rows = read_targets(json.loads((ROOT/'results/b13_06/components.json').read_text()))
    reference = validate_reference(json.loads((ROOT/'results/b14_claude_reach.json').read_text()), rows)
    ambient = ambient_inputs()
    result, requests = [], {}
    for row in rows:
        d, nu = key(row)
        tests = [difference_test(d, nu, s) for s in SOURCES]
        flags = {t['source']: t['reached'] for t in tests}
        require(flags == reference[d, nu]['reached_by'], 'frozen flag disagreement: '+str((d, nu)))
        for test in tests:
            if test['reached']:
                requests[test['witness_id']] = (test['degree_difference'], tuple(x for x in test['difference'] if x), test['multiplicity'])
        result.append({'degree': d, 'nu': list(nu), 'length': len(nu), 'reached_by': flags,
                       'tests': tests, 'tensor_multiplicity': row['tensor_multiplicity'],
                       'channels': row['channels'], **attach_bounds(row, tests, ambient)})
    validate_flags(result)
    metadata = {'board_numbering': 'batch14', 'session_id': 'B14-08', 'model': 'gpt-6-astra',
                'base': BASE, 'status': 'character census complete; positive witnesses pending',
                'sources': {s: {'degree': d, 'weight': list(w)} for s, (d, w) in SOURCES.items()},
                'targets': result}
    dump(args.out/'census.json', metadata)  # checkpoint before witness construction
    print(json.dumps({'checkpoint': '239 rows / 717 flags agree', 'unique_positive_differences': len(requests),
                      'seconds': time.monotonic()-start}), flush=True)
    witnesses = []
    for wid, (d, mu, mult) in sorted(requests.items()):
        witness = solve_witness(d, mu, mult, wid)
        witnesses.append(witness)
        dump(args.out/'witnesses.json', {'status': 'in_progress', 'witnesses': witnesses})
    summary = {'targets': len(result), 'tests': 3*len(result),
               'positive_tests': sum(t['reached'] for r in result for t in r['tests']),
               'unique_positive_witnesses': len(witnesses),
               'per_degree': {str(d): {'targets': sum(r['degree'] == d for r in result),
                 'reached_any': sum(r['degree'] == d and any(r['reached_by'].values()) for r in result),
                 'per_source': {s: sum(r['degree'] == d and r['reached_by'][s] for r in result) for s in SOURCES},
                 'ten_row_targets': sum(r['degree'] == d and r['length'] == 10 for r in result)} for d in (25, 26)},
               'numeric_inherited_birth_increments': sum(r['lemma_B']['ambient_increment'] is not None for r in result),
               'certified_exclusions': 0, 'seconds': time.monotonic()-start,
               'largest_raising_matrix_columns': max(w['construction']['columns'] for w in witnesses),
               'largest_raising_matrix_rows': max(w['construction']['rows'] for w in witnesses)}
    metadata['status'] = 'complete combinatorial census; independent verification required'
    metadata['summary'] = summary
    dump(args.out/'census.json', metadata)
    dump(args.out/'witnesses.json', {'status': 'complete', 'witnesses': witnesses})
    dump(args.out/'summary.json', summary)
    with (args.out/'census.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['degree', 'partition', 'length', 'rung13', 'rung14', 'lmr',
                         'witness_ids', 'conditional_i_pad_floor', 'certified_i_pad_floor',
                         'certified_i_det_upper', 'exclusion_status', 'B_predecessor',
                         'B_exact_inherited_increment', 'B_birth_upper', 'B_bound_kind'])
        for row in result:
            t, b = row['lemma_T'], row['lemma_B']
            writer.writerow([row['degree'], str(tuple(row['nu'])), row['length'],
                *row['reached_by'].values(), ';'.join(x['witness_id'] for x in row['tests'] if x['witness_id']),
                t['conditional_padded_ideal_floor'], t['certified_padded_ideal_floor'],
                t['determinant_ideal_upper_bound'], t['exclusion_status'], str(tuple(b['predecessor_weight'])),
                b['ambient_increment'], b['birth_upper_bound'], b['bound_kind']])
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
