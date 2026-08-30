"""Generate br.c spec files: a 9-regular bracket structure on NB brackets with
3*NB letters, in a DP order chosen to keep the partial-bracket front small."""
import itertools, sys, math
from collections import defaultdict
from functools import lru_cache

BY=defaultdict(int)
for bits in range(512):
    rc=[0,0,0]; cc=[0,0,0]; n=0
    for k in range(9):
        if bits>>k & 1: rc[k//3]+=1; cc[k%3]+=1; n+=1
    BY[(n,tuple(rc),tuple(cc))]+=1
KEYS=defaultdict(list)
for (n,rc,cc),v in BY.items(): KEYS[n].append((rc,cc,v))

@lru_cache(maxsize=None)
def statecount(dvec, L):
    cur={((0,0,0),(0,0,0)):1}
    for d in dvec:
        nxt=defaultdict(int)
        for (rs,cs),c in cur.items():
            for rc,cc,v in KEYS[d]:
                nr=tuple(rs[i]+rc[i] for i in range(3))
                if max(nr)>L: continue
                nc=tuple(cs[i]+cc[i] for i in range(3))
                if max(nc)>L: continue
                nxt[(nr,nc)]+=c*v
        cur=nxt
    return cur.get(((L,L,L),(L,L,L)),0)

def peak_and_front(S, order, NB):
    d=[0]*NB; best=0; front=0
    for i,idx in enumerate(order):
        for v in S[idx]: d[v]+=1
        best=max(best, statecount(tuple(sorted(d)), i+1))
        front=max(front, sum(1 for x in d if 0<x<9))
    return best, front

def greedy(S, NB):
    n=len(S); used=[False]*n; d=[0]*NB; order=[]
    for _ in range(n):
        bi=None;bc=None
        for i in range(n):
            if used[i]: continue
            dd=d[:]
            for v in S[i]: dd[v]+=1
            c=statecount(tuple(sorted(dd)), len(order)+1)
            f=sum(1 for x in dd if 0<x<9)
            key=(f>7, c)
            if bc is None or key<bc: bc=key; bi=i
        used[bi]=True
        for v in S[bi]: d[v]+=1
        order.append(bi)
    return order

def write_spec(path, S, order, u):
    NB=max(max(t) for t in S)+1
    with open(path,'w') as f:
        f.write(f"{NB} {len(S)}\n")
        for i in order:
            f.write("%d %d %d\n"%S[i])
        f.write(" ".join(str(x) for x in u)+"\n")

SGN=[1,-1,-1,1,1,-1]   # itertools.permutations((0,1,2)) order
