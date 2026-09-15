# B15-08 preregistration

Model for proof, coding, controls, analysis and delivery: gpt-6-astra, xhigh reasoning as dispatched. No additional agents. Banked B14-06 mathematics and code retain their Claude Opus 5 attribution; the new extension is this session's work.

## Readiness and frozen inputs

Existing worktree B15-08 and branch b15-08-new-brackets retained. HEAD and batch15-base resolve to f365568d80d5f66fea2dd9342ff1998e1d866915; tree aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd; annotated tag object 80209c13e9ae33bad8933cb47413bf7710c96cb1. Compared before changes. No applicable AGENTS.md was found in this worktree or its project ancestors. Read the common preamble, accepted state, brief, wording guide, B14-06 report and source entry points. The native READINESS.md records a passed bounded runtime control; preserved setup logs are not research outputs.

Exact-byte SHA-256 of the local input files (CRLF is retained where present):

| File | SHA-256 |
|---|---|
| analysis/b14_06_bracket.py | d67a78c39694b1d4229970fd1bec46213913935030afcfae5165d2697d68b493 |
| analysis/b14_06_points.py | 17f7b435ffe6dc796ed709c6fa554a43e804957e0b4986cb6361d20a41901aaf |
| analysis/b14_04/recount.py | b6493216beebe4487691cdc0a1e12d01d779673bbaf3f0e0c952d64ce40efe83 |
| results/b14_06/selftest.json | 1fceae142e1e850d8a89a9c84a3edc597385d78f44e4d7375267486f3551c8c6 |
| docs/batch15/ACCEPTED_STATE.md | 9805ecc550bae5dbdfe845e280f42a0c2b03e0b6989e819e5a3d93e62f59148c |
| results/integrate/inherited_exclusions.json | b71469d2d3db97e4d16f6b9b4be6f77ac1cfc00ea286b2e9cedefcec43b1458b |
| results/b15_prep/transport_overlay.json | b594dcdae7b4b448039d705d6f15f319e245a0d2cf3636f8b08b15cbfc42b4df |

## Question and representation

Extend explicit bracket evaluation on Z = Sym^2(V'^*) + Sym^3(V'^*) + Sym^4(V'^*) to tails with conjugate (h,h,2,1^k), particularly (t,3,2^6) at h=8, t>=3, k=t-3. The weighted degree is W=2h+2+k. The coordinate algebra is Sym(Sym^2 V' + Sym^3 V' + Sym^4 V'); the upper triangular highest-weight convention uses e_0 singletons and e_0 wedge e_1 for the short column. The stable multiplicity a_inf is the Schur coefficient in this algebra, not the number of brackets. The associated quartic convention is n=4, ell=h+1, lambda=(4*delta-W, tail), with stable identification inherited only for delta>=W. No finite-degree assertion is obtained by guessing a stabilization degree.

A letter of valence d places at most one slot in each alternating column; unused slots are e_0. Define sources over the integers using symmetric tensor entries, with ordinary polynomial coefficient alpha equal to d!/prod(alpha_i!) times the tensor entry. Store explicit integral point constructions. Tensor derivatives divided by falling factorials must agree with these entries. Degree-three data are needed where a letter meets all three columns. For Pad use independent padding z*per3 in ten essential variables, followed only by an explicitly identified linear map; a nine-variable restriction is a rank-floor witness and is never asserted to parametrize all ten-variable points.

## Algorithm and predeclared controls

Expand the height-two column in its two signed permutations. Each term leaves scalars, vectors and matrices for the two height-h columns. Reorder the column slots with explicit parity and evaluate the resulting bordered determinant. Extract the multilinear matrix coefficient by finite differences: sum over subsets of labelled matrix copies, grouping identical matrices with binomial weights. Homogeneity removes every monomial except the desired multilinear one; this retains repeated-letter factorials without a large carrier. A brute epsilon contraction uses independently enumerated permutations at h=2 and h=3.

Enumerate signatures by degree and subset of columns; count source rows and determinant work before allocating an evaluation matrix. Recount a_inf by B14-04's exact rational power-sum recurrence and Murnaghan-Nakayama inner product, with small known Schur controls. Choose the smallest nonzero full-height prototype that passes sizing, initially searching t=3..9. If useful, modest larger tails may be sized, never launched without a measured envelope and lease.

Controls: exact formula/brute agreement on nonempty small sets and rational points; independent known nonzero two-column determinant control; column swap sign, repeated vector/letter zeros, repeated-matrix factorials; torus weight and upper triangular highest-weight behavior; integral coefficients versus polynomial jets and Euler relations; valid determinant and independently padded permanent parameters with direct polynomial evaluation. Alter signs, factorial factors, tensor entries or normalization to ensure the checks detect defects. All sampled ranks must be at most counted a_inf. Generic full rank equal to the exact a_inf certifies ambient completeness for that cell only; deficient ranks are floors, never global ideal lower bounds.

## Resources and decisions

Read LEASES.json: initial holders 01 and 02; slot08 has no heavy lease. Begin with proof, code, counts and small controls. Local executable is the assigned .venv/python.exe (absolute path in shell commands). One process and one BLAS thread; all research numerical runs use analysis/b15_bound.py. Small controls initially have a 60-second, 512-MiB cap. Request a heavy lease before production. Maximum pilot 900 seconds, 1536 MiB aggregate; only a measured pilot can justify a 5400-second production attempt. Record construction, evaluation and reduction costs separately. No unchanged repeat after a resource stop.

Success requires the derived evaluator, exact small brute controls and at least one full-height generic rank equal to its exact ambient count within the envelope. If the contraction width or host lease prevents this, deliver the certified small evaluator and explicit cost/availability limitation, with no completeness claim. Determinant or Pad controls do not need a desired rank. Apply typed inherited predicates and the accepted overlay before cell evaluation. For an actual gap calculation use U_pad=min(a,h_pad,a-L_pad,other valid bounds); absent additional bounds use the valid conservative a. A determinant floor reaching U_pad excludes positive D. A positive D requires a global determinant upper bound and a larger padded floor; no such outcome is assumed.

## Delivery

Preserve setup provenance untracked. Commit this preregistration first with model attribution, stage intended slot08 artifacts only, then deliver per-slot proof/report, explicit sources and points, outcomes, replay commands and resource receipts. Proposed exclusions are separate and may be empty. Do not modify shared records, protected papers, trust configuration, ownership or worktree layout. Do not push. Run the prescribed committed-object and bundle checks after the final commit, using a fresh delivery directory and one-ref delta bundle.
