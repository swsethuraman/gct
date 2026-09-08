#!/usr/bin/env python3
"""s76 -- exact C_24 by the C_delta engine, with a finer checkpoint and workers.

C_24 = sum over the 160 two-strip paths lambda_24 -> mu -> nu of a_22(nu),
      = sum_{mu one-strip predecessor} B_23(mu),
over 42 distinct shapes nu at delta = 22.  The instrument is unchanged from
analysis/wk11_int_cdelta.py (pruned Weyl alternation, terms collapsed by sorted
key, N_S_tail_n per distinct key); this driver only

  * splits the 42 shapes over workers (shape index i goes to worker i % k),
  * checkpoints the running alternation every CHECK_EVERY keys or CHECK_SECS
    seconds, not only at the end of a shape, so an interrupted run loses at
    most that much,
  * banks each finished shape as its own JSON in results/s76_c24/.

Usage:  python3 analysis/wk12_s76_c24.py --worker 0 --nworkers 2 [--budget SECS]
        python3 analysis/wk12_s76_c24.py --assemble      # after all 42 are banked
"""
import argparse
import json
import os
import pickle
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
from wk9_s42_census import N_S_tail_n            # noqa: E402
from wk11_int_cdelta import two_strip_paths, weyl_terms   # noqa: E402
from wk11_int_bdelta import lam_of, horiz_strips          # noqa: E402

DELTA = 24
OUTDIR = os.path.join(ROOT, "results", "s76_c24")
CHECK_EVERY = 50
CHECK_SECS = 30.0


def shapes_and_mult(delta=DELTA):
    paths = two_strip_paths(delta)
    mult = Counter(nu for _, nu in paths)
    return sorted(mult), mult, paths


def run_worker(w, k, budget, state_dir):
    shapes, mult, paths = shapes_and_mult()
    mine = [(i, nu) for i, nu in enumerate(shapes) if i % k == w]
    os.makedirs(OUTDIR, exist_ok=True)
    os.makedirs(state_dir, exist_ok=True)
    t_start = time.time()
    for i, nu in mine:
        out = os.path.join(OUTDIR, f"shape_{i:02d}.json")
        if os.path.exists(out):
            continue
        sp = os.path.join(state_dir, f"c24_shape_{i:02d}.pkl")
        if os.path.exists(sp):
            s = pickle.load(open(sp, "rb"))
        else:
            t = time.time()
            T = weyl_terms(nu)
            s = {"nu": nu, "keys": sorted(T), "sgn": T, "done": 0, "tot": 0,
                 "secs": 0.0}
            print(f"[w{w}] shape {i} {nu}: {len(T)} Weyl terms "
                  f"[enumerated in {time.time() - t:.1f}s]", flush=True)
        t0 = time.time()
        last_ck = time.time()
        n_since = 0
        while s["done"] < len(s["keys"]):
            if budget is not None and time.time() - t_start > budget:
                s["secs"] += time.time() - t0
                pickle.dump(s, open(sp, "wb"))
                print(f"[w{w}] budget reached at shape {i}: "
                      f"{s['done']}/{len(s['keys'])} keys", flush=True)
                return
            mu = s["keys"][s["done"]]
            s["tot"] += s["sgn"][mu] * N_S_tail_n(mu, DELTA - 2, 4)
            s["done"] += 1
            n_since += 1
            if n_since >= CHECK_EVERY or time.time() - last_ck > CHECK_SECS:
                s["secs"] += time.time() - t0
                t0 = time.time()
                pickle.dump(s, open(sp, "wb"))
                last_ck = time.time()
                n_since = 0
        s["secs"] += time.time() - t0
        rec = {"index": i, "nu": list(nu), "delta": DELTA - 2, "a22": int(s["tot"]),
               "path_multiplicity": mult[nu], "weyl_terms": len(s["keys"]),
               "secs": round(s["secs"], 1),
               "instrument": "wk11_int_cdelta.weyl_terms + wk9_s42_census.N_S_tail_n"}
        json.dump(rec, open(out, "w"), indent=1)
        print(f"[w{w}] DONE shape {i} {nu}: a_22 = {s['tot']}  "
              f"(mult {mult[nu]}, {len(s['keys'])} terms, {s['secs']:.0f}s)", flush=True)
        try:
            os.remove(sp)
        except OSError:
            pass


def assemble():
    shapes, mult, paths = shapes_and_mult()
    a = {}
    secs = 0.0
    for i, nu in enumerate(shapes):
        out = os.path.join(OUTDIR, f"shape_{i:02d}.json")
        if not os.path.exists(out):
            print(f"missing shape {i} {nu}")
            return None
        r = json.load(open(out))
        assert tuple(r["nu"]) == nu
        a[nu] = r["a22"]
        secs += r["secs"]
    C = sum(a[nu] for _, nu in paths)
    lam = lam_of(DELTA)
    preds = horiz_strips(lam, 4)
    B23 = {mu: sum(a[nu] for nu in horiz_strips(mu, 4)) for mu in preds}
    assert sum(B23.values()) == C
    res = {
        "quantity": "C_delta -- dim (S^lambda)^{K'}, K' = H_{delta-2} x S_4 x S_4",
        "identity": "C_delta = sum_{mu one-strip pred of lambda_delta} B_{delta-1}(mu)"
                    " = sum over two-strip paths of a_{delta-2}(nu)",
        "delta": DELTA, "lambda": list(lam), "C": C,
        "two_strip_paths": len(paths), "distinct_shapes": len(shapes),
        "nonzero_shapes": sum(1 for v in a.values() if v),
        "max_channel": max(a.values()),
        "max_path_multiplicity": max(mult.values()),
        "a_22_by_shape": {str(nu): a[nu] for nu in shapes},
        "path_multiplicity_by_shape": {str(nu): mult[nu] for nu in shapes},
        "B_23_by_predecessor": {str(mu): B23[mu] for mu in preds},
        "context": {"B_24": 2168, "a_24": 274, "C_over_B": round(C / 2168, 4),
                    "C_over_a": round(C / 274, 2)},
        "total_engine_secs": round(secs, 1),
        "engine": "analysis/wk11_int_cdelta.py functions driven by analysis/wk12_s76_c24.py",
    }
    path = os.path.join(ROOT, "results", "s76_c24.json")
    json.dump(res, open(path, "w"), indent=1)
    print(f"C_{DELTA} = {C}  over {len(paths)} paths, {len(shapes)} shapes, "
          f"{res['nonzero_shapes']} nonzero, max channel {res['max_channel']}")
    for mu in preds:
        print(f"  B_23{mu} = {B23[mu]}")
    print(f"  written {path}")
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--worker", type=int, default=0)
    ap.add_argument("--nworkers", type=int, default=1)
    ap.add_argument("--budget", type=float, default=None)
    ap.add_argument("--state-dir", default=os.path.join(ROOT, "results", "s76_c24", "state"))
    ap.add_argument("--assemble", action="store_true")
    args = ap.parse_args()
    if args.assemble:
        assemble()
    else:
        run_worker(args.worker, args.nworkers, args.budget, args.state_dir)
