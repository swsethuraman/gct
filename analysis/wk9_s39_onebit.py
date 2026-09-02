#!/usr/bin/env python3
"""
Session 39 -- Phase 1: one-bit and forced-cell obstruction tests.

A ONE-BIT cell (a = 1, m_det = 0): mult_det <= m_det = 0, so det side is zero
for free.  Build the unique highest-weight vector v of weight lam with the
validated stabiliser reduction (wk9_s36_stabred.measure_reduced, a = 1 so the
chi-kernel is one-dimensional), reconstruct it exactly over Z from the two
primes (CRT + rational reconstruction), and verify every simple raising
operator kills it over Z.  Then, both primes:
  (1) 20 det_4 pencils in lam-variables -- MUST vanish (audits m_det = 0; a
      nonzero value is a KILL: a, m_det, or the pipeline is wrong);
  (2) 20 true padded-permanent points l(s).per_3(A(s)), built by
      wk9_s36_bite.family('truepad') which shares no code with restrict() --
      nonzero at ANY one means mult_pad = 1 > 0 = mult_det: an OCCURRENCE
      OBSTRUCTION CANDIDATE.

A FORCED cell (a > m_det >= 1): mult_det <= m_det, so pad-side rank
>= m_det + 1 certifies mult_pad > mult_det with no det computation.  Pad-side
rank at 3(a + 8) true padded-permanent points, both primes; rank >= m_det + 1
is a CANDIDATE.

On ANY candidate: STOP -- write the row to docs/OBSTRUCTION_CANDIDATE.md-draft
and return the candidate; the driver halts the session and the full protocol
(results/PREREG_s39.md section 4) is executed separately.  No further cells.

Exact-Z reconstruction and the independent point families are exactly those of
wk9_s36_exact.py / wk9_s36_bite.py (the s36-audited certificate path).

usage: wk9_s39_onebit.py onebit  <lam as 22,2,2,2,2,2,2,2,2,2> <delta>
       wk9_s39_onebit.py forced  <lam> <delta> <a> <m_det>
       wk9_s39_onebit.py runall  <screen.csv>       # all one-bit then forced, ascending n_chi
"""
import sys, os, time, random
from fractions import Fraction
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s36_stabred import (orbit_setup, reduced_rows, kernel_exact,
                             kernel_compressed, expand, exps, DET4, N_DET,
                             PAD34, N_PAD, point_rows, mult_from, P1, P2, log)
from wk9_s36_bite import family, eval_full
from wk9_s36_exact import ratrec
from wk8_s30_pleth import a_of
from flint import nmod_mat

LEDGER = os.path.join(HERE, '..', 'results', 'onebit_ledger.md')
CELLS = os.path.join(HERE, '..', 'results', 's39_cells')
DRAFT = os.path.join(HERE, '..', 'docs', 'OBSTRUCTION_CANDIDATE.md-draft')
EXACT_CAP = 2500


def build_hwv(n, r, delta, lam, a_expect, verbose=True):
    """chi-kernel of the reduced raising system at both primes, plus sizes."""
    basis, vecs, group = orbit_setup(n, r, delta, lam, verbose)
    nchi = len(vecs)
    rows, nfx = reduced_rows(n, r, delta, lam, vecs, verbose)
    route = 'exact' if nchi <= EXACT_CAP else 'compressed'
    kerns = {}
    for prime in (P1, P2):
        if route == 'exact':
            a, rk, kern = kernel_exact(rows, nchi, prime)
        else:
            a, rk, kern = kernel_compressed(rows, nchi, prime)
            if a != a_expect:
                a, rk, kern = kernel_compressed(rows, nchi, prime, pseed=102)
        assert a == a_expect, ('a mismatch vs plethysm', lam, prime, a, a_expect)
        assert rk == nchi - a, ('rank(R) != n_chi - a', lam, prime, rk, nchi, a)
        kerns[prime] = kern
    return basis, vecs, group, nchi, route, kerns


def exact_vector_onebit(basis, vecs, kerns):
    """CRT+ratrec the a=1 HWV (full monomial coords) to an integer vector."""
    full = {p: expand(vecs, kerns[p][0], p) for p in (P1, P2)}
    # normalise each mod-p exhibit at a common leading monomial
    common = sorted(set(full[P1]) & set(full[P2]))
    assert common, 'primes share no support'
    m0 = common[0]
    for p in (P1, P2):
        inv = pow(full[p][m0], p - 2, p)
        full[p] = {m: v * inv % p for m, v in full[p].items()}
    assert set(full[P1]) == set(full[P2]), 'supports differ after normalisation'
    M = P1 * P2; inv12 = pow(P1, -1, P2)
    vec = {}
    for m in full[P1]:
        a1, a2 = full[P1][m], full[P2][m]
        x = (a1 + P1 * (((a2 - a1) * inv12) % P2)) % M
        q = ratrec(x, M)
        assert q is not None, ('rational reconstruction failed', m, x)
        vec[m] = q
    den = 1
    for q in vec.values(): den = den * q.denominator // gcd(den, q.denominator)
    ivec = {m: int(q * den) for m, q in vec.items()}
    g = 0
    for v in ivec.values(): g = gcd(g, abs(v))
    ivec = {m: v // g for m, v in ivec.items()}
    # must reduce to each mod-p exhibit up to a scalar
    for p in (P1, P2):
        m0 = next(iter(ivec)); lam_ = ivec[m0] * pow(full[p][m0], p - 2, p) % p
        assert all(ivec[m] % p == lam_ * full[p][m] % p for m in ivec), ('mod-p mismatch', p)
    return ivec


def raising_kills_Z(ivec, n, r, lam):
    """apply every simple raising operator over Z (corrected rule); all zero?"""
    for i in range(r - 1):
        j = i + 1
        acc = {}
        for m, cf in ivec.items():
            for p_ in range(len(m)):
                al = m[p_]
                if al[j] == 0: continue
                nb = list(al); nb[j] -= 1; nb[i] += 1
                nm = tuple(sorted(m[:p_] + (tuple(nb),) + m[p_ + 1:]))
                acc[nm] = acc.get(nm, 0) + cf * (al[i] + 1)
        if any(v for v in acc.values()):
            return False, i
    return True, None


def test_onebit(lam, delta, verbose=True):
    n, r = 4, len(lam)
    a_pleth = a_of(lam, delta, 4, 10)
    assert a_pleth == 1, ('one-bit cell must have a=1 by plethysm', lam, a_pleth)
    basis, vecs, group, nchi, route, kerns = build_hwv(n, r, delta, lam, 1, verbose)
    ivec = exact_vector_onebit(basis, vecs, kerns)
    mx = max(abs(v) for v in ivec.values())
    killed, badop = raising_kills_Z(ivec, n, r, lam)
    assert killed, ('raising operator E_%d did not kill the exact vector' % badop, lam)
    # exact-Z sanity: (star) reducible-locus restriction, for the record only
    A = exps(n, r)
    res = dict(lam=lam, delta=delta, r=r, N_S=len(basis), n_chi=nchi, route=route,
               terms=len(ivec), maxcoef=mx)
    # evaluate exactly over Z at independent families
    rnd = random.Random(3900 + sum(lam))
    detvals = [ev_int(ivec, family('det', rnd, r, bound=9)) for _ in range(20)]
    padvals = [ev_int(ivec, family('truepad', rnd, r, bound=9)) for _ in range(20)]
    res['det_nonzero'] = sum(1 for v in detvals if v)
    res['pad_nonzero'] = sum(1 for v in padvals if v)
    # also mod-p evaluation through the reduced pipeline (independent of exact ev)
    K = 20
    for prime in (P1, P2):
        det_ev = point_rows(DET4, N_DET, n, r, basis, vecs, K, 11, 40, prime)
        pad_ev = point_rows(PAD34, N_PAD, n, r, basis, vecs, K, 29, 40, prime)
        res['det_rank_p%d' % (prime % 1000)] = mult_from(kerns[prime], det_ev, 1, prime)
        res['pad_rank_p%d' % (prime % 1000)] = mult_from(kerns[prime], pad_ev, 1, prime)
    res['kind'] = 'onebit'
    # classification
    if res['det_nonzero'] > 0 or res['det_rank_p647'] > 0 or res['det_rank_p629'] > 0:
        res['verdict'] = 'DET_NONVANISH_KILL'
    elif res['pad_nonzero'] > 0 or res['pad_rank_p647'] > 0 or res['pad_rank_p629'] > 0:
        res['verdict'] = 'OBSTRUCTION_CANDIDATE'
    else:
        res['verdict'] = 'clean'      # det zero, pad zero: mult_pad = 0 = mult_det, no obstruction
    save_onebit_vector(lam, delta, ivec, A)
    return res


def ev_int(ivec, F):
    tot = 0
    for m, cf in ivec.items():
        t = cf
        for al in m:
            c = F.get(al, 0)
            if c == 0: t = 0; break
            t *= c
        tot += t
    return tot


def save_onebit_vector(lam, delta, ivec, A):
    os.makedirs(CELLS, exist_ok=True)
    fn = os.path.join(CELLS, '%s_d%d_onebit_exactZ.txt' % ('_'.join(map(str, lam)), delta))
    with open(fn, 'w') as fh:
        fh.write('# weight %s delta %d: exact integer HWV (a=1, m_det=0 one-bit cell); '
                 '%d terms; verified E_i,i+1.v=0 over Z\n' % (lam, delta, len(ivec)))
        for m, v in sorted(ivec.items()):
            fh.write('%s %d\n' % ([list(a) for a in m], v))
    return fn


def test_forced(lam, delta, a_expect, m_det, verbose=True):
    n, r = 4, len(lam)
    basis, vecs, group, nchi, route, kerns = build_hwv(n, r, delta, lam, a_expect, verbose)
    K = 3 * (a_expect + 8)
    ranks = {}
    for prime in (P1, P2):
        pad_ev = point_rows(PAD34, N_PAD, n, r, basis, vecs, K, 907, 40, prime)
        ranks[prime] = mult_from(kerns[prime], pad_ev, a_expect, prime)
    assert len(set(ranks.values())) == 1, ('primes disagree on pad rank', lam, ranks)
    mult_pad = ranks[P1]
    res = dict(lam=lam, delta=delta, r=r, N_S=len(basis), n_chi=nchi, route=route,
               a=a_expect, m_det=m_det, mult_pad=mult_pad, npts=K, kind='forced')
    res['verdict'] = 'OBSTRUCTION_CANDIDATE' if mult_pad >= m_det + 1 else 'clean'
    return res


def bank(line):
    with open(LEDGER, 'a') as fh:
        fh.write(line + '\n'); fh.flush(); os.fsync(fh.fileno())


def n_chi_estimate(lam, delta):
    from wk9_s36_stabred import n_chi_of
    _, nchi, _ = n_chi_of(4, len(lam), delta, lam)
    return nchi


def main(argv):
    cmd = argv[0]
    if cmd == 'onebit':
        lam = tuple(int(x) for x in argv[1].split(',')); delta = int(argv[2])
        r = test_onebit(lam, delta)
        print(r)
        return 0
    if cmd == 'forced':
        lam = tuple(int(x) for x in argv[1].split(',')); delta = int(argv[2])
        a, md = int(argv[3]), int(argv[4])
        r = test_forced(lam, delta, a, md)
        print(r)
        return 0
    if cmd == 'runall':
        csv = argv[1]
        one, forced = [], []
        for ln in open(csv):
            if ln.startswith('delta') or not ln.strip(): continue
            f = ln.strip().split(',')
            delta = int(f[0]); lam = tuple(int(x) for x in f[1].split('|'))
            a, md, cls = int(f[3]), int(f[4]), f[5]
            if cls == 'onebit': one.append((delta, lam, a, md))
            elif cls == 'forced': forced.append((delta, lam, a, md))
        log('one-bit cells: %d ; forced cells: %d' % (len(one), len(forced)))
        # ascending n_chi within each list
        one.sort(key=lambda t: n_chi_estimate(t[1], t[0]))
        forced.sort(key=lambda t: n_chi_estimate(t[1], t[0]))
        cand = None
        for delta, lam, a, md in one:
            log('one-bit test: delta=%d lam=%s' % (delta, lam))
            r = test_onebit(lam, delta)
            bank('| onebit | `%s` | %d | %d | %d | %d | %s | det_nz=%d pad_nz=%d |'
                 % (lam, delta, len(lam), r['N_S'], r['n_chi'], r['verdict'],
                    r['det_nonzero'], r['pad_nonzero']))
            if r['verdict'] != 'clean':
                cand = r; break
        if cand is None:
            for delta, lam, a, md in forced:
                log('forced test: delta=%d lam=%s a=%d m_det=%d' % (delta, lam, a, md))
                r = test_forced(lam, delta, a, md)
                bank('| forced | `%s` | %d | %d | %d | a=%d m_det=%d mult_pad=%d | %s |'
                     % (lam, delta, len(lam), r['N_S'], r['n_chi'], a, md, r['mult_pad'], r['verdict']))
                if r['verdict'] != 'clean':
                    cand = r; break
        if cand is not None:
            with open(DRAFT, 'w') as fh:
                fh.write('# CANDIDATE (draft) — %s\n\n%s\n\nSTOP. Execute results/PREREG_s39.md section 4.\n'
                         % (cand['lam'], cand))
            log('*** CANDIDATE: %s -- session halts, protocol section 4 ***' % (cand['verdict'],))
            return 3
        log('all one-bit and forced cells clean: no obstruction candidate')
        return 0
    print(__doc__); return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
