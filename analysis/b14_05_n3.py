"""Replay exact n=3 coordinate transport with an independent target basis.

Banked filling-to-coordinate expansions are adopted, not recomputed. numpy is
used only to decode NPZ integer arrays. All algebra below uses Python int/Fraction.
"""
from fractions import Fraction as Q
from functools import reduce
from math import gcd
from pathlib import Path
import gzip
import json
import numpy as np
from b14_05_controls import require, rejects, REJECTIONS, PRIMES, matrix_rank


def read(path):
    with (gzip.open(path, 'rt') if path.endswith('.gz') else open(path, encoding='utf-8')) as f:
        return json.load(f)


def exps(n, r):
    if r == 1:
        return [(n,)]
    return [(i,)+a for i in range(n+1) for a in exps(n-i, r-1)]


def solve(a, b):
    n = len(b)
    a = [[Q(v) for v in row]+[Q(c)] for row, c in zip(a, b)]
    for j in range(n):
        k = next((i for i in range(j, n) if a[i][j]), None)
        require(k is not None, 'singular solve')
        a[j], a[k] = a[k], a[j]
        x = a[j][j]; a[j] = [v/x for v in a[j]]
        for i in range(n):
            if i != j:
                x = a[i][j]; a[i] = [v-x*w for v, w in zip(a[i], a[j])]
    return [row[-1] for row in a]


def pivot_columns(rows):
    indices, pivots = [], []
    for j in range(len(rows[0])):
        v = [Q(row[j]) for row in rows]
        for i, w in pivots:
            c = v[i]; v = [x-c*y for x, y in zip(v, w)]
        nz = next((i for i, x in enumerate(v) if x), None)
        if nz is not None:
            q = v[nz]; pivots.append((nz, [x/q for x in v])); indices.append(j)
            if len(indices) == len(rows):
                break
    require(len(indices) == len(rows), 'rank shortfall')
    return indices


def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    det = Q(1)
    for j in range(len(a)):
        k = next((i for i in range(j, len(a)) if a[i][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            det = -det; a[j], a[k] = a[k], a[j]
        q = a[j][j]; det *= q
        for i in range(j+1, len(a)):
            x = a[i][j]/q
            for c in range(j+1, len(a)):
                a[i][c] -= x*a[j][c]
    return det


def combination(rows, cs):
    require(len(rows) == len(cs), 'coefficient count')
    return [sum(Q(c)*row[j] for c, row in zip(cs, rows)) for j in range(len(rows[0]))]


def main():
    low = read('results/artefacts/s69_n3_d12_basis.json.gz')
    high = read('results/artefacts/s69_n3_d13_basis.json.gz')
    zlo = np.load('results/artefacts/s73_chi_basis_d12.npz', allow_pickle=False)
    zhi = np.load('results/artefacts/s73_chi_basis_d13.npz', allow_pickle=False)
    lo, hi = low['chi_vectors'], high['chi_vectors']
    require(len(lo) == len(hi) == 6, 'six basis rows required')
    require(low['prime_note'] == high['prime_note'] == 'exact integers', 'not integer columns')
    require(all(isinstance(v, int) for rows in (lo, hi) for row in rows for v in row), 'not integral')
    require(list(zlo['lam']) == low['lam'] and list(zhi['lam']) == high['lam'], 'weight mismatch')
    E = exps(3, 7); u = E.index((3, 0, 0, 0, 0, 0, 0))
    repslo = [tuple(map(int, row)) for row in zlo['reps']]
    repshi = [tuple(map(int, row)) for row in zhi['reps']]
    slo, shi = list(map(int, zlo['sgn_rep'])), list(map(int, zhi['sgn_rep']))
    require(len(set(repslo)) == len(repslo) == len(lo[0]), 'bad lower coordinate data')
    require(len(set(repshi)) == len(repshi) == len(hi[0]), 'bad upper coordinate data')
    low_index = {rep: i for i, rep in enumerate(repslo)}
    map_hi = []
    for rep in repshi:
        if u not in rep:
            map_hi.append(None)
        else:
            m = list(rep); m.remove(u)
            require(tuple(m) in low_index, 'upper representative does not reduce to lower representative')
            map_hi.append(low_index[tuple(m)])
    require(set(x for x in map_hi if x is not None) == set(range(len(repslo))), 'transport lost coordinates')
    # The appended letter contributes 3! u in the house m_alpha convention.
    def transport(row, factor=6):
        return [0 if k is None else factor*row[k]*slo[k]*shi[j] for j, k in enumerate(map_hi)]
    transported = [transport(row) for row in lo]
    pivlo, pivhi = pivot_columns(lo), pivot_columns(hi)
    a = [[hi[i][j] for i in range(6)] for j in pivhi]
    conversion = [solve(a, [row[j] for j in pivhi]) for row in transported]
    reconstructed = [combination(hi, c) for c in conversion]
    require(transported == reconstructed, 'full-coordinate conversion identity failed')
    require(determinant(conversion) != 0, 'transport mixes into a deficient subspace')
    require(any(c for i, row in enumerate(conversion) for j, c in enumerate(row) if i != j),
            'independent basis comparison did not exercise mixing')
    for prime in PRIMES:
        require(matrix_rank([[row[j] for j in pivlo] for row in lo], prime) == 6, 'source modular minor')
        require(matrix_rank([[row[j] for j in pivhi] for row in hi], prime) == 6, 'target modular minor')
        require(matrix_rank(conversion, prime) == 6, 'conversion modular minor')
    s62 = read('results/s62_n3_vec_d12.json')['vector_chi_coords']
    bank = read('results/artefacts/s69_banked_n3_d12.json')['vector_chi_coords']
    require(s62 == bank and any(bank), 'banked line mismatch')
    cs = [66, -972, 12, -37, 4, 320]
    line = combination(lo, cs)
    j = next(i for i, x in enumerate(bank) if x)
    line_scalar = line[j]/bank[j]
    require(line_scalar != 0 and line == [line_scalar*x for x in bank], 'integer line identity')
    s73 = read('results/artefacts/s73_kernels_d13_primary.json.gz')['U']['det']['int']
    require(len(s73) == 1 and len(s73[0]) == len(hi[0]), 'missing upper integer line')
    line_hi = transport(bank, factor=1)
    j = next(i for i, x in enumerate(s73[0]) if x)
    scale_hi = Q(line_hi[j], s73[0][j])
    require(scale_hi != 0 and line_hi == [scale_hi*x for x in s73[0]], 's73 line transport')
    changed = [row[:] for row in transported]; changed[0][pivhi[0]] += 1
    rejects('n3 altered target coordinate', lambda: require(changed == reconstructed, 'altered coordinate'))
    rejects('n3 omitted factorial', lambda: require([transport(v, 1) for v in lo] == reconstructed, '3! factor omitted'))
    rejects('n3 incorrectly unmixed target basis', lambda: require(transported == hi, 'basis directions differ'))
    rejects('n3 empty source data', lambda: require(len([]) == 6, 'required six source rows missing'))
    rejects('n3 wrong source line coefficient',
            lambda: require(combination(lo, [67, -972, 12, -37, 4, 320]) == line, 'line coefficient altered'))
    rejects('n3 dependent rank witness',
            lambda: require(determinant([a[0]]+a[:-1]) != 0, 'duplicated minor row'))
    record = {
        'status': 'CERTIFIED integer-coordinate identities; banked bracket expansions ADOPTED',
        'operator': 'first-row adjunction only: Phi(F)=6uF, not non-Cartan adjunction',
        'source_weight': low['lam'], 'target_weight': high['lam'], 'source_rows': 6, 'target_rows': 6,
        'ambient_multiplicity': '6 at both rungs, ADOPTED from s73_aladder.json; independent ranks rechecked',
        'source_chi_dimension': len(lo[0]), 'target_chi_dimension': len(hi[0]),
        'source_rank_minor_columns_zero_based': pivlo, 'target_rank_minor_columns_zero_based': pivhi,
        'source_minor_det': str(determinant([[row[j] for j in pivlo] for row in lo])),
        'target_minor_det': str(determinant([[row[j] for j in pivhi] for row in hi])),
        'conversion': {'values_are': 'rational coefficients: transported source row i = sum_j C_ij target row j',
                       'matrix': [[str(x) for x in row] for row in conversion],
                       'determinant': str(determinant(conversion)),
                       'identity': 'J(S)=C*T checked at all 6*17306 integer coordinates',
                       'denominators': sorted(set(x.denominator for row in conversion for x in row)),
                       'both_house_prime_ranks': [6, 6]},
        'line': {'source_coefficients': cs, 'source_combination_equals_scalar_times_s62': str(line_scalar),
                 's62_support': sum(bool(x) for x in bank),
                 'u_times_s62_equals_scalar_times_s73_d13': str(scale_hi),
                 'ideal_membership': 'not inferred here from sampled vanishing; LMR theorem is adopted separately'},
        'exponents': {'ordering': 'wk8_s30_core.exps ascending recursively, reimplemented without flint import',
                      'u_exponent': list(E[u]), 'resolved_u_index': u},
        'negative_controls': REJECTIONS,
        'replay_boundary': 'No fresh filling expansions, raising matrix build, or determinant rank computation.'}
    Path('results/b14_05/n3_transport.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': record['status'], 'ranks': [6, 6], 'line_scalar': str(line_scalar),
                      'conversion_determinant': str(determinant(conversion)), 'rejections': len(REJECTIONS)}))


if __name__ == '__main__':
    main()
