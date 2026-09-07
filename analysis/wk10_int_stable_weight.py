import itertools, time
def W(nv, rho, degs):
    caps=tuple(x+1 for x in rho)
    gens=[m for d in degs for m in itertools.product(*[range(min(d,rho[i])+1) for i in range(nv)]) if sum(m)==d]
    states=1
    for c in caps: states*=c
    strides=[1]*nv
    for i in range(nv-2,-1,-1): strides[i]=strides[i+1]*caps[i+1]
    def idx(s):
        t=0
        for i in range(nv): t+=s[i]*strides[i]
        return t
    A=[0]*states; A[0]=1
    allst=list(itertools.product(*[range(c) for c in caps]))
    for g in gens:
        for s in allst:
            u=tuple(s[i]-g[i] for i in range(nv))
            if min(u)>=0: A[idx(s)]+=A[idx(u)]
    return A[idx(rho)], len(gens), states

print("=== n=3 LMR cell, the one with a measured answer ===")
print("  delta=24 picture : lam=(19,7,2^5), N_S = 1,155,302   (computed earlier)")
w,g,s = W(6,(7,2,2,2,2,2),(2,3))
print("  stable picture   : rho=(7,2^5) in Sym(Sym^2+Sym^3)(C^6),  W = %d   [%d gens, %d states]"%(w,g,s))
print("  reduction factor : %.1fx"%(1155302/w))
print()
print("=== n=4 LMR cell ===")
NS24=156438903314; Wst=7212907703
print("  delta=24 picture : N_S = %d ,  n_chi = N_S/5040 = %.3e"%(NS24, NS24/5040))
print("  stable picture   : W   = %d ,  est n_chi = W/5040 = %.3e"%(Wst, Wst/5040))
print("  reduction factor : %.1fx  (same stabiliser S_7 on both sides, so it carries to n_chi)"%(NS24/Wst))
