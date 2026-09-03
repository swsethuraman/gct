#!/usr/bin/env python3
"""
Session 45 -- the six-row determinant-side sweep, ascending in n_chi, most
balanced cell available at each size (results/PREREG_s45.md section 4).

Per cell:  a (plethysm; asserted against the full-E nullity where affordable),
n_chi, nnz, nullity_p([E; ev_det]) at both house primes, the route/level used,
wall time, peak memory, and the verdict
    mult_det = a          (PROVED, nullity 0 at a single prime), or
    mult_det <= a - k     (measured; the stopping rules of the pre-registration
                           then take over: exhibited vectors, exact
                           verification, fresh preconditioner/seed/prime, 20
                           fresh determinant pencils, then the pad side).

Each cell is appended to results/s45_cells.jsonl as it completes.

usage: python3 wk9_s45_sweep.py <index|lam...> [--delta d] [--levels cheap|s42|full]
                                [--full-check] [--build-only]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied45')
os.environ.setdefault('WIED_WORK', '/home/claude/s45/work')
from wk9_s45_cell import measure_cell, LEVELS
from wk9_s45_build import build_cell, log, _rss_gb

# the pre-registered order (results/PREREG_s45.md section 4)
PLAN = [((9, 9, 4, 4, 1, 1), 7), ((9, 9, 6, 2, 1, 1), 7), ((12, 12, 3, 3, 1, 1), 8),
        ((8, 8, 5, 5, 1, 1), 7), ((8, 8, 7, 3, 1, 1), 7), ((7, 7, 6, 6, 1, 1), 7),
        ((8, 8, 6, 2, 2, 2), 7), ((9, 9, 9, 3, 1, 1), 8), ((6, 6, 6, 6, 2, 2), 7),
        ((8, 4, 4, 4, 4, 4), 7)]
OUT = os.path.join(HERE, '..', 'results', 's45_cells.jsonl')

def already(lam, delta, path=OUT):
    if not os.path.exists(path): return False
    for l in open(path):
        if not l.strip(): continue
        d = json.loads(l)
        if tuple(d['lam']) == tuple(lam) and d['delta'] == delta: return True
    return False

def run(lam, delta, levels='cheap', full_check=False, build_only=False):
    t0 = time.time()
    if not build_only and already(lam, delta):
        log(f"  {lam} d{delta} already banked in {OUT}; skipping"); return None
    if build_only:
        B = build_cell(lam, delta, verbose=True)
        rec = dict(lam=list(lam), delta=delta, N_S=B['N_S'], stab=B['stab'], n_chi=B['n_chi'],
                   nrows=B['nrows'], nnz=B['nnz'], build_secs=round(B['build_secs'], 1),
                   mono_secs=round(B['mono_secs'], 1), orbit_secs=round(B['orbit_secs'], 1),
                   rows_secs=round(B['rows_secs'], 1), hwm_gb=round(B['hwm_gb'], 2),
                   build_only=True)
        print(json.dumps(rec))
        with open(os.path.join(HERE, '..', 'results', 's45_buildcurve.jsonl'), 'a') as f:
            f.write(json.dumps(rec) + "\n")
        return rec
    res = measure_cell(lam, delta, sides=('det',), levels=LEVELS[levels],
                       full_check=full_check, verbose=True)
    k = res['sides']['det']['nullity']
    res['verdict'] = ('mult_det = a = %d (PROVED, nullity 0)' % res['a']) if k == 0 else \
                     ('mult_det <= a - %d = %d (MEASURED -- stopping rule 3 applies)' % (k, res['a'] - k))
    res['wall_secs'] = round(time.time() - t0, 1)
    print(json.dumps(res))
    with open(OUT, 'a') as f: f.write(json.dumps(res) + "\n")
    log(f"SWEEP {lam} d{delta}: n_chi={res['n_chi']} nnz={res['nnz']} -> {res['verdict']} "
        f"({res['wall_secs']}s, HWM {res.get('hwm_gb')} GB)")
    if k:
        log("*** nullity > 0 on the determinant side: the sweep HALTS here (pre-registered stopping rule 3). ***")
    return res

if __name__ == '__main__':
    args = sys.argv[1:]
    levels = 'cheap'; full = False; bo = False; delta = None; pos = []
    i = 0
    while i < len(args):
        if args[i] == '--levels': levels = args[i + 1]; i += 2
        elif args[i] == '--delta': delta = int(args[i + 1]); i += 2
        elif args[i] == '--full-check': full = True; i += 1
        elif args[i] == '--build-only': bo = True; i += 1
        else: pos.append(int(args[i])); i += 1
    if len(pos) == 1 and delta is None:
        lam, delta = PLAN[pos[0]]           # a plan index
    elif delta is None:
        delta, lam = pos[0], tuple(pos[1:]) # 'delta lam1 lam2 ...', the house convention
    else:
        lam = tuple(pos)
    run(lam, delta, levels=levels, full_check=full, build_only=bo)
