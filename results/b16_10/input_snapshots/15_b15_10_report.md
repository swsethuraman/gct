# B15-10: complete portable replay of the degree-8 Q1 cell

**EXACT: the full requested certificate is delivered.** Four integral
highest-weight polynomials give determinant rank 4; one gives padded rank 1
at a true z*per3 point. Together with the inherited exact bounds a=4 and
h_pad=1, these prove m_det=4, m_pad=1, i_det=0, i_pad=3 and **D=-3** for
n=4, delta=8, lambda=(12,4,4,4,4,4), in 16 ambient variables. This improves
the portability of an already closed cell; it adds no new frontier closure.

The complete certificate is `results/b15_10/full_certificate.json` (93,809
bytes). Its three standard-library verifier modules total about 25 KB. A fresh
receiver process regenerated every polynomial value and both minors in
2.234 seconds with aggregate peak committed memory 17,342,464 bytes
(16.54 MiB; peak working set 24.75 MiB). It loaded all three modules from the
separate retained `results/b15_10/receiver_01` directory. It needed neither
the native 753,614,285-byte operator nor a modular kernel lift.

## New sources and checked findings

`docs/b15_10_proved.md` gives the full defining formulas and global
highest-weight proof. They are flag contractions of an integral quartic
tensor T_ijkl=alpha! c_alpha with four epsilon tensors. A three-subset
recurrence evaluates their degree-6 invariant H, and formal series extraction
gives three further sources of degree 8. Their common weight is proved
symbolically. No full weight carrier or symbolic permutation expansion is
allocated. The maximum layer has 8,000 states and three integers per state.

| Fresh result | Exact evidence |
|---|---|
| Rank-one determinant exclusion | F0=5,284,823,040 on an explicit skew pencil |
| Four determinant directions | Nonzero integer 4-by-4 minor; residues 1261539314 and 635991447 at the two house primes |
| One padded direction | F2=-493414004913340416 on the stored six-by-ten frame for z*per3 |
| Source membership | Integral construction, exact epsilon identity, degree and weight count |
| Fresh receiver | Reconstructed det4 and z*per3 coefficients and all five source-value rows |
| Corrupted receiver | A changed native pencil entry rejected with exit code 1 |

The smaller format/control witness was the banked B14-10 cubic cell
(7,5,5,2,2,1,1,1), n=3, degree=8. Its original verifier freshly expanded the
source, checked every raising derivative over Z, and reproduced its nonzero
permanent evaluation. Its ambient multiplicity-one premise is inherited.

`results/b15_10/exclusion.json` retains the especially small 5,927-byte
rank-one certificate. `results/b15_10/extension_pilot.json` retains the
initial four-source independence pilot as CANDIDATE provenance; subsequent
proof, full production receipt and receiver upgrade the delivered sources to
EXACT. No failed mathematical candidate or resource stop was omitted.

## Controls and receiver

`results/b15_10/controls.json` records direct-permutation and direct-series
agreement at dimension 3, altered-sign and factorial-normalization detection,
independent liveness H(sum x_i^4)=24^6, five exact raising shears, and three
diagonal weight scalings. Zero and four-factor determinant points yield zero
on all sources, as required. The geometric verifier rejects an altered source,
normalization, native point, matrix, minor, padded minor, degree, and missing
native point. The global highest-weight theorem comes from the proof, not
from the finite shear controls.

The separate corrupted receiver run used the receiver's own copied modules
and an altered A0[0,1]. It returned 1 at the regenerated coefficient check.
The unchanged receiver returned 0. Both resource receipts and the corrupt
run's traceback are retained. The receiver manifest checks exact module and
certificate equality at copy time. No temporary or caller output was removed.

## Replay

In the assigned checkout, the exact local command is:

```powershell
& 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-10\.venv\python.exe' analysis/b15_bound.py --slot 10 --name b15_10_replay_fresh --seconds 60 --memory-mb 512 results/b15_10/receiver_01/b15_10_full.py verify --certificate results/b15_10/receiver_01/full_certificate.json
```

For a portable receiver with Python 3.10 or newer, copy the three modules and
certificate in `receiver_01` to an empty directory, then run:

```text
python b15_10_full.py verify --certificate full_certificate.json
```

Use a tested local resource limit. The standard-library verifier's source
guards bound tensor dimensions, pencil dimensions, and expansion counts.
The Windows wrapper adds the tested Job Object and wall-clock deadline.

## Resources, attribution and provenance

Actual model: **gpt-6-astra**, requested reasoning **xhigh**, for proof,
implementation, controls, and delivery. No additional agents or research
tasks were started. Existing banked code and formats retain their attribution;
the new tensor formulas and implementation are authored in this task.

The existing branch and worktree were retained. Base commit
f365568d80d5f66fea2dd9342ff1998e1d866915, tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd and annotated tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1 matched before work. Preregistration
was the first and only file in commit 90eb5a8a804c007d4d2494eaa512c2bbb82b631a.
Native readiness and the lease record were read. Slots 01/02 held the heavy
leases; slot 10 ran no heavy numerical job and requested no heavy lease.
All work fit measured small runs capped at 60 seconds and 512 MiB, with one
process and one BLAS thread. The verifier itself uses only Python integers.

| Run | Return code | Wall seconds | Aggregate peak MiB |
|---|---:|---:|---:|
| Banked small witness | 0 | 1.339 | 67.01 |
| Direct rank one | 0 | 0.015 | 12.83 |
| Four-source pilot | 0 | 1.697 | 16.12 |
| Full certificate construction/replay | 0 | 4.593 | 16.60 |
| Controls | 0 | 12.524 | 17.90 |
| Fresh receiver | 0 | 2.234 | 16.54 |
| Corrupted receiver | 1, expected | 0.016 | 12.70 |

`results/b15_10/resource_summary.json` retains exact bytes, times, return
codes, and links to individual PID/resource logs. `input_hashes.json` supplies
both exact working-byte and normalized-LF SHA-256 hashes. Native setup smoke
and runtime logs are preserved separately and are not research commits.
The current shared theorem/exclusion records, protected papers, shared launch
records, Git trust settings, and worktree ownership were not changed.

## Inherited premises, completion and delivery

The two bounds a<=4 and h_pad<=1 come from the accepted exact Q1 recount.
This task did not replay that recount. The new receiver gives fresh rank
floors, and hence fresh lower bounds a>=4 and m_pad>=1. The original B14-12
per4 result and its old multiplicity basis remain RECORDED; they are not
needed by this certificate. No basis conversion is asserted. No CRT integer
uniqueness or modular good-prime hypothesis is needed: all source polynomials
and both nonzero minors are integral.

**Completion:** both the exclusion and full D=-3 deliverables are complete.
There is no remaining missing witness for this assigned cell. To remove the
last inherited premises from a completely standalone proof, the next useful
deliverable is a compact verifier for the exact a<=4 and h_pad<=1 recount;
this is a bound calculation, not another rank witness. The integrator receives
the proposed evidence update in `results/b15_10/proposed_exclusions.json`.

The final commit/tree and one-ref delta-bundle hashes are external in
`delivery/b15_10_final/delivery_manifest.json`. The prescribed pre-bundle and
post-bundle checks are performed after the last research commit. Their PASS
status concerns packaging; the source proof and geometric replay above carry
the mathematical conclusion. Work ends after checked local bundle delivery;
no push or publication is authorized.
