"""F1: full forbidden rows of q3, q7, n02 at new general points, seeking a nonzero 3x3 minor (rank_Q(C|U) = 3).

Extraction (handoff section 4): skew part nu -> u nu (b18_02_carrier.adapted_scale_u), u = 1..13, Vandermonde for
z(u) = sum_{j<=12} u^j z_j (skew degree <= 12, B19-01 Prop. 3.1), rows z_11 and z_12; node u = 14 = degree control.
Points: sealed P6 points 2 and 3 (n02's row at point 2 is reused from the sealed parent result); P6 point 4 only if
>= 21 s remain.  Rows are combined with the ten inherited rows; the pilot stops when a 3x3 minor is nonzero.
Evaluator: sealed paired_runner.py (mod P = 524287), imported in place.  Internal deadline 52 s (wrapper 60 s)."""
import hashlib, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; SESSION = HERE.parent; ROOT = SESSION.parents[2]
PILOTS_HIST = ROOT / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(PILOTS_HIST))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 52.0
OUT = SESSION / 'results/f1_new_point_minor.json'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p6 = json.loads((PILOTS_HIST / 'p6_basis.json').read_text())
n02d = json.loads((SESSION.parent / 'routeA_signfilter_20260917/certificates/n02_definition.json').read_text())
s3 = json.loads((SESSION.parent / 'routeA_signfilter_20260917/results/s3_full_forbidden_rows.json').read_text())
rec = dict(pilot='f1_new_point_minor', prime=P, cell=dict(d=5, lam=[4] * 5), column_order=['q3', 'q7', 'n02'],
           inputs_sha256={'p6_basis.json': sha(PILOTS_HIST / 'p6_basis.json'), 'paired_runner.py': sha(PILOTS_HIST / 'paired_runner.py'), 'b18_02_carrier.py': sha(pr.SRC),
                          'n02_definition.json': sha(SESSION.parent / 'routeA_signfilter_20260917/certificates/n02_definition.json'),
                          's3_full_forbidden_rows.json': sha(SESSION.parent / 'routeA_signfilter_20260917/results/s3_full_forbidden_rows.json')},
           u_nodes=list(range(1, 14)), control_node=14, degrees=list(range(13)), evaluations=0, eval_wall_s=0.0, max_intermediate=0, log=[], values={}, controls={}, points={})
def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1) + '\n')
def left(): return DEADLINE - (time.perf_counter() - T0)
def det_mod(M):
    n = len(M); A = [r[:] for r in M]; det = 1
    for k in range(n):
        piv = next((i for i in range(k, n) if A[i][k]), None)
        if piv is None: return 0
        if piv != k: A[k], A[piv] = A[piv], A[k]; det = (-det) % P
        det = det * A[k][k] % P; inv = pow(A[k][k], P - 2, P)
        for i in range(k + 1, n):
            f = A[i][k] * inv % P; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[k])]
    return det
def as_quad(pi, rho, order, order_rev):
    pi = tuple(tuple(tuple(s) for s in b) for b in pi); rho = tuple(tuple(tuple(s) for s in b) for b in rho)
    for o, (a, b) in ((order, (pi, rho)), (order_rev, (rho, pi))):
        _, mi, _ = pr._plan(a, b, tuple(o)); assert mi <= 4 ** 10
    return (pi, rho, tuple(order), tuple(order_rev))
def qval(quad, T):
    pi, rho, order, order_rev = quad; te = time.perf_counter()
    a, m1, _ = pr.evaluate_P(pi, rho, T, order); b, m2, _ = pr.evaluate_P(rho, pi, T, order_rev)
    rec['evaluations'] += 1; rec['eval_wall_s'] += time.perf_counter() - te; rec['max_intermediate'] = max(rec['max_intermediate'], m1, m2)
    return (a + b) % P
VEC = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))): VEC['q%d' % b['index']] = as_quad(b['pi'], b['rho'], order, order)
VEC['n02'] = as_quad(n02d['pi_ordered_blocks'], n02d['rho_ordered_blocks'], n02d['hand_plan_column_order'], n02d['hand_plan_column_order_transposed'])
ORDER = ['q3', 'q7', 'n02']
stored = {'q3': p6['basis_matrix_pair_by_point'][0], 'q7': p6['basis_matrix_pair_by_point'][1], 'n02': n02d['values']['P6_points_0_to_4']}
pts = [np.array(Y, dtype=np.int64) for Y in p6['points_entries']]
NODES = rec['u_nodes']; DEG = rec['degrees']
# inherited rows on (q3, q7, n02): six S0 rows (P7 points 0,1,2; degrees 11,12) and four full rows (P6 points 0,1)
INH = [dict(label='S0_P7pt0_d11', row=[34725, 239889, 380115]), dict(label='S0_P7pt0_d12', row=[176113, 112168, 44818]),
       dict(label='S0_P7pt1_d11', row=[163934, 316261, 169076]), dict(label='S0_P7pt1_d12', row=[190461, 231336, 338217]),
       dict(label='S0_P7pt2_d11', row=[395778, 379744, 423266]), dict(label='S0_P7pt2_d12', row=[232316, 28953, 238815]),
       dict(label='full_P6pt0_d11', row=[86170, 71919, 226580]), dict(label='full_P6pt0_d12', row=[376209, 469277, 41046]),
       dict(label='full_P6pt1_d11', row=[347334, 318883, 320901]), dict(label='full_P6pt1_d12', row=[469768, 310015, 415152])]
rec['inherited_rows'] = INH
rec['controls']['inherited_2x2_minors'] = dict(S0_P7pt0=det_mod([[34725, 239889], [176113, 112168]]), full_P6pt0=det_mod([[86170, 71919], [376209, 469277]]), expect=[104967, 171205])
ALPHA, BETA = 265391, 275398
rec['controls']['inherited_rows_relation_residuals'] = [(ALPHA * r['row'][0] + BETA * r['row'][1] - r['row'][2]) % P for r in INH]
rec['controls']['corrupted_relation_rejected'] = any(((ALPHA + 1) * r['row'][0] + BETA * r['row'][1] - r['row'][2]) % P for r in INH)
rows = [dict(r) for r in INH]
def minors_search():
    R = [r['row'] for r in rows]
    rec['combined_rank_mod_P'] = c.rank_mod(R)
    for ri in itertools.combinations(range(len(R)), 3):
        d = det_mod([R[i] for i in ri])
        if d:
            rec['nonzero_3x3_minor'] = dict(rows=[rows[i]['label'] for i in ri], matrix=[R[i] for i in ri], det_mod_P=d); return True
    rec['nonzero_3x3_minor'] = None; return False
save('start')
def do_point(ip, names, control):
    key = 'P6pt%d' % ip; rec['points'][key] = rec['points'].get(key, {})
    tensors = {}
    for name in names:
        if left() < 13 * 0.5 + 1.0: rec['log'].append('deadline before %s at point %d' % (name, ip)); return False
        vals = []
        for u in NODES:
            if u not in tensors: tensors[u] = c.column_tensor(c.adapted_scale_u(pts[ip], u), 5)
            vals.append(qval(VEC[name], tensors[u])); rec['values']['%s_pt%d' % (name, ip)] = vals; save('in_progress')
        co = c.solve_vandermonde(NODES, vals, DEG)
        rec['values']['%s_pt%d_coeffs_u0_to_u12' % (name, ip)] = co
        rec['controls']['u1_equals_stored_%s_pt%d' % (name, ip)] = dict(u1=vals[0], stored=stored[name][ip], passed=(vals[0] == stored[name][ip]))
        rec['points'][key][name] = dict(z11=co[11], z12=co[12])
        if control and left() > 1.5:
            T14 = c.column_tensor(c.adapted_scale_u(pts[ip], 14), 5); v14 = qval(VEC[name], T14)
            pred = sum(cf * pow(14, e, P) for e, cf in zip(DEG, co)) % P
            rec['controls']['degree_le_12_%s_pt%d' % (name, ip)] = dict(value_u14=v14, predicted=pred, passed=(v14 == pred))
            # corrupted extraction: perturb node u = 3 by +1 and show the u = 14 prediction fails
            bad = list(vals); bad[2] = (bad[2] + 1) % P; cob = c.solve_vandermonde(NODES, bad, DEG)
            rec['controls']['corrupted_node_rejected_%s_pt%d' % (name, ip)] = (sum(cf * pow(14, e, P) for e, cf in zip(DEG, cob)) % P != v14)
        save('in_progress')
    return True
# ---- point 2: q3, q7 new; n02 reused from the sealed parent result
n02_pt2 = s3['values']['n02_pt2_coeffs_u0_to_u12']
rec['points']['P6pt2'] = {'n02': dict(z11=n02_pt2[11], z12=n02_pt2[12], source='routeA_signfilter_20260917/results/s3_full_forbidden_rows.json (sealed)')}
ok = do_point(2, ['q3', 'q7'], control=False)
if ok:
    for deg in (11, 12):
        rows.append(dict(label='full_P6pt2_d%d' % deg, row=[rec['points']['P6pt2'][n]['z%d' % deg] for n in ORDER]))
    found = minors_search(); save('point2_done')
    if found: rec['stopped_at'] = 'point 2'; save('NONZERO_3x3_MINOR'); print(json.dumps(rec['nonzero_3x3_minor'])); sys.exit(0)
# ---- point 3: all three, with the degree control
ok = do_point(3, ORDER, control=True)
if ok and all(n in rec['points']['P6pt3'] for n in ORDER):
    for deg in (11, 12):
        rows.append(dict(label='full_P6pt3_d%d' % deg, row=[rec['points']['P6pt3'][n]['z%d' % deg] for n in ORDER]))
    found = minors_search(); save('point3_done')
    if found: rec['stopped_at'] = 'point 3'; save('NONZERO_3x3_MINOR'); print(json.dumps(rec['nonzero_3x3_minor'])); sys.exit(0)
# ---- point 4 only if >= 21 s remain
if left() >= 21.0:
    ok = do_point(4, ORDER, control=False)
    if ok and all(n in rec['points']['P6pt4'] for n in ORDER):
        for deg in (11, 12):
            rows.append(dict(label='full_P6pt4_d%d' % deg, row=[rec['points']['P6pt4'][n]['z%d' % deg] for n in ORDER]))
        found = minors_search(); save('point4_done')
        if found: rec['stopped_at'] = 'point 4'; save('NONZERO_3x3_MINOR'); print(json.dumps(rec['nonzero_3x3_minor'])); sys.exit(0)
else:
    rec['log'].append('point 4 skipped: %.1f s left < 21 s' % left())
rec['new_rows'] = [r for r in rows if r['label'] not in {i['label'] for i in INH}]
rec['new_rows_relation_residuals'] = [(ALPHA * r['row'][0] + BETA * r['row'][1] - r['row'][2]) % P for r in rec['new_rows']]
rec['wall_per_evaluation_s'] = rec['eval_wall_s'] / max(rec['evaluations'], 1)
save('no_nonzero_3x3_minor')
print(json.dumps({k: v for k, v in rec.items() if k not in ('values', 'inherited_rows')}, indent=1)[:5000])
