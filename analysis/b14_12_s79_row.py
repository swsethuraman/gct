#!/usr/bin/env python3
"""
B14-12 -- emit session-79-schema rows for the two Q1 cells that are closed but sit
outside results/s79_cells.jsonl.

B13-10 section 6.1 defect 3: its pilot's result "is in results/b13_10/pilot.json and is
not merged into results/s79_cells.jsonl, whose schema carries four families and
not one."  The same would be true of this session's cell.  This script writes
both rows in that file's own field set, with every field this session did not
produce set to null and NAMED in `absent_fields` rather than filled with a
plausible-looking value.

It does NOT append to results/s79_cells.jsonl: that file is session 79's delivery
and its rows all carry four families and certificates; merging a row with named
gaps into it is an integration decision, not a worker's.

usage: python3 analysis/b14_12_s79_row.py [--out results/b14_12/s79_schema_rows.jsonl]
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))

SCHEMA = sorted(json.loads(open(os.path.join(ROOT, 'results', 's79_cells.jsonl')).readline()).keys())


def row_from(core, fam, queue, note, absent):
    b = core['build']
    r = {k: None for k in SCHEMA}
    r.update(lam=core['lam'], delta=core['delta'], ell=len(core['lam']), a=core['a'],
             N_S=b['N_S'], stab=b['stab'], n_chi=b['n_chi'], nrows=b['nrows'], nnz=b['nnz'],
             nfixed=b['nfixed'], NS_delta=b['N_S'] * core['delta'],
             build_secs=round(b['secs'], 1), build_hwm_gb=round(b['hwm_gb'], 2),
             primes=core['primes'], bound=core['bound'], K=core['a'] + 8,
             route='hybrid, lean builder (wk13_b10_lean) driven by analysis/b14_12_cell.py',
             cost_model='PROVED.md: cost_model (B13-09 sec 4): build_secs ~ 3.06e-6*N_S*delta + 1.07e-6*|Stab|*N_S',
             primes_concurrent=False, mult_det=core.get('mult_det'), i_det=core.get('i_det'))
    if fam:
        r.update(seeds=fam['seeds'], n_red=fam['n_red'], cover_E=fam['cover_E'], cover_Ered=fam['cover_Ered'],
                 sieve_secs=fam['sieve_secs'], sides=fam['sides'], per_prime=fam['per_prime'],
                 mult_pad=fam['mult_pad'], mult_per4=fam['mult_per4'], mult_red=fam['mult_red'],
                 mult_red_pts=fam['mult_red_pts'], mult_red_star=fam['mult_red_star'],
                 i_pad=fam['i_pad'], i_red=fam['i_red'], i_per4=fam['i_per4'],
                 D=fam['D'], D_R=fam['D_R'], pad_lt_red=fam['pad_lt_red'], monotone_ok=fam['monotone_ok'],
                 star_eq_pts=fam['star_eq_pts'], ok=fam['ok'], halt=fam['halt'], hwm_gb=fam['hwm_gb'],
                 secs=None)
    else:
        r.update(seeds=core.get('seeds'), cover_E=core.get('cover'), per_prime=core.get('per_prime'),
                 hwm_gb=core.get('hwm_gb'))
    r['certs'] = None
    r['_provenance'] = note
    r['_absent_fields'] = absent
    r['_queue_entry'] = queue
    return r


def main(argv):
    out = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b14_12', 's79_schema_rows.jsonl')
    q = json.load(open(os.path.join(ROOT, 'results', 's79_queue.json')))
    rows = []

    core = json.load(open(os.path.join(ROOT, 'results', 'b14_12', 'b14_12.json')))
    fam = json.load(open(os.path.join(ROOT, 'results', 'b14_12', 'b14_12_families.json')))
    qe = [x for x in q if tuple(x['lam']) == tuple(core['lam']) and x['delta'] == core['delta']][0]
    rows.append(row_from(core, fam, qe,
                         'B14-12: results/b14_12/b14_12.json (determinant column) + '
                         'results/b14_12/b14_12_families.json (the other three families)',
                         ['certs -- no tools/verify certificate exists: N_S*a = 1.08e8 is far above the '
                          'full_rank gate of 3e6 (PROVED.md: certificate_ceiling), so this tree can PROVE '
                          'this result and cannot CERTIFY it in the present formats',
                          'pred_mem_x_bytes -- the lean hybrid sizes its X blocks from S71_MEM_X directly',
                          'secs -- build and the two family passes were separate bounded processes; '
                          'no single wall time covers the cell',
                          'refute -- recorded: D = -3 <= 0, so False']))
    rows[-1]['refute'] = bool(fam['refute'])

    pcore = json.load(open(os.path.join(ROOT, 'results', 'b13_10', 'pilot.json')))
    pcore = dict(pcore, primes=pcore['primes'], bound=pcore['bound'], a=pcore['a'],
                 lam=pcore['lam'], delta=pcore['delta'])
    pq = [x for x in q if tuple(x['lam']) == tuple(pcore['lam']) and x['delta'] == pcore['delta']][0]
    rows.append(row_from(pcore, None, pq,
                         'B13-10 pilot: results/b13_10/pilot.json -- determinant family ONLY',
                         ['mult_pad, mult_red, mult_red_pts, mult_red_star, mult_per4 and every quantity '
                          'derived from them (i_pad, i_red, i_per4, D, D_R, pad_lt_red, monotone_ok, '
                          'star_eq_pts, ok, halt) -- B13-10 sec 4 states plainly that only the determinant '
                          'family was evaluated at this cell and prices the other three at ~5.9 CPU-minutes',
                          'n_red, cover_Ered, sieve_secs -- the (star) mask was never computed there',
                          'certs -- as above, N_S*a = 1.8e8 is above the full_rank gate']))

    with open(out, 'w') as f:
        for r in rows: f.write(json.dumps(r) + '\n')
    for r in rows:
        print(f"{tuple(r['lam'])}_{r['delta']}: a={r['a']} mult_det={r['mult_det']} i_det={r['i_det']} "
              f"mult_pad={r['mult_pad']} mult_red={r['mult_red']} D={r['D']} "
              f"({len(r['_absent_fields'])} absent field groups named)")
    print('->', out, os.path.getsize(out), 'bytes')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
