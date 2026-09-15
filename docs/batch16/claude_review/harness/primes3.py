import sys,time
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad')
from harness import *
from red import gen_RED
from flint import fmpz
def isprime(n): return fmpz(n).is_prime()
extra=[]
q=2147483000
while len(extra)<2:
    q-=1
    if isprime(q) and q not in PRIMES: extra.append(q)
print('extra primes',extra,flush=True)
bs=enumerate_brackets(W,COL)
for p in extra:
    ev=Evaluator(bs,COL,p)
    for fam,seed in (('GEN',501),('DET',502),('PAD',503)):
        reds,_=gen_points(fam,p,480,seed+p%97,uniform=(fam!='GEN'))
        print(f'p={p} {fam} valid={len(reds)} RANK={rank_mod(evalmat(ev,reds),p)}',flush=True)
    reds=gen_RED(p,480,504+p%97)
    print(f'p={p} RED valid={len(reds)} RANK={rank_mod(evalmat(ev,reds),p)}',flush=True)
