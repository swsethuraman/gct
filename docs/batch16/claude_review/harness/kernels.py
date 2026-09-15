import sys, time, collections
sys.path.insert(0,'/tmp/claude-0/-home-claude/41a93519-a080-57d4-8d2d-e54d1ee4e620/scratchpad')
import numpy as np
from harness import *
from red import gen_RED
from flint import nmod_mat
p=PRIMES[0]; bs=enumerate_brackets(W,COL); ev=Evaluator(bs,COL,p)
NB=len(bs)

def leftker(M):
    """basis (rows) of {k : k^T M = 0}, M given as list of rows (brackets x points)."""
    A=nmod_mat(len(M),len(M[0]),[int(v)%p for r in M for v in r],p)
    return A.nullspace()   # returns (X, nullity) for column nullspace of A

def kerbasis(M):
    A=nmod_mat(len(M),len(M[0]),[int(v)%p for r in M for v in r],p)
    X,n=A.transpose().nullspace()      # columns span null space of M^T  (= left ker of M)
    return np.array([[int(X[i,j]) for i in range(NB)] for j in range(n)],dtype=object), n

mats={}
t0=time.time()
reds,_=gen_points('GEN',p,480,301); mats['GEN']=evalmat(ev,reds)
reds,_=gen_points('DET',p,480,302,uniform=True); mats['DET']=evalmat(ev,reds)
reds,_=gen_points('PAD',p,480,303,uniform=True); mats['PAD']=evalmat(ev,reds)
mats['RED']=evalmat(ev,gen_RED(p,480,304))
print('matrices built',round(time.time()-t0),flush=True)
K={};n={}
for f in ('GEN','DET','PAD','RED'):
    K[f],n[f]=kerbasis(mats[f]); print(f,'rank',NB-n[f],'leftker',n[f],flush=True)
def dim_span(rows):
    if len(rows)==0: return 0
    A=nmod_mat(len(rows),NB,[int(v)%p for r in rows for v in r],p); return int(A.rank())
g=n['GEN']
print('i_fam (= 429 - rank):', {f: (NB-g)-(NB-n[f]) for f in K})
import itertools
for a,b in itertools.combinations(('DET','PAD','RED'),2):
    both=np.vstack([K[a],K[b]]); s=dim_span(list(both))
    inter=n[a]+n[b]-s
    print(f'dim(K_{a} + K_{b})={s}  dim(K_{a} cap K_{b})={inter}  -> dim(I_{a} cap I_{b})={inter-g}',flush=True)
# inclusion test I_RED subset I_PAD ?
s=dim_span(list(np.vstack([K['RED'],K['PAD']])))
print('K_RED subset K_PAD ?', s==n['PAD'], '(span',s,'vs',n['PAD'],')')
# per-multidegree profile
deg=collections.defaultdict(list)
for i,(a,b,c,z) in enumerate(bs):
    deg[tuple(a[k]+b[k]+c[k]+z[k] for k in range(3))].append(i)
print('\nmultideg  #br  GEN  DET  PAD  RED')
tot=collections.Counter()
for d in sorted(deg):
    idx=deg[d]; row=[]
    for f in ('GEN','DET','PAD','RED'):
        sub=[mats[f][i] for i in idx]; row.append(rank_mod(sub,p)); tot[f]+=row[-1]
    print(f'{str(d):12s}{len(idx):4d} {row[0]:4d} {row[1]:4d} {row[2]:4d} {row[3]:4d}')
print('sum of graded ranks:',dict(tot))
