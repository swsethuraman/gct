#!/usr/bin/env python3
"""B13-01: reducible-point evaluation E_source of the 39 rung-<=13 fillings at
one prime, and the left-kernel (candidate reducible relations) in RREF.
Points are a fixed integer reducible set (seed-derived) shared across primes so
the RREF kernels are directly CRT-combinable.  row_i = F_i^native * u^(13-d_i).
usage: wk13_b13_01_esource.py <prime> <out.json> [npoints] [seed]
"""
import sys, json, random, time, itertools, os
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import wk11_s69_circuit as C
from wk8_s30_core import exps
from flint import nmod_mat

N,R=4,9
def main():
    p=int(sys.argv[1]); out=sys.argv[2]
    npts=int(sys.argv[3]) if len(sys.argv)>3 else 44
    seed=int(sys.argv[4]) if len(sys.argv)>4 else 4242
    ROOT=os.path.normpath(os.path.join(HERE,'..'))
    src=json.load(open(os.path.join(ROOT,'results/s74/source.json')))
    ent=[e for e in src['entries'] if e['rung']<=13]; assert len(ent)==39
    deg=[e['rung'] for e in ent]
    fills=[C.Filling(e['native']['h'],e['native']['n'],e['native']['delta'],e['native']['C1'],e['native']['C2'],e['native']['two'],e['native']['one']) for e in ent]
    A,idx,fact,tab=C.sym_table(N,R); Aexps=exps(N,R)
    def red_point(rng,bound=11):
        lf=[rng.randint(-bound,bound) for _ in range(R)]
        cub={e:rng.randint(-bound,bound) for e in itertools.product(range(4),repeat=R) if sum(e)==3}
        f4={}
        for i,c1 in enumerate(lf):
            if not c1: continue
            e1=tuple(1 if k==i else 0 for k in range(R))
            for e2,c2 in cub.items():
                e=tuple(x+y for x,y in zip(e1,e2)); f4[e]=f4.get(e,0)+c1*c2
        mu=24*lf[0]*cub.get((3,)+(0,)*(R-1),0)
        return [int(f4.get(al,0)) for al in Aexps], mu
    rng=random.Random(seed); pts=[]
    while len(pts)<npts:
        cv,mu=red_point(rng)
        if mu==0: continue
        pts.append((cv,mu))
    t=time.time(); rows=[]
    for i in range(39):
        Fi=fills[i]; di=deg[i]; row=[]
        for cv,mu in pts:
            msym=[(cv[k]%p)*fact[k]%p for k in range(len(A))]
            v=C.dp_eval_c(Fi,msym,p,tab); v=v*pow(mu%p,13-di,p)%p
            row.append(v)
        rows.append(row)
    m=len(pts)
    M=nmod_mat(m,39,[rows[i][k] for k in range(m) for i in range(39)],p)
    rank=M.rank()
    K,nul=M.nullspace()
    KB=nmod_mat(nul,39,[int(K[i,j]) for j in range(nul) for i in range(39)],p).rref()[0]
    KBrows=[[int(KB[r,c]) for c in range(39)] for r in range(nul)]
    json.dump({'prime':p,'npoints':m,'seed':seed,'rank':rank,'nullity':nul,
               'kernel_rref':KBrows,'secs':time.time()-t,
               'esource_rows':rows,  # keep for exact re-derivation / minor certificate
               'points_cv':[cv for cv,_ in pts],'u':[mu for _,mu in pts]},
              open(out,'w'))
    print("p=%d rank=%d nullity=%d (%.0fs)"%(p,rank,nul,time.time()-t),flush=True)

if __name__=='__main__': main()
