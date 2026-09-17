"""B20-01 pilot 3: Route 2 (negation) at the reduced price of Theorem A.

New degree-11 functionals on (q3, q7, n02) are rows F_1 at seeded points (Z_1, Z_2, Z) of W'^3 with all 39
coordinates uniform mod P (seed 20260917; the tuple is (Z_1, Z_2, Z+u nu_1, u nu_2, u nu_3), five nodes u = 1..5,
[u^11] = the degree-11 value, [u^12] = the degree-12 value).  Cost 15 runner evaluations per point instead of 39.
Stop rule: the first nonzero 3x3 minor with at least two degree-11 rows (new or inherited) settles rank(C|_U) = 3.
Evidence rule (MEASURED only): a row at a point uniform mod P vanishes on a nonzero polynomial of degree <= 9 in the
39 coordinates with probability <= 9/P; concordant rows are reported as such, never as a ceiling (G5' condition 4).
Deadline 55 s; JSON saved after every point."""
import itertools, json, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import b20_01_pinned as pin
import b20_01_flag as fl
T0 = time.perf_counter(); DEADLINE = 55.0; NPOINTS = 5
OUT = ROOT / 'results/b20_01/p3_flag_rows.json'
pr, prrec = pin.load_runner(); c = pr.c; np = pr.np; P = pr.P
rec = dict(pilot='b20_01_p3_flag_rows', prime=P, seed=20260917, code_pins=prrec, inputs=dict(), checks=dict(), evaluations=0, eval_wall_s=0.0, log=[])
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
ORDER = ['q3', 'q7', 'n02']
def qval(d, T):
    te = time.perf_counter()
    a, m1, _ = pr.evaluate_P(d['pi'], d['rho'], T, d['order']); b_, m2, _ = pr.evaluate_P(d['rho'], d['pi'], T, d['order_rev'])
    rec['evaluations'] += 1; rec['eval_wall_s'] += time.perf_counter() - te; assert max(m1, m2) <= 4 ** 10
    return (a + b_) % P
# inherited rows (final_arc_diagnostic/code/f1_new_point_minor.py, INH; values mod P), columns (q3, q7, n02)
INH = [dict(label='S0_P7pt0_d11', row=[34725, 239889, 380115]), dict(label='S0_P7pt0_d12', row=[176113, 112168, 44818]),
       dict(label='S0_P7pt1_d11', row=[163934, 316261, 169076]), dict(label='S0_P7pt1_d12', row=[190461, 231336, 338217]),
       dict(label='S0_P7pt2_d11', row=[395778, 379744, 423266]), dict(label='S0_P7pt2_d12', row=[232316, 28953, 238815]),
       dict(label='full_P6pt0_d11', row=[86170, 71919, 226580]), dict(label='full_P6pt0_d12', row=[376209, 469277, 41046]),
       dict(label='full_P6pt1_d11', row=[347334, 318883, 320901]), dict(label='full_P6pt1_d12', row=[469768, 310015, 415152])]
ALPHA, BETA = 265391, 275398
rec['inherited_rows'] = INH
rec['checks']['inherited_2x2_minors'] = dict(S0_P7pt0=fl.det_mod([[34725, 239889], [176113, 112168]]), full_P6pt0=fl.det_mod([[86170, 71919], [376209, 469277]]), expect=[104967, 171205])
rec['checks']['inherited_relation_residuals'] = [(ALPHA * r['row'][0] + BETA * r['row'][1] - r['row'][2]) % P for r in INH]

def wprime_random(rng):
    """A W'-element with all 13 coordinates uniform mod P: a, r_1..3, c_1..3, symmetric block."""
    Z = np.zeros((4, 4), dtype=np.int64)
    Z[0, :] = rng.integers(0, P, size=4); Z[1:, 0] = rng.integers(0, P, size=3)
    S = rng.integers(0, P, size=(3, 3)); S = np.triu(S); S = S + np.triu(S, 1).T
    Z[1:, 1:] = S % P
    return Z % P
rng = np.random.default_rng(rec['seed'])
rows = [dict(r) for r in INH]
new = []
for ip in range(NPOINTS):
    if left() < 15 * 0.6 + 2: rec['log'].append('deadline before point %d' % ip); break
    Z1, Z2, Z = wprime_random(rng), wprime_random(rng), wprime_random(rng)
    T = [c.column_tensor(fl.tuple_F(Z1, Z2, Z, 0, u), 5) for u in fl.NODES5]
    d11, d12 = [], []
    for name in ORDER:
        vals = [qval(VEC[name], t) for t in T]
        co = fl.vandermonde_solve(fl.NODES5, vals, [8, 9, 10, 11, 12])
        d11.append(co[11]); d12.append(co[12])
    entry = dict(point=ip, Z1=Z1.tolist(), Z2=Z2.tolist(), Z=Z.tolist(), row_d11=d11, row_d12=d12,
                 relation_residual_d11=(ALPHA * d11[0] + BETA * d11[1] - d11[2]) % P,
                 relation_residual_d12=(ALPHA * d12[0] + BETA * d12[1] - d12[2]) % P,
                 d12_ratios=dict(q7_over_q3=(d12[1] * fl.inv_mod(d12[0])) % P if d12[0] else None, n02_over_q3=(d12[2] * fl.inv_mod(d12[0])) % P if d12[0] else None, expect=[101007, 295818]))
    new.append(entry); rows.append(dict(label='flag_pt%d_d11' % ip, row=d11)); rows.append(dict(label='flag_pt%d_d12' % ip, row=d12))
    rec['new_points'] = new
    # minors with at least two degree-11 rows
    R = [r for r in rows]
    nonzero = None; n_tested = 0
    for i, j, k in itertools.combinations(range(len(R)), 3):
        if sum(1 for t in (i, j, k) if R[t]['label'].endswith('d11')) < 2: continue
        n_tested += 1
        d = fl.det_mod([R[i]['row'], R[j]['row'], R[k]['row']])
        if d: nonzero = dict(rows=[R[i]['label'], R[j]['label'], R[k]['label']], det_mod_P=d); break
    rec['minors'] = dict(rows=len(R), tested_with_two_d11=n_tested, first_nonzero=nonzero, rank_mod_P_all_rows=fl.rank_mod([r['row'] for r in R]),
                         rank_mod_P_d11_rows=fl.rank_mod([r['row'] for r in R if r['label'].endswith('d11')]))
    save('point_%d' % ip)
    if nonzero: rec['verdict'] = 'rank(C|_U) = 3 CERTIFIED: nonzero 3x3 minor of integer evaluations mod P'; save('STOP_nonzero_minor'); break
if 'verdict' not in rec:
    rec['verdict'] = 'no nonzero 3x3 minor among %d rows; %d new degree-11 functionals concordant (MEASURED only, not a ceiling)' % (len(rows), len(new))
save('done')
print(json.dumps(dict(status=rec['status'], verdict=rec['verdict'], minors=rec.get('minors'), residuals=[(e['relation_residual_d11'], e['relation_residual_d12']) for e in new],
                      evaluations=rec['evaluations'], eval_wall_s=rec['eval_wall_s'], elapsed_s=rec['elapsed_s']), indent=1, default=str))
