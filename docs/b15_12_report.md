# B15-12: independent-padding scope and determinant-orbit feasibility

The nine-row restriction is inapplicable to independent z*per_3. Its correct essential-variable ceiling is ten, and a fresh determinant-one derivative minor proves that some length-ten Schur type occurs in coordinate degree ten. This is a scope correction, not a positive gap against det_4. The seven-cell determinant-orbit pilot and full character receiver are now **EXACT and complete**. Every symmetric Kronecker bound exceeds the ambient multiplicity, so U_det=a in all seven cells. The broad sweep stops as preregistered: these bounds are inexpensive but uninformative at these parameters.

## Findings and evidence

| Finding | Status | Evidence |
|---|---|---|
| z*per_3 has ten essential variables; x_11*per_3 has nine | EXACT | Explicit polynomials, full derivative coefficient matrices and a 10 by 10 minor of determinant 1 |
| The inside-variable orbit closure is a proper subvariety of the independent one | EXACT | Singular specialization in one direction; closed derivative-rank condition excludes the reverse |
| Some length-ten partition of 40 occurs in C[X_ind]_10 | EXACT, existential | Nonzero degree-ten catalecticant minor plus subspace inheritance; no partition label claimed |
| The cited appendix does not transfer a nine-row clamp at fixed n | EXACT scope audit | IP v2 Appendix 7 Claim 7.1 changes the determinant size to polynomially bounded N |
| m_det<=sk(lambda,(delta^4))<=g(lambda,(delta^4),(delta^4)) | EXACT formula | Determinant stabilizer, Schur--Weyl decomposition, orbit restriction and full dual/transpose conventions |
| Character engine and receiver small controls | EXACT | Independent Jacobi--Trudi comparison for 209 character values through S_6, orthogonality, dimensions, integrality, sign and normalization controls |
| Seven-cell numeric bounds | EXACT | Complete class-character sums, ambient recounts and separate full-row reconstruction; every bound exceeds a |

The claim, hypotheses, source versions, proof and verifier dependencies are in `docs/b15_12_proved.md`, P1--P4. The four versioned primary PDFs are retained under `results/b15_12/sources/`, with exact-byte hashes in `source_manifest.json`. The original theorem/appendix pages were rendered and visually read to check superscripts, duals and orbit-closure bars. Rendered audit images are local intermediates; the versioned source PDFs are the retained inputs.

Kadish--Landsberg v1, Theorem 1.2 and Proposition 1.12, give the M+1 convention; BIP v3, Theorem 2.1, uses inside-variable padding. BIP's no-occurrence Theorem 1.4 assumes n>=m^25 and cannot decide (4,3). The appendix supplies no fixed-size ring map. These source distinctions are recorded without asserting that the published theorems are wrong.

## Exact point and representation convention

n=4, W=C^16, point family f=z*per_3 in ten independent variables followed by six unused variables. Coefficient degree is delta. Positive partitions have size 4delta; the repository uses S_lambda V in Sym^delta(Sym^4 V), where V=W*. Coordinate multiplicities m, ambient multiplicities a, ideal multiplicities i and pullback upper bounds h are kept separate. No point sampled on det_4 is used for a fresh rank floor in this session.

The padding certificate uses ordinary monomial coefficients and actual formal derivatives. z is variable 0, and x_11,...,x_33 are variables 1,...,9 in row-major order. All polynomial coefficients are integers. There is no modulus, interpolation uniqueness issue, factorial-symbol conversion, u multiplication or modular-to-rational lifting. The derivative minor proves essential-variable scope, not a highest-weight determinant obstruction.

The character pilot uses R=(delta,delta,delta,delta), not (4 repeated delta times) by silent convention. Conjugating both rectangular factors would preserve the bound, and the proof explains why; conjugating lambda is not allowed as a label substitution. Symmetric-square refinement uses the plus sign because matrix transpose acts by the ordinary flip. Orbit upper bounds constrain the closure by restriction but need not equal its multiplicity.

## Fixed pilot and sizing

The brief's four degree-eight entries were resolved, before measurement, as the first four entries in the reviewed small panel. Its two a=1 cells are the first two survivors in `candidate_preflight.json`. The seventh row is the stated Q1 control. No replacement or expanded sweep was performed.

| delta | lambda | a | h_pad_ub | U_pad_ub | inherited r_det_lb | class count |
|---|---|---:|---:|---:|---:|---:|
|8|(13,11,3,2,1,1,1)|2|2|2|0|8,349|
|8|(12,11,4,2,1,1,1)|3|3|3|0|8,349|
|8|(11,11,5,2,1,1,1)|4|3|3|0|8,349|
|8|(11,10,6,2,1,1,1)|7|4|4|0|8,349|
|7|(11,8,5,1,1,1,1)|1|1|1|0|3,718|
|7|(13,5,5,2,1,1,1)|1|5|1|0|3,718|
|8|(12,4,4,4,4,4)|4|1|1|4|8,349|

The a values were freshly recounted during the full pilot and agree with the preregistered inputs. h and the nontrivial determinant floor remain inherited. Zero floors are trivial. The Q1 control's h_pad=1, m_pad=1 and m_det=4 come from `Q1_combined_bound.json` with its explicit inherited B14-12 premises. It is already closed. The other six rows have no matching exclusion in the frozen scoped predicate ledger. The tail transport overlay has no applicable degree-seven/eight entry. These are launch-state facts; no unverified live worker results were imported.

U_pad=min(a,h_pad,a-L_pad), with L_pad=0 except the inherited Q1 floor 3. The pilot checked U_det>=r_det for each row. Its exact results are:

| delta | lambda | rectangular g | symmetric sk | U_det=min(a,sk) | U_pad |
|---|---|---:|---:|---:|---:|
|8|(13,11,3,2,1,1,1)|4,866|2,442|2|2|
|8|(12,11,4,2,1,1,1)|9,155|4,545|3|3|
|8|(11,11,5,2,1,1,1)|8,636|4,347|4|3|
|8|(11,10,6,2,1,1,1)|21,023|10,463|7|4|
|7|(11,8,5,1,1,1,1)|2,269|1,168|1|1|
|7|(13,5,5,2,1,1,1)|2,394|1,227|1|1|
|8|(12,4,4,4,4,4)|1,373|804|4|1|

The symmetric refinement substantially reduces g, but still gives no improvement over a. This is a finite seven-cell conclusion; it proves no asymptotic limitation. No new exclusion or positive gap follows. The Q1 result is consistent with its inherited determinant floor 4.

Sizing counted p(28)=3,718 and p(32)=8,349, with 34,545 and 84,927 total cycle-type parts. The character cache has a 200,000-entry cap. The 195.3 MiB estimate used a conservative 1 KiB per cache entry; it was a planning estimate, not a measurement. The full job measured 89.004 MiB under the granted 1,536 MiB Job Object limit. There was no HWV carrier allocation or signed-Burnside quotient substitution. Thirteen complete class-character shards total 4,898,050 bytes; the largest is 477,387 bytes. Each has at most 1,000 classes and is hashed in `pilot.json`.

The rectangle and squared-cycle character construction took 0.107091 s for S_28 and 0.281697 s for S_32. The seven lambda character rows took 1.185621 s total. Exact scalar contractions took 0.008353 s, and ambient plethysm recounts took 0.059550 s. Total wrapped runtime was 1.946468 s, including class enumeration, checks, serialization and remaining overhead. Construction dominates the tiny contraction cost; geometric evaluation was not performed. Detailed per-cell timings and cache statistics are in `pilot.json`.

## Resources, controls and stop

| Run | Return code | Wall seconds | Aggregate peak MiB | Limit |
|---|---:|---:|---:|---|
|b15_12_controls|0|1.527629|24.516|60 s / 512 MiB|
|b15_12_sizing|0|0.030109|17.383|60 s / 512 MiB|
|b15_12_receiver_controls|0|0.070957|17.387|60 s / 512 MiB|
|b15_12_pilot|0|1.946468|89.004|900 s / 1,536 MiB|
|b15_12_receiver_pilot|0|2.089136|53.629|60 s / 512 MiB|

All five runs used the assigned local Python, one process and one BLAS thread through the accepted native Job Object wrapper. The code uses integer/rational arithmetic; NumPy 2.4.6 and python-flint 0.9.0 imported successfully. The receiver reconstructed the polynomial certificate and independent small character controls from source, and its S_4 certificate fixture rejected an altered character value. The full receiver recomputed all stored characters with the original banked routine, checked complete class coverage, exact g/sk contractions and floor consistency. Both full-row implementations use Murnaghan--Nakayama; the separate Jacobi--Trudi control is the independent algorithm. No output is labelled geometric determinant replay.

The first preregistration commit was made at 06:49 UTC; the session later continued following the user's usage-reset message. The proof-audit clock span includes that interruption and is not a measured two-hour continuous run. The scope audit stopped when the cited appendix and exact minor settled the question; no further broad literature search was performed. No heavy calculation ran during the interruption or before a lease was granted.

The first delivery was a proof-and-controls fallback while the lease request was pending. Automatic approval review rejected outbound task messages; none was sent. The integrator then read the local request directly, queued slot 12, and granted the lease after slot 06 released it. This removed the need for outbound-message approval. `lease_grant.json` records the checked LEASES.json hash and holders 01/12. The pilot ran at 14:54:33 UTC. Its measured runtime, peak and results were reported in this task and `pilot_measurement.json` before the smaller full receiver began at 14:55:10 UTC. No expanded search or production extension occurred.

The lease was explicitly released at 14:55:24 UTC in `lease_release.json`, with both return codes, start times, resource peaks and a fresh check that PIDs 37452 and 26100 were absent. No further heavy work is planned. The integrator alone updates canonical LEASES.json and INTAKE.json; this worker did not edit them. The earlier RESOURCE_STOP is preserved as history in the first delivery and superseded by the completed pilot.

## Replay and remaining work

Run from the existing assigned worktree. The exact executable is
`C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/.venv/python.exe`.
Use fresh log names when replaying to preserve this delivery's receipts.

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/.venv/python.exe' analysis/b15_bound.py --slot 12 --name b15_12_receiver_again --seconds 60 --memory-mb 512 analysis/b15_12_verify.py --output 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/results/b15_12/receiver_again.json'
```

The completed pilot used:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/.venv/python.exe' analysis/b15_bound.py --slot 12 --name b15_12_pilot --seconds 900 --memory-mb 1536 analysis/b15_12_orbit_bounds.py pilot
```

The full receiver command above is the concise replay: it reads the complete class shards and recomputes their characters using the banked engine. It does not merely eliminate a saved matrix. Both pilot and full receiver completed successfully. Re-running the pilot requires a new scheduling decision and care to preserve existing output files; an unchanged broad sweep is not justified by these results.

The next sufficient missing witness for a positive gap is a stronger global determinant-closure upper bound below U_pad, together with a padded rank floor exceeding it. Repeating these exact orbit bounds cannot provide that witness at these seven cells. For P2, the next missing witness is an explicitly labelled nonzero length-ten highest-weight projection; a derivative minor's weight is not automatically a highest weight. The independent-padding scope result by itself neither excludes an eligible cell nor establishes D>0.

## Delivery provenance

Frozen base commit `f365568d80d5f66fea2dd9342ff1998e1d866915`, tree `aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd`; tag object `80209c13e9ae33bad8933cb47413bf7710c96cb1`. Assigned existing branch `b15-12-padding-orbit-bounds`. Preregistration was the first commit, `3b263bd5ab1106b52ea61149943abc3e2f60a35e`, and contained only its intended preregistration file. Every new phase used gpt-6-astra with xhigh reasoning. Banked routines and B14-12 records retain their original attribution.

Input hashes are in the preregistration, `input_hashes.json` and the source manifest. Source edits are confined to slot-12 files. Native setup provenance was preserved and remains unstaged. No worktree, Git trust, ownership or sandbox setting was changed. No protected/shared theorem file was edited. New files are below the delivery size cap. The external final manifest, generated after the final commit, carries the exact head/tree and bundle hashes without self-reference. Delivery checking is a structural check, not a proof of the mathematics.

The original fallback bundle in `delivery/b15_12_final` remains preserved. The completed pilot delivery uses the fresh directory `delivery/b15_12_completed`. The pilot and receiver ran the code already committed at `f57316b64975dc2ef0d93bdd4b821eba22a02204`; no implementation change was needed after those runs.
