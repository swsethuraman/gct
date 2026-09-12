"""Recompute h_pad from scratch: my own horizontal-strip enumeration, house cubic
plethysm coefficients (Weyl alternation + CRT) -- a different lineage from B14-11's
power-sum / Murnaghan-Nakayama route.  Checks both directions."""
import os, pathlib
ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))
WORK = pathlib.Path(os.environ.get('GCT_WORK', ROOT / 'results' / 'integrate' / 'b14_11_replay'))
WORK.mkdir(parents=True, exist_ok=True)
import sys, json, time
sys.path.insert(0, str(ROOT / 'analysis'))
from wk9_s57_lib import a_weyl_mod
import subprocess

def hstrips_down(lam, d):
    lam = [x for x in lam if x]; L = len(lam); out = []
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

CACHE = {}
def hpad(lam, delta):
    tot = 0; chans = 0
    for nu in hstrips_down(lam, delta):
        if sum(nu) != 3*delta: continue
        chans += 1
        if nu in CACHE: c = CACHE[nu]
        else:
            c,_,_ = a_weyl_mod(nu, delta, n=3, cache=None)
            CACHE[nu] = c
        tot += c
    return tot, chans

def show(x): return '(' + ','.join(map(str,x)) + ')'

exc = json.loads(subprocess.run(['git','-C',str(ROOT),'show',
      'b14-11-astra:results/b14_11/exact_exclusions.json'],capture_output=True,text=True).stdout)
short = json.loads(subprocess.run(['git','-C',str(ROOT),'show',
      'b14-11-astra:results/b14_11/shortlist.json'],capture_output=True,text=True).stdout)

t=time.time(); bad=[]
print("=== the 153 claimed pullback-zero exclusions ===", flush=True)
for i,c in enumerate(exc['cells']):
    lam=tuple(c['lam']); d=c['delta']
    h,ch = hpad(lam,d)
    if h != 0: bad.append((d,lam,h))
    if i%25==0: print(f"  {i}/153 mine-nonzero={len(bad)} {time.time()-t:.1f}s", flush=True)
print(f"  153 checked; claimed h_pad=0 but I get nonzero: {len(bad)}")
for b in bad: print("   MISMATCH", b)

print("=== positive controls: the ten shortlist cells (h_pad must match exactly) ===", flush=True)
sl = short['candidates'] if isinstance(short,dict) and 'candidates' in short else short
if isinstance(sl, dict):
    sl = sl.get('shortlist', [])
mis=0
for c in sl:
    lam=tuple(c['lam']); d=c['delta']
    h,ch = hpad(lam,d)
    ok = (h == c['h_pad'])
    mis += (not ok)
    print(f"  {show(lam)}_{d}: mine={h} theirs={c['h_pad']} channels={ch} {'OK' if ok else 'MISMATCH'}")
print("shortlist h_pad mismatches:", mis)
json.dump({'exclusion_mismatches':bad,'shortlist_mismatches':mis}, open(str(WORK / 'hpad_check.json'),'w'))
print("elapsed %.1f"%(time.time()-t))
