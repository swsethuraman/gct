"""Independent exact coefficient expansion and diagram MN verifier, stdlib only.

Does not import recount.py, wk8_s30_pleth or any Weyl/scratch counter.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import gzip
import hashlib
import itertools
import json
from math import factorial
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/b14_04"
PRIMES = (2147483647, 2147483629)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def load(path):
    raw = path.read_bytes()
    if path.suffix == ".gz":
        raw = gzip.decompress(raw)
    return json.loads(raw.decode("utf-8-sig"))


def partitions(n, ceiling=None):
    if n == 0:
        yield ()
        return
    for i in range(1, min(n, n if ceiling is None else ceiling) + 1):
        for tail in partitions(n - i, i):
            yield (i,) + tail


def z(rho):
    value = 1
    for i, count in Counter(rho).items():
        value *= i ** count * factorial(count)
    return value


@lru_cache(maxsize=20000)
def rim_removals(lam, r):
    """Contiguous segments of the outer Young-diagram rim; no beta numbers."""
    if not lam:
        return ()
    rim = []
    i, j = 0, lam[0] - 1
    while True:
        rim.append((i, j))
        if i == len(lam) - 1 and j == 0:
            break
        if i + 1 < len(lam) and lam[i + 1] > j:
            i += 1
        else:
            j -= 1
    out = []
    for start in range(len(rim) - r + 1):
        removed = rim[start:start + r]
        counts = Counter(i for i, j in removed)
        mu = tuple(v - counts[i] for i, v in enumerate(lam))
        if any(mu[i] < mu[i + 1] for i in range(len(mu) - 1)):
            continue
        # Removing cells must remove a suffix of each affected row.
        if any(j < mu[i] for i, j in removed):
            continue
        out.append((tuple(v for v in mu if v), (-1) ** (len(counts) - 1)))
    return tuple(out)


@lru_cache(maxsize=300000)
def character(lam, rho):
    if not rho:
        return int(not lam)
    return sum(sign * character(mu, rho[1:]) for mu, sign in rim_removals(lam, rho[0]))


def exponential_product(N):
    """Multiply individual exp(c*p_sigma*t^degree) factors, exactly.

    This is not the producer's logarithmic-derivative recurrence.
    """
    factors = defaultdict(Fraction)
    for j in (2, 3, 4):
        for sigma in partitions(j):
            for r in range(1, N // j + 1):
                factors[(j * r, tuple(r * i for i in sigma))] += Fraction(1, r * z(sigma))
    F = [{(): Fraction(1)}] + [{} for _ in range(N)]
    for (degree, rho), coefficient in sorted(factors.items(), reverse=True):
        nxt = [defaultdict(Fraction, row) for row in F]
        c = Fraction(1)
        for k in range(1, N // degree + 1):
            c = c * coefficient / k
            monomial = rho * k
            for n in range(N - k * degree + 1):
                for tau, value in F[n].items():
                    nxt[n + k * degree][tuple(sorted(tau + monomial, reverse=True))] += value * c
        F = [dict(row) for row in nxt]
    return F


def modular_newton(N, p, cubic_outer=False):
    """Independent modular-only Newton recurrence, with no rational arithmetic."""
    L = [defaultdict(int) for _ in range(N + 1)]
    for j in ((3,) if cubic_outer else (2, 3, 4)):
        for r in range(1, (N if cubic_outer else N // j) + 1):
            weight = r if cubic_outer else j * r
            for sigma in partitions(j):
                rho = tuple(r * v for v in sigma)
                L[weight][rho] = (L[weight][rho] + (1 if cubic_outer else j) * pow(z(sigma), -1, p)) % p
    F = [{(): 1}]
    for n in range(1, N + 1):
        accum = defaultdict(int)
        for r in range(1, n + 1):
            for rho, c in L[r].items():
                for tau, v in F[n - r].items():
                    key = tuple(sorted(rho + tau, reverse=True))
                    accum[key] = (accum[key] + c * v) % p
        inv = pow(n, -1, p)
        F.append({rho: c * inv % p for rho, c in accum.items()})
    return F


def cubic_exact(N):
    """Newton h_d[h3], independent of producer's outer-partition enumeration."""
    F = [{(): Fraction(1)}]
    for d in range(1, N + 1):
        accum = defaultdict(Fraction)
        for r in range(1, d + 1):
            for sigma, c in (((r, r, r), Fraction(1, 6)), ((2 * r, r), Fraction(1, 2)), ((3 * r,), Fraction(1, 3))):
                for tau, v in F[d - r].items():
                    accum[tuple(sorted(sigma + tau, reverse=True))] += c * v / d
        F.append(dict(accum))
    return F


def check_stable(cert, exact, mods, n, first):
    need(cert["kind"] == "b14_04_symmetric_function_inner_product_v1", "wrong kind")
    need(cert["complete"] is True, "incomplete certificate")
    need(cert["generator_degrees"] == [2, 3, 4], "wrong generators")
    lam = (first,) + (2,) * 7
    need(tuple(cert["tail"]) == lam and cert["weighted_degree"] == n, "wrong tail or degree")
    need(cert["values_are"] == "rows [rho, power_coefficient_numerator, denominator, unscaled_MN_character]", "wrong normalization")
    rows = cert["rows"]
    need(bool(rows), "missing rows")
    got = {}
    subtotal = defaultdict(Fraction)
    for rho_list, num, den, ch in rows:
        rho = tuple(rho_list)
        need(rho not in got, "duplicate class")
        need(rho == tuple(sorted(rho, reverse=True)) and sum(rho) == n, "invalid class")
        need(type(num) is int and type(den) is int and type(ch) is int and den > 0, "invalid scalar type")
        c = Fraction(num, den)
        need(c > 0 and factorial(n) % den == 0, "invalid coefficient denominator")
        need(c.denominator == den and c.numerator == num, "nonreduced rational")
        need((c * z(rho)).denominator == 1, "nonintegral permutation character")
        need(c == exact.get(rho), "coefficient differs from independent exact expansion")
        need(ch == character(lam, rho), "character differs from diagram MN")
        for p in PRIMES:
            need(den % p != 0, "denominator not a unit")
            need(num * pow(den, -1, p) % p == mods[p].get(rho, 0), "modular disagreement")
        got[rho] = c
        subtotal[rho[0]] += c * ch
    need(got == exact, "missing nonzero power-sum class")
    total = sum(subtotal.values(), Fraction())
    need(total.denominator == 1 and total >= 0, "nonintegral multiplicity")
    need(total == cert["value"], "altered total")
    need(cert["signed_subtotals_by_largest_cycle"] == [[k, v.numerator, v.denominator] for k, v in sorted(subtotal.items())], "altered subtotals")
    identity = exact[(1,) * n] * factorial(n)
    # Independent recurrence for labelled set partitions with allowed block sizes.
    bells = [1]
    for k in range(1, n + 1):
        bells.append(sum(factorial(k - 1) // (factorial(j - 1) * factorial(k - j)) * bells[k - j]
                         for j in (2, 3, 4) if j <= k))
    need(identity == bells[n] == cert["identity_character_of_F"], "identity class wrong")
    return int(total)


def check_hpad(d, exact, mods, cert=None, power=None):
    if cert is None:
        cert = load(OUT / f"hpad{d}.json")
    if power is None:
        power = load(OUT / f"hpad{d}_power.json.gz")
    need(cert["complete"] is True and cert["degree"] == d, "incomplete or wrong hpad")
    need(power["degree"] == d and bool(power["rows"]), "missing hpad expansion")
    need(cert["values_are"] == "unscaled integer cubic Schur multiplicities a3", "wrong hpad normalization")
    need(power["values_are"] == "exact power-sum coefficients of h_d[h_3]", "wrong hpad power normalization")
    P = {tuple(rho): Fraction(a, b) for rho, a, b in power["rows"]}
    need(len(P) == len(power["rows"]) and P == exact, "hpad expansion disagrees")
    for rho, c in P.items():
        need(sum(rho) == 3 * d and c > 0 and (c * z(rho)).denominator == 1, "hpad power class")
        need(factorial(3 * d) % c.denominator == 0, "hpad denominator")
        for p in PRIMES:
            need(c.denominator % p and c.numerator * pow(c.denominator, -1, p) % p == mods[p].get(rho, 0), "hpad modular coefficient")
    lam = (4 * d - 31, 17) + (2,) * 7
    need(tuple(cert["lambda"]) == lam, "hpad partition")
    # Independent recursive bounded-composition enumeration, not Cartesian product.
    shapes = []
    def descend(i, remaining, prefix):
        if i == len(lam):
            if remaining == 0:
                shapes.append(tuple(v for v in prefix if v))
            return
        lower = lam[i + 1] if i + 1 < len(lam) else 0
        for v in range(lower, min(lam[i], remaining) + 1):
            descend(i + 1, remaining - v, prefix + (v,))
    descend(0, 3 * d, ())
    need(len(shapes) == {13: 15, 14: 27}[d], "strip count")
    rows = cert["rows"]
    got = {tuple(row["mu"]): row["a3"] for row in rows}
    need(len(got) == len(rows) and set(got) == set(shapes), "missing or repeated strip")
    for mu in shapes:
        value = sum(c * character(mu, rho) for rho, c in P.items())
        need(value.denominator == 1 and value >= 0 and value == got[mu], "hpad character sum")
        character.cache_clear()
    need(sum(got.values()) == cert["h"], "hpad total")
    return cert["h"]


def selfcheck_rim():
    for n in range(1, 8):
        ps = list(partitions(n))
        for lam in ps:
            hook_product = 1
            for i, row in enumerate(lam):
                for j in range(row):
                    hook_product *= row - j + sum(v > j for v in lam[i + 1:])
            need(character(lam, (1,) * n) == factorial(n) // hook_product, "diagram hook identity")
            for mu in ps:
                value = sum(Fraction(character(lam, rho) * character(mu, rho), z(rho)) for rho in ps)
                need(value == int(lam == mu), "diagram orthogonality")


def main():
    started = time.monotonic()
    (OUT / "verification.json").write_text('{"status":"RUNNING","complete":false}\n', encoding="utf-8")
    hashes = load(OUT / "input_manifest.json")
    need(len(hashes) >= 20, "missing manifest inputs")
    line_ending_variants = []
    append_only_extensions = []
    for item in hashes:
        path = ROOT / item["path"]
        raw = path.read_bytes()
        blob = subprocess.check_output(["git", "rev-parse", "9898e56941a7665f231873481dae956f08509995:" + item["path"]], cwd=ROOT, text=True).strip()
        need(blob == item["git_blob"], "input blob changed")
        canonical = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        normalized = raw.replace(b"\r\n", b"\n")
        frozen = canonical.replace(b"\r\n", b"\n")
        if item["path"] == "docs/PROVED.md" and normalized != frozen:
            need(normalized.startswith(frozen), "frozen proof index prefix changed")
            need(normalized[len(frozen):].startswith(b"\n## F. Batch-14 independent dimension certificates\n"), "unexpected proof index extension")
            append_only_extensions.append(item["path"])
        else:
            need(normalized == frozen, "input content changed: " + item["path"])
        if hashlib.sha256(raw).hexdigest() != item["sha256"] and item["path"] not in append_only_extensions:
            line_ending_variants.append(item["path"])
    selfcheck_rim()
    F = exponential_product(35)
    mods = {p: modular_newton(35, p) for p in PRIMES}
    stable = []
    for n, first in ((31, 17), (33, 19), (35, 21)):
        cert = load(OUT / f"stable{n}.json.gz")
        value = check_stable(cert, F[n], {p: mods[p][n] for p in PRIMES}, n, first)
        stable.append({"degree": n, "value": value, "classes": len(cert["rows"])})
        print("verified stable", n, value, flush=True)
        character.cache_clear()
    cubic = cubic_exact(14)
    cubic_mods = {p: modular_newton(14, p, cubic_outer=True) for p in PRIMES}
    hp = []
    for d in (13, 14):
        value = check_hpad(d, cubic[d], {p: cubic_mods[p][d] for p in PRIMES})
        hp.append({"degree": d, "h": value})
        print("verified hpad", d, value, flush=True)
    # A complete, authentic certificate must pass first; every changed one fails.
    original = load(OUT / "stable33.json.gz")
    mutations = []
    for name in ("empty", "missing", "duplicate", "coefficient", "character", "value", "tail", "generators", "complete", "normalization", "subtotal"):
        bad = json.loads(json.dumps(original))
        if name == "empty": bad["rows"] = []
        if name == "missing": bad["rows"].pop()
        if name == "duplicate": bad["rows"].append(bad["rows"][0])
        if name == "coefficient": bad["rows"][0][1] += 1
        if name == "character": bad["rows"][0][3] += 1
        if name == "value": bad["value"] += 1
        if name == "tail": bad["tail"][0] += 1
        if name == "generators": bad["generator_degrees"] = [1, 2, 3]
        if name == "complete": bad["complete"] = False
        if name == "normalization": bad["values_are"] = "scaled values"
        if name == "subtotal": bad["signed_subtotals_by_largest_cycle"][0][1] += 1
        try:
            check_stable(bad, F[33], {p: mods[p][33] for p in PRIMES}, 33, 19)
        except (ValueError, KeyError) as exc:
            mutations.append({"mutation": name, "rejected": True, "reason": str(exc)})
        else:
            raise ValueError("accepted deliberately corrupted certificate: " + name)
    try:
        load(OUT / "deliberately_missing_required_input.json")
    except FileNotFoundError:
        mutations.append({"mutation": "missing required file", "rejected": True})
    else:
        raise ValueError("missing-file fixture unexpectedly exists")
    for name in ("empty", "missing", "duplicate", "value", "normalization", "power coefficient", "power normalization"):
        cert = load(OUT / "hpad13.json")
        power = load(OUT / "hpad13_power.json.gz")
        if name == "empty": cert["rows"] = []
        if name == "missing": cert["rows"].pop()
        if name == "duplicate": cert["rows"].append(cert["rows"][0])
        if name == "value": cert["rows"][0]["a3"] += 1
        if name == "normalization": cert["values_are"] = "scaled"
        if name == "power coefficient": power["rows"][0][1] += 1
        if name == "power normalization": power["values_are"] = "scaled"
        try:
            check_hpad(13, cubic[13], {p: cubic_mods[p][13] for p in PRIMES}, cert, power)
        except (ValueError, KeyError) as exc:
            mutations.append({"mutation": "hpad " + name, "rejected": True, "reason": str(exc)})
        else:
            raise ValueError("accepted deliberately corrupted hpad certificate: " + name)
    summary = {"status": "PASS", "complete": True, "input_hashes_verified": len(hashes),
               "line_ending_only_variants": line_ending_variants,
               "frozen_prefix_preserved_with_session_append": append_only_extensions,
               "stable": stable, "hpad": hp, "mutations": mutations,
               "exact_coefficient_method": "product of scalar exponential factors; separate cubic Newton recurrence",
               "character_method": "outer-rim Young-diagram segment removal, no beta numbers",
               "modular_checks": list(PRIMES), "seconds": time.monotonic() - started,
               "values_are": "exact rational identities and explicit rejected mutations"}
    (OUT / "verification.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("verification PASS", summary["seconds"], flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        (OUT / "verification.json").write_text(json.dumps({"status": "FAIL", "complete": False, "error": repr(exc)}) + "\n", encoding="utf-8")
        raise
