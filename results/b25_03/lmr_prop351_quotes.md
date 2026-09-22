# LMR arXiv:1004.4802v1: the passages B25-03 read and quoted (UNCOMMITTED)

Read by B25-03 on 2026-09-21. Fetch started at 03:39:04 UTC. The files were
fetched fresh in this session, not taken from tool memory or earlier
sessions.

| object | URL | SHA-256 | bytes |
|---|---|---|---|
| PDF v1 | `https://arxiv.org/pdf/1004.4802v1` | `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79` | 180 675 |
| ar5iv rendering (text read) | `https://ar5iv.labs.arxiv.org/html/1004.4802` | `fb5844ada6bec339638b584bcf385686935e96e03aa8f0ab9e2561bb0b316e05` | 382 135 |
| arXiv abstract page | `https://arxiv.org/abs/1004.4802` | `dc097e58fa7eeed4adc1f7869a5a737e1b8b0de6ccfb6f0f315fe0042ca473d6` | 39 416 |
| tag-stripped text (derived by B25-03; `sed`/`tr`, annotation elements removed) | — | `96c668bf63e16dad43751731eac105d508cbb9a870b49e2d77775a70912e3333` | 683 lines |

- **All three fetched digests equal the record.** The PDF digest equals the
  one in B24-02b `results/b24_02b/lmr_quotes.md` at `5a97317e` and in B23-06
  `results/b23_06/MANIFEST.json` at `feed104e`, as SOURCE_INDEX states. The
  ar5iv and abstract-page digests equal B24-02b §1.
- **The version is unambiguous.** The abstract page lists only `[v1]`, so the
  ar5iv text and the hashed PDF are the same version.
- **The PDF itself was hashed, not rendered**, because no PDF text tool is on
  this host. The text was read from the ar5iv rendering.
- **The derived text file differs from B24-02b's `b772b08c…`.** The
  tag-stripping recipe is different, and no claim rests on the derived file.
- **The abstract page carries no journal-ref.** The CMH 88 (2013) 469–484
  metadata in the paper's `\bibitem{LMR}` is therefore not verified here.

Notation below is transcribed from the tag-stripped ar5iv text, with zero-width
characters removed and `^`/`_` added. Line numbers refer to the derived text.

---

## L1. §1, the paragraph pointing to Prop. 3.5.1 (lines 110–115)

> While it was generally understood that `End(M_n(C))·[det_n] ⊂ closure(GL_{n²}·[det_n])` was a
> proper inclusion, it had not been known if the difference was potentially significant.
> Proposition 3.5.1 exhibits an explicit codimension one `GL_{n²}(C)`-orbit that is contained in
> the boundary of `closure(GL_{n²}·[det_n])` but not contained in `End(C^{n²})·det_n`, at least
> when `n` is odd.

## L2. §3.5 "On the boundary of the orbit of the determinant": the construction (lines 478–486)

> Decompose a matrix `M` into its symmetric and skew-symmetric parts `S` and `A`. Define a
> polynomial `P_Λ ∈ S^n(M_n(C))*` by letting
> `P_Λ(M) = det_n(A,…,A,S)`.
> This is easily seen to be zero for `n` even so we suppose `n` to be odd.
> More explicitly, `P_Λ` can be expressed as follows. Let `Pf_i(A)` denote the Pfaffian of the
> skew-symmetric matrix, of even size, obtained from `A` by suppressing its `i`-th row and column.
> Then
> `P_Λ(M) = Σ_{i,j} s_{ij} Pf_i(A) Pf_j(A)`.

## L3. Proposition 3.5.1 (lines 487–490)

> **Proposition 3.5.1.** The polynomial `P_Λ` belongs to the orbit closure of the determinant.
> Moreover, `closure(GL(W)·P_Λ)` is an irreducible codimension one component of the boundary of
> `closure(GL(W)·[det_n])`, not contained in `End(W)·[det_n]`. In particular
> `dc̄(P_{Λ,m}) = m < dc(P_{Λ,m})`.

## L4. Proof, the steps that carry the weight (lines 491–516, excerpted)

> The first assertion is clear: for `t ≠ 0`, one can define an invertible endomorphism `u_t` of
> `M_n(C)` by `u_t(A+S) = A+tS` […] Since the determinant of a skew-symmetric matrix of odd size
> vanishes, `(u_t·det_n)(M) = det_n(A+tS) = n t det_n(A,…,A,S) + O(t²)`, and therefore
> `u_t·[det_n]` converges to `[P_Λ]` when `t` goes to zero.
>
> […] Then one can check that the modules `E_A, E_S, E_AS, E_SA` are not contained in the
> stabilizer, and that the contribution of the remaining terms is isomorphic with `gl_n ⊕ gl_n`.
> In particular it has dimension `2n²`, which is one more than the dimension of the stabilizer of
> `[det_n]`. This implies `closure(GL(W)·P_Λ)` has codimension one in `closure(GL(W)·[det_n])`.
> Since it is not contained in the orbit of the determinant, it must be an irreducible component
> of its boundary. Since the zero set is not a cone […], `P_Λ` cannot be in `End(W)·det_n` which
> consists of `GL(W)·det_n` plus cones. ∎

**Limit of the reading.** The stabiliser step is asserted ("one can check").
B25-03 did not audit it. The label is PRIMARY at the level of the statement
and the construction, and does not mean the proof was re-derived. The same
standard is used in B24-02b §0.

## L5. §1, Theorem 1.0.1 and the surrounding sentences (lines 55–57, 71, 77–78)

> The best known lower bound is `dc(perm_m) ≥ m²/2`, which was proved in [3].
>
> The best known lower bound on this function had been linear.
>
> **Theorem 1.0.1.** `dc̄(perm_m) ≥ m²/2`.

Reference [3] (line 592–595): "Thierry Mignon and Nicolas Ressayre, A quadratic bound for the
determinant and permanent problem, Int. Math. Res. Not. (2004), no. 79, 4241–4253."
