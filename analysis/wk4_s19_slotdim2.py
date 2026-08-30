import sys; sys.setrecursionlimit(10000)
exec(open('analysis/wk4_s19_slotdim.py').read().split('print(" (a,b)')[0])
import sympy as sp
CELLS = [(2,2),(2,3),(3,3),(2,4)]
for (a,b) in CELLS:
    ms = multisets(a,b); vals=[value(m) for m in ms]
    monos = sorted({m for v in vals for m in sp.Poly(v,*VARS).as_dict()})
    Mc = sp.Matrix([coeffvec(v,monos) for v in vals]); dim_conj = Mc.rank()
    c = sp.symbols('c0:%d'%len(ms)); f = sum(ci*vi for ci,vi in zip(c,vals))
    eqs=[]
    for (dA,dB,tr_) in [(-A*A,-A*B,t(A)),(-B*A,-B*B,t(B))]:
        E = sp.expand(deriv(f,dA,dB)+2*tr_*f)
        if E!=0: eqs += [sp.expand(x) for x in sp.Poly(E,*VARS).coeffs()]
    Msys,_ = sp.linear_eq_to_matrix(eqs,c); ns = Msys.nullspace()
    Fs = sp.Matrix([coeffvec(sp.expand(sum(v[i]*vals[i] for i in range(len(ms)))),monos) for v in ns]) if ns else sp.zeros(1,1)
    dim_eq = Fs.rank() if ns else 0
    print("(%d,%d): #words %d  dim_conj %d  dim_equivariant %d"%(a,b,len(ms),dim_conj,dim_eq), flush=True)
    if (a,b)==(2,2) and dim_eq==1:
        u1 = t(A*A)*t(B*B)-t(A*B)**2; u2 = t(A*A*B*B)-t(A*B*A*B)
        D  = (t(A)*t(B)-t(A*B))**2-(t(A)**2-t(A*A))*(t(B)**2-t(B*B))
        PSI = sp.expand(2*u1-4*u2-D)
        for v in ns:
            g = sp.expand(sum(v[i]*vals[i] for i in range(len(ms))))
            if g==0: continue
            r = sp.simplify(sp.expand(PSI*sp.Rational(1,1)) - sp.Rational(1,1)*g)
            # find scalar lam with PSI = lam*g
            lam = None
            pv = sp.Poly(PSI,*VARS).as_dict(); gv = sp.Poly(g,*VARS).as_dict()
            k0 = next(iter(gv)); lam = sp.Rational(pv.get(k0,0), gv[k0])
            print("   generator matches Psi up to scale:", sp.expand(PSI - lam*g)==0, " lambda =", lam, flush=True)
            break
