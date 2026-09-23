# B26-03 — Paper 1 primary-source obligations: report

**UNCOMMITTED / PRODUCER ONLY.** Session: Claude Code, Claude Opus 5.5 (1M context), default
permission mode. Worktree `work/batch15_workers/B23-05`, branch `b23-05-paper1`. No staging, no
commits, and no edits to the paper, GAPS, READINESS, manifests or ledgers. Verifying sources does
**not** make Paper 1 ready, and this report does not declare readiness.

**Outcome in one line.** All five points of use are decided and none is UNRESOLVED:

| # | point of use | verdict |
|---|---|---|
| 1 | IK Lemma 5.2 | **NARROW**, minor: `D = 2` is outside the lemma |
| 2 | Kumar, Compositio, Cor. 6.2 | **VERIFIED** |
| 3a | Hüttenhain §8.1 (Jacobi degeneration) | **VERIFIED** |
| 3b | Hüttenhain Cor. 8.3.2 | **VERIFIED** |
| 4 | G-P4, the product-of-variables citation | **WITHDRAW** the `KumarCMH` key; the correct attribution is `KumarComp` and `KL` |

Proposed patches are unified diffs against the LF blob in `results/b26_03/`.

## 0. Timeline (UTC, 2026-09-22)

| event | time |
|---|---|
| start (first command, preflight) | 23:42:43Z |
| first source fetched | 23:43:34Z |
| last source fetched (BI PDF) | 23:49:54Z |
| all readings complete; drafting | ~23:51Z |
| 45-minute checkpoint | **not reached**: work finished well under 45 minutes |
| stop | recorded in §9 |

There were no interruptions. Web access was used only to fetch the primary sources listed in §3.

## 1. Preflight

- **Admin hashes** (raw SHA-256, as on disk; recorded for the integrator, not matched):
  - `batch26_launch/B26_COMMON.md` `a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd` (5,419 B)
  - `batch26_launch/B26-03.md` `8cf14c4af457303c1846e2f8ae9e49e3c869af96d289c224ac49e49ea07c8132` (3,151 B)
  - `BATCH26_LIVE_LEDGER.md` `9d24c37c5953c66583f199af3e8fc226e4feb9f7c70d412f2d4424594b47d2c8` (17,593 B)

  The first two equal the adoption table in `LAUNCH_PROTOCOL_B26.md`.
- **Worktree:** branch `b23-05-paper1`, HEAD `848e22b4d7bf73c392bd6bac3ac6591315190b0e`, **equal to
  the expected HEAD**.
- **`git status --porcelain`:** empty (clean) at start.
- **Output paths:** `docs/b26_03_report.md` and `results/b26_03/` did not exist at start. **No
  collision.**
- **Local instructions:** no `AGENTS.md` or `CLAUDE.md` in the worktree or at the project root.

## 2. Committed inputs (all at `848e22b4` unless stated)

| input | bytes hashed | SHA-256 | size |
|---|---|---|---|
| `paper/det3-conductor.tex` | **LF blob** (`git show`) | `4e1ccf7006879c748beeb57676567ae2443a3a587df7251efc0523fec4686338` | 114,836 B |
| same | CRLF working copy (raw) | `fada5f7c9663f4a207252af574c49c2c84f2291cb27fa6115bce06ed82317086` | 116,972 B |
| `results/b25_03/SIGNATURE_SUPPLEMENT_20260922.md` | LF blob = raw working copy | `1e636f62165d977a7214173d9002cf4626138a7382f844e74dabb54a5f576de0` | 4,011 B |
| `GAPS.md` (the GAPS file, located with `git ls-tree`) | LF blob = raw | `b1b8d4c773a614d85610b63999959164291e05d42ca5fa3f96f6f7ce809a298d` | 27,371 B |
| `READINESS.md` | LF blob = raw | `9d82b251ead30b3e6b5634237b97b879365383a796c1db514447db87b5ee8470` | 9,662 B |
| `241da4db…:docs/b25_03_report.md` | LF blob | `fd1f0d93a23407f8f55f2d82ae342016a904c256573cba2be26262244087d01a` | — |
| `42e7f4ba…:docs/b25_10_review.md` (§5 read) | LF blob | `0488ce1e90a6cd08158eb277dd482b783aa4c58cfd6cec744bd35d25b589477e` | — |

The paper's LF hash equals the stage-3 signed hash in the signature supplement, and its CRLF hash
equals the supplement's working-copy "after" hash. All line numbers below are line numbers of the
**LF blob**. The already-decided items (signature, Form A at Cor. 4.2, the §6 intro wording, the
acknowledgement) were not reopened.

## 3. Sources fetched and read (the fetch ledger)

All files are untracked copies under `results/b26_03/literature/` and are **not proposed for
delivery**. Retrieval times are UTC, 2026-09-22.

| source | URL | retrieved | SHA-256 (raw file) | bytes |
|---|---|---|---|---|
| IK, arXiv:1911.03990**v1** PDF | https://arxiv.org/pdf/1911.03990v1 | 23:43:34Z | `c3af3ef18c507f5fdd9dc9dc60071c20060a682038bf922751afa696b798f33f` | 690,935 |
| IK v1 e-print (gzip TeX, `Mult_IK.tex`) | https://arxiv.org/e-print/1911.03990v1 | 23:44:24Z | `4ad79d67f26b89d221df18b007c65bde7d14e38b55ca18acc0aabfce5c405dfe` (unpacked TeX `be5871445ee3be712aab1ffd7c08b89ab3322d2a8f010af5e71f70e9379e1fb0`) | 48,859 |
| Kumar, arXiv:1109.5996**v2** PDF (journal-ref: Compositio 151 (2015) 292–312) | https://arxiv.org/pdf/1109.5996v2 | 23:43:35Z | `71078e231cffb307b8cf2baf06141a242f693471fc325fd057e96278b68da252` | 199,956 |
| Kumar v2 e-print (`newdet.tex`) | https://arxiv.org/e-print/1109.5996v2 | 23:44:25Z | `a5b83b254ad51ba96181f3ceb1d799c3f9cdeae276b76f726f3903e0521ae06f` (TeX `8a09109515231cdc5ab04c8af8053e689dcc99fff8b05f53b73b66e97762dd66`) | 21,127 |
| Kumar CMH, arXiv:1007.1695**v1** PDF (the only version) | https://arxiv.org/pdf/1007.1695v1 | 23:43:35Z | `3c6b70d7afab993077b4fb8b6988707773506c84baefdd034fd78c393ef17069` | 268,529 |
| Kumar CMH v1 e-print (`perm.tex`) | https://arxiv.org/e-print/1007.1695v1 | 23:44:25Z | `348bd03dbbad2edc0479af44794335a2c42018b3b9dae63a73ae48a6b4ceb2bf` (TeX `8209e0d18111dc3363b5497414be8f83a7876f5e9ab87e8deb284a54b4bc21fe`) | 24,986 |
| Kumar–Landsberg, arXiv:1410.8585**v1** PDF (the only version) | https://arxiv.org/pdf/1410.8585v1 | 23:43:35Z | `8397138d5f923bf71b5df9213d1ae6b9392a05c9a796e6be427b75c69f9e0caa` | 147,855 |
| KL v1 e-print (tar.gz) | https://arxiv.org/e-print/1410.8585v1 | 23:44:26Z | `135bc3479a8b65a56ac3098d645d87c018455f9cf40939194bd53fd930ffe7b2` (TeX `5c4eb18bed5b94c65ea7b18a5df3aa590ace8d1c128700324ebfeb166ca585ef`; `cortdefs.tex` `8c59eacd…`) | 17,109 |
| Hüttenhain thesis PDF, DepositOnce handle 11303/6524 (via doi:10.14279/depositonce-6032) | https://depositonce.tu-berlin.de/bitstreams/5b0e7d2c-cb06-48ee-8842-f92936d41782/download | 23:43:52Z | `ccf1a13e6b8c0d9ee25f0a85616eb47232bf90bdad0b03bb9169ee91e7609edd` | 1,314,561 |
| BI, arXiv:1511.02927**v2** e-print (`fund-invar.tex`); read for G-P4's attribution only | https://arxiv.org/e-print/1511.02927v2 | 23:47:27Z | `7861e6c23553073ca3eeb36d9326198fec643ab030d83cc1a8763a41e5f78fa3` (TeX `fb1cec089ab9b53975b31e5b89c6dd187075d0a29060252ad2526dbe08f4f8ad`) | 45,042 |
| BI v2 PDF (to confirm printed numbering) | https://arxiv.org/pdf/1511.02927v2 | 23:49:54Z | `a4138fc3ef45f144f367f227514b8345ddd74690c19ca07e1ef4be707fd6ea7b` | 451,754 |

**Attempted, not obtained:**
- STOC 2020 IK: https://dl.acm.org/doi/pdf/10.1145/3357713.3384257 returned HTTP 403.
- Published Compositio Kumar: the doi:10.1112/S0010437X14007660 landing page is the Cambridge Core
  abstract page, with access options. The PDF was not fetched.
- Published CMH 2013 Kumar and Discrete Math. 2015 KL: not attempted. The arXiv versions answer the
  questions asked.

**Method.** Exact statements were read in the authors' TeX sources. No PDF renderer is installed and
none was installed. Printed theorem numbers and PDF pages come from `pdftotext` of the hashed PDFs
(an administrative text extraction). The thesis has no source, so it was read from `pdftotext` of
the hashed PDF. Dropped glyphs are marked as reconstructions in `results/b26_03/SOURCE_QUOTES.md`.

**Relation to B24-01's record (not adopted, only compared).** The thesis hash matches B24-01's recorded
prefix `ccf1a13e…` (only the prefix is on record). The IK and Kumar PDF bytes differ from B24-01's `a34b735c…` and `7eeacd13…`. arXiv
regenerates PDFs, and B24-01 names no version, so the identity of the text they read cannot be
established from the prefix. Every reading below is this session's own.

## 4. Item 1 — IK, Lemma 5.2

**Point of use:** L153–158.

> That such a $k$ exists, at an explicit bound depending only on the degree and not on the weight,
> is a theorem of Ikenmeyer and Kandasamy \cite[Lem.~5.2]{IK} for power sums
> $x_1^{D}+\dots+x_m^{D}$ in the regime (number of variables) $m\ge D$ (degree): unconditionally for
> $D$ even, and for $D$ odd under the side condition $\binom{2(D-1)}{D-1}\ge 2(m-1)$. Their argument
> is algebraic and makes no optimality claim.

**Source:** arXiv:1911.03990v1 (TeX `be587144…`, PDF `c3af3ef1…`), Lemma 5.2, PDF p. 9, TeX
l. 510–527. The quotation is **verbatim** in `SOURCE_QUOTES.md` Q1. Paraphrase: for
`λ ⊢_m dD`, with `e = e(d, m, D)` given by explicit case formulas (for odd `D` only under the
binomial side condition), the closure multiplicity at `λ + (m × eD)` equals the orbit multiplicity
at `λ`.

**Hypothesis by hypothesis:**

| paper's wording | source | match |
|---|---|---|
| power sums `x_1^D+…+x_m^D` | §3: `p := x_1^D+⋯+x_m^D ∈ Sym^D ℂ^m` (READ) | yes |
| "in the regime `m ≥ D`" | This is IK's §2 framing ("For `m ≥ D` let `p := …`"). §3 and Lemma 5.2 do **not** assume it (READ). | The paper's restriction is narrower than the source, so it is harmless. No change is needed. |
| "unconditionally for `D` even" | Lemma 5.2's `e` for `d ≥ m` divides by `D−2`. Theorem 4.2 (on which the proof rests) defines `e_ϱ = Σ⌈ϱ_i/(D−2)⌉`. §3 identifies `H = stab p = ℤ_D^m ⋊ S_m` "for `D ≥ 3`" (READ). | **Overstated at `D = 2`.** `D = 2` is even, and there the source's statement is undefined and its stabiliser description fails. That the lemma is implicitly `D ≥ 3` is this session's reading of those three facts (**READ + hand derivation**). IK do not print "`D ≥ 3`" in the lemma. |
| odd-`D` side condition `C(2(D−1), D−1) ≥ 2(m−1)` | verbatim in Lemma 5.2 and Theorem 4.2 (READ) | yes |
| "explicit bound depending only on the degree and not on the weight" | `e` is a function of `d` (the degree), `m` and `D` only, not of `λ` (READ) | yes |
| "makes no optimality claim" | The only tightness statement is "provides `e_ϱ = d`, so the bound is tight" (TeX l. 539). It concerns `max e_ϱ = e`, not minimality of the shift (READ). | yes |
| "such a `k` exists" (the conductor along the `Δ`-ray) | IK state a shift by `(m × eD)`. They do not speak of a conductor or a `Δ`-ray. | The translation is the paper's own step (IK's shifts are multiples of the Lemma 5.1 periods `m×D` or `m×2D`). **Not audited here.** It is flagged in §8 and does not change the verdict. |

**Locator:** Lemma 5.2 is confirmed in arXiv v1. The bibitem names STOC 2020, pp. 713–726, which
is **UNREAD** (ACM 403), so the lemma number in the STOC version is unconfirmed. An optional patch
adds the arXiv id to the bibitem.

**Verdict: NARROW** (minor). Minimal wording is `$m\ge D$` → `$m\ge D\ge3$`. The diff is
`results/b26_03/b26_03_ik_lem52_narrow.diff`. Optionally,
`results/b26_03/b26_03_ik_arxiv_locator_OPTIONAL.diff` makes the cited locator point at the version
read.

## 5. Item 2 — Kumar, Compositio, Corollary 6.2

**Point of use:** L104–111.

> for even $n$, and assuming the Alon--Tarsi conjecture in its column Latin square form, Kumar
> shows that the irreducible of highest weight $n\lambda$ occurs in
> $\bC[\overline{\GL_{n^{2}}\cdot\det_n}]$ for every partition $\lambda$ of length at most $n$
> \cite[Cor.~6.2]{KumarComp}, the vanishing counterpart being Howe's. […] and $n=3$ is odd, which
> is the case that argument excludes.

**Source:** arXiv:1109.5996v2 (TeX `8a091095…`, PDF `71078e23…`). The arXiv abstract page gives
the journal-ref "Compositio Math. 151 (2015) 292-312". Corollary 6.2 is on PDF p. 20; the printed
"6.2 Corollary" was checked in the PDF text, and the TeX label is `coro3.2`. The quotation is
**verbatim** in `SOURCE_QUOTES.md` Q2.

| paper's wording | source | match |
|---|---|---|
| "for even `n`" | Thm 6.1: "Assume, as above, that `m` is even". §2: "From now on, `m` is an even positive integer" (READ) | yes |
| "assuming the Alon–Tarsi conjecture in its column Latin square form" | Cor 6.2: "assuming the validity of the column Latin `(m,m)`-square conjecture" (Conj. 4.3, Huang–Rota). Rem. 4.5 records its equivalence with Alon–Tarsi (READ). | yes |
| "irreducible of highest weight `nλ` occurs in `ℂ[closure of GL_{n²}·det_n]`" | "`V_E(mλ)` occurs in `ℂ[𝒳]` with nonzero multiplicity". `𝒳` is the `GL(E)`-orbit closure of the determinant in `Q = 𝒫^m(E)`, with `dim E = m²` (READ) | yes, at occurrence level |
| "for every partition `λ` of length at most `n`" | "`λ = Σ_{i=1}^m n_i δ_i`, `n_i ∈ ℤ_+`", which is exactly the partitions with at most `m` parts (READ; the identification with fundamental weights `δ_i` is standard) | yes |
| "the vanishing counterpart being Howe's" | Thm 6.1's "Moreover" clause (`V_E(dδ_i)`, `d < m`, does not occur) comes via Cor. 2.4 from Prop. 2.3, "from [H, Proposition 4.3]", i.e. Howe (READ) | yes |
| "`n = 3` is odd, which is the case that argument excludes" | The standing assumption is `m` even. Prop. 2.3(b) (Howe) gives `[S^ℓ(S^m E)]^{SL(E)} = 0` for `m` odd (READ) | yes |
| "Kumar shows" (a conditional result) | The Acknowledgements say the theorem "is proved only under the hypothesis that the Latin Square Conjecture is valid" (READ) | yes: the paper states it conditionally |

**Locator:** Cor. 6.2 is confirmed in arXiv v2, which carries the Compositio journal-ref. The
published Compositio pagination and numbering are **UNREAD**. The bibitem already gives
`arXiv:1109.5996`, so the reader can locate the version read.

**Verdict: VERIFIED.**

## 6. Item 3 — Hüttenhain thesis, §8.1 and Corollary 8.3.2

**Source:** J. Hüttenhain, PhD thesis, TU Berlin 2017, doi:10.14279/depositonce-6032, PDF
`ccf1a13e…`. Printed pages are given here. PDF page = printed + 10 for the pages used.

### 3a. §8.1: the Jacobi degeneration (L791–794)

> the explicit degeneration to $P_2$ that H\"uttenhain and Lairez supply --- $\det(A+tS)$ with $A$
> skew-symmetric and $S$ symmetric, whose order-$t$ term is $\tr(\operatorname{adj}(A)\,S)=2P_2$ by
> Jacobi's formula \cite[\S8.1]{Hue}

**Source locator:** Lemma 8.1.3 and its proof, pp. 90–91. The quotation (via `pdftotext`, with
reconstructed glyphs marked) is in `SOURCE_QUOTES.md` Q6. Paraphrase: with `b` the projection to
antisymmetric matrices and `a` the projection to symmetric ones, the coefficient of `t` in
`det(b + ta)` is `tr(b^♯ a)` by Jacobi's formula, where `b^♯` is the adjugate, and this equals
`2Q2`.

| paper | source | match |
|---|---|---|
| `det(A + tS)`, `A` skew-symmetric, `S` symmetric | approximation path `b + at`, `b` antisymmetric, `a` symmetric (READ) | yes |
| order-`t` term `tr(adj(A) S)` "by Jacobi's formula" | "The coefficient of t in det(b + ta) is equal to tr(b^♯a) by Jacobi's formula, where b^♯ is the adjugate matrix of b" (READ; the `♯` is reconstructed) | yes |
| `= 2P_2` | "tr(b^♯a) = u a u^t = 2Q2". The thesis's `Q2 = x4x1² + x5x2² + x6x3² + x7x1x2 + x8x2x3 + x9x1x3` is the paper's `P_2` verbatim (L738) (READ) | yes, in the thesis's coordinates, which the paper's representative shares |
| "that Hüttenhain and Lairez supply" | Ch. 8, p. 89: "These results have been previously published in [HL16]" (READ). HL16 itself was **not** read here. | acceptable: the thesis says the content is HL16's |

**Verdict: VERIFIED.**

### 3b. Corollary 8.3.2 (L750–752)

> The orbit closure of the traceless $d\times d$ determinant is a component of the boundary for
> every $d\ge3$ \cite[Cor.~8.3.2]{Hue}.

**Source locator:** Corollary 8.3.2, p. 96, quoted in Q6: "The orbit closure of the traceless
determinant is an irreducible component of ∂(det_d), for all d ≥ 3." The glyph `∂` is dropped by
the extraction, and its meaning is fixed by Theorem 8.0.1's "The boundary ∂(det3)".

| paper | source | match |
|---|---|---|
| traceless `d×d` determinant | §8.3: `P` is the restriction of `det_d` to `W = {tr A = 0}`. The corollary's proof works with `Q = D ∘ a` on `M = ℂ^{d×d}` (READ) | yes |
| "a component of the boundary" | "an irreducible component of ∂(det_d)" (READ) | yes; the paper's claim is weaker |
| "for every `d ≥ 3`" | "for all d ≥ 3" (READ) | yes |

The proof rests on Theorem 8.3.1 (a stabiliser dimension, `d² − 1`) and Lemma 8.3.3. These were
read at statement level only. The proof of 8.3.1 was not audited, and the paper does not need it.

**Verdict: VERIFIED.**

**Incidental (not a listed item):** the bare "(see also \cite{Hue})" at L735 is consistent with
Theorem 8.0.1 ("exactly two irreducible components", the traceless determinant and `Q2`). The
dimensions in Lemma 8.1.1 are 65 for the orbit closure and 64 for both components, consistent with
the paper's "pure of codimension one". The thesis also records "answers a question of Landsberg
[Lan15, Problem 5.4]", which matches L734. That last point is **SECONDARY** for the HL16 claim
itself.

## 7. Item 4 — G-P4: the product-of-variables statement

**Point of use:** Remark 4.14, L981–985.

> For even $n$, $e(\det_n)=n^{2}$ holds if and only if a signed count of admissible $n$-tables is
> nonzero \cite[Prop.~3.28]{BI}, an Alon--Tarsi-type criterion verified at $n=2$ and, by computer,
> at $n=4$; the analogous statement for the product of variables is Kumar's \cite{KumarCMH,KL}.

**The statement, located.** The analogue of BI Prop. 3.28 for `x_1⋯x_m` is **BI Proposition
3.25** (arXiv:1511.02927v2, PDF p. 16; the printed number was checked in the PDF). Verbatim: "Let
`m` be even. Then `e(X_1…X_m) ≥ m` and equality holds iff the Alon-Tarsi conjecture is true for
`m`." BI introduce it with "The following observation is due to Kumar [Kum:15] and Kumar and
Landsberg [kumar-landsberg:15]". In BI's bibliography `Kum:15` is **Kumar, *A study of the
representations supported by the orbit closure of the determinant***, i.e. the paper's
`KumarComp`. It is **not** CMH 2013. IK §5 attribute the related occurrence facts for
`x_1⋯x_m` to the same `[Kum15]` (READ, Q1).

**Kumar–Landsberg (`KL`), arXiv:1410.8585v1: supports the citation.** Theorem 1.9 (PDF p. 4): for
`n` even, (a) Alon–Tarsi for `n` ⇔ (b) `S_{(n^n)}V` is not in the kernel of `h_{n,n}`. Lemma 1.5
(Hadamard): `ker ⊕h_{d,n}` is the ideal of the Chow variety `Ch_n(V^*) = {ℓ_1⋯ℓ_n}`. Together
(READ; KL's §3 says "This proves the equivalence of (a) and (b) by Lemma 1.5") they give: for `n`
even, the degree-`n` `SL_n`-invariant on `S^n ℂ^n` is nonzero on the products of `n` linear forms
if and only if Alon–Tarsi holds for `n`. The products of `n` linear forms in `n` variables are the
orbit closure of `x_1⋯x_n` (**hand derivation**, elementary). Converting this to "`e(x_1⋯x_n) = n`"
is BI's own step (their Thm 3.15, invoked in the proof of Prop. 3.25; READ at statement level).

**Kumar, Compositio (`KumarComp`), arXiv:1109.5996v2: supports it, implicitly.** The text never
writes `x_1⋯x_m`, which confirms GAPS G-P4's observation. But its §3 map
`θ(A) = (𝒟 ⊙ A)|_{E_i}` sends `A` to a determinant of a *diagonal* matrix, because
`Ae_j = Σ_{p≤m} a^j_p e_p` and `e_1…e_m` are the diagonal units (READ, TeX l. 518). So `θ(A)` is a
product of `m` linear forms, and for `i = m` the image is the Chow variety (**hand derivation**).
Prop. 3.2 (nonvanishing of the invariant on `θ(M(m,i))` ⇔ `U_i ∩ 𝓘_{mδ_i} ≠ 0`) and the last clause
of **Theorem 5.6** ("For `i = m`, `U_m ∩ 𝓘_{mδ_m} ≠ (0)` if and only if the column Latin
`(m,m)`-square conjecture is true"; printed number checked in the PDF) together with Rem. 4.5 (the
Huang–Rota equivalence with Alon–Tarsi) give the same "iff" (READ + hand derivation for the
Chow identification). KL's Conjecture 1.6 is credited by KL themselves to this paper
(`kumarcoordring` = arXiv:1109.5996).

**Kumar CMH (`KumarCMH`), arXiv:1007.1695v1: does not support it.** Case-insensitive searches of
the whole TeX source find **no** occurrence of Alon, Tarsi, Latin, Chow, Hadamard, Foulkes, "product
of", or any `x_1⋯x_n` monomial (Q4). The published CMH 2013 text is **UNREAD**. arXiv has only v1.
Both BI and IK attribute the statement to the Compositio paper instead.

**Verdict: WITHDRAW** the `KumarCMH` key at L985. The statement itself stands, correctly
attributed. Minimal patch (`results/b26_03/b26_03_gp4_kumar_citation.diff`):

```
-product of variables is Kumar's \cite{KumarCMH,KL}.  For \emph{odd} $n$ the
+product of variables is due to Kumar and to Kumar and Landsberg
+\cite{KumarComp,KL}.  For \emph{odd} $n$ the
```

"Kumar's" becomes "due to Kumar and to Kumar and Landsberg" because `KL` is joint work. This
follows BI's own attribution sentence. An even smaller alternative is to swap only the key and
keep "Kumar's". The author decides.

A pointer "(see \cite[Prop.~3.25]{BI})" would give the reader the exact `e(x_1⋯x_n)` form. It is
**not** in the diff, because it is framing and not required. `KumarCMH` stays cited at L121 and
L782, so the bibitem does not become orphaned.

## 8. Proposed patches (against the LF blob `4e1ccf70…`; the paper is not edited)

| file | role | effect |
|---|---|---|
| `results/b26_03/b26_03_gp4_kumar_citation.diff` | **required** (item 4, WITHDRAW) | L985 |
| `results/b26_03/b26_03_ik_lem52_narrow.diff` | **recommended** (item 1, NARROW) | L156: `$m\ge D$` → `$m\ge D\ge3$` |
| `results/b26_03/b26_03_ik_arxiv_locator_OPTIONAL.diff` | optional (item 1 locator) | IK bibitem gains `arXiv:1911.03990` |

Each diff was checked with `git -c core.autocrlf=false apply --check` and then applied to a
disposable LF copy in the session scratchpad, alone and in combination. All applied cleanly, and no
CR bytes were introduced. Resulting LF hashes:

| applied | SHA-256 | bytes |
|---|---|---|
| G-P4 only | `98c35429b80ff27dde618e8feebf3730862282cff2703f610cbe1764307b2ed2` | 114,869 |
| IK narrow only | `a8a53ae73c9f854e529ea19adc904f6ae131e4faa701c2c70606170f16778f50` | 114,840 |
| IK locator only | `454925d4e949ee66e0e3ee17991ae5c471891829c238c58e59b6d3d7e453efda` | 114,854 |
| G-P4 + IK narrow | `bc3773240a8c3a9909935e626a11de3f166c926a186069372e54c75883bb359d` | 114,873 |
| all three | `3e506cc2bebb980806ffcba09b65403c9df4504076623c3e0972fc14e4b04551` | 114,891 |

No compile was run: this machine has no TeX. The changes touch no label, `\ref` or environment. The
cite keys used (`KumarComp`, `KL`) are existing bibitems.

## 9. Source/method ledger, limitations, resource receipt

**Labels at point of use** (this session's own; B24-01's labels were not adopted):

| claim | label |
|---|---|
| IK Lemma 5.2 statement, §2/§3 definitions, Thm 4.2 hypothesis, tightness remark, §5 attribution | **PRIMARY** (arXiv v1 TeX and PDF, read by me) |
| IK Lemma 5.2 excludes `D = 2` | **READ + hand derivation** (undefined `D−2` denominators and the §3 stabiliser for `D ≥ 3`) |
| Translation of IK's `(m×eD)` shift into the paper's conductor index `k` | **not audited** (the paper's step) |
| IK numbering in STOC 2020 | **UNREAD** (sought: Proc. STOC 2020, pp. 713–726, doi:10.1145/3357713.3384257, "Lemma 5.2") |
| Kumar Cor. 6.2, Thm 6.1, Prop. 2.3, Rem. 4.5, Thm 5.6, Prop. 3.2, §3 definition of `θ` | **PRIMARY** (arXiv v2 TeX and PDF) |
| Kumar Compositio published numbering | **UNREAD** (sought: Compositio 151 (2015) 292–312, Cor. 6.2) |
| `θ(M(m,m))` is the Chow variety (products of linear forms) | **hand derivation** |
| KL Thm 1.9, Lemma 1.5, Conj. 1.6, Chow definition | **PRIMARY** (arXiv v1). The published Discrete Math. 338 version is **UNREAD**. |
| Kumar CMH does not contain the statement | **PRIMARY, negative** (arXiv v1 full-text search). The published CMH 88 (2013) version is **UNREAD**. |
| BI Prop. 3.25 and its attribution sentence | **PRIMARY** (arXiv v2 TeX and PDF), read only for G-P4 |
| Hüttenhain Lemma 8.1.3 / §8.1, Cor. 8.3.2, Thm 8.0.1, Ch. 8 opening | **PRIMARY** (thesis PDF via text extraction; the dropped glyphs `∂`, `♯` and `^t` are reconstructed from context and marked) |
| Hüttenhain Thm 8.3.1 proof | **UNREAD** (statement level only) |
| HL16 (CRAS) itself | **UNREAD** in this session |

**Limitations.**
1. Every locator is to an arXiv version or the thesis. No publisher version was read. For IK, the
   bibitem cites only STOC, hence the optional locator patch.
2. The thesis and the PDFs were read through text extraction, not rendered pages. Exact statements
   of arXiv items were cross-read in the TeX source; the thesis has none.
3. Item 1's NARROW rests on an implicit hypothesis (`D ≥ 3`) that IK do not print in the lemma. A
   reader could call it pedantic. It is a literal overstatement at `D = 2` only, and nothing in
   Paper 1 uses `D = 2`.
4. The paper's conversion of IK's shift into a conductor index, and BI's conversion of Chow
   nonvanishing into `e(x_1⋯x_n) = n`, are not audited here.
5. I did not re-examine the other citations in Paper 1, such as G-P5, Marcus–Minc, LMR and BI
   beyond Prop. 3.25.

**Resource receipt.** **Zero pilots. Zero mathematical programs**: no symbolic, exact-arithmetic,
certificate or search computation. The administrative operations were: SHA-256 hashing, `git
show`/`ls-tree`/`status`/`rev-parse`/`branch`, `curl` fetches of the sources in §3, `tar`/`gunzip`
of e-prints, `pdftotext` extraction, `grep`/`awk` text location and page and theorem-number lookup,
and `diff -u` plus `git apply --check`/`apply` on disposable scratch copies outside the repository.
No compute lease. No dependency was installed. No subagents. No commits or staging. The paper was
not edited. Clock: start 23:42:43Z; the 45-minute checkpoint was not reached; stop at the time
recorded in `results/b26_03/MANIFEST.json` (`stop_utc`). Total time was about 15 minutes against a
90-minute ceiling.

## 10. Registered outcome and achievement level

**Outcome:** the Stop condition is met. Every listed use is VERIFIED, NARROW or WITHDRAW, and none
is UNRESOLVED:

| # | point of use | verdict |
|---|---|---|
| 1 | IK Lem. 5.2 | NARROW (`D ≥ 3`) |
| 2 | Kumar Cor. 6.2 | VERIFIED |
| 3a | Hüttenhain §8.1 | VERIFIED |
| 3b | Hüttenhain Cor. 8.3.2 | VERIFIED |
| 4 | G-P4 | WITHDRAW `KumarCMH` → `KumarComp` (with `KL` kept) |

**Achievement level:** not applicable. This is a source-verification slot, and no mathematical
achievement label (source condition, coefficient equation, separation on padding, positive
multiplicity gap) is advanced or claimed. The binding constraint stands as written: "No five-row
determinant equation is known to be nonzero on padding." Paper 1's readiness is not declared: the
compile of the signed bytes remains, and applying any of these patches is the author's act.
