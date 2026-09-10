#!/usr/bin/env python3
"""
B13-08 -- recalibrate the SCHEDULING peak-memory estimate on this session's own
measurements (pre-registration addendum A, 2026-09-10).

results/b13_08/queue.json is frozen and is NOT touched: its `pred_peak_gb` was an
a-priori model fitted by eye on session 79's records, and it is wrong by up to
2.0 GB on this box.  This writes a separate results/b13_08/schedule.json that the
sweep reads with --sched; it changes which weights run concurrently and nothing
else.  No result depends on it.

The model, least squares on the 22 weights measured here plus the two control
weights, all on the unchanged engine at S71_MEM_X = 2.5e8:

    peak_GB  =  0.986  +  0.0277 * (nnz / 1e6)  +  0.1057 * (n_chi * min(a,16) / 1e6)

    max residual 0.36 GB, p90 0.21 GB over the 22.

Mechanically: the constant is the interpreter plus the build's own transients;
the nnz term is E held as CSR (int64 data, int32 indices) plus the hybrid's
working copy, ~28 bytes per nonzero; the n_chi*min(a,16) term is the kernel K
(uint32), its int64 image Kp_, and the 16-column blocks of the kernel check.

For an unrun weight nnz and n_chi are not known, so they are estimated from N_S
and |Stab| by the ratios measured over session 79's 506 cubic-scan records and
this session's 22, taken at their p90 rather than their median so the estimate
errs high:

    n_chi  ~  N_S / |Stab|  (the orbit count; exact when |Stab| = 1, p90 ratio 1.0)
    nnz    ~  RHO[|Stab|] * N_S * delta

usage: python3 analysis/wk13_b08_schedule.py   (writes results/b13_08/schedule.json)
"""
import os, sys, json, glob, collections, math

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
RES = os.path.join(ROOT, 'results', 'b13_08')
DELTA = 10
C0, C_NNZ, C_KER = 0.986, 0.0277, 0.1057


def stab_order(mu):
    s = 1
    for v in collections.Counter(mu).values(): s *= math.factorial(v)
    return s


def measured_ratios():
    """nnz/(N_S*delta) and n_chi*|Stab|/N_S by |Stab|, at p90, over s79's records and this session's."""
    rows = []
    for ln in open(os.path.join(ROOT, 'results', 's79_per6.jsonl')):
        r = json.loads(ln); rows.append(r)
    p = os.path.join(RES, 'per6_d10.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            if ln.strip(): rows.append(json.loads(ln))
    rho = collections.defaultdict(list); chi = collections.defaultdict(list)
    for r in rows:
        s = stab_order(tuple(r['mu']))
        rho[s].append(r['nnz'] / (r['N_S'] * r['delta']))
        chi[s].append(r['n_chi'] * s / r['N_S'])
    def p90(v): return sorted(v)[min(len(v) - 1, int(0.9 * len(v)))]
    return {s: p90(v) for s, v in rho.items()}, {s: p90(v) for s, v in chi.items()}, {s: len(v) for s, v in rho.items()}


def main():
    RHO, CHI, N = measured_ratios()
    Q = json.load(open(os.path.join(RES, 'queue.json')))
    rho_default = max(RHO.values()); chi_default = max(CHI.values())
    out = dict(board_numbering='batch13', session='B13-08', addendum='A (2026-09-10)',
               model='peak_GB = %.3f + %.4f*(nnz/1e6) + %.4f*(n_chi*min(a,16)/1e6)' % (C0, C_NNZ, C_KER),
               fitted_on='the 22 weights measured in this session plus the two control weights; max residual 0.36 GB',
               ratios=dict(nnz_over_NS_delta_by_stab={str(k): round(v, 3) for k, v in sorted(RHO.items())},
                           n_chi_times_stab_over_NS_by_stab={str(k): round(v, 3) for k, v in sorted(CHI.items())},
                           sample_counts={str(k): v for k, v in sorted(N.items())}, quantile='p90'),
               note='scheduling only; results/b13_08/queue.json stays frozen and no result depends on this file',
               sched={})
    rows = []
    for w in Q['queue']:
        mu = tuple(w['mu']); s = stab_order(mu); a = w['a']
        nnz = RHO.get(s, rho_default) * w['N_S'] * DELTA
        n_chi = CHI.get(s, chi_default) * w['N_S'] / s
        gb = C0 + C_NNZ * nnz / 1e6 + C_KER * n_chi * min(a, 16) / 1e6
        out['sched'][str(w['rank'])] = round(gb, 2)
        rows.append((w['rank'], mu, a, w['N_S'], s, round(gb, 2), w['pred_peak_gb']))
    json.dump(out, open(os.path.join(RES, 'schedule.json'), 'w'), indent=1)
    # accuracy of the new model on what is already measured
    st = json.load(open(os.path.join(RES, 'status.json')))
    err = []
    for r in st['reached_list']:
        g = C0 + C_NNZ * r['nnz'] / 1e6 + C_KER * r['n_chi'] * min(r['a'], 16) / 1e6
        err.append(abs(g - r['hwm_gb']))
    if err:
        print(f"on the {len(err)} measured weights (exact nnz, n_chi): max error {max(err):.2f} GB, mean {sum(err)/len(err):.2f} GB")
    print(f"{'rank':>4} {'mu':<22} {'a':>3} {'N_S':>9} {'St':>3} {'new':>5} {'frozen':>6}")
    for rk, mu, a, ns, s, gb, old in rows[:4] + rows[-8:]:
        print(f"{rk:>4} {str(mu):<22} {a:>3} {ns:>9} {s:>3} {gb:>5} {old:>6}")
    v = [r[5] for r in rows]
    print(f"\nrecalibrated: max {max(v)} GB, {sum(1 for x in v if x > 4)} of 95 above 4 GB, {sum(1 for x in v if x > 5)} above 5 GB "
          f"(frozen model said {sum(1 for w in Q['queue'] if w['pred_peak_gb'] > 4)} above 4 GB)")


if __name__ == '__main__':
    sys.exit(main())
