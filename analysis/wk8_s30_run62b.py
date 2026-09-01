#!/usr/bin/env python3
"""Session 30 -- coverage pass: the 62 in ASCENDING N_S, skipping cells the
interleaved run has already banked.  Run alongside wk8_s30_run62.py so that the
expensive balanced/large-a regime test does not starve coverage."""
import sys, time, os
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_fast import cell
from wk8_s30_core import det_form, per_padded, monomials
from wk8_s30_sweep import cells62, NINE

LEDGER = "/root/gct/results/sweep62_ledger_asc.md"
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 7000
SKIP = {(13,5,3,2,1),(11,8,2,2,1),(10,9,2,2,1)}      # already banked
d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
allc = [c for c in cells62() if c[0] not in set(NINE) and c[0] not in SKIP]
sizes = {lam: len(monomials(4, len(lam), 6, lam)) for lam, _ in allc}
seq = sorted([c for c in allc if sizes[c[0]] <= CAP], key=lambda c: sizes[c[0]])
print("coverage pass: %d cells with N_S <= %d" % (len(seq), CAP))
print("lam                     ell  a   N_S   mult_det mult_pad   D     secs")
sys.stdout.flush()
for lam, av in seq:
    r, ns = len(lam), sizes[lam]
    t0 = time.time()
    res = cell([('det', d4, N4), ('pad', pd, Np)], 4, r, 6, lam, av,
               seeds={'det': 11, 'pad': 29}, verbose=False)
    md, mp = res['det'], res['pad']
    for nm, m, f, N in (("det", md, d4, N4), ("pad", mp, pd, Np)):
        if m < av:
            r2 = cell([(nm, f, N)], 4, r, 6, lam, av, npts=3 * av + 24,
                      seeds={nm: 907}, verbose=False)
            assert r2[nm] == m, ("short rank unstable", lam, nm, m, r2[nm])
    D = mp - md
    with open(LEDGER, "a") as fh:
        fh.write("| %s | %d | %d | %d | %d | %d | %+d |\n" % (str(lam), r, av, ns, md, mp, D))
    print("%-24s %2d %3d %6d    %2d %-5s %2d %-5s %+3d %6.0f%s"
          % (str(lam), r, av, ns, md, "(=a)" if md == av else "(<a)",
             mp, "(=a)" if mp == av else "(<a)", D, time.time() - t0,
             "   *** D>0 STOP ***" if D > 0 else ""))
    sys.stdout.flush()
    if D > 0: break
