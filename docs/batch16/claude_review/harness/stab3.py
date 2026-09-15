from math import comb
from functools import lru_cache
from collections import Counter
def N2(r,c):   # #{(e,f,g)>=0 : e+f+g=r, e<=c0,f<=c1,g<=c2}
    t=0
    for m in range(8):
        S=[i for i in range(3) if m>>i&1]
        n=r-sum(c[i]+1 for i in S)
        if n>=0: t+=(-1)**len(S)*comb(n+2,2)
    return t
@lru_cache(maxsize=None)
def T(r,c):
    if sum(r)!=sum(c): return 0
    tot=0
    for a in range(min(r[0],c[0])+1):
        for b in range(min(r[0]-a,c[1])+1):
            d=r[0]-a-b
            if d>c[2]: continue
            tot+=N2(r[1],(c[0]-a,c[1]-b,c[2]-d))
    return tot
comps=[(i,j,17-i-j) for i in range(18) for j in range(18-i)]
cls=Counter(tuple(sorted(x)) for x in comps)
B=0
for P,mp in cls.items():
    for Q,mq in cls.items():
        B+=mp*mq*T(P,Q)*T(tuple(29-x for x in P),tuple(29-x for x in Q))
print('dim (S_lambda C^10)^{T_H} =',B)
print('/72 (best case for the order-72 finite part) =',round(B/72))
print('ambient a_lambda =',429,' -> stabilizer bound is vacuous by a factor', round(B/72/429))
