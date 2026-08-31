"""Session 26 -- the regression suite.  Reproduces every headline number of the
session from scratch, in about 15 seconds, with no engine and no long run.

    python3 analysis/wk6_s26_regress.py
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'scripts'))
from wk6_s26_core import partitions, a_pleth, a_weyl, m_det
from wk6_s26_hwv import measure, measure_fast, measure_np, P1, P2
from wk6_s26_density import jacobian_rank
import ambient_screen as S

CELLS = [((12, 6), 6, 2, 2), ((15, 6), 7, 2, 2), ((9, 4, 2), 5, 2, 3),
         ((12, 4, 2), 6, 2, 3), ((13, 6, 2), 7, 3, 4)]


def main():
    t = time.time()
    ok = True

    def ck(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-52s %s" % ("ok" if good else "FAIL", lab, got)
              + ("" if good else "  want %s" % (want,)))

    print("SESSION 26 REGRESSION")
    ck("Sym^2(Sym^3) constituents (plethysm route)",
       [l for l in partitions(6) if a_pleth(l, 2)], [(6,), (4, 2)])
    ck("same, Weyl alternating sum over weight counts",
       [l for l in partitions(6) if a_weyl(l, 2)], [(6,), (4, 2)])
    ck("m_det rows (sum, support) at delta = 2,3,4",
       [(sum(m_det(l, 3, d) for l in partitions(3 * d) if len(l) <= 9),
         sum(1 for l in partitions(3 * d) if len(l) <= 9 and m_det(l, 3, d)))
        for d in (2, 3, 4)], [(3, 3), (11, 10), (43, 34)])
    ck("agrees with ambient_screen on a, delta <= 5",
       all(a_pleth(l, d) == S.a(l, d) for d in range(1, 6)
           for l in partitions(3 * d) if len(l) <= 9), True)
    ck("agrees with ambient_screen on m_det, delta <= 4",
       all(m_det(l, 3, d) == S.m_det(l, 3, d) for d in range(1, 5)
           for l in partitions(3 * d) if len(l) <= 9), True)
    for lam, d, aa, md in CELLS:
        a1, r1, _, _, _ = measure(lam, d, 'det', npts=8)
        a2, r2, _ = measure_fast(lam, d, 'det', mods=(P1, P2), check_q=True)
        a3, r3, _ = measure_np(lam, d, 'det', a_known=aa)
        p3 = measure_np(lam, d, 'per', a_known=aa)[1]
        ck("cell %s d=%d (a, m_det, mult_det, mult_per)" % (str(lam), d),
           (a1, md, r1, p3), (aa, md, aa, aa))
        ck("   three implementations agree", (a1, r1) == (a2, r2) == (a3, r3), True)
    ck("det Jacobian ranks r = 2..6",
       [jacobian_rank(r, 'det')[0] for r in range(2, 7)], [4, 10, 20, 29, 38])
    ck("per Jacobian ranks r = 2..6",
       [jacobian_rank(r, 'per')[0] for r in range(2, 7)], [4, 10, 20, 35, 50])
    ck("a <= m_det on every ell <= 4 weight, delta <= 7",
       all(a_pleth(l, d) <= m_det(l, 3, d) for d in range(1, 8)
           for l in partitions(3 * d) if len(l) <= 4), True)
    ck("sum m_det - sum a = published total deficits",
       [sum(m_det(l, 3, d) for l in partitions(3 * d) if len(l) <= 9)
        - sum(a_pleth(l, d) for l in partitions(3 * d) if len(l) <= 9)
        for d in range(2, 8)], [1, 6, 31, 141, 618, 2488])
    print("\n%s  [%.0fs]" % ("ALL REGRESSION CHECKS PASSED" if ok
                             else "*** REGRESSION FAILED ***", time.time() - t))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
