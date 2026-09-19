"""B23-01 pilot 1: the second-prime test (docs/b23_01_report.md sec. 1; B22-10 sec. 4, not redesigned).

Stage 0  G25: sha256 of results/b23_01/preregistration_snapshot.md, checked against --prereg-sha and
         written into this output before anything else; a mismatch stops the pilot.
Stage 1  artifacts: the pinned carrier/runner fetched by commit and path; materialised unmodified under
         results/b23_01/pinned_P1/ and, with exactly one line changed (P = 524269), under pinned_P2/.
Stage 2  controls before any new evaluation: (1) six sealed values at P with det(g)^{-4};
         (2) det(g)^{-4} normalisation at P2 (two slice forms, g-independence, teeth);
         (3) relation residuals of the recorded rows (arithmetic).  Any failure: stop, no test.
Stage 3  the test: q3, q7, n02 at certified points 0, 1, 2 mod P2 (45 evaluations); all 20 3x3 minors.
Stage 4  descriptive (MEASURED, decides nothing): relation and ratios mod P2, CRT + rational reconstruction;
         sixth-node consistency (u^7 coefficient must vanish).
Producer-only (G18).  JSON written after every stage."""
import hashlib, importlib.util, json, math, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
T0 = time.perf_counter(); DEADLINE = 55.0
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
OUTDIR = ROOT / 'results/b23_01'; OUT = OUTDIR / 'p1_secondprime.json'
assert not OUT.exists(), 'outputs are never overwritten (G10)'
args = sys.argv[1:]
PREREG_SHA = args[args.index('--prereg-sha') + 1]


def sha(b): return hashlib.sha256(b).hexdigest()
def left(): return DEADLINE - (time.perf_counter() - T0)


rec = dict(pilot='b23_01_p1_secondprime', log=[], runner_evaluations=dict(P=0, P2=0), runner_wall_s=dict(P=0.0, P2=0.0))
def save(status):
    rec['status'] = status; rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')

# ---------------------------------------------------------------- stage 0: G25
snap = (ROOT / 'results/b23_01/preregistration_snapshot.md').read_bytes()
rec['preregistration'] = dict(path='results/b23_01/preregistration_snapshot.md', sha256=sha(snap), expected=PREREG_SHA,
                              match=(sha(snap) == PREREG_SHA), recorded_at_elapsed_s=round(time.perf_counter() - T0, 4))
print('PREREGISTRATION sha256 %s match=%s' % (sha(snap), rec['preregistration']['match']), flush=True)
save('stage0_preregistration')
if not rec['preregistration']['match']:
    save('STOP_preregistration_mismatch'); sys.exit(0)

# ---------------------------------------------------------------- stage 1: artifacts
import numpy as np
import b20_01_pinned as pin          # fetch() only: git show + sha256; writes nothing
import b20_01_flag as fl             # mod-P helpers (P = 524287) for control 1
P = 524287; P2 = 524269
LINE = 'P = 524287  # 2**19 - 1, Mersenne prime'
NEWLINE = 'P = 524269  # B23-01 second prime 2**19 - 19'
cb, crec = pin.fetch('b18_02_carrier.py'); rb, rrec = pin.fetch('paired_runner.py')
rec['inputs'] = dict(carrier=crec, runner_original=rrec)
csrc = cb.decode(); assert csrc.count(LINE) == 1, 'the constant line must occur exactly once'
rsrc = rb.decode(); OLD = "SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'"
assert rsrc.count(OLD) == 1
rpatched = rsrc.replace(OLD, "SRC = HERE / 'b18_02_carrier.py'")
arts = {}
for tag, carrier_src in (('pinned_P1', csrc), ('pinned_P2', csrc.replace(LINE, NEWLINE))):
    d = OUTDIR / tag; d.mkdir(parents=True, exist_ok=True)
    (d / 'b18_02_carrier.py').write_bytes(carrier_src.encode()) if tag == 'pinned_P2' else (d / 'b18_02_carrier.py').write_bytes(cb)
    (d / 'paired_runner.py').write_text(rpatched, newline='\n')
    arts[tag] = dict(carrier_sha256=sha((d / 'b18_02_carrier.py').read_bytes()), runner_sha256=sha((d / 'paired_runner.py').read_bytes()))
arts['pinned_P1']['carrier_equals_pinned'] = arts['pinned_P1']['carrier_sha256'] == crec['sha256']
arts['pinned_P1']['runner_equals_b20_01_patched'] = arts['pinned_P1']['runner_sha256'] == 'e7ba4ff7ab676a0fb259dd662397d3a52bdbbcc12604f16e292fe005fce210fc'
arts['pinned_P2']['runner_equals_b20_01_patched'] = arts['pinned_P2']['runner_sha256'] == 'e7ba4ff7ab676a0fb259dd662397d3a52bdbbcc12604f16e292fe005fce210fc'
diff = [(a, b) for a, b in zip(csrc.splitlines(), (OUTDIR / 'pinned_P2/b18_02_carrier.py').read_text().splitlines()) if a != b]
arts['pinned_P2']['carrier_lines_changed'] = diff
rec['artifacts'] = arts
assert arts['pinned_P1']['carrier_equals_pinned'] and arts['pinned_P1']['runner_equals_b20_01_patched'] and len(diff) == 1


def load(tag, name):
    spec = importlib.util.spec_from_file_location(name, OUTDIR / tag / 'paired_runner.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


pr1 = load('pinned_P1', 'paired_runner_b23_p1'); pr2 = load('pinned_P2', 'paired_runner_b23_p2')
assert pr1.P == P and pr1.c.P == P and pr2.P == P2 and pr2.c.P == P2
rec['P2'] = dict(value=P2, trial_division_prime=all(P2 % q for q in range(2, math.isqrt(P2) + 1)), carrier_isprime_assert='passed at import',
                 vandermonde_det_nodes_1_5=288, divides_288=(288 % P2 == 0), below_P=(P2 < P))
assert rec['P2']['trial_division_prime'] and not rec['P2']['divides_288'] and rec['P2']['below_P']
save('stage1_artifacts')

p6b, r1 = pin.fetch('p6_basis.json'); n02b, r2 = pin.fetch('n02_definition.json')
rec['inputs'].update({'p6_basis.json': r1, 'n02_definition.json': r2})
p6 = json.loads(p6b); n02d = json.loads(n02b)
def tup(blocks): return tuple(tuple(tuple(int(x) for x in s) for s in b) for b in blocks)
V = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
    V['q%d' % b['index']] = dict(pi=tup(b['pi']), rho=tup(b['rho']), order=order, order_rev=order)
V['n02'] = dict(pi=tup(n02d['pi_ordered_blocks']), rho=tup(n02d['rho_ordered_blocks']),
                order=tuple(n02d['hand_plan_column_order']), order_rev=tuple(n02d['hand_plan_column_order_transposed']))
for d in V.values():
    assert tuple(pr1.hand_plan(d['pi'], d['rho'])[0]) == d['order'] and tuple(pr1.hand_plan(d['rho'], d['pi'])[0]) == d['order_rev']
ORDER = ['q3', 'q7', 'n02']
CERT = ROOT / 'results/b22_01/p2_basis.json'; cb2 = CERT.read_bytes()
assert sha(cb2) == '7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79'
cert = json.loads(cb2); rec['inputs']['p2_basis.json'] = dict(sha256=sha(cb2), bound_by='results/b22_01/MANIFEST.json 1931ab8f @ 53bdb31e')
P3F = ROOT / 'results/b20_01/p3_flag_rows.json'; p3b = P3F.read_bytes()
assert sha(p3b) == '73c3be3c0789d26001953f940792c9086ce19fc72d758566f5bea2c86ece66ee'
p3 = json.loads(p3b); rec['inputs']['p3_flag_rows.json'] = dict(sha256=sha(p3b), bound_by='results/b20_01/MANIFEST.json 0e5fd026')


def qval(pr, key, d, T):
    te = time.perf_counter()
    a, m1, _ = pr.evaluate_P(d['pi'], d['rho'], T, d['order']); b_, m2, _ = pr.evaluate_P(d['rho'], d['pi'], T, d['order_rev'])
    rec['runner_evaluations'][key] += 1; rec['runner_wall_s'][key] += time.perf_counter() - te; assert max(m1, m2) <= 4 ** 10
    return (a + b_) % pr.P


def inv(x, p): return pow(int(x) % p, p - 2, p)


def gauss_solve(A, b, p):
    """Vandermonde / square solve mod p (Python ints)."""
    n = len(A); M = [[int(x) % p for x in row] + [int(bb) % p] for row, bb in zip(A, b)]
    for c in range(n):
        r = next(i for i in range(c, n) if M[i][c]); M[c], M[r] = M[r], M[c]
        iv = inv(M[c][c], p); M[c] = [x * iv % p for x in M[c]]
        for i in range(n):
            if i != c and M[i][c]: f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[c])]
    return [M[i][n] for i in range(n)]


def vander(nodes, vals, degs, p): return dict(zip(degs, gauss_solve([[pow(u, e, p) for e in degs] for u in nodes], vals, p)))


def det_p(M, p):
    A = [[int(x) % p for x in r] for r in M]; n = len(A); det = 1
    for k in range(n):
        r = next((i for i in range(k, n) if A[i][k]), None)
        if r is None: return 0
        if r != k: A[k], A[r] = A[r], A[k]; det = -det
        det = det * A[k][k] % p; iv = inv(A[k][k], p)
        for i in range(k + 1, n):
            if A[i][k]: f = A[i][k] * iv % p; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[k])]
    return det % p


def rank_p(M, p):
    A = [[int(x) % p for x in r] for r in M]; rk = 0
    for c in range(len(A[0])):
        r = next((i for i in range(rk, len(A)) if A[i][c]), None)
        if r is None: continue
        A[rk], A[r] = A[r], A[rk]; iv = inv(A[rk][c], p); A[rk] = [x * iv % p for x in A[rk]]
        for i in range(len(A)):
            if i != rk and A[i][c]: f = A[i][c]; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[rk])]
        rk += 1
    return rk


EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
NU_INT = []
for k in range(3):
    m = np.zeros((4, 4), dtype=np.int64)
    for (i, j, kk), s in EPS.items():
        if kk == k: m[1 + i, 1 + j] = -s
    NU_INT.append(m)                                     # true integers (-1, 0, 1); reduced mod the prime at use
assert all(np.array_equal(a % P, b % P) for a, b in zip(NU_INT, fl.NU))
rec['checks'] = dict(nu_integer_matches_b20_01_mod_P=True)

# ---------------------------------------------------------------- stage 2: controls
ctrl = {}; rec['controls'] = ctrl
# (1) six sealed values at P with det(g)^{-4}
SEALED = dict(d11=[86170, 71919, 226580], d12=[376209, 469277, 41046])
Y0 = np.array(p6['points_entries'][0], dtype=np.int64)
g, detg, Yt = fl.slice_form(Y0); Zs = fl.wprime_part(Yt)
F = {n: [] for n in ORDER}; TOP = {n: [] for n in ORDER}
for k in range(3):
    T = [pr1.c.column_tensor(fl.tuple_F(Zs[0], Zs[1], Zs[2 + k], k, u), 5) for u in fl.NODES5]
    for name in ORDER:
        co = fl.vandermonde_solve(fl.NODES5, [qval(pr1, 'P', V[name], t) for t in T], [8, 9, 10, 11, 12])
        F[name].append(co[11]); TOP[name].append(co[12])
d4 = pow(detg, 4, P); i4 = inv(d4, P); c1 = {}
for i, name in enumerate(ORDER):
    s11, s12 = sum(F[name]) % P, TOP[name][0]
    c1[name] = dict(identity_d11=(s11 == d4 * SEALED['d11'][i] % P), identity_d12=(s12 == d4 * SEALED['d12'][i] % P),
                    full_d11=i4 * s11 % P, full_d12=i4 * s12 % P, sealed=[SEALED['d11'][i], SEALED['d12'][i]], top_equal_across_k=len(set(TOP[name])) == 1)
ctrl['c1_six_sealed_at_P'] = dict(det_g=detg, det_g_inv4=i4, per_vector=c1,
                                  matched=sum(int(c1[n]['full_d11'] == c1[n]['sealed'][0]) + int(c1[n]['full_d12'] == c1[n]['sealed'][1]) for n in ORDER))
ctrl['c1_pass'] = ctrl['c1_six_sealed_at_P']['matched'] == 6 and all(c1[n]['identity_d11'] and c1[n]['identity_d12'] and c1[n]['top_equal_across_k'] for n in ORDER)
save('stage2_c1')


# (2) det(g)^{-4} normalisation at P2
def slice_p(Y, p):
    Y = Y % p; E = Y[:, 1:, 1:]; i2 = inv(2, p)
    K = ((E - np.swapaxes(E, 1, 2)) % p) * i2 % p
    v = np.stack([(-K[:, 1, 2]) % p, (-K[:, 2, 0]) % p, (-K[:, 0, 1]) % p])     # v_k = -K_{ij}, (i,j,k) cyclic
    A = [[int(x) for x in row] for row in v]
    M = [r[:] for r in A]; piv = []; rr = 0
    for c in range(5):
        r = next((i for i in range(rr, 3) if M[i][c]), None)
        if r is None: continue
        M[rr], M[r] = M[r], M[rr]; iv = inv(M[rr][c], p); M[rr] = [x * iv % p for x in M[rr]]
        for i in range(3):
            if i != rr and M[i][c]: f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[rr])]
        piv.append(c); rr += 1
    assert rr == 3
    free = [j for j in range(5) if j not in piv]; rows = []
    for fj in free:
        kvec = [0] * 5; kvec[fj] = 1
        for i, c in enumerate(piv): kvec[c] = (-M[i][fj]) % p
        rows.append(kvec)
    for k in range(3):
        x = [0] * 5
        for i, c in enumerate(piv): x[c] = 1 if i == k else 0
        # M is reduced with pivots piv; x solves M x = e_k, and A x = e_k because M = R A with R invertible and rows reordered:
        rows.append(x)
    return A, rows


def check_slice(A, rows, p):
    """v u_1 = v u_2 = 0 and v u_{k+2} = e_k, verified directly (the reduction above is re-checked, not trusted)."""
    for i, u in enumerate(rows):
        want = [0, 0, 0] if i < 2 else [1 if j == i - 2 else 0 for j in range(3)]
        got = [sum(A[r][m] * u[m] for m in range(5)) % p for r in range(3)]
        if got != want: return False
    return True


def fix_slice(A, rows, p):
    """If a particular solution fails (row reordering), solve A x = e_k by least-norm-free elimination on A itself."""
    out = rows[:2]
    for k in range(3):
        M = [r[:] + [1 if j == k else 0] for j, r in enumerate(A)]
        piv = []; rr = 0
        for c in range(5):
            r = next((i for i in range(rr, 3) if M[i][c]), None)
            if r is None: continue
            M[rr], M[r] = M[r], M[rr]; iv = inv(M[rr][c], p); M[rr] = [x * iv % p for x in M[rr]]
            for i in range(3):
                if i != rr and M[i][c]: f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[rr])]
            piv.append(c); rr += 1
        x = [0] * 5
        for i, c in enumerate(piv): x[c] = M[i][5]
        out.append(x)
    return out


Y0p = Y0 % P2
A, rows = slice_p(Y0p, P2)
rows = fix_slice(A, rows, P2)          # kernel rows from slice_p; particular solutions from the augmented system [A | e_k]
assert check_slice(A, rows, P2), 'slice form mod P2'
g1 = [r[:] for r in rows]
g2 = [r[:] for r in rows]; g2[0] = [2 * x % P2 for x in g2[0]]; g2[2] = [(x + y) % P2 for x, y in zip(g2[2], g2[0])]
assert check_slice(A, g2, P2)
nuP2 = [m % P2 for m in NU_INT]
c2 = dict(per_g=[])
tops = []
for gg in (g1, g2):
    dg = det_p(gg, P2); assert dg != 0, 'det(g) = 0 mod P2'
    Yt2 = np.stack([sum(gg[i][m] * Y0p[m] for m in range(5)) % P2 for i in range(5)]).astype(np.int64)
    assert np.array_equal(Yt2[0, 1:, 1:], Yt2[0, 1:, 1:].T) and np.array_equal(Yt2[1, 1:, 1:], Yt2[1, 1:, 1:].T)
    T = pr2.c.column_tensor(np.stack([Yt2[0], Yt2[1], nuP2[0], nuP2[1], nuP2[2]]) % P2, 5)
    tv = {n: qval(pr2, 'P2', V[n], T) for n in ORDER}
    tops.append((dg, tv)); c2['per_g'].append(dict(det_g=dg, top=tv))
c2['identity'] = {n: (inv(pow(tops[0][0], 4, P2), P2) * tops[0][1][n] % P2 == inv(pow(tops[1][0], 4, P2), P2) * tops[1][1][n] % P2) for n in ORDER}
c2['teeth_inverted_recipe_fails'] = {n: (pow(tops[0][0], 4, P2) * tops[0][1][n] % P2 != pow(tops[1][0], 4, P2) * tops[1][1][n] % P2) for n in ORDER}
c2['full_top_mod_P2'] = {n: inv(pow(tops[0][0], 4, P2), P2) * tops[0][1][n] % P2 for n in ORDER}
c2['det_ratio'] = tops[1][0] * inv(tops[0][0], P2) % P2
ctrl['c2_normalisation_at_P2'] = c2
ctrl['c2_pass'] = all(c2['identity'].values()) and all(c2['teeth_inverted_recipe_fails'].values()) and c2['det_ratio'] == 2
save('stage2_c2')
# (3) recorded rows (arithmetic, mod P)
ALPHA, BETA = 265391, 275398
rws = [(r['label'], r['row']) for r in p3['inherited_rows']]
for e in p3['new_points']: rws += [('b20_01_p3_pt%d_d11' % e['point'], e['row_d11']), ('b20_01_p3_pt%d_d12' % e['point'], e['row_d12'])]
for pt in cert['points'][75:80]: rws += [(pt['label'] + '_d11', pt['recorded_d11']), (pt['label'] + '_d12', pt['recorded_d12'])]
res = {lab: (r[2] - ALPHA * r[0] - BETA * r[1]) % P for lab, r in rws}
ctrl['c3_recorded_rows'] = dict(rows=len(rws), nonzero=[k for k, v in res.items() if v]); ctrl['c3_pass'] = (len(rws) == 30 and not ctrl['c3_recorded_rows']['nonzero'])
ctrl['all_pass'] = bool(ctrl['c1_pass'] and ctrl['c2_pass'] and ctrl['c3_pass'])
save('stage2_controls_done')
if not ctrl['all_pass']:
    rec['outcome'] = '(c) control failure: no test run'; save('STOP_control_failure'); print(json.dumps(ctrl, default=int)); sys.exit(0)
if left() < 30:
    rec['outcome'] = '(c) insufficient time for the test after controls (%.1f s left)' % left(); save('STOP_time'); sys.exit(0)

# ---------------------------------------------------------------- stage 3: the test at P2
NODES = [1, 2, 3, 4, 5]
test = dict(points=[]); rec['test'] = test
rows6, labels = [], []
for i in range(3):
    pt = cert['points'][i]; assert pt['label'] == 'cert_%02d' % i
    Z1, Z2, Z = [np.array(pt[k], dtype=np.int64) for k in ('Z1', 'Z2', 'Z')]
    raw = {n: [] for n in ORDER}; Ts = {}
    for u in NODES:
        Tt = np.stack([Z1, Z2, Z + u * NU_INT[0], u * NU_INT[1], u * NU_INT[2]]) % P2
        Ts[u] = pr2.c.column_tensor(Tt, 5)
        for n in ORDER: raw[n].append(qval(pr2, 'P2', V[n], Ts[u]))
    co = {n: vander(NODES, raw[n], [8, 9, 10, 11, 12], P2) for n in ORDER}
    d11 = [co[n][11] for n in ORDER]; d12 = [co[n][12] for n in ORDER]
    test['points'].append(dict(label=pt['label'], raw_values_u1_to_5=raw, coefficients={n: {str(k): v for k, v in co[n].items()} for n in ORDER}, d11=d11, d12=d12))
    rows6 += [d11, d12]; labels += ['%s_d11' % pt['label'], '%s_d12' % pt['label']]
    save('stage3_point_%d' % i)
import itertools
minors = []
for tr in itertools.combinations(range(6), 3):
    minors.append(dict(rows=[labels[t] for t in tr], value=det_p([rows6[t] for t in tr], P2)))
test['rows'] = dict(labels=labels, values=rows6)
test['minors'] = minors; test['nonzero_minors'] = [m for m in minors if m['value']]
test['rank_mod_P2'] = rank_p(rows6, P2); test['rank_d11_mod_P2'] = rank_p(rows6[0::2], P2); test['rank_d12_mod_P2'] = rank_p(rows6[1::2], P2)
if test['nonzero_minors']:
    m0 = test['nonzero_minors'][0]
    test['recheck_first_nonzero'] = det_p([rows6[labels.index(l)] for l in m0['rows']], P2)
rec['outcome'] = '(a) nonzero 3x3 minor mod P2' if test['nonzero_minors'] else '(b) all 20 minors vanish mod P2'
save('stage3_test_done')

# ---------------------------------------------------------------- stage 4: descriptive (MEASURED; decides nothing)
desc = {}; rec['descriptive'] = desc
if test['rank_mod_P2'] == 2:
    # relation n02 = a2 q3 + b2 q7 from two independent rows, checked on all six
    pair = next((a, b) for a, b in itertools.combinations(range(6), 2) if det_p([rows6[a][:2], rows6[b][:2]], P2))
    a2, b2 = gauss_solve([rows6[pair[0]][:2], rows6[pair[1]][:2]], [rows6[pair[0]][2], rows6[pair[1]][2]], P2)
    desc['relation_mod_P2'] = dict(alpha2=a2, beta2=b2, residuals=[(r[2] - a2 * r[0] - b2 * r[1]) % P2 for r in rows6])
    desc['d12_ratios_mod_P2'] = [[r[1] * inv(r[0], P2) % P2, r[2] * inv(r[0], P2) % P2] if r[0] else None for r in rows6[1::2]]
    Mod = P * P2
    def crt(x, y): return (x + P * ((y - x) * inv(P, P2) % P2)) % Mod
    def ratrec(a, m):
        bound = math.isqrt(m // 2); r0, r1, s0, s1 = m, a % m, 0, 1
        while r1 > bound: q = r0 // r1; r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
        return (r1 * (1 if s1 > 0 else -1), abs(s1)) if abs(s1) <= bound and s1 and math.gcd(r1, abs(s1)) == 1 else None
    cands = {}
    for nm, x, y in (('alpha', ALPHA, a2), ('beta', BETA, b2)):
        cc = crt(x, y); rr = ratrec(cc, Mod)
        cands[nm] = dict(crt=cc, modulus=Mod, reconstruction=rr,
                         consistent=(rr is not None and (rr[0] - x * rr[1]) % P == 0 and (rr[0] - y * rr[1]) % P2 == 0))
    desc['crt_rational_reconstruction'] = dict(candidates=cands, label='MEASURED candidate only; not a lift, not a proof')
    save('stage4_relation')
if left() > 4:
    pt = cert['points'][0]; Z1, Z2, Z = [np.array(pt[k], dtype=np.int64) for k in ('Z1', 'Z2', 'Z')]
    T6 = pr2.c.column_tensor(np.stack([Z1, Z2, Z + 6 * NU_INT[0], 6 * NU_INT[1], 6 * NU_INT[2]]) % P2, 5)
    six = {}
    for n in ORDER:
        vals = test['points'][0]['raw_values_u1_to_5'][n] + [qval(pr2, 'P2', V[n], T6)]
        co6 = vander([1, 2, 3, 4, 5, 6], vals, [7, 8, 9, 10, 11, 12], P2)
        six[n] = dict(c7=co6[7], c11_equal=(co6[11] == test['points'][0]['d11'][ORDER.index(n)]), c12_equal=(co6[12] == test['points'][0]['d12'][ORDER.index(n)]))
    desc['sixth_node_point0'] = dict(per_vector=six, passes=all(v['c7'] == 0 and v['c11_equal'] and v['c12_equal'] for v in six.values()))
else:
    rec['log'].append('sixth-node check skipped: %.1f s left' % left())
save('done')
print(json.dumps(dict(outcome=rec['outcome'], controls={k: v for k, v in ctrl.items() if k.endswith('pass')}, rank=test['rank_mod_P2'],
                      rank_d11=test['rank_d11_mod_P2'], rank_d12=test['rank_d12_mod_P2'], nonzero=len(test['nonzero_minors']),
                      first_nonzero=(test['nonzero_minors'][0] if test['nonzero_minors'] else None), descriptive=desc,
                      evals=rec['runner_evaluations'], wall=rec['runner_wall_s'], elapsed=rec['elapsed_s']), indent=1, default=int))
