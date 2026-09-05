#!/usr/bin/env python3
"""
Session 52, Task 0 -- evaluate a six-row highest weight vector at the points
that Buergisser-Ikenmeyer-Panova's Theorem 2.5 supplies at n = 4.

BIP Thm 2.5 [Thm 2.8 in v1]: if n >= s*k then X^(n-s)(phi_1^s + ... + phi_k^s)
lies in Omega_n.  At n = 4 the admissible (s,k) are exactly the eight listed by
wk9_s52_bipreach.py, and every resulting quartic has linear span <= 3 (and is a
product of four linear forms over C).

Lemma B (pre-registration / report): a weight vector of weight lam vanishes at
every point whose linear span has dimension < ell(lam).  Proof: put the torus
element t = diag(1,..,1,c,..,c) trivial on the span; f(t.p) = t^lam f(p) with
t^lam = c^(lam_{u+1} + ... ) and t.p = p.

This script checks Lemma B empirically at a real six-row cell and, in the same
run, checks that the same vector is NON-vanishing at generic det_4 pencils --
so the vanishing is a property of BIP's points, not of the vector.

Controls, in order of support:
  bip_*     the eight BIP shapes, generic linear forms, support <= 3
  chow3     a generic product of four linear forms drawn from a 3-dim subspace
  chow6     a generic product of four linear forms of full support 6
  lc        a reducible point l . c with c a generic cubic (brief_wording section 5(2))
  det       a generic det_4 pencil, full support 6
  pad       the true padded permanent x_0 . per_3(x_1..x_9) restricted, support 6

usage: python3 wk9_s52_bippoints.py --lam 18,2,2,2,2,2 --delta 7 [--seed 907]
"""
import sys, os, json, random, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_core import exps, restrict, P1, P2
from wk9_s36_stabred import orbit_setup, reduced_rows, kernel_exact, DET4, N_DET, PAD34, N_PAD


def lin(r, rnd, bound=40, support=None):
    """a random linear form as a coefficient vector of length r; if `support`
    is a list of indices the form is supported there."""
    idx = range(r) if support is None else support
    v = [0] * r
    for i in idx:
        v[i] = rnd.randint(-bound, bound)
    if not any(v): v[list(idx)[0]] = 1
    return v


def mul(a, b, r):
    """multiply two coefficient dicts {exponent tuple: coeff}."""
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = tuple(e1[i] + e2[i] for i in range(r))
            out[k] = out.get(k, 0) + c1 * c2
    return out


def linform(v, r):
    return {tuple(1 if j == i else 0 for j in range(r)): c for i, c in enumerate(v) if c}


def power(f, e, r):
    out = {tuple([0] * r): 1}
    for _ in range(e): out = mul(out, f, r)
    return out


def add(a, b, r):
    out = dict(a)
    for k, c in b.items(): out[k] = out.get(k, 0) + c
    return out


def bip_points(r, rnd, n=4):
    """every padded power sum BIP Thm 2.5 supplies at this n, with generic
    linear forms.  Returns [(name, co, support_indices)]."""
    pts = []
    for s in range(1, n + 1):
        for k in range(1, n // s + 1):
            if s * k > n: continue
            # the point uses X and phi_1..phi_k: k+1 forms, so support <= k+1
            sup = list(range(min(k + 1, r)))
            X = linform(lin(r, rnd, support=sup), r)
            body = {}
            for _ in range(k):
                body = add(body, power(linform(lin(r, rnd, support=sup), r), s, r), r)
            co = mul(power(X, n - s, r), body, r) if n - s else body
            pts.append((f"bip_s{s}_k{k}", co, sup))
    return pts


def row_from_co(co, n, r, vecs, prime):
    A = exps(n, r)
    cor = {al: c % prime for al, c in co.items() if c % prime}
    row = []
    for vec in vecs:
        tot = 0
        for m, sgn in vec.items():
            v = sgn
            for kk in m:
                c = cor.get(A[kk], 0)
                if c == 0: v = 0; break
                v = v * c % prime
            tot += v
        row.append(tot % prime)
    return row


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


if __name__ == '__main__':
    lam = tuple(int(x) for x in arg('--lam').split(','))
    delta = int(arg('--delta'))
    seed = int(arg('--seed', 907))
    n, r = 4, len(lam)
    t0 = time.time()
    basis, vecs, group = orbit_setup(n, r, delta, lam, verbose=False)
    nchi = len(vecs)
    rows, nfx = reduced_rows(n, r, delta, lam, vecs, verbose=False)
    out = dict(lam=list(lam), delta=delta, n_chi=nchi, N_S=len(basis), stab=len(group), pts={})
    for prime in (P1, P2):
        a, rk, kern = kernel_exact(rows, nchi, prime)
        out.setdefault('a', a)
        assert a == out['a'], ("a differs between primes", a, out['a'])
        rnd = random.Random(seed)
        pts = bip_points(r, rnd)
        # chow points
        sup3 = [0, 1, 2]
        c3 = {tuple([0] * r): 1}
        for _ in range(4): c3 = mul(c3, linform(lin(r, rnd, support=sup3), r), r)
        pts.append(("chow3", c3, sup3))
        c6 = {tuple([0] * r): 1}
        for _ in range(4): c6 = mul(c6, linform(lin(r, rnd), r), r)
        pts.append(("chow6", c6, list(range(r))))
        # the reducible control l . c of docs/brief_wording.md section 5(2)
        cub = {}
        for al in exps(3, r):
            cub[al] = rnd.randint(-40, 40)
        pts.append(("lc", mul(linform(lin(r, rnd), r), cub, r), list(range(r))))
        # det and pad
        As = [[rnd.randint(-40, 40) for _ in range(N_DET)] for _ in range(r)]
        pts.append(("det", restrict(DET4, N_DET, n, r, As), list(range(r))))
        As = [[rnd.randint(-40, 40) for _ in range(N_PAD)] for _ in range(r)]
        pts.append(("pad", restrict(PAD34, N_PAD, n, r, As), list(range(r))))
        for name, co, sup in pts:
            row = row_from_co(co, n, r, vecs, prime)
            vals = [sum(row[i] * kv[i] for i in range(nchi) if kv[i]) % prime for kv in kern]
            nz = any(v for v in vals)
            rec = out['pts'].setdefault(name, dict(support=len(sup), nonzero={}))
            rec['nonzero'][str(prime)] = bool(nz)
        print(f"  p={prime} a={a} done ({time.time()-t0:.0f}s)", file=sys.stderr, flush=True)
    print("RESULT " + json.dumps(out))
