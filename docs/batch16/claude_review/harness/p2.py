import sys,time
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad')
from harness import *
from red import gen_RED
p=PRIMES[1]; bs=enumerate_brackets(W,COL); ev=Evaluator(bs,COL,p)
for fam,seed in (('GEN',401),('DET',402),('PAD',403)):
    reds,_=gen_points(fam,p,480,seed,uniform=(fam!='GEN'))
    print(f'p2 {fam} uniform seed={seed} valid={len(reds)} RANK={rank_mod(evalmat(ev,reds),p)}',flush=True)
reds=gen_RED(p,480,404)
print(f'p2 RED uniform seed=404 valid={len(reds)} RANK={rank_mod(evalmat(ev,reds),p)}',flush=True)
