"""B21-10 pilot 1 — independent evaluator for O1 (Theorem A of B20-01 vs. its own control).

This script imports NO project code. It takes as DATA only the 60 raw runner outputs that
B20-01 pilot 2 recorded (`F_k[name][k].values_u1_to_5` and the S_3 stage), pinned by the sha256
of the committed `results/b20_01/p2_reduction.json`, and re-derives everything downstream in
code written here: modular inverse, Vandermonde solve, the normalisation, the S_3 sign.

It answers three questions and nothing else.

  Q1  Is the degree-11/degree-12 extraction itself right?  (Recompute c_8..c_12 from the raw
      node values; compare with the JSON's coefficients.)
  Q2  Is the disagreement with the sealed rows a single normalising factor, and which one?
      Test  computed == det(g)^8 * sealed  for all six, and  sealed == det(g)^{-4} * (sum F_k).
  Q3  Corollary A.1: does the four-node odd extraction (u = +-1, +-2) really return the
      degree-12 value as well?  (Nullspace of the 4x5 node matrix, exact over Z.)

It also recomputes the two Weyl dimensions that C9 rests on, by the hook-content formula.

No runner evaluation is performed.  No producer script is executed or imported.
"""
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

P = 524287                     # the prime every recorded residue lives in
PIN = "6aa3e283f5d0bf39515656dc16375104530a8d651d2b809973c8028083beb812"

SEALED_D11 = {"q3": 86170, "q7": 71919, "n02": 226580}
SEALED_D12 = {"q3": 376209, "q7": 469277, "n02": 41046}
ORDER = ["q3", "q7", "n02"]
NODES5 = [1, 2, 3, 4, 5]
DEGREES = [8, 9, 10, 11, 12]

out = {"pilot": "b21_10_p1_theoremA_factor", "prime": P, "checks": {}, "inputs": {}}


# ---------------------------------------------------------------- my own linear algebra
def inv(x):
    return pow(int(x) % P, P - 2, P)


def solve_mod(rows, rhs):
    """Unique solution of rows @ x = rhs over F_P, by my own Gauss-Jordan.  Asserts squareness."""
    n = len(rows)
    A = [[int(v) % P for v in r] + [int(b) % P] for r, b in zip(rows, rhs)]
    for col in range(n):
        p = next((i for i in range(col, n) if A[i][col]), None)
        assert p is not None, "singular"
        A[col], A[p] = A[p], A[col]
        iv = inv(A[col][col])
        A[col] = [(v * iv) % P for v in A[col]]
        for i in range(n):
            if i != col and A[i][col]:
                f = A[i][col]
                A[i] = [(v - f * w) % P for v, w in zip(A[i], A[col])]
    return [A[i][n] for i in range(n)]


def extract(values, nodes=NODES5, degrees=DEGREES):
    """c_d with values[i] == sum_d c_d * nodes[i]^d (mod P)."""
    rows = [[pow(t, d, P) for d in degrees] for t in nodes]
    sol = solve_mod(rows, values)
    return dict(zip(degrees, sol))


# ---------------------------------------------------------------- input, pinned by hash
src = Path(sys.argv[1]).resolve()
raw = src.read_bytes()
got = hashlib.sha256(raw).hexdigest()
out["inputs"]["p2_reduction.json"] = {
    "path_read": str(src), "sha256": got, "bytes": len(raw),
    "expected_sha256": PIN, "pin_matches": got == PIN,
    "provenance": "git show 878258f295dd5a6b306137fadaab816ce0deb3df:results/b20_01/p2_reduction.json",
    "cross_check": "equals the value tabulated in b20_01_report.md section 11.7",
}
assert got == PIN, "input hash does not match the pin: %s" % got
d = json.loads(raw)

detg = int(d["slice_form"]["det_g_mod_P"])
detg4_recorded = int(d["slice_form"]["det_g4"])
out["checks"]["det_g4_recomputed"] = {
    "det_g_mod_P": detg,
    "det_g_to_the_4": pow(detg, 4, P),
    "recorded": detg4_recorded,
    "agree": pow(detg, 4, P) == detg4_recorded,
}
d4 = pow(detg, 4, P)
d8 = pow(detg, 8, P)
d4inv = inv(d4)


# ---------------------------------------------------------------- Q1: redo the extraction
q1 = {}
sumF = {}
top = {}
for name in ORDER:
    per_k = {}
    s = 0
    tops = set()
    for k in ("0", "1", "2"):
        e = d["F_k"][name][k]
        vals = [int(v) for v in e["values_u1_to_5"]]
        mine = extract(vals)
        theirs = {int(kk): int(vv) for kk, vv in e["coefficients"].items()}
        per_k[k] = {
            "values_u1_to_5": vals,
            "my_c11": mine[11], "their_c11": theirs[11], "c11_agree": mine[11] == theirs[11],
            "my_c12": mine[12], "their_c12": theirs[12], "c12_agree": mine[12] == theirs[12],
            "my_all_coefficients": {str(dd): mine[dd] for dd in DEGREES},
        }
        s = (s + mine[11]) % P
        tops.add(mine[12])
    assert len(tops) == 1, "top not equal across k for %s" % name
    sumF[name] = s
    top[name] = tops.pop()
    q1[name] = {"per_k": per_k, "my_sum_F_k": s, "my_top": top[name],
                "my_top_equal_across_k": True}
out["checks"]["Q1_extraction_reproduced"] = q1
out["checks"]["Q1_all_coefficients_agree"] = all(
    v["c11_agree"] and v["c12_agree"] for n in q1 for v in q1[n]["per_k"].values())


# ---------------------------------------------------------------- Q2: which normalisation
q2 = {"per_comparison": {}, "ratios_computed_over_sealed": {}}
for name in ORDER:
    for fam, mine_val, sealed in (("d11", sumF[name], SEALED_D11[name]),
                                  ("d12", top[name], SEALED_D12[name])):
        key = "%s_%s" % (fam, name)
        producer = (d4 * mine_val) % P                      # det(g)^{+4} * slice value
        corrected = (d4inv * mine_val) % P                  # det(g)^{-4} * slice value
        q2["per_comparison"][key] = {
            "slice_value": mine_val,
            "sealed": sealed,
            "producer_recipe_det_g4_times": producer,
            "corrected_recipe_det_g_minus4_times": corrected,
            "producer_matches_sealed": producer == sealed,
            "corrected_matches_sealed": corrected == sealed,
        }
        q2["ratios_computed_over_sealed"][key] = (producer * inv(sealed)) % P
out["checks"]["Q2_normalisation"] = q2
ratios = set(q2["ratios_computed_over_sealed"].values())
out["checks"]["Q2_all_six_share_one_ratio"] = len(ratios) == 1
out["checks"]["Q2_the_common_ratio"] = sorted(ratios)
out["checks"]["Q2_ratio_equals_det_g_to_the_8"] = (len(ratios) == 1 and ratios == {d8})
out["checks"]["Q2_det_g_to_the_8"] = d8
out["checks"]["Q2_corrected_recipe_reproduces_all_six_sealed_values"] = all(
    v["corrected_matches_sealed"] for v in q2["per_comparison"].values())

# the same statement stated the way Theorem A(i) states it: slice == det(g)^4 * full
out["checks"]["Q2_theorem_A_i_holds_numerically"] = {
    "%s_%s" % (fam, name): (
        (pow(detg, 4, P) * sealed) % P == val
    )
    for name in ORDER
    for fam, val, sealed in (("d11", sumF[name], SEALED_D11[name]),
                             ("d12", top[name], SEALED_D12[name]))
}

# ---------------------------------------------------------------- S_3 control, redone by me
s3 = {}
for name in ORDER:
    e = d["checks"]["S3_control"][name]
    s3[name] = {
        "F1_at_permuted_point": int(e["F1_at_permuted_point"]),
        "my_F2_at_point": q1[name]["per_k"]["1"]["my_c11"],
        "sum_is_zero_mod_P": (int(e["F1_at_permuted_point"]) + q1[name]["per_k"]["1"]["my_c11"]) % P == 0,
        "top_at_permuted_point": int(e["top_at_permuted_point"]),
        "my_top": top[name],
        "top_agrees": int(e["top_at_permuted_point"]) == top[name],
    }
out["checks"]["S3_control_recomputed_against_my_F2"] = s3
out["checks"]["S3_sign_is_minus_one_for_all_three"] = all(v["sum_is_zero_mod_P"] for v in s3.values())


# ---------------------------------------------------------------- Q3: Corollary A.1's cheap variant
# Nodes u = +-1, +-2 ; unknowns c_8..c_12.  Over Q, exactly.
nodes4 = [1, -1, 2, -2]
M = [[Fraction(u) ** dd for dd in DEGREES] for u in nodes4]
# kernel: a degree-<=4 polynomial in u (after dividing by u^8) vanishing at all four nodes
# is a multiple of (u^2-1)(u^2-4) = u^4 - 5u^2 + 4, i.e. (c_8..c_12) = (4, 0, -5, 0, 1).
kern = [Fraction(4), Fraction(0), Fraction(-5), Fraction(0), Fraction(1)]
out["checks"]["Q3_four_node_variant"] = {
    "nodes": nodes4,
    "kernel_vector_c8_to_c12": [str(x) for x in kern],
    "kernel_annihilates_every_node": [
        str(sum(M[i][j] * kern[j] for j in range(5))) for i in range(4)
    ],
    "kernel_is_zero_at_every_node": all(
        sum(M[i][j] * kern[j] for j in range(5)) == 0 for i in range(4)),
    "c11_component_of_kernel": str(kern[3]),
    "c12_component_of_kernel": str(kern[4]),
    "degree_11_is_determined_by_four_nodes": kern[3] == 0,
    "degree_12_is_determined_by_four_nodes": kern[4] == 0,
    "verdict": ("four nodes determine c_9 and c_11 but NOT c_8, c_10, c_12: the kernel has "
                "c_11 = 0 and c_12 = 1, so the degree-12 value is not recoverable"),
}


# ---------------------------------------------------------------- C9: the Weyl dimensions
def schur_dim(lam, n):
    """dim S_lambda(C^n) by the hook-content formula, exact integer arithmetic."""
    lam = [x for x in lam if x > 0]
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    num = 1
    den = 1
    for i, row in enumerate(lam):
        for j in range(row):
            num *= n + j - i                        # content, 0-based j - i
            den *= lam[i] + conj[j] - i - j - 1     # hook: arm + leg + 1, 0-based
    assert num % den == 0
    return num // den


def flag_multicone_dim(u):
    """dim of the multicone over Fl(2,3;U), dim U = u:  (3u-7) + 2."""
    return 3 * u - 5


out["checks"]["C9_weyl_dimensions"] = {
    "S_(4,4,1)_C7": schur_dim([4, 4, 1], 7),
    "S_(4,4,1)_C8": schur_dim([4, 4, 1], 8),
    "S_(4,4,1)_C13": schur_dim([4, 4, 1], 13),
    "S_(2,2)_C5": schur_dim([2, 2], 5),
    "target_dim_F_L_minus1": 70,
    "ratio_17640_over_70": schur_dim([4, 4, 1], 7) // 70,
    "ratio_55440_over_70": schur_dim([4, 4, 1], 8) // 70,
    "flag_multicone_dim_m7": flag_multicone_dim(7),
    "flag_multicone_dim_m8": flag_multicone_dim(8),
    "flag_multicone_dim_m13": flag_multicone_dim(13),
    "transversality_full_Gprime_slice_in_S_hat": {
        "ambient_dim_S_hat": flag_multicone_dim(13),
        "group_dim": 17,
        "required_slice_image_dim": flag_multicone_dim(13) - 17,
        "m_needed_if_slice_image_is_flag_multicone_over_V": min(
            m for m in range(2, 14) if 17 + flag_multicone_dim(m) >= flag_multicone_dim(13)),
        "producer_m": 7,
    },
    "transversality_full_Gprime_slice_in_Wprime_cubed": {
        "ambient_dim_Wprime_cubed": 39,
        "group_dim": 17,
        "m_needed": min(m for m in range(2, 14) if 17 + 3 * m >= 39),
        "producer_m": 7,
    },
    "transversality_levi_only": {
        "m_needed_in_S_hat": min(
            m for m in range(2, 14) if 7 + flag_multicone_dim(m) >= flag_multicone_dim(13)),
        "m_needed_in_Wprime_cubed": min(m for m in range(2, 14) if 7 + 3 * m >= 39),
        "producer_m": 9,
    },
}

print(json.dumps(out, indent=1))
dest = Path(sys.argv[2]) if len(sys.argv) > 2 else None
if dest:
    dest.write_text(json.dumps(out, indent=1) + "\n")
