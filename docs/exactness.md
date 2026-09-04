# The normalisation bound is not exact when it fires: `mult_red((15,12,6,1,1,1), 9) = 18 < 19 = h_pad`

Session 47 (2026-09-04), branch `s47-exactness`, clone tip `9aa6a9c` (clone check
passes; all eight required files present).  Pre-registration
`results/PREREG_s47.md`, committed `3984bbd` **before any measurement**.  Work
list `results/s47_todo.md`; ledger `results/s47_ledger.md`; the surviving free
bound `results/s47_units.md`; permanent weights `results/s47_per6_d8.md`; code
`analysis/wk9_s47_*.py`; certificate `results/s42_certs/15_12_6_1_1_1_d9.txt`.
Labels: **proved** / **measured** / **adopted-from-literature** / **expectation**.

*Flag: the brief's required reading lists `docs/s43_review.md`, which is not in
this clone.  Its §2 content is present in `results/sixrow_record.md` and
`docs/sixrow_close.md` §3 and those were read instead.  Nothing else is missing.*

## 0. Verdict

> **The conjecture is false.**  At `λ = (15,12,6,1,1,1)`, `δ = 9`, `ℓ = 6`:
> `a = 21`, `h_pad = 19` — so the bound fires — and `mult_red = 18`.  The
> normalisation bound is **not** attained.  This is the first cell the session
> measured.
>
> **The certificate.**  `a = 21` by two independent routes and `h_pad = 19` by
> **three** (symmetric-function plethysm, Weyl alternation, and a multiset DP
> written for this session that shares no code with either).  `mult_red ≥ 18`
> from `nullity_p(E_red) = 3` at both house primes; `mult_red ≤ 18` from **three
> independent integer highest-weight vectors** in `I(R_6)_9`, obtained by CRT and
> rational reconstruction over both primes (identical pivot columns, max
> coefficient 15360), verified `E_red v = 0` **over `Z`** against all 59,775
> uncompressed raising-operator rows, with the (★) criterion of
> `docs/reducible_ideal.md` asserted on all **240,282** monomials of their
> supports for both constrained indices.  So `mult_red = 18` exactly, `18 < 19`,
> and no part of the verdict rests on a cached number or on a single prime.
>
> **A correction to the evidence the conjecture rested on.**  At `h_pad = 0`
> exactness is a *theorem* of Corollary B2, not a conjecture: `mult_red ≤ 0`
> forces equality with no computation.  Of the 411 firing cells at `δ = 7, 8`,
> **140 are of that kind**; of the 62 at `δ = 9`, 22; and of session 42's eight
> banked firing cells, four.  The conjecture's real support was **seven cells**,
> five of them `ℓ = 6`, `δ = 8`, in one family — not the twelve the headline
> suggested.  This was pre-registered (`results/PREREG_s47.md` §0) before the
> counterexample was found.
>
> **What survives, and it is not nothing.**  `mult_red ≤ h_pad` is still proved
> (Corollary B2), so `units := a − mult_red ≥ a − h_pad` at **every** cell of the
> region, reachable or not, in milliseconds.  That free *lower bound* on the
> pad-side units — the thing the programme actually wants at unreachable cells —
> is untouched by the refutation; only the claim that it is an equality is gone.
> `results/s47_units.md` tabulates it at all 311 cells with `0 < h_pad < a`.
>
> **A regularity proposed, tested, and withdrawn — in that order.**  Write
> `d := min(a, h_pad) − mult_red` for the rank deficit of `μ_λ` and
> `e := h_pad − a`.  Across the 268 cells of the record where all three numbers
> are known, `d > 0` at eight, `d = 1` at every one, and at every one `e` was
> **even** with `|e| ≤ 4` — nine of nine including the counterexample, in a band
> that splits 52 even to 50 odd, with the parity of `e` a coin flip across the
> census (1155 odd to 1122 even over 2277 cells) and uncorrelated with `ℓ`, `δ`,
> `λ_1` and six other invariants.  It looked like a real discriminant.  **It is
> not.**  Two cells later `(16,10,7,1,1,1)_9` (`e = −1`, odd) and
> `(15,11,7,1,1,1)_9` (`e = −3`, odd) both fail, and the first of them fails by
> `d = 3`, so "`d = 1` always" is gone too.  The pattern is recorded here because
> it was proposed on the record and killed by this session's own measurements,
> not because it survived.  **There is no known statistic that separates the
> cells where `μ_λ` has maximal rank from those where it does not** — the same
> conclusion session 43 reached about *where* the bites are, one level up.

## 1. The conjecture, and what it really says

`h_pad(λ, δ) = mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V)` is the multiplicity in the
normalisation of `C[R_r]` (Theorem B1 of `docs/reducible_engine.md`
= Kadish–Landsberg Prop. 1.8), so `mult_red ≤ h_pad` always (Corollary B2), and
`h_pad` is a Pieri sum over a cubic plethysm — milliseconds at any cell.  The
conjecture under test:

> **(Exactness.)**  Whenever `h_pad(λ, δ) < a(λ, δ)`, `mult_red(λ, δ) = h_pad(λ, δ)`.

**The restatement that makes it legible (proved; pre-registered).**
`C[R_r]_δ = im(μ*_δ)` for the generalised Foulkes–Howe map
`μ*_δ : Sym^δ Sym^4 V → Sym^δ V ⊗ Sym^δ Sym^3 V` (KL Thm 1.7), which is
`GL(V)`-equivariant, hence in each isotypic component a map of multiplicity
spaces

        μ_λ :  C^{a(λ,δ)}  ⟶  C^{h_pad(λ,δ)},        mult_red(λ, δ) = rank μ_λ.

So `mult_red ≤ min(a, h_pad)` is Corollary B2 together with the trivial bound,
and the conjecture is exactly:

> **`μ_λ` is surjective whenever `h_pad < a`** — that is, `μ_λ` has *maximal
> rank* on the firing set.

Stated that way the conjecture was already in trouble before any measurement,
because the companion statement is known false: at eight measured cells `μ_λ`
drops rank below `min(a, h_pad)`, every one of them with the bound silent
(`h_pad ≥ a`).  The pre-registration set the prior at **0.40** on exactly this
ground and named the most exposed cells — large `a`, small gap, `ℓ = 6`,
`δ = 9`, in-family.  `(15,12,6,1,1,1)_9` is in that description.

## 2. The counterexample

| | value | how |
|---|---|---|
| `λ`, `δ`, `ℓ` | `(15,12,6,1,1,1)`, 9, 6 | in the `(λ_1,λ_2,λ_3,1,1,1)` family of session 43 |
| `a` | **21** | plethysm (`wk8_s30_pleth`) and Weyl alternation (`wk9_s42_census`) agree |
| `h_pad` | **19** | three routes agree (§0); 39 Pieri strips |
| `n_χ`, `n_red`, `nnz_red` | 21451, 20323, 222487 | `wk9_s42_redengine` build, 17 s |
| `nullity_p(E_red)` | **3** at `p = 2147483647` and `p = 2147483629` | sparse Wiedemann certificates |
| `mult_red` | **18** | `≥ 18` from the primes, `≤ 18` from three exhibited integer HWVs |
| `d = min(a,h_pad) − mult_red` | **1** | the bound is missed by exactly one |
| `e = h_pad − a` | **−2** | even, consistent with the pattern of §4 |

`mult_red = 18 ≤ 19 = h_pad`, so **Corollary B2 is not violated** and this is not
the brief's stopping rule 1 (a bug); it is stopping rule 2, and the
pre-registered sweep halted at once.

The three vectors are in `results/s42_certs/15_12_6_1_1_1_d9.txt` in the
χ-coordinates of the red orbits, with the orbit list in the header, so a reader
can re-run the (★) test and the `E_red v = 0` test on them without rebuilding
anything (`analysis/wk9_s47_starcheck.py` does exactly that, from the file).

**What it means for `I(R_6)`.**  `a − mult_red = 3`: the weight
`(15,12,6,1,1,1)` carries **three** independent reducibility equations in
degree 9, where the normalisation bound could only prove two.  It is the largest
unit count at any single cell in the record, and the first cell where a bite is
strictly deeper than the normalisation can see.

## 3. Phase A as left

The pre-registered sweep stopped at its first cell.  A **post-refutation** sweep
was then run under `--continue` — a different question (the failure *rate*, not
the binary), and labelled as such — over cells stratified by the parity of the
gap `a − h_pad`, the discriminant the pattern of §4 proposes.  See
`results/s47_ledger.md` for the full table.

