"""R27-02: exact check that B26-02's padding witness p4 = A(A+B) is also a literal 4x4 linear
determinant in the x1*I4 chart. Exact symbolic algebra only; no search or sampling."""
import json
import sys
import sympy as sp

x = sp.symbols('x1:6')
x1, x2, x3, x4, x5 = x
I = sp.I
A = x1**2 + x2**2
B = x3**2 + x4**2 + x5**2
z, w, u, v, t = x1 + I*x2, x1 - I*x2, x3 + I*x4, x3 - I*x4, x5
M = sp.Matrix([[w, -u, -t], [v, z, 0], [t, 0, z]])
L = sp.diag(w, M)
detM = sp.expand(M.det(method='berkowitz'))
detL = sp.expand(L.det(method='berkowitz'))
x1c = L.applyfunc(lambda e: sp.expand(e).coeff(x1, 1).subs({y: 0 for y in x[1:]}))
res = {
    'label': 'COMPUTED',
    'L': str(L.tolist()),
    'entries_linear_forms': all(e == 0 or sp.Poly(sp.expand(e), *x).total_degree() == 1 for e in L),
    'det_M_equals_zQ': sp.expand(detM - z * (A + B)) == 0,
    'det_L_equals_p4_A(A+B)': sp.expand(detL - A * (A + B)) == 0,
    'x1_coefficient_is_I4': x1c == sp.eye(4),
}
assert all(v for k, v in res.items() if k not in ('label', 'L'))
res['all_assertions_passed'] = True
sys.stdout.write(json.dumps(res, indent=2, sort_keys=True) + '\n')
