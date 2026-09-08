#!/usr/bin/env python3
"""
Session 69 -- the compact circuit: highest-weight vectors of Sym^delta(Sym^n C^r)
as bracket monomials (contractions), never as coordinate lists.

Specification: docs/compact_circuit.md.  Conventions (house, wk8_s30_core):
c_alpha(f) = coefficient of s^alpha in f;  E_ij c_alpha = (alpha_i+1) c_{alpha+e_i-e_j};
the letter symbol is  m_alpha := alpha! . c_alpha  (the polarised coefficient times n!).

A FILLING T of the diagram of lambda by delta letters, each used n times and never
twice in a column, defines the bracket monomial

    F_T(f) = sum_{sigma_1..sigma_{lambda_1}}  prod_j sgn(sigma_j)  prod_letters m_{alpha_l(sigma)}(f)

with sigma_j : rows of column j -> {1..h_j} a bijection, sgn w.r.t. the row order,
alpha_l(sigma) the multiplicity vector of the n indices at the cells of letter l.
F_T is a highest-weight vector of weight lambda (Identity 1 of the spec), and the
F_T span M_lambda (Identity 2).

This module handles the shapes of the LMR family,  lambda' = (h, h, 2^{n2}, 1^{n1}),
i.e. lambda = (2+n2+n1, 2+n2, 2^{h-2}):  two tall columns C1, C2 of height h, n2
two-columns, n1 one-columns.  Three evaluators of the SAME sum:

  * brute_force_eval  -- the Leibniz sum literally (tiny shapes; the definition);
  * fast_eval_py      -- Identity 3 (mixed-discriminant polarisation), flint dets;
  * fast_eval_c       -- the same in C (analysis/wk11_s69_eval.c), for n = 4.

Ranks/nullspaces by python-flint nmod_mat only.
"""
import ctypes
import itertools
import math
import os
import random
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import exps, restrict, det_form, P1, P2          # noqa: E402
from flint import nmod_mat                                          # noqa: E402

PRIMES = (P1, P2)


# ----------------------------------------------------------------------------- fillings
class Filling:
    """Two tall columns of height h (letters in row order), n2 two-columns as
    (letter at row 1, letter at row 2), n1 one-columns as a list of letters.
    n legs per letter, delta letters (0..delta-1)."""

    def __init__(self, h, n, delta, C1, C2, two, one):
        self.h, self.n, self.delta = h, n, delta
        self.C1, self.C2 = list(C1), list(C2)
        self.two = [tuple(e) for e in two]
        self.one = list(one)
        self.n2, self.n1 = len(self.two), len(self.one)
        self.validate()

    # lambda = (2 + n2 + n1, 2 + n2, 2^{h-2})
    @property
    def lam(self):
        return tuple([2 + self.n2 + self.n1, 2 + self.n2] + [2] * (self.h - 2))

    def validate(self):
        h, n, d = self.h, self.n, self.delta
        assert len(self.C1) == h and len(self.C2) == h
        assert len(set(self.C1)) == h and len(set(self.C2)) == h, "letter twice in a tall column"
        cnt = [0] * d
        for l in self.C1: cnt[l] += 1
        for l in self.C2: cnt[l] += 1
        for a, b in self.two:
            assert a != b, "letter twice in a 2-column"
            cnt[a] += 1; cnt[b] += 1
        for l in self.one: cnt[l] += 1
        assert all(c == n for c in cnt), ("every letter must have n legs", cnt)
        assert 2 * h + 2 * self.n2 + self.n1 == n * d

    @property
    def shared(self):
        return sorted(set(self.C1) & set(self.C2))

    def key(self):
        return (tuple(self.C1), tuple(self.C2), tuple(self.two), tuple(self.one))

    def to_json(self):
        return dict(h=self.h, n=self.n, delta=self.delta, C1=self.C1, C2=self.C2,
                    two=[list(e) for e in self.two], one=self.one, lam=list(self.lam))

    @staticmethod
    def from_json(d):
        return Filling(d["h"], d["n"], d["delta"], d["C1"], d["C2"], d["two"], d["one"])

    def cells_of_letter(self):
        """letter -> list of cells (column index, row index), columns 0 = C1, 1 = C2,
        2.. two-columns, then one-columns."""
        out = [[] for _ in range(self.delta)]
        for k, l in enumerate(self.C1): out[l].append((0, k))
        for k, l in enumerate(self.C2): out[l].append((1, k))
        for e, (a, b) in enumerate(self.two):
            out[a].append((2 + e, 0)); out[b].append((2 + e, 1))
        for c, l in enumerate(self.one): out[l].append((2 + self.n2 + c, 0))
        return out


def random_filling(h, n, delta, n2, n1, rng, k=None, max_tries=1000):
    """A uniformly-ish random column-strict filling of lambda' = (h,h,2^n2,1^n1).
    k = number of letters shared by the two tall columns (None = unconstrained)."""
    assert 2 * h + 2 * n2 + n1 == n * delta
    for _ in range(max_tries):
        letters = list(range(delta))
        C1 = rng.sample(letters, h)
        if k is None:
            C2 = rng.sample(letters, h)
        else:
            sh = rng.sample(C1, k)
            rest = [l for l in letters if l not in C1]
            if len(rest) < h - k: continue
            C2 = sh + rng.sample(rest, h - k)
            rng.shuffle(C2)
        rem = [n] * delta
        for l in C1: rem[l] -= 1
        for l in C2: rem[l] -= 1
        if min(rem) < 0: continue
        two = []
        ok = True
        for _e in range(n2):
            avail = [l for l in letters if rem[l] > 0]
            if len(avail) < 2: ok = False; break
            w = [rem[l] for l in avail]
            a = rng.choices(avail, weights=w)[0]
            avail2 = [l for l in avail if l != a]
            w2 = [rem[l] for l in avail2]
            b = rng.choices(avail2, weights=w2)[0]
            rem[a] -= 1; rem[b] -= 1
            two.append((a, b))
        if not ok: continue
        one = []
        for l in letters: one += [l] * rem[l]
        rng.shuffle(one)
        assert len(one) == n1
        try:
            return Filling(h, n, delta, C1, C2, two, one)
        except AssertionError:
            continue
    raise RuntimeError("no filling found")


# ----------------------------------------------------------------------------- symbols
def sym_table(n, r):
    """index of the exponent vector of any sorted n-tuple of indices in 0..r-1,
    and alpha! for each exponent vector."""
    A = exps(n, r)
    idx = {a: k for k, a in enumerate(A)}
    fact = [math.prod(math.factorial(x) for x in a) for a in A]
    tab = {}
    for tup in itertools.combinations_with_replacement(range(r), n):
        al = [0] * r
        for i in tup: al[i] += 1
        tab[tup] = idx[tuple(al)]
    return A, idx, fact, tab


def symbols_from_coeffs(cv, n, r, p):
    """m_alpha = alpha! c_alpha mod p, as a list over exps(n, r)."""
    A, idx, fact, tab = sym_table(n, r)
    return [(int(cv[a]) % p) * fact[a] % p for a in range(len(A))]


def generic_point(n, r, p, rng):
    """uniform random coefficient vector mod p (a generic form)."""
    return [rng.randrange(p) for _ in exps(n, r)]


def det_point(n, r, rng, bound=30):
    """integer coefficients of det_n(sum s_i A_i), A_i random integer n x n matrices
    (the same construction as wk9_s45_build.ev_rows_arr, same random stream shape)."""
    f, N = det_form(n)
    As = [[rng.randint(-bound, bound) for _ in range(N)] for _ in range(r)]
    co = restrict(f, N, n, r, As)
    A = exps(n, r)
    return [int(co.get(al, 0)) for al in A], As


# ----------------------------------------------------------------------------- brute force
def _perms_with_sign(h):
    out = []
    for perm in itertools.permutations(range(h)):
        s = 1
        for i in range(h):
            for j in range(i + 1, h):
                if perm[i] > perm[j]: s = -s
        out.append((perm, s))
    return out


def brute_force_eval(F, msym, p, tab=None):
    """the Leibniz sum, literally.  msym[a] = m_alpha mod p over exps(n, r); r >= h."""
    h, n, d = F.h, F.n, F.delta
    r = h
    if tab is None:
        _, _, _, tab = sym_table(n, r)
    perms = _perms_with_sign(h)
    cells = F.cells_of_letter()
    total = 0
    for s in range(1 << F.n2):
        ssign = (-1) ** bin(s).count("1")
        for p1, s1 in perms:
            for p2, s2 in perms:
                prod = ssign * s1 * s2
                for l in range(d):
                    ids = []
                    for (col, row) in cells[l]:
                        if col == 0: ids.append(p1[row])
                        elif col == 1: ids.append(p2[row])
                        elif col < 2 + F.n2:
                            e = col - 2
                            bit = (s >> e) & 1
                            ids.append(bit if row == 0 else 1 - bit)   # row-1 letter: index 1+bit
                        else: ids.append(0)
                    prod = prod * msym[tab[tuple(sorted(ids))]] % p
                    if prod == 0: break
                total = (total + prod) % p
    return total % p


# ----------------------------------------------------------------------------- identity 3
def unit_structure(F):
    """Row-units of C1: for C1 row k, either ('shared', letter) or ('pair', letter, partner)
    with partner in C2 only; the pairing is chosen to maximise 2-edges inside pairs.
    Returns (units, neither, pi_sign, pairs)."""
    h = F.h
    inC2 = {l: k for k, l in enumerate(F.C2)}
    U1 = [l for l in F.C1 if l not in inC2]
    U2 = [l for l in F.C2 if l not in set(F.C1)]
    assert len(U1) == len(U2)
    # multiplicity of 2-edges between letters
    ecount = {}
    for a, b in F.two:
        ecount[(a, b)] = ecount.get((a, b), 0) + 1
        ecount[(b, a)] = ecount.get((b, a), 0) + 1
    best, bestscore = None, -1
    if len(U1) <= 6:
        for perm in itertools.permutations(U2):
            sc = sum(ecount.get((a, b), 0) for a, b in zip(U1, perm))
            if sc > bestscore: best, bestscore = list(perm), sc
    else:  # greedy
        left = list(U2); best = []
        for a in U1:
            b = max(left, key=lambda x: ecount.get((a, x), 0))
            best.append(b); left.remove(b)
    partner = dict(zip(U1, best))
    units = []
    for k, l in enumerate(F.C1):
        if l in inC2: units.append(("shared", l))
        else: units.append(("pair", l, partner[l]))
    # pi: C1 row k -> C2 row of its C2 partner letter
    pi = [inC2[u[1]] if u[0] == "shared" else inC2[u[2]] for u in units]
    assert sorted(pi) == list(range(h))
    pi_sign = 1
    for i in range(h):
        for j in range(i + 1, h):
            if pi[i] > pi[j]: pi_sign = -pi_sign
    tall = set(F.C1) | set(F.C2)
    neither = [l for l in range(F.delta) if l not in tall]
    return units, neither, pi_sign, partner


def letter_tensors(F, msym, p, tab):
    """for each letter: (inC1, inC2, edge list [(edge id, side)], tensor) with
    tensor[(i, j, bits)] = m_alpha mod p; i (C1 index) and j (C2 index) range over
    0..h-1 or are absent; bits gives each 2-leg's index (0 -> '1', 1 -> '2')."""
    h = F.h
    cells = F.cells_of_letter()
    out = []
    for l in range(F.delta):
        inC1 = any(c == 0 for c, _ in cells[l])
        inC2 = any(c == 1 for c, _ in cells[l])
        edges = [(c - 2, row) for c, row in cells[l] if 2 <= c < 2 + F.n2]
        n1 = sum(1 for c, _ in cells[l] if c >= 2 + F.n2)
        d2 = len(edges)
        ri = range(h) if inC1 else [None]
        rj = range(h) if inC2 else [None]
        T = {}
        for i in ri:
            for j in rj:
                for bits in range(1 << d2):
                    ids = [0] * n1
                    if i is not None: ids.append(i)
                    if j is not None: ids.append(j)
                    for q in range(d2):
                        ids.append((bits >> q) & 1)
                    T[(i, j, bits)] = msym[tab[tuple(sorted(ids))]]
        out.append((inC1, inC2, edges, T))
    return out


def _det_mod(M, p):
    h = len(M)
    return int(nmod_mat(h, h, [int(x) % p for row in M for x in row], p).det())


def fast_eval_py(F, msym, p, tab=None):
    """Identity 3: F_T = sgn(pi) sum_s (-1)^|s| N(s) sum_{S subset [h]} (-1)^{h-|S|} det(sum_{k in S} M_k(s)).
    All 2-edges enumerated externally (2^n2 patterns); python-flint determinants."""
    h, n = F.h, F.n
    if tab is None:
        _, _, _, tab = sym_table(n, h)
    units, neither, pi_sign, _ = unit_structure(F)
    LT = letter_tensors(F, msym, p, tab)

    def bits_of(l, s):
        b = 0
        for q, (e, side) in enumerate(LT[l][2]):
            se = (s >> e) & 1
            idx = se if side == 0 else 1 - se
            b |= idx << q
        return b

    total = 0
    for s in range(1 << F.n2):
        ssign = -1 if bin(s).count("1") % 2 else 1
        N = 1
        for l in neither:
            N = N * LT[l][3][(None, None, bits_of(l, s))] % p
        if N == 0: continue
        Ms = []
        for u in units:
            if u[0] == "shared":
                l = u[1]; b = bits_of(l, s); T = LT[l][3]
                Ms.append([[T[(i, j, b)] for j in range(h)] for i in range(h)])
            else:
                l, m = u[1], u[2]
                bl, bm = bits_of(l, s), bits_of(m, s)
                v = [LT[l][3][(i, None, bl)] for i in range(h)]
                w = [LT[m][3][(None, j, bm)] for j in range(h)]
                Ms.append([[v[i] * w[j] % p for j in range(h)] for i in range(h)])
        acc = 0
        for S in range(1 << h):
            sm = [[0] * h for _ in range(h)]
            for k in range(h):
                if (S >> k) & 1:
                    Mk = Ms[k]
                    for i in range(h):
                        ri = sm[i]; mi = Mk[i]
                        for j in range(h): ri[j] += mi[j]
            dS = _det_mod(sm, p)
            if (h - bin(S).count("1")) % 2: dS = -dS
            acc += dS
        total = (total + ssign * N * acc) % p
    return pi_sign * total % p


# ----------------------------------------------------------------------------- C evaluator
_CLIB = None


def _clib():
    global _CLIB
    if _CLIB is None:
        so = os.path.join(HERE, "wk11_s69_eval.so")
        src = os.path.join(HERE, "wk11_s69_eval.c")
        if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
            os.system(f"gcc -O3 -march=native -shared -fPIC -o {so} {src}")
        _CLIB = ctypes.CDLL(so)
        _CLIB.eval_filling.restype = ctypes.c_longlong
    return _CLIB


def pack_for_c(F, msym, p, tab=None):
    """the flat integer description of (F, point) the C evaluator takes."""
    h, n = F.h, F.n
    if tab is None:
        _, _, _, tab = sym_table(n, h)
    units, neither, pi_sign, _ = unit_structure(F)
    LT = letter_tensors(F, msym, p, tab)
    d = F.delta
    # letters: inC1, inC2, d2, edges (id, side) padded to n, tensor offset
    maxd2 = n
    l_inC1 = np.zeros(d, np.int32); l_inC2 = np.zeros(d, np.int32); l_d2 = np.zeros(d, np.int32)
    l_edge = np.full((d, maxd2), -1, np.int32); l_side = np.zeros((d, maxd2), np.int32)
    l_off = np.zeros(d + 1, np.int64)
    tens = []
    for l in range(d):
        inC1, inC2, edges, T = LT[l]
        l_inC1[l] = inC1; l_inC2[l] = inC2; l_d2[l] = len(edges)
        for q, (e, side) in enumerate(edges):
            l_edge[l, q] = e; l_side[l, q] = side
        ni = h if inC1 else 1; nj = h if inC2 else 1
        l_off[l] = len(tens)
        for i in range(ni):
            for j in range(nj):
                for bits in range(1 << len(edges)):
                    tens.append(T[(i if inC1 else None, j if inC2 else None, bits)])
        l_off[l + 1] = len(tens)
    tens = np.array(tens, dtype=np.int64)
    u_type = np.zeros(h, np.int32); u_a = np.zeros(h, np.int32); u_b = np.zeros(h, np.int32)
    for k, u in enumerate(units):
        if u[0] == "shared": u_type[k] = 0; u_a[k] = u[1]; u_b[k] = -1
        else: u_type[k] = 1; u_a[k] = u[1]; u_b[k] = u[2]
    nei = np.array(neither, dtype=np.int32) if neither else np.zeros(0, np.int32)
    return dict(h=h, n=n, d=d, n2=F.n2, p=p, pi_sign=pi_sign, l_inC1=l_inC1, l_inC2=l_inC2,
                l_d2=l_d2, l_edge=l_edge, l_side=l_side, l_off=l_off, tens=tens,
                u_type=u_type, u_a=u_a, u_b=u_b, nei=nei)


def fast_eval_c(F, msym, p, tab=None):
    P = pack_for_c(F, msym, p, tab)
    lib = _clib()
    I32 = ctypes.POINTER(ctypes.c_int32); I64 = ctypes.POINTER(ctypes.c_int64)
    val = lib.eval_filling(
        ctypes.c_int(P["h"]), ctypes.c_int(P["d"]), ctypes.c_int(P["n2"]), ctypes.c_longlong(p),
        P["l_inC1"].ctypes.data_as(I32), P["l_inC2"].ctypes.data_as(I32), P["l_d2"].ctypes.data_as(I32),
        P["l_edge"].ctypes.data_as(I32), P["l_side"].ctypes.data_as(I32), ctypes.c_int(P["l_edge"].shape[1]),
        P["l_off"].ctypes.data_as(I64), P["tens"].ctypes.data_as(I64),
        P["u_type"].ctypes.data_as(I32), P["u_a"].ctypes.data_as(I32), P["u_b"].ctypes.data_as(I32),
        ctypes.c_int(len(P["nei"])), P["nei"].ctypes.data_as(I32))
    return P["pi_sign"] * int(val) % p


# ----------------------------------------------------------------------------- linear algebra
def rank_mod(rows, p):
    if not rows: return 0
    nc = len(rows[0])
    return nmod_mat(len(rows), nc, [int(x) % p for r in rows for x in r], p).rank()


def nullspace_mod(rows, nc, p):
    """basis of {x : rows x = 0} as python-int vectors."""
    M = nmod_mat(len(rows), nc, [int(x) % p for r in rows for x in r], p)
    X, nul = M.nullspace()
    return [[int(X[i, j]) for i in range(nc)] for j in range(nul)]


def left_kernel_mod(rows, p):
    """basis of {x : x^T rows = 0}: rows is a list of row vectors (fillings x points)."""
    nr = len(rows); nc = len(rows[0])
    T = [[rows[i][j] for i in range(nr)] for j in range(nc)]   # transpose: nc x nr
    return nullspace_mod(T, nr, p)


def rat_recon(a, m):
    if a == 0: return (0, 1)
    bound = math.isqrt(m // 2)
    r0, r1, s0, s1 = m, a % m, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound or math.gcd(r1, abs(s1)) != 1: return None
    if s1 < 0: r1, s1 = -r1, -s1
    return (r1, s1)


def reconstruct_integer_vector(vec_modp, p):
    """scale so that the first nonzero entry is 1, rational-reconstruct, clear denominators,
    make primitive.  None if reconstruction fails."""
    piv = next((c for c in vec_modp if c % p), None)
    if piv is None: return None
    inv = pow(piv, -1, p)
    fr = []
    for c in vec_modp:
        rr = rat_recon(c * inv % p, p)
        if rr is None: return None
        fr.append(rr)
    L = 1
    for _, den in fr: L = L * den // math.gcd(L, den)
    vint = [num * (L // den) for num, den in fr]
    g = 0
    for x in vint: g = math.gcd(g, abs(x))
    if g > 1: vint = [x // g for x in vint]
    return vint
