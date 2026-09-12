# B14-10 — recovered evidence and explicit remaining gaps

**Outcome: substantive fallback delivered.** The frozen evidence is fully
accounted for at file level, four compact exact witnesses replace the role of
eight missing certificate files, and recovered proof rules now have typed
machine applications. Full historical replay and complete semantic cell keys
remain unfinished. Delivery contains **one unsplit named-branch bundle (zero
bundle parts), one evidence ZIP, and four file-register parts, part00–part03**
inside the evidence package. The full artifact and part checksums are supplied.

**RECORDED attribution and base.** board_numbering: batch14. Actual model:
gpt-6-astra (OpenAI Codex, GPT-6); requested reasoning xhigh. No subagents.
Branch: b14-10-astra. Base commit:
9898e56941a7665f231873481dae956f08509995. Base tree:
cb688cd3fe454d638f3202e759e2eaa0c629739f. Both exact `git log -1 --format=%H`
and `--format=%T` commands on batch14-base matched; initial HEAD was that base.
Preregistration was committed at 2d19beb8, and the observed-pilot/addendum
checkpoint at 129438f8 preceded the new exact arithmetic. Final head/tree and
bundle prerequisite identities are recorded in the delivery manifest, avoiding
a report that attempts to name the commit containing itself.

## What the recount found — MEASURED / RECORDED

The old list has **874 distinct files and all 874 are present**. Its new
file-role register has **699 results and 175 metadata files**. These are
conservative content/schema classifications, not 699 new mathematical proofs.
No whole file was declared superseded without evidence. Exact duplicate Git
blobs are linked as duplicates; historical claim text and source pointers are
preserved separately from validation status.

The fresh frozen JSON/JSONL scope has **937 files**: 30 old observation-parser
sources and **907 without those parsers**, comprising the historical 874 plus
**33 additional inputs**. This excludes the review-only integration mirror
itself, non-JSON/JSONL artifacts, and compressed certificates (audited separately).
There are no JSON parse failures. Visibility is now complete for this scope;
semantic proof interpretation is not.

| Historical file cell-key disposition | Files |
|---|---:|
| At least one complete cell key extracted | 429 |
| Stable/ladder family key, not a single cell | 57 |
| Metadata with no cell key required | 149 |
| Geometric result with no representation-cell key | 16 |
| Complete cell key still unknown | **223** |

Keys contain polynomial degree n, partition length ell, coefficient degree
delta and lambda, with positive decreasing partitions and sum(lambda)=n*delta.
Every key carries its JSON pointer or attributed source. Derived degree fields
are labelled; unclear variety context remains unknown. **OPEN:** the 223
remaining cases need source-specific schema/reference review. Their names are
in results/b14_10/remaining_cell_keys.json; none becomes a false closure.

The banked unstaged scanner replays to **23 reports, zero missing references,
13 cross-path references, and one explicitly absent DAG artifact**. Cross-path
candidates retain the scanner's hash/provenance caveat. Zero reported staging
gaps does not mean every dependency of every historical calculation exists.

## Certificate accounting — MEASURED / RECORDED

| Manifest | Listed | Present | Missing | Present MD5 matches | Present MD5 mismatches |
|---|---:|---:|---:|---:|---:|
| s79 | 2,066 | 1,229 | **837** | 1,200 | **29** |
| B13-09 | 252 | 84 | **168** | 84 | 0 |

All 2,318 entries are registered exactly once, with frozen blob, current
presence, historical bytes/MD5, actual integrity checks, cell, prime, source
record when found, reason, replay status and replacement link where applicable.
The 837 s79 absences are all **recorded shipping-size exclusions**: each is
marked shipped=false and exceeds the manifest's **60,000-byte cut**. The
calibration keep-all list is empty. This is the shipping cut actually recorded
in the manifest, not the producer script's default 150,000-byte cut, the
3,000,000-term expansion condition, or its separate 4,500,000-byte deletion
guard. Listed bytes and MD5 establish a record of a written file; they do not
reconstruct its history or replay its mathematics. Seventeen missing s79 paths
have no matching cert reference in the three banked producer JSONL streams;
their cost/source detail stays unknown despite the manifest's shipping evidence.

B13-09 records that the 168 absent files were written but omitted from its
shipped chronological prefix/total-size budget. The requested finer per-file
classification as never-written, per-file-size-guard, or superseded is **unknown**;
the broad shipping explanation is retained. No absence is classified as
never-written or superseded merely because no current file exists.

**OPEN integrity discrepancies:** 29 present s79 files differ from historical
compressed MD5. Their actual compressed and uncompressed SHA256 hashes are
banked. Historical uncompressed digests are unavailable, so semantic equivalence
is unknown; a matching size is insufficient. The earlier B13-11 availability
ledger already recorded such mismatches. This run independently recounts them.

**Replay boundary:** 1,313 present compressed files were streamed completely
for payload hashes; 1,214 small payloads were decoded as JSON and 99 exceeded
the 1 MiB materialization limit. JSON decoding is not strict schema validation.
The s79 present set consists of 113 full_rank files and **1,116 hybrid_kernel
records**. The native verifier recognizes hybrid_kernel but checks only record
consistency, not the claimed ranks. This run does not mark those records PASS.
All 1,116 carry the producer's erroneous field_note saying a modular kernel
bounds i from below; the register flags that text. The valid direction remains
rank_p<=rank_Q and a sampled nullity is an upper bound on ideal dimension.

## Exact recovered witnesses — CERTIFIED

The legacy large raising-space producers require scipy and python-flint,
which are absent in this runtime. The registered fallback selected the four
missing B13-09 top cells with banked compact catalecticant witnesses:

| n=3, delta=ell=8 weight | Expanded nonzero terms | Recovery process seconds |
|---|---:|---:|
| (7,5,5,2,2,1,1,1) | 38,448 | 2.750 |
| (7,6,3,3,2,1,1,1) | 38,076 | 2.844 |
| (8,5,3,2,2,2,1,1) | 36,190 | 2.547 |
| (9,4,2,2,2,2,2,1) | 31,133 | 2.219 |

For each, **mult_per3=a=1 and i_per3=0 over Q**. The ambient dimension-one
input is `PROVED:top_cells_catalecticant`; exact nonvanishing is newly replayed
from the integral pencil in results/b13_05_topcells.json. Independent code
expands the six permanent permutations, builds the shifted-diagram matrix,
expands all 8! determinant summands, checks all weights and seven raising
derivatives over Z, and recomputes the integer determinant by Bareiss and
the independent Leibniz formula. The integer value and both prime residues
match the banked record. Source arithmetic shares no producer implementation.

These are **four new compact exact replacements for eight absent prime
files**, not recovery of the original compressed bytes. All 1,005 original
missing paths stay missing. The replacements add no new frontier closure:
these cells already lie inside degree8_global. The compact format has its
own included verifier; the standard gct-cert/1 verifier does not read it.

Every new certificate supplies its point, diagram, integral matrix,
values_are, orientation, exact determinant, both residues and polynomial
hash. Matrix rows are shifted quadratic monomials, columns are the eight
linear variables; these are not source-evaluation matrices. Entries are
alpha! times plain cubic coefficients. Scale factors 1,2,6 are units at
both house primes. The integral HWV exists before reduction; no modular
kernel lift, CRT reconstruction, u-transport or interpolation hypothesis is
being silently assumed.

## Mathematical and machine indexes — PROVED / CERTIFIED

Both indexes now include the following with explicit hypotheses and sources:

- `first_row_transport_bounds`: injections on ambient ring, ideal and
  coordinate ring; equal ambient dimensions preserve ideal dimensions.
- `stable_dimension_full_rank_closure`: a justified stable dimension and an
  exact full-rank witness at that dimension close every valid rung. It is a
  proved implication and is not applied without its premises.
- `peaked_quartic_ladders`: for **2<=ell<=16**, delta>=ell and
  lambda=(4delta-2(ell-1),2^(ell-1)), a=mult_det=1, i_det=0, hence D<=0.
  The recovered proof uses the rank-15 trace pairing on sl4; exact leading
  Gram determinants for all fifteen lengths and both residues are supplied.
- `b14_10_four_cubic_top_replacements`: the four integral witnesses above.

Proof details are in docs/b14_10_indexed_proofs.md. Existing containment
rules and the n=3 padded-per2 exclusion now have typed application contexts.
The machine consumer rejects unknown/empty predicates; the cubic census
requests only conclusions of the form i_per3=0. It cannot silently apply
a quartic containment conclusion or ladder identity as cubic ideal vanishing.

**MEASURED reconciliation:** all **1,846** cell frontier sets are identical
to the frozen reconciliation after normalizing the legacy `r` label to `ell`.
The remaining frontiers are still 47 length-seven degree-nine cells, 52
length-eight degree-nine cells and 58 length-six degree-ten cells. No new
drop or multiplicity obstruction is claimed.

**ADOPTED frozen boundary, unchanged:** a24=274, determinant rank 273,
padded rank at least 269, D in [-4,+1]. Five sampled kernel vectors remain
five sampled vectors, not five certified equations. No LMR upper rank,
complete-interpolation result, i_red value or positive obstruction was reached.

## Validation and bounded resources — MEASURED

results/b14_10/validation.json passes exact path/digest accounting, all four
replacement proofs, nine theorem-rule positive/negative/context controls,
empty inventories, omitted rows, missing required sources, wrong digests,
unsupported supersession and malformed predicates. Each recovered witness
rejects an altered matrix entry, determinant, normalization, degree and HWV
coefficient, a missing point, a zero pencil and the forced-zero diagonal per3
control. Peaked-rule boundaries ell=16/17 and delta=ell-1 are checked; the
stable closure refuses missing dimension/witness premises and deficient rank.
The integral trace matrix rejects a duplicated row. PASS is restricted to
these enumerated checks; it is not a historical-corpus replay status.

Host: Windows, Python 3.12.14, numpy 2.3.5, 20 logical CPUs exposed,
33,752,997,888 bytes physical RAM, 12,627,238,912 bytes available at preflight.
This is a shared host, not an exclusive memory allocation. scipy, flint and
psutil were absent; nothing was installed. Exact small arithmetic used stdlib.
Numerical thread environments were capped at one and calculations ran serially.

Windows Job Objects enforce process memory before computation starts; the
wrapper gates the child until assignment, records its PID, and enforces wall
time with a subprocess timeout. Inventory/validation limits were 120 s/1 GiB;
each exact recovery was limited to 90 s/768 MiB. The four recoveries consumed
10.36 process-wall seconds total; maximum recovery peak commit was about
111 MB. Final inventory took 14.078 s with 120,549,376-byte peak commit;
release validation took 6.859 s with 202,194,944-byte peak commit. Resource
logs record actual UTC starts and monotonic durations; gaps between log times
are not CPU work and no CPU-hours extrapolation is made.

Two failures are preserved rather than hidden. The first inventory expanded
a compressed basis and reached the **enforced 1 GiB limit** after 19.594 s;
streaming payload hashes and a materialization ceiling corrected it. The first
bounded reconciliation failed in 0.047 s because runpy had not added the
script directory to sys.path; the wrapper was fixed and reconciliation then
completed in 0.109 s. Neither failed run produced a mathematical PASS.

## Assignment defects and remaining work

**RECORDED defects:** 874 is a historical list length, while the comparable
fresh discovery gap is 907. The 837 s79 number happens to remain current.
The packet's three absence categories omit B13-09's documented shipment-prefix
case. File-size shipping and producer expansion/deletion guards are different
mechanisms. `hybrid_kernel` is recognized but record-only, not an unknown kind.
The producer's repeated lower-bound field_note is wrong. The banked s57
dimension expression 15ell-30 requires a stabilizer qualification and fails
for a single traceless matrix (ell=2); that expression was not indexed or used.

**NOT REACHED / OPEN, with priced domain:**

- Complete cell semantics for 223 named historical files: one schema/reference
  review per file, with analyst time unmeasured. The register already gives
  claims, references, families and duplicate provenance; no numerical build is
  required merely to finish those keys.
- Original bytes for 837 s79 and 168 B13-09 files: still missing. The recovery
  queue records dimensions and historical producer times when available. For
  example s79 (13,7,2,2,2,1)_9 has N_S=19,505, n_chi=4,137, a=3 and a recorded
  11.3 s producer run; this is a historical measurement, not a Windows forecast.
  Seventeen missing s79 rows lack such producer references; runtime is unknown.
- Independent large hybrid/full-rank replay: requires the absent heavy
  dependencies and validated generators; this session did not price an entire
  campaign from compressed file size. Ninety-nine large present payloads were
  streamed but not materialized. Four compact replacements were the bounded
  alternative and do not remove that backlog.
- The 29 historical digest discrepancies need original payloads or authoritative
  uncompressed digests before semantic equivalence can be settled.

Focus next on those discrepancies and the named schema queue. Do not redispatch
the four replaced top cells as open research or treat any missing certificate
as a negative mathematical result.

## Deliverables and replay

Delivery directory:
`C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-10`.
The report, REPLAY.md, b14_10_evidence.zip, b14_10_astra.bundle, delivery_manifest.json,
bare-filename MD5/SHA256 sidecars and verification logs are placed there.
The ZIP includes scripts, exact certificates, proof texts, all register parts
and validation/resource logs. The bundle contains the named session branch;
the receiver needs the frozen base commit. The standalone exact witness
checker works directly from the ZIP using only Python stdlib.

The delivery checker is run against the captured base before bundle creation
and again with the actual bundle. The external delivery manifest and logs give
the final check outcomes, named ref, head/tree, prerequisite and file digests.
All work is confined to the prepared branch plus its authorized delivery folder
and automation memory; protected files are untouched. No push, integration
merge, new recurring task, or external message was performed.
