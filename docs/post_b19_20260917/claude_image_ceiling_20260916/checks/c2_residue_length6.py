"""c2_residue_length6.py -- second and last bounded check of work/claude_image_ceiling_20260916.

(a) Weight-space dimensions N_S(mu) of Sym^6(Sym^3 C^6) at the four length-6 weights with a_3 > 0
    listed in batch-13 transfer_lemma.md: (8,2,2,2,2,2), (7,4,2,2,2,1), (6,5,3,2,1,1), (5,5,5,1,1,1),
    by a pruned multiset DP (states w <= mu componentwise). Compare with the batch-13 residue values
    {3988, 4028, 4456} of d5_ideal.md section 5.
(b) Impact of the census horizontal-strip over-count on padding_ceiling U: for every d = 6 five-row
    cell, compare min(a, T_recomputed) with the census U.
(c) Cells at d = 5, 6 whose Pieri range contains no length-5 mu with a_3 > 0 (route inert in all
    degrees by the length-5 concentration of I(D_5)); and the lambda_1 <= d criterion.

Pure Python. Writes results/c2_residue_length6.json (relative to cwd).
"""
import itertools
import json
import time
from pathlib import Path

T0 = time.perf_counter()
ROOT = Path(__file__).resolve().parents[3]
CENSUS = ROOT / "Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json"
C1 = Path("results/c1_pieri_transfer.json")
OUT = Path("results/c2_residue_length6.json")
RESIDUE = {3988, 4028, 4456}


def cubic_monomials(n):
    return [b for b in itertools.product(range(4), repeat=n) if sum(b) == 3]


def weight_space_dim(mu, d):
    """Number of multisets of size d of cubic monomials in len(mu) variables with total exponent mu."""
    n = len(mu)
    mons = [b for b in cubic_monomials(n) if all(b[i] <= mu[i] for i in range(n))]
    states = {(0, (0,) * n): 1}
    for b in mons:
        new = {}
        for (k, w), c in states.items():
            for j in range(0, d - k + 1):
                nw = tuple(w[i] + j * b[i] for i in range(n))
                if any(nw[i] > mu[i] for i in range(n)):
                    break
                key = (k + j, nw)
                new[key] = new.get(key, 0) + c
        states = new
    return states.get((d, tuple(mu)), 0)


report = {"script": "c2_residue_length6.py"}

# (a)
length6 = [(8, 2, 2, 2, 2, 2), (7, 4, 2, 2, 2, 1), (6, 5, 3, 2, 1, 1), (5, 5, 5, 1, 1, 1)]
ns6 = {str(list(mu)): weight_space_dim(mu, 6) for mu in length6}
report["N_S_length6_d6"] = ns6
report["residue_values"] = sorted(RESIDUE)
report["residue_matched_by_length6"] = {k: v for k, v in ns6.items() if v in RESIDUE}
report["residue_fully_explained"] = set(v for v in ns6.values() if v in RESIDUE) == RESIDUE
# control: the same routine reproduces two length-5 values of c1
c1 = json.load(open(C1))
ns5_c1 = c1["d"]["6"]["N_S_length5"]
ctrl = {}
for key in ("[6, 4, 4, 2, 2]", "[10, 2, 2, 2, 2]"):
    mu = tuple(json.loads(key))
    ctrl[key] = {"c1": ns5_c1[key], "c2_pruned": weight_space_dim(mu, 6)}
report["control_length5_reproduced"] = ctrl
report["max_N_S_length5_d6"] = max(ns5_c1.values())

# (b)
census = json.load(open(CENSUS))
rows = {(r["d"], tuple(r["weight"])): r for r in census["rows"]}
mism = {tuple(m["lambda"]): m["T_recomputed"] for m in c1["d"]["6"]["T_control"]["mismatches"]}
u_changes = []
for (d, lam), r in rows.items():
    if d != 6 or len(lam) != 5:
        continue
    T_mine = mism.get(lam, r["padding_source_raw"])
    U_mine = min(r["ambient"], T_mine)
    if U_mine != r["padding_ceiling"]:
        u_changes.append({"lambda": list(lam), "a": r["ambient"], "T_census": r["padding_source_raw"],
                          "T_recomputed": T_mine, "U_census": r["padding_ceiling"], "U_recomputed": U_mine})
report["census_U_changes_d6"] = u_changes
report["census_overcount_cells_d6"] = len(mism)

# (c)
def horizontal_strip_mus(lam, d):
    lam = list(lam) + [0]
    ranges = [range(lam[i + 1], lam[i] + 1) for i in range(5)]
    target = sum(lam) - d
    return [mu for mu in itertools.product(*ranges) if sum(mu) == target]

inert = {}
for d in (5, 6):
    a3_l5 = {tuple(json.loads(k)): v for k, v in c1["d"][str(d)]["length5_weights_a3"].items()}
    cells_inert = []
    cells_live = []
    for (dd, lam), r in rows.items():
        if dd != d or len(lam) != 5:
            continue
        l5 = [list(mu) for mu in horizontal_strip_mus(lam, d) if mu in a3_l5]
        (cells_live if l5 else cells_inert).append({"lambda": list(lam), "a": r["ambient"], "s": r["symmetric"],
                                                   "length5_mus_in_range": l5})
    inert[str(d)] = {"cells_with_no_length5_mu": cells_inert, "num_inert": len(cells_inert),
                     "num_with_length5_mu": len(cells_live),
                     "lambda1_le_d_all_inert": all(c["lambda"][0] <= d for c in cells_inert)
                                                 and all(c["lambda"][0] >= d + 1 for c in cells_live)}
report["inert_cells"] = inert
report["wall_seconds"] = round(time.perf_counter() - T0, 3)
OUT.write_text(json.dumps(report, indent=1) + "\n")
print(json.dumps({k: report[k] for k in ("N_S_length6_d6", "residue_matched_by_length6", "residue_fully_explained",
                                          "control_length5_reproduced", "max_N_S_length5_d6",
                                          "census_U_changes_d6", "census_overcount_cells_d6", "wall_seconds")}, indent=1))
for d in ("5", "6"):
    e = inert[d]
    print("d", d, "inert", e["num_inert"], "live", e["num_with_length5_mu"], "lambda1 criterion exact:", e["lambda1_le_d_all_inert"])
    print("  inert cells:", [c["lambda"] for c in e["cells_with_no_length5_mu"]])
