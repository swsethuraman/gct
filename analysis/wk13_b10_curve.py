#!/usr/bin/env python3
"""
B13-10 -- the memory curve: aggregate every build record into one table and fit
peak(above baseline) against the size statistics, per builder.

usage: python3 analysis/wk13_b10_curve.py [--scratch DIR] [--out results/b13_10/memcurve.jsonl]
"""
import sys, os, json, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))


def main():
    args = sys.argv[1:]
    def arg(n, d): return args[args.index(n) + 1] if n in args else d
    scratch = arg('--scratch', '/home/claude/b13_10_scratch')
    outp = arg('--out', os.path.join(ROOT, 'results', 'b13_10', 'memcurve.jsonl'))
    rows = []
    for fn in sorted(glob.glob(os.path.join(scratch, '*.json'))):
        try: r = json.load(open(fn))
        except Exception: continue
        if 'builder' not in r or 'N_S' not in r: continue
        rows.append(dict(tag=r['tag'], builder=r['builder'], knobs=r.get('knobs'), n=r['n'], lam=r['lam'], delta=r['delta'],
                         a=r['a'], N_S=r['N_S'], stab=r['stab'], n_chi=r['n_chi'], nrows=r['nrows'], nnz=r['nnz'],
                         NS_delta=r['NS_delta'], secs=r['secs']['total'], secs_mono=r['secs']['mono'], secs_orbits=r['secs']['orbits'],
                         secs_rows=r['secs']['rows'], peak_gb=r['hwm_above_baseline_gb'], hwm_gb=r['hwm_gb'],
                         baseline_gb=r['hwm_baseline_gb'], E_dtypes=r['E_dtypes'], M_dtype=r['M_dtype']))
    # the pilot, whose record has a different shape
    pj = os.path.join(ROOT, 'results', 'b13_10', 'pilot.json')
    if os.path.exists(pj):
        p = json.load(open(pj))
        if 'build' in p:
            b = p['build']
            rows.append(dict(tag='PILOT', builder='lean', knobs=p['knobs'], n=p['n'], lam=p['lam'], delta=p['delta'], a=p['a'],
                             N_S=b['N_S'], stab=b['stab'], n_chi=b['n_chi'], nrows=b['nrows'], nnz=b['nnz'],
                             NS_delta=b['N_S'] * p['delta'], secs=b['secs'], secs_mono=b['mono_secs'], secs_orbits=b['orbit_secs'],
                             secs_rows=b['rows_secs'], peak_gb=b['hwm_above_baseline_gb'], hwm_gb=b['hwm_gb'],
                             baseline_gb=b['baseline_gb'], E_dtypes=b['dtypes'], M_dtype=b['dtypes']['M']))
    with open(outp, 'w') as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    # pairs and fits
    by = {}
    for r in rows:
        key = (r['tag'], r['builder'], json.dumps(r['knobs'], sort_keys=True))
        by[key] = r
    print(f"{'cell':6} {'N_S*d':>12} {'n_chi':>9} {'nnz':>10} | {'old GB':>7} {'old s':>7} | {'lean GB':>7} {'lean s':>7} | {'x mem':>6} {'x time':>6}")
    ratios = []
    for r in sorted(rows, key=lambda r: r['NS_delta']):
        if r['builder'] != 'old': continue
        ln = by.get((r['tag'], 'lean', json.dumps(dict(chunk=400000, triples='store', blocks='memory'), sort_keys=True)))
        if not ln: continue
        rm = r['peak_gb'] / ln['peak_gb'] if ln['peak_gb'] else float('nan')
        rt = ln['secs'] / r['secs'] if r['secs'] else float('nan')
        ratios.append((r['NS_delta'], rm, rt, r['tag']))
        print(f"{r['tag']:6} {r['NS_delta']:12d} {r['n_chi']:9d} {r['nnz']:10d} | {r['peak_gb']:7.3f} {r['secs']:7.1f} | {ln['peak_gb']:7.3f} {ln['secs']:7.1f} | {rm:6.2f} {rt:6.2f}")
    # least-squares fit peak = alpha*N_S*delta + beta*nnz + gamma*max_targets(proxy: nrows) + c, per builder
    for bl in ('old', 'lean'):
        S = [r for r in rows if r['builder'] == bl and (bl == 'old' or r['knobs'] == dict(chunk=400000, triples='store', blocks='memory'))]
        if len(S) < 4: continue
        A = np.array([[r['NS_delta'], r['nnz'], r['nrows'], 1.0] for r in S], dtype=float)
        y = np.array([r['peak_gb'] for r in S], dtype=float)
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        pred = A @ coef
        res = np.abs(pred - y)
        print(f"fit[{bl}] peak_GB = {coef[0]:.3e}*N_S*delta + {coef[1]:.3e}*nnz + {coef[2]:.3e}*rows + {coef[3]:.3f}   "
              f"(n={len(S)}, max |residual| {res.max():.3f} GB, median {np.median(res):.3f} GB)")
    # variants
    print("\nvariants (lean, against the default lean run of the same cell):")
    for r in sorted(rows, key=lambda r: (r['tag'], str(r['knobs']))):
        if r['builder'] != 'lean' or r['knobs'] == dict(chunk=400000, triples='store', blocks='memory'): continue
        base = by.get((r['tag'], 'lean', json.dumps(dict(chunk=400000, triples='store', blocks='memory'), sort_keys=True)))
        if not base: continue
        print(f"  {r['tag']:5} {str(r['knobs']):68} peak {r['peak_gb']:6.3f} GB ({r['peak_gb']/base['peak_gb']:5.2f}x)  {r['secs']:7.1f}s ({r['secs']/base['secs']:5.2f}x)")


if __name__ == '__main__':
    main()
