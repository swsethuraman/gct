"""Session 28 -- where does the ideal first bite?

By Proposition 5 (docs/isotypic_rank.md), for ell(lam) = r,

    mult_lam C[closure(GL_9 det_3)]_delta  =  mult_lam C[D_r]_delta ,

and mult <= min( a(lam,delta), m_det(lam) ) always.  So

    a(lam,delta) > m_det(lam)  at a weight of length >= 5
        ==>  mult < a  ==>  I(D_r) != 0 in that degree,

a PROOF of biting from two classical counts with no geometry in them.  This
sweep looks for the first such (delta, lam), and reports the whole profile so
that a geometric bite (mult < min(a, m_det)) can be distinguished from an
arithmetic one.

Nothing here is a rank computation: it is the cheap necessary-and-sufficient
arithmetic that decides most of the question in advance.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import partitions, a_pleth, m_det


def sweep(dmin=2, dmax=10, lmin=5, lmax=9, verbose=True):
    """Return the list of (delta, lam, a, m_det) with a > m_det."""
    hits = []
    for d in range(dmin, dmax + 1):
        t = time.time()
        n = 0
        ties = 0
        worst = None
        for lam in partitions(3 * d):
            if not (lmin <= len(lam) <= lmax):
                continue
            aa = a_pleth(lam, d)
            if aa == 0:
                continue
            n += 1
            md = m_det(lam, 3, d)
            if aa > md:
                hits.append((d, lam, aa, md))
            if aa == md:
                ties += 1
            gap = md - aa
            if worst is None or gap < worst[0]:
                worst = (gap, lam, aa, md)
        if verbose:
            print("delta=%2d: %4d weights with a>0 and length in [%d,%d]; "
                  "a > m_det at %d; ties %d; tightest %s  [%.0fs]"
                  % (d, n, lmin, lmax,
                     sum(1 for h in hits if h[0] == d), ties, worst,
                     time.time() - t), flush=True)
    return hits


if __name__ == '__main__':
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    lmin = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    hits = sweep(lo, hi, lmin)
    print()
    if hits:
        print("FIRST ARITHMETIC BITE at delta = %d:" % hits[0][0])
        for h in hits:
            if h[0] == hits[0][0]:
                print("   lam=%-28s a=%d  m_det=%d  ->  mult <= %d < a"
                      % (str(h[1]), h[2], h[3], h[3]))
    else:
        print("no arithmetic bite in the swept range")
