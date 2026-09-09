---
board_numbering: batch13
session_id: B13-11
model: gpt-6-astra
reasoning_effort: xhigh
base_commit: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-11
---

# B13-11 — reconciled research ledger and control semantics

**RECORDED.** Delivery contains **one bundle part, `part00`**, plus the whole
bundle and whole-file/per-part MD5 and SHA256 checksums. This single Astra run
completed the bounded ledger/control assignment in the prepared isolated
checkout. No new search, point family, external publication, push, or follow-up
schedule was launched. Final candidate ranking remains batch 14's decision.

## Result and scope

**CERTIFIED (integer census); ADOPTED (inherited exclusions).** The complete
weight-13 census of tails with at most five parts has 57 shapes, ten with zero
stable ambient multiplicity and 47 with positive multiplicity. The reconciled
quartic record closes 26 positive blocks; the sixteen independently replayed
stable blocks contribute two additional closures, giving **28** in their union.
The remaining **19** all have at most three tail parts, hence quartic length at
most four. The existing padded-containment theorem excludes a positive padded
gap on all nineteen. Therefore **zero blocks in this stated census remain open
for `D > 0` after inherited exclusions**. This does not assert full determinant
rank on the nineteen blocks, nor a theorem at larger tail weights or lengths.

**RECORDED.** The legacy full-rank quartic view grows from **326 to 1,521 distinct
cells** (1,195 additions). The full research record has **5,375 cells and 6,862
observations**, including 1,522 quartic determinant-rank cells: the 1,521
full-rank cells plus LMR. The other entries retain dimension/cost information
or cubic/control measurements. No ambient-dimension conflicts were found.
Deduplication uses `(polynomial degree n, partition lambda, coordinate degree)`;
observations and all their provenance remain attached to the shared cell.

**RECORDED.** The machine-readable inventory joins the explicitly imported
records with the frozen s60 closing cells, s71 queue, s79 Q1/Q2 queues, and the
s79 cubic queue. It contains **14,783 distinct cells**, including 14,167 quartic
entries. Of these, 11,991 remain open in this bounded inventory; it is not an
exhaustive census of all mathematical candidates. The file manifests specify
the exact region and sources.

| Frozen queue | Cells | Closed by reconciled rules | Still open |
|---|---:|---:|---:|
| s79 Q1 | 123 | 121 | 2 |
| s79 Q2 | 10,513 | 635 | 9,878 |
| Cubic degree 10, length six | 402 | 296 | 106 |

**ADOPTED / RECORDED.** Q2 originally had 9,952 unmeasured entries. An additional
74 are excluded by the reconciled records and inheritance, leaving 9,878.
The cubic remainder is unchanged: **95** weights with `N_S < 10^7` and **11**
at or above that cutoff. Its objective is the cubic ideal screen; cubic
full-rank results alone do not exclude a positive quartic padded gap. Across
the imported dimension sources, 363 nonzero tails have whole-ladder determinant
exclusions; ten zero stable blocks are recorded separately.

## Mathematical and data semantics

**PROVED.** For the common ambient multiplicity `a`,
`D = mult_pad - mult_det = i_det - i_pad`. A finite modular evaluation rank
`k` supplies a rank floor, hence `0 <= i_X <= a-k`. A full-rank certificate
gives `i_X=0` over Q after source validation. A deficient sample does not
provide a rational ideal element. The 59 reducible deficiencies among s79's
682 cells remain **MEASURED**, regardless of old `exact`, `i_red`, or status
strings. They do not support a lower bound on the reducible ideal dimension.

**ADOPTED.** The closure dependencies are Lemma L and Proposition S in
`docs/s57_report.md`: ideal dimension is nondecreasing along a tail ladder;
the ambient dimension is bounded by `a_inf`. A full determinant rank at
`a=a_inf` closes the entire ladder. A full-rank cell closes lower rungs;
upward transport requires equal ambient dimension or established stability.
The additional length-at-most-four exclusion is the containment theorem of
`docs/n4_gate.md` section 1. Generic four-variable cubics have a 3-by-3
determinantal representation; `ell*c = det diag(ell,M)` then puts the
reducible locus, and hence the padded locus, in the determinant closure.
This is a containment exclusion, not an empty-determinant-ideal assertion.

**RECORDED.** `negative_record()` retains its historical tuple contract and
returns only full-rank quartic exclusions. The original snapshot is available
as `legacy_negative_record()`. `b13_11_ledger.load_record()` exposes the complete
record, including LMR and n=3. Existing callers that interpret every key as
closed therefore cannot accidentally treat LMR as a negative result.

**CERTIFIED (regression checks).** The old census stripped zero padding from
record tails while its census dictionary retained five-part padding; this
lost shorter-tail joins. The new join normalizes for matching and preserves
the caller's keys. It also explicitly unions the stable and quartic records.
`open_on_both_instruments` denotes absence from those two rank records;
`open_on_all_instruments` additionally applies the inherited containment rule.

## Verification actually performed

**CERTIFIED.** All **sixteen stable blocks passed 192/192 independent checks**,
using `wk12_int_s79_stable_verify.py`: exact weight-space enumeration, exact
ambient multiplicity, every kernel vector on the independent raising
operators, independent evaluation via principal minors, agreement of the
evaluation matrices up to the declared global sign, full rank at both house
primes, and tracelessness of every point. The wrapper includes the eleven
calibration blocks and five `a_inf=4` blocks. No term was silently discarded.

**CERTIFIED (matrix arithmetic); ADOPTED (native source evaluations and LMR
upper bound).** The LMR replay recomputed `msym_u` from all delivered integer
points in the determinant, padded and generic families, checked every stored
u-value and the absence of u-zero columns, and applied
`rows_native[i,j] * msym_u(P_j)^(24-rung_i)` before elimination. Both primes give
determinant rank **273**, padded rank **269**, and generic rank **274**.
The output records the transform next to the results, every u-value, and the
exact point-file references. This is a replay of banked matrix arithmetic;
the native filling evaluations were not regenerated.

**ADOPTED.** Combining the determinant floor with LMR's upper bound gives
`rank T_det = 273` exactly and `i_det=1`. The padded floor is **269**; therefore
`D = 1-i_pad(24)` remains in **[-4,+1]**. The sampled value -4 remains
**MEASURED**. The rational lift needed to identify `i_pad(24)` with `i_pad(23)`
remains unresolved. No epsilon-pad or reducible-membership claim was promoted.

**CERTIFIED / PROVED.** A further **28/28 control checks** passed, including
the LMR checks and the four n=3 minor replays below. **25/25 semantic regression
checks** passed, covering the two omitted s60 cells, duplicate identity,
malformed weights, conflicting dimensions, deficient-rank direction, zero
padding, the LMR API boundary, and all inventory/census counts. `git diff
--check` passed.

## The n=3 control, with its two comparisons separated

**CERTIFIED (minor arithmetic).** The six integral degree-12 fillings at
`lambda=(19,7,2,2,2,2,2)` in the existing S4 control give these nonzero minors,
recomputed directly by the integer Leibniz determinant formula:

| Family | Minor order | p=2147483647 | p=2147483629 |
|---|---:|---:|---:|
| determinant | 5 | 1039976059 | 898798153 |
| unpadded per3 | 6 | 1018711257 | 718047479 |

**ADOPTED.** The existing unpadded positive example has `a=6`,
`mult_det=5`, and `mult_per3=6`, so its unpadded gap is +1. The upper bound on
determinant rank comes from LMR, as correctly explained in
`docs/s63_report.md` section 3. The note in `results/s63_n3control.json`
reverses the modular rank inequality and must not be used as that upper
bound. The separate permanent-pencil certificates and S4 point/source files
are retained as dependencies; this run did not discover a new positive cell
or rerun their large native source evaluations.

**PROVED.** The padded cubic is `z*(a*d+b*c)`. Its five first derivatives have
nonempty disjoint monomial supports, so it has exactly five essential
variables. Every pullback lies in the closed subspace variety `Sub_5`.
Its coordinate ring has no Schur constituent of length greater than five.
Thus the seven-row weight has `mult_pad=0`, `i_pad=6`, and padded gap **-5**.
The unpadded positive example consequently supplies no padded test at this
weight. The exact derivative coefficient matrix is included in the control
artifact with its value convention.

## Certificate availability and unresolved work

**CERTIFIED (file hashes).** All **1,200 declared-shipped s79 files** are
present and match their manifest MD5. Of the other 866 manifest entries,
**837 are absent** and **29 have local calibration files with different
digests**. The latter were marked unshipped in the final manifest; they are
different local versions, not silently accepted as that manifest's files.
The availability inventory records expected and actual digests, byte sizes,
shipping declarations and per-file unresolved flags. Missing files and version
mismatches are not mathematical negatives.

**RECORDED.** Most quartic source certificates were not independently replayed
here. Imported full-rank claims are **ADOPTED**, with review scope,
certificate references and missing-file flags per observation. s79's Part-2
integrator check audited record consistency and dimensions; it is not a replay
of every numerical rank certificate. The report does not equate it with the
independent stable-block replay.

**RECORDED (priced continuation).** Regenerating missing certificates requires
the original per-cell builders and seeds in the frozen records. The inventory
retains measured seconds, reported peak memory, `N_S`, `n_chi`, and the
`N_S*delta` work proxy where available; absent prices are explicit flags.
The reported difficult-cell construction wall is approximately
`N_S*delta=1.47e8`, exceeding 4 GB in the historical engine. This run did not
attempt those builders or estimate a universal wall time from that proxy.
An exact padded/reducible membership calculation at LMR remains outside this
assignment; it is not replaced by further sampled nullities.

## Execution, defects in the brief, and replay

**RECORDED.** Actual model: **gpt-6-astra**, xhigh, as configured for this
automation. Python 3.12.14 and NumPy 2.3.5 were available. FLINT, SymPy and
SciPy were absent; the attempted local installation failed because network
socket access was restricted. No installation succeeded and no global
configuration changed. Exact object-integer counting and the existing small
independent arithmetic routines completed the assignment without downgrading
an exact computation to sampling. Singular/msolve were absent and unused.

**RECORDED.** One numerical worker and one BLAS thread were used. Every
computation ran under a Windows Job Object with a **1-GiB process-memory cap**
and **600-second wall cap**, with PID and resource observations logged. The
stable replay took 15.1 s, controls 20.5 s, census under 0.5 s, inventory 1.5 s,
and semantic checks 0.6 s in their recorded bounded runs. Physical RAM was
33.75 GB; available RAM was measured before each run (initially 7.40 GB).
No worker reached its wall or memory cap. Early adapter errors and their
tracebacks are retained; the final runs pass.

**RECORDED (assignment defects).** The prepared checkout has the frozen HEAD
but no `main` ref, so the user's frozen base replaces the generic clone/main
instruction. s57 and s63's quartic files carry dimensions and prices rather
than the additional rank measurements implied by the board. The board did not
name the length-at-most-four containment source: locating `docs/n4_gate.md`
was necessary to avoid presenting the nineteen rank-record omissions as open
padded candidates. The batch-12 stocktake/reviews retain older overstatements;
the controlling board and corrections govern all claims here.

**RECORDED.** Preregistration and its dated addendum were committed before the
computations they govern. Completed stable and control units were banked
separately. No history was rewritten. To replay, use the bundled Python and
run `analysis/b13_11_run.py --name <unique_name> --seconds 600 <script>` for
`analysis/b13_11_verify_stable.py`, `analysis/b13_11_controls.py`,
`analysis/wk12_int_w13_census.py --weight 13 --out results/b13_11/weight13_census.json`,
`analysis/b13_11_reconcile.py`, `analysis/b13_11_inventory.py`, and
`analysis/b13_11_validate.py`, in that order. Run from this isolated checkout.
Use fresh log names to retain previous replay logs. The manifests index all
output parts and input/output hashes. The user-facing results folder carries
whole-file copies and the bundle for application to the recorded base.
