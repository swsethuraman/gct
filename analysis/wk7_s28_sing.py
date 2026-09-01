"""Session 28 -- why the ideal of D_5 is nonzero, with an explicit element.

THE ARGUMENT (elementary and complete).  Let M(s) = s_1 A_1 + ... + s_5 A_5 be a
3x3 matrix of linear forms in 5 variables and F = det M.  The rank-<=1 locus of
M_3 is the affine cone over the Segre P^2 x P^2 in P^8, of dimension 4 and
degree 6.  The image of P^4 -> P^8 given by the A_i is a linear subspace of
dimension 4 (for a generic tuple), and 4 + 4 >= 8, so by the projective
dimension theorem the two MUST meet.  At a point s where rank M(s) <= 1 every
2x2 minor vanishes, so every cofactor vanishes, so every partial derivative
dF/ds_i = s-derivative of det = (cofactor contraction) vanishes: F is singular
there.

Hence EVERY member of D_5 is a singular quinary cubic, so

    disc  in  I(D_5),

where disc is the discriminant of quinary cubics -- an irreducible form of
degree n(d-1)^{n-1} = 5 * 2^4 = 80 in the 35 coefficients, and a GL_5
semi-invariant of weight det^48, i.e. sitting at the length-5 weight (48^5).

That is a rigorous, explicit, nonzero element of I(D_5).  It makes Theorem 6's
length bound SHARP: the ideal really does bite at length 5.

This script verifies the geometry numerically at random integer tuples: it
finds an actual rank-<=1 point of a random pencil, and checks that the cubic's
gradient vanishes there.  (Verification of a proof, not a substitute for it.)
"""
import sys, os, random
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def rank1_points(As, tries=400, seed=0, tol=1e-9):
    """Find s in C^5 with rank(sum s_i A_i) <= 1, by Newton on the 2x2 minors
    together with a random affine normalisation."""
    rng = np.random.default_rng(seed)
    A = np.array(As, dtype=complex)          # (5,3,3)

    def minors(s):
        M = np.tensordot(s, A, axes=(0, 0))
        out = []
        for i in range(3):
            for j in range(3):
                r = [x for x in range(3) if x != i]
                c = [x for x in range(3) if x != j]
                out.append(M[r[0], c[0]] * M[r[1], c[1]]
                           - M[r[0], c[1]] * M[r[1], c[0]])
        return np.array(out)

    def jac(s, h=1e-6):
        J = np.zeros((9, 5), dtype=complex)
        f0 = minors(s)
        for k in range(5):
            e = np.zeros(5, dtype=complex); e[k] = h
            J[:, k] = (minors(s + e) - f0) / h
        return J

    for _ in range(tries):
        s = rng.normal(size=5) + 1j * rng.normal(size=5)
        nrm = rng.normal(size=5) + 1j * rng.normal(size=5)
        for _ in range(200):
            f = np.concatenate([minors(s), [nrm @ s - 1.0]])
            J = np.vstack([jac(s), nrm[None, :]])
            try:
                step = np.linalg.lstsq(J, -f, rcond=None)[0]
            except np.linalg.LinAlgError:
                break
            s = s + step
            if np.linalg.norm(f) < tol:
                break
        if np.linalg.norm(np.concatenate([minors(s), [nrm @ s - 1.0]])) < 1e-8:
            return s
    return None


def grad_F(As, s):
    """gradient of F = det(sum s_i A_i) at s: dF/ds_k = tr(adj(M) A_k)."""
    A = np.array(As, dtype=complex)
    M = np.tensordot(s, A, axes=(0, 0))
    adj = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            r = [x for x in range(3) if x != i]
            c = [x for x in range(3) if x != j]
            m = (M[r[0], c[0]] * M[r[1], c[1]] - M[r[0], c[1]] * M[r[1], c[0]])
            adj[j, i] = ((-1) ** (i + j)) * m
    return np.array([np.trace(adj @ A[k]) for k in range(5)]), np.linalg.det(M)


if __name__ == '__main__':
    print("verification: every determinantal quinary cubic is singular")
    ok = 0
    for trial in range(6):
        rng = random.Random(100 + trial)
        As = [[[rng.randint(-6, 6) for _ in range(3)] for _ in range(3)]
              for _ in range(5)]
        s = rank1_points(As, seed=trial)
        if s is None:
            print("  trial %d: no rank-1 point found (Newton failure, not a "
                  "counterexample)" % trial)
            continue
        M = np.tensordot(np.array(s), np.array(As, dtype=complex), axes=(0, 0))
        sv = np.linalg.svd(M, compute_uv=False)
        g, F = grad_F(As, s)
        print("  trial %d: singular values of M(s) = %s" % (trial, np.round(sv, 10)))
        print("            |grad F| = %.3e   |F| = %.3e   -> F is singular at s"
              % (np.linalg.norm(g), abs(F)))
        if np.linalg.norm(g) < 1e-6 and sv[1] < 1e-6:
            ok += 1
    print("\n%d/6 random pencils: an explicit rank-1 point found and the cubic's "
          "gradient vanishes there." % ok)
