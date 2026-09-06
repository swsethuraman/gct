#!/usr/bin/env python3
"""
Session 58 -- symmetric rectangular Kronecker coefficients by a first-row reduction.

    sk(lam, n x delta) = < chi^lam , Sym^2 chi^{(delta^n)} >
                       = (1/2) [ g(lam, mu, mu) + A(lam, mu) ],   mu = (delta^n), N = n*delta,

    g(lam, mu, mu)  = sum_rho chi^lam(rho) chi^mu(rho)^2 / z_rho        (Kronecker)
    A(lam, mu)      = sum_rho chi^lam(rho) chi^mu(rho^2) / z_rho        (Adams pairing;
                                                                        rho^2 = cycle type of sigma^2)

This is the house `m_det` of scripts/ambient_screen.py.  Every earlier route
sums over all partitions of N.  The route here (results/PREREG_s58.md section 1)
expands s_lam by Jacobi-Trudi along its first row,

    s_lam = sum_j (-1)^j h_{lam_1 + j} s_{tail / (1^j)},     tail = (lam_2, lam_3, ...),

and uses, for the rectangle mu, Frobenius reciprocity plus c^mu_{alpha beta} = [beta = complement of alpha]:

    < h_k s_tau , s_mu * s_mu >  = sum_{beta |- |tau|, beta in the n x delta box} g(tau, beta, beta),
    < h_k s_tau , psi^2 chi^mu > = sum_{beta ...}                                 A(tau, beta),

(the second uses that every Frobenius-Schur indicator of S_k is 1).  Hence

    g(lam,mu,mu) = sum_{(j,tau)} (-1)^j sum_{beta in B_{|tau|}} g(tau,beta,beta),
    A(lam,mu)    = sum_{(j,tau)} (-1)^j sum_{beta in B_{|tau|}} A(tau,beta),

with tau running over the partitions obtained from the tail by removing a vertical
strip of j boxes, and B_m = { beta |- m : ell(beta) <= n, beta_1 <= delta }.  The
inner sums are class sums over S_m, m <= |tail|: the cost depends on the TAIL and on
n, and on N only through beta_1 <= delta, which is vacuous once delta >= |tail|.

Two other routes live in this file for cross-checking and share no logic with the
reduction beyond the partition utilities:

  * `sk_brute`  -- the plain partition sum over S_N with a fresh Murnaghan-Nakayama
                   (bead masks), the definition itself;
  * `sk_pieri`  -- the same reduction organised the other way round (Pieri inversion
                   of h_{lam_1} s_tail, recursing on the tail), a different combination
                   of the inner class sums.

Characters are exact integers (bead-mask Murnaghan-Nakayama, one depth-first pass
over the trie of partitions of m with parts ascending, so that common small parts
share work and the whole block of rows {chi^beta : beta in a box} is produced at
once).  The pairings are exact integer dot products (python-flint fmpz_mat when
available, Python integers otherwise); every division by m! is asserted exact.

Usage
    wk9_s58_sk.py cell  <lam as a|b|c...> <delta> [--n 4] [--brute] [--house] [--pieri]
    wk9_s58_sk.py calibrate            # PREREG_s58 M1 (brief table, screens, samples, brute force)
    wk9_s58_sk.py longweight [--delta 8,9] [--limit K] [--tag T] [--reverse]   # M1, the long-weight screen
    wk9_s58_sk.py sumrule <N> [--n 4] [--brute]   # sum rules over all lam |- N
    wk9_s58_sk.py costcurve            # PREREG M2
    wk9_s58_sk.py target               # PREREG M3 and M5 (goal cell + stability probe)
"""
import sys, os, time, json
from math import factorial

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
sys.setrecursionlimit(100000)

try:
    import flint
    HAVE_FLINT = True
except Exception:          # pragma: no cover
    HAVE_FLINT = False


# ---------------------------------------------------------------- partitions
def partitions(n, maxp=None):
    """Partitions of n as weakly decreasing tuples, largest part first."""
    if maxp is None or maxp > n:
        maxp = n
    if n == 0:
        yield ()
        return
    for k in range(maxp, 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


_PN = {}


def num_partitions(n):
    """p(n), by Euler's pentagonal recurrence (cached)."""
    if n < 0:
        return 0
    if n in _PN:
        return _PN[n]
    for k in range(len(_PN), n + 1):
        if k == 0:
            _PN[0] = 1
            continue
        tot, j = 0, 1
        while True:
            g1 = j * (3 * j - 1) // 2
            g2 = j * (3 * j + 1) // 2
            if g1 > k:
                break
            sgn = 1 if j % 2 else -1
            tot += sgn * _PN[k - g1]
            if g2 <= k:
                tot += sgn * _PN[k - g2]
            j += 1
        _PN[k] = tot
    return _PN[n]


def partitions_in_box(m, rows, cols):
    """Partitions of m with at most `rows` parts, each at most `cols`."""
    def rec(n, maxp, left):
        if n == 0:
            yield ()
            return
        if left == 0:
            return
        for k in range(min(maxp, n), 0, -1):
            if k * left < n:
                break
            for rest in rec(n - k, k, left - 1):
                yield (k,) + rest
    if m < 0 or m > rows * cols:
        return []
    return list(rec(m, cols, rows))


def sub_partitions(lam):
    """All partitions contained in lam (as tuples without trailing zeros)."""
    lam = tuple(x for x in lam if x)
    out = []
    def rec(i, prev, cur):
        if i == len(lam):
            out.append(tuple(x for x in cur if x))
            return
        for v in range(min(lam[i], prev), -1, -1):
            rec(i + 1, v, cur + [v])
    rec(0, lam[0] if lam else 0, [])
    return out


def conjugate(lam):
    lam = [x for x in lam if x]
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x > i) for i in range(lam[0]))


def zee(rho):
    z, cnt = 1, {}
    for p in rho:
        cnt[p] = cnt.get(p, 0) + 1
    for p, m in cnt.items():
        z *= p ** m * factorial(m)
    return z


def square_type(rho):
    """Cycle type of sigma^2 for sigma of cycle type rho."""
    out = []
    for r in rho:
        if r % 2:
            out.append(r)
        else:
            out += [r // 2, r // 2]
    return tuple(sorted(out, reverse=True))


def vertical_strips(lam, j):
    """Partitions tau contained in lam with lam/tau a vertical strip of j boxes.

    A vertical strip removes at most one box per row; the result is a partition iff,
    within every maximal run of equal rows, the rows losing a box are a bottom
    segment of the run.  So enumerate per run how many rows (from the bottom) lose a
    box: polynomially many choices, never 2^(rows)."""
    lam = tuple(x for x in lam if x)
    runs = []                                   # (row length, run length) top to bottom
    for x in lam:
        if runs and runs[-1][0] == x:
            runs[-1][1] += 1
        else:
            runs.append([x, 1])
    out = []
    def rec(i, cur, left):
        if i == len(runs):
            if left == 0:
                out.append(tuple(x for x in cur if x))
            return
        x, r = runs[i]
        for t in range(min(r, left), -1, -1):    # t bottom rows of the run lose a box
            rec(i + 1, cur + [x] * (r - t) + [x - 1] * t, left - t)
    rec(0, [], j)
    return out


def horizontal_strip_additions(nu, k, max_len):
    """Partitions gamma with gamma/nu a horizontal strip of k boxes and ell(gamma) <= max_len."""
    nu = tuple(x for x in nu if x)
    L = min(max_len, len(nu) + 1)
    base = list(nu) + [0] * (L - len(nu))
    out = []
    def rec(i, cur, left):
        if i == L:
            if left == 0:
                out.append(tuple(x for x in cur if x))
            return
        hi = (base[i - 1] - base[i]) if i > 0 else left   # interlacing: nu_i <= gamma_i <= nu_{i-1}
        hi = min(hi, left)
        for add in range(hi, -1, -1):
            rec(i + 1, cur + [base[i] + add], left - add)
    rec(0, [], k)
    return out


# ------------------------------------------------------ bead-mask characters
def mask_of(lam, L):
    """Bead mask of a partition with L beads (positions lam_j + L-1-j)."""
    lam = tuple(x for x in lam if x)
    assert len(lam) <= L, (lam, L)
    parts = list(lam) + [0] * (L - len(lam))
    m = 0
    for j, p in enumerate(parts):
        m |= 1 << (p + L - 1 - j)
    return m


def partition_of(mask, L):
    beads = [b for b in range(mask.bit_length()) if mask >> b & 1]
    assert len(beads) == L
    beads.sort(reverse=True)
    return tuple(x for x in (b - (L - 1 - j) for j, b in enumerate(beads)) if x)


def _add_strip(D, k, allowed):
    """One Murnaghan-Nakayama step: add a k-strip to every state of D.

    D: dict mask -> integer.  allowed(mask) prunes states that can never reach a
    target.  A bead at b moves to b+k if that slot is free; the sign is (-1)^(number
    of beads strictly between b and b+k)."""
    out = {}
    for mask, val in D.items():
        m = mask
        while m:
            low = m & -m
            b = low.bit_length() - 1
            m ^= low
            top = 1 << (b + k)
            if mask & top:
                continue
            new = mask ^ low ^ top
            if not allowed(new):
                continue
            between = mask & (top - 1) & ~((low << 1) - 1)
            if between.bit_count() & 1:
                out[new] = out.get(new, 0) - val
            else:
                out[new] = out.get(new, 0) + val
    return {k_: v for k_, v in out.items() if v}


def char_block(m, L, allowed, targets, pure=None):
    """Characters chi^nu(rho) for every rho |- m and every nu in `targets` (masks with
    L beads), by one depth-first pass over partitions of m with parts ascending.

    `allowed` is the set of bead masks the pass may visit (every target and the empty
    partition included); a state outside it is pruned, together with everything above
    it.  Returns (rhos, rows): rhos the list of partitions of m (decreasing tuples)
    at which some state survived, rows a dict target-mask -> list of chi values
    aligned with rhos.  Uses the C accelerator (wk9_s58_chars.c) when it builds,
    the pure-Python pass otherwise or when pure=True; the two are compared on every
    calibration sample."""
    if pure is None:
        pure = PURE
    targets = list(targets)
    if not pure and max(allowed).bit_length() <= 63:
        so = _load_so()
        if so is not None:
            return _char_block_c(so, m, L, allowed, targets)
    rhos, cols = [], []           # cols[i] = dict mask -> chi at rhos[i]
    start = {(1 << L) - 1: 1}     # the empty partition
    ok = allowed.__contains__
    def rec(parts, total, minp, D):
        if total == m:
            rhos.append(tuple(reversed(parts)))
            cols.append(D)
            return
        for k in range(minp, m - total + 1):
            D2 = _add_strip(D, k, ok)
            if D2:
                rec(parts + [k], total + k, k, D2)
    rec([], 0, 1, start)
    rows = {t: [c.get(t, 0) for c in cols] for t in targets}
    return rhos, rows


PURE = bool(os.environ.get('S58_PURE'))
_SO = [None, False]


def _load_so():
    """Build (once) and load the C accelerator; None if it cannot be built."""
    if _SO[1]:
        return _SO[0]
    _SO[1] = True
    try:
        import ctypes, subprocess
        import numpy as np
        build = os.environ.get('S58_BUILD') or os.path.join('/tmp', 's58_build')
        os.makedirs(build, exist_ok=True)
        src = os.path.join(HERE, 'wk9_s58_chars.c')
        so = os.path.join(build, 'wk9_s58_chars.so')
        if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
            subprocess.check_call(['gcc', '-O2', '-shared', '-fPIC', '-o', so, src])
        lib = ctypes.CDLL(so)
        lib.s58_char_block.restype = ctypes.c_int
        lib.s58_char_block.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p,
                                       ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                                       ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
        _SO[0] = lib
    except Exception as e:          # pragma: no cover
        sys.stderr.write("[s58] C accelerator unavailable (%s); pure Python\n" % e)
        _SO[0] = None
    return _SO[0]


def _char_block_c(lib, m, L, allowed, targets):
    import ctypes
    import numpy as np
    states = sorted(allowed)
    idx = {mk: i for i, mk in enumerate(states)}
    st = np.array(states, dtype=np.uint64)
    tg = np.array([idx[t] for t in targets], dtype=np.int32)
    nl = num_partitions(m) + 1
    lo = np.zeros((nl, max(1, len(targets))), dtype=np.int64)
    hi = np.zeros((nl, max(1, len(targets))), dtype=np.int64)
    pr = np.zeros((nl, max(1, m)), dtype=np.int32)
    flags = ctypes.c_int(0)
    n = lib.s58_char_block(m, L, len(states), st.ctypes.data, len(targets), tg.ctypes.data,
                           lo.ctypes.data, hi.ctypes.data, pr.ctypes.data, nl, ctypes.byref(flags), 0)
    assert flags.value == 0, ("C character block failed", flags.value)
    desc = os.environ.get('S58_ASC') is None
    prl = pr[:n].tolist()
    if desc:
        rhos = [tuple(x for x in row if x) for row in prl]
    else:
        rhos = [tuple(x for x in reversed(row) if x) for row in prl]
    if m == 0:
        rhos = [()]
    rows = {}
    for j, t in enumerate(targets):
        lo_j = lo[:n, j].tolist()
        hi_j = hi[:n, j].tolist()
        rows[t] = [(h << 64) + (l & 0xFFFFFFFFFFFFFFFF) for l, h in zip(lo_j, hi_j)]
    return rhos, rows


def char_block_sums(m, L, allowed, targets):
    """Per class rho |- m: S1(rho) = sum_{t in targets} chi^t(rho) and S2(rho) = sum_t chi^t(rho)^2,
    without materialising the (classes x targets) block.  C pass (256-bit S2) when
    available, else the Python pass summed."""
    if not PURE and max(allowed).bit_length() <= 63:
        lib = _load_so()
        if lib is not None:
            import ctypes
            import numpy as np
            states = sorted(allowed)
            idx = {mk: i for i, mk in enumerate(states)}
            st = np.array(states, dtype=np.uint64)
            tg = np.array([idx[t] for t in targets], dtype=np.int32)
            nl = num_partitions(m) + 1
            lo = np.zeros((nl, 6), dtype=np.int64)
            hi = np.zeros((1, 1), dtype=np.int64)
            pr = np.zeros((nl, max(1, m)), dtype=np.int32)
            flags = ctypes.c_int(0)
            n = lib.s58_char_block(m, L, len(states), st.ctypes.data, len(targets), tg.ctypes.data,
                                   lo.ctypes.data, hi.ctypes.data, pr.ctypes.data, nl, ctypes.byref(flags), 1)
            assert flags.value == 0, ("C character block (sum mode) failed", flags.value)
            desc = os.environ.get('S58_ASC') is None
            prl = pr[:n].tolist()
            rhos = [tuple(x for x in row if x) for row in prl] if desc else [tuple(x for x in reversed(row) if x) for row in prl]
            if m == 0:
                rhos = [()]
            M64 = 0xFFFFFFFFFFFFFFFF
            S1, S2 = [], []
            for row in lo[:n].tolist():
                S1.append((row[1] << 64) + (row[0] & M64))
                S2.append(((row[5] & M64) << 192) + ((row[4] & M64) << 128) + ((row[3] & M64) << 64) + (row[2] & M64))
            return rhos, S1, S2
    rhos, rows = char_block(m, L, allowed, targets, pure=True)
    S1 = [sum(rows[t][i] for t in targets) for i in range(len(rhos))]
    S2 = [sum(rows[t][i] ** 2 for t in targets) for i in range(len(rhos))]
    return rhos, S1, S2


def char_row_memo(lam, rhos, L=None):
    """chi^lam(rho) for the listed rhos by memoised strip REMOVAL (independent of
    char_block: recursion on (mask, remaining parts))."""
    lam = tuple(x for x in lam if x)
    if L is None:
        L = max(1, len(lam))
    memo = {}
    def chi(mask, parts):
        if not parts:
            return 1
        key = (mask, parts)
        v = memo.get(key)
        if v is not None:
            return v
        k, rest = parts[0], parts[1:]
        tot = 0
        mm = mask
        while mm:
            low = mm & -mm
            b = low.bit_length() - 1
            mm ^= low
            if b < k:
                continue
            dn = 1 << (b - k)
            if mask & dn:
                continue
            new = mask ^ low ^ dn
            between = mask & (low - 1) & ~((dn << 1) - 1)
            s = chi(new, rest)
            tot += -s if between.bit_count() & 1 else s
        memo[key] = tot
        return tot
    m0 = mask_of(lam, L)
    return [chi(m0, tuple(rho)) if sum(rho) == sum(lam) else 0 for rho in rhos]


# --------------------------------------------------------- the inner pairings
def inner_pairings(m, taus, betas, n, delta, tail_box=None):
    """For tau in taus (all |- m) and beta in betas (all |- m, <= n rows, <= delta cols):
        G[tau][beta] = g(tau, beta, beta),   Aa[tau][beta] = A(tau, beta) = <chi^tau, psi^2 chi^beta>.
    tail_box: a partition containing every tau (prunes the tau-side pass); default: the
    union bound (max over rows)."""
    taus = [tuple(x for x in t if x) for t in taus]
    betas = [tuple(x for x in b if x) for b in betas]
    if m == 0:
        return {(): {(): 1}}, {(): {(): 1}}
    if not taus or not betas:
        return {t: {} for t in taus}, {t: {} for t in taus}
    # tau side: L_t beads, states pruned to sub-partitions of the box
    if tail_box is None:
        R = max(len(t) for t in taus)
        tail_box = tuple(max((t[i] if i < len(t) else 0) for t in taus) for i in range(R))
    tail_box = tuple(x for x in tail_box if x)
    Lt = max(1, len(tail_box))
    allowed_t = set(mask_of(s, Lt) for s in sub_partitions(tail_box))
    rhos_t, trows = char_block(m, Lt, allowed_t, [mask_of(t, Lt) for t in taus])
    # beta side: n beads inside the box
    rhos_b, brows = char_block(m, n, box_states(m, n, delta), [mask_of(b, n) for b in betas])
    # each pass prunes subtrees on which every target character vanishes, so the two
    # leaf lists differ.  A class absent on the beta side has chi^beta = 0 for every
    # beta in the box (the DP state was empty on the whole subtree).  The classes that
    # can contribute are the tau-side leaves; chi^beta is looked up at rho (g-part)
    # and at rho^2 (A-part) separately, an absent class counting as 0.
    ib = {rho: i for i, rho in enumerate(rhos_b)}
    rhos = rhos_t
    mfact = factorial(m)
    csize = [mfact // zee(rho) for rho in rhos]
    P = len(rhos)
    bcol = [ib.get(rho, -1) for rho in rhos]
    sq = [ib.get(square_type(rho), -1) for rho in rhos]
    # matrices: T (taus x P) with class sizes folded in; U (betas x P) squares; W (betas x P) at rho^2
    Tm = [[csize[i] * trows[mask_of(t, Lt)][i] for i in range(P)] for t in taus]
    Um = [[(brows[mask_of(b, n)][bcol[i]] ** 2 if bcol[i] >= 0 else 0) for i in range(P)] for b in betas]
    Wm = [[(brows[mask_of(b, n)][sq[i]] if sq[i] >= 0 else 0) for i in range(P)] for b in betas]
    if HAVE_FLINT:
        T = flint.fmpz_mat(Tm)
        GU = T * flint.fmpz_mat(Um).transpose()
        GW = T * flint.fmpz_mat(Wm).transpose()
        getG = lambda i, j: int(GU[i, j])
        getA = lambda i, j: int(GW[i, j])
    else:
        getG = lambda i, j: sum(a * b for a, b in zip(Tm[i], Um[j]))
        getA = lambda i, j: sum(a * b for a, b in zip(Tm[i], Wm[j]))
    G, Aa = {}, {}
    for i, t in enumerate(taus):
        G[t], Aa[t] = {}, {}
        for j, b in enumerate(betas):
            gv, av = getG(i, j), getA(i, j)
            assert gv % mfact == 0 and av % mfact == 0, ("non-integer pairing", t, b)
            G[t][b], Aa[t][b] = gv // mfact, av // mfact
    return G, Aa


# ------------------------------------------------- the box weights (per m, delta)
_BOX = {}


def box_states(m, n, delta):
    """Bead masks (n beads) of every partition of size <= m inside the n x delta box."""
    out = set()
    for k in range(0, m + 1):
        for b in partitions_in_box(k, n, delta):
            out.add(mask_of(b, n))
    return out


def box_weights(m, n, delta):
    """The lam-independent part of the inner sums, once per (m, n, delta):

        w_g(rho) = sum_{beta in B_m} chi^beta(rho)^2,   w_A(rho) = sum_{beta in B_m} chi^beta(rho^2),

    over rho |- m, as dicts rho -> integer (classes absent from both are omitted).
    This is the house 'W(rho)' idea moved from S_N down to S_m."""
    key = (m, n, delta)
    if key in _BOX:
        return _BOX[key]
    betas = partitions_in_box(m, n, delta)
    if m == 0:
        _BOX[key] = ({(): 1}, {(): 1}, 1)
        return _BOX[key]
    allowed_b = box_states(m, n, delta)
    rhos_b, S1, S2 = char_block_sums(m, n, allowed_b, [mask_of(b, n) for b in betas])
    ib = {rho: i for i, rho in enumerate(rhos_b)}
    wg = {}
    for rho, i in ib.items():
        if S2[i]:
            wg[rho] = S2[i]
    wa = {}
    for rho in partitions(m):
        i = ib.get(square_type(rho), -1)
        if i >= 0 and S1[i]:
            wa[rho] = S1[i]
    _BOX[key] = (wg, wa, len(betas))
    return _BOX[key]


_CS = {}
_TS = {}


def _tail_states(tail_box, Lt):
    key = (tail_box, Lt)
    if key not in _TS:
        _TS[key] = set(mask_of(s, Lt) for s in sub_partitions(tail_box))
        if len(_TS) > 64:
            _TS.pop(next(iter(_TS)))
    return _TS[key]


def _class_sizes(m):
    if m not in _CS:
        mf = factorial(m)
        _CS[m] = {rho: mf // zee(rho) for rho in partitions(m)}
    return _CS[m]


def tail_sums(m, taus, n, delta, tail_box):
    """sum_{beta in B_m} g(tau,beta,beta) and sum_beta A(tau,beta) for every tau in taus
    (all |- m), by one tau-side character pass paired with the box weights."""
    taus = [tuple(x for x in t if x) for t in taus]
    if m == 0:
        return {(): (1, 1)}
    wg, wa, _ = box_weights(m, n, delta)
    tail_box = tuple(x for x in tail_box if x)
    Lt = max(1, len(tail_box))
    allowed_t = _tail_states(tail_box, Lt)
    rhos_t, trows = char_block(m, Lt, allowed_t, [mask_of(t, Lt) for t in taus])
    mfact = factorial(m)
    cs = _class_sizes(m)
    csize = [cs[rho] for rho in rhos_t]
    WG = [wg.get(rho, 0) for rho in rhos_t]
    WA = [wa.get(rho, 0) for rho in rhos_t]
    out = {}
    for t in taus:
        row = trows[mask_of(t, Lt)]
        gv = sum(c * x * w for c, x, w in zip(csize, row, WG) if x and w)
        av = sum(c * x * w for c, x, w in zip(csize, row, WA) if x and w)
        assert gv % mfact == 0 and av % mfact == 0, ("non-integer tail sum", t, m)
        out[t] = (gv // mfact, av // mfact)
    return out


# ------------------------------------------------------------ the reduction
def reduction_terms(tail):
    """[(sign, tau)] over the vertical strips of the tail: s_{tail/(1^j)} = sum_tau s_tau."""
    tail = tuple(x for x in tail if x)
    terms = []
    for j in range(0, len(tail) + 1):
        for tau in vertical_strips(tail, j):
            terms.append(((-1) ** j, tau))
    return terms


def sk_reduced(lam, delta, n=4, stats=None, shortcut=True, per_beta=False):
    """(g, A, sk) at (lam, delta^n) by the first-row reduction.
    per_beta=True routes the inner sums through inner_pairings (every g(tau,beta,beta)
    separately, flint matrix products) instead of the box weights -- same numbers,
    different code path."""
    lam = tuple(x for x in lam if x)
    N = n * delta
    if sum(lam) != N or any(lam[i] < lam[i + 1] for i in range(len(lam) - 1)):
        raise ValueError("lam must be a partition of n*delta: %r" % (lam,))
    if shortcut and len(lam) > n * n:
        return 0, 0, 0
    tail = lam[1:]
    terms = reduction_terms(tail)
    by_size = {}
    for s, tau in terms:
        by_size.setdefault(sum(tau), []).append((s, tau))
    g = A = 0
    ops = 0
    for mm, lst in by_size.items():
        taus = [t for _, t in lst]
        if per_beta:
            betas = partitions_in_box(mm, n, delta)
            G, Aa = inner_pairings(mm, taus, betas, n, delta, tail_box=tail)
            sums = {t: (sum(G[t].values()), sum(Aa[t].values())) for t in taus}
        else:
            sums = tail_sums(mm, taus, n, delta, tail)
        ops += len(taus) * num_partitions(mm)
        for s, tau in lst:
            g += s * sums[tau][0]
            A += s * sums[tau][1]
    assert (g + A) % 2 == 0, ("parity", lam, g, A)
    assert g >= 0 and (g + A) // 2 >= 0 and (g - A) // 2 >= 0, ("sign", lam, g, A)
    if stats is not None:
        stats['terms'] = len(terms)
        stats['sizes'] = sorted(by_size)
        stats['inner_ops'] = ops
    return g, A, (g + A) // 2


def sk_pieri(lam, delta, n=4):
    """The reduction organised by Pieri inversion (an internal cross-check):
        <s_gamma, F> = <h_{gamma_1} s_{gamma-bar}, F> - sum_{gamma' != gamma in Pieri} <s_gamma', F>,
    recursing on the tail (every other term of h_k s_nu has a strictly shorter tail).
    Needs the inner pairings for EVERY sub-partition of the tail."""
    lam = tuple(x for x in lam if x)
    N = n * delta
    if len(lam) > n * n:
        return 0, 0, 0
    tail = lam[1:]
    subs = sub_partitions(tail)
    by_size = {}
    for s in subs:
        by_size.setdefault(sum(s), []).append(s)
    H = {}                                       # nu -> (sum_beta g, sum_beta A)
    for mm, nus in by_size.items():
        H.update(tail_sums(mm, nus, n, delta, tail))
    memo = {}
    def Gval(gamma):
        gamma = tuple(x for x in gamma if x)
        if gamma in memo:
            return memo[gamma]
        if len(gamma) > n * n:
            return (0, 0)
        nu = gamma[1:]
        hg, ha = H[nu]
        for gp in horizontal_strip_additions(nu, gamma[0], n * n):
            if gp != gamma:
                a_, b_ = Gval(gp)
                hg -= a_
                ha -= b_
        memo[gamma] = (hg, ha)
        return memo[gamma]
    g, A = Gval(lam)
    return g, A, (g + A) // 2


# ------------------------------------------------------------- brute force
def sk_brute(lam, delta, n=4):
    """The definition: the plain sum over all partitions of N with a fresh
    Murnaghan-Nakayama (strip removal, memoised)."""
    lam = tuple(x for x in lam if x)
    N = n * delta
    rect = tuple([delta] * n)
    rhos = list(partitions(N))
    cl = char_row_memo(lam, rhos)
    cr = char_row_memo(rect, rhos)
    idx = {rho: i for i, rho in enumerate(rhos)}
    Nf = factorial(N)
    g = A = 0
    for i, rho in enumerate(rhos):
        if cl[i] == 0:
            continue
        w = (Nf // zee(rho)) * cl[i]
        g += w * cr[i] * cr[i]
        A += w * cr[idx[square_type(rho)]]
    assert g % Nf == 0 and A % Nf == 0
    g //= Nf
    A //= Nf
    return g, A, (g + A) // 2


def house_m_det(lam, delta, n=4):
    sys.path.insert(0, os.path.join(ROOT, 'scripts'))
    from ambient_screen import m_det, chi
    v = m_det(tuple(lam), n, delta)
    chi.cache_clear()
    return v


# ------------------------------------------------------------------ helpers
def parse_lam(s):
    return tuple(int(x) for x in s.replace(',', '|').split('|') if x.strip())


def fmt_lam(lam):
    return '(' + ','.join(str(x) for x in lam) + ')'


def log_pid(name):
    os.makedirs(os.path.join(ROOT, 'results', 'logs'), exist_ok=True)
    with open(os.path.join(ROOT, 'results', 'logs', name + '.pid'), 'w') as fh:
        fh.write(str(os.getpid()) + '\n')


# ---------------------------------------------------------------- commands
def cmd_cell(argv):
    lam = parse_lam(argv[0]); delta = int(argv[1])
    n = int(argv[argv.index('--n') + 1]) if '--n' in argv else 4
    st = {}
    t0 = time.time(); g, A, sk = sk_reduced(lam, delta, n, st); t1 = time.time()
    print("lam=%s delta=%d n=%d : g=%d  A=%d  sk=%d  ak=%d   [reduction %.2fs; %d terms, sizes %s, inner ops %d]"
          % (fmt_lam(lam), delta, n, g, A, sk, (g - A) // 2, t1 - t0, st['terms'], st['sizes'], st['inner_ops']))
    if '--pieri' in argv:
        t0 = time.time(); g2, A2, sk2 = sk_pieri(lam, delta, n); t1 = time.time()
        print("  pieri organisation : g=%d  A=%d  sk=%d   [%.2fs]  %s" % (g2, A2, sk2, t1 - t0,
              "AGREE" if (g2, A2, sk2) == (g, A, sk) else "*** DISAGREE ***"))
    if '--brute' in argv:
        t0 = time.time(); g3, A3, sk3 = sk_brute(lam, delta, n); t1 = time.time()
        print("  brute force        : g=%d  A=%d  sk=%d   [%.2fs]  %s" % (g3, A3, sk3, t1 - t0,
              "AGREE" if (g3, A3, sk3) == (g, A, sk) else "*** DISAGREE ***"))
    if '--house' in argv:
        t0 = time.time(); h = house_m_det(lam, delta, n); t1 = time.time()
        print("  house m_det        : sk=%d   [%.2fs]  %s" % (h, t1 - t0, "AGREE" if h == sk else "*** DISAGREE ***"))
    return 0


# ------------------------------------------------------------- calibration
BRIEF_TABLE = [  # (lam, delta, sk, source)
    ((16, 2, 2, 2, 2), 6, 8, 'results/occurrence_screen.md; integrator'),
    ((20, 2, 2, 2, 2), 7, 8, 'results/occurrence_screen.md; integrator'),
    ((24, 2, 2, 2, 2), 8, 8, 'results/occurrence_screen.md; integrator'),
    ((30, 2, 2, 2, 2, 2), 10, 13, 'integrator (docs/s50_s55_integrator_notes.md)'),
    ((29, 4, 2, 2, 2, 1), 10, 78, 'integrator'),
    ((29, 3, 2, 2, 2, 2), 10, 30, 'integrator'),
    ((4, 4, 4, 4, 4), 5, 5, 's38'),
]
S39_LOG_CELLS = [  # results/logs/s39_engine_timing.log (C engine of s39)
    ((22,) + (2,) * 9, 10, 18), ((26,) + (2,) * 9, 11, 18), ((30,) + (2,) * 9, 12, 18),
    ((10, 4, 4, 4, 3, 3, 3, 3, 3, 3), 10, 4988), ((11, 4, 4, 4, 4, 4, 4, 3, 3, 3), 11, 14123),
    ((12,) + (4,) * 9, 12, 2254), ((32,) + (1,) * 8, 10, 0), ((36,) + (1,) * 8, 11, 0), ((40,) + (1,) * 8, 12, 0),
]
N3_ANCHORS = {2: (3, 3), 3: (11, 10), 4: (43, 34)}     # n=3: (sum, support) of m_det over lam |- 3 delta, ell <= 9
S28_N3_ZERO = [(13, 3, 2, 2, 2, 2, 2, 2, 2), (12, 5, 2, 2, 2, 2, 2, 2, 1), (9, 9, 2, 2, 2, 2, 2, 2)]  # n=3, delta=10: m_det = 0


def read_screen(path):
    rows = []
    with open(path) as fh:
        head = fh.readline().strip().split(',')
        for ln in fh:
            f = ln.strip().split(',')
            if len(f) < 5:
                continue
            d = dict(zip(head, f))
            lam = tuple(int(x) for x in d['lam'].split('|'))
            rows.append((int(d['delta']), lam, int(d['a']), int(d['m_det'])))
    return rows


def cmd_calibrate(argv):
    """PREREG_s58 M1.  Writes results/s58_calibration.jsonl (every cell of the brief's
    table, the length-5 screen, the s39 cells, the samples) and results/s58_calibration.md."""
    import random
    log_pid('s58_calibrate')
    quick = '--quick' in argv
    out_jsonl = open(os.path.join(ROOT, 'results', 's58_calibration.jsonl'), 'w')
    summary = []
    mism = []
    def rec(kind, lam, delta, want, n=4, extra=None):
        st = {}
        t0 = time.time()
        g, A, sk = sk_reduced(lam, delta, n, st)
        dt = time.time() - t0
        ok = (sk == want)
        row = {'kind': kind, 'n': n, 'delta': delta, 'lam': list(lam), 'ell': len(lam), 'tail': sum(lam[1:]),
               'g': g, 'A': A, 'sk': sk, 'ak': (g - A) // 2, 'want': want, 'ok': ok, 'time': round(dt, 4)}
        if extra:
            row.update(extra)
        out_jsonl.write(json.dumps(row) + '\n'); out_jsonl.flush()
        if not ok:
            mism.append(row)
            print("  *** MISMATCH %s lam=%s delta=%d: reduction sk=%d, banked %d" % (kind, fmt_lam(lam), delta, sk, want))
            sys.stdout.flush()
        return row

    # 1. the brief's table
    print("[1] the brief's table"); sys.stdout.flush()
    for lam, delta, want, src in BRIEF_TABLE:
        r = rec('brief', lam, delta, want, extra={'source': src})
        print("   %-22s /%-2d  sk=%-4d (banked %d)  g=%d A=%d  %s  [%.3fs]" % (fmt_lam(lam), delta, r['sk'], want, r['g'], r['A'], 'ok' if r['ok'] else 'FAIL', r['time']))
    summary.append(('brief table', len(BRIEF_TABLE), sum(1 for r in mism if r['kind'] == 'brief')))

    # 2. the s39 timing-log cells
    print("[2] s39 timing-log cells"); sys.stdout.flush()
    for lam, delta, want in S39_LOG_CELLS:
        r = rec('s39log', lam, delta, want)
        print("   %-32s /%-2d  sk=%-6d (banked %d) %s [%.2fs]" % (fmt_lam(lam), delta, r['sk'], want, 'ok' if r['ok'] else 'FAIL', r['time']))
    summary.append(('s39 log cells', len(S39_LOG_CELLS), sum(1 for r in mism if r['kind'] == 's39log')))

    # 3. n=3 anchors and the s28 zeros
    print("[3] n=3 anchors"); sys.stdout.flush()
    n3bad = 0
    for delta, want in N3_ANCHORS.items():
        vals = [sk_reduced(lam, delta, 3)[2] for lam in partitions(3 * delta) if len(lam) <= 9]
        got = (sum(vals), sum(1 for v in vals if v))
        print("   n=3 delta=%d: (sum, support) = %s, banked %s %s" % (delta, got, want, 'ok' if got == want else 'FAIL'))
        n3bad += (got != want)
    for lam in S28_N3_ZERO:
        r = rec('s28n3', lam, 10, 0, n=3)
        print("   n=3 delta=10 %-28s sk=%d (banked 0) %s" % (fmt_lam(lam), r['sk'], 'ok' if r['ok'] else 'FAIL'))
    summary.append(('n=3 anchors + s28 zeros', 3 + len(S28_N3_ZERO), n3bad + sum(1 for r in mism if r['kind'] == 's28n3')))

    # 4. the length-5 screen, every cell
    print("[4] length-5 screen, every cell"); sys.stdout.flush()
    cells = read_screen(os.path.join(ROOT, 'results', 'occurrence_screen.csv')) + \
            read_screen(os.path.join(ROOT, 'results', 'screen_d10_12.csv'))
    t0 = time.time()
    for i, (delta, lam, av, md) in enumerate(cells):
        rec('screen5', lam, delta, md, extra={'a': av})
        if (i + 1) % 500 == 0:
            print("   ...%d/%d cells, %d mismatches [%.0fs]" % (i + 1, len(cells), len(mism), time.time() - t0)); sys.stdout.flush()
    print("   %d cells, %d mismatches [%.0fs]" % (len(cells), sum(1 for r in mism if r['kind'] == 'screen5'), time.time() - t0))
    summary.append(('length-5 screen (s38), delta 5-10', len(cells), sum(1 for r in mism if r['kind'] == 'screen5')))

    # 5. samples through the other routes (pure Python pass, per-beta flint route, Pieri organisation,
    #    brute force at N <= 28, house m_det at N <= 40)
    print("[5] the other routes on samples"); sys.stdout.flush()
    rnd = random.Random(58)
    sample = rnd.sample(cells, 40 if not quick else 8)
    sample += [(d, l, None, w) for l, d, w, _ in BRIEF_TABLE] + [(d, l, None, w) for l, d, w in S39_LOG_CELLS[:6]]
    routes_bad = {'pure': 0, 'perbeta': 0, 'pieri': 0}
    for delta, lam, av, md in sample:
        g, A, sk = sk_reduced(lam, delta, 4)
        global PURE
        PURE = True
        try:
            _BOX.clear()
            rp = sk_reduced(lam, delta, 4)
        finally:
            PURE = False
            _BOX.clear()
        rb = sk_reduced(lam, delta, 4, per_beta=True)
        rq = sk_pieri(lam, delta, 4)
        routes_bad['pure'] += (rp != (g, A, sk)); routes_bad['perbeta'] += (rb != (g, A, sk)); routes_bad['pieri'] += (rq != (g, A, sk))
        out_jsonl.write(json.dumps({'kind': 'routes', 'delta': delta, 'lam': list(lam), 'reduction': [g, A, sk], 'pure_python': list(rp),
                                    'per_beta': list(rb), 'pieri': list(rq), 'banked': md}) + '\n')
    print("   %d cells: pure-Python pass mismatches %d, per-beta route %d, Pieri organisation %d"
          % (len(sample), routes_bad['pure'], routes_bad['perbeta'], routes_bad['pieri']))
    summary.append(('other routes (pure/per-beta/Pieri) on samples', len(sample), sum(routes_bad.values())))

    # 6. brute force and house m_det on random cells of EVERY length, N = 20, 24, 28
    print("[6] brute force + house m_det, random cells of every length"); sys.stdout.flush()
    bf_bad = hs_bad = bf_n = 0
    for N in ((20, 24, 28) if not quick else (20,)):
        delta = N // 4
        lams = [l for l in partitions(N) if len(l) <= 16]
        bylen = {}
        for l in lams:
            bylen.setdefault(len(l), []).append(l)
        for ell, ls in sorted(bylen.items()):
            for lam in rnd.sample(ls, min(3, len(ls))):
                g, A, sk = sk_reduced(lam, delta, 4)
                gb, Ab, skb = sk_brute(lam, delta, 4)
                hs = house_m_det(lam, delta, 4) if N <= 24 or len(lam) <= 8 else None
                bf_n += 1
                bf_bad += ((g, A, sk) != (gb, Ab, skb))
                hs_bad += (hs is not None and hs != sk)
                out_jsonl.write(json.dumps({'kind': 'brute', 'delta': delta, 'lam': list(lam), 'reduction': [g, A, sk],
                                            'brute': [gb, Ab, skb], 'house': hs}) + '\n')
        print("   N=%d done: %d cells so far, brute mismatches %d, house mismatches %d" % (N, bf_n, bf_bad, hs_bad)); sys.stdout.flush()
    summary.append(('brute force (definition) on random cells of every length, N=20,24,28', bf_n, bf_bad + hs_bad))

    # 7. cells with more than 16 rows: the reduction must return 0 without the shortcut
    print("[7] lam with more than 16 rows (must vanish)"); sys.stdout.flush()
    z_bad = 0
    for lam in [(4,) + (1,) * 16, (3, 3) + (1,) * 14, (2,) * 18, (5, 2, 2) + (1,) * 15]:
        delta = sum(lam) // 4
        if sum(lam) % 4:
            continue
        r = sk_reduced(lam, delta, 4, shortcut=False)
        z_bad += (r != (0, 0, 0))
        print("   %-40s /%d -> %s" % (fmt_lam(lam), delta, r))
    summary.append(('lam with > 16 rows vanish without the shortcut', 4, z_bad))

    out_jsonl.close()
    # markdown
    with open(os.path.join(ROOT, 'results', 's58_calibration.md'), 'w') as fh:
        fh.write("# Session 58 — calibration of the first-row reduction\n\n")
        fh.write("Code `analysis/wk9_s58_sk.py calibrate`; every value in `results/s58_calibration.jsonl`.\n")
        fh.write("The pre-registered rule: one disagreement and the algorithm is wrong.\n\n")
        fh.write("| set | cells | disagreements |\n|---|---|---|\n")
        for name, cnt, bad in summary:
            fh.write("| %s | %d | **%d** |\n" % (name, cnt, bad))
        fh.write("\n## The brief's table\n\n| cell | banked `sk` | reduction `sk` | `g` | `A` | `ak = (g−A)/2` |\n|---|---|---|---|---|---|\n")
        for lam, delta, want, src in BRIEF_TABLE:
            g, A, sk = sk_reduced(lam, delta, 4)
            fh.write("| `%s/%d` | %d | **%d** | %d | %d | %d |\n" % (fmt_lam(lam), delta, want, sk, g, A, (g - A) // 2))
        fh.write("\n## The s39 C-engine cells (N up to 48)\n\n| cell | banked | reduction |\n|---|---|---|\n")
        for lam, delta, want in S39_LOG_CELLS:
            fh.write("| `%s/%d` | %d | **%d** |\n" % (fmt_lam(lam), delta, want, sk_reduced(lam, delta, 4)[2]))
        if mism:
            fh.write("\n## DISAGREEMENTS\n\n")
            for r in mism:
                fh.write("- %s\n" % json.dumps(r))
        else:
            fh.write("\nNo disagreement anywhere.\n")
    print("\nSUMMARY:")
    for name, cnt, bad in summary:
        print("   %-70s %6d cells  %d disagreements" % (name, cnt, bad))
    return 0 if not mism and all(b == 0 for _, _, b in summary) else 1


def cmd_longweight(argv):
    """PREREG_s58 M1, the long-weight screen: every m_det >= 0 cell of
    results/longweight_screen.csv (lengths 6-10, delta 8-12, N up to 48)."""
    import gzip
    tag = argv[argv.index('--tag') + 1] if '--tag' in argv else 'all'
    log_pid('s58_longweight_' + tag)
    rows = read_screen(os.path.join(ROOT, 'results', 'longweight_screen.csv'))
    rows = [r for r in rows if r[3] >= 0]
    only = [int(x) for x in argv[argv.index('--delta') + 1].split(',')] if '--delta' in argv else None
    if only:
        rows = [r for r in rows if r[0] in only]
    limit = int(argv[argv.index('--limit') + 1]) if '--limit' in argv else None
    if limit:
        import random
        rows = random.Random(58).sample(rows, min(limit, len(rows)))
    rows.sort(key=lambda r: (r[0], sum(r[1][1:]), r[1]))          # cheap tails first
    if '--reverse' in argv:                                        # a second worker meeting the first in the middle
        rows.reverse()
    out = gzip.open(os.path.join(ROOT, 'results', 's58_longweight_%s.jsonl.gz' % tag), 'wt')
    bad = 0
    t0 = time.time()
    per_delta = {}
    for i, (delta, lam, av, md) in enumerate(rows):
        t1 = time.time()
        g, A, sk = sk_reduced(lam, delta, 4)
        dt = time.time() - t1
        ok = (sk == md)
        bad += (not ok)
        d = per_delta.setdefault(delta, [0, 0, 0.0]); d[0] += 1; d[1] += (not ok); d[2] += dt
        out.write(json.dumps({'delta': delta, 'lam': list(lam), 'a': av, 'm_det': md, 'g': g, 'A': A, 'sk': sk, 'ok': ok, 'time': round(dt, 4)}) + '\n')
        if not ok:
            print("  *** MISMATCH lam=%s delta=%d: reduction %d, banked %d" % (fmt_lam(lam), delta, sk, md)); sys.stdout.flush()
        if (i + 1) % 2000 == 0:
            out.flush()
            print("  ...%d/%d cells, %d mismatches [%.0fs]" % (i + 1, len(rows), bad, time.time() - t0)); sys.stdout.flush()
    out.close()
    print("long-weight screen: %d cells, %d mismatches [%.0fs]" % (len(rows), bad, time.time() - t0))
    for delta in sorted(per_delta):
        c, b, t = per_delta[delta]
        print("   delta=%d: %d cells, %d mismatches, %.1fs" % (delta, c, b, t))
    return 0 if bad == 0 else 1


def cmd_sumrule(argv):
    """PREREG_s58 M1: sum_{lam |- N} f^lam sk(lam) = f^mu (f^mu + 1)/2 and
    sum_lam f^lam g(lam,mu,mu) = (f^mu)^2 over ALL lam |- N (no shortcut), plus the
    brute force at every lam when --brute."""
    N = int(argv[0])
    n = int(argv[argv.index('--n') + 1]) if '--n' in argv else 4
    delta = N // n
    assert n * delta == N
    log_pid('s58_sumrule_%d' % N)
    lams = list(partitions(N))
    rhos = list(partitions(N))
    # f^lam from the character at the identity (own MN), f^mu likewise
    def f_of(lam):
        return char_row_memo(lam, [tuple([1] * N)])[0]
    fmu = f_of(tuple([delta] * n))
    S1 = S2 = 0
    bad = 0
    t0 = time.time()
    for i, lam in enumerate(lams):
        g, A, sk = sk_reduced(lam, delta, n, shortcut=False)
        f = f_of(lam)
        S1 += f * sk
        S2 += f * g
        if '--brute' in argv:
            gb, Ab, skb = sk_brute(lam, delta, n)
            if (gb, Ab, skb) != (g, A, sk):
                bad += 1
                print("  *** brute mismatch at %s: %s vs %s" % (fmt_lam(lam), (g, A, sk), (gb, Ab, skb)))
        if (i + 1) % 500 == 0:
            print("  ...%d/%d [%.0fs]" % (i + 1, len(lams), time.time() - t0)); sys.stdout.flush()
    want1 = fmu * (fmu + 1) // 2
    want2 = fmu * fmu
    print("N=%d n=%d delta=%d: %d partitions, f^mu=%d" % (N, n, delta, len(lams), fmu))
    print("  sum f^lam sk = %d  vs f^mu(f^mu+1)/2 = %d  %s" % (S1, want1, 'ok' if S1 == want1 else 'FAIL'))
    print("  sum f^lam g  = %d  vs (f^mu)^2       = %d  %s" % (S2, want2, 'ok' if S2 == want2 else 'FAIL'))
    if '--brute' in argv:
        print("  brute force at every lam: %d mismatches" % bad)
    print("  [%.0fs]" % (time.time() - t0))
    with open(os.path.join(ROOT, 'results', 's58_sumrule_%d.json' % N), 'w') as fh:
        json.dump({'N': N, 'n': n, 'delta': delta, 'partitions': len(lams), 'f_mu': fmu, 'sum_f_sk': S1, 'want_sk': want1,
                   'sum_f_g': S2, 'want_g': want2, 'brute_mismatches': (bad if '--brute' in argv else None),
                   'ok': S1 == want1 and S2 == want2 and bad == 0}, fh, indent=1)
    return 0 if (S1 == want1 and S2 == want2 and bad == 0) else 1


def cmd_costcurve(argv):
    """PREREG_s58 M2: wall time of the reduction (i) at fixed tail (17,2^7) for delta 11..24,
    (ii) at delta 10 for growing tails, and of the partition-sum routes for N = 20..48."""
    log_pid('s58_costcurve')
    out = {'fixed_tail': [], 'growing_tail': [], 'house_python': [], 's39_engine': []}
    tail = (17,) + (2,) * 7
    print("[i] fixed tail (17,2^7), delta 12..24 (cold = box weights rebuilt, warm = cached)"); sys.stdout.flush()
    for delta in range(12, 25):
        N = 4 * delta
        lam = (N - 31,) + tail
        _BOX.clear()
        st = {}
        t0 = time.time(); g, A, sk = sk_reduced(lam, delta, 4, st); t1 = time.time()
        t2 = time.time(); sk_reduced(lam, delta, 4); t3 = time.time()
        nb = sum(box_weights(m, 4, delta)[2] for m in st['sizes'])
        row = {'delta': delta, 'N': N, 'lam': list(lam), 'g': g, 'A': A, 'sk': sk, 'cold': round(t1 - t0, 3), 'warm': round(t3 - t2, 3),
               'terms': st['terms'], 'inner_ops': st['inner_ops'], 'betas': nb}
        out['fixed_tail'].append(row)
        print("   delta=%2d N=%2d lam=%-16s sk=%-8d g=%-8d A=%-6d cold %6.2fs warm %6.2fs  (%d terms, %d betas, %d inner ops)"
              % (delta, N, fmt_lam(lam), sk, g, A, t1 - t0, t3 - t2, st['terms'], nb, st['inner_ops'])); sys.stdout.flush()
    print("[ii] growing tail at delta = 10 (N = 40): lam = (40 - m, tail_m)"); sys.stdout.flush()
    tails = [(2, 2), (2, 2, 2, 2), (4, 2, 2), (4, 4, 2, 2), (6, 4, 2, 2), (8, 4, 2, 2), (8, 4, 2, 2, 2, 2), (10, 4, 4, 2, 2),
             (10, 6, 4, 2, 2), (12, 6, 4, 2, 2), (12, 8, 4, 2, 2), (12, 8, 4, 2, 2, 2), (14, 8, 4, 2, 2, 2), (14, 8, 4, 4, 2, 2)]
    for t in tails:
        m = sum(t)
        lam = (40 - m,) + t
        if lam[0] < t[0]:
            continue
        _BOX.clear()
        st = {}
        t0 = time.time(); g, A, sk = sk_reduced(lam, 10, 4, st); t1 = time.time()
        t2 = time.time(); sk_reduced(lam, 10, 4); t3 = time.time()
        out['growing_tail'].append({'m': m, 'lam': list(lam), 'sk': sk, 'g': g, 'A': A, 'cold': round(t1 - t0, 3), 'warm': round(t3 - t2, 3),
                                    'terms': st['terms'], 'inner_ops': st['inner_ops']})
        print("   m=%2d lam=%-24s sk=%-9d cold %6.2fs warm %6.2fs (%d terms, %d inner ops)" % (m, fmt_lam(lam), sk, t1 - t0, t3 - t2, st['terms'], st['inner_ops'])); sys.stdout.flush()
    print("[iii] house partition sum (scripts/ambient_screen.m_det, Python), one cell (N-8,2,2,2,2) per N"); sys.stdout.flush()
    sys.path.insert(0, os.path.join(ROOT, 'scripts'))
    from ambient_screen import m_det as house, chi as house_chi
    maxN = int(argv[argv.index('--houseN') + 1]) if '--houseN' in argv else 36
    for N in range(20, maxN + 1, 4):
        delta = N // 4
        lam = (N - 8, 2, 2, 2, 2)
        house_chi.cache_clear()
        t0 = time.time(); v = house(lam, 4, delta); t1 = time.time()
        pN = num_partitions(N)
        out['house_python'].append({'N': N, 'lam': list(lam), 'sk': v, 'time': round(t1 - t0, 3), 'p_N': pN, 'memo': house_chi.cache_info().currsize})
        print("   N=%2d p(N)=%7d  house m_det=%d  %7.1fs  (chi memo %d entries)" % (N, pN, v, t1 - t0, house_chi.cache_info().currsize)); sys.stdout.flush()
        house_chi.cache_clear()
    print("[iv] the s39 C engine (analysis/wk9_s39_chars.c): engine build (rectangle weights over all rho |- N) + one cell of the fixed-tail family"); sys.stdout.flush()
    try:
        import wk9_s39_chars as C39
        maxE = int(argv[argv.index('--engineN') + 1]) if '--engineN' in argv else 60
        for N in range(48, maxE + 1, 4):
            delta = N // 4
            lam = (N - 31,) + tail
            t0 = time.time(); E = C39.MdetEngine(delta, n=4); t1 = time.time()
            t2 = time.time(); v = E.m_det(lam); t3 = time.time()
            t4 = time.time(); v2 = E.m_det((N - 8, 2, 2, 2, 2)); t5 = time.time()
            pN = num_partitions(N)
            row = {'N': N, 'lam': list(lam), 'sk': v, 'build': round(t1 - t0, 3), 'cell': round(t3 - t2, 3), 'cell_peaked': round(t5 - t4, 3), 'p_N': pN}
            out['s39_engine'].append(row)
            mine = sk_reduced(lam, delta, 4)[2]
            print("   N=%2d p(N)=%8d build %6.1fs  cell %-14s %7.2fs -> %d (reduction: %d %s)   peaked cell %.2fs -> %d"
                  % (N, pN, t1 - t0, fmt_lam(lam), t3 - t2, v, mine, 'agree' if mine == v else 'DISAGREE', t5 - t4, v2)); sys.stdout.flush()
            del E
    except Exception as e:
        print("   s39 engine unavailable: %r" % (e,))
    with open(os.path.join(ROOT, 'results', 's58_costcurve.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print("wrote results/s58_costcurve.json")
    return 0


def cmd_target(argv):
    """PREREG_s58 M3 + M5: the goal cell and the stability probe."""
    log_pid('s58_target')
    lam = (65, 17) + (2,) * 7
    delta = 24
    res = {}
    st = {}
    _BOX.clear()
    t0 = time.time(); g, A, sk = sk_reduced(lam, delta, 4, st); t1 = time.time()
    print("GOAL CELL lam=%s delta=%d N=%d" % (fmt_lam(lam), delta, 4 * delta))
    print("   g((65,17,2^7), 24^4, 24^4) = %d" % g)
    print("   A                          = %d" % A)
    print("   sk((65,17,2^7), 24^4)      = %d      ak = %d" % (sk, (g - A) // 2))
    print("   [reduction %.2fs; %d terms, tail sizes %s, inner ops %d]" % (t1 - t0, st['terms'], st['sizes'], st['inner_ops'])); sys.stdout.flush()
    res['goal'] = {'lam': list(lam), 'delta': delta, 'g': g, 'A': A, 'sk': sk, 'ak': (g - A) // 2, 'time': round(t1 - t0, 3), 'stats': st}
    t0 = time.time(); g2, A2, sk2 = sk_pieri(lam, delta, 4); t1 = time.time()
    print("   Pieri organisation: g=%d A=%d sk=%d  [%.2fs]  %s" % (g2, A2, sk2, t1 - t0, 'AGREE' if (g2, A2, sk2) == (g, A, sk) else '*** DISAGREE ***'))
    res['pieri'] = {'g': g2, 'A': A2, 'sk': sk2, 'time': round(t1 - t0, 3), 'agree': (g2, A2, sk2) == (g, A, sk)}
    t0 = time.time(); g3, A3, sk3 = sk_reduced(lam, delta, 4, per_beta=True); t1 = time.time()
    print("   per-beta flint route: g=%d A=%d sk=%d  [%.2fs]  %s" % (g3, A3, sk3, t1 - t0, 'AGREE' if (g3, A3, sk3) == (g, A, sk) else '*** DISAGREE ***'))
    res['per_beta'] = {'g': g3, 'A': A3, 'sk': sk3, 'time': round(t1 - t0, 3), 'agree': (g3, A3, sk3) == (g, A, sk)}
    global PURE
    PURE = True
    _BOX.clear()
    try:
        t0 = time.time(); g4, A4, sk4 = sk_reduced(lam, delta, 4); t1 = time.time()
    finally:
        PURE = False
        _BOX.clear()
    print("   pure-Python pass:   g=%d A=%d sk=%d  [%.2fs]  %s" % (g4, A4, sk4, t1 - t0, 'AGREE' if (g4, A4, sk4) == (g, A, sk) else '*** DISAGREE ***'))
    res['pure_python'] = {'g': g4, 'A': A4, 'sk': sk4, 'time': round(t1 - t0, 3), 'agree': (g4, A4, sk4) == (g, A, sk)}
    # M5 stability probe
    print("STABILITY PROBE: lam = (N-31, 17, 2^7), delta = 20..32"); sys.stdout.flush()
    res['stability'] = []
    for d in range(20, 33):
        N = 4 * d
        l = (N - 31, 17) + (2,) * 7
        t0 = time.time(); gg, AA, ss = sk_reduced(l, d, 4); t1 = time.time()
        res['stability'].append({'delta': d, 'lam': list(l), 'g': gg, 'A': AA, 'sk': ss, 'time': round(t1 - t0, 3)})
        print("   delta=%2d lam=%-14s g=%-10d A=%-8d sk=%-10d [%.2fs]" % (d, fmt_lam(l), gg, AA, ss, t1 - t0)); sys.stdout.flush()
    # the per-beta breakdown at the goal cell: which beta_1 contribute (support of the box condition)
    with open(os.path.join(ROOT, 'results', 's58_target.json'), 'w') as fh:
        json.dump(res, fh, indent=1)
    print("wrote results/s58_target.json")
    return 0


def main(argv):
    if not argv:
        print(__doc__); return 1
    cmd, rest = argv[0], argv[1:]
    cmds = {'cell': cmd_cell, 'calibrate': cmd_calibrate, 'longweight': cmd_longweight, 'sumrule': cmd_sumrule,
            'costcurve': cmd_costcurve, 'target': cmd_target}
    if cmd not in cmds:
        print(__doc__); return 1
    return cmds[cmd](rest)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
