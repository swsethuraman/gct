"""P4: structured 'paired-columns' epsilon contractions for M_(4^5) and a basis certificate.
Each block takes 2 slots from column A and 2 from column B (A,B a column pair), except one
'leftover' block with one slot from each of the four columns. The greedy planner then closes
the (A,B) sub-network before touching the other pair, so intermediates stay at 4^10 or 4^11.
Basis certified by a nonzero 5x5 modular minor at 5 integer points (s = 5 recomputed in P1).
Internal deadline 48 s; JSON written at every stage."""
import hashlib, importlib.util, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'
spec = importlib.util.spec_from_file_location('carrier', SRC); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
np = c.np; P = c.P
T0 = time.perf_counter(); DEADLINE = 48.0
LAM = (4, 4, 4, 4, 4); D = 5; HEIGHTS = c.conjugate(LAM)
SLOTS = [(j, k) for j, h in enumerate(HEIGHTS) for k in range(h)]
OUT = HERE / 'p4_paired_basis.json'
rec = dict(cell=dict(d=D, lam=list(LAM), heights=list(HEIGHTS)), prime=P, carrier_sha256=hashlib.sha256(SRC.read_bytes()).hexdigest(), stages=[])


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


def paired_partition(rng, pairing):
    """pairing: ((A,B),(C,E)) columns. For each column choose a 2+2+1 split of its 5 positions;
    blocks: (A:2 + B:2) x2, (C:2 + E:2) x2, leftover (one per column)."""
    blocks = []; left = []
    for (X, Y) in pairing:
        px = list(rng.permutation(5)); py = list(rng.permutation(5))
        blocks.append(tuple([(X, px[0]), (X, px[1]), (Y, py[0]), (Y, py[1])]))
        blocks.append(tuple([(X, px[2]), (X, px[3]), (Y, py[2]), (Y, py[3])]))
        left += [(X, px[4]), (Y, py[4])]
    blocks.append(tuple(left))
    # random slot order inside each block changes the sign only; keep as generated
    return blocks


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


def tensors(Y):
    return [c.column_tensor(Y, 5)] * 4


def qval(pair, ct):
    pi, rho = pair
    a, m1, f1 = c.evaluate_pair(pi, rho, ct, None, None); b, m2, f2 = c.evaluate_pair(rho, pi, ct, None, None)
    rec['max_intermediate_seen'] = max(rec.get('max_intermediate_seen', 0), m1, m2)
    rec['flops_seen_max'] = max(rec.get('flops_seen_max', 0), f1, f2)
    return (a + b) % P


rng = np.random.default_rng(20260916)
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
cands = []
for n in range(60):
    pi = paired_partition(rng, PAIRINGS[n % 3]); rho = paired_partition(rng, PAIRINGS[(n + 1) % 3])
    mi, fl = plan_cost(pi, rho)
    cands.append(dict(index=n, pi=pi, rho=rho, maxint=mi, flops=fl))
cands = [cd for cd in cands if cd['maxint'] <= 4 ** 11 and cd['flops'] <= 3 * 10 ** 8]
cands.sort(key=lambda cd: cd['flops'])
rec['candidates_planned'] = len(cands); rec['candidate_costs'] = [(cd['maxint'], cd['flops']) for cd in cands[:12]]
rec['stages'].append(dict(stage='planning', elapsed=time.perf_counter() - T0)); save('planning_done')
NPTS = 5
pts = [rng.integers(-3, 4, size=(5, 4, 4)).astype(np.int64) for _ in range(NPTS)]
cols = [tensors(Y % P) for Y in pts]
basis = []; rows = []; attempted = []
for cand in cands:
    if time.perf_counter() - T0 > DEADLINE - 6: break
    te = time.perf_counter(); vals = [qval((cand['pi'], cand['rho']), ct) for ct in cols]
    added = c.rank_mod(rows + [vals]) > len(rows)
    attempted.append(dict(index=cand['index'], maxint=cand['maxint'], flops=cand['flops'], values=vals, added=added, wall=time.perf_counter() - te))
    if added: basis.append(cand); rows.append(vals)
    save('basis_in_progress')
    if len(basis) == 5: break
rec['basis_attempts'] = attempted
rec['basis'] = [dict(index=b['index'], pi=[[list(s) for s in blk] for blk in b['pi']], rho=[[list(s) for s in blk] for blk in b['rho']], maxint=b['maxint'], flops=b['flops']) for b in basis]
rec['points_entries'] = [Y.tolist() for Y in pts]
rec['basis_matrix_pair_by_point'] = rows; rec['basis_rank_mod_P'] = c.rank_mod(rows) if rows else 0
rec['basis_5x5_minor_det_mod_P'] = det_mod(rows) if len(rows) == 5 else None
rec['stages'].append(dict(stage='basis', elapsed=time.perf_counter() - T0))
save('BASIS_certified' if rec.get('basis_5x5_minor_det_mod_P') else 'STOP_basis_not_certified')
print(json.dumps({k: v for k, v in rec.items() if k not in ('points_entries',)}, indent=1))
