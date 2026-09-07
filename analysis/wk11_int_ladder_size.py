"""Integrator check for batch 11 §2.1 : N_S along the LMR ladder
lam_delta = (4*delta - 31, 17, 2^7) for delta = 12..24.

Unbounded-knapsack recursion over the 495 degree-4 exponent vectors on nine
variables: coefficient of x^lam z^delta in prod_alpha 1/(1 - z x^alpha).  The
state space is prod_i (lam_i + 1) times (delta + 1) and is independent of N_S,
so the count is exact and costs seconds per rung.  Self-check: delta = 24 must
reproduce the banked N_S = 156,438,903,314 and n_chi = 31,039,465 (s57)."""
import os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_core import exps
R=9; N=4
A=[tuple(a) for a in exps(N,R)]
print('L =', len(A), flush=True)
def NS(lam, delta):
    shape=tuple(x+1 for x in lam)
    dp=np.zeros(shape+(delta+1,), dtype=np.float64)
    dp[(0,)*R+(0,)]=1.0
    for a in A:
        if any(a[i]>lam[i] for i in range(R)): continue
        src=tuple(slice(0,lam[i]-a[i]+1) for i in range(R))
        dst=tuple(slice(a[i],lam[i]+1) for i in range(R))
        for d in range(delta):
            dp[dst+(d+1,)] += dp[src+(d,)]
    return dp[tuple(lam)+(delta,)]
rows=[]
for delta in range(12,25):
    lam=(4*delta-31,17,2,2,2,2,2,2,2)
    t=time.time(); v=NS(lam,delta); el=time.time()-t
    stab=5040*(2 if lam[0]==lam[1] else 1)
    rows.append((delta,lam[0],v,v/stab,el))
    print('delta=%2d lam1=%2d  N_S=%.6g   n_chi~=%.4g  (stab %d)  %.1fs'%(delta,lam[0],v,v/stab,stab,el), flush=True)
