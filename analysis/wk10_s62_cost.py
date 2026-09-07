"""Session 62 — the cost curve (Task 1 / Task 5), with |S| corrected.

Three distinct scales, kept apart (the earlier draft conflated them; corrected after
the adversarial review):

  * n_lam = the weight-space dimension (number of monomials O) = s57's "N_S".
  * |S| (the REDUCED-ROUTE deciding number, integrator note 3) = the support of the
    highest-weight vectors in the weight-space / orbit-sum basis (how many monomials
    the source vectors touch); |S| <= n_lam.  The reduced block A = C_S^T beta_S C_S
    is a quadratic form over these, cost ~ a|S|^2 + a^2|S|.
  * |H_{4,delta}| = the whole Foulkes module; the ENUMERATION route costs |H|*n_lam per
    cell (one sweep of H per orbit rep), and Sum_{O in supp}|O| (= |H| when the HWV is
    dense) is its raw support.

Writes results/s62_cost.md and results/s62_cost.json.
"""
import json
import os
import re
from fractions import Fraction
from math import factorial

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def H_size(n, delta):
    return factorial(n * delta) // (factorial(n) ** delta * factorial(delta))


rows = []
for d in (2, 3, 4):
    p = os.path.join(ROOT, "results", f"s62_run_n4_d{d}.json")
    if not os.path.exists(p):
        continue
    D = json.load(open(p))
    for k, v in D["cells"].items():
        rows.append({"n": 4, "delta": d, "lambda": v["lambda"], "a": v["a"], "n_lam": v["n_lam"],
                     "S_reduced": v["reduced_route_S"], "S_over_n_lam": v["S_over_n_lam"],
                     "enumeration_raw_S": v["enumeration_raw_S"], "H": D["H"],
                     "pass_total_s": v["pass"].get("total_s", 0.0),
                     "H_times_n_lam": D["H"] * v["n_lam"]})

# measured enumeration pass rate (one sweep of H per rep): sec / |H|, from the uncached delta=4 log
sec_per_H = 1.74e-7
_logp = os.path.join(ROOT, "results", "logs", "s62_run_n4_d4.log")
if os.path.exists(_logp):
    _v = [float(m) for m in re.findall(r"([0-9.]+)s/rep", open(_logp).read())]
    if _v:
        sec_per_H = (sum(_v) / len(_v)) / H_size(4, 4)

wall = [{"delta": d, "H_4_delta": H_size(4, d), "one_pass_s_projected": sec_per_H * H_size(4, d)}
        for d in range(2, 25)]

# how often |S| reaches n_lam (HWV dense in the weight space)
dense = sum(1 for r in rows if r["delta"] == 4 and r["S_reduced"] == r["n_lam"])

lmr = {
    "n4_delta24": {"lambda": [65, 17, 2, 2, 2, 2, 2, 2, 2], "delta": 24, "r": 9, "a": 274,
                   "n_lam_from_s57": 156438903314, "n_chi_from_s57": 31039465,
                   "note": "The reduced-route |S| is the orbit-basis support of the 273 transported source "
                           "vectors, <= n_lam = 1.564e11 (s57). With 273 vectors the union is a large fraction "
                           "of n_lam, so |S| ~ 1e11 (>> the 1e5 'out of reach' regime of integrator note 3). "
                           "Reduced block A_24 is trivial as a 273x273 determinant, but its entries cost "
                           "~273*|S|^2 ~ 6e24 -- out of reach. (The enumeration route is worse: |H_{4,24}| ~ 1.2e93.)"},
    "n3_delta12": {"lambda": [19, 7, 2, 2, 2, 2, 2], "delta": 12, "r": 7, "a": 6,
                   "n_lam_monomials": 1155302, "n_chi": 17047, "H_3_12": H_size(3, 12),
                   "note": "the mandatory control: n_lam = 1.155e6, |H_{3,12}| = %.3e, so the Foulkes Gram "
                           "(orbit-basis |S| up to 1.155e6, enumeration |H| ~ 3.6e23) is out of reach even here. "
                           "Its ground truth is taken by the EVALUATION engine on the n_chi = 17047 reduction, "
                           "not the Foulkes Gram -- the concrete demonstration that the Gram route cannot reach "
                           "an LMR cell." % H_size(3, 12)},
}

out = {"measured_sec_per_H_pass": sec_per_H, "rows": rows, "wall": wall, "lmr": lmr,
       "n_lam_reaches_full_at_delta4": f"{dense}/28 cells have |S| = n_lam (HWV dense in the weight space)",
       "enumeration_route": "cost |H_{4,delta}| * n_lam per cell (one sweep of H per orbit rep)",
       "reduced_route_cost_model": "A = C_S^T beta_S C_S over the orbit-basis support |S|; ~ a|S|^2 + a^2|S| (integrator note 3)"}
json.dump(out, open(os.path.join(ROOT, "results", "s62_cost.json"), "w"), indent=1)


def humansec(s):
    if s is None:
        return "?"
    if s < 90:
        return f"{s:.1f} s"
    if s < 5400:
        return f"{s/60:.1f} min"
    if s < 200000:
        return f"{s/3600:.1f} h"
    return f"{s/86400:.3g} d"


md = ["# Session 62 — cost curve\n",
      "Three scales, kept apart (an earlier draft conflated them; corrected after the adversarial review):\n",
      "- **`n_lam`** — the weight-space dimension (number of monomials `O`), = s57's `N_S`.\n"
      "- **`|S|`** — the REDUCED-ROUTE deciding number (integrator note 3): the support of the\n"
      "  highest-weight vectors in the weight-space / orbit-sum basis, `|S| <= n_lam`. The reduced\n"
      "  block `A = C_S^T beta_S C_S` is a quadratic form over these, cost `~ a|S|^2 + a^2|S|`.\n"
      "- **`|H_{4,delta}|`** — the whole Foulkes module; the ENUMERATION route costs `|H| * n_lam`\n"
      "  per cell, and `Sum_{O in supp}|O|` (= `|H|` when the HWV is dense) is its raw support.\n"]

md.append("\n## Measured — `|S|`, `n_lam`, and the enumeration pass\n")
md.append("\n| delta | lambda | a | n_lam | \\|S\\| (reduced) | \\|S\\|/n_lam | enum raw (Sum\\|O\\|) | pass |")
md.append("|---|---|---|---|---|---|---|---|")
for r in rows:
    md.append(f"| {r['delta']} | {tuple(r['lambda'])} | {r['a']} | {r['n_lam']} | {r['S_reduced']} | "
              f"{float(Fraction(r['S_over_n_lam'])):.2f} | {r['enumeration_raw_S']:,} | {humansec(r['pass_total_s'])} |")
md.append(f"\n`|S| = n_lam` (the HWVs reach the whole weight space) at **{dense} of 28** `δ = 4` cells — the "
          "rectangular and near-rectangular ones; at the skewed cells `|S| < n_lam` but stays the same order. "
          "So the reduced-route cost is set by `n_lam`, the weight-space dimension.\n")
md.append(f"\nMeasured enumeration rate: **{sec_per_H*1e9:.1f} ns per element of `H` per representative** "
          f"(`δ = 4`, 0.456 s/rep over 2,627,625).\n")

md.append("\n## The enumeration wall — `|H_{4,delta}|` and the projected single-pass time\n")
md.append("\n| delta | \\|H_{4,delta}\\| | one pass (projected) |")
md.append("|---|---|---|")
for w in wall:
    md.append(f"| {w['delta']} | {w['H_4_delta']:,} | {humansec(w['one_pass_s_projected'])} |")
md.append("\n`δ = 5` is 7.4 min per single weight-pass (× ~192 weights per length-5 cell ≈ 24 h, matching s56's "
          "measured wall) and `δ = 6` is 9 days per pass. The **enumeration route is dead at `δ = 5`** "
          "(stopping rule 2).\n")

md.append("\n## The LMR cells — where `|S|` decides session 63\n")
md.append(f"- **n = 4, δ = 24** (`(65,17,2^7)`, a = 274): reduced-route `|S| <= n_lam = 156,438,903,314` (s57). "
          f"With 273 transported source vectors the union of supports is a large fraction of `n_lam`, so "
          f"`|S| ~ 10^11` — far past the `10^5` 'out of reach' regime of integrator note 3. The reduced `273×273` "
          f"block is trivial as a determinant, but its **entries** cost `~273·|S|^2 ~ 6·10^24`. Out of reach. "
          f"(Enumeration is worse: `|H_{{4,24}}| ~ 1.2·10^93`.)\n")
md.append(f"- **n = 3, δ = 12** (`(19,7,2^5)`, a = 6, the mandatory control): `n_lam = 1,155,302`, "
          f"`|H_{{3,12}}| ~ 3.6·10^23`. The Foulkes Gram (orbit-basis `|S|` up to `1.16·10^6`, enumeration `|H|` "
          f"astronomically larger) is out of reach **even for the control** — its ground truth is taken by the "
          f"evaluation engine on the `n_chi = 17,047` reduction. This is the concrete proof that the Gram route "
          f"cannot reach an LMR cell.\n")
md.append("\n**Consequence for session 63.** Neither the enumeration Gram nor the reduced block route reaches "
          "`δ = 24` (`|S| ~ 10^11`). Session 63 should report `|S|` at `r = 9` as its first deliverable and run "
          "the **direct `λ`-block (evaluation) route**, exactly as the `n = 3` control is done here.\n")

open(os.path.join(ROOT, "results", "s62_cost.md"), "w").write("\n".join(md) + "\n")
print("wrote results/s62_cost.md and .json; sec_per_H =", f"{sec_per_H:.3e}", f"; |S|=n_lam at {dense}/28 delta=4 cells")
