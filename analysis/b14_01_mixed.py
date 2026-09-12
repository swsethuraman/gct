#!/usr/bin/env python3
"""B14-01 -- the MIXED-LETTER bracket evaluator.

Two letter types on one diagram:  `l` of valence 1, `c` of valence 3, on the
shape  lambda' = (h, h, 2^n2, 1^n1).  At h = 9, n2 = 15, n1 = 4 this is
lambda = (21,17,2^7) = lambda_13; at n1 = 8 it is lambda = (25,17,2^7).

The object.  nu : (l, c) |-> l.c pulls degree-delta forms on quartics back to
bidegree (delta, delta) functions of (l, c), i.e. into
Sym^delta(V*) (x) Sym^delta((Sym^3 V)*).  A filling of lambda' by delta
valence-1 letters and delta valence-3 letters, column-strict, gives by the same
Leibniz alternation as the uniform case a highest-weight vector of weight lambda
in that space.  These are the members of the normalisation target N_delta.

Conventions, per letter type, stated separately (board slot 1 requires this):

  l-letter, valence 1: one leg, at index i.  Symbol  m_{e_i}(l) = 1! * l_i = l_i.
  c-letter, valence 3: three legs (i,j,k).   Symbol  m_alpha(c) = alpha! * c_alpha,
                                             alpha the multiplicity vector.
  Both: no letter twice in a column.  The delta letters of one type are
  interchangeable and the SAME form is substituted into every one of them.

Every coefficient is resolved by  exps(v, r).index(alpha)  -- never positionally.
wk8_s30_core.exps runs the first exponent UP from 0 while the point files run it
DOWN from n; the two orderings are opposite and three sessions have paid for it.

The C core wk12_s74_dpc.c is reused unchanged.  Compatibility is argued from its
source (the valence `n` appears nowhere in it; 1-column legs are folded into the
tensor VALUE by the packer, never into an index) and is discharged empirically by
brute_vs_dp() -- the literal Leibniz sum against the C core on small mixed shapes.
"""
import ctypes, itertools, math, os, random, sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk8_s30_core import exps, P1, P2                      # noqa: E402
from wk12_s74_dp import _lib as _dpc_lib                   # noqa: E402
from flint import nmod_mat                                 # noqa: E402

PRIMES = (P1, P2)


# --------------------------------------------------------------------- symbols
_STAB = {}

def sym_table_v(v, r):
    """(A, idx, fact, tab) for valence v in r variables; tab: sorted v-tuple -> row of A."""
    k = (v, r)
    if k not in _STAB:
        A = exps(v, r)
        idx = {a: i for i, a in enumerate(A)}
        fact = [math.prod(math.factorial(x) for x in a) for a in A]
        tab = {}
        for tup in itertools.combinations_with_replacement(range(r), v):
            al = [0] * r
            for i in tup:
                al[i] += 1
            tab[tup] = idx[tuple(al)]
        _STAB[k] = (A, idx, fact, tab)
    return _STAB[k]


def msym_linear(lin, r, p, scale_factorial=True):
    """m_alpha for a linear form.  lin[i] = coefficient of x_i (the point-file
    convention, verified against u_symbol).  Resolved by exps(1,r).index."""
    A, idx, fact, _ = sym_table_v(1, r)
    out = []
    for k, a in enumerate(A):
        i = a.index(1)
        f = fact[k] if scale_factorial else 1
        out.append(int(lin[i]) % p * f % p)
    return out


def msym_cubic(cmap, r, p, scale_factorial=True):
    """m_alpha for a cubic.  cmap: exponent tuple -> coefficient.  Resolved by
    exps(3,r).index, never positionally."""
    A, idx, fact, _ = sym_table_v(3, r)
    out = []
    for k, a in enumerate(A):
        f = fact[k] if scale_factorial else 1
        out.append(int(cmap.get(a, 0)) % p * f % p)
    return out


# --------------------------------------------------------------------- fillings
class MixedFilling:
    """lambda' = (h, h, 2^n2, 1^n1).  Letters 0..d-1 with valences val[l] in {1,3}.
    Columns: 0 = C1, 1 = C2, 2..2+n2-1 = two-columns, then the one-columns."""

    def __init__(self, h, n2, n1, val, C1, C2, two, one):
        self.h, self.n2, self.n1 = h, n2, n1
        self.val = list(val)
        self.d = len(self.val)
        self.C1, self.C2 = list(C1), list(C2)
        self.two = [tuple(e) for e in two]
        self.one = list(one)
        self.validate()

    @property
    def lam(self):
        return tuple([2 + self.n2 + self.n1, 2 + self.n2] + [2] * (self.h - 2))

    def validate(self):
        h, d = self.h, self.d
        assert len(self.C1) == h and len(self.C2) == h, "tall column height"
        assert len(set(self.C1)) == h, "letter twice in C1"
        assert len(set(self.C2)) == h, "letter twice in C2"
        assert len(self.two) == self.n2 and len(self.one) == self.n1
        cnt = [0] * d
        for l in self.C1: cnt[l] += 1
        for l in self.C2: cnt[l] += 1
        for a, b in self.two:
            assert a != b, "letter twice in a 2-column"
            cnt[a] += 1; cnt[b] += 1
        for l in self.one: cnt[l] += 1
        assert cnt == self.val, ("leg count != valence", cnt, self.val)
        assert 2 * h + 2 * self.n2 + self.n1 == sum(self.val)

    def key(self):
        return (tuple(self.C1), tuple(self.C2), tuple(self.two), tuple(self.one), tuple(self.val))

    def to_json(self):
        return dict(h=self.h, n2=self.n2, n1=self.n1, val=self.val, C1=self.C1,
                    C2=self.C2, two=[list(e) for e in self.two], one=self.one,
                    lam=list(self.lam))

    @staticmethod
    def from_json(j):
        return MixedFilling(j["h"], j["n2"], j["n1"], j["val"], j["C1"], j["C2"], j["two"], j["one"])

    def cells_of_letter(self):
        out = [[] for _ in range(self.d)]
        for k, l in enumerate(self.C1): out[l].append((0, k))
        for k, l in enumerate(self.C2): out[l].append((1, k))
        for e, (a, b) in enumerate(self.two):
            out[a].append((2 + e, 0)); out[b].append((2 + e, 1))
        for c, l in enumerate(self.one): out[l].append((2 + self.n2 + c, 0))
        return out


# --------------------------------------------------------------------- tensors
def letter_tensors_mixed(F, msym_by_val, p, r=None):
    """per letter: (inC1, inC2, edges, T) with T[(i,j,bits)] = m_alpha mod p.
    1-column legs contribute index 0 each and are folded into the VALUE."""
    h = F.h
    r = r or h
    cells = F.cells_of_letter()
    out = []
    for l in range(F.d):
        v = F.val[l]
        _, _, _, tab = sym_table_v(v, r)
        ms = msym_by_val[v]
        inC1 = any(c == 0 for c, _ in cells[l])
        inC2 = any(c == 1 for c, _ in cells[l])
        edges = [(c - 2, row) for c, row in cells[l] if 2 <= c < 2 + F.n2]
        n1c = sum(1 for c, _ in cells[l] if c >= 2 + F.n2)
        d2 = len(edges)
        assert (1 if inC1 else 0) + (1 if inC2 else 0) + d2 + n1c == v, "leg bookkeeping"
        ri = range(h) if inC1 else [None]
        rj = range(h) if inC2 else [None]
        T = {}
        for i in ri:
            for j in rj:
                for bits in range(1 << d2):
                    ids = [0] * n1c
                    if i is not None: ids.append(i)
                    if j is not None: ids.append(j)
                    for q in range(d2):
                        ids.append((bits >> q) & 1)
                    T[(i, j, bits)] = ms[tab[tuple(sorted(ids))]]
        out.append((inC1, inC2, edges, T))
    return out


# --------------------------------------------------------------------- brute force
def _perms_with_sign(h):
    out = []
    for perm in itertools.permutations(range(h)):
        s = 1
        for i in range(h):
            for j in range(i + 1, h):
                if perm[i] > perm[j]: s = -s
        out.append((perm, s))
    return out


def brute_force_mixed(F, msym_by_val, p, r=None):
    """the Leibniz sum, literally -- the definition, for small shapes only."""
    h, d = F.h, F.d
    r = r or h
    perms = _perms_with_sign(h)
    cells = F.cells_of_letter()
    tabs = {v: sym_table_v(v, r)[3] for v in set(F.val)}
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
                            bit = (s >> (col - 2)) & 1
                            ids.append(bit if row == 0 else 1 - bit)
                        else: ids.append(0)
                    prod = prod * msym_by_val[F.val[l]][tabs[F.val[l]][tuple(sorted(ids))]] % p
                    if prod == 0: break
                total = (total + prod) % p
    return total % p


# --------------------------------------------------------------------- DP packing
def letter_order_mixed(F, rng=None, restarts=50):
    """processing order minimising simultaneously-open 2-columns (valence-agnostic)."""
    d = F.d
    adj = [[] for _ in range(d)]
    for e, (a, b) in enumerate(F.two):
        adj[a].append((e, b)); adj[b].append((e, a))

    def run(start, rng_):
        done = [False] * d; order = []; open_e = set(); W = 0; cur = start
        while len(order) < d:
            done[cur] = True; order.append(cur)
            for e, other in adj[cur]:
                if done[other]: open_e.discard(e)
                else: open_e.add(e)
            W = max(W, len(open_e))
            if len(order) == d: break
            best, bestv = None, None
            cand = [l for l in range(d) if not done[l]]
            if rng_ is not None: rng_.shuffle(cand)
            for l in cand:
                v = len(open_e)
                for e, other in adj[l]:
                    v += -1 if done[other] else 1
                if bestv is None or v < bestv: best, bestv = l, v
            cur = best
        return order, W

    best = None
    for s0 in range(d):
        o, W = run(s0, None)
        if best is None or W < best[1]: best = (o, W)
    rng_ = rng or random.Random(0)
    for _ in range(restarts):
        o, W = run(rng_.randrange(d), rng_)
        if W < best[1]: best = (o, W)
    return best


_ORDER_CACHE = {}

def cached_order_mixed(F):
    k = F.key()
    if k not in _ORDER_CACHE:
        if len(_ORDER_CACHE) > 20000: _ORDER_CACHE.clear()
        _ORDER_CACHE[k] = letter_order_mixed(F)
    return _ORDER_CACHE[k]


def mixed_dp_pack(F, msym_by_val, p, r=None, order=None):
    """exactly dp_pack's layout and signs, with per-letter valences."""
    h = F.h
    r = r or h
    if order is None:
        order, _W = cached_order_mixed(F)
    LT = letter_tensors_mixed(F, msym_by_val, p, r)
    d = F.d
    first = [None] * F.n2; firstside = [0] * F.n2; slot = [-1] * F.n2
    free_slots = []; nslots = 0
    for t, l in enumerate(order):
        edges = LT[l][2]
        freed = [slot[e] for e, sd in edges if first[e] is not None and first[e] != t]
        for e, sd in edges:
            if first[e] is None:
                first[e] = t; firstside[e] = sd
                if free_slots: slot[e] = free_slots.pop()
                else: slot[e] = nslots; nslots += 1
        free_slots += freed
    W = nslots
    maxd2 = max(F.val) if F.val else 1
    l_inC1 = np.zeros(d, np.int32); l_inC2 = np.zeros(d, np.int32); l_d2 = np.zeros(d, np.int32)
    l_edge = np.full((d, maxd2), -1, np.int32); l_side = np.zeros((d, maxd2), np.int32)
    l_off = np.zeros(d + 1, np.int64); tens = []
    for t, l in enumerate(order):
        inC1, inC2, edges, T = LT[l]
        l_inC1[t] = inC1; l_inC2[t] = inC2; l_d2[t] = len(edges)
        for q, (e, sd) in enumerate(edges):
            l_edge[t, q] = e; l_side[t, q] = sd
        ni = h if inC1 else 1; nj = h if inC2 else 1
        l_off[t] = len(tens)
        for i in range(ni):
            for j in range(nj):
                for bits in range(1 << len(edges)):
                    tens.append(T[(i if inC1 else None, j if inC2 else None, bits)])
        l_off[t + 1] = len(tens)
    tens = np.array(tens, dtype=np.int64)

    def rho_sign(col):
        rows = [col.index(l) for l in order if l in col]
        s = 1
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                if rows[i] > rows[j]: s = -s
        return s

    sign = rho_sign(F.C1) * rho_sign(F.C2)
    return dict(h=h, d=d, n2=F.n2, W=W, p=p, sign=sign, order=order,
                l_inC1=l_inC1, l_inC2=l_inC2, l_d2=l_d2, l_edge=l_edge, l_side=l_side,
                l_off=l_off, tens=tens, slot=np.array(slot, np.int32),
                first=np.array(first, np.int32), firstside=np.array(firstside, np.int32))


def mixed_eval_c(F, msym_by_val, p, r=None, order=None, max_W=8):
    P = mixed_dp_pack(F, msym_by_val, p, r, order)
    if P["W"] > max_W:
        raise RuntimeError(f"pathwidth W={P['W']} exceeds max_W={max_W}")
    lib = _dpc_lib()
    I32 = ctypes.POINTER(ctypes.c_int32); I64 = ctypes.POINTER(ctypes.c_int64)
    val = lib.dp_eval_compact(
        ctypes.c_int(P["h"]), ctypes.c_int(P["d"]), ctypes.c_int(P["n2"]),
        ctypes.c_int(P["W"]), ctypes.c_longlong(p),
        P["l_inC1"].ctypes.data_as(I32), P["l_inC2"].ctypes.data_as(I32), P["l_d2"].ctypes.data_as(I32),
        P["l_edge"].ctypes.data_as(I32), P["l_side"].ctypes.data_as(I32), ctypes.c_int(P["l_edge"].shape[1]),
        P["l_off"].ctypes.data_as(I64), P["tens"].ctypes.data_as(I64),
        P["slot"].ctypes.data_as(I32), P["first"].ctypes.data_as(I32), P["firstside"].ctypes.data_as(I32))
    assert val >= 0, "dp_eval_compact failed (allocation)"
    return P["sign"] * int(val) % p


# --------------------------------------------------------------------- linear algebra
def rank_mod(rows, p):
    if not rows: return 0
    nc = len(rows[0])
    return nmod_mat(len(rows), nc, [int(x) % p for r in rows for x in r], p).rank()


# --------------------------------------------------------------------- samplers
def random_mixed_filling(h, n2, n1, n_ell, n_c, rng, max_tries=400, ell_cells=None):
    """A random column-strict mixed filling.  Letters 0..n_ell-1 have valence 1,
    letters n_ell..n_ell+n_c-1 have valence 3.

    ell_cells (optional, the strip-directed mode): a list of cells
    (col, row) that must carry the valence-1 letters, one each.  Columns are
    0 = C1, 1 = C2, 2..2+n2-1 = two-columns, then the one-columns."""
    val = [1] * n_ell + [3] * n_c
    assert 2 * h + 2 * n2 + n1 == n_ell + 3 * n_c, "box count != leg count"
    ncol = 2 + n2 + n1
    for _try in range(max_tries):
        rem = list(val)
        cell_letter = {}
        ok = True
        if ell_cells is not None:
            if len(ell_cells) != n_ell: raise ValueError("ell_cells length")
            for li, cell in enumerate(ell_cells):
                cell_letter[cell] = li
                rem[li] -= 1
        # column -> its rows, tallest first (most constrained)
        cols = [(0, list(range(h))), (1, list(range(h)))]
        cols += [(2 + e, [0, 1]) for e in range(n2)]
        cols += [(2 + n2 + c, [0]) for c in range(n1)]
        for col, rows in cols:
            used = {cell_letter[(col, rw)] for rw in rows if (col, rw) in cell_letter}
            for rw in rows:
                if (col, rw) in cell_letter: continue
                avail = [l for l in range(len(val)) if rem[l] > 0 and l not in used]
                # a valence-1 letter not pinned by ell_cells may still be placed freely
                if not avail: ok = False; break
                w = [rem[l] for l in avail]
                l = rng.choices(avail, weights=w)[0]
                cell_letter[(col, rw)] = l; rem[l] -= 1; used.add(l)
            if not ok: break
        if not ok or any(rem): continue
        C1 = [cell_letter[(0, k)] for k in range(h)]
        C2 = [cell_letter[(1, k)] for k in range(h)]
        two = [(cell_letter[(2 + e, 0)], cell_letter[(2 + e, 1)]) for e in range(n2)]
        one = [cell_letter[(2 + n2 + c, 0)] for c in range(n1)]
        try:
            return MixedFilling(h, n2, n1, val, C1, C2, two, one)
        except AssertionError:
            continue
    raise RuntimeError("no mixed filling found")


def strips(lam, delta):
    """all mu with lam/mu a horizontal delta-strip: lam_{i+1} <= mu_i <= lam_i,
    mu weakly decreasing, |mu| = |lam| - delta."""
    r = len(lam); out = []
    def rec(i, cur, left):
        if i == r:
            if left == 0: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        hi = lam[i]
        if cur: hi = min(hi, cur[-1])
        for v in range(lo, hi + 1):
            if left - v < 0: continue
            rec(i + 1, cur + [v], left - v)
    rec(0, [], sum(lam) - delta)
    return out


def strip_ell_cells(lam, mu, h, n2, n1, rng=None):
    """the cells of lam/mu, expressed in the evaluator's column layout.
    Row 1 excess sits in one-columns, row 2 excess in two-columns (row index 1),
    row h excess in the tall columns (row index h-1).  Equal-height columns are
    interchangeable, so which ones carry the excess is a free choice."""
    n_one = lam[0] - mu[0]
    n_two = lam[1] - mu[1]
    n_tall = (lam[h - 1] - mu[h - 1]) if h - 1 < len(mu) else lam[h - 1]
    for i in range(2, h - 1):
        if lam[i] != mu[i]:
            raise ValueError("strip touches a middle row; not in this layout")
    assert 0 <= n_one <= n1 and 0 <= n_two <= n2 and 0 <= n_tall <= 2, (n_one, n_two, n_tall)
    onecols = list(range(2 + n2, 2 + n2 + n1))
    twocols = list(range(2, 2 + n2))
    tallcols = [0, 1]
    if rng is not None:
        rng.shuffle(onecols); rng.shuffle(twocols); rng.shuffle(tallcols)
    cells = [(c, 0) for c in onecols[:n_one]]
    cells += [(c, 1) for c in twocols[:n_two]]
    cells += [(c, h - 1) for c in tallcols[:n_tall]]
    return cells
