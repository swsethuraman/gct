"""B17-02 sole bounded pilot: exact shared-block boundary and Taylor identities.

New standard-library implementation; does not import prior research code.
Run only with the existing .venv Python -B and inspected b15_bound.py.
"""
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results' / 'b17_02'
NAMES = ['a', 'r1', 'r2', 'r3', 'c1', 'c2', 'c3', 'v1', 'v2', 'v3',
         's11', 's22', 's33', 's12', 's13', 's23']
WEIGHTS = [-1]*4 + [1]*3 + [0]*3 + [1]*6
ONE = {(0, 0, ()): 1}
PAIR_PRODUCTS = 0
PEAK_SUPPORT = 0


def clean(p):
    global PEAK_SUPPORT
    q = {m: z for m, z in p.items() if z}
    PEAK_SUPPORT = max(PEAK_SUPPORT, len(q))
    if len(q) > 10000:
        raise RuntimeError('UNCOMPUTED: support guard exceeded')
    return q


def add(*args):
    ans = defaultdict(int)
    for p in args:
        for m, z in p.items():
            ans[m] += z
    return clean(ans)


def scale(p, z):
    return clean({m: z*x for m, x in p.items()})


def mul(p, q):
    global PAIR_PRODUCTS
    PAIR_PRODUCTS += len(p)*len(q)
    if PAIR_PRODUCTS > 1000000:
        raise RuntimeError('UNCOMPUTED: operation guard exceeded')
    ans = defaultdict(int)
    for (t, u, m), x in p.items():
        for (tt, uu, mm), y in q.items():
            ans[t+tt, u+uu, tuple(sorted(m+mm))] += x*y
    return clean(ans)


def shift(p, t=0, u=0):
    return {(tt+t, uu+u, m): x for (tt, uu, m), x in p.items()}


def prod(*ps):
    ans = ONE
    for p in ps:
        ans = mul(ans, p)
    return ans


def det(M):
    ans = {}
    for p in permutations(range(len(M))):
        parity = sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i+1, len(p)))
        ans = add(ans, scale(prod(*(M[i][p[i]] for i in range(len(p)))),
                             (-1)**parity))
    return ans


def adj(M):
    n = len(M)
    return [[scale(det([[M[i][j] for j in range(n) if j != row]
                        for i in range(n) if i != col]), (-1)**(row+col))
             for col in range(n)] for row in range(n)]


def dot(x, y):
    return add(*(mul(a, b) for a, b in zip(x, y)))


def matvec(M, v):
    return [dot(row, v) for row in M]


def skew(v):
    return [[{}, scale(v[2], -1), v[1]],
            [v[2], {}, scale(v[0], -1)],
            [scale(v[1], -1), v[0], {}]]


def coefficient(p, axis, exponent):
    ans = {}
    for (t, u, m), z in p.items():
        if (t, u)[axis] == exponent:
            ans[(0 if axis == 0 else t, 0 if axis == 1 else u, m)] = z
    return ans


def records(p):
    return [{'t': t, 'u': u, 'variables': [NAMES[i] for i in m], 'coefficient': z}
            for (t, u, m), z in sorted(p.items())]


def main():
    pinned = json.loads((OUT/'input_hashes.json').read_text(encoding='utf-8-sig'))
    checked = []
    for item in pinned['files']:
        got = hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()
        if got != item['sha256']:
            raise RuntimeError('UNCOMPUTED: changed input ' + item['path'])
        checked.append(item['path'])
    x = [{(0, 0, (i,)): 1} for i in range(16)]
    a, r, c, v = x[0], x[1:4], x[4:7], x[7:10]
    S = [[x[10], x[13], x[14]], [x[13], x[11], x[15]],
         [x[14], x[15], x[12]]]
    A = skew(v)
    E = [[add(A[i][j], shift(S[i][j], t=1)) for j in range(3)]
         for i in range(3)]
    M = [[shift(a, t=-1)] + [shift(z, t=-1) for z in r]]
    M += [[shift(c[i], t=1)] + E[i] for i in range(3)]
    direct = det(M)
    q0 = add(prod(a, dot(v, matvec(S, v))), scale(prod(dot(r, v), dot(v, c)), -1))
    q1 = dot(r, matvec(skew(matvec(S, v)), c))
    q2 = add(mul(a, det(S)), scale(dot(r, matvec(adj(S), c)), -1))
    expected = add(q0, shift(q1, t=1), shift(q2, t=2))
    assert direct == expected
    assert all(0 <= t <= 2 and u == 0 and len(m) == 4 for t, u, m in direct)
    assert [len(q) for q in (q0, q1, q2)] == [15, 18, 23]
    assert all(t == sum(WEIGHTS[i] for i in m) for t, u, m in direct)
    assert det(E) == add(shift(dot(v, matvec(S, v)), t=1), shift(det(S), t=3))
    adjE = adj(E)
    mid = skew(matvec(S, v))
    adjS = adj(S)
    for i in range(3):
        for j in range(3):
            assert adjE[i][j] == add(prod(v[i], v[j]),
                scale(shift(mid[i][j], t=1), -1), shift(adjS[i][j], t=2))

    # Direct determinant at the fixed coordinate point J: S=I, other x=0.
    MJ = [[shift(z, u=1) for z in row] for row in M]
    for i in range(1, 4):
        MJ[i][i] = add(MJ[i][i], shift(ONE, t=1))
    direct_J = det(MJ)
    trS = add(*(S[i][i] for i in range(3)))
    e2S = add(*(add(prod(S[i][i], S[j][j]), scale(prod(S[i][j], S[j][i]), -1))
                for i in range(3) for j in range(i+1, 3)))
    trIminusS = [[add(trS if i == j else {}, scale(S[i][j], -1))
                 for j in range(3)] for i in range(3)]
    qj1 = shift(a, t=2)
    qj2 = shift(add(prod(a, trS), scale(dot(r, c), -1)), t=2)
    qj3 = add(prod(a, dot(v, v)), shift(dot(r, matvec(A, c)), t=1),
              shift(add(prod(a, e2S), scale(dot(r, matvec(trIminusS, c)), -1)), t=2))
    qj4 = expected
    assert direct_J == add(*(shift(q, u=i+1) for i, q in enumerate([qj1,qj2,qj3,qj4])))
    at_boundary = coefficient(direct_J, 0, 0)
    assert coefficient(at_boundary, 1, 1) == {}
    assert coefficient(at_boundary, 1, 2) == {}
    assert coefficient(at_boundary, 1, 3) == prod(a, dot(v, v))
    assert coefficient(at_boundary, 1, 4) == q0
    assert sum(WEIGHTS) == 5

    # Mutation checks verify sensitivity; their residuals are exact polynomials.
    wrong_sign = add(q0, scale(shift(q1, t=1), -1), shift(q2, t=2))
    missing_cross = add(expected, scale(prod(a, v[0], v[1], S[0][1]), -2))
    residuals = [add(direct, scale(z, -1)) for z in [wrong_sign, missing_cross]]
    assert all(residuals)
    result = {
        'status': 'PASS', 'scope': 'universal boundary and shared four-order Taylor identities only',
        'python': sys.version, 'variables': NAMES, 'gamma_weights': WEIGHTS,
        'input_hashes_checked': checked, 'arc_supports': [len(q0),len(q1),len(q2)],
        'arc_coefficient_records': [records(q) for q in [q0,q1,q2]],
        'taylor_coefficient_records': [records(q) for q in [qj1,qj2,qj3,qj4]],
        'direct_taylor_support': len(direct_J), 'max_dictionary_support': PEAK_SUPPORT,
        'monomial_pair_products': PAIR_PRODUCTS, 'mutations_rejected': ['wrong Q1 sign','missing S12 cross term'],
        'mutation_residual_supports': [len(z) for z in residuals],
        'representations': {'degree_one_control': '(d,lambda)=(1,(4)); f has gamma weights 0,1,2',
                            'tested_new_cell': None, 'strict_multiplicity_improvement': False},
        'not_computed': ['H-invariant basis','forbidden-weight rank','padding minor','character census'],
    }
    (OUT/'verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','arc_supports','direct_taylor_support',
                                         'max_dictionary_support','monomial_pair_products']}))


if __name__ == '__main__':
    main()
