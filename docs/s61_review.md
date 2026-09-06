# Integrator review — session 61, the polar profile of `per_3`

**Accepted.  The headline is reproduced end to end by my own code, and it is
the first time this programme has separated the padded permanent from the
determinant by a statistic that is not the dual defect.**  Two corrections to
the record are owed by me, not by the session, and they are §1.  Two repairs to
the report's own text are §5.

Everything below was computed here before this was written, with my own random
data, my own scripts (`/root/work/s61v/`), and — for the first time in this
programme — a real computer algebra system.  See §7.

## 1. The correction I owe

`docs/external_reviews_round3.md` §3 and `docs/critic_gemini_scorecard_response.md`
§3 record the two Sheshadri preprints as unlocatable after several searches, and
`critic_gemini_scorecard_response.md` states a rule: *the conormal session does
not launch until the preprint is located and read.*

**Both preprints exist.**  The session located them; I have now confirmed it
myself by fetching `arxiv.org/html/2606.13628`, which returns the title
("A near-quadratic lower bound on the border determinantal complexity of
`Σ_i x_i^n` via conormal specialization"), the author (Karthik Sheshadri), the
abstract, Lemma 15 and Theorem 3.  The `arxiv.org/abs/` path returns an empty
document through the fetch tool; the `html` path and the search index do not.
My six attempts all used `abs`.  **This was a tooling false negative and the
finding was mine, not the session's.**  The failure mode is recorded here for
future citation checks: *if `arxiv.org/abs/<id>` comes back empty, try
`arxiv.org/html/<id>` before concluding the identifier is invalid.*

The rule's *conclusion* was still right and was followed: the session's
mathematics does not depend on either paper, and §4 of the report proves the one
statement it needs.  What was wrong was the factual premise.  Both files are
corrected in this merge.

## 2. Reproduced — the profiles

Method: my own implementation of the section count.  For `X = {F = 0} ⊂ P^N` and
slot `k`, a random integer `(k+2) × (N+1)` matrix gives `Λ ≅ P^{k+1}`; `G = F|_Λ`;
`k` random combinations `m_j` of the restricted partials; `I = (G, m_1, …, m_k)`
saturated by the restricted Jacobian ideal (and, separately, by one random
combination `g` of the partials).  Singular 4.3.2, `p = 2147483647` and
`2147483629`, seeds of my own choosing.  Full-Jacobian and single-`g`
saturation agreed at every slot where both were run.

| object | slots | measured here | report |
|---|---|---|---|
| `det_4`, 16 vars | 0–7 | **4, 12, 36, 68, 84, 60, 20, 0** | same |
| `det_3`, 9 vars (control) | 0–7 | **3, 6, 12, 12, 6, 0, 0, 0** | same |
| `per_3`, 9 vars, `p = 2147483647` | 0–7 | **3, 6, 12, 24, 48, 48, 30, 6** | same |
| `per_3`, `p = 2147483629`, other seed | 6, 7 | **30, 6** | same |
| dual sextic `X*`, 9 vars | 0–6 | **6, 30, 48, 48, 24, 12, 6** | same (biduality) |
| `x_0·per_3`, 10 vars, third seed | 5, 6 | **48, 30** | same |
| **`x_0·per_3` as a quartic in 16 vars** | 0–8 | **4, 6, 12, 24, 48, 48, 30, 6, 0** | same |
| `ℓ·c`, 10 vars (control) | 0–6 | **4, 6, 12, 24, 48, 96, 192** | same |
| smooth quartic in `P^7` (control) | 0–3 | **4, 12, 36, 108** `= 4·3^k` | — |

The dual sextic's profile is `per_3`'s read backwards at every slot computed,
which is biduality checked slot for slot, and the sixteen-variable padded
quartic — the object the containment question is actually about — was measured
directly at **all nine** slots rather than inferred from the cone lemma.

**The headline stands: `δ_6(x_0·per_3) = 30 > 20 = δ_6(det_4)`, and
`δ_7 = 6 > 0`.**

Independently, the smooth-Segre closed form.  For `P^r × P^r ⊂ P^{(r+1)²−1}`
with `c(T) = (1+a)^{r+1}(1+b)^{r+1}`, the polar degrees
`μ_k = Σ_{j≤k} (−1)^j C(m−j+1, k−j) ∫ c_j h^{m−j}` give, reversed:

    det_2  (2, 2, 2)                       sum 6
    det_3  (3, 6, 12, 12, 6)                sum 39
    det_4  (4, 12, 36, 68, 84, 60, 20)      sum 284
    det_5  (5, 20, 80, 220, 430, 580, 520, 280, 70)   sum 2205

matching the report's calibration and the four generic Euclidean-distance
degrees.  `Σ δ_k(per_3) = 177` likewise.

## 3. Reproduced — the closed-form facts, exactly over `Q`

- **`Sing(per_3)`**: projective dimension 2, degree 24, **15** minimal primes,
  every one of dimension 2, degrees `1⁶ 2⁹`, Jacobian ideal not radical.  The
  degree is forced by hand: `{two rows = 0}` is a `P²` (6 of them, degree 1);
  `{row i = 0, col j = 0}` is a `P³` because the shared entry makes 5
  independent conditions, and the complementary `2×2` permanent cuts a quadric
  surface (9 of them, degree 2); `6·1 + 9·2 = 24`.
- **Hessian ranks**: 9 at a generic point of `{per_3 = 0}` — so the Gauss map is
  generically immersive and `dim X* = 7`, which is what makes `X*` a
  hypersurface; 6 on the fifteen components; 4 on the 18 lines
  `{two rows = 0, one column = 0}` and at the coordinate points.  Each such line
  lies on exactly three components, as the report says: `{rows i,j = 0}` and the
  two quadrics `(i,k)`, `(j,k)`.
- **The dual.**  `g = 4·per(B∘B) − 2·per(B)² − det(B)²` expands to exactly 21
  terms, one for each `3×3` non-negative integer matrix of row and column sums
  `(2,2,2)` — the Birkhoff count `H_3(2) = 21` — with coefficient `+1` on the six
  `2P_σ`, `−2` on the nine `P_σ + P_τ` with `σ^{−1}τ` a transposition, and `−6`
  on the six `J − P_σ` (which are the six remaining pairs, `σ^{−1}τ` a 3-cycle).
  Exactly the report's sorting.
- **`g(∇per_3(A)) ≡ 0 mod per_3(A)`** over `Q`: verified, quotient of degree 9,
  not divisible a second time.
- **`g` is irreducible over `Q`** — Singular's `factorize` and sympy's
  `factor_list` both return a single factor of multiplicity 1.  This is stronger
  than the report's route (squarefree, plus a smooth plane section, hence
  irreducible) and shortens the argument: `X* ⊆ {g = 0}` is an inclusion of
  irreducible 7-folds, hence an equality, hence `deg X* = 6 = δ_7`.
- **`Sing{g = 0}`**: projective dimension **5**, degree **51**.  Codimension 3,
  so a generic `P²` misses it, so the generic plane section of `X*` is a smooth
  plane sextic and `δ_6(per_3) = δ_1(X*) = 6·5 = 30`.  **This is the decisive
  number and it is a theorem, not a measurement.**
- Arithmetic: `4·27 − 2·20 = 68`; `4·81 + 20(2·5 − 2 − 5·4) = 84`;
  `3·2⁵ − 2·24 = 48` and `6·5² − 2·51 = 48` (the two sides of slot 5);
  `4·3⁶ = 2916`; `729 + 6·972 = 6561 = 3⁸`.
- **`B(m,n) = Σ_{i=1}^{n−1} C(m,i) C(m−1,n−1−i) C(n−2,i−1)`**: `B(4,9) = 0`,
  `B(5,9) = 315`, `B(6,9) = 5355`.  So Theorem 3(i) fed with `δ_7(per_3) = 6`
  gives `dc̄ ≥ 5` and stops there, exactly as the report says.

## 4. The two rigour points raised in review, answered

**(a) "Flatness over the curve needs care."**  It does not need repair, only
restating.  `𝒞` is the *scheme-theoretic closure* in `P^15 × P^15* × Δ` of a
subscheme of `P^15 × P^15* × (Δ∖{0})`.  Over a smooth curve, flat is equivalent
to torsion-free over `O_Δ`, and a scheme-theoretic closure is torsion-free by
construction.  So flatness is automatic and the report's phrase "no component
lies over `t = 0`" is the informal shadow of the correct statement, which is
about associated points, not components.  Conservation of the numbers then
follows because `h` and `ȟ` are pulled back from the ambient factors and the
specialisation homomorphism on cycle classes commutes with proper pushforward
(Fulton §10.1).  **No gap.**

**(b) "Is `Z_6 = {F : δ_6 ≤ 20}` really Zariski closed?"**  The right answer is
that *the obstruction does not need it*.  The argument is: if
`x_0·per_3 ∈ closure(GL_16·det_4)`, curve selection gives a curve
`g(t)·det_4 → x_0·per_3`, and the specialisation inequality applied to that one
curve gives `δ_6 ≤ 20`, contradicting 30.  Global closedness is a description of
the locus, not a step in the proof, and the report should not have asserted it
without argument.  For the record, it is probably true on the reduced locus and
here is the route: `δ_k` is a constructible function of `F` (generic flatness
plus Noetherian induction on the universal family of reduced hypersurfaces), and
the specialisation inequality holds for *any* one-parameter degeneration with
reduced special fibre — nothing in §4's proof used that `X_t` was a determinant —
so `{δ_k ≤ c}` is constructible and stable under specialisation, hence closed.
The non-reduced locus needs a convention before the statement is even
well-posed.  **Downgrade the claim to "closed on the reduced locus, by an
argument not given here", or drop it.**

## 5. Two repairs to the report

**(i) The independence counterexamples in §5 are not quartics.**  To show
`Z_6 ⊄ Z_7` the report offers "a cone over a quadric of `P^8`", which has
`δ_6 = 2 ≤ 20` and `δ_7 = 2 > 0` — correct, but it is a quadric, and both
conditions are conditions on `Sym^4 C^16`.  A **product of two general
quadrics** repairs it: a smooth quadric in `P^N` has `δ_k = deg = 2` at every
slot (the Gauss map is linear, so `ȟ` pulls back to `h`), profiles add over a
reduced union, so the quartic `Q_1 Q_2` has `δ_k ≡ 4`, giving `δ_6 = 4 ≤ 20` and
`δ_7 = 4 > 0`.  Measured here in 10 variables: slots 5–8 all return 4, and the
single smooth quadric returns 2 at slots 0, 3, 6, 7.  The other counterexample —
a cone over a smooth quartic of `P^7`, `δ_7 = 0` and `δ_6 = 4·3⁶ = 2916 > 20` —
**is** a quartic and stands.  So the incomparability conclusion survives; only
the first witness needed replacing.

**(ii) The `det_m`, `m ≥ 5` comparison silently changes the object.**  Padding
`per_3` to degree 5 gives `x_0²·per_3`, which is *not reduced*.  The polar
profile of the reduced hypersurface underneath it is the same vector
`(4, 6, 12, 24, 48, 48, 30, 6, 0, …)` — which is why the report's comparison
against `det_5` is numerically right — but the specialisation argument of §4
then delivers `C(X_0^red) ⊆ 𝒞_0` only for the components on which `∇F_0 ≠ 0`,
i.e. it loses the hyperplane's `(1, 0, …, 0)`.  Harmless (slots 1–7 are
untouched, and those carry the whole comparison), but the report should say that
the object being compared at `m ≥ 5` is the reduced hypersurface, not the
quintic.

## 6. What the finding is worth — a scale reading

The report says the slot-6 margin is 10, and calls it a margin.  Put it on the
scale of the statistic and it reads the other way.  A generic quartic in `P^15`
has `δ_6 = 4·3⁶ = 2916`.  The padded permanent has 30.  The determinant has 20.

    generic 2916   ·······································   pad 30   det 4→20

Both points sit at the very bottom of the range; the separation is 10 parts in
2916.  The padded permanent is *already* almost as dual-degenerate as the
determinant, and slot 6 detects the last step.  This is the same shape as s55's
finding that the padded permanent lies in `Dual_{7,4,10}` and not
`Dual_{6,4,10}` — "the margin is one step" — now seen with a numerical
invariant instead of a dimension.  It is also, I think, the honest explanation
of §6's negative estimate: an equation family that separates two points this
close, in a statistic whose generic value is three orders of magnitude away, has
no reason to be cheap.

The crossing structure is worth recording as a fact about the determinant.  The
determinant's profile is *generic* (`4·3^k`) through slot 2 and first drops at
slot 3 (68 against 108); the padded permanent drops at slot 1 already (6 against
12).  So through slot 5 the padded permanent is the more degenerate of the two,
and only at the top two slots does the order reverse.  The programme's recurring
two-family taxonomy — excess-singularity statistics separate the wrong way,
dual-degeneracy statistics the right way — is visible inside a single eight-entry
vector.  That is the cleanest illustration of it we have.

Against `det_5` every slot of the padded permanent is dominated, so the reach of
the whole profile is `dc̄(per_3) ≥ 5` and nothing more.  I agree with the
report's own verdict on this, and with its refusal to promise an algebraisation.

## 7. Engine note — the CAS constraint is lifted

`docs/s50_s55_integrator_notes.md` records that no computer algebra system was
available to the integrator, which was the binding constraint on the border
track.  **It is available now**: `Singular 4.3.2` and `msolve 0.6.5` — the exact
versions this session used — install from the distribution repositories in about
a minute, and `Macaulay2 1.22` is packaged as well.  Every number in §2 and §3
was computed with them.  Gröbner, saturation, `radical`, `minAssGTZ` and
`multidegree`-style work are all now available for verification, and the s59
special-fibre computation that the Rees track needs is no longer blocked on
tooling.  **This should be recorded in the next batch's briefs.**

One engine pitfall found here and worth writing down, because it fails silently:
in Singular, `std(sat(I, P)[1])` written inline returns a **wrong ideal** — it
gave `dim 1, deg 2` where the answer is `dim 0, deg 6` — while
`list L = sat(I, P); std(L[1])` is correct.  No error is raised.  Anyone
re-running polar counts should bind the saturation result to a named `list`
first.  The session's own scripts do not have this defect; I introduced it, and
it cost the first pass of every number in §2.

## 8. Verdict

Accepted and merged.  The pre-registration is committed 21:19, the first
computation 23:13, the report 00:30 — the order holds.  No single-writer file is
touched, no blob exceeds the limit, no commit carries a session link, all three
carry `Co-Authored-By`.  The scorecard's three refutations are honestly marked,
including the one against me.

What I would carry forward, in order:

1. The slot-6 inequality is banked as a second, independent certificate that
   `x_0·per_3 ∉ closure(GL_16·det_4)`.  It is not a stronger bound and the
   report says so.
2. The one open question worth a bounded session is the **structure of the
   slot-6 locus** — whether `deg X* ≤ 20` on the dual-defective locus has
   equations below degree 24.  §6's estimate is against it; §6 is also honest
   that the estimate is not evidence for a floor.  I would not run it before the
   Foulkes engine is calibrated, because the rank question at
   `Θ⁺ : C²⁷⁴ → C^{sk}` is where the programme's expected value now is.
3. `docs/external_reviews_round3.md` and `docs/critic_gemini_scorecard_response.md`
   are corrected in this merge.  The rule they state — a session's mathematics
   must not depend on an unread citation — was right and stays.
