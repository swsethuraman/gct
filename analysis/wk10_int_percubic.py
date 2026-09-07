import sys, random, itertools
sys.path.insert(0,'analysis')
from math import comb
from pad import pmul, padd, P, rank_mod

def cub_rank(r, seed):
    rnd=random.Random(seed)
    # monomials of degree 3 in r vars
    monos=[e for e in itertools.product(range(4),repeat=r) if sum(e)==3]
    idx={e:i for i,e in enumerate(monos)}
    # M[a][b] = sum_i c s_i  (random linear forms)
    def lin():
        d={}
        for i in range(r):
            e=tuple(1 if k==i else 0 for k in range(r)); d[e]=rnd.randrange(1,P)
        return d
    M=[[lin() for _ in range(3)] for _ in range(3)]
    rows=[]
    for a in range(3):
        for b in range(3):
            sub=[[M[p][q] for q in range(3) if q!=b] for p in range(3) if p!=a]
            pm=padd(pmul(sub[0][0],sub[1][1],r), pmul(sub[0][1],sub[1][0],r))  # 2x2 PERMANENT
            for i in range(r):
                e_i=tuple(1 if k==i else 0 for k in range(r))
                der=pmul({e_i:1}, pm, r)
                row=[0]*len(monos)
                for e,c in der.items(): row[idx[e]]=(row[idx[e]]+c)%P
                rows.append(row)
    return rank_mod(rows, len(monos)), len(monos), 9*r

print("Permanental cubics: is  M -> per_3(M)  dominant onto Sym^3 C^r ?")
print("%3s %10s %8s %8s   %s"%("r","params 9r","target","rank","reading"))
for r in (3,4,5,6,7):
    rk=None
    for s in (0,1,2):
        v,tgt,pp=cub_rank(r,s); rk=max(rk or 0, v)
    note = "DOMINANT  -> permanental cubics fill all cubics" if rk==tgt else "deficit %d  -> strictly smaller"%(tgt-rk)
    print("%3d %10d %8d %8d   %s"%(r,pp,tgt,rk,note))
