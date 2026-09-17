"""F1: are the explicit order-four transverse conditions C4_{S1,S2}, C4_{S1,S4} independent of the
order-two condition C2 on the certified two-dimensional subspace span(q3, q7) of M_(4^5)?

Inputs (read-only): sealed p6_basis.json (slot lists of q3, q7), sealed p7_arc_S0.json (preserved
values at K5, K5+S1, K5+2S1 and the C2 row), sealed paired_runner.py (dense evaluator, imported
unmodified), historical b18_02_carrier.py (pinned by SHA-256), Check 2 JSON of the sealed
transverse-structure report (H5 line values, C4 integer coefficients).

Stage 1: pricing (hand_plan, label-only), reproduction of a preserved value for EACH vector,
a corrupted-input control (must be rejected), a corrupted-coefficient control (must be rejected).
Stage 2: new evaluations at K5+S2, K5+2S2, K5+S4, K5+2S4 (S2 = x2*I on Y_2; S4 = x1*diag(1,1,0,0)
on Y_1), evenness and degree controls, C2/C4 rows on the columns (q3, q7), explicit 2x2 minors mod P.
Deadline 55 s inside the 60 s wrapper. JSON saved after every step.
This is NOT a test of independence from the arc C (C is injective on span(q3, q7))."""
import hashlib, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SEALED = ROOT / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(SEALED))
import paired_runner as pr            # sealed runner, imported unmodified
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 55.0
OUT = HERE / 'f1_c4_vs_c2.json'
rec = dict(cell=dict(d=5, lam=[4] * 5), prime=P, sealed_runner_sha256=hashlib.sha256((SEALED / 'paired_runner.py').read_bytes()).hexdigest(),
           carrier_sha256=hashlib.sha256(pr.SRC.read_bytes()).hexdigest(), steps=[])
def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1) + '\n')
def left():
    return DEADLINE - (time.perf_counter() - T0)

b6 = json.loads((SEALED / 'p6_basis.json').read_text()); p7 = json.loads((SEALED / 'p7_arc_S0.json').read_text())
assert b6['carrier_sha256'] == rec['carrier_sha256'] == p7['carrier_sha256']
c2j = json.loads((ROOT / 'work/claude_transverse_structure_20260916/checks/c2_fivevar_order4.json').read_text())['five_variables']
basis = []
for b, plan in zip(b6['basis'], p7['basis_plans']):
    pi = tuple(tuple(tuple(s) for s in blk) for blk in b['pi']); rho = tuple(tuple(tuple(s) for s in blk) for blk in b['rho'])
    hp = pr.hand_plan(pi, rho); hr = pr.hand_plan(rho, pi)
    assert list(hp[0]) == plan['order'] and list(hr[0]) == plan['order_rev'], (hp, hr, plan)
    basis.append(dict(index=b['index'], pi=pi, rho=rho, order=hp[0], order_rev=hr[0], maxint=max(hp[1], hr[1]), flops=hp[2] + hr[2]))
rec['vectors'] = [dict(index=b['index'], pairing=b6['basis'][i]['pairing'], pi=[[list(s) for s in blk] for blk in b['pi']], rho=[[list(s) for s in blk] for blk in b['rho']],
                       plan_order=list(b['order']), plan_order_transposed=list(b['order_rev']), max_intermediate_entries=b['maxint'], flop_units_both_orientations=b['flops']) for i, b in enumerate(basis)]
# ---- pricing (label-only, before any array)
rec['pricing'] = dict(max_intermediate_entries=max(b['maxint'] for b in basis), max_intermediate_bytes_int64=8 * max(b['maxint'] for b in basis),
                      column_tensor_entries=16 ** 5, column_tensor_bytes=8 * 16 ** 5,
                      einsum_overflow_guard='entries < P = 2^19, at most 4^12 summed products of size < 2^38 per einsum: 4^12 * P^2 < 2^63 (carrier MAX_SUM_LEGS = 12)',
                      sealed_measured_wall_per_symmetrised_evaluation_s=b6['wall_per_q_evaluation_s'],
                      planned_evaluations=dict(reproduction=4, corrupted_input=1, evenness=1, degree_node3=2, new_points=8, total=16),
                      estimate_wall_s='16 x 0.55 s + 16 column tensors x 0.07 s ~ 10 s', estimate_peak_memory='< 250 MB (sealed P7 peak 219 MB)')
save('priced')

def qval(b, T):
    a, m1, f1 = pr.evaluate_P(b['pi'], b['rho'], T, b['order']); bb, m2, f2 = pr.evaluate_P(b['rho'], b['pi'], T, b['order_rev'])
    rec['max_intermediate_seen'] = max(rec.get('max_intermediate_seen', 0), m1, m2)
    return (a + bb) % P

def K5_tuple(t=0, direction='S1', corrupt=False):
    """Exactly the sealed P7 convention: Y[i] = coefficient matrix of x_{i+1}; x1 at (0,1),(1,0) and (2,3),(3,2)."""
    Y = np.zeros((5, 4, 4), dtype=np.int64)
    for i, (r, cc) in enumerate([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]):
        Y[i, r, cc] = 1; Y[i, cc, r] = -1
    Y[0, 2, 3] += 1; Y[0, 3, 2] += -1
    if corrupt:            # deliberate corruption: wrong sign at the repeated x1 position -> not K5
        Y[0, 2, 3] -= 2; Y[0, 3, 2] += 2
    if direction == 'S1':   Y[0] += t * np.eye(4, dtype=np.int64)
    elif direction == 'S2': Y[1] += t * np.eye(4, dtype=np.int64)
    elif direction == 'S4': Y[0] += t * np.diag(np.array([1, 1, 0, 0], dtype=np.int64))
    else: raise ValueError(direction)
    return Y % P
def evaluate(t, direction, corrupt=False):
    T = c.column_tensor(K5_tuple(t, direction, corrupt), 5)
    return [qval(b, T) for b in basis]

# ---- Stage 1 controls
pres = p7['C2_values_at_K5_K5S_K52S']          # [[q3(K5), q7(K5)], [q3(K5+S1), q7(K5+S1)], [q3(K5+2S1), q7(K5+2S1)]]
rec['preserved_values'] = dict(K5=pres[0], K5_S1=pres[1], K5_2S1=pres[2], C2_row=p7['C2_row'])
v0 = evaluate(0, 'S1'); v1 = evaluate(1, 'S1')
rec['reproduction'] = dict(K5_recomputed=v0, K5_stored=pres[0], K5_S1_recomputed=v1, K5_S1_stored=pres[1],
                           passed_each_vector=[v0[i] == pres[0][i] and v1[i] == pres[1][i] for i in range(2)])
save('reproduction_done')
assert all(rec['reproduction']['passed_each_vector']), rec['reproduction']
vc = evaluate(0, 'S1', corrupt=True)
rec['corrupted_input_control'] = dict(values=vc, stored=pres[0], rejected=(vc != pres[0]))
assert rec['corrupted_input_control']['rejected']
H5 = {k: c2j['ambient_line'][k]['H5_values_t0_to_4'] for k in ('S1=x1*I', 'S2=x2*I', 'S4=x1*diag(1,1,0,0)')}
C4 = {tuple(x['pair']): x['coefficients'] for x in c2j['C4']}
rows_def = {'C4_S1_S2': (C4[('S1=x1*I', 'S2=x2*I')], 'S2=x2*I'), 'C4_S1_S4': (C4[('S1=x1*I', 'S4=x1*diag(1,1,0,0)')], 'S4=x1*diag(1,1,0,0)')}
def h5vec(other):
    a = H5['S1=x1*I']; b = H5[other]; return [a[0], a[1], a[2], b[1], b[2]]
coef_ctrl = {}
for name, (co, other) in rows_def.items():
    good = sum(x * y for x, y in zip(co, h5vec(other)))
    bad = list(co); bad[0] += 1
    badv = sum(x * y for x, y in zip(bad, h5vec(other)))
    coef_ctrl[name] = dict(coefficients=co, value_on_H5_generator=good, corrupted_coefficients=bad, corrupted_value=badv, corruption_rejected=(good == 0 and badv != 0))
rec['coefficient_controls'] = coef_ctrl
assert all(x['corruption_rejected'] for x in coef_ctrl.values())
c2_re = [(112 * pres[1][i] - 7 * pres[2][i] - 177 * pres[0][i]) % P for i in range(2)]
rec['C2_row_recomputed_from_preserved'] = c2_re; assert c2_re == p7['C2_row']
save('stage1_controls_done')

# ---- Stage 2: new points
new = {}
for direction, ts in (('S2', (1, 2)), ('S4', (1, 2))):
    for t in ts:
        if left() < 8: save('deadline_before_new_points'); raise SystemExit(124)
        new[f'{direction}_t{t}'] = evaluate(t, direction); save('new_points_in_progress')
rec['new_values'] = new
# evenness control (q3, q7 at K5 - S2 must equal K5 + S2) and degree-<=4 control at t = 3 for S2
if left() > 8:
    vm = evaluate(-1, 'S2'); rec['evenness_control'] = dict(K5_minus_S2=vm, K5_plus_S2=new['S2_t1'], passed=(vm == new['S2_t1']))
if left() > 8:
    v3 = evaluate(3, 'S2')
    z0 = pres[0]; z1 = new['S2_t1']; z2 = new['S2_t2']
    inv12 = pow(12, P - 2, P)
    c2c = [((16 * z1[i] - z2[i] - 15 * z0[i]) * inv12) % P for i in range(2)]
    c4c = [((z2[i] - 4 * z1[i] + 3 * z0[i]) * inv12) % P for i in range(2)]
    pred = [(z0[i] + 9 * c2c[i] + 81 * c4c[i]) % P for i in range(2)]
    rec['degree_le_4_control_S2'] = dict(t3_recomputed=v3, t3_predicted_from_even_quartic=pred, passed=(v3 == pred), t2_coeff=c2c, t4_coeff=c4c)
save('controls_done')
# ---- rows on the same columns (q3, q7)
def row(co, other_key):
    vals = [pres[0], pres[1], pres[2], new[f'{other_key}_t1'], new[f'{other_key}_t2']]
    return [sum(co[k] * vals[k][i] for k in range(5)) % P for i in range(2)]
R = {'C2': p7['C2_row'], 'C4_S1_S2': row(rows_def['C4_S1_S2'][0], 'S2'), 'C4_S1_S4': row(rows_def['C4_S1_S4'][0], 'S4')}
rec['rows_on_q3_q7'] = R
def det2(a, b): return (a[0] * b[1] - a[1] * b[0]) % P
rec['minors_2x2_mod_P'] = {'C2,C4_S1_S2': det2(R['C2'], R['C4_S1_S2']), 'C2,C4_S1_S4': det2(R['C2'], R['C4_S1_S4']), 'C4_S1_S2,C4_S1_S4': det2(R['C4_S1_S2'], R['C4_S1_S4'])}
rec['rank_of_3x2_mod_P'] = c.rank_mod([R['C2'], R['C4_S1_S2'], R['C4_S1_S4']])
rec['verdict'] = ('INDEPENDENT_over_Q_on_span_q3_q7' if any(v for k, v in rec['minors_2x2_mod_P'].items() if k.startswith('C2,')) else 'no_nonzero_minor_modular_inconclusive')
save('DONE')
print(json.dumps({k: v for k, v in rec.items() if k not in ('vectors',)}, indent=1))
