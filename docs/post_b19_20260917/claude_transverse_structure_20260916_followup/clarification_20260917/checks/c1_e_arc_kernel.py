"""Premise check for the carrier count (arithmetic only, no source contraction):
e := H5 o phi, e(Y) = H5(det(sum_i x_i Y_i)), H5 the (4^5) alternant in the integral convention
T_alpha = alpha! c_alpha (sealed p3 / Check 2 formula).  At the three sealed P7 symmetric-part-zero
points, scaling a = Y[:,0,0] by t gives z(t) = z10 + t z11 + t^2 z12 with z11, z12 the S0-restricted
forbidden components (B18-02 Lemma 4.1 with #Sigma = 0).  Since e in E subset ker C, e(t) must be
CONSTANT in t at every such point (exact integers).  Also records e at the P6 points 0..4 and its
sign-flip / degenerate / scale-2 controls for the handoff."""
import itertools as it, json, math, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[3]
t0 = time.perf_counter()
x = sp.symbols('x1:6')
p7 = json.loads((ROOT / 'work/descent_followup_claude_20260916/pilots/p7_arc_S0.json').read_text())
p6 = json.loads((ROOT / 'work/descent_followup_claude_20260916/pilots/p6_basis.json').read_text())

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

def e_of(Y):                      # Y: list of five 4x4 integer matrices (coefficient matrices of x1..x5)
    M = sp.zeros(4, 4)
    for i in range(5): M += x[i] * sp.Matrix(Y[i])
    return H5(coeff_dict(M.det()))

out = {'convention': 'e(Y) = H5(det(sum x_i Y_i)), H5 = sum_{sigma,tau,upsilon in S5} sgn sgn sgn prod_i T_{i,sigma(i),tau(i),upsilon(i)}, T_alpha = alpha! c_alpha, exact integers'}
res = []
for pt in p7['points']:
    Y = pt['entries']; vals = {}
    for tt in range(4):
        Yt = [[row[:] for row in m] for m in Y]
        for i in range(5): Yt[i][0][0] = Y[i][0][0] * tt
        vals[tt] = e_of(Yt)
    res.append(dict(point=pt['index'], e_at_t0_t1_t2_t3=[vals[k] for k in range(4)], constant_in_t=(len(set(vals.values())) == 1)))
out['S0_points_forbidden_check'] = res
out['e_in_ker_C_on_S0_slice_all_points'] = all(r['constant_in_t'] for r in res)
out['e_at_P6_points_0_to_4'] = [e_of(Y) for Y in p6['points_entries']]
K5 = [[[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]], [[0, 0, 1, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0]],
      [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 0]],
      [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, -1, 0, 0]]]
out['e_at_K5'] = e_of(K5)                                        # expect 322560
Kflip = [[row[:] for row in m] for m in K5]; Kflip[0][2][3] = -1; Kflip[0][3][2] = 1
Kdeg = [[row[:] for row in m] for m in K5]; Kdeg[0][2][3] = 0; Kdeg[0][3][2] = 0
K2 = [[row[:] for row in m] for m in K5]; K2[1] = [[2 * v for v in row] for row in K2[1]]
out['e_at_stabilizer_conjugate_signflip'] = e_of(Kflip)          # expect 322560 (same orbit)
out['e_at_degenerate_pencil'] = e_of(Kdeg)                       # expect 0 (torus argument)
out['e_at_Y2_scaled_by_2'] = e_of(K2)                            # expect 16 * 322560
out['controls_passed'] = (out['e_at_K5'] == 322560 and out['e_at_stabilizer_conjugate_signflip'] == 322560 and out['e_at_degenerate_pencil'] == 0 and out['e_at_Y2_scaled_by_2'] == 16 * 322560)
out['elapsed_s'] = time.perf_counter() - t0
(HERE / 'c1_e_arc_kernel.json').write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
