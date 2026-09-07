import gzip, json, random, itertools
P=2147483647; r=5; N=4

def pmul(a,b):
    o={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(x+y for x,y in zip(e1,e2)); o[e]=(o.get(e,0)+c1*c2)%P
    return {e:c for e,c in o.items() if c}
def padd(a,b):
    o=dict(a)
    for e,c in b.items(): o[e]=(o.get(e,0)+c)%P
    return {e:c for e,c in o.items() if c}
def lin(rnd):
    return {tuple(1 if k==i else 0 for k in range(r)): rnd.randrange(1,P) for i in range(r)}

def per3(M):
    acc={}
    for s in itertools.permutations(range(3)):
        acc=padd(acc, pmul(pmul(M[0][s[0]],M[1][s[1]]),M[2][s[2]]))
    return acc
def det4(M):
    acc={}
    for s in itertools.permutations(range(4)):
        sgn=1
        pl=list(s)
        for i in range(4):
            for j in range(i+1,4):
                if pl[i]>pl[j]: sgn=-sgn
        t=pmul(pmul(M[0][s[0]],M[1][s[1]]),pmul(M[2][s[2]],M[3][s[3]]))
        acc=padd(acc,{e:(sgn*c)%P for e,c in t.items()})
    return acc

def pad_point(seed):                       # l(s) * per_3(A(s))
    rnd=random.Random(seed)
    return pmul(lin(rnd), per3([[lin(rnd) for _ in range(3)] for _ in range(3)]))
def red_point(seed):                       # l(s) * generic cubic
    rnd=random.Random(seed)
    cub={e:rnd.randrange(1,P) for e in itertools.product(range(4),repeat=r) if sum(e)==3}
    return pmul(lin(rnd), cub)
def det_point(seed):                       # det_4 pencil
    rnd=random.Random(seed)
    return det4([[lin(rnd) for _ in range(4)] for _ in range(4)])

def ev(terms, F):
    tot=0
    for t in terms:
        mult, coef = t[0], t[1]
        p=coef % P
        for al in mult:
            p=(p*F.get(tuple(al),0))%P
            if p==0: break
        tot=(tot+p)%P
    return tot

d=json.load(gzip.open('results/s64_kern/kern_13_13_8_1_1_d9.json.gz','rt'))
print('cell', d['cell']); print('mult', d['mult'])
for side in ('red','pad'):
    for vi,vec in enumerate(d['U_terms'][side]):
        terms=vec['terms']
        print('\nU_%s[%d]: %d terms'%(side,vi,len(terms)))
        for name,gen in (('padded',pad_point),('reducible',red_point),('det pencil',det_point)):
            vals=[ev(terms,gen(1000+s)) for s in range(3)]
            tag='ZERO  <- in the ideal' if all(v==0 for v in vals) else 'NONZERO'
            print('   at %-11s seeds 0,1,2 : %-34s %s'%(name,str(vals)[:34],tag))
