"""Exact replay of the one preregistered candidate. No search or sampling."""
from fractions import Fraction as R
from itertools import combinations, permutations
from math import factorial
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'results/b27_02/candidate.json').read_text())
MODE = sys.argv[1]
P = list(permutations(range(5)))

def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))

SP = {p: sign(p) for p in P}

def determinant(matrix):
    n = len(matrix)
    ans = R(0)
    for p in permutations(range(n)):
        term = R(sign(p))
        for i in range(n):
            term *= matrix[i][p[i]]
        ans += term
    return ans

def check_tableaux():
    for key in ('T1', 'T2'):
        t = DATA[key]
        columns = t['full_columns'] + [[j + 1] for j, n in enumerate(t['singleton_multiplicity']) for _ in range(n)]
        assert all(len(set(c)) == len(c) for c in columns)
        assert [sum(j in c for c in columns) for j in range(1, 11)] == [4] * 10
        assert [sum(len(c) >= j for c in columns) for j in range(1, 6)] == DATA['shape']
    assert DATA['coefficients'] == [1, -567]

def F_even(diag, pair, scale):
    """Enumerate epsilon indices; the fourth is forced by even quartic support.

    Grouped mode quotients only by the proved S2 x S3 coordinate symmetry.
    Full replay enumerates all 120 first-column permutations instead.
    At most 120^3 triples are checked, with exact integer products.
    """
    if MODE == 'grouped':
        first = []
        for u_slots in combinations(range(5), 2):
            p = [None] * 5
            for value, slot in enumerate(u_slots):
                p[slot] = value
            for value, slot in zip(range(2, 5), (i for i in range(5) if i not in u_slots)):
                p[slot] = value
            first.append(tuple(p))
        factor = 12
    else:
        assert MODE == 'full'
        first, factor = P, 1
    weights = [[diag[i] if i == j else pair[i][j] for j in range(5)] for i in range(5)]
    numerator = 0
    admissible = 0
    for p1 in first:
        s1 = SP[p1]
        for p2 in P:
            s12 = s1 * SP[p2]
            for p3 in P:
                p4 = []
                weight = 1
                for a, b, c in zip(p1, p2, p3):
                    if a == b:
                        d = c
                        weight *= weights[a][c]
                    elif c == a:
                        d = b
                        weight *= pair[a][b]
                    elif c == b:
                        d = a
                        weight *= pair[a][b]
                    else:
                        break
                    if not weight or d in p4:
                        break
                    p4.append(d)
                else:
                    admissible += 1
                    numerator += s12 * SP[p3] * SP[tuple(p4)] * weight
    return R(factor * numerator, scale ** 5), {'first_columns': len(first), 'triples_bound': len(first) * 120 ** 2,
                                               'nonzero_admissible': admissible, 'scaled_integer_sum': numerator,
                                               'orbit_factor': factor, 'tensor_scale': scale}

def even_form(alpha, beta, gamma, scale):
    diag = [int(scale * alpha)] * 2 + [int(scale * gamma)] * 3
    pair = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            value = alpha / 3 if i < 2 and j < 2 else gamma / 3 if i >= 2 and j >= 2 else beta / 6
            assert (scale * value).denominator == 1
            pair[i][j] = int(scale * value)
    value, certificate = F_even(diag, pair, scale)
    C = [[R(0) for _ in range(5)] for _ in range(5)]
    C[0][0], C[1][1] = alpha, alpha / 3
    for i in range(2, 5):
        C[i][i] = beta / 6
    H = 120 * determinant(C)
    f = alpha ** 5 * value - 567 * H ** 2
    return value, H, f, certificate

# Sparse polynomial arithmetic for an independent exact pencil determinant.
ZERO = (0,) * 5
def add(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, R(0)) + c
        if not out[m]:
            del out[m]
    return out

def mul(a, b):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            k = tuple(x + y for x, y in zip(m, n))
            out[k] = out.get(k, R(0)) + c * d
    return {m: c for m, c in out.items() if c}

def scale_poly(a, c):
    return {m: v * c for m, v in a.items() if v * c}

def poly_det(matrix):
    result = {}
    for p in permutations(range(len(matrix))):
        term = {ZERO: R(sign(p))}
        for i, j in enumerate(p):
            term = mul(term, matrix[i][j])
        result = add(result, term)
    return result

def tensor_entry(poly, indices):
    exponents = tuple(indices.count(i) for i in range(5))
    denom = factorial(4)
    for n in exponents:
        denom //= factorial(n)
    return poly.get(exponents, R(0)) / denom

def extra_determinant():
    x = [{tuple(int(i == j) for i in range(5)): R(1)} for j in range(5)]
    matrix = [[x[0], {}, {}, x[2]], [{}, x[0], {}, x[3]], [{}, {}, x[0], x[4]],
              [x[2], x[3], x[4], add(x[0], x[1])]]
    poly = poly_det(matrix)
    expected = mul(mul(x[0], x[0]), add(add(mul(x[0], x[0]), mul(x[0], x[1])),
                                      scale_poly(add(add(mul(x[2], x[2]), mul(x[3], x[3])), mul(x[4], x[4])), -1)))
    assert poly == expected
    # This is a finite support certificate: five tensor labels need >=10 occurrences
    # of coordinate 1; four height-five columns provide exactly four. Hence F(E)=0.
    minimum_x1 = min(m[0] for m in poly)
    assert minimum_x1 * 5 > 4
    C = [[tensor_entry(poly, [0, 0, i, j]) for j in range(5)] for i in range(5)]
    H = 120 * determinant(C)
    return R(0), H, -567 * H ** 2, {'pencil_terms': {' '.join(map(str, m)): str(c) for m, c in sorted(poly.items())},
                                         'C': [[str(c) for c in row] for row in C],
                                         'min_x1_degree': minimum_x1, 'F_zero_required_x1': minimum_x1 * 5,
                                         'F_zero_available_x1': 4, 'x1_matrix': 'I4'}

check_tableaux()
values = {}
certificates = {}
for name, parameters in [('Q_squared', (R(1), R(2), R(1), 3)),
                         ('D4', (R(1), R(1), R(1, 4), 12)),
                         ('p4', (R(1), R(1), R(0), 6))]:
    F, H, f, cert = even_form(*parameters)
    values.update({'F_' + name: str(F), 'H_' + name: str(H), 'f_' + name: str(f)})
    certificates[name] = cert
F, H, f, cert = extra_determinant()
values.update({'F_E': str(F), 'H_E': str(H), 'f_E': str(f)})
certificates['E'] = cert
assert values == DATA['expected'], (values, DATA['expected'])
assert R(values['f_D4']) - R(values['f_p4']) == R(175, 9)
assert R(values['F_Q_squared']) == R(factorial(5) * factorial(7), 2 * 3 ** 5)
assert R(values['F_D4']) * 64 == R(values['F_Q_squared'])
# Rows are evaluations of (a^5 F,H^2), at Q^2 and E, respectively.
span_matrix = [[R(values['F_Q_squared']), R(values['H_Q_squared']) ** 2], [R(0), R(values['H_E']) ** 2]]
assert determinant(span_matrix) != 0
print(json.dumps({'label': 'COMPUTED', 'mode': MODE, 'values': values, 'certificates': certificates,
                  'visibility_difference': '175/9', 'span_evaluation_determinant': str(determinant(span_matrix)),
                  'all_registered_assertions_passed': True}, indent=2, sort_keys=True))
