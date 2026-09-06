#!/usr/bin/env python3
"""
Session 57 -- the short ladders: every tail lam_bar with |lam_bar| <= SIZE_MAX and
exactly ell - 1 parts, ell = 6..10.  For each ladder:

  a_inf            the stable value of a (Proposition S), and the threshold |lam_bar|
  record           the measured cells on the ladder (delta, a, dead) and whether one of
                   them already has a = a_inf ('permanently dead': i_det = 0 at every
                   cell above it, Lemma L + Proposition S)
  a at delta 10-12 from the table, and the first delta where a = a_inf is observed
  first stable cell in the region, its N_S / n_chi estimate (table, or the modular DP)
  K_inf            the slice monomial count at tail weight lam_bar, and K_inf / |Stab'|:
                   the size of the stable-range computation done on the slice
  sk_inf_lb        sk at the first stable cell if tabulated (a lower bound for the stable sk)

Output: results/s57_cells/short_ladders.json and a printed table.
usage: python3 wk9_s57_shortladders.py [--size-max 12] [--ells 6,7,8,9,10]
"""
import sys, os, json, glob, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (partitions_exact, ladder_cell, negative_record, stab_order, tail_of, load_s39,
                         K_mod, crt2, merged_lower_bound, a_weyl_mod, gzip_copy, P1, P2, ROOT, log)
from wk9_s57_stable import a_inf, K_inf_mod
from wk9_s57_table import ns_cost, reach_class

CELLS = os.path.join(ROOT, 'results/s57_cells')

def load_table():
    T = {}
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')):
        for ln in open(p):
            r = json.loads(ln); T[(tuple(r['lam']), r['delta'])] = r
    fam = {}
    p = os.path.join(CELLS, 'bank_families.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln)
            if r['value'] is None: continue
            fam.setdefault((tuple(r['lam']), r['delta']), {})[r['col']] = r
    return T, fam

if __name__ == '__main__':
    args = sys.argv[1:]
    size_max = int(args[args.index('--size-max') + 1]) if '--size-max' in args else 12
    ells = [int(x) for x in args[args.index('--ells') + 1].split(',')] if '--ells' in args else [6, 7, 8, 9, 10]
    rec = negative_record(); s39, zeros = load_s39(); T, fam = load_table()
    wcache = {}
    def a_of(lam, d, compute=False):
        k = (lam, d)
        if k in T: return T[k]['a']
        if k in s39: return s39[k][0]
        if k in zeros: return 0
        if k in rec: return rec[k][0]
        if k in fam:
            for col in ('a_engine', 'a_weyl'):
                if col in fam[k]: return fam[k][col]['value']
        if compute:
            try:
                v, _, _ = a_weyl_mod(lam, d, 4, wcache, box_cap=3e7, terms_cap=5000)
                computed[k] = v
                return v
            except MemoryError:
                return None
        return None
    computed = {}
    out = []
    cache = {}
    for ell in ells:
        for m in range(ell - 1, size_max + 1):
            for tail in partitions_exact(m, ell - 1):
                t0 = time.time()
                ai = a_inf(tail, cache)
                so = stab_order(tail)
                kinf = crt2(K_inf_mod(tail, P1), K_inf_mod(tail, P2))
                cells = []
                for d in range(ell, 25):
                    lam = ladder_cell(tail, d)
                    if lam is None: continue
                    a = a_of(lam, d)
                    dead = (lam, d) in rec
                    cells.append(dict(delta=d, lam=list(lam), a=a, dead=dead, eligible=lam[0] >= d, stable_bound=d >= m))
                perm_dead = [c for c in cells if c['dead'] and c['a'] == ai]
                first_stab_obs = next((c['delta'] for c in cells if c['a'] == ai), None)
                # the first stable cell inside the region (delta >= 10): delta_first = max(10, first observed stable delta or m)
                d_first = max(10, first_stab_obs if first_stab_obs is not None else m)
                lam_first = ladder_cell(tail, d_first)
                ns = st = nchi = None
                if lam_first is not None:
                    k = (lam_first, d_first)
                    if k in T and T[k].get('N_S') is not None:
                        ns, st, nchi = T[k]['N_S'], T[k]['N_S_status'], T[k]['nchi_est']
                    elif k in fam and 'N_S' in fam[k]:
                        ns, st, nchi = fam[k]['N_S']['value'], fam[k]['N_S']['status'], fam[k]['N_S']['nchi_est']
                    else:
                        cost, box = ns_cost(lam_first, d_first)
                        if cost <= 2e9:
                            ns = crt2(K_mod(lam_first, d_first, 4, P1), K_mod(lam_first, d_first, 4, P2)); st = 'exact'
                        else:
                            ns = merged_lower_bound(lam_first, d_first); st = 'lb'
                        nchi = -(-ns // stab_order(lam_first))
                if lam_first is not None and ai >= 1 and a_of(lam_first, d_first) is None:
                    a_of(lam_first, d_first, compute=True)
                sk_first = None
                if lam_first is not None:
                    k = (lam_first, d_first)
                    if k in T: sk_first = T[k].get('sk')
                    elif k in s39: sk_first = s39[k][1]
                    elif k in fam and 'sk' in fam[k]: sk_first = fam[k]['sk']['value']
                row = dict(ell=ell, tail=list(tail), size=m, a_inf=ai, stab_tail=so, K_inf=kinf, K_inf_over_stab=-(-kinf // so),
                           cells=cells, permanently_dead=bool(perm_dead), perm_dead_at=(perm_dead[0]['delta'] if perm_dead else None),
                           any_dead=any(c['dead'] for c in cells), first_stable_observed=first_stab_obs,
                           first_region_stable=dict(delta=d_first, lam=list(lam_first) if lam_first else None, N_S=ns, N_S_status=st,
                                                    nchi_est=nchi, reach=(reach_class(nchi, st) if nchi is not None else None), sk=sk_first,
                                                    a=a_of(lam_first, d_first) if lam_first else None),
                           secs=round(time.time() - t0, 2))
                out.append(row)
        log(f"ell {ell}: {sum(1 for r in out if r['ell'] == ell)} tails")
    json.dump(out, open(os.path.join(CELLS, 'short_ladders.json'), 'w'))
    gzip_copy(os.path.join(CELLS, 'short_ladders.json'))
    if computed:
        with open(os.path.join(CELLS, 'bank_shortladders_a.jsonl'), 'a') as fh:
            for (lam, d), v in computed.items():
                fh.write(json.dumps(dict(lam=list(lam), delta=d, ell=len(lam), a=v, route='Weyl (modular DP, two primes)')) + "\n")
        log(f"{len(computed)} first-stable-cell a values computed by the Weyl route and banked")
    # summary
    for ell in ells:
        rows = [r for r in out if r['ell'] == ell]
        pd = sum(1 for r in rows if r['permanently_dead']); ad = sum(1 for r in rows if r['any_dead'])
        log(f"ell {ell}: {len(rows)} ladders with |tail| <= {size_max}; permanently dead {pd}; touched by the record {ad}; untouched {len(rows) - ad}")
    print("| ell | tail | size | a_inf | record cells (delta:a, * = dead) | permanently dead | first stable region cell | a | sk | n_chi~ | reach | K_inf/|Stab'| |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in out:
        rc = ", ".join(f"{c['delta']}:{c['a']}{'*' if c['dead'] else ''}" for c in r['cells'] if c['delta'] <= 12 and c['a'] is not None)
        f = r['first_region_stable']
        print(f"| {r['ell']} | `{tuple(r['tail'])}` | {r['size']} | {r['a_inf']} | {rc} | {'yes @' + str(r['perm_dead_at']) if r['permanently_dead'] else 'no'} | "
              f"`{tuple(f['lam']) if f['lam'] else '-'}` δ={f['delta']} | {f['a']} | {f['sk']} | {f['nchi_est']} ({f['N_S_status']}) | {f['reach']} | {r['K_inf_over_stab']} |")
