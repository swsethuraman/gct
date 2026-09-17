"""P7: old-arc forbidden-coefficient rows for the P6 basis, at points with all symmetric
parts zero.  By Lemma 4.1 (#alpha + #rho = d, #alpha + #kappa = d, weight = 2d - #nu and
#Sigma = 2d + #alpha - #nu), a monomial with #Sigma = 0 has #nu = 10 + #alpha; with
#nu <= lambda_1+lambda_2+lambda_3 = 12 (B19-01 Prop 3.1) only #alpha in {0,1,2} survive.
So at such points q(a -> t a) = q10 + t q11 + t^2 q12 where q11, q12 are exactly the
skew-degree 11 and 12 (forbidden) components: three nodes t = 0,1,2 suffice.
Rows are valid rows of the forbidden matrix Mf (B18-02 Claim 5.1), so a nonzero 4x4 minor
proves rank C >= 4 over Q.  Points are taken from a seeded generator; a third point is added
only if rank < 4 and time remains. Deadline 52 s."""
import hashlib, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 52.0
BASIS_FILE = sys.argv[1] if len(sys.argv) > 1 else 'p8_basis_v2.json'
b6 = json.loads((HERE / BASIS_FILE).read_text())
# A full basis is not required for a rank FLOOR of C; a partial independent set gives a valid floor.
assert len(b6['basis']) >= 1
basis = []
for b in b6['basis']:
    pi = tuple(tuple(tuple(s) for s in blk) for blk in b['pi']); rho = tuple(tuple(tuple(s) for s in blk) for blk in b['rho'])
    hp = pr.hand_plan(pi, rho); hr = pr.hand_plan(rho, pi)
    basis.append((pi, rho, hp[0], hr[0]))
OUT = HERE / 'p7_arc_S0.json'
rec = dict(cell=dict(d=5, lam=[4] * 5), prime=P, carrier_sha256=hashlib.sha256(pr.SRC.read_bytes()).hexdigest(), basis_from=BASIS_FILE, runner='paired_runner.py',
           basis_plans=[dict(order=list(b[2]), order_rev=list(b[3])) for b in basis], points=[], rows=[])


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


def qval(quad, T):
    pi, rho, order, order_rev = quad
    a, m1, f1 = pr.evaluate_P(pi, rho, T, order); b, m2, f2 = pr.evaluate_P(rho, pi, T, order_rev)
    rec['max_intermediate_seen'] = max(rec.get('max_intermediate_seen', 0), m1, m2)
    return (a + b) % P


def S0_point(rng):
    """Y_i with a, r, c, skew part random in [-3,3]; symmetric part of the 3x3 block zero."""
    Y = rng.integers(-3, 4, size=(5, 4, 4)).astype(np.int64)
    for i in range(5):
        E = Y[i, 1:, 1:]
        K = (E - E.T)  # 2 * skew part, integral
        Y[i, 1:, 1:] = K  # symmetric part zero; skew part doubled (harmless scaling)
    return Y


def scale_a(Y, t):
    Z = Y.copy() % P; Z[:, 0, 0] = (Z[:, 0, 0] * t) % P; return Z


rng = np.random.default_rng(777)
inv2 = pow(2, P - 2, P)
rows_only = []
# consistency control: the new runner must reproduce the stored P6 values at the first P6 point
Y0 = np.array(b6['points_entries'][0], dtype=np.int64) % P
T0c = c.column_tensor(Y0, 5)
stored = [a['values'][0] for a in b6['basis_attempts'] if a['added']]
recomputed = [qval(quad, T0c) for quad in basis]
rec['runner_consistency_control'] = dict(stored=stored, recomputed=recomputed, passed=(stored == recomputed), plans=rec['basis_plans'])
save('control_done')
assert stored == recomputed, (stored, recomputed)
for ip in range(3):
    if time.perf_counter() - T0 > DEADLINE - 20 and ip >= 2: break
    if ip == 2 and c.rank_mod(rows_only) >= 4: break
    Y = S0_point(rng)
    vals = {}
    for t in (0, 1, 2, 3):
        T = c.column_tensor(scale_a(Y, t), 5)
        vals[t] = [qval(triple, T) for triple in basis]
        save('in_progress')
    NB_ = len(basis)
    q10 = vals[0]
    q12 = [((vals[2][i] - 2 * vals[1][i] + vals[0][i]) * inv2) % P for i in range(NB_)]
    q11 = [(vals[1][i] - vals[0][i] - q12[i]) % P for i in range(NB_)]
    # degree-<=2 control (Lemma 4.1 + skew degree <= 12): the fourth node must be predicted exactly
    pred3 = [(q10[i] + 3 * q11[i] + 9 * q12[i]) % P for i in range(NB_)]
    rec['points'].append(dict(index=ip, entries=Y.tolist(), values_t0_t1_t2_t3=[vals[0], vals[1], vals[2], vals[3]], q10=q10, q11=q11, q12=q12,
                              degree_le_2_control_passed=(pred3 == vals[3])))
    rec['rows'].append(dict(point=ip, degree=11, row=q11)); rec['rows'].append(dict(point=ip, degree=12, row=q12))
    rows_only = [r['row'] for r in rec['rows']]
    rec['arc_rank_floor_mod_P'] = c.rank_mod(rows_only)
    save('in_progress')
NB = len(basis)
rec['independent_vectors_used'] = NB; rec['basis_status_in_source_file'] = b6['status']
# ---- transverse map C2 on the same vectors: values at K5, K5+S, K5+2S (S = x1 I4 acts on Y_1 only)
def K5_tuple(t):
    Y = np.zeros((5, 4, 4), dtype=np.int64)
    for i, (r, cc) in enumerate([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]):
        Y[i, r, cc] = 1; Y[i, cc, r] = -1
    Y[0, 2, 3] += 1; Y[0, 3, 2] += -1   # x1 also sits at (2,3)/(3,2)
    Y[0] += t * np.eye(4, dtype=np.int64)
    return Y % P
if time.perf_counter() - T0 < DEADLINE - 12:
    c2vals = {}
    for t in (0, 1, 2):
        T = c.column_tensor(K5_tuple(t), 5)
        c2vals[t] = [qval(quad, T) for quad in basis]
    rec['C2_values_at_K5_K5S_K52S'] = [c2vals[0], c2vals[1], c2vals[2]]
    rec['C2_row'] = [(112 * c2vals[1][i] - 7 * c2vals[2][i] - 177 * c2vals[0][i]) % P for i in range(NB)]
    rec['C2_rank_on_these_vectors'] = c.rank_mod([rec['C2_row']])
    rec['stacked_rank_C_and_C2_on_these_vectors'] = c.rank_mod(rows_only + [rec['C2_row']])
    save('in_progress')
minor4 = None
if rec.get('arc_rank_floor_mod_P', 0) >= 4:
    for ri in itertools.combinations(range(len(rows_only)), 4):
        for cj in itertools.combinations(range(NB), 4):
            det = det_mod([[rows_only[i][j] for j in cj] for i in ri])
            if det:
                minor4 = dict(rows=[dict(point=rec['rows'][i]['point'], degree=rec['rows'][i]['degree']) for i in ri], vector_columns=list(cj), det_mod_P=det); break
        if minor4: break
rec['arc_4x4_minor'] = minor4
save('ARC_RANK_FOUR_certified' if minor4 else 'ARC_rank_floor_below_four')
print(json.dumps({k: v for k, v in rec.items() if k != 'points'}, indent=1))
