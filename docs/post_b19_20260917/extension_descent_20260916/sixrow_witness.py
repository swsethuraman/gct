"""Lift the small invariant by squaring and test descent at two pencils."""
import itertools as it
import json
import math
import time
from collections import defaultdict
from pathlib import Path
import skew_witness as base

START = time.monotonic()
PI = ((0,1,6,7),(2,3,8,9),(4,5,10,11))
RHO = ((3,1,10,9),(5,2,11,6),(4,0,8,7))

def column_assignments(matrices):
    entries = [[(divmod(k,4),v) for k,v in enumerate(m) if v] for m in matrices]
    out = []
    for selected in it.product(*entries):
        coords = tuple(p for p,v in selected)
        if len(set(coords)) != 6:
            continue
        value = math.prod(v for p,v in selected)
        for perm in it.permutations(range(6)):
            cc = [coords[i] for i in perm]
            out.append((tuple(a for a,b in cc),tuple(b for a,b in cc), value*base.sign(perm)))
    return out

def aggregate(assignments, colpairs):
    out = defaultdict(int)
    for aa,bb,ss in assignments:
        key = []
        for indices,pairs in ((aa,base.PAIRS),(bb,colpairs)):
            for i,j in pairs:
                a,b = indices[i],indices[j]
                if a == b:
                    break
                key.append((1<<a)|(1<<b))
                if a>b:
                    ss = -ss
            else:
                continue
            break
        if len(key)==6:
            out[tuple(key)] += ss
    return {k:v for k,v in out.items() if v}

def invariant_P(matrices):
    assignments=column_assignments(matrices)
    left=aggregate(assignments,tuple(p[:2] for p in RHO))
    right=aggregate(assignments,tuple(tuple(v-6 for v in p[2:]) for p in RHO))
    return base.join(left,right)[0], len(assignments)

def transpose(matrices):
    return [[m[4*j+i] for i in range(4) for j in range(4)] for m in matrices]

def invariant_Q(matrices):
    val,n=invariant_P(matrices)
    vt,nt=invariant_P(transpose(matrices))
    return val+vt, n

def quartic(matrices):
    out=defaultdict(int)
    for perm in it.permutations(range(4)):
        choices=[[(k,m[4*i+perm[i]]) for k,m in enumerate(matrices) if m[4*i+perm[i]]] for i in range(4)]
        for vals in it.product(*choices):
            alpha=[0]*6
            v=base.sign(perm)
            for k,a in vals:
                alpha[k]+=1
                v*=a
            out[tuple(alpha)]+=v
    return {a:v for a,v in out.items() if v}

def H6(f):
    # H(T) with T_ijkl = alpha! c_alpha, exactly as B15-10's convention.
    tensors=[[] for _ in range(6)]
    for alpha,c in f.items():
        indices=tuple(i for i,a in enumerate(alpha) for _ in range(a))
        coeff=c*math.prod(math.factorial(a) for a in alpha)
        for tup in set(it.permutations(indices)):
            i,j,k,l=tup
            tensors[i].append((j,k,l,coeff))
    dp={(0,0,0):1}
    peak=1
    for row in tensors:
        nd=defaultdict(int)
        for masks,val in dp.items():
            for j,k,l,c in row:
                vs=(j,k,l)
                if any(mask & (1<<v) for mask,v in zip(masks,vs)):
                    continue
                inv=sum((mask>>(v+1)).bit_count() for mask,v in zip(masks,vs))
                mm=tuple(mask|(1<<v) for mask,v in zip(masks,vs))
                nd[mm]+=val*c*(-1)**inv
        dp={k:v for k,v in nd.items() if v}
        peak=max(peak,len(dp))
    return dp.get((63,63,63),0),peak

def main():
    skew=[]
    for i,j in base.EDGES:
        m=[0]*16
        m[4*i+j]=1
        m[4*j+i]=-1
        skew.append(m)
    cycle=[[0]*16 for _ in range(6)]
    for i in range(4):
        cycle[i][5*i]=1
    for i in range(4):
        cycle[4+i//2][4*i+(i+1)%4]=1
    result={'pi':PI,'rho':RHO,'points':[]}
    for label,ms in [('skew',skew),('cycle',cycle)]:
        q,n=invariant_Q(ms)
        f=quartic(ms)
        h,peak=H6(f)
        result['points'].append(dict(label=label,matrices=ms,Q=q,Q_squared=q*q,H=h,
            quartic=[{'exponent':a,'coefficient':v} for a,v in sorted(f.items())],
            column_assignments=n,H_DP_peak=peak))
    p0,p1=result['points']
    result['descent_minor']=p0['H']*p1['Q_squared']-p1['H']*p0['Q_squared']
    result['elapsed_seconds']=time.monotonic()-START
    assert p0['Q']==-86400
    assert p1['H'] != 0
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='points'},indent=2))
    for p in result['points']:
        print({k:v for k,v in p.items() if k not in ('matrices','quartic')})

if __name__=='__main__':
    main()
