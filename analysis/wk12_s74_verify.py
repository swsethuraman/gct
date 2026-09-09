#!/usr/bin/env python3
"""Session 74 -- independent re-derivation of the LMR decision from the banked
source, at FRESH points, through the literal fillings.

What is independent of the measurement path (wk12_s74_columns / decide):
  * fresh points: seed SEED[family] + 100000, entries in [-1000, 1000], K = a + 20;
  * the literal transported fillings T_i^up are evaluated directly (no native
    value, no transport scalar), so the declared row system is exercised from
    the other side;
  * ranks by python-flint on the fresh matrix; both primes on request.
What is shared: the DP circuit evaluator (the only evaluator that reaches this
cell) -- the compact-state one by default, the s69 original with
S74_VERIFY_S69_DP=1 (the two agree entry for entry, wk12_s74_dp.validate).
--spot cross-checks the s69 DP against the mixed-discriminant evaluator
fast_eval_c (Identity 3, a different algorithm) on sampled (filling, point)
pairs.  --count-ns recounts N_S(lambda_delta) by an exact multiset DP.

    python3 analysis/wk12_s74_verify.py --families det,pad --prime 2147483647 [--K 294]
    python3 analysis/wk12_s74_verify.py --spot 6
    python3 analysis/wk12_s74_verify.py --count-ns 23,24
"""
import argparse
import json
import os
import random
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk8_s30_core import P1, P2, exps, restrict, det_form, per_form, per_padded   # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs, dp_eval_c,   # noqa: E402
                              fast_eval_c, rank_mod)
import wk12_s74_columns as COL                                                  # noqa: E402
from wk12_s74_dp import dp_eval_compact                                        # noqa: E402

USE_S69_DP = os.environ.get("S74_VERIFY_S69_DP") == "1"     # the original evaluator (slow, no parallel gain)


def dp_eval(F, ms, p, tab):
    return (dp_eval_c if USE_S69_DP else dp_eval_compact)(F, ms, p, tab)

OUT = os.path.join(ROOT, "results", "s74")
N, H = 4, 9
_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))
_A, _idx, _fact, TAB = sym_table(N, H)
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


# ------------------------------------------------------------------ fresh points (box 1000)
def fresh_points(family, K, seed_shift=100000, bound=1000):
    old_seed, old_bound = COL.SEED[family], COL.BOUND
    COL.SEED[family] = old_seed + seed_shift
    COL.BOUND = bound
    try:
        pts, skipped = COL.make_points(family, K)
    finally:
        COL.SEED[family] = old_seed
        COL.BOUND = old_bound
    return pts, skipped


_MS = None
_P = None


def _init(msyms, p):
    global _MS, _P
    _MS, _P = msyms, p


def _row_literal(Fj):
    F = Filling.from_json(Fj)
    return [dp_eval(F, ms, _P, TAB) % _P for ms in _MS]


def rederive(families, p, K, workers, block=4):
    src = json.load(open(os.path.join(OUT, "source.json"), encoding="utf-8"))
    out = dict(prime=p, K=K, seed_shift=100000, bound=1000, families={})
    path = os.path.join(OUT, f"verify_{p}.json")
    if os.path.exists(path):
        out = json.load(open(path, encoding="utf-8"))
    for fam in families:
        if fam in out["families"] and out["families"][fam].get("rows") == src["size"]:
            log(f"{fam} p={p}: already re-derived, rank {out['families'][fam]['rank']}")
            continue
        pts, skipped = fresh_points(fam, K)
        msyms = [symbols_from_coeffs(q["cv"], N, H, p) for q in pts]
        rows = out["families"].get(fam, {}).get("rows_literal", {}) if fam in out["families"] else {}
        todo = [e for e in src["entries"] if str(e["index"]) not in rows]
        log(f"{fam} p={p}: fresh K={K} (skipped {skipped}); {len(todo)} literal rows to evaluate")
        t0 = time.time()
        with Pool(workers, initializer=_init, initargs=(msyms, p)) as pool:
            for s in range(0, len(todo), block):
                chunk = todo[s:s + block]
                res = pool.map(_row_literal, [e["literal"] for e in chunk], chunksize=1)
                for e, r in zip(chunk, res):
                    rows[str(e["index"])] = r
                out["families"][fam] = dict(rows=len(rows), rows_literal=rows, points=[q["record"] for q in pts],
                                            point_index=[q["j"] for q in pts], skipped=skipped,
                                            secs=round(time.time() - t0, 1))
                tmp = path + ".tmp"
                json.dump(out, open(tmp, "w", encoding="utf-8"))
                os.replace(tmp, path)
                log(f"{fam} p={p}: {len(rows)}/{src['size']} rows, {time.time()-t0:.0f}s")
        mat = [rows[str(e["index"])] for e in src["entries"]]
        rk = rank_mod(mat, p)
        rows23 = [rows[str(e["index"])] for e in src["entries"] if e["rung"] <= 23]
        rk23 = rank_mod(rows23, p)
        out["families"][fam].update(rank=rk, nullity=len(mat) - rk, rank_rows_le23=rk23,
                                    nullity_rows_le23=len(rows23) - rk23)
        json.dump(out, open(path, "w", encoding="utf-8"))
        log(f"{fam} p={p}: FRESH-POINT rank {rk}/{len(mat)} (nullity {len(mat)-rk}); "
            f"rows with rung<=23: rank {rk23}/{len(rows23)}")
    # compare with the decision file if present
    dpath = os.path.join(OUT, f"decision_{p}.json")
    if os.path.exists(dpath):
        dec = json.load(open(dpath, encoding="utf-8"))
        for fam in families:
            c = dec["columns"].get(fam, {})
            if "rank_24" in c and fam in out["families"]:
                agree = c["rank_24"] == out["families"][fam]["rank"]
                out["families"][fam]["agrees_with_decision"] = agree
                log(f"{fam} p={p}: decision rank {c['rank_24']} vs fresh {out['families'][fam]['rank']}: "
                    f"{'AGREE' if agree else 'DISAGREE'}")
        json.dump(out, open(path, "w", encoding="utf-8"))
    return out


# ------------------------------------------------------------------ evaluator cross-check
def spot(n, workers):
    src = json.load(open(os.path.join(OUT, "source.json"), encoding="utf-8"))
    rng = random.Random(7474)
    sample = rng.sample(src["entries"], min(n, len(src["entries"])))
    pts, _ = fresh_points("det", 2)
    out = []
    for e in sample:
        F = Filling.from_json(e["literal"])
        for p in (P1, P2):
            q = pts[rng.randrange(len(pts))]
            ms = symbols_from_coeffs(q["cv"], N, H, p)
            t0 = time.time()
            a = dp_eval_c(F, ms, p, TAB) % p
            t1 = time.time()
            b = fast_eval_c(F, ms, p, TAB) % p
            t2 = time.time()
            out.append(dict(index=e["index"], rung=e["rung"], prime=p, point=q["j"], dp=a, identity3=b,
                            agree=(a == b), dp_secs=round(t1 - t0, 3), id3_secs=round(t2 - t1, 1)))
            log(f"spot index {e['index']} rung {e['rung']} p={p}: DP {a} vs Identity-3 {b} "
                f"{'AGREE' if a == b else 'DISAGREE'} ({t1-t0:.2f}s vs {t2-t1:.1f}s)")
    json.dump(out, open(os.path.join(OUT, "spot_evaluators.json"), "w", encoding="utf-8"), indent=1)
    return out


# ------------------------------------------------------------------ N_S by an exact multiset DP
def count_ns(delta):
    """number of multisets of delta exponent vectors (degree 4, 9 variables) with sum
    lambda_delta = (4 delta - 31, 17, 2^7): the weight-space dimension N_S."""
    lam = [4 * delta - 31, 17] + [2] * 7
    shape = tuple(x + 1 for x in lam)
    dp = np.zeros((delta + 1,) + shape, dtype=np.int64)
    dp[(0,) + (0,) * 9] = 1
    for al in _E:
        if any(al[i] > lam[i] for i in range(9)):
            continue
        src_sl = tuple(slice(0, lam[i] - al[i] + 1) for i in range(9))
        dst_sl = tuple(slice(al[i], lam[i] + 1) for i in range(9))
        for k in range(delta):                    # unbounded multiplicity: ascending k, in place
            dp[(k + 1,) + dst_sl] += dp[(k,) + src_sl]
    return int(dp[(delta,) + tuple(lam)])


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--families", default="")
    ap.add_argument("--prime", type=int, default=P1)
    ap.add_argument("--K", type=int, default=294)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--spot", type=int, default=0)
    ap.add_argument("--count-ns", default="")
    args = ap.parse_args(argv)
    if args.count_ns:
        res = {}
        for d in [int(x) for x in args.count_ns.split(",")]:
            t0 = time.time()
            res[d] = count_ns(d)
            log(f"N_S(lambda_{d}) = {res[d]}  ({time.time()-t0:.0f}s)")
        json.dump(res, open(os.path.join(OUT, "ns_count.json"), "w", encoding="utf-8"), indent=1)
    if args.spot:
        spot(args.spot, args.workers)
    if args.families:
        rederive(args.families.split(","), args.prime, args.K, args.workers)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
