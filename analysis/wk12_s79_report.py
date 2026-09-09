#!/usr/bin/env python3
"""Session 79 -- tables for the report from the banked jsonl records."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))


def load(path):
    out = []
    if os.path.exists(path):
        for ln in open(path):
            try: out.append(json.loads(ln))
            except Exception: pass
    return out


def stable_table():
    rows = []
    for tag in ('6_3_3_1', '4_4_3_2', '6_2_2_2_1', '5_3_2_2_1', '5_2_2_2_2'):
        p = os.path.join(ROOT, 'results', 's79_stable', f'stable_{tag}_summary.json')
        if not os.path.exists(p): continue
        r = json.load(open(p))
        pp = r['per_prime']
        rows.append("| `(%s)` | %d | %d | %s | %s | %s | %s | %s | %.0f |" % (
            ','.join(str(x) for x in r['rho'] if x), r['a_inf'], r['raw_weight_space'],
            ' / '.join(str(pp[str(q)]['nullity']) for q in r['primes']),
            ' / '.join(str(pp[str(q)]['mult_det_inf']) for q in r['primes']),
            r['i_det_inf'], 'PASS' if r['covariance_all_pass'] else 'FAIL',
            ' / '.join(('%d/4' % pp[str(q)]['negative_control_random']['raisings_failed']) for q in r['primes']), r['secs']))
    hdr = ("| `ρ` | `a_∞` | raw space | nullity (P1 / P2) | `mult_det^∞` (P1 / P2) | `i_det^∞` | covariance | random-vector control fails | secs |\n"
           "|---|---|---|---|---|---|---|---|---|\n")
    return hdr + '\n'.join(rows) + '\n'


def cells_table(path, title):
    rows = load(path)
    rows.sort(key=lambda r: (r['delta'], -r['lam'][0], r['lam']))
    lines = [f"# {title}", "", f"{len(rows)} cells, both house primes, four families (`K = a + 8` points each), hybrid route (length-general driver).", "",
             "| `λ` | `δ` | `a` | `N_S` | `n_χ` | `mult_det` | `mult_pad` | `mult_red` (★ / pts) | `mult_per4` | `i_det` | `pad<red` | `D` | secs |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append("| `(%s)` | %d | %d | %d | %d | %s | %s | %s / %s | %s | %s | %s | %s | %.0f |" % (
            ','.join(map(str, r['lam'])), r['delta'], r['a'], r['N_S'], r['n_chi'], r['mult_det'], r['mult_pad'], r['mult_red_star'], r['mult_red_pts'],
            r['mult_per4'], r['i_det'], r['pad_lt_red'], r['D'], r['secs']))
    return '\n'.join(lines) + '\n', rows


def per6_table(path, delta):
    rows = [r for r in load(path) if r['delta'] == delta]
    rows.sort(key=lambda r: r.get('N_S', 0))
    lines = [f"# `I(D_6^{{per_3}})_{delta}` on the cubic side — session 79", "",
             f"{len(rows)} length-6 weights `μ ⊢ {3*delta}` with `a(μ,{delta}) ≥ 1` in `Sym^{delta}(Sym^3 C^6)`, points `per_3(Σ s_i A_i)` (seed 41, bound 40, `a + 8`), both house primes, hybrid route.", "",
             "| `μ` | `a` | `N_S` | Stab | `n_χ` | `mult` | units | secs |", "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append("| `(%s)` | %d | %d | %d | %d | %s | %s | %.0f |" % (','.join(map(str, r['mu'])), r['a'], r['N_S'], r['stab'], r['n_chi'], r['mult'], r['units'], r['secs']))
    return '\n'.join(lines) + '\n', rows


if __name__ == '__main__':
    open(os.path.join(ROOT, 'results', 's79_stable_blocks.md'), 'w').write("# The five `a_∞ = 4` weight-13 stable blocks — session 79\n\n" + stable_table())
    t, rows = cells_table(os.path.join(ROOT, 'results', 's79_cells.jsonl'), "The `ℓ = 6` cells measured — session 79")
    open(os.path.join(ROOT, 'results', 's79_cells.md'), 'w').write(t)
    c = collections.Counter((r['i_det'] == 0, r['pad_lt_red'], r['i_per4'] == 0, r['mult_pad'] == r['mult_red']) for r in rows)
    print("cells:", len(rows), dict(c))
    print("  by delta:", dict(collections.Counter(r['delta'] for r in rows)))
    print("  D_R < 0 (reducible drops):", sum(1 for r in rows if r['D_R'] < 0), " max |D_R|:", -min([r['D_R'] for r in rows] + [0]))
    print("  total secs:", round(sum(r['secs'] for r in rows)), " max secs:", max([r['secs'] for r in rows] + [0]), " max n_chi:", max([r['n_chi'] for r in rows] + [0]))
    for d in (9, 10):
        t, rows = per6_table(os.path.join(ROOT, 'results', 's79_per6.jsonl'), d)
        if rows:
            open(os.path.join(ROOT, 'results', f's79_per6_d{d}.md'), 'w').write(t)
            print(f"per6 d{d}:", len(rows), "weights; units>0:", sum(1 for r in rows if r['units']), "; total secs", round(sum(r['secs'] for r in rows)),
                  "; max N_S", max(r['N_S'] for r in rows), "; max n_chi", max(r['n_chi'] for r in rows))
