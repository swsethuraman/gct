#!/usr/bin/env python3
"""
Release claims for cells that were taken but never banked.

A worker killed mid-cell leaves results/claims/<lam>.claim behind with no
matching row in results/sweep62_ledger.md.  Without this, a restarted worker
would skip that cell forever and the coverage fraction would silently
overstate what was actually measured.  Run before every relaunch.
"""
import os, sys, re
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_report import read_ledger

CLAIMS = "/root/gct/results/claims"
banked = set(read_ledger())
freed = []
for fn in sorted(os.listdir(CLAIMS)):
    if not fn.endswith(".claim"): continue
    lam = tuple(int(x) for x in fn[:-6].split("_"))
    if lam not in banked:
        os.remove(os.path.join(CLAIMS, fn)); freed.append(lam)
print("released %d stale claim(s): %s" % (len(freed), freed if freed else "-"))
print("%d cells claimed and banked" % len(banked))
