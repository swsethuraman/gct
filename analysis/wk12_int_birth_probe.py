#!/usr/bin/env python3
"""Batch-12 pre-batch -- run S1's birth-quotient test on real candidates.

S1 proves M_d / u M_{d-1} = rho_d(M_d) with rho_d the restriction to u = 0.  The
reasoning side then proposed a sharply targeted experiment: of session 69's 113
saved delta=24 fillings, only five have no visible pure-u letter; the other 108
are n! u (something) and vanish identically in the birth test.  Test those five.

This script does that, and then goes on to run the same test on FRESH candidate
streams at the upper rungs, which is what actually measures whether the theorem
helps.

    census      the 113 saved fillings for pure-u letters
    probe       the survivors at points with u = 0, both house primes
    control     fillings WITH a pure-u letter must vanish -- they do, 20/20
    stream      fresh random fillings per rung: filter, evaluate, keep a
                candidate only when it raises the birth rank; stop at b_d

WHAT A NONZERO VALUE PROVES.  F_T has integer coefficients and the point is an
integer point, so a nonzero residue at either prime proves F_T|_{u=0} is not the
zero polynomial, hence F_T is not in u M_{d-1}.  That is a CERTIFICATE, not
sampling.  A zero value is only evidence in the other direction -- except for a
filling with a pure-u letter, where F_T = n! u F_deleted makes the vanishing an
identity.

WHAT IT DOES NOT PROVE (correction accepted from the reasoning side, 8 Sep).  A
filling with nonzero class SPANS the birth quotient when b_d = 1; it is not
thereby an element of any ideal.  An ideal element of that class differs from it
by a transported vector u w, w in M_{d-1}, and finding w needs the lower source.
"the birth direction is the determinant ideal vector" is true of the CLASS and
false of the representative.

usage: python3 analysis/wk12_int_birth_probe.py [--stream 24,23,22,21,20,17,14] [--cap 150]
"""
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk8_s30_core import P1, P2, exps                                    # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table,        # noqa: E402
                              symbols_from_coeffs, generic_point,
                              dp_eval_c, fast_eval_c, rank_mod)

N, H = 4, 9
BIRTH = {12: 2, 13: 37, 14: 54, 15: 52, 16: 43, 17: 31, 18: 22,
         19: 14, 20: 9, 21: 5, 22: 3, 23: 1, 24: 1}
N2 = 15                                     # lambda' = (9, 9, 2^15, 1^{4d-48})
_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))   # u = c_(4,0,...,0); LAST in this ordering
_A, _idx, _fact, TAB = sym_table(N, H)


def u0_point(p, seed):
    """a generic coefficient point with the u coordinate set to zero."""
    cv = generic_point(N, H, p, random.Random(seed))
    cv[IU] = 0
    return symbols_from_coeffs(cv, N, H, p)


def ev(F, msym, p):
    try:
        return dp_eval_c(F, msym, p, TAB) % p
    except Exception:                                        # noqa: BLE001
        return fast_eval_c(F, msym, p, TAB) % p


def pure_u_letters(F):
    """letters whose n legs are all in one-columns: symbol n!u, so F = n! u F'."""
    c = [0] * F.delta
    for l in F.C1:
        c[l] += 1
    for l in F.C2:
        c[l] += 1
    for a, b in F.two:
        c[a] += 1
        c[b] += 1
    return [l for l in range(F.delta) if c[l] == 0]


def probe_saved(state="results/s69_lmr_state.json", npts=24):
    st = json.load(open(os.path.join(ROOT, state), encoding="utf-8"))
    fills = [Filling.from_json(b) for b in st["basis"]]
    clean = [i for i, F in enumerate(fills) if not pure_u_letters(F)]
    out = {"saved": len(fills), "with_pure_u": len(fills) - len(clean), "clean": clean, "probe": {}}
    for i in clean:
        rec = {}
        for p, tag in ((P1, "P1"), (P2, "P2")):
            vals = [ev(fills[i], u0_point(p, 12000 + 97 * j), p) for j in range(npts)]
            rec[tag] = {"nonzero": sum(1 for v in vals if v), "of": npts,
                        "point_seeds": [12000 + 97 * j for j in range(npts)],
                        "values": [int(v) for v in vals]}
        out["probe"][str(i)] = rec
    out["hits"] = [i for i in clean
                   if out["probe"][str(i)]["P1"]["nonzero"] and out["probe"][str(i)]["P2"]["nonzero"]]
    # control: pure-u fillings must vanish identically
    pts = [u0_point(P1, 55000 + 13 * j) for j in range(4)]
    pu = [i for i in range(len(fills)) if i not in clean][:20]
    out["control_tested"] = len(pu)
    out["control_nonzero"] = [i for i in pu if any(ev(fills[i], ms, P1) for ms in pts)]
    out["hit_fillings"] = {str(i): fills[i].to_json() for i in out["hits"]}
    return out


def stream_rung(delta, cap_secs=150, seed=None, max_draws=4000, kset=(5, 6, 7, 8, 9)):
    """fresh candidates at one rung: filter, evaluate on u=0 points, keep on rank."""
    b = BIRTH[delta]
    n1 = N * delta - 2 * H - 2 * N2
    pts = [u0_point(P1, 61000 + 11 * j) for j in range(b + 8)]
    rng = random.Random(seed if seed is not None else 500 + delta)
    rows, keep, tried, filtered = [], [], 0, 0
    t0 = time.time()
    while time.time() - t0 < cap_secs and len(rows) < b and tried < max_draws:
        try:
            F = random_filling(H, N, delta, N2, n1, rng, k=rng.choice(list(kset)))
        except Exception:                                    # noqa: BLE001
            continue
        tried += 1
        if pure_u_letters(F):
            continue
        filtered += 1
        row = [ev(F, ms, P1) for ms in pts]
        if any(row) and rank_mod(rows + [row], P1) > len(rows):
            rows.append(row)
            keep.append(F)
    # ALWAYS retain the accepted fillings.  An earlier version kept them only for
    # b <= 5 to hold the JSON down, which discarded precisely the evidence that
    # makes a run checkable -- the delta=20 run lost all nine.  A filling is a few
    # hundred integers; there was never a reason.
    return {"delta": delta, "b": b, "rank": len(rows), "draws": tried, "past_filter": filtered,
            "secs": round(time.time() - t0, 1), "complete": len(rows) == b,
            "points": b + 8, "seed": seed if seed is not None else 500 + delta,
            "point_seeds": [61000 + 11 * j for j in range(b + 8)],
            "rows": [[int(x) for x in r] for r in rows],
            "fillings": [F.to_json() for F in keep]}


def main(argv):
    rungs = [int(x) for x in (argv[argv.index("--stream") + 1] if "--stream" in argv
                              else "23,22,21,20").split(",")]
    cap = float(argv[argv.index("--cap") + 1]) if "--cap" in argv else 150.0
    res = {"saved_probe": probe_saved(), "streams": []}
    sp = res["saved_probe"]
    print(f"saved delta=24 fillings: {sp['saved']};  with a pure-u letter {sp['with_pure_u']}, "
          f"without {len(sp['clean'])} -> {sp['clean']}")
    print(f"  nonzero mod u at both primes: {sp['hits']}")
    print(f"  control: {sp['control_tested']} pure-u fillings, "
          f"{len(sp['control_nonzero'])} nonzero (must be 0)")
    for d in rungs:
        r = stream_rung(d, cap_secs=cap)
        res["streams"].append(r)
        print(f"  delta={d:2d} b={r['b']:2d}: birth rank {r['rank']:2d}/{r['b']} from {r['draws']} draws "
              f"({r['past_filter']} past filter) in {r['secs']}s"
              f"{'' if r['complete'] else '   [time-capped, not stalled]'}", flush=True)
    # MERGE by rung, never overwrite.  The output path does not depend on
    # --stream, so a rerun at other rungs used to destroy the earlier record --
    # the same trap that cost the banked delta = 24 row in wk11_int_bdelta.json.
    path = os.path.join(ROOT, "results/wk12_int_birth_probe.json")
    if os.path.exists(path):
        try:
            prior = json.load(open(path, encoding="utf-8"))
        except Exception:                                        # noqa: BLE001
            prior = {}
        by = {r["delta"]: r for r in prior.get("streams", []) if "delta" in r}
        for r in res["streams"]:
            by[r["delta"]] = r
        res["streams"] = [by[d] for d in sorted(by, reverse=True)]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
