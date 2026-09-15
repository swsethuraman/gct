"""One fixed independent receiver, 60s/512MiB via original b15_bound.py.

No producer imports, subprocesses, random points, character census or search.
Inherited symbolic E vectors are inputs; Euler elimination and padding arithmetic
are implemented here. Modular evaluation proves a floor, never an upper rank.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import prod
from pathlib import Path
import hashlib
import json
import os
import sys
import time

WT = Path(__file__).resolve().parents[1]
ROOT = WT.parents[2]
P04 = WT.parent / 'B15-04'
OUT = WT / 'results/b17_11/supplement04_08'
PRIME = 1000003
DEGS = (2, 3, 4)
KEEP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
START = time.perf_counter()
COUNTS = {'modular_determinants': 0, 'peak_sparse_entries': 0}


def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def check_inputs():
    ledger = read(OUT / 'input_hashes.json')
    for e in ledger['files']:
        assert hashlib.sha256(Path(e['path']).read_bytes()).hexdigest() == e['sha256']
        if 'snapshot' in e:
            assert hashlib.sha256((WT / e['snapshot']).read_bytes()).hexdigest() == e['sha256']
    return len(ledger['files'])


def determinant(a):
    """Fraction-free Bareiss; works for integer or rational input."""
    a = [list(map(Q, row)) for row in a]
    sign, last = 1, Q(1)
    for k in range(len(a)-1):
        p = next((i for i in range(k, len(a)) if a[i][k]), None)
        if p is None:
            return Q(0)
        if p != k:
            a[k], a[p] = a[p], a[k]
            sign = -sign
        v = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] = (v*a[i][j]-a[i][k]*a[k][j])/last
            a[i][k] = 0
        last = v
    return sign*a[-1][-1]


def sparse_reducer(rows):
    """Ascending-index pivots, independent of producer's descending-key pivots."""
    basis = {}

    def reduce(v):
        v = {k: Q(x) for k, x in v.items() if x}
        for p in sorted(basis):
            x = v.get(p, 0)
            if x:
                for k, z in basis[p].items():
                    y = v.get(k, 0)-x*z
                    if y:
                        v[k] = y
                    else:
                        v.pop(k, None)
        return v

    for row in rows:
        v = reduce(row)
        if v:
            p = min(v)
            lead = v[p]
            basis[p] = {k: x/lead for k, x in v.items()}
        size = sum(map(len, basis.values()))
        COUNTS['peak_sparse_entries'] = max(COUNTS['peak_sparse_entries'], size)
        assert size <= 100000
    return reduce, len(basis)


def comps(n):
    for a in range(n+1):
        for b in range(n-a+1):
            yield (a, b, n-a-b)


def regenerate_relations(brackets):
    index = {b: i for i, b in enumerate(brackets)}

    def locate(I, J, h, z):
        a = tuple(int(i in I) for i in range(3))
        b = tuple(int(i in J) for i in range(3))
        return index[min(a, b), max(a, b), h, z]

    relations = []
    # Ordered bordered-column identity, extracted coefficient by coefficient.
    for size in (1, 2, 3):
        for I in combinations(range(3), size):
            for J in combinations(range(3), size-1):
                for h in comps(10-size):
                    weight = 35-sum(DEGS[j] for j in I+J)-sum(x*y for x, y in zip(DEGS, h))
                    for a in range(max(0, weight//2+1)):
                        for b in range(max(0, (weight-2*a)//3+1)):
                            rem = weight-2*a-3*b
                            if rem < 0 or rem % 4:
                                continue
                            z = (a, b, rem//4)
                            row = defaultdict(int)
                            for j in set(range(3))-set(J):
                                if h[j]:
                                    c = tuple(h[i]-(i == j) for i in range(3))
                                    row[locate(I, J+(j,), c, z)] += h[j]*(-1)**sum(i > j for i in J)
                            for i, j in enumerate(I):
                                zz = tuple(z[q]+(q == j) for q in range(3))
                                row[locate(I[:i]+I[i+1:], J, h, zz)] -= (-1)**(size-1-i)
                            row = {k: Q(x) for k, x in row.items() if x}
                            if row:
                                relations.append(row)
    return relations


def formal_match():
    original = read(ROOT / 'Batch16/claude_review/exact_ideals.json')
    inherited = read(ROOT / 'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/small_evidence.json')
    match = read(P04 / 'results/b17_04/basis_match.json')
    saved_relations = read(P04 / 'results/b17_04/Euler_relations.json')
    brackets = [tuple(map(tuple, b)) for b in original['brackets']]
    assert len(brackets) == len(set(brackets)) == 1019
    assert saved_relations['brackets'] == original['brackets']
    lookup = {b: i for i, b in enumerate(brackets)}
    E = [{lookup[tuple(map(tuple, k))]: Q(x) for k, x in inherited['source_vectors'][j]} for j in KEEP]
    relation_rows = regenerate_relations(brackets)
    signature = lambda r: tuple((k, str(x)) for k, x in sorted(r.items()))
    saved_rows = [{k: Q(x) for k, x in row} for row in saved_relations['relations']]
    assert Counter(map(signature, relation_rows)) == Counter(map(signature, saved_rows))
    reduce, relation_rank = sparse_reducer(relation_rows)
    assert len(relation_rows) == 884 and relation_rank == 590
    M = [list(map(Q, row)) for row in match['M']]
    inv = [list(map(Q, row)) for row in match['inverse']]
    assert len(M) == 11 and match['accepted_basis_indices'] == KEEP
    for i in range(11):
        for j in range(11):
            assert sum(M[i][k]*inv[k][j] for k in range(11)) == (i == j)
    md = determinant(M)
    assert str(md) == match['determinant'] and md
    declared = original['basis_bracket_indices']
    assert len(declared) == len(set(declared)) == 429
    C = [{declared[j]: Q(x) for j, x in enumerate(row) if x} for row in original['I_det']]

    def difference(c, e, coefficients):
        v = defaultdict(Q, c)
        for x, row in zip(coefficients, e):
            for k, y in row.items():
                v[k] -= x*y
        return reduce(v)

    residuals = [len(difference(c, E, row)) for c, row in zip(C, M)]
    assert residuals == [0]*11
    # Omitted original index9 has the exact shared-remainder coordinates.
    omitted = {lookup[tuple(map(tuple, k))]: Q(x) for k, x in inherited['source_vectors'][9]}
    assert not difference(omitted, E, [12,-10,4,3,0,-1,1,1,1,0,0])
    wrong_index = [{j: Q(x) for j, x in enumerate(row) if x} for row in original['I_det']]
    assert any(difference(c, E, row) for c, row in zip(wrong_index, M))
    sign_E = [{k: x*(-1)**sum(brackets[k][0]) for k, x in row.items()} for row in E]
    assert any(difference(c, sign_E, row) for c, row in zip(C, M))
    from math import factorial
    factorial_E = [{k: x*prod(factorial(v) for v in brackets[k][2]) for k, x in row.items()} for row in E]
    assert any(difference(c, factorial_E, row) for c, row in zip(C, M))
    changed = [row[:] for row in M]
    changed[0][0] += 1
    assert difference(C[0], E, changed[0])
    return {'relation_count': len(relation_rows), 'relation_rank': relation_rank,
            'rational_residual_supports': residuals, 'det_M': str(md),
            'inverse_checked': True, 'inherited_E_vectors': True,
            'mutations_rejected': ['wrong429indexmap', 'border_sign', 'mixed_factorials', 'matrix_coefficient']}


def moddet(a):
    COUNTS['modular_determinants'] += 1
    a = [[x % PRIME for x in row] for row in a]
    result = 1
    for k in range(len(a)):
        j = next((j for j in range(k, len(a)) if a[j][k]), None)
        if j is None:
            return 0
        if j != k:
            a[k], a[j] = a[j], a[k]
            result = -result
        v = a[k][k]
        result = result*v % PRIME
        iv = pow(v, -1, PRIME)
        for j in range(k+1, len(a)):
            mult = a[j][k]*iv % PRIME
            for q in range(k+1, len(a)):
                a[j][q] = (a[j][q]-mult*a[k][q]) % PRIME
    return result % PRIME


def hessian(L, t):
    """Unordered pairs of distinct linear factors, with symmetric outer products."""
    result = [[0]*10 for _ in range(10)]
    for sigma in permutations(range(3)):
        factors = [L[0]]+[L[1+3*i+sigma[i]] for i in range(3)]
        for i, j in combinations(range(4), 2):
            val = prod(factors[k][0]*t+factors[k][1] for k in range(4) if k not in (i, j))
            for a in range(10):
                for b in range(10):
                    result[a][b] += val*(factors[i][a]*factors[j][b]+factors[j][a]*factors[i][b])
    return result


def pmul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % PRIME
    return c


def interpolate(values):
    """Lagrange, at fixed distinct nodes -10..10 (producer uses 0..20)."""
    nodes = list(range(-10, 11))
    result = [0]*21
    for i, t in enumerate(nodes):
        numerator, denominator = [1], 1
        for j, u in enumerate(nodes):
            if i != j:
                numerator = pmul(numerator, [-u, 1])
                denominator = denominator*(t-u) % PRIME
        scale = values[i]*pow(denominator, -1, PRIME) % PRIME
        for j, x in enumerate(numerator):
            result[j] = (result[j]+scale*x) % PRIME
    return result


def remainder(a, p):
    a = a[:]
    assert p[-1] == 1
    for j in range(len(a)-1, len(p)-2, -1):
        x = a[j]
        for k, y in enumerate(p):
            a[j-len(p)+1+k] = (a[j-len(p)+1+k]-x*y) % PRIME
    return a[:len(p)-1]


def evaluate_E(N):
    s = [m[0][0] for m in N]
    u = [[m[i][0] for i in range(9)] for m in N]
    samples = [[] for _ in range(6)]
    for t in range(-10, 11):
        B = [[2*t*t*N[0][i][j]+6*t*N[1][i][j]+12*N[2][i][j] for j in range(9)] for i in range(9)]
        v = [4*t*u[0][i]+3*u[1][i] for i in range(9)]
        H = [[12*t*t+2*s[0]]+v]+[[v[i]]+B[i] for i in range(9)]
        border = lambda M, row, col: [r+[col[i]] for i, r in enumerate(M)]+[row+[0]]
        w = [0]+u[0]
        T2 = 0
        # Jacobi derivative by column replacement; no inverse or adjugate routine.
        for j in range(1, 10):
            altered = [row[:] for row in H]
            for i in range(10):
                altered[i][j] = N[0][i-1][j-1] if i else 0
            T2 += moddet(altered)
        values = [moddet(B), moddet(border(B, u[0], v)), moddet(border(B, u[1], v)),
                  -moddet(border(H, w, w)), moddet(H), T2]
        for column, val in zip(samples, values):
            column.append(val % PRIME)
    polynomials = list(map(interpolate, samples))
    p = [s[2] % PRIME, s[1] % PRIME, s[0] % PRIME, 0, 1]
    R = [remainder(f, p) for f in polynomials]
    S = remainder(polynomials[4], pmul(p, p))
    return [x % PRIME for x in [R[0][1],s[0]*R[0][3],R[1][2],R[2][3],R[3][3],
             S[3],s[0]*S[5],s[1]*S[6],s[2]*S[7],R[5][1],s[0]*R[5][3]]]


def fixed_padding():
    points = read(P04 / 'results/b17_04/padding_points.json')
    certificate = read(P04 / 'results/b17_04/restriction.json')
    rows = [list(map(int, row)) for row in certificate['rows']]
    assert len(points) == len(rows) == 12
    reconstructed = []
    for k, point in enumerate(points):
        L = point['L']
        assert len(L) == 10 and all(len(row) == 10 and all(row) for row in L)
        assert determinant(L) == Q(point['det_L']) != 0
        c, linear = 0, [0]*9
        for sigma in permutations(range(3)):
            factors = [L[0]]+[L[1+3*i+sigma[i]] for i in range(3)]
            c += prod(row[0] for row in factors)
            for j in range(9):
                linear[j] += sum(factors[i][j+1]*prod(factors[q][0] for q in range(4) if q != i) for i in range(4))
        assert c == point['c'] != 0 and linear == point['a1'] and c % PRIME
        A = [[row[0]]+[12*c*row[j+1]-3*linear[j]*row[0] for j in range(9)] for row in L]
        assert A == point['depressed_scaled_L'] and point['scale'] == 12*c
        minus, zero, plus = [hessian(A, t) for t in (-1, 0, 1)]
        N = []
        for n in range(3):
            m = []
            for i in range(1, 10):
                row = []
                for j in range(1, 10):
                    numerator = (plus[i][j]+minus[i][j]-2*zero[i][j], plus[i][j]-minus[i][j], zero[i][j])[n]
                    val = Q(numerator, (4,12,12)[n]*c)
                    assert val.denominator == 1
                    row.append(int(val))
                m.append(row)
            N.append(m)
        assert N == point['N']
        for t in (-3, 5):
            direct = hessian(A, t)
            v = [4*t*N[0][i][0]+3*N[1][i][0] for i in range(9)]
            B = [[2*t*t*N[0][i][j]+6*t*N[1][i][j]+12*N[2][i][j] for j in range(9)] for i in range(9)]
            expected = [[12*t*t+2*N[0][0][0]]+v]+[[v[i]]+B[i] for i in range(9)]
            assert direct == [[c*x for x in row] for row in expected]
        row = evaluate_E(N)
        assert row == [x % PRIME for x in rows[k]] == [int(x) % PRIME for x in point['E_values']]
        reconstructed.append(row)
    rid, cid = certificate['minor_rows'], certificate['minor_columns']
    assert rid == list(range(9)) and cid == [0,1,2,4,5,6,7,8,9]
    minor = [[rows[i][j] for j in cid] for i in rid]
    assert minor == [list(map(int, row)) for row in certificate['minor']]
    delta = determinant(minor)
    assert delta == Q(certificate['minor_determinant']) != 0
    residue = moddet([[reconstructed[i][j] for j in cid] for i in rid])
    assert residue == int(delta) % PRIME != 0
    finite_factor = prod(points[i]['c']**27 for i in rid)
    assert delta*finite_factor == Q(certificate['finite_degree27_minor_determinant'])
    _, rank = sparse_reducer([{j: x for j, x in enumerate(row) if x} for row in rows])
    assert rank == 9
    kappa = [12,-10,4,3,0,0,0,0,0,0,0]
    w = [216,-212,64,0,0,-1,1,1,13,4,2]
    for v in (kappa, w):
        assert all(sum(x*y for x, y in zip(row, v)) == 0 for row in rows)
    for v in certificate['sample_kernel_vectors']:
        assert all(sum(x*Q(y) for x, y in zip(row, v)) == 0 for row in rows)
    duplicate = [[reconstructed[i][j] for j in cid] for i in rid]
    duplicate[1] = duplicate[0][:]
    assert moddet(duplicate) == 0
    changed = reconstructed[0][:]
    changed[0] = (changed[0]+1) % PRIME
    assert changed != [x % PRIME for x in rows[0]]
    return {'points_checked': 12, 'exact_coordinate_and_jet_reconstruction': True,
            'modular_E_values_matched': 132, 'prime': PRIME, 'nonzero_minor_residue': residue,
            'exact_integer_minor_matched': True, 'degree27_factor_matched': True,
            'sample_rank': rank, 'global_rank_interval': [9,10],
            'second_global_kernel': 'UNVERIFIED', 'sample_kernel_independent': w[-1] != 0,
            'mutations_rejected': ['duplicate_minor_row', 'changed_E_value']}


def clipping_controls():
    total = 0
    for a in range(9):
        for s in range(13):
            for b in range(s+1):
                B = min(a, s-b)
                assert (B < min(a,s)) == (b >= s-min(a,s)+1)
                for U in range(1, a+1):
                    assert (B < U) == (b >= max(0, s-U+1))
                    for K in range(1, 10):
                        assert (B < U and B+1 <= K) == (b >= max(0,s-min(U,K)+1))
                    total += 1
    assert min(5, 8-1) == min(5, 8) == 5
    assert min(5, 8-4) < 5 and not min(5, 8-4) < 4
    assert min(5, 2) < 4
    assert determinant([[1,1],[0,0]]) == 0  # carrier dimension2 does not mean image rank2
    assert determinant([[1,0],[0,1]]) == 1
    return {'finite_threshold_checks': total, 'edge_cases': ['zero_ambient','U_zero_infeasible',
           'ambient_clipping','improvement_without_gate','s_below_U','source_dimension_not_rank'],
           'new_representation_census': False}


def main():
    assert sys.dont_write_bytecode and 'CI73_DEADLINE' in os.environ
    assert all(os.environ.get(k) == '1' for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS'))
    n = check_inputs()
    match = formal_match()
    print(json.dumps({'formal_match': 'PASS', 'seconds': time.perf_counter()-START}), flush=True)
    padding = fixed_padding()
    thresholds = clipping_controls()
    assert check_inputs() == n
    result = {'status': 'PASS_SCOPED_INDEPENDENT_CONTROL', 'inputs_checked_before_after': n,
              'basis_match': match, 'padding': padding, 'clipping': thresholds, 'statistics': COUNTS,
              'seconds': time.perf_counter()-START, 'producer_imports': False,
              'new_points': 0, 'new_representation_computation': False,
              'limits': ['inherited global polynomial/HW premises', 'no second global kernel proof',
                         'no numerical forbidden-weight rank', 'no finite candidate']}
    (OUT / 'verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
