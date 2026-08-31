"""Week 2, session 23 -- regression + sweep for the attainment question.

P1 gate: the top-weight criterion must reproduce the conductor read off the
multiplicity tables on the whole banked delta <= 10 range.
Then: the attainment sweep, far beyond delta = 10.
"""
import sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from wk2_s23_transport import *


def dominants(n):
    out = []
    for l1 in range(n + 1):
        for l2 in range(min(l1, n - l1) + 1):
            l3 = n - l1 - l2
            if 0 <= l3 <= l2: out.append((l1, l2, l3))
    return out


def regression(dmax=10, kmax=6, verbose=True):
    h3 = hist3(dmax + 6 * kmax)
    bad = []; tested = 0; positives = 0
    modsix = []            # nu not divisible by 6 -- must never happen
    for d in range(1, dmax + 1):
        for lam in dominants(3 * d):
            m = H_invariants_dim(lam)
            ct, _ = conductor_table(lam, h3, kmax=kmax)
            shp = shapes(lam)
            nu, wit = top_weight_max(lam, shp)
            cw = None if nu is None else max(0, nu // 6)
            if nu is not None and nu % 6: modsix.append((lam, nu))
            tested += 1
            if m > 0: positives += 1
            ok = (m == 0 and nu is None) or (m > 0 and cw == ct)
            if not ok:
                bad.append((lam, d, m, ct, nu, cw))
    if verbose:
        print(f"P1 regression, delta <= {dmax}: {tested} weights, "
              f"{positives} with m > 0, mismatches {len(bad)}")
        print(f"   nu not divisible by 6: {len(modsix)} (must be 0)")
        for b in bad[:20]: print("   MISMATCH", b)
    return bad, modsix, positives


def attainment_sweep(dmax, report_every=None):
    """For every lambda with |lambda| = 3 delta, delta <= dmax:
       does the component at nu* = 6 floor(mu_max/6) survive?"""
    fails_positive = []      # m > 0 but not attained  -- FALSIFIER F3
    orphans = []             # m = 0 with shadow pole >= 1
    attained_zero_m = []     # m = 0 yet attained -- would break "exactly"
    n = 0
    for d in range(1, dmax + 1):
        for lam in dominants(3 * d):
            mu = lam[0] - 2 * lam[2]
            m = H_invariants_dim(lam)
            shp = shapes(lam)
            wit = attained(lam, shp) if mu >= 0 else None
            n += 1
            if m > 0 and mu >= 6 and wit is None:
                fails_positive.append((lam, d, m))
            if m > 0 and mu >= 0 and wit is None and mu // 6 >= 1:
                pass
            if m == 0:
                if mu // 6 >= 1: orphans.append((lam, d))
                if wit is not None: attained_zero_m.append((lam, d))
        if report_every and d % report_every == 0:
            print(f"   ... delta {d} done, {n} weights, "
                  f"{len(fails_positive)} attainment failures with m>0")
    return fails_positive, orphans, attained_zero_m, n


if __name__ == '__main__':
    t0 = time.time()
    bad, modsix, pos = regression(10, 6)
    print(f"   [{time.time()-t0:.1f}s]")
    dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    t0 = time.time()
    fails, orph, az, n = attainment_sweep(dmax, report_every=2)
    print(f"\nattainment sweep delta <= {dmax}: {n} weights, "
          f"{len(fails)} failures with m > 0 (F3), "
          f"{len(orph)} orphans (m = 0, shadow >= 1), "
          f"{len(az)} m=0-but-attained")
    for f in fails[:20]: print("   F3 FIRED:", f)
    print("   orphans:", orph)
    print(f"   [{time.time()-t0:.1f}s]")
