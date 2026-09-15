"""RED family at r=10: F = (linear form) * (generic cubic) on C^10, uniform mod p.
Since every point of the padded-permanent orbit is a linear form times a cubic,
Y_PAD subset Y_RED, hence m_pad <= m_RED."""
import sys, time, itertools
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad')
import numpy as np
from harness import *
from b15_06_geometry import linear_jet

R=10; COL=9; W=35

def cubic_monomial_jets(J,p,s1val):
    """jets of every degree-3 monomial in (t,v_1..v_9) at t=s1val, v=e_1+eta."""
    mons=[a for a in itertools.product(range(4),repeat=R) if sum(a)==3]
    # coordinate jets: index0 = t (constant s1val), index1 = v_1 = 1+eta_0, index k = eta_{k-1}
    coord=[]
    z=J.zero(); z[0]=s1val%p; coord.append(z)
    z=J.zero(); z[0]=1; z[1]=1; coord.append(z)
    for k in range(2,R):
        z=J.zero(); z[1+(k-1)]=1; coord.append(z)
    out=[]
    for a in mons:
        t=J.zero(); t[0]=1
        for k in range(R):
            for _ in range(a[k]): t=J.mul(t,coord[k])
        out.append(t[:,0].copy())   # same for all points
    return mons, np.array(out)      # (nmon, jetdim)

def gen_RED(p,npts,seed):
    rng=np.random.default_rng(seed)
    J=Jet(COL,p,npts)
    L0=rng.integers(0,p,(R,npts),dtype=np.int64)
    mons=None
    C=None
    vals=[]
    for s1 in range(5):
        mons,MJ=cubic_monomial_jets(J,p,s1)
        if C is None:
            C=rng.integers(0,p,(len(mons),npts),dtype=np.int64)
        # cubic jet = sum_alpha C[alpha]*MJ[alpha]  -> (jetdim, npts)
        cj=(MJ.T.astype(object)@C.astype(object))%p
        cj=np.array(cj.tolist(),dtype=np.int64)
        vals.append(J.mul(linear_jet(L0,J,s1),cj))
    jets,c,defect,valid=normalise_depress(vals,list(range(5)),p,J)
    assert defect==0
    return [rd for rd,ok in zip(jet_point_list(J,jets),valid) if ok]

if __name__=='__main__':
    p=PRIMES[0]
    bs=enumerate_brackets(W,COL); ev=Evaluator(bs,COL,p)
    for seed in (201,202):
        t0=time.time(); reds=gen_RED(p,480,seed)
        assert all(consistency_defect(rd,COL,p)==0 for rd in reds)
        M=evalmat(ev,reds); r=rank_mod(M,p)
        print(f'RED uniform seed={seed} valid={len(reds)} RANK={r}  ({time.time()-t0:.0f}s)',flush=True)
