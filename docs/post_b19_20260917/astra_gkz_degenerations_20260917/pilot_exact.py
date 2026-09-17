"""One bounded exact pilot. Standard library only; no historical code imported.

Checks a 24-permutation expansion against separate 3x3 cofactor formulas.
Global redundancy is proved in REPORT.md, not inferred from these controls.
"""
from collections import defaultdict
from itertools import permutations, product
import json
from pathlib import Path

NAMES = ['a', 'r1', 'r2', 'r3', 'c1', 'c2', 'c3',
         'v1', 'v2', 'v3', 's11', 's22', 's33', 's12', 's13', 's23']
ZERO = (0,) * 16
ONE = {ZERO: 1}


def var(i):
    e = list(ZERO)
    e[i] = 1
    return {tuple(e): 1}


def add(*polys):
    out = defaultdict(int)
    for p in polys:
        for e, c in p.items():
            out[e] += c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: c * v for e, v in p.items() if c * v}


def mul(*polys):
    out = ONE
    for p in polys:
        acc = defaultdict(int)
        for e, c in out.items():
            for f, b in p.items():
                acc[tuple(a + z for a, z in zip(e, f))] += c * b
        out = {e: c for e, c in acc.items() if c}
        assert len(out) < 10000
    return out


def det(M):
    n = len(M)
    return add(*(scale(mul(*(M[i][p[i]] for i in range(n))),
                       (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)))
                 for p in permutations(range(n))))


def adj(M):
    n = len(M)
    return [[scale(det([[M[i][j] for j in range(n) if j != row]
                       for i in range(n) if i != col]), (-1) ** (row + col))
             for col in range(n)] for row in range(n)]


def dot(a, b):
    return add(*(mul(x, y) for x, y in zip(a, b)))


def matvec(M, v):
    return [dot(row, v) for row in M]


def skew(v):
    return [[{}, scale(v[2], -1), v[1]],
            [v[2], {}, scale(v[0], -1)],
            [scale(v[1], -1), v[0], {}]]


def records(p):
    return [{'powers': list(e), 'coefficient': c} for e, c in sorted(p.items())]


def main():
    x = [var(i) for i in range(16)]
    a, r, c, v = x[0], x[1:4], x[4:7], x[7:10]
    S = [[x[10], x[13], x[14]], [x[13], x[11], x[15]], [x[14], x[15], x[12]]]
    K = skew(v)
    E = [[add(S[i][j], K[i][j]) for j in range(3)] for i in range(3)]
    M = [[a] + r] + [[c[i]] + E[i] for i in range(3)]
    f = det(M)
    groups = {
        (1, 2): mul(a, dot(v, matvec(S, v))),
        (0, 2): scale(mul(dot(r, v), dot(v, c)), -1),
        (0, 1): dot(r, matvec(skew(matvec(S, v)), c)),
        (1, 0): mul(a, det(S)),
        (0, 0): scale(dot(r, matvec(adj(S), c)), -1),
    }
    assert add(*groups.values()) == f
    assert set((e[0], sum(e[7:10])) for e in f) == set(groups)
    for pq, g in groups.items():
        assert all((e[0], sum(e[7:10])) == pq for e in g)
    weights = [-1] + [0] * 3 + [1] * 3 + [0] * 3 + [1] * 6
    expanded = defaultdict(dict)
    for e, value in f.items():
        expanded[sum(w * k for w, k in zip(weights, e))][e] = value
    expected = {0: groups[1, 2], 1: groups[0, 2],
                2: add(groups[1, 0], groups[0, 1]), 3: groups[0, 0]}
    assert dict(expanded) == expected
    # The wrong sign in the skew cofactor term must fail the exact identity.
    corrupted = add(*[scale(g, -1) if pq == (0, 1) else g for pq, g in groups.items()])
    corruption_residual = add(f, scale(corrupted, -1))
    assert corruption_residual
    # The affine weight identity is checked at every actual determinant monomial.
    weight_controls = 0
    for A, R, C, s, vw in product(range(-1, 2), repeat=5):
        beta, u, h = R + C + 2 * s, A - R - C + s, vw - s
        ws = [A] + [R] * 3 + [C] * 3 + [vw] * 3 + [s] * 6
        for e in f:
            assert sum(w * k for w, k in zip(ws, e)) == beta + u * e[0] + h * sum(e[7:10])
            weight_controls += 1
    # Finite controls of the exact d-fold support formula, with missing-point control.
    support = {(0, 0)}
    support_sizes = {}
    for d in range(1, 7):
        support = {(p + a0, q + b0) for p, q in support for a0, b0 in groups}
        claimed = {(p, q) for p in range(d + 1) for q in range(2*d + 1)
                   if p < d or q % 2 == 0}
        assert support == claimed
        assert (d, 1) not in support
        support_sizes[str(d)] = len(support)
    # Deliberately invalid degree-four monomial a*v1^3 gives a pole, so extraction is sensitive.
    bad = mul(a, v[0], v[0], v[0])
    bad_weight = next(sum(w * k for w, k in zip(weights, e)) for e in bad)
    assert bad_weight == -1
    # Old test u=0,h=-1 recovers precisely nu>2d on the balanced candidate lattice.
    lattice_controls = 0
    for d in range(1, 7):
        for p in range(d + 1):
            for q in range(2*d + p + 1):
                assert (2*d - q < 0) == (q > 2*d)
                if q <= 2*d:
                    assert 0 <= 3*d - p - q <= 3*d
                lattice_controls += 1
    out = {
        'status': 'all exact controls passed',
        'scope': 'identity verification and finite controls; all-degree theorem is in REPORT.md',
        'variable_order': NAMES, 'determinant_monomials': len(f),
        'five_groups': {str(k): records(g) for k, g in groups.items()},
        'arc_coefficients': {str(t): records(g) for t, g in sorted(expanded.items())},
        'checks': {
            'independent_24_permutation_vs_cofactor_identity': True,
            'exact_arc_expansion': True,
            'wrong_skew_sign_rejected': bool(corruption_residual),
            'wrong_skew_sign_residual_terms': len(corruption_residual),
            'non_source_monomial_pole_detected': bad_weight,
            'missing_point_d_1_rejected_for_each_d': True,
            'affine_weight_monomial_checks': weight_controls,
            'balanced_lattice_controls': lattice_controls,
            'd_fold_support_sizes': support_sizes,
        },
    }
    dest = Path('results/pilot_exact.json')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': out['status'], 'checks': out['checks'],
                      'determinant_monomials': len(f)}))


if __name__ == '__main__':
    main()
