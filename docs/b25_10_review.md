# B25-10 — Independent review of the Batch 25 Claude packets, across all three papers

**Reviewer:** Claude, Opus 5 (1M context), model ID `claude-opus-5[1m]`. Worktree
`C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-10`, branch `b15-10-portable-witness`.
Session 2026-09-22, 14:34Z to 14:52Z (UTC).

**Status: UNCOMMITTED.** This review, `results/b25_10/preverdicts_formed_before_reading.md` and
`results/b25_10/MANIFEST.json` are local files. They count as evidence only after a separately
authorised delivery pass commits them. Nothing was published, committed or circulated.

**All decisions are in §10, the closing table.** Where §§1–9 and §10 differ, §10 governs.

---

## 0. State, method, and exposure

### 0.1 Repository state, recorded before any write

```
date -u                     2026-09-22T14:34:18Z
git rev-parse HEAD          ab2f8a407f5eac320c13d1eefca33c9b930ded86   (= baseline in the brief)
git rev-parse HEAD^{tree}   f44fecae7ceb243b7f9b879552c805c30f606454
git status --short          ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
no b25_10 path existed
```

The two 2026-09-13 receipts are pre-existing and are not mine. Git was used read-only
(`rev-parse`, `status`, `show`, `cat-file`, `diff`, `log`). HEAD at close is unchanged.

### 0.2 Method

The rules are those of B23-10 and B24-10: **committed bytes, not working trees**; every ruling says
whether it is READ, REPLAY or INDEPENDENT EVALUATOR (here, INDEPENDENT hand re-derivation counts as
independent); no sealed file is edited; producer verdicts are not adopted.

**Pre-formed risks and verdicts** are in `results/b25_10/preverdicts_formed_before_reading.md`,
in three appended blocks. Block 1 was written before any Batch 25 report, paper after-state or diff
was opened. Block 2 was written after reading B25-05 only. Block 3 corrects Block 2's timestamp,
which I had estimated rather than read (§9).

**Exposure, disclosed rather than backdated.** I was not a clean-room reader. Before Block 1 I had
seen (a) the integrator's launch prompt, which summarises several outcomes, and (b) this session's
auto-memory index, which holds one-line outcome notes written by the B25-01/02/04/05/06 producer
sessions. Both are listed in Block 1. **I treated the memory notes as a list of claims to check,
and none of them is a premise of any ruling below.**

**Delegation: none.** I read every byte I rule on myself. No subagent was used.

**Pilots: zero.** Every independent check below is a hand re-derivation or a read of a hashed
primary source. Administrative checks (hashing, `git apply --check`, `pdftotext` on the
integrator's PDFs) are not mathematical computation. No lease was taken and no `.pid` was
produced, so the missing `b25_10_` negation in `.gitignore` does not bite this slot (§9).

---

## 1. Delivery bindings — all verified from Git objects

Each hash below is SHA-256 of `git show <commit>:<path>`, the committed blob content, which I
computed myself. Every one matches the launch prompt's transcription.

| packet | delivery commit | path | SHA-256 (blob content) |
|---|---|---|---|
| B25-01 | `ddc7649ec43d87a86165b5acea608005d2ddbf44` | `docs/b25_01_report.md` | `b791ceb32707cc91abd29111281ee2f9b08b216ce844fd3359c030d944b16483` |
| B25-01 | same | `papers/det4-blindness/det4-blindness.tex` | `19e616cfb445ec36d16b7526a0972b8f4be52c05a1cb10df8d33da653082ff49` |
| B25-02 | `a480a0646d6d0aa0c5537e5f5d00661ae26bc050` | `docs/b25_02_report.md` | `0b976c69d629adcfd2fb7638dd9a09fb5664b8c6a542b282599935a462f1a25c` |
| B25-02 | same | `paper/det4-onset.tex` (raw CRLF, stored `-text`) | `39d15aeaf2d5eaaf3696f3250c9a95441dd92c3cda38f3a87f9f24cb3e79ebc5` |
| B25-02 | same | `results/b25_02/MANIFEST.json` (sealed, pre-repair) | `71c008fe10ed3496f1c10192e4ecce4ba8a1a746b2462cb998e99d564760b036` |
| B25-02 | same | `results/b25_02/REPAIR_SUPPLEMENT_20260922.md` | `ac3ee3a02b7ff3f0435f4258c93adf783be86d7a30dbb9840c7540adc394a0d3` |
| B25-03 | `241da4db9a274651da23f0df3cf2e8c0667732d4` | `docs/b25_03_report.md` | `fd1f0d93a23407f8f55f2d82ae342016a904c256573cba2be26262244087d01a` |
| B25-03 | same | `results/b25_03/MANIFEST.json` | `e476683e49221a24ff88f8702379ada3cb5ea8cf0c6e1cfc52ce56b3830e1607` |
| B25-03 | same | `paper/det3-conductor.tex` (LF blob, unchanged) | `f52f8d16a8d11d23a9f7ccd7ebc99dfb6d6fcf00b10ee3b128bb871034b4f866` |
| B25-04 | `92a7d054369a20854fd51685ee09ecb756344e8d` | `docs/b25_04_report.md` | `f6e14afdd7da6b2c7b3df340cce5d3571af864f14240abf82f6331edd6129a47` |
| B25-04 | same | `results/b25_04/MANIFEST.json` | `a33ab4dd19d5507e569870971ff1d835813ab2cd5cef96c48afb5de6b473edd9` |
| B25-05 | `2688efd1b5b14c78c11a9855e83357f4516cba54` | `docs/b25_05_report.md` | `38834c316c1b182e6acbe120b1608e3fb325c65e0f12790d0312e1c3a2373455` |
| B25-05 | same | `results/b25_05/MANIFEST.json` | `035ef6ead2033e64e847773efe7d0ddfb17108cf7d15d2b706cc424139c1a3fe` |
| B25-06 | `c740532b30acbcb25c84d15c5111ad4a06245e43` | `docs/b25_06_report.md` | `c2103a0aa3326cf622a026eff9ac8dc61bdb58b572fa7cb1279dee786b3091bb` |
| B25-06 | same | `results/b25_06/MANIFEST.json` | `88f5e8a7973d442f9d292d4c2268c1c515d349abcd1f432e8b94118c225bbedf` |

**Paper line endings.** Paper 2's committed blob is raw CRLF (`39d15aea…`). Stripping CR gives
`ec5b1b4d0724761a5f2027b8711986489967e0e0b5e8c5997299c0d8112748ed`, which is the integrator's
compiled source. Paper 1's `.tex` blob id is `975b59e9…` at both `bc7e62b7` and `241da4db`, so the
file is byte-unchanged. Paper 3's committed blob `19e616cf…` is LF and equals the compiled source.

**Build evidence** (`Claude_Handover_B15_B18/post_b19_housekeeping_20260917/build_evidence_20260922/`,
UNCOMMITTED integrator artefacts): `sha256sum -c SHA256SUMS.txt` passes for all 14 files. I read
the three `pass3` logs. Paper 3 is 24 pages, Paper 1 is 27 pages, and Paper 2 with the line-653
fix is 15 pages. None has an undefined reference or citation. The as-delivered Paper 2 log shows
exactly two errors, both at line 653. **These are integrator builds, bound to the right bytes.
They are not coordinator certification, and they are uncommitted.**

---

## 2. B25-05 and `(★)` — the label-changing result

### 2.1 What is claimed

B25-05 §A.3 states **Lemma R**. Let `f ∈ Sym^3(C^N)^*`, `X = closure(GL_N·f)` and
`X_r = closure Φ_f(Hom(C^r, C^N))`. Then for `ℓ(λ) ≤ r ≤ N`, the pull-back `ρ^*` along restriction
to `⟨e_1..e_r⟩` identifies both the highest-weight spaces and their ideal subspaces:
`K_{X_r} ≅ K_X`. At `N = 9`, `r = 7`, `f = det_3`, this carries LMR's ideal copy at
`λ = (19,7,2^5)`, `δ = 12` from `closure(GL_9·det_3)` to `D_7`, giving `i_det ≥ 1`.

### 2.2 My pre-registered risk, and why it does not bite

My central worry in Block 1 (R2) was that `N = 7 < n² = 9`, so `D_7` is not an orbit closure and
an inheritance argument written for orbit closures might not apply to it. **It does not bite.**
s73 §1 (`82633a60:docs/s73_report.md`, read) defines `D_7 = closure{det_3(Σ s_i A_i)}`, which is
exactly `X_7`. B25-05's step R5 uses only vanishing, never an orbit structure on `X_7`. This is also
the gap B25-05 identifies in the s26 write-up (`isotypic_rank.md` Prop. 5 appeals to its Lemma 2,
which is stated for orbit closures). I confirmed that Prop. 5 exists as stated, for `ℓ(λ) = r`
(`82633a60:docs/isotypic_rank.md` lines 116–147).

### 2.3 Independent re-derivation (hand, done before accepting)

- **Weights.** From `(g·F)(v) = F(g^{-1}v)`, a torus element acts on the coefficient function
  `c_α` by `t^α`. So weights are non-negative, `C[W_N]` is a polynomial module, and a monomial of
  weight `(λ, 0^{N−r})` uses only `c_α` with `supp α ⊆ [r]` (R1).
- **Raising operators.** Differentiating `F(y) ↦ F(y − t y_j e_i)` gives
  `E_ij c_α = (α_i + 1) c_{α+e_i−e_j}` when `α_j ≥ 1`, and 0 otherwise. So for `i ≥ r`,
  `E_{i,i+1}` kills every `c_α` with `α_{i+1} = 0`, hence the whole image of `ρ^*`. For `i < r` it
  commutes with `ρ^*`. Hence `H^N_{(λ,0)} = ρ^* H^r_λ` (R2).
- **Restriction.** `c_α(ρF) = c_{(α,0)}(F)`, so `ρ^* h̄ = h̄∘ρ` (R3).
- **Image of the orbit.** `ρ(g·f)(s) = f(Σ s_i g^{-1}e_i)`. The `A_i = g^{-1}e_i` are the first `r`
  columns of `g^{-1}`, which range over all independent `r`-tuples. Those are dense in `V^r`, so
  `closure ρ(GL_N·f) = X_r` (R4). This uses `r ≤ N`.
- **Kernel.** `h = ρ^*h̄ ∈ I(X)` iff `h̄` vanishes on `ρ(GL_N·f)` iff `h̄ ∈ I(X_r)`. Only vanishing
  is used (R5).
- **Multiplicity.** `X_r` is `GL_r`-stable, since precomposing a pencil with `g ∈ GL_r` gives
  another pencil. So `i = dim K` on both sides (R6).
- **The LMR input.** I read LMR arXiv:1004.4802v1 in my own extraction of the hashed PDF (§11).
  Thm 2.3.1 gives `Ω(k,d) = (d−1)(d−2)(k+2)ω_1 + (d(k+2)−2k−5)ω_2 + 2ω_{k+3}` in degree
  `(k+2)(d−1)`. At `k = 2n − 2 = 4`, `d = 3` (the Segre dual of §3.1) this is
  `12ω_1 + 5ω_2 + 2ω_7` in degree 12. With `|λ| = 36`, that is exactly `λ = (19,7,2^5)`.
- **One thing I found that the packets state only in part.** LMR §3.2's *general* display carries
  the ω_1 coefficient `n(n−1)(n−2)`, which is 6 at `n = 3` and gives size 30, not 36. The
  consistent coefficient is `2n(n−1)(n−2)`, and that is what Thm 2.3.1 yields. So the halving
  B24-10 recorded for Thm 1.0.2 is also in §3.2's general formula. B25-02's SOURCE_READING says so
  too. Neither paper cites the §3.2 general formula; both use Thm 2.3.1 and the printed `n = 3`
  example. **This is correct, and it should stay that way.**

The endpoint `ℓ(λ) = 7 = r` plays no special role: R1 needs only `λ_j = 0` for `j > r`. This settles
B24-10's §3.2(i) boundary question more strongly than B24-10 did.

### 2.4 Ruling

- **`(★)`, meaning the `N = 9 → 7` length-restriction statement of s73 §1, is PROVED.** It is
  `isotypic_rank.md` Prop. 5 (session 26), with its two implicit steps supplied by B25-05 Lemma R.
  Method: READ plus INDEPENDENT hand re-derivation of R1–R6.
- **C45 becomes PROVED.** Its one external input is LMR Thm 2.3.1 with §3.1 (Thm 3.1.1), whose
  `n = 3` instance §3.2 prints. That input is PRIMARY at statement level; its proofs are not
  audited. The ceiling `i_det ≤ 1` and `i_per = 0` are the s73 modular certificates, whose
  direction B24-10 §3.1–3.2 accepted.
- **Scope of the upgrade.** It covers the base rung `δ = 12`. Paper 3's ladder statement
  "`D = +1` for every `δ ≥ 12`" additionally uses s73's Lemma L and Proposition S. Those keep
  their existing record label and lineage, which Paper 3 already prints: "the computational half
  … still has no independent reviewer slot".
- **Renaming.** I endorse B25-05 §C: at every point of use, replace "`(★)`" with "the
  length-restriction lemma", so that it is not confused with the reducible-locus `(★)` of
  `stabiliser_reduction.md` §4.2.
- **B25-05's two corollaries are accepted.** `D = +1` also holds for the `GL_9` orbit closures,
  and LMR's unproved "only one copy" now follows from the record's own ceiling. The record should
  still not cite LMR for "only one copy".
- **Part B, outcome (c), is accepted on READ.** On `HWV_λ` every available group acts by scalars,
  and evaluation at a fixed finite point set is not equivariant. B25-05's M3 "vacuous" clause rests
  on the record value `sk = 10`, which I did not re-verify. The verdict (c) does not depend on it.
- **The `n = 4` sixteen-to-nine transfer in Paper 2 is NOT ruled on here**, as the launch prompt
  directs. For the record: my re-derivation above used no step specific to degree 3. The minimal
  certificate that would discharge Paper 2's "analogue of `(★)`" is a one-paragraph check that
  Paper 2's `D_9` in eq. (2.1) is the pencil closure `X_9` of `det_4` with `N = 16`, followed by
  Lemma R's hypotheses at `(d, N, r) = (4, 16, 9)`. Until someone checks that, the analogue flag
  stays.

---

## 3. Paper 3 — B25-01 at `ddc7649e`

I diffed `f95742ae` against `ddc7649e` for `det4-blindness.tex`: 1,133 lines became 1,209. I also
read `CLAIMS.md` (C11, C45, C51) and `GAPS.md` (G-15, G-37) at `ddc7649e`, and the built PDF text.

| item | check | finding |
|---|---|---|
| G-30 row 1 | Ruling C48 and its provenance; C24 provenance | C48: PROVED-kill **on elementary premises across `N = 5..8`**, and Kleiman is no longer an input to row 1. The `D(k)` sign is scoped to `k ≥ 3` and used for integer `k ≥ 10`; `D(0) = 25` and `D(1) = 10` are named. "**one control checked at three points**" appears, and the instrument check (5/5) is named. C24 says **INDEPENDENT hand re-derivation, not a code replay, no evaluator**. The GKZ Thm B label is unchanged. **Correct.** |
| G-31 C45 | C45 provenance | **PROVED modulo `(★)`**. Floor from Thm 2.3.1 with §3.1/§3.2, PRIMARY. Ceiling from the record's nullity. Thm 1.0.2 is named as not to be cited. The `N = 9 → 7` transport, the closed endpoint and the double pinch are all carried. G-37 is opened for `(★)`'s label. **Correct at delivery.** B25-01 did not pre-empt this review: it quarantined the memory note, and the paper does not drop the qualifier. |
| G-32 / C11 cap | abstract (iv), C11 (Thm 3.6), C34, §6.1 | All four uses read "**PROVED modulo** Kleiman (SECONDARY), Dimca (PRIMARY, statement level) and Gulliksen–Negård (SECONDARY), all three ADOPTED inputs". The only "ADOPTED modulo" left describes the superseded label. **Correct.** |
| G-36 D2′ | C51 in the source and in the built PDF | **Corollary 4.5** in the integrator's PDF: I extracted the text and it reads "Corollary 4.5 (C51; D2′, the pure-power witness)", followed by Fact 4.6 (C17) and, later, Proposition 4.21 (C49). The witness `x^n` is named in the statement, with `A_1 = I_4` for `x_1^4 ∈ D45` in the image. It follows from D2 alone; D1 is a premise only of the `b_F` item. It is called a **witness exclusion, not a mechanism exclusion**, and the escape route is stated. "Same kind and scope" is withdrawn. **Correct.** One precision: the sentence "no closed `GL_N`-stable condition on which `Q` holds contains `Det_n`" does not actually need closedness (it follows from `x^n ∈ Det_n`). Closedness is needed only for the last sentence, which the statement does carry. This is harmless. |
| G-A1 | Question 6.5 | Unchanged. It is Question 6.5 in the built PDF and still the principal open question. **OPEN.** |
| Scoping | all right-way-corner sentences (source L123, L207–208, L710, L900–901, L1075–1076) | Each is restricted to the determinant part, with the boundary named as open. **Preserved.** |
| Cubic `Σ_Π` | onset inequality, L836 | `deg f ≥ onset I(D_35 ∪ Σ_Π)`. **Preserved** (cubic side, not `T2`). |
| Baseline sentence | L96 | "no five-row determinant equation *known* to be nonzero on padding". **Preserved.** |
| Author line | L73 | `\author{Swami Sethuraman}`, the same text as before. |
| Build | integrator log | 24 pages; no undefined reference or citation; one harmless font-shape warning. |

**Paper 3 verdict: PROCEED.** The delivered after-state is correct and conservative. Its next step
is one edits-only pass, authorised by this review's §2.4 and bounded to the following:

- C45 / Theorem 8.1: "PROVED modulo `(★)`" becomes "PROVED". The provenance names the
  length-restriction lemma (`isotypic_rank.md` Prop. 5, B25-05 Lemma R @ `2688efd1`, B25-10 §2).
  LMR Thm 2.3.1 + §3.1 stays as the one PRIMARY external input.
- Rename `(★)` at L128–129, L215–216, L1036, L1054–1063 (§8) and L1095–1099 (§9 item 4).
- Close G-37. Update the `BIB.md` LMR entry (iii)'s last sentence.
- The ladder above `δ = 12` keeps its s73 lineage wording.

After that pass comes a recompile and the author's circulation decision. The pass is recommended
before circulation but is not a correctness defect: the delivered label is true, only weaker.

---

## 4. Paper 2 — B25-02 at `a480a064`

I diffed the LF renderings of `0019b2e2` and `a480a064`. The real change is `+433/−151`, which
matches the launch prompt. I read the abstract, §1's status paragraph, Prop. 6.1, Thm 6.2 and
Remark 6.3, Thm 7.1's heading, Cor. 5.3, Thm 9.1 with its proof, and §9's frame, `n = 3` control,
length-nine paragraph and `[−4,−2]` paragraph.

### 4.1 B2 — does the repair of Theorem 9.1 stand? **YES.** READ + INDEPENDENT hand re-derivation

The new Theorem 9.1 keeps the degree-free claim separate from the degree-bounded one, which is the
whole point of the repair.

1. **Item 1, `Δ ≤ 0` for `ℓ ≤ 4` in every degree.** For `k ≤ 4`, `P_k = R_k ⊆ D^det_k`. A
   containment gives a surjection `C[D^det_k] ↠ C[P_k]` of `GL_k`-algebras, so
   `mult C[P_k] ≤ mult C[D^det_k]`. No degree enters. **PROVED**, given Thm 3.1 (washout, a
   Jacobian-rank density certificate) and Prop. 6.1.
2. **Item 2, `i_det = 0` for `ℓ ≤ 3`.** `D^det_k = Sym^4 C^k` for `k ≤ 3`. **PROVED**, given the
   codimension table for `k = 3`; `k ≤ 2` is elementary.
3. **Item 3, `ℓ = 4` only for `δ ≤ e − 1`.** I re-derived each step:
   - `D^det_4` is irreducible of dimension 34 in 35, so it is a hypersurface.
   - Its ideal in the UFD is principal, generated by an irreducible `g` spanning a `GL_4`-stable
     line.
   - That line is a character `det^m`, and since `4m = 4e`, `g` spans `S_{(e^4)}`.
   - So `I_δ = 0` for `δ < e`, and `i_det((e^4), e) ≥ 1`. This is B24-10 §5.1's refutation of the
     old statement, now written into the theorem.
   - `e ≥ 10`: rank = `a` at `((δ^4), δ)` for `δ = 4, 6, 7, 8`, and `a = 0` at the other
     `δ ≤ 9`. A modular rank attaining `a` is a certificate over `Q`. This is CERTIFIED on the
     record's ranks, which I READ and did not replay.
   - `e = 320112` is **ADOPTED** from LLV and is kept separate.
4. **Item 4.** `Δ = −(a − mult R_k)` on that range is algebra. The two `Δ = −1` cells are READ
   record values.

**The old blanket statement is gone.** The paragraph after the proof says it plainly: equality
holds "at length four only below the onset `e`". The §1 summary and the built PDF (Theorem 9.1(1),
(2)–(3)) say the same.

### 4.2 The reversed Prop. 6.1 inequality — **the correction is right**

At `0019b2e2` Prop. 6.1 printed `R_r ⊆ D^det_4, hence mult C[R_r] ≥ mult C[D^det_4] and Δ ≤ 0`.
**That displayed inequality points the wrong way.** Containment gives `≤`, and `≥` would give
`Δ ≥ 0`, which contradicts its own conclusion. The target was also mistyped as `D^det_4`. The
after-state prints `R_r ⊆ D^det_r, hence mult C[R_r] ≤ mult C[D^det_r]`. **Correct.**

**This is a finding against B24-10, and I record it here (see also §8).** B24-10 §5.1 argued
"`Δ ≤ 0` follows from Prop. 6.1, a containment". That argument is sound because it used the
containment, but B24-10 did not notice that the inequality printed in the proposition was reversed.
B25-02 found it (its N1).

The proof now cites Beauville Cor. 6.4 (cubic surfaces) and independently a Jacobian-rank-20
density certificate. Beauville (1.9) supports the "does not extend to `r = 5`" sentence. I read
both passages myself in the hashed PDF (§11); **they say what they are cited for.**

### 4.3 Theorem 6.2 and the new B17-01 dependency — **correctly downgraded; one label precision**

The paper's own argument proves only the **determinant part**: actual determinants in `W` form a
set of dimension ≤ 31 < 35. It cannot give `R_5 ⊄ D^det_5`, because `D^det_5` is a closure. B25-02
retitled the theorem and moved the closure statement to a separate, labelled dependency. **That is
a withdrawal of an unsupported "unconditional", and it is right.**

The dependency is `B17-01` (`01c49022:docs/b17_01_report.md`). I read its opening. Its headline
claims more than the record uses: **"if `C` is smooth … `lC ∉ D_{4,5}`" for every smooth cubic**.
B23-03 §4 (`3bcad666`, read) carries it as "B17-01-C's `F* ∉ D45` (ADOPTED) excludes one specific
`C*` only". Paper 2 uses the narrow reading, one smooth witness. **Paper 2 and Paper 3 therefore
agree.**

Two precisions are required:

- **Label.** In this record, "adopted" normally means taken on an external source's authority.
  B17-01 is a record-internal producer result. The paper should say so where it is used, for
  example "a separate, unpublished result of this programme, carried as ADOPTED on the programme's
  record". The locator `\cite{Companion2}` ("Singular matrix spaces and the length-five
  non-containment, technical report") must actually contain the `s_5·C*` witness, or the citation
  must change. That is an [AUTHOR]/locator item.
- **A flag for the record, not for Paper 2.** If B17-01's general statement were accepted, it would
  answer G-A1 negatively for smooth cubic factors. The reason the record reads it narrowly is not in
  any input delivered to me, and **I did not audit B17-01**. Nothing may cite B17-01's general form
  until a review settles it. Whoever next works on G-A1 should record why it is read narrowly.

### 4.4 B3, B4, B1, cap label, Beauville, attribution, notation, build

| blocker | check | ruling |
|---|---|---|
| B3 (gate) | §9 L959, "honest frame" L971–982 | "`ℓ(λ) ≥ 5`". Length five is "not excluded". The washout is an interpretation, not an impossibility. Counts are 4,198 / 2,734 / 2,571. **Repaired.** |
| B4 | L1100 | `Δ ∈ [−4,−2]`, "certified conditional on the adopted value 73 … (not proved here)". `Δ = +1, 0, −1` are excluded. The uncommitted `[−4,−3]` is not used. **Repaired.** |
| B1 | Cor. 5.3 against **KL arXiv:1204.4693v1 Thm 1.3, read by me in the hashed PDF** | KL: "`I_d(F_{n−m}(S^nW))` contains the isotypic component of `S_πW` … for all `π` with `p_1 < d(n−m)`." At `n − m = 1` the whole component is in the ideal, so `mult C[R_r] = 0`. The after-state says exactly that, and "omits every variable". **B1 CONFIRMED at the primary source (PRIMARY, independent read) and REPAIRED.** This closes B24-10 ruling 5.6's honest negative. |
| Cap label | Thm 7.1 heading; abstract; §1 | Heading: "proved modulo Kleiman (read-status SECONDARY), Dimca [Thm 3.1] (PRIMARY, statement level) and Gulliksen–Negård (SECONDARY), all adopted". The abstract has moved the cap out of "We prove:" into "We also prove, modulo three adopted inputs from the literature". **Repaired, and consistent with Paper 3.** |
| Beauville | Prop. 6.1 (Cor. 6.4, (1.9)); SOURCE_READING §1 | PRIMARY for both uses (independently re-read, §11). B25-02's negative, that Beauville contains none of Prop. 2.1's dimensions, Thm 7.1 Step 2 or Thm 7.3, is READ, not independently checked. **Accepted.** |
| LMR uses | §1, §9 (L1010, L1053, L1062, L1114) | Thm 1.0.1 for `dc̄`; Thm 2.3.1 + Thm 3.1.1 + §3.2's `n = 3` example for the floors. Thm 1.0.2 is explicitly not used. **Consistent with Paper 3.** |
| `n = 3` control | L984–1030 | "proved modulo one premise, `(★)`". Floor and ceiling are separated. **Correct at delivery.** After §2.4 it may read PROVED. |
| `n = 4` transfer | L1058–1062 | "the `n = 4` analogue of the premise `(★)` … we do not separate the two here". **Keep the flag** (§2.4, last bullet). The clause "we do not separate the two" should become "the `n = 3` case is proved (B25-10 §2); the `n = 4` case is not yet checked". |
| Coefficient eq. / separation / gap | length-nine paragraph | Kept distinct. The nine-row kernel equation is nonzero at 282 padded points, so it separates **as a single equation**; that separation rests on LMR plus the `n = 4` transfer. Yet `i_pad ≥ 3` gives `Δ ≤ −2`, so there is no multiplicity gap. **Correct, and consistent with the five-row baseline**, because this is a nine-row cell. |
| Build | integrator logs | As delivered: **2 errors at L653**, a nested `\cite[..]` in a theorem optional argument. The committed state carries the integrator's one-line brace. I verified that the committed LF bytes differ from the as-delivered LF bytes **only** at L653, and only by the braces. That is typesetting, not mathematics. Now 0 errors, 15 pages. |

**Paper 2 verdict: REPAIR (bounded).** The B2 repair, the Prop. 6.1 correction, B1/B3/B4, the cap
label and Beauville are **accepted**. The paper is not ready. The minimal remaining repairs, none
of which needs new mathematics:

- (i) Precise wording and a real locator for the B17-01 dependency (§4.3).
- (ii) The `n = 3` control may drop its qualifier. The `n = 4` sentence is rephrased as in the
  table.
- (iii) The [AUTHOR] items B25-02 lists: the Companion/Companion2 locators (B14), the B16
  acknowledgement, and whether Paper 2 may cite B23-03 at all.
- (iv) The Paper 2 / Paper 3 overlap question (BLOCKERS §2), which was out of scope.

B25-02's other dispositions (B5–B16) are READ and not individually re-derived, except where the
table says otherwise.

---

## 5. Paper 1 — B25-03 at `241da4db`

| claim | my check | ruling |
|---|---|---|
| Six paths bound | B25-03 §2 tables; `git diff --stat bc7e62b7 241da4db` | The tex and README are unchanged; the blob `975b59e9…` is identical. CHANGES/GAPS/READINESS/ATTRIBUTION_PATCH have additions only. **Bound.** |
| `b911a151…` | `git show bc7e62b7:paper/det3-conductor.tex \| sed 's/$/\r/' \| sha256sum` | **= `b911a15184ebf819…`.** It is the CRLF rendering of the committed blob. **B24-10 ruling 11.4.7 ("resolves to NOTHING") was wrong in its conclusion** (§8). |
| LMR Prop. 3.5.1 | **read by me** in my own extraction of the hashed LMR v1 PDF, §3.5, lines 560–590 | "`P` belongs to the orbit closure … `GL(W)·P` is an irreducible codimension one component of the boundary … not contained in `End(W)·[det_n]`", with `n` odd. **CONFIRMED at PRIMARY, statement level.** The stabiliser step ("one can check") is not audited. |
| `n = 3` identification with `P₂` | independent hand check | `Pf_1 = a_23`, `Pf_2 = a_13`, `Pf_3 = a_12`, and `Σ s_ij Pf_i Pf_j` expands with coefficients `2s_12, 2s_23, 2s_13` on the cross terms. The linear change `x_1..x_9 = (a_23, a_13, a_12, s_11, s_22, s_33, 2s_12, 2s_23, 2s_13)` is invertible on `M_3 = Λ^2 ⊕ S^2` and maps it term by term to the universal quadric. **PROVED, elementary. The paper's sentence (L732–741, which states "For odd `n`") is accurate.** |
| "awaits one signature" | B25-03 §4.2 | **WITHDRAWN, and I agree.** Four items remain: the signature, a compile of the signed paper, G-P4, and read-statuses for IK/Kumar/Hüttenhain. The integrator's clean 27-page build covers the **unsigned** bytes only. |
| Attribution unapplied | grep at `241da4db` | `Cor.~7.2]{BI}` occurs **0** times; "no computation" is at L176 and L560. **Unapplied. CERTIFIED from bytes.** |
| Author credit unchanged | L40 | `\author{Swami Sethuraman}`, blob unchanged. **Confirmed.** |
| Patch usable | `git apply --check` of the committed `attribution_patch_extracted.diff` (`ea80adeb…`) against a scratch copy of the blob | exit 0. **Usable.** |
| §5.3 wording flag | B23-10 §4.3 (`239dd6e8`, read, lines 410–424) against the patch's intro hunk (L134, L161) | B23-10 ruled that "the case of Cor. 7.2 … in which no admissible set exists" is **not** Prop. 4.1. The patch's intro hunk says "in which no admissible family exists at all". **The flag is correct.** B24-10 §4.6 missed it (§8). **The §6 alternative ("no family of `δ` distinct `D`-subsets exists at all") is required, not optional**, because the intro would otherwise re-assert a ruled-out equivalence. This is my ruling; applying it remains the author's act. |

**Paper 1 verdict: PROCEED to the author's signature decision**, with these conditions: take the
§6 wording at the intro hunk, choose the Cor. 4.2 form, then compile the signed bytes, then settle
G-P4 and the three B24-01 read-statuses. Readiness is **not** one signature; it is four items. No
author-credit change is authorised or made.

---

## 6. Cross-paper consistency

| item | Paper 3 (`ddc7649e`) | Paper 2 (`a480a064`) | agree? |
|---|---|---|---|
| Cap label | PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), GN (SECONDARY), all three ADOPTED | the same three with the same read-statuses, "all adopted"; abstract "modulo three adopted inputs" | **Yes** |
| C45 / `n = 3` control | PROVED modulo `(★)` | proved modulo `(★)` | **Yes**; both may now read PROVED (§2.4) |
| LMR citation | Thm 2.3.1 with §§3.1–3.2; never 1.0.2 | Thm 2.3.1 + Thm 3.1.1 + §3.2 example; not 1.0.2 | **Yes** |
| Five-row baseline | "no five-row determinant equation *known* to be nonzero on padding" (L96) | no five-row claim; `I(D_5)` measured empty through degree 7 | **Yes** |
| Equation / separation / gap / bound | kept distinct (abstract; §8) | kept distinct (the nine-row paragraph) | **Yes** |
| G-A1 / closure | OPEN, Question 6.5 | closure statement ADOPTED via one witness; G-A1 OPEN | **Yes**, on the narrow B17-01 reading (§4.3) |
| B25-05 result through a paper edit | not applied | not applied | **Correct**: neither paper silently accepted it |

---

## 7. The research packets

### 7.1 B25-06 (`c740532b`): **PROCEED as a scoped partial result. G-A1 stays OPEN. Gates no paper.**

- **Scope, checked.** Theorem 1 covers `B1 ∩ P5` and its closure; it explicitly does not cover
  `closure(B1) ∩ P5`. That is the precise intersection-versus-closure statement. The "order
  exactly one" wording matches `B1`: `val = 1` forces `det M_0 ≡ 0` and a leading coefficient of
  `tr(adj M_0 · M_1)`.
- **Independent re-derivation (hand).**
  - Case (i), constant kernel: `F` is the determinant with column 4 replaced, so `F ∈ D45°`.
  - Case (ii-a) with `a = 2`: two quadrics on `P(N) ≅ P^2` have a common zero.
  - **The skew-bordered case (ii-b, `a = 3`), the one the producer asks a reviewer to redo.**
    `κ ∝ (c_4 u, −u·c')` and `F = c_4 u^TBu − (u·c')(r·u) ∈ I_L^2`. For `l = u_1`, the
    `c_4 ∈ span(u)` sub-case reduces to `c'^v` or `r^v = (f,0,0)`, and `C` is singular at the zero
    of `f` on `L`. In the `c_4 ∉ span(u)` sub-case, `C = c_4T − c̃(r·u) ∈ (c_4, c̃)`: `C` contains a
    plane or is divisible by `c_4`. **All hold.**
  - Proposition 3: a finite stabiliser gives an orbit of affine dimension 25.
- **READ only:** the `a = 4` sub-cases and the structure lemma's `rank P = 2` branch.
- **Labels.** Theorem 1 is **PROVED modulo B23-03 Thm 2.1** (producer; reviewer re-derived the
  cases listed above; the rest READ). Theorem 2 is **CONDITIONAL**, as labelled; the rank-≤2
  classification (Atkinson–Lloyd / Eisenbud–Harris) is UNREAD. Proposition 3 is **PROVED modulo
  Matsumura–Monsky** (UNREAD-CLASSICAL).
- **Paper effect: none now.** Paper 3's Question 6.5 provenance may later cite Theorem 1 as
  partial progress, after an author decision. That is not required.

### 7.2 B25-04 (`92a7d054`): **PROCEED as a scoped no-go.** A25-10 owns the construction and convergence audit

- **Lemma A** (the component factorisation from BDI eq. (5.2)) and **Theorem B** (a product lies
  in the prime ideal, so some factor does, and that factor is nonzero on `P_r`) re-derive by hand.
  Theorem B is **PROVED modulo primality of `I(D_r^{det_n})`**. Corollary B's "≤ 7 vertices" also
  depends on the record floor `D* ≥ 8`, which I READ.
- **Cheap evaluation is not treated as separation.** §6 of B25-04 separates evaluation cost,
  generator count, independent functions, sampled rank (a floor), membership proof and nonvanishing.
- The deterministic membership grid `(dn+1)^{(r−1)n²} = 41^{100} ≈ 10^{161}` checks: the degree in
  each variable is at most `dn`, over `(r−1)n² = 100` variables.
- The surviving corners are stated as OPEN: spans (the `xy − zw` example) and connected
  small-treewidth fillings.
- **Not reviewed here:** the pilots' code and outputs, BDI at the primary, and the convergence
  question with A25-02/05. Those belong to A25-10.

### 7.3 B25-05 (`2688efd1`): **PROCEED.** See §2.

---

## 8. Corrections to my own B24-10 (`ab2f8a40`), recorded rather than hidden

| B24-10 ruling | correction | found by | verified by me |
|---|---|---|---|
| 11.4.7: "`b911a151…` resolves to NOTHING" | It is the CRLF rendering of `bc7e62b7:paper/det3-conductor.tex`. The binding was recoverable; B24-10 hashed only LF blob content. The conclusion "UNBOUND" is **withdrawn**. The G29(b) lesson stands: say which bytes a hash names. | B25-03 §2.3 | yes (§5) |
| 11.4.6: the patch "meets all three qualitative requirements" | The intro hunk reintroduces "no admissible family", which B23-10 §4.3 rejected. B24-10 checked only that BI is credited. | B25-03 §5.3 | yes (§5) |
| 11.5.2: "`Δ ≤ 0` … follows from Prop. 6.1, a containment" | The argument is right, but Prop. 6.1 as printed at `0019b2e2` displayed the **reversed** inequality and the wrong target (`D^det_4`). B24-10 missed the defect in the proposition it cited. | B25-02 N1 | yes (§4.2) |
| 11.3.8: "`(★)`'s own label is not established" | **Now established: PROVED** (§2.4). | B25-05 | yes (§2.3) |
| 11.5.6: B1 "ADOPTED on B24-06's assessment" | **Confirmed at the primary source** (KL Thm 1.3). | B25-02 and this review | yes (§4.4) |

---

## 9. Honest negatives and limits

- **Not audited:** LMR's proofs (Thm 2.3.1, 3.1.1, the Prop. 3.5.1 stabiliser); s73's modular
  certificates, the `a`-ladder and Prop. S / Lemma L; `sk = 10`; B17-01 as a whole; B17-03; LLV
  (READ through B25-02); Dimca, Kleiman and GN (record statuses carried); BDI; B25-04's pilots;
  B25-06's `a = 4` sub-cases; B25-02's B5–B16 dispositions beyond §4.4; `PAPER2_*` and `CLAIMS.md`
  beyond the rows named.
- **The `n = 4` sixteen-to-nine transfer is not ruled on** (§2.4).
- **No PDF was produced by me.** Build evidence is the integrator's, bound by hash, and uncommitted.
- **A timestamp error of my own.** Block 2 of the pre-verdict file claims 14:50Z. It was actually
  written before 14:41:03Z. Block 3 corrects it without editing Block 2.
- **Gate note.** `.gitignore` at HEAD negates `b16_10_` through `b24_10_` `.pid` receipts, but not
  `b25_10_`. This slot produced **no `.pid`**, so nothing is ignored that should be committed.
  I did not edit `.gitignore`.

---

## 10. Closing decision table (governing)

PROCEED means ready for the **stated next step** only. It authorises no publication, no
author-credit change and no Git mutation.

| object | decision | exact reason | minimal repair / next step | remaining author / delivery / publication decisions |
|---|---|---|---|---|
| **B25-05** `(★)` / Lemma R | **PROCEED — `(★)` PROVED** | Lemma R R1–R6 re-derived by hand; `D_7` is the pencil closure by definition; only vanishing is used; the LMR weight checks | none; rename `(★)` to "length-restriction lemma" at points of use | delivery of this review |
| **C45** (unpadded `n = 3`, `δ = 12`, `λ = (19,7,2^5)`) | **PROVED** (label moves from "PROVED modulo `(★)`") | the floor is LMR Thm 2.3.1 + §3.1 (PRIMARY, statement level) transported by Lemma R; the ceiling and `i_per = 0` are s73 certificates | ladder `δ > 12` keeps its s73 lineage | — |
| B25-05 Part B (equivariance) | **PROCEED — outcome (c)** | scalars on `HWV_λ`; fixed point sets are not equivariant | none | — |
| **Paper 3** (B25-01 @ `ddc7649e`) | **PROCEED** | all five edits trace to committed sources; C51 = Cor. 4.5 in the built PDF; scoping, `Σ_Π`, the five-row baseline and the author line are preserved; built clean | one edits-only pass: C45 → PROVED, rename `(★)`, close G-37, BIB LMR (iii); recompile | circulation (user); delivery of the pass |
| **Paper 2** (B25-02 @ `a480a064`) | **REPAIR (bounded)**; B2 repair **ACCEPTED** | Thm 9.1 is the three-clause statement plus item 4; the Prop. 6.1 reversal is correctly fixed; B1 is confirmed at KL; B3, B4, the cap label and Beauville are right; the L653 byte edit is typesetting only | (i) the B17-01 wording and a real locator; (ii) `n = 3` control → PROVED, `n = 4` sentence reworded; (iii) the `n = 4` transfer stays flagged until the §2.4 check | [AUTHOR]: Companion locators (B14), B16 credit, whether to cite B23-03, Paper 2/3 overlap; circulation |
| **Paper 1** (B25-03 @ `241da4db`) | **PROCEED to the author's signature decision** | the six paths are bound; LMR Prop. 3.5.1 is confirmed PRIMARY; the `n = 3` identification is proved by hand; "one signature" is withdrawn; the patch is usable and unapplied; the author line is unchanged | use the patch's §6 wording at the intro hunk (**required**); then compile the signed bytes; settle G-P4; read-statuses for IK, Kumar and Hüttenhain | the signature and the Cor. 4.2 form (author); circulation |
| **B25-06** (G-A1 boundary) | **PROCEED as a partial result (outcome 3)** | Theorem 1 is scoped exactly (`B1 ∩ P5`); the longest case is re-derived; Theorem 2 is CONDITIONAL | next certificate as B25-06 §6: an order-two analysis over the two primitive types | none; gates no paper |
| **G-A1** | **OPEN** | no reviewed result closes it; B17-01's general statement is unreviewed and read narrowly | record why B17-01 is read narrowly; see §4.3 | — |
| **B25-04** | **PROCEED as a scoped no-go (outcome 2)** | Lemma A and Theorem B are re-derived; costs are kept separate | none from B25-10; construction and convergence belong to A25-10 | — |
| **B24-10 corrections** | **recorded** (§8) | 11.4.7 withdrawn; 11.4.6, 11.5.2, 11.3.8 and 11.5.6 amended | — | — |

**No cell was nominated, no gap was claimed, no worker was requested, and no pilot was run.**

---

## 11. Source and method ledger

**Primary sources read by me in this session.** Each was fetched from arXiv at 14:41Z into the
session scratchpad, hashed, and converted with `/mingw64/bin/pdftotext -layout`.

| source | version | PDF SHA-256 (bytes read) | text SHA-256 | used for | status |
|---|---|---|---|---|---|
| LMR, *Hypersurfaces with degenerate duals and the GCT program* | arXiv:1004.4802**v1** | `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79` (= record) | `148e24b0451f84e8f3158e1f74d64ca44ffd5ca994874b3545b9651c5e433bd2` | Thm 2.3.1; §3.2 (general formula and `n = 3` example); Prop. 3.5.1 with its construction and first proof step | **PRIMARY**, statements; proofs not audited |
| Kadish–Landsberg, *Padded polynomials, their cousins, and GCT* | arXiv:1204.4693**v1** | `599486883d141d224fd40155ff9533b09d500cc48c2f5281e10ab49636e1e7cd` | `8aaed3563100405fb64cd358d1df072cf24313e358c552863de7d05e832589b0` | Thm 1.3, first assertion (B1) | **PRIMARY**, statement |
| Beauville, *Determinantal hypersurfaces* | arXiv:math/9910030**v2** | `1ba560a5634f2ae15b94c6c2b3979308debaf2f96941edea7a0fd5adc98eb586` | `8b699cac97e1695463633a9fe432672c15c854ce868dff7e98ce0ec7d193ebcc` | Cor. 6.4; (1.9) | **PRIMARY**, statement |

My PDF digests and text digests are identical to those B25-02 recorded, which is an
extraction-level cross-check.

**Record inputs read from committed blobs:**
- `82633a60`: `docs/s73_report.md` §0–§1 and `docs/isotypic_rank.md` §3.
- `5a97317e:results/b24_02b/lmr_quotes.md` Q1, Q5–Q7.
- `3bcad666:docs/b23_03_report.md` §4.
- `01c49022:docs/b17_01_report.md` (opening only).
- `239dd6e8:docs/b23_10_review.md` §4.3.
- `ab2f8a40:docs/b24_10_review.md` §§0, 3, 5, 6, 11.
- The six delivered reports in full: B25-01, 02, 03, 04, 05, 06.
- `a480a064:results/b25_02/SOURCE_READING.md`.
- Paper 3 before/after tex, `CLAIMS.md`, `GAPS.md`; Paper 2 before/after tex; Paper 1 tex, patch
  and diff.

**Administrative inputs (UNCOMMITTED):** the B25-10 brief, CLAUDE_COMMON, COMPUTE_PROTOCOL,
SOURCE_INDEX, the live B25-12 ledger (read, not edited), and the launch prompt
`B25_REVIEW_LAUNCH_20260922.md`.

**Method per ruling:** stated in each row of §§2–7. READ where not marked. INDEPENDENT means my own
hand re-derivation or my own primary read. **No REPLAY** of any producer program. **No
INDEPENDENT EVALUATOR** program.

**Tool memory.** I consumed the session's memory index as context only; it is disclosed and
quarantined in Block 1. I created **one** memory note after this review was written; it records
the outcome and is not evidence.

## 12. Resources, files, manifest

- **Pilots: 0 of 3. Mathematical compute: 0 s. Lease: not requested.**
- **Created (all UNCOMMITTED):** `docs/b25_10_review.md` (this file),
  `results/b25_10/preverdicts_formed_before_reading.md` and `results/b25_10/MANIFEST.json`. The
  manifest hashes the first two and not itself.
- **Nothing else in the repository was modified.** No prior review, packet, paper, ledger or
  `.gitignore` was touched. Scratchpad files (PDFs, text extractions, paper renderings, a
  disposable copy for `git apply --check`) are outside the repository.
- Git was read-only. HEAD `ab2f8a407f5eac320c13d1eefca33c9b930ded86` is unchanged. **Delivery
  status: UNCOMMITTED, pending a separately authorised explicit-path delivery pass.**
