#!/usr/bin/env python3
"""
Session 41 -- one cell in its own process (so the VmHWM in the ledger is the
cell's own peak and memory is returned to the container between cells).

usage: python3 wk9_s41_cell.py --lam 16,4,2,2,2,2 --delta 7 --a 2 --out /root/s41/x.pkl
                               [--npts K] [--seed-det 11 --seed-pad 29] [--route auto|exact|compressed|inplace]
Writes the pickle (per-prime kernels, mults, sizes, hwm) and prints one JSON line.
"""
import sys, os, json, pickle, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s41_kernel import measure_cell, mult_red_of, vm_hwm

def arg(name, default=None):
    if name in sys.argv: return sys.argv[sys.argv.index(name) + 1]
    return default

if __name__ == '__main__':
    lam = tuple(int(x) for x in arg('--lam').split(','))
    delta = int(arg('--delta')); a = int(arg('--a'))
    out = arg('--out')
    npts = int(arg('--npts')) if arg('--npts') else None
    seeds = dict(det=int(arg('--seed-det', 11)), pad=int(arg('--seed-pad', 29)))
    route = arg('--route', 'auto')
    r = len(lam)
    res = measure_cell(4, r, delta, lam, a, npts=npts, seeds=seeds, route=route)
    mr, nnr, nr = mult_red_of(res)
    res['mult_red'] = mr; res['nonred_orbits'] = nnr; res['red_orbits'] = nr
    res['hwm'] = vm_hwm()
    pickle.dump(res, open(out, 'wb'))
    summ = {k: res[k] for k in ('lam', 'delta', 'a', 'N_S', 'stab', 'n_chi', 'nrows', 'route',
                                 'mult_det', 'mult_pad', 'mult_red', 'npts', 'secs', 'hwm')}
    print("RESULT " + json.dumps(summ), flush=True)
