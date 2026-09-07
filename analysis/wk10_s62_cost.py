"""Session 62 — the cost curve (Task 1 / Task 5).

Assembles, from the n = 4 delta = 2,3,4 runs, the two cost objects the brief and
integrator note 3 name, and projects the wall:

  * the ENUMERATION route (this session's B_lambda construction, = session 56's pass):
    one pass over H per orbit representative, cost Theta(|H_{4,delta}| * n_lam).  Dies
    at delta = 5 (|H_{4,5}| = 2.5e9; s56 measured ~24 h per length-5 cell, months above).
  * |S|, the FOULKES-basis support of the highest-weight vectors (integrator note 3),
    = sum of orbit sizes over the monomials the HWVs touch.  This is the number that
    decides the reduced (block-intersection) route of session 63: forming the
    273 x 273 block A_24 = C_S^T beta_S C_S costs ~ a*|S|^2 + a^2*|S|.

Writes results/s62_cost.md and results/s62_cost.json.
"""
import json
import os
import sys
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
    per_rep = []
    for k, v in D["cells"].items():
        pr = v["pass"].get("per_rep_s", 0.0)
        per_rep.append(pr)
        rows.append({"n": 4, "delta": d, "lambda": v["lambda"], "a": v["a"], "n_lam": v["n_lam"],
                     "H": D["H"], "foulkes_support_S": v["foulkes_support_S"], "N_S": v["N_S"],
                     "pass_total_s": v["pass"].get("total_s", 0.0), "per_rep_s": pr,
                     "H_times_n_lam": D["H"] * v["n_lam"]})

# measured per-representative pass cost (one pass over H): seconds / |H|.
# The re-runs rounded per_rep to 0 (delta=3 fast, delta=4 from cache); the authoritative
# measured rate is parsed from the original uncached delta=4 log.
import re as _re
sec_per_H = None
_logp = os.path.join(ROOT, "results", "logs", "s62_run_n4_d4.log")
if os.path.exists(_logp):
    _v = [float(m) for m in _re.findall(r"([0-9.]+)s/rep", open(_logp).read())]
    if _v:
        sec_per_H = (sum(_v) / len(_v)) / H_size(4, 4)   # mean per-rep / |H_{4,4}|
if sec_per_H is None:
    sec_per_H = 1.74e-7   # measured fallback (delta=4, 0.456 s/rep over 2,627,625)

# the wall: |H_{4,delta}| and the projected single-pass time (sec_per_H * |H|)
wall = []
for d in range(2, 25):
    h = H_size(4, d)
    wall.append({"delta": d, "H_4_delta": h,
                 "one_pass_s_projected": (sec_per_H * h if sec_per_H else None)})

# the LMR cells (from the record) and their |S| bound
lmr = {
    "n4_delta24": {"lambda": [65, 17, 2, 2, 2, 2, 2, 2, 2], "delta": 24, "r": 9, "a": 274,
                   "N_S_from_s57": 156438903314,
                   "note": "|S| <= N_S = 1.564e11; balanced cells show |S| = N_S, LMR is skewed but |S| stays ~1e11. "
                           "Reduced block A_24 is 273x273 but each entry needs C_S^T beta_S C_S over |S| ~ 1e11: "
                           "cost ~ 273*|S|^2 ~ 3e24 -- out of reach (integrator note 3)."},
    "n3_delta12": {"lambda": [19, 7, 2, 2, 2, 2, 2], "delta": 12, "r": 7, "a": 6,
                   "N_S_monomials": 1155302, "H_3_12": H_size(3, 12),
                   "note": "the mandatory control: |S| <= |H_{3,12}| = %d ~ 3.7e23, so the Foulkes Gram is out of "
                           "reach even here -- the ground truth is taken by the EVALUATION engine, not the Foulkes "
                           "Gram. This is the concrete demonstration that the Gram route cannot reach an LMR cell." % H_size(3, 12)},
}

out = {"measured_sec_per_H_pass": sec_per_H, "rows": rows, "wall": wall, "lmr": lmr,
       "enumeration_route": "cost Theta(|H_{4,delta}| * n_lam) per cell; the pass is one sweep of H per orbit rep",
       "reduced_route_cost_model": "A_ij = C_S^T beta_S C_S, |S| the Foulkes support; ~ a*|S|^2 + a^2*|S| (integrator note 3)"}
with open(os.path.join(ROOT, "results", "s62_cost.json"), "w") as fh:
    json.dump(out, fh, indent=1)


def humansec(s):
    if s is None:
        return "?"
    if s < 90:
        return f"{s:.1f} s"
    if s < 5400:
        return f"{s/60:.1f} min"
    if s < 200000:
        return f"{s/3600:.1f} h"
    return f"{s/86400:.0f} d"


md = []
md.append("# Session 62 — cost curve\n")
md.append("The single number session 63 needs is `|S|`, the support of the highest-weight vectors in\n"
          "the **Foulkes basis** (block decompositions) — not the weight-space support `n_lam`.\n"
          "`|S| = sum of orbit sizes over the monomials the HWVs touch`; the reduced block\n"
          "`A = C_S^T beta_S C_S` costs `~ a*|S|^2 + a^2*|S|` (integrator note 3).\n")

md.append("\n## Measured — the enumeration route (this session = session 56's pass)\n")
md.append("One pass over `H_{4,delta}` per orbit representative; cost `|H| * n_lam`.\n")
md.append("\n| delta | lambda | a | n_lam | \\|S\\| (Foulkes) | N_S | \\|S\\|/N_S | pass |")
md.append("|---|---|---|---|---|---|---|---|")
for r in rows:
    ratio = Fraction(r["foulkes_support_S"], r["N_S"])
    md.append(f"| {r['delta']} | {tuple(r['lambda'])} | {r['a']} | {r['n_lam']} | "
              f"{r['foulkes_support_S']:,} | {r['N_S']:,} | {float(ratio):.3f} | {humansec(r['pass_total_s'])} |")

md.append(f"\nMeasured pass rate: **{sec_per_H*1e9:.1f} ns per element of H per representative** "
          f"(so one full sweep of `H_{{4,delta}}` costs `{sec_per_H:.2e} s * |H|`).\n")
md.append("Note `|S| = N_S` at every balanced cell (the HWV touches every orbit): the Foulkes support "
          "is essentially the whole module there, and that is the wall.\n")

md.append("\n## The wall — `|H_{4,delta}|` and the projected single-pass time\n")
md.append("\n| delta | \\|H_{4,delta}\\| | one pass (projected) |")
md.append("|---|---|---|")
for w in wall:
    md.append(f"| {w['delta']} | {w['H_4_delta']:,} | {humansec(w['one_pass_s_projected'])} |")
md.append("\n`delta = 5` is already ~a day per length-5 cell and `delta >= 6` is months to years — "
          "s56 measured exactly this. The enumeration route is dead at `delta = 5`; **stopping rule 2 fires** "
          "and session 63 must use the reduced block-intersection route.\n")

md.append("\n## The LMR cells — where `|S|` decides session 63\n")
md.append(f"- **n = 4, delta = 24** (`(65,17,2^7)`, a = 274): `N_S = 156,438,903,314` (s57). "
          f"`|S| <= N_S ~ 1.6e11`; the balanced-cell data (`|S| = N_S`) says it does not shrink materially. "
          f"The reduced 273x273 block is trivial as a determinant; its **entries** cost `~273*|S|^2 ~ 3e24` — out of reach.\n")
md.append(f"- **n = 3, delta = 12** (`(19,7,2^5)`, a = 6, the mandatory control): "
          f"`|H_{{3,12}}| = {H_size(3,12):,}` ~ 3.7e23, so the Foulkes Gram is out of reach **even for the control**. "
          f"Its ground truth is therefore taken by the evaluation engine (`mult_det = a - nullity[E; ev_det]`), "
          f"not the Foulkes Gram — the concrete proof that the Gram route cannot reach an LMR cell.\n")
md.append("\n**Consequence for session 63.** The Foulkes/enumeration Gram cannot reach delta = 24. "
          "The reduced block route is bounded by `|S|`, and `|S|` at the LMR cell is ~1e11, so that route is "
          "out of reach too unless `|S|` collapses — which the balanced-cell measurements say it does not. "
          "Session 63 should report `|S|` at r = 9 as its first deliverable and treat the direct lambda-block "
          "(evaluation) route as the live one, exactly as the n = 3 control is done here.\n")

with open(os.path.join(ROOT, "results", "s62_cost.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print("wrote results/s62_cost.md and results/s62_cost.json")
print(f"sec_per_H = {sec_per_H:.3e}")
for w in wall:
    if w["delta"] in (4, 5, 6, 10, 24):
        print(f"  delta={w['delta']}: |H|={w['H_4_delta']:.3e} one-pass {humansec(w['one_pass_s_projected'])}")
