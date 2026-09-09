#!/usr/bin/env python3
"""B13-01: h_pad(lam,delta) = sum_mu a3(mu,delta) over the horizontal-delta-strips
lam/mu, a3(mu,delta)=mult of S_mu in Sym^delta(Sym^3 C^9), by the Weyl alternation
a3(mu)=sum_{w in S_9} sgn(w) m(w(mu+rho)-rho), m = #multisets of delta cubics summing
to that weight (analysis/wk13_b13_01_mcount.c, shared-memo).  Prints h_pad and the
per-block a3.  For lam=(21,17,2^7), delta=13: h_pad=73."""
import sys, subprocess, os, json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from wk9_s42_hpad import pieri_strips
def hpad(lam, delta, mcount_bin):
    rho=tuple(range(8,-1,-1))
    st=[tuple(x for x in m if x) for m in pieri_strips(lam,delta)]
    per_mu=[]; allnu={}
    for mu in st:
        mm=tuple(mu)+(0,)*(9-len(mu)); L=[mm[i]+rho[i] for i in range(9)]
        terms=[]; used=[False]*9; perm=[-1]*9
        def bt(pos):
            if pos==9:
                s=1
                for i in range(9):
                    for j in range(i+1,9):
                        if perm[i]>perm[j]: s=-s
                nu=tuple(sorted((L[perm[i]]-rho[i] for i in range(9)),reverse=True))
                allnu.setdefault(nu,len(allnu)); terms.append((s,nu)); return
            for j in range(9):
                if used[j] or L[j]<rho[pos]: continue
                used[j]=True; perm[pos]=j; bt(pos+1); used[j]=False; perm[pos]=-1
        bt(0); per_mu.append((mu,terms))
    nus=list(allnu)
    inp="%d\n"%len(nus)+"".join(" ".join(map(str,n))+"\n" for n in nus)
    vals=[int(x) for x in subprocess.run([mcount_bin],input=inp,capture_output=True,text=True).stdout.split()]
    mcm={nus[i]:vals[i] for i in range(len(nus))}
    rows=[(mu,sum(s*mcm[tuple(n)] for s,n in tm)) for mu,tm in per_mu]
    return sum(a for _,a in rows), rows
if __name__=='__main__':
    import subprocess as sp
    mb='/tmp/mcount'
    if not os.path.exists(mb):
        sp.run(['gcc','-O2','-o',mb,os.path.join(HERE,'wk13_b13_01_mcount.c')])
    h,rows=hpad((21,17,2,2,2,2,2,2,2),13,mb)
    for mu,a in rows: print("mu=%-28s a3=%d"%(str(mu),a))
    print("h_pad =",h)
