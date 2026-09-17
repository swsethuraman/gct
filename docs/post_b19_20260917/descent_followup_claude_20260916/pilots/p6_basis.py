"""P6: basis of M_(4^5) from same-pairing paired-columns contractions with the hand-ordered
runner (paired_runner.py). Certificate: 5x5 modular minor at 5 explicit integer points; s = 5 (P1).
Deadline 50 s; JSON saved after every candidate."""
import hashlib, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 50.0
OUT = HERE / 'p6_basis.json'
rec = dict(cell=dict(d=5, lam=[4] * 5, heights=[5] * 4), prime=P, carrier_sha256=hashlib.sha256(pr.SRC.read_bytes()).hexdigest(),
           runner='paired_runner.py', stages=[])


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


rng = np.random.default_rng(20260916)
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
cands = []
for n in range(30):
    prg = PAIRINGS[n % 3]
    cands.append(dict(index=n, pairing=prg, pi=pr.paired_partition(rng, prg), rho=pr.paired_partition(rng, prg)))
NPTS = 5
pts = [rng.integers(-3, 4, size=(5, 4, 4)).astype(np.int64) for _ in range(NPTS)]
rec['points_entries'] = [Y.tolist() for Y in pts]
tc = time.perf_counter(); cols = [c.column_tensor(Y % P, 5) for Y in pts]; rec['column_tensor_wall_s'] = time.perf_counter() - tc
basis = []; rows = []; attempted = []
for cand in cands:
    if time.perf_counter() - T0 > DEADLINE - 6: rec['stopped_by_deadline'] = True; break
    te = time.perf_counter(); vals = []; mi = 0; fl = 0
    for T in cols:
        v, m, f = pr.qval(cand['pi'], cand['rho'], T, cand['pairing']); vals.append(v); mi = max(mi, m); fl = max(fl, f)
    added = c.rank_mod(rows + [vals]) > len(rows)
    attempted.append(dict(index=cand['index'], maxint=mi, flops=fl, values=vals, added=added, wall=time.perf_counter() - te))
    if added: basis.append(cand); rows.append(vals)
    rec['basis_attempts'] = attempted
    rec['basis'] = [dict(index=b['index'], pairing=b['pairing'], pi=[[list(s) for s in blk] for blk in b['pi']], rho=[[list(s) for s in blk] for blk in b['rho']]) for b in basis]
    rec['basis_matrix_pair_by_point'] = rows; rec['basis_rank_mod_P'] = c.rank_mod(rows) if rows else 0
    save('basis_in_progress')
    if len(basis) == 5: break
rec['basis_5x5_minor_det_mod_P'] = det_mod(rows) if len(rows) == 5 else None
rec['wall_per_q_evaluation_s'] = (sum(a['wall'] for a in attempted) / (NPTS * len(attempted))) if attempted else None
rec['stages'].append(dict(stage='basis', elapsed=time.perf_counter() - T0))
save('BASIS_certified' if rec.get('basis_5x5_minor_det_mod_P') else 'STOP_basis_not_certified')
print(json.dumps({k: v for k, v in rec.items() if k not in ('points_entries', 'basis')}, indent=1))
