#!/usr/bin/env python3
"""Session 74 -- certificates in the declared format, session-67 spelling.

One `sparse_nullity` certificate per (family, prime) from results/s74/decision_<p>.json
and results/s74/columns_<family>_<p>.json: field "F_p", top-level nullity,
recipe, provenance, points as substitution data, basis null.  A positive
nullity exhibits its kernel through `kernel_certificates`, a companion file
holding the kernel vector(s) in the coordinates of the 274-vector circuit
source (the chi-expansion at this cell is out of range: N_S = 1.56e11), so the
verifier's exhibit-your-kernel rule is met in the only coordinates that exist
at this scale.

Honest scope: tools/verify re-derives a sparse_nullity by rebuilding [E; ev]
on the full weight space; at N_S = 156 438 903 314 that is not reachable, so
these certificates are RECORDED-class by construction.  The independent
re-derivation is analysis/wk12_s74_verify.py (fresh points, literal fillings).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                       # noqa: E402

OUT = os.environ.get("S74_OUT", os.path.join(ROOT, "results", "s74"))
CERTS = os.path.join(ROOT, "results", "certs")
CONV = {"coefficient": "c_alpha(F) = coefficient of s^alpha in F",
        "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}"}
VARIETY = dict(det="det_pencil", pad="padded_permanent", red="reducible", per4="permanent_pencil")
N_S = {24: 156438903314, 23: 156419279221}


def write(p):
    dec = json.load(open(os.path.join(OUT, f"decision_{p}.json"), encoding="utf-8"))
    src = json.load(open(os.path.join(OUT, "source.json"), encoding="utf-8"))
    cpath = os.path.join(OUT, "certified.json")
    certified = json.load(open(cpath, encoding="utf-8"))["primes"].get(str(p), {}) if os.path.exists(cpath) else {}
    os.makedirs(CERTS, exist_ok=True)
    written = []
    for fam, var in VARIETY.items():
        c = dec["columns"].get(fam)
        if not c or "rank_24" not in c:
            continue
        col = json.load(open(os.path.join(OUT, f"columns_{fam}_{p}.json"), encoding="utf-8"))
        nul = c["nullity_24"]
        cert = {
            "format": "gct-cert/1", "kind": "sparse_nullity",
            "title": f"LMR cell (65,17,2^7) delta=24: nullity_p of the {var} evaluation on the 274-vector "
                     f"circuit source built by births, p = {p}",
            "produced_by": "session 74, analysis/wk12_s74_columns.py + wk12_s74_decide.py",
            "cell": {"n": 4, "r": 9, "lambda": [65, 17, 2, 2, 2, 2, 2, 2, 2], "delta": 24, "a": 274},
            "conventions": CONV,
            "field": f"F_{p}",
            "variety": var,
            "nullity": nul,
            "points": col["points"],
            "recipe": {"K": col["K"], "point_seed": col["seed"], "bound": col["bound"],
                       "point_rule": f"random.Random({col['seed']} + j), j = 0..; entries in [-{col['bound']}, {col['bound']}]; "
                                     "points whose s_1^4 coefficient vanishes (as an integer or mod either house prime) skipped",
                       "skipped_points": col["skipped_points"], "point_index": col["point_index"],
                       "N_S": N_S[24],
                       "source": "results/s74/source.json -- 274 literal transported bracket fillings "
                                 "(s69 circuit), rung-by-rung birth bases certified at both primes "
                                 "(results/s74/births_d13..23.json), seeds results/s69_n4_seed.json, "
                                 "F_57 results/wk12_int_lmr_birth24.json",
                       "row_system": src["row_system"],
                       "rank_mod_p": c["rank_24"], "rows": c["rows"],
                       "instrument": "bracket-circuit evaluation (wk12_s74_dpc.c, the s69 DP with compact state, validated against wk11_s69_dp.c), python-flint rank; "
                                     "NOT [E; ev] on the weight space -- N_S is out of range"},
            "provenance": {"instrument": "circuit source by births", "produced_in": "session 74",
                           "cross_checked_prime": (P2 if p == P1 else P1),
                           "note": "rank_p <= rank_Q: nullity 0 proves mult = a over Q; a positive nullity "
                                   "is a mod-p kernel of the evaluation pairing on the source and bounds i_X "
                                   "from above; i_det >= 1 is the LMR theorem, not this file"},
            "basis": None,
        }
        minor = {"det": certified.get("det_minor_delta23"), "pad": certified.get("pad_minor")}.get(fam)
        if minor:
            cert["recipe"]["nonzero_minor"] = {k: minor[k] for k in ("rank", "row_set", "col_set", "det_mod_p", "statement")}
        if nul > 0:
            comp = f"s74_kernel_{fam}_{p}.json"
            kv = c.get("kernel_vectors_modp")
            kern = {"format": "gct-cert/1-companion", "kind": "circuit_kernel",
                    "title": f"ker T_{fam} at the LMR cell in the coordinates of the 274-vector circuit source, mod {p}",
                    "produced_by": "session 74",
                    "cell": cert["cell"], "prime": p, "family": var, "dimension": nul,
                    "coordinates": "coefficients on results/s74/source.json entries (index order), the literal "
                                   "transported fillings; a vector v means sum_i v_i F_{T_i^up}",
                    "rows_index": c["kernel_rows_index"],
                    "vectors_modp": kv,
                    "integer_vector": (dec.get("decision") or {}).get("UD_integer") if fam == "det" else None,
                    "note": "the chi-expansion of these vectors is out of range at this cell (N_S = 1.56e11); "
                            "they are exhibited as circuit coefficient vectors and re-derived by "
                            "analysis/wk12_s74_verify.py at fresh points"}
            json.dump(kern, open(os.path.join(CERTS, comp), "w", encoding="utf-8"))
            cert["kernel_certificates"] = [comp]
        name = f"s74_65_17_2x7_d24_{var}_{p}.json"
        json.dump(cert, open(os.path.join(CERTS, name), "w", encoding="utf-8"))
        written.append((name, nul, c["rank_24"]))
    for name, nul, rk in written:
        print(f"wrote results/certs/{name}: rank {rk}, nullity {nul}")
    return written


if __name__ == "__main__":
    for p in (P1, P2):
        if os.path.exists(os.path.join(OUT, f"decision_{p}.json")):
            write(p)
