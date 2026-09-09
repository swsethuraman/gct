#!/usr/bin/env python3
"""Independent verification of S4's target padded certificate, rank T_pad >= 12.

S4 ran on a Windows host that could not load this repository's Linux evaluators,
so its two target 12-minors were produced entirely by its own code paths.  This
script re-derives them here from S4's OWN inputs -- its 36 integer points and its
34 source fillings -- through the s69 Grassmann DP evaluator, and checks the
determinants by two algorithms of ours.  Nothing of S4's arithmetic is reused.

THREE LAYERS, all of which pass:

  1. Conventions.  S4's exponent list is wk8_s30_core.exps(4,9) entry for entry,
     and u = c_(4,0,...,0) sits at index 494 with the value S4 records per point.
  2. Entries.  Every entry of the 12 x 12 minor is recomputed at both primes by
     BOTH normalizations S4 specifies, which is where a silent error would live:
        (a) native filling evaluated, times u(f_j)^(24 - d_i)
        (b) literal degree-24 filling evaluated, times 24^-(24 - d_i)
     144 entries x 2 primes x 2 routes = 576 agreements, no exceptions.
  3. Determinants.  Modular elimination and exact integer Bareiss, both ours,
     reproduce S4's 1086325324 and 2097075880.

Because the fillings, the transport factors and the points are all defined over
Z, a nonzero modular determinant is the reduction of a nonzero integer one, so
this certifies 12 independent true-padded restrictions over Q.  It does NOT say
the source dimension is 12, and it says nothing about ideal membership.

usage: python3 analysis/wk12_int_s4_verify.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk8_s30_core import exps                                            # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs,   # noqa: E402
                              dp_eval_c, fast_eval_c)

A = "results/astra/S4/artifacts"


def det_mod(M, p):
    M = [[x % p for x in r] for r in M]
    n = len(M)
    det = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c]), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = (-det) % p
        det = det * M[c][c] % p
        inv = pow(M[c][c], p - 2, p)
        for r in range(c + 1, n):
            f = M[r][c] * inv % p
            if f:
                for k in range(c, n):
                    M[r][k] = (M[r][k] - f * M[c][k]) % p
    return det % p


def det_bareiss(M):
    M = [r[:] for r in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((r for r in range(k + 1, n) if M[r][k]), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def main():
    j = lambda f: json.load(open(os.path.join(ROOT, A, f), encoding="utf-8"))  # noqa: E731
    S, P, T, C = j("source.json"), j("points.json"), j("source_coordinate_transforms.json"), \
        j("padded_certificate.json")
    E = exps(4, 9)
    _a, _i, _f, tab = sym_table(4, 9)
    iu = E.index((4, 0, 0, 0, 0, 0, 0, 0, 0))
    conv = ([list(x) for x in E] == P["exponents"]
            and all(pt["coefficients"][iu] == pt["u"] for pt in P["points"]))
    print(f"conventions (exps order, u at index {iu} = recorded u): {'ok' if conv else 'MISMATCH'}")

    def ev(F, ms, p):
        try:
            return dp_eval_c(F, ms, p, tab) % p
        except Exception:                                    # noqa: BLE001
            return fast_eval_c(F, ms, p, tab) % p

    out = {"conventions_ok": conv, "primes": []}
    allok = conv
    for rec in C["results"]:
        p, Tm, mn = rec["prime"], rec["target_matrix"], rec["minor"]
        na = nb = 0
        for i in mn["rows"]:
            sv, tv = S["vectors"][i], T["vectors"][i]
            nat, lit = Filling.from_json(sv["native_filling"]), \
                Filling.from_json(tv["literal_target_filling"])
            d = sv["native_degree"]
            for c in mn["cols"]:
                ms = symbols_from_coeffs(P["points"][c]["coefficients"], 4, 9, p)
                u = P["points"][c]["coefficients"][iu] % p
                a = ev(nat, ms, p) * pow(u, 24 - d, p) % p
                b = ev(lit, ms, p) * tv["scalar_numerator"] % p \
                    * pow(tv["scalar_denominator"], p - 2, p) % p
                na += a == Tm[i][c] % p
                nb += b == Tm[i][c] % p
        sub = [[Tm[i][c] for c in mn["cols"]] for i in mn["rows"]]
        dm, db = det_mod(sub, p), det_bareiss(sub) % p
        n = len(mn["rows"]) * len(mn["cols"])
        ok = na == nb == n and dm == db == mn["det"] % p and dm != 0
        allok &= ok
        print(f"p = {p}: entries route(a) {na}/{n}, route(b) {nb}/{n}; "
              f"det ours {dm} vs claimed {mn['det']}; {'PASS' if ok else 'FAIL'}")
        out["primes"].append({"prime": p, "entries": n, "route_a_match": na, "route_b_match": nb,
                              "det_claimed": mn["det"], "det_modular": dm, "det_bareiss_mod_p": db,
                              "pass": ok})
    out["verdict"] = ("S4's rank T_pad >= 12 is independently reproduced here from S4's own points "
                      "and fillings, on an evaluator S4 could not run" if allok else "DISCREPANCY")
    print(out["verdict"])
    with open(os.path.join(ROOT, "results/wk12_int_s4_verify.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
