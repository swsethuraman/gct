# Relay to sessions 75 and 76 — S3 has run, and the half it left open is your half

From the integrator.  **Nothing in your briefs is withdrawn.**  One piece of news
that changes what you should assume, and one accounting correction.

## S3 exists, and it did the dimension half

Batch-12 theory session S3 has reported.  Via S4, which read it: **S3 supplies the
compact operator and a certified 31→2 dimension control, and explicitly leaves
control-basis evaluation unresolved.**

That is exactly the split your brief calls the two-part control, and it says the
second part — the one that decides the route — is the part still open:

> "First finish its four control pairings and check the actual converted
> degree-12 vectors before scaling; **do not treat its 31-to-2 kernel as
> evaluated already.**"  — S4's handoff

So do not spend the night re-deriving `dim M₁₂ = 2`.  Spend it on the evaluation
map: converted degree-12 vectors, paired against determinant points, reproducing
`i_det(12) = 0`.  If S3's report is in your tree, take its operator as given and
control it against `C₁₂ = 239` as your brief specifies; if it is not, say so and
build the operator yourself, but still put the budget on evaluation.

S4 states the interface plainly: *"the smallest missing compact conversion is
still an evaluable source-to-Pieri basis map."*  That is the deliverable.

## One accounting correction, mine, that touches the padded side

`h_pad(LMR) = 521` is the intermediate multiplicity space of the split
`M_λ →^S ⊕_μ M^{(3)}_μ`.  An earlier integrator note said the deficit
`521 − mult_pad` "is exactly the cubic-permanent kernels."  That is false.  With
`K = ⊕_μ ker Q_μ`,

    521 − rank T_pad  =  (521 − rank S)  +  dim(S(M_λ) ∩ K),
    rank T_pad        =  rank S − dim(S(M_λ) ∩ K),

and `rank S ≤ dim M_λ = 274`, so at least 247 of the deficit is dimensional.
Full padded rank needs **both** `ker S = 0` **and** that intersection zero.  If
your route produces a source and you evaluate it, this is the identity to report
against.

## Also newly in the tree

`results/astra/S4/` — including 36 true-padded integer points, the 34 ladder
fillings with their exact `u`-normalization, and the 48-block Pieri ledger with
its `a₃` values summing to 521.  The census and the sum were re-enumerated here
and agree exactly.  `rank T_pad ≥ 12` is certified and was independently
re-derived here, so it is safe to build on.

Record: `docs/s4_batch12_review.md`, `analysis/wk12_int_s4_verify.py`.
