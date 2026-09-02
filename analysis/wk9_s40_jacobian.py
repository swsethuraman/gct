#!/usr/bin/env python3
"""
Session 40, check 2 -- the corank drop at fresh pencils, and the defect
certificates, at n = 3, 4, 5, 6.

For each n and each fresh random integer pencil (box +-BOX, seed printed):
  (a) corank of the degree-(3n-5) Macaulay matrix of F = det M(s), both primes
      (expect mu_{3n-5}(n) + def_{2n-5}(N); the cap theorem needs >= mu + 1);
      controls: a random n-ic (expect mu exactly), and at n = 3 cubics with
      5 and 6 nodes at general points (expect 5 and 6: at n = 3 the drop is
      "six nodes", not "determinantal");
  (b) the Hilbert function of S/J, J = ideal of the (n-1)-minors of M(s), in
      degrees n-1 .. 2n, against the Gulliksen-Negard prediction; the value
      nu(n) it stabilises at is the node count;
  (c) the saturated values h^0(I_Z(k)) at k = 2n-5 and k = n via the quotient
      (J_{k+e} : m^e)_k with e chosen so that J_{k+e} = I_Z(k+e).

Direction of every promotion: a rank measured at a point is <= the generic
rank, so dim J_k measured is a LOWER bound on the generic dim J_k and
H_{S/J}(k) measured is an UPPER bound on the generic value; h^0(I_Z(k)) at a
point is >= the generic value (upper semicontinuity).  Hence
  * measured H_{S/J}(2n-5) = nu - 1 shows generic H <= nu - 1 (with GN: =);
  * measured h^0(I_Z(2n-5)) = dim S_{2n-5} - (nu - 1) shows the generic
    defect is <= 1, and with the GN lower bound it is exactly 1.
"""
import sys, random, time
from math import comb
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from wk9_s40_poly import *
from wk9_s40_cap import mu, H_J, nu_harris_tu, cap

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260902
BOX = 10 ** 6
NS = {3: 3, 4: 2, 5: 2, 6: 1}      # pencils per n
if len(sys.argv) > 2: NS = {int(a.split(':')[0]): int(a.split(':')[1]) for a in sys.argv[2:]}

def nodal_cubic(k, rnd, p):
    """a random cubic singular at k random integer points of P^4 (mod p)."""
    pts = [[rnd.randint(-9, 9) for _ in range(NV)] for _ in range(k)]
    E3 = monos(3); rows = []
    for pt in pts:
        for j in range(NV):
            row = {}
            for ci, e in enumerate(E3):
                if e[j]:
                    ee = list(e); ee[j] -= 1
                    v = e[j]
                    for t in range(NV): v *= pt[t] ** ee[t]
                    if v % p: row[ci] = v % p
            rows.append(row)
    M = nmod_mat(len(rows), len(E3), [0] * (len(rows) * len(E3)), p)
    for r, row in enumerate(rows):
        for c, v in row.items(): M[r, c] = v
    X, nul = M.nullspace()
    assert nul == 35 - 5 * k, ("node conditions dependent", k, nul)
    co = [rnd.randint(1, 10 ** 6) for _ in range(nul)]
    Fv = [sum(co[c] * int(X[i, c]) for c in range(nul)) % p for i in range(len(E3))]
    return {e: Fv[i] for i, e in enumerate(E3) if Fv[i]}

def run(n, trial):
    rnd = random.Random(SEED * 100 + n * 10 + trial)
    A = rand_pencil(n, rnd, BOX)
    ent = pencil_entries(A, n)
    F = det_form(ent, n)
    k = 3 * n - 5
    t0 = time.time()
    cor = [macaulay_corank(F, n, k, p) for p in (P1, P2)]
    mu_k = mu(k, n)
    print(f"n={n} pencil {trial}: corank M_{k}(det) = {cor[0]} / {cor[1]}   (smooth mu = {mu_k}; cap needs >= {mu_k+1}; cap(n) = {cap(n)})   [{time.time()-t0:.1f}s]")
    if trial == 0:
        G = randform(n, rnd, 99)
        corg = [macaulay_corank(G, n, k, p) for p in (P1, P2)]
        print(f"        control random {n}-ic: corank = {corg[0]} / {corg[1]}   (expect {mu_k})")
        if n == 3:
            for kn in (5, 6):
                cc = []
                for p in (P1, P2):
                    Fk = nodal_cubic(kn, random.Random(SEED + kn), p)
                    cc.append(macaulay_corank(Fk, 3, 4, p))
                print(f"        control cubic with {kn} general nodes: corank M_4 = {cc[0]} / {cc[1]}   (expect {5 + max(0, kn - 5)})")
    # (b) Hilbert function of the minor ideal
    mins = submax_minors(ent, n)
    nu = nu_harris_tu(n)
    hf = {}
    for kk in range(min(n - 1, 2 * n - 5), 2 * n + 1):
        vals = [hilbert_quotient(mins, n - 1, kk, p) for p in (P1, P2)]
        assert vals[0] == vals[1], (n, kk, vals)
        hf[kk] = vals[0]
    gn = {kk: H_J(kk, n) for kk in hf}
    ok = all(hf[kk] == gn[kk] for kk in hf)
    print(f"        H_{{S/J}}(k), k={min(n-1, 2*n-5)}..{2*n}: measured {list(hf.values())}  GN {list(gn.values())}  nu={nu}  {'AGREE' if ok else 'DIFFER'}")
    assert hf[2 * n] == nu, ("node count", n, hf[2 * n], nu)
    # (c) saturated values
    for kk, label in ((2 * n - 5, "2n-5"), (n, "n")):
        e = 1
        while hf.get(kk + e, None) != nu: e += 1
        vals = [saturated_dim(mins, n - 1, kk, e, p) for p in (P1, P2)]
        assert vals[0] == vals[1], (n, kk, vals)
        h0 = vals[0]; conds = comb(kk + 4, 4) - h0
        print(f"        h^0(I_Z({kk})) [k={label}] = {h0} via (J_{kk+e}:m^{e}); nodes impose {conds} of {nu} conditions; def_{kk} = {nu - conds};  dim J_{kk} = {comb(kk+4,4) - hf[kk]}")
    sys.stdout.flush()

if __name__ == '__main__':
    print(f"seed {SEED}, box +-{BOX}, primes {P1}, {P2}")
    for n in sorted(NS):
        for trial in range(NS[n]):
            run(n, trial)
