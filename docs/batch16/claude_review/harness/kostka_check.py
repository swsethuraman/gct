"""Control: verify the closed form for K_{lambda,mu} with lambda=(L1,L2,2^{n-2}),
alphabet size n, against brute-force SSYT enumeration."""
import itertools
from functools import lru_cache

def brute_K(lam, mu, n):
    # enumerate SSYT of shape lam with entries in 1..n and content mu
    rows = len(lam); cnt = 0
    cells = [(i,j) for i in range(rows) for j in range(lam[i])]
    def rec(idx, T, content):
        nonlocal cnt
        if idx == len(cells):
            cnt += 1; return
        i,j = cells[idx]
        lo = 1
        if j>0: lo = max(lo, T[(i,j-1)])
        if i>0: lo = max(lo, T[(i-1,j)]+1)
        for v in range(lo, n+1):
            if content[v-1] == 0: continue
            content[v-1]-=1; T[(i,j)]=v
            rec(idx+1, T, content)
            content[v-1]+=1
        T.pop((i,j),None)
    rec(0, {}, list(mu))
    return cnt

def formula_K(lam, mu, n):
    """lam = (L1, L2, 2,...,2) with n rows.  Columns 1,2 forced = (1..n).
    row1 tail length L1-2, row2 tail length L2-2, ballot condition."""
    L1,L2 = lam[0], lam[1]
    assert all(x==2 for x in lam[2:]) and len(lam)==n
    nu = [mu[k]-2 for k in range(n)]
    if any(x<0 for x in nu): return 0
    t2 = L2-2
    if sum(nu) != (L1-2)+t2: return 0
    tot = 0
    # b_k = number of letter k in row-2 tail
    def rec(k, bcum, acum):
        nonlocal tot
        if k==n:
            if bcum==t2: tot+=1
            return
        for bk in range(0, min(nu[k], t2-bcum)+1):
            if bcum+bk > acum:   # ballot: b_{<=k} <= a_{<=k-1}
                break
            rec(k+1, bcum+bk, acum + (nu[k]-bk))
    rec(0,0,0)
    return tot

import random
random.seed(7)
bad=0; tested=0
for n in (3,4):
    for L1,L2 in ((6,4),(7,5),(8,4),(9,6)):
        lam = (L1,L2)+(2,)*(n-2)
        tot = sum(lam)
        # all contents mu with sum tot, each >=0, n parts
        for mu in itertools.product(range(tot+1), repeat=n):
            if sum(mu)!=tot: continue
            bk = brute_K(lam, mu, n); fk = formula_K(lam, mu, n); tested+=1
            if bk!=fk:
                bad+=1
                if bad<6: print('MISMATCH', lam, mu, bk, fk)
print('tested',tested,'mismatches',bad)
# symmetry control
for n in (4,):
    lam=(9,6,2,2); tot=sum(lam)
    for mu in itertools.product(range(tot+1),repeat=n):
        if sum(mu)!=tot: continue
        vals={formula_K(lam,tuple(s),n) for s in itertools.permutations(mu)}
        assert len(vals)==1, (mu,vals)
print('formula is symmetric in mu: OK')
