#!/usr/bin/env python3
"""
Session 71 -- the per-cell table (results/s71_sweep.md), the cost curve
(results/s71_cost_curve.{json,png}) and the summary numbers the report quotes,
all from results/s71_sweep.jsonl and results/s71_queue.json.
"""
import sys, os, json, statistics, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def load():
    queue = json.load(open(os.path.join(ROOT, 'results', 's71_queue.json')))
    rows = [json.loads(l) for l in open(os.path.join(ROOT, 'results', 's71_sweep.jsonl'))]
    return queue, rows


def summary(queue, rows):
    meas = [r for r in rows if r.get('status') == 'measured']
    nr = [r for r in rows if r.get('status') == 'not reached']
    meas.sort(key=lambda r: r['rank'])
    S = dict(n_queue=len(queue), n_measured=len(meas), n_not_reached=len(nr),
             n_closed=sum(1 for r in meas if r['i_det'] == 0), n_idet_pos=sum(1 for r in meas if r['i_det'] > 0),
             n_D_pos=sum(1 for r in meas if r['D'] > 0), n_iper4_pos=sum(1 for r in meas if r['i_per4'] > 0),
             n_red_first=sum(1 for r in meas if r['i_red'] > 0 and r['i_det'] == 0),
             rungs_settled=sum(len(r['rungs']) for r in meas if r['i_det'] == 0),
             n_sieve_red=sum(1 for r in meas if r['cover_Ered']['certified']),
             total_secs=round(sum(r['secs'] for r in meas) + sum(r['secs'] for r in nr), 1),
             max_nchi=max(r['n_chi'] for r in meas), max_a=max(r['a'] for r in meas), max_NS=max(r['N_S'] for r in meas),
             max_rank=max(r['rank'] for r in meas), max_delta=max(r['delta'] for r in meas),
             primes_disagree=sum(1 for r in meas if not r['ok']),
             excess_frac_max=max((r['n_chi'] - r['cover_E']['size'] - r['a']) / r['n_chi'] for r in meas),
             excess_frac_median=statistics.median((r['n_chi'] - r['cover_E']['size'] - r['a']) / r['n_chi'] for r in meas),
             orders=dict(collections.Counter(r['cover_E']['order'] for r in meas)),
             ratio_actual_pred_median=statistics.median(r['secs'] / r['pred_secs'] for r in meas if r.get('pred_secs')),
             hwm_gb=max(r['hwm_gb'] for r in meas))
    S['n_closed_total'] = 99 + S['n_closed']
    S['frac_closed_total'] = round(S['n_closed_total'] / 1075, 4)
    return S, meas, nr


def cost_curve(meas, nr):
    cum = 0.0; pts = []
    allr = sorted(meas + nr, key=lambda r: r['rank'])
    for r in allr:
        cum += r['secs']
        pts.append(dict(rank=r['rank'], n_chi=r.get('n_chi', r.get('n_chi_census')), a=r['a'], secs=r['secs'], cum_secs=round(cum, 1),
                        pred_secs=r.get('pred_secs'), pred_prior=r.get('pred_secs_prior'), status=r.get('status')))
    return pts


def main():
    queue, rows = load()
    S, meas, nr = summary(queue, rows)
    pts = cost_curve(meas, nr)
    json.dump(dict(summary=S, curve=pts), open(os.path.join(ROOT, 'results', 's71_cost_curve.json'), 'w'), indent=0)
    try:
        import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4))
        ax[0].plot([p['rank'] for p in pts], [p['cum_secs'] / 3600 for p in pts], 'k-')
        ax[0].set_xlabel('queue rank (pre-registered cost order)'); ax[0].set_ylabel('cumulative wall hours'); ax[0].set_title('cost curve')
        ax[1].loglog([p['n_chi'] for p in pts if p['status'] == 'measured'], [p['secs'] for p in pts if p['status'] == 'measured'], 'k.', label='actual')
        ax[1].loglog([p['n_chi'] for p in pts if p['pred_secs']], [p['pred_secs'] for p in pts if p['pred_secs']], 'r.', ms=3, label='re-fitted prediction')
        ax[1].set_xlabel('n_chi'); ax[1].set_ylabel('seconds per cell'); ax[1].legend(); ax[1].set_title('per-cell cost')
        fig.tight_layout(); fig.savefig(os.path.join(ROOT, 'results', 's71_cost_curve.png'), dpi=110)
    except Exception as e:
        print('no plot:', e, file=sys.stderr)
    L = ["# Session 71 — the falsifier sweep over the closing cells: per-cell table\n",
         "One row per queue cell run (`results/s71_queue.json` order = ascending pre-registered certified cost).  `a` = `a_∞` of the tail (Weyl alternation, asserted = census); "
         "`h_pad` = normalisation bound; `n_χ` exact; `|U|` = uncovered residual of the initial-term cover of `E` (the hybrid's exact residual), excess = `|U| − a`; "
         "`i_det = a − mult_det` (`a + 8` `det_4` pencils, seed 11), `i_red = a − mult_red` point-free by (★) (the `ℓ·c` points, seed 29, agreed at every cell), "
         "`i_per4 = a − mult_per4` (`per_4` pencils, seed 47; `0` is a theorem, the column is the engine control); `D = i_det − i_red`; the falsifier is `D > 0`.  "
         "Cost: prior = pre-registered prediction (§2 of the PREREG), refit = after calibration, actual = wall seconds (both primes).  "
         "Every `i_det = 0` is a proof (`mult_det = a` over `Q`, full rank at both primes) and closes the tail for `D > 0` in every degree (ladder theorem); "
         "every `i_red > 0` is exact at both primes with the (★) kernel exhibited.\n",
         f"**{S['n_measured']} cells measured, {S['n_closed']} tails newly closed (`i_det = 0`), {S['n_idet_pos']} with `i_det ≥ 1`, {S['n_D_pos']} with `D > 0`, "
         f"{S['n_iper4_pos']} with `i_per4 > 0`; {S['n_red_first']} reducible-first tails; {S['rungs_settled']} census rungs settled; "
         f"{S['n_closed_total']} of 1 075 tails closed in all ({100*S['frac_closed_total']:.1f} %); {S['n_not_reached']} not reached; "
         f"total {S['total_secs']/3600:.2f} h; largest `n_χ` {S['max_nchi']}, largest `a` {S['max_a']}, largest `N_S` {S['max_NS']}, peak memory {S['hwm_gb']} GB.**\n",
         "| rank | λ | δ | tail ρ | a | h_pad | N_S | Stab | n_χ | \\|U\\| | excess | E_red sieve | i_det | i_red | i_per4 | D | rungs settled | cost prior | cost refit | actual s | primes |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(meas + nr, key=lambda r: r['rank']):
        if r.get('status') != 'measured':
            L.append(f"| {r['rank']} | `{tuple(r['lam'])}` | {r['delta']} | — | {r['a']} | {r['h_pad']} | — | — | — | — | — | — | — | — | — | — | — | {r.get('pred_secs_prior')} | {r.get('pred_secs')} | not reached ({r['secs']} s of {r['bound_secs']}) | — |")
            continue
        U = r['n_chi'] - r['cover_E']['size']
        L.append(f"| {r['rank']} | `{tuple(r['lam'])}` | {r['delta']} | `{tuple(r['tail'])}` | {r['a']} | {r['h_pad']} | {r['N_S']} | {r['stab']} | {r['n_chi']} | {U} | {U - r['a']} | "
                 f"{'yes' if r['cover_Ered']['certified'] else '—'} | {r['i_det']} | {r['i_red']} | {r['i_per4']} | {r['D']} | {r['rungs']} | "
                 f"{r.get('pred_secs_prior')} | {r.get('pred_secs')} | {r['secs']} | {'agree' if r['ok'] else 'DISAGREE'} |")
    open(os.path.join(ROOT, 'results', 's71_sweep.md'), 'w').write("\n".join(L) + "\n")
    print(json.dumps(S, indent=1))


if __name__ == '__main__':
    main()
