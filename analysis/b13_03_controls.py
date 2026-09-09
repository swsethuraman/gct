"""Preregistered completed controls for the exact reducible membership map."""
import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
import time

import b13_03_exact as e

OUT = Path("results/b13_03")
S4 = Path("results/astra/S4/artifacts")


def event(name, **data):
    print(json.dumps({"stage": name, **data}), flush=True)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


@lru_cache(None)
def weight_count(n, r, degree, weight):
    E = e.exps(n, r)
    @lru_cache(None)
    def rec(start, left, rem):
        if left == 0:
            return int(not any(rem))
        total = 0
        for j in range(start, len(E)):
            a = E[j]
            if all(a[i] <= rem[i] for i in range(r)):
                total += rec(j, left-1, tuple(rem[i]-a[i] for i in range(r)))
        return total
    return rec(0, degree, weight)


def map_data(polys, E, cell):
    n, r, d, lam = cell["n"], cell["r"], cell["degree"], cell["lambda"]
    fixed = e.fixed_factor(polys, E, n, r, d, lam)
    start = time.perf_counter()
    full, counts = e.full_pullback(polys, E, n, r, d, lam)
    elapsed = time.perf_counter()-start
    F, S = e.serialize_images(fixed, False), e.serialize_images(full, True)
    for key in ("rank", "kernel"):
        assert F["exact"][key] == S["exact"][key], key
    star = [[sum(bool(c) and all(E[j][i] > 0 for j in m)
                 for m, c in poly.items()) for i in range(r)] for poly in polys]
    return {"fixed_factor": F, "full_pullback": S, "full_pullback_seconds": elapsed,
            "expansion_counts": counts, "coordinate_factor_surviving_terms": star}


def source_data(polys, E, cell):
    return {"board_numbering": "batch13", "session_id": "B13-03", "cell": cell,
            "values_are": "ordinary coefficient polynomials; exact rational coefficients",
            "exponents": E, "polynomials": [e.polynomial_json(p) for p in polys]}


def build_complete(cell):
    n, r, d, lam = cell["n"], cell["r"], cell["degree"], tuple(cell["lambda"])
    E = e.exps(n, r)
    basis = e.weight_monomials(n, r, d, lam)
    rows, labels = e.raising_matrix(basis, E)
    event("raising_matrix", cell=cell, shape=[len(rows), len(basis)])
    start = time.perf_counter()
    exact = e.echelon(rows, len(basis))
    elapsed = time.perf_counter()-start
    event("exact_source", rank=exact["rank"], nullity=len(exact["kernel"]), seconds=elapsed)
    modular = {str(p): e.echelon(rows, len(basis), p)["rank"] for p in e.PRIMES}
    assert all(x == exact["rank"] for x in modular.values())
    polys = [{m: c for m, c in zip(basis, v) if c} for v in exact["kernel"]]
    e.check_hw(polys, E)
    proof = {"weight_basis_count": len(basis), "raising_shape": [len(rows), len(basis)],
             "raising_nonzeros": sum(map(len, rows)), "raising_exact_rank": exact["rank"],
             "raising_modular_ranks": modular, "exact_source_dimension": len(polys),
             "exact_elimination_seconds": elapsed,
             "exponent_order": "descending first exponent, recursive",
             "source_basis": [e.polynomial_json(p) for p in polys]}
    return E, basis, rows, polys, proof


def primary():
    start = time.perf_counter()
    old = json.loads((S4 / "s64_control.json").read_text())
    cell = {"n": 4, "r": 3, "degree": 6, "lambda": [8, 8, 8]}
    E, basis, rows, independent, proof = build_complete(cell)
    assert len(basis) == 561 and proof["raising_shape"] == [1056, 561]
    assert len(independent) == 2
    oldE = [tuple(a) for a in old["exponents"]]
    remap = {j: E.index(a) for j, a in enumerate(oldE)}
    assert len(remap) == len(E) and set(remap.values()) == set(range(len(E)))
    oldbasis = [tuple(sorted(remap[j] for j in m)) for m in old["basis"]]
    assert len(set(oldbasis)) == len(oldbasis) and set(oldbasis) == set(basis)
    polys = [{m: c for m, c in zip(oldbasis, v) if c} for v in old["source_vectors"]]
    e.validate(E, polys, 4, 3, 6, cell["lambda"])
    e.check_hw(polys, E)
    assert e.echelon(e.image_matrix(polys)[0], 2)["rank"] == 2
    assert e.echelon(e.image_matrix(independent+polys)[0], 4)["rank"] == 2
    maps = map_data(polys, E, cell)
    assert maps["fixed_factor"]["exact"]["rank"] == 1
    assert maps["fixed_factor"]["exact"]["kernel"] == [[1, 0]]
    assert maps["coordinate_factor_surviving_terms"][0] == [0, 0, 0]
    # A membership direction requiring coefficient cancellation in source coordinates.
    mixed0 = defaultdict(int, polys[0])
    for m, c in polys[1].items():
        mixed0[m] += c
    mixed = [{m: c for m, c in mixed0.items() if c}, polys[1]]
    mixedmaps = map_data(mixed, E, cell)
    assert mixedmaps["full_pullback"]["exact"]["kernel"] == [[1, -1]]
    assert all(x for x in mixedmaps["coordinate_factor_surviving_terms"][0])
    assert all(x for x in mixedmaps["coordinate_factor_surviving_terms"][1])
    # An explicit small non-element witness on x1*(x2^3+x3^3).
    C = e.exps(3, 3)
    cube = [int(b in ((0, 3, 0), (0, 0, 3))) for b in C]
    cv = [cube[C.index((a[0]-1,)+a[1:])] if a[0] else 0 for a in E]
    witness = [e.evaluate(p, cv) for p in polys]
    assert witness[0] == 0 and witness[1] != 0
    # Exact repeat of S4 point evaluations, remapped by exponent tuples.
    point_checks = []
    for point in old["points"]:
        cv = [point["coefficients"][oldE.index(a)] for a in E]
        values = [e.evaluate(p, cv) for p in polys]
        for p in e.PRIMES:
            record = next(x for x in old["evaluations"]
                          if x["family"] == point["family"] and x["prime"] == p)
            assert [v % p for v in values] == [row[point["index"]] for row in record["matrix"]]
        point_checks.append({"family": point["family"], "index": point["index"],
                             "values_are": "exact evaluations in archived S4 ordinary source basis",
                             "values": [str(x) for x in values]})
    # Only cubic Pieri predecessor is (8,8,2); certify its multiplicity exactly.
    cc = {"n": 3, "r": 3, "degree": 6, "lambda": [8, 8, 2]}
    _, _, _, cp, cubic_proof = build_complete(cc)
    assert len(cp) == 1
    target_weight = sum(weight_count(3, 3, 6, tuple(8-a for a in eta))
                        for eta in e.exps(6, 3))
    stats = {"ambient_source_dimension": math.comb(15+6-1, 6),
             "ambient_bidegree_target_dimension": math.comb(3+6-1, 6)*math.comb(10+6-1, 6),
             "target_weight_dimension": target_weight,
             "fixed_factor_weight_dimension": weight_count(3, 3, 6, (2, 8, 8)),
             "h_red_exact": 1, "cubic_pieri_predecessor": [8, 8, 2],
             "source_nonzero_terms": [len(p) for p in polys],
             "source_max_absolute_coefficients": [max(map(abs, p.values())) for p in polys]}
    result = {"board_numbering": "batch13", "session_id": "B13-03", "cell": cell,
              "status": "CERTIFIED over Q", "source_completeness": proof,
              "source_input_sha256": sha(S4 / "s64_control.json"),
              "independent_and_archived_source_span_equal_over_Q": True,
              "maps": maps, "mixed_source_maps": mixedmaps, "dimensions": stats,
              "normalization_multiplicity_control": cubic_proof,
              "non_element_witness": {"ell": [1, 0, 0], "cubic_exponents": C,
                                      "cubic_coefficients": cube,
                                      "values_are": "unscaled exact ordinary source evaluations",
                                      "source_values": [str(x) for x in witness]},
              "archived_point_checks": point_checks,
              "wall_seconds": time.perf_counter()-start}
    e.write_json(OUT / "primary_source.json", source_data(polys, E, cell))
    e.write_json(OUT / "mixed_source.json", source_data(mixed, E, cell))
    e.write_json(OUT / "primary.json", result)
    event("primary_complete", dimensions=stats, rank=1, ideal_dimension=1,
          witness=witness, wall_seconds=result["wall_seconds"])


def tiny():
    controls = []
    for r, lam in [(2, [4, 4]), (3, [4, 4, 0])]:
        c = {"n": 4, "r": r, "degree": 2, "lambda": lam}
        E, _, _, polys, proof = build_complete(c)
        maps = map_data(polys, E, c)
        assert maps["full_pullback"]["exact"]["rank"] == len(polys) == 1
        controls.append({"cell": c, "source": proof, "maps": maps})
    E = e.exps(4, 3)
    for d in (1, 2):
        j = E.index((4, 0, 0))
        c = {"n": 4, "r": 3, "degree": d, "lambda": [4*d, 0, 0]}
        maps = map_data([{(j,)*d: 1}], E, c)
        assert maps["full_pullback"]["exact"]["rank"] == 1
        assert maps["full_pullback"]["sparse_rows"] == [[[0, "1"]]]
        controls.append({"cell": c, "maps": maps})
    # Test multinomial multiplicities and ordinary-versus-house normalization.
    a = (2, 1, 1)
    p = {(E.index(a),)*2: 1}
    im, counts = e.full_pullback([p], E, 4, 3, 2, (4, 2, 2))
    assert len(im[0]) == 6 and sorted(im[0].values()) == [1, 1, 1, 2, 2, 2]
    # For m_a=a!*c_a the house substitution factors are a_i, not 1 or a_i/4.
    fact = lambda alpha: math.prod(math.factorial(x) for x in alpha)
    for alpha in E:
        for i, x in enumerate(alpha):
            if x:
                beta = list(alpha)
                beta[i] -= 1
                assert fact(alpha) == x*fact(beta)
    # Neither the all-coordinate support shortcut nor a fixed chart applies to
    # arbitrary non-HW polynomials. This counterexample must be rejected.
    diag = tuple(sorted(E.index(a) for a in [(4, 0, 0), (0, 4, 0), (0, 0, 4)]))
    nonhw = {diag: 1}
    assert all(any(E[j][i] == 0 for j in diag) for i in range(3))
    failure = None
    try:
        e.fixed_factor([nonhw], E, 4, 3, 3, (4, 4, 4))
    except ValueError as err:
        failure = str(err)
    assert failure and "not highest weight" in failure
    images, _ = e.full_pullback([nonhw], E, 4, 3, 3, (4, 4, 4))
    assert images[0]
    cv = [1 if max(alpha) >= 3 else 0 for alpha in E]
    assert e.evaluate(nonhw, cv) == 1
    malformed = []
    for label, coords, poly, weight in [
        ("missing_exponent", E[:-1], {(0,): 1}, (4, 0, 0)),
        ("duplicate_exponent", E+(E[0],), {(0,): 1}, (4, 0, 0)),
        ("invalid_index", E, {(len(E),): 1}, (4, 0, 0)),
        ("wrong_weight", E, {(0,): 1}, (0, 4, 0)),
        ("wrong_degree", E, {(0, 0): 1}, (4, 0, 0)),
        ("float_coefficient", E, {(0,): 0.5}, (4, 0, 0))]:
        try:
            e.full_pullback([poly], coords, 4, 3, 1, weight)
        except ValueError as err:
            malformed.append({"case": label, "rejected": str(err)})
        else:
            raise AssertionError(f"invalid input passed: {label}")
    # Exact Fraction transport is tested at both prescribed primes.
    rational = e.echelon([{0: Fraction(1, 2), 1: Fraction(1, 3)}], 2)
    assert rational["kernel"] == [[2, -3]]
    assert all(e.echelon([{0: Fraction(1, 2), 1: Fraction(1, 3)}], 2, p)["rank"] == 1
               for p in e.PRIMES)
    result = {"board_numbering": "batch13", "session_id": "B13-03", "status": "CERTIFIED over Q",
              "complete_controls": controls, "multinomial_control": e.serialize_images(im, True),
              "house_normalization_checked_for_all_15_coordinates": True,
              "non_highest_weight_trap": {"rejected": failure, "star_on_every_monomial": True,
                                           "full_pullback_nonzero_terms": len(images[0]),
                                           "ell": [1, 1, 1], "cubic": "x1^3+x2^3+x3^3",
                                           "exact_value": 1},
              "malformed_inputs": malformed, "rational_control": rational}
    e.write_json(OUT / "tiny.json", result)
    event("tiny_complete", controls=len(controls), malformed_rejected=len(malformed))


def extension():
    start = time.perf_counter()
    path = S4 / "s64_r5_exact_kernel.json.gz"
    old = json.loads(gzip.decompress(path.read_bytes()))
    E = e.exps(4, 5)
    oldE = [tuple(a) for a in old["exponents"]]
    remap = {j: E.index(a) for j, a in enumerate(oldE)}
    monomials = [tuple(sorted(remap[j] for j in m)) for m in old["monomials"]]
    assert len(set(monomials)) == len(monomials)
    poly = dict(zip(monomials, old["primitive_integer_coefficients"]))
    e.validate(E, [poly], 4, 5, 6, (8, 4, 4, 4, 4))
    support = []
    for i in range(4):
        residual = e.raising(poly, E, i)
        assert not residual
        support.append(len(residual))
    fixed = e.fixed_factor([poly], E, 4, 5, 6, (8, 4, 4, 4, 4))
    assert fixed == [{}]
    star = [sum(all(E[j][i] > 0 for j in m) for m in poly) for i in range(5)]
    assert star == [0]*5
    witnesses = []
    for point in old["points"]:
        vals = {}
        for family in ("det", "pad"):
            cv = [point[family+"_coefficients"][oldE.index(a)] for a in E]
            vals[family] = e.evaluate(poly, cv)
        assert vals["det"] and vals["pad"] == 0
        for record in point["values"]:
            assert vals["det"] % record["prime"] == record["det"]
            assert vals["pad"] % record["prime"] == record["pad"]
        witnesses.append({"seed": point["seed"], "values_are": "exact ordinary coefficient evaluations",
                          "values": {k: str(v) for k, v in vals.items()}})
    result = {"board_numbering": "batch13", "session_id": "B13-03",
              "cell": {"n": 4, "r": 5, "degree": 6, "lambda": [8, 4, 4, 4, 4]},
              "status": "CERTIFIED rational membership of one supplied vector",
              "source_input_sha256": sha(path), "source_terms": len(poly),
              "source_max_abs": max(map(abs, poly.values())),
              "all_exact_simple_raising_residuals": support,
              "coordinate_factor_surviving_terms": star,
              "fixed_factor_terms": 0,
              "nonzero_coefficient_witness": e.polynomial_json(poly)[0],
              "point_checks": witnesses,
              "complete_highest_weight_space_computed": False,
              "full_symbolic_pullback_computed": False,
              "wall_seconds": time.perf_counter()-start}
    e.write_json(OUT / "r5_membership.json", result)
    event("r5_complete", terms=len(poly), wall_seconds=result["wall_seconds"])


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("unit", choices=["primary", "tiny", "r5"])
    a = p.parse_args()
    {"primary": primary, "tiny": tiny, "r5": extension}[a.unit]()
