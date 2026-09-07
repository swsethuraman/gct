#!/usr/bin/env python3
"""Session 64 calibration driver.

Runs the common-source three-way engine (wk10_s64_cell) over a list of cells,
cross-checks each measured (mult_det, mult_red) against the session-60 banked
values, records mult_pad, and applies the calibration verdicts:

  * containment      mult_pad <= mult_red   (halt on violation, stopping rule S2)
  * r<=5 exactness   mult_pad == mult_red   (P_5 = R_5; FAIL blocks success)
  * banked agreement mult_det, mult_red match the s60 ledger (else FLAG)

Banks each cell to results/s64_calibration.jsonl as it completes, saves the
kernel artefact, and (optionally) writes point/HWV certificates.

usage: python3 analysis/wk10_s64_calibrate.py cells.json [--dense-cap N] [--seeds 2]
       cells.json : [{"delta":7,"lam":[9,9,8,1,1],"mult_det":2,"mult_red":1,"a":2,"hpad":1}, ...]
"""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk10_s64_cell import measure_cell
from wk9_s45_build import log

OUT = os.path.join(ROOT, 'results/s64_calibration.jsonl')
KERN = os.path.join(ROOT, 'results/s64_kern')


def main():
    cells = json.load(open(sys.argv[1]))
    def arg(name, d):
        return type(d)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else d
    dense_cap = arg('--dense-cap', 4600); seeds = arg('--seeds', 2)
    os.makedirs(KERN, exist_ok=True)
    done = set()
    if os.path.exists(OUT):
        for ln in open(OUT):
            try:
                r = json.loads(ln); done.add((r['delta'], tuple(r['lam'])))
            except Exception: pass
    for c in cells:
        key = (c['delta'], tuple(c['lam']))
        if key in done:
            log(f"  skip (already banked): {key}"); continue
        t0 = time.time()
        res, kern = measure_cell(c['lam'], c['delta'], seeds=seeds, dense_cap=dense_cap,
                                 want_kern=True, a_given=c.get('a'), hpad=c.get('hpad'), verbose=True)
        if res.get('status', '').startswith('skipped'):
            log(f"  {key}: {res['status']} (n_chi={res['n_chi']} > cap {dense_cap}); route to sparse")
            res['calibration'] = dict(route='needs_sparse')
            with open(OUT, 'a') as f: f.write(json.dumps(res) + "\n")
            continue
        # banked cross-check
        banked = dict(mult_det=c.get('mult_det'), mult_red=c.get('mult_red'))
        agree_det = (banked['mult_det'] is None) or (res['mult_det'] == banked['mult_det'])
        agree_red = (banked['mult_red'] is None) or (res['mult_red'] == banked['mult_red'])
        res['banked'] = banked
        res['calibration'] = dict(
            route='dense', banked_det_ok=bool(agree_det), banked_red_ok=bool(agree_red),
            containment_ok=bool(res['checks'].get('containment_pad_le_red', True)),
            r5_exact_ok=bool(res['checks'].get('P5eqR5_pad_eq_red', True)) if res['ell'] <= 5 else None,
            pad_eq_red=(res['mult_pad'] == res['mult_red']),
            PASS=bool(agree_det and agree_red and res['ok']))
        # save kernel artefact
        tag = '_'.join(map(str, c['lam'])) + f"_d{c['delta']}"
        if kern:
            import gzip
            art = dict(cell=dict(n=4, r=res['ell'], lam=res['lam'], delta=res['delta'], a=res['a'],
                                 n_chi=res['n_chi'], prime=int(kern['prime'])),
                       mult=dict(det=res['mult_det'], red=res['mult_red'], pad=res['mult_pad']),
                       conventions={"kernel": "kern[j]=j-th HWV of weight lambda in chi-coords (E kern=0)",
                                    "U": "U[side]: basis of ker T_side in a-coords; sum_j U[k][j] kern[j] in I(side)"},
                       kern=kern['kern'].tolist(), U=kern['U'], U_terms=kern['U_terms'])
            with gzip.open(os.path.join(KERN, f'kern_{tag}.json.gz'), 'wt', encoding='utf-8') as f:
                json.dump(art, f, separators=(',', ':'))
        with open(OUT, 'a') as f: f.write(json.dumps(res) + "\n")
        v = res['calibration']
        log(f"  BANKED {key}: mult_det={res['mult_det']} mult_red={res['mult_red']} mult_pad={res['mult_pad']} "
            f"D={res['D']} | banked det/red {agree_det}/{agree_red} pad=red {v['pad_eq_red']} PASS={v['PASS']} "
            f"({time.time()-t0:.0f}s)")
        if 'STOP' in res:
            log(f"  *** STOP: {res['STOP']} at {key} -- halting the sweep (stopping rule S2)")
            sys.exit(2)
    log("calibration driver done")


if __name__ == '__main__':
    main()
