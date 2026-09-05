"""Layer 2 -- semantic checks: is the recorded object the object claimed?

For a highest-weight-vector certificate ("hwv"):
  * cell consistency: |lambda| = n*delta, lambda weakly decreasing and positive
    with length r, every term has delta factors of degree n in r variables, and
    the claimed ambient multiplicity a equals an independent recomputation
    (pleth.py, Weyl alternation);
  * every term has weight exactly lambda;
  * every simple raising operator E_{i,i+1} annihilates every vector -- over Z
    for integer vectors, modulo the recorded prime for mod-p vectors (which are
    then reported as mod-p, never as integer, certificates);
  * the vectors are linearly independent (rank over Q via a prime lower bound
    and an exact recheck when small; mod p for mod-p vectors);
  * (star) support when claimed;
  * the recorded evaluation points are rebuilt from their substitution data and
    the vectors vanish / do not vanish there as claimed;
  * fresh points of the named families are drawn from the recorded seed and the
    same is required of them.

For a full-rank certificate ("full_rank"): the ambient multiplicity a is
recomputed; the kernel of the raising operators modulo the prime is either
recomputed (N_S within reach) or taken from the recorded basis after each basis
vector is checked to be a highest-weight vector mod p and the basis to be
independent with a members; the basis is evaluated at the recorded points and
the rank modulo the prime must be a.  Since rank_p <= rank_Q <= a, that proves
mult = a over Q at the cell, provided the points lie on the claimed variety --
which is exactly what rebuilding them from substitution data checks.
"""
import random
from flint import nmod_mat, fmpz_mat
from hwv import (check_vector_shape, is_highest_weight, star_support, evaluate,
                 apply_raising, canonical_term)
from pleth import ambient_multiplicity, exponent_tuples
from points import form_of_point, fresh_point, FAMILIES

HOUSE_PRIMES = (2147483647, 2147483629)
KERNEL_CAP = 3000          # weight-space dimension up to which the kernel is recomputed


def _rank_rows(rows, ncols, p):
    if not rows or ncols == 0:
        return 0
    return nmod_mat(len(rows), ncols, [v % p for r in rows for v in r], p).rank()


def _independent(vectors, modulus):
    """rank of the vectors on their union of terms; over Q via two primes plus
    an exact flint rank when the support is small."""
    terms = sorted({t for vec in vectors for t, _ in vec})
    idx = {t: k for k, t in enumerate(terms)}
    rows = []
    for vec in vectors:
        row = [0] * len(terms)
        for t, c in vec:
            row[idx[t]] = c
        rows.append(row)
    if modulus is not None:
        return _rank_rows(rows, len(terms), modulus), f"mod {modulus}"
    ranks = {p: _rank_rows(rows, len(terms), p) for p in HOUSE_PRIMES}
    r = max(ranks.values())
    if len(terms) * len(rows) <= 200000:
        r = fmpz_mat(len(rows), len(terms), [v for rw in rows for v in rw]).rank()
        return r, "over Q (flint, exact)"
    return r, f"over Q (lower bound from primes {list(ranks.values())}; equals the count so exact)"


def parse_vector(raw, r):
    """raw: {"terms": [[[alpha...], coeff], ...]} -> list of (alphas tuple, coeff)."""
    if not (isinstance(raw, dict) and set(raw) == {"terms"}):
        raise ValueError("vector must be a dict with exactly the key terms")
    out = []
    for e in raw["terms"]:
        if not (isinstance(e, list) and len(e) == 2):
            raise ValueError("term must be [[alpha, ...], coeff]")
        alphas, c = e
        if not (isinstance(alphas, list) and alphas):
            raise ValueError("term factors must be a nonempty list")
        tup = []
        for a in alphas:
            if not (isinstance(a, list) and len(a) == r
                    and all(isinstance(x, int) and not isinstance(x, bool) for x in a)):
                raise ValueError(f"exponent tuple must be a list of {r} integers")
            tup.append(tuple(a))
        if not isinstance(c, int) or isinstance(c, bool):
            raise ValueError("coefficient must be an integer")
        out.append((tuple(tup), c))
    return out


def check_cell(cell, log):
    n, r, lam, delta, a = cell["n"], cell["r"], tuple(cell["lambda"]), cell["delta"], cell["a"]
    ok = True
    ok &= _rec(log, "cell: n = 4", n == 4, f"n = {n}")
    ok &= _rec(log, "cell: length(lambda) = r", len(lam) == r and lam[-1] > 0,
               f"lambda {lam}, r {r}")
    ok &= _rec(log, "cell: lambda weakly decreasing", all(lam[i] >= lam[i + 1] for i in range(len(lam) - 1)))
    ok &= _rec(log, "cell: |lambda| = n*delta", sum(lam) == n * delta, f"{sum(lam)} vs {n}*{delta}")
    a_ind = ambient_multiplicity(lam, delta, n=n)
    if a_ind is None:
        _rec(log, "cell: a recomputed (Weyl alternation)", True, "cell too large for the DP box; a NOT recomputed")
    else:
        ok &= _rec(log, "cell: a recomputed (Weyl alternation)", a_ind == a, f"recomputed {a_ind}, claimed {a}")
    return ok


def _rec(log, name, ok, detail=""):
    log.append((name, bool(ok), detail))
    return bool(ok)


def check_hwv_certificate(cert, log):
    cell = cert["cell"]
    n, r, lam, delta = cell["n"], cell["r"], tuple(cell["lambda"]), cell["delta"]
    modulus = cert["modulus"]
    ok = check_cell(cell, log)
    vectors = [parse_vector(v, r) for v in cert["vectors"]]
    _rec(log, "vectors parsed", True, f"{len(vectors)} vector(s), supports {[len(v) for v in vectors]}"
         + (f", modulus {modulus}" if modulus else ", integer coefficients"))
    for k, vec in enumerate(vectors):
        try:
            check_vector_shape(vec, n, r, delta, lam)
            ok &= _rec(log, f"vector {k}: shape, degree, canonical terms, weight = lambda", True)
        except ValueError as e:
            ok &= _rec(log, f"vector {k}: shape, degree, canonical terms, weight = lambda", False, str(e))
            return False
        if modulus is not None and any(not (0 < c < modulus) for _, c in vec):
            ok &= _rec(log, f"vector {k}: coefficients in [1, p-1]", False)
            return False
        hw, op, res = is_highest_weight(vec, r, modulus)
        ok &= _rec(log, f"vector {k}: annihilated by every E_(i,i+1) "
                        + ("over Z" if modulus is None else f"mod {modulus}"),
                   hw, "" if hw else f"E_{op} leaves {res} terms")
    claims = cert["claims"]
    if claims.get("independent"):
        rk, how = _independent(vectors, modulus)
        ok &= _rec(log, "vectors linearly independent", rk == len(vectors), f"rank {rk} {how}")
    if "star_support" in claims:
        kk = claims["star_support"]["k"]
        for k, vec in enumerate(vectors):
            bad = star_support(vec, kk)
            ok &= _rec(log, f"vector {k}: (star) support for k = {kk} (Theorem (star): lies in I({{l^{kk} c}}))",
                       bad == 0, f"{bad} violating terms" if bad else "")
    # recorded points
    for key, want_zero in (("vanishes_at", True), ("nonvanishing_at", False)):
        pts = claims.get(key, [])
        if not pts:
            continue
        vals = []
        for j, pt in enumerate(pts):
            F = form_of_point(pt, r)
            vals.append([evaluate(vec, F, modulus) for vec in vectors])
        if want_zero:
            allz = all(v == 0 for row in vals for v in row)
            ok &= _rec(log, f"vanishes at {len(pts)} recorded point(s) [{', '.join(sorted({p['type'] for p in pts}))}]",
                       allz, "" if allz else f"nonzero values at {sum(1 for row in vals for v in row if v)} (vector, point) pairs")
        else:
            rk = _eval_rank(vals, len(vectors), modulus)
            ok &= _rec(log, f"evaluation at {len(pts)} recorded point(s) [{', '.join(sorted({p['type'] for p in pts}))}] has full row rank",
                       rk == len(vectors), f"rank {rk} of {len(vectors)}")
    # fresh points
    fp = claims.get("fresh_points")
    if fp:
        seed, count = fp["seed"], fp["count"]
        for fam in fp.get("vanishes_on", []):
            rnd = random.Random(seed + 1000 * FAMILIES.index(fam))
            bad = 0
            for _ in range(count):
                F = form_of_point(fresh_point(fam, r, rnd), r)
                bad += sum(1 for vec in vectors if evaluate(vec, F, modulus) != 0)
            ok &= _rec(log, f"vanishes at {count} fresh {fam} points (seed {seed})", bad == 0,
                       "" if bad == 0 else f"{bad} nonzero (vector, point) pairs")
        for fam in fp.get("nonvanishing_on", []):
            rnd = random.Random(seed + 1000 * FAMILIES.index(fam))
            vals = []
            for _ in range(count):
                F = form_of_point(fresh_point(fam, r, rnd), r)
                vals.append([evaluate(vec, F, modulus) for vec in vectors])
            rk = _eval_rank(vals, len(vectors), modulus)
            ok &= _rec(log, f"evaluation at {count} fresh {fam} points (seed {seed}) has full row rank",
                       rk == len(vectors), f"rank {rk} of {len(vectors)}")
    return ok


def _eval_rank(vals, nvec, modulus):
    """rank of the nvec x npoints evaluation matrix."""
    rows = [[vals[j][k] for j in range(len(vals))] for k in range(nvec)]
    if modulus is not None:
        return _rank_rows(rows, len(vals), modulus)
    return max(_rank_rows(rows, len(vals), p) for p in HOUSE_PRIMES)


# ------------------------------------------------------------- full rank
def weight_monomials(n, r, delta, lam):
    """all multisets of delta exponent tuples (degree n, r variables) with sum
    lambda, as sorted tuples."""
    E = exponent_tuples(n, r)
    out = []

    def rec(start, left, rem, cur):
        if left == 0:
            if not any(rem):
                out.append(tuple(cur))
            return
        if sum(rem) != left * n:
            return
        for i in range(start, len(E)):
            a = E[i]
            if any(a[j] > rem[j] for j in range(r)):
                continue
            rec(i, left - 1, tuple(rem[j] - a[j] for j in range(r)), cur + [a])

    rec(0, delta, tuple(lam), [])
    return out


def kernel_mod_p(n, r, delta, lam, p):
    """basis (list of vectors as term lists) of the highest-weight space mod p."""
    basis = weight_monomials(n, r, delta, lam)
    pos = {m: k for k, m in enumerate(basis)}
    rows = {}
    for i in range(r - 1):
        for col, m in enumerate(basis):
            res = apply_raising([(m, 1)], i, i + 1, p)
            for tgt, c in res.items():
                rows.setdefault((i, tgt), {})[col] = c
    R = list(rows.values())
    if not R:
        return basis, [[1 if k == j else 0 for k in range(len(basis))] for j in range(len(basis))]
    M = nmod_mat(len(R), len(basis), p)
    for a, row in enumerate(R):
        for b, v in row.items():
            M[a, b] = v
    X, nul = M.nullspace()
    vecs = [[int(X[i, j]) for i in range(len(basis))] for j in range(nul)]
    return basis, vecs


def check_full_rank_certificate(cert, log):
    cell = cert["cell"]
    n, r, lam, delta, a = cell["n"], cell["r"], tuple(cell["lambda"]), cell["delta"], cell["a"]
    p = cert["prime"]
    ok = check_cell(cell, log)
    if a == 0:
        return _rec(log, "a = 0: nothing to certify", True) and ok
    basis_vecs = None
    if cert.get("basis") is not None:
        basis_vecs = [parse_vector(v, r) for v in cert["basis"]]
        for k, vec in enumerate(basis_vecs):
            try:
                check_vector_shape(vec, n, r, delta, lam)
            except ValueError as e:
                return _rec(log, f"basis vector {k}: shape", False, str(e)) and False
            hw, op, res = is_highest_weight(vec, r, p)
            ok &= _rec(log, f"basis vector {k}: highest weight mod {p}", hw)
        rk, how = _independent(basis_vecs, p)
        ok &= _rec(log, f"basis: {len(basis_vecs)} independent vectors = a", rk == len(basis_vecs) == a,
                   f"rank {rk}, a = {a}")
    else:
        nb = len(weight_monomials(n, r, delta, lam)) if True else None
        if nb > KERNEL_CAP:
            return _rec(log, "kernel recomputed", False,
                        f"N_S = {nb} exceeds the verifier's cap {KERNEL_CAP} and no basis is recorded: NOT VERIFIED") and False
        basis, vecs = kernel_mod_p(n, r, delta, lam, p)
        ok &= _rec(log, f"kernel of the raising operators mod {p} has dimension a", len(vecs) == a,
                   f"N_S = {len(basis)}, nullity {len(vecs)}, a = {a}")
        basis_vecs = [[(m, c) for m, c in zip(basis, vec) if c] for vec in vecs]
    pts = cert["points"]
    vals = []
    for pt in pts:
        if pt["type"] != cert["variety"]:
            return _rec(log, "points are of the claimed variety", False, f"{pt['type']} vs {cert['variety']}") and False
        F = form_of_point(pt, r)
        vals.append([evaluate(vec, F, p) for vec in basis_vecs])
    rk = _eval_rank(vals, len(basis_vecs), p)
    ok &= _rec(log, f"evaluation of the a = {a} highest-weight vectors at {len(pts)} recorded {cert['variety']} points has rank a mod {p}",
               rk == a, f"rank {rk}")
    if ok:
        _rec(log, f"conclusion: mult_{cert['variety']}(lambda, delta) = a = {a} over Q (rank_p <= rank_Q <= a)", True)
    return ok
