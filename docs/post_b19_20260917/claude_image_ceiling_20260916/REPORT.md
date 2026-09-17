# The 1+3 image ceiling is the ideal of determinantal cubics: a precise negative for the restriction-to-reducible-pencils bound below the onset degree delta_0

Claude session, started 16 September 2026, finished 17 September 2026 (the local clock crossed midnight during the session). Fresh directory `work/claude_image_ceiling_20260916/` (did not exist before this session). Historical files, other sessions' outputs and shared ledgers are read-only. No agent launched; no dependency, sandbox, Git-trust or ownership change; no commit, push or publication. Written incrementally: sections 0-4 and the test plan in section 5.1 were written before the single bounded check of section 5.2 was run.

Status: **COMPLETE — precise negative result.** In every five-row cell with `d <= 6` (certified) and `d = 7` (given batch-13's measured totals) the exact 1+3 image multiplicity equals the padding multiplicity, `u_L = m_pad`, so the restriction-to-reducible-pencils bound can never certify a gap there, for any source rank `rho_L`. The general image bound (Corollary 2.4), the selection principle (section 6.1), the missing lemma (section 6.3) and one recommendation (section 6.5) are delivered. Two bounded checks ran (0.41 s and 0.09 s, under 20 MB, Job Object enforced). No cell is nominated; no positive gap is claimed. This line replaced the IN PROGRESS marker after section 8 was written and before hashing.

## 0. Verdict in plain terms (written before the check)

**Route selected (one route, no survey):** bound the coefficient multiplicity `u_L` of the closed image of the 1+3 block-diagonal pencils through the coefficient algebra of 3x3-determinantal cubics, transported to quartic cells by the product map and the Pieri branching rule.

**Result: a precise negative result, with the exact missing lemma.**

1. Let `D_5 subset Sym^3(C^5)^*` be the closure of the quinary cubics with a 3x3 linear determinantal representation (dimension 29, codimension 6; generic member a six-nodal cubic threefold). The closed image of the 1+3 locus is `Y_L = { l * C : l linear, C in D_5 }`, a closed cone inside the 39-dimensional padding cone `Y_pad = { l * C : C any cubic }`.
2. In every five-row cell `(d, lambda)` the exact deficit `m_pad - u_L` is bounded above by the Pieri transport of the ideal of `D_5` (Proposition 2.3):
   `0 <= m_pad - u_L <= sum_{mu |- 3d, lambda/mu a horizontal d-strip} dim I(D_5)^{hw}_{d, mu}`.
3. The ideal `I(D_5)` vanishes in every degree `d <= 5` (batch-13 certificates: rank attains `a` at every weight of every length), and in degrees `6, 7` given the batch-13 measured total-deficit identity. Its first known nonzero components are in degree 65 (Jacobian cap) and 80 (discriminant); the batch-13 paper conjectures the onset is exactly 65. The lowest onset consistent with the record is `delta_0 >= 8`.
4. Therefore, for every five-row cell with `d <= 5` unconditionally, and `d <= 7` given the measured totals: **`u_L = m_pad` exactly.** The restriction bound then reads `m_det <= min(a, s - rho_L + m_pad) >= m_pad >= r` for every actual-padding floor `r`, whatever the source restriction rank `rho_L` is. The route cannot certify a gap in the proposed regime. The reason is not that the ceiling `u_0 = U` is loose; it is that the exact image multiplicity coincides with the padding multiplicity: **polynomials of degree below `delta_0` cannot tell determinantal products `l * C_det` from arbitrary products `l * C`.**
5. The first cells where the route could act at all are at `d = delta_0 in [8, 65]`, and only in cells `lambda |- 4 delta_0` that contain an equation type `mu |- 3 delta_0` of `D_5` (necessarily `ell(mu) = 5`) as a horizontal-strip complement. At the conjectured onset `d = 65` these are the types of the `65 x 65` minors of the batch-13 Jacobian matrix `M_4(F)`. Even there a gap needs, in addition, a source restriction rank `rho_L > s - (m_pad - u_L) + (m_pad - r)`, with `s` in the thousands at such degrees, while the programme's full-H carrier reached rank 2 of 5 at `d = 5`.

No positive gap is claimed. No cell is nominated. The `d = 6` cell `(8,4,4,4,4)` is excluded by the reviewed H5 multiplication argument before any consideration (section 4), and the route independently shows it is dead.

**The exact next missing lemma** (section 6): a length-five highest-weight equation of `D_5` in a degree small enough that a five-row source of dimension `s(d, lambda)` can be carried, i.e. a proof that `delta_0 <= 7`, which contradicts the measured totals; failing that, the per-weight certification of the 3 + 80 ambient units at degrees 6 and 7 that would make the negative unconditional through degree 7. Nothing short of an explicit low-degree equation of the six-nodal cubic threefolds revives the route.

## 1. Provenance, scope, and what was read

Workspace `C:/Users/swami/Projects/gct-gpt`. No git command was run. Process state at start: no `python` process was running (`tasklist`); the separate session testing a sparse evaluator for `(5,(4^5))` was not running, and none of its files were read, modified or continued. Inputs read (SHA-256 pins in `MANIFEST.json`):

- `Claude_Handover_B15_B18/CLAUDE_DESCENT_FOLLOWUP_20260916.md`: the consolidated assignment, historical context only.
- `work/descent_followup_claude_20260916/REPORT.md`: the corrected restriction theorem (B1), the never-a-gap statement for `u_0 = U` (B2), the `(8,4,4,4,4)` exclusion (B.9), and B10, which names a sharpened `u_L` for the 1+3 image as a research direction.
- `work/batch15_workers/B15-12/docs/b18_12_coefficient_algebra.md`: the historical note; its Theorem 3.1 and section 4.3 as corrected by B1-B10. Its uncorrected claims (opening sufficiency, block-triangular nonvacuity, the `rho_L - u_L` interpretation) are not used.
- `work/extension_descent_20260916/REPORT.md`, `work/fiber_compatibility_20260916/REPORT.md`: consulted for the closure-correct proof style and the five-variable padding facts; nothing from them is re-derived or relied on here beyond what the descent follow-up already reviewed.
- `work/batch15_workers/B15-08/docs/b17_08_report.md`: the product-map rank formula (2), and the ceiling `U = min(a, T)`, `T = sum_mu [s_mu] h_d[h_3]` over horizontal strips (3).
- `work/batch15_workers/B15-03/docs/b17_03_report.md`, Lemma 1 (length restriction and multiplicity inheritance).
- `work/batch15_workers/B15-01/docs/b18_01_report.md`, Lemma 4.1 (`dim R135 = 39`) and the identification `closure(rho_5 X_pad) = R135`.
- **Batch-13 det3 material (Astra, sessions 26-38), read-only:** `work/batch13_astra/B13-02/docs/d5_ideal.md` (the object `D_5`, its singularity lemma, the length-5 concentration of `I(D_5)`, the measured bracket for `delta_0`); `work/batch13_astra/B13-02/docs/transfer_lemma.md` (Proposition 8: the Pieri-transport injection, proved there for the `per_3` analogue); `work/batch13_astra/B13-02/paper/det3-conductor.tex` (Theorem `thm:sharp`, Remark `rem:crossover`, Proposition `prop:jaccap`, the total-deficit identity, Question `q:delta0`); `work/batch13_astra/B13-02/docs/det_onset.md` (the det4 analogue, for contrast only).
- `Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json`: the inherited `a, s, g, T, U` for all five-row cells at `d = 5, 6` (this copy; pinned).

Labels used below: **PROVED** (argument written here), **ADOPTED** (accepted programme result, cited), **PRODUCER-CERTIFIED** (a batch-13 certificate described in its report, inspected, not replayed), **MEASURED** (a numerical statement without a certificate), **CONJECTURED**, **NOT REACHED**.

## 2. The closed image, the exact graded maps, and every bound direction

### 2.1 Objects and conventions

`V = C^5`. Forms live in `Sym^k(V^*)`; ordinary coefficient functions `c_alpha` (quartics), `C_beta` (cubics), `l_i` (linear forms) carry positive weights `alpha, beta, e_i` and the raising operators `E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}` of the programme's convention, so that `Sym^d(Sym^4 V)` and its relatives are the polynomial `GL_5`-modules and highest-weight coefficient polynomials have label `S_lambda(V)`.

- `P = Sym(Sym^4 V) = C[Sym^4 V^*]`, the ambient coefficient ring; `a(d, lambda) = dim P^{hw}_{d, lambda}`.
- `m : V^* x Sym^3 V^* -> Sym^4 V^*`, `(l, C) -> l C`, the product map. `Y_pad := m(V^* x Sym^3 V^*)`. This set is closed: it is the affine cone over the image of the projective morphism `P^4 x P^34 -> P^69`, and the image of a projective morphism is closed. `Y_pad = R135` of B18-01, `dim Y_pad = 39` (ADOPTED, B18-01 Lemma 4.1). By the accepted five-variable identification, `m_pad(d, lambda) = mult_lambda C[Y_pad]_d` (ADOPTED, B17-08 (2), B18-01 01-A with B17-03 Lemma 2).
- `D_5 := closure{ det(sum_k x_k M_k) : M_k in Mat_3 } subset Sym^3 V^*`, `dim D_5 = 29` (ADOPTED, batch-13 Remark `rem:crossover`: the map bound `9*5 - 16 = 29 < 35`). It is a `GL_5`-stable closed cone. `D_5^o` denotes the image of the pencil map before closure.
- `Y_L := m(V^* x D_5)`. Closed by the same projective-morphism argument (`D_5` is a closed cone, so `P^4 x P(D_5) -> P^69` is projective). **This is the closed image of the 1+3 locus:** for a block-diagonal tuple `a_k (+) M_k`, `phi(a (+) M) = det(sum x_k (a_k (+) M_k)) = (sum a_k x_k) * det(sum x_k M_k)`, so the `G x GL_5`-saturation of the block-diagonal tuples maps onto `{ l C : l in V^*, C in D_5^o }`, whose closure is `Y_L` (continuity of `m`, density of `D_5^o` in `D_5`, closedness of `Y_L`). The closure `L` of the saturated locus maps into `Y_L` because `phi(closure L^o) subset closure phi(L^o)`. **No description of the boundary of `D_5` is used anywhere:** `Y_L` is defined through the closed variety `D_5`, and the parameter ring below is the coordinate ring of that closure, boundary included. `dim Y_L = 33` is the note's count; only `Y_L subset Y_pad` is used.
- `Pi := Sym(V) (x) Sym(Sym^3 V) = C[V^* x Sym^3 V^*]`, bigraded. `Pi_L := Sym(V) (x) C[D_5] = C[V^* x D_5] = Pi / (Sym(V) (x) I(D_5))` (ideal of a product with an affine-space factor).
- Source and restriction data as in the corrected Theorem B1: `S` the full-H (transposition included) highest-weight source of type `lambda`, entry degree `4d`, `dim S = s`; `rho_L = rank(S -> C[L])`; `u_L = mult_lambda C[Y_L]_d`; `m_pad = mult_lambda C[Y_pad]_d`; `m_det = mult_lambda C[D45]_d`.

### 2.2 The exact graded map (PROVED)

**Lemma 2.1.** `m^* : P -> Pi`, `c_alpha -> sum_{i : alpha_i > 0} l_i (x) C_{alpha - e_i}`, is a `GL_5`-equivariant algebra homomorphism, homogeneous of bidegree `(1,1)`; hence `m^*(P_d) subset Pi_{(d,d)} = Sym^d V (x) Sym^d(Sym^3 V)`.

*Proof.* The formula is the coefficient of `x^alpha` in `(sum_i l_i x_i)(sum_beta C_beta x^beta)`, so `m^*` is the pullback of functions along `m` and is an algebra map of bidegree `(1,1)`. Equivariance in the stated convention, written out because the three rings use different index shifts: for `i < j`, applying `E_ij` to the right-hand side (with `E_ij l_k = delta_jk l_i` and `E_ij C_beta = (beta_i + 1) C_{beta + e_i - e_j}`) gives `l_i C_{alpha - e_j} + sum_k (alpha_i + 1 - delta_ik) l_k C_{alpha - e_k + e_i - e_j}`, while `m^*(E_ij c_alpha) = (alpha_i + 1) sum_k l_k C_{alpha + e_i - e_j - e_k}`; the difference is `l_i C_{alpha - e_j} - l_i C_{alpha - e_j} = 0`. (This is B17-08's formula (1).) QED

**Lemma 2.2 (the two coordinate rings inside the two parameter rings).**
(i) `ker(m^*) = I(Y_pad)`, so `R_pad := C[Y_pad] = P / I(Y_pad)` embeds as the subalgebra `m^*(P) subset Pi`, generated in bidegree `(1,1)`.
(ii) Let `nu : P -> Pi_L` be `m^*` followed by the quotient `Pi -> Pi_L`. Then `ker(nu) = I(Y_L)`, so `R_L := C[Y_L]` embeds as `nu(P) subset Pi_L`, and `R_L` is the image of `R_pad` under `Pi -> Pi_L`.

*Proof.* (i) `h in ker m^*` iff `h ∘ m = 0` on `V^* x Sym^3 V^*` iff `h` vanishes on `m(V^* x Sym^3 V^*) = Y_pad`. (ii) `h in ker nu` iff `m^* h in Sym(V) (x) I(D_5) = I(V^* x D_5)` iff `h ∘ m` vanishes on `V^* x D_5` iff `h` vanishes on `m(V^* x D_5) = Y_L`. The last statement is the commutativity `nu = (Pi -> Pi_L) ∘ m^*`. QED

**Every bound direction, stated once.** In type `lambda`, degree `d`:

- `u_L = mult_lambda (R_L)_d <= mult_lambda (Pi_L)_{(d,d)} =: T_L(d, lambda)`: the **parameter-ring ceiling** for the image algebra. The image algebra is the subalgebra generated in bidegree `(1,1)`; the parameter ring is larger in general; the inequality is only `<=`.
- `m_pad = mult_lambda (R_pad)_d <= mult_lambda Pi_{(d,d)} = T(d, lambda)`: B17-08's ceiling, `U = min(a, T)`.
- `u_L <= m_pad`, because `R_L` is a quotient of `R_pad` (Lemma 2.2 (ii)); geometrically `Y_L subset Y_pad`.
- `rho_L <= min(s, T^s_L)`, with `T^s_L` the multiplicity of the target of the block restriction (section 2.4).
- The restriction theorem B1: `m_det <= min(a, s - rho_L + u_L)`. A certified floor `rho_0 <= rho_L` and a certified ceiling `u_0 >= u_L` are the safe substitutions; the exact `u_L` is what this note pins.

### 2.3 The parameter-ring ceiling is the 3x3 coefficient algebra transported by Pieri (PROVED)

By Pieri, `Sym^d V (x) S_mu V = ⊕ S_lambda V` over the `lambda` with `lambda/mu` a horizontal `d`-strip. Write `a_3(d, mu) := mult_mu Sym^d(Sym^3 V) = [s_mu] h_d[h_3]`, `m_3(d, mu) := mult_mu C[D_5]_d`, and `i_3(d, mu) := mult_mu I(D_5)_d = a_3 - m_3`. Then

    T(d, lambda)   = sum_{mu |- 3d, lambda/mu horizontal d-strip} a_3(d, mu)          (B17-08 (3))
    T_L(d, lambda) = sum_{mu |- 3d, lambda/mu horizontal d-strip} m_3(d, mu)
                   = T(d, lambda) - sum_{mu} i_3(d, mu).

**Length reduction for `D_5` (ADOPTED, with the two-line proof).** For `ell(mu) <= 5`, `m_3(d, mu)` equals the multiplicity of `S_mu(C^9)` in `C[closure(GL_9 * det_3)]_d`. Proof: `D_5 = closure(GL_9 det_3) ∩ Sym^3(C^5)^*`, because a limit `g = lim det_3 ∘ G_i` of forms in the first five variables equals `lim det_3 ∘ (G_i ∘ iota)` with `iota : C^5 -> C^9` the coordinate inclusion; and restriction of functions from `Sym^3(C^9)^*` to the coordinate subspace `Sym^3(C^5)^*` is the exact truncation functor `S_mu(C^9) -> S_mu(C^5)` (zero for `ell(mu) > 5`), which carries the quotient `Sym / I(closure)` to `Sym / I(D_5)`. This is B17-03 Lemma 1 for cubics and batch-13's Proposition `prop:lengthred`. The same argument with `4` in place of `5` shows that `I(D_5)` is concentrated at `ell(mu) = 5`, because the restriction of `D_5` to a 4-plane is `D_4 = ` all cubic surfaces (Beauville; batch-13 `d5_ideal.md` section 3, PROVED there).

**Proposition 2.3 (the exact deficit and its two-sided estimate).** Let `delta_L := m_pad - u_L >= 0`. Then

    delta_L = mult_lambda [ (R_pad)_d ∩ ( Sym^d V (x) I(D_5)_d ) ],

and

    max( 0, sum_mu i_3(d, mu) - (T - m_pad) )  <=  delta_L  <=  sum_{mu : lambda/mu horizontal d-strip} i_3(d, mu).

*Proof.* By Lemma 2.2, `(R_pad)_d -> (R_L)_d` is the restriction to `(R_pad)_d subset Pi_{(d,d)}` of the quotient `Pi_{(d,d)} -> (Pi_L)_{(d,d)}`, whose kernel is `Sym^d V (x) I(D_5)_d`. So the kernel of `(R_pad)_d -> (R_L)_d` is the displayed intersection, and `delta_L` is its `lambda`-multiplicity (multiplicities are additive on exact sequences of `GL_5`-modules). The upper bound is monotonicity of multiplicity under the inclusion into `Sym^d V (x) I(D_5)_d`, whose `lambda`-multiplicity is the Pieri sum. The lower bound: for `GL_5`-submodules `A, B` of `Pi_{(d,d)}`, `mult(A ∩ B) = mult A + mult B - mult(A + B) >= mult A + mult B - mult Pi_{(d,d)}`, with `A = (R_pad)_d`, `B = Sym^d V (x) I(D_5)_d`. QED

**Corollary 2.4 (the certified image bound).** `u_L <= min( a, m_pad, T(d, lambda) - sum_mu i_3(d, mu) )`, where any certified lower bound on `dim I(D_5)^{hw}_{d, mu}` may be substituted for `i_3`: an explicit equation, or `a_3(d, mu) - s_3(d, mu) > 0` with `s_3` the symmetric Kronecker coefficient for the rectangle `(d^3)` (valid since `m_3 <= s_3`, the orbit bound for `det_3`).

**Corollary 2.5 (the regime where nothing can happen).** If `I(D_5)_d = 0` then `u_L = m_pad` for every `lambda`; equivalently `I(Y_L)_d = I(Y_pad)_d`. Then `min(a, s - rho_L + u_L) = min(a, s - rho_L + m_pad) >= m_pad >= r` for every actual-padding floor `r` and every `rho_L in [0, s]`: the 1+3 restriction bound cannot certify a gap in any cell of that degree. (It can still lower the ambient bound `a` on the determinant side when `s - rho_L + m_pad < a`; that is a determinant-only statement, as B2 already noted for `u_0 = U`.)

Corollary 2.5 is the transfer lemma of batch-13 (`transfer_lemma.md`, Proposition 8, proved there for `per_3` restrictions inside the padding locus in `r >= 6` variables), applied here to `det_3` and the 1+3 image inside the five-variable padding locus.

### 2.4 The source side: the loss `s - rho_L`, so that a target-side deficit is never mistaken for a gap

Restricting an `SL_4 x SL_4`-invariant of entry degree `4d` on `(Mat_4)^5` to 1+3 block-diagonal tuples `(a_k (+) M_k)` gives a function of `(a, M) in C^5 x (Mat_3)^5` that is invariant under `SL_3 x SL_3` on the blocks and under the block torus `(diag(t^{-3}, t I_3), diag(u^{-3}, u I_3)) in SL_4 x SL_4`, which forces bidegree `(d, 3d)` in `(a, M)`. Transposition restricts to transposition of the 3x3 block. So the block restriction is a `GL_5`-equivariant linear map

    S  -->  ( Sym^d V (x) ( C[(Mat_3)^5]_{3d} )^{SL_3 x SL_3, tau} )^{hw}_lambda,

whose target has multiplicity `T^s_L(d, lambda) = sum_{mu : lambda/mu horizontal d-strip} s_3(d, mu)` (Cauchy for `C^3 (x) C^3 (x) V` and the symmetric rectangular Kronecker coefficient for the rectangle `(d^3)`, exactly as in the note's Claim 1.2). Hence `rho_L <= min(s, T^s_L)`. Whatever the target-side deficit `delta_L` is, a gap through the route needs

    r  >  s - rho_L + u_L      <=>      rho_L  >  s - delta_L + (m_pad - r),

i.e. the source must be faithful on the block locus up to `delta_L` dimensions, minus the slack of the padding floor. A target-side deficit alone certifies nothing. By Corollary 2.5 the deficit is zero wherever `I(D_5)_d = 0`, so in that regime no value of `rho_L` helps.

The two ceilings share their arithmetic: `T^s_L` uses `s_3`, `T_L` uses `m_3 <= min(a_3, s_3)`. The stabilizer comparison `a_3 > s_3` is the only character-computable source of `i_3 > 0`; batch-13 measured that it never fires at length 5 through degree 10 (section 3.2).

## 3. What is known about `I(D_5)`, degree by degree

All statements in this section are batch-13 results (Astra, sessions 26-38), read in `d5_ideal.md`, `transfer_lemma.md`, `det-conductor.tex` and `det_onset.md`; nothing was replayed here. Their labels are the batch-13 labels, downgraded where the record itself says so.

### 3.1 The object and its two explicit equations (PROVED there)

- Every member of `D_5` is a singular cubic: a `P^4` in `P(Mat_3) = P^8` meets the 4-dimensional rank-one Segre locus, and at such a point all cofactors vanish, so all partials of `det` vanish (batch-13 Theorem `thm:sharp`). Hence the discriminant of quinary cubics, degree 80, type `(48^5)`, lies in `I(D_5)`.
- Jacobian cap (batch-13 Proposition `prop:jaccap`, using Kleiman transversality and Dimca's syzygy theorem as cited literature): for `F in D_5` the `75 x 70` matrix `M_4(F)` of the multiplication map `(Sym^2 V)^{+5} -> Sym^4 V` by the partials of `F` has rank `<= 64`, versus `65` for smooth `F`; its `65 x 65` minors are nonzero degree-65 polynomials spanning a `GL_5`-stable subspace of `I(D_5)_65`, of length-five types.
- `I(D_5)` is concentrated at length exactly 5 (section 2.3).

### 3.2 The measured bracket for the onset `delta_0` (the least degree with `I(D_5)_d != 0`)

- `d <= 5`: `I(closure(GL_9 det_3))_d = 0` at every weight of every length; each weight a rank-attains-`a` certificate, two primes (**PRODUCER-CERTIFIED**, batch-13; `d5_ideal.md` section 4 table, `det-conductor.tex` "no equations at all below degree 6").
- `d = 6, 7`: the total-deficit identity `sum_lambda (m(lambda) - a(lambda, d)) = 1, 6, 31, 141, 618, 2488` for `d = 2..7`, left side measured by the batch-13 streamed algorithm, right side exact plethysm/branching, forces `mult = a` at every weight through `d = 7` (**MEASURED**: the paper says "given the measured totals"; direct per-weight certificates cover all but 3 ambient units at `d = 6` and all but 80 at `d = 7`; the 3 units are three weights with weight-space dimensions `N_S = 3988, 4028, 4456` per `d5_ideal.md` section 5, whose lengths are identified in section 5.2 below).
- Occurrence route: `a_3(d, mu) <= m^{orbit}_3(d, mu)` at every length-5 weight through `d = 10` (exhaustive, **MEASURED** by characters, `d5_ideal.md` section 4), so no character comparison produces `i_3 > 0` in that window; and the transpose-symmetric semi-invariant ring's bidegree-`(d,d)` dimension stays above `dim Sym^d(Sym^3 C^5)` past degree 100, so no equation is forced by dimension counting anywhere in the bracket (**MEASURED/stated** in Question `q:delta0`).
- Bracket: `6 <= delta_0 <= 65` unconditionally; `8 <= delta_0 <= 65` given the measured totals; **CONJECTURED** `delta_0 = 65`.

### 3.3 Consequence for the route (PROVED given the labels above)

Combining Corollary 2.5 with section 3.2:

| degree `d` | status of `I(D_5)_d = 0` | consequence for every five-row `lambda |- 4d` |
|---|---|---|
| `d <= 5` | PRODUCER-CERTIFIED (batch-13) | `u_L = m_pad`; route cannot certify a gap |
| `d = 6, 7` | MEASURED (totals); per-weight residue 3 and 80 units | `u_L = m_pad` given the totals; unconditionally `delta_L <= (Pieri transport of the residue weights)` |
| `8 <= d < delta_0` | open, `delta_0` conjectured 65 | `u_L = m_pad`; route inert |
| `d = 65` | explicit equations (Jacobian cap, PROVED) | `delta_L` can be positive only in `lambda |- 260` containing a minor type as horizontal-strip complement |
| `d = 80` | discriminant, type `(48^5)` (PROVED) | `lambda |- 320` with `lambda/(48^5)` a horizontal 80-strip |

In the programme's proposed regime (`d = 5` closed by the degree-five theorem; `d = 6` the smallest open degree; `d = 7` the largest degree any five-row source has ever been priced at) the route cannot improve the existing bound. This is the precise negative result requested.

## 4. Exclusion of `d = 6`, `lambda = (8,4,4,4,4)` before consideration (ADOPTED, restated)

The reviewed H5 multiplication argument (descent follow-up, section B.9, PROVED there on premises P1 MEASURED, P2 VERIFIED, P3 PROVED by Pieri): with `H5` the unique `(4^5)` degree-five invariant, nonzero on `det K5` (`322560`) and vanishing on all of `Y_pad` (Pieri: `(4^5)/nu` is never a horizontal 5-strip, so `T(5,(4^5)) = 0`), the product `h = c_{(4,0,0,0,0)} * H5` is a highest-weight vector of type `(8,4,4,4,4)`, nonzero on `D45` (`C[D45]` is a domain and both factors are nonzero on it) and zero on `Y_pad`. Hence `m_det >= 1`, `i_pad >= 1`, `m_pad <= a - 1 = 1`, `D <= 0`. **Excluded.**

The route agrees independently: the Pieri range of `(8,4,4,4,4)` at `d = 6` is `mu in {(6,4,4,4), (5,4,4,4,1), (4,4,4,4,2)}` (the census gives `T = 1`, i.e. exactly one of these carries `a_3 = 1`; section 5.2 identifies which), so `u_L <= m_pad <= 1 <= m_det` and no bound below `m_det` is available from any `rho_L`. The cell is not considered further.

## 5. The one bounded check

### 5.1 Test plan and price (written before running)

Purpose: (a) validate the Pieri-transport arithmetic of section 2.3 against the inherited census by recomputing `T(d, lambda) = sum_mu a_3(d, mu)` for all 23 + 105 five-row cells at `d = 5, 6` from an independent computation of `a_3(d, mu)`; (b) identify the three batch-13 residue weights at `d = 6` (`N_S = 3988, 4028, 4456`) by computing the weight-space dimensions of `Sym^6(Sym^3 C^5)` at all length-5 dominant weights with `a_3 > 0`, and list which `d = 6` five-row cells `lambda` have any of them in their Pieri range (these are the only `d = 6` cells where Corollary 2.5 is not yet unconditional); (c) print the Pieri range of `(8,4,4,4,4)`.

Method: weight multiplicities of `Sym^d(Sym^3 C^5)` by a multiset dynamic programme over the 35 cubic monomials (states `(k, weight)`, `k <= d`); `a_3(d, mu)` by the Weyl alternant `sum_{w in S_5} sgn(w) K(mu + rho - w rho)`, `rho = (4,3,2,1,0)`; control `sum_mu a_3 * dim S_mu(C^5) = C(34 + d, d)` (`575757` at `d = 5`, `3838380` at `d = 6`); horizontal strips by the interlacing condition `lambda_{i+1} <= mu_i <= lambda_i`. Price: at most `1 + 35 + 210 + 715 + 1820 + 3876 + 7315` DP states times 35 monomials times 7 multiplicities, about `3.5 * 10^6` dictionary operations, well under 10 s and 100 MiB in pure Python; no BLAS. Run under the inspected Windows Job Object wrapper `work/batch15_workers/B15-02/analysis/b15_bound.py` (SHA-256 `ca001081f49e0048812b871a31e3be85435b210b3a538170a9f006408a41f854`, the copy the descent session used), `--seconds 60 --memory-mb 512`, one worker, one BLAS thread, with the B15-02 `.venv` Python 3.12.10. Stop condition: any cap hit means the check is reported as not completed; no retry.

### 5.2 Result (MEASURED here; receipts in `results/logs/`)

Two checks were run, both through the wrapper, both far under the caps, no retries:

| check | script | wall (s) | peak Job Object memory (bytes) | exit | Job Object enforced |
|---|---|---|---|---|---|
| C1 | `checks/c1_pieri_transfer.py` | 0.41 | 19,423,232 | 0 | yes |
| C2 | `checks/c2_residue_length6.py` | 0.09 | 12,886,016 | 0 | yes |

Outputs: `results/c1_pieri_transfer.json`, `results/c2_residue_length6.json`, `results/logs/c{1,2}_*_resources.json`. C2 was added after C1 to settle the length of the residue weights (section 5.1 (b) could not be answered by C1 alone, see below); it is the second and last check.

**(a) `a_3(d, mu)` and the dimension control.** `d = 5`: 28 constituents, `sum a_3 dim S_mu = 575757 = C(39,5)`; `d = 6`: 63 constituents, `3838380 = C(40,6)`. Both controls pass. Length-5 constituents (each with `a_3 = 1`):

- `d = 5` (3 weights): `(7,2,2,2,2)`, `(6,4,2,2,1)`, `(5,5,3,1,1)`.
- `d = 6` (16 weights): `(10,2,2,2,2)`, `(9,4,2,2,1)`, `(9,3,2,2,2)`, `(8,5,3,1,1)`, `(8,5,2,2,1)`, `(8,4,3,2,1)`, `(8,4,2,2,2)`, `(7,6,2,2,1)`, `(7,5,4,1,1)`, `(7,5,3,2,1)`, `(7,5,2,2,2)`, `(7,4,4,2,1)`, `(6,6,2,2,2)`, `(6,5,4,2,1)`, `(6,4,4,2,2)`, `(5,5,4,3,1)`.

These match batch-13's counts "3 weights of length >= 5 at delta = 5" and, together with the four length-6 constituents of `Sym^6(Sym^3)` listed in `transfer_lemma.md` (`(8,2,2,2,2,2)`, `(7,4,2,2,2,1)`, `(6,5,3,2,1,1)`, `(5,5,5,1,1,1)`), the "20 weights of length 5-9 at delta = 6".

**(b) The Pieri sum `T` against the census.** `d = 5`: all 23 five-row cells match `padding_source_raw` exactly. `d = 6`: 71 of 105 match; **34 cells differ by +1 or +2 in the census** (list in `results/c1_pieri_transfer.json`, `T_control.mismatches`). Cause, read off the census script `Batch17_Planning/symmetry_dream/astra/toy_character_screen.py`, function `horizontal(lam, mu)`: it tests the interlacing `lam_i >= mu_i >= lam_{i+1}` only for `i <= len(lam)`, so a `mu` with **more parts than `lam`** passes when its extra part is ignored; at `d = 6` the core allows `mu` of length 6, and the four length-6 constituents leak into 34 five-row cells. At `d = 5` the core is capped at length 5, so no leak. (The same defect makes the census's `padding_source_raw = 29` for `lambda = (20)`, where the true B17-08 sum is 1.) **The census's `padding_ceiling U = min(a, raw)` is unaffected in all 105 `d = 6` five-row cells** (C2, `census_U_changes_d6 = []`): the over-count never crosses `a`. The inherited `U` values therefore stand; the `padding_source_raw` field is over-counted at `d = 6` and should not be quoted as `T`. This is a side finding about an inherited file, recorded, not a correction applied to it.

**(c) The batch-13 residue weights are of length 6.** No length-5 weight at `d = 6` has weight-space dimension in `{3988, 4028, 4456}`: the length-5 values range from 416 to **2829** (`(6,4,4,2,2)`), and a length-5 weight space has the same dimension in any number of variables `>= 5` (a cubic-coefficient monomial of weight `mu` with `mu_6 = ... = 0` uses only the first five variables). C2 computes the length-6 weight spaces of `Sym^6(Sym^3 C^6)`: `(8,2,2,2,2,2) -> 4028`, `(7,4,2,2,2,1) -> 4456`, `(6,5,3,2,1,1) -> 3988`, `(5,5,5,1,1,1) -> 2737` (pruned DP; control: it reproduces C1's 2829 and 416 at two length-5 weights). So the three ambient units that batch-13 left without a direct certificate at `delta = 6` are exactly the three largest length-6 weights, and **all sixteen length-5 weights at `d = 6` carry a direct batch-13 rank-attains-`a` certificate.** Consequently:

> `I(D_5)_6 = 0` is **PRODUCER-CERTIFIED per weight** (batch-13 certificates, identified here), no longer only "given the measured totals". Corollary 2.5 holds unconditionally at `d = 6`: `u_L = m_pad` in every `d = 6` five-row cell.

At `d = 7` the residue is 80 ambient units of unknown length; the statement stays MEASURED (totals) there.

**(d) Pieri range of `(8,4,4,4,4)`.** `mu = (6,4,4,4)`: `a_3 = 1`; `(5,4,4,4,1)`: 0; `(4,4,4,4,2)`: 0. So `T = 1` comes from a **four-row** `mu`, and since `I(D_5)` is concentrated in length 5, `u_L = m_pad` in this cell in every degree-independent sense: the route is inert there unconditionally, in addition to the H5 exclusion of section 4.

**(e) Inert cells (unconditional, all degrees).** A five-row cell whose Pieri range contains no length-5 `mu` with `a_3(d, mu) > 0` has `delta_L = 0` by Proposition 2.3 and the length-5 concentration of `I(D_5)`, whatever `delta_0` is. A sufficient condition is `lambda_1 <= d` (then every `mu` in the range has `mu_5 = 0`: the interlacing forces `mu = (lambda_2, ..., lambda_5, 0)` when `lambda_1 = d`, and no `mu` at all when `lambda_1 < d` unless `T = 0`). The exact lists (C2):

- `d = 5` (6 of 23): `(9,7,2,1,1)`, `(8,7,3,1,1)`, `(7,7,4,1,1)`, `(7,4,4,4,1)`, `(6,4,4,4,2)`, `(4,4,4,4,4)`.
- `d = 6` (17 of 105): `(13,7,2,1,1)`, `(12,8,2,1,1)`, `(11,9,2,1,1)`, `(10,9,3,1,1)`, `(9,9,4,1,1)`, `(9,7,6,1,1)`, `(9,4,4,4,3)`, `(8,7,7,1,1)`, `(8,6,6,3,1)`, `(8,4,4,4,4)`, `(7,7,6,3,1)`, `(7,7,4,3,3)`, `(7,6,6,4,1)`, `(7,6,6,3,2)`, `(7,6,4,4,3)`, `(6,6,6,4,2)`, `(6,6,4,4,4)`.

This list includes the Astra five-row pilot cell `(12,8,2,1,1)` and the two `d = 6` cells with `lambda_1 <= 6`. For every other five-row cell at `d <= 6` the route is inert by the certified vanishing of `I(D_5)_d`; the distinction only matters for what would have to change (section 6).

## 6. The selection principle, the exact next missing lemma, and what would falsify this negative

### 6.1 What the route gives that is new (the deliverable)

Not a cell list. Two structural statements, both proved above:

1. **Image bound.** `u_L <= min( a, m_pad, T(d,lambda) - sum_{mu : lambda/mu horizontal d-strip} i_3(d,mu) )`, and the exact deficit satisfies `max(0, sum_mu i_3 - (T - m_pad)) <= m_pad - u_L <= sum_mu i_3` (Proposition 2.3, Corollary 2.4). The only sharpening of the padding ceiling available through the 1+3 image is the Pieri transport of the ideal of the six-nodal cubic threefolds; the image algebra's own non-normality (`R_L` versus `Pi_L`) cannot push `u_L` below `m_pad` by more than that transport.
2. **Selection principle.** A five-row cell `(d, lambda)` can carry a positive 1+3 deficit only if (i) `d >= delta_0`, the onset degree of `I(D_5)` at length 5, and (ii) `lambda` contains a length-5 equation type `mu |- 3d` of `D_5` as the complement of a horizontal `d`-strip; a necessary combinatorial condition for (ii) is `lambda_1 >= d + 1`. Given (i)-(ii), a gap still needs `rho_L > s - delta_L + (m_pad - r)` on the source side (section 2.4) and a padding floor `r`.

With the batch-13 record, (i) fails for every `d <= 5` (certified), for `d = 6` (certified per weight, section 5.2 (c)), for `d = 7` (measured totals), and for all `d < delta_0` with `8 <= delta_0 <= 65`, conjecturally `delta_0 = 65`.

### 6.2 The precise negative in the proposed regime

In every five-row cell with `d <= 6`, `u_L = m_pad` exactly, so `min(a, s - rho_L + u_L) >= m_pad >= r` for every source rank `rho_L` and every padding floor `r`: **the restriction-to-reducible-pencils bound cannot identify a structurally promising five-row cell, and cannot certify a gap, at any degree the programme can carry.** The obstruction is geometric, not a slack ceiling: `I(Y_L)_d = I(Y_pad)_d` for `d < delta_0`, i.e. the closed 1+3 image and the whole padding cone have the same equations through degree `delta_0 - 1 >= 6` (`>= 7` given the totals). Any restriction to a sublocus of `Y_pad` whose image is `{ l C : C in Z }` for a `GL_5`-stable closed `Z subset Sym^3 V^*` is subject to the same Pieri-transport bound with `I(Z)` in place of `I(D_5)`; for `Z = D_5` this is the whole story of the 1+3 locus. (The 2+2 locus has image `{ q_1 q_2 : rank q_i <= 4 }`, which is not of this form and is not contained in `Y_pad`; it is outside this route and B10 already records that `U` does not bound its `u_L`.)

### 6.3 The exact next missing lemma

**Lemma needed to revive the route:** *an explicit length-five highest-weight polynomial `G in Sym^d(Sym^3 C^5)` vanishing on all 3x3-determinantal quinary cubics, in a degree `d` at which a five-row full-H source can be carried* (the programme reached rank 2 of `s = 5` at `d = 5`; `s` is in the hundreds at `d = 6` and grows fast). Equivalently: `delta_0 <= d_carry`. Everything on the record points the other way: `delta_0 >= 8` given the measured totals, `delta_0 = 65` conjectured, and the only known equations cost 65 (Jacobian cap) and 80 (discriminant). Should such a `G` exist at some `d`, the route's first cells are `lambda = mu + (horizontal d-strip)` with `mu` the type of `G`, and the certified image bound there is `u_L <= T - 1` at least; the gap would then additionally require `rho_L >= s - delta_L + 1 + (m_pad - r)` on a source of dimension `s(d, lambda)`, which is the unpriced and, at `d >= 8`, unaffordable part.

**Secondary lemma (to make the negative unconditional through `d = 7`):** direct rank certificates for the 80 ambient units left at `delta = 7` by batch-13, restricted to the length-5 weights among them. This is bounded exact linear algebra in the cubic-coefficient ring (weight spaces of a few thousand columns), not a carrier construction; it was outside this session's cap and outside its scope.

### 6.4 What would falsify this negative

- A nonzero `i_3(d, mu)` for some `d <= 7` and length-5 `mu`: this would contradict a batch-13 certificate (`d <= 6`) or the measured total-deficit identity (`d = 7`). The bounded test is: take a cubic-coefficient highest-weight vector of type `mu` and degree `d`, evaluate it at one integer 3x3 pencil `det(sum x_k M_k)`; a nonzero value confirms `i_3 = 0` for that vector, and only an exact zero on a certified basis of the `mu`-highest-weight space refutes the negative. At `d = 6` this is 16 single evaluations; none is needed because the certificates exist.
- A proof that `delta_L > sum_mu i_3` in some cell would contradict Proposition 2.3; the proposition's proof is four lines and was checked twice.
- A cell where `u_L < m_pad` at `d <= 6` would require `I(Y_L)_d != I(Y_pad)_d`, i.e. `m^*(h) in Sym^d V (x) I(D_5)_d` for some `h notin I(Y_pad)`; with `I(D_5)_d = 0` this is impossible.

### 6.5 One recommendation, and its price

Do not pursue the 1+3 restriction bound further in any degree the programme can carry; retire it as a gap route with this negative on file. If the programme wants a target-side sharpening of the padding ceiling at all, the object to study is not the 1+3 locus but `delta_0` itself, and the batch-13 open Question `q:delta0` (the first covariant vanishing on cubics singular at a projective frame) is the right formulation. A structural attack that this session prices as cheap but did not run: test whether the degree-65 Jacobian-cap minors already have a **lower-degree factor or syzygy** by evaluating the rank drop `65 -> 64` of `M_4(F)` at an explicit six-nodal pencil and inspecting which `65 x 65` minors vanish identically versus generically; a common factor of degree `< 65` vanishing on `D_5` would lower `delta_0` and would be the first non-minor equation of `D_5`. Expected output: either a degree below 65 for `delta_0` or evidence that the cap is sharp. Falsification: a minor with no common factor beyond units. This is a det3 computation in 35 variables, not a five-row carrier, and it does not by itself produce a five-row gap.

## 7. Claim ledger

| # | Claim | Label | Where |
|---|---|---|---|
| L1 | `Y_pad = m(V^* x Sym^3 V^*)` and `Y_L = m(V^* x D_5)` are closed; `Y_L` is the closed image of the 1+3 locus; no boundary description of `D_5` is used | PROVED | 2.1 |
| L2 | `m^*` is `GL_5`-equivariant of bidegree `(1,1)` in the ordinary-coefficient convention | PROVED (equivariance written out) | Lemma 2.1 |
| L3 | `C[Y_pad] = m^*(P) subset Pi`, `C[Y_L] = nu(P) subset Pi_L`, `C[Y_L]` a quotient of `C[Y_pad]` | PROVED | Lemma 2.2 |
| L4 | `T_L = sum_mu m_3(d,mu) = T - sum_mu i_3(d,mu)`; length reduction for `D_5`; `I(D_5)` concentrated at length 5 | PROVED here (two-line truncation argument) / ADOPTED (B17-03 Lemma 1, batch-13 `prop:lengthred`, `d5_ideal.md` section 3) | 2.3 |
| L5 | `delta_L = m_pad - u_L = mult_lambda[(R_pad)_d ∩ (Sym^d V (x) I(D_5)_d)]`, with `max(0, sum i_3 - (T - m_pad)) <= delta_L <= sum_mu i_3` | PROVED | Prop. 2.3 |
| L6 | `u_L <= min(a, m_pad, T - sum_mu i_3)` | PROVED | Cor. 2.4 |
| L7 | If `I(D_5)_d = 0` then `u_L = m_pad` for all `lambda` and the 1+3 bound is `>= m_pad >= r` for all `rho_L` | PROVED | Cor. 2.5 |
| L8 | `rho_L <= min(s, sum_mu s_3(d,mu))`; gap needs `rho_L > s - delta_L + (m_pad - r)` | PROVED | 2.4 |
| L9 | `I(D_5)_d = 0` for `d <= 5` | PRODUCER-CERTIFIED (batch-13 rank-attains-`a` certificates, two primes; not replayed) | 3.2 |
| L10 | `I(D_5)_6 = 0` | PRODUCER-CERTIFIED per weight: the three uncertified batch-13 ambient units at `delta = 6` are the length-6 weights with `N_S = 4028, 4456, 3988` (C2), so all 16 length-5 weights carry certificates | 5.2 (c) |
| L11 | `I(D_5)_7 = 0` | MEASURED (batch-13 total-deficit identity; 80 uncertified ambient units of unknown length) | 3.2 |
| L12 | `I(D_5)_65 != 0` (Jacobian cap, length-5 types); `disc in I(D_5)_80` | PROVED in batch-13 paper (Kleiman, Dimca cited); ADOPTED | 3.1 |
| L13 | `delta_0 = 65` | CONJECTURED (batch-13) | 3.2 |
| L14 | `a_3(5,mu)`, `a_3(6,mu)` for all `mu`, with dimension controls; the 3 + 16 length-5 constituents | MEASURED here (exact integer arithmetic, controls pass) | 5.2 (a) |
| L15 | Census `padding_source_raw` over-counts 34 cells at `d = 6` (length-6 `mu` leak through `horizontal()`); `padding_ceiling U` unaffected in all 105 cells | MEASURED here + cause read in the census script | 5.2 (b) |
| L16 | Pieri range of `(8,4,4,4,4)` is `{(6,4,4,4): 1, (5,4,4,4,1): 0, (4,4,4,4,2): 0}`; the cell is excluded by H5 (B.9) and inert for the route | ADOPTED (B.9) + MEASURED | 4, 5.2 (d) |
| L17 | Inert-cell lists at `d = 5, 6`; `lambda_1 <= d` is a sufficient condition for inertness | MEASURED here / PROVED (sufficiency) | 5.2 (e) |
| L18 | In every five-row cell with `d <= 6` the 1+3 restriction bound cannot certify a gap; the same for `d = 7` given the totals and for `d < delta_0` | PROVED given L7, L9, L10, L11 | 6.2 |
| L19 | Any explicit low-degree length-5 equation of `D_5` would be needed to revive the route; none is known below 65 | PROVED (necessity, from L5) / NOT REACHED (existence) | 6.3 |
| L20 | The 2+2 locus is outside this route; its image is not inside `Y_pad` | ADOPTED (B10), stated for scope only | 6.2 |

Nothing here bounds `m_det` below `m_pad` anywhere, produces an `r`, or nominates a cell. The separate session's `(5,(4^5))` sparse-evaluator work was neither read nor touched.

## 8. Resource receipt and honest negatives

- Total measured wall time of the two checks: about 0.5 s of the 120 s allowed (two checks, 60 s each); peak Job Object memory 19.4 MB and 12.9 MB against 512 MiB; both exit 0; `job_object_enforced: true` in both receipts. No `ulimit` is relied on. The B15-02 `.venv` Python 3.12.10 was used, through `work/batch15_workers/B15-02/analysis/b15_bound.py` unchanged (hash in `MANIFEST.json`).
- Not replayed: any batch-13 rank certificate; the batch-13 total-deficit identity; the census's `a, s, g` values (inherited; their `T` is recomputed here and found over-counted at `d = 6` without effect on `U`).
- Not reached: `rho_L` in any cell (no full-H source was built or evaluated; the negative makes it irrelevant for `d <= 6`); `delta_0`; any equation of `D_5` below degree 65.
- The statement `I(D_5)_7 = 0` remains conditional on batch-13's measured totals; the negative is unconditional through `d = 6` and conditional at `d = 7`.
- The local clock crossed midnight during the session; the directory keeps its `20260916` name as assigned.
