"""B21-10 pilot 2 — replay of the three G8 certificates, and the two hand computations.

Imports no project code.  Everything it needs is pinned by sha256 and passed on the command
line as a directory of committed bytes extracted with `git show`.

  A. G8 certificates (B20-01 pilot 1's three emitted files).  For each: the file's own sha256
     against the table in b20_01_report.md section 11.7; the `ordering_hash` recomputed HERE
     under the scheme the file states; the shipped blocks against the report's section 3.1
     prose transcription; the shipped values against the sealed values quoted in section 3.
  B. Lemma 6.3 (B20-02 section 6.2): every dimension in the two incidence counts, recomputed.
  C. Lemma 6.1 / the certified rank profiles: rho_j(k) from the alternating sum, checked
     against the numbers B20-02 and B20-02b report.

No modular arithmetic, no linear algebra, no runner evaluation.
"""
import hashlib
import json
import sys
from pathlib import Path

D = Path(sys.argv[1]).resolve()
out = {"pilot": "b21_10_p2_certificates_and_lemmas", "checks": {}, "inputs": {}}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


# ------------------------------------------------------------------ A. the G8 certificates
PIN = {                                    # b20_01_report.md section 11.7
    "q3_definition.json": "ac93ff59113a1aca83a3a8a2d5a2cd90b2de216be70c793ea5f242c887e8428e",
    "q7_definition.json": "07d066b8f6aada7472e892801cbfd6f1a2708a3d592e18592d9996341af3a252",
    "n02_ordering_hash.json": "34900ea600da8b9a20535988f0a0a6cd901d866cd90ae74699e2ba60de845166",
    "n02_definition.json": "ffeead803ebad7510bd68766c364e3f87195b251c32d2032ee9938f4a68fc91b",
}
RECORDED_ORDERING_HASH = {                 # b20_01_report.md section 11.3
    "q3": "ae832e3d7e1dc80befba2e79bd0aa5bc1abe84a2f0b0a6cc9d3c4cdef07f4060",
    "q7": "17b7d324c5af5743e4237ec833556f18b1cf10f1ef430040bea06ece5a4fb17b",
    "n02": "61505bd5a571ace8cfb67b6ae79c66effc5d008ddd9e7794088ee5cf625408b4",
}
# b20_01_report.md section 3.1, transcribed from the PROSE (not from the certificates)
PROSE = {
    "q3": {
        "order": [0, 1, 2, 3],
        "pi": [[[0, 1], [0, 4], [1, 3], [1, 0]], [[0, 0], [0, 3], [1, 2], [1, 1]],
               [[2, 3], [2, 4], [3, 3], [3, 1]], [[2, 2], [2, 1], [3, 0], [3, 2]],
               [[0, 2], [1, 4], [2, 0], [3, 4]]],
        "rho": [[[0, 4], [0, 2], [1, 0], [1, 4]], [[0, 3], [0, 1], [1, 3], [1, 2]],
                [[2, 1], [2, 4], [3, 2], [3, 1]], [[2, 0], [2, 3], [3, 4], [3, 0]],
                [[0, 0], [1, 1], [2, 2], [3, 3]]],
    },
    "q7": {
        "order": [0, 2, 1, 3],
        "pi": [[[0, 1], [0, 3], [2, 3], [2, 0]], [[0, 4], [0, 0], [2, 4], [2, 2]],
               [[1, 1], [1, 4], [3, 4], [3, 2]], [[1, 2], [1, 0], [3, 0], [3, 1]],
               [[0, 2], [2, 1], [1, 3], [3, 3]]],
        "rho": [[[0, 4], [0, 1], [2, 2], [2, 0]], [[0, 3], [0, 0], [2, 3], [2, 4]],
                [[1, 3], [1, 0], [3, 3], [3, 2]], [[1, 2], [1, 4], [3, 0], [3, 4]],
                [[0, 2], [2, 1], [1, 1], [3, 1]]],
    },
}
# b20_01_report.md section 3, sealed values quoted in the PROSE
SEALED_VALUES = {
    "q3": {"P6": [260975, 509003, 336756, 260012, 342025], "P7_S0": 185448},
    "q7": {"P6": [301718, 423302, 275526, 317892, 384], "P7_S0": 288291},
}

certs = {}
for fn, pin in PIN.items():
    p = D / fn
    got = sha(p)
    out["inputs"][fn] = {"sha256": got, "pin": pin, "pin_matches": got == pin,
                         "bytes": p.stat().st_size}
    certs[fn] = json.loads(p.read_bytes())

A = {}
for name in ("q3", "q7"):
    c = certs["%s_definition.json" % name]
    four = {
        "hand_plan_column_order": c["hand_plan_column_order"],
        "hand_plan_column_order_transposed": c["hand_plan_column_order_transposed"],
        "pi_ordered_blocks": c["pi_ordered_blocks"],
        "rho_ordered_blocks": c["rho_ordered_blocks"],
    }
    mine = hashlib.sha256(canon(four)).hexdigest()
    A[name] = {
        "ordering_hash_recorded": c["ordering_hash"],
        "ordering_hash_recomputed_here": mine,
        "ordering_hash_replays": mine == c["ordering_hash"],
        "matches_report_11_3": c["ordering_hash"] == RECORDED_ORDERING_HASH[name],
        "blocks_equal_report_3_1_prose": (c["pi_ordered_blocks"] == PROSE[name]["pi"]
                                          and c["rho_ordered_blocks"] == PROSE[name]["rho"]),
        "orders_equal_report_3_1_prose": (c["hand_plan_column_order"] == PROSE[name]["order"]
                                          and c["hand_plan_column_order_transposed"] == PROSE[name]["order"]),
        "values_equal_report_3_prose": (c["values"]["P6_points_0_to_4"] == SEALED_VALUES[name]["P6"]
                                        and c["values"]["P7_S0_point0_t0"] == SEALED_VALUES[name]["P7_S0"]),
        "replay_flags_in_certificate": {
            "P6_match": c["values_replayed_here"]["P6_match"],
            "P7_match": c["values_replayed_here"]["P7_match"],
            "replayed_equals_sealed_P6": (c["values_replayed_here"]["P6_points_0_to_4"]
                                          == c["values_replayed_here"]["sealed_P6"]),
        },
        "values": c["values"],
    }

# n02: its ordering hash must come from the SEALED n02_definition.json, not from the sibling
n02d = certs["n02_definition.json"]
n02h = certs["n02_ordering_hash.json"]
four_n02 = {
    "hand_plan_column_order": n02d["hand_plan_column_order"],
    "hand_plan_column_order_transposed": n02d["hand_plan_column_order_transposed"],
    "pi_ordered_blocks": n02d["pi_ordered_blocks"],
    "rho_ordered_blocks": n02d["rho_ordered_blocks"],
}
mine_n02 = hashlib.sha256(canon(four_n02)).hexdigest()
A["n02"] = {
    "ordering_hash_recorded": n02h["ordering_hash"],
    "ordering_hash_recomputed_here_from_sealed_n02_definition": mine_n02,
    "ordering_hash_replays": mine_n02 == n02h["ordering_hash"],
    "matches_report_11_3": n02h["ordering_hash"] == RECORDED_ORDERING_HASH["n02"],
    "sealed_certificate_pin_in_file": n02h["sealed_certificate"]["sha256"],
    "sealed_pin_matches_file_on_disk": (n02h["sealed_certificate"]["sha256"]
                                        == out["inputs"]["n02_definition.json"]["sha256"]),
    "hand_plan_orders": [n02d["hand_plan_column_order"], n02d["hand_plan_column_order_transposed"]],
    "checks_recorded_in_file": n02h["checks"],
}
out["checks"]["A_certificates"] = A
out["checks"]["A_all_three_ordering_hashes_replay"] = all(
    A[n]["ordering_hash_replays"] and A[n]["matches_report_11_3"] for n in ("q3", "q7", "n02"))
out["checks"]["A_q3_q7_data_agrees_with_report_prose"] = all(
    A[n]["blocks_equal_report_3_1_prose"] and A[n]["orders_equal_report_3_1_prose"]
    and A[n]["values_equal_report_3_prose"] for n in ("q3", "q7"))
out["checks"]["A_all_input_pins_match"] = all(v["pin_matches"] for v in out["inputs"].values())


# ------------------------------------------------------------------ B. Lemma 6.3 arithmetic
def gr(k, n):
    """dim Gr(k, n)."""
    return k * (n - k)


def z_rank_cone(r, m=4, n=4):
    """dim of the affine cone {rank <= r} of m x n matrices."""
    return r * (m + n - r)


B = {
    "dim_Mat4": 16,
    "dim_P15": 15,
    "dim_Z2_affine_cone": z_rank_cone(2),
    "dim_PZ2": z_rank_cone(2) - 1,
    "dim_Z3_affine_cone": z_rank_cone(3),
    "dim_X_det_projective": z_rank_cone(3) - 1,
    "dim_Gr_5_16": gr(5, 16),
    "step_c_incidence_Psi": {
        "base": "smooth locus of X_det, dimension",
        "base_dim": z_rank_cone(3) - 1,
        "fibre": "Gr(4,14): five-dim subspaces of the 15-dim T_A containing the line C.A",
        "fibre_dim": gr(4, 14),
        "dim_Psi": (z_rank_cone(3) - 1) + gr(4, 14),
        "dim_Gr_5_16": gr(5, 16),
        "not_dominant": (z_rank_cone(3) - 1) + gr(4, 14) < gr(5, 16),
    },
    "step_d_incidence_Phi": {
        "base": "P(Z_2), dimension",
        "base_dim": z_rank_cone(2) - 1,
        "fibre": "Gr(4,15): five-dim subspaces of C^16 containing the line C.A",
        "fibre_dim": gr(4, 15),
        "dim_Phi": (z_rank_cone(2) - 1) + gr(4, 15),
        "equals_dim_Gr_5_16": (z_rank_cone(2) - 1) + gr(4, 15) == gr(5, 16),
        "generic_fibre_dim": ((z_rank_cone(2) - 1) + gr(4, 15)) - gr(5, 16),
        "projective_dimension_theorem_nonempty": (z_rank_cone(2) - 1) + 4 >= 15,
    },
    "step_e": {
        "dim_V_JF_affine": 1,
        "ht_JF": 5 - 1,
        "grade_JF_given_T2": 4,
        "n_minus_g": 5 - 4,
        "H_j_vanish_for_j_greater_than": 1,
    },
}
out["checks"]["B_lemma_6_3"] = B
out["checks"]["B_all_dimension_claims_reproduce"] = (
    B["dim_PZ2"] == 11 and B["dim_X_det_projective"] == 14 and B["dim_Gr_5_16"] == 55
    and B["step_c_incidence_Psi"]["fibre_dim"] == 40 and B["step_c_incidence_Psi"]["dim_Psi"] == 54
    and B["step_c_incidence_Psi"]["not_dominant"]
    and B["step_d_incidence_Phi"]["fibre_dim"] == 44 and B["step_d_incidence_Phi"]["dim_Phi"] == 55
    and B["step_d_incidence_Phi"]["generic_fibre_dim"] == 0
    and B["step_d_incidence_Phi"]["projective_dimension_theorem_nonempty"])


# ------------------------------------------------------------------ C. Lemma 6.1 rank profiles
def binom(n, k):
    if k < 0 or n < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def dim_S(m, N):
    return binom(m + N - 1, N - 1) if m >= 0 else 0


def dim_K(j, k, N):
    return binom(N, j) * dim_S(k - 3 * j, N)


def rho(j, k, N):
    return sum((-1) ** (i - j) * dim_K(i, k, N) for i in range(j, N + 1))


C = {
    "N5_rho_1_k3_to_9": [rho(1, k, 5) for k in range(3, 10)],
    "N5_certified_profile_at_P2_pencil": [5, 25, 75, 165, 299, 475, 695],
    "N5_deficiency_generic_minus_pencil": [rho(1, k, 5) - v for k, v in
                                           zip(range(3, 10), [5, 25, 75, 165, 299, 475, 695])],
    "N5_rho_2_8": rho(2, 8, 5),
    "N5_dim_K2_8": dim_K(2, 8, 5),
    "N5_dim_K3_8": dim_K(3, 8, 5),
    "N5_padding_rank_d2_8_reported": 146,
    "N5_padding_H2_8_reported": 4,
    "N5_padding_H2_8_recomputed": rho(2, 8, 5) - 146,
    "N16_dim_K2_8": dim_K(2, 8, 16),
    "N16_dim_K3_8": dim_K(3, 8, 16),
    "N16_rho_2_8": rho(2, 8, 16),
    "N16_dim_K1_8": dim_K(1, 8, 16),
    "N16_dim_K1_5": dim_K(1, 5, 16),
    "N16_dim_S5": dim_S(5, 16),
    "N16_reported_D8_rows_cols": [16320, 248064],
    "N16_reported_M5_rows_cols": [2176, 15504],
    "N16_H2_det4_recomputed": rho(2, 8, 16) - 15660,
    "N16_H2_pad_recomputed": rho(2, 8, 16) - 13490,
    "N16_H2_reported": [660, 2830],
}
C["N5_rho_1_matches_generic_maxima"] = C["N5_rho_1_k3_to_9"] == [5, 25, 75, 175, 300, 480, 710]
C["N5_rho_2_8_is_150"] = C["N5_rho_2_8"] == 150
C["N5_padding_H2_consistent"] = C["N5_padding_H2_8_recomputed"] == C["N5_padding_H2_8_reported"]
C["N16_rho_2_8_is_16320"] = C["N16_rho_2_8"] == 16320
C["N16_matrix_sizes_reproduce"] = (C["N16_dim_K2_8"] == 16320 and C["N16_dim_K1_8"] == 248064
                                   and C["N16_dim_K1_5"] == 2176 and C["N16_dim_S5"] == 15504)
C["N16_H2_reproduce"] = [C["N16_H2_det4_recomputed"], C["N16_H2_pad_recomputed"]] == C["N16_H2_reported"]
out["checks"]["C_rank_profiles"] = C

# ------------------------------------------------------------------ summary counts, emitted
flat = []


def walk(prefix, o):
    if isinstance(o, bool):
        flat.append((prefix, o))
    elif isinstance(o, dict):
        for k, v in o.items():
            walk(prefix + "." + str(k), v)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(prefix + "[%d]" % i, v)


walk("checks", out["checks"])
walk("inputs", out["inputs"])
out["boolean_checks_total"] = len(flat)
out["boolean_checks_true"] = sum(1 for _, v in flat if v)
out["boolean_checks_false"] = [k for k, v in flat if not v]
out["status"] = "done"

print(json.dumps(out, indent=1))
print("CHECKS %d/%d TRUE" % (out["boolean_checks_true"], out["boolean_checks_total"]))
if len(sys.argv) > 2:
    Path(sys.argv[2]).write_text(json.dumps(out, indent=1) + "\n")
