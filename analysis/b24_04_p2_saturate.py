"""B24-04 pilot 2: decide the classes pilot 1 could only label MEASURED.

Pre-registration: results/b24_04/PREREG_b24_04_p2.md, sha256 c62d9614... (asserted, G25).
Pilot 1's output results/b24_04/p1_patterns.json is pinned by sha256 e43e7412... .

For each pre-registered (block, statistic, threshold) class: rejection-sample patterns under seed
20260920, filtering on the statistic BEFORE any tensor work, evaluate the accepted ones at the 70
certified points, and track the rank of the class.  Stop at the first of: rank == block dimension
(the filtration is not proper there: a PROVED negative, a modular rank being a floor, G27); 120
consecutive accepted patterns with no rise; 400 accepted; the class's share of the deadline.

No runner evaluation.  Producer-only (G18).
"""
import hashlib, json, os, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
T0 = time.perf_counter()
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'analysis'))
import numpy as np

args = sys.argv[1:]
def arg(name, default):
    return args[args.index(name) + 1] if name in args else default
DEADLINE = float(arg('--deadline', '55'))
SEED = int(arg('--seed', '20260920'))

SCRATCH = Path(os.environ['B24_04_SCRATCH'])
sys.path.insert(0, str(SCRATCH / 'pinned'))
import b22_01_typed_v2 as ty
P = ty.P

# One source of truth for the statistics and the linear algebra: pilot 1's own file, of which only
# the prefix before its stage 0 (pure function definitions) is executed here.  Its sha256 is pinned
# below, so the definitions used here are provably the ones pilot 1 ran with.
_P1SRC = (Path(__file__).resolve().parent / 'b24_04_p1_patterns.py').read_text()
_MARK = '# ---------------------------------------------------------------- stage 0: pins and points'
assert _MARK in _P1SRC
_NS = {'np': np, 'ty': ty, 'P': P, 'sys': sys, 'os': os, 'json': json, 'time': time,
       'hashlib': hashlib, 'Path': Path, '__file__': __file__, '__name__': 'b24_04_p1_defs'}
exec(compile(_P1SRC.split(_MARK)[0].split('args = sys.argv')[0] +
             _P1SRC.split('# ---------------------------------------------------------------- '
                          'modular linear algebra')[1].split(_MARK)[0],
             'b24_04_p1_patterns.py:prefix', 'exec'), _NS)
stats_of, rank_mod = _NS['stats_of'], _NS['rank_mod']

OUT = ROOT / 'results/b24_04/p2_saturate.json'
assert not OUT.exists(), 'output exists; runs never overwrite (G10)'

PREREG_SHA = 'c62d96141bcb0cd8e37786858c0932448e7d5006ab3f10d9ad9f1bd25e4a2d7f'
P1_SHA = 'e43e7412cf92970e1a290854f350368621bb7a652be4f31d33c4bc4a07a12421'
PINS = {
    str(SCRATCH / 'pinned' / 'b22_01_typed_v2.py'):
        ('analysis/b22_01_typed_v2.py', '93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc'),
    str(SCRATCH / 'p2_basis.json'):
        ('results/b22_01/p2_basis.json', '7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79'),
}
TARGETS = {'11:1,4,4,0': 7, '11:2,3,3,1': 31, '11:3,2,2,2': 28, '11:4,1,1,3': 4}
BLOCK_MD = {'11:1,4,4,0': (1, 4, 4, 0), '11:2,3,3,1': (2, 3, 3, 1),
            '11:3,2,2,2': (3, 2, 2, 2), '11:4,1,1,3': (4, 1, 1, 3)}
# the pre-registered classes, in the order of the pre-registration table
CLASSES = [('11:2,3,3,1', 's_inv', 11), ('11:2,3,3,1', 's_inv', 13),
           ('11:2,3,3,1', 's_cr', 27), ('11:2,3,3,1', 's_sp', 11),
           ('11:3,2,2,2', 's_inv', 12), ('11:3,2,2,2', 's_nk', 5),
           ('11:3,2,2,2', 's_sp', 11), ('11:1,4,4,0', 's_rep', 0),
           ('11:1,4,4,0', 's_sp', 11), ('11:4,1,1,3', 's_cr', 20),
           ('11:4,1,1,3', 's_sp', 10)]
STALL, MAXACC = 120, 400


def sha(b):
    return hashlib.sha256(b).hexdigest()


def left():
    return DEADLINE - (time.perf_counter() - T0)


rec = dict(pilot='b24_04_p2_saturate', slot='B24-04', prime=P, seed=SEED,
           stall_limit=STALL, max_accepted=MAXACC, inputs={}, code={}, classes=[], log=[])


def save(status):
    rec['status'] = status
    rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')


preb = (ROOT / 'results/b24_04/PREREG_b24_04_p2.md').read_bytes()
rec['prereg_sha256'] = sha(preb)
print('PREREG sha256', rec['prereg_sha256'], flush=True)
assert rec['prereg_sha256'] == PREREG_SHA
p1b = (ROOT / 'results/b24_04/p1_patterns.json').read_bytes()
rec['p1_sha256'] = sha(p1b)
print('pilot 1 output sha256', rec['p1_sha256'], flush=True)
assert rec['p1_sha256'] == P1_SHA
for path, (rel, want) in PINS.items():
    b = Path(path).read_bytes()
    h = sha(b)
    assert h == want, (rel, h)
    rec['inputs'][rel] = dict(sha256=h, bytes=len(b), bound_by='results/b22_01/MANIFEST.json at 53bdb31e')
for rel in ('analysis/b24_04_p1_patterns.py', 'analysis/b24_04_p2_saturate.py'):
    b = (ROOT / rel).read_bytes()
    rec['code'][rel] = dict(sha256=sha(b), bytes=len(b))

# The 70 certificate points, taken from the sha256-pinned p2_basis.json.  Pilot 1 proved (control
# C0) that these are exactly the points rng(20260922) rebuilds, so no rebuild is repeated here.
basis = json.loads((SCRATCH / 'p2_basis.json').read_text())
pts = basis['points'][:70]
assert [q['label'] for q in pts] == ['cert_%02d' % i for i in range(70)]
PS = ty.PointSet(np.array([q['Z1'] for q in pts], dtype=np.int64),
                 np.array([q['Z2'] for q in pts], dtype=np.int64),
                 np.array([q['Z'] for q in pts], dtype=np.int64))
rec['points'] = dict(source='results/b22_01/p2_basis.json cert_00..cert_69',
                     rebuild_proved_by='pilot 1 control C0')
save('pins')

rng = np.random.default_rng(SEED)
budget = max(4.0, (DEADLINE - 6.0 - (time.perf_counter() - T0)) / len(CLASSES))
for block, name, j in CLASSES:
    t_end = time.perf_counter() + budget
    dim = TARGETS[block]
    md = BLOCK_MD[block]
    rows, drawn, accepted, zero, guard, since_rise = [], 0, 0, 0, 0, 0
    rank, stop = 0, None
    while True:
        if rank >= dim:
            stop = 'rank reached the block dimension'
            break
        if accepted >= MAXACC:
            stop = 'accepted cap'
            break
        if since_rise >= STALL:
            stop = 'stalled'
            break
        if time.perf_counter() > t_end or left() < 4:
            stop = 'deadline'
            break
        drawn += 1
        pat = ty.random_pattern(rng, md, 11)
        if pat is None:
            continue
        if stats_of(pat)[name] > j:
            continue
        try:
            xi = ty.xi_tensor(pat)
            if not np.any(xi % P):
                zero += 1
                continue
            v = [int(x) % P for x in ty.evaluate(pat, PS, xi=xi)]
        except AssertionError as exc:
            guard += 1
            rec['log'].append('guard skip %s %s<=%d: %r' % (block, name, j, exc))
            continue
        if not any(v):
            zero += 1
            continue
        accepted += 1
        rows.append(v)
        new = rank_mod(np.array(rows, dtype=np.int64))
        since_rise = 0 if new > rank else since_rise + 1
        rank = new
    verdict = ('trivial at this j (PROVED: the class spans the whole block)' if rank >= dim else
               'UNDECIDED (stopped by the deadline)' if stop == 'deadline' else
               'candidate, MEASURED only (rank stalled below the block dimension)')
    rec['classes'].append(dict(block=block, statistic=name, threshold=j, block_dim=dim,
                              drawn=drawn, accepted=accepted, zero_function=zero,
                              guard_skip=guard, rank=int(rank), stopped_by=stop,
                              verdict=verdict,
                              wall_s=round(budget - (t_end - time.perf_counter()), 3)))
    save('running')
    print(json.dumps(rec['classes'][-1]), flush=True)

save('done')
print(json.dumps({'elapsed_s': rec['elapsed_s'], 'status': rec['status']}), flush=True)
