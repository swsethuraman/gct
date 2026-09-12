#!/usr/bin/env python3
"""Batch-14 strategy session (Claude) -- h_pad(lam, delta) at any degree.

    h_pad(lam,delta) = sum_mu a3(mu,delta)   over the horizontal-delta-strips lam/mu
                     = mult of S_lam in Sym^delta V tensor Sym^delta(Sym^3 V)

which is the dimension of the target of the reducible pullback F |-> F(l.c) on
the weight-lam highest-weight space -- the number the batch-14 complete-
interpolation certificate needs (73 at rung 13, 159 at rung 14).

This is analysis/wk13_b13_01_hpad.py (B13-01) with the degree unfixed: same
strips (wk9_s42_hpad.pieri_strips), same Weyl alternation, same per-strip
backtracking, but the multiset counter is analysis/b14_claude_hpad_general.c,
which takes delta on the command line.  See that file for the two changes it
carries over B13-01's wk13_b13_01_mcount.c.

CONTROL (run first, always): `--cell 21,17,2,2,2,2,2,2,2 --delta 13` must print
h_pad = 73 with per-strip a3 = [1,2,2,3,3,4,4,5,5,5,6,7,8,9,9] over 15 strips,
which is B13-01's banked result (results/b13_01_hpad.json).

MEASURED here (2 cores, in-container): rung 13 ~32 s, rung 14 ~45 s.

STATUS: scratch.  Single code lineage -- it shares the counter and the strip
enumeration with B13-01, so it is NOT an independent recount of 73.  The
batch-14 memo asks for the recount to be done by a different method.

usage:
    python3 analysis/b14_claude_hpad.py                                      # control only
    python3 analysis/b14_claude_hpad.py --cell 25,17,2,2,2,2,2,2,2 --delta 14  # control, then the cell
    [--no-control]  skip the control   [--bin PATH]  compiled counter (default: built in /tmp)
"""
import argparse, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s42_hpad import pieri_strips          # noqa: E402  (B13-01's source of strips)

CSRC = os.path.join(HERE, 'b14_claude_hpad_general.c')


def ensure_bin(path=None):
    path = path or '/tmp/b14_mcount_general'
    if not os.path.exists(path):
        subprocess.run(['gcc', '-O2', '-o', path, CSRC], check=True)
    return path


def hpad(lam, delta, mcount_bin):
    """(h_pad, [(mu, a3(mu,delta)), ...]) by Weyl alternation, exactly as B13-01."""
    rho = tuple(range(8, -1, -1))
    strips = [tuple(x for x in m if x) for m in pieri_strips(lam, delta)]
    per_mu, allnu = [], {}
    for mu in strips:
        mm = tuple(mu) + (0,) * (9 - len(mu))
        L = [mm[i] + rho[i] for i in range(9)]
        terms, used, perm = [], [False] * 9, [-1] * 9

        def bt(pos):
            if pos == 9:
                s = 1
                for i in range(9):
                    for j in range(i + 1, 9):
                        if perm[i] > perm[j]:
                            s = -s
                nu = tuple(sorted((L[perm[i]] - rho[i] for i in range(9)), reverse=True))
                allnu.setdefault(nu, len(allnu))
                terms.append((s, nu))
                return
            for j in range(9):
                if used[j] or L[j] < rho[pos]:
                    continue
                used[j] = True; perm[pos] = j
                bt(pos + 1)
                used[j] = False; perm[pos] = -1

        bt(0)
        per_mu.append((mu, terms))

    nus = list(allnu)
    stdin = '%d\n' % len(nus) + ''.join(' '.join(map(str, n)) + '\n' for n in nus)
    run = subprocess.run([mcount_bin, str(delta)], input=stdin, capture_output=True, text=True)
    if run.returncode:
        raise SystemExit(f'counter failed ({run.returncode}): {run.stderr.strip()}')
    vals = [int(x) for x in run.stdout.split()]
    m = dict(zip(nus, vals))
    rows = [(mu, sum(s * m[tuple(n)] for s, n in tm)) for mu, tm in per_mu]
    return sum(a for _, a in rows), rows


CONTROL = ((21, 17, 2, 2, 2, 2, 2, 2, 2), 13, 73,
           [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9, 9])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cell')
    ap.add_argument('--delta', type=int)
    ap.add_argument('--no-control', action='store_true',
                    help='skip the rung-13 control (it runs by default)')
    ap.add_argument('--bin')
    args = ap.parse_args()
    binary = ensure_bin(args.bin)

    if not args.no_control:
        lam, delta, want, want_a3 = CONTROL
        t = time.time(); h, rows = hpad(lam, delta, binary)
        a3 = sorted(a for _, a in rows)
        ok = (h == want and a3 == want_a3)
        print(f'CONTROL {lam} delta={delta}: h_pad={h} (B13-01: {want}), '
              f'strips={len(rows)}, a3={a3}, {time.time() - t:.1f}s -> {"PASS" if ok else "FAIL"}')
        if not args.cell:
            return 0 if ok else 1
        if not ok:
            return 1

    lam = tuple(int(x) for x in args.cell.split(','))
    delta = args.delta if args.delta else sum(lam) // 4
    t = time.time(); h, rows = hpad(lam, delta, binary)
    print(f'{lam} delta={delta}: h_pad={h}, strips={len(rows)}, '
          f'a3={sorted(a for _, a in rows)}, {time.time() - t:.1f}s')
    for mu, a in rows:
        print(f'  mu={mu} a3={a}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
