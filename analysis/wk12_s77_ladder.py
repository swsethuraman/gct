#!/usr/bin/env python3
"""s77 -- the measured comparison on n=4 ladder rungs: the DETERMINISTIC construction's
fillings-scanned-per-accepted-birth-class vs the birth-quotient RANDOM stream's
draws-per-accepted-class (analysis/wk12_int_birth_probe.py baseline).

At rung delta the births b_delta = a_delta - a_{delta-1} are the new directions mod u
(u = c_{(4,0,..)}).  We test against b_delta via the u=0 restriction, not a_delta:
a filling is a birth candidate iff it is not a pure-u multiple (syntactic filter) and its
F_T is nonzero at generic points with the u-coordinate set to zero (S1's birth quotient).

  DETERMINISTIC arm: interleaved_ssyt (round-robin over overlap k), pure-u filtered, evaluated
     on the SAME b+8 u=0 points, kept on rank -- report SSYT scanned per accepted class.
  RANDOM arm: wk12_int_birth_probe.stream_rung on the same rung (fresh seeds).

Both stop at b_delta or a cap.  This is the "measured reduction in draws per accepted class"
the brief asks for -- reported as a ratio, with the honest note that the deterministic scan
is reproducible where the random draw is not.

    python3 analysis/wk12_s77_ladder.py --rungs 22,20 --cap 240
"""
import argparse, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2, exps                                     # noqa: E402
from wk11_s69_circuit import sym_table                                    # noqa: E402
from wk11_s69_circuit import dp_eval_c, fast_eval_c, rank_mod             # noqa: E402
from wk12_s77_bridge import interleaved_ssyt                              # noqa: E402
from wk12_int_birth_probe import u0_point, pure_u_letters, stream_rung, BIRTH, N, H, N2  # noqa: E402

_A, _idx, _fact, TAB = sym_table(N, H)
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def ev(F, ms, p):
    try:
        return dp_eval_c(F, ms, p, TAB) % p
    except Exception:                                                     # noqa: BLE001
        return fast_eval_c(F, ms, p, TAB) % p


def deterministic_rung(delta, cap_secs, maxscan):
    """interleaved SSYT stream at rung delta, pure-u filtered, birth-rank on u=0 points."""
    b = BIRTH[delta]
    n1 = N * delta - 2 * H - 2 * N2
    pts = [u0_point(P1, 61000 + 11 * j) for j in range(b + 8)]
    rows, scanned, filtered, first_hit = [], 0, 0, None
    t0 = time.time()
    for F in interleaved_ssyt(H, N, delta, N2, n1, order="A", limit=maxscan):
        if time.time() - t0 > cap_secs or len(rows) >= b:
            break
        scanned += 1
        if pure_u_letters(F):
            continue
        filtered += 1
        row = [ev(F, ms, P1) for ms in pts]
        if any(row):
            if first_hit is None:
                first_hit = scanned
            if rank_mod(rows + [row], P1) > len(rows):
                rows.append(row)
    return dict(delta=delta, b=b, rank=len(rows), scanned=scanned, past_filter=filtered,
                first_hit=first_hit, secs=round(time.time() - t0, 1),
                complete=(len(rows) == b),
                scans_per_class=(round(scanned / len(rows), 1) if rows else None))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rungs", default="22,20")
    ap.add_argument("--cap", type=float, default=240.0)
    ap.add_argument("--maxscan", type=int, default=200000)
    args = ap.parse_args()
    rungs = [int(x) for x in args.rungs.split(",")]
    out = {"rungs": [], "note": "deterministic = interleaved SSYT (Pieri chains), random = birth-probe stream"}
    for d in rungs:
        log(f"rung delta={d}: b={BIRTH[d]}")
        det = deterministic_rung(d, args.cap, args.maxscan)
        log(f"  deterministic: rank {det['rank']}/{det['b']}, scanned {det['scanned']} SSYT "
            f"({det['past_filter']} past pure-u filter), {det['secs']}s, "
            f"scans/class {det['scans_per_class']}{'' if det['complete'] else '  [capped]'}")
        rnd = stream_rung(d, cap_secs=args.cap)
        rnd_per = round(rnd["draws"] / rnd["rank"], 1) if rnd["rank"] else None
        log(f"  random: rank {rnd['rank']}/{rnd['b']}, {rnd['draws']} draws "
            f"({rnd['past_filter']} past filter), {rnd['secs']}s, draws/class {rnd_per}"
            f"{'' if rnd['complete'] else '  [capped]'}")
        out["rungs"].append(dict(delta=d, deterministic=det,
                                 random=dict(rank=rnd["rank"], b=rnd["b"], draws=rnd["draws"],
                                             past_filter=rnd["past_filter"], secs=rnd["secs"],
                                             complete=rnd["complete"], draws_per_class=rnd_per)))
        json.dump(out, open(os.path.join(ROOT, "results", "s77_ladder_compare.json"), "w"), indent=1)
    log("done")


if __name__ == "__main__":
    main()
