"""B22-01 pilot 2: the Missing Theorem's certificate (docs/b22_01_report.md sec. 1.2), after pilot 1.

Identical to analysis/b22_01_p1_basis.py (sha256 3b3c6a26...) except: it imports b22_01_typed_v2 (the fixed
mod_einsum); it resumes from pilot 1's kept patterns and records, per pattern, whether the fixed code
reproduces pilot 1's 80-point vector (a cross-check of two contraction orders); default output p2_basis.json.

Stage 0  pins; the 70 certificate points (rng 20260922, B20-01 pilot 3's wprime_random) and the 10
         recorded flag points (B20-01 pilot 3: 5; B21-01: 5), 80 in all.
Stage 1  search: random typed eps_3 patterns per multidegree block (rng --pattern-seed); Xi_h exact;
         F_1^h (degree 11) or top^h (degree 12) at the 80 points; a pattern is kept iff it raises the rank
         of the 70-point matrix; every nonzero pattern is also tested against its block's 80-point rank,
         which must never exceed the proved target (7, 31, 28, 4 | 1, 2, 1).  A violation stops the pilot.
Stage 2  certificate: det of the 70 x 70 matrix [F_1^{h_j}(p_i)] mod P by two eliminations (own; B20-01's
         det_mod); the 70 x 4 top matrix: rank and a nonzero 4 x 4 minor.
Stage 3  saturation probes (MEASURED): further random patterns per block, block ranks re-tested.
Stage 4  controls, deadline-guarded: Claim S(iii) (structured value = brute-force [u^11] / [u^12] of the
         full network at five u-nodes, other coefficients zero); L-invariance at a general 5-tuple, with a
         teeth check (beta doubled multiplies h by 2^{#a+#c} = 32).
No runner evaluation.  JSON written after every stage.  Producer-only (G18)."""
import hashlib, json, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
T0 = time.perf_counter()
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import numpy as np
import b22_01_typed_v2 as ty
P = ty.P

args = sys.argv[1:]
def arg(name, default):
    return args[args.index(name) + 1] if name in args else default
OUTNAME = arg('--out', 'p2_basis.json'); RESUME = arg('--resume', None)
PSEED = int(arg('--pattern-seed', '20260925')); DEADLINE = float(arg('--deadline', '55'))
SEARCH_END = DEADLINE - 20.0
OUTDIR = ROOT / 'results/b22_01'; OUTDIR.mkdir(parents=True, exist_ok=True); OUT = OUTDIR / OUTNAME
assert not OUT.exists(), 'output exists; runs never overwrite (G10)'


def sha(b): return hashlib.sha256(b).hexdigest()
def left(): return DEADLINE - (time.perf_counter() - T0)


PINS = {'analysis/b20_01_flag.py': '3236c78700872975497c8ef37d5eefde17f617a0dfdac302d6558c85454ae27a',
        'results/b20_01/p3_flag_rows.json': '73c3be3c0789d26001953f940792c9086ce19fc72d758566f5bea2c86ece66ee',
        'results/b21_01/p1_type_test.json': 'b6d047377cf4c3b082aea9d53a0a93d5ca4f4cf9677131813bc484ad69b0fa2e'}
rec = dict(pilot='b22_01_p2_basis', out=OUTNAME, prime=P, point_seed=20260922, pattern_seed=PSEED, resume=RESUME,
           inputs={}, code={}, log=[], counts={}, checks={})
for rel, want in PINS.items():
    b = (ROOT / rel).read_bytes(); h = sha(b); assert h == want, (rel, h)
    rec['inputs'][rel] = dict(sha256=h, bytes=len(b), bound_by='results/b20_01/MANIFEST.json 0e5fd026' if 'b20_01' in rel else 'results/b21_01/MANIFEST.json 1944b24d')
for rel in ('analysis/b22_01_typed_v2.py', 'analysis/b22_01_p2_basis.py', 'analysis/b22_01_typed.py', 'analysis/b22_01_p1_basis.py'):
    b = (ROOT / rel).read_bytes(); rec['code'][rel] = dict(sha256=sha(b), bytes=len(b))
import b20_01_flag as fl
assert fl.P == P
rec['checks']['nu_equal_b20_01_flag'] = all(np.array_equal(a % P, b % P) for a, b in zip(ty.NU, fl.NU))
assert rec['checks']['nu_equal_b20_01_flag']


def save(status):
    rec['status'] = status; rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')


# ---------------------------------------------------------------- stage 0: points
def wprime_random(rng):
    """Verbatim logic of analysis/b20_01_p3_flag_rows.py wprime_random."""
    Z = np.zeros((4, 4), dtype=np.int64)
    Z[0, :] = rng.integers(0, P, size=4); Z[1:, 0] = rng.integers(0, P, size=3)
    S = rng.integers(0, P, size=(3, 3)); S = np.triu(S); S = S + np.triu(S, 1).T
    Z[1:, 1:] = S % P
    return Z % P


rng = np.random.default_rng(20260922)
PTS = []
for i in range(70):
    Z1, Z2, Z = wprime_random(rng), wprime_random(rng), wprime_random(rng)
    PTS.append(dict(label='cert_%02d' % i, Z1=Z1, Z2=Z2, Z=Z))
p3 = json.loads((ROOT / 'results/b20_01/p3_flag_rows.json').read_text())
for e in p3['new_points']:
    PTS.append(dict(label='b20_01_p3_pt%d' % e['point'], Z1=np.array(e['Z1']), Z2=np.array(e['Z2']), Z=np.array(e['Z']),
                    recorded_d11=e['row_d11'], recorded_d12=e['row_d12']))
t1 = json.loads((ROOT / 'results/b21_01/p1_type_test.json').read_text())
for e in t1['points']:
    PTS.append(dict(label='b21_01_' + e['label'], Z1=np.array(e['Z']['Z1']), Z2=np.array(e['Z']['Z2']), Z=np.array(e['Z']['Z']),
                    recorded_d11=[e['direct_form']['z11'][k] for k in ('q3', 'q7', 'n02')],
                    recorded_d12=[e['direct_form']['z12'][k] for k in ('q3', 'q7', 'n02')]))
assert len(PTS) == 80
for p in PTS:
    for k in ('Z1', 'Z2', 'Z'):
        M = np.asarray(p[k], dtype=np.int64) % P
        assert np.array_equal(M[1:, 1:], M[1:, 1:].T), ('point not in W-prime', p['label'], k)
rec['points'] = [{k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in p.items()} for p in PTS]
ps = ty.PointSet(np.stack([p['Z1'] for p in PTS]), np.stack([p['Z2'] for p in PTS]), np.stack([p['Z'] for p in PTS]))
save('stage0_points')

# ---------------------------------------------------------------- stage 1: search
TARGET = {(11,) + md: d for md, d in ty.BLOCKS11.items()}
TARGET.update({(12,) + md: d for md, d in ty.BLOCKS12.items()})
KEYS = list(TARGET)
blk80 = {k: ty.Echelon(80) for k in KEYS}
comb = {11: ty.Echelon(70), 12: ty.Echelon(70)}
kept = {k: [] for k in KEYS}
stats = {k: dict(attempts=0, rejected_by_rule=0, zero_xi=0, zero_function=0, block_rank_raises=0, kept=0,
                 raised_block_not_comb=0, xi_wall_s=0.0, eval_wall_s=0.0) for k in KEYS}
violation = []


def key_str(k): return '%d:%s' % (k[0], ','.join(map(str, k[1:])))


def try_pattern(k, pat, phase):
    try:
        _try_pattern(k, pat, phase)
    except AssertionError as exc:                 # a guard in mod_einsum; recorded and counted, pattern skipped
        stats[k].setdefault('guard_skips', 0); stats[k]['guard_skips'] += 1
        if len(rec['log']) < 20: rec['log'].append('guard skip %s: %r' % (key_str(k), exc))


def _try_pattern(k, pat, phase):
    st = stats[k]
    t = time.perf_counter(); xi = ty.xi_tensor(pat); st['xi_wall_s'] += time.perf_counter() - t
    if not xi.any(): st['zero_xi'] += 1; return
    t = time.perf_counter(); vec = ty.evaluate(pat, ps, xi); st['eval_wall_s'] += time.perf_counter() - t
    if not vec.any(): st['zero_function'] += 1; return
    if blk80[k].add(vec):
        st['block_rank_raises'] += 1
        if len(blk80[k].rows) > TARGET[k]:
            violation.append(dict(block=key_str(k), phase=phase, rank=len(blk80[k].rows), target=TARGET[k], pattern=pat))
            return
        if phase == 'search':
            if comb[k[0]].add(vec[:70]):
                kept[k].append(dict(pattern=pat, vec80=[int(x) for x in vec])); st['kept'] += 1
            else:
                st['raised_block_not_comb'] += 1


if RESUME:
    old = json.loads((ROOT / RESUME).read_text())
    rec['resume_sha256'] = sha((ROOT / RESUME).read_bytes())
    rec['resume_vec80_reproduced'] = []
    for s in old.get('selected', []):
        k = tuple(s['block_key']); pat = s['pattern']
        stats[k]['attempts'] += 1; nk = len(kept[k]); try_pattern(k, pat, 'search')
        rec['resume_vec80_reproduced'].append(bool(len(kept[k]) > nk and kept[k][-1]['vec80'] == s['vec80']))
    rec['log'].append('resumed %d patterns from %s' % (len(old.get('selected', [])), RESUME))

prng = np.random.default_rng(PSEED)
rr = 0
while not violation and time.perf_counter() - T0 < SEARCH_END:
    open_keys = [k for k in KEYS if stats[k]['kept'] < TARGET[k] and len(blk80[k].rows) <= TARGET[k]
                 and not (len(blk80[k].rows) == TARGET[k] and stats[k]['kept'] < TARGET[k])]
    if not open_keys: break
    k = open_keys[rr % len(open_keys)]; rr += 1
    stats[k]['attempts'] += 1
    pat = ty.random_pattern(prng, k[1:], k[0])
    if pat is None: stats[k]['rejected_by_rule'] += 1; continue
    try_pattern(k, pat, 'search')


def summarise():
    rec['counts'] = {key_str(k): dict(stats[k], target=TARGET[k], block_rank_80=len(blk80[k].rows),
                                      xi_wall_s=round(stats[k]['xi_wall_s'], 3), eval_wall_s=round(stats[k]['eval_wall_s'], 3)) for k in KEYS}
    rec['rank70'] = {11: len(comb[11].rows), 12: len(comb[12].rows)}
    rec['selected'] = [dict(block_key=list(k), block=key_str(k), pattern=s['pattern'], vec80=s['vec80']) for k in KEYS for s in kept[k]]
    rec['violation'] = violation
    stuck = [key_str(k) for k in KEYS if len(blk80[k].rows) == TARGET[k] and stats[k]['kept'] < TARGET[k]]
    rec['points_degenerate_for_block'] = stuck


summarise(); rec['search_wall_s'] = round(time.perf_counter() - T0, 3)
save('stage1_search' + ('_VIOLATION' if violation else ''))
if violation:
    rec['verdict'] = 'STOP: a block rank exceeded its proved target (transcription sentence 2 branch)'; save('STOP_violation'); sys.exit(0)

# ---------------------------------------------------------------- stage 2: certificate
sel11 = [s for k in KEYS if k[0] == 11 for s in kept[k]]; sel12 = [s for k in KEYS if k[0] == 12 for s in kept[k]]
cert = dict(n11=len(sel11), n12=len(sel12))
if len(sel11) == 70:
    E = [[sel11[j]['vec80'][i] for j in range(70)] for i in range(70)]    # rows = points, columns = patterns
    d1 = ty.det_rows(E); d2 = fl.det_mod(E); r2 = fl.rank_mod(E)
    cert.update(det_own=d1, det_b20_01_flag=d2, dets_agree=(d1 == d2), rank_b20_01_flag=r2,
                certified_injective_V70=bool(d1 != 0 and d1 == d2 and r2 == 70), E_rows_points_cols_patterns=E)
if len(sel12) == 4:
    Tm = [[sel12[j]['vec80'][i] for j in range(4)] for i in range(70)]
    ech = ty.Echelon(4); rows = []
    for i in range(70):
        if ech.add(Tm[i]): rows.append(i)
        if len(rows) == 4: break
    m4 = [Tm[i] for i in rows]
    cert.update(top_rank=fl.rank_mod(Tm), top_minor_rows=rows, top_minor_det_own=ty.det_rows(m4), top_minor_det_b20_01_flag=fl.det_mod(m4),
                certified_injective_top=bool(len(rows) == 4 and ty.det_rows(m4) != 0 and ty.det_rows(m4) == fl.det_mod(m4)))
rec['certificate'] = cert
save('stage2_certificate')

# ---------------------------------------------------------------- stage 3: saturation probes (MEASURED)
sat_end = min(time.perf_counter() - T0 + 3.0, DEADLINE - 16.0)
sat = {key_str(k): 0 for k in KEYS}
while not violation and time.perf_counter() - T0 < sat_end:
    k = KEYS[rr % len(KEYS)]; rr += 1
    pat = ty.random_pattern(prng, k[1:], k[0])
    if pat is None: continue
    before = stats[k]['zero_xi'] + stats[k]['zero_function']
    try_pattern(k, pat, 'saturation')
    if stats[k]['zero_xi'] + stats[k]['zero_function'] == before: sat[key_str(k)] += 1
rec['saturation_nonzero_patterns_tested'] = sat
summarise(); save('stage3_saturation' + ('_VIOLATION' if violation else ''))
if violation:
    rec['verdict'] = 'STOP: a block rank exceeded its proved target in the saturation probes'; save('STOP_violation'); sys.exit(0)

# ---------------------------------------------------------------- stage 4: controls (deadline-guarded)
ctrl = {}
NODES = [1, 2, 3, 4, 5]
def claim_s_check(s, deg):
    pat = s['pattern']; p = PTS[0]; vals = []
    for u in NODES:
        vals.append(ty.brute_value(pat, ty.flag_tuple(p['Z1'], p['Z2'], p['Z'], u)))
    co = fl.vandermonde_solve(NODES, vals, [8, 9, 10, 11, 12])
    want = s['vec80'][0]
    other = [d for d in (8, 9, 10, 11, 12) if d != deg]
    return dict(block=pat['md'], deg=deg, coefficients={str(d): co[d] for d in co}, structured=want,
                match=(co[deg] == want), others_zero=all(co[d] == 0 for d in other))
rec['controls'] = ctrl
def guarded(name, fn):
    t = time.perf_counter()
    try:
        ctrl[name] = fn()
    except Exception as exc:                                    # recorded, never swallowed silently
        ctrl[name] = dict(exception=repr(exc))
    ctrl[name]['wall_s'] = round(time.perf_counter() - t, 3); save('stage4_' + name)
def l_invariance():
    r2g = np.random.default_rng(20260924)
    Y = r2g.integers(0, P, size=(5, 4, 4), dtype=np.int64)
    while True:
        g = r2g.integers(0, P, size=(3, 3), dtype=np.int64); dg = fl.det_mod(g.tolist())
        if dg: break
    al, cc = int(r2g.integers(1, P)), int(r2g.integers(1, P))
    be = ty.inv_mod(al * pow(cc, 3, P) % P * pow(dg, 2, P) % P)
    def act(Y, beta):
        A = np.zeros((4, 4), dtype=np.int64); B = np.zeros((4, 4), dtype=np.int64)
        A[0, 0] = al; A[1:, 1:] = g; B[0, 0] = beta; B[1:, 1:] = (cc * g.T) % P
        return np.stack([((A @ Y[m]) % P @ B) % P for m in range(5)])
    pat = sel11[0]['pattern']
    h0 = ty.brute_value(pat, Y); h1 = ty.brute_value(pat, act(Y, be))
    out = dict(block=pat['md'], character_check=(al * be % P * pow(cc, 3, P) % P * pow(dg, 2, P) % P), h_Y=h0, h_lY=h1, invariant=(h0 == h1))
    if left() > 5:
        h2 = ty.brute_value(pat, act(Y, 2 * be % P))
        out.update(h_beta_doubled=h2, expected=32 * h0 % P, teeth=(h2 == 32 * h0 % P and h2 != h0))
    return out
if sel11 and left() > 12: guarded('claim_S_iii_degree11', lambda: claim_s_check(sel11[0], 11))
if sel12 and left() > 12: guarded('claim_S_iii_degree12', lambda: claim_s_check(sel12[0], 12))
if sel11 and left() > 10: guarded('L_invariance', l_invariance)
ok = cert.get('certified_injective_V70') and cert.get('certified_injective_top')
rec['verdict'] = ('CERTIFIED: 70 patterns with det != 0 mod P at the 70 points; 4 top patterns with a nonzero 4x4 minor'
                  if ok else 'NOT certified in this launch: rank70 = %s' % rec['rank70'])
save('done')
print(json.dumps(dict(status=rec['status'], verdict=rec['verdict'], rank70=rec['rank70'],
                      counts={k: (v['block_rank_80'], v['target'], v['kept'], v['attempts']) for k, v in rec['counts'].items()},
                      det=cert.get('det_own'), det2=cert.get('det_b20_01_flag'), top=cert.get('top_minor_det_own'),
                      controls={k: {kk: vv for kk, vv in v.items() if kk in ('match', 'others_zero', 'invariant', 'teeth', 'wall_s')} if isinstance(v, dict) else v for k, v in ctrl.items()},
                      elapsed=rec['elapsed_s']), indent=1, default=int))
