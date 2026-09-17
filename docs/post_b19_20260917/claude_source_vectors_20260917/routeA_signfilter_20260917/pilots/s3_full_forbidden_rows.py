"""S3: FULL forbidden-component rows (not the S0 slice) for q3, q7, n02 at general points.

At a general point Y (nonzero symmetric parts), scale the skew part nu of the lower-right 3x3 block of every
Y_i by u (b18_02_carrier.adapted_scale_u).  By B18-02 Lemma 4.1 / B19-01 Prop. 3.1 every monomial of z in M
has skew degree #nu <= lambda_1+lambda_2+lambda_3 = 12, so z(Y(u)) = sum_{j=0}^{12} u^j z_j(Y) and the
forbidden components are z_11(Y), z_12(Y) (skew degree 2d+1 = 11 and 12).  Thirteen nodes u = 1..13
determine them exactly (Vandermonde mod P); a fourteenth node u = 14 is a degree control (must be
predicted exactly).  Rows (point, degree) on columns (q3, q7, n02) are actual rows of the forbidden
matrix; their modular rank is a characteristic-zero floor for rank C on span(q3, q7, n02).
Points: sealed P6 points 0, 1 (and 2 as best effort).  The u = 1 node must reproduce the stored P6
values (control).  Internal deadline 52 s (wrapper 60 s); JSON saved after every evaluation."""
import hashlib, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
ROOT = SESSION.parents[2]
PILOTS_HIST = ROOT / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(PILOTS_HIST))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 52.0
OUT = SESSION / 'results/s3_full_forbidden_rows.json'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
cand_doc = json.loads((SESSION / 'certificates/candidates_selected.json').read_text())
s2 = json.loads((SESSION / 'results/s2_certify_n02_and_new.json').read_text())
p6 = json.loads((PILOTS_HIST / 'p6_basis.json').read_text())
rec = dict(pilot='s3_full_forbidden_rows', cell=dict(d=5, lam=[4] * 5), prime=P,
           inputs_sha256={'p6_basis.json': sha(PILOTS_HIST / 'p6_basis.json'), 'paired_runner.py': sha(PILOTS_HIST / 'paired_runner.py'),
                          'b18_02_carrier.py': sha(pr.SRC), 'candidates_selected.json': sha(SESSION / 'certificates/candidates_selected.json'),
                          's2_certify_n02_and_new.json': sha(SESSION / 'results/s2_certify_n02_and_new.json')},
           u_nodes=list(range(1, 14)), control_node=14, degrees=list(range(13)), forbidden_degrees=[11, 12],
           evaluations=0, eval_wall_s=0.0, max_intermediate_seen=0, log=[], values={}, rows=[], controls={})

def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1) + '\n')

def det_mod(M):
    n = len(M); A = [r[:] for r in M]; det = 1
    for k in range(n):
        piv = next((i for i in range(k, n) if A[i][k]), None)
        if piv is None: return 0
        if piv != k: A[k], A[piv] = A[piv], A[k]; det = (-det) % P
        det = det * A[k][k] % P; inv = pow(A[k][k], P - 2, P)
        for i in range(k + 1, n):
            f = A[i][k] * inv % P
            A[i] = [(x - f * y) % P for x, y in zip(A[i], A[k])]
    return det

def as_quad(pi, rho, order, order_rev):
    pi = tuple(tuple(tuple(s) for s in blk) for blk in pi); rho = tuple(tuple(tuple(s) for s in blk) for blk in rho)
    for o, (ppi, prho) in ((order, (pi, rho)), (order_rev, (rho, pi))):
        steps, mi, fl = pr._plan(ppi, prho, tuple(o)); assert mi <= 4 ** 10
    return (pi, rho, tuple(order), tuple(order_rev))

def qval(quad, T):
    pi, rho, order, order_rev = quad
    te = time.perf_counter()
    a, m1, f1 = pr.evaluate_P(pi, rho, T, order); b, m2, f2 = pr.evaluate_P(rho, pi, T, order_rev)
    rec['evaluations'] += 1; rec['eval_wall_s'] += time.perf_counter() - te
    rec['max_intermediate_seen'] = max(rec['max_intermediate_seen'], m1, m2)
    return (a + b) % P

def time_left(): return DEADLINE - (time.perf_counter() - T0)

vecs = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
    vecs['q%d' % b['index']] = as_quad(b['pi'], b['rho'], order, order)
n02d = next(cd for cd in cand_doc['candidates'] if cd['name'] == 'n02')
vecs['n02'] = as_quad(n02d['pi'], n02d['rho'], n02d['order'], n02d['order_rev'])
ORDER = ['q3', 'q7', 'n02']
stored_u1 = {'q3': p6['basis_matrix_pair_by_point'][0], 'q7': p6['basis_matrix_pair_by_point'][1], 'n02': s2['independence_P6']['matrix_rows_by_point'][3]}
pts6 = [np.array(Y, dtype=np.int64) for Y in p6['points_entries']]
NODES = rec['u_nodes']; DEG = rec['degrees']
tensors = {}
def tensor(ip, u):
    if (ip, u) not in tensors: tensors[(ip, u)] = c.column_tensor(c.adapted_scale_u(pts6[ip], u), 5)
    return tensors[(ip, u)]

def rows_for_point(ip, names, with_control):
    for name in names:
        if time_left() < 13 * 0.5 + 1: rec['log'].append('deadline before %s at point %d' % (name, ip)); return False
        vals = []
        for u in NODES:
            vals.append(qval(vecs[name], tensor(ip, u))); rec['values']['%s_pt%d' % (name, ip)] = vals; save('in_progress')
        coeffs = c.solve_vandermonde(NODES, vals, DEG)
        rec['values']['%s_pt%d_coeffs_u0_to_u12' % (name, ip)] = coeffs
        rec['controls']['u1_equals_stored_%s_pt%d' % (name, ip)] = dict(u1=vals[0], stored=stored_u1[name][ip], passed=(vals[0] == stored_u1[name][ip]))
        if with_control and time_left() > 1.5:
            v14 = qval(vecs[name], tensor(ip, 14)); pred = sum(cf * pow(14, e_, P) for e_, cf in zip(DEG, coeffs)) % P
            rec['controls']['degree_le_12_%s_pt%d' % (name, ip)] = dict(value_u14=v14, predicted=pred, passed=(v14 == pred))
        save('in_progress')
    return True

def assemble():
    rows = []
    for ip in (0, 1, 2):
        if all(('%s_pt%d_coeffs_u0_to_u12' % (n, ip)) in rec['values'] for n in ORDER):
            for deg in (11, 12):
                rows.append(dict(point=ip, degree=deg, row=[rec['values']['%s_pt%d_coeffs_u0_to_u12' % (n, ip)][deg] for n in ORDER]))
    rec['rows'] = rows; rec['columns'] = ORDER
    R = [r['row'] for r in rows]
    rec['full_forbidden_rank_mod_P_q3_q7_n02'] = c.rank_mod(R) if R else None
    if R and len(R) >= 3:
        for ri in itertools.combinations(range(len(R)), 3):
            d = det_mod([R[i] for i in ri])
            if d:
                rec['nonzero_3x3_minor'] = dict(rows=[dict(point=rows[i]['point'], degree=rows[i]['degree']) for i in ri], det_mod_P=d); break
        else:
            rec['nonzero_3x3_minor'] = None
    # S0-slice comparison for the record: relation column n02 = alpha q3 + beta q7 on full rows?
    if R and len(R) >= 2 and c.rank_mod([r[:2] for r in R]) == 2:
        A = [r[:2] for r in R[:2]]; b = [r[2] for r in R[:2]]
        det = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % P
        if det:
            inv = pow(det, P - 2, P)
            al = ((A[1][1] * b[0] - A[0][1] * b[1]) * inv) % P; be = ((A[0][0] * b[1] - A[1][0] * b[0]) * inv) % P
            rec['n02_relation_on_full_rows'] = dict(alpha=al, beta=be, residuals=[(al * r[0] + be * r[1] - r[2]) % P for r in R],
                                                    S0_slice_alpha_beta=[265391, 275398])

ok = rows_for_point(0, ORDER, with_control=True); assemble(); save('point0_done')
if ok: ok = rows_for_point(1, ['n02', 'q3', 'q7'], with_control=False); assemble(); save('point1_done')
if ok: rows_for_point(2, ['n02', 'q3', 'q7'], with_control=False); assemble(); save('point2_done')
rec['wall_per_evaluation_s'] = rec['eval_wall_s'] / max(rec['evaluations'], 1)
r_ = rec.get('full_forbidden_rank_mod_P_q3_q7_n02')
save('FULL_ROWS_rank_%s' % r_)
print(json.dumps({k: v for k, v in rec.items() if k not in ('log', 'values')}, indent=1)[:5000])
