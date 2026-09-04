#!/usr/bin/env python3
"""
Session 47 -- Phase A: measure mult_red at cells where the normalisation bound
fires (0 < h_pad < a) and compare with h_pad.

Wraps analysis/wk9_s42_redengine.py and adds the two guards the s42 engine does
not have, because it does not know about h_pad:

  * mult_red > h_pad is IMPOSSIBLE (Corollary B2, docs/reducible_engine.md sec B).
    Seeing it is a bug, not a discovery: the run stops with status 'BUG'.
  * mult_red < h_pad at a firing cell REFUTES the exactness conjecture.  The run
    stops with status 'REFUTED' so the cell can be certified hard.
  * mult_red == h_pad confirms the conjecture at that cell.

h_pad is recomputed here from wk9_s42_hpad, not read from the census, so the
comparison never rests on a cached number.

usage: python3 wk9_s47_sweep.py --cells "9:15,12,6,1,1,1;8:9,9,9,3,1,1" [--route sparse]
       python3 wk9_s47_sweep.py --auto N [--maxns 2000000] [--slot ell7] ...
"""
import sys, os, json, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'results', 's47_cells.jsonl')

from wk9_s42_redengine import measure_cell
from wk9_s42_hpad import h_pad as _h_pad_fn


def h_pad_of(lam, delta):
    return _h_pad_fn(tuple(lam), delta)


def verdict(a, h, mr):
    if mr > h:  return 'BUG'            # Corollary B2 forbids it
    if mr < h:  return 'REFUTED'        # the conjecture fails at this cell
    return 'EXACT'                      # mult_red == h_pad


def run_cell(lam, delta, route='sparse'):
    lam = tuple(lam)
    t0 = time.time()
    h = h_pad_of(lam, delta)
    res = measure_cell(lam, delta, route=route, want_kern=False)
    a, mr = res['a'], res['mult_red']
    assert h < a, ("cell does not fire; not a test of the conjecture", lam, delta, a, h)
    res['h_pad'] = h
    res['verdict'] = verdict(a, h, mr)
    res['deficit'] = a - mr
    res['wall'] = round(time.time() - t0, 1)
    return res


def bank(res):
    with open(OUT, 'a') as f:
        f.write(json.dumps(res) + "\n")


if __name__ == '__main__':
    args = sys.argv[1:]
    route = 'sparse'
    cells = []
    if '--route' in args: route = args[args.index('--route') + 1]
    if '--cells' in args:
        spec = args[args.index('--cells') + 1]
        for part in spec.split(';'):
            part = part.strip()
            if not part: continue
            d, lam = part.split(':')
            cells.append((tuple(int(v) for v in lam.split(',')), int(d)))
    stop = None
    for lam, delta in cells:
        print(f"=== {lam} delta={delta} ===", flush=True)
        try:
            res = run_cell(lam, delta, route=route)
        except Exception as e:
            print(json.dumps(dict(lam=list(lam), delta=delta, status='ERROR',
                                  err=repr(e)[:400])), flush=True)
            traceback.print_exc()
            continue
        bank(res)
        print(json.dumps({k: res[k] for k in
              ('lam','delta','ell','a','h_pad','mult_red','deficit','verdict',
               'n_chi','n_red','nnz_red','nullity','status','wall')}), flush=True)
        if res['verdict'] in ('BUG', 'REFUTED'):
            stop = res
            print(f"!!! STOP: {res['verdict']} at {lam} delta={delta} "
                  f"(a={res['a']} h_pad={res['h_pad']} mult_red={res['mult_red']})", flush=True)
            break
    if stop: sys.exit(3)
