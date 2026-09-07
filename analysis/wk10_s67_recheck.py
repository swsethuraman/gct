#!/usr/bin/env python3
"""
Session 67, Part A3 -- independently re-derive a sample of the back-filled
sparse_nullity certificates and record the coverage.

Each result is appended to results/s67_sparse_sample.jsonl as it completes, so a
budget cut-off never loses finished work.  Two modes:

  * full   -- the checker's default: nullity_p(E) = a (the build's kernel is the
              highest-weight space) AND nullity_p([E; ev]) = 0.  The strongest
              per-cell check; used on a spread of stabiliser sizes and on the
              object-code (delta >= 11) path.
  * ev     -- nullity_p([E; ev]) = 0 only, with the build taken as validated by
              the full-mode cells (chi_build is deterministic and
              cell-shape-independent).  Used to widen coverage cheaply.

usage: python3 analysis/wk10_s67_recheck.py [--budget SECONDS]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools/verify'))
OUT = os.path.join(ROOT, 'results/s67_sparse_sample.jsonl')

FULL = ['12_5_4_2_1_d6', '12_5_3_2_2_d6', '8_7_6_2_1_d6', '17_9_2_2_2_d8',
        '29_10_2_2_1_d11', '36_16_2_1_1_d14']
BROAD_TARGETS = [5731, 6983, 8987, 11015, 13005, 14912, 16933, 20138, 24865,
                 28000, 31000, 34000]


def load_cells():
    rows = [json.loads(l) for l in open(os.path.join(ROOT, 'results/s60_cells.jsonl'))]
    return {('_'.join(map(str, r['lam'])) + f"_d{r['delta']}"): r for r in rows if r['route'] == 'sparse'}


def run_one(tag, rec, mode, results):
    os.environ['VERIFY_MAX_NS'] = '80000'
    if mode == 'ev':
        os.environ['VERIFY_SKIP_BUILD_CHECK'] = '1'
    else:
        os.environ.pop('VERIFY_SKIP_BUILD_CHECK', None)
    import importlib
    import layer3, verify
    importlib.reload(layer3); importlib.reload(verify)
    path = os.path.join(ROOT, f"results/certs/s60/{tag}_det_sparse_p2147483647.json.gz")
    t = time.time()
    st, log = verify.verify_file(path)
    dt = round(time.time() - t, 1)
    concl = any('conclusion:' in n and o for n, o, d in log)
    bk = any('build check' in n and o and 'assumed' not in (d or '') for n, o, d in log)
    row = dict(tag=tag, N_S=rec['N_S'], n_chi=rec['n_chi'], stab=rec['stab'],
               delta=rec['delta'], a=rec['a'], status=st, mode=mode,
               build_checked=bk, concluded=concl, secs=dt)
    results.append(row)
    with open(OUT, 'a') as f:
        f.write(json.dumps(row) + "\n")
    print(f"{st:5s} [{mode:4s}] {tag:22s} N_S={rec['N_S']:6d} n_chi={rec['n_chi']:6d} "
          f"stab={rec['stab']} d={rec['delta']} a={rec['a']:2d} build_ok={bk} concl={concl} {dt}s", flush=True)
    return dt


def main(argv):
    budget = 540
    if '--budget' in argv:
        budget = int(argv[argv.index('--budget') + 1])
    cells = load_cells()
    open(OUT, 'w').close()          # fresh
    results = []
    t0 = time.time()
    for tag in FULL:
        if tag in cells and time.time() - t0 < budget:
            run_one(tag, cells[tag], 'full', results)
    done = {r['tag'] for r in results}
    by_ns = sorted(cells.values(), key=lambda r: r['N_S'])
    seen = set(done)
    for tt in BROAD_TARGETS:
        if time.time() - t0 >= budget:
            break
        cand = min((r for r in by_ns if ('_'.join(map(str, r['lam'])) + f"_d{r['delta']}") not in seen),
                   key=lambda r: abs(r['N_S'] - tt), default=None)
        if cand is None:
            continue
        tag = '_'.join(map(str, cand['lam'])) + f"_d{cand['delta']}"
        seen.add(tag)
        run_one(tag, cand, 'ev', results)
    npass = sum(1 for r in results if r['status'] == 'PASS')
    print(f"\nre-derived {len(results)} sparse certs, {npass} PASS "
          f"({sum(1 for r in results if r['mode']=='full')} full soundness, "
          f"{sum(1 for r in results if r['mode']=='ev')} [E;ev]-only)")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
