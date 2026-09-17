"""Check 2: target-side transverse jets at u^2 in r variables, the universal quartic A_{r,k}(S), the
H_4-pairing N(h_4(S)), the explicit E-free order-four condition C4 in five variables (k = 1), and
the control that it vanishes exactly on the ambient line H5 o phi.  Six-variable constants are
recomputed as a control against attachment 515d31fd (ratios 108 and -14) and the sealed p9 values.
No source contraction is evaluated. Output: c2_fivevar_order4.json in the same directory.
"""
import itertools as it, json, math, time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
t0 = time.perf_counter()
t = sp.Symbol('t')

def setup(n, K, u, x):
    Q0 = sp.Matrix(n, n, lambda i, j: sp.Rational(1, 2) * sp.diff(u, x[i], x[j]))
    Qinv = Q0.inv()
    def Lap(f):
        return sp.expand(sum(Qinv[i, j] * sp.diff(f, x[i], x[j]) for i in range(n) for j in range(n)))
    def c_of(q):                       # u^2-component of a quartic q
        return sp.Rational(Lap(Lap(q)), Lap(Lap(u ** 2)))
    def harmonic_split(q):             # q = h4 + u h2 + c u^2
        c = c_of(q)
        h2 = sp.expand((Lap(q) - c * (4 * n + 8) * u) / (2 * n + 8))
        h4 = sp.expand(q - u * h2 - c * u ** 2)
        assert Lap(h2) == 0 and Lap(h4) == 0, "harmonic split failed"
        return h4, h2, c
    def Npair(h, hp):                  # h(Qinv d) hp
        eta = sp.symbols('eta0:%d' % n)
        op = sp.Poly(sp.expand(h.subs({x[i]: sum(Qinv[i, j] * eta[j] for j in range(n)) for i in range(n)}, simultaneous=True)), *eta)
        total = 0
        for mon, coeff in zip(op.monoms(), op.coeffs()):
            g = hp
            for j, e in enumerate(mon):
                if e: g = sp.diff(g, x[j], e)
            total += coeff * g
        return sp.nsimplify(sp.expand(total))
    def direction(S, d, k):
        D = sp.Poly(sp.expand((K + t * S).det()), t)
        coeffs = {m[0]: sp.expand(c) for m, c in zip(D.monoms(), D.coeffs())}
        support = sorted(coeffs)
        v = coeffs.get(2, sp.Integer(0)); w = coeffs.get(4, sp.Integer(0))
        h4, h2, cv = harmonic_split(v)
        a = sp.expand(h2 + cv * u)
        Qa = sp.Matrix(n, n, lambda i, j: sp.Rational(1, 2) * sp.diff(a, x[i], x[j]))
        M = Qinv * Qa
        trM = M.trace(); trM2 = (M * M).trace()
        A = d * c_of(w) + sp.Rational(1, 4) * (k * (2 * k * trM ** 2 - trM2) - d * c_of(sp.expand(a ** 2)))
        N = Npair(h4, h4)
        return dict(support=support, c_v=str(cv), c_w=str(c_of(w)), trM=str(trM), trM2=str(trM2),
                    A=str(sp.nsimplify(A)), N_h4=str(N), h4_nonzero=(h4 != 0), _A=sp.nsimplify(A), _N=N, _cv=cv, _v=v, _w=w)
    return dict(Q0=Q0, Qinv=Qinv, Lap=Lap, c_of=c_of, split=harmonic_split, N=Npair, direction=direction)

out = {}
# ------------------------------------------------------------------ six variables (control)
x6 = sp.symbols('x1:7')
K6 = sp.Matrix([[0, x6[0], x6[1], x6[2]], [-x6[0], 0, x6[3], x6[4]], [-x6[1], -x6[3], 0, x6[5]], [-x6[2], -x6[4], -x6[5], 0]])
u6 = x6[0] * x6[5] - x6[1] * x6[4] + x6[2] * x6[3]
S6 = setup(6, K6, u6, x6)
six = {}
six['Lap2_u2'] = int(S6['Lap'](S6['Lap'](u6 ** 2)))               # expect 384
dirs6 = {'S1=x1*I': x6[0] * sp.eye(4), 'S2=(x1+x6)*I': (x6[0] + x6[5]) * sp.eye(4)}
res6 = {name: S6['direction'](S, 6, 1) for name, S in dirs6.items()}
six['directions'] = {name: {k: v for k, v in r.items() if not k.startswith('_')} for name, r in res6.items()}
r1, r2 = res6['S1=x1*I'], res6['S2=(x1+x6)*I']
six['N_ratio_S2_over_S1'] = str(sp.nsimplify(r2['_N'] / r1['_N']))            # expect 108
six['A2_minus_108_A1'] = str(sp.nsimplify(r2['_A'] - 108 * r1['_A']))          # expect -14
# sealed p9 values of [t^4]/[t^0] on the extendable line: 3/14 (S1), 64/7 (S2): one kappa must fit both
kap1 = (sp.Rational(3, 14) - r1['_A']) / r1['_N']; kap2 = (sp.Rational(64, 7) - r2['_A']) / r2['_N']
six['kappa_from_S1'] = str(kap1); six['kappa_from_S2'] = str(kap2); six['single_kappa_fits_p9_values'] = (kap1 == kap2)
six['t2_over_t0_on_E'] = {n: str(6 * r['_cv']) for n, r in res6.items()}      # expect 1, 2 (p9)
out['six_variables_control'] = six

# ------------------------------------------------------------------ five variables, k = 1
x = sp.symbols('x1:6')
K5 = sp.Matrix([[0, x[0], x[1], x[2]], [-x[0], 0, x[3], x[4]], [-x[1], -x[3], 0, x[0]], [-x[2], -x[4], -x[0], 0]])
u5 = x[0] ** 2 - x[1] * x[4] + x[2] * x[3]
S5 = setup(5, K5, u5, x)
five = {}
five['detK5_is_u2'] = sp.expand(K5.det() - u5 ** 2) == 0
five['Lap2_u2'] = int(S5['Lap'](S5['Lap'](u5 ** 2)))               # expect 280
five['det_Q0'] = str(S5['Q0'].det())
dirs5 = {
    'S1=x1*I': x[0] * sp.eye(4),
    'S2=x2*I': x[1] * sp.eye(4),
    'S3=(x1+x2)*I': (x[0] + x[1]) * sp.eye(4),
    'S4=x1*diag(1,1,0,0)': x[0] * sp.diag(1, 1, 0, 0),
    'S5=(x1+x3)*I': (x[0] + x[2]) * sp.eye(4),
}
d5, k5 = 5, 1
res5 = {name: S5['direction'](S, d5, k5) for name, S in dirs5.items()}
five['directions'] = {name: {k: v for k, v in r.items() if not k.startswith('_')} for name, r in res5.items()}

# ---- H5: the unique (4^5) degree-five ambient invariant, integral convention T_alpha = alpha! c_alpha
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
        dp = {kk: vv for kk, vv in nd.items() if vv}
    return dp.get((31, 31, 31), 0)

line = {}
kappas = {}
for name, S in dirs5.items():
    D = sp.expand((K5 + t * S).det())
    vals = [H5(coeff_dict(D.subs(t, tt))) for tt in range(0, 5)]
    poly = sp.Poly(sp.interpolate(list(zip(range(5), vals)), t), t)
    cf = {m[0]: int(c) for m, c in zip(poly.monoms(), poly.coeffs())}
    z0, z2, z4 = cf.get(0, 0), cf.get(2, 0), cf.get(4, 0)
    r = res5[name]
    three_point_t4 = Fraction(vals[2] - 4 * vals[1] + 3 * vals[0], 12)
    three_point_t2 = Fraction(16 * vals[1] - vals[2] - 15 * vals[0], 12)
    kap = (sp.Rational(z4, z0) - r['_A']) / r['_N'] if r['_N'] != 0 else None
    kappas[name] = kap
    line[name] = dict(H5_values_t0_to_4=vals, poly_support=sorted(cf), is_even_quartic=(set(cf) <= {0, 2, 4}),
                      three_point_t4_matches=(three_point_t4 == Fraction(z4)), three_point_t2_matches=(three_point_t2 == Fraction(z2)),
                      t2_over_t0=str(sp.Rational(z2, z0)), predicted_t2_over_t0=str(d5 * r['_cv']),
                      order2_automatic_on_E=(sp.Rational(z2, z0) == d5 * r['_cv']),
                      t4_over_t0=str(sp.Rational(z4, z0)), kappa_tilde=str(kap))
five['ambient_line'] = line
five['H5_at_K5'] = line['S1=x1*I']['H5_values_t0_to_4'][0]            # expect 322560
five['single_kappa_fits_all_directions'] = len({str(v) for v in kappas.values() if v is not None}) == 1
five['kappa_tilde'] = str(next(iter(kappas.values())))

# ---- explicit E-free order-four condition C4 for a pair of directions (S, S'), k = 1:
#  12*[ N' (J_S - z0 A) - N (J_S' - z0 A') ] with J = (z(K+2S) - 4 z(K+S) + 3 z(K))/12
def C4_coeffs(nameA, nameB):
    rA, rB = res5[nameA], res5[nameB]
    NA, NB, AA, AB = rA['_N'], rB['_N'], rA['_A'], rB['_A']
    # coefficient vector on (z(K), z(K+S_A), z(K+2S_A), z(K+S_B), z(K+2S_B)), times 12
    vec = [NB * 3 - NA * 3 - 12 * (NB * AA - NA * AB), -4 * NB, NB, 4 * NA, -NA]
    vec = [sp.nsimplify(v) for v in vec]
    den = sp.ilcm(*[sp.fraction(v)[1] for v in vec])
    ivec = [int(v * den) for v in vec]
    g = math.gcd(*ivec); ivec = [v // g for v in ivec]
    hA = line[nameA]['H5_values_t0_to_4']; hB = line[nameB]['H5_values_t0_to_4']
    vals = [hA[0], hA[1], hA[2], hB[1], hB[2]]
    return dict(pair=(nameA, nameB), integer_coefficients_on=(f'z(K5)', f'z(K5+{nameA})', f'z(K5+2{nameA})', f'z(K5+{nameB})', f'z(K5+2{nameB})'),
                coefficients=ivec, value_on_H5_line=sum(c * v for c, v in zip(ivec, vals)),
                N_ratio=str(sp.nsimplify(NB / NA)), A_combination=str(sp.nsimplify(AB - (NB / NA) * AA)))
five['C4'] = [C4_coeffs('S1=x1*I', 'S2=x2*I'), C4_coeffs('S1=x1*I', 'S3=(x1+x2)*I'), C4_coeffs('S1=x1*I', 'S4=x1*diag(1,1,0,0)'), C4_coeffs('S1=x1*I', 'S5=(x1+x3)*I')]
# ---- general-k formula recorded symbolically for (4k)^5 (not checked beyond k = 1)
kk = sp.Symbol('k')
five['general_k_note'] = ('[t^2] z / z(K5) on E = d*c_v = 5k*c_v; A_{5,k}(S) = 5k*c_w + (1/4)*(k*(2k*trM^2 - trM2) - 5k*c(a^2)); '
                          'z(K5 + t S) is even of degree <= 4k in t for S = ell(x)*M (rank-one tuple update), so [t^2],[t^4] need 2k+1 even nodes.')
five['t2_over_t0_general_k_S1'] = str(sp.nsimplify(5 * kk * res5['S1=x1*I']['_cv']))
out['five_variables'] = five
out['elapsed_s'] = time.perf_counter() - t0
(HERE / 'c2_fivevar_order4.json').write_text(json.dumps(out, indent=1, default=str) + '\n')
print(json.dumps(out, indent=1, default=str))
