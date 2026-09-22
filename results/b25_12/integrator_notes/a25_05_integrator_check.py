import itertools, sympy as sp
X = sp.symbols('x1:6')
mons4 = [e for e in itertools.product(range(5), repeat=5) if sum(e)==4]
mons3 = [e for e in itertools.product(range(4), repeat=5) if sum(e)==3]
print("dim Sym^4 =", len(mons4), " dim Sym^3 =", len(mons3))
# 1. retained dims: exponent >=2 in some x_i, i<m
for m in (3,4,5):
    J = [e for e in mons4 if any(e[i]>=2 for i in range(m))]
    print(f"m={m}: dim J_m={len(J)} (claim {15*m-m*(m-1)//2}), omitted={70-len(J)}")
# 2. fibre kernel of C -> pi_m(l*C), l = sum_{i in sel} x_i (a_i!=0 on r of the m centers) + unselected vars
def kernel_dim(m, r):
    l = sum(X[i] for i in range(r)) + sum(X[i] for i in range(m,5))
    retained = [e for e in mons4 if any(e[i]>=2 for i in range(m))]
    cols=[]
    for e in mons3:
        C = sp.Mul(*[X[i]**e[i] for i in range(5)])
        P = sp.Poly(sp.expand(l*C), *X)
        cols.append([P.coeff_monomial(sp.Mul(*[X[i]**f[i] for i in range(5)])) for f in retained])
    M = sp.Matrix(cols).T
    return 35 - M.rank()
t=sp.symbols('t')
def formula(m,r):
    return sp.series((1+t)**(m-r)/(1-t)**(5-m), t, 0, 5).removeO().coeff(t,3)
for (m,r) in [(3,3),(4,4),(5,5),(5,2),(5,3),(4,2),(3,1)]:
    print(f"m={m} r={r}: kernel dim computed={kernel_dim(m,r)}  formula={formula(m,r)}")
# 3. six-term identity
a,b,c = [sp.Add(*[sp.Symbol(f'{n}{i}')*X[i] for i in range(5)]) for n in 'abc']
z,d,e,f = X[0],X[1],X[2],X[3]
S = sp.Matrix([[a,d,e],[d,b,f],[e,f,c]])
per = sum(sp.Mul(*[S[i,p[i]] for i in range(3)]) for p in itertools.permutations(range(3)))
M = sp.Matrix([[a,d,e],[-d,b,f],[-e,-f,c]])
lhs = sp.expand(z*per - z*M.det())
print("six-term identity z*per - det diag(z,M) =", sp.factor(lhs), " | equals 2x1x2x3x4:", sp.simplify(lhs-2*X[0]*X[1]*X[2]*X[3])==0)
