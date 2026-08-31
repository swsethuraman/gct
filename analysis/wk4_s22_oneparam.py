"""Session 22: the one-parameter slab subgroups and the functional equation."""
import sympy as sp, random
from wk4_s22_dict import (h_elt, chi, Psi, transport, graph_normalise,
                          net_rows, rand_pencil)

t = sp.symbols('t')
a_ = sp.symbols('a0:9'); b_ = sp.symbols('b0:9')
A = sp.Matrix(3,3, lambda i,j: a_[3*i+j]); B = sp.Matrix(3,3, lambda i,j: b_[3*i+j])
I3 = sp.eye(3)

def induced_net(A, B, alpha, beta):
    a = alpha.inv().T; b = beta.inv().T
    Rp = net_rows(A, B) * h_elt(a, b).inv()
    Ap, Bp, G = graph_normalise(Rp)
    return sp.simplify(Ap), sp.simplify(Bp), sp.cancel(sp.simplify(G.det()))

print("=== 6. slab one-parameter subgroup  slab_0 -> slab_0 + t*slab_1 ===")
alpha = sp.Matrix([[1, t, 0],[0,1,0],[0,0,1]])
Ap, Bp, dG = induced_net(A, B, alpha, I3)
g = I3 + t*A
print("  A' == A (I+tA)^-1 == (I+tA)^-1 A :",
      sp.simplify(Ap - A*g.inv()) == sp.zeros(3,3), sp.simplify(Ap - g.inv()*A) == sp.zeros(3,3))
print("  B' == B (I+tA)^-1 :", sp.simplify(Bp - B*g.inv()) == sp.zeros(3,3),
      " | B' == (I+tA)^-1 B :", sp.simplify(Bp - g.inv()*B) == sp.zeros(3,3))
print("  det G =", sp.factor(dG), "   det(I+tA) =", sp.factor(g.det()))
print("  det G == det(I+tA)^-1 :", sp.simplify(dG*g.det() - 1) == 0)
print("  => chi = det(G)^-2 = det(I+tA)^2")
print("  NOTE the right/left discrepancy with the session-18 record is a conjugation:")
print("       (g^-1 X g) applied to (A g^-1, B g^-1) gives ((I+tA)^-1 A, (I+tA)^-1 B):",
      sp.simplify(g.inv()*(B*g.inv())*g - g.inv()*B) == sp.zeros(3,3))

print()
print("=== 7. b-side subgroup: pure conjugation, chi = 1 ===")
beta = sp.Matrix([[1, t, 0],[0,1,0],[0,0,1]])
Ap2, Bp2, dG2 = induced_net(A, B, I3, beta)
print("  A' == beta^T A beta^-T :", sp.simplify(Ap2 - beta.T*A*beta.T.inv()) == sp.zeros(3,3),
      " B' :", sp.simplify(Bp2 - beta.T*B*beta.T.inv()) == sp.zeros(3,3),
      "  det G =", sp.simplify(dG2))

print()
print("=== 8. THE FUNCTIONAL EQUATION as a polynomial identity (18 indets + t) ===")
adj = g.adjugate()
lhs = sp.expand(Psi(A*adj, B*adj) - g.det()**2 * Psi(A, B))
print("  Psi(A adj(g), B adj(g)) - det(g)^2 Psi(A,B) == 0 :", lhs == 0)
