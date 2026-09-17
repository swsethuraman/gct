"""B20-01 pilot 2: numerical control of Theorem A (reduction of the degree-11 identity to the flag locus).

At the sealed P6 point 0 (Y0), for q in (q3, q7, n02):
  1. slice form: g in GL_5, Ytilde = g.Y0 = (Z_1, Z_2, Z_3+nu_1, Z_4+nu_2, Z_5+nu_3);
  2. F_k := [u^11] q(Z_1, Z_2, [Z_{k+2}]+u nu_1, [Z_{k+2}]+u nu_2, [Z_{k+2}]+u nu_3), k = 1,2,3, from the five nodes
     u = 1..5 (u-degrees 8..12 only at such tuples); the [u^12] coefficient must be the same for all k (the top);
  3. claim: det(g)^4 (F_1 + F_2 + F_3) == z^{[11]}(Y0) (sealed full row full_P6pt0_d11 = [86170, 71919, 226580])
            det(g)^4 [u^12]           == z^{[12]}(Y0) (sealed full row full_P6pt0_d12 = [376209, 469277, 41046]);
  4. S_3 control: F_2(Z_1, Z_2, Z_4) == -F_1(P Z_1 P^T, P Z_2 P^T, P Z_4 P^T) for P = diag(1, transposition) swapping
     matrix indices 1 <-> 2 (block indices 0 <-> 1; P nu_1 P^T = -nu_2), report Theorem A(iv); the sign is recorded.
Runner evaluations: 3 vectors x (3 x 5 + 5) = 60, about 30 s.  Deadline 55 s; JSON saved after every stage."""
import json, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import b20_01_pinned as pin
import b20_01_flag as fl
T0 = time.perf_counter(); DEADLINE = 55.0
OUT = ROOT / 'results/b20_01/p2_reduction.json'
pr, prrec = pin.load_runner(); c = pr.c; np = pr.np; P = pr.P; assert P == fl.P
rec = dict(pilot='b20_01_p2_reduction', prime=P, code_pins=prrec, inputs=dict(), checks=dict(), evaluations=0, eval_wall_s=0.0, log=[])
def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1, default=str) + '\n')
def left(): return DEADLINE - (time.perf_counter() - T0)
def get(name):
    b, r = pin.fetch(name); rec['inputs'][name] = r; return b
p6 = json.loads(get('p6_basis.json')); n02d = json.loads(get('n02_definition.json'))
def tup(blocks): return tuple(tuple(tuple(int(x) for x in s) for s in b) for b in blocks)
VEC = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
    VEC['q%d' % b['index']] = dict(pi=tup(b['pi']), rho=tup(b['rho']), order=order, order_rev=order)
VEC['n02'] = dict(pi=tup(n02d['pi_ordered_blocks']), rho=tup(n02d['rho_ordered_blocks']), order=tuple(n02d['hand_plan_column_order']), order_rev=tuple(n02d['hand_plan_column_order_transposed']))
for d in VEC.values():
    assert tuple(pr.hand_plan(d['pi'], d['rho'])[0]) == d['order'] and tuple(pr.hand_plan(d['rho'], d['pi'])[0]) == d['order_rev']
ORDER = ['q3', 'q7', 'n02']
SEALED = dict(d11=[86170, 71919, 226580], d12=[376209, 469277, 41046], source='final_arc_diagnostic/code/f1_new_point_minor.py INH full_P6pt0 (s3_full_forbidden_rows.json)')
def qval(d, T):
    te = time.perf_counter()
    a, m1, _ = pr.evaluate_P(d['pi'], d['rho'], T, d['order']); b_, m2, _ = pr.evaluate_P(d['rho'], d['pi'], T, d['order_rev'])
    rec['evaluations'] += 1; rec['eval_wall_s'] += time.perf_counter() - te; assert max(m1, m2) <= 4 ** 10
    return (a + b_) % P

Y0 = np.array(p6['points_entries'][0], dtype=np.int64)
rec['checks']['sign_convention_reconstruction'] = fl.reconstruct(Y0)
assert rec['checks']['sign_convention_reconstruction']
g, detg, Yt = fl.slice_form(Y0)
Z = fl.wprime_part(Yt)                       # Z_1..Z_5 (W'-parts); Yt[i] = Z[i] + nu_{i-2} for i >= 2
rec['slice_form'] = dict(g=g.tolist(), det_g_mod_P=detg, det_g4=pow(detg, 4, P), Ztilde=Z.tolist())
save('slice_form')

# ---- stage 2: F_k by five-node extraction
tensors = {}
def T_of(k, u):
    key = (k, u)
    if key not in tensors: tensors[key] = c.column_tensor(fl.tuple_F(Z[0], Z[1], Z[2 + k], k, u), 5)
    return tensors[key]
F = {name: {} for name in ORDER}; TOP = {name: {} for name in ORDER}
for k in range(3):
    for name in ORDER:
        if left() < 5 * 0.6 + 1: rec['log'].append('deadline before k=%d %s' % (k, name)); save('partial'); sys.exit(0)
        vals = [qval(VEC[name], T_of(k, u)) for u in fl.NODES5]
        co = fl.vandermonde_solve(fl.NODES5, vals, [8, 9, 10, 11, 12])
        F[name][k] = co[11]; TOP[name][k] = co[12]
        rec.setdefault('F_k', {}).setdefault(name, {})[k] = dict(values_u1_to_5=vals, coefficients={str(d): v for d, v in co.items()})
    save('F_k_%d' % k)
d4 = pow(detg, 4, P)
rec['checks']['top_equal_across_k'] = {name: len(set(TOP[name].values())) == 1 for name in ORDER}
rec['checks']['degree11_reconstruction'] = {name: dict(det_g4_times_sum_F=(d4 * sum(F[name].values())) % P, sealed=SEALED['d11'][i]) for i, name in enumerate(ORDER)}
rec['checks']['degree12_reconstruction'] = {name: dict(det_g4_times_top=(d4 * TOP[name][0]) % P, sealed=SEALED['d12'][i]) for i, name in enumerate(ORDER)}
rec['checks']['theorem_A_passed'] = all(v['det_g4_times_sum_F'] == v['sealed'] for v in rec['checks']['degree11_reconstruction'].values()) and \
                                    all(v['det_g4_times_top'] == v['sealed'] for v in rec['checks']['degree12_reconstruction'].values())
rec['checks']['sealed_rows_source'] = SEALED['source']
save('theorem_A')

# ---- stage 3: S_3 control (block transposition 1 <-> 2, i.e. matrix rows/columns 2 <-> 3)
Pm = np.eye(4, dtype=np.int64)[[0, 2, 1, 3]]
def conj(M): return (Pm @ (M % P) @ Pm.T) % P
s3 = {}
for name in ORDER:
    if left() < 5 * 0.6 + 1: rec['log'].append('deadline before S3 %s' % name); break
    T = [c.column_tensor(fl.tuple_F(conj(Z[0]), conj(Z[1]), conj(Z[3]), 0, u), 5) for u in fl.NODES5]
    vals = [qval(VEC[name], t) for t in T]
    co = fl.vandermonde_solve(fl.NODES5, vals, [8, 9, 10, 11, 12])
    s3[name] = dict(F1_at_permuted_point=co[11], F2_at_point=F[name][1], equal_up_to_sign=(co[11] == F[name][1] or (co[11] + F[name][1]) % P == 0),
                    sign=(1 if co[11] == F[name][1] else (-1 if (co[11] + F[name][1]) % P == 0 else None)), top_at_permuted_point=co[12], top=TOP[name][0])
rec['checks']['S3_control'] = s3
save('done')
print(json.dumps(dict(status=rec['status'], checks=rec['checks'], evaluations=rec['evaluations'], eval_wall_s=rec['eval_wall_s'], elapsed_s=rec['elapsed_s']), indent=1, default=str))
