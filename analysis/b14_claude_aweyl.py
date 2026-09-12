#!/usr/bin/env python3
"""Batch-14 strategy session (Claude) -- a thin driver for the house a_weyl.

STATUS: scratch, planning computation; not pre-registered.
Provenance: docs/b14_claude_scratch_code.md.

`analysis/wk9_s42_census.a_weyl(lam, delta, n)` is the programme's ambient
multiplicity (plethysm) routine.  This script only runs it at a named cell with
a timer and a banked control, so that a single number can be reproduced from one
command line and its cost recorded.

CONTROLS (run by default; both are banked values; measured cost 1 s and 101 s):
    n=3  (19,7,2^5)  delta=12  ->  6     the n=3 LMR cell (docs/lmr_cell.md 3b)
    n=4  (17,17,2^7) delta=12  ->  2     the LMR ladder bottom (results/s63_aladder.json)
Pass --no-control to skip them when sweeping several cells.

CELLS COMPUTED FOR THE BATCH-14 MEMO (n=4; measured 217-271 s each, 2 cores):
    63,19,2,2,2,2,2,2,2  delta 24  ->  390
    67,19,2,2,2,2,2,2,2  delta 25  ->  391
    69,21,2,2,2,2,2,2,2  delta 26  ->  531   (reproduces B13-06)
    73,21,2,2,2,2,2,2,2  delta 27  ->  532
Two more were wanted and not finished inside the session's bound:
    77,21,2,2,2,2,2,2,2  delta 28  (the closing cell of the (21,2^7) ladder;
                                    the stable count says a_inf = 533)
    68,17,2^7,1 / 67,17,2^8  delta 25  (ten-row cells; both exceeded 560 s)

usage:
    python3 analysis/b14_claude_aweyl.py --cell 63,19,2,2,2,2,2,2,2 --delta 24 [--n 4]
    python3 analysis/b14_claude_aweyl.py --controls
    [--no-control] to skip the controls before a cell
"""
import argparse, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s42_census import a_weyl              # noqa: E402

CONTROLS = [((19, 7, 2, 2, 2, 2, 2), 12, 3, 6),
            ((17, 17, 2, 2, 2, 2, 2, 2, 2), 12, 4, 2)]


def run(lam, delta, n):
    t = time.time()
    v = a_weyl(lam, delta, n, {})
    return v, time.time() - t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cell')
    ap.add_argument('--delta', type=int)
    ap.add_argument('--n', type=int, default=4)
    ap.add_argument('--controls', action='store_true')
    ap.add_argument('--no-control', action='store_true')
    args = ap.parse_args()

    ok = True
    if args.controls or not args.no_control:
        for lam, delta, n, want in CONTROLS:
            v, secs = run(lam, delta, n)
            ok &= v == want
            print(f'CONTROL n={n} {lam} delta={delta}: a={v} (banked {want}), '
                  f'{secs:.0f}s -> {"PASS" if v == want else "FAIL"}', flush=True)
        if not args.cell:
            return 0 if ok else 1
        if not ok:
            return 1

    lam = tuple(int(x) for x in args.cell.split(','))
    delta = args.delta if args.delta else sum(lam) // args.n
    v, secs = run(lam, delta, args.n)
    print(f'n={args.n} {lam} delta={delta}: a={v}, {secs:.0f}s')
    return 0


if __name__ == '__main__':
    sys.exit(main())
