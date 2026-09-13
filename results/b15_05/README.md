# B15-05 replay instructions

Run from the existing B15-05 worktree on b15-05-tail21. Use its absolute
Python executable:

    C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-05\.venv\python.exe

Commands below use `PY` as an explanatory placeholder for that executable.
In PowerShell invoke the quoted executable with `&` and then the arguments.
No activation or PATH lookup is required.

    PY analysis/b15_bound.py --slot 05 --name b15_05_recheck_controls --seconds 60 --memory-mb 512 analysis/b15_05_tail21.py controls
    PY analysis/b15_bound.py --slot 05 --name b15_05_recheck_transport --seconds 30 --memory-mb 512 analysis/b15_05_tail21.py transport
    PY analysis/b15_bound.py --slot 05 --name b15_05_recheck_defect --seconds 30 --memory-mb 512 analysis/b15_05_tail21.py defect

The first two commands require exit 0. The intentional altered-value
`defect` command requires exit 1 with the expected disagreement message.
Use fresh log names to preserve existing resource receipts. Controls
write the per-slot controls, source and transport JSON files.

The following are heavy jobs and require a currently granted integrator
lease. The script checks the external lease record before either mode.

    PY analysis/b15_bound.py --slot 05 --name b15_05_pilot --seconds 900 --memory-mb 1536 analysis/b15_05_tail21.py pilot
    PY analysis/b15_bound.py --slot 05 --name b15_05_geometric_replay --seconds 900 --memory-mb 1536 analysis/b15_05_tail21.py replay

The pilot saves the ordered bracket definitions, complete integral pencil
and generic point data, residue matrices, actual square minors, row and
column indices, determinants and sampled modular kernels. Progress files
identify the prefix completed before any bounded stop. Every numeric
NPZ archive has named arrays (`data` for points, `values` for matrices).

Rows are points and columns are sources. `source.json` defines every
bracket, the tensor convention and a complete generic homogeneous-form
construction. The detector uses eight integral traceless matrices per
point, in array order [variable,row,column,point]. Generic point arrays
use [point,degree-index,row,column], with degree-index 0,1,2 denoting
degrees 2,3,4. `replay` reconstructs the selected geometric points and
source evaluations with a different interpolation seed before checking
the actual minor entries and determinant. Reading and reducing the
saved residue matrix alone does not constitute geometric replay.

The generic rank-533 pivot columns define the basis used by each kernel
file. Kernel entries are finite-field residues, not rational equations;
their vanishing on finitely many determinant points does not establish
global ideal membership. Input hashes are in `controls.json`; the final
file receipt supplements them with new implementation/output hashes.
