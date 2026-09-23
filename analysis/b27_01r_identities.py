"""R27-01 exact symbolic check of the four determinant identities B27-01 uses, over
Q(s) or Q[u]/(u^2-2), with fully generic symbols.  No numerics, no sampling."""
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b27_01r_cap import run  # noqa: E402


def per3(M):
    import itertools as it
    return sp.expand(sum(M[0][s[0]] * M[1][s[1]] * M[2][s[2]] for s in it.permutations(range(3))))


def body():
    out = {'status': 'PASS', 'label': 'COMPUTED'}
    a, b, c, d, e, f, g, h, l, u, s = sp.symbols('a b c d e f g h l u s')
    # (1) A33 = 0: per = det with two sign flips (report 1a).
    lhs = per3([[a, b, c], [d, e, f], [g, h, 0]])
    rhs = sp.Matrix([[-a, b, c], [d, -e, f], [g, h, 0]]).det()
    out['a33_zero_identity'] = sp.expand(lhs - rhs) == 0 and sp.expand(lhs - (a*f*h + b*f*g + c*d*h + c*e*g)) == 0
    # (2) A26-01 symmetric lift, u^2 = 2: det diag(l, M_u) = l per_3(A).
    A = [[a, d, e], [d, b, f], [e, f, c]]
    Mu = sp.Matrix([[a, d, e], [-d, b, (u - 1) * f], [-e, -(u + 1) * f, c]])
    diff = sp.expand(l * Mu.det() - l * per3(A))
    out['a26_symmetric_identity_mod_u2_minus_2'] = sp.rem(sp.Poly(diff, u), sp.Poly(u**2 - 2, u)).is_zero
    # (3) Laurent pencil for p4 = z w (z w + u v + t^2) (MAP_AND_BOUNDARY_PROOF section 6).
    z, w, U, V, t = sp.symbols('z w U V t')
    ws = w + s**2 * z
    rs = (s**2 * z - w) / (2 * s)
    Ns = sp.Matrix([[ws / (4 * s**2), U, t - rs], [-V, ws, 0], [-(t + rs), 0, ws]])
    Q = z * w + U * V + t**2
    det4 = sp.simplify(z * Ns.det())
    out['pencil_det_equals_z_ws_Q'] = sp.simplify(det4 - z * ws * Q) == 0
    out['pencil_limit_s_to_0'] = str(sp.expand(sp.limit(sp.expand(det4), s, 0)))
    out['pencil_limit_equals_p4'] = sp.expand(sp.limit(sp.expand(det4), s, 0) - z * w * Q) == 0
    # (4) w Q with Q = k w^2 + a c + b d.
    k, A1, B1, C1, D1 = sp.symbols('k A1 B1 C1 D1')
    M = sp.Matrix([[k * w, A1, B1], [-C1, w, 0], [-D1, 0, w]])
    out['wQ_identity'] = sp.expand(M.det() - w * (k * w**2 + A1 * C1 + B1 * D1)) == 0
    out['status'] = 'PASS' if all(v is True for kk, v in out.items() if kk not in ('status', 'label', 'pencil_limit_s_to_0')) else 'FAIL'
    return out


if __name__ == '__main__':
    run(5, __file__, body, ['analysis/b27_01r_identities.py', 'analysis/b27_01r_cap.py'],
        ['IDENTITIES.json'])
