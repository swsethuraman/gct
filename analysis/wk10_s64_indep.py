#!/usr/bin/env python3
"""Session 64 -- an INDEPENDENT, r-generic three-way engine.

Shares NO code with the session-45/60 isotypic engine: it uses the full
weight-lambda monomial basis and raising rows of wk8_s30_core (build_R), the
exact flint nullspace (nullspace), and eval_row on that basis -- the session-30
route, before any stabiliser reduction or Wiedemann certificate.  So agreement
with wk10_s64_cell is a genuine second-implementation check, and it is r-generic
(the s60 primitives are hardwired to r = 5), so it also covers r = 3, 4.

    mult_det = rank[ ev_det . ker R ] ,  det_4 pencils   (DET4, N=16)
    mult_red = rank[ ev_red . ker R ] ,  l . (generic cubic in r vars)
    mult_pad = rank[ ev_pad . ker R ] ,  l(s).per_3(A(s))   (PAD34, N=10)

Small cells only (the full basis is used); intended for r = 3, 4 and for a
random audit of r = 5 cells against the reduced engine.
"""
import os, sys, random, itertools, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_core import (exps, build_R, restrict, eval_row, rank_of, nullspace,
                          det_form, per_padded, P1, P2)

N = 4
PRIMES = (P1, P2)
DET4, N_DET = det_form(4)
PAD34, N_PAD = per_padded(3, 4)


def _det_pts(K, r, seed, bound):
    rnd = random.Random(seed)
    return [[[rnd.randint(-bound, bound) for _ in range(N_DET)] for _ in range(r)] for _ in range(K)]


def _pad_pts(K, r, seed, bound):
    rnd = random.Random(seed)
    return [[[rnd.randint(-bound, bound) for _ in range(N_PAD)] for _ in range(r)] for _ in range(K)]


def _red_pts(K, r, seed, bound):
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        lin = [rnd.randint(-bound, bound) for _ in range(r)]
        cub = {al: rnd.randint(-bound, bound) for al in exps(3, r)}
        out.append((lin, cub))
    return out


def _red_coeffs(pt, r):
    lin, cub = pt; out = {}
    for a3, cc in cub.items():
        if not cc: continue
        for i in range(r):
            if not lin[i]: continue
            a4 = list(a3); a4[i] += 1; k = tuple(a4)
            out[k] = out.get(k, 0) + lin[i] * cc
    return {k: v for k, v in out.items() if v}


def _mult(basis, kern_by_p, form_coeffs, K, r, seed, bound, kind):
    """rank of evaluation functionals on the kernel, per prime.  form_coeffs is a
    callable(point)->coeff dict.  Returns dict prime->mult and the agreement."""
    if kind == 'det':
        pts = _det_pts(K, r, seed, bound); co = lambda P: restrict(DET4, N_DET, N, r, P)
    elif kind == 'pad':
        pts = _pad_pts(K, r, seed, bound); co = lambda P: restrict(PAD34, N_PAD, N, r, P)
    else:
        pts = _red_pts(K, r, seed, bound); co = lambda P: _red_coeffs(P, r)
    res = {}
    for p in PRIMES:
        kern = kern_by_p[p]; a = len(kern); nb = len(basis)
        if a == 0: res[p] = 0; continue
        rows = []
        for pt in pts:
            e = eval_row(basis, co(pt), N, r)
            rows.append([sum(e[i] * kv[i] for i in range(nb) if kv[i]) % p for kv in kern])
        res[p] = rank_of(rows, a, p)
    return res


def measure_indep(lam, delta, seeds=2, bound=40, npts=None, seed_det=11, seed_red=29, seed_pad=37):
    lam = tuple(lam); r = len(lam)
    basis, R = build_R(N, r, delta, lam)
    nb = len(basis)
    kern_by_p = {}
    a = None
    for p in PRIMES:
        k = nullspace(R, nb, p); kern_by_p[p] = k
        if a is None: a = len(k)
        assert len(k) == a, ("a disagrees across primes", lam, delta, p, len(k), a)
    out = dict(lam=list(lam), delta=delta, ell=r, a=a, nbasis=nb, primes=list(PRIMES), engine='indep(wk8_s30_core)')
    if a == 0:
        out.update(status='a=0'); return out
    K = npts if npts else a + 8
    sides = {}
    for kind in ('det', 'red', 'pad'):
        best = {}
        for si in range(seeds):
            sd = {'det': seed_det, 'red': seed_red, 'pad': seed_pad}[kind] + 1000 * si
            r_p = _mult(basis, kern_by_p, None, K, r, sd, bound, kind)
            for p in PRIMES: best[p] = max(best.get(p, 0), r_p[p])
        agree = len(set(best.values())) == 1
        sides[kind] = dict(mult=(best[PRIMES[0]] if agree else None), per_prime={str(p): int(v) for p, v in best.items()}, primes_agree=agree)
    out['mult_det'] = sides['det']['mult']; out['mult_red'] = sides['red']['mult']; out['mult_pad'] = sides['pad']['mult']
    out['i_det'] = a - out['mult_det']; out['i_red'] = a - out['mult_red']; out['i_pad'] = a - out['mult_pad']
    out['D'] = out['mult_pad'] - out['mult_det']
    out['containment_pad_le_red'] = out['mult_pad'] <= out['mult_red']
    out['pad_eq_red'] = (out['mult_pad'] == out['mult_red'])   # must hold at r <= 5 (P_r = R_r)
    out['sides'] = sides
    out['K'] = K
    return out


if __name__ == '__main__':
    cells = json.load(open(sys.argv[1]))
    outp = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    f = open(outp, 'w') if outp else None
    allok = True
    for c in cells:
        res = measure_indep(c['lam'], c['delta'], seeds=2)
        if res.get('status') == 'a=0':
            print(f"  r? d{c['delta']} {tuple(c['lam'])}: a=0 (skip)"); continue
        bank = ''
        if 'mult_det' in c: bank += f" [banked det {c['mult_det']}{'=' if c['mult_det']==res['mult_det'] else '!='}{res['mult_det']}]"
        if 'mult_red' in c: bank += f" [banked red {c['mult_red']}{'=' if c['mult_red']==res['mult_red'] else '!='}{res['mult_red']}]"
        eqok = res['pad_eq_red'] if res['ell'] <= 5 else True
        allok = allok and eqok and res['containment_pad_le_red']
        print(f"  r{res['ell']} d{c['delta']} {tuple(c['lam'])}: a={res['a']} mult_det={res['mult_det']} "
              f"mult_red={res['mult_red']} mult_pad={res['mult_pad']} D={res['D']} pad=red:{res['pad_eq_red']}{bank}")
        if f: f.write(json.dumps(res) + "\n")
    if f: f.close()
    print("INDEP verdict:", "all pad=red (r<=5) and containment held" if allok else "MISMATCH -- inspect")
