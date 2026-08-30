"""Symbolic closure of session 19:
 (a) I6 on the GENERIC 3x3x3 tensor -- term count, to be matched against the
     1152 terms reported for the Aronhold I6 by Bremner-Hu (Math. Comp. 2013);
 (b) I6 restricted to slabs (I,A,B) as an EXACT polynomial identity in the 18
     pencil entries, compared with Psi."""
import sympy as sp, numpy as np, sys
from itertools import permutations, product
sys.path.insert(0,'analysis')
from wk4_s19_fast import PARTS, axes

PERM3 = []
for p in permutations(range(3)):
    s = 1
    q = list(p)
    for i in range(3):
        for j in range(i+1,3):
            if q[i] > q[j]: s = -s
    PERM3.append((p, s))

def sym_I6(T, P2, P3):
    """T[s][p][q] sympy expressions.  Two-stage contraction, symbolic."""
    H = {}
    for j0,k0,j1,k1,j2,k2 in product(range(3), repeat=6):
        acc = 0
        for p, s in PERM3:
            acc += s*T[p[0]][j0][k0]*T[p[1]][j1][k1]*T[p[2]][j2][k2]
        H[(j0,k0,j1,k1,j2,k2)] = sp.expand(acc)
    tot = 0
    for (pa, sa) in PERM3:            # slot-2, block A
      for (pb, sb) in PERM3:          # slot-2, block B
        for (pc, sc) in PERM3:        # slot-3, block A
          for (pd, sd) in PERM3:      # slot-3, block B
            idx = {}
            for slot, P, (pu, pv) in ((0, P2, (pa, pb)), (1, P3, (pc, pd))):
                for blk, perm in zip(P, (pu, pv)):
                    for pos, c in enumerate(blk): idx[(c, slot)] = perm[pos]
            key1 = tuple(idx[(c,s)] for c in (0,1,2) for s in (0,1))
            key2 = tuple(idx[(c,s)] for c in (3,4,5) for s in (0,1))
            tot += sa*sb*sc*sd*H[key1]*H[key2]
    return sp.expand(tot)

PAT = (1,5); P2, P3 = PARTS[1], PARTS[5]

# ---- (a) generic tensor ----
Tg = [[[sp.Symbol('t%d%d%d'%(s,p,q)) for q in range(3)] for p in range(3)] for s in range(3)]
G = sym_I6(Tg, P2, P3)
nt = len(sp.Poly(G, *[Tg[s][p][q] for s in range(3) for p in range(3) for q in range(3)]).as_dict())
print("I6 on the generic 3x3x3 tensor: %d monomials" % nt)
print("  Bremner-Hu report 1152 terms for the Aronhold I6 -> match:", nt == 1152)
cs = [abs(c) for c in sp.Poly(G, *[Tg[s][p][q] for s in range(3) for p in range(3) for q in range(3)]).coeffs()]
from collections import Counter
print("  |coefficient| histogram:", Counter(cs))
g = sp.gcd(list(sp.Poly(G, *[Tg[s][p][q] for s in range(3) for p in range(3) for q in range(3)]).coeffs()))
print("  content (gcd of coefficients):", g)

# numeric cross-check of the symbolic route against the fast evaluator
from wk4_s19_fast import all_values
rng = np.random.default_rng(4)
Tn = rng.integers(-5,6,size=(3,3,3)).astype(np.int64)
sub = {Tg[s][p][q]: int(Tn[s,p,q]) for s in range(3) for p in range(3) for q in range(3)}
print("  symbolic == fast evaluator at a random tensor:",
      int(G.subs(sub)) == all_values(Tn)[PAT])

# ---- (b) restriction to slabs (I,A,B) ----
Am = sp.Matrix(3,3, lambda i,j: sp.Symbol('a%d%d'%(i,j)))
Bm = sp.Matrix(3,3, lambda i,j: sp.Symbol('b%d%d'%(i,j)))
Ts = [[[sp.Integer(1 if p==q else 0) for q in range(3)] for p in range(3)],
      [[Am[p,q] for q in range(3)] for p in range(3)],
      [[Bm[p,q] for q in range(3)] for p in range(3)]]
R = sym_I6(Ts, P2, P3)
t = sp.trace
u1 = t(Am*Am)*t(Bm*Bm) - t(Am*Bm)**2
u2 = t(Am*Am*Bm*Bm) - t(Am*Bm*Am*Bm)
D  = (t(Am)*t(Bm)-t(Am*Bm))**2 - (t(Am)**2-t(Am*Am))*(t(Bm)**2-t(Bm*Bm))
PSI = sp.expand(2*u1 - 4*u2 - D)
print("\nEXACT SYMBOLIC IDENTITY  I6(I,A,B) == -6*Psi(A,B) :",
      sp.expand(R + 6*PSI) == 0)
VARS = [Am[i,j] for i,j in product(range(3),repeat=2)]+[Bm[i,j] for i,j in product(range(3),repeat=2)]
PR = sp.Poly(R, *VARS)
degs = {(sum(m[:9]), sum(m[9:])) for m in PR.as_dict()}
print("bidegrees actually occurring in I6|(I,A,B):", sorted(degs))
print("  (structural reason: each slot-1 epsilon needs three DISTINCT slab")
print("   indices, so each of the two 3-blocks uses I, A and B exactly once)")
