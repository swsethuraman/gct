"""Sparse exact evaluator for the two five-row carrier vectors at a simple fiber pair."""
import itertools as it
import json
from collections import defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
PERMS=list(it.permutations(range(5)))
def sign(v):return (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
SIGNS=[sign(v) for v in PERMS]

def wedges(Y):
    entries=[[(k,v) for k,v in enumerate(m) if v] for m in Y]
    result=[]
    for chosen in it.product(*entries):
        if len(set(k for k,v in chosen))<5:continue
        c0=1
        for k,v in chosen:c0*=v
        for perm,ss in zip(PERMS,SIGNS):
            result.append((tuple(chosen[i][0] for i in perm),ss*c0))
    return result

def flatten(part):
    starts=[0,5,10,11]
    return [tuple(starts[j]+k for j,k in block) for block in part]

def evaluate_P(Y,pi,rho):
    # Slots 0..4,10,11 on the left; 5..9 on the right.
    left_slots=set(range(5))|{10,11}
    blocks=[(part,axis) for part,axis in [(pi,0),(rho,1)] for part in part]
    # A constant sign moves each ordered epsilon's left arguments before its right arguments.
    sh=1
    for block,axis in blocks:
        types=[int(k not in left_slots) for k in block]
        sh*=(-1)**sum(types[i]>types[j] for i in range(4) for j in range(i+1,4))
    def key_sign(coords,left):
        key=[]
        ss=1
        for block,axis in blocks:
            vals=[divmod(coords[k],4)[axis] for k in block if (k in left_slots)==left]
            if len(set(vals))!=len(vals):return None,0
            key.append(sum(1<<v for v in vals))
            ss*=sign(vals)
        return tuple(key),ss
    ww=wedges(Y)
    buckets=defaultdict(int)
    for cc,v in ww:
        key,ss=key_sign(dict(zip(range(5,10),cc)),False)
        if key is not None:buckets[key]+=ss*v
    total=0
    entries=[(k,v) for k,v in enumerate(Y[0]) if v]
    for cc,v in ww:
        for (a,va),(b,vb) in it.product(entries,repeat=2):
            coord=dict(zip(range(5),cc))
            coord.update({10:a,11:b})
            key,ss=key_sign(coord,True)
            if key is None:continue
            cv=buckets.get(tuple(15^m for m in key),0)
            if not cv:continue
            for mask in key:
                aa=[i for i in range(4) if mask&(1<<i)]
                bb=[i for i in range(4) if not mask&(1<<i)]
                ss*=sign(aa+bb)
            total+=sh*ss*v*va*vb*cv
    return total

def qvalue(Y,pair):
    pi,rho=map(flatten,pair)
    return evaluate_P(Y,pi,rho)+evaluate_P(Y,rho,pi)

def main():
    data=json.loads(HERE.joinpath('pilot.json').read_text())
    Y=[[0]*16 for _ in range(5)]
    for i,entries in enumerate([(0,10),(1,11),(4,14),(5,),(15,)]):
        for k in entries:Y[i][k]=1
    partner=[list(m) for m in Y]
    for m in partner:m[1],m[4]=m[4],m[1]
    vals=[[qvalue(Z,pair) for pair in data['basis']] for Z in (Y,partner)]
    differences=[a-b for a,b in zip(*vals)]
    assert any(differences)
    result={'pencil':'diag([[x1,x2],[x3,x4]],[[x1,x2],[x3,x5]])',
            'partner':'transpose first 2x2 block only',
            'common_determinant':'(x1*x4-x2*x3)*(x1*x5-x2*x3)',
            'basis_pairs_flat':[[flatten(part) for part in pair] for pair in data['basis']],
            'values':vals,'difference':differences,'matrices':Y,'partner_matrices':partner,
            'column_assignments':len(wedges(Y))}
    HERE.joinpath('exact_pair.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('matrices','partner_matrices')},indent=2))

if __name__=='__main__':main()
