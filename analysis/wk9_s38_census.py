#!/usr/bin/env python3
"""
Session 38 -- Phase 1: the delta=8, ell=5 census and the det-side measurements.

The census: for every ell=5 weight with a>=1 at delta=8, the weight-space size
N_S = #{ degree-delta monomials in the 70 coefficient functionals c_alpha
(alpha a degree-4 exponent in 5 vars) of weight exactly lam }.  Computed by a
CAPPED recursive count (never materialises the space), so huge cells cost O(cap)
not O(N_S).

Reachability: the unreduced measure() of wk8_s30_core builds flint matrices
N_S columns wide with more rows than columns; the run62 memory fit is
~7.5e-8 * N_S^2 GB, usable budget ~6.5 GB, so N_S <~ 9000 is the wall for a
single cell with the exact route (no certified ell=5 reduction is available --
see PREREG_s38 section 0).

Measurement: for reachable cells, det-side mult via measure(det_4, 16, 4, 5,
delta, lam) -- a two-prime rank that attains a is a certificate that
det_units = a - mult.  A bite (mult < a) gets the sceptical recheck.

Usage:
    wk9_s38_census.py sizes <delta> [--cap N] [--csv path]
    wk9_s38_census.py validate6              # reproduce n4_gate delta=6 ell=5 cells
    wk9_s38_census.py measure <delta> <NS_cap> [--csv path] [--seed s]
"""
import sys, time
sys.setrecursionlimit(400000)
sys.path.insert(0, 'scripts')
sys.path.insert(0, 'analysis')
from ambient_screen import a as amb_a, m_det, partitions
from wk8_s30_core import exps, monomials, build_R, restrict, eval_row, det_form, \
    rank_of, measure, P1, P2

E5 = exps(4, 5)                 # 70 degree-4 exponents in 5 vars
NE5 = len(E5)


def ns_capped(delta, lam, cap):
    """count degree-delta monomials in E5 of weight lam, capped at cap+1.
    Mirrors wk8_s30_core.monomials' recursion but counts (with early exit)."""
    lam = tuple(lam) + (0,) * (5 - len(lam))
    if sum(lam) != 4 * delta:
        return 0
    A = E5
    total = 0

    def rec(start, left, rem):
        nonlocal total
        if total > cap:
            return
        if left == 0:
            if not any(rem):
                total += 1
            return
        if sum(rem) != left * 4:
            return
        for i in range(start, NE5):
            al = A[i]
            if any(al[j] > rem[j] for j in range(5)):
                continue
            rec(i, left - 1, tuple(rem[j] - al[j] for j in range(5)))
            if total > cap:
                return
    rec(0, delta, lam)
    return total


def census(delta, cap=20000, ell=5):
    """rows (lam, a, m_det, N_S_capped) for ell=5, a>=1, sorted by N_S then a."""
    N = 4 * delta
    rows = []
    for lam in partitions(N):
        if len(lam) != ell:
            continue
        av = amb_a(lam, delta, d=4, nv=ell)
        if av < 1:
            continue
        md = m_det(lam, 4, delta)
        ns = ns_capped(delta, lam, cap)
        rows.append((lam, av, md, ns))
    rows.sort(key=lambda r: (r[3], -r[1], r[0]))
    return rows


def validate6():
    """Reproduce the nine banked delta=6, ell=5 cells of docs/n4_gate.md sec 6:
    mult_det = a at each, by the unreduced measure()."""
    banked = [((14, 5, 2, 2, 1), 2), ((13, 5, 4, 1, 1), 2), ((12, 7, 3, 1, 1), 3),
              ((13, 6, 2, 2, 1), 3), ((11, 8, 3, 1, 1), 2), ((14, 4, 2, 2, 2), 2),
              ((12, 7, 2, 2, 1), 3), ((12, 6, 4, 1, 1), 2), ((12, 5, 5, 1, 1), 2)]
    d4, N4 = det_form(4)
    ok = True
    print("validate6: n4_gate.md sec 6 -- delta=6 ell=5, expect mult_det = a")
    for lam, a_exp in banked:
        t0 = time.time()
        av2 = amb_a(lam, 6, d=4, nv=5)
        res = measure(d4, N4, 4, 5, 6, lam, a_expect=a_exp)
        good = (av2 == a_exp and res['a'] == a_exp and res['mult'] == a_exp)
        ok &= good
        print("  [%s] lam=%-20s a=%d (pleth %d) mult_det=%d  N_S=%d  [%.0fs]"
              % ("ok" if good else "FAIL", str(lam), res['a'], av2, res['mult'],
                 res['nbasis'], time.time() - t0))
        sys.stdout.flush()
    print("VALIDATE6 %s" % ("PASS" if ok else "*** FAIL ***"))
    return ok


def measure_cell(delta, lam, a_exp, seed=11, primes=(P1, P2)):
    """det-side mult with the sceptical recheck on a bite."""
    d4, N4 = det_form(4)
    res = measure(d4, N4, 4, 5, delta, lam, seed=seed, primes=primes, a_expect=a_exp)
    if res['mult'] < a_exp:                       # a bite -- recheck sceptically
        res2 = measure(d4, N4, 4, 5, delta, lam, npts=3 * a_exp + 24, seed=907,
                       primes=primes, a_expect=a_exp)
        assert res2['mult'] == res['mult'], ("bite unstable", lam, res, res2)
        res['rechecked'] = True
    return res


def read_census(path):
    rows = []
    import csv
    for r in csv.DictReader(open(path)):
        lam = tuple(int(x) for x in r['lam'].split('|'))
        rows.append((lam, int(r['a']), int(r['m_det']), int(r['NS_capped'])))
    return rows


def measurecsv(argv):
    """Measure det-side mult on reachable delta=8 cells read from a census CSV,
    ascending N_S, banking each to results/onset_ledger.md.  Stops on first bite
    for the full sceptical protocol."""
    census_csv = argv[1]
    delta = int(argv[2])
    ns_cap = int(argv[3])
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 11
    lo = int(argv[argv.index('--lo') + 1]) if '--lo' in argv else 0
    rows = [r for r in read_census(census_csv) if lo < r[3] <= ns_cap]
    rows.sort(key=lambda r: (r[3], -r[1]))
    ledger = 'results/onset_ledger.md'
    d4, N4 = det_form(4)
    print("measurecsv delta=%d: %d cells with %d<N_S<=%d (seed=%d)"
          % (delta, len(rows), lo, ns_cap, seed))
    for lam, av, md, ns in rows:
        t0 = time.time()
        res = measure_cell(delta, lam, av, seed=seed)
        du = av - res['mult']
        rechk = res.get('rechecked', False)
        line = ("| %s | %d | %d | %d | %d | %d | %+d | %s |"
                % (str(lam), 5, av, md, ns, res['mult'], du,
                   ("BITE, rechecked" if du > 0 else "=a")))
        with open(ledger, 'a') as fh:
            fh.write(line + "\n"); fh.flush()
        print("  %-24s a=%-2d m_det=%-4d N_S=%-5d mult_det=%-2d det_units=%d%s [%.0fs]"
              % (str(lam), av, md, ns, res['mult'], du,
                 "  *** BITE ***" if du > 0 else "", time.time() - t0))
        sys.stdout.flush()
        if du > 0:
            print("STOP: first bite at lam=%s delta=%d, det_units=%d "
                  "(mult_det=%d < a=%d). Hand to full protocol." % (lam, delta, du, res['mult'], av))
            return 0
    print("measurecsv done: no bite up to N_S<=%d at delta=%d" % (ns_cap, delta))
    return 0


def main(argv):
    if argv[0] == 'measurecsv':
        return measurecsv(argv)
    if argv[0] == 'sizes':
        delta = int(argv[1])
        cap = int(argv[argv.index('--cap') + 1]) if '--cap' in argv else 20000
        t0 = time.time()
        rows = census(delta, cap)
        reach = [r for r in rows if r[3] <= 9000]
        print("delta=%d ell=5: %d cells (a>=1); N_S capped at %d" % (delta, len(rows), cap))
        print("reachable unreduced (N_S<=9000): %d cells" % len(reach))
        print("  lam                      a    m_det   N_S(<=cap)")
        for lam, av, md, ns in rows[:40]:
            tag = "" if ns <= 9000 else "  (wall)"
            print("  %-24s %-4d %-6d %s%s"
                  % (str(lam), av, md, ns if ns <= cap else ">%d" % cap, tag))
        print("  [%.0fs]" % (time.time() - t0))
        if '--csv' in argv:
            with open(argv[argv.index('--csv') + 1], 'w') as fh:
                fh.write("delta,lam,a,m_det,NS_capped\n")
                for lam, av, md, ns in rows:
                    fh.write("%d,%s,%d,%d,%d\n" % (delta, "|".join(map(str, lam)), av, md, ns))
            print("wrote csv")
        return 0
    if argv[0] == 'validate6':
        return 0 if validate6() else 1
    if argv[0] == 'measure':
        delta = int(argv[1]); ns_cap = int(argv[2])
        seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 11
        rows = census(delta, ns_cap)
        pool = [r for r in rows if 0 < r[3] <= ns_cap]
        print("measure delta=%d: %d cells with 0<N_S<=%d, ascending N_S" % (delta, len(pool), ns_cap))
        print("  lam                      a  m_det  N_S  mult_det  det_units  D?")
        csvp = argv[argv.index('--csv') + 1] if '--csv' in argv else None
        fh = open(csvp, 'w') if csvp else None
        if fh: fh.write("delta,lam,a,m_det,NS,mult_det,det_units\n")
        for lam, av, md, ns in pool:
            t0 = time.time()
            res = measure_cell(delta, lam, av, seed=seed)
            du = av - res['mult']
            flag = "  *** BITE ***" if du > 0 else ""
            print("  %-24s %-2d %-5d %-5d  %-2d %-6s  %d%s  [%.0fs]"
                  % (str(lam), av, md, ns, res['mult'],
                     "(=a)" if res['mult'] == av else "(<a)", du, flag, time.time() - t0))
            sys.stdout.flush()
            if fh:
                fh.write("%d,%s,%d,%d,%d,%d,%d\n"
                         % (delta, "|".join(map(str, lam)), av, md, ns, res['mult'], du))
                fh.flush()
            if du > 0:
                print("  -> BITE at lam=%s: det_units=%d (mult_det=%d < a=%d). "
                      "First onset candidate; stop sweep for full protocol." % (lam, du, res['mult'], av))
                break
        if fh: fh.close()
        return 0
    print(__doc__); return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
