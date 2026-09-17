# GKZ-style discriminants, resultants and complexes as a source of determinant coefficient equations: one construction assessed

Claude session, 17 September 2026. Fresh directory `work/claude_gkz_incidence_20260917/` (did not exist before this session). Historical files, other sessions' outputs and shared ledgers are read-only. No agent launched; no dependency, sandbox, Git-trust or ownership change; no commit, push or publication. Written incrementally: sections 0-5 and the pilot plan in 6.1 were written before any computation was dispatched; the status line below was replaced after the pilots ran and before hashing.

Status: **COMPLETE - Outcome C (rigorous negative), with Theorems A and B certified.** Three wrapped pilots ran (5.45 s, 4.00 s, 0.51 s; peak Job Object memory 236 MB, 93 MB, 76 MB; all exit 0), 9.96 s of the 180 s budget. Every certificate the proofs of section 3 call for was produced and passed (section 6.2). One exploratory hypothesis in P1 (that the second Koszul differential has full row rank at `det_4` in degree 7) was recorded as `false` in P1's JSON; that is a finding, not a failed certificate, and P3 settled it exactly (rank 1904 of 1920). No positive gap is claimed; no cell is nominated. This line replaced the IN PROGRESS marker after section 8 was written and before hashing.

Labels: **PROVED** (argument written here), **ADOPTED** (accepted programme result or named literature theorem, cited with the exact statement used), **VERIFIED-SOURCE** (primary source fetched and the statement read), **CERTIFIED** (exact integer computation in this session, receipt attached), **MEASURED** (modular or sampled numerical statement), **NOT ASSESSED**.

## 0. Verdict in plain terms

**Outcome C, with one rigorous extension of an existing negative.** Read against the actual question, the GKZ toolbox contains exactly three things that act on a single quartic's coefficients, and none of them produces a determinant equation that is both new to the programme and nonzero on padding:

1. **Projective duality / the discriminant of the hypersurface `X_F = {F = 0}`** (Segal section 2.1). Applied to the Veronese this is the ordinary discriminant, which vanishes on `ell * C` products for the elementary reason in the brief. Applied to `X_F` itself it is the dual variety `X_F^vee`, whose dimension is read off the Hessian rank on `X_F`; the resulting equations are the Landsberg-Manivel-Ressayre / Mignon-Ressayre Hessian-rank (dual-degeneracy) family, already fully worked out in the programme's equation census (`equation_census.md` sections 2.2-2.6: `rank Hess = 8` on determinantal hypersurfaces, `9` on the `per_3` component of every padded form, one separating member at `k = 6`, degree 24). **Known; repackaged, not new.**

2. **The Cayley method** (Segal section 3.1): resultants and discriminants as determinants of Koszul complexes pushed down to coefficient space. The discriminant is the determinant of the Koszul complex of the five (or sixteen) partials; every other equation this complex yields is a Fitting ideal of one of its differentials in a fixed degree `k`. For the first differential these are exactly the Macaulay-matrix minors, i.e. the programme's Jacobian-cap family (`onset_conjecture.md` Theorem 1: degree 300 at `n = 4`, five variables). This is the one GKZ construction that produces determinant-specific information beyond "singular" (it reads the defect of the twenty nodes). It is the construction selected and assessed in section 3. **Result: rigorously blind to padding in every degree.** Theorem B (five variables) removes the measured dependency of the record's Proposition D (`excess_singularity.md`) at `r = 5`, using only Kleiman transversality plus one exact rank certificate; Theorem A (sixteen variables, the full `GL_16` ambient, every partition length) is new: for every Macaulay degree `k`, `rank M_k(z * per_3) <= rank M_k(det_4)`, so every Macaulay minor vanishing on the determinant orbit closure vanishes on the padded-permanent orbit closure. Its contribution to `D = m_pad - m_det` is zero in every cell.

3. **Toric degenerations, secondary fans and principal `A`-determinants** (Segal sections 1.2, 2.2, 2.4). Applied to the monomial support of `det_4` (the 24 permutation matrices, Newton polytope the Birkhoff polytope `B_4`) these organise the torus-orbit closure of `det_4` and its face degenerations. Everything here is a statement about coefficient scalings of a fixed sparse family or about a toric boundary chosen by coordinates; the only `GL_16`-compatible content is lower bounds `m_det >= m_{in_Gamma(det_4)}` from face degenerations, which run against a gap. The sign sensitivity that the brief asks for (`det` versus `per` on the same support) does enter here, but only as a coordinate-dependent torus statement. **Rejected by the early tests of section 4** (toric boundary condition mistaken for a `GL`-invariant one; the padded permanent is not even in the family).

No positive multiplicity gap is claimed; no cell is nominated. The recommendation (section 8) is to stop the GKZ route as a source of equations. The second Koszul differential was also checked exactly in sixteen variables (section 6.2, pilot P3): in degree 7 it does yield determinant equations (rank 1904 of 1920 at `det_4`), and they are blind too (rank 1650 at `z per_3`). The higher differentials and higher degrees remain NOT ASSESSED; closing them is priced in section 8 but not recommended.

## 1. Provenance, scope and input pins

Workspace `C:/Users/swami/Projects/gct-gpt`; original project `C:/Users/swami/Projects/gct` read-only. No git command was run. Process state at start: `tasklist` showed no `python`, CAS or worker process. No `AGENTS.md` exists at depth <= 5 in either tree (`find` at session start); the delivery conventions followed are those of the sealed sibling sessions (`work/claude_image_ceiling_20260916`, `work/claude_source_vectors_20260917/*`): fresh directory, incremental report, Job Object wrapper, receipts preserved, `MANIFEST.json` sealed last. SHA-256 pins of every input listed here are in `MANIFEST.json`.

Literature (kept in the session scratchpad, outside the delivery tree; hash and size recorded):

- E. Segal, *A short guide to GKZ*, arXiv:2412.14748v1 (19 Dec 2024), fetched from `https://arxiv.org/pdf/2412.14748`, 579,885 bytes, SHA-256 `8c8d9d058c878e77c953928c63d9d8fc9db184c46e6f94bf4d5a66f9eb31afc1`; text extracted with `pdftotext`. Read in full. Statements used: section 1.2 (definition of `Delta_A`, Example 1.7, the principal `A`-determinant (1.8), Theorem 1.9 = [GKZ p302]); section 2.1 (`Delta_A` is the equation of the dual of `V_A`; Remark 2.6); section 2.2 (extreme toric degenerations, Claim 2.13); section 2.3 (associated hypersurface, `V`-resultant, Chow form, Examples 2.15-2.16); section 2.4 (Cayley trick with logarithmic derivatives, `E_A` as the resultant of `f_A` and its logarithmic derivatives, Example 2.28); section 3.1 (Cayley method: Koszul complex of the tautological section, push-down, `det D = R`, "determinant of a complex" [GKZ Appendix A]).
- A. Dimca, *Syzygies of Jacobian ideals and defects of linear systems*, arXiv:1210.1795v4 (24 Dec 2012), fetched from `https://arxiv.org/pdf/1210.1795`, SHA-256 `20b96f5830291574137000073237b9081e134e45d52c89d9981996e5a83c9c05`. **VERIFIED-SOURCE**: Theorem 3.1 read on p. 6 of the extracted text: for `D : f = 0` of degree `d` in `P^n` with only isolated singularities, `dim M(f)_{T-k} = dim M(f_s)_k + def_k Sigma_f` for `0 <= k <= nd - 2n - 1`, `T = (n+1)(d-2)`, and `dim H^n(K(f))_j = tau(D)` for `j >= n(d-1)`. Both clauses are used below (the second is what the onset note did not quote).
- Gulliksen-Negard resolution and Kleiman transversality: **ADOPTED** exactly as in `onset_conjecture.md` section 2 (not re-fetched; the statements used are reproduced where used).

Programme documents read (relevant sections only):

- Original project: `work/docs/onset_conjecture.md` (sections 0-3: the cap theorem at every `n`, its four steps and labels, the `n = 4` numbers); `work/docs/paper1_delta0_patch.md` (Proposition `prop:jaccap`); `work/docs/PROVED.md` (ledger, `washout_thm2`); `work/paper/det4-onset.tex` (lines 160-190, 520-560: Theorem `thm:cap`, identical mechanism); `work/paper/det3-conductor.tex` (not needed beyond what the image-ceiling report already extracted; not re-read).
- Recent project: `work/batch15_workers/B15-01/docs/b18_01_report.md` (sections 0-2, `dim D45 = 50`, `R135`, the withdrawn `MN = F I_4`); `work/batch15_workers/B15-05/docs/b18_05_report.md` (Hessian-divisibility identity, `Psi = 0` on the whole product family); `work/batch15_workers/B15-10/docs/b18_10_review.md` (section 4.4: `MN = F I_4` REJECTED with the witness `M = l I_4`, `N = C I_4`); `work/claude_image_ceiling_20260916/REPORT.md` (1+3 barrier, `u_L = m_pad` below `delta_0`, the `65 / 80 / 300` record); `work/claude_singular_locus_audit_20260916/REPORT.md` (sections 0-1 only; not load-bearing here).
- Located while checking novelty: `work/batch15_workers/B15-01/docs/equation_census.md` (sections 2.2-2.6, row 12), `work/batch15_workers/B15-01/docs/excess_singularity.md` (Proposition D and its proved-vs-measured note), `work/batch15_workers/B15-01/docs/s49_s55_batch_review.md` (section 2, the two-family table), `work/batch15_workers/B15-04/docs/b17_04_report.md` (header, the eleven-equation space).
- Context only, not relied on: `work/claude_transverse_structure_20260916_followup/clarification_20260917/SOURCE_HANDOFF.md`, `work/claude_source_vectors_20260917/routeA_signfilter_20260917/REPORT.md`, `work/claude_source_vectors_20260917/arc_target_dimension_followup/REPORT.md` (verdict sections). Nothing of the independent arc session was modified, reproduced or used.

Wrapper: `work/batch15_workers/B15-02/analysis/b15_bound.py` (SHA-256 `ca001081f49e0048812b871a31e3be85435b210b3a538170a9f006408a41f854`, inspected: Windows Job Object with process and job memory caps, kill-on-close, wall timer with exit 124, BLAS/OMP threads pinned to 1, receipts in `results/logs/<name>_resources.json`). Interpreter: `work/batch15_workers/B15-02/.venv/python.exe` (Python 3.12.10, numpy 2.4.6, sympy 1.14.0, python-flint 0.9.0). One job at a time, at most three wrapped pilots, 60 s / 512 MiB each, 180 s total.

## 2. Mapping GKZ to the actual question (Part 1)

### 2.1 What the survey establishes, and what it does not

Notation for the rest of the report. `N in {5, 16}`, `V = C^N`, `S = C[x_1..x_N]`, quartics `F in S_4`. `J_F = (d_1 F, ..., d_N F)`. For `k >= 3` the **Macaulay matrix** `M_k(F)` has rows `(i, m)`, `m` a monomial of degree `k - 3`, columns the monomials of degree `k`, entry the coefficient of the column monomial in `m d_i F`; its entries are linear in `F`, its row space is `(J_F)_k`, and

    r_k(F) := rank M_k(F) = dim (J_F)_k,       c_k(F) := dim (S/J_F)_k = dim S_k - r_k(F).

For a `GL_N`-stable irreducible closed cone `Y subset S_4`, `r_k(Y) := max_{F in Y} r_k(F)`, attained on a dense open subset of `Y` (rank is lower semicontinuous); on an orbit closure `r_k` is the value at the orbit representative, since `(J_{F o g})_k = g . (J_F)_k`. `Y_det = closure(GL_N . det_4)` (for `N = 5`: `D45`, the closure of the five-variable pencil image, `dim 50`, ADOPTED B18-01), `Y_pad = closure(GL_N . z per_3)` (for `N = 5`: `P5 = R135 = { ell C }`, `dim 39`, ADOPTED B17-01/B18-01).

The GKZ objects, as the survey presents them, and where they act:

| GKZ object (Segal) | acts on | output | GL-equivariant in `F`? |
|---|---|---|---|
| `A`-discriminant `Delta_A` (1.2, 2.1) = equation of `V_A^vee` | coefficient vector of a Laurent polynomial with support `A` | one polynomial on `C^A` | only if `A` is `GL`-stable: `A = all quartic monomials` gives the classical discriminant `Delta_405` (`N = 5`), `Delta_{4 . 3^15}` (`N = 16`) |
| principal `A`-determinant `E_A` (1.8, 2.4) = product of face discriminants | same | one polynomial on `C^A` | no: faces of `conv(A)` are coordinate faces |
| `V`-resultant / Chow form `R_V` (2.3) | a linear subspace (matrix `M`, or Plucker coordinates) | one polynomial on a Grassmannian | yes for `V = X_F` or `V = Sing X_F`, but the variable is the subspace, not `F`; coefficients in `F` are recovered only by expanding in the subspace variables |
| Cayley method (3.1): determinant of the pushed-down Koszul complex | coefficients of `d + 1` forms; for discriminants, `f` and its (logarithmic) derivatives | resultant `R` (or a power) as `det` of a complex; and, in every other degree, the Fitting ideals of the differentials | yes: the Koszul complex of the partials of `F` is `GL_N`-equivariant |
| extreme toric degenerations, secondary polytope (2.2, 3.2) | the torus orbit of a point of `P^{|A|-1}` | combinatorial: triangulations, extremal terms of `E_A` | no: torus-boundary structure |

Two remarks the survey makes that matter here. (i) Remark 2.6: `Delta_A` only sees tangency at points of the big torus of `V_A`; the face factors of `E_A` are what the torus boundary contributes (Example 1.7, Example 2.28). (ii) Section 2.4: to get a discriminant from a resultant one must specialise the resultant's variables non-equivariantly for the torus, and the Cayley trick with logarithmic derivatives is what keeps the toric structure. Neither remark involves the general linear group; GKZ's symmetry is the torus.

**The one identification that carries the rest of this report (PROVED, definition-level).** The Cayley method applied to the discriminant of quartics in `N` variables takes the Koszul complex `K(F)` of the `N` partials `d_i F` (forms of degree 3) on `P^{N-1}`, `K_j = Lambda^j (S(-3)^N)`, with differential `d_j(e_{i_1} ^ ... ^ e_{i_j}) = sum (-1)^{a} d_{i_a}F . (omit e_{i_a})`, and pushes it down degree by degree: `K_j` in internal degree `k` is `Lambda^j C^N (x) S_{k - 3j}`, and the differentials are matrices whose entries are linear in `F`. The determinant of this complex in a suitable degree is (a power of) the resultant of the partials, i.e. (a power of, up to a constant) the discriminant, by Euler's identity `4F = sum x_i d_i F` (Segal Remark 1.5 with Example 2.23's specialisation; the exact power and constant are not needed below and are not claimed). **The degree-`k` graded piece of the first differential `d_1 : K_1 -> K_0` is the Macaulay matrix `M_k(F)`.** Every Fitting ideal of a differential of `K(F)` in a fixed internal degree is a `GL_N`-stable space of polynomials in the coefficients of `F`, and the Fitting ideals of `d_1` are the spaces spanned by the minors of `M_k(F)` of a given size. So the Cayley method's non-determinantal output, restricted to `d_1`, is precisely the programme's Macaulay-minor family (`onset_conjecture.md`, `sixrow_cap.md`, census row 12).

### 2.2 Candidate 1: a resultant / Chow form for a determinant-specific incidence configuration

- *Geometric object.* Either the dual variety `X_F^vee` (the discriminant of the linear system `|O_{X_F}(1)|`, Segal 2.1 with `V = X_F`), or the Chow form of the singular scheme `Sing X_F` (Segal 2.3 with `V = Sing X_F`), or the restricted discriminants `Delta(F o A)`, `A` an `N x r` matrix (the Chow-form-type expression of "every `r`-plane section is singular").
- *Parameter space.* `F in S_4` together with a hyperplane (dual variable), a `P^{r-1}` (Plucker/Stiefel variable), or an `N x r` matrix `A`.
- *Expected coefficient-level output.* For `X_F^vee`: the conditions `dim X_F^vee <= k`, i.e. "`F` divides every `(k+3)`-minor of `Hess F`" (`dim X^vee = rank Hess - 2` at a general point of `X`, `equation_census.md` section 9, PROVED there). For `Sing X_F`: the coefficients, as polynomials in `A`, of `Delta_{4 . 3^{r-1}}(F o A)`; their common vanishing says `dim Sing X_F >= N - r`. For the Chow form proper: the coefficients of the Chow form of `Sing X_F` are regular functions on the locus where `Sing X_F` has the expected dimension and degree, not polynomials on `S_4`.
- *Why it might distinguish determinant from product structure.* `dim X_{det_4}^vee = 6` (Gauss image is the rank-one Segre), while the `per_3` component of `X_{z per_3}` has dual of dimension `7` (`rank Hess(per_3) = 9` at a general point of `{per_3 = 0}`, census 2.2, MEASURED there, 40 of 40 clean draws; and `rank Hess(z q) <= 9` on `{q = 0}` for every padded form, PROVED census 2.4). Dual degeneracy runs the right way.
- *First obstruction.* This is the LMR / Mignon-Ressayre construction, present in the programme since sessions 49-55 with its degree (24 at `k = 6`), its unique separating member and its floor (`equation_census.md` 2.3-2.6). The `Sing`-dimension version runs the wrong way (`dim Sing = 11` for `det_4`, `13` for `z per_3`), so its equations are padding equations. The Chow form of `Sing X_F` is not polynomial in `F`. **Nothing here is new to the programme.**

### 2.3 Candidate 2: a complex whose failure of exactness / rank drop yields coefficient equations

- *Geometric object.* The Koszul complex `K(F)` of the partials on `P^{N-1}` (the Cayley method's complex for the discriminant), pushed down to coefficient space degree by degree.
- *Parameter space.* `F in S_4` alone. No auxiliary parameter survives the push-down: the internal degree `k` is a discrete index.
- *Expected coefficient-level output.* For each `k` and each differential `d_j`, the ideal of `(rho + 1)`-minors where `rho` is the rank of `d_j` in degree `k` on the determinant orbit closure. For `d_1` this is the Macaulay family: at `N = 5, k = 7` the size-300 minors (cap), at `N = 16, k = 4` the size-227 minors of the `256 x 3876` matrix `M_4(F)` (the condition "`F` has at least 30 independent linear syzygies among its partials", i.e. "`dim Lie(Stab F) >= 30`").
- *Why it might distinguish determinant from product structure.* At `N = 5` the rank drop at `k = 7` reads the defect of the twenty nodes (Dimca), a property of the Gulliksen-Negard node configuration, not of "being singular". At `N = 16` the drop at `k = 4` reads the stabiliser dimension.
- *First obstruction.* Products and padded forms have a larger singular locus (codimension 2 against 4), so their Milnor algebra is larger in every degree where the determinant's is larger than the smooth one; the mechanism then reads padding as "more determinantal than the determinant". This is the record's Proposition D at `r <= 6`, proved there given measured determinantal coranks. Whether the obstruction is total (all `k`, all `N`, all differentials) is the question this report settles for `d_1` (section 3).

### 2.4 Candidate 3: a toric / secondary-fan organisation of a restricted family of degenerations

- *Geometric object.* `A = { permutation matrices } subset Z^16`, `|A| = 24`, `conv(A) = B_4` (Birkhoff polytope, dimension 9); the sparse family `f_a = sum_sigma a_sigma x^sigma`, `a in C^24`; `det_4 = f_{sgn}`, `per_4 = f_1`. The torus `T^16 subset GL_16` acts on `S_4` by scaling monomials; `closure(T . det_4) subset closure(GL_16 . det_4)` is the toric variety `V_A` translated by the sign vector, and its boundary points are the initial forms `in_Gamma(det_4) = sum_{sigma in Gamma} sgn(sigma) x^sigma`, `Gamma` a face of `B_4`.
- *Parameter space.* `C^24` (coefficient scalings), or the secondary fan of `A` (coherent triangulations of `B_4`).
- *Expected coefficient-level output.* `E_A(a) = prod_Gamma Delta_{A cap Gamma}(a_Gamma)^{m_Gamma}`; evaluated at `a = sgn` and `a = 1` it compares torus-singularity of `det_4`, `per_4` and their face restrictions. This is the only place in the GKZ toolbox where coefficient *signs* on a common support enter, as the brief requires.
- *Why it might distinguish.* `Delta_A(sgn) = 0` (rank-two matrices with all entries nonzero exist), while for `per_3` the analogous `Delta_{A_3}(1) != 0` (no `3 x 3` matrix with all entries nonzero has all nine `2 x 2` permanental cofactors zero: two rows `(a_j)`, `(b_j)` with `a_j b_l = -a_l b_j` for all `j != l` force a zero entry when there are three columns). So `det` and `per` are separated by a sign-sensitive, support-independent statement.
- *First obstruction.* It is a statement about the point `a` in the sparse family, not about the `GL`-orbit: "singular at a point of the torus" is coordinate-dependent, and the padded permanent `z per_3` has a different support (`B_3 x point`) so is not in the family at all. The `GL_16`-compatible content reduces to `closure(GL . in_Gamma(det_4)) subset Y_det`, giving lower bounds `m_det(lambda, d) >= m_{in_Gamma}(lambda, d)` for every face; these can only kill cells, never open them. **Rejected** (section 4).

### 2.5 Selection

Candidate 2, restricted to the first differential. It is the only candidate that (a) acts on `F` alone with no auxiliary variable to eliminate, (b) is `GL_N`-equivariant by construction, (c) has already produced a determinant equation that reads more than singularity (the cap), and (d) admits a complete answer with the tools at hand. Candidate 1 is a repackaging of LMR; candidate 3 fails the invariance test. The theorem target for candidate 2 is stated in 3.B: **for every degree `k`, `r_k(Y_pad) <= r_k(Y_det)`, in `N = 5` and in `N = 16`**; if true, every Macaulay-minor determinant equation vanishes on padding and the route is closed; if false at some `k`, the size-`(r_k(Y_det)+1)` minors of `M_k` are determinant equations nonzero on padding.

## 3. The selected construction (Part 2)

### 3.A Explicit complex and matrix

`K(F)`: `0 -> Lambda^N E -> ... -> Lambda^2 E -> E -> S`, `E = S(-3)^N` with basis `e_1..e_N`, `d(e_i) = d_i F`, graded by internal degree. In internal degree `k`:

    (K_1)_k = C^N (x) S_{k-3}  --M_k(F)-->  (K_0)_k = S_k,
    (K_2)_k = Lambda^2 C^N (x) S_{k-6}  --D_k(F)-->  (K_1)_k,   D_k(e_i ^ e_j (x) m) = m d_i F e_j - m d_j F e_i.

Variables: the coefficients `c_alpha` of `F` (70 for `N = 5`, 3876 for `N = 16`). Auxiliary parameters: none. Setting: affine cone over `P(S_4)`; all constructions are `GL_N`-equivariant maps of the `GL_N`-modules `S_4 -> Hom(C^N (x) S_{k-3}, S_k)`, linear in `F`. Closed loci: for each `k` and `rho`, `Z_{k, rho} := { F : rank M_k(F) <= rho }`, closed (minors), `GL_N`-stable, a cone. The Macaulay-minor equations of `Y_det` in degree `k` are `I_{k}(Y_det) := ideal of (r_k(Y_det) + 1)-minors of M_k`, which is `GL_N`-stable and lies in `I(Y_det)`.

### 3.B Determinant-side theorem (PROVED)

**Lemma 3.1.** `I_k(Y_det) subset I(Y_det)` for every `k`; and for `Y = closure(GL_N . F_0)` one has `r_k(Y) = r_k(F_0)`.
*Proof.* `M_k(F o g)` is the matrix of the map `(e_i (x) m) -> m d_i(F o g)`, and `d_i(F o g) = sum_j g_{ji} (d_j F) o g`, so its row space is `g . (J_F)_k`, of the same dimension: `r_k` is constant on the orbit, hence equal to `r_k(F_0)` on the dense orbit, and `<= r_k(F_0)` on the closure by lower semicontinuity of rank. A minor of size `r_k(F_0) + 1` therefore vanishes on the closure. No choice of matrix representation enters: the construction is a function of `F` only, and the passage from the pencil image to `D45` is the closedness of `Z_{k,rho}`. QED

**Lemma 3.2 (blindness criterion).** If `r_k(Y_pad) <= r_k(Y_det)` then `I_k(Y_det) subset I(Y_pad)`. If `r_k(Y_pad) > r_k(Y_det)` then some element of `I_k(Y_det)` is nonzero on `Y_pad`. *Proof.* Immediate from Lemma 3.1 applied to `Y_pad`. QED

**Theorem A (sixteen variables, the full ambient; PROVED given Gulliksen-Negard (ADOPTED) and the CERTIFIED exact values of section 6.2).** For every `k >= 0`, `r_k(z per_3) <= r_k(det_4)` in `S = C[x_1..x_16]`. Consequently every minor of every Macaulay matrix `M_k` that vanishes on `closure(GL_16 . det_4)` vanishes on `closure(GL_16 . z per_3)`, in every degree and every `GL_16`-type, i.e. in every cell `(d, lambda)` of every length.

*Proof.* Coordinates: `x = (z, y_11..y_33, w_1..w_6)`, `F_pad = z per_3(y)`, `F_det = det_4(x)` in the same sixteen variables. Write `p(m) = C(m+15, 15)` (`= 0` for `m < 0`) for `dim S_m`, `c(m) = C(m+6, 6)` for `dim C[z, w]_m`.

*Determinant side.* `J_{det_4}` is the ideal of `3 x 3` minors of the generic `4 x 4` matrix (the partials of `det_4` are the signed cofactors). ADOPTED (Gulliksen-Negard 1972; Bruns-Vetter, *Determinantal rings*; as quoted in `onset_conjecture.md` 2.3(c)): the submaximal minors of the generic `n x n` matrix have the resolution `0 -> S(-2n) -> S(-n-1)^{n^2} -> S(-n)^{2n^2-2} -> S(-n+1)^{n^2} -> S`, here `0 -> S(-8) -> S(-5)^16 -> S(-4)^30 -> S(-3)^16 -> S`. Hence, exactly,

    r_k(det_4) = 16 p(k-3) - 30 p(k-4) + 16 p(k-5) - p(k-8).                       (A1)

*Padding side.* `d_z F_pad = per_3`, `d_{y_ij} F_pad = z p_ij` with `p_ij` the nine `2 x 2` permanental cofactors, `d_w F_pad = 0`. So `J_pad = per_3 . S + z P S`, `P subset C[y]` the ideal of the nine `2 x 2` permanents. Laplace expansion gives `per_3 = sum_j y_1j p_1j in P`. Claim: `per_3 S cap z P S = z per_3 S`. If `per_3 g = z h`, `z` prime and `z` not dividing `per_3` force `z | g`, and conversely `z per_3 S subset z P S` since `per_3 in P`. Since `z` is a nonzerodivisor,

    r_k(z per_3) = dim (per_3 S)_k + dim (z P S)_k - dim (z per_3 S)_k = p(k-3) + dim (PS)_{k-1} - p(k-4),      (A2)

and, `S = C[y] (x) C[z,w]` with `PS = P (x) C[z,w]`,

    dim (PS)_m = sum_{j=0}^{m} dim P_j . c(m-j),     dim P_j = C(j+8, 8) - u(j),   u(j) := dim (C[y]/P)_j.     (A3)

*Comparison for `k <= 10`.* Substituting (A1)-(A3), `r_k(z per_3) <= r_k(det_4)` reads

    Q(k) + U(k-1) >= 0,   Q(k) := 15 p(k-3) - 29 p(k-4) + 16 p(k-5) - p(k-8) - p(k-1),   U(m) := sum_{j=0}^{m} u(j) c(m-j).   (A4)

`U(k-1)` involves `u(0..k-1)`. The values `u(0..9)` are computed exactly in pilot P1 (exact integer ranks over `Q` of the multigraded blocks of the spanning set `{ monomial . p_ij }`, python-flint `fmpz_mat.rank`; the `Z^3 x Z^3` row/column multigrading of `P` makes every block small). With those values (A4) is an integer inequality checked for `k = 0..10` in P1. *Written before the run:* the expected values are `u = 1, 9, 36, 89, ...` (`dim P_2 = 9`, `dim P_3 = 81 - 4 = 77` from the four independent linear syzygies of the permanental cofactors, the Lie algebra of the torus stabiliser of `per_3`), giving `r_3 = 10 <= 16`, `r_4 = 155 <= 226` [post-run note: `89` was an arithmetic slip for `165 - 77 = 88`; the checked item was `dim P_3 = 77`, which passed]; if any `k <= 10` fails, Theorem A fails at that `k` and Lemma 3.2 yields a separating equation, which would be reported as such.

*Comparison for `k >= 11`.* `U >= 0`, so it suffices that `Q(k) >= 0`. `Q` is a polynomial in `k` of degree at most 15 for all `k >= 0` (each `p(k-a)` is the polynomial `prod_{i=1}^{15}(k - a + i)/15!`, which vanishes at the integers `k - a + 15 in [0, 14]` exactly where the binomial does, and `k - a + 15 >= 0` for `k >= 0`, `a <= 8`). Its two leading terms cancel (`sum c_a = 0`, `sum c_a a = 0` for the coefficient vector `(c_1, c_3, c_4, c_5, c_8) = (-1, 15, -29, 16, -1)`), and the `k^13` coefficient is `(1/2) sum c_a a^2 = 3 > 0` times that of `p''`, so `Q(k) -> +infinity`. Certificate for all `k >= 11` at once (Newton's forward-difference formula, exact for polynomials): with `e_i := Delta^i Q(11)`, `i = 0..15`, one has `Q(k) = sum_i e_i C(k-11, i)` for every integer `k >= 11`; if every `e_i >= 0` then `Q(k) >= 0` for all `k >= 11`. P1 computes the `e_i` exactly. *Written before the run:* `Q(11) = 7582`, `Q(12) = 392122` by hand (section 6.1); the certificate is expected to pass. If some `e_i < 0`, the fallback is to check `Q(k) >= 0` directly for `k` up to the point where the positive differences dominate; that fallback is also implemented and reported. QED (given the certificates)

**Theorem B (five variables; PROVED given Kleiman transversality (ADOPTED) and the CERTIFIED exact ranks of section 6.2; Dimca's Theorem 3.1 VERIFIED-SOURCE gives the exact profile but is not needed for the inequality at `k >= 7`).** For every `k >= 0`, `r_k(P5) <= r_k(D45)` in `S = C[x_1..x_5]`. Consequently every Macaulay minor vanishing on `D45`, in every degree `k` (in particular the size-300 minors of `M_7`, the cap), vanishes identically on `P5 = { ell C }` and hence on every actual five-variable padding restriction.

*Proof.* Let `h(k) := C(k+3, 3) - C(k, 3)` (Hilbert function of `S/(ell, C)`, a regular sequence when `ell` does not divide `C`) and `mu_k := [t^k](1+t+t^2)^5 = 1, 5, 15, 30, 45, 51, 45, 30, 15, 5, 1` (`k = 0..10`, zero after).

*Padding side (PROVED, the argument of Proposition D).* For `F = ell C`, `d_i F = (d_i ell) C + ell d_i C in (ell, C)`, so `(J_F)_k subset (ell, C)_k` and `r_k(F) <= dim S_k - h(k)`; the generic point of `P5` has `ell` not dividing `C`, so `r_k(P5) <= dim S_k - h(k)`:

    k:          3    4    5    6    7    8    9    10   11
    dim S_k:    35   70   126  210  330  495  715  1001 1365
    h(k):       19   31   46   64   85   109  136  166  199
    pad UB:     16   39   80   146  245  386  579  835  1166

*Determinant side.* (i) `k <= 2`: `r_k = 0` on both. (ii) `k = 3, 4, 5`: the global maximum of `r_k` over all quartics is `rho_k = 5 dim S_{k-3} = 5, 25, 75` (the Koszul syzygies begin in degree 6), and it is attained at an explicit integer pencil `F_0` (exact rank over `Q`, pilot P2, CERTIFIED); by Lemma 3.1, `r_k(D45) >= r_k(F_0) = rho_k >= r_k(P5)`. (Expected: `r_4 = 25` is the statement that a generic quinary determinantal quartic has finite stabiliser, ADOPTED `washout_lemma.md` section 4; `r_5 = 75` is new as a certificate.) (iii) `k >= 6`: ADOPTED (Kleiman, as in `onset_conjecture.md` 2.2): the generic pencil `F` has exactly twenty ordinary double points and no other singularity. Then `V(J_F) subset C^5` is the affine cone over twenty points, of dimension 1, so `height J_F = grade J_F = 4`, and four general `C`-linear combinations `g_1..g_4` of the five partials form a regular sequence (graded prime avoidance over an infinite field; Bruns-Herzog, Cohen-Macaulay rings, Prop. 1.5.12 in the form "an ideal of grade `g` generated by forms of one degree contains a regular sequence of `g` general linear combinations of the generators"). Hence `(J_F)_k supset (g_1..g_4)_k` and

    c_k(D45) = dim (S/J_F)_k <= dim (S/(g))_k = sigma(k) := [t^k] (1-t^3)^4/(1-t)^5 = 1, 5, 15, 31, 50, 66, 76, 80, 81, 81, ...

For `k >= 7`: `sigma(k) <= 81 < 85 <= h(k)`, so `r_k(D45) >= dim S_k - 81 > dim S_k - h(k) >= r_k(P5)`. For `k = 6`: `sigma(6) = 76 > 64`, so use instead Dimca's Theorem 3.1 (VERIFIED-SOURCE) with `n = 4, d = 4, T = 10`: `c_6(F) = mu_4 + def_4(N) = 45 + (20 - H_{S/I_N}(4))`, and twenty distinct points impose at least `min(20, 5) = 5` conditions on quartics, so `c_6(F) <= 60 < 64 <= c_6(P5)`; independently, P2 certifies `r_6(F_0) = 165 = rho_6 = 5 . 35 - 10`, the global maximum, which suffices by itself. QED

**Remark 3.3 (the exact determinantal profile, for the record; ADOPTED/VERIFIED, not needed above).** Dimca's two clauses with the onset note's bookkeeping `c_k(F) = mu_k + dim H^4(K(F))_{k+1}` give, for the generic twenty-nodal pencil, `c_k = mu_k + def_{10-k}(N)` for `3 <= k <= 10` and `c_k = 20` for `k >= 11` (second clause: `dim H^4(K)_j = tau = 20` for `j >= n(d-1) = 12`). With `def_3 = 1`, `def_4 = 0` (MEASURED exact in session 40) and the Gulliksen-Negard lower bounds `def_2 >= 5`, `def_1 = 15`, `def_0 = 19`: `c_k(D45) = 30, 45, 51, 45, 31, >= 20, 20, 20, 20, ...` for `k = 3, 4, ..., 11, ...`, against `c_k(P5) >= 19, 31, 46, 64, 85, 109, 136, 166, 199`. The two profiles cross between `k = 5` and `k = 6` and never cross back. This is the row `r = 5` of Proposition D's table with the measured entries replaced by proved bounds.

### 3.C Nontriviality (PROVED)

The construction is not identically zero: at `N = 5, k = 7` a smooth quartic has `r_7 = 300` while `r_7(D45) = 299` (Theorem 1 of the onset note, ADOPTED), so the size-300 minors are nonzero polynomials vanishing on `D45`. At `N = 16, k = 4`, a generic quartic has `r_4 = 256` (no linear syzygies: finite stabiliser) while `r_4(det_4) = 226` by (A1); so the size-227 minors of `M_4(F)` are nonzero degree-227 polynomials in `I(closure GL_16 . det_4)`, and (A1) gives such a family in every degree `k >= 4`. P1 measures `r_4(det_4) = 226` directly as a check on (A1).

### 3.D Extraneous components and factors (PROVED)

No factor removal, saturation or division is proposed, so nothing needs to be shown to preserve vanishing. The loci `Z_{k,rho}` are closed and `GL_N`-stable; limits are retained by Lemma 3.1 (semicontinuity), not by any finite-witness argument. The extraneous content is instead total: by Theorems A and B, `Y_pad subset Z_{k, r_k(Y_det)}` for every `k`, so the padding family is not an extraneous *component* of the Macaulay locus but is contained in it outright. Coordinate hyperplanes and toric faces do not arise (the construction is `GL_N`-equivariant). Singularities present on both families are exactly what the mechanism reads, in the wrong direction: it measures `dim (S/J_F)_k`, and any functional monotone in that quantity inherits the inequality (this is the record's own formulation in `excess_singularity.md` section 3, now proved rather than measured at `N = 5` and extended to `N = 16`).

### 3.E Representation relevance and the path to a multiplicity comparison

- *Transformation law.* `M_k` is the matrix of the `GL_N`-equivariant, `F`-linear map `Phi_k(F) : V (x) S_{k-3} -> S_k`; the ideal of `s`-minors is the `(dim S_k - s)`-th Fitting ideal of `coker Phi_k`, a `GL_N`-submodule of `Sym^s(S_4^*)`. Degree `s = r_k(Y_det) + 1`: `300` (`N = 5, k = 7`), `227, 1713, ...` (`N = 16, k = 4, 5, ...`). Partition lengths: all lengths occur in principle at `N = 16` (the module is a quotient of `Lambda^s(V (x) S_{k-3}) (x) Lambda^s(S_k^*)`-type data), and the length-`<= 6` components are exactly what Proposition D governs by restriction; Theorem A covers all lengths at once.
- *Path.* Determinant equation: Lemma 3.1 (PROVED). Padding evaluation: identically zero on `Y_pad` (Theorems A, B; PROVED given the certificates). Multiplicity comparison: for every cell `(d, lambda)`, `I_k(Y_det)_{d,lambda} subset I(Y_det)_{d,lambda} cap I(Y_pad)_{d,lambda}`, hence contributes equally to `i_det` and `i_pad` and contributes `0` to `D = i_det - i_pad`. There is no unproved transition on this path; the path ends in zero.

## 4. Early rejection tests (Part 3)

| test | candidate 1 (duality) | candidate 2 (Cayley complex, `d_1`) | candidate 3 (toric) |
|---|---|---|---|
| merely the ordinary discriminant? | for `V = Veronese`, yes (blind); for `V = X_F`, no: it is LMR | no: the discriminant is the determinant of the complex; the minors are its Fitting ideals in other degrees | `Delta_A` for the full support is the discriminant; the face factors are not |
| an existing Hessian/Jacobian equation in new notation? | **yes** (LMR / MR, census 2.2-2.6) | **yes** (Macaulay minors, census row 12, Proposition D) | no, but see next rows |
| sensitive only to support? | no | no | `E_A` at `a = sgn` vs `a = 1` is sign-sensitive, but the `GL`-shadow is support-only |
| vanishes on the whole product family for an elementary reason? | no (right direction; `rank Hess = 9 > 8` on `{per_3 = 0}`) | **yes, and now proved in all degrees**: `J_{ell C} subset (ell, C)` (Theorems A, B) | not applicable (no `GL`-invariant equation produced) |
| is the discriminant locus a hypersurface? | `X_F^vee` is not, for both families (dual defect) - that is the content | not applicable | face discriminants can be `1` (Example 1.7); irrelevant |
| toric boundary condition used as `GL`-invariant? | no | no | **yes** - this is the rejection |
| specialisation of an equation justified? | division `F | minor` is closed (image of a projective morphism); fine | Lemma 3.1 | the specialisation `a -> sgn` is a point evaluation on `C^24`, not a `GL`-statement |
| padding headroom in the prospective representation? | census: one separating member (`k = 6`, degree 24); the brief records insufficient padding multiplicity in the examined cells | none: contribution to `D` is zero in every cell | none |

Two of the brief's specific warnings are answered directly. "The determinant and permanent have the same support in native coordinates": candidate 3 is the only place signs enter, and it does not survive the invariance test. "A toric degeneration of a chosen model is not automatically a degeneration inside the determinant orbit closure": the face degenerations `in_Gamma(det_4)` *are* inside the orbit closure (torus limits of an orbit point), but that only yields `m_det >= m_{in_Gamma}`, the wrong direction for a gap.

## 5. Relation to existing work

- **The onset note / cap theorem** (`onset_conjecture.md` Thm 1, `det4-onset.tex` Thm `thm:cap`): audited. The statement "size-`cap(n)` minors of `M_{3n-5}` lie in `I(D_5^{det_n})`, `cap(4) = 300`" is sound as labelled (proved modulo Kleiman, Dimca, Gulliksen-Negard, all named); the Dimca dependency is now VERIFIED-SOURCE at the statement level (Theorem 3.1, both clauses). So five-row determinant equations *are* known, in degree 300 (and 65 for `det_3`); the reconciliation with "no five-row determinant equations are known" is that none is known below `delta_0 >= 8`, none is known to be nonzero on padding, and by Theorem B none of the Macaulay family ever is. Existence: yes (degree 300). Usable explicit representation components: not computed (the `GL_5`-decomposition of the size-300 Fitting module is not on record). Separation: no (Theorem B). Feasibility: expanding a size-300 minor is out of scope and, by Theorem B, pointless for separation.
- **Proposition D** (`excess_singularity.md`, session 48, corrected session 55): the Macaulay mechanism does not separate at `4 <= r <= 6`, proved given measured determinantal coranks (mod-`p` coranks at `d = 6, 7, 8`; `Q_d = 0` for `d >= 9`). Theorem B makes the `r = 5` row unconditional in the sense above (Kleiman plus one exact certificate at `k <= 6`), replacing the measured entries by the bound `c_k <= 81`. Theorem A is the statement for the full sixteen-variable ambient, which Proposition D does not cover (it argues by restriction to `r` variables and therefore only reaches cells of length `<= 6`).
- **Equation census** rows 12 (Macaulay) and the LMR rows: consistent; the two-family table of `s49_s55_batch_review.md` section 2 (excess singularity wrong way, dual degeneracy right way) is exactly the sorting that candidates 2 and 1 fall into. GKZ adds the identification of the first family with the Cayley method and nothing else.
- **B18-05 / B17-04** Hessian-divisibility: the `Psi = 0` proof on the whole product family is the same phenomenon (a determinant equation that reads product structure); not touched here.
- **The withdrawn `MN = F I_4`** (B18-10 section 4.4): not used; the witness `M = l I_4, N = C I_4` is also a reminder that any construction phrased through a chosen matrix representation must be shown to descend to `F`. The Macaulay construction never uses a representation.
- **The 1+3 barrier** (image-ceiling report): independent of this note; Theorem B is about a specific family of equations of `D45`, the image ceiling about all equations of degree below `delta_0`. They agree where they overlap: the cap is the first known equation at `k = 7`, degree 300, and it is blind.
- **The independent arc-kernel session**: not touched.

## 6. Pilots and controls (Part 4)

### 6.1 Plan and price (written before any run)

Two wrapped pilots, one reserve. Both are exact-integer or modular linear algebra on matrices that are built, not expanded; no elimination, no resultant expansion, no minor expansion.

**P1 `p1_ambient_macaulay.py` (sixteen variables; certificates for Theorem A, plus two measurements).**
(a) `u(j) = dim (C[y]/P)_j` for `j = 0..9`, exactly: for each `Z^3 x Z^3` multidegree `(r | c)` with `|r| = |c| = j`, the block spanned by `m . p_ab,cd` over monomials `m` of multidegree `(r - e_a - e_b | c - e_c - e_d)`, exact rank over `Q` by `flint.fmpz_mat.rank`; `dim P_j` is the sum of block ranks. Controls: `u(0) = 1`, `u(1) = 9`, `u(2) = 36` (nine independent quadrics), `dim P_3 = 77` (four linear syzygies), and `sum_j` over blocks equals `C(j+8,8)`. Price: at `j = 9`, `C(11,2)^2 = 3025` blocks, total rows `9 . C(15,8) = 57,915`, each block at most a few hundred entries; well under 10 s and 100 MiB.
(b) Inequality (A4) for `k = 0..10` with the exact `u(j)`; the forward differences `e_i = Delta^i Q(11)`, `i = 0..15`, exactly (Python integers); fallback direct check of `Q(k) >= 0` for `k = 11..200` if any `e_i < 0`.
(c) MEASURED cross-checks of (A1)-(A2): `rank M_3`, `rank M_4` at `det_4` and at `z per_3` mod `p = 2^31 - 1` (`flint.nmod_mat`), expected `16 / 226` and `10 / 155`; the `256 x 3876` matrix `M_4` is built from the 3876 quartic monomials. Modular rank is a lower bound on the rational rank, so agreement with the exact formula is a consistency check, not a proof.
(d) MEASURED, NOT ASSESSED theoretically: rank of the second Koszul differential `D_k` in degrees `k = 6, 7` at `det_4`, `z per_3` and a random integer quartic (`120 x 256` and `1920 x 2176`, mod `p`). If `det_4` attains the generic value in both degrees, the second differential yields no determinant equation there; if `z per_3` has rank `<=` that of `det_4`, blindness extends to those degrees by Lemma 3.2's argument for `D_k`. Anything else is reported as found.
Budget: under 30 s, under 200 MiB. Stop condition: any wrapper cap hit means the pilot is reported as not completed; one retry allowed on a programming error only.

**P2 `p2_quinary_macaulay.py` (five variables; certificates for Theorem B, plus controls).**
For `k = 3..9`, `rank M_k` at four integer points: `F_det = det(sum x_i A_i)` with seeded `A_i in Mat_4(Z)`, entries in `[-5, 5]` (a point of `D45`); `F_prod = ell . C` with random integer `ell`, `C` (a point of `P5`); `F_padpt = x_1 . per_3(L x)`, `L in Mat_{9 x 5}(Z)` random (an actual padding restriction, a point of `P5`); `F_smooth` a random integer quartic (ambient control). Exact rank over `Q` (`fmpz_mat.rank`) at `F_det` for `k <= 7` (matrices `5 dim S_{k-3} x dim S_k`, at most `350 x 330`), which is the CERTIFIED lower bound Theorem B(ii),(iii) uses; modular rank for the others and for `k = 8, 9`. Expected (from Remark 3.3): `F_det`: `5, 25, 75, 165, 299, 475, 695`; `F_smooth`: `5, 25, 75, 165, 300, 480, 710`; products: at most the pad UB row `16, 39, 80, 146, 245, 386, 579`. Controls that can fail: the smooth control must attain `rho_k`; the two product points must not exceed the pad UB (a violation would refute the `J_F subset (ell, C)` argument, i.e. a bug). Price: under 5 s, under 100 MiB.

**P3 reserve**: not planned; available for one retry.

Hand values used as pre-run expectations for (A4): `Q(11) = -p(10) + 15 p(8) - 29 p(7) + 16 p(6) - p(3) = -3268760 + 7354710 - 4945776 + 868224 - 816 = 7582`; `Q(12) = -p(11) + 15 p(9) - 29 p(8) + 16 p(7) - p(4) = -7726160 + 19612560 - 14219106 + 2728704 - 3876 = 392122`. (`p(3) = 816`, `p(4) = 3876`, `p(6) = 54264`, `p(7) = 170544`, `p(8) = 490314`, `p(9) = 1307504`, `p(10) = 3268760`, `p(11) = 7726160`.)

### 6.2 Results

All three pilots completed. Every certificate check passed; P1's tenth check, the exploratory hypothesis "`D_6` and `D_7` have full row rank at `det_4`", evaluated to `false` (hence `all_checks_pass: false` in its JSON) and is the finding that P3 resolved. The JSON outputs are `pilots/p1_ambient_macaulay.json`, `pilots/p2_quinary_macaulay.json`, `pilots/p3_koszul2_exact.json`. Exact means exact over `Q` (`fmpz_mat.rank`, `fmpz_mat.nullspace`); mod `p` means `p = 2^31 - 1`.

**P1 (Theorem A certificates; 5.45 s).**

(a) CERTIFIED (exact): `u(j) = dim (C[y]/P)_j = 1, 9, 36, 88, 162, 261, 384, 531, 702, 897` and `dim P_j = 0, 0, 9, 77, 333, 1026, 2619, 5904, 12168, 23413` for `j = 0..9` (sum of exact block ranks; 2704 blocks at `j = 9`). Controls `u(0..2) = 1, 9, 36` and `dim P_3 = 77` passed.

(b) CERTIFIED (exact integers): the two sides of Theorem A for `k = 0..10`,

    k:        0  1  2   3    4     5      6       7       8        9        10
    r_pad(k): 0  0  0  10  155  1244   6949   30543  112893   365592  1066075
    r_det(k): 0  0  0  16  226  1712   9232   39712  144839   465104  1348712

`r_pad(k) <= r_det(k)` at every `k <= 10`, and the identity `r_det - r_pad = Q(k) + U(k-1)` was asserted at each `k`. The Newton certificate for `k >= 11`: `e_i = Delta^i Q(11) = 7582, 384540, 782782, 1012452, 977874, 739194, 443955, 211887, 79535, 22988, 4935, 740, 69, 3, 0, 0, 0` for `i = 0..16`, all nonnegative, with `Delta^14 = Delta^15 = Delta^16 = 0` (so `Q` has degree exactly 13 as computed by hand). Hence `Q(k) = sum_{i<=13} e_i C(k-11, i) >= 0` for every integer `k >= 11`, and `r_pad(k) <= r_det(k)` for all `k`. **Theorem A is now PROVED** given Gulliksen-Negard (ADOPTED) and these certificates. The hand values `Q(11) = 7582`, `Q(12) = 392122` were reproduced.

(c) MEASURED (mod `p`, lower bounds on the rational ranks): `rank M_3 = 16 / 10 / 16` and `rank M_4 = 226 / 155 / 256` at `det_4 / z per_3 / random dense quartic`, agreeing with (A1)-(A2) and with the generic maxima. P3 then computed `rank_Q M_4 = 226` and `155` exactly, so (A1) at `k = 4` and (A2) at `k = 4` are also CERTIFIED directly.

(d) MEASURED (second Koszul differential, mod `p`): `rank D_6 = 120 / 105 / 120` exact mod `p` at `det_4 / z per_3 / random`; Gram lower bounds `rank D_7 >= 1904 / 1650 / 1920` at `det_4 / z per_3 / sparse random (300 terms)`. The `det_4` value `1904 < 1920` prompted P3.

**P2 (Theorem B certificates and controls; 4.00 s).** Exact ranks over `Q` of `M_k`, `k = 3..9`, at the four integer points (seed 20260917; the pencil, `ell` and `L` are stored in the JSON):

    k:                 3    4    5    6    7    8    9
    rho_k (generic):   5   25   75  165  300  480  710
    padUB(k):         16   39   80  146  245  386  579
    F_det:             5   25   75  165  299  475  695
    F_smooth:          5   25   75  165  300  480  710
    F_prod (ell C):    5   25   69  141  244  386  579
    F_padpt (x1 per3): 5   25   69  141  244  386  579

CERTIFIED: `r_k(F_det) = rho_k` for `k = 3, 4, 5, 6` (Theorem B(ii) and the `k = 6` certificate), and `r_k(F_det) > padUB(k)` for every `k = 6..9` at this point. Controls that could have failed and did not: `F_smooth` attains `rho_k` at every `k`; both `P5` points stay at or below `padUB(k)` at every `k` (they equal it from `k = 8`, i.e. `(J_F)_k = (ell, C)_k` there). MEASURED consistency: `r_k(F_det) = 5, 25, 75, 165, 299, 475, 695` is exactly the Remark 3.3 profile `dim S_k - c_k` with `c_k = 30, 45, 51, 45, 31, 20, 20`, including the cap drop by one at `k = 7` and the stabilised corank `20` from `k = 8` at this pencil (Dimca's profile predicts `c_8 = 15 + def_2 >= 20`, so `def_2 = 5` at this pencil: no quadric through its twenty nodes). **Theorem B is now PROVED** given Kleiman (ADOPTED) and these certificates. (At this pencil the modular caveat does not even arise: the ranks are rational.)

**P3 (reserve; exact rank of the second differential; 0.51 s).** Using `ker D_k = { antisymmetric matrices of forms of degree k - 6 whose columns are syzygies of the partials }` (the identity `D(sum_{i<j} a_ij e_i ^ e_j) = sum_j (sum_i a_ij d_i F) e_j` with `a_ji = -a_ij`), the exact rational syzygy spaces (`fmpz_mat.nullspace` of `M_k^T`) and the exact rank of the antisymmetry system:

    D_6 at det_4:   dim ker 0,   rank 120  (of 120);   at z per_3: dim ker 15 (constant antisymmetric matrices on the six idle variables), rank 105.
    D_7 at det_4:   dim ker 16,  rank 1904 (of 1920);  at z per_3: dim ker 270, rank 1650.

CERTIFIED consequences (Lemma 3.1 applies verbatim to `D_k`: `rank D_k(F o g) = rank D_k(F)`): (i) the second Koszul differential *does* yield determinant equations in sixteen variables, in degree `k = 7`: the size-1905 minors of the `1920 x 62016` matrix `D_7(F)`, nonzero degree-1905 polynomials in `I(closure GL_16 . det_4)` (nonzero because the sparse random control has full rank 1920); (ii) they are blind: `rank D_7(z per_3) = 1650 <= 1904`, so all of them vanish on `closure(GL_16 . z per_3)`. In degree 6 the second differential yields nothing on the determinant side (full rank 120). Degrees `k >= 8` of `D_k`, and the differentials `D_j`, `j >= 3`, are NOT ASSESSED; the same exact method applies (the degree-8 case needs the quadratic syzygy space, `dim 464` at `det_4` and `932` at `z per_3`, from the `2176 x 15504` matrix `M_5`, about 270 MB as a dense modular matrix, so it would need a sparse or blockwise kernel computation to stay under 512 MiB).

The sixteen-dimensional kernel at `det_4` has a natural candidate description (antisymmetric combinations of the thirty stabiliser syzygies `sum_ij (XM + MY)_ij d_ij det`), not verified here; it is recorded only as a number.

## 7. Resource receipts

Original wrapper receipts, never overwritten: `results/logs/p1_ambient_macaulay_resources.json`, `results/logs/p2_quinary_macaulay_resources.json`, `results/logs/p3_koszul2_exact_resources.json` (with the `.pid` files). All three: `job_object_enforced: true`, one worker, BLAS/OMP threads 1, cap 60 s / 512 MiB, exit code 0.

| pilot | script | started (UTC) | wall (s) | peak Job Object memory (bytes) | exit |
|---|---|---|---|---|---|
| P1 | `pilots/p1_ambient_macaulay.py` | 2026-09-17T14:45:40Z | 5.454 | 235,610,112 | 0 |
| P2 | `pilots/p2_quinary_macaulay.py` | 2026-09-17T14:46:32Z | 3.997 | 93,257,728 | 0 |
| P3 | `pilots/p3_koszul2_exact.py` | 2026-09-17T14:47:16Z | 0.509 | 75,894,784 | 0 |

Total computational wall time 9.96 s of 180 s; no retries; no killed runs. Before dispatch, `tasklist` showed no other Python or CAS process and the wrapper recorded about 9.3-9.8 GB of free physical memory. One sub-second unwrapped command was run before P1: a syntax check of the `python-flint` API on `2 x 2` matrices (`fmpz_mat([[1,2],[2,4]]).rank()`, `nmod_mat(...)`), which computed nothing about the objects of this report; it is disclosed here rather than counted as a pilot. Outside the wrapper, only file reading, hashing and the `pdftotext` extraction of the two papers were run. Literature files stay in the session scratchpad (hashes in section 1 and `MANIFEST.json`); nothing was added to the delivery tree except this directory.

## 8. Decision outcome and the single next step

**Outcome C.** The selected GKZ route (the Cayley method's complex for the discriminant, read through its Fitting ideals) coincides with the programme's Macaulay-minor / Jacobian-cap family and is rigorously blind to padding:

- **PROVED:** Theorem A (all Macaulay degrees, sixteen variables, every cell of every length; given Gulliksen-Negard and the exact certificates), Theorem B (all Macaulay degrees, five variables; given Kleiman and the exact certificates), Lemma 3.1-3.2, the identification of section 2.1, the rejection of candidate 3, the classification of candidate 1 as LMR.
- **CERTIFIED (exact over `Q`):** the second Koszul differential in sixteen variables gives determinant equations in degree 7 (rank 1904 of 1920) and they are blind (padding rank 1650); nothing in degree 6.
- **ADOPTED / VERIFIED-SOURCE:** Gulliksen-Negard, Kleiman (as in the onset note), Dimca Theorem 3.1 (both clauses read in the primary source; used only for the `k = 6` alternative and Remark 3.3).
- **Known, not new:** the dual-degeneracy / Hessian-rank family (candidate 1), the cap theorem, Proposition D at `r <= 6`.
- **NOT ASSESSED:** higher Koszul differentials `D_j`, `j >= 3`, and `D_2` in degrees `>= 8`; the `GL_16`-decomposition of any Fitting module.

What GKZ adds concretely: a unifying description (every equation of the Macaulay/Koszul type is a Fitting ideal of one complex, whose determinant is the discriminant) and, through it, the observation that the *whole* complex, not just its first differential, is subject to the same wrong-way comparison (`dim (S/J_F)_k` and its syzygy analogues are larger on padding). It adds no new determinant equation nonzero on padding, and it cannot: the three GKZ mechanisms are the discriminant (blind), Fitting ideals of the discriminant complex (blind, Theorems A-B and P3), and toric/face structure (not `GL`-invariant). The one GKZ object that separates in the right direction, the dual variety of `X_F`, is LMR and was already in the census.

**Realistic computational cost of continuing this route:** zero for the negative (it is proved); expanding any Macaulay or Koszul minor (degree 300, 227, 1905, ...) is out of scope and, by Theorems A-B, pointless for separation.

**Single next step:** none on the GKZ route; it should stop. If the programme wants the higher-differential statement closed as well (for completeness only, since no separating equation can come from a wrong-way statistic), the bounded item is the exact rank of `D_8` at `det_4` and `z per_3` through a blockwise (weight-graded) kernel of `M_5`, priced at one 60 s / 512 MiB pilot with a sparse nullspace; it is not recommended, because a positive answer (blind) changes nothing and a negative answer (not blind at `D_8`) would contradict the monotonicity that the Hilbert-function comparison makes overwhelmingly likely. The programme's effort is better spent on the dual-degeneracy side, where the census already shows the only right-way family, and on the multiplicity accounting of the cells where its degree-24 member lives.
