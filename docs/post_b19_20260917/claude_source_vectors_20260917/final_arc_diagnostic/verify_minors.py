"""Arithmetic verifier for the final arc diagnostic (standard library only).

Replays, from the recorded integers (results/f1_new_point_minor.json and the inherited rows quoted there):
  - the inherited 2x2 forbidden minors 104967 and 171205;
  - every 3x3 minor of the 14 rows on (q3, q7, n02) modulo P (all zero; combined rank 2);
  - the relation n02 = 265391 q3 + 275398 q7 on all 14 rows and its rejection for a corrupted coefficient;
  - the rank-1 structure of the degree-12 rows (constant ratios 101007, 295818) on all 7 degree-12 rows;
  - the Vandermonde extraction of the new rows from the recorded 13 node values, and the u = 14 degree controls.
It does not re-evaluate any contraction (values come from the sealed runner inside the wrapped pilot)."""
import itertools, json
from pathlib import Path
P = 524287
HERE = Path(__file__).resolve().parent
r = json.loads((HERE / 'results/f1_new_point_minor.json').read_text())
ok = True
def check(name, cond, detail=''):
    global ok
    ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name + (' ' + str(detail) if detail else ''))
def det_mod(M):
    n = len(M); A = [[x % P for x in row] for row in M]; det = 1
    for k in range(n):
        piv = next((i for i in range(k, n) if A[i][k]), None)
        if piv is None: return 0
        if piv != k: A[k], A[piv] = A[piv], A[k]; det = (-det) % P
        det = det * A[k][k] % P; inv = pow(A[k][k], P - 2, P)
        for i in range(k + 1, n):
            f = A[i][k] * inv % P; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[k])]
    return det
def rank_mod(M):
    M = [[x % P for x in row] for row in M]; rk = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]; inv = pow(M[rk][c], P - 2, P); M[rk] = [x * inv % P for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]: f = M[i][c]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
def vandermonde_solve(nodes, values, degrees):
    n = len(nodes); A = [[pow(x, e, P) for e in degrees] + [v % P] for x, v in zip(nodes, values)]
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c]); A[c], A[piv] = A[piv], A[c]
        inv = pow(A[c][c], P - 2, P); A[c] = [x * inv % P for x in A[c]]
        for i in range(n):
            if i != c and A[i][c]: f = A[i][c]; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[c])]
    return [A[i][n] for i in range(n)]
rows = r['inherited_rows'] + r['new_rows']
check('14 rows present (10 inherited + 4 new)', len(rows) == 14)
check('inherited 2x2 minor S0 P7 point 0 == 104967', det_mod([[34725, 239889], [176113, 112168]]) == 104967)
check('inherited 2x2 minor full P6 point 0 == 171205', det_mod([[86170, 71919], [376209, 469277]]) == 171205)
R = [row['row'] for row in rows]
check('combined rank of the 14 rows == 2', rank_mod(R) == 2)
check('all 364 3x3 minors vanish mod P', all(det_mod([R[i] for i in ri]) == 0 for ri in itertools.combinations(range(14), 3)))
a, b = 265391, 275398
check('relation n02 = 265391 q3 + 275398 q7 holds on all 14 rows (mod P)', all((a * x[0] + b * x[1] - x[2]) % P == 0 for x in R))
check('corrupted coefficient (alpha+1) rejected', any(((a + 1) * x[0] + b * x[1] - x[2]) % P for x in R))
d12 = [x['row'] for x in rows if x['label'].endswith('d12')]
check('7 degree-12 rows have rank 1 with ratios 101007 and 295818', len(d12) == 7 and rank_mod(d12) == 1 and all(x[1] * pow(x[0], P - 2, P) % P == 101007 and x[2] * pow(x[0], P - 2, P) % P == 295818 for x in d12))
nodes = r['u_nodes']; degs = r['degrees']
for name, ip in (('q3', 2), ('q7', 2), ('q3', 3), ('q7', 3), ('n02', 3)):
    vals = r['values']['%s_pt%d' % (name, ip)]; co = vandermonde_solve(nodes, vals, degs)
    check('Vandermonde extraction %s pt%d reproduces recorded coefficients' % (name, ip), co == r['values']['%s_pt%d_coeffs_u0_to_u12' % (name, ip)])
    check('row entries %s pt%d equal z11, z12' % (name, ip), (co[11], co[12]) == (r['points']['P6pt%d' % ip][name]['z11'], r['points']['P6pt%d' % ip][name]['z12']))
for k, v in r['controls'].items():
    if isinstance(v, dict) and 'passed' in v: check('control ' + k, v['passed'])
    elif k.startswith('corrupted_node_rejected'): check('control ' + k, v)
check('n02 row at P6 point 2 reused from the sealed parent (240230, 285304)', r['points']['P6pt2']['n02']['z11'] == 240230 and r['points']['P6pt2']['n02']['z12'] == 285304)
print('ALL CHECKS PASSED' if ok else 'SOME CHECKS FAILED')
