#!/usr/bin/env python3
"""
Session 39 -- independent verification of the completed screen, at the degrees
(delta = 10, 11, 12) the C engine self-test could not reach through s38's table.

  A. `a` cross-check: the C engine `a(lam,delta)` vs the house plethysm
     `wk8_s30_pleth.a_of` (a DIFFERENT plethysm implementation) at a random
     sample of screened cells per delta -- both must agree.
  B. `m_det` cross-check: the C engine `m_det(lam)` vs the house
     `scripts/ambient_screen.m_det` (independent Murnaghan-Nakayama) at a random
     sample where the house routine is affordable (delta = 10; N = 40).  At
     delta = 11, 12 the house character sum over partitions of 44, 48 is beyond
     the house memory wall (s38), so m_det there stands on: the C engine's exact
     agreement with the house at delta <= 9 (708 cells at delta 9), the per-cell
     exact asserts (g >= 0, |T| <= g, g+T even) that ran on every screened cell,
     and the two-prime CRT.  We re-assert those invariants on a delta=11,12
     sample here for the record.
  C. the classification is monotone-consistent: every banked cell has
     a <= m_det (silent), and there is no a=1,m_det=0 or a>m_det row.

usage: python3 wk9_s39_verify.py            -> appends results/s39_verify.md
"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'scripts'))
from wk9_s39_chars import PlethEngine, MdetEngine, LIB, partitions, crt_signed
import ambient_screen as hs
from wk8_s30_core import monomials, build_R, rank_of, P1 as FP1

OUT = os.path.join(HERE, '..', 'results', 's39_verify.md')
CSV = os.path.join(HERE, '..', 'results', 'longweight_screen.csv')


def emit(s):
    print(s, flush=True)
    with open(OUT, 'a') as fh: fh.write(s + '\n')


def load_rows():
    rows = {}
    for ln in open(CSV):
        if ln.startswith('delta') or not ln.strip(): continue
        f = ln.strip().split(',')
        d = int(f[0]); lam = tuple(int(x) for x in f[1].split('|'))
        rows.setdefault(d, []).append((lam, int(f[3]), int(f[4]), f[5]))
    return rows


def main():
    open(OUT, 'w').write('# Session 39 — independent verification of the completed screen\n\n')
    rows = load_rows()
    rnd = random.Random(3939)
    ok = True

    # C — global classification invariant over ALL banked rows
    emit('## C. Classification invariant (all %d cells with a>=1, exhaustive)\n'
         % sum(1 for d in rows for (lam, a, md, cls) in rows[d] if a >= 1))
    nbad = nonsilent = 0
    for d in rows:
        for lam, a, md, cls in rows[d]:
            if a >= 1 and not (a <= md and cls == 'silent'):
                nbad += 1
            if cls in ('onebit', 'forced'):
                nonsilent += 1
    emit('- rows violating `a <= m_det` / not classified silent: **%d**' % nbad)
    emit('- one-bit or forced rows: **%d**' % nonsilent)
    ok &= (nbad == 0 and nonsilent == 0)
    emit('- verdict: %s\n' % ('**every a>=1 cell has a <= m_det; occurrence route silent** ✓'
                              if nbad == 0 and nonsilent == 0 else '**FAIL**'))

    # A1 — a cross-check against the house per-weight plethysm at delta 10,11,12
    emit('## A. `a` — independent confirmation at δ=10,11,12\n')
    emit('### A1. C engine vs house per-weight plethysm `ambient_screen.a` '
         '(different chi and different plethysm code)\n')
    emit('| δ | sample cells | mismatches |')
    emit('|---|---|---|')
    for delta in (10, 11, 12):
        PE = PlethEngine(delta, d=4)
        sample = rnd.sample(rows[delta], min(30, len(rows[delta])))
        bad = 0
        for i, (lam, a, md, cls) in enumerate(sample):
            ce = PE.a(lam)
            hv = hs.a(lam, delta, d=4, nv=10)
            if not (ce == hv == a): bad += 1; emit('  MISMATCH %s C=%d house=%d banked=%d' % (lam, ce, hv, a))
            if (i + 1) % 8 == 0: hs.chi.cache_clear()
        hs.chi.cache_clear()
        emit('| %d | %d | %d |' % (delta, len(sample), bad))
        ok &= (bad == 0)
    emit('')

    # A2 — a vs dim ker R (flint raising-operator kernel): the fully independent route,
    # on the lowest-N_S cells reachable (peaked long weights)
    emit('### A2. C engine `a` vs `dim ker R` (flint raising operators, s30 pipeline) '
         'on the lowest-N_S cells\n')
    emit('| δ | λ | ℓ | N_S | a (C) | N_S − rank(R) | agree |')
    emit('|---|---|---|---|---|---|---|')
    for delta in (10, 11, 12):
        # peaked cells (large lam_1) have the smallest N_S; sort cheaply by -lam_1,
        # then compute N_S only for the top few and take the two smallest <= cap.
        peaked = sorted((r for r in rows[delta] if r[1] >= 1), key=lambda r: (-r[0][0], r[0][1:]))[:12]
        sized = []
        for lam, a, md, cls in peaked:
            ns = len(monomials(4, len(lam), delta, lam))
            sized.append((ns, lam, a))
        sized.sort()
        done = 0
        for ns, lam, a in sized:
            if ns > 6000 or done >= 2: continue
            basis, R = build_R(4, len(lam), delta, lam)
            adef = len(basis) - rank_of(R, len(basis), FP1)
            good = (adef == a); ok &= good; done += 1
            emit('| %d | `%s` | %d | %d | %d | %d | %s |'
                 % (delta, lam, len(lam), ns, a, adef, '✓' if good else '**FAIL**'))
        if done == 0:
            emit('| %d | (lowest N_S peaked cell exceeds the flint cap 6000) | — | %d | — | — | n/a |'
                 % (delta, sized[0][0]))
    emit('')

    # B — m_det cross-check against the house at delta 10 (affordable), invariants at 11,12
    emit('## B. `m_det` — C engine vs house `ambient_screen.m_det` (independent MN)\n')
    ME10 = MdetEngine(10, n=4)
    sample = rnd.sample([r for r in rows[10] if r[1] >= 1], 15)
    bad = 0
    t0 = time.time()
    for lam, a, md, cls in sample:
        hv = hs.m_det(lam, 4, 10)
        hs.chi.cache_clear()
        ce = ME10.m_det(lam)
        if not (ce == hv == md): bad += 1
    emit('- δ=10, N=40: %d random cells, C engine vs house m_det mismatches: **%d** [%.0fs]'
         % (len(sample), bad, time.time() - t0))
    ok &= (bad == 0)
    for delta in (11, 12):
        ME = MdetEngine(delta, n=4)
        sample = rnd.sample([r for r in rows[delta] if r[1] >= 1], 20)
        bad = 0
        for lam, a, md, cls in sample:
            g, T = ME.gT(lam)                       # re-asserts g>=0, |T|<=g, parity internally
            if (g + T) // 2 != md: bad += 1
        emit('- δ=%d, N=%d: %d random cells, C engine invariants (g≥0, |T|≤g, g+T even) re-hold '
             'and (g+T)/2 = banked m_det: mismatches **%d** '
             '(house m_det beyond its memory wall at N=%d — s38)'
             % (delta, 4 * delta, len(sample), bad, 4 * delta))
        ok &= (bad == 0)
    emit('')

    # tightest cells per delta (for the doc)
    emit('## Tightest margins per δ (smallest `m_det − a` among a>=1 cells)\n')
    emit('| δ | λ | ℓ | a | m_det | margin |')
    emit('|---|---|---|---|---|---|')
    for delta in sorted(rows):
        cells = [(md - a, lam, len(lam), a, md) for lam, a, md, cls in rows[delta] if a >= 1]
        m = min(cells)
        emit('| %d | `%s` | %d | %d | %d | %d |' % (delta, m[1], m[2], m[3], m[4], m[0]))
    emit('')
    emit('**VERIFICATION %s**' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
