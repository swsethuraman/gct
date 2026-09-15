"""B16-03: division-free export of c^23 S7. Ordinary coefficient convention.

New independent receiver by gpt-6-astra. Mathematical recipe: the Batch15
Hessian11_1631 report; earlier bracket conventions retain Claude Opus 5
attribution. No B15 evaluator or saved Hessian coefficient is imported.
Run computations through the inspected analysis/b15_bound.py.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations
from math import comb
from flint import fmpz_mat, fmpq_mat

N = 10
Z = (0,) * N


def determinant(rows):
    if all(Q(x).denominator == 1 for row in rows for x in row):
        return int(fmpz_mat([[int(x) for x in row] for row in rows]).det())
    return Q(str(fmpq_mat([[str(x) for x in row] for row in rows]).det()))


def multiply(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def evaluate(a, t):
    v = 0
    for x in reversed(a):
        v = v * t + x
    return v


def remainder(a, divisor):
    """Independent ordinary long division over Q, including nonmonic input."""
    a = list(map(Q, a))
    for k in range(len(a) - 1, len(divisor) - 2, -1):
        v = a[k] / divisor[-1]
        for j, x in enumerate(divisor):
            a[k - len(divisor) + 1 + j] -= v * x
    return a[:len(divisor) - 1]


def interpolate(values, start=0):
    """Complete degree <= len(values)-1 Newton interpolation, exact Q."""
    ans = [Q(0)] * len(values)
    differences = list(map(Q, values))
    base = [Q(1)]
    for k in range(len(values)):
        for i, b in enumerate(base):
            ans[i] += differences[0] * b
        differences = [y - x for x, y in zip(differences, differences[1:])]
        base = [x / (k + 1) for x in multiply(base, [-start-k, 1])]
    return ans


def quartic_from_products(terms):
    """Fully expand the small quartic, never its degree-23 equation."""
    ans = defaultdict(Q)
    for sign, factors in terms:
        p = {Z: Q(sign)}
        for factor in factors:
            nxt = defaultdict(Q)
            for exps, coef in p.items():
                for j, x in enumerate(factor):
                    if x:
                        key = list(exps)
                        key[j] += 1
                        nxt[tuple(key)] += coef * x
            p = {k: v for k, v in nxt.items() if v}
        for key, value in p.items():
            ans[key] += value
    return {k: v for k, v in ans.items() if v}


def padding_terms(L):
    # Independent source order: z, X11,X12,X13,X21,...,X33.
    return [(1, [L[0]] + [L[1 + 3*i + p[i]] for i in range(3)])
            for p in permutations(range(3))]


def determinant_terms(matrices):
    forms = [[[matrices[k][i][j] for k in range(N)] for j in range(4)]
             for i in range(4)]
    return [((-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)),
             [forms[i][p[i]] for i in range(4)]) for p in permutations(range(4))]


def hessian_coefficients(G):
    """Differentiate expanded ordinary coefficients and restrict to (t,1,0^8)."""
    H = [[[Q(0) for j in range(N)] for i in range(N)] for k in range(3)]
    for exps, coefficient in G.items():
        for i in range(N):
            if not exps[i]:
                continue
            for j in range(N):
                factor = exps[i] * (exps[j] - (i == j))
                if not factor:
                    continue
                key = list(exps)
                key[i] -= 1
                key[j] -= 1
                if any(key[2:]):
                    continue
                H[key[0]][i][j] += coefficient * factor
    return H


def hessian_at(H, t):
    return [[sum(H[k][i][j] * t**k for k in range(3)) for j in range(N)]
            for i in range(N)]


def line_coefficients(G):
    return [G.get((k, 4-k) + (0,)*8, Q(0)) for k in range(5)]


def top_recurrence(a):
    """a=(c,a1,a2,a3,a4). B_i=c^i[t^(8-i)](G/c)^2."""
    c = a[0]
    B = [0, 2*a[1]]
    for i in range(2, 9):
        B.append(c**(i-2) * sum(a[u]*a[i-u] for u in range(5) if 0 <= i-u <= 4))
    T = [0]*7 + [1]
    for k in range(8, 21):
        T.append(-sum(B[i]*T[k-i] for i in range(1, 9) if k-i >= 7))
    return B, T


def exported_value(g, D):
    """Polynomial circuit valid also at c=0; no division by c is performed."""
    a = list(reversed(g))
    B, T = top_recurrence(a)
    return sum(D[k] * a[0]**(20-k) * T[k] for k in range(7, 21)), B, T


def equation(G, start=0):
    H = hessian_coefficients(G)
    values = [determinant(hessian_at(H, t)) for t in range(start, start+21)]
    D = interpolate(values, start)
    assert all(evaluate(D, t) == value for t, value in zip(range(start, start+21), values))
    g = line_coefficients(G)
    P, B, T = exported_value(g, D)
    answer = dict(g=g, H=H, D=D, P=P, B=B, T=T, nodes=list(range(start, start+21)), values=values)
    if g[4]:
        rem = remainder(D, multiply(g, g))
        assert P == g[4]**13 * rem[7]
        answer['remainder'] = rem
    return answer


def shear(G, i, j, u):
    """G(x) -> G(x_0,...,x_i+u*x_j,...)."""
    ans = defaultdict(Q)
    for key, coefficient in G.items():
        for k in range(key[i]+1):
            new = list(key)
            new[i] -= k
            new[j] += k
            ans[tuple(new)] += coefficient * comb(key[i], k) * u**k
    return {k: v for k, v in ans.items() if v}


def depress(G):
    c = line_coefficients(G)[4]
    assert c
    F = {k: v/c for k, v in G.items()}
    a1 = []
    for j in range(1, N):
        key = [0]*N
        key[0], key[j] = 3, 1
        a1.append(G.get(tuple(key), Q(0)))
    for j, v in enumerate(a1, 1):
        F = shear(F, 0, j, -v/(4*c))
    assert all(not v for key, v in F.items() if key[0] == 3)
    return F, a1


def natural_padding_hessian(y):
    """Second route: differentiate in the ten independent source variables."""
    z, X = y[0], y[1:]
    C, grad = 0, [0]*9
    HC = [[0]*9 for _ in range(9)]
    for p in permutations(range(3)):
        ids = [3*i+p[i] for i in range(3)]
        C += X[ids[0]]*X[ids[1]]*X[ids[2]]
        for i in range(3):
            grad[ids[i]] += X[ids[(i+1)%3]]*X[ids[(i+2)%3]]
            for j in range(3):
                if i != j:
                    HC[ids[i]][ids[j]] += X[ids[3-i-j]]
    H = [[0]+grad] + [[grad[i]]+[z*HC[i][j] for j in range(9)] for i in range(9)]
    return H, C, HC


def pullback(H, L):
    HL = [[sum(H[i][k]*L[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    return [[sum(L[k][i]*HL[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def encode(obj):
    if isinstance(obj, Q):
        return str(obj)
    if isinstance(obj, dict):
        return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [encode(v) for v in obj]
    return obj


def encode_quartic(G):
    return [[list(k), str(v)] for k, v in sorted(G.items())]


def symbolic_recurrence():
    """Small universal arithmetic certificate in the five binary coefficients."""
    zero = (0,)*5
    def pmul(a, b):
        out = defaultdict(int)
        for e, x in a.items():
            for f, y in b.items():
                out[tuple(v+w for v, w in zip(e, f))] += x*y
        return {k: v for k, v in out.items() if v}
    B = [{}, {(0, 1, 0, 0, 0): 2}]
    for i in range(2, 9):
        out = defaultdict(int)
        for u in range(5):
            v = i-u
            if 0 <= v <= 4:
                key = [i-2, 0, 0, 0, 0]
                key[u] += 1
                key[v] += 1
                out[tuple(key)] += 1
        B.append(dict(out))
    T = [{} for _ in range(7)] + [{zero: 1}]
    for k in range(8, 21):
        out = defaultdict(int)
        for i in range(1, 9):
            if k-i >= 7:
                for key, x in pmul(B[i], T[k-i]).items():
                    out[key] -= x
        T.append({e: x for e, x in out.items() if x})
    for k in range(7, 21):
        for e in T[k]:
            assert sum(e) == k-7
            assert sum(i*e[i] for i in range(5)) == k-7
            # Complete coefficient degree and first two variable weights.
            assert 10 + 20-k + sum(e) == 23
            assert k+2 + 4*(20-k) + sum((4-i)*e[i] for i in range(5)) == 61
            assert 22-k + sum(i*e[i] for i in range(5)) == 15
    return B, T
