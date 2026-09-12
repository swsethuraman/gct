"""My own signed-Burnside check.  Fix(g) by DIRECT enumeration of the weight-lam
monomial basis and elementwise comparison -- no generating function, no orbit DP.
Sums over EVERY group element, so class sizes are verified too."""
import os, pathlib
ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))
WORK = pathlib.Path(os.environ.get('GCT_WORK', ROOT / 'results' / 'integrate' / 'b14_11_replay'))
WORK.mkdir(parents=True, exist_ok=True)
import sys, json, time, itertools, subprocess
import numpy as np

def letters(r, deg, cap):
    """exponent vectors of total degree deg in r variables, componentwise <= cap"""
    out=[]
    def rec(i, cur, left):
        if i==r-1:
            if left<=cap[i]: out.append(tuple(cur+[left]))
            return
        for v in range(0, min(left,cap[i])+1): rec(i+1, cur+[v], left-v)
    rec(0,[],deg)
    return out

def monomials(lam, delta, deg=4):
    """sorted tuples of letter ids: multisets of delta letters summing to lam"""
    r=len(lam)
    L=letters(r,deg,lam)
    L.sort()
    idx={a:i for i,a in enumerate(L)}
    res=[]
    n=len(L)
    lam=list(lam)
    def rec(i, chosen, rem, cnt):
        if cnt==0:
            if all(x==0 for x in rem): res.append(tuple(chosen))
            return
        if i==n: return
        # prune: remaining degree must match
        if sum(rem) != deg*cnt: return
        a=L[i]
        # multiplicity of letter i
        mx=cnt
        for k in range(r):
            if a[k]>0: mx=min(mx, rem[k]//a[k])
        for m in range(mx, -1, -1):
            rec(i+1, chosen+[i]*m, [rem[k]-m*a[k] for k in range(r)], cnt-m)
    rec(0,[],lam,delta)
    return L, idx, res

def group(lam):
    """(perm on positions, epsilon) for every element of prod_b S_{m_b}"""
    r=len(lam)
    blocks={}
    for i,p in enumerate(lam): blocks.setdefault(p,[]).append(i)
    items=sorted(blocks.items())
    gens=[]
    for b,pos in items: gens.append([(b,pos,pi) for pi in itertools.permutations(range(len(pos)))])
    out=[]
    for combo in itertools.product(*gens):
        perm=list(range(r)); eps=1
        for b,pos,pi in combo:
            for a,t in enumerate(pi): perm[pos[a]]=pos[t]
            # sign of pi
            s=1
            for a in range(len(pi)):
                for c in range(a+1,len(pi)):
                    if pi[a]>pi[c]: s=-s
            if b%2==1: eps*= s
        out.append((tuple(perm), eps))
    return out

def n_chi_direct(lam, delta, deg=4, verbose=False):
    L, idx, mons = monomials(lam, delta, deg)
    N=len(mons)
    A=np.array(mons, dtype=np.int32)
    A=np.sort(A,axis=1)
    G=group(lam)
    r=len(lam)
    total=0; fix_by_perm={}
    for perm,eps in G:
        # induced permutation on letters
        pl=np.empty(len(L),dtype=np.int32)
        for i,a in enumerate(L):
            b=tuple(a[perm.index(k)] for k in range(r)) if False else None
        # careful: letter alpha -> alpha o perm^{-1};  x_{perm[i]} receives x_i
        inv=[0]*r
        for i,p in enumerate(perm): inv[p]=i
        for i,a in enumerate(L):
            img=tuple(a[inv[k]] for k in range(r))
            pl[i]=idx[img]
        B=np.sort(pl[A],axis=1)
        f=int(np.all(B==A,axis=1).sum())
        fix_by_perm[perm]=(f,eps)
        total+=eps*f
    assert total % len(G)==0, (lam,delta,total,len(G))
    return N, len(G), total, total//len(G), fix_by_perm

def show(x): return '('+','.join(map(str,x))+')'

short=json.loads(subprocess.run(['git','-C',str(ROOT),'show',
      'b14-11-astra:results/b14_11/shortlist.json'],capture_output=True,text=True).stdout)

print("=== controls first ===", flush=True)
N,gs,tot,nc,_ = n_chi_direct((3,3,1,1),2)
print(f"  (3,3,1,1)_2: N_S={N} |G|={gs} signed sum={tot} n_chi={nc}  [proofs claim 2, unsigned 4]")
# unsigned version
_,_,_,_,fb = n_chi_direct((3,3,1,1),2)
uns=sum(f for f,e in fb.values())//gs
print(f"  (3,3,1,1)_2 unsigned (wrong trivial character) = {uns}")
N,gs,tot,nc,_ = n_chi_direct((14,2,2,2,2,2),6)
print(f"  (14,2,2,2,2,2)_6: N_S={N} n_chi={nc}  [banked control claims 7508 / 171]", flush=True)

print("=== the ten shortlist cells ===", flush=True)
bad=0
for c in short['candidates']:
    lam=tuple(c['lam']); d=c['delta']; t0=time.time()
    N,gs,tot,nc,fb = n_chi_direct(lam,d)
    okN = N==c['N_S']; okG = gs==c['stabilizer_order']; okT = tot==c['signed_trace_sum']; okC = nc==c['n_chi']
    # per-class agreement with the shipped representatives
    cls_ok=True
    for cl in c['classes']:
        p=tuple(cl['permutation'])
        if p not in fb: cls_ok=False; print("   class rep not in my group:",p); continue
        f,e=fb[p]
        if f!=cl['fixed_monomials'] or e!=cl['character']:
            cls_ok=False
            print(f"   CLASS MISMATCH {show(lam)} perm={p} mine=({f},{e}) theirs=({cl['fixed_monomials']},{cl['character']})")
    # class sizes: my full-group sum reproduces theirs only if class sizes are right
    csum=sum(cl['class_size'] for cl in c['classes'])
    their_tot=sum(cl['class_size']*cl['character']*cl['fixed_monomials'] for cl in c['classes'])
    flags=[okN,okG,okT,okC,cls_ok,csum==gs,their_tot==c['signed_trace_sum']]
    if not all(flags): bad+=1
    print(f"  {show(lam)}_{d}: N_S {N}/{c['N_S']} |G| {gs}/{c['stabilizer_order']} "
          f"sum {tot}/{c['signed_trace_sum']} n_chi {nc}/{c['n_chi']} classes={'OK' if cls_ok else 'BAD'} "
          f"sizes {csum}/{gs} theirsum={their_tot} {'OK' if all(flags) else 'MISMATCH'} {time.time()-t0:.1f}s", flush=True)
print("candidates with any mismatch:", bad)
