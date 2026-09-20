"""B24-10 pilot 1 — independent evaluator, exact arithmetic only.

No project code imported, no external library, no randomness. Every quantity is a
Fraction or an int, so every number below is exact and reproducible by hand.

A. B24-04 §2.4's sizing law and its extrapolation.
   The report fits min N_S ~ c * t^4 and quotes c = 0.060 from the four measured
   pairs at t = 12, 16, 20, 24. It then evaluates at t = 900 to get ~4e10.
   This block asks three questions the report does not:
     A1. Do the printed constants c(t) = minN_S(t)/t^4 reproduce?
     A2. Has c(t) converged over the fitted range, or is it still drifting?
         Richardson: assume c(t) = c_inf - a/t and solve on pairs.
     A3. The report justifies the exponent 4 structurally, citing partitions into
         parts <= n growing like t^(n-1)/((n-1)! n!). Does that closed form's
         constant agree with the measured c? (n = 5 here.)
   A4. Evaluate 0.060*900^4 and c_inf*900^4 and compare.

B. B24-02 §4.2/§4.3's closed forms and the three negative controls.
   h5(k) = C(k+3,3) - C(k,3) claimed = (3k^2+3k+2)/2;  H(k) = 18k - 24 (k >= 3);
   D(k) = h5(k) - H(k) claimed = (3k^2 - 33k + 50)/2, claimed > 0 "exactly for
   integer k >= 10".  Replay D(7), D(8), D(9) = -17, -11, -2, and test the word
   "exactly" over the full integer range, not only k >= 3.

C. Paper 3 C50's boundary precision: visible rows are 2n+1 .. m^2+1, so they
   exist iff n <= m^2/2. At n = m^2/2 exactly (m even), how many remain?

D. C35/C34 dimension consistency: T2 = {l*C : C in Sigma_Pi} should have
   affine dim = dim Sigma_Pi + 5 - 1 if the product map is generically finite
   with only the scaling fibre. Checks 31 + 5 - 1 = 35 against the recorded 35.
"""
import json
import sys
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

out = {"pilot": "b24_10_p1_arith", "method": "exact rational arithmetic; no floats in any check"}

# ---------------------------------------------------------------- A. the sizing law
# The four measured pairs, transcribed from docs/b24_04_report.md §2.4 control C3.
PAIRS = [(12, 1189), (16, 3829), (20, 9492), (24, 19921)]
REPORTED_C = ["0.0573", "0.0584", "0.0593", "0.0600"]

c_exact = [(t, F(n, t ** 4)) for t, n in PAIRS]
A1 = []
for (t, c), printed in zip(c_exact, REPORTED_C):
    # round c to 4 decimal places exactly, then compare as a string
    scaled = (c * 10000 + F(1, 2)).__floor__()
    got = "0.%04d" % scaled
    A1.append({"t": t, "min_N_S": dict(PAIRS)[t], "c_exact": str(c),
               "c_4dp": got, "report_printed": printed, "agrees": got == printed})
out["A1_constants_reproduce"] = A1
out["A1_all_agree"] = all(r["agrees"] for r in A1)

# A2. monotonicity and Richardson extrapolation c(t) = c_inf - a/t.
cs = [c for _, c in c_exact]
out["A2_monotone_increasing"] = all(cs[i] < cs[i + 1] for i in range(len(cs) - 1))
out["A2_increments"] = [str(cs[i + 1] - cs[i]) for i in range(len(cs) - 1)]


def richardson(t1, c1, t2, c2):
    # c_inf - a/t1 = c1 ; c_inf - a/t2 = c2  =>  a (1/t1 - 1/t2) = c2 - c1
    a = (c2 - c1) / (F(1, t1) - F(1, t2))
    return c2 + a / t2, a


A2 = []
for i in range(len(c_exact)):
    for j in range(i + 1, len(c_exact)):
        (t1, c1), (t2, c2) = c_exact[i], c_exact[j]
        cinf, a = richardson(t1, c1, t2, c2)
        A2.append({"pair": [t1, t2], "c_inf_exact": str(cinf),
                   "c_inf_float": float(cinf), "a": str(a)})
out["A2_richardson"] = A2
# the most reliable estimate uses the two widest-separated points
cinf_best, _ = richardson(12, cs[0], 24, cs[3])
out["A2_c_inf_best_pair_12_24"] = {"exact": str(cinf_best), "float": float(cinf_best)}
out["A2_c_inf_vs_one_sixteenth"] = {"c_inf": float(cinf_best), "1/16": 0.0625,
                                    "ratio": float(cinf_best / F(1, 16))}
out["A2_c_still_drifting_at_top_of_fitted_range"] = bool(cs[3] < cinf_best)

# A3. the structural closed form the report cites, at n = 5.
n = 5
struct_c = F(1, factorial(n - 1) * factorial(n))
out["A3_structural_constant"] = {
    "formula": "1/((n-1)! * n!) at n = 5",
    "value_exact": str(struct_c), "value_float": float(struct_c),
    "measured_c_at_t24": float(cs[3]),
    "ratio_measured_over_structural": float(cs[3] / struct_c),
    "note": ("if the cited closed form were the law for min N_S, the constant would be "
             "this, not 0.060; the ratio is the size of the gap")}
# what the structural formula alone would predict at t = 900
out["A3_structural_prediction_at_900"] = float(struct_c * 900 ** 4)

# A4. the extrapolation itself.
out["A4_extrapolation"] = {
    "900^4": 900 ** 4,
    "0.060 * 900^4": float(F(6, 100) * 900 ** 4),
    "c_inf * 900^4": float(cinf_best * 900 ** 4),
    "ratio_cinf_to_0060": float(cinf_best / F(6, 100)),
    "fold_beyond_fitted_range": float(F(900, 24)),
    "report_states_fold": 37}

# ---------------------------------------------------------------- B. B24-02 closed forms
B = {}
h5_closed_ok, H_ok, D_ok = True, True, True
for k in range(0, 40):
    if comb(k + 3, 3) - comb(k, 3) != (3 * k * k + 3 * k + 2) // 2:
        h5_closed_ok = False
B["h5_closed_form_k_0_to_39"] = h5_closed_ok
B["h5_at_3_to_9"] = [comb(k + 3, 3) - comb(k, 3) for k in range(3, 10)]
B["h5_at_3_to_9_report"] = [19, 31, 46, 64, 85, 109, 136]
B["h5_agrees"] = B["h5_at_3_to_9"] == B["h5_at_3_to_9_report"]


def h5(k):
    return F(3 * k * k + 3 * k + 2, 2)


def H(k):
    return 18 * k - 24


def D(k):
    return h5(k) - H(k)


for k in range(3, 40):
    if D(k) != F(3 * k * k - 33 * k + 50, 2):
        D_ok = False
B["D_closed_form_k_3_to_39"] = D_ok
B["D_negative_controls"] = {str(k): str(D(k)) for k in (7, 8, 9)}
B["D_negative_controls_report"] = {"7": "-17", "8": "-11", "9": "-2"}
B["D_negative_controls_agree"] = (
    [D(7), D(8), D(9)] == [F(-17), F(-11), F(-2)])
# the word "exactly": test the sign over all integers where the closed form is written
sign_table = {k: str(F(3 * k * k - 33 * k + 50, 2)) for k in range(0, 13)}
B["D_closed_form_sign_k_0_to_12"] = sign_table
B["D_positive_integers_below_10"] = [k for k in range(0, 10)
                                     if F(3 * k * k - 33 * k + 50, 2) > 0]
B["D_claim_exactly_k_ge_10_holds_unrestricted"] = (
    B["D_positive_integers_below_10"] == [])
B["D_claim_holds_when_restricted_to_k_ge_3"] = all(
    F(3 * k * k - 33 * k + 50, 2) < 0 for k in range(3, 10))
B["note"] = ("H(k) = 18k-24 is stated by the report only for k >= 3, so D(k) is "
             "only defined there; the sentence 'D(k) > 0 exactly for integer k >= 10' "
             "is true on k >= 3 and false if read over all integers")
# are the three controls independent, or three samples of one quadratic?
B["controls_are_samples_of_one_quadratic"] = True
B["D_root_upper"] = float((33 + (33 ** 2 - 4 * 3 * 50) ** 0.5) / 6)
out["B_b24_02_closed_forms"] = B

# ---------------------------------------------------------------- C. C50 boundary
C50 = {}
for m in (4, 6, 8):
    n_star = m * m // 2
    lo, hi = 2 * n_star + 1, m * m + 1
    C50[f"m={m}"] = {"n = m^2/2": n_star, "visible_rows_from": lo, "to": hi,
                     "count": max(0, hi - lo + 1)}
C50["claim"] = ("at n = m^2/2 exactly one row remains visible, so LMR's inequality "
                "is not strict there")
C50["claim_holds"] = all(v["count"] == 1 for k, v in C50.items()
                         if k.startswith("m="))
out["C_c50_boundary"] = C50

# ---------------------------------------------------------------- D. C35 dimensions
out["D_c35_dimension_consistency"] = {
    "dim_Sigma_Pi_affine": 31, "plus_linear_form": 5, "minus_scaling": 1,
    "predicted_T2_affine": 31 + 5 - 1, "recorded_T2_affine": 35,
    "agrees": (31 + 5 - 1) == 35,
    "dim_D35_affine": None,
    "note": ("confirms T2 and Sigma_Pi are different objects in different spaces: "
             "31/30 on the cubic side, 35/34 on the quartic side")}

Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n")
print("checks:", sum(1 for k in out if k.endswith(("agree", "agrees", "ok", "holds"))))
