# gct — conductors and deficits of orbit closures

Computational companion to the working paper *Conductors of Orbit Closures*
and the log *The Boundary Deficit* (Swami & Claude, Aug 2026). Start with
`PROJECT_NOTES.md` — it is the standing project context: results bank,
infrastructure protocol, and roadmap.

## Layout
    engine/     dp.c (checkpointed sharded exact DP), bit.c, bit3.c (anchors)
    scripts/    grind workers (w1/w2/resume.sh), assemble.py, deficit.py
    analysis/   week-1/2/3 sympy analyses (World A, World B, det3)
    inputs/     evalin/*.txt evaluation inputs (f1C grind, h-series bank, anchors)
    results/    results_f1C.md (canonical grind record), ASSEMBLY.md (procedure)
    docs/       artifact links

## Quickstart (cloud container or any Linux box)
    gcc -O2 -o dp2g engine/dp.c
    ./dp2g quad          # expect VALUE 24
    ./dp2g det3 6        # expect level-6 line: states 1818118 emitted 2336283
    # grind mode (checkpointed, resumable, sharded):
    ./dp2g evalopts inputs/evalin/f1C_00.txt
Regression values that must match exactly after any engine change are listed
in PROJECT_NOTES.md ("Canonical regression").

## Sync protocol
The cloud work container is scratch and can roll back: this repo (at
C:\Users\swami\Projects\gct) is the durable copy. Each session: stage the
repo in at start; commit and write back (tree + fresh `gct.bundle`) at every
milestone. The bundle is a full clone: `git clone gct.bundle gct-restore`.
