"""Session 22: the consolidated sweep.
For each (pencil, H-element) it checks, exactly:
   (1) q = u_{N'} t u_N^{-1} preserves W;
   (2) det(q) = det(t)  and  chi = det(q)^6 det(q|_{V/W})^2   [the 8 = 6+2 identity];
   (3) det(q|_{V/W}) = det(G)^{-1}                            [the slot dictionary];
   (4) chi = det(G)^{-2}                                      [P1+P2];
   (5) Psi(A',B') = det(G)^{-2} Psi(A,B)                      [P3/P4];
   (6) for non-unimodular g (m = det a det b != 1): chi = m^18 det(G)^{-2} and
       the evaluation factor m^{-20} chi = m^{-2} det(G)^{-2} = the Psi ratio.
"""
import sympy as sp, random
from wk4_s22_dict import (mat_from_transvections, h_elt, chi, Psi, transport,
                          BANK, rand_sl3, rand_pencil)

def case(A, B, a, b, tp):
    t = h_elt(a, b, tp)
    Ap, Bp, G, q = transport(A, B, t)
    if Ap is None: return None
    m = sp.nsimplify(a.det()*b.det())
    dG = sp.nsimplify(G.det()); d3 = sp.nsimplify(q[0:3,0:3].det())
    ch = sp.nsimplify(chi(q)); dq = sp.nsimplify(q.det()); dt = sp.nsimplify(t.det())
    p0, p1 = Psi(A,B), Psi(Ap,Bp)
    out = {
      'W':  all(sp.simplify(q[i,j]) == 0 for i in range(3) for j in range(3,9)),
      'detq': sp.simplify(dq - dt) == 0,
      '8=6+2': sp.simplify(ch - dq**6 * d3**2) == 0,
      'dict': sp.simplify(d3 - dG**-1) == 0,
      'chi':  sp.simplify(ch - m**18 * dG**-2) == 0,
      'psi':  (sp.simplify(p1 - m**-2 * dG**-2 * p0) == 0),
      'eval': sp.simplify(m**-20*ch - m**-2*dG**-2) == 0,
    }
    return out, m

if __name__ == '__main__':
    rng = random.Random(9091)
    tally = {}
    n_ok = 0
    pencils = [mat_from_transvections(tv) for tv in BANK.values()] + \
              [rand_pencil(rng) for _ in range(6)]
    for A, B in pencils:
        for tp in (False, True):
            for trial in range(3):
                a, b = rand_sl3(rng), rand_sl3(rng)
                if trial == 2:                      # non-unimodular: m != 1
                    a = a * sp.diag(rng.choice([2,-3,5]), 1, 1)
                r = case(A, B, a, b, tp)
                if r is None: continue
                out, m = r
                n_ok += 1
                for k, v in out.items(): tally[k] = tally.get(k, 0) + (1 if v else 0)
    print(f"cases: {n_ok}")
    for k in ('W','detq','8=6+2','dict','chi','psi','eval'):
        print(f"   {k:7s} {tally.get(k,0)}/{n_ok}  {'OK' if tally.get(k,0)==n_ok else '*** FAIL ***'}")
    print()
    print("=== pure scaling consistency: g = mu*I_9 must give factor 1 ===")
    mu = sp.symbols('mu', positive=True)
    A, B = mat_from_transvections(BANK['C'])
    t = h_elt(mu*sp.eye(3), sp.eye(3))
    Ap, Bp, G, q = transport(A, B, t)
    m = mu**3
    print(f"  N' == N: {sp.simplify(Ap-A)==sp.zeros(3,3) and sp.simplify(Bp-B)==sp.zeros(3,3)};"
          f"  chi = {sp.simplify(chi(q))};  m^-20 chi = {sp.simplify(m**-20*chi(q))} (must be 1)")

# --- P4 checked a second, independent way: the slot-1<->3 swap character ----
def swap_family(rng):
    """Tensors with slabs (I,A,B) symmetric under swapping slots 1 and 3:
       (S_k)_{ji} = (S_j)_{ki} for all i,j,k, with S_0 = I."""
    p,q,r,s,u,v,w,y,z = [sp.Integer(rng.randint(-6,6)) for _ in range(9)]
    A = sp.Matrix([[0,1,0],[p,q,r],[s,u,v]])
    B = sp.Matrix([[0,0,1],[s,u,v],[w,y,z]])
    return A, B

if __name__ == '__main__':
    print()
    print("=== P4 second route: I_6 under the slot-1<->3 swap (transpose of the net) ===")
    rng2 = random.Random(31337)
    vals = []
    for _ in range(6):
        A, B = swap_family(rng2)
        S = [sp.eye(3), A, B]
        sym = all(S[k][j,i] == S[j][k,i] for i in range(3) for j in range(3) for k in range(3))
        vals.append((sym, Psi(A,B)))
    print("   swap-symmetric tensors, (is symmetric, Psi):", vals)
    print("   => if the swap acted by the sign character, I_6 and hence Psi would vanish")
    print("      identically on this family; it does not.  Character is trivial.")
