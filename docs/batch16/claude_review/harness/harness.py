"""Replication harness: rebuild GEN/DET/PAD rank floors for r=10, W=35, col=9.
Adds a PAD variant with L sampled UNIFORMLY mod p (Schwartz-Zippel-certifiable)."""
import sys, time, itertools
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad/packet')
import numpy as np
from math import factorial
from b14_06_bracket import (enumerate_brackets, Jet, jet_point_list, random_point,
                            consistency_defect, det_mod, rank_mod, _fl, PRIMES)
from b14_06_points import normalise_depress, _principal_minors, _det_jet, _per3
from b15_06_geometry import Evaluator, linear_jet, determinant, product_point

R = 10
COL = R-1          # 9
W  = 35

def gen_points(family, p, npts, seed, entry=12, uniform=False):
    rng = np.random.default_rng(seed)
    if family=='GEN':
        return [random_point(COL,p,rng) for _ in range(npts)], None
    if family=='DET':
        if uniform:
            A = rng.integers(0,p,(COL,4,4,npts),dtype=np.int64)
        else:
            A = rng.integers(-entry,entry+1,(COL,4,4,npts),dtype=np.int64)
        A[:,3,3] = -(A[:,0,0]+A[:,1,1]+A[:,2,2])
        J,jets = determinant(R,p,A)
        return jet_point_list(J,jets), A
    if family in ('PAD','NEG'):
        nf = 10 if family=='PAD' else 4
        if uniform:
            L = rng.integers(0,p,(nf,R,npts),dtype=np.int64)
        else:
            L = rng.integers(-entry,entry+1,(nf,R,npts),dtype=np.int64)
        J,jets,c,valid = product_point(R,p,L,family=='PAD')
        reds=[red for red,ok in zip(jet_point_list(J,jets),valid) if ok]
        return reds, L
    raise ValueError(family)

def evalmat(ev, reds):
    return list(map(list, zip(*(ev.values(red) for red in reds))))

if __name__=='__main__':
    p = PRIMES[0]
    bs = enumerate_brackets(W,COL)
    t0=time.time(); ev = Evaluator(bs,COL,p); print('build',round(time.time()-t0,1),flush=True)
    npts = int(sys.argv[1]) if len(sys.argv)>1 else 40
    for fam,unif,seed in [('GEN',False,11),('DET',False,12),('PAD',False,15060010*0+15060000+100*R+0)]:
        t0=time.time(); reds,_ = gen_points(fam,p,npts,seed,uniform=unif)
        assert all(consistency_defect(rd,COL,p)==0 for rd in reds)
        t1=time.time(); M = evalmat(ev,reds); t2=time.time()
        r = rank_mod(M,p); t3=time.time()
        print(f'{fam:4s} unif={unif} npts={npts} valid={len(reds)} rank={r}  '
              f'pts={t1-t0:.1f}s eval={t2-t1:.1f}s rank={t3-t2:.1f}s',flush=True)
