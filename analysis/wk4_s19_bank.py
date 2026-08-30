"""Step 6: banked cross-check + machinery invariance checks."""
import numpy as np, sympy as sp, sys
sys.path.insert(0,'analysis')
from wk4_s19_fast import all_values
PAT=(1,5)
def I6(T): return all_values(np.array(T,dtype=np.int64))[PAT]

# --- SL3^3 semi-invariance with character det^2 (machinery check) ---
rng = np.random.default_rng(9)
def rand_uni():
    M = np.eye(3, dtype=np.int64)
    for _ in range(6):
        i,j = rng.choice(3,2,replace=False); M[i] += rng.integers(-2,3)*M[j]
    return M
T = rng.integers(-4,5,size=(3,3,3)).astype(np.int64)
base = I6(T)
ok = True
for slot in range(3):
    g = rand_uni()                       # det 1
    Tg = np.tensordot(g, T, axes=([1],[slot]))
    Tg = np.moveaxis(Tg, 0, slot)
    ok &= (I6(Tg) == base)
print("SL3 invariance in each of the 3 slots:", ok)
for slot in range(3):
    lam = 2
    Tg = T.copy().astype(object)
    Tg = np.moveaxis(np.moveaxis(T,slot,0)*lam, 0, slot).astype(np.int64)
    print("  slot %d scaled by 2: ratio = %s  (det(2I)^2 = 64)" % (slot, I6(Tg)//base if base else None))

# --- banked nets ---
def E(i,j):
    M = np.zeros((3,3),dtype=np.int64); M[i,j]=1; return M
def dg(*d): return np.diag(np.array(d,dtype=np.int64))
I3 = np.eye(3,dtype=np.int64)
def net(A,B):
    T = np.zeros((3,3,3),dtype=np.int64); T[0]=I3; T[1]=A; T[2]=B; return T
def psi(A,B):
    A,B = sp.Matrix(3,3,[int(x) for x in np.array(A).reshape(-1)]), sp.Matrix(3,3,[int(x) for x in np.array(B).reshape(-1)]); t=sp.trace
    u1=t(A*A)*t(B*B)-t(A*B)**2; u2=t(A*A*B*B)-t(A*B*A*B)
    D=(t(A)*t(B)-t(A*B))**2-(t(A)**2-t(A*A))*(t(B)**2-t(B*B))
    return sp.expand(2*u1-4*u2-D)

TC = 1152144000
PTS = [
 ('C   cyclic pencil      ', E(2,1), E(1,2),                 TC),
 ('R   DD pencil          ', E(0,0), E(1,1),                 TC),
 ('T4  invertible-containing', dg(1,1,0), dg(0,1,1),         None),
 ('Q   H-translate of C   ', E(1,0), E(0,1),                 None),
 ('X4                     ', E(0,0), E(1,2)+E(2,1),          4*TC),
 ('Xm3                    ', E(0,2)+E(1,1), E(1,1)+E(2,0),   None),
 ('P   rank-1 (compression)', E(0,0), E(0,0),                0),
 ('Y2  B = I (compression) ', E(2,1), I3,                    0),
 ('Y4  AB=0, A+B=I        ', dg(1,0,0), dg(0,1,1),           0),
 ('N=0                    ', 0*I3, 0*I3,                     0),
]
print("\n point                      Psi   I6(I,A,B)   I6/(-6)  banked TOTAL      Psi*TOTAL_C")
for name,A,B,tot in PTS:
    A=np.array(A,dtype=np.int64); B=np.array(B,dtype=np.int64)
    v = I6(net(A,B)); p = psi(A,B)
    print("  %-26s %4s %10s %8s   %-15s %s" % (name, p, v, sp.Rational(v,-6), tot if tot is not None else 'not run', p*TC))
