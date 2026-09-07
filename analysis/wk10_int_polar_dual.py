from math import comb
from itertools import product

def segre_polar(a,b):
    """classical polar classes mu_0..mu_d of the Segre P^a x P^b in P^{(a+1)(b+1)-1}"""
    d=a+b
    # Chow ring: h1^i h2^j, i<=a, j<=b ; integral = coeff of h1^a h2^b
    def mul(X,Y):
        Z={}
        for (i,j),c in X.items():
            for (k,l),e in Y.items():
                if i+k<=a and j+l<=b: Z[(i+k,j+l)]=Z.get((i+k,j+l),0)+c*e
        return Z
    def power(X,n):
        R={(0,0):1}
        for _ in range(n): R=mul(R,X)
        return R
    h={(1,0):1,(0,1):1}
    # total Chern class (1+h1)^{a+1} (1+h2)^{b+1}
    c1={(1,0):1}; c2={(0,1):1}
    C=mul(power({(0,0):1,**c1},a+1), power({(0,0):1,**c2},b+1))
    C.setdefault((0,0),1)
    ci=[{k:v for k,v in C.items() if k[0]+k[1]==i} for i in range(d+1)]
    def deg(X): return X.get((a,b),0)
    mu=[]
    for k in range(d+1):
        s=0
        for i in range(k+1):
            if d-i+1 < k-i or k-i<0: continue
            s += (-1)**i * comb(d-i+1,k-i) * deg(mul(ci[i], power(h,d-i)))
        mu.append(s)
    return mu

for (a,b,name,banked) in [(3,3,'det_4',(4,12,36,68,84,60,20)), (4,4,'det_5',None)]:
    mu=segre_polar(a,b)
    prof=tuple(reversed(mu))
    print("Segre P^%d x P^%d : deg = %d , polar classes mu = %s"%(a,b,mu[0],mu))
    print("  => %s polar profile (reverse, biduality) = %s"%(name,prof))
    if banked: print("     banked det_4 profile                  = %s   %s"%(banked, "MATCH" if prof==banked else "MISMATCH"))
    print()
print("S5 reports det_5 profile = (5,20,80,220,430,580,520,280,70)")
