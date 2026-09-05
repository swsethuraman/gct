#!/usr/bin/env python3
"""
Session 54 -- the R_5 vs D_5^{det_4} multiplicity comparison at length-5 weights.

For a length-5 cell (lam, delta):
  a        = nb - rank_p(R)              [raising-operator kernel], cross-checked
             against the plethysm a_of  [wk8_s30_pleth]
  mult_det = mult_lam C[D_5^{det_4}]     [eval at det_4(M(s)) points]
  mult_red = mult_lam C[R_5]             [eval at reducible l(s).c(s) points]

R_5 subset D_5^{det_4}  <=>  mult_red <= mult_det at every length-5 cell
(necessary; T1/T3 of PREREG_s54.md). A cell with mult_red > mult_det refutes
containment and exhibits an equation of D_5 not vanishing on R_5.

Exact ranks by flint nmod_mat over two house primes; mult=a is a certificate.
"""
import sys, json, time, random, argparse
sys.path.insert(0, 'analysis')
from wk8_s30_core import (exps, monomials, build_R, rank_of, eval_row,
                          restrict, det_form, per_padded, P1, P2)
from wk8_s30_pleth import a_of

PRIMES = (P1, P2)
N = 4     # quartic
R = 5     # five variables

def nb_capped(delta, lam, cap):
    """count degree-delta weight-lam monomials, aborting once it exceeds cap.
    Returns min(count, cap+1). Cheap way to skip oversized cells without the
    full enumeration that monomials() does."""
    lam = tuple(lam) + (0,) * (R - len(lam))
    A = exps(N, R); L = len(A)
    cnt = 0
    stack = [(0, delta, lam)]
    # iterative to avoid deep recursion; count multisets (nondecreasing index)
    def rec(start, left, rem):
        nonlocal cnt
        if cnt > cap: return
        if left == 0:
            if not any(rem): cnt += 1
            return
        if sum(rem) != left * N: return
        for i in range(start, L):
            al = A[i]
            if any(al[j] > rem[j] for j in range(R)): continue
            rec(i, left - 1, tuple(rem[j] - al[j] for j in range(R)))
            if cnt > cap: return
    rec(0, delta, lam)
    return cnt

def reducible_point(rng, bound):
    """coeffs of l(s).c(s): random linear l, random quinary cubic c."""
    lin = [rng.randint(-bound, bound) for _ in range(R)]
    cub = {a: rng.randint(-bound, bound) for a in exps(3, R)}
    out = {}
    for a3, cc in cub.items():
        if cc == 0: continue
        for i in range(R):
            if lin[i] == 0: continue
            a4 = list(a3); a4[i] += 1
            k = tuple(a4)
            out[k] = out.get(k, 0) + lin[i] * cc
    return out

def det_point(rng, bound):
    """coeffs of det_4(sum s_i A_i): random A_i in M_4."""
    f, Nv = det_form(4)
    As = [[rng.randint(-bound, bound) for _ in range(Nv)] for _ in range(R)]
    return restrict(f, Nv, N, R, As)

def pad_point(rng, bound):
    """coeffs of l(s).per_3(M(s)): x_0.per_3 pulled back (mult_red at r=5)."""
    f, Nv = per_padded(3, 4)     # N=10
    As = [[rng.randint(-bound, bound) for _ in range(Nv)] for _ in range(R)]
    return restrict(f, Nv, N, R, As)

def measure_cell(lam, delta, seed=11, bound=30, want_pad=False, a_expect=None):
    lam = tuple(lam) + (0,) * (R - len(lam))
    basis, Rrows = build_R(N, R, delta, lam)
    nb = len(basis)
    res = dict(lam=[int(x) for x in lam if x], delta=delta, nb=nb)
    if nb == 0:
        res.update(a=0, mult_det=0, mult_red=0, ok=True); return res
    rkR = {p: rank_of(Rrows, nb, p) for p in PRIMES}
    a = nb - rkR[PRIMES[0]]
    res['a'] = a
    res['a_selfcheck'] = all(nb - rkR[p] == a for p in PRIMES)
    if a_expect is not None:
        res['a_pleth'] = a_expect
        res['a_agree'] = (a == a_expect)
    if a == 0:
        res.update(mult_det=0, mult_red=0, ok=res['a_selfcheck']); return res
    rng = random.Random(seed)
    K = a + 8
    det_ev = [eval_row(basis, det_point(rng, bound), N, R) for _ in range(K)]
    red_ev = [eval_row(basis, reducible_point(rng, bound), N, R) for _ in range(K)]
    md, mr = {}, {}
    for p in PRIMES:
        md[p] = rank_of(list(Rrows) + det_ev, nb, p) - rkR[p]
        mr[p] = rank_of(list(Rrows) + red_ev, nb, p) - rkR[p]
    res['mult_det'] = md[PRIMES[0]]
    res['mult_red'] = mr[PRIMES[0]]
    res['det_prime_agree'] = (len(set(md.values())) == 1)
    res['red_prime_agree'] = (len(set(mr.values())) == 1)
    if want_pad:
        pad_ev = [eval_row(basis, pad_point(rng, bound), N, R) for _ in range(K)]
        mp = {p: rank_of(list(Rrows) + pad_ev, nb, p) - rkR[p] for p in PRIMES}
        res['mult_pad'] = mp[PRIMES[0]]
        res['pad_eq_red'] = (mp[PRIMES[0]] == mr[PRIMES[0]] and len(set(mp.values())) == 1)
    res['refute'] = res['mult_red'] > res['mult_det']
    res['ok'] = res['a_selfcheck'] and res['det_prime_agree'] and res['red_prime_agree']
    return res

def run(cells, out_path, maxnb=None, want_pad_first=0, seed=11):
    done = []
    n_ref = 0
    t_start = time.time()
    with open(out_path, 'a') as f:
        for i, (lam, a_pl) in enumerate(cells):
            lam = tuple(lam)
            if maxnb:
                nbc = nb_capped(delta_of(lam), lam, maxnb)
                if nbc > maxnb:
                    rec = dict(lam=list(lam), delta=delta_of(lam), nb=f'>{maxnb}',
                               a=a_pl, skipped='over_maxnb')
                    f.write(json.dumps(rec) + '\n'); f.flush(); continue
            t0 = time.time()
            rec = measure_cell(lam, delta_of(lam), seed=seed, a_expect=a_pl,
                               want_pad=(i < want_pad_first))
            rec['sec'] = round(time.time() - t0, 2)
            f.write(json.dumps(rec) + '\n'); f.flush()
            done.append(rec)
            flag = ''
            if rec.get('refute'):
                flag = '  *** REFUTE: mult_red > mult_det ***'; n_ref += 1
            if not rec.get('ok', True): flag += '  [SELFCHECK FAIL]'
            print(f"[{i+1}/{len(cells)}] d={rec['delta']} lam={rec['lam']} "
                  f"nb={rec['nb']} a={rec.get('a')} "
                  f"mdet={rec.get('mult_det')} mred={rec.get('mult_red')}"
                  f"{flag} ({rec['sec']}s)", flush=True)
    print(f"\nDONE {len(done)} cells, {n_ref} refutations, "
          f"{round(time.time()-t_start,1)}s -> {out_path}", flush=True)
    return done

def delta_of(lam):
    return sum(lam) // N

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--census', default='results/s54_length5_census.json')
    ap.add_argument('--delta', type=int, required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--maxnb', type=int, default=None)
    ap.add_argument('--padfirst', type=int, default=0)
    ap.add_argument('--seed', type=int, default=11)
    ap.add_argument('--limit', type=int, default=None)
    a = ap.parse_args()
    cens = json.load(open(a.census))
    cells = [(tuple(l), int(av)) for l, av in cens[str(a.delta)]]
    # cheap ordering proxy: more skewed (larger lam_1) => smaller weight space.
    cells.sort(key=lambda x: (-x[0][0], -sum(y*y for y in x[0])))
    if a.limit: cells = cells[:a.limit]
    run(cells, a.out, maxnb=a.maxnb, want_pad_first=a.padfirst, seed=a.seed)
