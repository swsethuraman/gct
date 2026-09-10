#!/usr/bin/env python3
"""
B13-09 -- remove the one top-level key `board_numbering` from already-written
gct-cert/1 certificates, and nothing else.

Why: the worker preamble asks every report and every MANIFEST to carry a
`board_numbering` field, and this session's evaluator wrongly put it in the
CERTIFICATES too.  `gct-cert/1` is a closed schema and tools/verify refuses an
unknown top-level key -- correctly; that refusal is the house verifier doing its
job, and it is a defect in this session's evaluator, not in the verifier.  The
evaluator is fixed for every certificate written after this point; this tool
repairs the ones already written.

It is deliberately the narrowest possible edit: it asserts that the ONLY
difference between the old and new object is the removal of that single key, and
refuses to touch a file for which that is not true.  No mathematical content --
cell, prime, points, basis, conventions -- is read, rewritten or reinterpreted.

usage: python3 analysis/b13_09_cert_fix.py [DIR] [--dry-run]
"""
import sys, os, json, gzip

def main(argv):
    d = next((a for a in argv if not a.startswith('--')), 'results/certs/b13_09')
    dry = '--dry-run' in argv
    fixed = clean = skipped = 0
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.json.gz'): continue
        path = os.path.join(d, fn)
        with gzip.open(path, 'rt', encoding='utf-8') as f:
            obj = json.load(f)
        if obj.get('format') != 'gct-cert/1':
            skipped += 1; continue            # this session's own ideal_* records, not gct-cert/1
        if 'board_numbering' not in obj:
            clean += 1; continue
        before = dict(obj)
        removed = before.pop('board_numbering')
        assert removed == 'batch13', (fn, removed)
        assert set(before) == set(obj) - {'board_numbering'}, fn
        assert all(before[k] == obj[k] for k in before), ('a key other than board_numbering would change', fn)
        if not dry:
            with gzip.open(path, 'wt', encoding='utf-8') as f:
                json.dump(before, f, separators=(',', ':'))
        fixed += 1
    print(f"{'would fix' if dry else 'fixed'} {fixed}, already clean {clean}, not gct-cert/1 {skipped}")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
