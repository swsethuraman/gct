"""a_lambda(delta) three ways: my own exact Weyl alternation over my own weight
counter, the house a_weyl_mod (modular DP + CRT), and the census a_weyl the driver
itself called."""
import sys, itertools, time
import pathlib as _p
ROOT=_p.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'analysis'))
sys.path.insert(0, str(_p.Path(__file__).resolve().parent))
from b14_12_nchi_burnside import letters, fixcount
from wk9_s57_lib import a_weyl_mod
from wk9_s42_census import a_weyl as census_a_weyl

def M(mu, delta, deg=4):
    """weight-space dimension at composition mu: monomials of degree delta in the
    quartic letters with exponent sum mu."""
    mu=list(mu)
    if any(x<0 for x in mu) or sum(mu)!=deg*delta: return 0
    r=len(mu); L=letters(r,deg)
    sup=[(1, tuple(a[1:])) for a in L]
    return fixcount(sup, delta, mu[1:])

def a_mine(lam, delta, deg=4):
    lam=tuple(lam); r=len(lam)
    rho=[r-1-i for i in range(r)]
    lr=[lam[i]+rho[i] for i in range(r)]
    tot=0; terms=0; cache={}
    for perm in itertools.permutations(range(r)):
        mu=tuple(lr[perm[t]]-rho[t] for t in range(r))
        if any(x<0 for x in mu): continue
        s=1
        for i in range(r):
            for j in range(i+1,r):
                if perm[i]>perm[j]: s=-s
        key=tuple(sorted(mu, reverse=True))          # M is symmetric in the weight
        if key not in cache: cache[key]=M(key, delta, deg)
        tot+=s*cache[key]; terms+=1
    return tot, terms, len(cache)

for lam, delta in [((12,4,4,4,4,4),8), ((10,6,6,6,2,2),8)]:
    t=time.time(); a1,nt,nd=a_mine(lam,delta); t1=time.time()-t
    t=time.time(); a2,_,_=a_weyl_mod(lam,delta,n=4,cache={}); t2=time.time()-t
    t=time.time(); a3=int(census_a_weyl(lam,delta,4,{})); t3=time.time()-t
    print(f"lam={lam} delta={delta}:  mine={a1} ({nt} Weyl terms, {nd} distinct, {t1:.1f}s)"
          f"   a_weyl_mod={a2} ({t2:.1f}s)   census a_weyl={a3} ({t3:.1f}s)"
          f"   {'ALL AGREE' if a1==a2==a3 else 'DISAGREE'}")
