"""Independent rebuild of session 32's two exceptional strata.

k = 4:  M_0(y) t = phi(y ^ t),  phi : Lambda^2 C^4 -> C^4 arbitrary
        -> column j of M_0(y) = sum_i y_i Phi_ij,  Phi_ij = -Phi_ji in C^4.
        Params: Phi (6 x 4 = 24) + A_1 (16).           Expected rank 25.
k = 3:  ker L = <f_4>, phi kills C^4 ^ f_4 -> only Phi_12, Phi_13, Phi_23 (12);
        column 4 of M_0(y) arbitrary linear (16); substitution y -> G y (16)
        restored as parameters per session 32's bug fix; + A_1 (16).
        Params 60 (their "60-parameter family").        Expected rank 27.
Rank of d(params -> coefficients of G = det(s_1 A_1 + M_0(Gy))/s_1) mod p.
"""
import random, itertools
P=(1<<61)-1; R=5
def pmul(a,b):
    o={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(e1[k]+e2[k] for k in range(R)); o[e]=(o.get(e,0)+c1*c2)%P
    return {e:c for e,c in o.items() if c}
def padd(a,b):
    o=dict(a)
    for e,c in b.items(): o[e]=(o.get(e,0)+c)%P
    return {e:c for e,c in o.items() if c}
def det4(M):
    acc={}
    for pm in itertools.permutations(range(4)):
        sg=1
        for i in range(4):
            for j in range(i+1,4):
                if pm[i]>pm[j]: sg=-sg
        t={tuple([0]*R):sg%P}
        for p_ in range(4): t=pmul(t,M[p_][pm[p_]])
        acc=padd(acc,t)
    return acc
def div_s1(poly):
    o={}
    for e,c in poly.items():
        assert e[0]>=1,"branch left the divisible locus"
        o[tuple([e[0]-1]+list(e[1:]))]=c
    return o
MON3=[e for e in itertools.product(range(4),repeat=R) if sum(e)==3]
IDX={e:k for k,e in enumerate(MON3)}
def coeffs(params, build_fn):
    A1,rest=params
    Msym=build_fn(rest)
    M=[[{} for _ in range(4)] for _ in range(4)]
    for p_ in range(4):
        for q in range(4):
            d={}
            v=A1[p_][q]%P
            if v: d[(1,0,0,0,0)]=v
            for i in range(4):
                w=Msym[i][p_][q]%P
                if w:
                    e=[0]*R; e[i+1]=1; e=tuple(e)
                    d[e]=(d.get(e,0)+w)%P
            M[p_][q]=d
    G=div_s1(det4(M))
    v=[0]*35
    for e,c in G.items(): v[IDX[e]]=c
    return v
def jrank(build,unpack_fn,npar,seed):
    """finite-difference-free exact Jacobian: params are linear->cubic, so use
       symbolic epsilon: f(p+eps q)-f(p) has eps-linear part = directional deriv.
       Cheap trick with three evaluations since coeffs are degree <=4 in params:
       use exact directional derivative via 5-point... simpler: coeffs are
       polynomial of degree <= 4 in params; directional derivative extracted by
       finite differences over the prime field at 5 scales with Vandermonde."""
    rnd=random.Random(seed)
    base=[rnd.randint(-6,6) for _ in range(npar)]
    def f(vec): return coeffs(unpack_fn(vec),build)
    rows=[]
    ts=[1,2,3,4,5]
    import functools
    # Vandermonde solve for the linear coefficient of f(base + t*e_k) in t
    V=[[pow(t,j,P) for j in range(1,6)] for t in ts]
    # invert V mod P (5x5)
    n=5; A=[row[:]+[1 if i==j else 0 for j in range(n)] for i,row in enumerate(V)]
    for c in range(n):
        piv=next(r for r in range(c,n) if A[r][c])
        A[c],A[piv]=A[piv],A[c]
        inv=pow(A[c][c],P-2,P)
        A[c]=[(x*inv)%P for x in A[c]]
        for r in range(n):
            if r!=c and A[r][c]:
                f_=A[r][c]; A[r]=[(A[r][k]-f_*A[c][k])%P for k in range(2*n)]
    Vinv=[row[n:] for row in A]
    f0=f(base)
    for k in range(npar):
        col=[]
        for t in ts:
            vec=base[:]; vec[k]+=t
            ft=f(vec)
            col.append([(ft[i]-f0[i])%P for i in range(35)])
        # linear coeff = sum_j Vinv[0][j]*col[j]
        row=[0]*35
        for j in range(5):
            for i in range(35): row[i]=(row[i]+Vinv[0][j]*col[j][i])%P
        rows.append(row)
    rk=0
    for c in range(35):
        piv=next((r for r in range(rk,len(rows)) if rows[r][c]),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        inv=pow(rows[rk][c],P-2,P); rows[rk]=[(x*inv)%P for x in rows[rk]]
        for r in range(len(rows)):
            if r!=rk and rows[r][c]:
                f_=rows[r][c]; rows[r]=[(rows[r][k]-f_*rows[rk][k])%P for k in range(35)]
        rk+=1
    return rk

# ---- k = 4: params = A1(16) + Phi(24); M_0(y) col j = sum_i y_i Phi[ij]
def unpack4(vec):
    A1=[vec[4*i:4*i+4] for i in range(4)]
    ph=vec[16:]
    Phi={}
    t=0
    for i in range(4):
        for j in range(i+1,4):
            Phi[(i,j)]=ph[4*t:4*t+4]; t+=1
    return A1,Phi
def build4(Phi):
    # Msym[i][p][q]: coefficient of y_i in entry (p,q); column q gets sum_i y_i Phi[i][q]
    Ms=[[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for q in range(4):
            if i==q: continue
            v=Phi[(min(i,q),max(i,q))]
            s=1 if i<q else -1
            for p_ in range(4): Ms[i][p_][q]=(Ms[i][p_][q]+s*v[p_])%P
    return Ms
# ---- k = 3: params = A1(16)+Phi3(12)+col4(16)+G(16)
def unpack3(vec):
    A1=[vec[4*i:4*i+4] for i in range(4)]
    ph=vec[16:28]
    Phi={}
    t=0
    for (i,j) in ((0,1),(0,2),(1,2)):
        Phi[(i,j)]=ph[4*t:4*t+4]; t+=1
    C4=[vec[28+4*i:28+4*i+4] for i in range(4)]     # col 4 = sum_i y_i C4[i]
    G=[vec[44+4*i:44+4*i+4] for i in range(4)]      # substitution y -> G y
    return A1,(Phi,C4,G)
def build3(rest):
    Phi,C4,G=rest
    Ms=[[[0]*4 for _ in range(4)] for _ in range(4)]   # in variable z (pre-subst)
    for i in range(3):
        for q in range(3):
            if i==q: continue
            v=Phi[(min(i,q),max(i,q))]
            s=1 if i<q else -1
            for p_ in range(4): Ms[i][p_][q]=(Ms[i][p_][q]+s*v[p_])%P
    for i in range(4):
        for p_ in range(4): Ms[i][p_][3]=(Ms[i][p_][3]+C4[i][p_])%P
    # substitute z = G y :  coeff of y_i = sum_m G[m][i] * Ms[m]
    My=[[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for m in range(4):
            g=G[m][i]%P
            if g:
                for p_ in range(4):
                    for q in range(4):
                        My[i][p_][q]=(My[i][p_][q]+g*Ms[m][p_][q])%P
    return My
r4=max(jrank(build4,unpack4,40,s) for s in (0,1))
print("stratum k=4 (primitive, Lambda^2 projection): rank %d of 35   session 32 says 25  %s"%(r4,"MATCH" if r4==25 else "*** DIFFERS ***"))
r3=max(jrank(build3,unpack3,60,s) for s in (0,1,2))
print("stratum k=3 (with the GL_4 substitution restored): rank %d of 35   session 32 says 27  %s"%(r3,"MATCH" if r3==27 else "*** DIFFERS ***"))
