#!/usr/bin/env python3
"""Is session 79's frozen Q1 queue complete, and is every cell in it i_det = 0?

    python3 analysis/integrate/b14_12_q1_join.py

Joins the frozen queue (results/s79_queue.json) against the three places its cells
are answered: session 79's own delivery, B13-10's pilot, and B14-12.  Writes
results/integrate/s79_q1_complete.json.  Nothing here is taken on a report's word.

It must be able to fail: --mutate drops one cell's i_det and the join must refuse.
"""
import json, os, pathlib, sys

ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))


def load():
    queue = json.loads((ROOT / 'results' / 's79_queue.json').read_text())
    cells = [json.loads(l) for l in (ROOT / 'results' / 's79_cells.jsonl').read_text().splitlines() if l.strip()]
    pilot = json.loads((ROOT / 'results' / 'b13_10' / 'pilot.json').read_text())
    b1412 = json.loads((ROOT / 'results' / 'b14_12' / 'b14_12.json').read_text())
    return queue, cells, pilot, b1412


def join(mutate=False):
    queue, cells, pilot, b1412 = load()
    Q1 = [(tuple(c['lam']), c['delta']) for c in queue]
    by = {}
    for r in cells:
        by.setdefault((tuple(r['lam']), r['delta']), []).append(r)
    if mutate:                      # the check must be able to fail
        k = Q1[0]
        by[k] = [dict(by[k][0], i_det=1)]
    extra = {(tuple(pilot['lam']), pilot['delta']): ('results/b13_10/pilot.json', pilot['i_det'], pilot['a'], pilot['mult_det']),
             (tuple(b1412['lam']), b1412['delta']): ('results/b14_12/b14_12.json', b1412['i_det'], b1412['a'], b1412['mult_det'])}

    resolved, unresolved = [], []
    for k in Q1:
        if k in by:
            vals = {r.get('i_det') for r in by[k]}
            if vals == {0}:
                resolved.append({'lam': list(k[0]), 'delta': k[1], 'i_det': 0, 'source': 'results/s79_cells.jsonl'})
            else:
                unresolved.append({'lam': list(k[0]), 'delta': k[1], 'i_det': sorted(str(v) for v in vals),
                                   'source': 'results/s79_cells.jsonl'})
        elif k in extra:
            src, idet, a, mult = extra[k]
            if idet == 0 and mult == a:
                resolved.append({'lam': list(k[0]), 'delta': k[1], 'i_det': 0, 'a': a, 'mult_det': mult, 'source': src})
            else:
                unresolved.append({'lam': list(k[0]), 'delta': k[1], 'i_det': idet, 'source': src})
        else:
            unresolved.append({'lam': list(k[0]), 'delta': k[1], 'i_det': None, 'source': None})
    return queue, Q1, resolved, unresolved


def main(argv):
    if '--mutate' in argv:
        _, Q1, res, un = join(mutate=True)
        print(f"mutated: {len(res)} resolved, {len(un)} unresolved -- "
              + ('the join refuses, as it must' if un else 'THE JOIN CANNOT FAIL -- fix it'))
        return 0 if un else 1
    queue, Q1, res, un = join()
    from collections import Counter
    bysrc = Counter(r['source'] for r in res)
    out = {
        'produced_by': 'integrator, B14-12 intake',
        'question': "is session 79's frozen Q1 queue complete, and does every cell carry i_det = 0?",
        'queue': 'results/s79_queue.json, frozen before the first cell (PREREG_s79 section 2.4)',
        'queue_size': len(Q1),
        'resolved': len(res),
        'unresolved': len(un),
        'unresolved_cells': un,
        'by_source': dict(bysrc),
        'delta_histogram': dict(sorted(Counter(c['delta'] for c in queue).items())),
        'cost_ordered': all(queue[i]['NS_delta'] <= queue[i + 1]['NS_delta'] for i in range(len(queue) - 1)),
        'first': {'lam': queue[0]['lam'], 'delta': queue[0]['delta'], 'NS_delta': queue[0]['NS_delta']},
        'last': {'lam': queue[-1]['lam'], 'delta': queue[-1]['delta'], 'NS_delta': queue[-1]['NS_delta']},
        'nchi_est_is_the_forbidden_quotient': {
            'entries': len(queue),
            'equal_to_ceil_NS_over_stab': sum(1 for c in queue if c['nchi_est'] == -(-c['N_S'] // c['stab'])),
            'note': 'PROVED.md: nchi_2_21_guard -- N_S/|Stab| is neither an upper nor a lower bound on n_chi',
        },
        'conclusion': ('every cell of the frozen Q1 queue carries i_det = 0: there is no six-row determinant '
                       'equation anywhere in Q1' if not un else 'INCOMPLETE'),
        'cells_not_in_session_79s_own_delivery': [r for r in res if r['source'] != 'results/s79_cells.jsonl'],
    }
    p = ROOT / 'results' / 'integrate' / 's79_q1_complete.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2) + '\n')
    for k in ('queue_size', 'resolved', 'unresolved', 'by_source', 'delta_histogram', 'cost_ordered',
              'nchi_est_is_the_forbidden_quotient', 'conclusion'):
        print(f"  {k}: {json.dumps(out[k])}")
    print(f"  wrote {p.relative_to(ROOT)}")
    return 0 if not un else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
