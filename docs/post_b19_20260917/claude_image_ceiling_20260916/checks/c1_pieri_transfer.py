"""c1_pieri_transfer.py -- the one bounded check of work/claude_image_ceiling_20260916.

(a) Recompute a_3(d, mu) = mult of S_mu(C^5) in Sym^d(Sym^3 C^5) for d = 5, 6 (multiset DP over
    the 35 cubic monomials + Weyl alternant), with the dimension control
    sum_mu a_3 * dim S_mu = C(34 + d, d).
(b) Recompute T(d, lambda) = sum_{mu : lambda/mu horizontal d-strip} a_3(d, mu) for every five-row
    lambda |- 4d in the inherited census and compare with its padding_source_raw.
(c) Weight-space dimensions N_S(mu) of Sym^6(Sym^3 C^5) at length-5 dominant weights with a_3 > 0;
    match against the batch-13 residue values {3988, 4028, 4456}; list d = 6 five-row cells whose
    Pieri range contains a residue weight.
(d) Print the Pieri range of (8,4,4,4,4).

Pure Python, no BLAS. Writes results/c1_pieri_transfer.json (relative to the cwd it is run from).
"""
import itertools
import json
import sys
import time
from math import comb
from pathlib import Path

T0 = time.perf_counter()
ROOT = Path(__file__).resolve().parents[3]  # .../gct-gpt
CENSUS = ROOT / "Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json"
OUT = Path("results/c1_pieri_transfer.json")
RESIDUE = {3988, 4028, 4456}
N = 5
RHO = (4, 3, 2, 1, 0)

CUBICS = [b for b in itertools.product(range(4), repeat=N) if sum(b) == 3]
assert len(CUBICS) == 35


def sym_weights(d):
    """Weight multiplicities of Sym^d(Sym^3 C^5): multisets of size d of cubic monomials."""
    states = {(0, (0,) * N): 1}
    for b in CUBICS:
        new = {}
        for (k, w), c in states.items():
            for j in range(0, d - k + 1):
                key = (k + j, tuple(w[i] + j * b[i] for i in range(N)))
                new[key] = new.get(key, 0) + c
        states = new
    return {w: c for (k, w), c in states.items() if k == d}


def perms_with_sign():
    out = []
    for p in itertools.permutations(range(N)):
        inv = sum(1 for i in range(N) for j in range(i + 1, N) if p[i] > p[j])
        out.append((p, -1 if inv % 2 else 1))
    return out


PERMS = perms_with_sign()


def alternant(wt, mu):
    """Multiplicity of S_mu in a module with weight-multiplicity dict wt (Weyl character formula)."""
    total = 0
    for p, sgn in PERMS:
        key = tuple(mu[i] + RHO[i] - RHO[p[i]] for i in range(N))
        total += sgn * wt.get(key, 0)
    return total


def dim_schur(mu):
    num = 1
    den = 1
    for i in range(N):
        for j in range(i + 1, N):
            num *= (mu[i] - mu[j] + j - i)
            den *= (j - i)
    return num // den


def dominant_weights(total):
    out = []
    for mu in itertools.product(range(total + 1), repeat=N):
        if sum(mu) == total and all(mu[i] >= mu[i + 1] for i in range(N - 1)):
            out.append(mu)
    return out


def horizontal_strip_mus(lam, d):
    """All mu |- |lam| - d with lam/mu a horizontal strip (interlacing)."""
    lam = list(lam) + [0]
    ranges = [range(lam[i + 1], lam[i] + 1) for i in range(N)]
    target = sum(lam) - d
    return [mu for mu in itertools.product(*ranges) if sum(mu) == target]


report = {"script": "c1_pieri_transfer.py", "d": {}, "census_file": str(CENSUS)}
census = json.load(open(CENSUS))
rows = {(r["d"], tuple(r["weight"])): r for r in census["rows"]}

for d in (5, 6):
    t = time.perf_counter()
    wt = sym_weights(d)
    a3 = {}
    dimsum = 0
    for mu in dominant_weights(3 * d):
        m = alternant(wt, mu)
        assert m >= 0, (mu, m)
        if m:
            a3[mu] = m
            dimsum += m * dim_schur(mu)
    control_ok = (dimsum == comb(34 + d, d))
    five_row = {mu: m for mu, m in a3.items() if mu[4] > 0}
    entry = {
        "seconds_a3": round(time.perf_counter() - t, 3),
        "num_weights_with_a3_positive": len(a3),
        "dimension_control": {"sum_a3_dimS": dimsum, "expected": comb(34 + d, d), "ok": control_ok},
        "length5_weights_a3": {str(list(mu)): m for mu, m in sorted(five_row.items(), reverse=True)},
    }
    # (b) T control against the census for all five-row lambda |- 4d
    mismatches = []
    ncells = 0
    pieri = {}
    for (dd, lam), r in rows.items():
        if dd != d or len(lam) != 5:
            continue
        ncells += 1
        mus = [mu for mu in horizontal_strip_mus(lam, d) if mu in a3]
        T = sum(a3[mu] for mu in mus)
        pieri[lam] = mus
        if T != r["padding_source_raw"]:
            mismatches.append({"lambda": list(lam), "T_recomputed": T, "census_T": r["padding_source_raw"]})
    entry["T_control"] = {"five_row_cells": ncells, "mismatches": mismatches, "all_match": not mismatches}
    if d == 6:
        # (c) residue identification
        ns = {mu: wt[mu] for mu in five_row}
        matched = {str(list(mu)): n for mu, n in ns.items() if n in RESIDUE}
        entry["N_S_length5"] = {str(list(mu)): n for mu, n in sorted(ns.items(), reverse=True)}
        entry["residue_matches"] = matched
        residue_mus = {mu for mu, n in ns.items() if n in RESIDUE}
        hit = {}
        for lam, mus in pieri.items():
            h = [list(mu) for mu in mus if mu in residue_mus]
            if h:
                r = rows[(6, lam)]
                hit[str(list(lam))] = {"residue_mus_in_range": h, "a": r["ambient"], "s": r["symmetric"],
                                       "T": r["padding_source_raw"], "U": r["padding_ceiling"]}
        entry["cells_with_residue_weight_in_pieri_range"] = hit
        # (d)
        lam = (8, 4, 4, 4, 4)
        entry["pieri_range_84444"] = {str(list(mu)): a3.get(mu, 0) for mu in horizontal_strip_mus(lam, 6)}
    report["d"][str(d)] = entry
    print(f"d={d}: a3 weights={len(a3)} control_ok={control_ok} cells={ncells} mismatches={len(mismatches)} "
          f"({entry['seconds_a3']} s)", flush=True)

report["wall_seconds"] = round(time.perf_counter() - T0, 3)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=1) + "\n")
print(json.dumps({k: v for k, v in report["d"]["6"].items() if k in ("residue_matches", "cells_with_residue_weight_in_pieri_range", "pieri_range_84444", "T_control")}, indent=1))
print("wall", report["wall_seconds"], flush=True)
