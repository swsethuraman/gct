#!/usr/bin/env python3
"""Session 74 -- assemble the evaluation columns under the declared row system and
read the decision table.

Reads results/s74/source.json and results/s74/columns_<family>_<p>.json (native
values F_{T_i}(f_j) mod p at the K points of each family) and forms

    M_24[i, j] = native[i][j] * usym[j]^(24 - d_i)     (the literal transported rows)
    M_23[i, j] = native[i][j] * usym[j]^(23 - d_i),  rows with d_i <= 23, first 281 points

then: generic rank (assembly check), rank T_det on M_23 (i_det(23)) and on M_24,
rank T_pad, rank T_red, rank T_per4, the left kernels U_D, U_P in source
coordinates, dim(U_D cap U_P), the orientation, and D = rank T_pad - rank T_det.
All ranks by python-flint.  Writes results/s74/decision.json and prints the table.

    python3 analysis/wk12_s74_decide.py [--prime 2147483647] [--families gen,det,pad,red,per4]
"""
import argparse
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from flint import nmod_mat                                            # noqa: E402
from wk8_s30_core import P1, P2                                       # noqa: E402
from wk11_s69_circuit import rank_mod, nullspace_mod, rat_recon       # noqa: E402

OUT = os.environ.get("S74_OUT", os.path.join(ROOT, "results", "s74"))
A24, A23 = 274, 273


def load_col(family, p):
    """a banked column; the generic column is stored gzipped (5 MB rule)."""
    path = os.path.join(OUT, f"columns_{family}_{p}.json")
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    if os.path.exists(path + ".gz"):
        import gzip
        return json.load(gzip.open(path + ".gz", "rt", encoding="utf-8"))
    return None


def assemble(src, col, p, top):
    """rows for the degree-`top` source: entries with rung <= top, exponent top - d."""
    usym = col["u_symbol"]
    K = len(usym) if top == 24 else min(len(usym), A23 + 8)
    rows, idx = [], []
    for e in src["entries"]:
        if e["rung"] > top:
            continue
        key = json.dumps(e["key"])
        if key not in col["rows_native"]:
            continue
        nat = col["rows_native"][key]
        ex = top - e["rung"]
        rows.append([nat[j] * pow(usym[j], ex, p) % p for j in range(K)])
        idx.append(e["index"])
    return rows, idx, K


def left_kernel(rows, p):
    """{x : x^T rows = 0} as python-int vectors over the row index."""
    nr, nc = len(rows), len(rows[0])
    T = [[rows[i][j] for i in range(nr)] for j in range(nc)]
    return nullspace_mod(T, nr, p)


def dim_sum(U, V, p):
    if not U and not V:
        return 0
    return rank_mod(U + V, p)


def in_span(vecs, U, p):
    """every vec in vecs lies in span(U) mod p."""
    if not vecs:
        return True
    if not U:
        return all(all(x % p == 0 for x in v) for v in vecs)
    return rank_mod(U + vecs, p) == rank_mod(U, p)


def reconstruct(vec, p):
    """rational reconstruction of a mod-p vector to a primitive integer vector (None on failure)."""
    piv = next((c for c in vec if c % p), None)
    if piv is None:
        return None
    inv = pow(piv, -1, p)
    fr = []
    for c in vec:
        rr = rat_recon(c * inv % p, p)
        if rr is None:
            return None
        fr.append(rr)
    L = 1
    for _, den in fr:
        L = L * den // math.gcd(L, den)
    v = [num * (L // den) for num, den in fr]
    g = 0
    for x in v:
        g = math.gcd(g, abs(x))
    return [x // g for x in v] if g > 1 else v


def decide(p, families):
    src = json.load(open(os.path.join(OUT, "source.json"), encoding="utf-8"))
    n_src = src["size"]
    out = dict(prime=p, source_size=n_src, source_complete=src["complete"], present=src["present"],
               row_system=src["row_system"], columns={})
    kern = {}
    for fam in families:
        col = load_col(fam, p)
        if col is None:
            out["columns"][fam] = dict(status="absent")
            continue
        rows24, idx24, K24 = assemble(src, col, p, 24)
        rec = dict(K=K24, rows=len(rows24), banked_rows=len(col["rows_native"]))
        if len(rows24) == 0:
            out["columns"][fam] = rec
            continue
        t0 = time.time()
        rk24 = rank_mod(rows24, p)
        rec["rank_24"] = rk24
        rec["nullity_24"] = len(rows24) - rk24
        rows23, idx23, K23 = assemble(src, col, p, 23)
        rk23 = rank_mod(rows23, p) if rows23 else 0
        rec["rank_23"] = rk23
        rec["rows_23"] = len(rows23)
        rec["nullity_23"] = len(rows23) - rk23
        if fam in ("det", "pad", "red", "per4"):
            kv = left_kernel(rows24, p) if rk24 < len(rows24) else []
            kern[fam] = (kv, idx24)
            rec["kernel_dim"] = len(kv)
            rec["kernel_rows_index"] = idx24 if kv else None
            rec["kernel_vectors_modp"] = kv if kv and len(kv) <= 8 else None
        rec["secs"] = round(time.time() - t0, 1)
        out["columns"][fam] = rec
        print(f"p={p} {fam:5s}: rows {len(rows24):3d}/{n_src} K={K24}: rank_24 = {rk24:3d} (nullity {len(rows24)-rk24}); "
              f"delta=23 rows {len(rows23)} rank_23 = {rk23} (nullity {len(rows23)-rk23})", flush=True)
    # the decision quantities, on the rows present
    if "det" in kern and "pad" in kern:
        UD, iD = kern["det"]
        UP, iP = kern["pad"]
        assert iD == iP, "det and pad columns cover different rows; refusing to compare kernels"
        rd = out["columns"]["det"]["rank_24"]
        rp = out["columns"]["pad"]["rank_24"]
        dsum = dim_sum(UD, UP, p)
        inter = len(UD) + len(UP) - dsum
        dec = dict(rank_T_det=rd, rank_T_pad=rp, i_det=len(UD), i_pad=len(UP), D=rp - rd,
                   dim_UD=len(UD), dim_UP=len(UP), dim_UD_plus_UP=dsum, dim_UD_cap_UP=inter,
                   UD_subset_UP=in_span(UD, UP, p), UP_subset_UD=in_span(UP, UD, p),
                   rows_compared=len(iD), source_complete=src["complete"])
        if "red" in kern:
            UR, _ = kern["red"]
            dec["i_red"] = len(UR)
            dec["rank_T_red"] = out["columns"]["red"]["rank_24"]
            dec["UR_subset_UP"] = in_span(UR, UP, p)          # P_9 in R_9: I(R) in I(P) -> U_R in U_P
            dec["UR_subset_UD"] = in_span(UR, UD, p)
        if "per4" in kern:
            dec["i_per4"] = len(kern["per4"][0])
            dec["rank_T_per4"] = out["columns"]["per4"]["rank_24"]
        if "gen" in out["columns"] and "rank_24" in out["columns"]["gen"]:
            dec["generic_rank"] = out["columns"]["gen"]["rank_24"]
        # the characteristic-zero exhibit for a one-dimensional det kernel
        if len(UD) == 1:
            v = reconstruct(UD[0], p)
            dec["UD_integer"] = v
            dec["UD_integer_support"] = sum(1 for x in v if x) if v else None
            dec["UD_integer_maxabs"] = max(abs(x) for x in v) if v else None
        out["decision"] = dec
        print(f"p={p}: rank T_det = {rd}, rank T_pad = {rp}, i_det = {len(UD)}, i_pad = {len(UP)}, "
              f"D = {rp - rd}, dim(U_D cap U_P) = {inter}, U_D in U_P: {dec['UD_subset_UP']}, "
              f"U_P in U_D: {dec['UP_subset_UD']}" + (f", i_red = {dec['i_red']}" if 'i_red' in dec else "")
              + (f", i_per4 = {dec['i_per4']}" if 'i_per4' in dec else ""), flush=True)
    path = os.path.join(OUT, f"decision_{p}.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=1)
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=P1)
    ap.add_argument("--families", default="gen,det,pad,red,per4")
    args = ap.parse_args(argv)
    decide(args.prime, args.families.split(","))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
