"""B19-02 pilot: the counting criterion of docs/b19_02_report.md section 4.

Computes, for n = 5 (the object) or n = 4 (the calibration control where the
answer is known):

    A_n(d)  = binom(C(n+3,4) - 1 + d, d)     ambient dim Sym^d(Sym^4 C^n)
    r_n(d)  = dim ( C[(Mat_4)^n]_{4d} )^{SL_4 x SL_4}
            = sum_{rho |- 4d} n^{ell(rho)} chi_{(d^4)}(rho)^2 / z_rho

Theorem 4.2: r_n(d) < A_n(d) implies a determinant equation of degree d exists.

Controls, including one that must fail, are in run_controls().
All arithmetic is exact (Fraction / int).
"""
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from pathlib import Path

sys.setrecursionlimit(100000)


@lru_cache(None)
def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        return ((),)
    return tuple((k,) + r for k in range(min(n, mx), 0, -1) for r in partitions(n - k, k))


def z_rho(rho):
    a = 1
    for k, c in Counter(rho).items():
        a *= k ** c * factorial(c)
    return a


@lru_cache(None)
def chi(lam, rho):
    """Murnaghan-Nakayama character of S_n, beta-number form."""
    if not rho:
        return int(not lam)
    k, tail = rho[0], rho[1:]
    ell = len(lam)
    beta = tuple(lam[i] + ell - i - 1 for i in range(ell))
    tot = 0
    for b in beta:
        c = b - k
        if c < 0 or c in beta:
            continue
        sign = (-1) ** sum(1 for t in beta if c < t < b)
        new = sorted([t for t in beta if t != b] + [c], reverse=True)
        mu = tuple(t - ell + i + 1 for i, t in enumerate(new))
        mu = tuple(t for t in mu if t)
        tot += sign * chi(mu, tail)
    return tot


def invariant_dim(d, nvars, rect_rows=4):
    """r_n(d) by the rho-sum (Lemma 4.1)."""
    R = (d,) * rect_rows
    tot = Fraction(0)
    for rho in partitions(4 * d):
        c = chi(R, rho)
        if c:
            tot += Fraction(nvars ** len(rho) * c * c, z_rho(rho))
    assert tot.denominator == 1, "non-integer invariant dimension"
    return int(tot)


def ambient_dim(d, nvars):
    return comb(comb(nvars + 3, 4) - 1 + d, d)


def weyl_dim(mu, n):
    """dim S_mu(C^n)."""
    mu = list(mu) + [0] * (n - len(mu))
    if len(mu) > n:
        return 0
    num = den = 1
    for i in range(n):
        for j in range(i + 1, n):
            num *= (mu[i] - mu[j] + j - i)
            den *= (j - i)
    return num // den


def invariant_dim_via_mu(d, nvars, rect_rows=4):
    """Independent route: sum over mu of g(mu,R,R) * dim S_mu(C^nvars)."""
    R = (d,) * rect_rows
    total = 0
    for mu in partitions(4 * d):
        if len(mu) > nvars:
            continue
        g = Fraction(0)
        for rho in partitions(4 * d):
            cR = chi(R, rho)
            if cR:
                g += Fraction(chi(mu, rho) * cR * cR, z_rho(rho))
        assert g.denominator == 1
        if g:
            total += int(g) * weyl_dim(mu, nvars)
    return total


def run_controls(out):
    rec = {"controls": []}

    def add(name, expect, got, passed, extra=None):
        row = {"name": name, "expected": expect, "got": got, "passed": bool(passed)}
        if extra:
            row.update(extra)
        rec["controls"].append(row)

    # A. r_n(1) must be the number of quartic coefficients: the 70 (resp 35)
    #    coefficients of det(sum x_k B_k) are exactly the weight-one invariants.
    for n in (4, 5):
        got = invariant_dim(1, n)
        add(f"r_{n}(1) equals dim Sym^4(C^{n})", comb(n + 3, 4), got, got == comb(n + 3, 4))

    # B. character table orthogonality for S_m, m <= 8
    ok = True
    for m in range(1, 9):
        ps = partitions(m)
        for lam in ps:
            s = sum(Fraction(chi(lam, rho) ** 2, z_rho(rho)) for rho in ps)
            if s != 1:
                ok = False
    add("S_m row orthogonality, m <= 8", 1, 1 if ok else 0, ok)

    # C. independent route agreement at small d (rho-sum vs mu-sum)
    ok = True
    pairs = []
    for n in (4, 5):
        for d in (1, 2, 3):
            a1, a2 = invariant_dim(d, n), invariant_dim_via_mu(d, n)
            pairs.append({"n": n, "d": d, "rho_sum": a1, "mu_sum": a2})
            ok &= (a1 == a2)
    add("rho-sum equals mu-sum for n=4,5 and d<=3", "equal", "equal" if ok else "differ", ok,
        {"pairs": pairs})

    # D. MUST FAIL: the same formula with the wrong rectangle (d^3) cannot
    #    reproduce the count of quartic coefficients at d = 1.
    wrong = invariant_dim(1, 5, rect_rows=3)
    add("wrong rectangle (d^3) is rejected at d=1", "!= 70", wrong, wrong != 70,
        {"note": "a control that must fail; if this equalled 70 the formula would "
                 "not be testing the SL4 x SL4 rectangle condition"})

    # E. MUST FAIL: a corrupted character value must break integrality of r(d).
    real = chi.__wrapped__ if hasattr(chi, "__wrapped__") else None
    detected = False
    try:
        R = (2,) * 4
        tot = Fraction(0)
        for rho in partitions(8):
            c = chi(R, rho) + (1 if rho == (8,) else 0)      # deliberate corruption
            tot += Fraction(5 ** len(rho) * c * c, z_rho(rho))
        detected = (tot.denominator != 1) or (int(tot) != invariant_dim(2, 5))
    except Exception:
        detected = True
    add("corrupted character is rejected", "rejected", "rejected" if detected else "NOT DETECTED",
        detected)

    rec["all_passed"] = all(c["passed"] for c in rec["controls"])
    out.write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({"controls_all_passed": rec["all_passed"],
                      "checks": [(c["name"], c["passed"]) for c in rec["controls"]]}))


def run_sweep(nvars, dmax, out, dmin=1):
    rows = []
    t0 = time.perf_counter()
    prev = None
    for d in range(dmin, dmax + 1):
        t = time.perf_counter()
        A = ambient_dim(d, nvars)
        r = invariant_dim(d, nvars)
        row = {"d": d, "A": A, "r": r, "A_over_r": A / r,
               "growth_A": (A / prev[0]) if prev else None,
               "growth_r": (r / prev[1]) if prev else None,
               "criterion_fires": bool(r < A),
               "seconds": time.perf_counter() - t}
        rows.append(row)
        prev = (A, r)
        chi.cache_clear()
        print(json.dumps({k: (f"{v:.6g}" if isinstance(v, float) else v)
                          for k, v in row.items()}), flush=True)
    rec = {"nvars": nvars, "dmin": dmin, "dmax": dmax, "rows": rows,
           "any_fire": any(x["criterion_fires"] for x in rows),
           "seconds_total": time.perf_counter() - t0}
    out.write_text(json.dumps(rec, indent=1) + "\n")


def main():
    what = sys.argv[1]
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)
    if what == "controls":
        run_controls(out)
    else:
        nvars = int(what)
        dmax = int(sys.argv[3])
        dmin = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        run_sweep(nvars, dmax, out, dmin)


if __name__ == "__main__":
    main()
