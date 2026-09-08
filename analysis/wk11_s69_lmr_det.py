#!/usr/bin/env python3
"""Session 69: the det-side worker for the LMR cell, running concurrently with phase A of
wk11_s69_lmr.py.  It reads the phase-A state (the accepted fillings, in order), evaluates every
filling not yet done at the K_det det_4 pencils at prime p, and banks the rows in its own
state file results/s69_lmr_det_<p>.json (resumable).  When phase A has finished (rank 274) and
all rows are present it reports rank (= mult_det, a rigorous lower bound over Q), the left
kernel (U_D as a circuit) and i_det = 274 - rank.

    python3 analysis/wk11_s69_lmr_det.py [--p 2147483647] [--kdet 290] [--once]
"""
import argparse, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                              # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs, dp_eval_c, rank_mod, left_kernel_mod)  # noqa: E402
from wk11_s69_lmr import det_points, STATE, A_LMR, N_DEG, R                  # noqa: E402

T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=P1)
    ap.add_argument("--kdet", type=int, default=290)
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--poll", type=int, default=60)
    args = ap.parse_args()
    p = args.p
    A, idx, fact, tab = sym_table(N_DEG, R)
    my = os.path.join(ROOT, "results", f"s69_lmr_det_{p}.json")
    st = json.load(open(my)) if os.path.exists(my) else dict(p=p, kdet=args.kdet, det_seed=11, det_bound=30, rows=[], fillings=[])
    pts, As = det_points(args.kdet)
    msyms = [symbols_from_coeffs(cv, N_DEG, R, p) for cv in pts]
    while True:
        if not os.path.exists(STATE):
            time.sleep(args.poll); continue
        A_state = json.load(open(STATE))
        basis = A_state["basis"]
        # consistency: our fillings must be a prefix of the phase-A basis
        for i, Fj in enumerate(st["fillings"]):
            assert Fj == basis[i], "phase-A basis changed under the det worker"
        done_before = len(st["rows"])
        for i in range(len(st["rows"]), len(basis)):
            F = Filling.from_json(basis[i])
            t = time.time()
            row = [dp_eval_c(F, msy, p, tab) for msy in msyms]
            st["rows"].append(row); st["fillings"].append(basis[i])
            tmp = my + ".tmp"; json.dump(st, open(tmp, "w")); os.replace(tmp, my)
            log(f"  det rows p={p}: {i+1}/{len(basis)} ({(time.time()-t)/len(msyms):.3f}s/eval)")
        finished = A_state.get("generic_rank_P1", 0) >= A_LMR and len(st["rows"]) == len(basis)
        if finished:
            st["det_rank"] = rank_mod(st["rows"], p)
            st["kernel"] = left_kernel_mod(st["rows"], p)
            st["i_det"] = A_LMR - st["det_rank"]
            tmp = my + ".tmp"; json.dump(st, open(tmp, "w")); os.replace(tmp, my)
            log(f"FINAL p={p}: det rank {st['det_rank']} -> i_det = {st['i_det']}, kernel dim {len(st['kernel'])}")
            return
        if args.once: return
        if len(st["rows"]) == done_before:
            time.sleep(args.poll)


if __name__ == "__main__":
    main()
