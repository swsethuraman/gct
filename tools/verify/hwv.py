"""Highest-weight vectors in C[Sym^n C^r]_delta, written from scratch for the
verifier.  Nothing here is imported from analysis/.

Conventions (these are the conventions the declared format requires, and the
verifier checks a certificate against them and nothing else):

  * coordinates: c_alpha(F) = the coefficient of s^alpha in the form F,
    alpha an exponent tuple of length r with |alpha| = n;
  * a term is a multiset {alpha^1, ..., alpha^delta} with an integer
    coefficient, standing for coeff * prod_j c_{alpha^j};
  * the weight of a term is sum_j alpha^j (componentwise), and a vector of
    weight lambda has every term of weight lambda;
  * the Lie algebra gl_r acts on the c_alpha by
        E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}      (0 if alpha_j = 0)
    extended to products as a derivation.  This is the action induced by
    (g.F)(s) = F(g^{-1} s) when c_alpha is the plain coefficient (see FORMAT.md
    for the one-line derivation and the discriminant check);
  * a highest-weight vector is annihilated by every simple raising operator
    E_{i,i+1}, i = 1..r-1 (which generate the raising operators).
"""


def term_weight(alphas):
    r = len(alphas[0])
    return tuple(sum(a[i] for a in alphas) for i in range(r))


def canonical_term(alphas):
    """sorted tuple of exponent tuples (the multiset in canonical order)."""
    return tuple(sorted(tuple(a) for a in alphas))


def check_vector_shape(vec, n, r, delta, lam):
    """Structural checks; raises ValueError with the reason on failure."""
    if not vec:
        raise ValueError("empty vector")
    lam = tuple(lam)
    seen = set()
    for alphas, coeff in vec:
        if len(alphas) != delta:
            raise ValueError(f"term has {len(alphas)} factors, degree claimed {delta}")
        for a in alphas:
            if len(a) != r:
                raise ValueError(f"exponent tuple of length {len(a)}, r = {r}")
            if any((x < 0) for x in a) or sum(a) != n:
                raise ValueError(f"exponent tuple {a} is not of degree {n}")
        if term_weight(alphas) != lam:
            raise ValueError(f"term of weight {term_weight(alphas)} != lambda {lam}")
        key = canonical_term(alphas)
        if key != tuple(alphas):
            raise ValueError("term not in canonical (sorted) order")
        if key in seen:
            raise ValueError("duplicate term")
        seen.add(key)
        if coeff == 0:
            raise ValueError("zero coefficient recorded")


def apply_raising(vec, i, j, modulus=None):
    """E_ij applied to the vector (list of (alphas, coeff)); returns a dict
    canonical term -> coefficient (nonzero entries only)."""
    out = {}
    for alphas, coeff in vec:
        for pos, a in enumerate(alphas):
            if a[j] == 0:
                continue
            factor = a[i] + 1
            b = list(a)
            b[i] += 1
            b[j] -= 1
            new = list(alphas)
            new[pos] = tuple(b)
            key = tuple(sorted(new))
            v = out.get(key, 0) + coeff * factor
            if modulus is not None:
                v %= modulus
            if v:
                out[key] = v
            elif key in out:
                del out[key]
    return out


def is_highest_weight(vec, r, modulus=None):
    """Returns (ok, first failing operator index or None, size of the residual)."""
    for i in range(r - 1):
        res = apply_raising(vec, i, i + 1, modulus)
        if res:
            return False, (i + 1, i + 2), len(res)
    return True, None, 0


def star_support(vec, k=1):
    """Theorem (star) support condition for the locus {l^k * c}: every term has,
    for every variable index i, a factor alpha with alpha_i <= k-1.  Returns the
    number of terms violating it."""
    bad = 0
    for alphas, coeff in vec:
        r = len(alphas[0])
        for i in range(r):
            if not any(a[i] <= k - 1 for a in alphas):
                bad += 1
                break
    return bad


def evaluate(vec, F, modulus=None):
    """Value of the vector at the form F (dict exponent tuple -> int)."""
    tot = 0
    for alphas, coeff in vec:
        v = coeff
        for a in alphas:
            c = F.get(a, 0)
            if c == 0:
                v = 0
                break
            v *= c
        tot += v
        if modulus is not None:
            tot %= modulus
    return tot


def support_size(vec):
    return len(vec)
