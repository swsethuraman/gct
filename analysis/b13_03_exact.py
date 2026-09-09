"""Exact coefficient pullback and checked highest-weight restriction over Q.

All polynomials use ordinary coefficients c_alpha of sum c_alpha*x**alpha.
Monomials are sorted tuples of coordinate indices, including repeated factors.
There are no silent coordinate defaults in source parsing or substitution.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import itertools
import json
import math
from pathlib import Path
import time

PRIMES = (2147483647, 2147483629)
TERM_CAP = 250_000


@lru_cache(None)
def exps(n, r):
    """Descending first exponent: intentionally opposite the old core."""
    if r == 1:
        return ((n,),)
    return tuple((k,) + tail for k in range(n, -1, -1)
                 for tail in exps(n-k, r-1))


def weight_monomials(n, r, degree, weight, cap=1500):
    E = exps(n, r)
    out = []
    def rec(start, left, rem, word):
        if not left:
            if not any(rem):
                out.append(word)
                if len(out) > cap:
                    raise RuntimeError(f"weight monomial cap {cap} exceeded")
            return
        for j in range(start, len(E)):
            a = E[j]
            if all(a[i] <= rem[i] for i in range(r)):
                rec(j, left-1, tuple(rem[i]-a[i] for i in range(r)), word+(j,))
    if sum(weight) != n*degree:
        raise ValueError("weight size differs from n*degree")
    rec(0, degree, tuple(weight), ())
    return out


def validate(E, polynomials, n, r, degree, weight=None):
    if n < 2 or r < 1 or degree < 1:
        raise ValueError("n>=2, r>=1, degree>=1 required")
    if len(set(E)) != len(E) or set(E) != set(exps(n, r)):
        raise ValueError("exponent list must contain every coordinate exactly once")
    for poly in polynomials:
        for m, c in poly.items():
            if not isinstance(c, (int, Fraction)):
                raise ValueError("coefficients must be exact integers or Fractions")
            if len(m) != degree or m != tuple(sorted(m)):
                raise ValueError("monomial has wrong degree or noncanonical ordering")
            if any(not isinstance(j, int) or j < 0 or j >= len(E) for j in m):
                raise ValueError("coordinate index out of bounds")
            if weight is not None and tuple(sum(E[j][i] for j in m)
                                             for i in range(r)) != tuple(weight):
                raise ValueError("source term has the wrong weight")


def raising(poly, E, i):
    pos = {a: j for j, a in enumerate(E)}
    out = defaultdict(int)
    for m, c in poly.items():
        for j, count in Counter(m).items():
            a = E[j]
            if a[i+1] == 0:
                continue
            b = list(a)
            b[i] += 1
            b[i+1] -= 1
            word = list(m)
            word.remove(j)
            word.append(pos[tuple(b)])  # absent coordinate is always an error
            out[tuple(sorted(word))] += c * count * (a[i]+1)
    return {m: c for m, c in out.items() if c}


def check_hw(polynomials, E):
    for j, poly in enumerate(polynomials):
        for i in range(len(E[0])-1):
            residual = raising(poly, E, i)
            if residual:
                term, coefficient = next(iter(residual.items()))
                raise ValueError(f"source {j} is not highest weight: E_{i},{i+1}, "
                                 f"term {term}, coefficient {coefficient}")


def raising_matrix(basis, E):
    rows = {}
    for j, m in enumerate(basis):
        for i in range(len(E[0])-1):
            for target, value in raising({m: 1}, E, i).items():
                rows.setdefault((i, target), {})[j] = value
    labels = sorted(rows)
    if len(labels) > 2500 or len(labels)*len(basis) > 5_000_000:
        raise RuntimeError("raising matrix size cap exceeded")
    return [rows[label] for label in labels], labels


def primitive(row):
    row = {j: int(c) for j, c in row.items() if c}
    if not row:
        return row
    g = math.gcd(*row.values())
    if row[min(row)] < 0:
        g = -g
    return {j: c//g for j, c in row.items()}


def echelon(rows, ncols, modulus=None):
    """Sparse exact elimination; integer primitive rows or modular rows.

    Each elimination replaces a row by a nonzero rational multiple of itself
    plus a pivot row. Thus ranks and nullspaces are preserved over Q.
    """
    piv = {}
    pivot_input_rows = []
    for row_id, original in enumerate(rows):
        if any(j < 0 or j >= ncols for j in original):
            raise ValueError("matrix coordinate out of bounds")
        if modulus:
            row = {}
            for j, c in original.items():
                q = Fraction(c)
                if q.denominator % modulus == 0:
                    raise ValueError("prime divides coefficient denominator")
                value = q.numerator * pow(q.denominator, -1, modulus) % modulus
                if value:
                    row[j] = value
        else:
            den = math.lcm(*(Fraction(c).denominator for c in original.values()))
            row = primitive({j: int(Fraction(c)*den) for j, c in original.items()})
        while row:
            j = min(row)
            if j not in piv:
                if modulus:
                    inv = pow(row[j], -1, modulus)
                    row = {k: v*inv % modulus for k, v in row.items()}
                piv[j] = row
                pivot_input_rows.append(row_id)
                break
            v, base = row[j], piv[j]
            if modulus:
                for k, a in base.items():
                    value = (row.get(k, 0) - v*a) % modulus
                    if value:
                        row[k] = value
                    else:
                        row.pop(k, None)
            else:
                b = base[j]
                g = math.gcd(v, b)
                scale, subtract = b//g, v//g
                row = {k: scale*a for k, a in row.items()}
                for k, a in base.items():
                    row[k] = row.get(k, 0) - subtract*a
                row = primitive(row)
    free = [j for j in range(ncols) if j not in piv]
    kernel = []
    for f in free:
        v = [0]*ncols
        v[f] = 1
        for j in sorted(piv, reverse=True):
            numerator = -sum(a*v[k] for k, a in piv[j].items() if k != j)
            v[j] = (numerator * pow(piv[j][j], -1, modulus) % modulus
                    if modulus else Fraction(numerator, piv[j][j]))
        if modulus:
            kernel.append(v)
        else:
            den = math.lcm(*(Fraction(x).denominator for x in v))
            integers = [int(x*den) for x in v]
            g = math.gcd(*integers)
            if next((x for x in integers if x), 1) < 0:
                g = -g
            kernel.append([x//g for x in integers])
    return {"rank": len(piv), "kernel": kernel,
            "pivot_columns": sorted(piv), "pivot_input_rows": pivot_input_rows}


def fixed_factor(polynomials, E, n, r, degree, weight, coordinate=0):
    validate(E, polynomials, n, r, degree, weight)
    check_hw(polynomials, E)
    if coordinate != 0:
        raise ValueError("single-factor shortcut uses the first coordinate only")
    cubic = exps(n-1, r)
    pos = {a: j for j, a in enumerate(cubic)}
    images = []
    for poly in polynomials:
        out = {}
        for m, c in poly.items():
            if not c or any(E[j][0] == 0 for j in m):
                continue
            target = tuple(sorted(pos[(E[j][0]-1,)+E[j][1:]] for j in m))
            if target in out:
                raise AssertionError("fixed-factor monomial map must be injective")
            out[target] = c
        images.append(out)
    return images


def full_pullback(polynomials, E, n, r, degree, weight=None, term_cap=TERM_CAP):
    """Universal finite restriction; no highest-weight hypothesis is needed."""
    validate(E, polynomials, n, r, degree, weight)
    cubic = exps(n-1, r)
    pos = {a: j for j, a in enumerate(cubic)}
    replacements = []
    for a in E:
        branches = []
        for i in range(r):
            if a[i]:
                b = list(a)
                b[i] -= 1
                branches.append((i, pos[tuple(b)]))
        replacements.append(branches)
    images = []
    counts = {"source_terms": 0, "branch_accumulations": 0,
              "peak_monomial_terms": 0, "peak_polynomial_terms": 0}
    for poly in polynomials:
        out = defaultdict(int)
        for m, c in poly.items():
            if not c:
                continue
            counts["source_terms"] += 1
            expansion = {((0,)*r, ()): 1}
            for j in m:
                nxt = defaultdict(int)
                for (eta, word), value in expansion.items():
                    for i, k in replacements[j]:
                        beta = list(eta)
                        beta[i] += 1
                        nxt[(tuple(beta), tuple(sorted(word+(k,))))] += value
                        counts["branch_accumulations"] += 1
                expansion = dict(nxt)
                counts["peak_monomial_terms"] = max(counts["peak_monomial_terms"], len(expansion))
                if len(expansion) > term_cap:
                    raise RuntimeError("monomial pullback term cap exceeded")
            for key, value in expansion.items():
                out[key] += c*value
                if not out[key]:
                    del out[key]
            counts["peak_polynomial_terms"] = max(counts["peak_polynomial_terms"], len(out))
            if len(out) > term_cap:
                raise RuntimeError("polynomial pullback term cap exceeded")
        images.append(dict(out))
    return images, counts


def image_matrix(images):
    labels = sorted(set().union(*(x.keys() for x in images)))
    return [{j: p[key] for j, p in enumerate(images) if key in p} for key in labels], labels


def serialize_images(images, full):
    rows, labels = image_matrix(images)
    return {"values_are": "exact ordinary coefficient pullback; unscaled; source columns",
            "shape": [len(labels), len(images)], "full_pullback": full,
            "row_labels": labels,
            "sparse_rows": [[[j, str(v)] for j, v in sorted(row.items())] for row in rows],
            "exact": echelon(rows, len(images)),
            "modular_ranks": {str(p): echelon(rows, len(images), p)["rank"] for p in PRIMES}}


def evaluate(poly, coefficients):
    return sum(c*math.prod(coefficients[j] for j in m) for m, c in poly.items())


def polynomial_json(poly):
    return [[list(m), str(c)] for m, c in sorted(poly.items()) if c]


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    if path.stat().st_size > 5_000_000:
        raise RuntimeError(f"artifact exceeds repository cap: {path}")


def load_source(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("values_are") != "ordinary coefficient polynomials; exact rational coefficients":
        raise ValueError("missing or unsupported source coefficient convention")
    E = [tuple(a) for a in data["exponents"]]
    polys = []
    for terms in data["polynomials"]:
        poly = {}
        for m, c in terms:
            m = tuple(m)
            if m in poly:
                raise ValueError("duplicate source monomial")
            if isinstance(c, float):
                raise ValueError("floating coefficient is not an exact rational input")
            poly[m] = Fraction(c)
        polys.append(poly)
    cell = data["cell"]
    validate(E, polys, cell["n"], cell["r"], cell["degree"], cell["lambda"])
    return data, E, polys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    start = time.perf_counter()
    data, E, polys = load_source(args.input)
    c = data["cell"]
    fixed = fixed_factor(polys, E, c["n"], c["r"], c["degree"], c["lambda"])
    source_rows, _ = image_matrix(polys)
    source_rank = echelon(source_rows, len(polys))["rank"]
    if source_rank != len(polys):
        raise ValueError("source vectors are linearly dependent")
    result = {"board_numbering": "batch13", "session_id": "B13-03", "cell": c,
              "source_rank": source_rank, "highest_weight_verified_over_Q": True,
              "source_completeness": "not asserted by this supplied-source interface",
              "fixed_factor": serialize_images(fixed, False)}
    if args.full:
        full, counts = full_pullback(polys, E, c["n"], c["r"], c["degree"], c["lambda"])
        result["full_pullback"] = serialize_images(full, True)
        result["expansion_counts"] = counts
        if result["full_pullback"]["exact"] != result["fixed_factor"]["exact"]:
            # Ranks/kernels must agree; pivot row indices need not.
            for key in ("rank", "kernel"):
                assert result["full_pullback"]["exact"][key] == result["fixed_factor"]["exact"][key]
    result["wall_seconds"] = time.perf_counter()-start
    write_json(args.output, result)
    print(json.dumps({"output": args.output, "rank": result["fixed_factor"]["exact"]["rank"],
                      "kernel": result["fixed_factor"]["exact"]["kernel"],
                      "wall_seconds": result["wall_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
