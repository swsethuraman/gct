#!/usr/bin/env python3
"""
Session 71 -- calibration of the hybrid route on BANKED session-60 cells only.

Set (results/PREREG_s71.md sec. 1): every session-60 closing cell with
n_chi <= 6000; the eleven mult_red < a cells of docs/s60_report.md sec. 3 and
the closing cell (24,4,4,4,4)_10; the three largest closed cells.  For every
cell the hybrid must reproduce a, mult_det, mult_red(star), mult_red(pts)
EXACTLY (both primes); mult_per4 must be a (per_4 dominance, results/
s71_per4_dominance.json).  A disagreement halts the session (stopping rule 3).

usage: python3 analysis/wk11_s71_calib.py [--out results/s71_calibration.jsonl] [--max-nchi 6000]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk11_s71_cell import measure_cell, log

BITES = [((8, 4, 4, 4, 4), 6), ((9, 9, 8, 1, 1), 7), ((8, 8, 8, 2, 2), 7), ((12, 4, 4, 4, 4), 7), ((11, 11, 8, 1, 1), 8),
         ((12, 9, 9, 1, 1), 8), ((16, 4, 4, 4, 4), 8), ((13, 9, 8, 1, 1), 8), ((15, 15, 4, 1, 1), 9), ((20, 4, 4, 4, 4), 9),
         ((13, 13, 8, 1, 1), 9), ((24, 4, 4, 4, 4), 10)]
LARGEST = [((24, 4, 4, 4, 4), 10), ((22, 5, 4, 4, 1), 9), ((16, 7, 3, 3, 3), 8)]


def banked():
    cells = {}
    for line in open(os.path.join(ROOT, 'results', 's60_cells.jsonl')):
        c = json.loads(line); cells[(tuple(c['lam']), c['delta'])] = c
    return cells


def calibration_set(cells, max_nchi):
    tails = json.load(open(os.path.join(ROOT, 'results', 's60_tail_census.json')))
    dclose = {tuple(t['tail']): t['delta_close'] for t in tails}
    sel = []
    for (lam, d), c in cells.items():
        if dclose.get(lam[1:]) == d and c['n_chi'] <= max_nchi:
            sel.append((lam, d))
    sel = sorted(set(sel), key=lambda k: cells[k]['n_chi'])
    for k in BITES + LARGEST:
        if k not in sel: sel.append(k)
    return sel


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    outp = arg('--out', os.path.join(ROOT, 'results', 's71_calibration.jsonl'))
    max_nchi = arg('--max-nchi', 6000)
    only = arg('--only', '')
    cells = banked()
    sel = calibration_set(cells, max_nchi)
    if only == 'bites': sel = BITES
    elif only == 'largest': sel = LARGEST
    elif only == 'closing': sel = [k for k in sel if k not in BITES and k not in LARGEST]
    done = set()
    if os.path.exists(outp):
        for line in open(outp):
            r = json.loads(line); done.add((tuple(r['lam']), r['delta']))
    log(f"calibration set: {len(sel)} cells, {len(done)} already done")
    for lam, d in sel:
        if (lam, d) in done: continue
        b = cells[(lam, d)]
        hp = b.get('h_pad')
        t0 = time.time()
        res = measure_cell(lam, d, a_given=b['a'], hpad=hp, certs=None, keep_kernel=False)
        cmp = dict(lam=list(lam), delta=d, n_chi=res['n_chi'], a=res['a'], secs=res['secs'], build_secs=res['build_secs'],
                   sieve_secs=res['sieve_secs'], hybrid_secs={p: v['hybrid']['secs'] for p, v in res['per_prime'].items()},
                   ev_secs={p: v['ev_secs'] for p, v in res['per_prime'].items()},
                   rank_secs={p: v['rank_secs'] for p, v in res['per_prime'].items()},
                   nU=res['n_chi'] - res['cover_E']['size'], excess=res['cover_E']['excess'], cover_order=res['cover_E']['order'],
                   cover_stats=res['cover_E']['stats'], Ered_certified=res['cover_Ered']['certified'],
                   nnz=res['nnz'], nrows=res['nrows'], N_S=res['N_S'],
                   hwm_gb=res['hwm_gb'], attempts={p: len(v['hybrid']['attempts']) for p, v in res['per_prime'].items()},
                   banked=dict(a=b['a'], mult_det=b['mult_det'], mult_red_star=b['mult_red_star'], mult_red_pts=b['mult_red_pts'], route=b['route']),
                   hybrid=dict(mult_det=res['mult_det'], mult_red_star=res['mult_red_star'], mult_red_pts=res['mult_red_pts'], mult_per4=res['mult_per4']),
                   ok=res['ok'])
        agree = (b['a'] == res['a'] and b['mult_det'] == res['mult_det'] and b['mult_red_star'] == res['mult_red_star']
                 and (b['mult_red_pts'] is None or b['mult_red_pts'] == res['mult_red_pts']) and res['mult_per4'] == res['a'] and res['ok'])
        cmp['agree'] = bool(agree)
        with open(outp, 'a') as f: f.write(json.dumps(cmp) + "\n")
        log(f"CALIB {lam} d{d}: n_chi={res['n_chi']} banked det/star/pts = {b['mult_det']}/{b['mult_red_star']}/{b['mult_red_pts']} "
            f"hybrid = {res['mult_det']}/{res['mult_red_star']}/{res['mult_red_pts']} per4={res['mult_per4']} a={res['a']} "
            f"{'AGREE' if agree else '*** DISAGREE ***'} ({res['secs']}s)")
        if not agree:
            log("calibration disagreement: halting (stopping rule 3)"); sys.exit(2)
    log("calibration complete: every cell agrees")
