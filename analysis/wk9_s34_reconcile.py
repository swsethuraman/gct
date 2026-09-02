#!/usr/bin/env python3
"""
Session 34 -- release claims for delta=7 cells taken but never banked.
PID-aware, exactly wk8_s30_reconcile.py's rule: a claim is released only when
its owning process is dead; a live owner's claim is left alone and reported.
Run BEFORE any worker restart.
"""
import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAIMS = os.path.join(ROOT, "results", "claims_d7")
LEDGER = os.path.join(ROOT, "results", "d7_ledger.md")

def alive(pid):
    try: os.kill(pid, 0)
    except (ProcessLookupError, ValueError): return False
    except PermissionError: return True
    return True

def banked_lams():
    out = set()
    if not os.path.exists(LEDGER): return out
    for ln in open(LEDGER):
        m = re.match(r'\| \((\d+(?:, \d+)*)\) \| \d+ \| \d+ \| \d+ \| (\d+|—) \|', ln)
        if m and m.group(2) != "—":       # DEFER rows are not banked measurements
            out.add(tuple(int(x) for x in m.group(1).split(', ')))
    return out

if __name__ == '__main__':
    banked = banked_lams()
    freed, held = [], []
    if not os.path.isdir(CLAIMS):
        print("no claims dir"); sys.exit(0)
    for fn in sorted(os.listdir(CLAIMS)):
        if not fn.endswith(".claim"): continue
        lam = tuple(int(x) for x in fn[:-6].split("_"))
        if lam in banked: continue
        try:
            parts = open(os.path.join(CLAIMS, fn)).read().split()
            who, pid = parts[0], int(parts[1])
        except Exception:
            who, pid = "prebanked", -1
        if pid > 0 and alive(pid):
            held.append((lam, who, pid))
        else:
            os.remove(os.path.join(CLAIMS, fn)); freed.append(lam)
    print("released %d stale claim(s): %s" % (len(freed), freed if freed else "-"))
    print("left %d live claim(s) alone: %s" % (len(held), held if held else "-"))
    print("%d cells claimed and banked" % len(banked))
