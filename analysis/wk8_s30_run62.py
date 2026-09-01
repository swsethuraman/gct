#!/usr/bin/env python3
"""Session 30 -- sweep the 62 with the fast path, banking each cell."""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_fast import cell
from wk8_s30_core import det_form, per_padded, monomials
from wk8_s30_pleth import a_of, amb
from wk8_s30_sweep import cells62, NINE, order, balance

LEDGER = "/root/gct/results/sweep62_ledger.md"
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 9000

d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
allc = [c for c in cells62() if c[0] not in set(NINE)]
sizes = {lam: len(monomials(4, len(lam), 6, lam)) for lam, _ in allc}
seq = [c for c in order(allc, sizes) if sizes[c[0]] <= CAP]
print("the 62: %d cells; %d within cap N_S <= %d" % (len(allc), len(seq), CAP))
print("order interleaves 3 cheapest : 1 most-balanced/largest-a, on purpose")
print("lam                     ell  a   N_S   mult_det mult_pad   D     secs")
sys.stdout.flush()

done = hits = shortdet = shortpad = 0
for lam, av in seq:
    r, ns = len(lam), sizes[lam]
    t0 = time.time()
    res = cell([('det', d4, N4), ('pad', pd, Np)], 4, r, 6, lam, av,
               seeds={'det': 11, 'pad': 29}, verbose=False)
    md, mp = res['det'], res['pad']
    for nm, m, f, N in (("det", md, d4, N4), ("pad", mp, pd, Np)):
        if m < av:                       # a short rank is re-run at 3x points
            r2 = cell([(nm, f, N)], 4, r, 6, lam, av, npts=3 * av + 24,
                      seeds={nm: 907}, verbose=False)
            assert r2[nm] == m, ("short rank unstable", lam, nm, m, r2[nm])
    D = mp - md
    done += 1
    shortdet += (md < av); shortpad += (mp < av)
    if D > 0: hits += 1
    with open(LEDGER, "a") as fh:
        fh.write("| %s | %d | %d | %d | %d | %d | %+d |\n"
                 % (str(lam), r, av, ns, md, mp, D))
    print("%-24s %2d %3d %6d    %2d %-5s %2d %-5s %+3d %6.0f%s"
          % (str(lam), r, av, ns, md, "(=a)" if md == av else "(<a)",
             mp, "(=a)" if mp == av else "(<a)", D, time.time() - t0,
             "   *** D>0 STOP ***" if D > 0 else ""))
    sys.stdout.flush()
    if D > 0: break
print()
print("completed %d of 62 (%.0f%%); D>0: %d; mult_det<a: %d; mult_pad<a: %d"
      % (done, 100.0 * done / 62, hits, shortdet, shortpad))
