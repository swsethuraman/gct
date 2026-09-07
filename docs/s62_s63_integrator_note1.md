# Integrator note 1 to sessions 62 and 63 — the S2 memo, with one correction accepted and one sharpened

## 1. The correction is to me, and it is right

I wrote, in the batch-10 planning and in session 62's brief, that the room-one
scalar is a ratio of consecutive-degree Gram determinants:

    s  =  det G_{a_δ} / det G_{a_{δ−1}}          ← WRONG

S2 corrects this: the denominator is the **current-degree** Gram restricted to
the transported predecessor, not the predecessor's own Gram,

    s  =  det B_{λ,δ} / det A_{λ,δ} ,     A_{λ,δ} = B_{λ,δ} |_{J(M_{δ−1})}

because first-row transport `J` is injective (Lemma L) but **has never been
shown to be an isometry** for the determinant target inner product.  There is no
reason it should be: `J` preserves independence, not norms.

Verified here on an explicit small instance (`analysis/wk10_int_schur.py`, exact
rationals, a `12 × 5` map with a distinguished 4-dimensional transported
subspace):

    s = c − bᵀA⁻¹b            = 35574830688 / 194332817
        det B / det A         = 35574830688 / 194332817     agree
        ‖(I − P)T(v)‖²        = 35574830688 / 194332817     agree
        det B / det G_prev    = 71149661376 /  41215007     DOES NOT agree

So all three of S2's formulations coincide and mine does not.  **The mechanism
is untouched** — `s = c − bᵀA⁻¹b`, `s = 0 ⟺ the last-born line dies` — and the
distance form `s = ‖(I − P)T(v)‖²` is a genuine improvement: it makes the
content obvious (the squared norm of the part of the new line's image that
escapes the transported image) and it shows `s ≥ 0` with equality exactly at
dependence.

**What this costs is the speculation, not the mathematics.**  My "ratio of two
Gram determinants, one per degree" gloss was what made a product formula look
plausible.  A Schur complement *within one degree* is a weaker invitation.
Session 62 should drop that framing and keep the mechanism.

## 2. The C2 reduction is correct — and it is safe modulo a prime

S2's reduction for the LMR cell: form `A_24 = B_{λ,24}|_{J(M_23)}`, a `273 × 273`
Gram block, and show it is nonsingular.  Then

    det A_24 ≠ 0  ⟹  rank Θ_24 ≥ 273        and   LMR gives  rank Θ_24 ≤ 273
                  ⟹  rank = 273,  i_det(24) = 1

Correct, and it never touches `δ = 23` as a separate measurement.  **Sharpening
that S2 did not state, and it matters operationally:** this step needs no
characteristic-zero Gram identity at all.  The direction used is the trivial one,

    rank(MᵀM) ≤ rank(M)      in every characteristic,

so `det A_24 ≢ 0 (mod p)` already gives `det A_24 ≠ 0` over `Z`, hence
`rank_Q A_24 = 273`, hence `rank_Q Θ_24 ≥ 273`.  Reduction is a ring
homomorphism, so **the entries may be computed modulo `p` from the start and the
determinant taken there too.**  Note 1 to session 64 and session 62's brief both
say the Gram route is characteristic-zero only; that remains true of a claimed
rank *drop* (`s = 0`), and is **not** true of this nonsingularity step.  Run it
at both house primes.

## 3. But the cost has moved, not vanished — and one number decides it

The reduction removes the 48 825-dimensional target and the `δ = 23`
measurement.  It does not remove the wall; it relocates it into the entries.
Writing each source vector in the Foulkes basis, `w_i = Σ_P c^i_P · P`,

    A_ij = Σ_{P,Q} c^i_P c^j_Q · β(type(P,Q)) ,      A = C_S ᵀ β_S C_S

where `S` is the **union of the supports of the 273 transported source
vectors**.  Cost is about `273·|S|² + 273²·|S|`.  So:

    |S| ≈ 10³   →  ~3 × 10⁸     comfortable
    |S| ≈ 10⁴   →  ~3 × 10¹⁰    heavy but possible
    |S| ≈ 10⁵   →  ~3 × 10¹²    out of reach

**`|S|` is the single number that decides session 63**, and it is exactly what
session 62 task 1 was told to measure.  The two sessions are correctly coupled:
session 63 should read session 62's cost curve before choosing a route, and
should report `|S|` at `r = 9` as its own first deliverable whichever route it
takes.  Do not report "C2 reduces to one 273 × 273 determinant" without `|S|`
beside it — the determinant is trivial; the entries are the session.

## 4. The centrality falsifier — accept, and here is the cheapest instance

S2 is right that multiplicity 2 does not decide whether `β_4` is central: the
centre of `Q²³ ⊕ Mat_2(Q)^{⊕5}` is 28-dimensional, and `β_4` could lie in it
with all five `2×2` blocks scalar.  Worth settling, and one non-scalar block
settles it.

The cheapest instance is **`λ = (12,4)` at `δ = 4`**, and it is much cheaper than
the other four: it has length 2, so the ambient is `Sym⁴(Sym⁴ C²)` with
`dim Sym⁴C² = 5` and `dim Sym⁴(Sym⁴C²) = 70`, and `a = 2`.  A two-dimensional
multiplicity space inside seventy dimensions.  Two further remarks:

- `λ_1 = 12 = 3δ`, so `(12,4)` sits **exactly on the stable-range boundary**
  `λ_1 ≥ 3δ` — its tail is `(4)` with `t = 4 = δ`.  So the same block doubles as
  a stable-range check on Proposition S, and is worth handing to S1 as well.
- Prior: Gram blocks are generically non-scalar, so expect noncentral.  If so,
  matrix-valued blocks are unavoidable in general — but note this is **not
  load-bearing for the LMR route**, because at a room-one cell the Schur
  complement is a scalar whether or not the surrounding algebra is commutative.
  Run the check for what it says about the general theory, not as a gate.

## 5. Unchanged

Session 56's `β = K ∘ K` remains the origin of the orbital observation.  The
`δ ≤ 4` orbital counts and `Σ_λ a_λ² = #orbitals` (3, 9, 43) stand.  The `n = 3`
LMR cell remains the mandatory positive control, and it is the only place where
`s = 0` will ever have been observed before LMR itself.
