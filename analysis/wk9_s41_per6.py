#!/usr/bin/env python3
"""
Session 41 -- Phase 0b: the permanent's own ideal at r = 6,
I(D_6^{per_3}) inside C[Sym^3 C^6], degrees delta = 7, 8 (and higher if cheap).

Why (docs/transfer_lemma.md Prop. 8): at r = 6, mult_pad(lam, delta) <
mult_red(lam, delta) -- a permanent-specific equation -- requires
I(D_6^{per_3})_delta != 0, and that ideal is concentrated at weights of length
exactly 6 (restriction lemma; D_5^{per_3} = Sym^3 C^5).  s37 measured it empty
at delta = 6 (Pieri: empty below).  If it is empty at delta = 7, 8 then
mult_pad = mult_red at EVERY weight of those degrees, as a theorem, and the
permanent adds nothing anywhere in this session's range.

Pipeline: the stabiliser reduction of wk9_s36_stabred.py with n = 3, r = 6,
evaluation at per_3(sum s_i A_i) points (per_form(3), random integer A_i),
both house primes, a + 8 points, sceptical branch (3a + 24 points, seed 907)
on any mult < a.  a by plethysm (wk8_s30_pleth.a_of) and by kernel dimension,
asserted equal.

usage: python3 wk9_s41_per6.py <delta_lo> <delta_hi> [--nchi-cap 6000] [--min-nchi 0]
(a second pass with --min-nchi picks up the cells a first pass skipped above its cap)
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.join(HERE, '..')
from wk9_s36_stabred import (orbit_setup, reduced_rows, kernel_exact, kernel_compressed,
                             point_rows, mult_from, monomials, P1, P2, log)
from wk9_s41_kernel import kernel_inplace, sparse_M, verify_kernel
from wk8_s30_core import per_form
from wk8_s30_pleth import a_of

PER3, N_PER = per_form(3)

def partitions(total, parts, maxpart=None):
    if maxpart is None: maxpart = total
    if parts == 0:
        if total == 0: yield ()
        return
    for first in range(min(total, maxpart), 0, -1):
        for rest in partitions(total - first, parts - 1, first):
            yield (first,) + rest

def measure_per6(delta, lam, a_exp, npts=None, seed=41, bound=40):
    n, r = 3, 6
    t0 = time.time()
    basis, vecs, group = orbit_setup(n, r, delta, lam, verbose=False)
    nchi = len(vecs)
    rows, nfx = reduced_rows(n, r, delta, lam, vecs, verbose=False)
    K = npts if npts else a_exp + 8
    res = {}
    Msp = sparse_M(rows, nchi) if nchi > 2500 else None
    for p in (P1, P2):
        if nchi <= 2500: a, rk, kern = kernel_exact(rows, nchi, p)
        else:
            a, rk, kern = kernel_inplace(rows, nchi, p, Msp=Msp)      # validated route, results/s41_validation.md
            if a == a_exp: verify_kernel(Msp, kern, p)
        assert a == a_exp, ("a mismatch vs plethysm", lam, p, a, a_exp)
        assert rk == nchi - a, (lam, p, rk, nchi, a)
        ev = point_rows(PER3, N_PER, n, r, basis, vecs, K, seed, bound, p)
        res[p] = mult_from(kern, ev, a, p)
    assert res[P1] == res[P2], (lam, res)
    monomials.cache_clear()
    return dict(lam=lam, a=a_exp, N_S=len(basis), stab=len(group), n_chi=nchi, nrows=len(rows),
                mult=res[P1], npts=K, secs=time.time() - t0)

def banked_per6(out):
    done = set()
    if os.path.exists(out):
        for ln in open(out):
            if ln.startswith('| '):
                c = [x.strip() for x in ln.strip().strip('|').split('|')]
                try: done.add((int(c[0]), eval(c[1].strip('`'))))
                except Exception: pass
    return done

if __name__ == '__main__':
    if sys.argv[1] == '--one':
        # one cell in its own process (memory is returned to the container afterwards)
        import json
        delta = int(sys.argv[2]); lam = tuple(int(x) for x in sys.argv[3].split(',')); a = int(sys.argv[4])
        res = measure_per6(delta, lam, a)
        if res['mult'] < a:
            log(f"   *** {lam}: mult {res['mult']} < a {a} — sceptical branch")
            res2 = measure_per6(delta, lam, a, npts=3 * a + 24, seed=907)
            assert res2['mult'] == res['mult'], ("short rank unstable", lam, res, res2)
            res['sceptical'] = res2['mult']
        print("RESULT " + json.dumps(res), flush=True)
        sys.exit(0)
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    cap = int(sys.argv[sys.argv.index('--nchi-cap') + 1]) if '--nchi-cap' in sys.argv else 6000
    lo_nchi = int(sys.argv[sys.argv.index('--min-nchi') + 1]) if '--min-nchi' in sys.argv else 0
    out = os.path.join(ROOT, 'results', 's41_per6.md')
    new = not os.path.exists(out)
    fh = open(out, 'a')
    if new:
        fh.write("# `I(D_6^{per_3})` in `C[Sym^3 C^6]`, by degree — session 41, Phase 0b\n\n"
                 "Reduced pipeline (`wk9_s36_stabred`, `n = 3`, `r = 6`), points `per_3(Σ s_i A_i)`, both primes, "
                 "`a + 8` points; sceptical branch at `3a + 24` points (seed 907) on any `mult < a`.  "
                 "Every length-6 weight `μ ⊢ 3δ` with `a(μ, δ) ≥ 1`.  `units = a − mult` is the ideal's share.  "
                 "By Prop. 8 of `docs/transfer_lemma.md`, `I(D_6^{per_3})_δ = 0` ⇒ `mult_pad = mult_red` at every weight of degree `δ`.\n\n"
                 "| delta | mu | a | N_S | Stab | n_chi | mult | units | secs |\n|---|---|---|---|---|---|---|---|---|\n")
    import subprocess, json
    done = banked_per6(out)
    for delta in range(lo, hi + 1):
        tot_a = tot_u = 0; bites = []; skipped = []
        cells = [(lam, a_of(lam, delta, 3, 6)) for lam in partitions(3 * delta, 6)]
        cells = [(l, a) for l, a in cells if a >= 1]
        log(f"== delta={delta}: {len(cells)} length-6 weights with a>=1, sum a = {sum(a for _, a in cells)}")
        for lam, a in cells:
            if (delta, lam) in done:
                continue            # banked by an earlier pass (rows are the record; totals are recomputed by the report)
            basis, vecs, group = orbit_setup(3, 6, delta, lam, verbose=False)
            nchi = len(vecs); monomials.cache_clear()
            if nchi > cap:
                skipped.append((lam, a, nchi)); log(f"   skip {lam} a={a} n_chi={nchi} > cap"); continue
            if nchi <= lo_nchi: continue
            pr = subprocess.run([sys.executable, os.path.abspath(__file__), '--one', str(delta), ','.join(map(str, lam)), str(a)],
                                stdout=subprocess.PIPE, stderr=sys.stderr, text=True)
            res = None
            for ln in pr.stdout.splitlines():
                if ln.startswith('RESULT '): res = json.loads(ln[7:])
            assert res is not None, ("cell process failed", lam, pr.returncode)
            res['lam'] = tuple(res['lam'])
            if res['mult'] < a:
                bites.append(res)
            tot_a += a; tot_u += a - res['mult']
            line = (f"| {delta} | `{lam}` | {a} | {res['N_S']} | {res['stab']} | {res['n_chi']} | {res['mult']} | "
                    f"{a - res['mult']} | {res['secs']:.0f} |")
            fh.write(line + "\n"); fh.flush(); os.fsync(fh.fileno())
            log(f"   {lam} a={a} N_S={res['N_S']} n_chi={res['n_chi']} mult={res['mult']} ({res['secs']:.0f}s)")
        summary = (f"\n**δ = {delta}" + (f" (pass with n_χ in ({lo_nchi}, {cap}])" if lo_nchi else "") + f": measured Σa = {tot_a}, ideal units = {tot_u}"
                   + (f"; bites: " + ", ".join(f"`{b['lam']}` (a={b['a']}, mult={b['mult']})" for b in bites) if bites else "; no bites")
                   + (f"; {len(skipped)} cells above the n_χ cap {cap} unmeasured: " + ", ".join(f"`{l}` a={a} n_χ={nc}" for l, a, nc in skipped) if skipped else "; every cell measured")
                   + ".**\n")
        fh.write(summary); fh.flush(); os.fsync(fh.fileno())
        log(summary)
    fh.close()
