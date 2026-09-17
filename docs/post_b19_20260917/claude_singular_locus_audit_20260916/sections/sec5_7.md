
## 5. Answers to the seven required items

1. **Primary statements read.** EH Theorems 1.1, 1.2, Corollaries 1.3, 1.4 and the
   definitions, transcribed verbatim from the scanned primary text (section 1.1, pages
   135-141, PDF SHA-256 `6b10d8fe...`). HL arXiv:2306.14428v1 sections 1, 4.1, 4.2 read for
   the Atkinson restatement and the competing definition of "primitive". Atkinson 1983 and
   Ballico's addendum (Beitraege Algebra Geom. 36 (1995) 119-122, "...and vector bundles on
   projective spaces") were **not** read: the EUDML record carries no abstract and zbMATH
   refused the fetch. Ballico's title points at the bundle-theoretic part (EH sections 2
   and 4); no correction to the rank `<= 3` statements of EH section 1 is known to this
   session, and Atkinson's independent proof (cited by EH p. 136 and restated by HL) covers
   the same statements. This residual dependence is recorded in the ledger (C3).
2. **Definitions** kept distinct in section 2: EH-primitive (projection form (7)) versus
   HL/Atkinson-Lloyd-primitive (hyperplane form); compression (equality) versus
   sub-compression; shrunk subspace; `G`-semistability; `GL5 x G` weight vanishing.
3. **Generic ranks.** Rank `<= 2` (either side): Lemma 3.2(c) via Corollary 1.4, unstable.
   Rank 3 degenerate: Lemma 3.2(b), unstable. Rank 3 compression: Lemma 3.2(a), unstable.
   Rank 3 primitive: dimension 4 (Theorem 1.2), so a five-tuple in it is dependent.
   Rank 3 with skew primitive part: shape (S) or its transpose (Lemma 3.3), semistable
   possible, and handled by Theorem 4.1. Transposes appear in Lemma 3.3 and in the last
   line of the proof of Theorem 4.1.
4. **The linear-kernel argument.** Surjective `kappa`: the note's proof stands
   (`dim X <= 4`). Non-surjective `kappa`: the conclusion `dim X <= 4` is **false** (`Mt`,
   `dim 7`, `kappa` linear with 3-dimensional image). Non-linear kernel map: realised by
   `Mt^T`. So Claim 4.2.3 cannot be completed as a dimension bound; the route is closed
   instead by Theorem 4.1, whose mechanism is a `GL5 x G` one-parameter subgroup, not a
   dimension count.
5. **Semistable independent five-tuple in `Z` under `G = SL4 x SL4`: YES.**
   `X_0 = skew_3 + <E_14> + <E_44>` with the basis of section 3 is independent, identically
   singular, and `G`-semistable (check 1: degree-8 blow-up determinant `-1044`). But under
   the group that matters for five-row functions the answer is **no**: for every
   5-dimensional singular `G`-semistable `X` the tensor is `SL5 x G`-unstable (Remark 4.1(i)),
   and every five-row isotypic component vanishes on it (Theorem 4.1). The earlier "no
   compression subspace" paraphrase conflated the two questions.
6. **Not applicable as an inference; recorded as a negative.** Because such spaces exist,
   the certification protocol was executed rather than assumed: check 2 evaluated the two
   certified full-`H` vectors `q_3, q_7` of `M_(4^5)` (descent follow-up session, ledger E5)
   at four `GL5`-mixes of `X_0` after two controls that can fail (the stored `K5` values are
   reproduced; a dependent tuple gives zero). All eight values are zero, exactly as
   Theorem 4.1 predicts; they are **not** used as evidence, the theorem is. Had a nonzero
   residue appeared, it would have refuted Theorem 4.1 (a nonzero residue mod `P` is a
   nonzero integer).
7. **Complete deduction that `Z` is invisible to all five-row functions:** Theorem 4.1 with
   Lemmas 3.1-3.3, citing EH Theorem 1.1 (p. 140), Theorem 1.2 (p. 140), Corollary 1.3
   (p. 141), Corollary 1.4 (p. 141), the rank formula (p. 139) and the nondegeneracy
   convention (p. 137).

## 6. Bounded checks (two, both through the inspected Job Object wrapper)

Wrapper: `work/batch15_workers/B15-02/analysis/b15_bound.py` (60 s, 512 MiB, one worker,
one BLAS thread, `job_object_enforced: true` in both receipts under `checks/results/logs/`).
Both checks were prepriced from the descent follow-up receipts (0.34 s per column tensor,
0.55 s per vector evaluation).

| check | script / certificate | content | wall | outcome |
|---|---|---|---|---|
| 1 | `checks/check1_counterexample.py` -> `.json` | `det(sum x_i B_i)` for `X_0` expands to `0` (sympy, exact); the five matrices are independent (rank 5); 2x2 blow-up with fixed integer `M_k` (seed 20260917) has determinant `-1044`; generic rank 3; generic kernel `(c/a, -b/a, 1, 0)` | 1.16 s | PASSED: `X_0` in `Z`, independent, `G`-semistable |
| 2 | `checks/check2_restriction_to_Z.py` -> `.json` | `q_3, q_7` (p6_basis.json plans, p7 hand orders, `P = 524287`) at four `GL5(Z)`-mixes of `X_0` (mix determinants `-246, 57, -54, 150`) | 5.97 s | all values `0`; controls passed (`K5` values `94237, 491460` reproduced; dependent tuple `0, 0`) - INCONCLUSIVE as evidence, CONSISTENT with Theorem 4.1 |

Two aborted starts of check 2 (0.75 s and 0.31 s, no computation reached) were caused by
this session's own script errors (list-versus-tuple plan labels; a wrong assertion about
which basis file p7 used - it used `p6_basis.json`). They are not retries of a failed
bounded computation. Total measured wall time including them: about 8.2 s.

## 7. Claim ledger, negatives, and the next lemma

| id | claim | status | where |
|---|---|---|---|
| C1 | EH Thms 1.1, 1.2, Cors 1.3, 1.4 as transcribed | READ FROM PRIMARY SCAN (proofs not re-verified) | section 1.1 |
| C2 | HL's "primitive" differs from EH's | VERIFIED from both texts | sections 1.2, 2 |
| C3 | No later correction alters EH section 1 | NOT VERIFIED (Ballico addendum not read; title indicates bundle scope; Atkinson independent proof) | section 5.1 |
| C4 | Shrunk implies `G`-unstable; compression/degenerate/rank `<= 2` are shrunk | PROVED (Lemmas 3.1, 3.2; 3.2(c) uses Cor 1.4) | section 3 |
| C5 | `G`-semistable singular `X` is (P) dim 4 or (S) inside `Mt` | PROVED from C1 | Lemma 3.3 |
| C6 | H-EH is false; `Mt`, `X_0` are `G`-semistable singular of dim 7, 5 | PROVED and CERTIFIED (check 1) | section 3, check 1 |
| C7 | Note's Claim 4.2.3, non-surjective case | REFUTED as a dimension bound | section 3 |
| C8 | Every five-row isotypic component vanishes on `Z` (`rho_Z = 0`) | PROVED (Theorem 4.1), conditional only on C1 | section 4 |
| C9 | Same for `>= 5` rows in any `m`-variable model | PROVED (Remark 4.1(ii)) | section 4 |
| C10 | `q_3, q_7` vanish at four points of `X_0` | MEASURED (mod `P`), explained by C8 | check 2 |
| C11 | Four-row cells can see `Z` | NOT CLAIMED either way; outside scope | Remark 4.1(iii) |

**Honest negatives.** (a) The proofs in EH section 3 were not replayed; the closure rests on
the published statements. (b) The Ballico addendum was not read. (c) No `rho_Z`, no
`m_det`, no `m_pad`, no `r`, no gap: the outcome is purely a closure. (d) Check 2's zeros
are consistent with, not evidence for, Theorem 4.1.

**Decision.** *Rigorous closure theorem for this route.* The identically singular locus
`Z` was excluded for the **wrong reason** in the B15-12 note (H-EH is false, and the
linear-kernel argument cannot be completed), but the **exclusion itself is correct**:
Theorem 4.1 shows every five-row full-`H` function vanishes on `Z`, so `Z` can never
supply a five-row determinant constraint, in five or more variables. Nothing on `Z` can be
"certified nonzero in a named full-`H` cell" with five rows; the route is closed, not
reopened.

**Exact next missing lemma (the only residual).** *Independence from later literature:*
confirm that Ballico (1995) and any addendum to Atkinson (1983) leave EH Theorems 1.1-1.2
and Corollaries 1.3-1.4 unchanged for `4 x 4` matrices. Inputs: those two texts. Expected
output: one sentence each, with page references. Falsification: a corrected list of
rank-3 primitive or imprimitive `4 x 4` spaces containing a `G`-semistable 5-dimensional
member with no column-only (or row-only) element, which would break Case 3 of
Theorem 4.1. Independently of the literature, a self-contained proof of Lemma 3.3 for
`4 x 4` matrices (rank-3 spaces with no shrunk subspace are contained in `Mt` or `Mt^T`)
would remove C1 and C3 from the dependency list entirely; it is a finite linear-algebra
statement and is the natural target if the closure is to be made literature-free.

Status: **COMPLETE - closure theorem delivered; H-EH refuted; exclusion of `Z` upheld by a
different proof; one residual literature dependence recorded.**
