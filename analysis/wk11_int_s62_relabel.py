#!/usr/bin/env python3
"""Integrator housekeeping: label session 62's Gram certificates.

Session 62 ran in wave 1, before session 67's declared-field rule landed.  Its
44 matrix certificates are semantically Foulkes Gram matrices G = V^T B V with a
rank claimed over Q and a nonvanishing minor exhibited, but they carry neither
matrix_role nor field.  tools/verify/FORMAT.md is explicit that an unlabelled
Gram is read as a plain rank of that matrix and NOT as rank(Theta) -- which is
exactly the reading that keeps a Gram from smuggling in a multiplicity claim --
so these certificates verify but do not certify what their titles assert.

This pass adds

    "matrix_role": "gram",   "field": "Q"

to each, which is the labelling the format asks the producer for.  It is sound
here because the rank is claimed over Q with an integer minor exhibited:
rank(Gram) = rank(Theta) is the characteristic-zero identity, and the verifier
refuses the label on anything but field Q.  Nothing else in any file changes.
"""
import json, os, sys, glob

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results', 'certs', 's62')


def main():
    changed = skipped = 0
    for f in sorted(glob.glob(os.path.join(SRC, '*.json'))):
        d = json.load(open(f))
        why = None
        if d.get('kind') != 'matrix':
            why = 'not a matrix certificate'
        elif 'claimed_rank_Q' not in d:
            why = 'no rank over Q claimed'
        elif not ('G_lambda' in d.get('title', '') or 'Gram' in d.get('notes', '')):
            why = 'not identified as a Gram'
        elif d.get('matrix_role') == 'gram' and d.get('field') == 'Q':
            why = 'already labelled'
        if why:
            print(f'  skip {os.path.basename(f)}: {why}'); skipped += 1; continue
        d['matrix_role'] = 'gram'
        d['field'] = 'Q'
        with open(f, 'w') as fh:
            json.dump(d, fh, indent=1)
        changed += 1
    print(f'labelled {changed}, skipped {skipped}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
