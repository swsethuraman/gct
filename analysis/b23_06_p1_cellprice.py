"""B23-06 pilot 1: price cells by exact weight-space dimensions of Sym^d(Sym^n C^r).

Pricing only. No multiplicity of any orbit closure, no rank, no evaluation at any point.
See results/b23_06/PREREG.md for the controls (C1-C5) and configurations.
"""
import argparse
import hashlib
import itertools
import json
import math
import time
from pathlib import Path

import numpy as np

T0 = time.time()


def exponents(n, r):
    return [a for a in itertools.product(range(n + 1), repeat=r) if sum(a) == n]


def weight_function(n, r, d):
    """layers[d][mu] = dim of the mu-weight space of Sym^d(Sym^n C^r), exact in uint32."""
    layers = [np.ones((1,) * r, dtype=np.uint32)]
    for k in range(1, d + 1):
        layers.append(np.zeros((n * k + 1,) * r, dtype=np.uint32))
    for a in exponents(n, r):
        for k in range(1, d + 1):  # ascending k: unbounded multiplicity of item a
            side = n * (k - 1) + 1
            sl = tuple(slice(aj, aj + side) for aj in a)
            layers[k][sl] += layers[k - 1]
    return layers[d]


def partitions(total, parts, maxpart=None):
    """Partitions of total with at most `parts` parts, as length-`parts` tuples (zero padded)."""
    if maxpart is None:
        maxpart = total
    if parts == 0:
        if total == 0:
            yield ()
        return
    for first in range(min(total, maxpart), -1, -1):
        if first * parts < total:
            break
        for rest in partitions(total - first, parts - 1, first):
            yield (first,) + rest


def weyl_dim(lam):
    r = len(lam)
    num = den = 1
    for i in range(r):
        for j in range(i + 1, r):
            num *= lam[i] - lam[j] + j - i
            den *= j - i
    return num // den


def perm_sign(p):
    s, seen = 1, [False] * len(p)
    for i in range(len(p)):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            if L % 2 == 0:
                s = -s
    return s


def config(n, r, d):
    t = time.time()
    W = weight_function(n, r, d)
    top = n * d
    M = math.comb(n + r - 1, r - 1)
    total = math.comb(M + d - 1, d)
    wsum = int(W.sum(dtype=np.uint64))
    rho = list(range(r - 1, -1, -1))
    perms = [(perm_sign(p), [rho[p[i]] for i in range(r)]) for p in itertools.permutations(range(r))]

    def K(mu):
        if any(x < 0 or x > top for x in mu):
            return 0
        return int(W[tuple(mu)])

    def mult(lam):
        return sum(s * K([lam[i] + rho[i] - wr[i] for i in range(r)]) for s, wr in perms)

    cells, dimcheck = [], 0
    for lam in partitions(top, r):
        a = mult(lam)
        if a < 0:
            raise RuntimeError(f"negative multiplicity at {lam}")
        dimcheck += a * weyl_dim(lam)
        if a > 0 and lam[-1] > 0:
            cells.append({"lambda": list(lam), "N_S": K(list(lam)), "a": a,
                          "rectangle": len(set(lam)) == 1})
    nonrect = [c for c in cells if not c["rectangle"]]
    ns = sorted(c["N_S"] for c in nonrect)
    out = {
        "n": n, "r": r, "d": d, "M_exponent_vectors": M,
        "dim_Sym_d_Sym_n_affine": total, "weight_function_total": wsum,
        "C0_total_matches": wsum == total,
        "C4_weyl_identity": dimcheck == total,
        "exactly_r_row_cells_with_a_pos": len(cells),
        "nonrect_cells": len(nonrect),
        "N_S_nonrect_min": ns[0] if ns else None,
        "N_S_nonrect_median": ns[len(ns) // 2] if ns else None,
        "N_S_nonrect_max": ns[-1] if ns else None,
        "cheapest_nonrect_cell": min(nonrect, key=lambda c: c["N_S"]) if nonrect else None,
        "rectangles": [c for c in cells if c["rectangle"]],
        "cells": cells,
        "seconds": round(time.time() - t, 3),
    }
    return out


def log10_avg_weight_dim(n, r, d):
    M = math.comb(n + r - 1, r - 1)
    return math.log10(math.comb(M + d - 1, d)) - math.log10(math.comb(n * d + r - 1, r - 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prereg", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    prereg = Path(args.prereg).read_bytes()
    me = Path(__file__).read_bytes()
    cap = {n: 5 * n * (n - 1) ** 2 * (7 * n - 8) // 12 for n in range(2, 8)}
    res = {
        "run": "b23_06_p1_cellprice",
        "prereg_sha256": hashlib.sha256(prereg).hexdigest(),
        "script_sha256": hashlib.sha256(me).hexdigest(),
        "C5": {
            "dim_Sym4_C16_affine": math.comb(19, 4), "dim_Sym5_C25_affine": math.comb(29, 5),
            "cap": cap,
            "cap_exact_division": all((5 * n * (n - 1) ** 2 * (7 * n - 8)) % 12 == 0 for n in range(2, 8)),
            "C5_pass": math.comb(19, 4) == 3876 and math.comb(29, 5) == 118755
                       and [cap[n] for n in range(2, 8)] == [5, 65, 300, 900, 2125, 4305],
        },
        "flattening_rank_Cnk_sq": {n: {k: math.comb(n, k) ** 2 for k in range(1, n)} for n in range(4, 8)},
        "log10_avg_weight_space_dim": {
            f"({n},{r},{d})": round(log10_avg_weight_dim(n, r, d), 2)
            for (n, r, d) in [(4, 5, 5), (5, 5, 5), (6, 5, 5), (5, 6, 6), (6, 6, 6), (4, 9, 24),
                              (4, 5, cap[4]), (5, 5, cap[5]), (6, 5, cap[6])]},
        "configs": [], "skipped": [],
    }
    outp = Path(args.out)
    outp.write_text(json.dumps(res, indent=1))
    for (n, r, d) in [(4, 5, 5), (5, 5, 5), (6, 5, 5)]:
        if time.time() - T0 > 45:
            res["skipped"].append([n, r, d])
            continue
        c = config(n, r, d)
        if (n, r, d) == (4, 5, 5):
            rect = [x for x in c["rectangles"] if x["lambda"] == [4] * 5]
            c["C1_NS_4^5_is_19834"] = bool(rect) and rect[0]["N_S"] == 19834
            c["C2_a_4^5_is_1"] = bool(rect) and rect[0]["a"] == 1
            c["C3_count_is_23"] = c["exactly_r_row_cells_with_a_pos"] == 23
        res["configs"].append(c)
        outp.write_text(json.dumps(res, indent=1))
        print(n, r, d, "cells", c["exactly_r_row_cells_with_a_pos"], "NS min/med/max",
              c["N_S_nonrect_min"], c["N_S_nonrect_median"], c["N_S_nonrect_max"],
              "C0", c["C0_total_matches"], "C4", c["C4_weyl_identity"], c["seconds"], "s", flush=True)
    checks = [res["C5"]["C5_pass"], res["C5"]["cap_exact_division"]]
    for c in res["configs"]:
        checks += [c["C0_total_matches"], c["C4_weyl_identity"]]
        checks += [c[k] for k in ("C1_NS_4^5_is_19834", "C2_a_4^5_is_1", "C3_count_is_23") if k in c]
    res["checks_passed"] = f"{sum(map(bool, checks))}/{len(checks)}"
    res["wall_seconds"] = round(time.time() - T0, 2)
    outp.write_text(json.dumps(res, indent=1))
    print("checks", res["checks_passed"], "wall", res["wall_seconds"], flush=True)


if __name__ == "__main__":
    main()
