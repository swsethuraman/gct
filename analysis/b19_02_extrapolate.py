"""HEURISTIC extrapolation of the counting-criterion crossover (report section 6).

Not a proof. Fits K_r(d) = K_inf + c*d^(-alpha) to the measured local exponents
and integrates d log(r/A)/d log d = K_r - K_A. Its only purpose is to be checked
against the four-variable case, where the true first-equation degree (320112)
is known, so that the procedure's reliability can be measured.
"""
import json, math, sys
from pathlib import Path

def fit(rows, K_inf, K_A, label):
    pts = []
    for a, b in zip(rows, rows[1:]):
        K_r = (b["r"] / a["r"] - 1) * b["d"]
        pts.append((b["d"], K_r))
    (d1, k1), (d2, k2) = pts[-4], pts[-1]
    alpha = math.log((k1 - K_inf) / (k2 - K_inf)) / math.log(d2 / d1)
    c = (k2 - K_inf) * d2 ** alpha
    d0 = rows[-1]["d"]
    L = math.log(rows[-1]["r"] / rows[-1]["A"])
    # d log(r/A)/d log d = (K_inf - K_A) + c d^-alpha ; integrate from d0
    def logratio(d):
        return L + (K_inf - K_A) * math.log(d / d0) - (c / alpha) * (d ** -alpha - d0 ** -alpha)
    lo, hi = d0, 10.0 ** 40
    if logratio(hi) > 0:
        return {"label": label, "alpha": alpha, "c": c, "crossover": None,
                "note": "no crossover below 1e40 under this fit"}
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if logratio(mid) > 0: lo = mid
        else: hi = mid
    return {"label": label, "K_inf": K_inf, "K_A": K_A, "alpha": alpha, "c": c,
            "fit_points": pts[-4:], "crossover_estimate": hi,
            "log10_crossover": math.log10(hi)}

out = Path(sys.argv[1]); res = {}
for n, K_inf, K_A in ((5, 49, 69), (4, 33, 34)):
    rows = json.load(open(f"results/b19_02/combined_n{n}.json"))
    res[f"n={n}"] = fit(rows, K_inf, K_A, f"n={n}")
res["four_variable_truth"] = 320112
res["overshoot_factor_in_control"] = (res["n=4"]["crossover_estimate"] / 320112
                                      if res["n=4"].get("crossover_estimate") else None)
res["status"] = "HEURISTIC, NOT PROVED"
out.write_text(json.dumps(res, indent=1) + "\n")
print(json.dumps(res, indent=1))
