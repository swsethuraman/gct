"""CI73 dimension component adapted from the independent B14-04 verifier.
Original SHA256: da4c1eaf11393ada59b1f07a1c197b01e87cb6a5871117c012b5be6fa242c44f
No producer imports; explicit certificate inputs are mandatory.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial
PRIMES=(2147483647,2147483629)
def need(ok,why):
    if not ok:raise ValueError(why)

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

def check_hpad(d, exact, mods, cert, power):
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


def power_plethysm(n, degree):
    """Exact Newton recurrence d*h_d = sum_r p_r*h_(d-r), with p_r[h_n]."""
    pieces=[(sigma,Fraction(1,z(sigma))) for sigma in partitions(n)]
    F=[{():Fraction(1)}]
    for d in range(1,degree+1):
        row=defaultdict(Fraction)
        for r in range(1,d+1):
            for sigma,c in pieces:
                rho=tuple(r*x for x in sigma)
                for tau,v in F[d-r].items():
                    row[tuple(sorted(rho+tau,reverse=True))]+=c*v/d
        F.append(dict(row))
    return F[degree]


def ambient13():
    power=power_plethysm(4,13);lam=(21,17)+(2,)*7
    value=sum(c*character(lam,rho) for rho,c in power.items())
    need(value.denominator==1 and value>=0,'nonintegral quartic ambient value')
    character.cache_clear()
    return int(value),power
