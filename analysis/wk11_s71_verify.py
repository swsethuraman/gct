#!/usr/bin/env python3
"""
Session 71 -- independent re-derivation of sweep cells by session 60's route.

For each named cell, session 60's `wk9_s60_cell.measure_cell` (the Wiedemann
certificates on [E; ev_det] and on E_red with the h_pad floor; unchanged code,
the same point seeds 11 / 29, so the matrices are identical) is run at both
primes and compared with the session-71 hybrid record.  The two instruments
share the build (wk9_s45_build) and nothing else: the hybrid's cover, Schur
residual, projection and lift against the Wiedemann minimal polynomial and its
nonsingularity certificate.  Agreement is recorded per cell in
results/s71_verify.jsonl; a disagreement halts (stopping rule 3).

usage: python3 analysis/wk11_s71_verify.py "43,15,4,1,1:16" "32,9,9,1,1:13" ...
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/home/claude/s71/wied71')
os.environ.setdefault('WIED_WORK', '/home/claude/s71/work')
import wk11_s71_codes; wk11_s71_codes.install()
from wk9_s60_cell import measure_cell, log

OUT = os.path.join(ROOT, 'results', 's71_verify.jsonl')

if __name__ == '__main__':
    rec = {}
    for line in open(os.path.join(ROOT, 'results', 's71_sweep.jsonl')):
        r = json.loads(line)
        if r.get('status') == 'measured': rec[(tuple(r['lam']), r['delta'])] = r
    for spec in sys.argv[1:]:
        lam, d = spec.split(':'); lam = tuple(int(x) for x in lam.split(',')); d = int(d)
        r71 = rec[(lam, d)]
        t0 = time.time()
        res, _ = measure_cell(lam, d, route='sparse', red_points='always', hpad=r71['h_pad'], a_given=r71['a'],
                              parallel=False, certs=None, levels='auto')
        cmp = dict(lam=list(lam), delta=d, n_chi=res['n_chi'], a=res['a'], secs_wiedemann=res['secs'], secs_hybrid=r71['secs'],
                   wiedemann=dict(mult_det=res['mult_det'], mult_red_star=res['mult_red_star'], mult_red_pts=res['mult_red_pts'],
                                  route=res['route'], levels=res['levels'], per_prime={p: v['sides'] for p, v in res['per_prime'].items()}),
                   hybrid=dict(mult_det=r71['mult_det'], mult_red_star=r71['mult_red_star'], mult_red_pts=r71['mult_red_pts'], mult_per4=r71['mult_per4']))
        agree = (res['mult_det'] == r71['mult_det'] and res['mult_red_star'] == r71['mult_red_star']
                 and (res['mult_red_pts'] is None or res['mult_red_pts'] == r71['mult_red_pts']) and res['ok'])
        cmp['agree'] = bool(agree)
        with open(OUT, 'a') as f: f.write(json.dumps(cmp) + "\n")
        log(f"VERIFY {lam} d{d}: wiedemann det/star/pts = {res['mult_det']}/{res['mult_red_star']}/{res['mult_red_pts']} "
            f"hybrid = {r71['mult_det']}/{r71['mult_red_star']}/{r71['mult_red_pts']} {'AGREE' if agree else '*** DISAGREE ***'} "
            f"({res['secs']}s vs {r71['secs']}s)")
        if not agree:
            log("disagreement between instruments: halting (stopping rule 3)"); sys.exit(2)
