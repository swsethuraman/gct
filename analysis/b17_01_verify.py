"""One bounded replay: per3 five-variable density and a smooth actual cubic.

Only standard-library arithmetic. Run with the existing .venv/python.exe -B
through analysis/b15_bound.py --seconds 60 --memory-mb 512. No child processes.
The seed and entry ordering reproduce wk6_s26_density.jacobian_rank trial zero.
No legacy raising-operator code is imported or used.
"""
import hashlib
import itertools as it
import json
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results' / 'b17_01'
P = 65521


def exponents(degree):
    ans = []
    for choices in it.combinations_with_replacement(range(5), degree):
        ans.append(tuple(choices.count(i) for i in range(5)))
    return sorted(ans, reverse=True)


def permanent_coefficients(matrices):
    """Full six-permutation expansion in raw monomial coefficients."""
    out = dict.fromkeys(exponents(3), 0)
    for perm in it.permutations(range(3)):
        for choices in it.product(range(5), repeat=3):
            coefficient = 1
            for row in range(3):
                coefficient *= matrices[choices[row]][row][perm[row]]
            alpha = tuple(choices.count(i) for i in range(5))
            out[alpha] += coefficient
    return out


def cofactor_jacobian(matrices):
    """Rows (k,i,j); columns cubic exponents in descending lexicographic order."""
    exps = exponents(3)
    index = {a: i for i, a in enumerate(exps)}
    rows = []
    for k, i, j in it.product(range(5), range(3), range(3)):
        rr = [a for a in range(3) if a != i]
        cc = [a for a in range(3) if a != j]
        row = [0] * len(exps)
        for a, b in it.product(range(5), repeat=2):
            alpha = tuple(int(v == k) + int(v == a) + int(v == b)
                          for v in range(5))
            row[index[alpha]] += (
                matrices[a][rr[0]][cc[0]] * matrices[b][rr[1]][cc[1]]
                + matrices[a][rr[0]][cc[1]] * matrices[b][rr[1]][cc[0]])
        rows.append(row)
    return rows


def select_independent_rows(rows):
    """Greedy modular row basis; returns original row indices, not row mixtures."""
    basis = {}
    selected = []
    for number, raw in enumerate(rows):
        row = [x % P for x in raw]
        for col in sorted(basis):
            value = row[col]
            if value:
                row = [(x - value * y) % P for x, y in zip(row, basis[col])]
        pivot = next((i for i, x in enumerate(row) if x), None)
        if pivot is None:
            continue
        inverse = pow(row[pivot], -1, P)
        basis[pivot] = [(x * inverse) % P for x in row]
        selected.append(number)
        if len(selected) == len(row):
            break
    return selected


def determinant_mod(rows):
    a = [[v % P for v in row] for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    ans = 1
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            ans = -ans
        value = a[col][col]
        ans = ans * value % P
        inverse = pow(value, -1, P)
        for i in range(col + 1, n):
            factor = a[i][col] * inverse % P
            if factor:
                a[i][col + 1:] = [(x - factor * y) % P
                                  for x, y in zip(a[i][col + 1:], a[col][col + 1:])]
                a[i][col] = 0
    return ans % P


def determinant_integer(rows):
    """Fraction-free Bareiss; every division checked exact."""
    a = [list(row) for row in rows]
    n, previous, sign = len(a), 1, 1
    for col in range(n - 1):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign = -sign
        value = a[col][col]
        for i in range(col + 1, n):
            for j in range(col + 1, n):
                numerator = value * a[i][j] - a[i][col] * a[col][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][j] = quotient
            a[i][col] = 0
        previous = value
    return sign * a[-1][-1]


def main():
    start = time.perf_counter()
    inputs = json.loads((OUT / 'input_hashes.json').read_text(encoding='utf-8-sig'))
    for item in inputs['files']:
        assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest() == item['sha256']
    assert all(P % divisor for divisor in range(2, 256))  # sqrt(P) < 256
    rng = random.Random(1)
    matrices = [[[rng.randint(-7, 7) for _ in range(3)] for _ in range(3)]
                for _ in range(5)]
    exps = exponents(3)
    cubic = permanent_coefficients(matrices)
    jacobian = cofactor_jacobian(matrices)
    # Independently differentiate the FULL permanent expansion. Each source entry
    # occurs with degree at most one, so a unit finite difference is exact.
    for row, (k, i, j) in zip(jacobian, it.product(range(5), range(3), range(3))):
        matrices[k][i][j] += 1
        plus = permanent_coefficients(matrices)
        matrices[k][i][j] -= 1
        assert row == [plus[alpha] - cubic[alpha] for alpha in exps]
    chosen = select_independent_rows(jacobian)
    assert len(chosen) == 35
    minor = [jacobian[i] for i in chosen]
    exact = determinant_integer(minor)
    modular = determinant_mod(minor)
    assert exact and modular and exact % P == modular
    density_seconds = time.perf_counter() - start

    # Smoothness: S_6 is spanned by x^beta * partial_i(C), |beta|=4.
    # A nonzero 210-square integer minor mod P implies this over Q and C.
    quadratic = exponents(2)
    quartic = exponents(4)
    sextic = exponents(6)
    sextic_index = {alpha: i for i, alpha in enumerate(sextic)}
    partials = []
    for i in range(5):
        row = {}
        for alpha in exps:
            if alpha[i]:
                beta = tuple(alpha[j] - int(i == j) for j in range(5))
                row[beta] = alpha[i] * cubic[alpha]
        partials.append(row)
    macaulay, labels = [], []
    for i, beta in it.product(range(5), quartic):
        row = [0] * len(sextic)
        for gamma in quadratic:
            alpha = tuple(a + b for a, b in zip(beta, gamma))
            row[sextic_index[alpha]] = partials[i].get(gamma, 0)
        macaulay.append(row)
        labels.append([i, list(beta)])
    smooth_rows = select_independent_rows(macaulay)
    assert len(smooth_rows) == 210
    smooth_det = determinant_mod([macaulay[i] for i in smooth_rows])
    assert smooth_det
    frame = [[matrices[k][i][j] for k in range(5)]
             for i, j in it.product(range(3), repeat=2)]
    frame_rows = select_independent_rows(frame)
    assert len(frame_rows) == 5
    frame_det = determinant_integer([frame[i] for i in frame_rows])
    assert frame_det

    certificate = {
        'status': 'PASS', 'field': 'Q, hence C', 'prime': P,
        'seed': 1, 'spread': 7, 'trial': 0, 'matrices_A0_to_A4': matrices,
        'coefficient_convention': 'raw monomial coefficients; descending lex order',
        'cubic_exponents': exps, 'cubic_coefficients': [cubic[a] for a in exps],
        'padding_linear_form': [1, 0, 0, 0, 0],
        'density': {'shape': [45, 35], 'rank': 35, 'selected_rows': chosen,
                    'minor_integer': str(exact), 'minor_mod_prime': modular,
                    'all_1575_entries_match_independent_full_expansion': True},
        'smoothness': {'degree': 6, 'shape': [350, 210], 'rank': 210,
                       'selected_rows': smooth_rows,
                       'selected_row_labels': [labels[i] for i in smooth_rows],
                       'column_exponents': sextic, 'minor_mod_prime': smooth_det,
                       'interpretation': 'All degree-six monomials lie in the gradient ideal over Q'},
        'source_frame': {'rank': 5, 'selected_rows': frame_rows,
                         'minor_integer': str(frame_det)},
        'scope': 'Density and explicit smooth actual per3 restriction; no representation multiplicity computation',
    }
    destination = OUT / 'certificate.json'
    if destination.exists():
        assert json.loads(destination.read_text()) == json.loads(json.dumps(certificate))
    else:
        destination.write_text(json.dumps(certificate, indent=2) + '\n')
    receipt = {'status': 'PASS', 'input_hashes_checked': len(inputs['files']),
               'density_seconds': density_seconds, 'total_seconds': time.perf_counter() - start,
               'certificate_sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
               'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT / 'verification_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'receipt': receipt, 'density': certificate['density'],
                      'smooth_minor_mod_prime': smooth_det, 'frame_minor': frame_det}))


if __name__ == '__main__':
    main()
