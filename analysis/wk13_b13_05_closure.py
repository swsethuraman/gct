#!/usr/bin/env python3
"""
B13-05 -- the product-closure engine (Theorem F).

Theorem F.  X irreducible, I = I(X).  If h_kappa is a weight-kappa highest-weight vector of degree p
with h_kappa not in I, and h_nu one of weight nu and degree q with h_nu not in I, then h_kappa . h_nu is
a weight-(kappa+nu) highest-weight vector of degree p+q and is not in I (C[X] is a domain).  Hence

    i(kappa, p) = 0  and  i(nu, q) = 0   ==>   mult(kappa+nu, p+q) >= 1,   i.e. i <= a - 1,
                                          and  i(kappa+nu, p+q) = 0  whenever  a(kappa+nu, p+q) = 1.

(i(kappa,p) = 0 says the whole weight-kappa HW space injects into C[X], so EVERY nonzero HWV of that
weight is nonzero in C[X]; no choice of vector is involved.)  By the restriction lemma i(kappa,p) does
not depend on the ambient r >= ell(kappa), so blocks of any length combine at the target's length.

Seed blocks (i = 0, from the record and from this session):
    ell <= 5, every degree            washout_lemma Thm 2 + the restriction lemma      ADOPTED
    ell  = 6, delta <= 9              s37 / s43 / s41+s47 / s79                        ADOPTED (certified)
    ell  = delta (top cells)          this session, exact integer catalecticant minors CERTIFIED
Iterated to a fixed point.

usage: python3 analysis/wk13_b13_05_closure.py [--dmax 9] [--out results/b13_05_closure.json]
board_numbering: batch13
"""
import sys, os, json, time, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


def is_partition(v):
    return all(v[i] >= v[i + 1] for i in range(len(v) - 1)) and (len(v) == 0 or v[-1] >= 0)


def trim(v):
    v = list(v)
    while v and v[-1] == 0: v.pop()
    return tuple(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--census', default='results/b13_05_census.json')
    ap.add_argument('--dmax', type=int, default=9)
    ap.add_argument('--out', default='results/b13_05_closure.json')
    args = ap.parse_args()
    cen = json.load(open(args.census))
    A = {}                      # (delta, mu) -> a
    bydeg = {}
    for r in cen['rows']:
        mu = tuple(r['mu']); d = r['delta']
        A[(d, mu)] = r['a']
        bydeg.setdefault(d, []).append(mu)

    # ---- seed blocks
    known = {}                  # (delta, mu) -> reason
    for (d, mu), a in A.items():
        if len(mu) <= 5:
            known[(d, mu)] = 'inherited: ell <= 5, washout_lemma Thm 2 + restriction lemma (PROVED)'
        elif len(mu) == 6 and d <= 9:
            known[(d, mu)] = 'inherited: ell = 6, certified length-6 record s37/s43/s41+s47/s79 (CERTIFIED)'
        elif len(mu) == d:
            known[(d, mu)] = 'top cell: exact catalecticant maximal minor nonzero at a per_3 pencil (CERTIFIED, this session)'
    seed_n = len(known)
    print(f'seed blocks with i = 0: {seed_n} of {len(A)} census cells')

    # ---- iterate Theorem F to a fixed point
    derived = {}
    partial = {}                # a >= 2 cells where a product exists: i <= a - 1
    it = 0
    while True:
        it += 1
        new = 0
        for d in range(2, args.dmax + 1):
            for mu in bydeg.get(d, []):
                if (d, mu) in known: continue
                hits = []
                for p in range(1, d):
                    q = d - p
                    for kap in bydeg.get(p, []):
                        if (p, kap) not in known: continue
                        if len(kap) > len(mu): continue
                        nu = trim(tuple(mu[i] - (kap[i] if i < len(kap) else 0) for i in range(len(mu))))
                        if any(x < 0 for x in nu) or not is_partition(nu): continue
                        if (q, nu) not in A or (q, nu) not in known: continue
                        hits.append(dict(p=p, kappa=list(kap), q=q, nu=list(nu)))
                        if len(hits) >= 4: break
                    if len(hits) >= 4: break
                if not hits: continue
                if A[(d, mu)] == 1:
                    known[(d, mu)] = 'Theorem F: product of two known-empty highest-weight vectors, a = 1 (PROVED)'
                    derived[(d, mu)] = hits
                    new += 1
                else:
                    partial[(d, mu)] = dict(a=A[(d, mu)], bound='i <= a - 1', witnesses=hits)
        # ---- Theorem D (the ladder), downward: i(M, D) = 0 and M = mu + nu, a(nu, D-d) >= 1  ==>  i(mu, d) = 0
        for d in range(1, args.dmax):
            for mu in bydeg.get(d, []):
                if (d, mu) in known: continue
                hits = []
                for q in range(1, args.dmax + 1 - d):
                    D = d + q
                    for nu in bydeg.get(q, []):
                        L = max(len(mu), len(nu))
                        M = trim(tuple((mu[i] if i < len(mu) else 0) + (nu[i] if i < len(nu) else 0) for i in range(L)))
                        if not is_partition(M) or (D, M) not in known: continue
                        hits.append(dict(successor_delta=D, successor_mu=list(M), nu=list(nu), nu_delta=q))
                        if len(hits) >= 4: break
                    if len(hits) >= 4: break
                if hits:
                    known[(d, mu)] = 'Theorem D (ladder, downward): a known-empty successor mu + nu at degree d + q (PROVED)'
                    derived[(d, mu)] = hits
                    new += 1
        print(f'  iteration {it}: {new} newly closed (Theorem F upward + Theorem D downward)')
        if new == 0: break

    # ---- report
    out = dict(board_numbering='batch13', session='B13-05', theorem='F (product closure)',
               seed_blocks=seed_n, census_cells=len(A), closed=len(known), iterations=it,
               derived=[dict(delta=d, mu=list(mu), a=A[(d, mu)], witnesses=w) for (d, mu), w in sorted(derived.items())],
               partial=[dict(delta=d, mu=list(mu), **v) for (d, mu), v in sorted(partial.items())],
               open=[])
    print()
    for d in range(7, args.dmax + 1):
        for ell in (7, 8, 9):
            cells = [mu for mu in bydeg.get(d, []) if len(mu) == ell]
            if not cells: continue
            nk = sum(1 for mu in cells if (d, mu) in known)
            nd = sum(1 for mu in cells if (d, mu) in derived)
            npart = sum(1 for mu in cells if (d, mu) in partial)
            print(f'delta={d} ell={ell}: {len(cells)} cells, {nk} closed ({nd} newly by Theorem F), '
                  f'{npart} bounded i<=a-1, {len(cells)-nk} open')
    for d in range(1, args.dmax + 1):
        for mu in bydeg.get(d, []):
            if (d, mu) not in known:
                out['open'].append(dict(delta=d, mu=list(mu), a=A[(d, mu)], ell=len(mu),
                                        bounded=(d, mu) in partial))
    print(f'\nTOTAL open after Theorem F: {len(out["open"])} of {len(A)} census cells '
          f'(of which {sum(1 for o in out["open"] if o["bounded"])} have i <= a-1)')
    json.dump(out, open(args.out, 'w'), indent=0)
    print('wrote', args.out)


if __name__ == '__main__':
    main()
