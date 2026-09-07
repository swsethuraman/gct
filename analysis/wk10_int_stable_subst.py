import itertools, pickle, random, sys, functools
P=2147483647; NV=5; N=4
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
def psc(a,s): return {e:(c*s)%P for e,c in a.items() if (c*s)%P}
def matmul(X,Y):
    return [[functools.reduce(padd,[pmul(X[i][k],Y[k][j]) for k in range(N)],{}) for j in range(N)] for i in range(N)]
def trace(X): return functools.reduce(padd,[X[i][i] for i in range(N)],{})
def pencil(seed):
    rnd=random.Random(seed); As=[]
    for _ in range(NV):
        M=[[rnd.randrange(P) for _ in range(N)] for _ in range(N)]
        s=sum(M[i][i] for i in range(N))%P; M[N-1][N-1]=(M[N-1][N-1]-s)%P
        As.append(M)
    return As
def gvals(As):
    A=[[{} for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d={}
            for k in range(NV):
                e=tuple(1 if q==k else 0 for q in range(NV))
                if As[k][i][j]%P: d[e]=As[k][i][j]%P
            A[i][j]=d
    A2=matmul(A,A); A3=matmul(A2,A); A4=matmul(A2,A2)
    p2,p3,p4=trace(A2),trace(A3),trace(A4)
    i2=pow(2,P-2,P);i3=pow(3,P-2,P);i4=pow(4,P-2,P);i8=pow(8,P-2,P)
    return {2:psc(p2,(-i2)%P),3:psc(p3,(-i3)%P),4:padd(psc(pmul(p2,p2),i8),psc(p4,(-i4)%P))}
def monolist():
    def m(d): return [a for a in itertools.product(range(d+1),repeat=NV) if sum(a)==d]
    return [(d,a) for d in (2,3,4) for a in m(d)]
GENS=monolist()
def evalF(D,As):
    g=gvals(As); yv=[g[d].get(a,0) for (d,a) in GENS]
    tot=0
    for ci,mm in enumerate(D['src']):
        c=D['vec'][ci]
        if not c: continue
        p=c
        for gi in mm:
            p=p*yv[gi]%P
            if p==0: break
        tot=(tot+p)%P
    return tot
for tag in sys.argv[1:]:
    D=pickle.load(open('/tmp/hwvA_%s.pkl'%tag,'rb'))
    vals=[evalF(D,pencil(2000+s)) for s in range(3)]
    verdict="NONZERO  => i_det^inf = 0 (exact: one nonzero point certifies it)" if any(vals) else "zero at 3 points (inconclusive)"
    print("rho=%-16s F at 3 pencils: %s"%(str(D['w']),vals))
    print("   verdict: %s"%verdict)
    # convention-independent HWV check: P must be invariant under A_{i+1} -> A_{i+1} + eps*A_i
    As=pencil(4242); base=evalF(D,As); ok=True
    for i in range(NV-1):
        for eps in (1,7,999):
            Bs=[list(map(list,M)) for M in As]
            for r in range(N):
                for c in range(N): Bs[i+1][r][c]=(Bs[i+1][r][c]+eps*As[i][r][c])%P
            if evalF(D,Bs)!=base: ok=False; print("   HWV CHECK FAILED at E_%d%d, eps=%d"%(i+1,i+2,eps))
    print("   highest-weight check (P invariant under A_{i+1} -> A_{i+1}+eps A_i, all 4 raisings, 3 eps): %s"%("PASS" if ok else "FAIL"))
