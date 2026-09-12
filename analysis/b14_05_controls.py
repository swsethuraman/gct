"""Exact, bounded controls for B14-05. Stdlib only; no historical drivers.

Binary polynomial keys are sorted tuples of (letter type, x2 exponent).
The type degree supplies the x1 exponent. Coefficients are Fractions.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, factorial, gcd
from pathlib import Path
import copy
import json

OUT = Path('results/b14_05')
PRIMES = (2147483647, 2147483629)
DEGREES = {'f': 4, 'l': 1, 'c': 3}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def clean(p):
    return {m: Q(c) for m, c in p.items() if c}


def add(*polys):
    out = Counter()
    for p in polys:
        for m, c in p.items():
            out[m] += c
    return clean(out)


def scale(p, s):
    return clean({m: s*c for m, c in p.items()})


def mul(p, q):
    out = Counter()
    for m, c in p.items():
        for n, d in q.items():
            out[tuple(sorted(m+n))] += c*d
    return clean(out)


def var(t, j):
    return {((t, j),): Q(1)}


def root(p, raising):
    out = Counter()
    for m, c in p.items():
        for k, (t, j) in enumerate(m):
            n = DEGREES[t]
            if (raising and j == 0) or (not raising and j == n):
                continue
            new_j = j-1 if raising else j+1
            factor = n-j+1 if raising else j+1
            mm = list(m); mm[k] = (t, new_j)
            out[tuple(sorted(mm))] += c*factor
    return clean(out)


def weight(p, expected):
    require(bool(p), 'zero polynomial does not witness a direction')
    for m in p:
        require((sum(DEGREES[t]-j for t, j in m), sum(j for t, j in m)) == expected,
                'wrong weight')
    require(not root(p, True), 'raising operator is nonzero')


def bracket(columns, types, normalized=True):
    counts = Counter(x for col in columns for x in col)
    require(set(counts) == set(range(len(types))), 'missing or extra letter')
    require(all(counts[i] == DEGREES[t] for i, t in enumerate(types)), 'wrong valence')
    require(all(1 <= len(c) <= 2 and len(c) == len(set(c)) for c in columns),
            'bad binary column')
    pairs = [c for c in columns if len(c) == 2]
    require(2**len(pairs) <= 1000000, 'expansion budget')
    out = Counter()
    for bits in product((0, 1), repeat=len(pairs)):
        twos = [0]*len(types)
        for col, bit in zip(pairs, bits):
            twos[col[1-bit]] += 1
        coeff = (-1)**sum(bits)
        if normalized:
            for t, j in zip(types, twos):
                coeff *= factorial(j)*factorial(DEGREES[t]-j)
        mon = tuple(sorted(zip(types, twos)))
        out[mon] += coeff
    return clean(out)


def extend(columns, new_letter, k, n=4):
    b = sum(len(c) == 2 for c in columns)
    require(all(len(c) == 2 for c in columns[:b]), 'columns not in diagram order')
    require(len(columns)-b >= k, 'strip not horizontal')
    out = [list(c) for c in columns]
    for i in range(b, b+k):
        out[i].append(new_letter)
    out += [[new_letter] for _ in range(n-k)]
    return out


def averaged_extension(columns, types, k):
    b = sum(len(c) == 2 for c in columns)
    pairs, singletons = columns[:b], columns[b:]
    out = {}
    for chosen in combinations(range(len(singletons)), k):
        chosen = set(chosen)
        reordered = pairs + [c for i, c in enumerate(singletons) if i in chosen]
        reordered += [c for i, c in enumerate(singletons) if i not in chosen]
        out = add(out, bracket(extend(reordered, len(types), k), types+['f']))
    return scale(out, Q(1, comb(len(singletons), k)))


def pieri_binary(p, a, b, k, n=4):
    m = a-b
    require(0 <= k <= min(m, n) and n == 4, 'unsupported strip')
    term, coefficient, result = p, Q(1), {}
    for i in range(k+1):
        result = add(result, scale(mul(term, var('f', k-i)), coefficient))
        if i < k:
            coefficient *= Q(-(n-k+1+i), (i+1)*(m-i))
            term = root(term, False)
    return result


def matrix_rank(rows, prime=None):
    if not rows:
        return 0
    require(all(len(x) == len(rows[0]) for x in rows), 'ragged matrix')
    if prime:
        for row in rows:
            for x in row:
                require(Q(x).denominator % prime != 0, 'bad denominator')
        a = [[int(Q(x).numerator)*pow(int(Q(x).denominator), -1, prime) % prime
              for x in row] for row in rows]
    else:
        a = [[Q(x) for x in row] for row in rows]
    rank = 0
    for j in range(len(a[0])):
        idx = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if idx is None:
            continue
        a[rank], a[idx] = a[idx], a[rank]
        inv = pow(a[rank][j], -1, prime) if prime else 1/a[rank][j]
        a[rank] = [(x*inv) % prime if prime else x*inv for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][j]:
                v = a[i][j]
                a[i] = [(x-v*y) % prime if prime else x-v*y
                        for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def coefficient_matrix(polys):
    monomials = sorted(set().union(*(set(p) for p in polys)))
    return monomials, [[p.get(m, 0) for m in monomials] for p in polys]


def encode_poly(p):
    return [{'monomial': [list(x) for x in m], 'coefficient': str(c)} for m, c in sorted(p.items())]


def dim_binary(d, b, n=4):
    def count(w):
        return sum(sum(m) == w for m in combinations_with_replacement(range(n+1), d))
    return count(b)-count(b-1)


def evaluate(p, values):
    out = Q(0)
    for m, c in p.items():
        for t, j in m:
            c *= values[t][j]
        out += c
    return out


REJECTIONS = []


def rejects(name, check):
    try:
        check()
    except (ValueError, KeyError, TypeError, ZeroDivisionError) as e:
        REJECTIONS.append({'name': name, 'rejected': True, 'reason': str(e)})
    else:
        raise RuntimeError('Control did not reject: '+name)


def binary_control():
    # Both diagrams represent 576*(8 c0 c2-3 c1^2)^2; singleton order is invisible.
    pairs = [[0, 1], [0, 1], [2, 3], [2, 3]]
    t = pairs + [[i] for i in [0, 0, 1, 1, 2, 2, 3, 3]]
    u = pairs + [[i] for i in [0, 2, 0, 1, 1, 2, 3, 3]]
    s = [[0, 1]]*4 + [[2]]*4 + [[3]]*4
    types = ['f']*4
    f, g = bracket(t, types), bracket(s, types)
    require(f == bracket(u, types), 'source relation failed')
    h = add(scale(mul(var('f', 0), var('f', 2)), 8), scale(mul(var('f', 1), var('f', 1)), -3))
    require(f == scale(mul(h, h), 576), 'source normalization')
    for p in (f, g):
        weight(p, (12, 4))
    require(dim_binary(4, 4) == 2 and dim_binary(5, 6) == 2, 'dimension count')
    raw_t = bracket(extend(t, 4, 2), types+['f'])
    raw_u = bracket(extend(u, 4, 2), types+['f'])
    difference = add(raw_t, scale(raw_u, -1))
    require(bool(difference), 'expected non-Cartan obstruction not found')
    for p in (raw_t, raw_u):
        weight(p, (14, 6))
    rejects('raw adjunction descends to source polynomials',
            lambda: require(raw_t == raw_u, 'equal source representatives have unequal images'))
    images = [pieri_binary(p, 12, 4, 2) for p in (f, g)]
    for p in images:
        weight(p, (14, 6))
    for diagram, im in zip((t, s), images):
        require(averaged_extension(diagram, types, 2) == scale(im, 4), 'averaged adjunction identity')
    require(averaged_extension(t, types, 2) == averaged_extension(u, types, 2), 'averaging depends on representative')
    _, src = coefficient_matrix([f, g]); _, dst = coefficient_matrix(images)
    require(matrix_rank(src) == matrix_rank(dst) == 2, 'two directions required')
    for prime in PRIMES:
        require(matrix_rank(src, prime) == matrix_rank(dst, prime) == 2, 'modular rank check')
    mixed = [add(f, scale(g, 2)), add(scale(f, 3), scale(g, 5))]
    mixed_images = [add(images[0], scale(images[1], 2)), add(scale(images[0], 3), scale(images[1], 5))]
    require([pieri_binary(p, 12, 4, 2) for p in mixed] == mixed_images, 'basis mixing failure')
    rejects('unmixed image under changed source basis',
            lambda: require([pieri_binary(p, 12, 4, 2) for p in mixed] == images, 'basis change was not applied'))
    rejects('wrong averaged-adjunction normalization',
            lambda: require(averaged_extension(t, types, 2) == images[0], 'missing factor (n-k)! k! = 4'))
    rejects('zero multiplier as injective witness', lambda: weight({}, (6, 2)))
    # q62 and q44 are the two degree-two Cartan factors, no census is recomputed.
    q44 = add(scale(mul(var('f', 0), var('f', 4)), 12),
              scale(mul(var('f', 1), var('f', 3)), -3), mul(var('f', 2), var('f', 2)))
    weight(h, (6, 2)); weight(q44, (4, 4))
    point = {'f': [1, 2, 3, 4, 5]}
    # Retain the whole symbolic difference even if this first point is a zero.
    witness = next((list(v) for v in product(range(3), repeat=5)
                    if evaluate(difference, {'f': v})), None)
    require(witness is not None, 'no evaluation witness')
    return {'status': 'CERTIFIED counterexample; PROVED corrected binary operator in companion note',
            'source_weight': [12, 4], 'target_weight': [14, 6], 'source_dim': 2, 'target_dim': 2,
            'source_fillings': [t, u, s], 'raw_extensions': [extend(t, 4, 2), extend(u, 4, 2)],
            'equal_source': encode_poly(f), 'second_source': encode_poly(g),
            'raw_image_t': encode_poly(raw_t), 'raw_image_u': encode_poly(raw_u),
            'difference': encode_poly(difference), 'witness_point': witness,
            'witness_difference': str(evaluate(difference, {'f': witness})),
            'operator_images': [encode_poly(p) for p in images],
            'average_to_operator_factor': 4, 'basis_change_rows': [[1, 2], [3, 5]],
            'source_coefficient_rank_Q': 2, 'image_coefficient_rank_Q': 2,
            'modular_ranks': {str(p): [matrix_rank(src, p), matrix_rank(dst, p)] for p in PRIMES},
            'values_are': 'exact ordinary coefficient polynomials; m_alpha=alpha! c_alpha'}


def mixed_control():
    # Bidegree (2,2), shape (6,2), two independent target directions.
    types = ['l', 'l', 'c', 'c']
    t = [[0, 1], [2, 3], [2], [2], [3], [3]]
    # t is identically zero after equal linear letters coalesce; it tests this cancellation.
    require(not bracket(t, types), 'linear-letter coalescing control')
    a = [[0, 2], [1, 3], [2], [2], [3], [3]]
    b = [[2, 3], [2, 3], [0], [1], [2], [3]]
    polys = [bracket(c, types) for c in (a, b)]
    for p in polys:
        weight(p, (6, 2))
        require(all(sum(t == 'l' for t, j in m) == 2 and sum(t == 'c' for t, j in m) == 2 for m in p), 'mixed bidegree')
    require(matrix_rank(coefficient_matrix(polys)[1]) == 2, 'mixed directions')
    rejects('mixed factorial normalization error', lambda: require(bracket(a, types, False) == polys[0], 'alpha factorials omitted'))
    rejects('mixed wrong valence', lambda: bracket(a, ['c']*4))
    # Pullback of a quartic bracket: choose one linear slot in each old letter.
    old = [[0, 1], [0, 1], [0], [0], [1], [1]]
    source = bracket(old, ['f', 'f'])
    pullback = {}
    for mon, coefficient in source.items():
        term = {(): coefficient}
        for _, j in mon:
            factors = {}
            if j <= 3:
                factors = add(factors, mul(var('l', 0), var('c', j)))
            if j >= 1:
                factors = add(factors, mul(var('l', 1), var('c', j-1)))
            term = mul(term, factors)
        pullback = add(pullback, term)
    occurrences = [[(j, k) for j, col in enumerate(old) for k, x in enumerate(col) if x == i]
                   for i in range(2)]
    split_sum = {}
    split_fillings = []
    for chosen in product(*occurrences):
        split = [[x+2 for x in col] for col in old]
        for i, (j, k) in enumerate(chosen):
            split[j][k] = i
        split_sum = add(split_sum, bracket(split, types))
        split_fillings.append(split)
    require(pullback == split_sum and bool(pullback), 'quartic-to-mixed pullback normalization')
    rejects('extra factor in mixed slot splitting',
            lambda: require(pullback == scale(split_sum, Q(1, 16)), 'slot splitting is a sum, not an average in m normalization'))
    return {'status': 'CERTIFIED small mixed membership control', 'weight': [6, 2],
            'bidegree': [2, 2], 'types': types, 'fillings': [a, b],
            'coefficient_rank_Q': 2, 'polynomials': [encode_poly(p) for p in polys],
            'pullback_control': {'quartic_filling': old, 'mixed_splits': split_fillings,
                                 'split_count': 16, 'identity': 'mu_star(F_T)=sum_of_all_4^2_slot_splits',
                                 'exact_pullback': encode_poly(pullback)},
            'values_are': 'ordinary l and cubic coefficients; cubic m_alpha=alpha! c_alpha'}


def poly_value(coefficients, x):
    return sum(Q(c)*Q(x)**i for i, c in enumerate(coefficients))


def ci_check(c):
    require(c['target_model'] == 'Q[t] degree <= 1', 'unjustified target model')
    require(c['dimension'] == 2, 'wrong proved dimension')
    require(c['source_model'] == 'span(y0,y1,y2); pullback (1,t,2t)', 'source model')
    require(c['values_are'] == 'unscaled exact pullback values; source rows, point columns', 'scaling convention')
    points, gs = c['points'], c['target_polynomials']
    require(len(gs) == 2 and len(points) >= 2, 'missing target or points')
    require(all(len(g) <= 2 for g in gs), 'target member outside N')
    b = [[poly_value(g, p) for p in points] for g in gs]
    require(b == c['target_values'], 'target entry or point mismatch')
    require(matrix_rank(b) == 2, 'target minor zero')
    for prime in PRIMES:
        require(matrix_rank(b, prime) == 2, 'modular target minor zero')
    a = [[poly_value(g, p) for p in points] for g in ([1], [0, 1], [0, 2])]
    require(a == c['source_values'], 'source entry or scaling mismatch')
    k = c['kernel_columns']
    require(len(k) == 3 and all(len(row) == 1 for row in k), 'kernel orientation')
    require(all(sum(a[i][j]*Q(k[i][0]) for i in range(3)) == 0 for j in range(len(points))), 'A^T K nonzero')
    require(matrix_rank(k) == 1 and matrix_rank(a) == 2, 'incomplete kernel')
    return True


def ci_control():
    c = {'target_model': 'Q[t] degree <= 1', 'dimension': 2,
         'source_model': 'span(y0,y1,y2); pullback (1,t,2t)',
         'values_are': 'unscaled exact pullback values; source rows, point columns',
         'points': [0, 1, 2], 'target_polynomials': [[1], [0, 1]],
         'target_values': [[1, 1, 1], [0, 1, 2]],
         'source_values': [[1, 1, 1], [0, 1, 2], [0, 2, 4]],
         'kernel_columns': [[0], [-2], [1]]}
    require(ci_check(c), 'CI control rejected')
    mutants = {}
    def mutate(name, key, value):
        q = copy.deepcopy(c); q[key] = value; mutants[name] = q
    mutate('CI wrong dimension', 'dimension', 3)
    mutate('CI invalid target membership', 'target_polynomials', [[1], [0, 0, 1]])
    mutate('CI target deficient', 'target_polynomials', [[1], [1]])
    mutants['CI target deficient']['target_values'] = [[1, 1, 1], [1, 1, 1]]
    mutate('CI target missing', 'target_polynomials', [])
    mutate('CI wrong points', 'points', [0, 1, 3])
    mutate('CI source altered integer', 'source_values', [[1, 1, 1], [0, 1, 2], [0, 2, 5]])
    mutate('CI source scaled row', 'source_values', [[1, 1, 1], [0, 2, 4], [0, 2, 4]])
    mutate('CI kernel transposed', 'kernel_columns', [[0, -2, 1]])
    mutate('CI false null vector', 'kernel_columns', [[0], [-1], [1]])
    mutate('CI incompatible values_are', 'values_are', 'divided by u')
    q = copy.deepcopy(c); del q['source_values']; mutants['CI source missing'] = q
    for name, mutant in mutants.items():
        rejects(name, lambda mutant=mutant: ci_check(mutant))
    for prime in PRIMES:
        rejects('denominator divisible by '+str(prime), lambda prime=prime: matrix_rank([[Q(1, prime)]], prime))
    c['status'] = 'CERTIFIED abstract CI control, not an LMR interpolation certificate'
    c['rank_Q'] = 2; c['nullity_Q'] = 1
    return c


def main():
    OUT.mkdir(exist_ok=True)
    result = {'binary_adjunction': binary_control(), 'mixed': mixed_control(), 'ci': ci_control()}
    result['negative_controls'] = REJECTIONS
    result['status'] = 'PASS for qualified claims; raw adjunction REFUTED'
    (OUT/'controls.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'negative_controls_rejected': len(REJECTIONS),
                      'counterexample_value': result['binary_adjunction']['witness_difference']}))


if __name__ == '__main__':
    main()
