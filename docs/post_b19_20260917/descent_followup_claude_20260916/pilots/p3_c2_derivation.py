"""P3: independent symbolic check of the chat-only five-row transverse condition.
Conventions: ordinary coefficients c_alpha=[x^alpha]F; H5 uses T_alpha = alpha! c_alpha
(B15-10 integral convention, as sixrow_witness.H6). Also the e95-attachment convention
T'_{ijkl} with q = sum T' x_i x_j x_k x_l, i.e. T' = T/24."""
import itertools as it, json, math, time
from fractions import Fraction
from collections import defaultdict
import sympy as sp
t0 = time.perf_counter()
x = sp.symbols('x1:6'); t = sp.Symbol('t')
K5 = sp.Matrix([[0, x[0], x[1], x[2]], [-x[0], 0, x[3], x[4]], [-x[1], -x[3], 0, x[0]], [-x[2], -x[4], -x[0], 0]])
S = x[0] * sp.eye(4)
u = x[0]**2 - x[1]*x[4] + x[2]*x[3]
out = {}
out['detK5_equals_u2'] = sp.expand(K5.det() - u**2) == 0
D = sp.expand((K5 + t*S).det())
P = sp.Poly(D, t)
coeffs = {m[0]: sp.factor(c) for m, c in zip(P.monoms(), P.coeffs())}
out['det_K5_tS_t_support'] = sorted(coeffs)
v = sp.expand(P.coeff_monomial(t**2))
w = sp.expand(P.coeff_monomial(t**4))
v_claim = sp.expand(x[0]**2 * (2*x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2))
out['v_matches_claim'] = sp.expand(v - v_claim) == 0
out['w_equals_x1^4'] = sp.expand(w - x[0]**4) == 0
def Delta(f):
    return sp.diff(f, x[0], 2) - 4*sp.diff(f, x[1], x[4]) + 4*sp.diff(f, x[2], x[3])
out['Delta2_u2'] = int(sp.expand(Delta(Delta(u**2))))
out['Delta2_v'] = int(sp.expand(Delta(Delta(v))))
# Q0 and its inverse: Delta must be the Q0^{-1}-Laplacian
Q0 = sp.Matrix(5, 5, lambda i, j: sp.Rational(1, 2) * sp.diff(u, x[i], x[j]))
Qinv = Q0.inv()
lap = sum(Qinv[i, j] * sp.diff(u**2, x[i], x[j]) for i in range(5) for j in range(5))
out['Delta_is_Q0inv_laplacian_on_u2'] = sp.expand(lap - Delta(u**2)) == 0
out['constant_5c'] = str(Fraction(5 * out['Delta2_v'], out['Delta2_u2']))  # should be 6/7
# ---- H5 : the unique (4^5) invariant of degree 5, integral convention T = alpha! c_alpha
def coeff_dict(F):
    p = sp.Poly(sp.expand(F), *x)
    return {m: int(c) for m, c in zip(p.monoms(), p.coeffs())}
def H5(f):
    rows = [[] for _ in range(5)]
    for alpha, c in f.items():
        inds = tuple(i for i, a in enumerate(alpha) for _ in range(a))
        coeff = c * math.prod(math.factorial(a) for a in alpha)
        for tup in set(it.permutations(inds)):
            rows[tup[0]].append((tup[1:], coeff))
    dp = {(0, 0, 0): 1}
    for row in rows:
        nd = defaultdict(int)
        for masks, val in dp.items():
            for vs, c in row:
                if any(m & (1 << q) for m, q in zip(masks, vs)): continue
                inv = sum((m >> (q + 1)).bit_count() for m, q in zip(masks, vs))
                nd[tuple(m | (1 << q) for m, q in zip(masks, vs))] += val * c * (-1) ** inv
        dp = {k: val for k, val in nd.items() if val}
    return dp.get((31, 31, 31), 0)
vals = {}
for tt in range(0, 5):
    vals[tt] = H5(coeff_dict(D.subs(t, tt)))
out['H5_at_K5_plus_tS_integral_convention'] = vals
base = vals[0]
out['H5_base_e95_convention_T_over_24'] = str(Fraction(base, 24**5))  # expect 175/36
out['normalized_values_t=0,1,2'] = [str(Fraction(vals[k], base)) for k in (0, 1, 2)]  # expect 1, 52/21, 301/21
out['C2_on_extendable_line_112v1-7v2-177v0'] = 112*vals[1] - 7*vals[2] - 177*vals[0]
# even polynomial of degree <= 4 in t on the extendable line? interpolate degree-20 poly from 21 points would be needed;
# instead check that H5(det(K5+tS)) computed symbolically in t is even and of degree <= 4:
Dt = sp.Poly(D, t)
# H5 symbolic in t: use exact polynomial arithmetic over Q[t] by evaluating at 21 nodes and interpolating
nodes = list(range(-10, 11))
ys = [H5(coeff_dict(D.subs(t, n))) for n in nodes]
poly = sp.interpolate(list(zip(nodes, ys)), t)
Pp = sp.Poly(sp.expand(poly), t)
out['H5_det_K5_tS_as_polynomial_in_t'] = {str(m[0]): str(c) for m, c in zip(Pp.monoms(), Pp.coeffs())}
c2 = Pp.coeff_monomial(t**2); c0 = Pp.coeff_monomial(1)
out['[t^2]/[t^0] on extendable line'] = str(sp.Rational(c2, c0))
# transposition/evenness on the whole source is a theorem (degree 4 in Y_1, K5^T=-K5); recorded, not computed.
# (8,4^4) exclusion premise: H5 nonzero at an actual determinant point (K5 itself is a pencil) 
out['H5_nonzero_at_actual_pencil_K5'] = base != 0
out['elapsed_s'] = time.perf_counter() - t0
open('pilots/p3_c2_derivation.json', 'w').write(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
