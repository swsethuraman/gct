"""B24-04 pilot 3 (last of the slot's budget): close pilot 2's one open class, and control the
counting half of the Question 1 theorem.

Pre-registration: results/b24_04/PREREG_b24_04_p3.md, sha256 7b52ea97... (asserted, G25).
Pilots 1 and 2 outputs pinned by sha256 e43e7412... and 1819b8f3... .

Part A  the class (block 11:1,4,4,0, s_rep <= 0) sampled DIRECTLY from its rigid family
        (cols[0] a permutation of (a,r,c); cols[1..3] permutations of (r,c)), seed 20260921.
Part B  N_S by dynamic programming, calibrated against B23-06's independently produced
        553 / 621 / 641; the factorisation checked by literal enumeration on two small cells;
        and the stable N_S as a function of the tail size t (the price of the Q1 theorem).

No runner evaluation.  Producer-only (G18).
"""
import hashlib, itertools, json, os, sys, time
from collections import defaultdict
from pathlib import Path
sys.dont_write_bytecode = True
T0 = time.perf_counter()
ROOT = Path(__file__).resolve().parent.parent
import numpy as np

args = sys.argv[1:]
def arg(name, default):
    return args[args.index(name) + 1] if name in args else default
DEADLINE = float(arg('--deadline', '55'))
A_BUDGET = float(arg('--a-budget', '26'))
SEED = int(arg('--seed', '20260921'))

SCRATCH = Path(os.environ['B24_04_SCRATCH'])
sys.path.insert(0, str(SCRATCH / 'pinned'))
import b22_01_typed_v2 as ty
P = ty.P

# same single source for the statistics and the linear algebra as pilot 2 (see its comment)
_P1SRC = (Path(__file__).resolve().parent / 'b24_04_p1_patterns.py').read_text()
_MARK = '# ---------------------------------------------------------------- stage 0: pins and points'
_LIN = '# ---------------------------------------------------------------- modular linear algebra'
_NS = {'np': np, 'ty': ty, 'P': P, 'sys': sys, 'os': os, 'json': json, 'time': time,
       'hashlib': hashlib, 'Path': Path, '__file__': __file__, '__name__': 'b24_04_p1_defs'}
exec(compile(_P1SRC.split(_MARK)[0].split('args = sys.argv')[0] +
             _P1SRC.split(_LIN)[1].split(_MARK)[0], 'b24_04_p1_patterns.py:prefix', 'exec'), _NS)
stats_of, rank_mod = _NS['stats_of'], _NS['rank_mod']

OUT = ROOT / 'results/b24_04/p3_close.json'
assert not OUT.exists(), 'output exists; runs never overwrite (G10)'

PREREG_SHA = '7b52ea97be3732eb3a4166206bfa5ff13c3169d950dc0e45c4d9ab0078de46d8'
P1_SHA = 'e43e7412cf92970e1a290854f350368621bb7a652be4f31d33c4bc4a07a12421'
P2_SHA = '1819b8f3fbed9938092a7be83924c8dd2f361f6f9d0fc2e7d3f1b11f44246c5c'
TYPED_SHA = '93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc'
BASIS_SHA = '7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def left():
    return DEADLINE - (time.perf_counter() - T0)


rec = dict(pilot='b24_04_p3_close', slot='B24-04', prime=P, seed=SEED, inputs={}, code={}, log={})


def save(status):
    rec['status'] = status
    rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')


for rel, want in (('results/b24_04/PREREG_b24_04_p3.md', PREREG_SHA),
                  ('results/b24_04/p1_patterns.json', P1_SHA),
                  ('results/b24_04/p2_saturate.json', P2_SHA)):
    h = sha((ROOT / rel).read_bytes())
    print(rel, h, flush=True)
    assert h == want, (rel, h)
    rec['inputs'][rel] = dict(sha256=h)
for path, rel, want in ((SCRATCH / 'pinned' / 'b22_01_typed_v2.py', 'analysis/b22_01_typed_v2.py', TYPED_SHA),
                        (SCRATCH / 'p2_basis.json', 'results/b22_01/p2_basis.json', BASIS_SHA)):
    h = sha(Path(path).read_bytes())
    assert h == want, (rel, h)
    rec['inputs'][rel] = dict(sha256=h, bound_by='results/b22_01/MANIFEST.json at 53bdb31e')
for rel in ('analysis/b24_04_p1_patterns.py', 'analysis/b24_04_p3_close.py'):
    b = (ROOT / rel).read_bytes()
    rec['code'][rel] = dict(sha256=sha(b), bytes=len(b))
save('pins')

# ================================================================= Part A
basis = json.loads((SCRATCH / 'p2_basis.json').read_text())
pts = basis['points'][:70]
assert [q['label'] for q in pts] == ['cert_%02d' % i for i in range(70)]
PS = ty.PointSet(np.array([q['Z1'] for q in pts], dtype=np.int64),
                 np.array([q['Z2'] for q in pts], dtype=np.int64),
                 np.array([q['Z'] for q in pts], dtype=np.int64))

KC = [2, 3, 3, 3]
COL0 = [list(p) for p in itertools.permutations(('a', 'r', 'c'))]
COLJ = [list(p) for p in itertools.permutations(('r', 'c'))]
rng = np.random.default_rng(SEED)
t_end = time.perf_counter() + A_BUDGET
rows, accepted, drawn, zero, guard, since_rise, rank = [], 0, 0, 0, 0, 0, 0
stop = None
while True:
    if rank >= 7:
        stop = 'rank reached the block dimension'
        break
    if accepted >= 2500:
        stop = 'accepted cap'
        break
    if since_rise >= 600:
        stop = 'stalled'
        break
    if time.perf_counter() > t_end or left() < 20:
        stop = 'deadline'
        break
    drawn += 1
    cols = [COL0[int(rng.integers(6))]] + [COLJ[int(rng.integers(2))] for _ in range(3)]
    legs = ty.pattern_legs(KC, [tuple(c) for c in cols])
    assert len(legs) == 30
    perm = [int(x) for x in rng.permutation(30)]
    pat = dict(deg=11, md=[1, 4, 4, 0], kcounts=KC, cols=cols,
               triples=[sorted(perm[3 * i:3 * i + 3]) for i in range(10)])
    assert stats_of(pat)['s_rep'] == 0 and stats_of(pat)['s_a'] == 1
    try:
        xi = ty.xi_tensor(pat)
        if not np.any(xi % P):
            zero += 1
            continue
        v = [int(x) % P for x in ty.evaluate(pat, PS, xi=xi)]
    except AssertionError as exc:
        guard += 1
        rec['log'].setdefault('A_guard', []).append(repr(exc))
        continue
    if not any(v):
        zero += 1
        continue
    accepted += 1
    rows.append(v)
    if accepted % 50 == 0 or accepted <= 10:
        new = rank_mod(np.array(rows, dtype=np.int64))
        since_rise = 0 if new > rank else since_rise + 50
        rank = new
rank = max(rank, rank_mod(np.array(rows, dtype=np.int64))) if rows else 0
rec['partA'] = dict(block='11:1,4,4,0', statistic='s_rep', threshold=0, block_dim=7,
                    family='cols[0] in perms(a,r,c); cols[1..3] in perms(r,c); triples free',
                    drawn=drawn, accepted=accepted, zero_function=zero, guard_skip=guard,
                    rank=int(rank), stopped_by=stop,
                    verdict=('trivial (PROVED: the class spans the whole block)' if rank >= 7 else
                             'UNDECIDED (deadline)' if stop == 'deadline' else
                             'candidate, MEASURED only: codimension %d in one 7-dimensional block'
                             % (7 - rank)),
                    pilot2_saw=dict(accepted=126, rank=6))
save('partA')
print(json.dumps(rec['partA']), flush=True)

# ================================================================= Part B
def tails(n, r):
    """Nonzero exponent tails alphabar in Z_{>=0}^{r-1} with |alphabar| <= n."""
    out = []
    for v in itertools.product(range(n + 1), repeat=r - 1):
        if 0 < sum(v) <= n:
            out.append(v)
    return out


def NS(n, r, lam_bar, d):
    """# multisets of at most d elements of tails(n,r) summing to lam_bar.

    d=None is the STABLE value: every part has |alphabar| >= 1, so a multiset summing to lam_bar
    has at most t = |lam_bar| elements and the size cap is never binding.  The element counter is
    then dropped, which is what makes the t = 18..24 rows affordable."""
    parts = [v for v in tails(n, r) if all(v[i] <= lam_bar[i] for i in range(len(lam_bar)))]
    L = len(lam_bar)
    zero = tuple(0 for _ in lam_bar)
    if d is None:
        cur = {zero: 1}
        for v in parts:
            nxt = defaultdict(int)
            for tgt, c in cur.items():
                t2 = tgt
                while True:
                    nxt[t2] += c
                    t2 = tuple(t2[i] + v[i] for i in range(L))
                    if any(t2[i] > lam_bar[i] for i in range(L)):
                        break
            cur = nxt
        return cur.get(tuple(lam_bar), 0)
    cur = {(zero, 0): 1}
    for v in parts:
        nxt = defaultdict(int)
        for (tgt, k), c in cur.items():
            t2, k2 = tgt, k
            while True:
                nxt[(t2, k2)] += c
                t2 = tuple(t2[i] + v[i] for i in range(L))
                k2 += 1
                if k2 > d or any(t2[i] > lam_bar[i] for i in range(L)):
                    break
        cur = nxt
    return sum(c for (tgt, k), c in cur.items() if tgt == tuple(lam_bar))


B = dict()
# --- C1 calibration against B23-06 §2.3 (produced independently, at feed104e)
cal = {}
for n, want in ((4, 553), (5, 621), (6, 641)):
    got = NS(n, 5, (2, 2, 2, 2), 5)
    cal['n=%d r=5 lambdabar=(2,2,2,2) d=5' % n] = dict(got=int(got), b23_06=want, agree=bool(got == want))
B['C1_calibration'] = cal
save('partB-C1')

# --- C2 the factorisation, by literal enumeration (independent of the DP)
def vectors(n, r):
    return [v for v in itertools.product(range(n + 1), repeat=r) if sum(v) == n]


c2 = {}
for (n, r, d, lb) in ((3, 3, 5, (1, 1)), (3, 4, 6, (1, 1, 1))):
    t = sum(lb)
    lam = (n * d - t,) + lb
    V = vectors(n, r)
    e1 = tuple([n] + [0] * (r - 1))
    mons, min_e1 = 0, None
    for ms in itertools.combinations_with_replacement(range(len(V)), d):
        s = [0] * r
        for i in ms:
            for j in range(r):
                s[j] += V[i][j]
        if tuple(s) != lam:
            continue
        mons += 1
        k = sum(1 for i in ms if V[i] == e1)
        min_e1 = k if min_e1 is None else min(min_e1, k)
    mu_bar = lb
    at_t = NS(n, r, mu_bar, t)
    c2['n=%d r=%d d=%d lambdabar=%s' % (n, r, d, lb)] = dict(
        lam=list(lam), t=t, d=d, monomials_at_d=int(mons),
        min_multiplicity_of_n_e1=(None if min_e1 is None else int(min_e1)),
        required_d_minus_t=d - t,
        divisibility_holds=bool(min_e1 is not None and min_e1 >= d - t),
        count_at_degree_t=int(at_t), counts_agree=bool(mons == at_t))
    if left() < 10:
        rec['log'].setdefault('B', []).append('deadline inside C2')
        break
B['C2_factorisation_by_enumeration'] = c2
save('partB-C2')

# --- C3 the price: stable N_S (d >= t) against the tail size t
def four_part(t):
    out = []
    for a in range(1, t + 1):
        for b in range(1, min(a, t) + 1):
            for c in range(1, min(b, t) + 1):
                e = t - a - b - c
                if 1 <= e <= c:
                    out.append((a, b, c, e))
    return out


price, deadline_hit = {}, False
for t in range(4, 17):
    if left() < 8:
        deadline_hit = True
        break
    shapes = four_part(t)
    vals = {}
    for lb in shapes:
        if left() < 6:
            deadline_hit = True
            break
        vals[str(lb)] = int(NS(5, 5, lb, None))
    if not vals:
        break
    mn = min(vals.values())
    price[str(t)] = dict(shapes_evaluated=len(vals), all_shapes=len(shapes),
                         min_over_evaluated=mn,
                         argmin=[k for k, v in vals.items() if v == mn][0],
                         max_over_evaluated=max(vals.values()))
for t in (18, 20, 22, 24):
    if left() < 8:
        deadline_hit = True
        break
    lbs = [(t - 3, 1, 1, 1), tuple(sorted([t // 4 + (1 if i < t % 4 else 0) for i in range(4)], reverse=True))]
    vals = {}
    for lb in lbs:
        if sum(lb) != t or min(lb) < 1 or left() < 6:
            continue
        vals[str(lb)] = int(NS(5, 5, lb, None))
    if vals:
        price[str(t)] = dict(shapes_evaluated=len(vals), all_shapes=len(four_part(t)),
                             min_over_evaluated=min(vals.values()),
                             argmin=[k for k, v in vals.items() if v == min(vals.values())][0],
                             max_over_evaluated=max(vals.values()),
                             note='two shapes only, not a global minimum')
B['C3_price_stable_NS_vs_tail'] = price
B['C3_deadline_hit'] = deadline_hit
B['C3_note'] = ('minimum over the shapes evaluated, never a proved global minimum; '
                'stable value means d >= t, where N_S no longer depends on d (B23-06 Lemma 2.3)')
rec['partB'] = B
save('done')
print(json.dumps({'elapsed_s': rec['elapsed_s'], 'status': rec['status']}), flush=True)
