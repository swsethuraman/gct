"""B24-04 pilot 1: the 70 typed eps_3-contraction patterns of B22-01, their multidegree grading,
and whether any further statistic on them grades F^L_{-1}.

Pre-registration: results/b24_04/PREREG_b24_04_p1.md, sha256 e77a79e1... (asserted at stage 0, G25).

Stage 0  pins (B22-01's typed_v2 and p2_basis.json, both bound by its MANIFEST.json at 53bdb31e);
         the 70 certificate points rebuilt from rng(20260922) and compared to the recorded ones (C0).
Stage 1  replay: Xi_h and F_1^h at the 80 recorded points for all 70 selected degree-11 patterns,
         compared to the recorded vec80; the 70 x 70 determinant mod P recomputed (C1).
Stage 2  the multidegree grading: per-block ranks of the selected patterns, and the total rank.
         sum of block ranks == total rank proves the four block spans independent -> a grading.
Stage 3  saturation under a NEW seed 20260919: no block rank may exceed its target (C2).
Stage 4  the eight pre-registered statistics: per block, the profile (j, #{st <= j}, rank), and the
         verdict trivial (lowest class already spans: PROVED negative) / candidate (MEASURED only).

Point evaluation at the 70 certificate points is certified injective on F^L_{-1} (B22-01 sec. 1.2),
so a rank of evaluation vectors IS the dimension of the span.  All arithmetic mod P = 524287.
No runner evaluation.  Producer-only (G18).
"""
import hashlib, json, os, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
T0 = time.perf_counter()
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
import numpy as np

args = sys.argv[1:]
def arg(name, default):
    return args[args.index(name) + 1] if name in args else default
DEADLINE = float(arg('--deadline', '55'))
SAMPLES = int(arg('--samples', '150'))
SAMPLE_SEED = int(arg('--sample-seed', '20260919'))

SCRATCH = Path(os.environ['B24_04_SCRATCH'])       # holds pinned/b22_01_typed_v2.py and p2_basis.json
sys.path.insert(0, str(SCRATCH / 'pinned'))
import b22_01_typed_v2 as ty
P = ty.P

OUTDIR = ROOT / 'results/b24_04'
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / 'p1_patterns.json'
assert not OUT.exists(), 'output exists; runs never overwrite (G10)'

PREREG_SHA = 'e77a79e1a36a03d8075606f01c27d1d987a2eeb766999ad986b2eec31b071519'
PINS = {
    str(SCRATCH / 'pinned' / 'b22_01_typed_v2.py'):
        ('analysis/b22_01_typed_v2.py', '93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc'),
    str(SCRATCH / 'p2_basis.json'):
        ('results/b22_01/p2_basis.json', '7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79'),
}
TARGETS = {'11:1,4,4,0': 7, '11:2,3,3,1': 31, '11:3,2,2,2': 28, '11:4,1,1,3': 4}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def left():
    return DEADLINE - (time.perf_counter() - T0)


rec = dict(pilot='b24_04_p1_patterns', slot='B24-04', prime=P, prereg_sha256=None,
           sample_seed=SAMPLE_SEED, samples_per_block=SAMPLES,
           inputs={}, code={}, log=[], checks={}, stages={})


def save(status):
    rec['status'] = status
    rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')


# ---------------------------------------------------------------- modular linear algebra
def rank_mod(M):
    """Rank mod P of an integer matrix, Gaussian elimination."""
    A = (np.asarray(M, dtype=np.int64) % P).copy()
    if A.size == 0:
        return 0
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        if r == rows:
            break
        piv = np.nonzero(A[r:, c])[0]
        if piv.size == 0:
            continue
        i = r + int(piv[0])
        if i != r:
            A[[r, i]] = A[[i, r]]
        inv = pow(int(A[r, c]), P - 2, P)
        A[r] = A[r] * inv % P
        nz = np.nonzero(A[r + 1:, c])[0]
        if nz.size:
            idx = r + 1 + nz
            A[idx] = (A[idx] - np.outer(A[idx, c], A[r])) % P
        r += 1
    return r


def det_mod(M):
    """Determinant mod P of a square integer matrix."""
    A = (np.asarray(M, dtype=np.int64) % P).copy()
    n = A.shape[0]
    assert A.shape == (n, n)
    det = 1
    for c in range(n):
        piv = np.nonzero(A[c:, c])[0]
        if piv.size == 0:
            return 0
        i = c + int(piv[0])
        if i != c:
            A[[c, i]] = A[[i, c]]
            det = (-det) % P
        det = det * int(A[c, c]) % P
        inv = pow(int(A[c, c]), P - 2, P)
        A[c] = A[c] * inv % P
        nz = np.nonzero(A[c + 1:, c])[0]
        if nz.size:
            idx = c + 1 + nz
            A[idx] = (A[idx] - np.outer(A[idx, c], A[c])) % P
    return det % P


# ---------------------------------------------------------------- the pre-registered statistics
def stats_of(pat):
    """The eight statistics of the pre-registration, from the pattern alone."""
    legs = ty.pattern_legs(pat['kcounts'], [tuple(c) for c in pat['cols']])
    tri = [list(t) for t in pat['triples']]
    col_of = [legs[i][0] for i in range(30)]
    typ_of = [legs[i][2] for i in range(30)]

    s_in = s_sp = s_kk = 0
    for t in tri:
        cs = {col_of[i] for i in t}
        s_in += (len(cs) == 1)
        s_sp += len(cs) - 1
        s_kk += all(typ_of[i] == 'K' for i in t)
    s_nk = 10 - s_kk
    s_rep = sum(1 for c in pat['cols'] if len(set(c)) < len(c))

    # crossing number: pairs of triples A, B with a < b < c < d, a,c in A and b,d in B
    s_cr = 0
    for x in range(len(tri)):
        for y in range(x + 1, len(tri)):
            A, B = sorted(tri[x]), sorted(tri[y])
            cross = False
            for a in A:
                for c in A:
                    if c <= a:
                        continue
                    for b in B:
                        if not (a < b < c):
                            continue
                        for dd in B:
                            if dd > c:
                                cross = True
                                break
                        if cross:
                            break
                    if cross:
                        break
                if cross:
                    break
            if not cross:
                for a in B:
                    for c in B:
                        if c <= a:
                            continue
                        for b in A:
                            if not (a < b < c):
                                continue
                            for dd in A:
                                if dd > c:
                                    cross = True
                                    break
                            if cross:
                                break
                        if cross:
                            break
                    if cross:
                        break
            s_cr += cross

    order = {'a': 0, 'r': 1, 'c': 2, 'S': 3, 'K': 4}
    word = [order[t] for col in pat['cols'] for t in col]
    s_inv = sum(1 for i in range(len(word)) for j in range(i + 1, len(word)) if word[i] > word[j])

    return dict(s_a=int(pat['md'][0]), s_in=int(s_in), s_sp=int(s_sp), s_kk=int(s_kk),
                s_nk=int(s_nk), s_rep=int(s_rep), s_cr=int(s_cr), s_inv=int(s_inv))


STATS = ('s_a', 's_in', 's_sp', 's_kk', 's_nk', 's_rep', 's_cr', 's_inv')

# ---------------------------------------------------------------- stage 0: pins and points
preb = (ROOT / 'results/b24_04/PREREG_b24_04_p1.md').read_bytes()
rec['prereg_sha256'] = sha(preb)
print('PREREG sha256', rec['prereg_sha256'], flush=True)
assert rec['prereg_sha256'] == PREREG_SHA, ('prereg hash', rec['prereg_sha256'])

for path, (rel, want) in PINS.items():
    b = Path(path).read_bytes()
    h = sha(b)
    assert h == want, (rel, h)
    rec['inputs'][rel] = dict(sha256=h, bytes=len(b),
                              bound_by='results/b22_01/MANIFEST.json at 53bdb31e')
rec['code']['analysis/b24_04_p1_patterns.py'] = dict(
    sha256=sha(Path(__file__).read_bytes()), bytes=len(Path(__file__).read_bytes()))

basis = json.loads((SCRATCH / 'p2_basis.json').read_text())


def wprime_random(rng):
    """Verbatim logic of B22-01 pilot 2 stage 0 (itself B20-01 pilot 3's wprime_random)."""
    Z = np.zeros((4, 4), dtype=np.int64)
    Z[0, :] = rng.integers(0, P, size=4)
    Z[1:, 0] = rng.integers(0, P, size=3)
    S = rng.integers(0, P, size=(3, 3))
    S = np.triu(S)
    S = S + np.triu(S, 1).T
    Z[1:, 1:] = S % P
    return Z % P


rng0 = np.random.default_rng(20260922)
CERT = [dict(Z1=wprime_random(rng0), Z2=wprime_random(rng0), Z=wprime_random(rng0)) for _ in range(70)]
recorded = basis['points']
same = all(np.array_equal(np.array(recorded[i][k], dtype=np.int64), CERT[i][k])
           for i in range(70) for k in ('Z1', 'Z2', 'Z'))
rec['checks']['C0_points_rebuilt_equal_recorded'] = bool(same)
assert same, 'certificate points do not reproduce'
ALL = [dict(Z1=np.array(p['Z1'], dtype=np.int64), Z2=np.array(p['Z2'], dtype=np.int64),
            Z=np.array(p['Z'], dtype=np.int64), label=p['label']) for p in recorded]
PS = ty.PointSet(np.stack([p['Z1'] for p in ALL]), np.stack([p['Z2'] for p in ALL]),
                 np.stack([p['Z'] for p in ALL]))
rec['stages']['s0'] = dict(n_points=len(ALL), n_cert=70)
save('s0')

# ---------------------------------------------------------------- stage 1: replay the 70 (C1)
sel11 = [s for s in basis['selected'] if s['pattern']['deg'] == 11]
assert len(sel11) == 70, len(sel11)

vecs, mismatches = [], []
t1 = time.perf_counter()
for k, s in enumerate(sel11):
    v = ty.evaluate(s['pattern'], PS)
    v = [int(x) % P for x in v]
    if v != [int(x) % P for x in s['vec80']]:
        mismatches.append(k)
    vecs.append(v)
V = np.array(vecs, dtype=np.int64)            # 70 patterns x 80 points
E = V[:, :70].T                               # points x patterns, as B22-01 built it
d70 = det_mod(E)
rec['checks']['C1_vec80_reproduced_all_70'] = (len(mismatches) == 0)
rec['checks']['C1_mismatched_indices'] = mismatches
rec['checks']['C1_det70_nonzero'] = bool(d70 != 0)
rec['stages']['s1'] = dict(det70_mod_P=int(d70), replay_wall_s=round(time.perf_counter() - t1, 3),
                           n_replayed=len(sel11))
assert not mismatches, mismatches
assert d70 != 0
save('s1')

# ---------------------------------------------------------------- stage 2: the multidegree grading
by_block = {}
for s, v in zip(sel11, vecs):
    by_block.setdefault(s['block'], []).append((s['pattern'], v))
block_rank = {b: rank_mod(np.array([v for _, v in lst], dtype=np.int64)[:, :70])
              for b, lst in by_block.items()}
total_rank = rank_mod(V[:, :70])
rec['stages']['s2'] = dict(
    block_sizes={b: len(l) for b, l in by_block.items()},
    block_ranks=block_rank, targets=TARGETS, total_rank=int(total_rank),
    sum_of_block_ranks=int(sum(block_rank.values())),
    direct_sum=bool(sum(block_rank.values()) == total_rank == 70),
    graded_dimensions_by_s_a={str(5 - int(b.split(':')[1].split(',')[1])): block_rank[b]
                              for b in block_rank})
save('s2')

# ---------------------------------------------------------------- stage 3: saturation, new seed
rng = np.random.default_rng(SAMPLE_SEED)
pool = {b: [(pat, v, stats_of(pat)) for pat, v in l] for b, l in by_block.items()}   # pattern, vec, stats
sample_log = {b: dict(attempts=0, none=0, zero_xi=0, guard_skip=0, kept=0) for b in TARGETS}
BLOCK_MD = {'11:1,4,4,0': (1, 4, 4, 0), '11:2,3,3,1': (2, 3, 3, 1),
            '11:3,2,2,2': (3, 2, 2, 2), '11:4,1,1,3': (4, 1, 1, 3)}
violation = []
for b, md in BLOCK_MD.items():
    for _ in range(SAMPLES):
        if left() < 14:
            rec['log'].append('deadline: stopped sampling in %s' % b)
            break
        sample_log[b]['attempts'] += 1
        pat = ty.random_pattern(rng, md, 11)
        if pat is None:
            sample_log[b]['none'] += 1
            continue
        try:
            xi = ty.xi_tensor(pat)
        except AssertionError as exc:
            sample_log[b]['guard_skip'] += 1
            rec['log'].append('guard skip %s: %r' % (b, exc))
            continue
        if not np.any(xi % P):
            sample_log[b]['zero_xi'] += 1
            continue
        try:
            v = [int(x) % P for x in ty.evaluate(pat, PS, xi=xi)]
        except AssertionError as exc:
            sample_log[b]['guard_skip'] += 1
            rec['log'].append('guard skip eval %s: %r' % (b, exc))
            continue
        if not any(v[:70]):
            sample_log[b]['zero_xi'] += 1
            continue
        sample_log[b]['kept'] += 1
        pool[b].append((pat, v, stats_of(pat)))
    r = rank_mod(np.array([v for _, v, _ in pool[b]], dtype=np.int64)[:, :70])
    if r > TARGETS[b]:
        violation.append((b, r, TARGETS[b]))
    sample_log[b]['pool_rank'] = int(r)
    sample_log[b]['pool_size'] = len(pool[b])
rec['stages']['s3'] = dict(sampling=sample_log, violation=violation,
                           block_dimension_confirmed={b: bool(sample_log[b]['pool_rank'] == TARGETS[b])
                                                      for b in TARGETS})
assert not violation, violation
save('s3')

# ---------------------------------------------------------------- stage 4: the statistics
selected_stats = [dict(block=s['block'], **stats_of(s['pattern'])) for s in sel11]
rec['stages']['s4_the_70'] = selected_stats

profiles = {}
for b in TARGETS:
    pats = pool[b]
    st = [x for _, _, x in pats]
    M = np.array([v for _, v, _ in pats], dtype=np.int64)[:, :70]
    dim = TARGETS[b]
    prof = {}
    for name in STATS:
        vals = sorted({x[name] for x in st})
        rows = []
        for j in vals:
            idx = [i for i, x in enumerate(st) if x[name] <= j]
            rows.append(dict(j=int(j), n=len(idx), rank=int(rank_mod(M[idx]))))
        low = rows[0]
        prof[name] = dict(values=vals, profile=rows, block_dim=dim,
                          lowest_class_spans=bool(low['rank'] == dim),
                          verdict=('trivial (PROVED: lowest class already spans the block)'
                                   if low['rank'] == dim else
                                   'candidate (MEASURED: sampled rank below the block dimension)'),
                          distinct_ranks=len({r['rank'] for r in rows}))
    profiles[b] = prof
rec['stages']['s4_profiles'] = profiles

# cross-block: does any statistic grade all of F^L_{-1} beyond s_a?
allpats = [x for b in TARGETS for x in pool[b]]
Mall = np.array([v for _, v, _ in allpats], dtype=np.int64)[:, :70]
stall = [x for _, _, x in allpats]
whole = {}
for name in STATS:
    vals = sorted({x[name] for x in stall})
    rows = []
    for j in vals:
        idx = [i for i, x in enumerate(stall) if x[name] <= j]
        rows.append(dict(j=int(j), n=len(idx), rank=int(rank_mod(Mall[idx]))))
    whole[name] = dict(profile=rows, ambient_dim=70,
                       graded=[rows[0]['rank']] + [rows[i]['rank'] - rows[i - 1]['rank']
                                                   for i in range(1, len(rows))],
                       proper=bool(len({r['rank'] for r in rows}) > 1),
                       reaches_70=bool(rows[-1]['rank'] == 70))
rec['stages']['s4_whole_space'] = whole
save('done')
print(json.dumps({'elapsed_s': rec['elapsed_s'], 'status': rec['status']}), flush=True)
