#!/usr/bin/env python3
"""s77 -- the measured comparison on n=4 ladder rungs: the DETERMINISTIC construction's
fillings-scanned-per-accepted-birth-class vs the RANDOM stream's draws-per-accepted-class.

Both arms are run here with IDENTICAL u=0 points, the same syntactic pure-u filter, the same
short-circuit birth test (S1's birth quotient: nonzero at generic points with u-coordinate 0),
the same greedy rank build, and the same wall-clock budget -- so the only difference is the
CANDIDATE SOURCE:

  deterministic : interleaved_ssyt (Pieri chains, round-robin over overlap k), order A.
  random        : random_filling with k in {5..9} (the s69 / birth-probe sampler).

Tests against b_delta, not a_delta (docs/batch12_s1_s2_consolidated.md S1).  Reports, per rung,
the rank each arm reaches, candidates consumed, births found, and candidates-per-accepted-class.

    python3 analysis/wk12_s77_ladder.py --rungs 14,13 --cap 90 --points 24
"""
import argparse, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1                                               # noqa: E402
from wk11_s69_circuit import sym_table, random_filling, dp_eval_c, fast_eval_c, rank_mod  # noqa: E402
from wk12_s77_bridge import interleaved_ssyt                              # noqa: E402
from wk12_int_birth_probe import u0_point, pure_u_letters, BIRTH, N, H, N2  # noqa: E402

_A, _idx, _fact, TAB = sym_table(N, H)
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def ev(F, ms, p):
    try:
        return dp_eval_c(F, ms, p, TAB) % p
    except Exception:                                                     # noqa: BLE001
        return fast_eval_c(F, ms, p, TAB) % p


def greedy_rank(candidates, pts, b, cap_secs):
    """consume Filling candidates; pure-u filter; short-circuit birth test on pts[0]; keep on rank.
    Returns stats."""
    rows, seen, filtered, births, first = [], 0, 0, 0, None
    t0 = time.time()
    for F in candidates:
        if time.time() - t0 > cap_secs or len(rows) >= b:
            break
        seen += 1
        if pure_u_letters(F):
            continue
        filtered += 1
        v0 = ev(F, pts[0], P1)
        if not v0:
            continue
        births += 1
        if first is None:
            first = seen
        row = [v0] + [ev(F, ms, P1) for ms in pts[1:]]
        if rank_mod(rows + [row], P1) > len(rows):
            rows.append(row)
    return dict(rank=len(rows), consumed=seen, past_filter=filtered, births=births,
                first_birth=first, secs=round(time.time() - t0, 1),
                per_class=(round(seen / len(rows), 1) if rows else None),
                births_per_class=(round(births / len(rows), 1) if rows else None))


def det_candidates(delta, n1):
    return interleaved_ssyt(H, N, delta, N2, n1, order="A", limit=10 ** 9)


def rnd_candidates(delta, n1, seed):
    rng = random.Random(seed)
    while True:
        try:
            yield random_filling(H, N, delta, N2, n1, rng, k=rng.choice([5, 6, 7, 8, 9]))
        except Exception:                                                 # noqa: BLE001
            continue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rungs", default="14,13")
    ap.add_argument("--cap", type=float, default=90.0)
    ap.add_argument("--points", type=int, default=24)
    args = ap.parse_args()
    rungs = [int(x) for x in args.rungs.split(",")]
    out = {"note": "identical points/filter/budget; deterministic=interleaved SSYT, random=s69 sampler",
           "points_cap": args.points, "cap_secs": args.cap, "rungs": []}
    for d in rungs:
        b = BIRTH[d]; n1 = N * d - 2 * H - 2 * N2
        NP = min(b + 8, args.points)
        pts = [u0_point(P1, 61000 + 11 * j) for j in range(NP)]
        log(f"rung delta={d}: b={b}, {NP} u=0 points, cap {args.cap}s/arm")
        det = greedy_rank(det_candidates(d, n1), pts, b, args.cap)
        log(f"  deterministic (SSYT): rank {det['rank']}/{b}, consumed {det['consumed']}, "
            f"births {det['births']}, per-class {det['per_class']}, {det['secs']}s")
        rnd = greedy_rank(rnd_candidates(d, n1, 900 + d), pts, b, args.cap)
        log(f"  random (sampler):     rank {rnd['rank']}/{b}, consumed {rnd['consumed']}, "
            f"births {rnd['births']}, per-class {rnd['per_class']}, {rnd['secs']}s")
        out["rungs"].append(dict(delta=d, b=b, points=NP, deterministic=det, random=rnd))
        json.dump(out, open(os.path.join(ROOT, "results", "s77_ladder_compare.json"), "w"), indent=1)
    log("done")


if __name__ == "__main__":
    main()
