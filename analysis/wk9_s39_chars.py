#!/usr/bin/env python3
"""
Session 39 -- fast exact characters (C Murnaghan-Nakayama, wk9_s39_chars.c) and
the two arithmetic quantities of the occurrence screen:

    a(lam, delta)  = < h_delta[h_4], s_lam >           (ambient plethysm)
    m_det(lam)     = (1/2) [ g(lam, rect, rect) + T(lam) ],  rect = (delta^4)
                     g = sum_rho chi^lam(rho) chi^rect(rho)^2 / z_rho   (Kronecker)
                     T = sum_rho chi^lam(rho) chi^rect(tau rho) / z_rho (transpose twist,
                         tau = cycle type of sigma^2: even parts 2k -> k, k)

both as exact integers: chi^lam(rho) is exact (__int128) in C, the weighted sums
are accumulated mod two 61-bit primes and reconstructed by CRT (bounds:
a <= f^lam, |T| <= g <= f^rect < 2^70 for N <= 48, against p1 p2 ~ 2^122).
The anti-symmetric part (g - T)/2 must also be a non-negative integer -- asserted
on every cell as a free consistency check.

This is a SECOND, INDEPENDENTLY WRITTEN implementation of the same quantities as
scripts/ambient_screen.py (a, m_det); `python3 wk9_s39_chars.py --selftest`
checks it against the house routines, the n=3 anchors (m_det sums 3, 11, 43 at
delta=2,3,4; the s28 delta=10 cells with a=1, m_det=0), and s38's length-5
table (results/occurrence_screen.csv), before it is used for anything.

Build: gcc -O2 -shared -fPIC -o <build>/wk9_s39_chars.so analysis/wk9_s39_chars.c
(done automatically into $S39_BUILD or /tmp/s39_build).
"""
import os, sys, ctypes, subprocess, time
from fractions import Fraction
from functools import lru_cache
from math import factorial
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'scripts'))
sys.setrecursionlimit(400000)

P1 = (1 << 61) - 1                 # Mersenne prime 2^61 - 1
P2 = 2305843009213693921           # prime below 2^61 (checked at import)


def _is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True


assert _is_prime(P1) and _is_prime(P2), "primes"


# --------------------------------------------------------------- build / load
def _load():
    build = os.environ.get('S39_BUILD', '/tmp/s39_build')
    os.makedirs(build, exist_ok=True)
    so = os.path.join(build, 'wk9_s39_chars.so')
    src = os.path.join(HERE, 'wk9_s39_chars.c')
    if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
        subprocess.check_call(['gcc', '-O2', '-shared', '-fPIC', '-o', so, src])
    lib = ctypes.CDLL(so)
    i32p = ctypes.POINTER(ctypes.c_int32)
    i64p = ctypes.POINTER(ctypes.c_int64)
    u64p = ctypes.POINTER(ctypes.c_uint64)
    lib.chi_batch.argtypes = [ctypes.c_int, i32p, ctypes.c_int, i32p, i32p, i32p, i64p, i64p]
    lib.chi_batch.restype = ctypes.c_int
    lib.weighted_sums.argtypes = [ctypes.c_int, i32p, ctypes.c_int, i32p, i32p, i32p,
                                  ctypes.c_int, u64p, ctypes.c_uint64, ctypes.c_uint64, u64p]
    lib.weighted_sums.restype = ctypes.c_int
    lib.memo_reset.argtypes = []; lib.memo_reset.restype = None
    lib.memo_set_cap.argtypes = [ctypes.c_uint64]; lib.memo_set_cap.restype = None
    lib.memo_entries.argtypes = []; lib.memo_entries.restype = ctypes.c_uint64
    lib.memo_clears.argtypes = []; lib.memo_clears.restype = ctypes.c_uint64
    return lib


LIB = _load()
_I32 = ctypes.POINTER(ctypes.c_int32)
_I64 = ctypes.POINTER(ctypes.c_int64)
_U64 = ctypes.POINTER(ctypes.c_uint64)


# ------------------------------------------------------------- partitions etc.
def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield (); return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def zee(rho):
    z, cnt = 1, {}
    for p in rho: cnt[p] = cnt.get(p, 0) + 1
    for p, m in cnt.items(): z *= (p ** m) * factorial(m)
    return z


def tau_of(rho):
    out = []
    for r in rho:
        if r % 2: out.append(r)
        else: out += [r // 2, r // 2]
    return tuple(sorted(out, reverse=True))


class RhoList:
    """a list of partitions packed for the C engine."""
    def __init__(self, rhos):
        self.rhos = list(rhos)
        flat, off, ln = [], [], []
        for r in self.rhos:
            off.append(len(flat)); ln.append(len(r)); flat += list(r)
        self.flat = np.array(flat if flat else [0], dtype=np.int32)
        self.off = np.array(off if off else [0], dtype=np.int32)
        self.len = np.array(ln if ln else [0], dtype=np.int32)
        self.n = len(self.rhos)

    def ptrs(self):
        return (self.flat.ctypes.data_as(_I32), self.off.ctypes.data_as(_I32),
                self.len.ctypes.data_as(_I32))


def _lam_arr(lam, L):
    lam = tuple(x for x in lam if x)
    assert len(lam) <= L, (lam, L)
    return np.array(list(lam) + [0] * (L - len(lam)), dtype=np.int32)


def chi_batch(lam, rl, L=10):
    """exact chi^lam(rho) for every rho in RhoList rl (python ints)."""
    la = _lam_arr(lam, L)
    lo = np.zeros(rl.n, dtype=np.int64); hi = np.zeros(rl.n, dtype=np.int64)
    rc = LIB.chi_batch(L, la.ctypes.data_as(_I32), rl.n, *rl.ptrs(),
                       lo.ctypes.data_as(_I64), hi.ctypes.data_as(_I64))
    assert rc == 0, ("chi_batch rc", rc, lam)
    return [int(h) * (1 << 64) + (int(l) & ((1 << 64) - 1)) for l, h in zip(lo.tolist(), hi.tolist())]


def weighted_sums(lam, rl, Wmod, L=10):
    """Wmod: array shape (nw, 2, n) of residues mod (P1, P2).  Returns list of
    (r1, r2) residues of sum_rho chi^lam(rho) W_k(rho)."""
    la = _lam_arr(lam, L)
    nw = Wmod.shape[0]
    out = np.zeros(2 * nw, dtype=np.uint64)
    rc = LIB.weighted_sums(L, la.ctypes.data_as(_I32), rl.n, *rl.ptrs(), nw,
                           Wmod.ctypes.data_as(_U64), P1, P2, out.ctypes.data_as(_U64))
    assert rc == 0, ("weighted_sums rc", rc, lam)
    o = out.tolist()
    return [(int(o[2 * k]), int(o[2 * k + 1])) for k in range(nw)]


def crt_signed(r1, r2):
    M = P1 * P2
    x = (r1 + P1 * (((r2 - r1) * pow(P1, -1, P2)) % P2)) % M
    return x - M if x > M // 2 else x


def frac_mod(fr, p):
    return fr.numerator % p * pow(fr.denominator % p, -1, p) % p


# ----------------------------------------------------------- the plethysm a
@lru_cache(maxsize=None)
def pleth_pcoeffs(delta, d):
    """h_delta[h_d] in the power-sum basis {tau: Fraction} (own derivation:
    h_delta = sum_rho p_rho / z_rho, p_r[h_d] = sum_sigma p_{r sigma} / z_sigma)."""
    inner = [(sig, Fraction(1, zee(sig))) for sig in partitions(d)]
    acc = {}
    for rho in partitions(delta):
        cur = {(): Fraction(1, zee(rho))}
        for r in rho:
            nxt = {}
            for tau, c in cur.items():
                for sig, cs in inner:
                    t2 = tuple(sorted(tau + tuple(r * s for s in sig), reverse=True))
                    nxt[t2] = nxt.get(t2, Fraction(0)) + c * cs
            cur = nxt
        for t, c in cur.items():
            acc[t] = acc.get(t, Fraction(0)) + c
    return {t: c for t, c in acc.items() if c != 0}


class PlethEngine:
    def __init__(self, delta, d=4):
        self.delta, self.d = delta, d
        P = pleth_pcoeffs(delta, d)
        self.rl = RhoList(sorted(P))
        W = np.zeros((1, 2, self.rl.n), dtype=np.uint64)
        for i, t in enumerate(self.rl.rhos):
            W[0, 0, i] = frac_mod(P[t], P1); W[0, 1, i] = frac_mod(P[t], P2)
        self.W = W

    def a(self, lam, L=10):
        (r1, r2), = weighted_sums(lam, self.rl, self.W, L)
        assert r1 == r2, ("plethysm residues disagree", lam, r1, r2)   # a < p1, p2
        return r1


# --------------------------------------------------------------- m_det
class MdetEngine:
    """rect = (delta^n), N = n*delta; W1 = chi_rect^2 / z, W2 = chi_rect(tau .)/z."""
    def __init__(self, delta, n=4, verbose=False):
        t0 = time.time()
        self.delta, self.n = delta, n
        N = n * delta; self.N = N
        rect = tuple([delta] * n)
        allrho = list(partitions(N))
        rl_all = RhoList(allrho)
        LIB.memo_reset()
        row = chi_batch(rect, rl_all, L=n)          # exact rectangle row
        LIB.memo_reset()
        self.rect_row = dict(zip(allrho, row))
        supp, w1, w2 = [], [], []
        for rho in allrho:
            cr = self.rect_row[rho]; ct = self.rect_row[tau_of(rho)]
            if cr == 0 and ct == 0: continue
            z = zee(rho)
            supp.append(rho); w1.append(Fraction(cr * cr, z)); w2.append(Fraction(ct, z))
        self.rl = RhoList(supp)
        W = np.zeros((2, 2, self.rl.n), dtype=np.uint64)
        for i in range(self.rl.n):
            W[0, 0, i] = frac_mod(w1[i], P1); W[0, 1, i] = frac_mod(w1[i], P2)
            W[1, 0, i] = frac_mod(w2[i], P1); W[1, 1, i] = frac_mod(w2[i], P2)
        self.W = W
        self.frect = self.rect_row[tuple([1] * N)]
        if verbose:
            print(f"  [MdetEngine delta={delta} n={n}] N={N}: {len(allrho)} classes, "
                  f"W-support {self.rl.n}, f^rect={self.frect}  [{time.time()-t0:.0f}s]",
                  file=sys.stderr, flush=True)

    def gT(self, lam, L=10):
        (g1, g2), (t1, t2) = weighted_sums(lam, self.rl, self.W, L)
        g = crt_signed(g1, g2); T = crt_signed(t1, t2)
        assert 0 <= g <= self.frect, ("g out of bounds", lam, g)
        assert abs(T) <= g, ("|T| > g", lam, g, T)
        assert (g + T) % 2 == 0, ("parity", lam, g, T)
        return g, T

    def m_det(self, lam, L=10):
        g, T = self.gT(lam, L)
        return (g + T) // 2


# ---------------------------------------------------------------- self-test
def selftest():
    import random
    from ambient_screen import chi as chi_house, m_det as mdet_house, a as a_house
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = (got == want); ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "FAIL", label,
                                   "" if good else "got %s want %s" % (got, want)))
        sys.stdout.flush()

    print("wk9_s39_chars self-test (C engine vs house python, and the anchors)")
    # 1. exhaustive character tables N <= 14, lam with <= 10 rows, L=10
    for N in range(1, 15):
        rl = RhoList(list(partitions(N)))
        bad = 0
        for lam in partitions(N):
            if len(lam) > 10: continue
            got = chi_batch(lam, rl)
            want = [chi_house(lam, r) for r in rl.rhos]
            bad += sum(1 for x, y in zip(got, want) if x != y)
        check("full character table N=%d (rows <= 10) matches house chi" % N, bad, 0)
    # 2. sampled characters at N = 24, 32, 40 (random lam of <= 10 rows, random rho)
    rnd = random.Random(39)
    for N in (24, 32, 40):
        lams = [l for l in partitions(N) if 5 <= len(l) <= 10]
        rhos = list(partitions(N))
        sample_l = rnd.sample(lams, 6); sample_r = rnd.sample(rhos, 40)
        rl = RhoList(sample_r)
        bad = 0
        for lam in sample_l:
            got = chi_batch(lam, rl)
            want = [chi_house(lam, r) for r in sample_r]
            chi_house.cache_clear()
            bad += sum(1 for x, y in zip(got, want) if x != y)
        check("sampled chi at N=%d (6 lam x 40 rho) matches house chi" % N, bad, 0)
    # 3. the n=3 anchors: m_det sums 3, 11, 43 (supports 3, 10, 34) at delta = 2, 3, 4
    for delta, want in ((2, (3, 3)), (3, (11, 10)), (4, (43, 34))):
        E = MdetEngine(delta, n=3)
        vals = [E.m_det(lam) for lam in partitions(3 * delta) if len(lam) <= 9]
        check("n=3 delta=%d m_det (sum, support)" % delta, (sum(vals), sum(1 for v in vals if v)), want)
    # 4. the s28 precedent at n=3, delta=10: three weights with a=1, m_det=0 (lengths 8, 9)
    E = MdetEngine(10, n=3); PE = PlethEngine(10, d=3)
    for lam in ((13, 3, 2, 2, 2, 2, 2, 2, 2), (12, 5, 2, 2, 2, 2, 2, 2, 1), (9, 9, 2, 2, 2, 2, 2, 2)):
        check("s28 n=3 delta=10 %s: (a, m_det) = (1, 0)" % (lam,), (PE.a(lam), E.m_det(lam)), (1, 0))
    check("s28 n=3 delta=10 (9,4,2)+... a((9,4,2),5) = 2 via PlethEngine(5,3)", PlethEngine(5, d=3).a((9, 4, 2)), 2)
    # 5. plethysm a vs house a at n=4: every lam with <= 10 rows at delta = 5, 6 (d=4)
    for delta in (5, 6):
        PE = PlethEngine(delta, d=4)
        bad, cnt = 0, 0
        for lam in partitions(4 * delta):
            if len(lam) > 10: continue
            cnt += 1
            if PE.a(lam) != a_house(lam, delta, d=4, nv=10): bad += 1
        chi_house.cache_clear()
        check("a(lam,delta=%d) all %d weights (<=10 rows) match house a" % (delta, cnt), bad, 0)
    # 6. m_det vs s38's length-5 table (results/occurrence_screen.csv), every row delta 5..8
    csv = os.path.join(HERE, '..', 'results', 'occurrence_screen.csv')
    rows = {}
    for ln in open(csv):
        if ln.startswith('delta'): continue
        d, lam, ell, av, md, du = ln.strip().split(',')
        rows.setdefault(int(d), []).append((tuple(int(x) for x in lam.split('|')), int(av), int(md)))
    for delta in (5, 6, 7, 8):
        E = MdetEngine(delta, n=4); PE = PlethEngine(delta, d=4)
        bad = 0
        for lam, av, md in rows[delta]:
            if PE.a(lam) != av or E.m_det(lam) != md: bad += 1
        check("s38 length-5 table delta=%d: %d rows (a, m_det) reproduced" % (delta, len(rows[delta])), bad, 0)
    # 7. m_det vs house m_det directly, n=4 delta=6, a sample of 30 weights of any length <= 10
    E = MdetEngine(6, n=4)
    lams = [l for l in partitions(24) if len(l) <= 10]
    sample = rnd.sample(lams, 30)
    bad = 0
    for lam in sample:
        if E.m_det(lam) != mdet_house(lam, 4, 6): bad += 1
        chi_house.cache_clear()
    check("m_det n=4 delta=6: 30 random weights (<=10 rows) match house m_det", bad, 0)
    print("\n%s" % ("ALL CHECKS PASSED" if ok else "*** SELF-TEST FAILED ***"))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    print(__doc__)
