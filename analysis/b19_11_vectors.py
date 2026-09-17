"""B19-11: regenerate, verify and package the batch-18 sweep vectors.

For one cell id (S01..S19, R01, R02) this script
  1. imports the UNMODIFIED batch-18 sweep script from the B15-06 worktree
     (hash recorded in the output) and rebuilds the exact integer
     highest-weight vector W by the sweep's own construction;
  2. records the monomial ordering that W is expressed in: the explicit list
     of 70 degree-4 exponent vectors (MONS) and, for each of the K basis
     elements, the sorted 5-tuple of MONS indices, plus a SHA-256 of the
     fully expanded ordering;
  3. verifies W exactly over Z against the four simple raising operators,
     recording per operator: source weight, target weight, source and target
     dimensions, operator nonzero count, and an independent nontrivial action
     test (the operator applied to a fixed non-kernel vector is nonzero);
  4. replays the batch-18 certificate: rebuilds every recorded determinant
     and padding point from the recorded integer data (no random numbers)
     and compares the exact values with the recorded ones; compares the
     recorded size data (a, K, max |coeff|, nonzeros, target dims).
Nothing in the B15-06 worktree is modified. Output: one JSON per cell under
results/b19_11/vectors/. Exact integer arithmetic throughout.
"""
import hashlib
import importlib.util
import itertools
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent            # B15-11 worktree
B06 = HERE.parent / "B15-06"
SWEEP_PY = B06 / "analysis" / "b18_06_sweep.py"
SWEEP_DIR = B06 / "results" / "b18_06_sweep"


def load_sweep():
    spec = importlib.util.spec_from_file_location("b18_06_sweep", SWEEP_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def det_form(sw, A):
    """det(sum_k x_k A_k) from the recorded 4x4 array of 5-vectors, no rng."""
    f = {}
    for perm in itertools.permutations(range(4)):
        sgn = (-1) ** sum(1 for x in range(4) for y in range(x + 1, 4) if perm[x] > perm[y])
        term = {(0,) * sw.NV: sgn}
        for r in range(4):
            term = sw.polymul(term, sw.linear(A[r][perm[r]]))
        for e, c in term.items():
            f[e] = f.get(e, 0) + c
    return {e: c for e, c in f.items() if c}


def pad_form(sw, l, N):
    per = {}
    for perm in itertools.permutations(range(3)):
        term = {(0,) * sw.NV: 1}
        for r in range(3):
            term = sw.polymul(term, sw.linear(N[r][perm[r]]))
        for e, c in term.items():
            per[e] = per.get(e, 0) + c
    return sw.polymul(sw.linear(l), per)


def main():
    cid = sys.argv[1]
    outpath = Path(sys.argv[2])
    t0 = time.perf_counter()
    sw = load_sweep()
    lam = sw.CELLS[cid]
    cert_path = SWEEP_DIR / f"{cid}.json"
    cert_bytes = cert_path.read_bytes()
    cert = json.loads(cert_bytes)
    rec = {}
    W, base, ops, dims, K = sw.exact_hwv(lam, record=rec)
    out = {
        "cell": cid, "lambda": list(lam), "d": sw.D, "n_variables": sw.NV,
        "sweep_script": str(SWEEP_PY.relative_to(HERE.parent)),
        "sweep_script_sha256": sha256_bytes(SWEEP_PY.read_bytes()),
        "batch18_certificate": str(cert_path.relative_to(HERE.parent)),
        "batch18_certificate_sha256": sha256_bytes(cert_bytes),
        "conventions": {
            "coefficients": "ordinary c_alpha = [x^alpha] f",
            "raising": "E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j) when alpha_j > 0, extended as a derivation",
            "basis_element": "a multiset of 5 degree-4 monomials in 5 variables, stored as the sorted 5-tuple of indices into MONS; the basis vector is the product of the corresponding coefficients c_alpha",
            "vector_normalisation": "primitive integer vector, first nonzero coordinate positive",
        },
    }
    if W is None:
        out["status"] = "NOT_REACHED_no_exact_hwv"
        out["lift_attempts"] = rec.get("lift_attempts")
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(json.dumps(out, indent=1) + "\n")
        print(json.dumps({"cell": cid, "status": out["status"]}))
        return
    # --- 2. ordering
    mons = [list(m) for m in sw.MONS]
    basis_idx = [list(b) for b in base]
    expanded = json.dumps([[mons[i] for i in b] for b in basis_idx], separators=(",", ":"))
    out["monomial_ordering"] = {
        "MONS_degree4_exponent_vectors_in_order": mons,
        "basis_as_MONS_index_tuples_in_order": basis_idx,
        "weight_space_dim_K": K,
        "expanded_ordering_sha256": sha256_bytes(expanded.encode()),
        "first_basis_element_expanded": [mons[i] for i in basis_idx[0]],
        "last_basis_element_expanded": [mons[i] for i in basis_idx[-1]],
    }
    out["vector_W"] = [int(x) for x in W]
    out["vector_sha256_of_json"] = sha256_bytes(json.dumps(out["vector_W"], separators=(",", ":")).encode())
    # --- 3. verification with the new contract fields
    first_nz = next(i for i, x in enumerate(W) if x)
    ver = {"vector_is_primitive_first_nonzero_positive": W[first_nz] > 0, "operators": []}
    from math import gcd
    g = 0
    for x in W:
        g = gcd(g, abs(x))
    ver["gcd_of_coordinates"] = g
    ver["max_abs_coefficient"] = max(abs(x) for x in W)
    ver["nonzero_coordinates"] = sum(1 for x in W if x)
    all_zero = True
    for i in range(sw.NV - 1):
        op = ops[("down", i + 1, i)]
        tdim = dims[("mid", i + 1, i)]
        target = sw.shift(lam, i, i + 1)
        s_arr = op[0]
        nnz = int(len(s_arr))
        res = sw.apply_exact(op, W, tdim)
        zero = not any(res)
        all_zero = all_zero and zero
        # independent nontrivial action: apply to e_(first basis element) and
        # to the all-ones vector; at least one must be nonzero if op is populated
        e0 = [1] + [0] * (K - 1)
        act0 = sw.apply_exact(op, e0, tdim)
        ones = [1] * K
        act1 = sw.apply_exact(op, ones, tdim)
        ver["operators"].append({
            "operator": f"E_{i + 1},{i + 2}",
            "source_weight": list(lam), "source_dim": K,
            "target_weight": list(target), "target_dim": tdim,
            "operator_nonzero_entries": nnz,
            "residue_on_W_is_zero": zero,
            "residue_nonzero_count": sum(1 for x in res if x),
            "action_on_e0_nonzero_count": sum(1 for x in act0 if x),
            "action_on_all_ones_nonzero_count": sum(1 for x in act1 if x),
            "nontrivial_action_test_passed": nnz > 0 and (any(act0) or any(act1)),
        })
    ver["all_simple_raising_residues_zero"] = all_zero
    ver["all_nontrivial_action_tests_passed"] = all(o["nontrivial_action_test_passed"] for o in ver["operators"])
    out["verification"] = ver
    # --- 4. replay of the recorded certificate
    a_here = sw.weyl_multiplicity(lam)
    rep = {
        "a_recorded": cert.get("a_weyl_alternant"), "a_recomputed": a_here,
        "K_recorded": cert.get("weight_space_dim"), "K_recomputed": K,
        "hwv_max_abs_recorded": cert.get("hwv_max_abs"), "hwv_max_abs_recomputed": ver["max_abs_coefficient"],
        "hwv_nonzeros_recorded": cert.get("hwv_nonzeros"), "hwv_nonzeros_recomputed": ver["nonzero_coordinates"],
        "raising_target_dims_recorded": cert.get("raising_target_dims"),
        "raising_target_dims_recomputed": [o["target_dim"] for o in ver["operators"]],
        "seed_used_recorded": cert.get("seed_used"), "seed_used_here": rec.get("seed_used"),
        "primes_used_recorded": cert.get("primes_used"), "primes_used_here": rec.get("primes_used"),
        "points": [],
    }
    all_match = True
    for kind in ("det_values", "pad_values"):
        for k, entry in enumerate(cert.get(kind, [])):
            pt = entry["point"]
            if pt["kind"] == "det":
                f = det_form(sw, pt["A"])
                rows = [pt["A"][r][c] for r in range(4) for c in range(4)]
                extra = {"block_rank_recomputed": sw.rank_over_Q(rows)}
            else:
                f = pad_form(sw, pt["l"], pt["N"])
                extra = {"all_ten_forms_nonzero": bool(any(pt["l"]) and all(any(pt["N"][r][c]) for r in range(3) for c in range(3)))}
            val = sw.evaluate_exact(W, base, f)
            match = (val == entry["value"])
            all_match = all_match and match
            rep["points"].append({"kind": kind, "index": k, "value_recorded": entry["value"],
                                  "value_recomputed": val, "match": match, **extra})
    rep["all_point_values_match"] = all_match
    rep["size_data_match"] = (rep["a_recorded"] == a_here and rep["K_recorded"] == K and
                              rep["hwv_max_abs_recorded"] == ver["max_abs_coefficient"] and
                              rep["hwv_nonzeros_recorded"] == ver["nonzero_coordinates"] and
                              rep["raising_target_dims_recorded"] == rep["raising_target_dims_recomputed"])
    out["replay"] = rep
    out["status"] = ("REPLAYED_ALL_MATCH" if (all_match and rep["size_data_match"] and all_zero
                                                 and ver["all_nontrivial_action_tests_passed"])
                     else "REPLAY_MISMATCH")
    out["seconds"] = time.perf_counter() - t0
    outpath.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(out, indent=1) + "\n"
    outpath.write_text(txt)
    out_bytes = len(txt.encode())
    print(json.dumps({"cell": cid, "status": out["status"], "K": K,
                      "all_point_values_match": all_match, "size_data_match": rep["size_data_match"],
                      "residues_zero": all_zero, "action_tests": ver["all_nontrivial_action_tests_passed"],
                      "operator_nnz": [o["operator_nonzero_entries"] for o in ver["operators"]],
                      "output_bytes": out_bytes, "seconds": out["seconds"]}))


if __name__ == "__main__":
    main()
