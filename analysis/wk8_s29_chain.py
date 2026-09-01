#!/usr/bin/env python3
"""
Session 29 -- C: the subspace protocol, on the padded-permanent CHAIN.

x_0^{n-m} per_m restricted to an r-plane is  ell^{n-m} . (restriction of per_m),
so for n = 4:

    m=1: ell^3 . m'          {ell^3 m}      tangent-developable type
    m=2: ell^2 . q           {ell^2 q}
    m=3: ell   . c           {ell c}        the reducible quartics
    det: everything at r <= 3

and each locus contains the previous one (ell^3 m = ell^2.(ell m) = ell.(ell^2 m)),
so
    D^{per_1} subset D^{per_2} subset D^{per_3} subset D^{det_4}
        =>  I(det) subset I(per_3) subset I(per_2) subset I(per_1)
        =>  U_det  subset U_3      subset U_2      subset U_1     at every weight.

That is the containment prediction, and on this chain the lower members have
ideals that are visible at small degree, so the test is NON-VACUOUS.
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk8_s29_core import measure, det_form, per_padded, monomials, PRIMES
from wk8_s29_pleth import amb

FORMS = [("det", det_form(4)), ("m3", per_padded(3, 4)),
         ("m2", per_padded(2, 4)), ("m1", per_padded(1, 4))]
ELL = int(sys.argv[1]) if len(sys.argv) > 1 else 3
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 5
CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 3000

def contained(U, V, p):
    """is span(U) inside span(V)?  reduce U against a RREF of V."""
    if not U: return True
    n = len(U[0])
    B, piv = [], []
    for v in [list(x) for x in V]:
        w = v[:]
        for r, pc in zip(B, piv):
            if w[pc]:
                f = w[pc] * pow(r[pc], p - 2, p) % p
                w = [(w[i] - f * r[i]) % p for i in range(n)]
        nz = next((i for i in range(n) if w[i]), None)
        if nz is not None: B.append(w); piv.append(nz)
    for v in [list(x) for x in U]:
        w = v[:]
        for r, pc in zip(B, piv):
            if w[pc]:
                f = w[pc] * pow(r[pc], p - 2, p) % p
                w = [(w[i] - f * r[i]) % p for i in range(n)]
        if any(w): return False
    return True

cells = []
for delta in range(2, DMAX + 1):
    for lam, av in amb(delta, 4, 16).items():
        if len(lam) > ELL: continue
        cells.append((len(monomials(4, max(2,len(lam)), delta, lam)), delta, lam, av))
cells.sort()
print("length <= %d, delta <= %d : %d weights with a >= 1 (cap %d)"
      % (ELL, DMAX, len(cells), CAP))
print("delta lam            dim   a | mult: det  m3  m2  m1 | Udim: det m3 m2 m1"
      " | containments")
nvis = 0
for nb, delta, lam, av in cells:
    if nb > CAP: break
    res = {}
    for nm, (f, N) in FORMS:
        res[nm] = measure(f, N, 4, max(2,len(lam)), delta, lam,
                          seed={"det": 11, "m3": 29, "m2": 53, "m1": 71}[nm],
                          want_U=True)
        assert res[nm]['a'] == av, (lam, nm, res[nm], av)
    mu = [res[k]['mult'] for k in ("det", "m3", "m2", "m1")]
    ud = [res[k]['Udim'] for k in ("det", "m3", "m2", "m1")]
    assert mu[0] >= mu[1] >= mu[2] >= mu[3], ("CHAIN VIOLATED", lam, delta, mu)
    p = PRIMES[0]
    ver = []
    for i, j, nmi, nmj in ((0, 1, "det", "m3"), (1, 2, "m3", "m2"),
                           (2, 3, "m2", "m1")):
        if ud[i] == 0: ver.append("%s<%s:vac" % (nmi, nmj)); continue
        ok = contained(res[nmi]['U'], res[nmj]['U'], p)
        ver.append("%s<%s:%s" % (nmi, nmj, "OK" if ok else "*** FAIL ***"))
        nvis += 1
    print("  %d   %-14s %5d %3d | %4d %3d %3d %3d | %8d %2d %2d %2d | %s"
          % (delta, str(lam), nb, av, *mu, *ud, "  ".join(ver)))
    sys.stdout.flush()
print()
print("non-vacuous containment tests run: %d" % nvis)
