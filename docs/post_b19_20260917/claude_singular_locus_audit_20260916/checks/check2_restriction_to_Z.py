"""Check 2 (prepriced from p6/p7 receipts: ~0.34 s per column tensor + ~0.55 s per
vector evaluation; 6 points x 2 vectors ~ 11 s; memory well under 512 MiB):
evaluate the two certified full-H vectors q_3, q_7 of M_(4^5) (descent_followup
session, p6_basis.json / p7_arc_S0.py, mod P = 524287) at explicit points of
Z = {det(sum x_i B_i) == 0}. The points are GL5-mixes of the basis of the
singular non-compression space X = skew(3) + <E14> + <E44> of check 1.

A nonzero residue mod P is a nonzero integer, hence a nonzero rational value:
it certifies q|_Z != 0 (and, being a positive-degree invariant value, the
semistability of that point). Zero residues prove nothing.

Controls (able to fail): (C1) a dependent tuple must give 0 for both vectors
(five-row functions vanish on dependent tuples); (C2) the K5 point must reproduce
the stored p7 values.  Historical files are imported read-only.
"""
import json, sys, time
from pathlib import Path
import numpy as np
T0 = time.perf_counter(); DEADLINE = 50.0
HERE = Path(__file__).resolve().parent
PIL = HERE.parents[2] / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(PIL))
import paired_runner as pr
c = pr.c; P = pr.P
b6 = json.load(open(PIL / 'p6_basis.json')); b7 = json.load(open(PIL / 'p7_arc_S0.json'))
assert b7['basis_from'] == 'p6_basis.json', b7['basis_from']
basis = []
for b in b6['basis']:
    pi = tuple(tuple(tuple(s) for s in blk) for blk in b['pi']); rho = tuple(tuple(tuple(s) for s in blk) for blk in b['rho'])
    hp = pr.hand_plan(pi, rho); hr = pr.hand_plan(rho, pi)
    basis.append((pi, rho, hp[0], hr[0]))
assert [dict(order=list(b[2]), order_rev=list(b[3])) for b in basis] == b7['basis_plans']
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'check2_restriction_to_Z.json'
rec = dict(cell=dict(d=5, lam=[4]*5), prime=P, vectors=[q['index'] for q in b6['basis']], points=[], controls={})
def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1) + '\n')
def qval(quad, T):
    pi, rho, order, order_rev = quad
    a, m1, f1 = pr.evaluate_P(pi, rho, T, order); b, m2, f2 = pr.evaluate_P(rho, pi, T, order_rev)
    return (a + b) % P
def vals_at(Y):
    T = c.column_tensor(Y % P, 5)
    return [qval(q, T) for q in basis]
def E(i, j):
    M = np.zeros((4, 4), dtype=np.int64); M[i-1, j-1] = 1; return M
B = [E(1,2)-E(2,1), E(1,3)-E(3,1), E(2,3)-E(3,2), E(1,4), E(4,4)]
# control C2: K5 point of p7
def K5_tuple(t):
    Y = np.zeros((5, 4, 4), dtype=np.int64)
    for i, (r, cc) in enumerate([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]):
        Y[i, r, cc] = 1; Y[i, cc, r] = -1
    Y[0, 2, 3] += 1; Y[0, 3, 2] += -1
    Y[0] += t * np.eye(4, dtype=np.int64)
    return Y % P
v = vals_at(K5_tuple(0))
rec['controls']['K5_reproduced'] = dict(stored=b7['C2_values_at_K5_K5S_K52S'][0], recomputed=v, passed=(v == b7['C2_values_at_K5_K5S_K52S'][0]))
save('control_K5_done')
# control C1: dependent tuple (B1,B2,B3,B4,B1+B2) -> must be 0
Yd = np.array([B[0], B[1], B[2], B[3], B[0] + B[1]], dtype=np.int64)
v = vals_at(Yd)
rec['controls']['dependent_tuple_zero'] = dict(values=v, passed=(v == [0, 0]))
save('control_dependent_done')
rng = np.random.default_rng(20260917)
for ip in range(4):
    if time.perf_counter() - T0 > DEADLINE - 8: break
    while True:
        g = rng.integers(-3, 4, size=(5, 5))
        if round(abs(np.linalg.det(g))) != 0: break
    Y = np.einsum('ik,kab->iab', g, np.array(B, dtype=np.int64))
    v = vals_at(Y)
    rec['points'].append(dict(index=ip, mix_matrix=g.tolist(), det_mix=int(round(np.linalg.det(g))), tuple_entries=Y.tolist(), values_mod_P=v, nonzero=[x != 0 for x in v]))
    save('in_progress')
nz = any(any(p['nonzero']) for p in rec['points'])
save('Z_RESTRICTION_NONZERO_certified' if nz else 'all_sampled_values_zero_inconclusive')
print(json.dumps({k: (v if k != 'points' else [dict(index=p['index'], values_mod_P=p['values_mod_P'], det_mix=p['det_mix']) for p in v]) for k, v in rec.items()}, indent=1))
