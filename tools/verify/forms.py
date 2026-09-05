"""Forms and their coefficients, written from scratch for the verifier.

Nothing here is imported from analysis/.  A form in r variables s_1..s_r is a
dict {exponent tuple (length r): integer coefficient}; c_alpha(F) is the plain
coefficient of s^alpha in F.  Everything is exact over Z; a modulus may be
applied at the end by the caller.

The three families of evaluation points the programme uses:

  det pencil     F(s) = det_4( sum_i s_i A_i ),        A_i in Z^{4x4}
  padded per_3   F(s) = x_0(s) * per_3( X(s) ),        x_0, X_11..X_33 linear forms in s
  reducible      F(s) = l(s) * c(s),                    l linear, c a cubic

The padded permanent is the restriction of the ten-variable form
x_0 * per_3(x_1..x_9) along a linear map C^r -> C^10 given by ten linear forms.
"""
import itertools


def _add_into(acc, key, val):
    v = acc.get(key, 0) + val
    if v:
        acc[key] = v
    elif key in acc:
        del acc[key]


def poly_mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            _add_into(out, tuple(x + y for x, y in zip(ka, kb)), va * vb)
    return out


def poly_add(a, b, scale=1):
    out = dict(a)
    for k, v in b.items():
        _add_into(out, k, scale * v)
    return out


def poly_degree_check(F, deg, r):
    for k, v in F.items():
        if len(k) != r or sum(k) != deg or any(x < 0 for x in k):
            raise ValueError(f"form is not homogeneous of degree {deg} in {r} variables: {k}")


def linear_form(coeffs):
    """coeffs: list of r integers -> the linear form sum coeffs[i] s_i."""
    r = len(coeffs)
    out = {}
    for i, c in enumerate(coeffs):
        if c:
            out[tuple(1 if t == i else 0 for t in range(r))] = c
    return out


def det_of_linear_matrix(entries):
    """entries: n x n nested list of forms (dicts).  Laplace expansion along the
    first row, exact.  Returns a form."""
    n = len(entries)
    for row in entries:
        if len(row) != n:
            raise ValueError("matrix is not square")

    def rec(rows, cols):
        if len(rows) == 1:
            return entries[rows[0]][cols[0]]
        tot = {}
        i = rows[0]
        for k, j in enumerate(cols):
            e = entries[i][j]
            if not e:
                continue
            sub = rec(rows[1:], cols[:k] + cols[k + 1:])
            tot = poly_add(tot, poly_mul(e, sub), scale=(-1) ** k)
        return tot

    return rec(list(range(n)), list(range(n)))


def per_of_linear_matrix(entries):
    """permanent of an n x n matrix of forms, by Laplace expansion (no signs)."""
    n = len(entries)
    for row in entries:
        if len(row) != n:
            raise ValueError("matrix is not square")

    def rec(rows, cols):
        if len(rows) == 1:
            return entries[rows[0]][cols[0]]
        tot = {}
        i = rows[0]
        for k, j in enumerate(cols):
            e = entries[i][j]
            if not e:
                continue
            sub = rec(rows[1:], cols[:k] + cols[k + 1:])
            tot = poly_add(tot, poly_mul(e, sub))
        return tot

    return rec(list(range(n)), list(range(n)))


def det_pencil_form(pencil, r):
    """pencil: list of r integer 4x4 matrices A_1..A_r.  Returns det_4(sum s_i A_i)."""
    if len(pencil) != r:
        raise ValueError(f"pencil has {len(pencil)} matrices, expected r = {r}")
    n = len(pencil[0])
    if n != 4 or any(len(A) != 4 or any(len(row) != 4 for row in A) for A in pencil):
        raise ValueError("pencil matrices must be 4x4")
    entries = [[linear_form([pencil[k][i][j] for k in range(r)]) for j in range(4)]
               for i in range(4)]
    F = det_of_linear_matrix(entries)
    poly_degree_check(F, 4, r)
    return F


def padded_permanent_form(lin, r):
    """lin: ten integer vectors of length r, the linear forms x_0, x_1..x_9 in s.
    Returns x_0(s) * per_3(X(s)) with X_{ab} = x_{1 + 3a + b}."""
    if len(lin) != 10 or any(len(v) != r for v in lin):
        raise ValueError("padded-permanent point needs ten linear forms of length r")
    x0 = linear_form(lin[0])
    X = [[linear_form(lin[1 + 3 * a + b]) for b in range(3)] for a in range(3)]
    F = poly_mul(x0, per_of_linear_matrix(X))
    poly_degree_check(F, 4, r)
    return F


def reducible_form(l, cubic, r):
    """l: integer vector of length r; cubic: {exponent tuple: int} of degree 3."""
    poly_degree_check(cubic, 3, r)
    F = poly_mul(linear_form(l), cubic)
    poly_degree_check(F, 4, r)
    return F


def ten_variable_padded_permanent():
    """The full x_0 * per_3(x_1..x_9) as a form in 10 variables (no restriction)."""
    ident = [[1 if i == j else 0 for j in range(10)] for i in range(10)]
    return padded_permanent_form(ident, 10)


def coefficient(F, alpha):
    return F.get(tuple(alpha), 0)


def reduce_mod(F, p):
    return {k: v % p for k, v in F.items() if v % p}
