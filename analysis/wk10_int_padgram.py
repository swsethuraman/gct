from itertools import permutations, combinations
from functools import lru_cache

def comps(M, d):
    """connected components of bipartite multigraph with multiplicity matrix M (d x d)"""
    par=list(range(2*d))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    def u(a,b):
        a,b=f(a),f(b)
        if a!=b: par[a]=b
    for i in range(d):
        for j in range(d):
            if M[i][j]>0: u(i, d+j)
    return len({f(v) for v in range(2*d)})

def perfect_matchings(M, d):
    """yield (weight, M-minus-matching) for each permutation with positive product"""
    for s in permutations(range(d)):
        w=1
        for i in range(d):
            w*=M[i][s[i]]
            if w==0: break
        if w:
            N=[row[:] for row in M]
            for i in range(d): N[i][s[i]]-=1
            yield w, N

def E3(H, d):
    """number of proper labeled 3-edge-colourings of a cubic bipartite multigraph"""
    tot=0
    for w,R in perfect_matchings(H,d):
        tot += w * (2**comps(R,d))
    return tot

def Kpad(G, d):
    tot=0
    for w,R in perfect_matchings(G,d):
        tot += w * E3(R,d)**2
    return tot

# ---- delta = 2 : the three orbital types ----
print("delta = 2 orbital types (2x2 intersection matrices, row/col sums 4):")
seen={}
for a in range(5):
    M=[[a,4-a],[4-a,a]]
    key=tuple(sorted([a,4-a]))
    v=Kpad(M,2)
    seen.setdefault(key,[]).append((a,v))
for key,vs in sorted(seen.items(), key=lambda z:-z[1][0][1]):
    print("   overlap type %-8s  K_pad = %d      (a = %s)" % (str(key), vs[0][1], [x[0] for x in vs]))
print()
print("Sol reports: 20736, 2592, 1152")

# ---- build the 35 x 35 Gram on H_{4,2} and take its rank ----
labels=list(range(8))
parts=[]
for c in combinations(labels[1:],3):
    B1=(0,)+c; B2=tuple(x for x in labels if x not in B1)
    parts.append((B1,B2))
print("\n|H_{4,2}| =", len(parts))
G=[[0]*len(parts) for _ in parts]
for i,P in enumerate(parts):
    for j,Q in enumerate(parts):
        M=[[len(set(P[a])&set(Q[b])) for b in range(2)] for a in range(2)]
        G[i][j]=Kpad(M,2)

from fractions import Fraction
def rank_Q(A):
    A=[[Fraction(x) for x in r] for r in A]; n=len(A); m=len(A[0]); r=0
    for c in range(m):
        p=next((i for i in range(r,n) if A[i][c]!=0), None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]
        for i in range(n):
            if i!=r and A[i][c]!=0:
                f=A[i][c]/pv
                for k in range(c,m): A[i][k]-=f*A[r][k]
        r+=1
    return r
print("exact rational rank of the 35 x 35 padded Gram :", rank_Q(G))
print("distinct entries:", sorted({v for row in G for v in row}, reverse=True))
