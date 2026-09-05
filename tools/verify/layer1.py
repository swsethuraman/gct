"""Layer 1 -- syntactic checks on serialised integer matrices, exact.

  * rank over Q         : exact, by the multimodular argument -- rank_p at any
                          prime is a lower bound; all (r0+1)-minors vanish over
                          Z once they vanish modulo a set of primes whose
                          product exceeds twice their Hadamard bound, which
                          proves the upper bound (flint fmpz_mat.rank() is
                          exact too but takes minutes at 300 x 400)
  * rank modulo primes  : flint nmod_mat.rank() at every recorded prime, and at
                          the two house primes whenever they are not recorded
  * a non-vanishing minor: flint fmpz_mat.det() of the named square submatrix
  * a nullity-zero claim : nmod_mat rank == number of columns at the named prime

Matrices are given dense (list of rows) or sparse ({"shape": [m, n],
"entries": [[i, j, v], ...]}), or built from a declared source (a Macaulay
matrix of the partials of a determinantal pencil), in which case the matrix
recorded in the certificate, if any, must coincide with the rebuilt one.
Nothing here is imported from analysis/.
"""
import math
from flint import fmpz_mat, nmod_mat
from forms import det_pencil_form, poly_degree_check

HOUSE_PRIMES = (2147483647, 2147483629)


def to_dense(mat):
    """mat: dense list-of-lists or sparse dict -> (rows, m, n) with rows a list of
    lists of python ints."""
    if isinstance(mat, dict):
        if set(mat.keys()) != {"shape", "entries"}:
            raise ValueError("sparse matrix must have exactly the keys shape, entries")
        m, n = mat["shape"]
        if not (isinstance(m, int) and isinstance(n, int) and m > 0 and n > 0):
            raise ValueError("bad shape")
        rows = [[0] * n for _ in range(m)]
        for e in mat["entries"]:
            if not (isinstance(e, list) and len(e) == 3):
                raise ValueError("sparse entry must be [i, j, v]")
            i, j, v = e
            if not (isinstance(i, int) and isinstance(j, int) and isinstance(v, int)):
                raise ValueError("sparse entry must be integers")
            if not (0 <= i < m and 0 <= j < n):
                raise ValueError("sparse entry out of range")
            if rows[i][j] != 0:
                raise ValueError("sparse entry recorded twice")
            rows[i][j] = v
        return rows, m, n
    if not isinstance(mat, list) or not mat:
        raise ValueError("dense matrix must be a nonempty list of rows")
    n = None
    for row in mat:
        if not isinstance(row, list) or not row:
            raise ValueError("dense matrix row must be a nonempty list")
        if n is None:
            n = len(row)
        elif len(row) != n:
            raise ValueError("ragged dense matrix")
        for v in row:
            if not isinstance(v, int) or isinstance(v, bool):
                raise ValueError("matrix entries must be integers")
    return [list(r) for r in mat], len(mat), n


def _primes_62bit(bits_needed):
    """descending probable primes just below 2^62 until sum log2 > bits_needed."""
    from flint import fmpz
    out, acc, q = [], 0.0, 2 ** 62 - 1
    while acc <= bits_needed:
        if fmpz(q).is_probable_prime():
            out.append(q)
            acc += math.log2(q)
        q -= 2
    return out


def hadamard_bits(rows, k):
    """log2 of a bound on every k x k minor: the product of the k largest row
    2-norms (each minor's rows are sub-rows of these)."""
    norms = sorted((sum(v * v for v in r) for r in rows), reverse=True)[:k]
    return sum(0.5 * math.log2(s) for s in norms if s > 0)


def rank_Q(rows, tiny=48):
    """Exact rank over Q.  Small matrices: flint fmpz_mat.rank().  Otherwise the
    multimodular certificate: r0 = rank at the first prime (a lower bound), then
    every (r0+1)-minor vanishes modulo each of enough 62-bit primes to exceed
    twice its Hadamard bound, so it vanishes over Z (upper bound).  Returns
    (rank, number of primes used)."""
    m, n = len(rows), len(rows[0])
    if max(m, n) <= tiny:
        return fmpz_mat(m, n, [v for r in rows for v in r]).rank(), 0
    from flint import fmpz
    q = 2 ** 62 - 1
    while not fmpz(q).is_probable_prime():
        q -= 2
    return rank_Q_from(rows, rank_mod(rows, q))


def rank_Q_from(rows, r0):
    m, n = len(rows), len(rows[0])
    if r0 == min(m, n):
        return r0, 1                     # full rank: nothing to certify
    bits = 1 + hadamard_bits(rows, r0 + 1)
    primes = _primes_62bit(bits)
    for p in primes:
        rp = rank_mod(rows, p)
        if rp > r0:
            # a prime saw a larger rank: the lower bound rises and the
            # certificate is redone at the new size
            return rank_Q_from(rows, rp)
    return r0, len(primes)


def rank_mod(rows, p):
    m, n = len(rows), len(rows[0])
    return nmod_mat(m, n, [v % p for r in rows for v in r], p).rank()


def minor_det(rows, ri, ci, tiny=48):
    """Exact determinant of the named square submatrix over Z: flint for small
    minors, otherwise Chinese remaindering of nmod_mat determinants over enough
    62-bit primes to exceed twice the Hadamard bound (then the symmetric
    residue is the determinant)."""
    if len(ri) != len(ci) or not ri:
        raise ValueError("a minor needs equally many rows and columns, at least one")
    k = len(ri)
    sub = [[rows[i][j] for j in ci] for i in ri]
    if k <= tiny:
        return int(fmpz_mat(k, k, [v for r in sub for v in r]).det())
    bits = 1 + hadamard_bits(sub, k)
    primes = _primes_62bit(bits)
    x, mod = 0, 1
    for p in primes:
        dp = int(nmod_mat(k, k, [v % p for r in sub for v in r], p).det())
        t = ((dp - x) * pow(mod, -1, p)) % p
        x += mod * t
        mod *= p
    x %= mod
    return x - mod if x > mod // 2 else x


# ------------------------------------------------ declared matrix sources
def monomials(r, d):
    if r == 1:
        return [(d,)]
    out = []
    for a in range(d, -1, -1):
        for rest in monomials(r - 1, d - a):
            out.append((a,) + rest)
    return out


def macaulay_matrix(F, n, r, d):
    """M_d(F): rows (i, m) for i = 1..r and m a monomial of degree d-n+1, columns
    the monomials of degree d, entry the coefficient of the column monomial in
    m * dF/ds_i.  Row order: i outer, m inner in the order of monomials();
    column order: monomials(r, d)."""
    cols = monomials(r, d)
    cidx = {c: t for t, c in enumerate(cols)}
    rows = []
    for i in range(r):
        part = {}
        for k, v in F.items():
            if k[i] > 0:
                kk = list(k)
                kk[i] -= 1
                part[tuple(kk)] = v * k[i]
        for m in monomials(r, d - n + 1):
            row = [0] * len(cols)
            for k, v in part.items():
                row[cidx[tuple(x + y for x, y in zip(k, m))]] = v
            rows.append(row)
    return rows


def build_from_source(src):
    """src = {"type": "macaulay_det_pencil", "n": 4, "r": r, "d": d, "pencil": [...]}."""
    if not isinstance(src, dict) or src.get("type") != "macaulay_det_pencil":
        raise ValueError("unknown matrix source type")
    if set(src.keys()) != {"type", "n", "r", "d", "pencil"}:
        raise ValueError("matrix source must have exactly the keys type, n, r, d, pencil")
    n, r, d = src["n"], src["r"], src["d"]
    if n != 4:
        raise ValueError("only det_4 pencils are declared")
    F = det_pencil_form(src["pencil"], r)
    poly_degree_check(F, n, r)
    if d < n - 1:
        raise ValueError("Macaulay degree below n-1")
    return macaulay_matrix(F, n, r, d)


def check_matrix_certificate(cert, log):
    """Runs every layer-1 check present in the certificate; appends
    (name, ok, detail) triples to log; returns True iff all pass."""
    ok_all = True

    def rec(name, ok, detail=""):
        nonlocal ok_all
        ok_all &= bool(ok)
        log.append((name, bool(ok), detail))

    rows = None
    if "matrix_source" in cert:
        built = build_from_source(cert["matrix_source"])
        rec("source: matrix rebuilt from the recorded pencil", True,
            f"shape {len(built)}x{len(built[0])}")
        if "matrix" in cert:
            given, m, n = to_dense(cert["matrix"])
            same = (m == len(built) and n == len(built[0]) and given == built)
            rec("source: recorded matrix equals the rebuilt one", same)
            if not same:
                return False
        rows = built
    else:
        rows, m, n = to_dense(cert["matrix"])
    m, n = len(rows), len(rows[0])
    rec("shape", True, f"{m}x{n}")

    if "claimed_rank_Q" in cert:
        rq, used = rank_Q(rows)
        rec("rank over Q (exact, multimodular certificate)", rq == cert["claimed_rank_Q"],
            f"computed {rq} ({used} certificate primes), claimed {cert['claimed_rank_Q']}")
    primes_done = {}
    if "claimed_ranks_mod_p" in cert:
        for ps, rk in cert["claimed_ranks_mod_p"].items():
            p = int(ps)
            got = rank_mod(rows, p)
            primes_done[p] = got
            rec(f"rank mod {p}", got == rk, f"computed {got}, claimed {rk}")
    for p in HOUSE_PRIMES:
        if p not in primes_done:
            primes_done[p] = rank_mod(rows, p)
            rec(f"rank mod {p} (house prime, not claimed)", True, f"computed {primes_done[p]}")
    if len(primes_done) < 2:
        rec("at least two distinct primes", False)
    if "claimed_rank_Q" in cert:
        rec("mod-p ranks do not exceed the rank over Q",
            all(v <= cert["claimed_rank_Q"] for v in primes_done.values()))
    if "nonvanishing_minor" in cert:
        mn = cert["nonvanishing_minor"]
        if set(mn.keys()) != {"rows", "cols"}:
            raise ValueError("nonvanishing_minor must have exactly rows, cols")
        dv = minor_det(rows, mn["rows"], mn["cols"])
        rec(f"minor {len(mn['rows'])}x{len(mn['rows'])} is nonzero over Z", dv != 0, f"det = {dv}")
    if "nullity_zero" in cert:
        nz = cert["nullity_zero"]
        if set(nz.keys()) != {"prime"}:
            raise ValueError("nullity_zero must have exactly the key prime")
        p = int(nz["prime"])
        got = rank_mod(rows, p)
        rec(f"nullity zero modulo {p}", got == n, f"rank {got} of {n} columns at prime {p}")
    return ok_all
