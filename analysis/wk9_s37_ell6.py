#!/usr/bin/env python3
"""
Session 37, check 5 -- the length-6 cells at n = 4, delta = 6, 7: ambient
multiplicity a (plethysm route, analysis/wk8_s30_pleth.py) and weight-space
size N_S (analysis/wk8_s30_core.py::monomials), cheapest first.  Used only to
name concrete candidate cells in docs/dip_transfer.md section 5; no
multiplicities are measured here.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_pleth import amb
from wk8_s30_core import monomials

n = 4
for delta in (6, 7):
    A = amb(delta, n, 6)
    rows = []
    for lam, a in A.items():
        if len(lam) != 6: continue
        NS = len(monomials(n, 6, delta, lam))
        rows.append((NS, lam, a))
    rows.sort()
    print(f"delta = {delta}: {len(rows)} length-6 weights with a > 0; "
          f"sum a = {sum(r[2] for r in rows)}")
    for NS, lam, a in rows[:12]:
        print(f"   lam={lam}  a={a}  N_S={NS}")
