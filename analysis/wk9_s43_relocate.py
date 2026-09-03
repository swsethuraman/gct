#!/usr/bin/env python3
"""
Session 43 -- move the bite artefacts this session produced out of
results/s41_cells/ and into results/s43_cells/.

analysis/wk9_s41_bite.py writes its exhibited vectors and battery reports to a
path hard-coded as results/s41_cells/.  That directory is session 41's record;
this session's artefacts belong in its own.  The file is not edited, so the
relocation is done here: any file under results/s41_cells/ that is not tracked
in git at the session's base commit is moved to results/s43_cells/, and the
in-file reference to the old directory is rewritten.

usage: python3 wk9_s43_relocate.py [base-commit]
"""
import os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
SRC = os.path.join(ROOT, 'results', 's41_cells')
DST = os.path.join(ROOT, 'results', 's43_cells')

base = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
tracked = set(subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', base, 'results/s41_cells/'],
                             capture_output=True, text=True).stdout.split())
moved = []
if os.path.isdir(SRC):
    os.makedirs(DST, exist_ok=True)
    for fn in sorted(os.listdir(SRC)):
        rel = 'results/s41_cells/' + fn
        if rel in tracked:
            continue
        src, dst = os.path.join(SRC, fn), os.path.join(DST, fn)
        data = open(src, 'rb').read()
        if fn.endswith('.md') or fn.endswith('.txt'):
            data = data.replace(b'results/s41_cells/', b'results/s43_cells/')
        open(dst, 'wb').write(data)
        os.remove(src)
        moved.append(fn)
print("relocated %d file(s) to results/s43_cells/: %s" % (len(moved), ", ".join(moved) if moved else "(none)"))
