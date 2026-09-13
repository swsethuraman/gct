# B15-12: independent-padding scope and determinant-orbit feasibility

The nine-row restriction is inapplicable to independent z*per_3. Its correct essential-variable ceiling is ten, and a fresh determinant-one derivative minor proves that some length-ten Schur type occurs in coordinate degree ten. This is a scope correction, not a positive gap against det_4. The determinant-bound formula and small character controls are complete. The seven-cell numerical pilot is **RESOURCE_STOP: not launched because no heavy lease was granted**.

## Findings and evidence

| Finding | Status | Evidence |
|---|---|---|
| z*per_3 has ten essential variables; x_11*per_3 has nine | EXACT | Explicit polynomials, full derivative coefficient matrices and a 10 by 10 minor of determinant 1 |
| The inside-variable orbit closure is a proper subvariety of the independent one | EXACT | Singular specialization in one direction; closed derivative-rank condition excludes the reverse |
| Some length-ten partition of 40 occurs in C[X_ind]_10 | EXACT, existential | Nonzero degree-ten catalecticant minor plus subspace inheritance; no partition label claimed |
| The cited appendix does not transfer a nine-row clamp at fixed n | EXACT scope audit | IP v2 Appendix 7 Claim 7.1 changes the determinant size to polynomially bounded N |
| m_det<=sk(lambda,(delta^4))<=g(lambda,(delta^4),(delta^4)) | EXACT formula | Determinant stabilizer, Schur--Weyl decomposition, orbit restriction and full dual/transpose conventions |
| Character engine and receiver small controls | EXACT | Independent Jacobi--Trudi comparison for 209 character values through S_6, orthogonality, dimensions, integrality, sign and normalization controls |
| Seven-cell numeric bounds | RESOURCE_STOP, unlaunched | Code and exact class counts delivered; no values or finite-route competitiveness conclusion asserted |

The claim, hypotheses, source versions, proof and verifier dependencies are in `docs/b15_12_proved.md`, P1--P3. The four versioned primary PDFs are retained under `results/b15_12/sources/`, with exact-byte hashes in `source_manifest.json`. The original theorem/appendix pages were rendered and visually read to check superscripts, duals and orbit-closure bars. Rendered audit images are local intermediates; the versioned source PDFs are the retained inputs.

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

a, h and the nontrivial determinant floor in this table are inherited, not recomputed during the small controls. Zero floors are trivial. The Q1 control's h_pad=1, m_pad=1 and m_det=4 come from `Q1_combined_bound.json` with its explicit inherited B14-12 premises. It is already closed. The other six rows have no matching exclusion in the frozen scoped predicate ledger. The tail transport overlay has no applicable degree-seven/eight entry. These are launch-state facts; no unverified live worker results were imported.

U_pad=min(a,h_pad,a-L_pad), with L_pad=0 except the inherited Q1 floor 3. The pilot is implemented to check U_det>=r_det for each row and recount the ambient multiplicity of each selected shape. Since it has not run, this report supplies no numeric g, sk or tightened U_det. The ambient ceiling a remains a valid inherited upper bound.

Sizing counted p(28)=3,718 and p(32)=8,349, with 34,545 and 84,927 total cycle-type parts. The character cache has a 200,000-entry cap. The 195.3 MiB estimate uses a conservative 1 KiB per cache entry; it is a planning estimate, not a measurement. A 1,536 MiB Job Object is the requested hard aggregate limit. There is no HWV carrier allocation, no signed-Burnside quotient substitution and no assumption about source/evaluation cost from a stabilizer quotient. Full class tables would be split into 1,000-class shards below 5,000,000 bytes each.

## Resources, controls and stop

| Run | Return code | Wall seconds | Aggregate peak MiB | Limit |
|---|---:|---:|---:|---|
|b15_12_controls|0|1.527629|24.516|60 s / 512 MiB|
|b15_12_sizing|0|0.030109|17.383|60 s / 512 MiB|
|b15_12_receiver_controls|0|0.070957|17.387|60 s / 512 MiB|

All three runs used the assigned local Python, one process and one BLAS thread through the accepted native Job Object wrapper. The code uses integer/rational arithmetic; NumPy 2.4.6 and python-flint 0.9.0 imported successfully. The small receiver reconstructed the polynomial certificate and independent character controls from source, and its S_4 certificate fixture rejected an altered character value. No output is labelled geometric determinant replay.

The first preregistration commit was made at 06:49 UTC; the session later continued following the user's usage-reset message. The proof-audit clock span includes that interruption and is not a measured two-hour continuous run. The scope audit stopped when the cited appendix and exact minor settled the question; no further broad literature search was performed. No heavy calculation ran during the interruption or afterwards.

The lease record was read before considering the pilot and showed holders 01 and 03, with no slot-12 grant. Two attempts to send the lease request to the dispatch-named integrator were rejected by automatic approval review, including after its local task identity was checked. No task message was sent. A user authorization question remains pending. The request is recorded in `results/b15_12/lease_request.json`; canonical LEASES.json and INTAKE.json were not edited. This administrative resource stop says nothing about whether the seven coefficients would be expensive or useful. No lease release is needed because none was held.

## Replay and remaining work

Run from the existing assigned worktree. The exact executable is
`C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/.venv/python.exe`.
Use fresh log names when replaying to preserve this delivery's receipts.

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/.venv/python.exe' analysis/b15_bound.py --slot 12 --name b15_12_receiver_again --seconds 60 --memory-mb 512 analysis/b15_12_verify.py --controls-only --output 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/results/b15_12/receiver_again.json'
```

After an explicit integrator lease, the prepared pilot command is:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/.venv/python.exe' analysis/b15_bound.py --slot 12 --name b15_12_pilot --seconds 900 --memory-mb 1536 analysis/b15_12_orbit_bounds.py pilot
```

Its receiver command is `analysis/b15_12_verify.py --output results/b15_12/receiver_pilot.json` under a separately justified bounded run. The receiver recomputes every stored character using the original banked engine, checks full class coverage and exact contractions, and compares recorded floors. It does not merely eliminate a saved matrix. Neither full pilot nor full receiver is claimed tested by this delivery; the small fixture tests their certificate-reading contract.

The next sufficient missing evidence for this route is the seven exact sk coefficients. A useful coefficient below U_pad would still require a padded rank floor above it. For P2, the next missing witness is an explicitly labelled nonzero length-ten highest-weight projection; a derivative minor's weight is not automatically a highest weight. The independent-padding scope result by itself neither excludes an eligible cell nor establishes D>0.

## Delivery provenance

Frozen base commit `f365568d80d5f66fea2dd9342ff1998e1d866915`, tree `aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd`; tag object `80209c13e9ae33bad8933cb47413bf7710c96cb1`. Assigned existing branch `b15-12-padding-orbit-bounds`. Preregistration was the first commit, `3b263bd5ab1106b52ea61149943abc3e2f60a35e`, and contained only its intended preregistration file. Every new phase used gpt-6-astra with xhigh reasoning. Banked routines and B14-12 records retain their original attribution.

Input hashes are in the preregistration, `input_hashes.json` and the source manifest. Source edits are confined to slot-12 files. Native setup provenance was preserved and remains unstaged. No worktree, Git trust, ownership or sandbox setting was changed. No protected/shared theorem file was edited. New files are below the delivery size cap. The external final manifest, generated after the final commit, carries the exact head/tree and bundle hashes without self-reference. Delivery checking is a structural check, not a proof of the mathematics.
