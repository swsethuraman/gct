#!/usr/bin/env python3
"""
Session 30 -- the 62.  n=4, delta=6, a>=2, ell>=5, minus session 27's nine.

Sweep order is deliberately NOT pure ascending N_S: session 27's nine were the
nine cheapest, and cheapness selects LOPSIDED weights (large lam_1, short tail,
small a).  To test the regime rather than extend it, the order interleaves the
ascending sweep with a pass over the largest-a / most balanced cells.

Each cell banked to results/sweep62_ledger.md as it completes.
"""
import sys, time, os, json
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_core import measure, det_form, per_padded, monomials, P1, P2
from wk8_s30_pleth import amb

NINE = [(14,5,2,2,1),(13,5,4,1,1),(12,7,3,1,1),(13,6,2,2,1),(11,8,3,1,1),
        (14,4,2,2,2),(12,7,2,2,1),(12,6,4,1,1),(12,5,5,1,1)]
LEDGER = "/root/gct/results/sweep62_ledger.md"

def cells62():
    A = amb(6, 4, 16)
    out = []
    for lam, av in A.items():
        if av >= 2 and len(lam) >= 5:
            out.append((lam, av))
    return out

def balance(lam):
    """0 = perfectly balanced; larger = more lopsided."""
    return max(lam) - min(lam)

def order(cells, sizes):
    asc = sorted(cells, key=lambda c: sizes[c[0]])
    bal = sorted(cells, key=lambda c: (-c[1], balance(c[0]), sizes[c[0]]))
    seq, seen = [], set()
    ia = ib = 0
    while len(seq) < len(cells):
        for _ in range(3):                      # 3 cheap : 1 balanced
            while ia < len(asc) and asc[ia][0] in seen: ia += 1
            if ia < len(asc): seq.append(asc[ia]); seen.add(asc[ia][0])
        while ib < len(bal) and bal[ib][0] in seen: ib += 1
        if ib < len(bal): seq.append(bal[ib]); seen.add(bal[ib][0])
    return seq

def bank(line):
    with open(LEDGER, "a") as fh: fh.write(line + "\n")

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else "nine"
    CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 12000
    d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
    if mode == "nine":
        todo = [(lam, amb(6, 4, 16)[lam]) for lam in NINE]
        print("RE-CERTIFYING session 27's nine under the corrected rule")
        print("(session 27 reported mult_det = mult_pad = a at all nine)")
    else:
        allc = cells62()
        todo_all = [c for c in allc if c[0] not in set(NINE)]
        sizes = {lam: len(monomials(4, len(lam), 6, lam)) for lam, _ in todo_all}
        todo = [c for c in order(todo_all, sizes) if sizes[c[0]] <= CAP]
        print("the 62: %d cells (of %d live at delta=6), %d within the cap %d"
              % (len(todo_all), len(allc), len(todo), CAP))
    print("lam                     ell  a   N_S   mult_det  mult_pad   D")
    hits, done = [], 0
    for lam, av in todo:
        r = len(lam)
        ns = len(monomials(4, r, 6, lam))
        if mode != "nine" and ns > CAP: continue
        t0 = time.time()
        md = measure(d4, N4, 4, r, 6, lam, a_expect=av)
        mp = measure(pd, Np, 4, r, 6, lam, seed=29, a_expect=av)
        # a rank BELOW a is re-run at 3x points before it is believed
        for nm, m, f, N in (("det", md, d4, N4), ("pad", mp, pd, Np)):
            if m['mult'] < av:
                m2 = measure(f, N, 4, r, 6, lam, npts=3 * av + 24, seed=907,
                             a_expect=av)
                assert m2['mult'] == m['mult'], ("short rank unstable", lam, nm, m, m2)
        D = mp['mult'] - md['mult']
        done += 1
        flag = ""
        if D > 0: hits.append((lam, av, md['mult'], mp['mult'])); flag = "  *** D>0 ***"
        line = ("| %s | %d | %d | %d | %d | %d | %+d |"
                % (str(lam), r, av, ns, md['mult'], mp['mult'], D))
        bank(line)
        print("%-24s %2d %3d %6d    %2d %-5s  %2d %-5s %+3d%s  [%.0fs]"
              % (str(lam), r, av, ns, md['mult'], "(=a)" if md['mult'] == av else "(<a)",
                 mp['mult'], "(=a)" if mp['mult'] == av else "(<a)", D, flag,
                 time.time() - t0))
        sys.stdout.flush()
        if hits:
            print("*** STOPPING: D > 0 ***"); break
    print()
    print("cells completed: %d ; D>0: %d ; mult<a on det: %d ; on pad: %d"
          % (done, len(hits), 0, 0))
