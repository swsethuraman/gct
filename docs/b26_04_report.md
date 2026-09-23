# B26-04 — the quartic sixteen-to-nine transfer: certificate

**Slot:** B26-04 (reading and hand derivation, no pilots). **Worktree:** `work/batch15_workers/B15-01`,
branch `b15-01-ci159`. **HEAD:** `2688efd1b5b14c78c11a9855e83357f4516cba54`. This is exactly the expected
B25-05 delivery, not a descendant. **Status: UNCOMMITTED / PRODUCER ONLY** until B26-10 reviews it.
Paper 2 keeps its flag until then. **Git was read-only.** Nothing was staged, committed or reset.
**Zero pilots, zero mathematical programs, no lease.**

**Registered outcome: the self-contained short certificate.** Paper 2's `D9` (`\Ddet_9`) is exactly
Lemma R's pencil closure `X_9` for `f = det_4`, `N = 16`, `r = 9`. Each of R1–R6 holds at
`(d, N, r) = (4, 16, 9)` for `λ = (65,17,2^7)`, `δ = 24`, and each is checked below directly at degree 4,
not by analogy with `n = 3`. The weight conventions at Paper 2's point of use agree with Lemma R's.
**Achievement level:** this is a transfer lemma for the determinant-side ideal copy, which Paper 2 needs
for `i_det ≥ 1` at the goal cell. It is **not** a source condition or a coefficient equation in its own
right, and it gives no separation on padding, no positive multiplicity gap and no asymptotic bound. The
binding constraint is unchanged: "No five-row determinant equation is known to be nonzero on padding."

---

## 0. Preflight (incremental record)

| check | observed | result |
|---|---|---|
| UTC start | `2026-09-22T23:43:11Z` | — |
| `B26_COMMON.md` raw SHA-256 | `a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd` | equals the `LAUNCH_PROTOCOL_B26.md` adoption table |
| `B26-04.md` raw SHA-256 | `871039894a901644ef90f8033aa8d561c4840625661daa48335e682d71160c1e` | equals the adoption table |
| `BATCH26_LIVE_LEDGER.md` raw SHA-256 (in `post_b19_housekeeping_20260917\`) | `9d24c37c5953c66583f199af3e8fc226e4feb9f7c70d412f2d4424594b47d2c8` | recorded only; no expected value given |
| `LAUNCH_PROTOCOL_B26.md` raw SHA-256 (read for context) | `2681f57275935d1e0e8bb8b566dcb21599b4d84f0f63db206ed7bd962a0a24fc` | recorded only |
| branch | `b15-01-ci159` | matches |
| HEAD | `2688efd1b5b14c78c11a9855e83357f4516cba54` | matches exactly |
| `git status --porcelain` | 10 383 entries, all untracked (`??`) under `results/logs/`, `results/b15_01/cache/`, `results/b15_01/verification_cache/`, `results/b18_01/literature/`. No modified tracked file | left alone |
| output paths `docs/b26_04_report.md`, `results/b26_04/` | absent before writing | no collision |
| `AGENTS.md` / `CLAUDE.md` (worktree and project root) | none present | — |

## 1. Inputs, with the bytes each hash names

Every hash below is SHA-256 of `git show <commit>:<path>` output, which is the **committed blob content**.
The CR column counts carriage returns in that blob.

| input | commit:path | git blob | sha256 (blob content) | bytes | CR | bytes named |
|---|---|---|---|---|---|---|
| B25-05 report (Lemma R) | `2688efd1:docs/b25_05_report.md` | `844e13f6…` | `38834c316c1b182e…` | 25 204 | 0 | LF blob; equals the brief's `38834c31…` |
| B25-05 manifest | `2688efd1:results/b25_05/MANIFEST.json` | `96c88c81…` | `035ef6ead2033e64…` | 5 304 | 0 | LF blob; equals the brief's `035ef6ea…` |
| B25-10 review | `42e7f4ba:docs/b25_10_review.md` | `e29797e6…` | `0488ce1e90a6cd08…` | 40 991 | 0 | LF blob. The brief gives no hash |
| Paper 2 | `79b68dcf:paper/det4-onset.tex` | `60bc18a4…` | `065f8799dbec4b24b0ddd93b2cd1fdf8528d435c4464bcc529700010f08f55d8` | 71 849 | 1 247 (every one of 1 247 lines) | **CRLF blob.** `.gitattributes` at `79b68dcf` has `paper/det4-onset.tex -text whitespace=cr-at-eol`, so the blob is the raw CRLF bytes, as the brief says. This differs from B25-10's `39d15aea…`, which pins an earlier Paper 2 state before B25-02's edits |
| `isotypic_rank.md` (s26 Lemmas 1–4, Prop. 5) | `82633a60:docs/isotypic_rank.md` | `4b204683…` | `5f33e38e72be947a…` | 19 013 | 0 | LF blob; blob id equals B25-05 §A.5's `4b204683…` |
| s73 report §1 | `82633a60:docs/s73_report.md` | `de79c8dc…` | `f40783ba4dd5489d…` | 28 206 | 0 | LF blob; equals B25-05's `f40783ba…` |
| B17-03 report (quartic Lemmas 1–2) | `0cce6172:docs/b17_03_report.md` | `856a9fe9…` | `bcb38b5f2682f69c…` | 20 187 | 0 | LF blob; blob id equals B25-05's `856a9fe9…` |

Full hashes are in `results/b26_04/MANIFEST.json` under `inputs`. `79b68dcf` is not an ancestor of this
worktree's HEAD. It resolves through the shared object database, as `B26_COMMON.md` says. Quotations
from Paper 2 below are CR-stripped for display only. Line numbers refer to the blob.

## 2. What Paper 2 says (READ, `79b68dcf:paper/det4-onset.tex`)

**Definition of `D_r`** (lines 112–117, with `\Ddet = D^{\det}`):

> The two players become, inside `\Sym^{4}\bC^{r}`,
> `\Ddet_r=\overline{\{\det_4(s_1A_1+\dots+s_rA_r):A_i\in M_4\}}`

**The length reduction** (lines 251–261, `\label{eq:lengthred}`):

> the length reduction (`\cite[Prop.~4.19]{Companion}` for `\det_3`; the proof uses only that `\lambda`
> has `r` rows and applies verbatim to `\det_4` and to `x_0\per_3`) identifies
> `\mult_\lambda\bC[\cO]_\delta=\mult_{S_\lambda(\bC^r)}\bC[\cO|_{\bC^r}]_\delta`, where `\cO|_{\bC^r}` is
> the restricted variety. For `\cO=\overline{\GL_{16}\cdot\det_4}` this is `\Ddet_r`; …

**The flagged sentence** (lines 1058–1063):

> at `n=d=4`, `k=6`, `N=16` this is the weight `48\omega_1+15\omega_2+2\omega_9=(65,17,2^{7})` in degree
> `24`, and the length reduction `\eqref{eq:lengthred}` carries the copy from sixteen variables to
> `\Ddet_9`. That transfer is the `n=4` analogue of the premise `(\star)` of the `n=3` control above: the
> `n=3` case is proved; the `n=4` case is not yet checked, so this transfer is flagged, not established.

There is only one flag site. A grep for `flag`, `not yet checked`, `(\star)`, `lengthred` and
`Prop.~4.19` finds the transfer flagged only at lines 1061–1063. Lines 705, 860 and 888 use
`eq:lengthred` at lengths `≤ 5` and `≤ 4`, which is outside this slot.

**Locator note.** B25-10 §2.4 refers to "Paper 2's `D_9` in eq. (2.1)". In the blob, `D_r` is defined in
the unnumbered introduction display (line 114). The numbered equation in §2 is `eq:lengthred`, and
lines 260–261 identify its restricted variety with `D_r`. The content B25-10 names is the same. I did not
compile the paper, so I have not confirmed the printed number "(2.1)".

## 3. The identification `D9 = X_9` (hand derivation on READ text)

Lemma R's object (B25-05 §A.3, READ) is `X_r = closure Φ_f(Hom(C^r, C^N))` with `Φ_f(T) = f∘T`.

- Take `V_16 = M_4(C)`, `N = 16`, `f = det_4 ∈ Sym^4 V_16^*`, `r = 9`.
- A linear map `T : C^9 → M_4` is exactly a tuple `(A_1, …, A_9) ∈ M_4^9` with `T(s) = Σ s_i A_i`, and
  every tuple occurs, dependent ones included. Hence
  `Φ_{det_4}(T)(s) = det_4(s_1A_1 + … + s_9A_9)`.
- So `X_9 = closure{det_4(Σ_{i≤9} s_i A_i) : A_i ∈ M_4}`, which is Paper 2's line-114 set at `r = 9`,
  with the same closure and the same unrestricted `A_i ∈ M_4`.
- The choice of linear isomorphism `M_4 ≅ C^16` does not matter. Two choices differ by an element of
  `GL_16`, so `GL_16·det_4` and every restriction statement below are unchanged.
- Paper 2's "restricted variety" `\cO|_{\bC^r}` for `\cO = closure(GL_16·det_4)` is
  `closure ρ(\cO) = closure ρ(GL_16·det_4)`. Here `ρ(\cO) ⊆ closure ρ(orbit)` because `ρ` is continuous
  and the orbit is dense in `\cO`. By R4 below this equals `X_9`. B17-03 Lemma 2, eq. (6)–(7) (READ,
  `0cce6172`), states the same identity for quartics at `N = 16` and general `r`. I re-derived it rather
  than relying on B17-03's acceptance status.

**Conclusion: Paper 2's `D9` is exactly the `det_4` pencil closure that the length-restriction argument
needs at `(4, 16, 9)`.**

## 4. R1–R6 at `(d, N, r) = (4, 16, 9)`, step by step

The fixed data are: `W_N = Sym^4 (C^N)^*`, `(g·F)(v) = F(g^{-1}v)` and `(g·h)(F) = h(g^{-1}·F)`.
`c_α(F)` is the coefficient of `y^α`, with `|α| = 4`. `ρ : W_16 → W_9` restricts forms to
`L = ⟨e_1..e_9⟩`, and `ρ^* : C[W_9] ↪ C[W_16]` is `c_α ↦ c_{(α,0^7)}`. The cell is
`λ = (65,17,2^7)`, `ℓ(λ) = 9`, `δ = 24`, `|λ| = 65 + 17 + 14 = 96 = 4·24`.

**Weights and raising operators at degree 4 (hand derivation).**
- For a torus element `t`, `(t·c_α)(F) = c_α(t^{-1}·F)`. Since `(t^{-1}·F)(y) = F(ty)`, the coefficient
  of `y^α` is multiplied by `t^α`. So `wt(c_α) = α`, with all entries `≥ 0`.
- For `g = exp(xE_ij)` with `i ≠ j`, `(g^{-1}·F)(y) = F(y + x y_j e_i) + O(x²)`. The first-order term is
  `y_j ∂_i F`. The coefficient of `y^α` in `y_j ∂_i y^β` is nonzero only for `β = α + e_i − e_j`, which
  needs `α_j ≥ 1`. It equals `β_i = α_i + 1`.
- So `E_ij c_α = (α_i+1) c_{α+e_i−e_j}` if `α_j ≥ 1`, and `0` if `α_j = 0`, extended as a derivation.
- Nothing here uses `|α| = 3`. This agrees with B17-03 (3), which is stated for quartics (READ).

**(R1) Weight support. Holds (hand derivation).** A monomial `Π_{k=1}^{24} c_{α^(k)}` has weight
`Σ_k α^(k)`, and every entry is `≥ 0`. At weight `(65,17,2^7,0^7)`, coordinates 10–16 are 0, so every
factor has `supp α^(k) ⊆ [9]`. The weight space of `C[W_16]_24` at `(λ,0^7)` is therefore
`ρ^*` of the weight-`λ` space of `C[W_9]_24`. `ρ^*` is injective because it includes a polynomial
subring. Degree 4 enters only through `|α| = 4`, which plays no role.

**(R2) Raising operators. Holds (hand derivation).**
- For `1 ≤ i ≤ 8`, the formula for `E_{i,i+1}` involves only indices `i, i+1 ≤ 9`, and
  `α + e_i − e_{i+1}` stays supported in `[9]`. So `E_{i,i+1}∘ρ^* = ρ^*∘E^{(9)}_{i,i+1}`.
- For `9 ≤ i ≤ 15`, every `c_α` in the image has `α_{i+1} = 0` because `i + 1 ≥ 10`. So
  `E_{i,i+1} c_α = 0`, and as a derivation `E_{i,i+1}` kills the whole image.
- Hence `H^{16}_{24,(λ,0^7)} = ρ^* H^9_{24,λ}`, and `a_16 = a_9`. The boundary `ℓ(λ) = 9 = r` plays no
  special role, because R1 needs only `λ_j = 0` for `j > 9`.

**(R3) Restriction identity. Holds (hand derivation).** `(ρF)(s) = F(Σ_{i≤9} s_i e_i)`, so the coefficient
of `s^α` in `ρF` is the coefficient of `y^{(α,0^7)}` in `F`, i.e. `c_α(ρF) = c_{(α,0)}(F)`. Therefore
`(ρ^*h̄)(F) = h̄(ρF)` for every `F ∈ W_16`.

**(R4) The image of the orbit. Holds (hand derivation).**
- For `g ∈ GL_16`, `ρ(g·det_4)(s) = det_4(g^{-1} Σ_{i≤9} s_i e_i) = det_4(Σ s_i A_i)`, where
  `A_i := g^{-1}e_i ∈ M_4` are the first nine columns of `g^{-1}`.
- As `g` runs over `GL_16`, `(A_1..A_9)` runs over exactly the linearly independent 9-tuples in
  `C^16`. Any such tuple extends to a basis because **`r = 9 ≤ 16 = N`**; this is where that
  inequality is used.
- These tuples form a nonempty Zariski-open subset of the irreducible affine space
  `M_4^9 ≅ C^{144}`, so they are dense.
- `Φ_{det_4}` is polynomial: each coefficient of `det_4(Σ s_i A_i)` is a quartic in the 144 entries.
- So for any polynomial `q` on `W_9`: `q` vanishes on `ρ(GL_16·det_4)` ⇔ `q∘Φ` vanishes on a dense open
  set ⇔ `q∘Φ ≡ 0` ⇔ `q` vanishes on `X_9 = D9`.
- Dependent tuples are included in `X_9`, which is Paper 2's definition. No claim is made that the
  image of a closed set is closed.

**(R5) Kernel identification. Holds (hand derivation).** Take `h = ρ^*h̄ ∈ H^{16}_{24,(λ,0)}`. Then:
`h ∈ I(\overline{GL_16·det_4})` ⇔ `h` vanishes on `GL_16·det_4` (the orbit is dense in its closure) ⇔
(R3) `h̄` vanishes on `ρ(GL_16·det_4)` ⇔ (R4) `h̄ ∈ I(D9)`. So `ρ^*(K_{D9}) = K_X`, where
`X = \overline{GL_16·det_4}`. Only vanishing is used. So the step does not need `D9` to be an orbit
closure, which is the concern B25-10 §2.2 raised and discharged at `n = 3`. It is discharged here the
same way.

**(R6) Multiplicities. Holds (hand derivation), with one degree-specific adjustment.**
- `D9` is `GL_9`-stable. For `g ∈ GL_9`,
  `(g·Φ(A))(s) = det_4(Σ_i (g^{-1}s)_i A_i) = det_4(Σ_j s_j A'_j)`, where
  `A'_j = Σ_i (g^{-1})_{ij} A_i` is another tuple in `M_4^9`. The closure of a stable set is stable.
- `D9` is a cone. `Φ(tA) = t^4 Φ(A)`, and over `C` every `c ∈ C^*` is `t^4` for some `t`, so `c·Φ(A) = Φ(tA)`.
  **The degree-specific step:** B25-05 used `t^3` at degree 3. Here the exponent is 4, and the
  conclusion survives because `C` is algebraically closed.
- `X = \overline{GL_16·det_4}` is `GL_16`-stable, and it is a cone because scalars in `GL_16` scale
  `det_4` by `t^{-4}`, which covers `C^*`.
- In characteristic 0, `I ∩ M_λ = S_λ ⊗ U` for both varieties (`isotypic_rank.md` Lemma 1, READ;
  B17-03's complete-reducibility paragraph, READ). `U ≅ K` through the highest-weight line.
- So `i = dim K` and `mult = a − i` on both sides. With R2 and R5, this gives `a_16 = a_9`,
  `i_X = i_{D9}` and `mult_X = mult_{D9}` at `(λ, 24)`. That is Paper 2's `eq:lengthred` at `r = 9`
  for `det_4`. ∎

**Hypothesis checklist at the point of use.**

| hypothesis | value at the cell | label |
|---|---|---|
| `f` a form of degree `d` on `C^N` | `det_4 ∈ Sym^4 M_4^*`, `d = 4`, `N = 16` | READ (Paper 2 l. 114, 260) + hand derivation |
| `1 ≤ r ≤ N` | `9 ≤ 16` | hand derivation |
| `ℓ(λ) ≤ r` | `ℓ(65,17,2^7) = 9 ≤ 9` | hand derivation |
| `|λ| = dδ` | `96 = 4·24` | hand derivation |
| `D9 = X_9` | §3 | READ + hand derivation |
| field / characteristic | `C`, char 0 (used in R6 and in the fourth-root step) | hand derivation |
| R1–R6 | §4 | hand derivation, each at degree 4 |

## 5. Weight conventions at Paper 2's point of use

Paper 2 never states the action `(g·F)(v) = F(g^{-1}v)` explicitly (a grep for `g^{-1}`, `Borel` and
`\mathrm{wt}` finds nothing). Its point-of-use objects fix the convention anyway (READ + hand
derivation):

1. **The ambient module is polynomial.** Line 1072 writes `M_λ = HWV_λ(Sym^{24} Sym^4 C^9)`. This is
   `C[Sym^4 (C^9)^*]_24 = Sym^{24}(Sym^4 C^9)`, a polynomial `GL_9`-module. So its highest weights are
   partitions, as in Lemma R. Under the dual convention the weights would be `≤ 0`, and a partition such
   as `(65,17,2^7)` could not be a highest weight of `Sym^{24}(Sym^4 (C^9)^*)`.
2. **The coefficient symbols have non-negative weights.** Line 1075's `u = c_{(4,0,…,0)}` is used as a
   weight-`(4,0,…)` element that shifts the ladder `(4δ−31,17,2^7)` by `(4,0,…)`. That is `wt(c_α) = α`,
   i.e. R1's convention.
3. **The LMR weight converts to the same partition.**
   - At `d = 4`, `k = 2n − 2 = 6`: `Ω = 3·2·8 ω_1 + (32 − 12 − 5) ω_2 + 2ω_9 = 48ω_1 + 15ω_2 + 2ω_9`,
     in degree `8·3 = 24`.
   - As a partition: `(48) + (15,15) + (2^9) = (65,17,2^7)`, of size 96.
   - The `SL_16` weight determines `λ` only up to full columns of length 16. `|λ| = 96 = 4·24` and
     `ℓ = 9 < 16` exclude any such column.
   - `N = 16 ≥ k + 3 = 9`.
   - The remaining conversions are the same as B25-05 §A.4 step 2, and none depends on the degree:
     SL-submodule vs GL-submodule (scalars act on degree 24 by `t^{±96}`); projective vs affine cone
     (scalars scale `det_4` over all of `C^*`); any nonzero copy contains a Borel-highest-weight vector
     for the upper-triangular `E_{i,i+1}`.
   - This agrees with Paper 2 lines 1056–1059 (hand derivation).
4. **The Borel.** Paper 2 line 798 computes multiplicities as "kernels of raising operators on the
   weight space". Lemma R's kernels are for the upper-triangular simple `E_{i,i+1}`, and R2 is proved
   for exactly those.

**No convention mismatch was found.**

## 6. What the certificate gives, and what it does not

- **Gives:** the length-restriction lemma holds at `(d, N, r) = (4, 16, 9)` for `f = det_4`, with Paper
  2's `D9`. Hence `K_{\overline{GL_16·det_4}}(24, λ) ≠ 0 ⇒ K_{D9}(24, λ) ≠ 0`. Given LMR's `n = 4`
  statement, this means `i_det ≥ 1` on `D9` at `(λ, δ) = ((65,17,2^7), 24)`. It also gives
  `a_16 = a_9` at this cell.
- **Does not give:**
  - I did not read the LMR input itself at `n = 4` (Thm 2.3.1 + Thm 3.1.1 at `k = 6`, `d = 4`,
    `N = 16`), in this slot. My label for it is **UNREAD**. Paper 2 records its own PRIMARY reading at
    statement level; that is SECONDARY for me. I checked only the arithmetic of the weight conversion.
  - Nothing about `i_det ≤ 1`, the rank-273 certificate, the padded side, `i_pad`, `Δ`, or separation
    on padding. The binding constraint stands verbatim: "No five-row determinant equation is known to
    be nonzero on padding."
  - The same argument works for any `f`, including `x_0 per_3`, since R1–R6 never use `f = det_4`
    beyond §3. The brief asks only about `D9`, so **I make no ruling on Paper 2's `P_r` clause**.
  - Paper 2's citation `\cite[Prop.~4.19]{Companion}` is **UNREAD** by me. The certificate does not
    rest on it. It rests on B25-05 Lemma R, re-derived here at degree 4.
- **The brief's warning is honoured.** The cubic ruling (B25-10 §2.4) is not used as a premise. Every
  step was redone with `|α| = 4`, `N = 16`, `r = 9` and `t^4`. Only the cone step (R6) changes form, and
  it still holds over `C`.

## 7. Proposed Paper 2 wording (proposal only; **the paper is not edited**)

The sentence that could change after independent review (B26-10) is at lines 1060–1063:

> **Current.** "…and the length reduction `\eqref{eq:lengthred}` carries the copy from sixteen variables
> to `\Ddet_9`. That transfer is the `n=4` analogue of the premise `(\star)` of the `n=3` control above:
> the `n=3` case is proved; the `n=4` case is not yet checked, so this transfer is flagged, not
> established."

> **Proposed.** "…and the length reduction `\eqref{eq:lengthred}` carries the copy from sixteen
> variables to `\Ddet_9`. Here `\Ddet_9` is exactly the closure of the restrictions of
> `\overline{\GL_{16}\cdot\det_4}` to a $9$-plane, and the length-restriction lemma holds at
> $(d,N,r)=(4,16,9)$ with the same proof as at $n=3$: weights of coefficient functionals are
> non-negative, the raising operators $E_{i,i+1}$ with $i\ge9$ kill every restricted coefficient,
> independent $9$-tuples are dense in $M_4^{9}$, and complete reducibility holds in characteristic zero.
> So the transfer is proved, and $i_{\det}\ge1$ on $\Ddet_9$ rests only on \cite{LMR}."

**Companion changes for B26-10 to consider (not required by this slot):**
- **Line 1019–1020 and 1003.** Rename "`call it (\star)`" / "`(\star)` below" to "the length-restriction
  lemma". This is the standing convention in `B26_COMMON.md`, and B25-10 §2.4 endorsed it. Paper 2 still
  uses `(\star)` there, while `Theorem~\ref{thm:star}` (line 429) is the *different* reducible-locus
  criterion.
- **Lines 254–256.** Optionally cite the record's lemma (`isotypic_rank.md` Prop. 5 with B25-05 Lemma R)
  alongside or instead of `\cite[Prop.~4.19]{Companion}`, which I have not read.

These changes would apply only after B26-10 accepts this certificate. **Until then the flag at lines
1061–1063 stands.**

## 8. Source/method ledger

| claim | label | locator |
|---|---|---|
| Paper 2's definition of `D_r` | READ | `79b68dcf:paper/det4-onset.tex` l. 112–117 (CRLF blob `065f8799…`) |
| Paper 2's identification of the restricted variety with `D_r` | READ | same, l. 251–261 |
| The flag sentence | READ | same, l. 1058–1063 |
| Paper 2's point-of-use conventions (`M_λ`, `u = c_{(4,0..)}`, raising kernels) | READ | same, l. 798, 1072, 1075 |
| Lemma R statement and n = 3 proof | READ | `2688efd1:docs/b25_05_report.md` §A.3 (LF blob `38834c31…`) |
| B25-10's check statement | READ | `42e7f4ba:docs/b25_10_review.md` §2.4, last bullet (LF blob `0488ce1e…`) |
| Complete reducibility, `I ∩ M_λ = S_λ ⊗ U` | READ | `82633a60:docs/isotypic_rank.md` §2 Lemma 1 (LF blob `5f33e38e…`) |
| Quartic statements of R1–R5 | READ, not relied on | `0cce6172:docs/b17_03_report.md` Lemmas 1–2, eq. (3), (6), (7) (LF blob `bcb38b5f…`) |
| s73 `D_7` definition (context for the n = 3 case only) | READ | `82633a60:docs/s73_report.md` l. 55 (LF blob `f40783ba…`) |
| `D9 = X_9` (§3) | hand derivation | this report |
| R1–R6 at (4, 16, 9) (§4) | hand derivation | this report |
| Weight conversion `Ω(6,4) = (65,17,2^7)`, degree 24 (§5) | hand derivation | this report |
| LMR Thm 2.3.1 / 3.1.1 at n = 4 | UNREAD by me (SECONDARY via Paper 2) | not load-bearing for the transfer |
| `\cite[Prop.~4.19]{Companion}` | UNREAD | not used |

**Tool memory.** The session memory index was loaded automatically. It covers housekeeping delivery state
and a post-B19 status note. Neither was used as evidence.

## 9. Limitations

- This certificate is producer-only. It is the same argument as B25-05 Lemma R, checked at new
  parameters, and it claims no new mathematics.
- The certificate transfers an ideal copy. Whether a copy exists at `N = 16` is LMR's statement, which I
  did not read.
- I did not compile Paper 2, so the printed equation numbers are unconfirmed (§2 locator note).
- The `P_r` / `x_0 per_3` half of `eq:lengthred` is outside this slot and was not ruled on.

## 10. Resource receipt

| item | value |
|---|---|
| UTC start | `2026-09-22T23:43:11Z` |
| last reading step (input hash table) | `2026-09-22T23:45:36Z` |
| UTC stop | recorded in `results/b26_04/MANIFEST.json` (`utc_stop`) |
| interruptions | none |
| ceiling | 30 substantive minutes; finished well inside it |
| pilots | **0** |
| mathematical programs | **0** (no symbolic, exact-arithmetic, replay or search runs) |
| compute lease | not requested |
| tools | `git` read-only (`show`, `rev-parse`, `cat-file`, `ls-tree`, `log`, `merge-base --is-ancestor`, `status`, `check-attr`); `sha256sum`, `wc`, `tr`, `od`, `grep`, `sed`, `awk`, `nl`, `cut`, `ls`, `find`, `date` |
| git writes | none |
| subagents / other sessions | none |

## 11. Files (UNCOMMITTED / PRODUCER ONLY)

| path | state |
|---|---|
| `docs/b26_04_report.md` | this report, created |
| `results/b26_04/PROPOSED_DELIVERY_PATHS.txt` | created |
| `results/b26_04/MANIFEST.json` | created; binds the two files above; not self-hashed |

No paper, sealed packet, manifest of another slot, ledger or Batch 25 record was edited.
