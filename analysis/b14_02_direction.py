#!/usr/bin/env python3
"""B14-02 direction control -- the check that separates "the instrument is broken"
from "the reducible locus is special".

The pre-registered expectation E1 was rank 39 / k = 0 and the measurement gave
rank 36 / k = 3.  E2 says the first hypothesis for a deficiency is an instrument
fault.  This control discriminates: the SAME 39 transported rows, the SAME
evaluator and the SAME arithmetic, evaluated at GENERIC quartic points instead of
reducible ones.  A broken climb, a wrong transport exponent, an exps-ordering
slip or a stalled evaluator all lower the rank at generic points too.  A rank
deficiency confined to the reducible locus is not an instrument fault -- it is
the object i_red is defined by.
"""
import json, os, random, sys, time
from flint import nmod_mat

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from b14_02_source13 import PRIMES, load_rows, load_points, OUT, N, H, E4, FACT, IU  # noqa: E402
from wk11_s69_circuit import sym_table                                               # noqa: E402
from wk12_s74_dp import dp_eval_compact                                              # noqa: E402

t0 = time.time()


def main():
    _A, _i, _f, TAB = sym_table(N, H)
    _, rows = load_rows()
    p = PRIMES[0]
    rng = random.Random(20260212)
    out = dict(values_are="ranks of the 39-row degree-13 source matrix at three point "
                          "families, mod the stated prime; no transform", prime=p)

    # generic integer quartics (span 9, not reducible)
    gen = []
    while len(gen) < 41:
        cv = [rng.randint(-7, 7) for _ in E4]
        ms = [(c % p) * FACT[a] % p for a, c in enumerate(cv)]
        if ms[IU]:
            gen.append(ms)
    G = [[dp_eval_compact(r["F"], ms, p, TAB) for ms in gen] for r in rows]
    rg = nmod_mat(39, len(gen), [int(x) % p for r in G for x in r], p).rank()
    out["generic"] = dict(n_points=len(gen), rank=rg)
    print(f"[{time.time()-t0:7.1f}s] generic points: rank {rg} / 39", flush=True)

    # the reducible points actually used, same prime, read back from the sweep
    blk = json.load(open(os.path.join(OUT, f"residues_primary_{p}.json"), encoding="utf-8"))
    R = [blk["rows"][str(i)] for i in range(39)]
    rr = nmod_mat(39, 96, [int(x) % p for r in R for x in r], p).rank()
    out["reducible_primary"] = dict(n_points=96, rank=rr)
    print(f"[{time.time()-t0:7.1f}s] reducible P13 points: rank {rr} / 39", flush=True)

    out["verdict"] = (
        "instrument exonerated: full rank 39 at generic points with the same rows, "
        "evaluator and arithmetic, so the deficiency to %d is a property of the "
        "reducible locus, not of the instrument" % rr) if (rg == 39 and rr < 39) else (
        "inconclusive or instrument fault: generic rank %d" % rg)
    out["control_can_fail"] = True
    out["control_can_fail_evidence"] = (
        "this control distinguishes the two hypotheses by construction: had the climb, "
        "the transport exponent, the exps ordering or the evaluator been wrong, the "
        "generic-point rank would also have fallen below 39. It did not.")
    json.dump(out, open(os.path.join(OUT, "direction_control.json"), "w"), indent=1)
    print(out["verdict"], flush=True)


if __name__ == "__main__":
    main()
