#!/usr/bin/env python3
"""
Session 30 -- end-of-session verification.

Three checks, run after all measurement is finished, on the artefacts as they
will be delivered rather than on anything held in memory:

  1. The discriminating witness still passes.  If the corrected rule were not
     actually in force, nothing else in this session counts.
  2. Every `a` in the banked ledger is re-derived by the plethysm route,
     independently of the raising-operator kernel that produced the ledger.
  3. A random sample of banked cells is re-measured from scratch at a
     different seed and different evaluation-point count, and must reproduce.
"""
import sys, random
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_core import measure, det_form, per_padded, monomials
from wk8_s30_pleth import amb
from wk8_s30_report import read_ledger

fails = []

# --- 1. the witness --------------------------------------------------------
from wk8_s30_core import build_R, nullspace, P1
f1, N1 = per_padded(1, 4)                       # x_0^3 . x_1  =  l^3 m
w = measure(f1, N1, 4, 2, 2, (4, 4))['mult']
basis, R = build_R(4, 2, 2, (4, 4))
kb = [x % P1 for x in nullspace(R, len(basis), P1)[0]]
want = [12 % P1, (-3) % P1, 1]
ok1 = (w == 0) and (kb == want)
print("1. witness (l^3 m, lam=(4,4), delta=2) : mult = %d (want 0), "
      "kernel %s (want (12,-3,1))  %s"
      % (w, "matches" if kb == want else kb, "PASS" if ok1 else "FAIL"))
print("   (the WRONG rule gives mult = 1 and kernel (1,-4,3) -- this check "
      "discriminates)")
if not ok1: fails.append("witness")

# --- 2. every a re-derived by plethysm ------------------------------------
led = read_ledger()
A = amb(6, 4, 16)
bad = [(l, v['a'], A.get(l)) for l, v in led.items() if A.get(l) != v['a']]
print("2. a re-derived by plethysm for all %d banked cells : %s"
      % (len(led), "PASS" if not bad else "FAIL %s" % bad[:3]))
if bad: fails.append("a-mismatch")

# --- 3. resample -----------------------------------------------------------
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 3
rnd = random.Random(20260901)
pool = sorted(led, key=lambda l: led[l]['ns'])[:14]      # cheap ones only
pick = rnd.sample(pool, min(NS, len(pool)))
d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
print("3. re-measuring %d banked cells from scratch, new seeds and point counts:"
      % len(pick))
for lam in pick:
    v = led[lam]; r = len(lam)
    md = measure(d4, N4, 4, r, 6, lam, npts=3 * v['a'] + 31, seed=5551, a_expect=v['a'])
    mp = measure(pd, Np, 4, r, 6, lam, npts=3 * v['a'] + 31, seed=7717, a_expect=v['a'])
    ok = (md['mult'] == v['det'] and mp['mult'] == v['pad'])
    print("   %-24s ledger (%d,%d)  rerun (%d,%d)  %s"
          % (str(lam), v['det'], v['pad'], md['mult'], mp['mult'],
             "PASS" if ok else "FAIL"))
    if not ok: fails.append(("resample", lam))

print()
print("VERIFICATION: %s" % ("ALL PASS" if not fails else "FAILURES %s" % fails))
sys.exit(1 if fails else 0)
