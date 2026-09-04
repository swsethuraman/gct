#!/usr/bin/env python3
"""
Session 47 -- independent (star) certificate for the counterexample's vectors.

analysis/wk9_s42_lift.py produced k integer highest-weight vectors supported on
the RED columns of the isotypic reduction and verified E_red v = 0 over Z.  That
already places them in I(R_r) -- but only via the engine's own claim that the red
columns are exactly the M_star orbits.  This script checks that claim from
scratch, on the actual monomials:

  Theorem 1 (star), docs/reducible_ideal.md: a B-eigenvector lies in I(R_r) iff
  EVERY monomial of it has, for every i, a factor c_alpha with alpha_i = 0.

For each exhibited vector it expands the support into monomials of C[W]_delta,
and asserts the condition on every one, for every constrained index.  It also
re-verifies E_red v = 0 over the integers against the UNCOMPRESSED raising-
operator rows, independently of the lift's own check.

usage: python3 wk9_s47_starcheck.py delta lam1 lam2 ...
"""
import sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s42_redengine import build, csr_to_rows
from wk9_s36_stabred import exps


def main(delta, lam):
    cert = os.path.join(ROOT, 'results', 's42_certs',
                        f"{'_'.join(map(str, lam))}_d{delta}.txt")
    vecs = []
    for line in open(cert):
        if line.startswith('#'): continue
        line = line.strip()
        if line: vecs.append([int(v) for v in line.split()])
    print(f"loaded {len(vecs)} integer vectors from {os.path.relpath(cert, ROOT)}", flush=True)

    B = build(lam, delta, verbose=False)
    A = exps(4, len(lam))
    red, vecs_orb = B['red'], B['vecs']
    cons = B['cons']
    n = B['n_red']
    print(f"  n_red={n} constrained indices (lam_i >= delta) = {cons}", flush=True)
    assert all(len(v) == n for v in vecs), "vector length != n_red"

    # (star) on every monomial of every red orbit carrying a nonzero coefficient
    checked = 0
    for vi, v in enumerate(vecs):
        supp = [j for j, c in enumerate(v) if c]
        mons = 0
        for j in supp:
            for m in vecs_orb[red[j]]:          # m = tuple of indices into A
                mons += 1
                for i in cons:
                    assert any(A[k][i] == 0 for k in m), \
                        ("(star) FAILS", lam, delta, vi, j, m, i)
        print(f"  vector {vi}: {len(supp)} red orbits, {mons} monomials, "
              f"(star) holds on every one for every i in {cons}", flush=True)
        checked += mons

    # E v = 0 over Z against the uncompressed rows
    rows = csr_to_rows(B['E_red'])
    for vi, v in enumerate(vecs):
        for d in rows:
            s = 0
            for c, val in d.items(): s += val * v[c]
            assert s == 0, ("E_red v != 0 over Z", lam, delta, vi)
    print(f"  E_red v = 0 over Z re-verified for all {len(vecs)} vectors "
          f"against {len(rows)} uncompressed rows", flush=True)

    from flint import nmod_mat
    from wk9_s36_stabred import P1
    rk = nmod_mat(len(vecs), n, [x % P1 for v in vecs for x in v], P1).rank()
    assert rk == len(vecs), "vectors are not independent"
    print(f"  independence: rank = {rk} = number of vectors", flush=True)
    print(f"VERDICT: {len(vecs)} independent integer HWVs of weight {lam} in "
          f"I(R_{len(lam)})_{delta}, (star) certified on {checked} monomials; "
          f"so dim(HWV ∩ span M_star) >= {len(vecs)} over Q, i.e. "
          f"mult_red <= a - {len(vecs)}.", flush=True)


if __name__ == '__main__':
    main(int(sys.argv[1]), tuple(int(v) for v in sys.argv[2:]))
