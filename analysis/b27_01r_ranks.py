"""R27-01 independent check of B27-01's two witnesses, written from the report text
without reusing the producer's code.  SymPy builds the cubics; the Macaulay matrices are
reduced by full Gaussian elimination (no fixed row set) modulo two primes different from
65521.  rank mod p is a lower bound for rank over Q, so full rank mod p certifies full
rank over Q.  No random choice anywhere."""
import itertools as it
import json
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b27_01r_cap import blob, run  # noqa: E402

X = sp.symbols('x0:5')
PRIMES = [1000003, 2147483647]

# T* exactly as displayed in docs/b27_01_report.md section 1b (rows l, A11..A33).
TSTAR = [[1, 0, 0, 0, 0],
         [-5, 5, -7, 4, -2], [2, 0, 7, 0, -7], [6, 0, 6, -3, -7],
         [5, 3, -1, 4, -7], [5, -1, -1, 5, 3], [-6, 5, 2, -4, 1],
         [-3, -4, 5, 2, -7], [-6, -6, 5, -6, 7], [0, 0, -7, 7, -1]]


def per3(M):
    return sp.expand(sum(M[0][s[0]] * M[1][s[1]] * M[2][s[2]] for s in it.permutations(range(3))))


def lin(row):
    return sum(c * x for c, x in zip(row, X))


def mons(d):
    return sorted((tuple(c.count(i) for i in range(5))
                   for c in it.combinations_with_replacement(range(5), d)), reverse=True)


def coeffs(f, d):
    P = sp.Poly(f, *X)
    return [int(P.coeff_monomial(sp.Mul(*[x**e for x, e in zip(X, m)]))) for m in mons(d)]


def macaulay(f, deg_f, k, drop=()):
    """rows x^beta * d_i f, |beta| = k - deg_f + 1; columns degree-k monomials."""
    cols = [m for m in mons(k) if m not in drop]
    idx = {m: j for j, m in enumerate(cols)}
    rows, dropped_nonzero = [], 0
    for i in range(5):
        g = sp.Poly(sp.diff(f, X[i]), *X)
        for beta in mons(k - deg_f + 1):
            r = [0] * len(cols)
            for mono, c in g.terms():
                m = tuple(a + b for a, b in zip(mono, beta))
                if m in idx:
                    r[idx[m]] += int(c)
                elif c:
                    dropped_nonzero += 1
            rows.append(r)
    return rows, len(cols), dropped_nonzero


def rank_mod(rows, p):
    a = [[v % p for v in r] for r in rows]
    rank, ncol = 0, len(a[0])
    for j in range(ncol):
        piv = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if piv is None:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        inv = pow(a[rank][j], -1, p)
        a[rank] = [v * inv % p for v in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][j]:
                f = a[i][j]
                a[i] = [(u - f * v) % p for u, v in zip(a[i], a[rank])]
        rank += 1
    return rank


def body():
    out = {'status': 'PASS', 'label': 'COMPUTED', 'primes': PRIMES}
    tj = json.loads(blob('results/b27_01/T_STAR.json'))
    assert tj['T'] == TSTAR, 'report table differs from T_STAR.json'
    out['tstar_table_equals_T_STAR_json'] = True
    A = [[lin(TSTAR[1 + 3 * i + j]) for j in range(3)] for i in range(3)]
    Cs = per3(A)
    assert coeffs(Cs, 3) == tj['cubic_coefficients']
    out['tstar_cubic_coefficients_match'] = True
    out['tstar_rank_T_over_Q'] = sp.Matrix(TSTAR).rank()
    rows, n, _ = macaulay(Cs, 3, 6)
    out['tstar_M6_shape'] = [len(rows), n]
    out['tstar_M6_rank_mod_p'] = [rank_mod(rows, p) for p in PRIMES]
    rows, n, _ = macaulay(Cs, 3, 4)
    out['tstar_cubic_M4_rank_mod_p'] = [rank_mod(rows, p) for p in PRIMES]
    rows, n, _ = macaulay(sp.expand(lin(TSTAR[0]) * Cs), 4, 7)
    out['tstar_quartic_M7_shape'] = [len(rows), n]
    out['tstar_quartic_M7_rank_mod_p'] = [rank_mod(rows, p) for p in PRIMES]

    # A^dagger rebuilt from MAP_AND_BOUNDARY_PROOF.md section 3 formulas.
    q = sp.Matrix([[1, 2, 3], [4, 5, 6], [91, 104, -333]])
    E = sp.symbols('e0:9')
    Pg = per3([[E[3 * i + j] for j in range(3)] for i in range(3)])
    qs = {E[k]: q[k // 3, k % 3] for k in range(9)}
    out['per_q'] = int(Pg.subs(qs))
    g = [int(sp.diff(Pg, E[k]).subs(qs)) for k in range(9)]
    assert g == [-1041, -786, 871, -354, -60, 286, 27, 18, 13]
    V = []
    for r in range(1, 5):
        v = [13 * r**i for i in range(8)]
        v.append(-sum(g[i] * r**i for i in range(8)))
        assert sum(a * b for a, b in zip(g, v)) == 0
        V.append(v)
    ent = [q[k // 3, k % 3] * X[0] + sum(V[r][k] * X[r + 1] for r in range(4)) for k in range(9)]
    Ad = [[ent[3 * i + j] for j in range(3)] for i in range(3)]
    Cd = per3(Ad)
    tc = json.loads(blob('results/b27_01/TANGENT_CERTIFICATE.json'))
    assert coeffs(Cd, 3) == [int(c) for c in tc['cubic_coefficients']]
    out['dagger_cubic_coefficients_match'] = True
    rows, n, _ = macaulay(Cd, 3, 6)
    x06 = [r[0] for r in rows]  # column 0 is x0^6 in descending lex
    out['dagger_x0^6_column_all_zero'] = all(v == 0 for v in x06)
    out['dagger_M6_rank_mod_p'] = [rank_mod(rows, p) for p in PRIMES]
    grad_e0 = [int(sp.diff(Cd, X[i]).subs({X[0]: 1, X[1]: 0, X[2]: 0, X[3]: 0, X[4]: 0}))
               for i in range(5)]
    out['dagger_gradient_at_e0'] = grad_e0
    aff = Cd.subs(X[0], 1)
    H = sp.hessian(aff, X[1:]).subs({x: 0 for x in X[1:]})
    out['dagger_hessian_det'] = str(H.det())
    # Parameter differential: d per / d(A_ij coefficient of x_k) = x_k * cofactor_ij.
    cols = mons(3)
    drows = []
    for i, j in it.product(range(3), repeat=2):
        cof = per3([[Ad[a][b] if (a != i and b != j) else (1 if (a == i and b == j) else 0)
                     for b in range(3)] for a in range(3)])
        for k in range(5):
            drows.append(coeffs(sp.expand(X[k] * cof), 3))
    out['dagger_param_differential_shape'] = [len(drows), len(cols)]
    out['dagger_param_differential_rank_mod_p'] = [rank_mod(drows, p) for p in PRIMES]

    # Controls for the rank ceilings used against D35 and Sigma_Pi.
    M = [[lin([1, 2, 0, -1, 3]), lin([0, 1, 1, 2, -2]), lin([3, 0, -1, 1, 1])],
         [lin([2, -1, 1, 0, 1]), lin([1, 1, 2, -3, 0]), lin([0, 3, 1, 1, -1])],
         [lin([1, 0, 3, 2, 1]), lin([-2, 1, 0, 1, 2]), lin([1, 1, -1, 0, 3])]]
    D = sp.expand(sp.Matrix(M).det())
    rows, _, _ = macaulay(D, 3, 6)
    out['control_det3_M6_rank_mod_p'] = [rank_mod(rows, p) for p in PRIMES]
    a, b = X[3], X[4]
    Q1 = X[0]**2 - X[2]**2 + a * X[1] + b * X[0] + a * b
    Q2 = X[1]**2 - X[2]**2 + a * X[2] - b * X[1] + b**2
    Pl = sp.expand(a * Q1 + b * Q2)
    rows, _, _ = macaulay(Pl, 3, 6)
    out['control_plane_cubic_M6_rank_mod_p'] = [rank_mod(rows, p) for p in PRIMES]
    return out


if __name__ == '__main__':
    run(4, __file__, body, ['analysis/b27_01r_ranks.py', 'analysis/b27_01r_cap.py',
                            'TIP:results/b27_01/T_STAR.json', 'TIP:results/b27_01/TANGENT_CERTIFICATE.json'],
        ['RANKS.json'])
