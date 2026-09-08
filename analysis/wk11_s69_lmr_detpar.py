#!/usr/bin/env python3
"""Session 69: parallel det-side finisher for the LMR cell.  Reads the spanner's basis from
results/s69_lmr_state.json, evaluates every filling at K_det det_4 pencils at prime p across a
process pool (reusing rows already banked in results/s69_lmr_det_<p>.json), then reports
rank = mult_det (a rigorous lower bound on mult_det over Q), the left kernel (U_D as a circuit)
and i_det = 274 - rank.  det points are reproducible from the recorded seed.

    python3 analysis/wk11_s69_lmr_detpar.py --p 2147483647 [--kdet 290] [--workers 2]
"""
import argparse, json, os, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                              # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs, dp_eval_c, rank_mod, left_kernel_mod)  # noqa: E402
from wk11_s69_lmr import det_points, STATE, A_LMR, N_DEG, R                  # noqa: E402

T0 = time.time(); _MS = None; _TAB = None


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def _init(msyms, tab):
    global _MS, _TAB
    _MS = msyms; _TAB = tab


def _eval(Fj):
    F = Filling.from_json(Fj)
    return [dp_eval_c(F, ms, _MS_P, _TAB) for ms in _MS]


_MS_P = None


def _initp(msyms, tab, p):
    global _MS, _TAB, _MS_P
    _MS = msyms; _TAB = tab; _MS_P = p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=P1)
    ap.add_argument("--kdet", type=int, default=290)
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    p = args.p
    A, idx, fact, tab = sym_table(N_DEG, R)
    pts, As = det_points(args.kdet)
    msyms = [symbols_from_coeffs(cv, N_DEG, R, p) for cv in pts]
    st = json.load(open(STATE))
    basis = st["basis"]
    log(f"basis {len(basis)} (generic rank {st.get('generic_rank_P1')}); det at p={p}, {args.kdet} pencils")
    my = os.path.join(ROOT, "results", f"s69_lmr_det_{p}.json")
    old = json.load(open(my)) if os.path.exists(my) else dict(rows=[], fillings=[])
    rows = []
    # reuse banked rows whose filling matches the current basis prefix and has the right width
    for i, (Fj, row) in enumerate(zip(old.get("fillings", []), old.get("rows", []))):
        if i < len(basis) and Fj == basis[i] and len(row) == args.kdet:
            rows.append(row)
        else:
            break
    log(f"reusing {len(rows)} banked det rows")
    todo = basis[len(rows):]
    if todo:
        with Pool(args.workers, initializer=_initp, initargs=(msyms, tab, p)) as pool:
            for j, row in enumerate(pool.imap(_eval, todo, chunksize=4)):
                rows.append(row)
                if (len(rows)) % 20 == 0:
                    json.dump(dict(p=p, kdet=args.kdet, det_seed=11, det_bound=30, fillings=basis[:len(rows)], rows=rows),
                              open(my + ".tmp", "w")); os.replace(my + ".tmp", my)
                    log(f"  det {len(rows)}/{len(basis)} ({(time.time()-T0)/max(len(rows)-len(old.get('rows',[])),1):.1f}s/filling)")
    det_rank = rank_mod(rows, p)
    kern = left_kernel_mod(rows, p)
    out = dict(p=p, kdet=args.kdet, det_seed=11, det_bound=30, fillings=basis, rows=rows,
               det_rank=det_rank, i_det=A_LMR - det_rank, kernel=kern, a=A_LMR, generic_rank=st.get("generic_rank_P1"))
    json.dump(out, open(my, "w"))
    log(f"FINAL p={p}: basis {len(basis)}, det rank {det_rank} -> mult_det = {det_rank}, i_det = {A_LMR - det_rank}, kernel dim {len(kern)}")


if __name__ == "__main__":
    main()
