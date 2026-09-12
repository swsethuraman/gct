"""My own checks of B14-11's corrected support lemma and the two eligibility bounds."""
import os, pathlib
ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))
WORK = pathlib.Path(os.environ.get('GCT_WORK', ROOT / 'results' / 'integrate' / 'b14_11_replay'))
WORK.mkdir(parents=True, exist_ok=True)
import sys, itertools, json
from fractions import Fraction
sys.path.insert(0, str(ROOT / 'analysis'))
from wk9_s57_lib import a_weyl_mod

print("=== 1. the old arbitrary-weight lemma is FALSE ===")
# point p = (x+y)^4 in Sym^4 C^r: essential span 1.  Coordinate functional
# c_(3,1) on Sym^4 is a torus weight vector of weight (3,1), length 2 > 1.
from math import comb
c31 = comb(4,1)            # coefficient of x^3 y in (x+y)^4
print("  c_(3,1)((x+y)^4) =", c31, "-> nonzero at a span-1 point, weight length 2")
assert c31 != 0
# a second, independent witness: c_(2,1,1) on (x+y+z)^4
from itertools import permutations
c211 = 4*3*2//(2*1*1)     # multinomial 4!/(2!1!1!)
print("  c_(2,1,1)((x+y+z)^4) =", c211, "-> nonzero at a span-1 point, weight length 3")
assert c211 != 0

print("=== 2. the corrected statement: every weight of S_lam has >= ell(lam) nonzero parts ===")
def kostka(lam, mu):
    """SSYT of shape lam and content mu, counted directly."""
    lam = [x for x in lam if x]; mu = [x for x in mu if x]
    rows = len(lam); res = 0
    def rec(i, filled, remaining):
        nonlocal res
        if i == rows:
            res += 1; return
        # fill row i weakly increasing, strictly greater than row above per column
        above = filled[i-1] if i else None
        def place(j, cells, rem, lo):
            if j == lam[i]:
                rec(i+1, filled+[cells], rem); return
            for v in range(lo, len(mu)+1):
                if rem[v-1] == 0: continue
                if above is not None and j < len(above) and above[j] >= v: continue
                rem2 = list(rem); rem2[v-1] -= 1
                place(j+1, cells+[v], rem2, v)
        place(0, [], remaining, 1)
    rec(0, [], list(mu))
    return res
def parts(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for k in range(min(n,maxp),0,-1):
        for r in parts(n-k,k): yield (k,)+r
bad = 0; checked = 0
for N in range(1, 10):
    for lam in parts(N):
        for mu in parts(N):
            k = kostka(lam, mu)
            checked += 1
            if k > 0 and len(mu) < len(lam):
                bad += 1; print("   COUNTEREXAMPLE", lam, mu, k)
print(f"  checked {checked} (lam,mu) pairs up to |lam|=9; violations: {bad}")
assert bad == 0

print("=== 3. quartic length bound: a_lam(delta) = 0 whenever ell(lam) > delta ===")
cache = {}; n_over = 0
for delta in range(1, 8):
    for lam in parts(4*delta):
        if len(lam) > delta and len(lam) <= 9 and lam[0] >= 1:
            a,_,_ = a_weyl_mod(lam, delta, n=4, cache=cache)
            n_over += 1
            if a != 0:
                print("   VIOLATION", lam, delta, a); raise SystemExit(1)
    print(f"  delta={delta}: all length>{delta} labels (len<=9) give a=0")
print(f"  {n_over} over-length labels checked, all zero")

print("=== 4. first-row bound: constituents of Sym^d V tensor Sym^d(Sym^3 V) have lam_1 >= d ===")
def hstrips_down(lam, d):
    """partitions nu with lam/nu a horizontal d-strip (interlacing)."""
    lam = [x for x in lam if x]; L = len(lam)
    out = []
    def rec(i, cur, left):
        if i == L:
            if left == 0: out.append(tuple(x for x in cur if x))
            return
        hi = lam[i]; lo = lam[i+1] if i+1 < L else 0
        for v in range(lo, hi+1):
            t = hi - v
            if 0 <= t <= left: rec(i+1, cur+[v], left-t)
    rec(0, [], d)
    return out
viol = 0; tot = 0
for delta in range(1, 6):
    for lam in parts(4*delta):
        if len(lam) > 9: continue
        h = 0
        for nu in hstrips_down(lam, delta):
            if sum(nu) != 3*delta: continue
            c,_,_ = a_weyl_mod(nu, delta, n=3, cache=cache) if nu else (1,0,0)
            h += c
        tot += 1
        if h > 0 and lam[0] < delta:
            viol += 1; print("   VIOLATION", lam, delta, h)
print(f"  {tot} labels scanned for delta<=5; first-row violations: {viol}")
assert viol == 0
print("ALL CHECKS PASS")
