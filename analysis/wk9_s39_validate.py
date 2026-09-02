#!/usr/bin/env python3
"""
Session 39 -- P1: the stabiliser reduction reproduces s36 ledger cells and the
witness IN THIS CLONE/CONTAINER, before it is used for Phase 1.

Cells (pre-registered in results/PREREG_s39.md, chosen before running):
  (8,4,4,4,4)   delta 6  -- the D = -1 cell (most discriminating): a 2, mult_det 2, mult_pad 1
  (11,4,4,4,1)  delta 6  -- cheapest ell=5 row:                     a 2, mult_det 2, mult_pad 2
  (13,8,4,1,1,1) delta 7 -- cheapest ell=6 row:                     a 2, mult_det 2, mult_pad 2
Witness: l^3 m, (4,4), delta 2 -- reduced kernel prop (12,-3,1), mult 0.

Prints the reproduced tuple against the ledger; any deviation -> P1 FAIL (stop).
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s36_stabred import (measure_reduced, orbit_setup, reduced_rows,
                             kernel_exact, expand, P1, P2)
from wk8_s30_core import per_padded

# ledger truth (results/s36_ledger.md)
CELLS = [
    ((8, 4, 4, 4, 4), 6, dict(a=2, N_S=94675, stab=24, n_chi=4562, mult_det=2, mult_pad=1)),
    ((11, 4, 4, 4, 1), 6, dict(a=2, N_S=11574, stab=6, n_chi=2113, mult_det=2, mult_pad=2)),
    ((13, 8, 4, 1, 1, 1), 7, dict(a=2, N_S=27213, stab=6, n_chi=1844, mult_det=2, mult_pad=2)),
]
OUT = os.path.join(HERE, '..', 'results', 's39_validation.md')


def emit(s):
    print(s, flush=True)
    with open(OUT, 'a') as fh: fh.write(s + '\n')


def witness():
    # the s36 witness: l^3 m = per_padded(1,4) (x0^3 . x1), weight (4,4), delta 2;
    # the reduced kernel must be prop (12,-3,1) (corrected rule), not (1,-4,3).
    ok = True
    basis, vecs, group = orbit_setup(4, 2, 2, (4, 4), verbose=False)
    rows, _ = reduced_rows(4, 2, 2, (4, 4), vecs, verbose=False)
    for p in (P1, P2):
        a, rk, kern = kernel_exact(rows, len(vecs), p)
        full = expand(vecs, kern[0], p)
        v = [full.get(m, 0) for m in basis]
        inv = pow(v[2], p - 2, p); vn = tuple(x * inv % p for x in v)
        good = (a == 1 and vn == (12 % p, (-3) % p, 1))
        ok &= good
        emit('- witness `l^3 m` (4,4) d2, p=%d: a=%d kernel %s %s'
             % (p, a, '(12,-3,1)' if good else vn, 'ok' if good else '**FAIL**'))
    return ok


def main():
    open(OUT, 'w').write('# Session 39 — P1 reduction validation (reproduce s36 ledger cells + witness)\n\n')
    ok = True
    okw = witness(); ok &= okw
    emit('')
    for lam, delta, truth in CELLS:
        t0 = time.time()
        res = measure_reduced(4, len(lam), delta, lam, truth['a'], verbose=True)
        got = dict(a=res['a'], N_S=res['N_S'], stab=res['stab'], n_chi=res['n_chi'],
                   mult_det=res['mult_det'], mult_pad=res['mult_pad'])
        good = all(got[k] == truth[k] for k in truth)
        ok &= good
        emit('- `%s` d%d: got %s vs ledger %s — %s [%.0fs]'
             % (lam, delta, got, truth, 'ok' if good else '**FAIL**', time.time() - t0))
    emit('\n**P1: %s**' % ('PASS' if ok else 'FAIL — STOP'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
