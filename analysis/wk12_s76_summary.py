#!/usr/bin/env python3
"""s76 -- summarise the finished recursion runs: the top-cell source, the
independent B_24 / a_24 / C_24 re-derivations, the per-level cost table, the
agreement between the two house primes, and the Weyl spot checks.

Writes results/s76_recursion_summary.json and results/s76_source24_p<P>.npz
(the 274 x 2168 reduced-row-echelon basis of M_24 in precursor coordinates,
column blocks over the twelve predecessors in horiz_strips order).
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
from wk11_int_bdelta import lam_of, horiz_strips        # noqa: E402
from wk12_s76_recursion import P1, P2, load_refs, build_dag   # noqa: E402

DAG = os.path.join(ROOT, "results", "s76_dag")
lam = tuple(lam_of(24))
out = {"lambda": list(lam), "primes": {}}
dims = {}
for p in (P1, P2):
    f = os.path.join(DAG, f"dims_p{p}.json")
    if not os.path.exists(f):
        continue
    dims[p] = json.load(open(f))
if not dims:
    sys.exit("no finished run")

# the a-tables agree between primes
ps = sorted(dims)
if len(ps) == 2:
    A, B = dims[ps[0]]["a"], dims[ps[1]]["a"]
    common = [d for d in A if d in B]
    diff = sum(1 for d in common for k in A[d] if A[d][k] != B[d].get(k))
    out["two_prime_agreement"] = {"levels_compared": len(common), "disagreements": diff}

refs, src = load_refs(ROOT, 24)
spot = {}
sf = os.path.join(ROOT, "results", "s76_weyl_spotchecks.json")
if os.path.exists(sf):
    for k, v in json.load(open(sf)).items():
        spot[(tuple(v["nu"]), v["delta"])] = v["a"]
for p in ps:
    a = dims[p]["a"]
    top_d = max(int(d) for d in a)
    rec = {"levels_done": top_d}
    if top_d >= 23:
        a23 = {tuple(eval(k)): v for k, v in a["23"].items()}
        preds = horiz_strips(lam, 4)
        rec["a_23_by_predecessor"] = {str(mu): a23.get(mu, 0) for mu in preds}
        rec["B_24_recursion"] = sum(a23.get(mu, 0) for mu in preds)
        rec["ladder_predecessor_a_23"] = a23.get(tuple(lam_of(23)), 0)
    if top_d >= 22:
        a22 = {tuple(eval(k)): v for k, v in a["22"].items()}
        from wk11_int_cdelta import two_strip_paths
        rec["C_24_recursion"] = sum(a22.get(nu, 0) for _, nu in two_strip_paths(24))
    if top_d >= 24:
        rec["a_24_recursion"] = a["24"].get(str(lam), 0)
    # every banked reference and every spot check vs the recursion
    checked = mism = 0
    spot_checked = spot_mism = 0
    for (nu, d), v in refs.items():
        if str(d) in a and str(nu) in a[str(d)]:
            checked += 1
            if a[str(d)][str(nu)] != v:
                mism += 1
    for (nu, d), v in spot.items():
        if str(d) in a and str(nu) in a[str(d)]:
            spot_checked += 1
            if a[str(d)][str(nu)] != v:
                spot_mism += 1
    rec["banked_refs_checked"] = checked
    rec["banked_refs_mismatch"] = mism
    rec["weyl_spotchecks_checked"] = spot_checked
    rec["weyl_spotchecks_mismatch"] = spot_mism
    st = dims[p]["stats"]
    rec["per_level"] = {d: {k: s[k] for k in ("shapes", "nonzero", "sum_a", "sum_aB", "max_B",
                                              "max_rows", "max_C", "secs")}
                        for d, s in st.items()}
    rec["worst_node_by_C"] = max((s["worst"] for s in st.values() if s["worst"]),
                                 key=lambda w: w[4])
    rec["total_secs"] = round(sum(s["secs"] for s in st.values()), 1)
    rec["peak_sum_aB"] = max(s["sum_aB"] for s in st.values())
    rec["total_sum_aB"] = sum(s["sum_aB"] for s in st.values())
    rec["total_sum_a"] = sum(s["sum_a"] for s in st.values())
    out["primes"][str(p)] = rec
    # the top-cell source
    lf = os.path.join(DAG, f"level_24_p{p}.npz")
    if os.path.exists(lf):
        z = np.load(lf)
        E = z[str(lam)]
        np.savez_compressed(os.path.join(ROOT, "results", f"s76_source24_p{p}.npz"), E24=E,
                            predecessors=np.array([str(mu) for mu in horiz_strips(lam, 4)]),
                            block_widths=np.array([rec["a_23_by_predecessor"][str(mu)]
                                                   for mu in horiz_strips(lam, 4)]))
        rec["source24_shape"] = list(E.shape)
        rec["source24_pivots"] = int(sum(1 for i in range(E.shape[0])))
json.dump(out, open(os.path.join(ROOT, "results", "s76_recursion_summary.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "primes"}, indent=1))
for p, rec in out["primes"].items():
    print(p, {k: v for k, v in rec.items() if k not in ("per_level", "a_23_by_predecessor")})
