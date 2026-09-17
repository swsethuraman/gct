"""S2: certify the new source direction n02 and test the last two candidates m00, m01.

Work items in priority order (deadline-aware, JSON saved after every evaluation):
 1. cross-pilot consistency: n02 at P7 point 0, t=0 must reproduce pilot 1 (53303); q3 at K5 must be 94237.
 2. n02 at the five sealed P6 points -> 4x5 matrix (q3, q7, e, n02), modular rank / 4x4 minor (independence).
 3. n02 at P7 point 2 (t = 0..3) and t = 3 at point 1: rows at all three points + degree controls.
 4. m00, m01 at P7 points 0 and 1 (t = 0,1,2): arc rows; all 4x4 minors on (q3, q7, x, y) and with n02.
 5. n02 at the seven pencil points K5, K5+S1, K5+2S1, K5+S2, K5+2S2, K5+S4, K5+2S4: C2, C4 rows.
 6. corruption control: S0 extraction of q3 at a point with nonzero symmetric parts (P6 point 0) must FAIL
    the fourth-node degree control (z(t) has degree up to 5 there).
 7. transpose-convention control: P_{pi,rho}(Y^T) == P_{rho,pi}(Y) for n02 at P6 point 0.
Conventions: SOURCE_HANDOFF.md section 1; runner = sealed paired_runner.py (mod P = 524287)."""
import hashlib, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
ROOT = SESSION.parents[2]
PILOTS_HIST = ROOT / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(PILOTS_HIST))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 50.0
OUT = SESSION / 'results/s2_certify_n02_and_new.json'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
cand_doc = json.loads((SESSION / 'certificates/candidates_selected.json').read_text())
s1 = json.loads((SESSION / 'results/s1_screen_arc.json').read_text())
p7 = json.loads((PILOTS_HIST / 'p7_arc_S0.json').read_text())
p6 = json.loads((PILOTS_HIST / 'p6_basis.json').read_text())
rec = dict(pilot='s2_certify_n02_and_new', cell=dict(d=5, lam=[4] * 5), prime=P,
           inputs_sha256={'p7_arc_S0.json': sha(PILOTS_HIST / 'p7_arc_S0.json'), 'p6_basis.json': sha(PILOTS_HIST / 'p6_basis.json'),
                          'paired_runner.py': sha(PILOTS_HIST / 'paired_runner.py'), 'b18_02_carrier.py': sha(pr.SRC),
                          'candidates_selected.json': sha(SESSION / 'certificates/candidates_selected.json'),
                          's1_screen_arc.json': sha(SESSION / 'results/s1_screen_arc.json')},
           evaluations=0, eval_wall_s=0.0, max_intermediate_seen=0, log=[])

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
    hp = pr.hand_plan(pi, rho, orders=tuple(itertools.permutations(range(4)))); hr = pr.hand_plan(rho, pi, orders=tuple(itertools.permutations(range(4))))
    assert hp is not None and hr is not None and max(hp[1], hr[1]) <= 4 ** 10
    # use the recorded orders (they must be admissible plans with maxint <= 4^10)
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

def halfval(pi, rho, T, order):
    te = time.perf_counter()
    a, m1, f1 = pr.evaluate_P(pi, rho, T, order)
    rec['evaluations'] += 0.5; rec['eval_wall_s'] += time.perf_counter() - te
    rec['max_intermediate_seen'] = max(rec['max_intermediate_seen'], m1)
    return a % P

def scale_a(Y, t):
    Z = Y.copy() % P; Z[:, 0, 0] = (Z[:, 0, 0] * t) % P; return Z

def time_left(): return DEADLINE - (time.perf_counter() - T0)

known = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
    known['q%d' % b['index']] = as_quad(b['pi'], b['rho'], order, order)
cands = {cd['name']: as_quad(cd['pi'], cd['rho'], cd['order'], cd['order_rev']) for cd in cand_doc['candidates']}
n02 = cands['n02']; NEW = ['m00', 'm01']
pts7 = [np.array(pt['entries'], dtype=np.int64) for pt in p7['points']]
pts6 = [np.array(Y, dtype=np.int64) for Y in p6['points_entries']]
E_P6 = [1133111758001692800, -204681391250300160, -123041748408339456, -7214659371047040, 437311725353472]  # handoff section 3, exact
E_P7 = [-103092282930268800, -205527152486400, 12248442247766400]
inv2 = pow(2, P - 2, P)
tensors = {}
def tensor(key, Y):
    if key not in tensors: tensors[key] = c.column_tensor(Y % P, 5)
    return tensors[key]

def K5_tuple(direction=None, t=0):
    Y = np.zeros((5, 4, 4), dtype=np.int64)
    for i, (r, cc) in enumerate([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]):
        Y[i, r, cc] = 1; Y[i, cc, r] = -1
    Y[0, 2, 3] += 1; Y[0, 3, 2] += -1
    if direction == 'S1': Y[0] += t * np.eye(4, dtype=np.int64)
    elif direction == 'S2': Y[1] += t * np.eye(4, dtype=np.int64)
    elif direction == 'S4': Y[0] += t * np.diag([1, 1, 0, 0]).astype(np.int64)
    return Y

# ---- 1. consistency controls
v = qval(n02, tensor(('p7', 0, 0), scale_a(pts7[0], 0)))
rec['control_n02_pilot1'] = dict(recomputed=v, pilot1=s1['point0']['n02']['values_t0_t1_t2'][0], passed=(v == s1['point0']['n02']['values_t0_t1_t2'][0]))
vk = qval(known['q3'], tensor(('K5',), K5_tuple()))
rec['control_q3_K5'] = dict(recomputed=vk, stored=94237, passed=(vk == 94237))
save('controls_1'); assert rec['control_n02_pilot1']['passed'] and rec['control_q3_K5']['passed']

# ---- 2. independence at the P6 points
n02_p6 = []
for ip in range(5):
    n02_p6.append(qval(n02, tensor(('p6', ip), pts6[ip]))); save('p6_values')
rows_q = p6['basis_matrix_pair_by_point']          # [q3 row, q7 row] over the 5 points
mat = [rows_q[0], rows_q[1], [x % P for x in E_P6], n02_p6]
rec['independence_P6'] = dict(row_order=['q3', 'q7', 'e', 'n02'], matrix_rows_by_point=mat, rank_mod_P=c.rank_mod(mat))
minors = {}
for cols in itertools.combinations(range(5), 4):
    d = det_mod([[r[j] for j in cols] for r in mat])
    if d: minors[str(list(cols))] = d
rec['independence_P6']['nonzero_4x4_minors_by_point_columns'] = minors
save('independence_done')

# ---- 3. n02 at point 2 (t = 0..3) and t = 3 at point 1
def s0_extract(vals):
    q10 = vals[0]; q12 = ((vals[2] - 2 * vals[1] + vals[0]) * inv2) % P; q11 = (vals[1] - vals[0] - q12) % P
    return q10, q11, q12
n02_pts = {0: dict(values=s1['point0']['n02']['values_t0_t1_t2'] + [s1['degree_control_point0']['n02']['value_t3']]),
           1: dict(values=s1['point1']['n02']['values_t0_t1_t2'] + [None]), 2: dict(values=[None] * 4)}
for t in (0, 1, 2, 3):
    n02_pts[2]['values'][t] = qval(n02, tensor(('p7', 2, t), scale_a(pts7[2], t))); save('point2')
n02_pts[1]['values'][3] = qval(n02, tensor(('p7', 1, 3), scale_a(pts7[1], 3))); save('point1_t3')
for ip in (0, 1, 2):
    vals = n02_pts[ip]['values']; q10, q11, q12 = s0_extract(vals)
    n02_pts[ip].update(q10=q10, q11=q11, q12=q12, degree_le_2_control_passed=((q10 + 3 * q11 + 9 * q12) % P == vals[3]))
rec['n02_S0_points'] = n02_pts
def stored_row(ip, deg): return next(r['row'] for r in p7['rows'] if r['point'] == ip and r['degree'] == deg)
rows6 = []
for ip in (0, 1, 2):
    for deg, fld in ((11, 'q11'), (12, 'q12')):
        rows6.append(stored_row(ip, deg) + [n02_pts[ip][fld]])
rec['arc_rows_3pts_q3_q7_n02'] = dict(columns=['q3', 'q7', 'n02'], rows=rows6, rank_mod_P=c.rank_mod(rows6))
save('n02_rows_done')

# ---- 4. m00, m01 at points 0, 1 (t = 0,1,2) then minors
rec['new'] = {}
for name in NEW:
    rec['new'][name] = {}
    for ip in (0, 1):
        if time_left() < 3 * 0.6 + 1: rec['log'].append('deadline before %s point %d' % (name, ip)); break
        vals = [qval(cands[name], tensor(('p7', ip, t), scale_a(pts7[ip], t))) for t in (0, 1, 2)]
        q10, q11, q12 = s0_extract(vals)
        rec['new'][name][ip] = dict(values_t0_t1_t2=vals, q10=q10, q11=q11, q12=q12)
        save('new_candidates')
have = [n for n in NEW if 0 in rec['new'][n] and 1 in rec['new'][n]]
cols = ['q3', 'q7', 'n02'] + have
rows4 = []
for ip in (0, 1):
    for deg, fld in ((11, 'q11'), (12, 'q12')):
        rows4.append(stored_row(ip, deg) + [n02_pts[ip][fld]] + [rec['new'][n][ip][fld] for n in have])
rec['arc_rows_pts01_all'] = dict(columns=cols, rows=rows4, rank_mod_P=c.rank_mod(rows4))
mins = []
for cc in itertools.combinations(range(len(cols)), 4):
    d = det_mod([[r[j] for j in cc] for r in rows4])
    mins.append(dict(columns=[cols[j] for j in cc], det_mod_P=d))
rec['minors_4x4_pts01_all'] = mins
nz = [m for m in mins if m['det_mod_P']]
rec['nonzero_4x4_minors'] = nz
save('minors_done')
# degree controls (t = 3) for new candidates that are nonzero
rec['degree_control_new'] = {}
for name in have:
    for ip in (0, 1):
        if time_left() < 0.6 + 0.5: rec['log'].append('deadline before t=3 %s pt %d' % (name, ip)); break
        d = rec['new'][name][ip]
        if (d['q10'], d['q11'], d['q12']) == (0, 0, 0): continue
        v3 = qval(cands[name], tensor(('p7', ip, 3), scale_a(pts7[ip], 3)))
        rec['degree_control_new']['%s_pt%d' % (name, ip)] = dict(value_t3=v3, predicted=(d['q10'] + 3 * d['q11'] + 9 * d['q12']) % P, passed=(v3 == (d['q10'] + 3 * d['q11'] + 9 * d['q12']) % P))
        save('degree_controls_new')

# ---- 5. transverse rows for n02
pencil = [('K5', None, 0), ('K5+S1', 'S1', 1), ('K5+2S1', 'S1', 2), ('K5+S2', 'S2', 1), ('K5+2S2', 'S2', 2), ('K5+S4', 'S4', 1), ('K5+2S4', 'S4', 2)]
tv = {}
for label, dirn, t in pencil:
    if time_left() < 0.6 + 0.5: rec['log'].append('deadline before pencil %s' % label); break
    tv[label] = qval(n02, tensor(('pencil', label), K5_tuple(dirn, t))); save('transverse')
rec['n02_pencil_values'] = tv
stored = {'q3': dict(zip([p[0] for p in pencil], [94237, 458787, 323691, 372809, 299315, 196638, 503841])),
          'q7': dict(zip([p[0] for p in pencil], [491460, 393135, 229099, 122730, 228736, 458687, 360368]))}
if len(tv) == 7:
    def rows_T(z):
        C2 = (112 * z['K5+S1'] - 7 * z['K5+2S1'] - 177 * z['K5']) % P
        C4a = (-27 * z['K5'] - 60 * z['K5+S1'] + 15 * z['K5+2S1'] + 368 * z['K5+S2'] - 92 * z['K5+2S2']) % P
        C4b = (-2211 * z['K5'] - 252 * z['K5+S1'] + 63 * z['K5+2S1'] + 2576 * z['K5+S4'] - 644 * z['K5+2S4']) % P
        return [C2, C4a, C4b]
    T = {k: rows_T(v) for k, v in list(stored.items()) + [('n02', tv)]}
    rec['transverse_rows'] = dict(row_order=['C2', 'C4_S1S2', 'C4_S1S4'], columns=['q3', 'q7', 'n02'], values={k: v for k, v in T.items()},
                                  stored_row_check=dict(q3=T['q3'], q7=T['q7'], expected_C2=[456851, 3402], expected_C4a=[30271, 137059], expected_C4b=[120670, 19278]))
    M3 = [[T['q3'][i], T['q7'][i], T['n02'][i]] for i in range(3)]
    rec['transverse_rows']['matrix_rows_C2_C4a_C4b_cols_q3_q7_n02'] = M3
    rec['transverse_rows']['det_3x3_mod_P'] = det_mod(M3)
    rec['transverse_rows']['rank_mod_P'] = c.rank_mod(M3)
    save('transverse_done')

# ---- 6. corruption control: S0 extraction at a non-S0 point must fail the fourth-node control
if time_left() > 4 * 0.6 + 1:
    Y = pts6[0]
    vals = [qval(known['q3'], tensor(('p6_scaled', t), scale_a(Y, t))) for t in (0, 1, 2, 3)]
    q10, q11, q12 = s0_extract(vals)
    rec['corruption_control_nonS0_point'] = dict(point='P6 point 0 (nonzero symmetric parts)', vector='q3', values_t0_t1_t2_t3=vals,
                                                 fourth_node_predicted=(q10 + 3 * q11 + 9 * q12) % P, rejected_as_required=((q10 + 3 * q11 + 9 * q12) % P != vals[3]))
    save('corruption_done')

# ---- 7. transpose-convention control
if time_left() > 1.5:
    Y = pts6[0]; YT = np.transpose(Y, (0, 2, 1)).copy()
    pi, rho, order, order_rev = n02
    a = halfval(pi, rho, tensor(('p6T', 0), YT), order); b = halfval(rho, pi, tensor(('p6', 0), Y), order_rev)
    rec['transpose_convention_control'] = dict(P_pi_rho_at_YT=a, P_rho_pi_at_Y=b, passed=(a == b))
    save('transpose_done')
rec['wall_per_evaluation_s'] = rec['eval_wall_s'] / max(rec['evaluations'], 1)
save('ARC_RANK_FOUR_minor_found' if nz else 'no_rank_four_minor')
print(json.dumps({k: v for k, v in rec.items() if k not in ('log', 'minors_4x4_pts01_all')}, indent=1)[:7000])
