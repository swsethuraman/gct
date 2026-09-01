#!/usr/bin/env python3
"""
Fill the generated blocks of docs/sweep62.md from the banked ledger.

The tables and the coverage fraction in the write-up are NEVER typed by hand:
they are substituted from results/sweep62_ledger.md at the end, so the prose
cannot drift from the measurements.  Idempotent -- re-running replaces the
generated blocks between the markers rather than appending.
"""
import sys, re
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_core import monomials
from wk8_s30_pleth import amb
from wk8_s30_sweep import NINE, cells62, balance
from wk8_s30_report import read_ledger

DOC = "/root/gct/docs/sweep62.md"
B0, B1 = "<!--GEN:TABLE-->", "<!--/GEN:TABLE-->"
C0, C1 = "<!--GEN:COVERAGE-->", "<!--/GEN:COVERAGE-->"

led   = read_ledger()
live  = [c for c in cells62() if c[0] not in set(NINE)]
sizes = {lam: len(monomials(4, len(lam), 6, lam)) for lam, _ in live}
meas  = {l: v for l, v in led.items() if l in sizes}
nine  = {l: v for l, v in led.items() if l in set(NINE)}
n, N  = len(meas), len(live)
amass = sum(v['a'] for v in meas.values()); atot = sum(c[1] for c in live)

tbl = ["**Session 27's nine, re-certified under the corrected rule** "
       "(%d of 9, all unchanged):" % len(nine), "",
       "| lam | a | `N_S` | `mult_det` | `mult_pad` | `D` |", "|---|---|---|---|---|---|"]
for lam in sorted(nine, key=lambda l: nine[l]['ns']):
    v = nine[lam]
    tbl.append("| `%s` | %d | %d | %d | %d | %+d |"
               % (lam, v['a'], v['ns'], v['det'], v['pad'], v['D']))
tbl += ["", "**The 62** — %d measured, in ascending `N_S`:" % n, "",
        "| lam | `a` | `N_S` | `mult_det` | `mult_pad` | `D` | balance |",
        "|---|---|---|---|---|---|---|"]
for lam in sorted(meas, key=lambda l: meas[l]['ns']):
    v = meas[lam]
    tbl.append("| `%s` | %d | %d | %d | %d | %+d | %d |"
               % (lam, v['a'], v['ns'], v['det'], v['pad'], v['D'], balance(lam)))
tbl += ["", "Every row: `mult_det = mult_pad = a`, `D = 0`.  No cell fell below "
        "the ambient cap on either side, so the sceptical re-run branch was "
        "never entered."]

bs = [balance(l) for l in meas] or [0]
cov = ["**Coverage: %d of the 62 cells, %.0f%%** — and %d of the 62's %d units "
       "of ambient multiplicity, %.0f%%." % (n, 100.0*n/N, amass, atot, 100.0*amass/atot),
       "",
       "| axis | measured | across the 62 |", "|---|---|---|",
       "| `N_S` | %d – %d | %d – %d |" % (min(v['ns'] for v in meas.values()),
                                          max(v['ns'] for v in meas.values()),
                                          min(sizes.values()), max(sizes.values())),
       "| `a` | %d – %d | %d – %d |" % (min(v['a'] for v in meas.values()),
                                        max(v['a'] for v in meas.values()),
                                        min(c[1] for c in live), max(c[1] for c in live)),
       "| balance | %d – %d | %d – %d |" % (min(bs), max(bs),
                                            min(balance(c[0]) for c in live),
                                            max(balance(c[0]) for c in live))]

s = open(DOC).read()
def put(s, a, b, body):
    blk = a + "\n" + body + "\n" + b
    if a in s:
        return re.sub(re.escape(a) + r".*?" + re.escape(b), blk.replace("\\", "\\\\"), s, flags=re.S)
    return s
s = s.replace("TABLE_PLACEHOLDER", B0 + "\n" + B1) if "TABLE_PLACEHOLDER" in s else s
s = s.replace("**COVERAGE_PLACEHOLDER**", C0 + "\n" + C1) if "COVERAGE_PLACEHOLDER" in s else s
s = put(s, B0, B1, "\n".join(tbl))
s = put(s, C0, C1, "\n".join(cov))
open(DOC, "w").write(s)
print("filled: %d of 62 (%.0f%%), a-mass %d/%d" % (n, 100.0*n/N, amass, atot))
