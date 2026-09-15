#!/usr/bin/env python3
"""
B14-06 -- point families for the stable bracket evaluator, new code.

Every family produces the Proposition S stable point (g_2,g_3,g_4) in Z from an
integer construction on C^9, and hands the evaluator only the reduced data
(s_d, u_d, N_d) = value / gradient / Hessian of g_d at e_1.  All arithmetic is
exact mod p; jets are truncated at eta-degree 2 (module b14_06_bracket.Jet) and
vectorised over the whole batch with numpy int64 (p < 2^31 so a*b < 2^62).

    GEN  random (f_2,f_3,f_4) directly in Z
    DET  (e_2,e_3,e_4) of a traceless pencil A(s') = sum s_k A_k       -- Z_D = M_ell
    DETQ det(s_1 I + sum s'_k A_k) put through normalise+depress       -- control C8
    PAD  (x_0.per_3) composed with a linear L : C^9 -> C^10
    RED  ell . cubic
    NEG  four linear forms                                             -- forced rank 0

The normalise+depress map: for F with c = [s_1^4]F != 0, write
F/c = s_1^4 + g1 s_1^3 + g2 s_1^2 + g3 s_1 + g4 and substitute s_1 -> s_1 - g1/4:

    G2 = g2 - (3/8)g1^2
    G3 = g3 - (1/2)g1 g2 + (1/8)g1^3
    G4 = g4 - (1/4)g1 g3 + (1/16)g1^2 g2 - (3/256)g1^4

The (3/8) agrees with s57 Theorem P's own statement of the same coefficient.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"""
import itertools
import numpy as np

from b14_06_bracket import DEGS, Jet, inv_mod, _fl

NV = 8          # dim V'
AMB = 9         # ambient C^9 : s_1 (the c-direction) and V' = s_2..s_9


# --------------------------------------------------------------------- utilities
def _vander_inv(nodes, p):
    """inverse of V[t][k] = nodes[t]^(4-k), k=0..4  (so F(s1) = sum g_k s1^(4-k))."""
    V = [[pow(int(t), 4 - k, p) for k in range(5)] for t in nodes]
    return _fl(V, p).inv()


def _interp_s1(jets_by_s1, nodes, p, J):
    """jets_by_s1[t] = F(nodes[t], e_1+eta) -> g_0..g_4 as jets."""
    Vi = _vander_inv(nodes, p)
    g = []
    for k in range(5):
        acc = J.zero()
        for t in range(5):
            acc = (acc + int(Vi[k, t]) * jets_by_s1[t]) % p
        g.append(acc)
    return g


def normalise_depress(jets_by_s1, nodes, p, J):
    """(G2,G3,G4) jets, the scalar c per point, and the g_0-is-constant control."""
    g = _interp_s1(jets_by_s1, nodes, p, J)
    g0_eta_max = int(np.abs(g[0][1:]).max()) if g[0][1:].size else 0
    c = g[0][0] % p
    valid = (c % p) != 0          # c(F) = 0 puts the point outside W_c; dropped, and counted
    cinv = np.array([inv_mod(int(v), p) if int(v) % p else 1 for v in c], dtype=np.int64)
    gh = [(g[k] * cinv) % p for k in range(5)]
    g1, g2, g3, g4 = gh[1], gh[2], gh[3], gh[4]
    i8, i2, i4, i16, i256 = (inv_mod(8, p), inv_mod(2, p), inv_mod(4, p),
                             inv_mod(16, p), inv_mod(256, p))
    g1sq = J.mul(g1, g1)
    G2 = (g2 - 3 * i8 % p * g1sq) % p
    G3 = (g3 - i2 * J.mul(g1, g2) % p + i8 * J.mul(g1sq, g1) % p) % p
    G4 = (g4 - i4 * J.mul(g1, g3) % p + i16 * J.mul(g1sq, g2) % p
          - 3 * i256 % p * J.mul(g1sq, g1sq) % p) % p
    return {2: G2, 3: G3, 4: G4}, c, g0_eta_max, valid


def _lin_jet(coef, J, s1val, p):
    """coef[0]*s_1 + coef[1]*(1+eta_0) + sum_{k>=2} coef[k]*eta_{k-1};
    coef has shape (AMB, npts)."""
    z = J.zero()
    z[0] = (coef[0] * (s1val % p) + coef[1]) % p
    z[1] = coef[1] % p
    for k in range(2, AMB):
        z[1 + (k - 1)] = coef[k] % p
    return z


def _per3(M, J, p):
    tot = J.zero()
    for s in itertools.permutations(range(3)):
        t = J.mul(J.mul(M[0][s[0]], M[1][s[1]]), M[2][s[2]])
        tot = (tot + t) % p
    return tot


def _principal_minors(A, J, p, k):
    """sum of k x k principal minors of the 4x4 jet matrix A."""
    tot = J.zero()
    for idx in itertools.combinations(range(4), k):
        sub = [[A[i][j] for j in idx] for i in idx]
        tot = (tot + _det_jet(sub, J, p)) % p
    return tot


def _det_jet(M, J, p):
    n = len(M)
    tot = J.zero()
    for perm in itertools.permutations(range(n)):
        sign = 1
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    sign = -sign
        t = M[0][perm[0]]
        for i in range(1, n):
            t = J.mul(t, M[i][perm[i]])
        tot = (tot + sign * t) % p
    return tot


# --------------------------------------------------------------------- families
def family_GEN(npts, p, rng):
    """random (f_2,f_3,f_4) in Z, given as full coefficient dicts; jet read off."""
    J = Jet(NV, p, npts)
    jets = {}
    for d in DEGS:
        jet = J.zero()
        for alpha in itertools.product(range(d + 1), repeat=NV):
            if sum(alpha) != d:
                continue
            rest = sum(alpha[1:])
            cvec = rng.integers(0, p, npts).astype(np.int64)
            if rest > 2:
                continue                      # killed by the eta-truncation
            # monomial = (1+eta_0)^alpha_0 * prod_{k>=1} eta_k^{alpha_k}
            if rest == 0:
                jet[0] = (jet[0] + cvec) % p
                jet[1] = (jet[1] + alpha[0] * cvec) % p
                if alpha[0] >= 2:
                    jet[1 + NV + J.pix[(0, 0)]] = (jet[1 + NV + J.pix[(0, 0)]]
                                                   + alpha[0] * (alpha[0] - 1) // 2 * cvec) % p
            elif rest == 1:
                i = next(k for k in range(1, NV) if alpha[k] == 1)
                jet[1 + i] = (jet[1 + i] + cvec) % p
                jet[1 + NV + J.pix[(0, i)]] = (jet[1 + NV + J.pix[(0, i)]]
                                               + alpha[0] * cvec) % p
            else:
                ks = [k for k in range(1, NV) for _ in range(alpha[k])]
                i, j = ks[0], ks[1]
                key = (min(i, j), max(i, j))
                jet[1 + NV + J.pix[key]] = (jet[1 + NV + J.pix[key]] + cvec) % p
        jets[d] = jet
    return J, jets, {"valid": np.ones(npts, dtype=bool)}


def family_DET(npts, p, rng, A=None):
    """Z_D = M_ell verbatim: (e_2,e_3,e_4) of A(s') = sum_k s'_k A_k, A_k traceless.

    A_k is integral and traceless by construction (last diagonal entry fixed), so
    the point needs no normalisation and no depression: Proposition S's proof
    identifies exactly these with the depressed quartic's (g_2,g_3,g_4)."""
    J = Jet(NV, p, npts)
    if A is None:
        A = rng.integers(-50, 51, (NV, 4, 4, npts)).astype(np.int64)
        A[:, 3, 3] = -(A[:, 0, 0] + A[:, 1, 1] + A[:, 2, 2])
    Am = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            z = J.zero()
            z[0] = A[0, i, j] % p                 # value at e_1  (s'_0 = 1)
            for t in range(NV):
                z[1 + t] = A[t, i, j] % p         # d/d eta_t
            Am[i][j] = z
    jets = {2: _principal_minors(Am, J, p, 2),
            3: _principal_minors(Am, J, p, 3),
            4: _principal_minors(Am, J, p, 4)}
    return J, jets, {"A": A, "valid": np.ones(npts, dtype=bool)}


def family_DETQ(npts, p, rng, A=None, shift=None):
    """det(s_1 I + sum_k s'_k A_k) put through normalise+depress.

    Control C8: with A_k traceless and shift_k arbitrary, A'_k = A_k + shift_k.I
    has the same traceless part, so this must return the family_DET point of A
    EXACTLY.  A normalise/depress defect shows up as a mismatch."""
    J = Jet(NV, p, npts)
    nodes = [0, 1, 2, 3, 4]
    if A is None:
        A = rng.integers(-50, 51, (NV, 4, 4, npts)).astype(np.int64)
        A[:, 3, 3] = -(A[:, 0, 0] + A[:, 1, 1] + A[:, 2, 2])
    Ash = A.copy()
    if shift is not None:
        for t in range(NV):
            for i in range(4):
                Ash[t, i, i] = Ash[t, i, i] + shift[t]
    per_s1 = []
    for s1 in nodes:
        Am = [[None] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                z = J.zero()
                z[0] = (Ash[0, i, j] + (s1 if i == j else 0)) % p
                for t in range(NV):
                    z[1 + t] = Ash[t, i, j] % p
                Am[i][j] = z
        per_s1.append(_det_jet(Am, J, p))
    jets, c, g0eta, valid = normalise_depress(per_s1, nodes, p, J)
    return J, jets, {"A": A, "shift": shift, "c": c, "g0_eta_max": g0eta, "valid": valid}


def _linear_batch(nforms, npts, p, rng):
    return rng.integers(-50, 51, (nforms, AMB, npts)).astype(np.int64)


def family_PAD(npts, p, rng):
    """F = (x_0 o L) . per_3((x_1..x_9) o L), L : C^9 -> C^10 random integer."""
    J = Jet(NV, p, npts)
    nodes = [0, 1, 2, 3, 4]
    L = _linear_batch(10, npts, p, rng)
    per_s1 = []
    for s1 in nodes:
        Lj = [_lin_jet(L[t], J, s1, p) for t in range(10)]
        M = [[Lj[1 + 3 * a + b] for b in range(3)] for a in range(3)]
        per_s1.append(J.mul(Lj[0], _per3(M, J, p)))
    jets, c, g0eta, valid = normalise_depress(per_s1, nodes, p, J)
    return J, jets, {"L": L, "c": c, "g0_eta_max": g0eta, "valid": valid}


def family_RED(npts, p, rng):
    """F = ell . C with C a random cubic on C^9 (reducible quartics)."""
    J = Jet(NV, p, npts)
    nodes = [0, 1, 2, 3, 4]
    L0 = _linear_batch(1, npts, p, rng)[0]
    cubs = [a for a in itertools.product(range(4), repeat=AMB) if sum(a) == 3]
    Cc = rng.integers(-50, 51, (len(cubs), npts)).astype(np.int64)
    per_s1 = []
    for s1 in nodes:
        acc = J.zero()
        for m, alpha in enumerate(cubs):
            rest = sum(alpha[2:])
            if rest > 2:
                continue
            z = J.zero()
            z[0] = Cc[m] % p
            term = z
            for _ in range(alpha[0]):
                term = J.scal(term, s1 % p)
            for _ in range(alpha[1]):
                one_plus = J.zero(); one_plus[0] = 1; one_plus[1] = 1
                term = J.mul(term, one_plus)
            for k in range(2, AMB):
                for _ in range(alpha[k]):
                    e = J.zero(); e[1 + (k - 1)] = 1
                    term = J.mul(term, e)
            acc = (acc + term) % p
        per_s1.append(J.mul(_lin_jet(L0, J, s1, p), acc))
    jets, c, g0eta, valid = normalise_depress(per_s1, nodes, p, J)
    return J, jets, {"L0": L0, "c": c, "g0_eta_max": g0eta, "valid": valid}


def family_NEG(npts, p, rng):
    """F = l_1 l_2 l_3 l_4: negative_control_forced.  Any weight of more than
    four rows must read rank 0 on these."""
    J = Jet(NV, p, npts)
    nodes = [0, 1, 2, 3, 4]
    L = _linear_batch(4, npts, p, rng)
    per_s1 = []
    for s1 in nodes:
        t = _lin_jet(L[0], J, s1, p)
        for k in (1, 2, 3):
            t = J.mul(t, _lin_jet(L[k], J, s1, p))
        per_s1.append(t)
    jets, c, g0eta, valid = normalise_depress(per_s1, nodes, p, J)
    return J, jets, {"L": L, "c": c, "g0_eta_max": g0eta, "valid": valid}


FAMILIES = {"GEN": family_GEN, "DET": family_DET, "DETQ": family_DETQ,
            "PAD": family_PAD, "RED": family_RED, "NEG": family_NEG}
