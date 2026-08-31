# Pre-registration — session 25: the ambient cap, backwards and forwards

Written **before** any computation of this session.  Branch `s25-race`,
2026-08-31.

**Clone state.**  `origin/main` is at **`3dfd524`** ("Correct the expected tip
in both briefs, and point them at the screen").  The brief expects `a3df8ba`;
`a3df8ba` is an *ancestor* of `3dfd524` and the single commit between them is a
correction to the briefs themselves, so this is a benign fast-forward, not a
rollback.  `c9240f3` and `ad9502f` are both present.  Sessions 24 and 24b are
merged (`61e748e`), which resolves the sync alarm raised in
`docs/session_24b.md` §0.

## 0. Definitions fixed in advance

`a(lam, delta)` = multiplicity of `S_lam` in the ambient
`Sym^delta(Sym^d C^N)` (`d = 4, N = 2` for World A; `d = n, N = n^2` for the
determinant world).  Both closure rings are quotients of the ambient, so
`mult_det <= a`, `mult_per <= a`, `D = mult_per - mult_det <= a`.

For the audit of session 24's 742 zeros I will report a **trichotomy**, not a
dichotomy, because the brief's "genuine" bucket silently contains two very
different things:

* **forced** — `a = 0`; both closure counts are 0 by ambient arithmetic;
* **empty** — `a >= 1` but `mult_A = mult_B = 0` anyway; the cancellation is
  real but between two absences;
* **substantive** — `a >= 1` and `mult_A = mult_B >= 1`.

Only the third bucket could ever have supported a "saturation law".

**A precision the brief elides, recorded now so I do not quietly inherit it.**
`m_det < a` does **not** hand over an obstruction.  It gives
`mult_det <= m_det < a` and leaves `mult_per <= a` — room, not a lower bound.
An obstruction still needs `mult_per > mult_det`, i.e. an upper bound on
`def_per`.  What `m_det < a` buys is that the determinant side is capped below
the ambient by group theory alone, so the deficit has to work on one side only.
I will call such a weight **half-free**, not free, throughout.

## 1. Pre-registered predictions

**S1 — the forced fraction of the 742.**  I predict **55%** forced (`a = 0`),
with a stated range of **40–70%**.  Reasoning: `a = 0` *guarantees* `D = 0`, so
`a = 0` cells are heavily over-represented among the zeros even though only
~12% of World A weights have `a = 0`; but World A's ambient is rich and the
`Gam`/`tau`/`Q` pairs contribute many genuine both-zero cells at `a >= 1`.
*Falsifier:* a measured forced fraction outside 40–70%.

**S2 — the sharper version, which I think is the real finding.**  I predict
**at least 90% of the 742 fall in `forced` ∪ `empty`**, i.e. have
`mult_A = mult_B = 0`, and that the `substantive` bucket is **under 5%**.
If so, the saturation-law hypothesis should be retired on the honest ground —
not that the ambient forced it, but that there was almost never anything
present at either weight to saturate.
*Falsifier:* `substantive` at or above 10% of the 742.

**S3 — direction of `m_det / a` in `n`.**  I agree with the integrator: the
ratio **falls** with `n`, measured as `sum m_det / sum a` over the ambient
support (`a >= 1`) at fixed `delta`.  Reasoning: the mean of `m_det` over its
own support is flat at 1.00 in `n` (`docs/easy_counts.md`), while the ambient
in `n^2` variables gets strictly richer.  *Falsifier:* the ratio rising from
`n = 3` to `n = 4`, or from `n = 4` to `n = 5`, at any fixed `delta` I reach.

**S4 — will any weight have `m_det < a` at `n = 4` or `5`?**  I predict
**no**, in every range I can reach (I expect `delta <= 4` at `n = 4` and
`delta <= 3` at `n = 5`).  But I also predict that it **must happen
eventually**, for a reason worth stating in advance:

    sum_lam a(lam,delta) dim S_lam  =  dim Sym^delta(Sym^n C^{n^2})  ~  delta^{D-1},
    sum_lam m_det(lam)  dim S_lam                                    ~  delta^{d-1},
    D = binom(n^2+n-1, n)  >>  d = n^4 - 2n^2 + 2 = dim closure(det_n).

The ambient grows in a vastly larger dimension than the orbit, so `a` must
exceed `m_det` on a growing fraction of weights.  The race is therefore not
"can the cap be beaten" but "at what `delta`, and does larger `n` bring it
forward".  I predict the first `m_det < a` occurs at a weight with `a >= 2`
and `m_det = 1` — because `m_det` is essentially a 0/1 indicator (mean 1.00
over its support) — hence not before `delta = 5` at `n = 3`.
*Falsifier for the "no":* any weight with `m_det < a`.  Per the brief's kill
criteria I will stop and report it immediately.

**S5 — `delta = 2` is a structural tie, everywhere.**  `Sym^2(Sym^n)` is
multiplicity-free, so `a = 1` on its support; the first partials of `det_n` are
linearly independent, so no quadric contains the orbit closure, the degree-2
part of the ideal is zero, `mult_det = a = 1`, and `def >= 0` forces
`m_det >= 1 = a`.  I predict `m_det = a = 1` exactly on the ambient support at
`delta = 2` for every `n` computed, i.e. a tie and never a win.
*Falsifier:* `m_det != 1` at any `delta = 2` ambient-support weight.

**S6 — the paper audit.**  I predict `def_det((2,2,2), 2) = 1` is **100%
forced** (its weight has `a = 0`), and that the forced fraction of the total
determinant deficit is **high but falling** across `delta = 2, 3, 4` — I
predict above 80% at every one of the three.  *Falsifier:* any of the three
below 80%, or the `delta = 2` value not being 100%.

**S7 — the `easy_counts.md` claim about BIP.**  `docs/easy_counts.md` says the
34 live weights at `(n,delta) = (5,2)` with `m_det = 0 < m_per` are "exactly
the weights where BIP forces `def_per = m_per`".  I predict **most of them have
`a = 0`**, so that `def_per = m_per` there is ambient arithmetic and BIP is not
needed — meaning that sentence overstates what the data shows and should be
corrected.  *Falsifier:* most of the 34 having `a >= 1`.

## 2. What I expect the verdict to be

That the ambient cap is a real and previously unapplied constraint which
retires the saturation law, but retires it for the *plainer* reason S2 names —
almost nothing was present at those weights — rather than the sharper reason
the brief proposes; that `m_det / a` falls with `n` as the integrator expects;
that no half-free weight appears in reachable range; and that the no-go should
be written as a statement about the **rate** at which `a` overtakes `m_det`,
not as a claim that it never does, because the dimension count in S4 says it
must.

## 3. Discipline

Exact arithmetic only.  Every reported number by two independent routes.
`scripts/ambient_screen.py` is a **cross-check, never an input**: my own
Murnaghan–Nakayama, Kronecker and plethysm routines are written first, and any
disagreement with the screen is reported before anything else.
