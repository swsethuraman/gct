"""Session 23: the point symmetry and orbit weights of X_{-3}.

A balanced substitution point N = E10 (x) A + E20 (x) B is a set of "arrows"
(block, position) <- (0, position).  A monomial symmetry of the point is a pair
(alpha, beta) in S3 x S3 acting on the 3x3 grid by (r,c) -> (alpha r, beta c);
it fixes det_3 up to sgn(alpha)sgn(beta) and preserves the point iff it
preserves the arrow set.  The induced action on the subproblem index is
pre-composition by rho = beta.  (Derivation validated below against the two
banked points C and R, whose recorded pi and rho it reproduces exactly.)

Combined with the two point-INDEPENDENT scheme automorphisms of session 12
(swap: (s6,s7) -> (s7,s6); post: (s6,s7) -> (s6 w, s7 w), w = (0 2)) this gives
the orbit decomposition of the 36 subproblems and hence the assembly weights.
"""
import itertools

perms = list(itertools.permutations((0,1,2)))
ix = {p:i for i,p in enumerate(perms)}
def comp(a,b): return tuple(a[b[i]] for i in range(3))
OM = (2,1,0)   # omega = (0 2)

def arrows(A,B):
    s=set()
    for i in range(3):
        for j in range(3):
            if A[i][j]: s.add(((1,i),(0,j)))
            if B[i][j]: s.add(((2,i),(0,j)))
    return frozenset(s)

def act(arr, alpha, beta):
    return frozenset((((alpha[t[0]], beta[t[1]]), (alpha[s[0]], beta[s[1]])))
                     for t,s in arr)

def symmetries(A,B):
    arr = arrows(A,B); out=[]
    for alpha in perms:
        for beta in perms:
            if (alpha,beta)==((0,1,2),(0,1,2)): continue
            if act(arr,alpha,beta)==arr: out.append((alpha,beta))
    return out

def pi_of(alpha,beta):
    """the induced permutation of the nine variables x_{3r+c}"""
    return tuple(3*alpha[k//3]+beta[k%3] for k in range(9))

def orbits(rho):
    def pre(s):  return (comp(rho,s[0]), comp(rho,s[1]))
    def post(s): return (comp(s[0],OM), comp(s[1],OM))
    def swap(s): return (s[1], s[0])
    seen=set(); out=[]
    for a in perms:
        for b in perms:
            if (a,b) in seen: continue
            orb=set(); st=[(a,b)]
            while st:
                x=st.pop()
                if x in orb: continue
                orb.add(x)
                for f in (pre,post,swap): st.append(f(x))
            seen|=orb; out.append(sorted(orb))
    W={}
    for orb in out:
        rep=min(6*ix[s[0]]+ix[s[1]] for s in orb)
        W["%02d"%rep]=len(orb)
    return W, out

def E(i,j):
    M=[[0]*3 for _ in range(3)]; M[i][j]=1; return M
def add(X,Y): return [[X[i][j]+Y[i][j] for j in range(3)] for i in range(3)]

BANKED = {
  'C'  : (E(2,1), E(1,2), (0,2,1,6,8,7,3,5,4), (0,2,1)),   # recorded pi, rho=(1 2)
  'R'  : (E(0,0), E(1,1), (1,0,2,7,6,8,4,3,5), (1,0,2)),   # recorded pi, rho=(0 1)
}
print("=== validation against the two banked points ===")
for name,(A,B,pi_rec,rho_rec) in BANKED.items():
    S = symmetries(A,B)
    hit = [(a,b) for a,b in S if pi_of(a,b)==pi_rec]
    print(f"{name}: symmetries {[(a,b) for a,b in S]}")
    print(f"   recorded pi {pi_rec} reproduced: {bool(hit)}"
          + (f" by (alpha,beta) = {hit[0]}, rho = beta = {hit[0][1]}"
             f" (recorded rho {rho_rec}: {'MATCH' if hit[0][1]==rho_rec else 'MISMATCH'})" if hit else ""))
    W,_ = orbits(rho_rec)
    print(f"   orbit weights from rho: {W}  (sum {sum(W.values())})")

print("\n=== X_{-3} ===")
A = add(E(0,2),E(1,1)); B = add(E(1,1),E(2,0))
S = symmetries(A,B)
print("monomial point symmetries (alpha,beta):", S)
for a,b in S:
    print("   pi =", pi_of(a,b), "  rho = beta =", b, "  sgn(alpha)sgn(beta) =",
          ( -1 if a in [(0,2,1),(1,0,2),(2,1,0)] else 1)*( -1 if b in [(0,2,1),(1,0,2),(2,1,0)] else 1))
if S:
    rho = S[0][1]
    W,orbs = orbits(rho)
    print("\nX_{-3} orbit weights:", W, " sum =", sum(W.values()))
    for orb in orbs:
        print("   rep %02d  size %d : %s" % (min(6*ix[s[0]]+ix[s[1]] for s in orb), len(orb),
              [ "%02d"%(6*ix[s[0]]+ix[s[1]]) for s in sorted(orb, key=lambda s:6*ix[s[0]]+ix[s[1]])]))
print("\n=== control: orbits using ONLY the point-independent scheme automorphisms ===")
Wid,_ = orbits((0,1,2))
print(Wid, " sum =", sum(Wid.values()), " (", len(Wid), "runs if no point symmetry is assumed )")
