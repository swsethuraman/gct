#!/usr/bin/env python3
"""Session 69: parallel pooled spanner for the LMR cell (replaces the incremental phase A of
wk11_s69_lmr.py once the coupon-collector tail dominates).  Same object, same points, same
state file -- so the det worker (wk11_s69_lmr_det.py) keeps consuming the growing `basis`.

Fixed set of NPTS = a + margin generic points at P1 (seeds recorded).  Rounds: each round
samples a batch of fillings, evaluates every nonzero one at all NPTS points across a process
pool (2 workers), and grows a maximal independent set (in discovery order) by incremental
flint rank.  The independent set is written to results/s69_lmr_state.json as `basis` (JSON
fillings, in order) after every round, exactly the contract phase A used.  Stops at rank
A_LMR = 274 or --maxrounds.

    python3 analysis/wk11_s69_lmr_span.py [--batch 240] [--npts 300] [--workers 2] [--maxrounds 200]
"""
import argparse, json, os, random, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1                                                  # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table, symbols_from_coeffs, generic_point,
                              dp_eval_c, rank_mod, PRIMES)                    # noqa: E402
from wk11_s69_lmr import STATE, A_LMR, N_DEG, R, H, DELTA, N2, N1            # noqa: E402

T0 = time.time()
_MS = None   # per-worker: list of symbol lists at the fixed generic points
_TAB = None


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def _init(msyms, tab):
    global _MS, _TAB
    _MS = msyms; _TAB = tab


def _eval_filling(Fj):
    F = Filling.from_json(Fj)
    v0 = dp_eval_c(F, _MS[0], P1, _TAB)
    if v0 == 0:
        return None
    row = [v0] + [dp_eval_c(F, ms, P1, _TAB) for ms in _MS[1:]]
    return (Fj, row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=240)
    ap.add_argument("--npts", type=int, default=300)     # >= a + margin
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--maxrounds", type=int, default=400)
    ap.add_argument("--kset", default="6,7,8,9")
    ap.add_argument("--seed", type=int, default=4242)
    args = ap.parse_args()
    A, idx, fact, tab = sym_table(N_DEG, R)
    kset = [int(x) for x in args.kset.split(",")]

    # fixed generic points at P1 (same rule as phase A so the two are compatible; recorded)
    NPTS = args.npts
    msyms = [symbols_from_coeffs(generic_point(N_DEG, R, P1, random.Random(69 * 1000 + i)), N_DEG, R, P1) for i in range(NPTS)]

    st = json.load(open(STATE)) if os.path.exists(STATE) else dict(basis=[], hist=[], samples=0)
    st.setdefault("lam", list((65, 17) + (2,) * 7)); st.setdefault("delta", DELTA); st.setdefault("a", A_LMR)
    st["span_method"] = "parallel pooled (wk11_s69_lmr_span.py)"; st["npts_generic"] = NPTS
    st["generic_seed_rule"] = "random.Random(69*1000+i), uniform mod P1, point i"
    basis = [Filling.from_json(F) for F in st["basis"]]
    if st.get("rows") and st["rows"] and len(st["rows"][0]) == NPTS and len(st["rows"]) == len(basis):
        rows = st["rows"]
        rank = rank_mod(rows, P1) if rows else 0
        log(f"resume: reusing {len(rows)} seeded rows at {NPTS} points, rank {rank}")
    else:
        log(f"resume: {len(basis)} basis fillings; evaluating them at {NPTS} fixed points to seed the rank")
        with Pool(args.workers, initializer=_init, initargs=(msyms, tab)) as pool:
            seed_rows = pool.map(_eval_filling, [F.to_json() for F in basis])
        keep, keeprows = [], []
        for F, pr in zip(basis, seed_rows):
            if pr is None: continue
            if rank_mod(keeprows + [pr[1]], P1) > len(keep):
                keep.append(F); keeprows.append(pr[1])
        basis, rows = keep, keeprows
        rank = rank_mod(rows, P1) if rows else 0
    st["basis"] = [F.to_json() for F in basis]; st["rows"] = rows; st["npts"] = NPTS
    json.dump(st, open(STATE + ".tmp", "w")); os.replace(STATE + ".tmp", STATE)
    log(f"seeded rank {rank} of {A_LMR}")

    rng = random.Random(args.seed + st.get("samples", 0))
    with Pool(args.workers, initializer=_init, initargs=(msyms, tab)) as pool:
        for rd in range(args.maxrounds):
            if rank >= A_LMR: break
            batch = []
            for _ in range(args.batch):
                kk = rng.choice(kset)
                batch.append(random_filling(H, N_DEG, DELTA, N2, N1, rng, k=kk).to_json())
            t = time.time()
            res = pool.map(_eval_filling, batch, chunksize=8)
            st["samples"] = st.get("samples", 0) + len(batch)
            nz = 0; added = 0
            for pr in res:
                if pr is None: continue
                nz += 1
                if rank_mod(rows + [pr[1]], P1) > rank:
                    basis.append(Filling.from_json(pr[0])); rows.append(pr[1]); rank += 1; added += 1
                    if rank >= A_LMR: break
            st["basis"] = [F.to_json() for F in basis]; st["rows"] = rows
            st["generic_rank_P1"] = rank
            json.dump(st, open(STATE + ".tmp", "w")); os.replace(STATE + ".tmp", STATE)
            log(f"round {rd}: batch {len(batch)}, {nz} nonzero, +{added} -> rank {rank}/{A_LMR}  "
                f"({(time.time()-t)/max(len(batch),1):.2f}s/sample, {st['samples']} total)")
    st["generic_rank_P1"] = rank
    json.dump(st, open(STATE + ".tmp", "w")); os.replace(STATE + ".tmp", STATE)
    log(f"done: generic rank {rank} of {A_LMR}")


if __name__ == "__main__":
    main()
