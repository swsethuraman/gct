#!/usr/bin/env python3
"""
scripts/ambient_screen.py -- the ambient cap, as a gate.

Both C[closure(det)] and C[closure(per)] are quotients of the SAME ambient
Sym^delta(Sym^d C^N).  So with

    a(lam, delta) = mult of S_lam(C^N) in Sym^delta(Sym^d C^N),

we have mult_det <= a and mult_per <= a, hence D = mult_per - mult_det <= a.

  a = 0  ->  both closure counts are forced to zero.  def = m on both sides
             IDENTICALLY, Def = P is an algebraic identity, and any D = 0
             measured there carries no information about anything.
  a = 1  ->  both counts are 0 or 1.  Any obstruction is an OCCURRENCE
             obstruction -- closed by Buergisser-Ikenmeyer-Panova.
  a >= 2 ->  a multiplicity obstruction is arithmetically possible.  Live.

CALL must_have_room() BEFORE MEASURING ANY CELL.  A sweep that does not screen
is spending its time on weights that cannot produce a result.

    python3 ambient_screen.py --selftest          # verify against the record
    python3 ambient_screen.py 3 5                 # stratify n=3, delta=5
    python3 ambient_screen.py 3 5 --live          # list only the live weights
"""
import sys
from fractions import Fraction
from functools import lru_cache
from math import factorial


# ----------------------------------------------------------------- partitions
def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def zee(rho):
    z, cnt = 1, {}
    for p in rho:
        cnt[p] = cnt.get(p, 0) + 1
    for p, m in cnt.items():
        z *= (p ** m) * factorial(m)
    return z


@lru_cache(maxsize=None)
def chi(lam, rho):
    """chi^lam(rho), Murnaghan-Nakayama on beta-numbers."""
    lam = tuple(x for x in lam if x)
    if not rho:
        return 1 if not lam else 0
    r, rest, L, tot = rho[0], rho[1:], len(lam), 0
    beta = [lam[j] + (L - 1 - j) for j in range(L)]
    for i in range(L):
        b = beta[i] - r
        if b < 0 or b in beta:
            continue
        nb = sorted([x for j, x in enumerate(beta) if j != i] + [b], reverse=True)
        ht = nb.index(b) - i
        new = tuple(nb[j] - (L - 1 - j) for j in range(L))
        if any(x < 0 for x in new):
            continue
        tot += ((-1) ** ht) * chi(tuple(x for x in new if x), rest)
    return tot


# ------------------------------------------------------- the ambient plethysm
@lru_cache(maxsize=None)
def _pleth_pcoeffs(delta, d):
    """h_delta[h_d] in the power-sum basis: {tau: Fraction}."""
    inner = list(partitions(d))
    acc = {}
    for rho in partitions(delta):
        cur = {(): Fraction(1, zee(rho))}
        for r in rho:
            nxt = {}
            for tau, c in cur.items():
                for sig in inner:
                    t2 = tuple(sorted(tau + tuple(r * s for s in sig), reverse=True))
                    nxt[t2] = nxt.get(t2, Fraction(0)) + c * Fraction(1, zee(sig))
            cur = nxt
        for t, c in cur.items():
            acc[t] = acc.get(t, Fraction(0)) + c
    return tuple(sorted(acc.items()))


def a(lam, delta, d=3, nv=9):
    """ambient room at lam: mult of S_lam(C^nv) in Sym^delta(Sym^d C^nv)."""
    lam = tuple(x for x in lam if x)
    if sum(lam) != delta * d or len(lam) > nv:
        return 0
    s = sum(c * chi(lam, tau) for tau, c in _pleth_pcoeffs(delta, d))
    assert s.denominator == 1, (lam, s)
    return int(s)


# ------------------------------------------------------------------ the gate
def must_have_room(lam, delta, d=3, nv=9, need=2):
    """Raise unless lam has enough ambient room to be worth measuring.

    need=1 admits the occurrence layer; need=2 (default) admits only weights
    where a MULTIPLICITY obstruction is arithmetically possible.
    """
    room = a(lam, delta, d, nv)
    if room < need:
        why = ("both closure counts are forced to 0" if room == 0
               else "both counts are 0 or 1: occurrence layer, closed by BIP")
        raise ValueError(
            "ambient screen: lam=%s delta=%d has a=%d (<%d) -- %s. "
            "Measuring this cell cannot produce a result." % (lam, delta, room, need, why))
    return room


# ------------------------------------------------------------- the easy count
def _tau(rho):
    out = []
    for r in rho:
        if r % 2:
            out.append(r)
        else:
            out += [r // 2, r // 2]
    return tuple(sorted(out, reverse=True))


def m_det(lam, n, delta):
    """dim (S_lam^*)^{Stab(det_n)}: symmetric rectangular Kronecker.

    (1/2)[ g(lam,rect,rect) + T(lam) ], T the transpose-coset average, in which
    p_r -> p_r for odd r and p_{2k} -> p_k^2 for even r.
    """
    N, rect, s = n * delta, tuple([delta] * n), Fraction(0)
    for rho in partitions(N):
        c = chi(lam, rho)
        if c:
            s += Fraction(c, zee(rho)) * (chi(rect, rho) ** 2 + chi(rect, _tau(rho)))
    s /= 2
    assert s.denominator == 1, (lam, s)
    return int(s)


# ---------------------------------------------------------------- stratifying
def stratify(n, delta, d=None):
    d = d or n
    rows = []
    for lam in partitions(delta * d):
        if len(lam) <= n * n:
            rows.append((lam, a(lam, delta, d, n * n)))
    return rows


# ------------------------------------------------------------------ self-test
CALIBRATION = """\
Sym^2(Sym^3) = s_(6) + s_(4,2)                     -> a((2,2,2),2) = 0
n=3 stratification a=0/a=1/a>=2 at delta=2,3,4,5
(9,4,2) the unique a>=2 weight at delta=5, with a=2
m_det sums 3, 11, 43 and supports 3, 10, 34 at delta=2,3,4"""


def selftest():
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-46s got %s" % ("ok" if good else "FAIL", label, got)
              + ("" if good else "  want %s" % (want,)))

    print("ambient_screen self-test")
    t2 = {lam: v for lam, v in stratify(3, 2) if v}
    check("Sym^2(Sym^3) decomposition", t2, {(6,): 1, (4, 2): 1})
    check("a((2,2,2),2)", a((2, 2, 2), 2), 0)
    for delta, want in ((2, (11, 9, 2, 0)), (3, (30, 25, 5, 0)),
                        (4, (73, 61, 12, 0)), (5, (157, 129, 27, 1))):
        rows = stratify(3, delta)
        got = (len(rows),
               sum(1 for _, v in rows if v == 0),
               sum(1 for _, v in rows if v == 1),
               sum(1 for _, v in rows if v >= 2))
        check("n=3 delta=%d  (#lam, a=0, a=1, a>=2)" % delta, got, want)
    live = [(lam, v) for lam, v in stratify(3, 5) if v >= 2]
    check("the unique live weight at delta=5", live, [((9, 4, 2), 2)])
    for delta, want in ((2, (3, 3)), (3, (11, 10)), (4, (43, 34))):
        vals = [m_det(lam, 3, delta) for lam in partitions(3 * delta) if len(lam) <= 9]
        check("m_det n=3 delta=%d (sum, support)" % delta,
              (sum(vals), sum(1 for v in vals if v)), want)
    try:
        must_have_room((2, 2, 2), 2)
        check("gate rejects a=0", "no raise", "ValueError")
    except ValueError:
        check("gate rejects a=0", "raised", "raised")
    print("\n%s" % ("ALL CHECKS PASSED" if ok else "*** SELF-TEST FAILED ***"))
    return 0 if ok else 1


# ------------------------------------------------------------------------ cli
def main(argv):
    sys.setrecursionlimit(20000)
    if "--selftest" in argv:
        return selftest()
    if len(argv) < 3:
        print(__doc__)
        return 2
    n, delta = int(argv[1]), int(argv[2])
    rows = stratify(n, delta)
    live = [(lam, v) for lam, v in rows if v >= 2]
    if "--live" in argv:
        print("live weights (a >= 2), n=%d delta=%d:" % (n, delta))
        for lam, v in sorted(live, key=lambda r: -r[1]):
            print("   lam=%-24s a=%-3d m_det=%d" % (str(lam), v, m_det(lam, n, delta)))
        if not live:
            print("   none -- nothing at this degree can carry a multiplicity obstruction")
        return 0
    z = sum(1 for _, v in rows if v == 0)
    o = sum(1 for _, v in rows if v == 1)
    print("n=%d delta=%d: %d weights (<= %d rows)" % (n, delta, len(rows), n * n))
    print("  a = 0  : %4d   forced -- D = 0 by arithmetic, no information" % z)
    print("  a = 1  : %4d   occurrence layer -- closed by BIP" % o)
    print("  a >= 2 : %4d   LIVE" % len(live))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
