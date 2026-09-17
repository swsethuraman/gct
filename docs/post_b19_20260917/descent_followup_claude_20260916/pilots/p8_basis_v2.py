"""P8: basis of M_(4^5), second attempt. Seeds: the two independent same-pairing vectors of P6
(indices 3 and 7, values reused at the same five points). New candidates: random and
'pair-block' partitions priced by the label-only hand-order simulation; only plans with
max intermediate <= 4^10 and <= 2.5e8 flop units per orientation are evaluated.
Certificate: 5x5 modular minor at the five P6 points. Deadline 50 s."""
import hashlib, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import paired_runner as pr
c = pr.c; np = pr.np; P = pr.P
T0 = time.perf_counter(); DEADLINE = 50.0
OUT = HERE / 'p8_basis_v2.json'
b6 = json.loads((HERE / 'p6_basis.json').read_text())
pts = [np.array(Y, dtype=np.int64) for Y in b6['points_entries']]
rec = dict(cell=dict(d=5, lam=[4] * 5, heights=[5] * 4), prime=P, carrier_sha256=hashlib.sha256(pr.SRC.read_bytes()).hexdigest(),
           runner='paired_runner.py', points_from='p6_basis.json', stages=[])


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


def pair_blocks(rng):
    free = {j: [int(k) for k in rng.permutation(5)] for j in range(4)}
    blocks = []
    for _ in range(4):
        cols = [j for j in range(4) if len(free[j]) >= 2]
        if len(cols) < 2: return None
        A, B = [int(v) for v in rng.choice(cols, 2, replace=False)]
        blocks.append(tuple([(A, free[A].pop()), (A, free[A].pop()), (B, free[B].pop()), (B, free[B].pop())]))
    rest = [(j, k) for j in range(4) for k in free[j]]
    if len(rest) != 4: return None
    blocks.append(tuple(rest))
    return blocks


rng = np.random.default_rng(20260917)
cands = []; tried = 0
while tried < 4000 and time.perf_counter() - T0 < 6:
    tried += 1
    kind = 'random' if tried % 2 else 'pairblock'
    if kind == 'random':
        pi, rho = pr.random_partition(rng), pr.random_partition(rng)
    else:
        pi, rho = pair_blocks(rng), pair_blocks(rng)
        if pi is None or rho is None: continue
    hp = pr.hand_plan(pi, rho); hr = pr.hand_plan(rho, pi)
    if hp is None or hr is None: continue
    mi = max(hp[1], hr[1]); fl = hp[2] + hr[2]
    if mi <= 4 ** 10 and fl <= 5 * 10 ** 8:
        cands.append(dict(kind=kind, tried=tried, pi=pi, rho=rho, order=hp[0], order_rev=hr[0], maxint=mi, flops=fl))
cands.sort(key=lambda cd: cd['flops'])
rec['partitions_tried'] = tried; rec['candidates_accepted'] = len(cands)
rec['candidate_costs_first20'] = [(cd['kind'], cd['maxint'], cd['flops']) for cd in cands[:20]]
rec['stages'].append(dict(stage='planning', elapsed=time.perf_counter() - T0)); save('planning_done')
# seeds from P6
basis = []; rows = []
for b, att in zip(b6['basis'], [a for a in b6['basis_attempts'] if a['added']]):
    basis.append(dict(kind='same-pairing-P6', index=b['index'], pi=[[tuple(s) for s in blk] for blk in b['pi']], rho=[[tuple(s) for s in blk] for blk in b['rho']], pairing=b['pairing']))
    rows.append(att['values'])
assert c.rank_mod(rows) == len(rows)
cols = [c.column_tensor(Y % P, 5) for Y in pts]
attempted = []
for cand in cands:
    if time.perf_counter() - T0 > DEADLINE - 7: rec['stopped_by_deadline'] = True; break
    te = time.perf_counter(); vals = []; mi = 0; fl = 0
    for T in cols:
        a, m1, f1 = pr.evaluate_P(cand['pi'], cand['rho'], T, cand['order']); b_, m2, f2 = pr.evaluate_P(cand['rho'], cand['pi'], T, cand['order_rev'])
        vals.append((a + b_) % P); mi = max(mi, m1, m2); fl = max(fl, f1 + f2)
    added = c.rank_mod(rows + [vals]) > len(rows)
    attempted.append(dict(kind=cand['kind'], tried=cand['tried'], maxint=mi, flops=fl, values=vals, added=added, wall=time.perf_counter() - te))
    if added:
        basis.append(dict(kind=cand['kind'], tried=cand['tried'], pi=[[list(s) for s in blk] for blk in cand['pi']], rho=[[list(s) for s in blk] for blk in cand['rho']], order=list(cand['order']), order_rev=list(cand['order_rev'])))
        rows.append(vals)
    rec['basis_attempts'] = attempted
    rec['basis'] = [dict((k, (v if k not in ('pi', 'rho') else [[list(s) for s in blk] for blk in v])) for k, v in b.items()) for b in basis]
    rec['basis_matrix_pair_by_point'] = rows; rec['basis_rank_mod_P'] = c.rank_mod(rows)
    save('basis_in_progress')
    if len(basis) == 5: break
rec['basis_5x5_minor_det_mod_P'] = det_mod(rows) if len(rows) == 5 else None
rec['stages'].append(dict(stage='basis', elapsed=time.perf_counter() - T0))
save('BASIS_certified' if rec.get('basis_5x5_minor_det_mod_P') else 'STOP_basis_not_certified')
print(json.dumps({k: v for k, v in rec.items() if k not in ('basis',)}, indent=1))
