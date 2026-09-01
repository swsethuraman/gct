#!/usr/bin/env python3
"""
Session 30 -- turn results/sweep62_ledger.md into the numbers docs/sweep62.md
quotes.  Kept separate from the sweep so the sweep is never edited while it
runs, and so the reported fractions are derived from the banked ledger rather
than from anything held in a process's memory.
"""
import re, sys
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_core import monomials
from wk8_s30_pleth import amb
from wk8_s30_sweep import NINE, cells62, balance

ROW = re.compile(r'^\| (\([\d, ]+\)) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| ([+-]\d+) \|')

def read_ledger(path="/root/gct/results/sweep62_ledger.md"):
    out = {}
    for ln in open(path):
        m = ROW.match(ln)
        if not m: continue
        lam = tuple(int(x) for x in m.group(1).strip("()").split(","))
        out[lam] = dict(ell=int(m.group(2)), a=int(m.group(3)), ns=int(m.group(4)),
                        det=int(m.group(5)), pad=int(m.group(6)), D=int(m.group(7)))
    return out

if __name__ == '__main__':
    led   = read_ledger()
    live  = [c for c in cells62() if c[0] not in set(NINE)]
    sizes = {lam: len(monomials(4, len(lam), 6, lam)) for lam, _ in live}
    meas  = {lam: v for lam, v in led.items() if lam in sizes}
    nine  = {lam: v for lam, v in led.items() if lam in set(NINE)}

    print("session 27's nine re-certified : %d of 9" % len(nine))
    print("  all mult_det = mult_pad = a  : %s"
          % all(v['det'] == v['a'] and v['pad'] == v['a'] for v in nine.values()))
    print()
    print("the 62 : %d measured of %d  (%.0f%%)"
          % (len(meas), len(live), 100.0 * len(meas) / len(live)))
    print("  D = 0 on every measured cell : %s" % all(v['D'] == 0 for v in meas.values()))
    print("  mult_det = a everywhere      : %s" % all(v['det'] == v['a'] for v in meas.values()))
    print("  mult_pad = a everywhere      : %s" % all(v['pad'] == v['a'] for v in meas.values()))
    if meas:
        print("  a  range measured : %d .. %d   (over the 62: %d .. %d)"
              % (min(v['a'] for v in meas.values()), max(v['a'] for v in meas.values()),
                 min(c[1] for c in live), max(c[1] for c in live)))
        print("  N_S range measured : %d .. %d  (over the 62: %d .. %d)"
              % (min(v['ns'] for v in meas.values()), max(v['ns'] for v in meas.values()),
                 min(sizes.values()), max(sizes.values())))
        bs = [balance(l) for l in meas]
        print("  balance measured   : %d .. %d  (over the 62: %d .. %d)"
              % (min(bs), max(bs),
                 min(balance(c[0]) for c in live), max(balance(c[0]) for c in live)))
        # how much of the 62's total a-mass is covered
        tot = sum(c[1] for c in live); got = sum(v['a'] for v in meas.values())
        print("  ambient multiplicity covered : %d of %d  (%.0f%%)"
              % (got, tot, 100.0 * got / tot))
    print()
    print("| lam | ell | a | N_S | mult_det | mult_pad | D |")
    print("|---|---|---|---|---|---|---|")
    for lam in sorted(meas, key=lambda l: meas[l]['ns']):
        v = meas[lam]
        print("| %s | %d | %d | %d | %d | %d | %+d |"
              % (str(lam), v['ell'], v['a'], v['ns'], v['det'], v['pad'], v['D']))
    print()
    print("UNMEASURED (%d):" % (len(live) - len(meas)))
    for lam, av in sorted(live, key=lambda c: sizes[c[0]]):
        if lam not in meas:
            print("  %-24s a=%-3d N_S=%d" % (str(lam), av, sizes[lam]))
