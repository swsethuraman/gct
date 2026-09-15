# B16-11 portable receiver specification

Version `b16-11-receiver/1`. Author: the user-authorized B16-11 task,
gpt-6-astra/xhigh. No subagent, other task, heavy computation, or mathematical
production replay. Original B15 reports and source retain their authorship,
including their stated Claude Opus 5 dependencies. Filesystem delivery only.

## Scope and trust root

This receiver checks a frozen launch and its cited evidence, not later B16
research deliveries. `INPUT_HASHES.json` contains exact byte SHA-256 hashes,
relative source paths, byte sizes, roles, and portable copies. Its code,
manifest and final delivery seal must be reviewed together. Hash consistency
is not a proof of mathematics and a self-edited manifest cannot confer trust.
Git SHA-1 blob IDs establish a separate binding to the observed frozen commits;
raw bytes or CRLF-to-LF conversion are the only accepted source equivalences.

The six launch hashes are authoritative. Each of the twelve worktrees has its
own frozen commit and tree. No common merged base is inferred from shared
ancestry. The native read-only Git receipt records observed HEAD/branch, frozen
commit object type/tree, and selected original source blob IDs. The portable
receiver verifies receipt joins and original source bytes. It does not invoke
Git, inspect live branches, revalidate Git bundles, or certify an unsigned
receipt independently of its reviewed provenance. The PowerShell audit is a
separate optional operation subject to normal Git approvals. A later HEAD
change need not invalidate an extant frozen commit, but must be recorded.

The old Slot01 input manifest includes incidental Python bytecode. Those bytes
are hash-checked in the original snapshot but are not copied, run, or staged.
All semantic manifest inputs and the reviewed small reports/source used here
are included. Runtime identity records the Python version and interpreter
SHA-256, not a complete independently hashed standard-library distribution.

## Required delivery envelope for subsequent receivers

Each claim needs the producer and original attribution; exact input paths and
byte hashes; frozen source commit/tree or an explicit uncommitted snapshot;
full cell key; representation/normalization conventions; exact claim;
hypotheses; separate fresh computation, fresh deduction and inherited premises;
proof artifact and executable bounded verifier; measured resource receipt;
process exit; limitations; and next sufficient witness. Later amendments must
name the precise superseded fields without overwriting old evidence.

The cell key is `(n, degree, lambda, ambient_variables, field, representation,
padding, space)`. In this batch n=4, ambient_variables=16, field=Q (with stated
characteristic-zero extension), `sum(lambda)=4*degree`, and the representation
is `positive_partition_coordinate_HWV`. Padding is
`independent_z_per3_ten_essential_variables`; space is `orbit_closures`.
Partition length is distinct from ambient dimension and essential variables.
An eight/nine-direction restriction is not a replacement for the ten-variable
padding model; any restriction-derived rank needs its valid lifting argument.

Bound kinds are distinct: exact finite ambient dimension, stable ambient
dimension, actual coordinate rank floor, global ideal floor, global ideal
upper bound, and source dimension/ceiling. A source count is never accepted
as a coordinate rank. A sampled kernel or repeated zero cannot be accepted as
a global ideal floor. Native modular rank needs exact integer/rational source
definitions, compatible primes and denominator control, and a freshly rebuilt
nonzero minor or an exact coefficient witness. HWV membership and weight must
be verified in the specified source convention. A global equation needs an
identity after arbitrary determinant substitution (or a proved equivalent
polynomiality/density argument), not a special pencil check.

If a finite equation is obtained on a chart, retain the explicit pole bound,
polynomial extension, covariance/HWV argument, density and ambient extension.
A sufficient lift degree is not a minimum degree or a complete filtration.
Independent products need actual image and overlap certificates; tensor
multiplicities and factor nonmembership cannot supply them. Being outside the
ideal generated in degree24 is distinct from being outside every LMR
construction or saturation.

## Arithmetic and proof boundary

In one finite ambient multiplicity space A of dimension a, restriction gives
`m_X=a-i_X`. Therefore

`D=m_pad-m_det=i_det-i_pad`.

If `i_det>=q` globally and actual padding restriction rank is at least r,
then `i_pad<=a-r` and `D>=q+r-a`. Thus the sufficient positive gate is
`q+r>a`. Its failure alone is inconclusive. The executable gate uses a
receiver-owned registry and requires all three premises to share an exact cell.
The delivered research registry is empty; its positive examples are synthetic
controls and admit no external mathematical claim. A real new adapter needs
separate proof review, not just an observation with a checksum.

Two useful negative gates are `i_det<=Q` with `i_pad>=P` and Q<=P, or
`m_det>=L` with `m_pad<=U` and U<=L. Equality/upper bounds must have the stated
scope. In particular a source ceiling plus a *determinant ideal floor* cannot
by itself exclude a cell.

The receiver freshly adds the inherited cubic channel values
`1,1,2,3,5,6,9,11,14,16,19,21,24,26,29,31,34,36`.
They sum to158/218/288 through b=15/17/19. Their character computations and
ring-map proof are inherited from Dream_Upper288. The ring map is
`C[Z]_d -> Sym^d(V) tensor C[Sub_9(Sym^3 V*)]_d` injective, followed by the
surjective restriction to padding. Characteristic-zero semisimplicity gives
the multiplicity ceiling. A dense monic depressed-cubic restriction is an
injection on a specified HWV space, giving a finite upper bound, not equality.

For degree d, tail t and lambda `(4d-t-16,t,2^8)`, Pieri channels are
`(3d-14-b,b,2^7)` for2<=b<=t. The receiver checks the sizes/interlacing of
these channels at d23/25/26/27. In particular it records218 at d26 as a
conditional extension of the reviewed chart bound, not an exact new count.
The c multiplier transports the two degree25 global equations to degree26
under the polynomial domain/HWV hypotheses.

| Cell | Global determinant floor q | Padding ceiling U | Known q could succeed only if | With reviewed i_det<=11, exclusion if |
|---|---:|---:|---:|---:|
| d23 `(61,15,2^8)` | 1 | 158 | a<=158 | a>=169 |
| d25 `(67,17,2^8)` | 2 | 218 | a<=219 | a>=229 |
| d26 `(71,17,2^8)` | 2 | 218 | a<=219 | a>=229 |
| d27 `(73,19,2^8)` | 5 | 288 | a<=292 | a>=299 |

The third column is an upper bound, not an achieved floor. Even in the feasible
range, actual r>=a-q+1 is needed. The last column additionally assumes the
accepted finite-to-stable determinant ideal injection; absent that premise it
is not an exclusion. Unknown a is never replaced with a stable dimension.

For the stable d35 cell `(105,19,2^8)`, inherited `a=429`, `m_det=418`,
`243<=m_pad<=288` yield `i_det=11`, `141<=i_pad<=186` and
`-175<=D<=-130`. Rank419 is impossible there. No exact padding rank243 or288,
nor an explicit141-equation padding basis, is asserted.

The accepted Slot01 partial interpolation has a159-dimensional target with
evaluation rank at least158; its evaluation kernel has dimension at most1.
A complete93-dimensional source evaluates with rational rank88, so its
sampled kernel has dimension5. Restriction maps that5-space into the target
evaluation kernel; its global kernel therefore has dimension at least4 and
at most5. The saved arithmetic is `5-(159-158)=4`, and `93*158=14694` exact
entries. The target rank159 and an explicit fourth global kernel vector are
not claimed. All large evaluations and rank calculations are inherited from
the accepted2296.626s replay and are not repeated.

The four degree14 equations of weight `(25,17,2^7)` multiply injectively by
nonzero q44 (degree2, weight `(4,4)`) to degree16 `(29,21,2^7)`. Leading
coefficient powers continue the ladder. With the recorded stable determinant
ideal upper4 and transport, D<=0 from16. This leaves14/15 open within the
specified nine-row investigation. The independent B15-08 ambient-two source
for tail `(4,3,2^6)` has recorded stable onset d19 and weight `(57,4,3,2^6)`;
`5040*720=3628800` is a generic independence minor, not determinant geometry.

## Resource and execution contract

The build and receiver are standard-library, sequential, with no subprocess
or BLAS call, under the inspected worktree `analysis/b15_bound.py`:

```powershell
& ./.venv/python.exe -B analysis/b15_bound.py --slot 11 --name b16_11_receiver_fresh --seconds 60 --memory-mb 512 analysis/b16_11_receiver.py --package delivery/b16_11 --output results/b16_11/receiver_fresh.json
```

For the portable package, from the assigned worktree:

```powershell
& ./.venv/python.exe -B delivery/b16_11/b15_bound.py --slot 11 --name b16_11_portable_fresh --seconds 60 --memory-mb 512 delivery/b16_11/b16_11_receiver.py --package delivery/b16_11 --output results/b16_11/portable_fresh.json
```

Choose an unused receipt/output name. `--input-root` optionally verifies live
original payload hashes as well; default execution uses only packaged paths.
The receiver never imports inherited producer code. Payload budgets are512
files,16MiB per file and64MiB total. Inspection priced the66 Slot01 manifest
files at6,072,578 bytes before hashing. This is a metadata/copy task, not a
dense expansion. A non-Windows host requires an equivalently enforced
60s/512MiB supervisor and the documented one-thread environment/deadline.
The bundled Windows wrapper is not a portable Unix memory supervisor.

The wrapper enforces process and aggregate Job Object memory and a wall timer;
its idle timer is not a computational worker. It declares workers=1 but does
not enforce an ActiveProcessLimit; the new receiver/build launch no children.
Timeout uses os._exit and may leave an incomplete receipt: absence of final
measurements or exit status is a failed/incomplete run, never a successful
zero-resource run. Legacy batch15 labels are preserved. New B16 command names,
hashes, timestamps and owned paths identify the run. CPU usage is not measured
by this wrapper. Read-only Git metadata timing is reported separately.

The historical B15-01 cap5400s/1536MiB is accepted historical evidence; it grants
no B16 lease. No heavy lease was acquired by B16-11. A completed delivery needs
the final wrapper receipts and a post-run process-exit observation. External
mutation controls must detect hash corruption, same-shape/different-degree
joins, source-ceiling-as-rank, sampled-zeros-as-global-proof, stable-as-finite
ambient, inside-variable padding, and self-authorized proof observations.
