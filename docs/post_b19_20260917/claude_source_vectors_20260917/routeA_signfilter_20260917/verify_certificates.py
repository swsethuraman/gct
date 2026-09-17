"""Independent re-check of the LINEAR ALGEBRA behind every certificate in this directory.

Dependencies: Python 3 standard library only (no numpy, no sympy, no carrier, no runner).
What it does NOT do: it does not re-evaluate any contraction.  All contraction values were produced
by the sealed runner (work/descent_followup_claude_20260916/pilots/paired_runner.py over
b18_02_carrier.py) inside pilots s1-s3; this script only re-derives ranks, minors, Vandermonde
coefficients and relations from the recorded integers modulo P = 524287 with its own arithmetic.
Run:  python verify_certificates.py   (from this directory)."""
import itertools, json
from pathlib import Path
P = 524287
HERE = Path(__file__).resolve().parent

def rank_mod(M):
    M = [[x % P for x in r] for r in M]; r = 0
    for cidx in range(len(M[0]) if M else 0):
        piv = next((i for i in range(r, len(M)) if M[i][cidx]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][cidx], P - 2, P); M[r] = [x * inv % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][cidx]:
                f = M[i][cidx]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[r])]
        r += 1
    return r

def det_mod(M):
    n = len(M); A = [[x % P for x in r] for r in M]; det = 1
    for k in range(n):
        piv = next((i for i in range(k, n) if A[i][k]), None)
        if piv is None: return 0
        if piv != k: A[k], A[piv] = A[piv], A[k]; det = (-det) % P
        det = det * A[k][k] % P; inv = pow(A[k][k], P - 2, P)
        for i in range(k + 1, n):
            f = A[i][k] * inv % P; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[k])]
    return det

def vandermonde_solve(nodes, values, degrees):
    n = len(nodes); A = [[pow(x, e, P) for e in degrees] + [v % P] for x, v in zip(nodes, values)]
    for cidx in range(n):
        piv = next(i for i in range(cidx, n) if A[i][cidx]); A[cidx], A[piv] = A[piv], A[cidx]
        inv = pow(A[cidx][cidx], P - 2, P); A[cidx] = [x * inv % P for x in A[cidx]]
        for i in range(n):
            if i != cidx and A[i][cidx]:
                f = A[i][cidx]; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[cidx])]
    return [A[i][n] for i in range(n)]

ok = True
def check(name, cond, detail=''):
    global ok
    ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name + (' ' + str(detail) if detail else ''))

# 1. independence of q3, q7, e, n02 at the P6 points
ind = json.loads((HERE / 'certificates/independence_q3_q7_e_n02.json').read_text())
M = ind['matrix_rows_by_point']
check('e row equals reduction of the exact integers', [x % P for x in ind['e_exact_integers']] == M[2])
check('rank(q3,q7,e,n02 | P6 points) == 4', rank_mod(M) == 4)
for cols, d in ind['nonzero_4x4_minors_by_point_columns'].items():
    cc = json.loads(cols); check('4x4 minor on point columns %s == %d' % (cols, d), det_mod([[r[j] for j in cc] for r in M]) == d)

# 2. transverse triple rank 3
tr = json.loads((HERE / 'certificates/transverse_triple_rank3.json').read_text())
def rows_T(z):
    return [(112 * z['K5+S1'] - 7 * z['K5+2S1'] - 177 * z['K5']) % P,
            (-27 * z['K5'] - 60 * z['K5+S1'] + 15 * z['K5+2S1'] + 368 * z['K5+S2'] - 92 * z['K5+2S2']) % P,
            (-2211 * z['K5'] - 252 * z['K5+S1'] + 63 * z['K5+2S1'] + 2576 * z['K5+S4'] - 644 * z['K5+2S4']) % P]
T = {k: rows_T(v) for k, v in tr['pencil_values'].items()}
check('q3 transverse row reproduces sealed (456851, 30271, 120670)', T['q3'] == [456851, 30271, 120670])
check('q7 transverse row reproduces sealed (3402, 137059, 19278)', T['q7'] == [3402, 137059, 19278])
M3 = [[T['q3'][i], T['q7'][i], T['n02'][i]] for i in range(3)]
check('transverse 3x3 matrix matches certificate', M3 == tr['matrix'])
check('det(C2, C4_S1S2, C4_S1S4 | q3, q7, n02) == %d != 0' % tr['det_mod_P'], det_mod(M3) == tr['det_mod_P'] and tr['det_mod_P'] != 0)

# 3. arc rows: S0 slice (recorded t-values) and full rows (Vandermonde from raw node values)
arc = json.loads((HERE / 'certificates/arc_rows_and_sampled_kernel_candidate.json').read_text())
n02 = json.loads((HERE / 'certificates/n02_definition.json').read_text())
inv2 = pow(2, P - 2, P)
s0 = arc['S0_slice_rows']['rows_point_degree']
# re-derive n02's S0 rows from its recorded t-values
for ip in range(3):
    v = n02['values']['P7_S0_points_t0_t1_t2_t3'][str(ip)]
    q12 = ((v[2] - 2 * v[1] + v[0]) * inv2) % P; q11 = (v[1] - v[0] - q12) % P
    check('n02 S0 degree control at P7 point %d (t=3 predicted)' % ip, (v[0] + 3 * q11 + 9 * q12) % P == v[3])
    check('n02 S0 rows at point %d match certificate' % ip, [r['row'][2] for r in s0 if r['point'] == ip] == [q11, q12])
S0M = [r['row'] for r in s0]
check('S0 6x3 rank == 2', rank_mod(S0M) == 2)
full = arc['full_rows']
nodes = list(range(1, 14)); degs = list(range(13))
FM = []
for r in full['rows']:
    ip, deg = r['point'], r['degree']; row = []
    for name in arc['columns']:
        vals = full['raw_node_values']['%s_pt%d' % (name, ip)]
        co = vandermonde_solve(nodes, vals, degs); row.append(co[deg])
        stored = full['raw_node_values']['%s_pt%d_coeffs_u0_to_u12' % (name, ip)]
        check('Vandermonde coefficients %s pt%d reproduce recorded' % (name, ip), co == stored) if deg == 11 else None
    check('full row (pt %d, deg %d) matches' % (ip, deg), row == r['row'])
    FM.append(row)
for k, v in full['controls'].items():
    check('control ' + k, v['passed'])
check('full 4x3 rank == 2', rank_mod(FM) == 2)
al, be = arc['sampled_kernel_candidate']['alpha_mod_P'], arc['sampled_kernel_candidate']['beta_mod_P']
check('relation n02 = alpha q3 + beta q7 on all 6 S0 rows', all((al * r[0] + be * r[1] - r[2]) % P == 0 for r in S0M))
check('same relation on all 4 full rows', all((al * r[0] + be * r[1] - r[2]) % P == 0 for r in FM))
Tn = [(T['n02'][i] - al * T['q3'][i] - be * T['q7'][i]) % P for i in range(3)]
check('transverse values on n (mod P) match certificate', Tn == list(arc['sampled_kernel_candidate']['transverse_values_on_n_mod_P'].values()))
print('ALL CHECKS PASSED' if ok else 'SOME CHECKS FAILED')
