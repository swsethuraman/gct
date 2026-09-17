"""P2: full-H carrier of M_(4^5) (d=5) and a rank floor for the old arc C.
Uses the historical b18_02_carrier.py read-only (tensor network mod P=2^19-1).
Certificates: basis matrix + explicit 5x5 minor; forbidden-coefficient matrix + explicit 4x4 minor.
Internal deadline 50 s; partial JSON is written on every stage."""
import hashlib, importlib.util, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'
spec = importlib.util.spec_from_file_location('carrier', SRC); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
np = c.np; P = c.P
T0 = time.perf_counter(); DEADLINE = 50.0
LAM = (4, 4, 4, 4, 4); D = 5; HEIGHTS = c.conjugate(LAM)  # (5,5,5,5)
SLOTS = [(j, k) for j, h in enumerate(HEIGHTS) for k in range(h)]
OUT = HERE / 'p2_carrier_arc.json'
rec = dict(cell=dict(d=D, lam=list(LAM), heights=list(HEIGHTS), slots=[list(s) for s in SLOTS]), prime=P,
           carrier_source=str(SRC), carrier_sha256=hashlib.sha256(SRC.read_bytes()).hexdigest(), stages=[])


def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1) + '\n')


def labels_for(pi, rho):
    ll = []
    for j, h in enumerate(HEIGHTS):
        lab = []
        for k in range(h): lab += [('a', (j, k)), ('b', (j, k))]
        ll.append(lab)
    ll += [[('a', s) for s in b] for b in pi]; ll += [[('b', s) for s in b] for b in rho]
    return ll


def plan_cost(pi, rho):
    _, mi1, f1 = c.Net.plan(labels_for(pi, rho)); _, mi2, f2 = c.Net.plan(labels_for(rho, pi))
    return max(mi1, mi2), f1 + f2


def tensors(Y):
    D5 = c.column_tensor(Y, 5)
    return [D5] * 4


def qval(pair, ct):
    pi, rho = pair
    a, m1, f1 = c.evaluate_pair(pi, rho, ct, None, None); b, m2, f2 = c.evaluate_pair(rho, pi, ct, None, None)
    rec['max_intermediate_seen'] = max(rec.get('max_intermediate_seen', 0), m1, m2)
    return (a + b) % P


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


# ---- candidates: local shifts first, then cheap random partitions
rng = np.random.default_rng(20260916)
cands = []
for sh in range(1, 20):
    pi, rho = c.local_pairs(SLOTS, sh); mi, fl = plan_cost(pi, rho)
    cands.append(dict(kind='local', shift=sh, pi=pi, rho=rho, maxint=mi, flops=fl))
nrand = 0
while len(cands) < 60 and nrand < 400 and time.perf_counter() - T0 < 8:
    nrand += 1
    pi = c.random_block_partition(SLOTS, rng); rho = c.random_block_partition(SLOTS, rng)
    mi, fl = plan_cost(pi, rho)
    if mi <= 4 ** 8 and fl <= 5 * 10 ** 7:
        cands.append(dict(kind='random', seed_index=nrand, pi=pi, rho=rho, maxint=mi, flops=fl))
rec['candidates_planned'] = len(cands); rec['random_partitions_tried'] = nrand
rec['stages'].append(dict(stage='planning', elapsed=time.perf_counter() - T0)); save('planning_done')

# ---- basis certification at 7 integer points (entries in [-3,3], reduced mod P)
NPTS = 7
pts = [rng.integers(-3, 4, size=(5, 4, 4)).astype(np.int64) for _ in range(NPTS)]
tc = time.perf_counter(); cols = [tensors(Y % P) for Y in pts]; rec['column_tensor_wall_s_7pts'] = time.perf_counter() - tc
basis = []; rows = []; attempted = []
for cand in cands:
    if time.perf_counter() - T0 > DEADLINE - 15: break
    te = time.perf_counter(); vals = [qval((cand['pi'], cand['rho']), ct) for ct in cols]
    added = c.rank_mod(rows + [vals]) > len(rows)
    attempted.append(dict(kind=cand['kind'], shift=cand.get('shift'), seed_index=cand.get('seed_index'), maxint=cand['maxint'], flops=cand['flops'], values=vals, added=added, wall=time.perf_counter() - te))
    if added: basis.append(cand); rows.append(vals)
    if len(basis) == 5: break
rec['basis_attempts'] = attempted
rec['basis'] = [dict(kind=b['kind'], shift=b.get('shift'), seed_index=b.get('seed_index'), pi=[[list(s) for s in blk] for blk in b['pi']], rho=[[list(s) for s in blk] for blk in b['rho']], maxint=b['maxint'], flops=b['flops']) for b in basis]
rec['points_entries'] = [Y.tolist() for Y in pts]
rec['basis_matrix_pair_by_point'] = rows; rec['basis_rank_mod_P'] = c.rank_mod(rows) if rows else 0
minor = None
if len(rows) == 5:
    for cols5 in itertools.combinations(range(NPTS), 5):
        det = det_mod([[rows[i][j] for j in cols5] for i in range(5)])
        if det: minor = dict(point_columns=list(cols5), det_mod_P=det); break
rec['basis_5x5_minor'] = minor
rec['stages'].append(dict(stage='basis', elapsed=time.perf_counter() - T0)); save('basis_done')
if len(basis) < 5:
    save('STOP_basis_not_certified'); print(json.dumps({k: v for k, v in rec.items() if k not in ('basis_attempts', 'points_entries')}, indent=1)); sys.exit(0)

# ---- old arc: forbidden skew-degree coefficients j=11..15 at 2 points, 16 nodes
unodes = list(range(1, 3 * D + 2)); udeg = list(range(0, 3 * D + 1)); forb = list(range(2 * D + 1, 3 * D + 1))
arc = []; arc_rows = []
for ip in range(2):
    if time.perf_counter() - T0 > DEADLINE - 5: break
    Y = pts[ip] % P; vals_u = []
    for u in unodes:
        ct = tensors(c.adapted_scale_u(Y, u)); vals_u.append([qval((b['pi'], b['rho']), ct) for b in basis])
    coeffs = [c.solve_vandermonde(unodes, [vu[i] for vu in vals_u], udeg) for i in range(5)]
    arc.append(dict(point=ip, u_nodes=unodes, values_by_node=vals_u, coefficients_by_vector=coeffs,
                    u1_consistency=[sum(coeffs[i]) % P == vals_u[0][i] for i in range(5)],
                    coeff_degrees_13_15=[[coeffs[i][j] for j in (13, 14, 15)] for i in range(5)]))
    for j in forb:
        arc_rows.append(dict(point=ip, degree=j, row=[coeffs[i][j] for i in range(5)]))
rec['arc'] = arc; rec['forbidden_rows'] = arc_rows
rows_only = [r['row'] for r in arc_rows]
rec['arc_rank_floor_mod_P'] = c.rank_mod(rows_only) if rows_only else 0
minor4 = None
if rec['arc_rank_floor_mod_P'] >= 4:
    for ri in itertools.combinations(range(len(rows_only)), 4):
        for cj in itertools.combinations(range(5), 4):
            det = det_mod([[rows_only[i][j] for j in cj] for i in ri])
            if det:
                minor4 = dict(rows=[dict(point=arc_rows[i]['point'], degree=arc_rows[i]['degree']) for i in ri], vector_columns=list(cj), det_mod_P=det); break
        if minor4: break
rec['arc_4x4_minor'] = minor4
rec['stages'].append(dict(stage='arc', elapsed=time.perf_counter() - T0))
save('ARC_RANK_FOUR_certified' if minor4 else ('ARC_rank_below_four_sampled' if arc_rows else 'STOP_arc_not_reached'))
print(json.dumps({k: v for k, v in rec.items() if k not in ('basis_attempts', 'points_entries', 'arc')}, indent=1))
