"""Session 73 -- shared helpers for the n = 3 D-ladder on (3 delta - 17, 7, 2^5).

Everything here is glue around the validated instruments:

  * wk9_s45_build.build_cell(lam, delta, n=3)      the chi-isotypic build (E, arrays)
  * wk9_s45_build.ev_rows_arr                         chi-coordinate evaluation rows
  * wk9_s45_cell.nullity_stacked                      the s42/s45 Wiedemann certificates
  * wk8_s30_core.det_form(3) / per_form(3)            the two cubics in Sym^3 C^9

plus the session's own pieces: exact (over Z) evaluation of integer chi-vectors,
rational reconstruction, the monomial expansion of chi-vectors (for hwv
certificates), and the first-row transport J: V_chi(delta) -> V_chi(delta+1),
multiplication by c_{(3,0,...,0)}, computed at the monomial level.

chi-coordinates (wk9_s45_build.orbit_setup_arr): a monomial m (row of arr['M'],
delta indices into exps(3, 7)) has coefficient  vec[col_of[m]] * sgn[m]  in the
expansion of the chi-vector vec over the weight-lambda monomial basis; col_of = -1
and sgn = 0 on the dropped orbits.
"""
import json
import math
import os
import random
import sys
import time
from fractions import Fraction

import numpy as np
from scipy import sparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
os.environ.setdefault("WIED_BIN", "/home/claude/wied73")
os.environ.setdefault("WIED_WORK", "/home/claude/s73/work")

from wk8_s30_core import exps, restrict, det_form, per_form, P1, P2   # noqa: E402
from wk9_s42_orbits import _codes                                      # noqa: E402

N_DEG = 3            # det_3 / per_3 are cubics
R = 7                # s_1..s_7
NENT = 9             # 3x3 matrix entries
DET3, _ = det_form(3)
PER3, _ = per_form(3)
FORMS = dict(det=DET3, per=PER3)
PRIMES = (P1, P2)
SESSION_SEED = 20260908
SEEDS = dict(det=SESSION_SEED, per=SESSION_SEED + 1000,
             det2=SESSION_SEED + 2000, per2=SESSION_SEED + 3000,
             fresh_det=SESSION_SEED + 4000, fresh_per=SESSION_SEED + 5000,
             fresh_generic=SESSION_SEED + 6000)
BOUND = 40
A_EXPS = exps(N_DEG, R)
L_EXPS = len(A_EXPS)
ALPHA0 = tuple([N_DEG] + [0] * (R - 1))
IDX_ALPHA0 = A_EXPS.index(ALPHA0)
LOCAL = "/home/claude/s73"
ART = os.path.join(ROOT, "results", "artefacts")
CERTS = os.path.join(ROOT, "results", "certs", "s73")
LOGS = os.path.join(ROOT, "results", "logs")

T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def lam_of(delta):
    return (3 * delta - 17, 7, 2, 2, 2, 2, 2)


def a_two_ways(lam, delta):
    """the ambient multiplicity by the from-scratch verifier DP and by the house
    Weyl alternation; asserted equal."""
    from pleth import ambient_multiplicity
    from wk9_s42_census import a_weyl
    a1 = ambient_multiplicity(lam, delta, n=N_DEG)
    a2 = a_weyl(lam, delta, N_DEG, {})
    assert a1 == a2, ("a disagrees between engines", lam, delta, a1, a2)
    return int(a1)


# ------------------------------------------------------------ points
def pencils(K, seed, bound=BOUND):
    """K integer 7-pencils of 3x3 matrices, as lists of 7 flat 9-vectors (the
    wk8_s30_core.restrict layout: As[i][t] = entry t of A_i, t = 3a + b)."""
    rnd = random.Random(seed)
    return [[[rnd.randint(-bound, bound) for _ in range(NENT)] for _ in range(R)] for _ in range(K)]


def pencil_record(pen):
    """substitution data for a certificate: r matrices, each 3x3 (rows)."""
    return [[[int(A[3 * a + b]) for b in range(3)] for a in range(3)] for A in pen]


def coeffs_of(form, pen):
    """coefficient dict {alpha: int} of form(sum_i s_i A_i)."""
    return restrict(form, NENT, N_DEG, R, pen)


def ev_rows_from_pencils(arr, form, pens, prime, chunk=2_000_000):
    """chi-coordinate evaluation rows at explicit pencils (the numpy kernel of
    wk9_s45_build.ev_rows_arr, with the point drawn outside)."""
    from wk9_s45_build import _grouping
    M = arr['M']; sgn = arr['sgn']; n_chi = arr['n_chi']
    mem, starts = _grouping(arr)
    out = []
    for pen in pens:
        co = coeffs_of(form, pen)
        cv = np.zeros(L_EXPS, dtype=np.int64)
        for a, al in enumerate(A_EXPS):
            cv[a] = co.get(al, 0) % prime
        row = np.zeros(n_chi, dtype=np.int64)
        for b0 in range(0, len(mem), chunk):
            mm = mem[b0:b0 + chunk]
            term = cv[M[mm, 0]].copy()
            for k in range(1, M.shape[1]):
                term *= cv[M[mm, k]]
                term %= prime
            term *= sgn[mm]
            term %= prime
            s0 = np.searchsorted(starts, b0, side='right') - 1
            s1 = np.searchsorted(starts, b0 + len(mm), side='left')
            loc = np.maximum(starts[s0:s1] - b0, 0)
            np.add.at(row, np.arange(s0, s1), np.add.reduceat(term, loc) % prime)
            del term, mm, loc
        out.append((row % prime).astype(np.int64))
    return np.array(out, dtype=np.int64).reshape(len(pens), n_chi)


# ------------------------------------------------------------ exact arithmetic
def rat_recon(a, m):
    if a == 0:
        return Fraction(0)
    bound = int(math.isqrt(m // 2))
    r0, r1, s0, s1 = m, a % m, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound or math.gcd(r1, abs(s1)) != 1:
        return None
    return Fraction(r1, s1)


def reconstruct_integer(vec_modp, p):
    """normalise by the first nonzero coordinate, rationally reconstruct every
    coordinate, clear denominators, divide by the content.  None if any
    coordinate fails to reconstruct."""
    piv = next((c for c in vec_modp if c % p), None)
    if piv is None:
        return None
    inv = pow(int(piv), -1, p)
    fr = []
    for c in vec_modp:
        r = rat_recon(int(c) * inv % p, p)
        if r is None:
            return None
        fr.append(r)
    Lc = 1
    for f in fr:
        Lc = Lc * f.denominator // math.gcd(Lc, f.denominator)
    vint = [int(f * Lc) for f in fr]
    g = 0
    for x in vint:
        g = math.gcd(g, abs(x))
    if g > 1:
        vint = [x // g for x in vint]
    # sign convention: first nonzero coordinate positive
    for x in vint:
        if x:
            if x < 0:
                vint = [-y for y in vint]
            break
    return vint


def sparse_dot_exact(E, vint):
    """E @ v over Z for a scipy sparse E with small integer entries and v a list
    of Python ints (accumulated over the COO entries with big-int arithmetic)."""
    C = E.tocoo()
    out = [0] * C.shape[0]
    for i, j, d in zip(C.row.tolist(), C.col.tolist(), C.data.tolist()):
        vj = vint[j]
        if vj:
            out[i] += int(d) * vj
    return out


def _mono_support(arr, vint):
    """(rows of M, integer coefficient) for every monomial with nonzero
    coefficient in the expansion of the integer chi-vector vint."""
    M = arr['M']; sgn = arr['sgn']; col_of = arr['col_of']
    sel = np.nonzero(col_of >= 0)[0]
    vv = np.array(vint, dtype=object)
    coef = vv[col_of[sel]] * sgn[sel].astype(object)
    nz = np.array([bool(c) for c in coef], dtype=bool)
    return M[sel[nz]], coef[nz]


def eval_exact(arr, vint, coeff_dict):
    """value over Z of the integer chi-vector vint at the form with the given
    coefficient dict (a point of Sym^3 C^7)."""
    Msel, coef = _mono_support(arr, vint)
    cv = [int(coeff_dict.get(al, 0)) for al in A_EXPS]
    total = 0
    d = Msel.shape[1]
    for row in range(Msel.shape[0]):
        c = int(coef[row])
        prod = 1
        for k in range(d):
            prod *= cv[int(Msel[row, k])]
            if prod == 0:
                break
        total += c * prod
    return total


def eval_exact_many(arr, vint, coeff_dicts):
    Msel, coef = _mono_support(arr, vint)
    d = Msel.shape[1]
    rows = [(int(coef[i]), Msel[i].tolist()) for i in range(Msel.shape[0])]
    vals = []
    for co in coeff_dicts:
        cv = [int(co.get(al, 0)) for al in A_EXPS]
        total = 0
        for c, mono in rows:
            prod = c
            for k in mono:
                prod *= cv[k]
                if prod == 0:
                    break
            total += prod
        vals.append(total)
    return vals


def generic_cubics(K, seed, bound=BOUND):
    rnd = random.Random(seed)
    return [{al: rnd.randint(-bound, bound) for al in A_EXPS} for _ in range(K)]


def expand_terms_int(arr, vint):
    """integer chi-vector -> canonical hwv-certificate term list
    [[alpha_1, ..., alpha_delta], coeff] over the monomial basis (sorted, distinct)."""
    Msel, coef = _mono_support(arr, vint)
    terms = []
    for i in range(Msel.shape[0]):
        terms.append([[list(A_EXPS[k]) for k in Msel[i].tolist()], int(coef[i])])
    terms.sort(key=lambda t: t[0])
    return terms


# ------------------------------------------------------------ chi-basis bookkeeping
def chi_reps(arr):
    """(reps, sgn_rep): for every chi-column its representative monomial (the
    minimum-index member of the orbit, as delta indices into exps) and the sign
    of that representative."""
    if 'reps' in arr:
        return arr['reps'], arr['sgn_rep']
    M = arr['M']; col_of = arr['col_of']; sgn = arr['sgn']; n_chi = arr['n_chi']
    sel = np.nonzero(col_of >= 0)[0]          # increasing monomial index
    cols = col_of[sel]
    order = np.argsort(cols, kind='stable')   # stable: within a column, increasing index
    cs = cols[order]
    starts = np.searchsorted(cs, np.arange(n_chi))
    first = sel[order[starts]]                # the minimum-index monomial of every kept orbit
    assert np.array_equal(cols[order[starts]], np.arange(n_chi))
    reps = np.ascontiguousarray(M[first], dtype=np.int32)
    srep = sgn[first].astype(np.int64)
    arr['reps'] = reps; arr['sgn_rep'] = srep
    return reps, srep


def ufree_columns(arr):
    """chi-columns whose monomials carry no factor c_{(3,0,...,0)} (the u-free
    part; c is stabiliser-fixed so the property is constant on orbits)."""
    reps, _ = chi_reps(arr)
    return np.nonzero(~(reps == IDX_ALPHA0).any(axis=1))[0]


def save_build(delta, B):
    """the arrays a later rung needs for the transport check (local only; big)."""
    os.makedirs(LOCAL, exist_ok=True)
    arr = B['arr']
    np.savez(os.path.join(LOCAL, f"build_d{delta}.npz"), M=arr['M'], col_of=arr['col_of'].astype(np.int32),
             sgn=arr['sgn'].astype(np.int8), n_chi=np.int64(arr['n_chi']), N_S=np.int64(arr['N_S']),
             stab=np.int64(arr['stab']))
    sparse.save_npz(os.path.join(LOCAL, f"E_d{delta}.npz"), B['E'].tocsr())


def load_build(delta):
    z = np.load(os.path.join(LOCAL, f"build_d{delta}.npz"))
    arr = dict(M=z['M'], col_of=z['col_of'].astype(np.int64), sgn=z['sgn'].astype(np.int64),
               n_chi=int(z['n_chi']), N_S=int(z['N_S']), stab=int(z['stab']))
    E = sparse.load_npz(os.path.join(LOCAL, f"E_d{delta}.npz")).tocsr()
    return arr, E


# ------------------------------------------------------------ transport
class Lookup:
    """monomial (delta indices, sorted) -> row of arr['M'], by the multiset
    combinadic code of wk9_s42_orbits."""
    def __init__(self, arr):
        self.M = arr['M']
        codes = _codes(self.M, L_EXPS)
        self.order = np.argsort(codes, kind='stable')
        self.sorted = codes[self.order]
        assert np.all(np.diff(self.sorted) > 0)

    def rows(self, monos):
        c = _codes(np.ascontiguousarray(monos, dtype=np.int32), L_EXPS)
        p = np.searchsorted(self.sorted, c)
        ok = (p < len(self.sorted))
        ok[ok] = self.sorted[p[ok]] == c[ok]
        out = np.full(len(c), -1, dtype=np.int64)
        out[ok] = self.order[p[ok]]
        return out


def transport(arr_lo, look_lo, arr_hi, vec_lo, modulus=None):
    """J(vec): multiply the chi-vector vec (rung delta, arrays arr_lo) by
    c_{(3,0,...,0)} and express it in the chi-coordinates of rung delta+1
    (arrays arr_hi).  vec_lo may be a list of Python ints (exact) or an int64
    array mod `modulus`.  Returns the chi-vector at delta+1 in the same kind."""
    reps_hi, sgn_hi = chi_reps(arr_hi)
    n_hi = reps_hi.shape[0]
    has = (reps_hi == IDX_ALPHA0).any(axis=1)
    idx_has = np.nonzero(has)[0]
    # remove one copy of alpha0 from each representative that carries it
    lo_monos = np.zeros((len(idx_has), reps_hi.shape[1] - 1), dtype=np.int32)
    for t, j in enumerate(idx_has.tolist()):
        row = reps_hi[j].tolist()
        row.remove(IDX_ALPHA0)
        lo_monos[t] = row
    rows_lo = look_lo.rows(lo_monos)
    assert np.all(rows_lo >= 0), "transported representative is not a weight-lambda monomial of the lower rung"
    col_lo = arr_lo['col_of'][rows_lo]
    s_lo = arr_lo['sgn'][rows_lo]
    if modulus is None:
        out = [0] * n_hi
        for t, j in enumerate(idx_has.tolist()):
            cl = int(col_lo[t])
            if cl >= 0:
                out[j] = int(vec_lo[cl]) * int(s_lo[t]) * int(sgn_hi[j])
        return out
    out = np.zeros(n_hi, dtype=np.int64)
    v = np.asarray(vec_lo, dtype=np.int64) % modulus
    keep = col_lo >= 0
    out[idx_has[keep]] = (v[col_lo[keep]] * s_lo[keep] * sgn_hi[idx_has[keep]]) % modulus
    return out


def check_hwv_modp(E, nc, p, vec):
    from wk9_s45_cell import check_kernel_full
    return check_kernel_full(E, nc, p, [int(x) % p for x in vec])


def rank_modp(vectors, nc, p):
    from flint import nmod_mat
    if not vectors:
        return 0
    return nmod_mat(len(vectors), nc, [int(v) % p for vec in vectors for v in vec], p).rank()


def proportional_modp(u, v, p):
    """u ~ v mod p (rank of the 2 x n stack is <= 1) and both nonzero."""
    nc = len(u)
    return rank_modp([u, v], nc, p) == 1 and rank_modp([u], nc, p) == 1 and rank_modp([v], nc, p) == 1


def dump_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=1)
