"""B19-05: re-run of the B18-05 generic-quartic control with FULL monomial support.

The B18-05 run-1 control used a sparse random quartic (<= 60 of the 715 degree-4
monomials in ten variables).  It happened to contain no t^k x_1^(4-k) monomial, so
p(t) = F(t, e_1) collapsed to t^4, every E vanished, and `w.E != 0` was never
tested.  This script rebuilds the control with a quartic in which EVERY one of the
715 monomials has a nonzero integer coefficient (so no chart quantity can vanish
for support reasons), keeps [t^4] = 1 (c = 1, on chart), and evaluates the same
eleven-equation vector E with the unchanged B18-05 evaluator (imported, not
copied).  It then reports w.E and kappa.E exactly, plus the size of what it
checked (nonzero coefficient count, p(t) coefficients, degrees of the interpolated
t-polynomials) so the check cannot pass vacuously.

Also re-runs the ORIGINAL degenerate control (seeded exactly as in b18_05_psi.py,
rng seed 1805 after the two det4 draws) to show the two differ only in support.

Run only through analysis/b15_bound.py (60 s / 512 MiB).  Writes only
results/b19_05/control_full_support.json.
"""
import json, os, random, sys, time
from pathlib import Path
from itertools import combinations_with_replacement

sys.path[:0] = [str(Path('analysis').resolve())]
from b18_05_psi import Quartic, equations, rand_matrix, det4, W, KAPPA, NAMES  # noqa: E402

OUT = Path('results/b19_05')
OUT.mkdir(parents=True, exist_ok=True)
t0 = time.perf_counter()
ID10 = [[int(i == j) for j in range(10)] for i in range(10)]
report = {}


def monomials_deg4():
    for idx in combinations_with_replacement(range(10), 4):
        d = {}
        for v in idx:
            d[v] = d.get(v, 0) + 1
        yield tuple(sorted(d.items()))


def tk_x1(k):
    """Monomial key for t^k x_1^(4-k) in the b18_05_psi dictionary convention."""
    if k == 4:
        return ((0, 4),)
    if k == 0:
        return ((1, 4),)
    return ((0, k), (1, 4 - k))


def summarize(P, r, label):
    E = r['E']
    p = r['p']
    return dict(
        label=label,
        monomials_nonzero=sum(1 for c in P.values() if c),
        monomials_total=715,
        has_t4=P.get(((0, 4),), 0),
        tk_x1_monomials_present=[k for k in range(5) if P.get(tk_x1(k), 0) != 0],
        p_coeffs_low_to_high=[str(x) for x in p],
        p_is_t4_only=all(x == 0 for x in p[:4]),
        interpolated_degrees=r['polydeg'],
        E_values=[str(e) for e in E],
        E_nonzero_count=sum(1 for e in E if e != 0),
        w_E=str(r['w_E']), w_E_nonzero=r['w_E'] != 0,
        kappa_E=str(r['kappa_E']), kappa_E_nonzero=r['kappa_E'] != 0,
        ambient_identity_residual=str(r['ambient_identity_residual']),
        psi_direct_equals_wE=r['psi_direct'] == r['w_E'],
    )


# ---- (A) the original degenerate control, reproduced exactly as in b18_05_psi.py ----
rng = random.Random(1805)
for k in range(2):                       # the two det4 draws consumed before control 3
    rand_matrix(rng, 16, 10, 7)
Pgen = {}
for _ in range(60):
    idx = sorted(rng.randrange(10) for _ in range(4))
    d = {}
    for v in idx:
        d[v] = d.get(v, 0) + 1
    Pgen[tuple(sorted(d.items()))] = rng.randint(-4, 4)
Pgen[((0, 4),)] = 1
rA = equations(Quartic(Pgen, ID10))
report['A_original_sparse_control'] = summarize(Pgen, rA, 'B18-05 run-1 control, reproduced')
print(json.dumps(report['A_original_sparse_control']), flush=True)

# ---- (B) full-support quartic, deterministic seed, every coefficient nonzero ----
results_B = []
for seed in (190501, 190502, 190503):
    rg = random.Random(seed)
    P = {}
    for mono in monomials_deg4():
        c = 0
        while c == 0:
            c = rg.randint(-9, 9)
        P[mono] = c
    P[((0, 4),)] = 1                     # monic in t: c = [t^4] F = 1, on chart
    assert len(P) == 715 and all(P.values())
    r = equations(Quartic(P, ID10))
    s = summarize(P, r, f'full support, seed {seed}')
    s['seed'] = seed
    results_B.append(s)
    print(json.dumps(dict(seed=seed, w_E=s['w_E'], w_E_nonzero=s['w_E_nonzero'],
                          kappa_E_nonzero=s['kappa_E_nonzero'], E_nonzero_count=s['E_nonzero_count'],
                          p=s['p_coeffs_low_to_high'])), flush=True)
report['B_full_support_controls'] = results_B

# ---- (C) det4 control, unchanged from B18-05, to show the evaluator still returns E = 0 there ----
rngd = random.Random(1805)
M = rand_matrix(rngd, 16, 10, 7)
rd = equations(Quartic(det4(), M))
report['C_det4_control'] = dict(all_E_zero=all(e == 0 for e in rd['E']), w_E=str(rd['w_E']))
print(json.dumps(report['C_det4_control']), flush=True)

report['verdict'] = dict(
    original_control_measured_nothing=report['A_original_sparse_control']['p_is_t4_only'],
    full_support_w_E_nonzero_all=all(s['w_E_nonzero'] for s in results_B),
    full_support_kappa_E_nonzero_all=all(s['kappa_E_nonzero'] for s in results_B),
)
report['wall_seconds'] = time.perf_counter() - t0
report['W'] = W
report['KAPPA'] = KAPPA
report['E_names'] = NAMES
(OUT / 'control_full_support.json').write_text(json.dumps(report, indent=1) + '\n')
print(json.dumps(report['verdict']), flush=True)
