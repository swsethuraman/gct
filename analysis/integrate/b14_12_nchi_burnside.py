"""n_chi by my own Burnside orbit count -- a different lineage from the builder's
_canon_acc orbit enumeration.  Fix(g) is a generating-function coefficient over the
g-orbits of the quartic letters; Fix(identity) is N_S, so the same code also
reproduces N_S.  For both cells the character is trivial (every repeated part is
even), so n_chi is exactly the orbit count."""
import sys, itertools, time
from collections import defaultdict
import pathlib as _p
ROOT=_p.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'analysis'))

def letters(r, deg):
    out=[]
    def rec(i, cur, left):
        if i==r-1: out.append(tuple(cur+[left])); return
        for v in range(left+1): rec(i+1, cur+[v], left-v)
    rec(0,[],deg)
    return out

def fixcount(superletters, delta, tail):
    """[t^delta x^tail] prod (1 - t^{w} x^{v})^{-1} over (w, v) in superletters."""
    dims=[t+1 for t in tail]
    # state: dict keyed by (count, tail tuple) -> int ; use nested dict for speed
    cur={(0,)+tuple([0]*len(tail)):1}
    for w,v in superletters:
        if any(v[i]>tail[i] for i in range(len(tail))): continue
        if w>delta: continue
        nxt=dict(cur)
        # unbounded: repeatedly add one more copy
        frontier=cur
        m=1
        while True:
            newf={}
            for st,c in frontier.items():
                k=st[0]+w
                if k>delta: continue
                t2=tuple(st[1+i]+v[i] for i in range(len(tail)))
                if any(t2[i]>tail[i] for i in range(len(tail))): continue
                key=(k,)+t2
                newf[key]=newf.get(key,0)+c
            if not newf: break
            for key,c in newf.items(): nxt[key]=nxt.get(key,0)+c
            frontier=newf; m+=1
        cur=nxt
    return cur.get((delta,)+tuple(tail),0)

def group_elements(lam):
    r=len(lam); blocks=defaultdict(list)
    for i,p in enumerate(lam): blocks[p].append(i)
    gens=[]
    for b,pos in sorted(blocks.items()):
        gens.append([(b,pos,pi) for pi in itertools.permutations(range(len(pos)))])
    out=[]
    for combo in itertools.product(*gens):
        perm=list(range(r)); eps=1
        for b,pos,pi in combo:
            for a,t in enumerate(pi): perm[pos[a]]=pos[t]
            s=1
            for a in range(len(pi)):
                for c in range(a+1,len(pi)):
                    if pi[a]>pi[c]: s=-s
            if b%2==1: eps*=s
        out.append((tuple(perm),eps))
    return out

def n_chi(lam, delta, deg=4):
    r=len(lam); L=letters(r,deg); tail=list(lam[1:])
    G=group_elements(lam)
    total=0; NS=None; fixes={}
    for perm,eps in G:
        inv=[0]*r
        for i,p in enumerate(perm): inv[p]=i
        img={a: tuple(a[inv[k]] for k in range(r)) for a in L}
        seen=set(); sup=[]
        for a in L:
            if a in seen: continue
            orb=[]; x=a
            while x not in seen:
                seen.add(x); orb.append(x); x=img[x]
            v=tuple(sum(o[k] for o in orb) for k in range(r))
            sup.append((len(orb), v[1:]))
        f=fixcount(sup, delta, tail)
        fixes[perm]=(f,eps)
        if perm==tuple(range(r)): NS=f
        total+=eps*f
    assert total % len(G)==0, (lam,total,len(G))
    return NS, len(G), total, total//len(G), fixes

for lam, delta, claim_NS, claim_nchi, label in [
      ((10,6,6,6,2,2), 8, None, 1606104, "B13-10 pilot control"),
      ((12,4,4,4,4,4), 8, 27009659, 244454, "B14-12 target")]:
    t=time.time()
    NS,G,tot,nc,fixes = n_chi(lam, delta)
    q = -(-NS // G)
    print(f"{label}  lam={lam} delta={delta}")
    print(f"   N_S      = {NS:,}" + (f"   (claim {claim_NS:,}) {'OK' if NS==claim_NS else 'MISMATCH'}" if claim_NS else ""))
    print(f"   |Stab|   = {G}")
    print(f"   signed sum = {tot:,}")
    print(f"   n_chi    = {nc:,}   (claim {claim_nchi:,}) {'OK' if nc==claim_nchi else 'MISMATCH'}")
    print(f"   ceil(N_S/|Stab|) = {q:,}   quotient is {100*(claim_nchi-q)/claim_nchi:.1f}% below the measured n_chi")
    print(f"   N_S/n_chi = {NS/nc:.1f}  (|Stab| = {G})")
    print(f"   all characters trivial: {all(e==1 for _,e in fixes.values())}   {time.time()-t:.1f}s")
