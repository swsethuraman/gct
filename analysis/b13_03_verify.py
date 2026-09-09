"""Separate replay: no import from the producer or its polynomial routines.

Uses literal labeled-factor expansion (rather than incremental aggregation),
occurrence-wise raising, brute-force monomial enumeration, and independent dense
integer modular elimination on NumPy. All products fit int64 before reduction.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import gzip
import itertools as it
import json
import math
from pathlib import Path
import time
import numpy as np

P = (2147483647, 2147483629)
OUT = Path("results/b13_03")


def compositions(n, r):
    return sorted(a for a in it.product(range(n+1), repeat=r) if sum(a) == n)


def read_source(name):
    data = json.loads((OUT / name).read_text())
    E = [tuple(a) for a in data["exponents"]]
    polys = [{tuple(m): Fraction(c) for m, c in terms} for terms in data["polynomials"]]
    assert all(len(poly) == len(terms) for poly, terms in zip(polys, data["polynomials"]))
    return E, polys


def literal_pullback(poly, E):
    r = len(E[0])
    image = defaultdict(Fraction)
    for m, coefficient in poly.items():
        allowed = [[i for i in range(r) if E[j][i]] for j in m]
        for assignment in it.product(*allowed):
            linear = tuple(assignment.count(i) for i in range(r))
            cubic = []
            for j, i in zip(m, assignment):
                a = list(E[j])
                a[i] -= 1
                cubic.append(tuple(a))
            image[(linear, tuple(sorted(cubic)))] += coefficient
    return {k: v for k, v in image.items() if v}


def stored_images(record, n, r):
    C = sorted(compositions(n-1, r), reverse=True)
    images = [{} for _ in range(record["shape"][1])]
    assert len(record["row_labels"]) == len(record["sparse_rows"]) == record["shape"][0]
    for (eta, word), row in zip(record["row_labels"], record["sparse_rows"]):
        key = (tuple(eta), tuple(sorted(C[j] for j in word)))
        for column, coefficient in row:
            assert key not in images[column]
            images[column][key] = Fraction(coefficient)
    return images


def derivative(poly, E, i):
    r = defaultdict(Fraction)
    for monomial, coefficient in poly.items():
        for occurrence, j in enumerate(monomial):
            a = E[j]
            if a[i+1]:
                target = list(a)
                target[i] += 1
                target[i+1] -= 1
                m = list(monomial)
                m[occurrence] = E.index(tuple(target))
                r[tuple(sorted(m))] += (a[i]+1)*coefficient
    return {m: c for m, c in r.items() if c}


def dense_mod_rank(matrix, prime):
    A = np.asarray(matrix, dtype=np.int64).copy() % prime
    assert (prime-1)**2 + (prime-1) < 2**63
    row = 0
    for col in range(A.shape[1]):
        nonzero = np.flatnonzero(A[row:, col])
        if not len(nonzero):
            continue
        pivot = row+int(nonzero[0])
        A[[row, pivot]] = A[[pivot, row]]
        A[row, col:] = (A[row, col:] * pow(int(A[row, col]), -1, prime)) % prime
        if row+1 < A.shape[0]:
            A[row+1:, col:] = (A[row+1:, col:] -
                              A[row+1:, col, None] * A[row, col:][None, :]) % prime
        row += 1
        if row == A.shape[0]:
            break
    return row


def main():
    start = time.perf_counter()
    report = json.loads((OUT / "primary.json").read_text())
    E, polys = read_source("primary_source.json")
    assert set(E) == set(compositions(4, 3)) and len(E) == 15
    assert all(not derivative(poly, E, i) for poly in polys for i in range(2))
    basis = [m for m in it.combinations_with_replacement(range(15), 6)
             if tuple(sum(E[j][i] for j in m) for i in range(3)) == (8, 8, 8)]
    assert len(basis) == 561
    entries = defaultdict(dict)
    for j, m in enumerate(basis):
        for i in range(2):
            for target, c in derivative({m: 1}, E, i).items():
                entries[(i, target)][j] = int(c)
    assert len(entries) == 1056
    matrix = np.zeros((1056, 561), dtype=np.int64)
    for i, row in enumerate(entries.values()):
        for j, c in row.items():
            matrix[i, j] = c
    ranks = {str(p): dense_mod_rank(matrix, p) for p in P}
    assert list(ranks.values()) == [559, 559]
    # Two exact HW vectors and a nonzero coefficient minor prove equality over Q.
    M = np.array([[int(poly.get(m, 0)) for poly in polys] for m in basis], dtype=np.int64)
    assert all(dense_mod_rank(M, p) == 2 for p in P)
    symbolic = [literal_pullback(poly, E) for poly in polys]
    assert symbolic == stored_images(report["maps"]["full_pullback"], 4, 3)
    assert not symbolic[0] and len(symbolic[1]) == 1720
    # A separate first-factor coefficient extraction is checked on all terms.
    C = sorted(compositions(3, 3), reverse=True)
    fixed = []
    for poly in polys:
        fixed.append({tuple(sorted(C.index((E[j][0]-1,)+E[j][1:]) for j in m)): c
                      for m, c in poly.items() if all(E[j][0] > 0 for j in m)})
    F = report["maps"]["fixed_factor"]
    actual = [{} for _ in polys]
    for label, row in zip(F["row_labels"], F["sparse_rows"]):
        for j, c in row:
            actual[j][tuple(label)] = Fraction(c)
    assert fixed == actual
    # Independently check all 28 linear-degree slices and the total weight.
    for image in symbolic:
        for (eta, word), coefficient in image.items():
            assert coefficient and sum(eta) == 6 and len(word) == 6
            assert tuple(eta[i]+sum(a[i] for a in word) for i in range(3)) == (8, 8, 8)
    ME, mixed = read_source("mixed_source.json")
    assert ME == E
    mixed_images = [literal_pullback(poly, E) for poly in mixed]
    assert mixed_images == stored_images(report["mixed_source_maps"]["full_pullback"], 4, 3)
    assert mixed_images[0] == mixed_images[1] == symbolic[1]
    witness = report["non_element_witness"]
    cubemap = {tuple(a): c for a, c in zip(witness["cubic_exponents"], witness["cubic_coefficients"])}
    quartic = [sum(witness["ell"][i]*cubemap[tuple(a[k]-(i == k) for k in range(3))]
                   for i in range(3) if a[i]) for a in E]
    values = [sum(c*math.prod(quartic[j] for j in m) for m, c in poly.items()) for poly in polys]
    assert values == [0, 729]
    # Exact source polynomial reconstruction under the mixing.
    assert all(mixed[0].get(m, 0)-mixed[1].get(m, 0) == polys[0].get(m, 0)
               for m in set(mixed[0]) | set(mixed[1]) | set(polys[0]))
    # Extension replay uses original exponent ordering and occurrence derivatives.
    old = json.loads(gzip.decompress(Path("results/astra/S4/artifacts/s64_r5_exact_kernel.json.gz").read_bytes()))
    OE = [tuple(a) for a in old["exponents"]]
    op = {tuple(sorted(m)): int(c) for m, c in zip(old["monomials"], old["primitive_integer_coefficients"])}
    assert len(op) == 19834
    assert all(not derivative(op, OE, i) for i in range(4))
    assert all(any(OE[j][i] == 0 for j in m) for m in op for i in range(5))
    result = {"board_numbering": "batch13", "session_id": "B13-03", "status": "PASS",
              "producer_module_imported": False,
              "independent_source_monomials": len(basis), "independent_raising_rows": len(entries),
              "raising_ranks_both_house_primes": ranks,
              "exact_source_vectors_checked": 2, "exact_source_dimension_certified": 2,
              "literal_symbolic_pullback_equal_entrywise": True,
              "literal_pullback_supports": list(map(len, symbolic)),
              "fixed_factor_equal_entrywise": True,
              "mixed_source_cancellation_equal_entrywise": True,
              "non_element_witness": [str(v) for v in values],
              "r5_exact_membership_terms_checked": len(op),
              "wall_seconds": time.perf_counter()-start,
              "numpy_version": np.__version__}
    (OUT / "independent_verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
