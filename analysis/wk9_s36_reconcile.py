#!/usr/bin/env python3
"""Release s36 claims whose owner PID is dead and whose cell is not banked
(PID-aware, as wk8_s30_reconcile.py; live owners are left alone)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s36_sweep import CLAIMS, banked
def alive(pid):
    try: os.kill(pid, 0)
    except ProcessLookupError: return False
    except PermissionError: return True
    return True
if __name__ == '__main__':
    done = banked(); freed, held = [], []
    for fn in sorted(os.listdir(CLAIMS)):
        lam = tuple(int(x) for x in fn[:-6].split('_'))
        if lam in done: continue
        who, pid = open(os.path.join(CLAIMS, fn)).read().split()
        if alive(int(pid)): held.append((lam, who, pid))
        else: os.remove(os.path.join(CLAIMS, fn)); freed.append(lam)
    print("released:", freed or '-'); print("held by live workers:", held or '-')
