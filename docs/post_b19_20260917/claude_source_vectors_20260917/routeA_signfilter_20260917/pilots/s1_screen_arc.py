"""S1: screen sign-filtered candidate source vectors n00..n09 on the S0 arc rows.

At the sealed P7 symmetric-part-zero points (p7_arc_S0.json), scaling a = Y[:,0,0] by t gives
q(t) = q10 + t q11 + t^2 q12 with q11, q12 the S0-restricted forbidden components (B18-02 Lemma 4.1,
#Sigma = 0 => #nu = 10 + #alpha, #nu <= 12).  Rows (point, degree) on columns (q3, q7, n_a, n_b):
a nonzero 4x4 modular minor of these actual forbidden rows proves rank C >= 4 over Q.
Runner: sealed paired_runner.py (hand-ordered dense contraction, mod P = 524287), imported in place.
Internal deadline 50 s (wrapper 60 s); JSON saved after every evaluation."""
import hashlib, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent          # .../routeA_signfilter_20260917/pilots
SESSION = HERE.parent
ROOT = SESSION.parents[2]                        # .../gct-gpt
PILOTS_HIST = ROOT / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(PILOTS_HIST))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 50.0
OUT = SESSION / 'results/s1_screen_arc.json'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
cand_doc = json.loads((SESSION / 'certificates/candidates_selected.json').read_text())
p7 = json.loads((PILOTS_HIST / 'p7_arc_S0.json').read_text())
p6 = json.loads((PILOTS_HIST / 'p6_basis.json').read_text())
rec = dict(pilot='s1_screen_arc', cell=dict(d=5, lam=[4] * 5), prime=P,
           inputs_sha256={'p7_arc_S0.json': sha(PILOTS_HIST / 'p7_arc_S0.json'), 'p6_basis.json': sha(PILOTS_HIST / 'p6_basis.json'),
                          'paired_runner.py': sha(PILOTS_HIST / 'paired_runner.py'), 'b18_02_carrier.py': sha(pr.SRC),
                          'candidates_selected.json': sha(SESSION / 'certificates/candidates_selected.json')},
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
    hp = pr.hand_plan(pi, rho); hr = pr.hand_plan(rho, pi)
    assert list(hp[0]) == list(order) and list(hr[0]) == list(order_rev), (hp, hr, order, order_rev)
    assert max(hp[1], hr[1]) <= 4 ** 10
    return (pi, rho, tuple(order), tuple(order_rev))

def qval(quad, T):
    pi, rho, order, order_rev = quad
    te = time.perf_counter()
    a, m1, f1 = pr.evaluate_P(pi, rho, T, order); b, m2, f2 = pr.evaluate_P(rho, pi, T, order_rev)
    rec['evaluations'] += 1; rec['eval_wall_s'] += time.perf_counter() - te
    rec['max_intermediate_seen'] = max(rec['max_intermediate_seen'], m1, m2)
    return (a + b) % P

def scale_a(Y, t):
    Z = Y.copy() % P; Z[:, 0, 0] = (Z[:, 0, 0] * t) % P; return Z

def time_left(): return DEADLINE - (time.perf_counter() - T0)

# known vectors (sealed): q3 = P6 index 3, q7 = P6 index 7
known = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
    known['q%d' % b['index']] = as_quad(b['pi'], b['rho'], order, order)
assert list(known) == ['q3', 'q7']
cands = {cd['name']: as_quad(cd['pi'], cd['rho'], cd['order'], cd['order_rev']) for cd in cand_doc['candidates']}
PLANNED = [cd['name'] for cd in cand_doc['candidates']][:10]
rec['planned'] = PLANNED
pts = [np.array(pt['entries'], dtype=np.int64) for pt in p7['points']]
inv2 = pow(2, P - 2, P)

# ---- runner consistency control at P7 point 0, t = 0 (stored values_t0 of q3, q7)
tensors = {}
def tensor(ip, t):
    if (ip, t) not in tensors: tensors[(ip, t)] = c.column_tensor(scale_a(pts[ip], t), 5)
    return tensors[(ip, t)]
stored0 = p7['points'][0]['values_t0_t1_t2_t3'][0]
recomputed0 = [qval(known['q3'], tensor(0, 0)), qval(known['q7'], tensor(0, 0))]
rec['runner_consistency_control'] = dict(point=0, t=0, stored=stored0, recomputed=recomputed0, passed=(stored0 == recomputed0))
save('control_done')
assert stored0 == recomputed0, (stored0, recomputed0)

# ---- stage A: point 0, t = 0,1,2 for n00..n09
rec['point0'] = {}; survivors = []
for name in PLANNED:
    if time_left() < 3 * 0.8 + 1: rec['log'].append('deadline before %s at point 0' % name); break
    vals = {}
    for t in (0, 1, 2):
        vals[t] = qval(cands[name], tensor(0, t)); save('stageA')
    q10 = vals[0]; q12 = ((vals[2] - 2 * vals[1] + vals[0]) * inv2) % P; q11 = (vals[1] - vals[0] - q12) % P
    alive = (q11, q12) != (0, 0)
    rec['point0'][name] = dict(values_t0_t1_t2=[vals[0], vals[1], vals[2]], q10=q10, q11=q11, q12=q12, nonzero_at_t0=(q10 != 0), forbidden_nonzero=alive)
    if alive: survivors.append(name)
    save('stageA')
rec['survivors_after_point0'] = survivors

# ---- stage B: point 1 for survivors
rec['point1'] = {}
for name in survivors:
    if time_left() < 3 * 0.8 + 1: rec['log'].append('deadline before %s at point 1' % name); break
    vals = {}
    for t in (0, 1, 2):
        vals[t] = qval(cands[name], tensor(1, t)); save('stageB')
    q10 = vals[0]; q12 = ((vals[2] - 2 * vals[1] + vals[0]) * inv2) % P; q11 = (vals[1] - vals[0] - q12) % P
    rec['point1'][name] = dict(values_t0_t1_t2=[vals[0], vals[1], vals[2]], q10=q10, q11=q11, q12=q12)
    save('stageB')

# ---- minors: rows (pt0 d11, pt0 d12, pt1 d11, pt1 d12); columns q3, q7 (stored rows) + candidates with both points
def stored_row(ip, deg): return next(r['row'] for r in p7['rows'] if r['point'] == ip and r['degree'] == deg)
have_both = [n for n in survivors if n in rec['point1']]
cols = ['q3', 'q7'] + have_both
rows = []
for ip, key in ((0, 'point0'), (1, 'point1')):
    for deg, fld in ((11, 'q11'), (12, 'q12')):
        rows.append(stored_row(ip, deg) + [rec[key][n][fld] for n in have_both])
rec['arc_rows_pts01'] = dict(columns=cols, row_labels=['pt0_deg11', 'pt0_deg12', 'pt1_deg11', 'pt1_deg12'], rows=rows)
rec['arc_rank_pts01_mod_P'] = c.rank_mod(rows) if rows and have_both else None
minors = []
for a_, b_ in itertools.combinations(range(2, len(cols)), 2):
    d = det_mod([[r[0], r[1], r[a_], r[b_]] for r in rows])
    minors.append(dict(columns=[cols[0], cols[1], cols[a_], cols[b_]], det_mod_P=d))
rec['minors_4x4_pts01'] = minors
nz = [m for m in minors if m['det_mod_P']]
rec['nonzero_4x4_minors'] = nz
save('minors_done')

# ---- remaining time: t = 3 degree control at point 0 for survivors (prediction q10 + 3 q11 + 9 q12)
rec['degree_control_point0'] = {}
for name in survivors:
    if time_left() < 0.8 + 0.5: rec['log'].append('deadline before t=3 control for %s' % name); break
    v3 = qval(cands[name], tensor(0, 3))
    d = rec['point0'][name]; pred = (d['q10'] + 3 * d['q11'] + 9 * d['q12']) % P
    rec['degree_control_point0'][name] = dict(value_t3=v3, predicted=pred, passed=(v3 == pred))
    save('controls')
rec['wall_per_evaluation_s'] = rec['eval_wall_s'] / max(rec['evaluations'], 1)
save('ARC_RANK_FOUR_minor_found' if nz else 'no_rank_four_minor_on_pts01')
print(json.dumps({k: v for k, v in rec.items() if k not in ('log',)}, indent=1)[:6000])
