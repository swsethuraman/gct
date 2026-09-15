import sys, time
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad')
from harness import *
p = PRIMES[0]
bs = enumerate_brackets(W,COL); ev = Evaluator(bs,COL,p)
jobs = [('GEN',False,101),('DET',False,102),('PAD',False,103),
        ('PAD',True,104),('PAD',True,105),('DET',True,106)]
for fam,unif,seed in jobs:
    t0=time.time(); reds,src = gen_points(fam,p,480,seed,uniform=unif)
    assert all(consistency_defect(rd,COL,p)==0 for rd in reds)
    M = evalmat(ev,reds); r = rank_mod(M,p)
    print(f'{fam:4s} uniform={str(unif):5s} seed={seed} valid={len(reds):3d} RANK={r:4d}   ({time.time()-t0:.0f}s)',flush=True)
