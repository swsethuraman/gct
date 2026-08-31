#!/usr/bin/env python3
"""
Session 27 -- independent implementation of the isotypic rank algorithm.

For a form f of degree n on C^N and a weight lam of length r:

    mult_lam C[closure(GL_N . f)]_delta  =  mult of S_lam(C^r) in C[D_r^f]_delta
    D_r^f = closure{ (s_1..s_r) |-> f(s_1 A_1 + ... + s_r A_r) } in Sym^n C^r

(session 26 Prop. 5; the short-weight reduction).  We compute the right side:

  * monomial basis of the weight-lam subspace of Sym^delta(Sym^n C^r), in the
    coefficient functionals c_alpha (alpha of degree n in r variables);
  * R  = matrix of the simple raising operators E_{i,i+1};  a = dim ker R;
  * E  = evaluation of each monomial at points F_j = f(sum s_i A_i^{(j)});
  * mult = rank([R;E]) - rank(R).

Written from the algorithm statement, not from analysis/wk6_s26_hwv.py.
"""
import itertools, random
from fractions import Fraction
from functools import lru_cache

P1, P2 = (1 << 61) - 1, 2305843009213693951 - 60   # two large primes
P2 = 2147483647

# ------------------------------------------------------------------ exponents
@lru_cache(maxsize=None)
def exps(n, r):
    """exponent vectors of degree n in r variables, as tuples."""
    out = []
    def rec(k, left, cur):
        if k == r - 1:
            out.append(tuple(cur + [left])); return
        for v in range(left + 1):
            rec(k + 1, left - v, cur + [v])
    rec(0, n, [])
    return tuple(out)

@lru_cache(maxsize=None)
def monomials(n, r, delta, lam):
    """multisets (as sorted index tuples) of delta exponent vectors summing to lam."""
    A = exps(n, r)
    L = len(A)
    lam = tuple(lam) + (0,) * (r - len(lam))
    out = []
    def rec(start, left, rem, cur):
        if left == 0:
            if all(x == 0 for x in rem): out.append(tuple(cur))
            return
        for i in range(start, L):
            al = A[i]
            if any(al[j] > rem[j] for j in range(r)): continue
            # prune: remaining budget must still be reachable
            if sum(rem) != left * n: return
            rec(i, left - 1, tuple(rem[j] - al[j] for j in range(r)), cur + [i])
    if sum(lam) != delta * n: return ()
    rec(0, delta, lam, [])
    return tuple(out)

# --------------------------------------------------------- raising operators
def raise_monomial(mon, i, j, n, r):
    """E_{ij} applied to the monomial (a derivation); returns list of (coef, mon)."""
    A = exps(n, r)
    idx = {a: k for k, a in enumerate(A)}
    out = []
    for pos in range(len(mon)):
        al = A[mon[pos]]
        if al[j] == 0: continue
        nb = list(al); nb[j] -= 1; nb[i] += 1
        k = idx[tuple(nb)]
        nm = tuple(sorted(mon[:pos] + (k,) + mon[pos + 1:]))
        out.append((al[j], nm))
    return out

def build_R(n, r, delta, lam):
    """matrix of the simple raising operators on the weight-lam space."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    basis = monomials(n, r, delta, lam)
    pos = {m: c for c, m in enumerate(basis)}
    rows = []
    for i in range(r - 1):
        j = i + 1
        tgt = tuple(lam[k] + (1 if k == i else (-1 if k == j else 0))
                    for k in range(r))
        if tgt[j] < 0: continue
        tb = monomials(n, r, delta, tgt)
        tp = {m: c for c, m in enumerate(tb)}
        acc = {}
        for m in basis:
            for coef, nm in raise_monomial(m, i, j, n, r):
                acc.setdefault(tp[nm], {})[pos[m]] = \
                    acc.setdefault(tp[nm], {}).get(pos[m], 0) + coef
        rows += list(acc.values())
    return basis, rows

# ------------------------------------------------------------- evaluation
def restrict(f_coeffs, N, n, r, As):
    """f is given as dict beta -> coef on C^N (beta a degree-n exponent vector).
    Return dict alpha -> coef of the r-ary form f(sum s_i A_i)."""
    out = {}
    for beta, cf in f_coeffs.items():
        # product over the N coordinates of ( sum_i s_i A_i[t] )^{beta_t}
        cur = {tuple([0]*r): cf}
        for t in range(N):
            for _ in range(beta[t]):
                nxt = {}
                for al, c in cur.items():
                    for i in range(r):
                        v = As[i][t]
                        if v == 0: continue
                        k = list(al); k[i] += 1; k = tuple(k)
                        nxt[k] = nxt.get(k, 0) + c * v
                cur = nxt
        for al, c in cur.items():
            out[al] = out.get(al, 0) + c
    return out

def eval_row(basis, coeffs, n, r):
    A = exps(n, r)
    row = []
    for m in basis:
        v = 1
        for k in m:
            v *= coeffs.get(A[k], 0)
            if v == 0: break
        row.append(v)
    return row

# ------------------------------------------------------------------- ranks
def rank_mod(rows, ncols, p):
    M = []
    for rw in rows:
        if isinstance(rw, dict):
            v = [0]*ncols
            for c, x in rw.items(): v[c] = x % p
            M.append(v)
        else:
            M.append([x % p for x in rw])
    rk, m = 0, len(M)
    for col in range(ncols):
        piv = next((i for i in range(rk, m) if M[i][col]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][col], p - 2, p)
        for i in range(rk + 1, m):
            if M[i][col]:
                f = M[i][col] * inv % p
                Mr, Mi = M[rk], M[i]
                for k in range(col, ncols):
                    if Mr[k]: Mi[k] = (Mi[k] - f * Mr[k]) % p
        rk += 1
        if rk == m: break
    return rk

def rank_QQ(rows, ncols):
    M = []
    for rw in rows:
        if isinstance(rw, dict):
            v = [Fraction(0)]*ncols
            for c, x in rw.items(): v[c] = Fraction(x)
            M.append(v)
        else:
            M.append([Fraction(x) for x in rw])
    rk, m = 0, len(M)
    for col in range(ncols):
        piv = next((i for i in range(rk, m) if M[i][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]
        for i in range(rk + 1, m):
            if M[i][col] != 0:
                f = M[i][col] / pv
                for k in range(col, ncols): M[i][k] -= f * M[rk][k]
        rk += 1
        if rk == m: break
    return rk

# ------------------------------------------------------------------ driver
def measure(f_coeffs, N, n, r, delta, lam, npts=None, seed=11, exact=False,
            bound=40):
    lam = tuple(lam) + (0,) * (r - len(lam))
    basis, R = build_R(n, r, delta, lam)
    nb = len(basis)
    if nb == 0: return dict(a=0, mult=0, nbasis=0)
    rk_R = rank_mod(R, nb, P1)
    a = nb - rk_R
    if a == 0: return dict(a=0, mult=0, nbasis=nb)
    rnd = random.Random(seed)
    K = npts if npts else a + 6
    ev = []
    for _ in range(K):
        As = [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]
        ev.append(eval_row(basis, restrict(f_coeffs, N, n, r, As), n, r))
    both = list(R) + ev
    m1 = rank_mod(both, nb, P1) - rk_R
    m2 = rank_mod(both, nb, P2) - (nb - (nb - rank_mod(R, nb, P2)))
    res = dict(a=a, mult=m1, mult_p2=m2, nbasis=nb)
    if exact:
        res['mult_QQ'] = rank_QQ(both, nb) - rank_QQ(R, nb)
    return res

# ---------------------------------------------------------------- the forms
def det_form(k):
    """det_k as a dict on C^(k*k), coordinate (i*k+j) = entry (i,j)."""
    import itertools as it
    out = {}
    for perm in it.permutations(range(k)):
        sgn = 1
        p = list(perm)
        for i in range(k):
            for j in range(i + 1, k):
                if p[i] > p[j]: sgn = -sgn
        beta = [0] * (k * k)
        for i in range(k): beta[i * k + perm[i]] += 1
        out[tuple(beta)] = out.get(tuple(beta), 0) + sgn
    return out, k * k

def per_form(k):
    import itertools as it
    out = {}
    for perm in it.permutations(range(k)):
        beta = [0] * (k * k)
        for i in range(k): beta[i * k + perm[i]] += 1
        out[tuple(beta)] = out.get(tuple(beta), 0) + 1
    return out, k * k

def per_padded(k, N=None):
    """x_0 . per_k on C^(1+k*k) (coordinate 0 is the padding variable)."""
    base, nb = per_form(k)
    N = N or (1 + nb)
    out = {}
    for beta, c in base.items():
        nbta = [0] * N
        nbta[0] = 1
        for t in range(nb): nbta[1 + t] = beta[t]
        out[tuple(nbta)] = c
    return out, N
