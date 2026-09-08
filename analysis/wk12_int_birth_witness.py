#!/usr/bin/env python3
"""Explicit point/value witnesses for the delta=24 birth representative F_{T57}.

WHY THIS EXISTS.  The consolidation quoted 24 nonzero evaluations per prime for
F_{T57}; the committed probe artefact recorded 6, because the hardening run that
produced 24 was ad hoc and never banked.  A reviewer found the discrepancy, which
is the right outcome and the wrong way round -- in this programme a claim that
cannot be reproduced from the tree is not established.  This script banks the
witnesses properly, and in a form that does not require running our evaluator:
the full integer coefficient vector of every point, and the value there.

THE CERTIFICATE CHAIN.
  * T57 is saved filling index 57 of results/s69_lmr_state.json, lambda =
    (65,17,2^7), delta = 24.  Its polynomial F_T is the bracket contraction of
    docs/compact_circuit.md; F_T has INTEGER coefficients.
  * Each point below is an integer coefficient vector c in Z^495, indexed by
    wk8_s30_core.exps(4,9), with the u coordinate -- alpha = (4,0,...,0), the
    LAST index in that ordering -- set to exactly 0.
  * The recorded value is F_T(c) mod p.  It is nonzero.  Therefore the integer
    F_T(c) is nonzero, therefore F_T|_{u=0} is not the zero polynomial, therefore
    F_T is not in u*M_23.  This is a certificate over Q, not sampling: one
    nonzero value settles it, and the second prime is redundancy, not evidence.
  * With the banked b_24 = a_24 - a_23 = 274 - 273 = 1, the class of F_T spans
    M_24 / u M_23, so M_24 = u M_23 (+) <F_T>.

WHAT IT DOES NOT SAY.  Nothing about ideal membership.  F_T is not thereby in
I(Det) or outside I(Pad); an ideal element of its class differs from it by a
transported u w.  See docs/batch12_integrator_note3.md section 4.

The controls are the other half of the certificate: fillings carrying a pure-u
letter satisfy F_T = n! u F_deleted identically, so they MUST vanish at every
point with u = 0.  If any did not, the u index or the evaluator would be wrong.

usage: python3 analysis/wk12_int_birth_witness.py [--points 24] [--controls 8]
"""
import gzip
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk8_s30_core import P1, P2, exps                                    # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs,   # noqa: E402
                              generic_point, dp_eval_c, fast_eval_c)

N, H, INDEX = 4, 9, 57


def main(argv):
    npts = int(argv[argv.index("--points") + 1]) if "--points" in argv else 24
    nctl = int(argv[argv.index("--controls") + 1]) if "--controls" in argv else 8
    E = exps(N, H)
    iu = E.index(tuple([N] + [0] * (H - 1)))
    _A, _i, _f, tab = sym_table(N, H)
    st = json.load(open(os.path.join(ROOT, "results/s69_lmr_state.json"), encoding="utf-8"))
    fills = [Filling.from_json(b) for b in st["basis"]]
    F = fills[INDEX]

    def pure_u(G):
        c = [0] * G.delta
        for l in G.C1:
            c[l] += 1
        for l in G.C2:
            c[l] += 1
        for a, b in G.two:
            c[a] += 1
            c[b] += 1
        return [l for l in range(G.delta) if c[l] == 0]

    def ev(G, ms, p):
        try:
            return dp_eval_c(G, ms, p, tab) % p
        except Exception:                                    # noqa: BLE001
            return fast_eval_c(G, ms, p, tab) % p

    out = {
        "claim": "F_{T57}|_{u=0} != 0 over Q, hence F_{T57} not in u*M_23; with "
                 "b_24 = 1 this gives M_24 = u*M_23 (+) <F_{T57}>",
        "cell": {"n": N, "r": H, "delta": 24, "lambda": st["lam"], "a": st["a"]},
        "filling_index": INDEX, "filling": F.to_json(), "shared_k": len(F.shared),
        "u": {"alpha": [N] + [0] * (H - 1), "index_in_wk8_s30_core_exps": iu,
              "note": "LAST index in this ordering; chi_build.exps puts it first"},
        "exps_ordering": "wk8_s30_core.exps(4,9), 495 entries",
        "points": {}, "controls": {},
        "how_to_check": "for each point: take the integer vector c (u coordinate is 0), "
                        "evaluate the bracket contraction F_{T57} over Z, reduce mod p, "
                        "and compare with value. One nonzero suffices.",
    }
    for p, tag in ((P1, "P1"), (P2, "P2")):
        recs = []
        for j in range(npts):
            seed = 91000 + 17 * j
            cv = generic_point(N, H, p, random.Random(seed))
            cv[iu] = 0
            v = ev(F, symbols_from_coeffs(cv, N, H, p), p)
            recs.append({"seed": seed, "coeffs": [int(x) for x in cv], "value": int(v)})
        out["points"][tag] = {"prime": p, "n": npts,
                              "nonzero": sum(1 for r in recs if r["value"]), "witnesses": recs}
        print(f"  {tag} (p = {p}): {out['points'][tag]['nonzero']}/{npts} nonzero", flush=True)

    ctl = [i for i in range(len(fills)) if pure_u(fills[i])][:nctl]
    cv0 = out["points"]["P1"]["witnesses"][0]["coeffs"]
    ms0 = symbols_from_coeffs(cv0, N, H, P1)
    out["controls"] = {"claim": "a filling with a pure-u letter is n! u F_deleted, so it "
                                "vanishes identically at u = 0",
                       "point_seed": out["points"]["P1"]["witnesses"][0]["seed"],
                       "results": {str(i): {"pure_u_letters": pure_u(fills[i]),
                                            "value": int(ev(fills[i], ms0, P1))} for i in ctl}}
    bad = [i for i, r in out["controls"]["results"].items() if r["value"]]
    out["controls"]["all_vanish"] = not bad
    print(f"  controls: {len(ctl)} pure-u fillings, {len(bad)} nonzero (must be 0)")

    path = os.path.join(ROOT, "results/wk12_int_birth24_witness.json.gz")
    with gzip.open(path, "wt", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"  -> {os.path.relpath(path, ROOT)} ({os.path.getsize(path)/1024:.0f} KB)")
    return 0 if (out["points"]["P1"]["nonzero"] and out["points"]["P2"]["nonzero"]
                 and out["controls"]["all_vanish"]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
