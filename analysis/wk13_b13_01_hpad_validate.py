#!/usr/bin/env python3
"""B13-01 validation: the Weyl-alternation h_pad (wk13_b13_01_hpad, used at rung 13
where the house amb plethysm OOMs) agrees with the house amb-based h_pad
(wk9_s42_hpad.h_pad) on small cells, including s42 banked cells."""
import sys, itertools
sys.path.insert(0,'analysis'); sys.path.insert(0,'.')
from wk9_s42_hpad import h_pad as house_hpad, pieri_strips
def cubics(r):
    out=[]
    def rec(k,left,cur):
        if k==r-1: out.append(tuple(cur+[left])); return
        for v in range(left+1): rec(k+1,left-v,cur+[v])
    rec(0,3,[]); return sorted(out)
def mcount(target,delta,CUB):
    r=len(target)
    if any(x<0 for x in target) or sum(target)!=3*delta: return 0
    n=len(CUB); memo={}; sys.setrecursionlimit(100000)
    def rec(i,k,rem):
        if k==0: return 1 if all(x==0 for x in rem) else 0
        if i==n or sum(rem)!=3*k: return 0
        key=(i,k,rem); v=memo.get(key)
        if v is not None: return v
        a=CUB[i]; mm=k
        for c in range(r):
            if a[c]: mm=min(mm,rem[c]//a[c])
        t=sum(rec(i+1,k-m,tuple(rem[c]-m*a[c] for c in range(r))) for m in range(mm+1))
        memo[key]=t; return t
    return rec(0,delta,tuple(target))
def my_hpad(lam,delta):
    lam=tuple(x for x in lam if x); r=len(lam); CUB=cubics(r); rho=tuple(range(r-1,-1,-1))
    tot=0
    for mu in [tuple(x for x in m if x) for m in pieri_strips(lam,delta)]:
        mm=tuple(mu)+(0,)*(r-len(mu)); L=[mm[i]+rho[i] for i in range(r)]
        for perm in itertools.permutations(range(r)):
            nu=tuple(L[perm[i]]-rho[i] for i in range(r))
            if any(x<0 for x in nu): continue
            s=1; p=list(perm)
            for i in range(r):
                for j in range(i+1,r):
                    if p[i]>p[j]: s=-s
            tot+=s*mcount(nu,delta,CUB)
    return tot
if __name__=='__main__':
    for lam,d in [((8,4,4,4,4),6),((12,9,9,1,1),8),((10,6,4,2,2),6),((8,8,8),6),((9,9,8,1,1),7),((12,8,8),7)]:
        assert house_hpad(lam,d)==my_hpad(lam,d), (lam,d)
        print("OK",lam,d,house_hpad(lam,d))
    print("all h_pad methods agree on small cells")
