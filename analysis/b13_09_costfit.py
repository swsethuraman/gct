#!/usr/bin/env python3
"""
B13-09 -- refit the build cost model at lengths 7 and 8, and re-price the census.

The s79/s71 model is  build_secs = 2.1e-6 * N_S*delta , fitted at length 6 where
it held at a median 0.99x.  At lengths 7 and 8 it underprices by up to 22x, and
the reason is structural rather than statistical: `wk9_s45_build.orbit_setup_arr`
makes TWO passes over the whole group Stab_W(mu) (`_canon_acc`: one pass for
`canon`, one for `acc`), each pass an O(N_S) permutation-image-and-lookup over
the (N_S x delta) monomial array.  So the orbit setup costs O(|Stab| * N_S),
which is invisible at length 6 -- where a weight with |Stab| = 120 is already
unusual -- and dominant at lengths 7 and 8, where repeated parts push |Stab| to
720 at (9,2^6), 5040 at (10,2^7).

    build_secs  ~=  c1 * N_S*delta  +  c2 * |Stab| * N_S

fitted here by minimising RELATIVE error (the quantity a queue order actually
needs, since the weights span three orders of magnitude), and reported with the
worst over- and under-prediction so a planner knows the spread it is trusting.

usage: python3 analysis/b13_09_costfit.py [--census results/b13_09_census.json]
          [--out results/b13_09/costfit.json] [--reprice]
`--reprice` writes `cost_model_s` and `cost_rank` into every census weight
(leaving `build_model_s`, the s79 number, in place beside it for comparison).
"""
import sys, os, json, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

S79_RATE = 2.1e-6


def load_measured():
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'results', 'b13_09', 'per_r*.jsonl'))):
        for ln in open(f):
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if r.get('N_S') and r.get('build_secs') is not None:
                rows.append(r)
    seen = {}
    for r in rows: seen[(tuple(r['mu']), r['delta'])] = r      # last wins; identical re-runs are idempotent
    return list(seen.values())


def fit(rows):
    """minimise sum (log(pred) - log(actual))^2 over c1, c2 >= 0 on a coarse grid
    then a local refine -- two parameters, so a grid is honest and reproducible."""
    X1 = np.array([r['NS_delta'] for r in rows], float)
    X2 = np.array([r['stab'] * r['N_S'] for r in rows], float)
    y = np.array([r['build_secs'] for r in rows], float)
    keep = y > 0.05                                            # a sub-0.05 s build carries no information about a rate
    X1, X2, y = X1[keep], X2[keep], y[keep]
    best = None
    lo1, hi1, lo2, hi2 = 1e-7, 3e-5, 1e-9, 3e-6
    for _ in range(6):
        g1 = np.geomspace(lo1, hi1, 40); g2 = np.geomspace(lo2, hi2, 40)
        for c1 in g1:
            pred1 = c1 * X1
            for c2 in g2:
                pred = pred1 + c2 * X2
                err = float(np.sum((np.log(pred) - np.log(y)) ** 2))
                if best is None or err < best[0]: best = (err, c1, c2)
        _, c1, c2 = best
        lo1, hi1 = c1 / 3, c1 * 3
        lo2, hi2 = c2 / 3, c2 * 3
    err, c1, c2 = best
    pred = c1 * X1 + c2 * X2
    ratio = pred / y
    s79 = S79_RATE * X1 / y
    return dict(c1_per_NS_delta=float(c1), c2_per_Stab_NS=float(c2), n=int(len(y)),
                median_pred_over_actual=float(np.median(ratio)),
                p10=float(np.percentile(ratio, 10)), p90=float(np.percentile(ratio, 90)),
                worst_underprediction=float(ratio.min()), worst_overprediction=float(ratio.max()),
                s79_model_median_actual_over_model=float(np.median(1 / s79)),
                s79_model_worst_actual_over_model=float((1 / s79).max()),
                fitted_on='the weights measured by this session at lengths 7 and 8')


def main(argv):
    cpath = argv[argv.index('--census') + 1] if '--census' in argv else os.path.join(ROOT, 'results', 'b13_09_census.json')
    opath = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b13_09', 'costfit.json')
    rows = load_measured()
    if len(rows) < 8:
        print(f"only {len(rows)} measured weights: too few to fit", file=sys.stderr); return 1
    f = fit(rows)
    C = json.load(open(cpath))
    c1, c2 = f['c1_per_NS_delta'], f['c2_per_Stab_NS']
    groups = {}
    for k, cells in C['cells'].items():
        for r in cells:
            r['cost_model_s'] = round(c1 * r['NS_delta'] + c2 * r['stab'] * r['N_S'], 1)
        order = sorted(cells, key=lambda r: r['cost_model_s'])
        for i, r in enumerate(order, 1): r['cost_rank'] = i
        groups[k] = dict(weights=len(cells),
                         total_model_h=round(sum(r['cost_model_s'] for r in cells) / 3600, 2),
                         total_s79_h=round(sum(r['build_model_s'] for r in cells) / 3600, 2),
                         cheapest=[[r['mu'], r['cost_model_s']] for r in order[:3]],
                         dearest=[[r['mu'], r['cost_model_s']] for r in order[-3:]])
    f['groups'] = groups
    f['note'] = ('cost_model_s is the refitted build estimate; build_model_s beside it is the s79 '
                 'N_S*delta-only number, kept for comparison.  Neither includes the evaluation rows '
                 '(2.7e-8 s per point per N_S*delta) or the hybrid, which was never the cost here.')
    json.dump(dict(board_numbering='batch13', session='B13-09', **f), open(opath, 'w'), indent=1)
    if '--reprice' in argv:
        json.dump(C, open(cpath, 'w'), indent=1)
        print(f"census repriced in place: {cpath}", file=sys.stderr)
    print(f"build_secs ~ {c1:.3g} * N_S*delta + {c2:.3g} * |Stab|*N_S  (n={f['n']}); "
          f"median pred/actual {f['median_pred_over_actual']:.2f} (p10 {f['p10']:.2f}, p90 {f['p90']:.2f}); "
          f"s79 model underprices by up to {f['s79_model_worst_actual_over_model']:.1f}x", file=sys.stderr)
    for k, g in groups.items():
        print(f"  {k}: {g['weights']} weights, refitted {g['total_model_h']} h vs s79 {g['total_s79_h']} h", file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
