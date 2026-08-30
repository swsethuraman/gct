"""A-priori (no I6 used): for each bidegree (a,b) with a+b<=6, the dimension of
the space of simultaneous-conjugation invariants of a 3x3 pencil that satisfy
the slab-equivariance  D_A f + 2 tr(A) f = D_B f + 2 tr(B) f = 0.

Careful point (found this session): the 10 trace words spanning bidegree (2,2)
are linearly DEPENDENT for 3x3 matrices (one relation, from the polarised
Cayley-Hamilton identity), so dimensions must be computed in FUNCTION space,
not coefficient space."""
import sympy as sp
from itertools import product

A = sp.Matrix(3,3, lambda i,j: sp.Symbol('a%d%d'%(i,j)))
B = sp.Matrix(3,3, lambda i,j: sp.Symbol('b%d%d'%(i,j)))
VARS = [A[i,j] for i,j in product(range(3),repeat=2)] + [B[i,j] for i,j in product(range(3),repeat=2)]
t = sp.trace
MAT = {'A': A, 'B': B}

def necklaces(a, b):
    """cyclic words in A,B with a A's and b B's, up to rotation (nonempty)."""
    seen, out = set(), []
    n = a + b
    for w in product('AB', repeat=n):
        if w.count('A') != a: continue
        rot = min(tuple(w[i:]+w[:i]) for i in range(n))
        if rot in seen: continue
        seen.add(rot); out.append(''.join(rot))
    return out

def multisets(a, b):
    """multisets of nonempty cyclic words with total multidegree (a,b)."""
    words = []
    for i in range(a+1):
        for j in range(b+1):
            if i+j == 0: continue
            for w in necklaces(i, j): words.append((w, i, j))
    res = []
    def rec(start, ra, rb, acc):
        if ra == 0 and rb == 0:
            res.append(tuple(acc)); return
        for k in range(start, len(words)):
            w, i, j = words[k]
            if i <= ra and j <= rb: rec(k, ra-i, rb-j, acc+[w])
    rec(0, a, b, [])
    return res

def value(ms):
    p = sp.Integer(1)
    for w in ms:
        M = sp.eye(3)
        for ch in w: M = M*MAT[ch]
        p = p*t(M)
    return sp.expand(p)

def deriv(f, dA, dB):
    s = 0
    for i,j in product(range(3),repeat=2):
        s += sp.diff(f, A[i,j])*dA[i,j] + sp.diff(f, B[i,j])*dB[i,j]
    return sp.expand(s)

def coeffvec(poly, monos):
    P = sp.Poly(poly, *VARS)
    d = P.as_dict()
    return [d.get(m, 0) for m in monos]

print(" (a,b)  #words  dim(conj-inv)  dim(equivariant)   generator")
table = {}
for a in range(7):
    for b in range(7-a):
        ms = multisets(a,b)
        if not ms:
            table[(a,b)] = (0,0,0,None); continue
        vals = [value(m) for m in ms]
        monos = sorted({m for v in vals for m in sp.Poly(v, *VARS).as_dict()})
        Mc = sp.Matrix([coeffvec(v, monos) for v in vals])
        dim_conj = Mc.rank()
        c = sp.symbols('c0:%d'%len(ms))
        f = sum(ci*vi for ci,vi in zip(c, vals))
        eqs = []
        for (dA,dB,tr_) in [(-A*A,-A*B,t(A)), (-B*A,-B*B,t(B))]:
            E = sp.expand(deriv(f,dA,dB) + 2*tr_*f)
            if E != 0: eqs += [sp.expand(x) for x in sp.Poly(E, *VARS).coeffs()]
        if eqs:
            Msys,_ = sp.linear_eq_to_matrix(eqs, c)
            ns = Msys.nullspace()
        else:
            ns = [sp.Matrix([1 if k==i else 0 for k in range(len(ms))]) for i in range(len(ms))]
        # function-space dimension of the equivariant solutions
        if ns:
            Fs = sp.Matrix([coeffvec(sp.expand(sum(v[i]*vals[i] for i in range(len(ms)))), monos)
                            for v in ns])
            dim_eq = Fs.rank()
        else:
            dim_eq = 0
        gen = None
        if dim_eq == 1:
            for v in ns:
                g = sp.expand(sum(v[i]*vals[i] for i in range(len(ms))))
                if g != 0:
                    gen = " + ".join("%s*%s"%(sp.nsimplify(v[i]), "".join("tr(%s)"%w for w in ms[i]))
                                     for i in range(len(ms)) if v[i]!=0)
                    break
        table[(a,b)] = (len(ms), dim_conj, dim_eq, gen)
        print("  (%d,%d)   %4d      %4d          %4d         %s" % (a,b,len(ms),dim_conj,dim_eq, (gen or '')[:90]))
