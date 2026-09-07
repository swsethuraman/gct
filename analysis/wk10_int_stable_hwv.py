import itertools, time, sys
from flint import nmod_mat
P=2147483647; NV=5
def monos(d): return [a for a in itertools.product(range(d+1),repeat=NV) if sum(a)==d]
GENS=[(d,a) for d in (2,3,4) for a in monos(d)]
GIDX={g:i for i,g in enumerate(GENS)}
def wm(w):
    out=[]; n=len(GENS)
    def rec(start, rem, cur):
        if all(x==0 for x in rem): out.append(tuple(cur)); return
        if sum(rem)<2: return
        for gi in range(start,n):
            d,a=GENS[gi]
            if d>sum(rem): continue
            if all(a[k]<=rem[k] for k in range(NV)):
                rec(gi, tuple(rem[k]-a[k] for k in range(NV)), cur+[gi])
    rec(0,tuple(w),[]); return out
def hwv(w, verbose=True):
    src=wm(tuple(w)); nc=len(src)
    if verbose: print("  raw weight space :", nc, flush=True)
    blocks=[]; nr=0
    for i in range(NV-1):
        tw=list(w); tw[i]+=1; tw[i+1]-=1
        if tw[i+1]<0: continue
        tgt=wm(tuple(tw)); tix={m:k for k,m in enumerate(tgt)}
        ent={}
        for ci,m in enumerate(src):
            for pos in range(len(m)):
                d,a=GENS[m[pos]]
                if a[i+1]==0: continue
                na=list(a); na[i]+=1; na[i+1]-=1
                nm=tuple(sorted(m[:pos]+m[pos+1:]+(GIDX[(d,tuple(na))],)))
                k=(nr+tix[nm],ci); ent[k]=(ent.get(k,0)+a[i]+1)%P
        if verbose: print("    E_%d%d target %6d  nnz %8d"%(i+1,i+2,len(tgt),len(ent)), flush=True)
        blocks.append(ent); nr+=len(tgt)
    A=nmod_mat(nr,nc,P)
    for ent in blocks:
        for (r,c),v in ent.items(): A[r,c]=v
    del blocks
    Nsp,nul=A.nullspace()
    return src,Nsp,nul
w=tuple(int(x) for x in sys.argv[1:])
print("rho =",w, flush=True)
t=time.time(); src,Nsp,nul=hwv(w)
print("  a_inf = dim ker = %d    (%.1fs)"%(nul,time.time()-t), flush=True)
if nul==1:
    v=[int(Nsp[i,0])%P for i in range(len(src))]
    nz=[i for i,x in enumerate(v) if x]
    print("  HWV support: %d of %d monomials"%(len(nz),len(src)), flush=True)
    import pickle
    pickle.dump({'w':w,'src':src,'vec':v,'P':P}, open('/tmp/hwvA_%s.pkl'%('_'.join(map(str,w))),'wb'))
    print("  saved.", flush=True)
