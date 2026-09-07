from fractions import Fraction as F
import random
random.seed(7)

def mat(n,m,lo=-6,hi=6): return [[F(random.randint(lo,hi)) for _ in range(m)] for _ in range(n)]
def T(A): return [list(r) for r in zip(*A)]
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det(A):
    A=[r[:] for r in A]; n=len(A); d=F(1)
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]!=0), None)
        if p is None: return F(0)
        if p!=c: A[c],A[p]=A[p],A[c]; d=-d
        d*=A[c][c]
        for i in range(c+1,n):
            f=A[i][c]/A[c][c]
            for k in range(c,n): A[i][k]-=f*A[c][k]
    return d
def solve(A,b):
    n=len(A); M=[A[i][:]+[b[i]] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c]!=0); M[c],M[p]=M[p],M[c]
        for i in range(n):
            if i!=c and M[i][c]!=0:
                f=M[i][c]/M[c][c]
                for k in range(c,n+1): M[i][k]-=f*M[c][k]
    return [M[i][n]/M[i][i] for i in range(n)]

a, tgt = 5, 12            # source dim a_delta = 5, transported predecessor = first 4
Tmap = mat(tgt, a)        # Theta_delta on M_delta, in a basis adapted to J(M_{delta-1}) + <v>
B = mul(T(Tmap), Tmap)                     # full current-degree Gram, a x a
A = [row[:a-1] for row in B[:a-1]]         # CURRENT-degree Gram restricted to J(M_{delta-1})
b = [B[i][a-1] for i in range(a-1)]
c = B[a-1][a-1]
x = solve(A,b)
s_schur = c - sum(b[i]*x[i] for i in range(a-1))

# (i) Schur complement equals det B / det A
s_ratio = det(B)/det(A)

# (ii) Schur complement equals the squared distance ||(I-P)T(v)||^2
Tv = [Tmap[i][a-1] for i in range(tgt)]
cols = [[Tmap[i][j] for i in range(tgt)] for j in range(a-1)]
coef = solve(A, [sum(cols[j][i]*Tv[i] for i in range(tgt)) for j in range(a-1)])
resid = [Tv[i] - sum(coef[j]*cols[j][i] for j in range(a-1)) for i in range(tgt)]
s_dist = sum(r*r for r in resid)

# (iii) the PREVIOUS-degree Gram is a different matrix: Theta_{delta-1} has its own target
Tprev = mat(9, a-1)                        # Theta_{delta-1} on M_{delta-1}, different target
G_prev = mul(T(Tprev), Tprev)
s_wrong = det(B)/det(G_prev)

print("s  = c - b^T A^{-1} b        =", s_schur)
print("     det B / det A           =", s_ratio, "   agree:", s_schur==s_ratio)
print("     ||(I-P)T(v)||^2         =", s_dist,  "   agree:", s_schur==s_dist)
print()
print("det B / det G_prev  (my earlier phrasing) =", s_wrong)
print("   equals s ?", s_wrong==s_schur)
print()
print("A  (current-degree Gram on the transported subspace) =", [[str(y) for y in r] for r in A])
print("G_prev (previous-degree Gram, own target)            =", [[str(y) for y in r] for r in G_prev])
