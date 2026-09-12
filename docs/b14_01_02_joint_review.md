# B14-01 + B14-02: completed degree-13 interpolation and the LMR consequence

Integrator review, September 12, 2026. **New combined result:** B14-01's 72 mixed target members, supplemented by **source row 15 from B14-02, pulled back to (ell,c)**, give a complete 73-dimensional target at both house primes. B14-02's exact sampled kernel therefore consists of genuine equations. With the banked source-dimension and determinant certificates, **i_red(13)=3** and **D_LMR is in [-4,-2]**. The positive multiplicity obstruction at the degree-24 LMR cell is excluded. The exact value D=-4 remains open.

This is an integration deduction from the delivered data, not a claim either individual report made. It supersedes the weaker conditional [-4,-1] route in the preceding B14-01 review. The repository's general certificate registry and PROVED ledger have not been modified.

## Answer to the search question

B14-01 used a hybrid, bounded search: strip-directed random fillings, a small deterministic greedy/rotating pass, and further random searches including overlap-stratified candidates. The implementation is **not an exhaustive spanning enumeration** and has no finite-time guarantee of finding 73 directions.

The function called `semistandard_fillings` describes itself as “semistandard-style”; it does not enforce row-weak inequalities and does not enumerate all semistandard tableaux. Determinism alone is not a completeness guarantee. The local diagnostic from the earlier review found all 49 generated fillings in a 60-attempt first-strip sample failed row-weakness in the numerical label order after column sorting.

There is also an unsafe screen for a completeness claim: candidates zero on the first three probe points are skipped before the full 96-point row is evaluated. Vanishing at those three points does not imply that the polynomial is zero or that its full evaluation row is redundant. This may save search time but cannot be retained as a proof of exhaustive coverage. The review does not establish that this screen caused the actual missing direction.

The full mixed-bracket family has a characteristic-zero spanning proof, supplied in B14-05: project the spanning column-wedge tensors equivariantly into Sym^13(V) tensor Sym^13(Sym^3(V)). The projection spans the required highest-weight space. An exhaustive, correctly implemented enumeration with exact dependence checks can therefore recover a basis in principle. That theorem does not certify the truncated sampler or guarantee that arbitrary fixed finite-field points distinguish a basis.

The joined 73-minor now proves that the actual P13 points do distinguish the target. It also disproves the idea that the target itself is only 72-dimensional. We have not localized which omitted single mixed filling would have completed B14-01's sampler. We instead supplied a different, explicitly defined target polynomial that completes its span.

## The missing direction was already in the source delivery

Let g_1,...,g_72 be B14-01's mixed target polynomials, and F_15 the source polynomial indexed **15, zero-based** in `results/s74/source.json` and B14-02's matrix. This is the sixteenth row. It is native degree 13, so no transport factor is needed. Define

    g_73(ell,c) = F_15(ell*c).

This is a genuine member of N13: restriction has bidegree (13,13), preserves the highest-weight type (21,17,2^7), and uses the stated ordinary coefficient and factorial-symbol conventions. A target member need not be a single mixed bracket; this pullback is an exactly specified polynomial and, by the slot-expansion identity, a finite sum of mixed brackets. There is no need to expand its 4^13 slot choices.

All 96 primary point definitions agree across the two deliveries. Append B14-02's integer matrix row 15, reduced modulo the prime, to B14-01's 72 target rows. The resulting 73-by-96 matrix has a nonzero 73-minor at both primes:

| Prime | Target rank before | Target rank after | Completed minor determinant |
|---|---:|---:|---:|
| 2147483647 | 72 | 73 | 1832982837 |
| 2147483629 | 72 | 73 | 1811606566 |

Exact column indices and point IDs are in `results/b14_01/certificate_d13.json` under `minor_certificate` (`point_ids`, `point_index_in_primary`, `u_symbols`). *Corrected at the batch-14 close: this sentence named `joint_certificate.json`, a file that was never written — the content is in the certificate above. Found by `tools/integrate/scan_unstaged.py --root docs`.* Replacing the added row with a duplicate of an existing target row leaves rank 72, as it must.

Using a source pullback to complete the target is not circular: its membership follows from the polynomial restriction map before knowing any source kernel. Its nonzero target minor is an independently checkable numerical statement. Neither step assumes that the three candidate equations vanish identically.

## Why the three equations are now genuine

Write phi:M13->N13 for restriction to ell*c and E for evaluation at the 96 primary points.

1. The independently recounted target dimension is **73**.
2. The completed target minor proves rank(E)>=73 over Q, so E is injective on N13.
3. B14-02 gives the exact 39-by-96 source matrix A, with source vectors as rows.
4. Exact integer checks give A^T K=0, rank(K)=3 and rank_Q(A)=36.
5. Therefore ker(E phi)=ker(phi), and **dim ker(phi)=39-36=3**.

The source really has 39 independent vectors. In addition to the inherited dimension count, the review reconstructed the degree-13 transport of the same 39 source entries on S74's banked generic values. Their 39-minors are nonzero at both primes (1497446691 and 1417764581). This prevents a coefficient-space kernel from being confused with a redundant choice of source generators.

The actual three equations are compactly explicit:

    Q_j = sum_(i=0..38) K[i,j] F_i^up13,  j=0,1,2.

`results/b14_02/kernel_primary.json` records their coefficient matrix as `left_kernel_K` (39 x 3, with `A_transpose_K_is_zero`), and the source filling definitions are in `results/b14_01/members_d13_merged.json`. *Corrected at the batch-14 close: this sentence named `exact_relations.json`, a file that was never written.* These are integer representatives of a rational basis; no assertion of a saturated integral-lattice basis is made. The same three vectors from B14-02 can now be certified as equations, rather than merely saying that some two combinations must exist.

## Consequence at degree 24

Multiply each Q_j by msym_u^11, where msym_u=24*[x1^4]f. This is multiplication by a nonzero highest-weight polynomial in an integral polynomial ring, so it preserves linear independence and ideal membership. The weight becomes

    (21,17,2^7) + (44) = (65,17,2^7).

The equations vanish on every reducible quartic ell*c, hence on every padded ell*per3. Thus **i_pad(24)>=3**. The existing padded rank floor 269 in the 274-dimensional source gives **i_pad(24)<=5**. The established determinant multiplicity 273 gives

    D = (274-i_pad(24))-273 = 1-i_pad(24),
    3 <= i_pad(24) <= 5,
    -4 <= D <= -2.

This rules out D=+1, D=0 and D=-1 at this cell. It does not establish whether the two additional sampled padded relations are genuine, nor does it settle the search for multiplicity obstructions at other weights.

In the S74 literal degree-24 source, the transported equations use the same K coefficients on the first 39 rows and zeros on the remaining 235 rows: both descriptions multiply each native row by the same msym_u^(24-native_degree).

## Verification performed here

- B14-02 bundle and part00 MD5 both match `983029dbc5e958bb084f3811ec8a3fb3`; Git bundle verification passes. Head `f0e626263ef48e60e39e162daf418616162c3e2e`, named branch `b14-02-source13`, prerequisite base `9898e56941a7665f231873481dae956f08509995`.
- Frozen source and P13 contents match the base and match between B14-01 and B14-02. All source row/rung/transport metadata are checked, including climbing the two degree-12 rows to 13 rather than using source.json's degree-24 literal field.
- Recomputed quartic coefficient products, factorial symbols, u-values and per-point maximum symbols for all 96 primary points.
- Independently reconstructed all **3,744 integers** from the seven saved residue blocks, checked all **26,208 residue equalities**, and checked the global and per-point signed uniqueness bounds. The 217-bit modulus exceeds twice the independently justified 185-bit value bound.
- Recomputed the exact **3,770-bit** determinant of the source 36-minor using integer Bareiss elimination, all 288 scalar identities in A^T K=0, and a nonzero 3-minor of K.
- Recomputed the source's generic independence on banked S74 data at both primes, with explicit 39-minor witnesses and independent transport.
- Recomputed both original 72-minors and both new 73-minors with a standard-library elimination implementation.
- Freshly evaluated the newly completing source row at P13-000 with the Python set-state DP, without the native C core or flint. A single modulus greater than 2H permits exact signed recovery. It gives **-5131733063598099268592803340746752**, agreeing with A[15,0], in about 47 seconds.
- The preceding B14-01 review freshly replayed four mixed-target entries through Python and replayed the independent 73-dimensional character count.

**Verification scope:** all delivered source arithmetic and the new joint rank certificate were replayed. The full native evaluation sweeps were not regenerated. Polynomial-value correctness relies on the inspected evaluators, their delivered independent controls and exact-entry checks, the fresh checks above, and the banked source certificates. This is a computational mathematical certificate and proof, not a new accepted kind in the repository's general checker and not a proof-assistant formalization.

One report qualification: B14-02's full generic rank is a strong independence control, but it does not by itself “exonerate” every possible convention or evaluator error. An incorrect invertible transformation can preserve generic rank. The explicit coefficient, transport, exact-entry and point-contract checks are what address that risk.

## Replay and handoff

`joint_verify.py check` replays the delivered arithmetic and writes the joint certificate, completed target matrices and exact relation definitions. `joint_verify.py source_entry` separately replays the fresh completing-member evaluation. The local layout is this project's `work/reviews/b14-01`, `work/reviews/b14-02`, and `Batch14_Results/B14-01_review/review_checks.py`; the latter supplies shared review helpers. The arithmetic check takes about a second on this host. The optional source-entry replay was bounded at 240 seconds.

The mathematical dependency chain is: frozen polynomial definitions and source basis -> B14-04 dimension 73 -> 72 mixed members plus the source pullback -> full target minor -> B14-02 exact source kernel -> three equations -> injective first-row transport and Pad subset Red -> D in [-4,-2].

Recommended integration work: teach B14-03's target-member representation to accept a certified quartic-source pullback as well as a single mixed bracket, replay this certificate in the general checker, and index the new exact equations and LMR exclusion. These registration tasks remain separate from the completed mathematical deduction.

For degree 14, seed target construction with available source pullbacks and augment them with mixed target members. There is no mathematical requirement that every basis member be discovered by the same random filling search. The 159-dimensional target and degree-14 source still need their own certificates before concluding D=-4.
