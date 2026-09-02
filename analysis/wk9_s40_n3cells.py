#!/usr/bin/env python3
"""
Session 40 -- det-side measurements at n = 3 (paper 1's D_5 = D_5^{det_3})
through the validated s36 stabiliser reduction, corrected raising rule, both
house primes.  det points are det_3(sum s_i A_i) with random integer A_i
(box +-40), a + 8 points; a rank attaining a certifies mult_det = a
(det_units = 0); a rank below a fires the sceptical branch (3x points, seed
907, both primes) before it is believed.

    python3 wk9_s40_n3cells.py validate            # gates: n=3 reduced vs unreduced; n=4 I_5 anchor
    python3 wk9_s40_n3cells.py run DELTA NCHI_MAX  # every census cell at DELTA with n_chi <= NCHI_MAX, ascending
    python3 wk9_s40_n3cells.py cell DELTA l1 l2 l3 l4 l5

Ledger: results/n3_ledger.md (appended per cell, committed by the caller).
"""
import sys, os, time, pickle, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import wk9_s36_stabred as sr
from wk9_s36_stabred import measure_reduced, log, P1, P2
from wk8_s30_core import det_form, measure, monomials
from wk8_s30_pleth import a_of

ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, 'results', 'n3_ledger.md')
CELLS = os.path.join(ROOT, 'results', 'logs', 's40_n3cells.pkl')
DET3, N3 = det_form(3)

def use_det3():
    sr.DET4, sr.N_DET = DET3, N3          # measure_reduced reads the module globals at call time

def bank(row):
    new = not os.path.exists(LEDGER)
    with open(LEDGER, 'a') as f:
        if new:
            f.write("# s40 ledger — det side of `I(D_5^{det_3})`, `ell = 5`, reduced pipeline, two primes\n\n"
                    "Each row: `measure_reduced(n=3, r=5, delta, lam)` with det_3 pencils in five variables (box ±40, `a + 8` points, seed 11), "
                    "kernel by the exact route (`n_chi <= 2500`) or the certified compressed route; `a` asserted against the plethysm and `rank(R) = n_chi − a` asserted in-run; "
                    "both primes must agree.  `det_units = a − mult_det`; `= a` is a rank-attaining certificate that the cell is empty.\n\n"
                    "| delta | lam | a | N_S | Stab | n_chi | route | mult_det | det_units | secs | note |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
        f.write(f"| {row['delta']} | `{row['lam']}` | {row['a']} | {row['N_S']} | {row['stab']} | {row['n_chi']} | {row['route']} | "
                f"{row['mult_det']} | {row['a'] - row['mult_det']:+d} | {row['secs']:.0f} | {row['note']} |\n")

def run_cell(delta, lam, sides=('det',)):
    use_det3()
    a = a_of(lam, delta, 3, 5)
    assert a >= 1, (lam, delta, a)
    out = measure_reduced(3, 5, delta, lam, a, sides=sides)
    note = '=a'
    if out['mult_det'] < a:
        log(f"  *** BITE at {lam} delta {delta}: mult_det {out['mult_det']} < a {a} -- sceptical branch")
        out2 = measure_reduced(3, 5, delta, lam, a, sides=sides, npts=3 * (a + 8), seeds=dict(det=907, pad=907))
        note = f"**BITE**: sceptical branch mult_det {out2['mult_det']} at 3(a+8) points seed 907"
        out['sceptical'] = out2['mult_det']
    row = dict(delta=delta, lam=tuple(lam), a=a, N_S=out['N_S'], stab=out['stab'], n_chi=out['n_chi'],
               route=out['route'], mult_det=out['mult_det'], secs=out['secs'], note=note)
    if 'pad' in sides: row['mult_pad'] = out['mult_pad']
    cells = pickle.load(open(CELLS, 'rb')) if os.path.exists(CELLS) else {}
    slim = {k: v for k, v in out.items() if k != 'per_prime'}
    slim['kern_p1'] = out['per_prime'][P1]['kern'] if out['n_chi'] <= 3000 else None
    cells[(delta, tuple(lam))] = slim
    pickle.dump(cells, open(CELLS, 'wb'))
    bank(row)
    monomials.cache_clear()
    return row

def validate():
    use_det3()
    print("== gate (a): n = 3, reduced vs unreduced at three small cells (det side)")
    for delta, lam in ((8, (16, 2, 2, 2, 2)), (8, (14, 4, 2, 2, 2)), (8, (13, 5, 2, 2, 2))):
        a = a_of(lam, delta, 3, 5)
        u = measure(DET3, N3, 3, 5, delta, lam, a_expect=a)
        r = measure_reduced(3, 5, delta, lam, a, sides=('det',), verbose=False)
        print(f"   {lam} delta {delta}: unreduced a={u['a']} N_S={u['nbasis']} mult={u['mult']} | reduced a={r['a']} N_S={r['N_S']} n_chi={r['n_chi']} mult={r['mult_det']}")
        assert u['a'] == r['a'] == a and u['nbasis'] == r['N_S'] and u['mult'] == r['mult_det']
        monomials.cache_clear()
    print("== gate (b): n = 4 anchor (4,4,4,4,4) delta 5 -- the I_5 bite (expect det 1, pad 0)")
    sr.DET4, sr.N_DET = det_form(4)
    r = measure_reduced(4, 5, 5, (4, 4, 4, 4, 4), 1, sides=('det', 'pad'), verbose=False)
    print(f"   (4,4,4,4,4) delta 5: a={r['a']} n_chi={r['n_chi']} mult_det={r['mult_det']} mult_pad={r['mult_pad']}")
    assert r['a'] == 1 and r['mult_det'] == 1 and r['mult_pad'] == 0
    monomials.cache_clear()
    print("GATES PASSED")

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'validate':
        validate()
    elif mode == 'cell':
        delta = int(sys.argv[2]); lam = tuple(int(x) for x in sys.argv[3:8])
        row = run_cell(delta, lam); print(row)
    elif mode == 'run':
        delta = int(sys.argv[2]); cap = int(sys.argv[3])
        cache = pickle.load(open(os.path.join(ROOT, 'results', 'logs', 's40_n3census.pkl'), 'rb'))
        done = pickle.load(open(CELLS, 'rb')) if os.path.exists(CELLS) else {}
        rows = sorted((v for (d, l), v in cache.items() if d == delta and v['n_chi'] <= cap and not v['approx']),
                      key=lambda v: (v['n_chi'], v['lam']))
        print(f"delta {delta}: {len(rows)} cells with n_chi <= {cap}; {sum(1 for v in rows if (delta, v['lam']) in done)} already done")
        for v in rows:
            if (delta, v['lam']) in done: continue
            t = time.time()
            row = run_cell(delta, v['lam'])
            print(f"  {v['lam']} a={row['a']} n_chi={row['n_chi']} mult_det={row['mult_det']} {row['note']} [{time.time()-t:.0f}s]", flush=True)
            if row['mult_det'] < row['a']:
                print("STOP: bite -- no further cells (pre-registered)"); break
