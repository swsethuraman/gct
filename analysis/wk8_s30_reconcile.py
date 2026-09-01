#!/usr/bin/env python3
"""
Release claims for cells that were taken but never banked.

A worker killed mid-cell leaves results/claims/<lam>.claim behind with no
matching row in results/sweep62_ledger.md.  Without this, a restarted worker
would skip that cell forever and the coverage fraction would silently
overstate what was actually measured.

PID-AWARE, and this is not optional.  The first version released every
unbanked claim, which freed the cell a still-running worker was in the middle
of computing -- two workers would then have raced on it.  Each claim file
records "<who> <pid>", so a claim is released only when its owning process is
gone.  A claim whose owner is alive is left alone and reported as held.
"""
import os, sys
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_report import read_ledger

CLAIMS = "/root/gct/results/claims"

def alive(pid):
    try:
        os.kill(pid, 0)
    except (ProcessLookupError, ValueError):
        return False
    except PermissionError:
        return True
    return True

def owner(path):
    try:
        parts = open(path).read().split()
        return parts[0], int(parts[1])
    except Exception:
        return ("prebanked", -1)          # no live owner

if __name__ == '__main__':
    banked = set(read_ledger())
    freed, held = [], []
    for fn in sorted(os.listdir(CLAIMS)):
        if not fn.endswith(".claim"): continue
        lam = tuple(int(x) for x in fn[:-6].split("_"))
        if lam in banked: continue
        who, pid = owner(os.path.join(CLAIMS, fn))
        if pid > 0 and alive(pid):
            held.append((lam, who, pid))
        else:
            os.remove(os.path.join(CLAIMS, fn)); freed.append(lam)
    print("released %d stale claim(s): %s" % (len(freed), freed if freed else "-"))
    print("left %d live claim(s) alone: %s" % (len(held), held if held else "-"))
    print("%d cells claimed and banked" % len(banked))
