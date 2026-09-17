"""P9: independent arithmetic replay of the six-row fourth-order transverse condition
(attachment 515d31fd) using Astra's own sparse evaluator read-only (sixrow_witness.invariant_Q,
sixrow_witness.H6, sixrow_witness.quartic). Checks:
  (i)  Q(K + t S1), Q(K + t S2) for t = 0,1,2 and the claimed normalised values 1, 9/4, 9, 4, 25 of P^2;
  (ii) the necessary map on the extendable line: 12 C2(z) = z(K+2S2) - 4 z(K+S2) - 108 z(K+2S1) + 432 z(K+S1) - 153 z(K)
       must vanish for z = H6 o phi (a = 1, so E = span(H6 o phi));
  (iii) C2(Q^2) normalised by Q(K)^2 equals -12;
  (iv) the derivation constants c = Delta^2 v / 384 for S1, S2 with Delta = 4(d1 d6 - d2 d5 + d3 d4), and [t^2]/[t^0] = 6c on E.
"""
import json, sys, time
from fractions import Fraction
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
ASTRA = HERE.parents[1] / 'extension_descent_20260916'
sys.path.insert(0, str(ASTRA))
import sixrow_witness as sw
import skew_witness as base
t0 = time.perf_counter()
# K: six standard skew matrices (edges in EDGES order), as in sixrow_witness.main
skew = []
for i, j in base.EDGES:
    m = [0] * 16; m[4 * i + j] = 1; m[4 * j + i] = -1; skew.append(m)
def with_S(tt, kind):
    Y = [list(m) for m in skew]
    if kind == 1:      # S1 = x1 I4 : add t*I to Y_1
        for d in range(4): Y[0][5 * d] += tt
    else:              # S2 = (x1 + x6) I4 : add t*I to Y_1 and Y_6
        for d in range(4): Y[0][5 * d] += tt; Y[5][5 * d] += tt
    return Y
out = {}
pts = {('K', 0): skew}
for kind in (1, 2):
    for tt in (1, 2):
        pts[('S%d' % kind, tt)] = with_S(tt, kind)
vals = {}
for key, Y in pts.items():
    q, n = sw.invariant_Q(Y)
    f = sw.quartic(Y)
    h, peak = sw.H6(f)
    vals[key] = dict(Q=q, Q2=q * q, H6=h, assignments=n)
out['values'] = {str(k): v for k, v in vals.items()}
QK = vals[('K', 0)]['Q']; HK = vals[('K', 0)]['H6']
out['Q_K'] = QK; out['H6_K'] = HK
order = [('K', 0), ('S1', 1), ('S1', 2), ('S2', 1), ('S2', 2)]
out['P2_normalised'] = [str(Fraction(vals[k]['Q2'], QK * QK)) for k in order]          # expect 1, 9/4, 9, 4, 25
out['P_normalised'] = [str(Fraction(vals[k]['Q'], QK)) for k in order]                 # expect 1, 3/2, 3, 2, 5
def C2x12(z):
    return z[('S2', 2)] - 4 * z[('S2', 1)] - 108 * z[('S1', 2)] + 432 * z[('S1', 1)] - 153 * z[('K', 0)]
out['12C2_on_H6_extendable_line'] = C2x12({k: vals[k]['H6'] for k in order})          # must be 0
out['12C2_on_Q2_normalised'] = str(Fraction(C2x12({k: vals[k]['Q2'] for k in order}), QK * QK))   # expect -144
out['C2_on_Q2_normalised'] = str(Fraction(C2x12({k: vals[k]['Q2'] for k in order}), 12 * QK * QK))  # expect -12
# (iv) derivation constants in six variables
x = sp.symbols('x1:7'); t = sp.Symbol('t')
K = sp.Matrix([[0, x[0], x[1], x[2]], [-x[0], 0, x[3], x[4]], [-x[1], -x[3], 0, x[5]], [-x[2], -x[4], -x[5], 0]])
u = x[0] * x[5] - x[1] * x[4] + x[2] * x[3]
out['detK_is_u2'] = sp.expand(K.det() - u ** 2) == 0
def Delta(f):
    return 4 * (sp.diff(f, x[0], x[5]) - sp.diff(f, x[1], x[4]) + sp.diff(f, x[2], x[3]))
consts = {}
for kind, ell in ((1, x[0]), (2, x[0] + x[5])):
    Dt = sp.Poly(sp.expand((K + t * ell * sp.eye(4)).det()), t)
    v = sp.expand(Dt.coeff_monomial(t ** 2)); w = sp.expand(Dt.coeff_monomial(t ** 4))
    r = sum(xi ** 2 for xi in x)
    consts['S%d' % kind] = dict(support=sorted(m[0] for m in Dt.monoms()), v_equals_ell2_r=(sp.expand(v - ell ** 2 * r) == 0), w_equals_ell4=(sp.expand(w - ell ** 4) == 0),
                                Delta2_v=int(Delta(Delta(v))), Delta2_u2=int(Delta(Delta(u ** 2))), c=str(Fraction(int(Delta(Delta(v))), 384)))
out['derivation_constants'] = consts
# [t^2]/[t^0] on E from H6 values: use t = 0,1,2 with the even-degree-<=4 structure
for kind in (1, 2):
    z0 = vals[('K', 0)]['H6']; z1 = vals[('S%d' % kind, 1)]['H6']; z2 = vals[('S%d' % kind, 2)]['H6']
    c2 = Fraction(16 * z1 - z2 - 15 * z0, 12)   # [t^2] for an even quartic in t
    c4 = Fraction(z2 - 4 * z1 + 3 * z0, 12)
    consts['S%d' % kind]['t2_over_t0_on_E'] = str(c2 / z0); consts['S%d' % kind]['six_c'] = str(6 * Fraction(consts['S%d' % kind]['c']))
    consts['S%d' % kind]['t4_over_t0_on_E'] = str(c4 / z0)
out['elapsed_s'] = time.perf_counter() - t0
(HERE / 'p9_sixrow_replay.json').write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
