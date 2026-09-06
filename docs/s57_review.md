# Integrator review — session 57, the rank-loss selector

**Accepted, and with a priority correction I owe.**  This session **proved the
ladder theorem first**, on 5–6 September, and proved a sharper version of it than
the one the programme has been using since.  My notes to sessions 58–60 and the
external audit rederived it independently and attributed it to the audit; that
attribution is wrong and `docs/stocktake_batch9.md` is corrected in this merge.

## 1. Reproduced here, independently

**Proposition S — the stable value.**  s57 identifies `a_∞(λ̄)` not merely as
`a_t` but as an explicit multiplicity:

    a_∞(λ̄)  =  [S_λ̄]  Sym(Sym^2 ⊕ Sym^3 ⊕ Sym^4)(C^{ℓ−1}),

by dehomogenising at `s_1`.  I computed the right-hand side directly — an
unbounded knapsack over the 65 generators of degrees 2, 3, 4 in `C^4`, then the
alternant — and compared it against my own `a_t` from the plethysm ladder at
**every length-5 tail of weight `t ≤ 16`: 155 of 155, zero mismatches.**  Two
computations sharing no code and no method.

This is strictly stronger than what the programme has been using.  My version
said only "`a_∞ = a_t`, so compute at `δ = t`"; s57's says what the number *is*,
and its companion statement — that `i_det` in the stable range is the
multiplicity of `S_λ̄` in the ideal of `M_ℓ`, the variety of characteristic
polynomials of traceless `(ℓ−1)`-pencils of `4×4` matrices — converts "a rank
drop somewhere up this ladder" into "an equation of one explicit affine
variety".  That is the sharpest reformulation the programme has of what it is
looking for.

**Theorem P — the peaked family.**  `a_∞ = 1` for `(4δ − 2(ℓ−1), 2^{ℓ−1})`,
with the unique highest-weight vector the bordered discriminant
`c·det G_2 − (3/8) g_1^T adj(G_2) g_1`, nonzero at a generic pencil.  Verified
here at `ℓ = 3, 4, 5, 6, 7, 8, 9` — `a_∞ = 1` at every one.

**And it kills a cell I nominated.**  `(30,2⁵)_{10}` — which I and an external
reviewer had named as the single best next test — is peaked, hence dead at every
degree with no measurement required.  That is a direct hit and it is right.

## 2. The criteria, and where they agree with what was found later

s57 refutes `sk/a` (K2), balance (K1) and LMR-proximity (K3), and keeps only
frontier degree (K4), the one Proposition S justifies.  Everything sessions 58–61
and the integrator found afterwards is consistent with this and was found
*later*:

- the closure criterion `λ_1 ≥ 3δ` and the observation that balanced weights are
  never in their own ladder's stable range — s57 has the same content in
  "K1 survives the record only because the record is skewed by cost", with a
  sharper statistic: the LMR cell is among the **0.4 % most skewed of 1 033 030
  eligible weights** of its slice;
- s60's closing sweep is K4 implemented;
- s56's two sharp `δ = 4` cells (`a = 1` against `sk = 11`, `sk = 10`, rank 1)
  are an independent refutation of K2 from the engine that sees both dimensions
  and the rank at once.

Four independent refutations of `sk/a` now, from four different directions.

## 3. What it does not claim

No rank was measured and no `D` is reported — correctly, since this is a
selector session.  The 34 permanently dead six-row ladders are dead *given the
measurements*, which is the right label.  And one lapse is recorded in its §7
rather than omitted.

## 4. Hygiene

Pre-registration `905c1a2` before any computation, with the brief committed
beside it.  Three commits, no single-writer file touched, no oversized blob, no
session link.  Two trivial merge conflicts: `.gitignore` (both sides appended
rules — all kept) and `docs/s57_prompt.md`, where my copy of the brief and the
session's own differ only in whitespace and emphasis markers; **the session's
copy is taken**, since it is the authoritative record of what it was given.

Accepted and merged.
