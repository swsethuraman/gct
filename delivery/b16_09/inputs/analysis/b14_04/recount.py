"""B14-04: sparse power-sum/MN recounts, independent of Weyl counters."""
import argparse
from collections import defaultdict
from fractions import Fraction as Q
import gzip
import itertools
import json
from math import factorial
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "analysis"))
from wk8_s30_pleth import parts, zr, chi, pleth_p

OUT = ROOT / "results/b14_04"
PRIMES = (2147483647, 2147483629)


def save(name, value):
    raw = (json.dumps(value, separators=(",", ":"), sort_keys=True) + "\n").encode()
    path = OUT / name
    if name.endswith(".gz"):
        raw = gzip.compress(raw, mtime=0)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_bytes(raw)
    temp.replace(path)


def read(path):
    raw = path.read_bytes()
    if path.suffix == ".gz":
        raw = gzip.decompress(raw)
    return json.loads(raw.decode("utf-8-sig"))


def mul(A, B):
    out = defaultdict(Q)
    for x, a in A.items():
        for y, b in B.items():
            out[tuple(sorted(x + y, reverse=True))] += a * b
    return {x: v for x, v in out.items() if v}


def logs(max_n, degrees=(2, 3, 4)):
    """Return t*d/dt log F, so coefficient of p_(r sigma) is j/z_sigma."""
    out = [defaultdict(Q) for _ in range(max_n + 1)]
    for j in degrees:
        for r in range(1, max_n // j + 1):
            for sigma in parts(j):
                out[j * r][tuple(r * v for v in sigma)] += Q(j, zr(sigma))
    return out


def exp_series(max_n, degrees=(2, 3, 4), checkpoint=False):
    L = logs(max_n, degrees)
    F = [{(): Q(1)}]
    start = time.monotonic()
    for n in range(1, max_n + 1):
        row = defaultdict(Q)
        for m in range(1, n + 1):
            for x, a in L[m].items():
                for y, b in F[n - m].items():
                    row[tuple(sorted(x + y, reverse=True))] += a * b
        F.append({x: v / n for x, v in row.items() if v})
        if checkpoint:
            save("stable_progress.json", {"status": "PARTIAL", "completed_degree": n,
                                         "terms": len(F[-1]), "seconds": time.monotonic() - start})
            print("degree", n, "terms", len(F[-1]), "seconds", round(time.monotonic() - start, 3), flush=True)
    return F


def strips(lam, d):
    return sorted({tuple(v for v in mu if v) for mu in
                   itertools.product(*(range(lo, hi + 1) for lo, hi in zip(lam[1:] + (0,), lam)))
                   if sum(mu) == 3 * d}, reverse=True)


def scalar(P, lam):
    value = sum((a * chi(lam, rho) for rho, a in P.items()), Q())
    assert value.denominator == 1 and value >= 0, (lam, value)
    return int(value)


def match_rows(actual, expected):
    assert actual and expected, "empty channel input"
    aa = {tuple(x["mu"]): x["a3"] for x in actual}
    ee = {tuple(x["mu"]): x["a3"] for x in expected}
    assert len(aa) == len(actual) and len(ee) == len(expected), "duplicate channel"
    assert aa == ee, "missing or altered channel"


def reject(fn):
    try:
        fn()
    except (AssertionError, ValueError, KeyError, FileNotFoundError):
        return True
    raise AssertionError("deliberately invalid input was accepted")


def hooks(lam):
    denominator = 1
    for i, width in enumerate(lam):
        for j in range(width):
            denominator *= width - j + sum(v > j for v in lam[i + 1:])
    return factorial(sum(lam)) // denominator


def controls():
    checks = []
    for n in range(1, 8):
        ps = parts(n)
        for lam in ps:
            assert chi(lam, (1,) * n) == hooks(lam)
            trans = tuple(sum(x >= j for x in lam) for j in range(1, lam[0] + 1))
            for rho in ps:
                assert chi((n,), rho) == 1
                assert chi((1,) * n, rho) == (-1) ** (n - len(rho))
                assert chi(trans, rho) == (-1) ** (n - len(rho)) * chi(lam, rho)
            for mu in ps:
                assert sum(Q(chi(lam, rho) * chi(mu, rho), zr(rho)) for rho in ps) == int(lam == mu)
        checks.append({"name": "MN hook, sign, conjugation, full orthogonality", "n": n, "partitions": len(ps)})
    for j, wanted in ((2, {(4,): 1, (2, 2): 1}), (3, {(6,): 1, (4, 2): 1})):
        got = {lam: scalar(pleth_p(2, j), lam) for lam in parts(2 * j)}
        assert {lam: v for lam, v in got.items() if v} == wanted
        checks.append({"name": "small plethysm Schur decomposition", "j": j})
    cubic = {(1, 1, 1): Q(1, 6), (2, 1): Q(1, 2), (3,): Q(1, 3)}
    assert pleth_p(1, 3) == cubic
    def correct_cubic(p):
        assert p == cubic, "wrong cubic normalization"
    bad = dict(cubic)
    bad[(2, 1)] = Q(1, 6)
    assert reject(lambda: correct_cubic(bad))
    checks.append({"name": "wrong cubic normalization rejected"})
    F = exp_series(13)
    for n in range(11):
        direct = defaultdict(Q)
        for a in range(n // 2 + 1):
            for b in range(n // 3 + 1):
                rem = n - 2 * a - 3 * b
                if rem < 0 or rem % 4:
                    continue
                for rho, c in mul(mul(pleth_p(a, 2), pleth_p(b, 3)), pleth_p(rem // 4, 4)).items():
                    direct[rho] += c
        assert dict(direct) == F[n], n
        checks.append({"name": "exponential vs explicit plethysm product", "n": n})
    for lam in ((6, 3, 3, 1), (5, 2, 2, 2, 2)):
        assert scalar(F[13], lam) == 4
        checks.append({"name": "banked stable control", "tail": lam, "value": 4})
    example = [{"mu": [3], "a3": 1}, {"mu": [2, 1], "a3": 0}]
    for invalid in ([], example[:-1], example + example[:1], [{"mu": [3], "a3": 2}, example[1]]):
        assert reject(lambda invalid=invalid: match_rows(invalid, example))
    assert reject(lambda: match_rows(example, []))
    # Exercise character and equality controls on deliberately wrong values.
    assert reject(lambda: require(chi((2, 1), (1, 1, 1)) == 3))
    assert reject(lambda: require(F[2] == {}))
    checks.append({"name": "empty, missing, duplicate, altered channels and wrong character rejected", "mutations": 7})
    save("controls.json", {"status": "PASS", "checks": checks, "values_are": "exact rational/integer control identities"})
    print("controls PASS", len(checks))


def require(condition):
    if not condition:
        raise AssertionError("validation condition failed")


def hpad(d):
    assert read(OUT / "controls.json")["status"] == "PASS"
    start = time.monotonic()
    lam = (4 * d - 31, 17) + (2,) * 7
    shapes = strips(lam, d)
    assert len(shapes) == {13: 15, 14: 27}[d]
    P = pleth_p(d, 3)
    rows = []
    for mu in shapes:
        rows.append({"mu": mu, "a3": scalar(P, mu)})
        if chi.cache_info().currsize > 250000:
            chi.cache_clear()
        save(f"hpad{d}_progress.json", {"status": "PARTIAL", "rows": rows, "expected_channels": len(shapes)})
    pilot_dir = ROOT / "results/b14_prep/astra_slot04_pilot"
    for name in (f"slot04_character_pilot_d{d}.json", f"integrator_replay_d{d}.json"):
        pilot = read(pilot_dir / name)
        assert pilot["complete"] and pilot["degree"] == d and tuple(pilot["lambda"]) == lam
        match_rows(rows, pilot["rows"])
    if d == 13:
        bank = read(ROOT / "results/b13_01_hpad.json")
        match_rows(rows, [{"mu": mu, "a3": a} for mu, a in bank["blocks"]])
    result = {"status": "CERTIFIED", "complete": True, "degree": d, "lambda": lam,
              "h": sum(row["a3"] for row in rows), "rows": rows,
              "method": "Pieri interlacing; banked power-sum plethysm and MN characters",
              "values_are": "unscaled integer cubic Schur multiplicities a3",
              "prior": "73/159 were observed pre-dispatch pilots", "power_terms": len(P),
              "seconds": time.monotonic() - start}
    save(f"hpad{d}.json", result)
    save(f"hpad{d}_progress.json", {"status": "COMPLETE", "rows": rows, "expected_channels": len(shapes)})
    # Bank exact source expansion; the verifier must recompute it.
    save(f"hpad{d}_power.json.gz", {"values_are": "exact power-sum coefficients of h_d[h_3]",
                                  "degree": d, "rows": [[rho, c.numerator, c.denominator] for rho, c in sorted(P.items(), reverse=True)]})
    print("hpad", d, result["h"], result["seconds"])


def sizing():
    L = logs(35)
    p = [len(parts(n)) for n in range(36)]
    operations = sum(len(L[m]) * p[n - m] for n in range(1, 36) for m in range(1, n + 1))
    estimate = sum(p) * 1024
    result = {"partition_counts": p, "recurrence_multiply_add_upper_bound": operations,
              "estimated_storage_bytes_at_1024_per_partition": estimate,
              "storage_estimate_is_not_a_bound": True, "enforced_commit_memory_bytes": 1024**3}
    assert estimate < 1024**3
    save("sizing.json", result)
    print("sizing", result)


def stable():
    assert read(OUT / "controls.json")["status"] == "PASS"
    sizing()
    start = time.monotonic()
    F = exp_series(35, checkpoint=True)
    certificate_stats = []
    for n, first in ((31, 17), (33, 19), (35, 21)):
        lam = (first,) + (2,) * 7
        rows, grouped = [], defaultdict(Q)
        nfac = factorial(n)
        for rho, c in sorted(F[n].items(), reverse=True):
            assert sum(rho) == n and c > 0 and nfac % c.denominator == 0
            assert (zr(rho) * c).denominator == 1
            assert all(c.denominator % p for p in PRIMES)
            character = chi(lam, rho)
            rows.append([rho, c.numerator, c.denominator, character])
            grouped[rho[0]] += c * character
            if chi.cache_info().currsize > 350000:
                chi.cache_clear()
        value = sum(grouped.values(), Q())
        assert value.denominator == 1 and value >= 0
        ident = sum(Q(nfac, (2**a) * (6**b) * (24**c) * factorial(a) * factorial(b) * factorial(c))
                    for a in range(n // 2 + 1) for b in range(n // 3 + 1)
                    for c in range(n // 4 + 1) if 2 * a + 3 * b + 4 * c == n)
        assert F[n][(1,) * n] * nfac == ident
        cert = {"kind": "b14_04_symmetric_function_inner_product_v1", "status": "CERTIFIED",
                "complete": True, "tail": lam, "weighted_degree": n, "generator_degrees": [2, 3, 4],
                "value": int(value), "values_are": "rows [rho, power_coefficient_numerator, denominator, unscaled_MN_character]",
                "coefficient_normalization": "[p_rho] F_n, NOT z_rho times coefficient; scalar=sum coefficient*character",
                "matrix_orientation": "not applicable: no evaluation matrix",
                "common_integral_model": "F_n is Frobenius characteristic of permutation module on set partitions with block sizes 2,3,4",
                "denominators_divide_factorial": n, "denominators_invertible_at": PRIMES,
                "identity_character_of_F": int(ident), "rows": rows,
                "signed_subtotals_by_largest_cycle": [[k, v.numerator, v.denominator] for k, v in sorted(grouped.items())]}
        save(f"stable{n}.json.gz", cert)
        stats = {k: cert[k] for k in ("tail", "weighted_degree", "value", "identity_character_of_F")}
        stats.update(terms=len(rows), elapsed_seconds=time.monotonic() - start)
        certificate_stats.append(stats)
        save("stable_summary.json", {"status": "PARTIAL", "completed": certificate_stats})
        print("stable", stats, flush=True)
        chi.cache_clear()
    save("stable_summary.json", {"status": "CERTIFIED", "complete": True, "completed": certificate_stats,
                                 "seconds": time.monotonic() - start, "values_are": "exact stable Schur multiplicities"})
    save("stable_progress.json", {"status": "COMPLETE", "completed_degree": 35})


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("controls", "hpad13", "hpad14", "stable"))
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    if args.mode == "controls":
        controls()
    elif args.mode == "stable":
        stable()
    else:
        hpad(int(args.mode[4:]))
