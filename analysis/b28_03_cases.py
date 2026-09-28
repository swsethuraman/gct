"""COMPUTED: symbolic, non-determinant tests at d=4 and d=3; no sampling."""
import json
import sympy as sp

rows = []
for d in (4, 3):
    # c_j denotes the ordinary coefficient of x^(d-j)y^j.
    c0, c1, c2, a, b = sp.symbols('c0 c1 c2 a b')
    h = 2*d*c0*c2 - (d-1)*c1**2
    raising = sp.expand(sp.diff(h, c1)*d*c0 + sp.diff(h, c2)*(d-1)*c1)
    substitution = {c0: a**d, c1: d*a**(d-1)*b, c2: sp.binomial(d,2)*a**(d-2)*b**2}
    evaluation = sp.expand(h.subs(substitution, simultaneous=True))
    matrix = sp.Matrix([[(d-1), 2*d]])
    kernel = matrix.nullspace()
    assert raising == evaluation == 0
    assert len(kernel) == 1 and matrix*sp.Matrix([2*d, -(d-1)]) == sp.zeros(1,1)
    assert h.subs({c0: 1, c1: 0, c2: 1}) == 2*d
    rows.append({'d': d, 'N': 3, 'r': 2, 'delta': 2, 'lambda': [2*d-2, 2], 'f': 'x1^d', 'ordinary_coefficient_basis': ['c0*c2', 'c1^2'], 'highest_weight_vector_coordinates': [2*d, -(d-1)], 'raising_matrix': [[d-1, 2*d]], 'raising_kernel_dimension': len(kernel), 'raising_residual': str(raising), 'symbolic_substitution_residual': str(evaluation), 'nonzero_polynomial_control': 2*d, 'tail_raising_reason': 'All coefficients have zero exponents in coordinates after r; the raising generators with i>=r kill them.', 'claim_scope': 'Finite symbolic identity and rational kernel; the ideal and multiplicity interpretation is HAND in the report.'})
print(json.dumps({'label': 'COMPUTED', 'cases': rows, 'failures': 0}, indent=2, sort_keys=True))
