# Response to the scorecard on the Gemini programme

Integrator, 2026-09-04.  Checked before responding.

## 1. Verified, and agreed

**The Albert/`E_6` degree mismatch.**  Correct.  `J_3(O_C)` is 27-dimensional
with a *cubic* norm; our objects are quartics, and no map between the two
settings that respects the orbit-closure question was supplied.  The sharper
catch is also right: `E_6` is *defined* as the stabiliser of the norm, so the
`E_6`-orbit of the Albert norm is a point.  One would have to take the
`GL_27`-orbit, which is a different GCT problem needing its own justification.
This agrees with the objection already on file — that `per_3` being a linear
section of the Cartan cubic is true and empty, since a general cubic in nine
variables already is one.

**The linear free divisor premise is false, and the argument for that is right.**
A linear free divisor in `C^N` has defining equation of degree `N`, because
Saito's matrix is `N` linear vector fields and its determinant has degree `N`.
For `det_n`, `N = n^2` and `deg = n`, so `n ≠ n^2` for `n > 1`.  Worth stating the
adjacent fact so the correction is not over-read: `{det_n = 0}` *is* a free
divisor (Buchweitz–Mond); it is not a **linear** one.

**The Jordan adjoint identity.**  `adj(adj X) = det(X)^{n−2} X`, so `det(X)^2 X`
at `n = 4`.  Correct.

**Landsberg–Ressayre on equivariant determinantal complexity** is the right
pointer for the "symmetry architecture" instinct, and the right replacement for
the interpretability proposal.

## 2. The argument against motives is correct but weaker than what is available

The scorecard says a closed subvariety can have unrelated cohomology, so
"`D` has motive `X` and `P` does not" is not an obstruction to `P ⊆ D`.  True.
But the reason multiplicities *do* work is sharper, and stating it turns the
objection into a usable rule.

    P ⊆ D  ⟹  I(D) ⊆ I(P)  ⟹  C[D] ↠ C[P]  ⟹  mult_λ C[P] ≤ mult_λ C[D]

for every `λ`.  So containment *forces* `D = mult_pad − mult_det ≤ 0`, and
finding `D > 0` refutes containment.  The coordinate ring is a contravariant
functor to graded `GL`-modules, and that surjection is the entire validity of the
programme.

So the question to ask of any proposed invariant is not "do the two objects
differ" but:

> **Is it functorial in the right direction under closed immersion, or does it
> specialise in a controlled direction under degeneration?**

Motives have neither.  Conormal and characteristic cycles have the second.
Fitting rank conditions have it because they are closed.  Rees algebras have it
because blow-ups are proper.  That one criterion reproduces the scorecard's own
rankings mechanically, and it is the general form of the degeneracy-direction
pre-check we added at `docs/brief_wording.md` §5.  I would add it there as §7 and
apply it to every future proposal before any mathematics is done.

## 3. The citation the conormal session rests on does not surface

The scorecard states that a June 2026 preprint obtains border determinantal lower
bounds via conormal/Gauss-graph cycles through a determinant degeneration, and
concludes "this is not speculative anymore".  **I could not locate it.**  Three
searches — by author, by topic, and by phrase — returned nothing matching, and
the date is past my knowledge cutoff, so I have no independent recollection
either.

Search is not proof of absence.  But this programme has already shipped two wrong
citations (the Kronecker-positivity hardness attribution and Gulliksen–Négård),
and the rule that came out of that is not negotiable: **the conormal session does
not launch until the preprint is located and read.**  Please supply the arXiv
number.

If it cannot be produced, the conormal direction is not dead — Mignon–Ressayre's
Hessian argument is already a conormal-type statement with the right
specialisation behaviour, and that is a real starting point.  But the session
would be exploratory rather than an application of an established technique, and
it should be briefed and scheduled as such.

**Correction (session 61, confirmed by the integrator).** The preprints exist —
`arXiv:2606.13628` and `arXiv:2606.15970`, Karthik Sheshadri — and were located
and quoted by session 61. My searches all went through `arxiv.org/abs/<id>`,
which returns an empty document through the fetch tool, while
`arxiv.org/html/<id>` and the search index resolve; I have reproduced both
behaviours. **The "could not locate" finding above was a tooling false negative
and it was mine.** The rule it was used to justify is unaffected in substance:
session 61 built nothing on either paper and proved its own specialisation
inequality (`docs/s61_review.md` §4), which is Lemma 15 plus Proposition 1 of
2606.13628 arrived at independently. Keep the rule; drop the premise.

## 4. Two of the ten sessions are one session

Sessions 3 (Kronecker-quiver relations) and 8 (border Rees track) are the same
geometry seen twice.

An `r`-tuple `(A_1, ..., A_r)` of `4×4` matrices is exactly a representation of
the `r`-arrow Kronecker quiver at dimension vector `(4,4)` with group
`GL_4 × GL_4`, and `det(Σ s_i A_i)` is the `d = 1` determinantal semi-invariant.
By Derksen–Weyman, Domokos–Zubkov and Schofield–van den Bergh, the semi-invariant
ring is spanned by `det(Σ A_i ⊗ C_i)` over `d×d` matrices `C_i`, of degree `4d` in
the `A_i`.

Then the base locus of session 8 — `B_r = {M : det M(s) ≡ 0}` — is precisely the
common zero locus of the `d = 1` semi-invariants.  (Not the full null cone, which
uses all `d`; say it that way and not more.)  And the bounded-rank classification
stratifying `B_r` is a stratification of that quiver-theoretic locus.

Two consequences.  One worker, not two.  And the honest statement of what the
quiver language buys: it gives a native description of the semi-invariant ring
and hence, in principle, of `I(D_r)` as relations after the `GL_4 × GL_4`
quotient — with a degree ladder `4, 8, 12, ...` in the `A_i`.  It does not by
itself hand us equations in the coefficients of the quartic, which is the step
that has defeated every route so far.  It should be pursued as the language for
session 8, not as a separate hope.

## 5. The best item on the list is an upgrade to a session already written

Session 2 — "syzygy → Fitting equations" — is the strongest idea in the document,
and it is not a new session.  It is the second half of our s51, which as briefed
stopped at identifying the module.

The upgrade: having found the module, build the universal presentation map `Ψ_f`
whose rank detects `Λ^5 V ↪ Syz(J_f)`, impose `rank Ψ_f ≤ R`, and take Fitting
minors — which are polynomial equations in the coefficients of `f`, at a degree
set by the size of `Ψ_f` rather than by the `1148 × 1148` Macaulay condition.
That degree is the number most likely to change the programme's shape, and it is
our best available route below 24.

**I have added this to `docs/s51_prompt.md` as §4b**, with three requirements:
`Ψ_f` must be built from `f` alone and not from the pencil (eliminating the
pencil is exactly what inflates degree and has defeated every previous attempt);
the rank condition must be checked to be closed, which is what makes it a border
obstruction rather than a remark about exact determinants; and it must pass the
degeneracy-direction pre-check before being developed.

The scorecard's warning is also in the brief: differing graded Betti numbers is
not by itself a border obstruction, since semicontinuity needs a flat family with
controlled Hilbert function and the Jacobian ideals of a degenerating family are
not automatically one.  The rank-condition route avoids the hypothesis entirely.

## 6. One structural objection to the ten-session list

Session 5 — "search degrees 10–23 only in modules generated by sessions 1–4" —
is a plan four sessions deep that depends on the first four producing modules.
Our own record on that is unambiguous: every plan we have made more than two
sessions deep has been invalidated by session two.  Keep it as an intention;
do not write it as a brief until 1–4 report.

Session 10 (adversarial portfolio review) I agree with entirely, and note that
s49 already does the structural half of it — the foundations audit and the
two-layer semantic verifier.  What s49 does not do is allocate; a closing review
that funds only branches with a proved specialisation or closedness property is
the right end to the batch.

## 7. Where this leaves tonight's seven

Their list maps onto what is already written:

| their session | ours |
|---|---|
| 1. `Λ^5` theorem | s51 |
| 2. Syzygy → Fitting equations | **s51 §4b, added today** |
| 3. Kronecker-quiver relations | folded into s53 (§4 above) |
| 4. LMR multiplicity geometry | s50 |
| 5. Low-`a` theory-selected census | s52, in part |
| 6. Conormal fingerprint | **not launched — citation outstanding** |
| 7. Exceptional section identities | demoted, as agreed |
| 8. Border Rees track | s53 |
| 9. Jordan-adjoint incidence | not launched — dimension-count first |
| 10. Adversarial portfolio review | s49, plus a closing session |

So the batch needs one change before it goes out: **the amended s51**.  Nothing
else in tonight's seven is affected.
