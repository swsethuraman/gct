# B21-10 — Independent review of the Batch 20 producer packets, and Phase 2 gates for Batch 21

Slot 10, Batch 21, Phase 1 (run alone). Claude Code (Opus 5, 1M context), default permission
mode, 18 September 2026. Worktree `work/batch15_workers/B15-10`, branch `b15-10-portable-witness`.

**Status: COMPLETE.** Closing ledger in §10; decisions are transcribed from §10 only.

## 0. Provenance, and what "independent" means in this document

Recorded before any write (read-only git only: `rev-parse`, `status --porcelain`, `log`,
`show`, `ls-tree`, `cat-file`; no commit, push, fetch, checkout, stash or history operation):

```
git rev-parse HEAD          6915ae6fea04c446da5042fad4c43c1667230602
git rev-parse HEAD^{tree}   7052fbfdfd1e6619149420a0405be49a241bbf6c
git status --porcelain      ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
recorded at                 2026-09-18T00:23:22Z
```

Zero tracked changes, zero staged; the two untracked files are B15-era run residue, pre-existing
and unchanged. HEAD and tree equal the values in the brief.

The method rules are B20-10 §0's, verbatim: verdicts formed **before** reading a deliverable's
own defence, marked as such and preserved byte-for-byte; **committed bytes**, not the working
tree; every verdict labelled READ, REPLAY or INDEPENDENT EVALUATOR; later corrigenda govern; no
sealed report, manifest or packet is edited. No subagent was used. Every judgement below is mine.

Pre-formed verdicts are in `results/b21_10/preverdicts_formed_before_reading.md`, written
00:26:57Z (P1, Theorem A) and 00:32:43Z (P2, the C9 counting) — P1 after reading only §§4.1–4.2
of `b20_01_report.md` and before opening §11, `p2_reduction.json` or any B20-01c artifact; P2
after reading §§0–3, §§4.1–4.5, §5.1 and the first paragraph of §5.2 and before opening §5.2's
derivation. That file is **not edited** after the fact; the two places where reading the defence
changed my mind are corrected here, in §4.1 and §4.3, each with a pointer back.

Every packet document was read from `git show <commit>:<path>` into a scratch copy and hashed:

| document | commit | sha256 |
|---|---|---|
| `docs/b20_01_report.md` | `878258f2…` | `e5f426410f6e5dff4037dc0d837826fb09cca173f7da420dbeb41bb15eb35c89` |
| `docs/b20_02_report.md` | `7de65d7c…` | `15ef389b5eb84074e77f2bd88c2dd5e98b14399a394d150b05f2b1b3f2baeda2` |
| `docs/b20_02b_report.md` | `7de65d7c…` | `60ff4be461ad1f3b4733fdec36372bf0f0af3612a31f8a48af6260c49b5902ea` |
| `docs/b20_12_ledger.md` | `da803892…` | `08c516263a644e13aef38d7714dbfad7c14abe1e68a657a2f6a072500b7c3b94` |

All four equal the prefixes recorded in `BATCH20_CLOSE.md` §2. The uncommitted
`Claude_Handover_B15_B18\post_b19_housekeeping_20260917\BATCH20_CLOSE.md` is cited by sha256
`2c9dcc59a2e0df88b3ab4d757c42d3dee2cb411817bb879e3d945c789005da46` (8,680 bytes), as the brief
requires for anything under `Claude_Handover_B15_B18\`.

## 1. Plain terms

**O1 is resolved, and Theorem A is not the casualty.** B20-01's Theorem A is proved exactly as
written. What failed is the *control* the report specified for it: §4.2's "Status of Theorem A"
paragraph tells the pilot to reconstruct the sealed rows from `det(g)^4 (F_1 + F_2 + F_3)`, which
applies the theorem's own covariance backwards. The slice is `g.Y`, not `Y`, and part (i) reads
`z^{[n]}(g.Y) = det(g)^4 z^{[n]}(Y)`; so the reconstruction needs `det(g)^{-4}`. All six
comparisons are wrong by the single factor `det(g)^8`, one number, the same in both degree
families, and invisible to every internal check the pilot ran — the `S_3` signs, the equality of
the top across `k` and the sign convention all compare slice quantities with slice quantities.
I took the 60 raw runner outputs the pilot recorded as data, redid the extraction, the modular
inverse and the normalisation in my own code, and **`det(g)^{-4}` reproduces all six sealed
values exactly**. `det(g)^8 = 432557 mod 524287` is the factor; it enters at
`analysis/b20_01_p2_reduction.py`'s two reconstruction lines, and it was *specified* there by
§4.2. The `nu`-sign suspect named in §10 is not the fault. **Theorem A: PROVED. Its numerical
control: PASSES, corrected.** O1 closes; C3 and C8 come off CONDITIONAL.

Three further things the record gets wrong, none of which overturns a theorem:

1. **Corollary A.1 over-claims the cheap variant.** "Both give, in addition, the degree-12 value
   at the same point" is false for the four-node extraction: the kernel of the node matrix is
   `(c_8..c_12) = (4, 0, -5, 0, 1)`, so `u = ±1, ±2` determines `c_11` and leaves `c_12` free.
   The 15-evaluation figure of C3 is the right price for both rows; the 12-evaluation variant
   buys degree 11 alone. The same correction moves C8's `840` (degree-11 decision only) apart
   from its `1050` (which does give the degree-12 rows free, as §5.1 says).
2. **C9 understates its own case.** `17,640 = dim S_{(4,4,1)}(C^7)` is right, and I reproduce it
   by an independent hook-content computation; the producer's Weyl-formula arithmetic is also
   correct. But the transversality inequality that fixes `m = 7` compares a slice dimension `3m`
   taken in `W'^3` against the ambient `34` taken in the flag cone `S^`. Done consistently in
   either ambient, the full-`G'` case needs `m >= 8`, not `m >= 6`, and the Levi-only case
   `m >= 11`, not `m >= 9`. The true floor is `dim S_{(4,4,1)}(C^8) = 55,440` — `792` times the
   70-dimensional target rather than `252`. The conclusion holds a fortiori.
3. **The three Bruns–Herzog citations remain unread, and two numbers are unreconciled.** Seven
   routes to the primary text failed (§3.1). But the Dimca preprint that B20-02 leans on *is*
   reachable: I re-fetched it, its sha256 equals the pin byte-for-byte, and I read Remarks 3.5
   and 3.6 in full. B20-02's transcription of them is accurate. Remark 3.6 cites Bruns–Herzog
   **Theorem 1.6.16, page 50**; B20-02's (T1) cites **Theorem 1.6.17**. Both numbers sit in
   B20-02 §9 without being reconciled. More usefully: **(T1)'s condition can be lifted**. The
   only thing Theorem 6.4 needs from depth sensitivity is `H_j = 0` for `j >= 2`, and that
   follows from `grade(J_F) >= 4` by three elementary steps I write out in §3.2. Theorem 6.4's
   all-`k` case is then CONDITIONAL on (T2) alone.

Everything else held. Lemma 6.3 is proved and every dimension in it reproduces. The three G8
certificates replay: their ordering hashes recompute from their own bytes under their own stated
scheme, their blocks and orders equal the report's §3.1 prose, and their values equal the sealed
values. B20-02b is the cleanest packet on this record — pre-registered transcription sentences,
exact scope, and its ranks reproduce every derived quantity I checked. Scope discipline holds in
all four packets; I found no claim stated above its evidence.

Release gates for Phase 2 are in §7. **G19 is adopted with a definition it currently lacks**
(as written it forbids `sha256sum`). **G20 does not belong in the gates** — a reviewer cannot
check a session's permission mode from committed bytes — and I propose a checkable replacement.
Three new gates, each traceable to a defect above. The Phase 2 slot recommendation is **(a)**:
Theorem A survives, so the isotropic-type test of `B` is supported.

No cell is nominated. No gap is claimed. No producer computation was redone beyond the spot
replay and the one independent evaluator O1 needed.

## 2. O1 — Theorem A (B20-01 §4.2) versus its own control

### 2.1 The theorem, ruled before the defence was opened

**[pre-formed, READ]** `results/b21_10/preverdicts_formed_before_reading.md` §P1, 00:26:57Z.
I re-derived all five parts by hand before opening §11 or the pilot JSON, and rule **Theorem A
(i)–(v) PROVED as stated**. In summary, with the details in P1.1:

- **(i)** The `nu`-grading is the weight decomposition of the one-parameter subgroup `sigma_u`
  scaling `W_0` and fixing `W'`, applied diagonally to all five entries; `sigma_u` commutes with
  the `GL_5` action on the tuple index because that action takes linear combinations with the
  *same* map on each `Y_m`. Comparing `u`-coefficients in
  `z(sigma_u(g.Y)) = det(g)^4 z(sigma_u Y)` gives the graded statement.
- **(ii)** The `nu_k`-coordinate of `(g.Y)_i` is `(v u_i)_k`; `det g != 0` because `u_3, u_4, u_5`
  are independent modulo `ker v` and `u_1, u_2` span it.
- **(iii)** `11 = 3+3+3+2` is the only partition into four parts each `<= 3`, so
  `z^{[11]}|slice = 4 z~(D_3, D_3, D_3, D_2)`, linear in `D_2`, hence three terms each linear in
  one of `Z_3, Z_4, Z_5`. *Wording defect:* the proof's phrase "a sum of functions of disjoint
  variable groups" is false as a general principle — the groups share `Z_1, Z_2` — but the
  mechanism the same sentence supplies (set the other groups to zero) is valid, because each term
  is linear in its own `Z`.
- **(iv)** I re-derived `P nu_k P^T = sgn(sigma) nu_{sigma(k)}` from
  `eps_{sigma^{-1}(i) sigma^{-1}(j) sigma^{-1}(sigma(k))} = sgn(sigma) eps_{i j sigma(k)}`, and
  both `GL_5` moves: the tuple permutation contributes `det^4 = s^4 = 1`, the scaling
  `diag(1,1,s,s,s)` contributes `(s^3)^4 = s^12 = 1` (the proof writes `s^4`; both are 1 for
  `s = ±1`, nothing moves). The sign comes out exactly as stated.
- **(v)** Forward is specialisation; backward uses (iv), (iii) and density of `{rank v = 3}` with
  the covariance (i). `39 = 3 · 13`. On an `F_1`-tuple
  `D(sigma_u T_1) = u^2(D_2' + u D_3)`, so `u`-degrees `8..12` only: five unknowns, five nodes.

*Notation, recorded not charged:* the statement writes the symmetry `Y -> A Y A^{-T}`, the proof
`Y -> P Y P^T`. For a permutation matrix `A^{-T} = A`, so these are literally different maps
unless `sigma` is an involution; they agree once `A Y A^{-T}` is read as naming the *pair*
`(A, A^{-T}) in SL(A) x SL(B)`, whose action on `A (x) B = Mat` is `A Y A^{-1} = P Y P^T`, which
is plainly what is meant.

### 2.2 The defect, also pre-formed, and the prediction it licensed

**[pre-formed, READ]** P1.2a, written before I opened §11.4. The "Status of Theorem A" paragraph
specifies the control as reconstructing the sealed rows from `det(g)^4 (F_1 + F_2 + F_3)` and
`det(g)^4 [u^{12}]`. This inverts (i). The sealed rows are `z^{[n]}(Y)` at the general point; the
`F_k` live on `g.Y`; (i) says `z^{[n]}(g.Y) = det(g)^4 z^{[n]}(Y)`. So

    z^{[11]}(Y) = det(g)^{-4} (F_1 + F_2 + F_3),      z^{[12]}(Y) = det(g)^{-4} [u^{12}],

and the printed recipe is wrong by `det(g)^8`. It is worse than wrong by a constant: `g` is built
from an arbitrary basis of `ker v` and arbitrary preimages, so the printed recipe's output depends
on choices the theorem exists to quotient out; the correct recipe is `g`-independent.

I recorded, before looking, that if the pilot implemented the paragraph as printed then (a) all
six reconstructions would fail while every internal check passed, and (b) **the six failures would
share a single ratio `computed / sealed = det(g)^8`, one rational number common to both degree
families**. I wrote that (b) was the first thing I would test.

### 2.3 What the committed bytes say, and what my evaluator found

`analysis/b20_01_p2_reduction.py` (`5124cf7d…`) implements the paragraph as printed:
`d4 = pow(detg, 4, P)` and then `det_g4_times_sum_F=(d4 * sum(F[name].values())) % P` and
`det_g4_times_top=(d4 * TOP[name][0]) % P`. Its docstring item 3 repeats the wrong direction.
Notably `analysis/b20_01_flag.py` (`3236c787…`) states the covariance **correctly** in its module
docstring — "`z^{[n]}(Ytilde) = det(g)^4 z^{[n]}(Y)`". The error is in the two places that apply
it and in the report paragraph that specified them, not in the module that states it.

**Method: INDEPENDENT EVALUATOR.** `analysis/b21_10_p1_theoremA_factor.py` imports no project
code. Its only input is `results/b20_01/p2_reduction.json` at `878258f2…`, pinned by sha256
`6aa3e283f5d0bf39515656dc16375104530a8d651d2b809973c8028083beb812` (asserted in the script; equal
to the value tabulated in `b20_01_report.md` §11.7). From that file it takes **only the 60 raw
runner outputs** (`F_k[name][k].values_u1_to_5` and the `S_3` stage) and redoes everything
downstream in code written here: modular inverse, Gauss–Jordan, Vandermonde solve, normalisation.
No runner evaluation was performed and no producer script was executed or imported.

Results (`results/b21_10/p1_theoremA_factor.json`):

| check | outcome |
|---|---|
| `det_g^4` recomputed from `det_g_mod_P = 199728` | `471465`, equals the recorded `det_g4` |
| my Vandermonde extraction of `c_8..c_12` vs the pilot's, all nine `(name, k)` | **identical** for `c_11` and `c_12` |
| the six ratios `producer / sealed` | **all equal**, to the single value `432557` |
| `det(g)^8 mod P` | `432557` — the six ratios *are* `det(g)^8` |
| `det(g)^{-4} ·` (slice value) vs sealed, all six | **all six match exactly** |
| Theorem A (i) as an identity: slice `= det(g)^4 ·` sealed, all six | **true** |
| `S_3` control, my `F_2` against the pilot's `F_1` at the permuted point | sum `≡ 0 mod P` for all three; sign `-1` |

The corrected reconstructions, against the sealed rows:

| family | vector | slice value `Σ F_k` / `[u^12]` | producer's `det(g)^4 ·` | corrected `det(g)^{-4} ·` | sealed |
|---|---|---:|---:|---:|---:|
| deg 11 | `q3` | 187994 | 300999 | **86170** | 86170 |
| deg 11 | `q7` | 78184 | 497738 | **71919** | 71919 |
| deg 11 | `n02` | 14876 | 126141 | **226580** | 226580 |
| deg 12 | `q3` | 462650 | 491631 | **376209** | 376209 |
| deg 12 | `q7` | 139666 | 329212 | **469277** | 469277 |
| deg 12 | `n02` | 319220 | 279654 | **41046** | 41046 |

**Ruling on O1: Theorem A is PROVED. Its numerical control is PROVED-with-correction —
`det(g)^4` must be `det(g)^{-4}` — and, corrected, it PASSES on all six comparisons.**
The bookkeeping that is wrong is the *report's specification of the control* (§4.2, "Status of
Theorem A"), inherited verbatim by the pilot. The theorem's own bookkeeping — the `nu` signs, the
kernel construction, the node extraction, the `S_3` signs — is right, and the run exercised all of
it successfully. §10's diagnostic hint named the wrong suspect: `sign_convention_reconstruction`
and the `S_3` control had already discharged the sign half, and the `nu`-scale half is a
non-issue, because the `nu`-degree grading depends only on the splitting `W = W' ⊕ W_0` and not on
any scaling of a basis of `W_0`. The fault was the one place nobody looked: the exponent's sign.

**What this ruling is not.** It is a second lineage for everything *downstream* of the runner. The
60 evaluations themselves are still the producer's runner, so "the values are right" remains
single-lineage; what is now two-lineage is "the reduction reconstructs the sealed rows", and that
is exactly the claim the control existed to test. The sealed rows come from a different script
(`f1_new_point_minor.py`), so the comparison is genuinely between two computations.

### 2.4 Carried to C3 and C8

**C3 (the 15-evaluation cost).** The headline stands: a full degree-11-plus-degree-12 functional
costs `3 × 5 = 15` symmetrised runner evaluations against `3 × 13 = 39`. The parenthesis does not.
**[pre-formed, P1.2b]** Writing `P(u) = u^8(c_8 + c_9 u + c_10 u^2 + c_11 u^3 + c_12 u^4)`, the
four nodes `u = ±1, ±2` give four equations in five unknowns. The kernel is the degree-`≤ 4`
polynomial vanishing at all four nodes, `(u^2-1)(u^2-4) = u^4 - 5u^2 + 4`, i.e.
`(c_8..c_12) = (4, 0, -5, 0, 1)` — verified exactly over `Q` in pilot 1. Its `c_11` entry is `0`,
so the degree-11 value **is** determined; its `c_12` entry is `1`, so the degree-12 value **is
not**. Corollary A.1's "both give, in addition, the degree-12 value at the same point" is
**REJECTED** for the 12-evaluation variant. Label: C3 PROVED, with its parenthesis corrected.

**C8 (the 840–1050 count).** `70 × 3 × 5 = 1050` and `70 × 3 × 4 = 840` are both right as counts.
The two are not interchangeable: §5.1's clause "and the degree-12 rows come free at the same
points" is true of `1050` and false of `840`. Since the identity to be decided is the degree-11
one, `840` suffices for the decision itself and forgoes the degree-12 rows that would otherwise
serve as a control at the same points. Label: **C8 PROVED**, off CONDITIONAL, with that
distinction stated. The exceedance remains the user's.

## 3. O2 — the three unread citations

### 3.1 Seven routes to Bruns–Herzog, all failed

`Cohen–Macaulay rings` (Cambridge Studies in Advanced Mathematics 39, 1993) is a copyrighted
monograph, not on arXiv, and no legitimate route reached its text. Attempts, all read-only:
(1) a filesystem sweep of the user's tree for any Bruns/Herzog/Cohen–Macaulay file — nothing;
(2) a sweep of the repository for PDFs — four, none of them this book (and the three removed at
`d56bd2cd…` are Bipartite/BLMW/IP, not this); (3)–(6) four web searches for the numbered results
and their statements; (7) a fetch of the Cambridge Core book page, which returns the chapter
titles ("Chapter 1, Regular sequences and depth, pp. 3–56"; "Chapter 2, Cohen–Macaulay rings")
but not the subsection listing, behind a paywall. Two further fetches of papers that surfaced in
the searches found the book in their bibliographies but no citation by number.

**All three citations are therefore UNREAD in primary text, as they were for B20-10.** Under G9
and G14 that is the honest label and I keep it. What follows is what can be settled without the
book, which turns out to be most of what matters.

### 3.2 (T1) Bruns–Herzog Thm 1.6.17 — depth sensitivity: **condition LIFTED**

The statement B20-02 §6.3 attributes to it — for `f_1..f_n` in a Noetherian ring with
`grade(I) = g`, `H_j(f; R) = 0` for `j > n - g` and `H_{n-g} != 0` — is standard and correct; two
independent commutative-algebra sources surfaced in the searches state it in the same words
("the Koszul complex is grade sensitive, that is, if `grade(I, M) = g` then `H_{l-g}(y, M) != 0`
and `H_i(y, M) = 0` whenever `i > l - g`"). That is corroboration, not primary text.

More to the point, **Theorem 6.4 does not need the theorem.** It uses only the vanishing half, and
only in one instance. That instance has a short self-contained proof:

> **Claim.** Let `S = C[x_1..x_5]`, let `f_1..f_5` be forms of one degree with `I = (f_1..f_5)`
> proper and `grade(I) >= 4`. Then `H_j(f_1..f_5; S) = 0` for every `j >= 2`.
>
> *Step 1 (general linear combinations).* Suppose `g_1..g_{i-1}` is an `S`-regular sequence of
> linear combinations of the `f`'s, `i <= 4`. Then `grade(I, S/(g_1..g_{i-1})) >= 4 - (i-1) >= 1`,
> so `I` is not contained in any associated prime `p` of `S/(g_1..g_{i-1})` — if it were, every
> element of `I` would be a zerodivisor there. `Ass(S/(g_1..g_{i-1}))` is finite, and for each such
> `p` the set `{c in C^5 : Σ c_j f_j in p}` is a *proper* linear subspace of `C^5`. A finite union
> of proper subspaces over an infinite field is not everything, so a general `c` makes `g_i` a
> nonzerodivisor. Inductively, four general combinations `g_1..g_4` form a regular sequence.
>
> *Step 2 (change of generating sequence).* Extend to `g_5`, a fifth general combination, so that
> `(g_1..g_5) = h · (f_1..f_5)` for some `h in GL_5(C)`. A linear automorphism of the free module
> `C^5 ⊗ S` induces an isomorphism of Koszul complexes, so `H_j(f) ≅ H_j(g)` for every `j`.
>
> *Step 3 (one element at a time).* `K(g_1..g_5) = K(g_1..g_4) ⊗_S K(g_5)`, and since `g_1..g_4`
> is regular, `H_i(g_1..g_4) = 0` for `i >= 1`. The standard short exact sequence
> `0 -> H_j(g_{1..4})/g_5 H_j(g_{1..4}) -> H_j(g_{1..5}) -> Ann_{H_{j-1}(g_{1..4})}(g_5) -> 0`
> has both outer terms zero whenever `j >= 2`. Hence `H_j(g_{1..5}) = 0` for `j >= 2`. ∎

**Ruling: the (T1) condition on Theorem 6.4 is LIFTED.** Method: READ (the statement) plus an
INDEPENDENT proof of the instance used. Nothing in Theorem 6.4's all-`k` case now rests on an
unread citation for depth sensitivity. The *non*vanishing half (`H_{n-g} != 0`) is used only in
Corollary 6.5's last sentence about the padding side, which B20-02 already labels CONDITIONAL;
that label **stands**, unchanged.

Note the trade this makes: Step 1 is precisely the fact the GKZ packet attributes to Bruns–Herzog
1.5.12. It is proved above, so the record is better off by one citation and no worse by any.

### 3.3 (T2) Bruns–Herzog Cor. 2.1.4 — `grade = height`: **condition KEPT, exposure nil**

"In a Cohen–Macaulay ring, `grade(I) = ht(I)` for every proper ideal" is as classical as
commutative algebra gets and appears in every standard text; `S = C[x_1..x_5]` is regular, hence
Cohen–Macaulay. It is correctly applied in Lemma 6.3(e) and it is the step that converts the
geometric input (`dim V(J_F) = 1`, hence `ht(J_F) = 4`) into the algebraic input Theorem 6.4 needs
(`grade(J_F) >= 4`). I found no route around it that does not amount to re-proving it.

**Ruling: KEPT.** The citation is UNREAD and I do not pretend otherwise; but the exposure is nil,
and the correct label for it is not the same as the label a genuinely specialist unread theorem
would carry. See G14′ in §7. After §3.2, **Theorem 6.4's all-`k` case is CONDITIONAL on (T2)
alone**, where it was CONDITIONAL on (T1) and (T2).

### 3.4 Bruns–Herzog Prop. 1.5.12 — the GKZ Theorem B(iii) pointer: **condition KEPT; the fact
proved; the labelling defect stands**

B20-10 R15 found this an unlabelled load-bearing pointer inside the GKZ packet's Theorem B(iii).
I read it at its point of use (`claude_gkz_incidence_20260917/REPORT.md` at `82633a60`, line 145):
it is invoked "in the form 'an ideal of grade `g` generated by forms of one degree contains a
regular sequence of `g` general linear combinations of the generators'", to get
`(J_F)_k ⊇ (g_1..g_4)_k` and hence the `sigma(k)` bound. That statement is exactly Step 1 of
§3.2, which I prove there. B20-02 §9 correctly records that this slot does **not** use it.

**Ruling: the citation stays UNREAD; the mathematical fact is PROVED here, so no claim needs to
rest on the citation.** The R15 defect — that it appears in no literature table or manifest of the
packet that uses it — **stands unrepaired**, and cannot be repaired by editing the sealed GKZ
packet (G12). It needs a sibling corrigendum. That is producer work, not mine.

### 3.5 Dimca, the one primary source that *is* reachable

**Method: READ (primary).** I re-fetched `https://arxiv.org/pdf/1210.1795v4` into the session
scratchpad: 198,017 bytes, sha256
`20b96f5830291574137000073237b9081e134e45d52c89d9981996e5a83c9c05` — **byte-identical to B20-02
§1.1's pin and to the parent manifest's pin**. The pin resolves at review time (G9 satisfied).
The local environment has no PDF text library and no `pdftoppm`, so I read Remarks 3.5 and 3.6 in
full through the arXiv HTML rendering at `ar5iv.labs.arxiv.org/html/1210.1795`.

Two findings:

1. **B20-02's transcription is accurate.** Remark 3.5 does contain, verbatim, the sentence B20-02
   quotes: "we get nonzero terms only on the last two columns, which correspond to the Čech
   complex for `H^n(K^*(f))` (resp. `H^{n+1}(K^*(f))`)". That my rendering and B20-02's independent
   extraction of the pinned PDF agree word for word on this passage is itself the cross-check that
   the rendering corresponds to the pinned version at the point that matters.
2. **The two Bruns–Herzog numbers are unreconciled on this record.** Remark 3.6 reads: "recall
   that the first nonzero cohomology group in the Koszul complex is nothing else but the shifted
   canonical module … see **Theorem 1.6.16 page 50** in [1]". B20-02's (T1) cites **Theorem
   1.6.17**. B20-02 §9 tabulates both numbers — its Dimca row says "pointer to Bruns–Herzog Thm
   1.6.16", its (T1) row says "Thm 1.6.17" — without noting that they differ. This is not an
   error: adjacent numbered results in the same section are exactly what one expects, and the two
   facts are neighbours. But **neither number has been verified by anyone**, and a reviewer with
   the book should check both in one sitting. Recorded as a provenance note, not a defect in a
   claim. (Remark 3.6 also cites Bruns–Herzog Theorem 3.6.19 page 142 for graded local duality —
   a third number, not load-bearing here.)

## 4. The two hand computations nobody had replayed

### 4.1 B20-01 C9 — the Weyl-dimension count

**[pre-formed, INDEPENDENT (hand)]** P2, 00:32:43Z, written before §5.2's derivation was opened.

*The number.* From Corollary A.2, `F_1^z` depends on `(Z_1, Z_2, Z)` only through
`beta = Z_1^Z_2` and `gamma = Z_1^Z_2^Z` with bidegree `(3,1)`; the ambient is the multicone over
`Fl(2,3;U)`, whose bidegree-`(a,b)` coordinate ring piece is `S_lambda(U^*)` with
`lambda = (a+b, a+b, b)`, i.e. `(4,4,1)`. By the hook-content formula (contents `0,1,2,3 / -1,0,1,2
/ -2`; hooks `6,4,3,2 / 5,3,2,1 / 1`, product `4320`), at `u = 7` the numerator is
`(7·8·9·10)(6·7·8·9)(5) = 76,204,800` and the dimension is **`17,640`** — the producer's number, on
the nose, before I saw the derivation. Pilot 1 confirms it and computes the neighbours: `55,440`
at `u = 8` and `3,643,640` at `u = 13`. I also checked the producer's *own* Weyl-formula
computation as displayed in §5.2: its three row-products `35`, `504/5`, `5` are each right and
multiply to `17,640`. Two lineages for the number.

*The comparison.* `dim F^L_{-1} = 70` (Prop. C), and the slice method certifies vanishing of
*every* function of the type on the slice, never using `L`-covariance — so it must control
`17,640` dimensions where the covariant argument controls `70`, a ratio of `252`. The conclusion
that the density method cannot substitute for an explicit basis **follows**.

*Where the derivation is wrong.* P2.3 recorded, in advance, that "any transversal slice" asserts
`17,640` as a *lower bound*, that my own arithmetic makes the multicone over a 7-dimensional `V`
only `3·7 - 5 = 16`-dimensional against a required `34 - 17 = 17`, and that I expected one of
three things — (a) a wider class of slices, (b) an 18-dimensional `G'` on the flag cone, or
(c) the `>=` is loose and the true floor is `55,440`. **It is (c).** §5.2 item 2 writes the
transversality condition as `7 + 3m >= 34` (Levi only) and `17 + 3m >= 34` (full `G'`), which
compares `3m` — the dimension of the slice `cone(V^3)` inside `W'^3` — against `34`, the dimension
of the flag cone `S^`. The map `(Z_1, Z_2, Z) -> (beta, gamma)` has 5-dimensional fibres, which is
why `dim S^ = 3·13 - 5 = 34` and not `39`. Done consistently:

| ambient | Levi only (7) | full `G'` (17) | producer's `m` |
|---|---|---|---|
| in `S^`: `dim G' + (3m - 5) >= 34` | `m >= 11` | `m >= 8` | 9 and 6/7 |
| in `W'^3`: `dim G' + 3m >= 39` | `m >= 11` | `m >= 8` | 9 and 6/7 |

Both readings agree, and neither gives `m = 7`. The smallest transversal slice of the stated shape
is `m = 8`, and its function space is `dim S_{(4,4,1)}(C^8) = 55,440` — **`792` times the target,
not `252`**. The cost line changes with it: `55,440 × 15 ≈ 8.3 × 10^5` runner evaluations
(`~115 h`) rather than `2.6 × 10^5` (`~36 h`).

**Ruling on C9's counting: PROVED, with the floor corrected upward from `17,640` to `55,440`.**
The defect is in the justification of the word "any", exactly where P2.3 predicted it would be;
the load-bearing conclusion is strengthened, not weakened. `17,640` remains correct as what it
actually is: the dimension at `m = 7`, one dimension short of transversal.

### 4.2 B20-01 C9 — `U_-` mixes `z_{-1}` with `z_{-2}`: **CORRECT**, and a correction to my own
pre-verdict

§5.2 item 1's mechanism is right and I verified it: on an `F_1`-tuple, `Z_1 -> Z_1' + lambda nu_1`
adds `lambda nu_1 ^ Z_2 ^ Z ^ nu_2 ^ nu_3`, a `nu`-degree-3 term, so the 2-plane underlying the top
changes; on `S*` the same substitution is killed by `nu_1 ^ nu_2 ^ nu_3 ^ Z_1 ^ Z_2`, which is why
the degree-12 problem was `G'`-stable and the degree-11 one is not. **This is the structural
obstruction, not merely a cost problem**, and §5.2 presents it as one of two reasons rather than
burying it — my P2.4 worry that the report might present `17,640` as the only obstruction does not
bite, and I withdraw it.

**Correction to P2.4.** My pre-verdict asserted that "`z_{-1}` is the `nu`-degree-11 piece and
`z_{-2}` the `nu`-degree-10 piece". That is **wrong**. The grading is `arc_target` §6.1's
`gamma`-weight, in which `C(z) = (z_{-2}, z_{-1})` with `z_{-2}` the **top**, `nu`-degree 12, and
`z_{-1}` the `nu`-degree-11 piece (consistent with B20-01 §4.1's `C(q) = (q^{[12]}, q^{[11]})` and
§4.4's `F^L_{-1} = ((S_lambda W)_{#v = 11})^L`). I assumed `z_0` was the top and it is not. So the
report's "`U_-` mixes `z_{-1}` with `z_{-2}`" means degrees 11 and 12, which is exactly what its
own displayed top-type term produces, and the integrator's transcription ("mixes degrees 11 and
12", ledger §8.7) is right too. My structural reasoning — that the top is `U_-`-stable and the
degree-11 piece is not — survives the correction intact; my identification of the subscript did
not. The pre-verdict file is preserved unedited.

### 4.3 B20-02 Lemma 6.3 — **PROVED**

**Method: INDEPENDENT (hand), with every dimension recomputed in pilot 2.** I worked the proof
through and found no gap.

- (a) `grad det = cof`; it vanishes iff `rank A <= 2` and has rank one iff `rank A = 3`. Correct.
- (b) `d_i F(x) = <cof(A(x)), A_i>` by the chain rule, so `x in Sing X_F` iff `cof(A(x)) ⊥ Lambda`,
  which splits into `rank A(x) <= 2` and the tangency case. Correct; and both cases lie on `X_F`,
  as they must.
- (c) `Psi` fibres over the 14-dimensional smooth locus of `X_det` with fibre
  `{Lambda : C A ⊆ Lambda ⊆ T_A}` ≅ `Gr(4, 14)`, since `T_A` of the affine cone is the
  15-dimensional hyperplane `cof(A)^⊥`, which contains `A` by Euler. `dim Psi = 14 + 40 = 54 < 55
  = dim Gr(5,16)`: not dominant. Correct.
- (d) `dim Z_2 = 2(4+4-2) = 12`, so `dim P(Z_2) = 11`; `11 + 4 >= 15` gives nonemptiness by the
  projective dimension theorem; `Phi` is a `Gr(4,15)`-bundle over the irreducible `P(Z_2)`, hence
  irreducible of dimension `11 + 44 = 55`, and surjects onto `Gr(5,16)`, so the generic fibre has
  dimension `0`. Correct.
- (e) By Euler, `V(J_F) \ {0}` is the cone over `Sing X_F`, of dimension 1; `ht(J_F) = 4`;
  `grade = ht` by (T2). Correct.

Pilot 2 reproduces every one of these dimensions (`11, 14, 55, 40, 54, 44, 55, 0`) from the
formulas `dim Gr(k,n) = k(n-k)` and `dim Z_r = r(8-r)`; all checks true.

**One observation the packet does not make, in its favour.** Theorem 6.4 needs only
`grade(J_F) >= 4`, since it applies (T1) as `H_j = 0` for `j > 5 - g`. Step (d)'s *nonemptiness*
is what pins `grade` to exactly `4`; if `Sing X_F` were empty for a generic `Lambda`, `grade`
would be `5` and Theorem 6.4 would hold a fortiori. So Theorem 6.4 is robust to a failure of the
one step of Lemma 6.3 that uses the projective dimension theorem. That is worth having on the
record, because it means the two textbook dimension-theory facts of step (d) — themselves labelled
UNREAD in §9 — are not load-bearing for the theorem, only for the precise value `grade = 4`.

### 4.4 A coherence check that came free

Pilot 2 recomputes `rho_j(k)` from Lemma 6.1's alternating sum and compares with the certified
profiles. `rho_1(k)` for `k = 3..9` at `N = 5` is `5, 25, 75, 165, 300, 480, 710`; the certified
profile at the P2 pencil is `5, 25, 75, 165, 299, 475, 695`; the deficiencies are
`0, 0, 0, 0, 1, 5, 15`. These match the GKZ packet's independent statements exactly — `r_6(F_0) =
165 = rho_6 = 5·35 - 10` (its §3(ii)), `r_7 = 300` generic against `299` on `D45` (its §3.C), and
`def_3 = 1`, `def_2 >= 5`, `def_1 = 15` (its Remark 3.3). At `N = 5`, `rho_2(8) = 150` and the
padding rank `146` gives `dim H_2 = 4`, as reported. At `N = 16`, `dim K_2(8) = 120 · 136 = 16320
= rho_2(8)` (since `K_3(8) = 0`), `dim K_1(8) = 16 · 15504 = 248064`, `dim K_1(5) = 2176`, and
`16320 - 15660 = 660`, `16320 - 13490 = 2830` — every matrix size and every homology dimension
B20-02b reports reproduces. **Lemma 6.1 and the two packets' rank arithmetic: REPLAYED, consistent.**

## 5. Scope, under pressure, again

I checked every scope-sensitive statement the brief names, in committed bytes, and found no claim
stated above its evidence.

- **B20-02 Theorem 6.4's scope.** §6.5 is exact and honest: five variables; the rank-threshold
  reading only; and it names what is *not* covered — individual minors of size `<= rho_j(k)`
  vanishing on `D45` for a zero-pattern or support reason ("nothing is claimed about them either
  way"), the `GL_5`-module structure of `H_1(F)` beyond its dimension, sixteen variables,
  Candidate B. §0's "What this does not establish" repeats it. The unconditional certificate (L7)
  is separated from the all-`k` conditional statement (L6) throughout, including in §0's status
  paragraph. **Holds.**
- **B20-02b's scope.** `j = 2`, `k = 8`, `N = 16`, one computation, one lineage — stated in §0, in
  the pre-registered transcription sentence, in §4 ("Scope: `j = 2`, `k = 8` only; nothing is said
  about `k >= 9` or `j >= 3`"), in §5 and in the integrator's §8.6. C6 (monotonicity in `k`) is
  explicitly kept withdrawn: "two data points, `k = 7, 8`, are not a trend". The pre-registration
  in §1 was written before the run and the matching sentence was transcribed, not composed. I
  checked the one inferential step: `rank` is constant on the `GL_16`-orbit and semicontinuous on
  its closure, so the single evaluation at `det_4` does give `r^{(2)}_{Y_det}(8)`, and likewise at
  `z per_3` — the packet's appeal to the parent's Lemma 3.1 is sound. **Holds.** This is the
  best-disciplined packet of the four.
- **B20-01 pilot 3's `rank(C|_U) = 2`.** Correctly handled. A modular rank of an evaluation matrix
  is a floor on the rank over `Q` and never a ceiling, and the absence of a nonzero minor among
  sampled points proves nothing at all. §11.5 says so in its own verdict string ("MEASURED only,
  not a ceiling"), adds "not a proof that no nonzero `3x3` minor exists", and the ledger §8.8
  repeats it. The bare equality "`rank(C|_U) = 2`" in §11.5's first line is a slip, immediately
  qualified in the next sentence; not carried forward anywhere. The Schwartz–Zippel framing in §6
  is correctly labelled MEASURED evidence, with the honest note that the earlier fourteen
  functionals were at points where no such bound applies. **Holds.**
- **The four-achievements distinction.** Present in B20-01 §0 in full ("A necessary source
  condition, a coefficient equation, a separation and a positive multiplicity gap are four
  different achievements; this slot touches the first only"), and in operative form in B20-02 §0
  and B20-02b §4. **Holds.**
- **The `n02`/`q_3`/`q_7` orderings as data (G8).** Replayed; see §6. **Holds.**

## 6. G8 — the three certificates, and the text inconsistency

### 6.1 The certificates replay

**Method: REPLAY.** `analysis/b21_10_p2_certificates_and_lemmas.py`, no project code.

- All four input pins match: `q3_definition.json` `ac93ff59…`, `q7_definition.json` `07d066b8…`,
  `n02_ordering_hash.json` `34900ea6…` (the three §11.7 values) and the sealed
  `n02_definition.json` `ffeead80…` at archive commit `82633a60`.
- **The ordering hashes recompute.** For `q3` and `q7` I rebuilt the four-key object from each
  certificate's own bytes and hashed it under the scheme the file states (canonical JSON,
  `sort_keys`, separators `(",", ":")`); for `n02` I built it from the **sealed**
  `n02_definition.json`, as that certificate specifies. All three reproduce the recorded values
  `ae832e3d…`, `17b7d324…`, `61505bd5…`, which are also the values in report §11.3. The
  `n02_ordering_hash.json` file's own pin of the sealed certificate matches the file on disk.
- **The shipped data equals the report's prose.** The `pi`/`rho` blocks and both hand-plan orders
  in the two certificates equal, entry for entry, the §3.1 transcription in the report — a check
  worth making, because §3.1 was typed by a session that could not execute anything.
- **The shipped values equal the sealed values** quoted in §3 prose: `q_3` `260975, 509003, 336756,
  260012, 342025` and `185448`; `q_7` `301718, 423302, 275526, 317892, 384` and `288291`; and each
  certificate's own `P6_match` / `P7_match` replay flags are true with replayed equal to sealed.

**Ruling: G8 is discharged, and the three certificates are CERTIFIED-portable.** The D3 defect
that B20-10 R18 made a hard prerequisite is repaired. Phase 2 and Phase 3 may consume `q_3` and
`q_7` as data. Method: REPLAY of hashes and of the hash scheme; the underlying 12 runner
evaluations are the producer's and are not re-run here.

### 6.2 The §0/§2.2/§8 versus §11 inconsistency

The facts: §0, §2.2 and §8 item 2 of `b20_01_report.md` say G8 is **not** discharged and that no
certificate exists; §11.3 and `results/b20_01/MANIFEST.json` (`0e5fd026…`) say it **is** and bind
three certificates. §§0–8 were sealed by session B20-01 before any run and were deliberately not
edited by the completion session B20-01c, which recorded the change in §11 and in deviation D7.
The integrator ruled that §11 governs.

**Ruling: I affirm the integrator's ruling.** G15 says later corrigenda govern and that a sealed
report is never edited, and §11 is a later section of the same document, added by a later session,
which states its own scope ("This section is written by the execution session … It changes nothing
in §§0–8"). The artifacts agree with §11: the three certificates exist at the hashes §11.3 gives,
they replay (§6.1), and the manifest binds them. §§0–8 are an accurate record of what was true
when they were written, and are not to be edited by anyone.

One qualification, and it is the reason I would not leave this as a bare precedent. "A later
section governs an earlier one" is only safe when the later section says which earlier statements
it supersedes. §11 does this well for the Theorem A contradiction (§11.6 item C1 names the claim
and its ledger row) and **not at all** for G8: no sentence of §11 says "§0's G8 sentence, §2.2's
consequence list and §8 item 2 are superseded". A reader arriving at §0 has no pointer forward.
That is a G15 shortfall — "a withdrawal names every withdrawn sentence" — and the fix belongs in a
sibling corrigendum, not in the sealed report. See G15′ in §7.

## 7. Release gates for Phase 2

**G1–G4, G6, G7, G5′, G8–G18 stand** as written in `b18_10_review.md` §7 and `b20_10_review.md`
§§8–9. G8 is now *discharged* for `q_3`/`q_7` (§6.1) and continues to bind future certificates.
Rulings on the two proposed gates, and four additions.

**G19 — no unwrapped numerical run of any size: ADOPT, with the definition it currently lacks.**
The rule is right and its motivation is sound: B20-02's two unwrapped bisections reached a 735 MB
working set outside the Job Object, above the 512 MiB cap, and the cap is the only thing standing
between a diagnostic and the user's machine. But as written the rule is unbounded. Taken
literally it forbids `sha256sum`, `git show | wc -l`, and every packet's own seal script —
B20-01c's, B20-02b's `b20_02b_seal.py` and mine would all be violations, and B20-10's
`verify_layers.py` already was one. Adopt as:

> **G19.** No unwrapped execution of a program that performs mathematical computation on the
> objects under study — linear algebra, polynomial or modular arithmetic, evaluation, search,
> enumeration. Hashing, manifest generation, file listing, text extraction and read-only git are
> not numerical runs and need no wrapper; each still gets a line in the resource table. The pilot
> budget counts **launches, not scripts**: a retry, a crash and a cap hit each consume one, each
> gets its own unique run name (G10), and no receipt is overwritten.

I ran under this reading: three wrapped launches and nothing else that computes. The last clause
is not academic — one of my three launches was a crash of my own (§9 item 1).

**G20 — producer sessions run in default permission mode: NOT a gate; it belongs in the
handover, where it already is.** Every gate G1–G18 is a predicate on an artifact that a reviewer
can check from committed bytes. A session's permission mode is not: I cannot verify from
`b20_01_report.md` that B20-01c ran in default mode, only that it says so. A gate nobody can check
is a convention wearing a gate's clothes, and mixing the two weakens the ones that bite. It is
correctly placed in `BATCH20_CLOSE.md` §4 "standing changes" and in the launch-prompt template,
and it should stay there. What *is* checkable is the harm it prevents, so:

> **G20′ — a session that cannot execute says so at the point of every claim it could not test,
> and its slot is PAUSED, not COMPLETE, until the runs exist.** B20-01 did exactly this — §2.2 as
> the first honest negative, consequences stated where each bites, C10 OPEN, §9 empty, and the
> slot labelled PAUSED. That behaviour is why the record survived a session that lost execution,
> and it is what the gate should require.

Four additions, each traceable to a defect found above.

- **G21 — a control is specified as the identity it tests, not as a recipe.** O1's entire cost was
  that §4.2 wrote "reproduce the sealed rows from `det(g)^4 (F_1 + F_2 + F_3)`" — a solved-for form,
  typed, inverting the covariance the same section had just proved. A numerical control states the
  identity (`slice = det(g)^4 · full`); the solved-for form is derived from it, in the script, not
  transcribed into prose. Corollary: a control whose value depends on an arbitrary choice the
  theorem quotients out (here, the basis of `ker v`) is mis-specified by construction, and saying
  so is a one-line check any author can run.
- **G22 — an interpolation claim names what it determines and what it leaves free.** Corollary
  A.1's "both give, in addition, the degree-12 value" is false for its four-node variant. A claim
  that `n` nodes recover coefficients `c_{d_1}..c_{d_k}` exhibits the kernel of the node matrix, or
  states which coefficients are undetermined.
- **G23 — a dimension or transversality inequality names the ambient it is taken in.** §5.2's
  `17 + 3m >= 34` adds a group dimension and a slice dimension measured in `W'^3` to an ambient
  measured in `S^`, two spaces differing by the 5-dimensional fibre. Both sides of such an
  inequality are stated in one space, named.
- **G14′ — UNREAD is two labels, not one.** G14 currently gives the same label to an unread
  specialist theorem and to an unread pointer at a fact every textbook states. Distinguish
  **UNREAD-SPECIALIST** (the claim is CONDITIONAL and a reviewer must reach the text) from
  **UNREAD-CLASSICAL** (the fact is stated in three or more independent standard sources, the
  claim is ADOPTED-classical, and the citation number is a convenience). (T2) and Bruns–Herzog
  1.5.12 are UNREAD-CLASSICAL; Ballico 1995 (B20-10 R12) is UNREAD-SPECIALIST. Where two sources
  give different numbers for the same fact — 1.6.16 against 1.6.17 — both are recorded and the
  discrepancy is stated, as §3.5 does.
- **G15′ — a later section that governs an earlier one names the sentences it supersedes.** §11
  does this for Theorem A (§11.6 C1) and not for G8 (§6.2). The rule is G15's already; this makes
  explicit that it binds *within* a document, not only between documents.

**Stop gates for Phase 2 (unchanged, restated).** Stop a diagnostic slot when its three wrapped
pilots (60 s / 512 MiB, 180 s total) are spent without the named identity certified or refuted;
record PAUSED with reopening conditions. Do not describe a necessary-condition result as a gap; do
not describe the absence of a gap as the programme's failure.

## 8. Which Phase 2 slot the record supports

**Recommendation: (a) — the isotropic-type test of `B` (B20-01 §4.5(c), open item O5), one
pilot.** The condition the brief attaches to it is met: **Theorem A survives**, and survives with
its control now passing rather than merely unrun. §4.5(c) is the one mechanism the symmetry search
left testable — §4.5(a) closed the relabelling route with a reason, §4.5(b) is a constraint that
does not decide — and the packet prices it as cheap: the `half_tensor` routine of `direct_arc`
pilot 3 evaluates a covariant at a locus point in about 0.1 s, and the test is whether the `t` and
`s` parts of the four covariants have one or two nonzero type components on the flag locus, after
which the identity would follow from a rank computation on at most `10 × 2` numbers. It fits one
wrapped pilot with room to spare. It is a necessary source condition and nothing more, and the
slot's §0 must say so in the four-achievements form.

**On O4 (the Missing-Theorem run, ≈ 1,000 evaluations): its premises stand.** That is the whole
of my ruling; the exceedance is the user's decision, not mine.

- **Theorem A**: PROVED, control passing (§2). Off CONDITIONAL.
- **Proposition C**: PROVED. Its proof — elements of `F^L_{-1}` are `GL_5`-semi-invariant of weight
  `(4^5)`, are polynomials in the Plücker coordinates of `D` by the first fundamental theorem for
  `SL_5`, and are `diag(1, sigma)`-invariant, so Theorem A (i)–(iv) applies and gives
  `z_{-1} = 0 ⟺ F_1^z = 0` — is sound, and its two inherited premises are unchanged: `b_L(11) = 70`
  (PROVED in `arc_target` §5.1, inherited, not recomputed here) and the FFT for `SL_5` (ADOPTED,
  classical). I add no lineage to either.
- **The price**: `1050` evaluations if the degree-12 rows are wanted as a control at the same
  points, `840` for the degree-11 decision alone (§2.4). Quoting `840` *and* "the degree-12 rows
  come free" together is the one thing the launch prompt must not do.

**Not supported for a Phase 2 slot:** Candidate B (no stated escape from the direction reversal);
`d_2` at `k >= 9` or `d_j`, `j >= 3` at `N = 16` (sized, not priced in blocks); any cell-selection
carrier. I concur with `BATCH20_CLOSE.md` §4 on all three.

## 9. Honest negatives

1. **One of my three wrapped launches was a crash of mine.** `b21_10_p1_theoremA_factor` exited 1
   at 00:37:36Z: my `schur_dim` used the 1-based hook formula with 0-based indices. I fixed the
   line and relaunched under a **new** run name, `b21_10_p1r_theoremA_factor` (G10: the first
   receipt is not overwritten and is listed in §11). Two of my three launches therefore went to
   one pilot.
2. **Pilot 2 emitted 38 of 39 boolean checks true; the one false was mine.** I had hardcoded
   `rho_1(6) = 175` in an expectation array, forgetting the `-dim K_2(6) = -10` correction; the
   correct `165` is what the script computed and what the packets state. No finding is affected —
   the check caught my typo, which is what G16 is for. I have not edited the receipt.
3. **The three Bruns–Herzog citations are still unread by anyone**, after seven routes (§3.1).
   What I supply instead is a proof of the one instance Theorem 6.4 needs (§3.2); (T2) and 1.5.12
   are ruled classical on my own judgement, not on a reading.
4. **My reading of Dimca's Remarks 3.5 and 3.6 is from an arXiv HTML rendering, not from the
   hashed PDF bytes.** The PDF re-fetches to the exact pin, but this environment has no PDF text
   library and no `pdftoppm`, so I could not extract from the pinned bytes themselves. The
   cross-check that the rendering matches the pinned version at the passage that matters is
   B20-02's own independent quotation of the same sentence, which agrees verbatim.
5. **The 60 runner evaluations behind O1 are the producer's.** I re-derived everything downstream
   of them, not them. If the runner were wrong at this point, my check would not see it — though
   the sealed rows it reproduces came from a different script, which limits how that could happen.
6. **`b_L(11) = 70`, the `arc_target` dimension count, was not recomputed here**, nor was
   `dim F''`, nor any of B20-02's or B20-02b's ranks. Pilot 2 re-derives the *consistency* of the
   reported ranks with Lemma 6.1's formula (§4.4); it does not recompute a rank.
7. **The R15 defect stands unrepaired**: Bruns–Herzog 1.5.12 is still in no literature table or
   manifest of the GKZ packet that uses it. Only a sibling corrigendum can fix that, and that is
   producer work.
8. **Ballico 1995 (O3) was not attempted here.** B20-10 tried three routes and failed; I had no
   new one and did not spend the budget repeating it. C3 of the singular-locus theorem stays open,
   and every use of that theorem stays CONDITIONAL, exactly as B20-10 R11–R12 left it.
9. Nothing here bounds any `m_pad`, produces any `r`, nominates any cell, or claims any gap.

## 10. Closing ledger

Decisions are transcribed from this table only.

| id | statement | label | method | pre-formed? |
|---|---|---|---|---|
| R1 | Session state as §0; four packet documents read from committed bytes, all four hashes equal the `BATCH20_CLOSE.md` §2 prefixes | VERIFIED | REPLAY (hashes) | — |
| R2 | **Theorem A (i)–(v)** (B20-01 §4.2) | **PROVED** | READ, re-derived by hand | **yes (P1)** |
| R3 | The control specified in §4.2's "Status" paragraph and implemented in `b20_01_p2_reduction.py` inverts Theorem A(i): it uses `det(g)^4` where the slice-to-full direction needs `det(g)^{-4}`. All six comparisons are wrong by the single factor `det(g)^8 = 432557 mod 524287`, identical in both degree families and invisible to every internal check | **defect identified and named** | READ, then INDEPENDENT EVALUATOR | **yes (P1.2a), with the ratio predicted before looking** |
| R4 | With `det(g)^{-4}`, **all six sealed values are reproduced exactly** (86170, 71919, 226580; 376209, 469277, 41046), and Theorem A(i) holds numerically at P6 point 0 for both degree families and all three vectors | **Theorem A's control PASSES, corrected**; O1 CLOSED | INDEPENDENT EVALUATOR (pilot 1; my own extraction, inverse and normalisation from the 60 raw runner outputs) | — |
| R5 | §10's diagnostic hint (`nu` sign vs `adapted_scale_u`) named the wrong suspect; the `nu`-degree grading depends only on the splitting `W = W' ⊕ W_0`, not on any scaling of a basis of `W_0`, and the sign convention and `S_3` signs had already passed | hint REJECTED | READ + REPLAY | — |
| R6 | **C3**: the 15-evaluation price stands. Corollary A.1's "both give, in addition, the degree-12 value" is false for the four-node variant: the node kernel is `(4, 0, -5, 0, 1)`, `c_11` determined, `c_12` not | **PROVED, parenthesis REJECTED**; C3 off CONDITIONAL | INDEPENDENT (exact over `Q`, pilot 1) | **yes (P1.2b)** |
| R7 | **C8**: `1050` stands and delivers the degree-12 rows free; `840` decides the degree-11 identity alone and does **not**. §5.1's "the degree-12 rows come free at the same points" attaches to `1050` only | **PROVED**, off CONDITIONAL, with the distinction stated | READ + R6 | — |
| R8 | **Proposition C** (B20-01 §4.4) | **PROVED** on inherited `b_L(11) = 70` (`arc_target`, not recomputed here) and the FFT for `SL_5` (ADOPTED, classical) | READ | — |
| R9 | **C9's number**: `17,640 = dim S_{(4,4,1)}(C^7)`, the bidegree-`(3,1)` functions on the flag multicone over a 7-dimensional `V`; the producer's own Weyl-formula arithmetic is also correct | **PROVED, two lineages** | INDEPENDENT (hand, hook-content) + REPLAY (pilot 1) | **yes (P2, number derived before the derivation was opened)** |
| R10 | **C9's transversality inequality is wrong**: `7 + 3m >= 34` and `17 + 3m >= 34` add slice dimensions measured in `W'^3` to an ambient measured in `S^`, which differ by the 5-dimensional fibre. Consistently, `m >= 11` (Levi) and `m >= 8` (full `G'`), not 9 and 6/7; the true floor is `dim S_{(4,4,1)}(C^8) = 55,440`, i.e. `792 ×` the target, not `252 ×` | **PROVED-with-correction**; conclusion holds a fortiori | INDEPENDENT (hand) + REPLAY (pilot 1) | **yes (P2.3 predicted this branch by name)** |
| R11 | **`U_-` mixes `z_{-1}` with `z_{-2}`** (degrees 11 and 12 in `arc_target` §6.1's `gamma`-weight, in which `z_{-2}` is the top): correct, and it is a structural obstruction, not a cost problem. My pre-verdict P2.4 mis-identified `z_{-2}` as `nu`-degree 10; the reasoning survives, the identification does not (§4.2) | **PROVED**; pre-verdict corrected here, file unedited | READ | yes (P2.4), **partly wrong, corrected** |
| R12 | **B20-02 Lemma 6.3**: `Sing X_F = P(Lambda) ∩ P(Z_2)`, finite, nonempty, `grade(J_F) = 4`. Every dimension (`11, 14, 55, 40, 54, 44, 55, 0`) recomputed | **PROVED** | INDEPENDENT (hand) + REPLAY (pilot 2) | — |
| R13 | Theorem 6.4 needs only `grade(J_F) >= 4`, so Lemma 6.3's step (d) — and with it the two UNREAD textbook dimension-theory facts — is load-bearing for the value `grade = 4`, not for the theorem | robustness note | READ | — |
| R14 | **(T1) Bruns–Herzog Thm 1.6.17**: UNREAD in primary text (seven routes, §3.1). **Condition LIFTED**: the vanishing half Theorem 6.4 needs is proved here from `grade >= 4` by graded prime avoidance, invariance of Koszul homology under a `GL_5` change of the generating sequence, and the one-element short exact sequence (§3.2). The nonvanishing half, used only in Cor. 6.5's last sentence, stays CONDITIONAL | **UNREAD; condition LIFTED** | READ (statement) + INDEPENDENT proof | — |
| R15 | **(T2) Bruns–Herzog Cor. 2.1.4** (`grade = height` in a CM ring): UNREAD; classical; correctly applied. **Condition KEPT**, exposure nil. **Theorem 6.4's all-`k` case is now CONDITIONAL on (T2) alone** | **UNREAD-CLASSICAL; condition KEPT** | READ | — |
| R16 | **Bruns–Herzog Prop. 1.5.12**: UNREAD; read at its point of use (GKZ `REPORT.md` line 145, archive `82633a60`); the fact it names is proved here as §3.2 Step 1, so no claim need rest on the citation. B20-02 correctly records it as not used there. The R15 labelling defect — absent from the GKZ packet's literature table and manifest — **stands unrepaired**; only a sibling corrigendum can fix it (G12) | **UNREAD-CLASSICAL; fact PROVED here; packet defect stands** | READ + INDEPENDENT proof | — |
| R17 | Dimca arXiv:1210.1795v4 re-fetched; sha256 `20b96f58…` **equals** B20-02's pin and the parent manifest's, byte for byte; Remarks 3.5 and 3.6 read in full. B20-02's transcription of Remark 3.5 is **accurate, verbatim**. Remark 3.6 cites Bruns–Herzog **Thm 1.6.16 p. 50**; B20-02's (T1) cites **Thm 1.6.17**; B20-02 §9 carries both without reconciling them, and neither is verified | **PRIMARY (statement level, via the arXiv HTML rendering); pin RESOLVES at review time**; one provenance note | READ | — |
| R18 | **G8 discharged.** The three certificates' sha256 match §11.7; all three ordering hashes recompute from the certificates' own bytes (and, for `n02`, from the sealed `n02_definition.json`) under the stated scheme; blocks and orders equal the report's §3.1 prose; values equal the sealed values; the replay flags are true. `q_3`, `q_7` are CERTIFIED-portable; B20-10 R18's hard prerequisite is met | **CERTIFIED** | REPLAY (pilot 2) | — |
| R19 | Lemma 6.1's `rho_j(k)` reproduces every reported profile and derived quantity: `N = 5` `rho_1 = 5, 25, 75, 165, 300, 480, 710` against the certified `5, 25, 75, 165, 299, 475, 695` (deficiencies `0,0,0,0,1,5,15`, matching GKZ Remark 3.3's `def_3 = 1`, `def_2 >= 5`, `def_1 = 15`); `rho_2(8) = 150`, padding `H_2 = 4`; `N = 16` `rho_2(8) = 16320`, matrix sizes `16320 × 248064` and `2176 × 15504`, `H_2 = 660` and `2830` | **REPLAYED, consistent** | REPLAY (pilot 2) | — |
| R20 | Scope holds in all four packets: Theorem 6.4's exact scope (§6.5); B20-02b's `j = 2, k = 8, N = 16`, one computation, one lineage, C6 kept withdrawn, and its orbit/semicontinuity step checked; pilot 3's `rank(C\|_U) = 2` handled as a floor throughout (one bare-equality slip in §11.5, qualified in the next sentence, carried nowhere); the four-achievements distinction present. No claim stated above its evidence | **holds** | READ | — |
| R21 | **The G8 text ruling: §11 governs, the integrator's ruling AFFIRMED**, on G15 and on the artifacts. §§0–8 stand unedited as an accurate record of what was true when written. Qualification: §11 names the superseded sentences for Theorem A (§11.6 C1) but not for G8 — a G15 shortfall, repairable only by a sibling corrigendum | ruling | READ + R18 | — |
| R22 | **G19 ADOPTED with a definition** (numerical computation on the objects under study; hashing, manifests, listings and read-only git are not numerical runs; the budget counts launches, not scripts). **G20 is NOT a gate** — a permission mode is not checkable from committed bytes — and belongs in the handover, where it already is; **G20′** replaces it with the checkable requirement B20-01 already met | ruling | — | — |
| R23 | Gates for Phase 2: G1–G4, G6, G7, G5′, G8–G18 stand; **G19** as R22; **G20′**, **G21** (a control is the identity it tests), **G22** (an interpolation claim names what it leaves free), **G23** (a dimension inequality names its ambient), **G14′** (UNREAD-SPECIALIST vs UNREAD-CLASSICAL), **G15′** (a governing later section names the sentences it supersedes) added | ruling | — | — |
| R24 | **Phase 2 slot: (a)**, the isotropic-type test of `B` (B20-01 §4.5(c), O5), one pilot — Theorem A survives, so the condition is met. O4's premises (Theorem A, Proposition C) **stand**; its price is `1050` with the degree-12 control rows or `840` without; the exceedance is the user's decision, not mine. Not supported: Candidate B, `N = 16` at `k >= 9` or `j >= 3`, any cell-selection carrier | recommendation | — | — |
| R25 | Three wrapped launches, 0.040 s total of 180 s; peaks 13.37, 13.05, 13.81 MB of 512 MiB; exits 1, 0, 0; the exit-1 was my own bug, relaunched under a new name, receipt kept; no cap hit; no unwrapped numerical run; no lease; no cell nominated; no gap claimed | MEASURED | — | — |
| R26 | Wording items recorded, none changing a label and none to be quoted forward: §4.2(iii)'s "disjoint variable groups" (the groups share `Z_1, Z_2`); §4.2(iv)'s `s^4` for `s^12`; the `A Y A^{-T}` / `P Y P^T` notation; §11.5's bare `rank(C\|_U) = 2` | wording | READ | — |
| R27 | **For the housekeeping session, not for a label.** `.gitignore:51` ignores `results/logs/*.pid`, re-included only for `b15_*` (`.gitignore:74`). Every prior packet's `.pid` receipts are nevertheless committed (three at `878258f2`, one at `7de65d7c`, two at `6915ae6f`), so they were force-added. My three `b21_10_*.pid` are bound by this packet's manifest and are **currently ignored**; unless they are `git add -f`-ed, a fresh checkout will not contain files the manifest binds — a provenance break of exactly the kind G10 forbids | **action required at commit** | REPLAY (`git check-ignore -v`, `git ls-tree`) | — |

**Status: COMPLETE.** Phase 2 may open on this report. O1 is closed, O2 is reduced to one
classical condition and one packet-labelling repair, and O7 (producer-only status of every Batch
20 theorem) is discharged for exactly the items in this table and for nothing else.

## 11. Resources, footprint and manifest

Interpreter `..\B15-02\.venv\python.exe`, Python 3.12.10, sha256 `4d6f5f81…`; wrapper
`..\B15-02\analysis\b15_bound.py` sha256 `ca001081…` (working tree, CRLF; the committed LF blob is
`1f73ad8d…`, B20-10 R25); `PYTHONDONTWRITEBYTECODE=1` set in every launch shell;
`job_object_enforced: true` on all three. `Get-Process python*` returned nothing before the first
launch and before the last; no sibling `.pid` was live. One numerical job at a time, sequential.

| run | exit | wall | peak job memory | receipt |
|---|---|---|---|---|
| `b21_10_p1_theoremA_factor` | **1** (my bug, §9 item 1; not repaired in place, relaunched) | 0.014 s | 13,373,440 B | `results/logs/b21_10_p1_theoremA_factor_resources.json`, `.pid` |
| `b21_10_p1r_theoremA_factor` | 0 | 0.013 s | 13,045,760 B | `results/logs/b21_10_p1r_theoremA_factor_resources.json`, `.pid` |
| `b21_10_p2_certificates_and_lemmas` | 0 | 0.013 s | 13,811,712 B | `results/logs/b21_10_p2_certificates_and_lemmas_resources.json`, `.pid` |

Three of three wrapped launches used; 0.040 s of 180 s; no cap hit. **The three `.pid` receipts
above are matched by `.gitignore:51` (`results/logs/*.pid`, re-included only for `b15_*` at line
74) and will not be committed unless force-added; every prior packet's were. See R27 — this needs
one action from the housekeeping session, or the manifest binds files a fresh checkout lacks.**
Non-numerical, unwrapped and
declared under G19 as ruled in §7: read-only `git show`/`ls-tree`/`rev-parse`/`status`,
`sha256sum` on extracted bytes, one `curl` fetch of the Dimca preprint, six web searches and three
web fetches (§3.1, §3.5), and the seal script.

Write footprint (all new, nothing modified): `docs/b21_10_review.md`,
`analysis/b21_10_p1_theoremA_factor.py`, `analysis/b21_10_p2_certificates_and_lemmas.py`,
`results/b21_10/` (this manifest's file list), `results/logs/b21_10_*`. No sealed report, manifest
or packet was edited; no file of any other packet was touched. No git command beyond `rev-parse`,
`status --porcelain`, `log`, `show`, `ls-tree`, `cat-file` was run; no commit, no push, no fetch,
no stash.

`results/b21_10/MANIFEST.json` binds every file with sha256 — this report, both scripts, both
pilot outputs, the pre-verdict file, the six receipt files, and the pinned inputs (the four packet
documents at their commits, the four certificate files, `p2_reduction.json`, the Dimca PDF and
`BATCH20_CLOSE.md`) — and is written by a script that prints every count it writes into
`results/b21_10/SEAL_LOG.txt`. The manifest cannot bind itself or a log written after it; both
files say so. This document does not name its own hash.

**Disclosed:** the seal was run twice. The first run (00:59:02Z) sealed the report as it stood;
R27 and the two paragraphs it required were then added to this document, and the seal was re-run
so that the manifest binds the final bytes. No receipt was touched and no pilot was re-run between
the two seals; the only file whose hash changed is `docs/b21_10_review.md`. The seal script
(`b21_10_seal.py`, sha256 `c8f062ae0bdbe617f82a61f416d2bead030d3aae3571f89536b21be8471b6b6e`,
10,980 bytes) lives in the session scratchpad, outside the `analysis/b21_10_*.py` set it binds,
and is byte-identical across both runs.
