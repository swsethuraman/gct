#!/usr/bin/env python3
"""
B14-09 -- the sizing table for the 58 open six-row degree-10 cells.

`docs/batch14_board.md` slot 9: "These 58 have never been built and no `n_chi` is
recorded. ... Use a twisted-orbit count, a justified bound for the
representation, or a measured reduced dimension; never size, route or reject a
cell on `N_S/|Stab|` alone.  **Fallback** the sizing table alone is worth the
slot; nobody has one."

This builds it, with `n_chi` an EXACT value from `b14_09_sizing.n_chi_exact`
(the character sum), not a bound and not a quotient.

The open set is DERIVED here, not asserted: session 79's frozen 402-weight
degree-10 queue, minus s79's 296 banked weights, minus B13-08's 48.  The
derivation is checked against B13-08 section 0 (48 measured, 47 unreached below
`N_S = 10^7`, 11 deferred at or above it).

usage: python3 analysis/b14_09_table.py [--out results/b14_09/sizing.json]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
import b14_09_sizing as S

WIDE = 1 << 21                      # nchi_2_21_guard: the inner-dimension bound of matmul_mod


def open_cells():
    """the 58, derived from the frozen objects."""
    q = json.load(open(os.path.join(ROOT, 'results/b13_08/queue.json')))
    done = set()
    with open(os.path.join(ROOT, 'results/b13_08/per6_d10.jsonl')) as f:
        for line in f:
            line = line.strip()
            if line:
                done.add(tuple(json.loads(line)['mu']))
    below = [dict(e, tier='b13_08 queue, not reached') for e in q['queue'] if tuple(e['mu']) not in done]
    above = [dict(e, tier='deferred by B13-08 at N_S >= 1e7') for e in q['deferred_batch14']]
    assert len(done) == 48, ('B13-08 measured count', len(done))
    assert len(below) == 47, ('unreached below 1e7', len(below))
    assert len(above) == 11, ('deferred at or above 1e7', len(above))
    return below + above, q, done


def cost_model_build(N_S, delta, stab):
    """PROVED.md: cost_model (B13-09).  ADOPTED, not measured here."""
    return 3.06e-6 * N_S * delta + 1.07e-6 * stab * N_S


def fit_decide(recs):
    """A two-term least-squares fit of B13-08's MEASURED decide time (total minus
    build, both primes) on its 48 degree-10 cells:  t ~ c1*n_chi*a + c2*nnz.
    This is a fit to 48 points on the same host class, not a theorem; it is used
    only to order the queue and to price what is not reached."""
    import numpy as np
    X, y = [], []
    for r in recs:
        X.append([r['n_chi'] * r['a'], r['nnz']])
        y.append(r['secs'] - r['build_secs'])
    X = np.array(X, float); y = np.array(y, float)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ c
    rel = np.abs(pred - y) / np.maximum(y, 1e-9)
    return dict(coeffs=[float(c[0]), float(c[1])], n=len(y),
                median_rel_err=float(np.median(rel)), max_rel_err=float(rel.max()))


def fit_mem(recs):
    import numpy as np
    X, y = [], []
    for r in recs:
        X.append([r['nnz'], r['N_S'] * r['delta'], r['n_chi'] * r['a']])
        y.append(r['hwm_gb'])
    X = np.array(X, float); y = np.array(y, float)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ c
    rel = np.abs(pred - y) / np.maximum(y, 1e-9)
    return dict(coeffs=[float(v) for v in c], n=len(y),
                median_rel_err=float(np.median(rel)), max_rel_err=float(rel.max()))


def main():
    cells, q, done = open_cells()
    recs = [json.loads(l) for l in open(os.path.join(ROOT, 'results/b13_08/per6_d10.jsonl')) if l.strip()]
    fd = fit_decide(recs); fm = fit_mem(recs)
    # nnz is not known before the build; fit it too, from the same 48
    import numpy as np
    Xn = np.array([[r['N_S'] * r['delta']] for r in recs], float)
    yn = np.array([r['nnz'] for r in recs], float)
    cn, *_ = np.linalg.lstsq(Xn, yn, rcond=None)
    nnz_rel = np.abs(Xn @ cn - yn) / yn
    fnnz = dict(coeff=float(cn[0]), n=len(yn), median_rel_err=float(np.median(nnz_rel)),
                max_rel_err=float(nnz_rel.max()))

    out = []
    t0 = time.time()
    for e in cells:
        mu = tuple(e['mu'])
        t = time.time()
        z = S.n_chi_exact(mu, 10, n=3)
        secs = time.time() - t
        assert z['N_S'] == e['N_S'], ('N_S disagrees with the frozen queue', mu, z['N_S'], e['N_S'])
        assert z['stab'] == e['stab'], ('|Stab| disagrees with the frozen queue', mu, z['stab'], e['stab'])
        nchi = z['n_chi']
        nnz_pred = fnnz['coeff'] * e['N_S'] * 10
        build_pred = cost_model_build(e['N_S'], 10, e['stab'])
        dec_pred = fd['coeffs'][0] * nchi * e['a'] + fd['coeffs'][1] * nnz_pred
        mem_pred = fm['coeffs'][0] * nnz_pred + fm['coeffs'][1] * e['N_S'] * 10 + fm['coeffs'][2] * nchi * e['a']
        out.append(dict(
            rank=e['rank'], mu=list(mu), a=e['a'], N_S=e['N_S'], stab=e['stab'],
            n_chi=nchi, n_chi_source='exact character sum (analysis/b14_09_sizing.py), MEASURED',
            NS_over_stab=e['N_S'] / e['stab'],
            ratio_nchi_to_quotient=round(nchi / (e['N_S'] / e['stab']), 4),
            quotient_verdict=('quotient UNDER-states n_chi' if nchi > e['N_S'] / e['stab'] else
                              'quotient OVER-states n_chi' if nchi < e['N_S'] / e['stab'] else 'equal'),
            inner_dim_of_ev_times_K=nchi,
            needs_matmul_mod_wide=bool(nchi >= WIDE),
            wide_predicted_by_quotient=bool(e['N_S'] / e['stab'] >= WIDE),
            quotient_routing_wrong=bool((nchi >= WIDE) != (e['N_S'] / e['stab'] >= WIDE)),
            pred_build_secs=round(build_pred, 1),
            pred_nnz=int(nnz_pred),
            pred_decide_secs=round(dec_pred, 1),
            pred_total_secs=round(build_pred + dec_pred, 1),
            pred_peak_gb=round(mem_pred, 2),
            queue_pred_peak_gb=e['pred_peak_gb'],
            tier=e['tier'], sizing_secs=round(secs, 3)))
    out.sort(key=lambda d: d['pred_total_secs'])
    doc = dict(
        session='B14-09', board_numbering='batch14', delta=10, n=3, r=6,
        objects=dict(queue='results/s79_per6_queue.json (402 weights, frozen by s79)',
                     banked_s79='results/s79_per6.jsonl (296)',
                     banked_b13_08='results/b13_08/per6_d10.jsonl (48)',
                     open=len(out)),
        instrument='n_chi = (1/|G|) sum_{g in G} chi_mu(g) |Fix_X(g)|, exact; |Fix| by an orbit knapsack over exps(3,6)',
        guard=dict(bound=WIDE, applies_to='the actual inner dimension of each multiplication',
                   binding_multiplication='G = ev_rows . K in wk12_s79_per6.measure_weight; inner dimension = n_chi'),
        cost_fits=dict(build='PROVED.md: cost_model (ADOPTED)', decide=fd, mem=fm, nnz=fnnz,
                       caveat='fitted on B13-08 48 degree-10 cells, same host class; ordering and pricing only'),
        total_sizing_secs=round(time.time() - t0, 2),
        cells=out)
    dest = os.path.join(ROOT, sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv
                        else 'results/b14_09/sizing.json')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    json.dump(doc, open(dest, 'w'), indent=1)
    print(f"58 cells sized in {doc['total_sizing_secs']}s -> {os.path.relpath(dest, ROOT)}")
    return doc


if __name__ == '__main__':
    main()
