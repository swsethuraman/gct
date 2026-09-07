#!/usr/bin/env python3
"""
Session 63 -- the TWO-SIDED n=3 LMR control (integrator note 2 to 62/63 sec.4).

The delta=12 drop (mult_det=5 < a=6) is a one-sided pass: random evaluation only
LOWER-bounds rank, so the measurement gives i_det <= 1 and the >= 1 is the LMR
theorem.  A degenerate evaluation family would fake the same drop.  The ladder
supplies the two-sided control: BELOW the closing degree delta_close = 12 the
module is vacuous, so the engine MUST return full rank.

    delta = 9   a = 2   expect mult_det = 2   (full rank, i_det = 0)
    delta = 10  a = 4   expect mult_det = 4   (full rank, i_det = 0)
    delta = 11  a = 5   expect mult_det = 5   (full rank, i_det = 0)
    delta = 12  a = 6   expect mult_det = 5   (RANK DROP,  i_det = 1)

If full rank at 9,10,11 and a drop only at 12, the instrument does not
under-report rank and the control is two-sided.  A drop before 12 means the
delta=12 drop is worthless and the engine needs fixing.  Also: delta=11 full rank
+ ladder monotonicity + LMR reproduces the 273/274 predecessor argument in
miniature (mult_det(11)=5 full ==> mult_det(12) >= 5 ==> i_det(12) <= 1 ==> =1).

usage: python3 analysis/wk10_s63_n3ladder.py <delta> <prime>   # one rung, one prime
       appends a JSON line to results/s63_n3ladder.jsonl
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/root/wied60')
os.environ.setdefault('WIED_WORK', '/root/s63work')
import numpy as np
import pickle
from scipy import sparse
import wk10_s63_n3control as C
from wk9_s45_build import build_cell
from wk9_s45_cell import nullity_stacked, LEVELS
from wk9_s42_census import a_weyl

JSONL = os.path.join(ROOT, 'results', 's63_n3ladder.jsonl')


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def cell(delta):
    return (3 * delta - 17, 7, 2, 2, 2, 2, 2)


def get_build(delta):
    os.makedirs('/root/s63work', exist_ok=True)
    cache = f'/root/s63work/n3_build_d{delta}.pkl'
    if delta == 12 and os.path.exists('/root/s63work/n3_build.pkl'):
        cache = '/root/s63work/n3_build.pkl'
    if os.path.exists(cache):
        return pickle.load(open(cache, 'rb'))
    B = build_cell(cell(delta), delta, n=3, verbose=True)
    pickle.dump(B, open(cache, 'wb'))
    return B


def main():
    delta = int(sys.argv[1]); p = int(sys.argv[2])
    lam = cell(delta)
    a = a_weyl(lam, delta, 3, {})
    t0 = time.time()
    B = get_build(delta)
    nc = B['n_chi']
    log(f"[n=3 ladder] delta={delta} lam={lam} a={a} n_chi={nc} nrows={B['nrows']} nnz={B['nnz']}")
    pencils = C.det3_pencils(a + 8, 20260907, 40)
    cd = [C.det3_coeffs(pp) for pp in pencils]
    EVd = C.ev_rows_from_coeffs(B['arr'], cd, p)
    EVs = sparse.csr_matrix(EVd % p)
    tk = time.time()
    k, kern, lvl, diag = nullity_stacked(B['E'], EVs, nc, p, want_kern=True, seed0=1,
                                         tag=f'n3lad_d{delta}_{p}', levels=LEVELS['cheap'], verbose=True)
    mult = a - k
    expect_full = (delta < 12)
    ok = (mult == a) if expect_full else (k >= 1)
    row = dict(delta=delta, lam=list(lam), n=3, r=7, a=int(a), n_chi=int(nc), prime=int(p),
               nullity_i_det=int(k), mult_det=int(mult), expect=('full rank' if expect_full else 'drop'),
               as_expected=bool(ok), K=a + 8, seed=20260907, level=int(lvl),
               secs=round(time.time() - tk, 1), total_secs=round(time.time() - t0, 1))
    with open(JSONL, 'a') as fh:
        fh.write(json.dumps(row) + "\n")
    log(f"  RESULT delta={delta} p={p}: a={a} i_det={k} mult_det={mult}  expect={'full' if expect_full else 'drop'}  "
        f"{'OK' if ok else '*** UNEXPECTED ***'}  ({row['secs']}s)")
    print("RESULT " + json.dumps(row))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
