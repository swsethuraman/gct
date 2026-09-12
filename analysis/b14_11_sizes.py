"""Exact character-twisted Burnside dimensions, with explicit orbit controls."""
import itertools, math, time
from collections import Counter
import numpy as np
from wk8_s30_pleth import parts, zr


def exps(n,r):
    if r==1:return [(n,)]
    return [(i,)+t for i in range(n+1) for t in exps(n-i,r-1)]


def permute(e,g):return tuple(e[g[i]] for i in range(len(g)))


def classes(lam):
    blocks=[]
    for value in sorted(set(lam),reverse=True):
        idx=[i for i,x in enumerate(lam) if x==value]
        blocks.append((value,idx))
    for types in itertools.product(*(parts(len(idx)) for _,idx in blocks)):
        g=list(range(len(lam))); count=1;sign=1
        for (value,idx),ctype in zip(blocks,types):
            count*=math.factorial(len(idx))//zr(ctype)
            sign*=(-1)**((len(idx)-len(ctype))*value)
            pos=0
            for length in ctype:
                cycle=idx[pos:pos+length];pos+=length
                for i,j in zip(cycle,cycle[1:]+cycle[:1]):g[i]=j
        yield tuple(g),count,sign


def letter_orbits(lam,g):
    E=set(e for e in exps(4,len(lam)) if all(a<=b for a,b in zip(e,lam)))
    orbits=[]
    while E:
        e=min(E);orb=[];x=e
        while x not in orb:orb.append(x);x=permute(x,g)
        E.difference_update(orb)
        orbits.append((len(orb),tuple(sum(x[j] for x in orb) for j in range(len(lam)))))
    return orbits


def fixed_count(lam,d,g):
    """Coefficient of product_orbits (1-t^size x^orbit_sum)^-1, over Z."""
    tail=lam[1:];shape=(d+1,)+tuple(x+1 for x in tail)
    F=np.zeros(shape,dtype=object);F[(0,)*len(shape)]=1
    for length,e in letter_orbits(lam,g):
        if length>d or any(a>b for a,b in zip(e,lam)):continue
        src=tuple(slice(0,b+1-a) for a,b in zip(e[1:],tail))
        dst=tuple(slice(a,b+1) for a,b in zip(e[1:],tail))
        for k in range(length,d+1):F[(k,)+dst]+=F[(k-length,)+src]
    return int(F[(d,)+tuple(tail)])


def burnside(lam,d):
    start=time.time();records=[];total=0;group=math.prod(math.factorial(c) for c in Counter(lam).values())
    for g,size,sign in classes(lam):
        count=fixed_count(lam,d,g);total+=size*sign*count
        records.append(dict(permutation=g,class_size=size,character=sign,fixed_monomials=count))
    require(sum(x['class_size'] for x in records)==group,'class coverage')
    require(total%group==0,'nonintegral dimension');nchi=total//group
    ns=next(x['fixed_monomials'] for x in records if x['permutation']==tuple(range(len(lam))))
    require(0<=nchi<=ns,'dimension bounds')
    return dict(n=4,delta=d,lam=lam,N_S=ns,stabilizer_order=group,n_chi=nchi,
                signed_trace_sum=total,classes=records,arithmetic='Z; exact final division by group order',
                wall_seconds=round(time.time()-start,4))


def require(condition,message):
    if not condition:raise ValueError(message)


def direct_orbits(lam,d):
    E=exps(4,len(lam));M=set()
    for indices in itertools.combinations_with_replacement(range(len(E)),d):
        if tuple(sum(E[j][i] for j in indices) for i in range(len(lam)))==tuple(lam):
            M.add(tuple(sorted(E[j] for j in indices)))
    raw=len(M);kept=0
    blocks=[[i for i,x in enumerate(lam) if x==v] for v in sorted(set(lam),reverse=True)]
    group=[]
    for product in itertools.product(*(list(itertools.permutations(b)) for b in blocks)):
        g=list(range(len(lam)));sign=1
        for block,perm in zip(blocks,product):
            for i,j in zip(block,perm):g[i]=j
            inversions=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
            sign*=(-1)**(inversions*lam[block[0]])
        group.append((g,sign))
    while M:
        m=min(M);images={};compatible=True
        for g,sign in group:
            new=tuple(sorted(permute(e,g) for e in m))
            if new in images and images[new]!=sign:compatible=False
            images[new]=sign
        M.difference_update(images)
        kept+=int(compatible)
    return raw,kept


def controls():
    out=[]
    for lam,d in [((2,2,2,2),2),((3,3,1,1),2),((4,2,2),2),((4,4),2)]:
        b=burnside(lam,d);raw,nchi=direct_orbits(lam,d)
        require((raw,nchi)==(b['N_S'],b['n_chi']),'explicit orbit mismatch')
        badsum=b['signed_trace_sum']+1
        try:require(badsum==nchi*b['stabilizer_order'],'altered fixed count')
        except ValueError:rejected=True
        else:raise AssertionError('bad fixed count passed')
        out.append(dict(lam=lam,delta=d,N_S=raw,n_chi=nchi,mutation_rejected=rejected))
    odd=burnside((3,3,1,1),2)
    wrong=sum(x['class_size']*x['fixed_monomials'] for x in odd['classes'])//odd['stabilizer_order']
    require(wrong!=odd['n_chi'],'odd-character control vacuous')
    bank=burnside((14,2,2,2,2,2),6)
    require(bank['N_S']==7508 and bank['n_chi']==171,'s36 size mismatch')
    return dict(status='PASS',explicit_orbit_controls=out,wrong_trivial_character=wrong,
                correct_odd_character=odd['n_chi'],wrong_character_rejected=True,banked_s36=bank)
