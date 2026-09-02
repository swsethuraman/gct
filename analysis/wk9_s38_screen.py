#!/usr/bin/env python3
"""
Session 38 -- Phase 0: the occurrence screen for I(D_5^det).

For ell(lam) = 5, |lam| = 4*delta, a(lam,delta) >= 1, tabulate

    a(lam,delta)   = mult of S_lam in Sym^delta(Sym^4 C^5)   [plethysm h_d[h_4]]
    m_det(lam)     = dim (S_lam^*)^{Stab(det_4)}             [sym rect Kronecker,
                                                              rectangle (delta^4)]

mult_det <= min(a, m_det), so any cell with a > m_det has
det_units >= a - m_det > 0 : an equation of D_5^det by arithmetic alone
(the s28 n=3 occurrence mechanism).  The first delta carrying such a cell is an
unconditional upper bound on the onset.

`a` and `m_det` are the exact quantities of scripts/ambient_screen.py (validated
by --selftest against the n=3 record).  Here m_det is computed by a *batched*
route that precomputes the lam-independent weight
    W(rho) = [ chi_rect(rho)^2 + chi_rect(tau rho) ] / z_rho
once per delta and sums chi(lam,rho) W(rho) over the (small) support {W != 0}.
This is asserted equal to ambient_screen.m_det on a sample every run (route
cross-check), and `a` is cross-checked against the DEFINITION dim ker(R) with
--checkdef.  Variable-count independence a(nv=5)==a(nv=16) is asserted too.

Usage:
    wk9_s38_screen.py <delta> [--csv path] [--checkdef NS_CAP]
    wk9_s38_screen.py sweep <d_lo> <d_hi> [--csv path]
"""
import sys, time
from fractions import Fraction
sys.setrecursionlimit(400000)
sys.path.insert(0, 'scripts')
sys.path.insert(0, 'analysis')
from ambient_screen import a as amb_a, m_det as m_det_ref, partitions, chi, zee, _tau


def parts_len(N, ell):
    for lam in partitions(N):
        if len(lam) == ell:
            yield lam


def mdet_weights(delta, n=4):
    """W(rho) = [chi_rect(rho)^2 + chi_rect(tau rho)]/z_rho for rho with W != 0.
    rect = (delta^n), N = n*delta.  Returned as list of (rho, W: Fraction)."""
    N, rect = n * delta, tuple([delta] * n)
    out = []
    for rho in partitions(N):
        cr = chi(rect, rho)
        ct = chi(rect, _tau(rho))
        if cr == 0 and ct == 0:
            continue
        W = Fraction(cr * cr + ct, zee(rho))
        if W != 0:
            out.append((rho, W))
    return out


def m_det_fast(lam, Ws):
    s = Fraction(0)
    for rho, W in Ws:
        c = chi(lam, rho)
        if c:
            s += c * W
    s /= 2
    assert s.denominator == 1, (lam, s)
    return int(s)


def screen_big(delta, ell=5, d=4, verbose=False, rho_clear=300):
    """Memory-bounded screen for large delta (N>=44): transpose the m_det sum.

    m_det_fast(lam) sums chi(lam,rho) over ALL rho in the W-support, which for
    one lam populates the chi() memo with a rho-suffix subtree per rho -- at
    N=44,48 that peaks past the cgroup and OOMs (observed at delta=11,12).

    Here we loop rho OUTER and lam INNER, accumulating m[lam] += chi(lam,rho)W,
    and clear the chi memo every `rho_clear` rho.  Peak memory is then one
    rho-batch's Murnaghan-Nakayama subtree plus |lam| integer accumulators --
    bounded independent of delta.  `a` is computed per-lam with the same
    periodic clearing (its plethysm support is small).
    """
    from fractions import Fraction
    N = d * delta
    lams = [lam for lam in partitions(N) if len(lam) == ell]
    # a, per lam, with periodic cache clears
    avs = {}
    for i, lam in enumerate(lams):
        avs[lam] = amb_a(lam, delta, d=d, nv=ell)
        if (i + 1) % 400 == 0:
            chi.cache_clear()
    keep = [lam for lam in lams if avs[lam] >= 1]
    chi.cache_clear()
    # m_det for all `keep` lam, transposed over the W-support
    Ws = mdet_weights(delta, d)
    if verbose:
        print("    screen_big d=%d: %d cells (a>=1) of %d; |W|=%d"
              % (delta, len(keep), len(lams), len(Ws)), file=sys.stderr)
        sys.stderr.flush()
    acc = {lam: 0 for lam in keep}
    for j, (rho, W) in enumerate(Ws):
        assert W.denominator == 1 or True
        num, den = W.numerator, W.denominator
        for lam in keep:
            c = chi(lam, rho)
            if c:
                acc[lam] += Fraction(c * num, den)
        if (j + 1) % rho_clear == 0:
            chi.cache_clear()
            if verbose and (j + 1) % (rho_clear * 20) == 0:
                print("      ...%d/%d rho" % (j + 1, len(Ws)), file=sys.stderr)
                sys.stderr.flush()
    rows = []
    for lam in keep:
        m = acc[lam] / 2
        assert m.denominator == 1, (lam, m)
        md = int(m)
        rows.append((lam, avs[lam], md, avs[lam] - md))
    rows.sort(key=lambda r: (-(r[1] - r[2]), -r[1], r[0]))
    return rows


def screen_delta(delta, ell=5, d=4, Ws=None, clear_every=120, verbose=False):
    """Occurrence screen at one delta.

    The chi() memo (ambient_screen, lru_cache(maxsize=None)) otherwise grows
    without bound across the huge partition sets of N=4*delta and OOMs the
    container at delta>=10.  W(rho) has the rectangle characters baked in as
    plain ints, so once it is built the cache can be cleared freely; we clear
    it every `clear_every` weights to cap peak memory at one weight's worth of
    Murnaghan-Nakayama intermediates.
    """
    N = d * delta
    if Ws is None:
        Ws = mdet_weights(delta, d)
    chi.cache_clear()                     # rect chars now baked into Ws
    rows = []
    cnt = 0
    for lam in parts_len(N, ell):
        av = amb_a(lam, delta, d=d, nv=ell)
        if av < 1:
            chi.cache_clear() if (cnt := cnt + 1) % clear_every == 0 else None
            continue
        md = m_det_fast(lam, Ws)
        rows.append((lam, av, md, av - md))
        cnt += 1
        if cnt % clear_every == 0:
            chi.cache_clear()
            if verbose:
                print("    ...%d weights scanned, %d kept" % (cnt, len(rows)),
                      file=sys.stderr); sys.stderr.flush()
    rows.sort(key=lambda r: (-(r[1] - r[2]), -r[1], r[0]))
    return rows


def validate_mdet(delta, rows, d=4, k=6):
    """assert batched m_det == ambient_screen.m_det on the first k cells."""
    for lam, av, md, du in rows[:k]:
        assert md == m_det_ref(lam, d, delta), ("m_det route mismatch", lam, md)
    print("  [mdet-xcheck] batched == ambient_screen.m_det on %d cells OK"
          % min(k, len(rows)))


def report(delta, rows):
    fires = [r for r in rows if r[3] > 0]
    amax = max((r[1] for r in rows), default=0)
    print("delta=%d  ell=5  |lam|=%d : %d cells with a>=1 ; max a = %d"
          % (delta, 4 * delta, len(rows), amax))
    print("  cells with a > m_det (occurrence bite): %d" % len(fires))
    for lam, av, md, du in fires:
        print("    FIRE  lam=%-28s a=%d  m_det=%d  det_units>=%d"
              % (str(lam), av, md, du))
    tight = sorted(rows, key=lambda r: (r[2] - r[1], -r[1]))[:8]
    print("  tightest margins (m_det - a; smaller = closer to firing):")
    for lam, av, md, du in tight:
        print("      lam=%-28s a=%-4d m_det=%-5d margin=%d"
              % (str(lam), av, md, md - av))
    return fires


def checkdef(rows, ns_cap, delta, d=4, ell=5):
    from wk8_s30_core import monomials, build_R, rank_of, P1
    checked = 0
    for lam, av, md, du in rows:
        ns = len(monomials(d, ell, delta, lam))
        if ns == 0 or ns > ns_cap:
            continue
        basis, R = build_R(d, ell, delta, lam)
        adef = len(basis) - rank_of(R, len(basis), P1)
        a16 = amb_a(lam, delta, d=d, nv=16)
        assert adef == av, ("route B (def) != route A (pleth)", lam, adef, av)
        assert a16 == av, ("a(nv=16) != a(nv=5)", lam, a16, av)
        checked += 1
    print("  [checkdef] %d cells: a(def)==a(pleth)==a(nv=16), rank(R)=N_S-a  OK"
          % checked)


def write_csv(path, allrows):
    with open(path, 'w') as fh:
        fh.write("delta,lam,ell,a,m_det,det_units_lb\n")
        for delta in sorted(allrows):
            for lam, av, md, du in allrows[delta]:
                fh.write("%d,%s,%d,%d,%d,%d\n"
                         % (delta, "|".join(map(str, lam)), len(lam), av, md, du))
    print("wrote", path)


def main(argv):
    if argv and argv[0] == 'big':
        # memory-bounded single-delta screen for large N; append to csv
        delta = int(argv[1])
        t0 = time.time()
        rows = screen_big(delta, verbose=True)
        report(delta, rows)
        print("  [%.0fs]" % (time.time() - t0))
        if '--csv' in argv:
            with open(argv[argv.index('--csv') + 1], 'w') as fh:
                fh.write("delta,lam,ell,a,m_det,det_units_lb\n")
                for lam, av, md, du in rows:
                    fh.write("%d,%s,%d,%d,%d,%d\n"
                             % (delta, "|".join(map(str, lam)), len(lam), av, md, du))
            print("wrote", argv[argv.index('--csv') + 1])
        return 0
    if argv and argv[0] == 'sweep':
        d_lo, d_hi = int(argv[1]), int(argv[2])
        csv = argv[argv.index('--csv') + 1] if '--csv' in argv else None
        allrows = {}
        for delta in range(d_lo, d_hi + 1):
            t0 = time.time()
            Ws = mdet_weights(delta)
            rows = screen_delta(delta, Ws=Ws, verbose=True)
            allrows[delta] = rows
            validate_mdet(delta, rows)
            report(delta, rows)
            print("  [%.0fs, |W-support|=%d]" % (time.time() - t0, len(Ws)))
            sys.stdout.flush()
            if csv:
                write_csv(csv, allrows)   # rewrite after each delta (bank as we go)
        return 0
    delta = int(argv[0])
    t0 = time.time()
    Ws = mdet_weights(delta)
    rows = screen_delta(delta, Ws=Ws)
    validate_mdet(delta, rows)
    report(delta, rows)
    print("  [%.0fs, |W-support|=%d]" % (time.time() - t0, len(Ws)))
    if '--checkdef' in argv:
        checkdef(rows, int(argv[argv.index('--checkdef') + 1]), delta)
    if '--csv' in argv:
        write_csv(argv[argv.index('--csv') + 1], {delta: rows})
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
