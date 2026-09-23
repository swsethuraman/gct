"""R27-02 independent exact check of the B27-02 candidate (reviewer code; shares nothing with
analysis/b27_02_verify.py).

Each quartic is built from its literal matrix: Q^2 and D4 as det of the skew pencils, p4 as
z*per_3(Y) with the ten linear forms of B26-02 item 3, and E as det L_E. Tensor entries come from
the expanded coefficients. F is evaluated for an arbitrary quartic by the label-permutation
symmetry (fix column 1 to the identity, times 5!), with the column-4 sum done as a 5x5
determinant. It therefore assumes no even support and no linear-factor argument. H is a direct
double-epsilon sum, not the 5! det C shortcut. Exact arithmetic only; no search or sampling.
"""
from fractions import Fraction as R
from itertools import permutations
from math import factorial
import json
import sys
import time
import sympy as sp

t0 = time.perf_counter()
x = sp.symbols('x1:6')
x1, x2, x3, x4, x5 = x
I = sp.I
A = x1**2 + x2**2
B = x3**2 + x4**2 + x5**2
z, w, u, v, t = x1 + I*x2, x1 - I*x2, x3 + I*x4, x3 - I*x4, x5
P5 = list(permutations(range(5)))

def sgn(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s

SG = {p: sgn(p) for p in P5}

def skew(k12, k13, k14, k23, k24, k34):
    return sp.Matrix([[0, k12, k13, k14], [-k12, 0, k23, k24], [-k13, -k23, 0, k34], [-k14, -k24, -k34, 0]])

def x1_coeff(M):
    return M.applyfunc(lambda e: sp.expand(e).coeff(x1, 1).subs({y: 0 for y in x[1:]}))

def per3(Y):
    return sp.expand(sum(Y[0, p[0]] * Y[1, p[1]] * Y[2, p[2]] for p in permutations(range(3))))

def tensor(poly):
    """q_ijkl with q = sum q_ijkl x_i x_j x_k x_l (no extra factorials)."""
    P = sp.Poly(sp.expand(poly), *x)
    assert P.is_homogeneous and P.total_degree() == 4
    coeffs = {}
    for mon, c in P.terms():
        c = sp.nsimplify(c)
        assert c.is_rational, (mon, c)
        coeffs[mon] = R(int(c.p), int(c.q))
    def entry(*ix):
        mon = tuple(ix.count(i) for i in range(5))
        mult = factorial(4)
        for n in mon:
            mult //= factorial(n)
        return coeffs.get(mon, R(0)) / mult
    return {ix: entry(*ix) for ix in [(i, j, k, l) for i in range(5) for j in range(5) for k in range(5) for l in range(5)]}

def det(M):
    M = [row[:] for row in M]
    n, d = len(M), R(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return R(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            if M[r][c]:
                f = M[r][c] / M[c][c]
                for k in range(c, n):
                    M[r][k] -= f * M[c][k]
    return d

def F_general(q):
    total = R(0)
    for c2 in P5:
        for c3 in P5:
            M = [[q[(l, c2[l], c3[l], d)] for d in range(5)] for l in range(5)]
            if any(all(e == 0 for e in row) for row in M):
                continue
            total += SG[c2] * SG[c3] * det(M)
    return factorial(5) * total

def H_direct(q):
    return sum((SG[c1] * SG[c2] * prod_(q[(0, 0, c1[l], c2[l])] for l in range(5)) for c1 in P5 for c2 in P5), R(0))

def prod_(it):
    r = R(1)
    for e in it:
        r *= e
    return r

out = {'label': 'COMPUTED', 'checks': {}, 'values': {}}
chk = out['checks']

# Tableaux: content, shape, distinct labels, same-label-set pairing in the same order (eps_T=+1).
T1 = [list(range(1, 6))] * 4 + [[j] for j in range(6, 11) for _ in range(4)]
T2 = [list(range(1, 6))] * 2 + [list(range(6, 11))] * 2 + [[j] for j in range(1, 11) for _ in range(2)]
for name, T in (('T1', T1), ('T2', T2)):
    assert [sum(j in c for c in T) for j in range(1, 11)] == [4] * 10
    assert [sum(len(c) >= r for c in T) for r in range(1, 6)] == [24, 4, 4, 4, 4]
    assert all(len(set(c)) == len(c) for c in T)
    counts = {}
    for c in T:
        counts[tuple(c)] = counts.get(tuple(c), 0) + 1
    assert all(n % 2 == 0 for n in counts.values())  # pairable into identical, same-order columns
chk['tableaux_content_shape_pairing'] = True

# Literal determinant points and the literal padding point.
KQ = skew(z, u, t, t, -v, w)
KD = skew(z, u/2, t/2, t, -v, w)
LE = sp.Matrix([[x1, 0, 0, x3], [0, x1, 0, x4], [0, 0, x1, x5], [x3, x4, x5, x1 + x2]])
Jb = sp.Matrix([[0, 1], [-1, 0]])
DJJ = sp.diag(Jb, Jb)
Q2 = sp.expand(KQ.det(method='berkowitz'))
D4 = sp.expand(KD.det(method='berkowitz'))
E = sp.expand(LE.det(method='berkowitz'))
assert sp.expand(Q2 - (A + B)**2) == 0
assert sp.expand(D4 - (A + B/2)**2) == 0
assert sp.expand(E - x1**2 * (x1**2 + x1*x2 - B)) == 0
assert x1_coeff(KQ) == DJJ and x1_coeff(KD) == DJJ and DJJ.det() == 1
assert x1_coeff(LE) == sp.eye(4)
chk['Q2_D4_E_literal_4x4_pencils_in_x1_chart'] = True

Jm = sp.ones(3, 3)
r_ = sp.Matrix([z, u, t])
s_ = sp.Matrix([w, v, t])
assert (Jm - sp.eye(3)) * (-sp.eye(3) + Jm / 2) == sp.eye(3)
b_ = (-sp.eye(3) + Jm / 2) * s_
Y = sp.Matrix([list(r_), list(b_), [w, w, w]])
assert all(sp.Poly(sp.expand(e), *x).total_degree() == 1 for e in Y)
assert Y != Y.T
pY = per3(Y)
assert sp.expand(pY - w * (A + B)) == 0
p4 = sp.expand(z * pY)
assert sp.expand(p4 - A * (A + B)) == 0
chk['p4_equals_z_per3_Y_literal_linear_forms_Y_nonsymmetric'] = True

pts = {'Q_squared': Q2, 'D4': D4, 'p4': p4, 'E': E}
for name, poly in pts.items():
    q = tensor(poly)
    a = q[(0, 0, 0, 0)]
    F = F_general(q)
    H = H_direct(q)
    C = [[q[(0, 0, i, j)] for j in range(5)] for i in range(5)]
    assert H == 120 * det(C)
    f = a**5 * F - 567 * H**2
    out['values'][name] = {'a': str(a), 'F': str(F), 'H': str(H), 'f': str(f)}

# Visibility: t -> f(p4 + t B^2) at t=0 and t=1/4 (p4 + B^2/4 = D4 as polynomials).
assert sp.expand(p4 + B**2 / 4 - D4) == 0
V = out['values']
expected = {'Q_squared': ('1', '11200/9', '40/27', '0'), 'D4': ('1', '175/9', '5/27', '0'),
            'p4': ('1', '0', '5/27', '-175/9'), 'E': ('1', '0', '5/144', '-175/256')}
for name, (a, F, H, f) in expected.items():
    assert V[name] == {'a': a, 'F': F, 'H': H, 'f': f}, (name, V[name])
span = det([[R(V['Q_squared']['F']), R(V['Q_squared']['H'])**2], [R(V['E']['F']), R(V['E']['H'])**2]])
assert span == R(4375, 2916)
out['span_det_(a^5F,H^2)_at_(Q2,E)'] = str(span)
out['coefficient_567_equals_F_over_H2_at_Q2'] = str(R(V['Q_squared']['F']) / R(V['Q_squared']['H'])**2)
out['all_assertions_passed'] = True
sys.stderr.write('wall %.3f s\n' % (time.perf_counter() - t0))
sys.stdout.write(json.dumps(out, indent=2, sort_keys=True) + '\n')
