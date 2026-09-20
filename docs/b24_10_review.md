# B24-10 — Independent review of the seven Batch 24 packets, and gates for Batch 25

**Reviewer:** Claude, **Opus 5 (1M context)**, exact model ID `claude-opus-5[1m]`, default
permission mode. Worktree `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-10`, branch
`b15-10-portable-witness`.

**All decisions are transcribed from §11, the closing ledger.** Where an intermediate section and
§11 differ, §11 governs. Sections 1–10 are the working; §11 is the record.

---

## 0. State, method, and what I actually did

### 0.1 Repository state, recorded before any write

```
git rev-parse HEAD          239dd6e84417ab04914a8d84cca02ddf754bf1fb
git rev-parse HEAD^{tree}   3008235a92bf10a108ae673564d879a5716b4a1d
git status --porcelain      ?? results/b24_10/
                            ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
                            0 tracked changes
```

Both 2026-dated `results/logs/` items are the pre-existing residue the brief names; they are not
mine and they stay out. Git was read-only throughout: no commit, no push, no fetch. No producer
session was running; `Get-Process python*` returned nothing before the single pilot launch.

### 0.2 Method, inherited verbatim

The rules are B20-10 through B23-10's, as `docs/b23_10_review.md` §0 states them at `239dd6e8`:
verdicts formed **before** reading a deliverable's own defence, marked as such and preserved
byte-for-byte; **committed bytes**, not the working tree; every verdict says whether it is READ,
REPLAY, or INDEPENDENT EVALUATOR; later corrigenda govern; no sealed report is edited.

**Pre-formed verdicts are in `results/b24_10/preverdicts_formed_before_reading_v3.md`**, 25,193
bytes, appended in four blocks as they were formed (§1 priority 1; §2 priority 1's sizing,
extrapolation and basis; §3 priority 2; §4 priority 3), each timestamped, none edited afterwards.
§1 and §2 were written **before `preverdicts_formed_before_reading_v2.md` was opened** and before
any packet was opened, as the brief directs. §3 and §4 were written before `docs/b24_05_report.md`,
`docs/b24_02_report.md` and `docs/b24_02b_report.md` were opened. Where the bytes overturned a
pre-verdict, §10 says so and the wrong reading stays visible in `v3`.

**Delegation: none.** I read every byte ruled on below myself. No subagent, no delegated reader, no
summariser. B24-04's caught gloss is the reason; I took the warning literally.

### 0.3 What I read, replayed, and evaluated

| packet | what I did |
|---|---|
| B24-01 | READ the six committed paths at `bc7e62b7`; INDEPENDENT check of the tree for a packet; hashed the `.tex` at four commits |
| B24-02 | READ §1, §2.3, §2.4, §4.2–§4.4; READ `analysis/b24_02_p1_n5_kleiman.py` lines 22–48 for byte order; REPLAYED the closed forms and the three negative controls (pilot 1, block B) |
| B24-02b | READ §1, §2.1–§2.4, §3.1–§3.4 |
| B24-03 | READ `CLAIMS.md` (50 rows), `GAPS.md` §E, and the relevant passages of `det4-blindness.tex`; INDEPENDENT derivation of the §6 environment numbering; INDEPENDENT arithmetic on C50's boundary (pilot 1, block C) and C35's dimensions (block D) |
| B24-04 | READ §2.1–§2.5, §3.4, §4.2, §4.5; INDEPENDENT EVALUATOR on the sizing law and its extrapolation (pilot 1, block A); re-derived Theorem 1's proof step by step by hand |
| B24-05 | READ §1.2 in full; re-derived D1, D2 and D2′ by hand |
| B24-06 | READ `PAPER2_BLOCKERS.md` §0, B2, B3, B4, and the blocker list |
| integrator | READ `docs/b24_12_ledger.md` and `docs/b23_12_ledger.md` at `744eb77b` |

**Hash verification.** Every pinned deliverable in the brief's table hashes as stated. I verified
all seven by `git cat-file` at the pinned commit:

```
bc7e62b7:paper/det3-conductor.tex               f52f8d16a8d11d23…
f8273c35:docs/b24_02_report.md                  cf09c536cf1fb4ab…   (brief: cf09c536…) ✓
5a97317e:docs/b24_02b_report.md                 3ecb611a38933232…   (brief: 3ecb611a…) ✓
f95742ae:papers/det4-blindness/det4-blindness.tex  ab69ccbe6cc79dec…  (brief: ab69ccbe…) ✓
aafcbb69:docs/b24_04_report.md                  3d24884a82d47e73…   (brief: 3d24884a…) ✓
5c5ba86e:docs/b24_05_report.md                  e13ad0f1d8cab936…   (brief: e13ad0f1…) ✓
0019b2e2:PAPER2_BLOCKERS.md                     00e3ebbeccfda6d2…   (brief: 00e3ebbe…) ✓
```

The two files already in `results/b24_10/` hash as the brief's table states, both verified before
being relied on: the 561-byte fragment `683d3880…` and the 7,438-byte `v2` `bd5ea242…`. **I edited
neither.** Both are bound in the manifest.

### 0.4 Pilots, and one gate defect found

**One wrapped pilot of the three allowed**, `b24_10_p1_arith`, 0.003 s of a 60 s cap, 512 MiB cap,
`PYTHONDONTWRITEBYTECODE=1`, exit 0. Exact rational arithmetic only — `fractions.Fraction` and
`math.comb`; **no floats in any comparison**, no randomness, no project code imported. Output
`results/b24_10/p1_arith.json`. Two pilots unspent. The three negative controls of priority 3(d)
needed no pilot beyond this one: they are closed-form arithmetic and I replayed them by hand first.

> ### **negation missing for `b24_10_`**
>
> `.gitignore:51` ignores `results/logs/*.pid`. The file carries negations
> `!results/logs/b16_10_*.pid` through `!results/logs/b23_10_*.pid` — one per slot-10 batch, every
> batch from 16 to 23 — and **the series stops at `b23_10`**. So
> `results/logs/b24_10_p1_arith.pid` is ignored, while
> `results/logs/b24_10_p1_arith_resources.json` is not. Verified with
> `git check-ignore -v`. The `.pid` receipt of this slot's only pilot cannot be committed without
> a new negation line. **I did not edit `.gitignore`** — that is a delivery decision, not a
> reviewer's. It needs one line before this slot's receipts are staged.

`docs/b24_10_review.md` and `results/b24_10/*.json` are **not** ignored; `git check-ignore`
returns 1 for each.

---

## 1. Priority 1 — B24-04's tail theorem, the sizing, the extrapolation, the basis

### 1.1 The tail theorem — **PROVED**. Method: READ + independent hand re-derivation of every step

**Pre-formed (v3 §1): CONDITIONAL on three named conditions.** I pre-registered that the statement
as the brief prints it is incomplete in a specific way, and named exactly what the proof would have
to supply. **All three conditions are met by the committed bytes.** The ruling converts to PROVED.

Theorem 1 at `aafcbb69:docs/b24_04_report.md` §2.2 is not the brief's elliptical statement; it is
a three-part theorem with a corollary, and it proves what the brief's summary leaves out. Taking my
three pre-registered conditions in turn:

**(C1) The factorisation must hold for weight vectors — spans — not merely for monomials.**
**Met, and this is the step the proof gets right.** The proof does not argue about one monomial and
extend by hope. It fixes the monomial basis of the `λ`-weight space (multisets `{α_1,…,α_d}` with
`Σ α_i = λ`), shows `Σ_i |ᾱ_i| = Σ_{j≥2} λ_j = t`, and concludes that since each `α_i` with
`ᾱ_i ≠ 0` contributes at least 1 to a total of `t`, **at least `d − t` of the `α_i` equal `n e_1`**.
So *every basis monomial* is divisible by `c_{n e_1}^{d-t}`, and therefore so is every linear
combination of them. I re-derived this by hand and it is correct. The report then upgrades the
count to a bijection (delete exactly `d − t` copies of `n e_1`; add them back), which is
well-defined precisely because at least `d − t` copies are present, and which gives (i)'s equality
of dimensions. The report is explicit that this "is B23-06's Lemma 2.3 upgraded from a count to a
map" — an honest statement of what is new.

The report also anticipates the span question directly, in the first of its two remarks: *"Theorem 1
is about arbitrary weight vectors, not only highest weight vectors, which is why it is stated that
way."* That is the right thing to have noticed and the right place to say it.

**(C2) `c_{n e_1} ∉ I(D_r^{det_n})` must be established, not assumed.** **Met, with two explicit
witnesses.** The proof exhibits them: on `D_r^{det_n}`, `c_{n e_1}(F) = det_n(A_1)`, nonzero at
`A_1 = I`; on `P_r`, an explicit substitution gives `c_{n e_1} = 1`. My pre-verdict called the
omission of this condition "a named omission in the statement". It is — **but the omission is in
the brief's summary, not in the packet.** The packet supplies both non-memberships before using
primality. I record this as a correction to my own pre-verdict, not as a finding against B24-04.

**(C3) `D*` must be an onset minimised over the whole class, not weight-indexed.** **Met.** §2.1
defines `D* := min { deg f : f ∈ I(D_r^{det_n}), f|_{P_r} ≠ 0 }` — a minimum over all separating
`f` with no weight index anywhere. So `deg g = t` gives `t ≥ D*` immediately, and the descent
cannot leak across weights. My pre-registered risk does not materialise.

**The corollary's case split is complete and correct.** If `t ≥ d`, then `t ≥ d ≥ D*` because `f`
itself is separating of degree `d`. If `t < d`, then `D* ≤ t` by (iii). Either way `t ≥ D*`. And
the reduced object `g` has tail `t` and degree `t`, so tail equals degree — which is what makes
§2.4's search space finite. No induction is needed and none is used; my pre-verdict said I would
not count its absence as a gap, and I do not.

**One observation of my own, which is not a defect and which the packet is entitled to.** Part (ii)
is stated as an **iff**, and the corollary uses only one direction. In the used direction —
`f` separating ⟹ `g` separating — the vanishing half needs primality of `I(D_r^{det_n})` together
with `c_{n e_1} ∉ I`, and the non-vanishing half is free, because an ideal absorbs multiplication:
`g ∈ I` would force `f = c^{d-t}g ∈ I`. **Irreducibility of `P_r` and `c_{n e_1}|_{P_r} ≠ 0` are
needed only for the unused direction**, where one must multiply two functions nonzero on `P_r` and
know the product is nonzero, i.e. that the coordinate ring of `P_r` is a domain. So the hypothesis
set the corollary actually consumes is strictly smaller than the hypothesis set the theorem
announces. My pre-verdict guessed that one of the two invoked hypotheses was inert; it is not inert
— it earns its place in (ii) — but it is **not load-bearing for the conclusion the record uses**.
Stating a clean iff and proving more than is needed is good practice, and I flag this only so that
a later reader who wants to weaken a hypothesis knows which one is free.

**Ruling: PROVED.** Elementary, self-contained, correct as written. The brief's one-sentence
summary of it is incomplete — it invokes primality without the non-membership that makes primality
useful, and it does not say `D*` is un-indexed — and **the summary should not be quoted in place of
the theorem.** That is a transcription warning, not a finding against the packet.

### 1.2 The sizing `N_S ≈ 0.060 · t⁴` — **MEASURED (a fit), valid on `t = 12…24`.** Method: INDEPENDENT EVALUATOR (pilot 1 block A) + READ

**Pre-formed (v3 §2.1): MEASURED at best, and I expected to rule it a fit, not a law.** That is
where it lands, and the packet says so itself.

The four measured pairs at `n = r = 5`, minimised over four-part tails, are
`(12, 1189), (16, 3829), (20, 9492), (24, 19921)`. **I recomputed `c(t) = min N_S(t)/t⁴` exactly as
rationals and all four printed constants reproduce to the digit:** `0.0573, 0.0584, 0.0593,
0.0600`. B24-04's arithmetic is correct.

Three findings the packet does not make, all from exact arithmetic:

**(i) The constant has not converged. It is still climbing at the top of the fitted range.**
`c(t)` is strictly increasing across all four points, with decreasing increments. Fitting
`c(t) = c_∞ − a/t` on the widest-separated pair `(12, 24)` gives
**`c_∞ = 10409/165888 ≈ 0.062747`**, which is `1.0040 ×` the value `1/16 = 0.0625`. Every other
pair agrees to three digits. So `0.060` is not the asymptotic constant; it is the value at the last
sampled point of a sequence that is still rising.

**(ii) The drift runs upward, which strengthens the report's conclusion rather than weakening it.**
`c_∞ · 900⁴ = 4.117 × 10¹⁰` against the report's `0.060 · 900⁴ = 3.9366 × 10¹⁰` — **4.6 % higher**.
The true price, on this fit's own terms, is slightly *larger* than the report claims. A reviewer's
finding that a producer's number is conservative is still a finding, and it is the good kind.

**(iii) The structural justification does not carry the constant, and read carelessly it is a
two-order-of-magnitude trap.** §2.4 argues the exponent structurally: the argmin `(t−3,1,1,1)` puts
almost all the tail on one coordinate, where the count is governed by partitions into parts of size
`≤ n = 5`, "which grow like `t^{n-1}/((n−1)!·n!)`". The exponent that argument gives, `n − 1 = 4`,
is right and is the reason the quartic form is more than curve-fitting. **But the constant that
closed form carries is `1/(4!·5!) = 1/2880 = 0.000347`, and the measured constant is `0.060` — a
ratio of 172.9.** A reader who takes the printed closed form as the law and evaluates it at
`t = 900` gets `2.28 × 10⁸`, not `4 × 10¹⁰`: **wrong by a factor of 173, and in the dangerous
direction, because it makes the programme look reachable.** The formula governs the growth *order*
of a related count, not the value of `min N_S`. It should be written as supporting the exponent
only, with the constant explicitly flagged as measured and not derived.

**Ruling: MEASURED, a fit on `t = 12…24`.** The exponent `4` is structurally supported and may be
carried outside the range as a *form*; the constant `0.060` is measured, unconverged, and may not.

### 1.3 The `≈ 4 × 10¹⁰` at tail 900 — **EXTRAPOLATION, and the label alone is not sufficient.** Method: INDEPENDENT EVALUATOR (pilot 1 block A)

The brief asks three things. I answer them in order.

**(a) Is the figure independent of the sizing law, or is it that law at `t = 900`?**
**It is the law at `t = 900`, and nothing else.** I settled this by hand from the two printed
numbers *before opening the packet* (`v3` §2.2): `900⁴ = 656,100,000,000` and
`0.060 × 6.561 × 10¹¹ = 3.9366 × 10¹⁰ ≈ 4 × 10¹⁰`, an exact match to every digit printed. The
packet then confirms it in its own words — *"Taking `0.060` at the tail `900` that Conjecture 2
forces gives min `N_S` ≈ 4·10¹⁰"*. **There is no second route to the figure and the packet claims
none.** There is therefore **no circularity** of the kind I pre-registered: B24-04 does not present
the figure as corroborating the law, nor the law as corroborating the figure. It presents one
number derived from the other and says so. That is honest, and it means the figure's entire warrant
is the fit's warrant.

**(b) Is the `EXTRAPOLATION` label sufficient without the fitted range printed beside it?**
**No — and B24-04 already agrees, because B24-04 prints the range.** The packet's own sentence is:

> *"**EXTRAPOLATION** — a quartic fitted on `t = 12…24` and evaluated 37-fold outside that range.
> It is not MEASURED and it is not PROVED."*

That is a model of how such a figure should be written: label, fitted range, and fold-factor, in
one sentence, next to the number. (The fold is `900/24 = 37.5`; "37-fold" rounds down, immaterial.)
My pre-formed requirement — that the range travel with the figure — **is already met inside the
packet.** So the defect, if it appears, is not B24-04's; **it is a transcription risk in the
record**, which is where the brief says the figure is being carried. A bare "≈ 4 × 10¹⁰,
EXTRAPOLATION" in a ledger, with the range left behind in the report, is exactly the failure mode,
and it is the one carry-forward item 6 is exposed to.

**Ruling: the label `EXTRAPOLATION` is necessary and not sufficient. The fitted range `t = 12…24`
and the fold-factor must be printed wherever the figure is printed.** A label discloses the kind of
claim; only the range discloses its distance.

**(c) May the record use it as a price?**
**Yes, but only in the form B24-04 states it, and only with its condition.** Three constraints,
and they are not stylistic:

1. **It is CONDITIONAL on Conjecture 2**, which the packet labels *"an expectation on the record,
   not a theorem"*. The unconditional statement is much weaker and the packet prints it:
   with only the proved floor `D* ≥ 8`, the corresponding number is `min N_S ≥ 231`, **inside the
   programme's reach of `≈ 2 × 10⁴`**. Any use of `4 × 10¹⁰` that drops Conjecture 2 converts an
   expectation into a price and is a misuse.
2. **Two significant figures are not available.** The constant is unconverged and drifts up by
   4.6 % on a one-term correction; the extrapolation is 37-fold. The figure carries one significant
   figure at most, and the honest form is *"of order `10¹⁰`, conditional on Conjecture 2, by a
   quartic fitted on `t = 12…24`"*.
3. **The gap, not the figure, is what the record should carry.** The packet's own framing is the
   useful one: against a reach of `2 × 10⁴`, the gap is *"about `10⁶` — six orders, not a hundred
   and forty-six"*. An order-of-magnitude gap is robust to everything I found in §1.2; the
   two-digit figure is not.

**On superseding `10^150.4`: the verb is wrong, and the record should stop using it.** My
pre-verdict asked whether `10^150` had been shown wrong or merely shown to be larger. **It is
neither.** §2.3 is explicit that `10^150.4` was *"an average over all cells at degree 900"*, while
`4 × 10¹⁰` is a conditional *minimum over the cells Theorem 1 does not exclude*. **These are two
different statistics of two different sets.** A minimum does not supersede an average; it answers a
different question. What actually happened is better than a supersession and should be recorded as
what it is: **Theorem 1 changed which statistic is binding**, and the average was never the binding
number. Equally, the `621` was not reduced by Theorem 1 — the packet says so plainly (that cell has
`t = 8 > d = 5`); it was already excluded by the floor `D* ≥ 8`. So **neither of B23-06's two
numbers is refuted, and neither is superseded; both are answers to questions that are no longer the
question.** Carry-forward item 6 should say that, and should carry the range, the fold and
Conjecture 2.

### 1.4 B24-04 Q3: the 70-pattern basis is a seeded greedy selection — **CONFIRMED, and `v2`'s refinement is right where my pre-verdict was wrong.** Method: READ

**The finding stands.** §4.2 establishes it from the construction: B22-01 drew random typed patterns
under `numpy.random.default_rng(20260925)`, keeping one iff it raised the rank. A different seed
gives a different 70. The spanning set — all typed patterns — is astronomically larger, the map
pattern `↦` function is enormously non-injective, and **the record has no rule that picks 70 of
them.** The packet names two obstructions of different kinds: no distinguished sub-basis exists,
and the construction is per-cell (`λ = (4⁵)`, `d = 5`, `W = Mat_4`, targets `7, 31, 28, 4`, the
`ε_3` contraction scheme — nothing stated for a family). Both are correct and both matter.

**"Bespoke" is the right word, and the consequence B24-04 draws is the right one:** the Missing
Theorem must be re-proved per cell, and *"the next cell does not cost nothing; it costs a theorem"*.
Any feasibility estimate that assumed the `F^L_{-1}` construction transfers must be corrected. I
adopt that.

**Where my own pre-verdict was wrong, and `v2` was right.** I pre-registered (`v3` §2.3) that
"greedy selection does not in general find a canonical or even an extremal object; the count 70 is
an upper bound on nothing and a lower bound on nothing unless a separate argument pins the number."
**The separate argument exists.** The greedy stopped *"at each block's proved target"*, and
`7 + 31 + 28 + 4 = 70`. So **70 is a rank, and a rank does not depend on the seed.** `v2` §Q1.4 had
this exactly right — *"the count is canonical and the set is not"* — and drew the correct
consequence, that the Missing Theorem is bespoke precisely to the extent that it quantifies over
the *set* rather than the *count*, so that restating it in terms of the rank or of a
seed-independent property of the span would remove the bespokeness entirely. **I hold `v2`'s
reading over my own on this point.** It is sharper, it points at a repair rather than only at
damage, and it is what the bytes support.

**The one thing this does *not* infect.** I pre-registered (`v3` §1.4) that the single most
consequential thing to check was whether Theorem 1's "tail" is defined through this same 70-pattern
basis, because the theorem would then inherit the bespokeness. **It is not.** §2.2 defines
`t = |λ̄|` for `λ = (nd − t, λ̄) ⊢ nd` — a function of the partition alone, intrinsic, with no
basis, no seed and no pattern anywhere in it. **Theorem 1 is basis-free and the Q3 finding does not
reach it.** I record this explicitly because the two results sit in one report and a reader could
easily assume otherwise.

### 1.5 Comparison with `v2` on priority 1, as the brief directs

`v2` is a genuine pre-formed reading: it records what had been opened (brief, `git` metadata,
B23-10 §0 — its own prior report), states the method rule, and blocks Q1.1–Q1.4 with timestamps.
I cannot vouch for it beyond what it wrote down, which is the position B23-10 took toward its
predecessor and which I take here. On its face it is what it says it is.

| point | `v2` | this reviewer (`v3`) | outcome on the bytes |
|---|---|---|---|
| the theorem | PROVED in shape; predicted thin at **(W1)** the base case (`c_{n e_1}` itself not separating) and **(W2)** the grading | CONDITIONAL on **(C1)** span-not-monomial, **(C2)** `c ∉ I`, **(C3)** `D*` un-indexed | **PROVED.** Both readings land in the same place by different routes |
| `c_{n e_1}` | flagged as (W1), predicted asserted not proved | flagged as (C2), predicted "one line away" | **Both vindicated in substance, both too pessimistic**: the packet proves it with two explicit witnesses |
| redundant hypothesis | "`I` prime **and** `P_r` irreducible is very likely redundant"; recorded so as to notice if it matters | one hypothesis "doing no work in the direction invoked" | **Both partly right.** Not redundant — irreducibility earns its place in the **unused** direction of the iff. Neither of us predicted that split |
| `4e10` is the law at 900 | derived it, same arithmetic | derived it, same arithmetic | **Agree, confirmed.** Two independent pre-formed derivations of the same point |
| the range | "I will require the fitted range to be printed" | same requirement | **Agree** — and both of us were pre-emptively wrong about the packet, which prints it |
| the asymmetry of the supersession | *"a number that invites work must be better supported than a number that forbids it"* | asked whether `10^150` was shown wrong or merely larger | **`v2`'s framing is the better one and I adopt it.** My question is answered differently than either of us expected: the two numbers are different statistics |
| the 70 | count canonical, set not; repair-directed | count pinned by nothing | **`v2` right, I was wrong.** See §1.4 |

**Where we differ, I hold `v2`** on the 70-pattern count and on the asymmetry framing, and I hold
**my own** on one point only: `v2` predicted the base case would be "asserted rather than proved"
and called it "load-bearing, not decorative: were `c` separating, the theorem would be false." That
is right about the stakes but the packet does prove it, and `v2`'s Q1.1 does not anticipate the
span-versus-monomial issue (C1), which is the step where a real gap would have lived. Two
pre-formed readings, and between them they named every load-bearing step; neither named all of them
alone. **That is the case for the practice.**

---

## 2. Priority 2 — B24-05's Corollary D2′, its two lemmas, and its placement

### 2.1 Lemma D1 — **PROVED**, self-contained, classical in content. Method: READ + independent hand re-derivation

**Pre-formed (v3 §3.1): PROVED and classical.** Confirmed, and the packet is stronger than I
expected: it does not cite the b-function of a pure power, it **proves** it from the Weyl algebra
in half a page, and cites the textbook `k = 2` value only as a check.

I re-derived the proof by hand and it is correct at every step. The key move — `∂_j(x_1^{k(s+1)}) = 0`
for `j ≥ 2`, so only `β = (b,0,…,0)` contributes; distinct `(α_2,…,α_N)` and distinct `α_1 − b`
give distinct monomials so nothing cancels; hence the ideal of valid `b(s)` is generated by
`{[k(s+1)]_b : b ≥ k}` — is right, and the reduction to a single generator is right because
`[t]_b = [t]_k · [t−k]_{b−k}`. The monic generator computes as
`k^{−k}[k(s+1)]_k = ∏_{j=0}^{k−1}(s + 1 − j/k) = ∏_{i=1}^{k}(s + i/k)` under `i = k − j`, which I
verified independently.

**On the Cayley convention — the brief's specific question.** **The convention used in D1 is the
standard one, `b(s) f^s ∈ D[s]·f^{s+1}`, and it is used consistently.** Three confirmations:

1. **The formula is self-certifying.** The product contains `(s + k/k) = (s + 1)`, and `(s+1)`
   divides `b_f` for every non-constant `f` exactly in the standard convention. I pre-registered
   this test in `v3` §3.1 before opening the packet, and it passes.
2. **The proof states the convention explicitly** rather than leaving it to be inferred: the ideal
   is defined as the set of `b(s)` with `b(s) f^s ∈ D[s]·f^{s+1}`.
3. **The join is consistent, which is where a convention error actually appears.** Lemma D3 uses
   *"By Cayley, `b_{det_n}/(s+1) = (s+2)···(s+n)"*, i.e. `b_{det_n} = (s+1)(s+2)···(s+n)` — the
   same convention as D1. Its two consequences are then arithmetically right in that convention:
   largest root `−1` gives `lct(det_n) = 1`, and largest root of the reduced `b` at `−2` gives
   `α̃(det_n) = 2`. Against `x_0^k`, D1 gives reduced largest root `−(k−1)/k` and
   `α̃ ≤ (k−1)/k < 1`. **All of this is internally consistent; no convention error propagated into
   the `D`-module lineage.**

**On the integrator's self-booked Cayley error (`b24_12_ledger.md` §4, "tenth integrator error").**
The integrator records that Caracciolo–Sokal–Sportiello state Cayley's identity as
`b(s) = s(s+1)···(s+n−1)` in the `f^s → f^{s−1}` convention, and that *"my brief's `(s+1)···(s+n)`
is correct only after the convention shift"*. **The two are the same identity: substituting
`s → s+1` in `s(s+1)···(s+n−1)` gives `(s+1)(s+2)···(s+n)`.** The integrator's formula is the one
in the standard Bernstein–Sato convention — the dominant convention, and the one B24-05 proves and
uses throughout. **The self-booking as an "error" is over-harsh.** What happened is that a
convention was asserted without being stated, and a source using the other convention was then
consulted. The substantive lesson — state the convention — stands and is worth keeping. The label
should be *"convention not stated"*, not *"error"*. I flag this because a self-penalising integrator
that over-counts its own errors degrades the error count as an instrument, and the count is being
used to calibrate trust.

**Attribution: no defect.** My pre-registered caution was that D1 might be claimed as novel. It is
not: the report calls D1 and D2 *"entirely self-contained"*, which is a claim about the proof's
dependencies, not about priority, and it cites the textbook value as a check on its own arithmetic.
That is correct practice.

### 2.2 Lemma D2 — **PROVED**, both clauses, trivially. Method: READ + independent hand re-derivation

**(b) `x_{11}^n ∈ End(C^{n²})·det_n ⊆ Det_n` for `n ≥ 2`.** The packet's proof is the one I
reconstructed in `v3` §3.2 before opening it: `A : X ↦ x_{11}·I_n` is linear in the entries,
`det_n(A(X)) = det(x_{11}I_n) = x_{11}^n`; `GL` is dense in `End` and `(A,f) ↦ f∘A` is continuous,
so `f∘A ∈ closure(GL·f)`. Correct, and one line.

**(a) `x_1^4 ∈ D45`, "in the image".** **My pre-formed CONDITIONAL is overturned, and in the
direction opposite to the one I feared.** I flagged "in the image" as a hedge that might be
distinguishing a constructible image from a closed set, which would have invalidated any downstream
use as a *closed* condition. It does the opposite: the packet means `x_1^4` is in the **image of the
pencil parametrisation itself**, not merely in its closure — witnessed by `A_1 = I_4`,
`A_2 = … = A_5 = 0`, so `det_4(Σ x_i A_i) = det_4(x_1 I_4) = x_1^4`. **The qualifier strengthens the
claim.** I record the overturn; the hedge was a producer being precise, and I read it as a producer
being evasive.

### 2.3 Corollary D2′ — **PROVED**, and it needs only D2. Method: READ + independent hand re-derivation

The argument, which I reconstructed independently before reading and which the packet matches: let
`Q` be `GL_N`-invariant, true at `det_n`, false at `x^n`. By D2, `x^n ∈ Det_n`. A closed
`GL_N`-invariant locus containing `det_n` contains the orbit, hence its closure `Det_n`, hence
`x^n` — contradiction. So no closed condition extracted from `Q` contains `Det_n`, and `Q` is a
property of the orbit, not of the orbit closure. **Correct.**

**The dependency is over-stated in the brief and stated correctly in the packet.** I pre-registered
(`v3` §3.3) that **D1 is not a premise of D2′** — the corollary needs one fact only, that some pure
power lies in `Det_n`, and D1 is a premise of the *application*, being what exhibits a particular
invariant as failing at `x^n`. **The packet gets this right**: its statement of D2′ invokes only
`x^n ∈ Det_n`, and D1 appears in the list of what is disposed of, parenthetically, attached to the
one item that needs it — *"integrality of the roots of `b_F` (by Lemma D1)"*. The brief's framing —
*"Its premises are Lemma D1 and Lemma D2"* — is therefore **the brief's over-attribution, not
B24-05's.** This matters for placement: stated correctly, D2′ needs **no `D`-module theory at all**,
and a reader who thinks it rests on a b-function computation will over-estimate both its depth and
its narrowness.

**One precision the statement should carry.** The argument needs the locus of `Q` to be **closed**.
The packet's phrasing — "no closed condition extracted from `Q`" — is careful enough to survive,
and the weaker consequence ("the locus does not contain `Det_n`") holds unconditionally for any
`Q` whatever. If D2′ goes into Paper 3's body, the word *closed* should be in the hypothesis, not
only in the conclusion.

**What it disposes of.** Six named items: integrality of the roots of `b_F`, prehomogeneity of the
generic stabiliser, rational/klt/canonical singularities of `X_F`, reducedness, irreducibility, and
`X_F^∨` being a hypersurface. I checked the last by hand — for `F = x^n` the dual is a single point
— and it is right. The list is substantial and each item is one line given D2′.

### 2.4 The proposed placement beside Lemma 1.3 and Lemma 1.4 — **JUSTIFIED AS TO SCOPE, NOT AS TO KIND.** Method: READ

**Pre-formed (v3 §3.4): NARROWER, a single-witness sieve.** The bytes refine this rather than
confirm it, and the refinement matters, so I state the ruling precisely.

The packet's own Remark claims only this: *"B22-02's Lemma 1.3 excludes constructions that go
through `r × r` minors of a derivative matrix, and Lemma 1.4 excludes `SL_5`-covariants into a
determinantal locus. D2′ excludes a class that goes through neither."* **That claim is correct and
I affirm it.** D2′ does reach a class the other two do not.

`GAPS.md` §E (G-36) goes further, and this is the sentence the brief is asking me about: *"It is of
the same kind and scope as C15 (Lemma 1.3 …) and C16 (Lemma 1.4 …)."* **"Same scope" is
defensible. "Same kind" is not.**

- **Scope: comparable.** D2′ kills six named families of candidate obstruction in one line each.
  That is not a narrow haul, and on coverage it sits with 1.3 and 1.4 honestly.
- **Kind: different, and the difference is not cosmetic.** Lemmas 1.3 and 1.4 are **mechanism**
  exclusions: they rule out constructions by their *route*, whatever those constructions compute.
  D2′ is a **witness** exclusion: its entire force comes from one point, `x^n`, and it is **silent
  on every `GL_N`-invariant property that happens to hold at `x^n`.** That silence is the whole
  content of the difference. A mechanism exclusion tells you a road is closed; a witness exclusion
  tells you that everything you have tried so far hits one particular rock.

**Why this is worth insisting on rather than waving through.** The witness form carries an
**actionable escape route that the mechanism lemmas do not**: to evade D2′, find a `GL`-invariant
property that does *not* degenerate at pure powers. A reader who takes D2′ as a mechanism exclusion
of "the same kind" as 1.3/1.4 will conclude that a class of approaches is closed, when what is
closed is a class of approaches *that share one failure at one point*. That over-reading is exactly
the kind of thing this review series exists to prevent, and B24-05's own remark does not commit it —
only §E's gloss does.

**Ruling: D2′ takes its own claim ID next to C15 and C16 — the placement is right — but its
statement must name its witness**, so the escape route is visible in the statement rather than in
the proof. Wording, offered and not applied: *"Every `GL_N`-invariant property whose locus is
closed, which holds at `det_n` and fails at the pure power `x^n` — a point of `Det_n` by Lemma D2 —
yields no closed condition containing `Det_n`."* With the witness in the sentence, "same kind" is
no longer claimed and nothing is lost.

---

## 3. Priority 3 — C45, the chain B24-02 → B24-02b

### 3.1 (a) The ceiling/floor asymmetry — **PROVED**, elementary. Method: READ + independent re-derivation

**Pre-formed (v3 §4.1): PROVED, elementary.** Confirmed, and B24-02 §2.3 states it correctly and
draws the right consequence.

For an integer matrix, reduction mod `p` can only drop rank, so `nullity_p ≥ nullity_Q`. With
`i_det = nullity_Q[E; ev_det]`, a measured `nullity_p = 1` gives `i_det ≤ 1` — **a ceiling**. The
packet's statement of the consequence is the sharp one and I adopt it verbatim in substance:
*"No sharpening of the numerics, no extra prime, no fresh evaluation family can supply it; the
inequality runs the wrong way for the instrument."* That is right. Every prime independently
over-reports, so no number of primes produces a floor.

**The packet also gets the asymmetry's other half right**, which is the part that is easy to state
backwards: `i_per = 0` **is** genuinely proved over `Q`, because a nullity-`0` certificate at one
prime forces `nullity_Q = 0` — `nullity_Q ≤ nullity_p = 0`. That is the direction that does work,
and the packet says so. Hence `D = i_det` and the measurement alone establishes only `0 ≤ D ≤ 1`,
*"which is not a positive result at all"*. **The entire sign comes from the LMR floor.** Correctly
identified and correctly weighted.

My one pre-registered failure mode — that `i_det` might be the nullity of a matrix whose entries
depend on `p` — does not occur: `E` and `ev_det` are defined over `Z` independently of the prime.

### 3.2 (b) The `(★)` qualification at the boundary — **SOUND at the boundary; C45 is PROVED modulo `(★)`, whose own label I could not settle.** Method: READ

This is the brief's sharpest question and it deserves the sharpest answer I can give. I separate
two things the phrasing merges, as I pre-registered in `v3` §4.2.

**(i) Is a premise used at the exact boundary of its stated validity sound here? YES.**

The criterion is whether the range is stated **closed** at that end, and it is. The reduction is
recorded as valid *"for `ℓ(λ) ≤ 7`"*, and the record's cell has `ℓ(λ) = 7`. A closed range includes
its endpoint; **using a premise at an included endpoint is not an approximation and is not a
weakening.** There is no "boundary effect" to worry about in a statement of the form `ℓ(λ) ≤ 7`.
Had the range been `ℓ(λ) < 7`, or "`ℓ(λ)` small", or had it been proved by an argument needing
slack, the answer would be the opposite. It is not. **The boundary use is legitimate, and I rule
against reading `(★)`-at-the-boundary as a defect in itself.**

What *is* true, and what the record should carry, is that **the cell sits at the pinch with no
margin**: `N ≥ k+3 = 7` and `r = 7`, and `ℓ(λ) = 7` against `ℓ(λ) ≤ 7`. Two independent conditions
are both exactly saturated. That is not an error, but it means **any future widening of the cell,
in `N` or in `ℓ(λ)`, leaves the validated region immediately**, and it means an error in either
stated range would bite here first and nowhere else. That is worth a sentence at the point of use,
and B24-02b's `(★)` carry is that sentence.

**(ii) The transport across `N`, which is the load-bearing step and which the brief's framing
under-weights.**

LMR's printed numbers are at `N = 9` (`S^{12}(S^3 C^9)`, `closure(GL_9·[det_3])`); the record's cell
is at `N = 7` (`Sym^{12}(Sym^3 C^7)`, `D_7`). **A statement established at `N = 9` does not transfer
to `N = 7` merely because `N` is smaller** — smaller `N` is the more degenerate regime. The bridge
is the programme's own `(★)` reduction plus multiplicity stability in the variable count. So the
composite is: *someone else's theorem, at a different `N`, transported by the programme's own
reduction, used at that reduction's included endpoint.*

**B24-02b handles this better than I expected, and supplies a genuine external check I did not
anticipate.** s73 computed `a = 6` for `S_λ(C^7)` in `Sym^{12}(Sym^3 C^7)` by three independent
engines; LMR prints multiplicity **six** in `S^{12}(S^3 C^9)`. Different variable counts,
independent computations, same number. **That is a free external corroboration of the stability
step at exactly the cell in question**, on a step that previously had none. The packet calls it
"small" — it is more than small, because it is the only evidence in the chain that the `N = 9 → 7`
transport behaves, and it is method-disjoint from everything else.

**But it corroborates the ambient multiplicity `a`, not the ideal count.** `a = 6` agreeing across
`N = 9` and `N = 7` is evidence that *ambient* multiplicities are stable there. What the floor needs
is that the **ideal-copy count** does not drop to zero on restriction to the 7-pencil slice — a
different quantity, and the one `(★)` must actually supply. The cross-check makes the transport
much more plausible; it does not prove it.

**(iii) What I can and cannot settle, stated plainly as the brief requires.**

`(★)` is a record-internal premise recorded at `s73` §1, which is **not among the deliverables
pinned to me**. B24-02b describes it accurately as *"a record-internal premise already on the
record; it is not a new condition, and it is not LMR's"*, and carries it on every affected row. But
neither pinned packet states whether `(★)` is **PROVED** at `ℓ(λ) = 7` or **ADOPTED**. I did not
open `s73` — it is outside the commits I was given, and ruling on it from a description would be
exactly the delegated-gloss failure B24-04 caught.

**Ruling: C45's floor is PROVED modulo `(★)` at `ℓ(λ) = 7`.** The boundary use is sound. The
citation is PRIMARY and correct. **`(★)`'s own label is not established by anything I reviewed, and
I flag it for B25-10 rather than rounding it to a confident verdict.** If `(★)` is PROVED, C45 is
PROVED outright and the qualification is bookkeeping. If `(★)` is ADOPTED, then C45 — *the
programme's only positive result* — rests on an adopted record-internal reduction as well as on an
external theorem, and the label must say so. **That distinction is worth one half-slot of a reader's
time in Batch 25 and it is the single most consequential unlabelled thing I found.**

### 3.3 (c) The recommendation against taking `i_det = 1` from LMR — **CORRECT. Endorsed.** Method: READ

**Pre-formed (v3 §4.3): endorse.** Confirmed, and B24-02b's reasoning is better than mine.

The situation: LMR's §3.2 example makes two claims — `a = 6` and "only one copy of it is in the
ideal" (`i_det = 1`) — and **neither carries a printed proof**; they illustrate. What *is* proved is
the general statement, Thm 2.3.1 with Thm 3.1.1, giving `i_det ≥ 1`. The record takes the **floor**
from LMR and measures the **ceiling** itself. **That is the correct division and it was already the
record's.** Adopting an asserted half because it travels in the same paper as a proved half is the
error hardest to detect later, because by then both halves carry the same citation.

**The argument I did not anticipate, and which converts my endorsement from hygiene to substance.**
B24-02b observes that the close *"does not depend on LMR's unproved 'only one copy': if that
assertion were wrong, `i_det` could only be larger, and `D = i_det − i_per ≥ 1 > 0` would still
hold."* **The positive result is robust to the weakest link in its own citation.** That is a
genuine structural argument, it is correct, and it is worth more than the hygiene point: it means
the one unproved sentence in the source cannot damage the conclusion in any direction.

**Ruling: the refusal is correct and is endorsed. The measured ceiling stays.** And per my
pre-registration: if `i_det = 1` has been taken from LMR anywhere in the record, that use must be
**relabelled, not grandfathered**. I found no such use in the pinned packets; B24-02b §3.2's
ten-row table attaches the label at each point of use and none of them takes the ceiling from LMR.

### 3.4 (d) The pre-registration hash and the three negative controls

**The hash was written before `import flint`. CONFIRMED from the bytes, not from a description.**
Method: READ of `f8273c35:analysis/b24_02_p1_n5_kleiman.py`, lines 22–48. The order in the source
is unambiguous:

```
25  PREREG = Path("results/b24_02/p1_prereg.md")
26  got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
27  out = {"preregistration": {... "sha256": got, "expected": sys.argv[2],
29        "match": got == sys.argv[2], "recorded_at_elapsed_s": ...}}
37  dump()                          # <- writes the JSON to disk
38  if got != sys.argv[2]:
39      out["status"] = "prereg hash mismatch; nothing run"
41      sys.exit(1)                 # <- aborts
44  import flint                    # <- only here
```

`dump()` writes the preregistration block to the output file at line 37, **before** the mismatch
check and **before** `import flint` at line 44. The abort path is real. I also verified
independently that `f8273c35:results/b24_02/p1_prereg.md` hashes to
`b0b4b66054d41f583d53d1341648d67cf130732b60e6e66cd8819a6d85c70d2b`, matching both the `sha256` and
the `expected` fields recorded in `p1_n5_kleiman.json`, with `"match": true` and
`"recorded_at_elapsed_s": 0.0`. **G25 is satisfied.**

One structural note, not a defect: `expected` arrives as `sys.argv[2]`, so the guarantee is that the
launcher supplied the expected digest at launch. Combined with the prereg file being committed and
hashing correctly, this is the standard and correct implementation.

**The three negative controls — REPLAYED exactly, and they are one control, not three.**
Method: REPLAY by hand, then INDEPENDENT EVALUATOR (pilot 1, block B).

By hand from the pre-registered closed form `D(k) = (3k² − 33k + 50)/2`:

```
D(7) = (147 − 231 + 50)/2 = −34/2 = −17   ✓
D(8) = (192 − 264 + 50)/2 = −22/2 = −11   ✓
D(9) = (243 − 297 + 50)/2 =  −4/2 =  −2   ✓
```

All three reproduce. Pilot 1 confirms the same in exact rational arithmetic, and additionally
verifies `h_5(k) = C(k+3,3) − C(k,3) = (3k²+3k+2)/2` for `k = 0…39`, the printed values
`19, 31, 46, 64, 85, 109, 136` at `k = 3…9`, and `D(k) = h_5(k) − H(k)` against its closed form for
`k = 3…39`. **B24-02's arithmetic is correct throughout.**

**Two findings, both minor, both of the same species as §1.2(iii).**

1. **They are three samples of one quadratic, not three independent controls.** I pre-registered
   this test in `v3` §4.4 before opening the packet: *"if the three values are monotone by
   construction, or are three values of one smooth function of `N`, they are one control and not
   three."* They are. `D` is a single pre-registered closed form; `D(7), D(8), D(9)` are three
   evaluations of it, and the informative content is **one** fact — the location of the upper root
   at `≈ 9.186`, hence the sign change between `k = 9` and `k = 10`. The report calls them *"three
   negative controls"* and *"the sharpest check available on the instrument"*. The first is an
   overcount; the second overstates, because a prediction derived from a closed form the
   preregistration itself fixed checks the **derivation**, not the instrument. **What genuinely
   checks the instrument is elsewhere in the same section and is not counted:**
   `rank M_k(F_0) = dim S_k − H(k)` verified at `k = 3…7`, 5/5, which is a real measurement against
   a real prediction. That is the control worth naming.
2. **"`D(k) > 0` exactly for integer `k ≥ 10`" is false read unrestricted.** Pilot 1 block B:
   `D(0) = 25` and `D(1) = 10`, both positive; the roots are `≈1.816` and `≈9.186`, so the closed
   form is positive at `k = 0, 1` as well. The statement is **true on `k ≥ 3`**, which is the range
   where `H(k) = 18k − 24` is asserted, and the report prints the roots on the same line so an
   attentive reader can see it. But the word *"exactly"* is carrying a range restriction that is not
   written next to it. **Same defect as §1.2(iii): a formula quoted without the range it inherits.**

**Neither finding disturbs B24-02's verdict.** The `N = 5` PASS, the coverage over `k`, and Theorem
B24-02.1 stand; the margins `+19, +54, +89, +116` and the ties at `k = 3,4,5` are unaffected.

---

## 4. Priority 4 — B24-01 has no packet

### 4.1 The finding, verified from the tree. Method: INDEPENDENT check of the committed tree

**Confirmed, and it is unambiguous.** At `bc7e62b714632c20d2405e54030224a2549c242d`:

- `git ls-tree -r` returns **no `results/b24_01/`**, no results directory for the slot at all, and
  **no `docs/b24_01_report.md`**. I searched the whole tree, not a guessed path.
- The six committed paths — `paper/det3-conductor.tex`, `CHANGES.md`, `GAPS.md`, `READINESS.md`,
  `README.md`, `ATTRIBUTION_PATCH.md` — are **unbound**: no manifest binds them, no report states
  what was checked to produce them, and no hash ties them to an input.

So the slot delivered edits and no packet. Under G26 — every claim carries its packet *and* commit —
**nothing from B24-01 is citable as a finding.**

### 4.2 The two claims the record carries from it — **PRODUCER-RELAY-ONLY, both.**

The record carries two claims from B24-01: that **Paper 1 awaits one signature**, and that **LMR
Prop. 3.5.1 constructs `P_2`**. Both come to the record through the integrator's transcription of a
relay (`b24_12_ledger.md` §8.0c), with nothing committed to check against.

**Ruling on each of the brief's three options:**

- **"Paper 1 awaits one signature."** This is **partly checkable and it checks out**, but not from
  a packet. `ATTRIBUTION_PATCH.md` is committed, is self-labelled *"PREPARED, NOT APPLIED"*, and
  §5 states exactly what signing means. I verified independently (§4.3) that it is unapplied. So
  the *existence* of one outstanding signature is verifiable from committed bytes. What is **not**
  verifiable is the word **"one"** — that all other blockers are cleared. That claim rests on
  `CHANGES.md`, `GAPS.md` and `READINESS.md`, which are edits with no report binding them and no
  manifest. **Label: the patch-pending state is CERTIFIED from bytes; "awaits *one* signature" is
  PRODUCER-RELAY-ONLY.**
- **"LMR Prop. 3.5.1 constructs the paper's boundary component `P_2`."** **PRODUCER-RELAY-ONLY, and
  this one should not be carried at any strength.** It is a **prior-art finding against the
  programme's own paper** — the second such, after the bracket census. The integrator's own ledger
  draws the general lesson from it: *"two results presented as the paper's own that were already
  published, and both were invisible until someone read the source rather than the abstract."* A
  finding of that weight, resting on a relayed sentence with no committed reading, no quoted
  passage, no hash and no read-status label, **is exactly what G14′ exists to prevent.** Note the
  contrast that makes this stark: in the very same batch, B24-02b read LMR and produced verbatim
  quotes, a PDF hash matching the record's, a named section list and a `lmr_quotes.md` file. The
  standard is set within the batch; B24-01 does not meet it.

**Ruling: both claims carry a producer-relay-only label, and a re-run that produces a packet is
required — but the re-run is narrow.** It does not need to redo Paper 1's edits. It needs to (i)
bind the six paths with before/after hashes in a manifest, (ii) state what was checked to reach
"awaits one signature", and (iii) **read LMR Prop. 3.5.1 to the standard B24-02b set in this same
batch** — quote the construction, hash the source, record PRIMARY at the point of use — or withdraw
the claim. That is a half-slot, not a slot.

### 4.3 `ATTRIBUTION_PATCH.md` is not applied — **CONFIRMED from bytes**, and its wording matches B23-10 §4.4

**Not applied. Verified three ways** at `bc7e62b7:paper/det3-conductor.tex`:

- The **original** text is still present where the patch would replace it: line 176,
  `$e(\det_3)\ge18$ turns out to need no computation:`, and line 560,
  `$e(\det_3)\ge 18$, with no computation.` These are precisely the two passages the patch rewrites.
- The **added** text is absent: `\cite[Cor.~7.2]{BI}` occurs **0 times** in the file.
- The patch's own header says so: *"**Status: PREPARED, NOT APPLIED.** `paper/det3-conductor.tex`
  is unchanged by this file."*

The three "plethysm bound" occurrences in the file (lines 79, 200, 1030) are pre-existing text about
the ambient plethysm bound and are unrelated to the patch.

**The wording matches B23-10 §4.4 verbatim.** I compared against `239dd6e8:docs/b23_10_review.md`
§4.4 directly:

| B23-10 §4.4 supplied | patch §2 proposes | match |
|---|---|---|
| the Prop. 4.1 sentence, from *"Proposition 4.1 is the case of Bürgisser and Ikenmeyer's plethysm bound"* through *"because it is short and self-contained."* | §2.1's added LaTeX, same sentence | **verbatim** |
| Cor. 4.2: *"by `\cite[Cor.~7.2]{BI}` and the period theorem" (or keep "with no computation" and add the citation)"* | §2.2 takes the second option, and prints the first as the authorised alternative | **matches, both options preserved** |
| the introduction *"should credit BI"* | §2.3 rewrites it to *"and it is Bürgisser and Ikenmeyer's"* | **matches** |

And the three qualitative requirements the brief names:

- **RELATED, not equivalent** — patch §1: *"**RELATED — a special case, not an equivalent.**"* It
  also correctly rejects B23-05's *own* proposed phrase as wrong for a second reason (that case
  includes the regularity failures), which is B23-10's ruling faithfully carried. ✓
- **One remark sentence** — patch §4 offers exactly one sentence, explicitly as an optional
  addendum, *"not part of the ruling's required wording"*. ✓
- **No novelty claim** — patch §1: *"worth **one remark sentence** and **no claim of a new
  result**"*; §5 confirms nothing is withdrawn and lists what survives untouched. ✓

Prop. 7.3 is correctly dropped from the credit, with the right reason given (BI state it without
proof, so citing it would import an unproved statement for nothing). That is the same discipline
B24-02b applies to LMR's unproved half, arrived at independently in a different slot — worth noting
as a sign the standard has taken.

**One defect found, and it is a real one.** The patch binds itself to a target:

> *"Applies to: `paper/det3-conductor.tex` as it stands after the B24-01 edits recorded in
> `CHANGES.md`, sha256 `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445`."*

**No committed version of that file hashes to `b911a151…`.** I hashed **every** version of
`paper/det3-conductor.tex` in the history of `b23-05-paper1` — all 20+ commits that touch it — and
the digest appears nowhere. The three nearest candidates are `bc7e62b7 → f52f8d16…`,
`bbd1d12e → 2cc15d3f…`, `7309c4e2 → dd0d2abf…`.

So the patch's stated target is a **working-tree state that was never committed**. Consequences:
its "applies cleanly" assertion cannot be verified by anyone; its diff hunks' line offsets are
stated against a file that cannot be retrieved; and its own self-checks ("braces balanced, `$` count
even, 52 environments, numbering byte-for-byte identical") were performed on a file nobody else can
reproduce. The patch's parenthetical — *"the patch also applies cleanly to the file at HEAD, modulo
line offsets"* — is the saving grace, and it is true: the two target passages are present and intact
at `bc7e62b7`, at lines 176 and 560 against the patch's stated 175–179 and 559–561. **The patch is
usable. Its binding is not.** This is the single clearest illustration of why G29 is needed, and I
cite it in §9.1.

---

## 5. Priority 5 — Paper 2, and the cap-theorem label

### 5.1 B2 first — **CONFIRMED: Theorem 9.1 is false as stated.** Method: READ + independent check

B24-06 reports that §9's `thm:slab` states: *"For every weight with `ℓ(λ) ≤ 4` and **every degree**,
`mult_λ C[D^det_4] = a(λ,δ)`."* **The refutation is correct and it is elementary.**

`dim D^det_4 = 34` in `dim W_4 = 35` — the paper's **own** Prop. 2.1 table. A hypersurface of
codimension 1 in an ambient space has a **principal, nonzero** ideal. So `I(D^det_4) ≠ 0`, and at
and above the degree of its generator, `mult_det < a`. The universal quantifier "every degree" is
therefore false, and it is false for a reason printed three sections earlier in the same paper.

**The paper's own proof already knows this**, which is what makes it a defect of statement rather
than of mathematics: the proof says *"whose ideal begins in degree `≫ δ` **for the degrees in
question**"* — a restricted quantifier that the theorem statement does not carry. **A theorem whose
proof proves something weaker than its statement is false as stated**, regardless of whether the
weaker version is true.

**The repair is on the record and the headline survives.** `docs/blindness_slab.md` §0 Theorem A at
`82633a60` splits it into three clauses: `Δ ≤ 0` for `ℓ(λ) ≤ 4` at every `δ`; `det_units = 0` for
`ℓ ≤ 3` at every `δ`; and for `ℓ = 4` **only at `δ ≤ e − 1`**, with `e = onset I(D_4^{det_4})`,
`e ≥ 10` CERTIFIED (s33) and `e = 320112` ADOPTED (LLV). B24-06's assessment that the headline
conclusion is **not lost** is correct and I verify the reason it gives: `Δ ≤ 0` on the whole
length-`≤ 4` slab follows from the paper's own Prop. 6.1 / `docs/PROVED.md` `n4_gate_containment`,
which is a **containment** and therefore degree-free. A containment argument cannot acquire a degree
restriction, so the slab result is safe.

**Ruling: B2 CONFIRMED. Theorem 9.1 must be restated as the record's three-clause Theorem A with
`e` cited, carrying `e ≥ 10` CERTIFIED and `e = 320112` ADOPTED separately.** This is the highest-
severity item in Batch 24: a false theorem in a paper. It is also, mercifully, cheap — the true
statement exists, is on the record, and preserves the conclusion the paper wants.

### 5.2 The other three mathematical blockers

**B1 — Corollary 5.3 states the Kadish–Landsberg bound backwards. ACCEPTED on B24-06's assessment;
method READ, not independently verified.** I did not fetch Kadish–Landsberg and do not rule on the
bound's direction from the source. A reversed inequality in a corollary is a defect of the kind that
is trivially checkable against the source and I recommend it be checked at the source before repair,
not repaired from the record.

**B3 — "length `≥ 6`" is the wrong gate. CONFIRMED on the record's own bytes; method READ.**
B24-06's case is strong and internally checkable: the paper's **own** Theorem 3.1 gives `P_5 = R_5`
exactly at `r = 5`, so `Δ = Δ_R` there and a positive `Δ_R` at `ℓ = 5` **is** a multiplicity
obstruction for the padded permanent. The record's gate is `ℓ ≥ 5` in two places —
`docs/n4_gate.md` §2 and `docs/PROVED.md` `quartic_length_and_eligibility` — and that is where the
open region lives: `b14_11_quartic_census` counts 2,571 still-open labels in the `ℓ ≥ 5` region.
**A gate written one step too tight silently declares the open region empty.** That is the worst
direction for this error, and B24-06 is right to rank it third of sixteen. Its further point — that
the washout's true content is about *interpretation* (such a certificate would certify reducibility
against the determinant) and not about existence — is a real distinction and should survive into the
repair as a separate sentence.

**B4 — §9's LMR interval is stale. CONFIRMED; method READ.** The paper says `Δ ∈ [−4, +1]`;
`docs/PROVED.md` `lmr_D_upper` at `82633a60` gives `D_LMR ∈ [−4, −2]`, CERTIFIED conditional on the
ADOPTED `dim N₁₃ = 73`. **The substantive change is not the interval, it is the sign**: the paper
currently leaves `Δ = +1` on the table at the one cell where the programme has excluded it. B24-06
is right to flag that as the point, and right that the condition (`dim N₁₃ = 73`, ADOPTED) must
travel rather than be dropped. **Its `[AUTHOR]` handling of the uncommitted `[−4, −3]` narrowing is
correct** — it names it, marks it uncommitted, declines to use it, and leaves the citation decision
to the author. That is G26 applied to the producer's own advantage, and it is the behaviour the
gate is for.

**B5 — LMR load-bearing four times over and unread. CONFIRMED, and now PARTLY DISCHARGED.**
This is a finding B24-06 could not have made and I can, because I hold both packets: **B24-02b read
LMR and recorded PRIMARY** — §2.3 (the construction, `Dual_{k,d,N}`, Thm 2.3.1), §3.1 (the
determinant's dual, Thm 3.1.1), §3.2 (the global ideal statement and the `n=3` example), §1
(Thm 1.0.2), with the PDF hash `cfc28275…` matching the record's and verbatim quotes in
`lmr_quotes.md`. **Paper 2's B5 is therefore cheaper than B24-06 priced it**, to the extent its four
uses fall within those sections. **Two things must travel with the discharge**, both established in
§3: cite **Thm 2.3.1**, never Thm 1.0.2 (whose printed `ω_1` coefficient and degree are both halved
and mutually inconsistent — citing it yields `(13,7,2⁵)` at degree 6, not the record's cell); and
carry `(★)` wherever the `N = 9 → 7` transport is used.

**Beauville joins LMR as an unread load-bearing source.** Noted, and I rule it the same way: a
load-bearing source that is unread at the point of use carries **UNREAD** there, whatever is known
about it elsewhere. B24-02b's slot is the template and the price is known — *one reviewer-hour, no
pilot*. Batch 25 should read Beauville to that standard before Paper 2's repair cites it, not after.

### 5.3 The cap-theorem label collision — **B24-03's refusal was correct, and the right label is "PROVED modulo Kleiman, Dimca and Gulliksen–Negård, all ADOPTED".** Method: READ

**Three labels for one theorem, verified in the bytes:**

| where | label |
|---|---|
| Paper 2, Theorem 7.1 | **flat**, with a four-step proof, and listed in the abstract under **"we prove"** |
| Paper 3, `CLAIMS.md` C11 | `ADOPTED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), Gulliksen–Negård (SECONDARY)` |
| `docs/onset_conjecture.md` §0 | *"**proved modulo** Kleiman, Dimca and Gulliksen–Negård, all adopted and named"* |

**First: was B24-03's refusal to re-label C11 correct? YES, and the reason it gives is the right
reason.** `GAPS.md` G-32 records: *"a writing slot that re-labels a theorem to match a sibling paper
has made a mathematical ruling it has no authority for."* That is correct as a matter of the
programme's own division of labour — a producer slot tasked with corrections to Paper 3 is not the
authority on whether a theorem shared with Paper 2 is proved. Equally important, it **recorded the
divergence before either paper circulates**, which is the whole value of catching it. Recording
without resolving was the correct action and I affirm it.

**Second: which label is right? The source wording, `docs/onset_conjecture.md` §0.** My reasoning:

- **Paper 2's flat statement is wrong, and it is the dangerous one.** The theorem's proof consumes
  three external results, two of them SECONDARY. Shipping it flat **drops the dependency
  entirely**, and shipping it in the abstract under "we prove" asserts to a referee that the
  programme proved it unconditionally. **This must be corrected before circulation**, and it is a
  submission blocker of the same species as Paper 1's attribution patch.
- **C11's "ADOPTED modulo …" is imprecise, and errs conservatively.** In this record's vocabulary,
  ADOPTED means taken on an external source's authority — `e = 320112` adopted from LLV,
  `dim N₁₃ = 73` ADOPTED. **The cap theorem is not adopted; it is the programme's own (session
  40).** What is adopted is its three *inputs*. So "ADOPTED modulo X" misdescribes the theorem's
  provenance, saying the theorem came from outside when in fact the theorem is the programme's and
  its premises came from outside. A category error — but one that **understates**, which is the
  right direction to err.
- **"Proved modulo …, all adopted and named" is exactly accurate**: the proof is complete given
  three named inputs, each carrying its own read-status. It names the theorem's provenance
  correctly, names the dependency correctly, and names the read-status of each dependency. In the
  brief's label vocabulary this is **CONDITIONAL with the condition named**.

**Ruling: the right label is `PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level)
and Gulliksen–Negård (SECONDARY)` — i.e. the source wording, which neither paper currently carries
correctly.** Paper 2 must add the modulus to both Theorem 7.1 and the abstract. Paper 3's C11 should
change `ADOPTED modulo` to `PROVED modulo`, keeping the three named inputs and their read-statuses
exactly as they are. **This ruling is mine and I make it; it is not B24-03's to make and it was
right not to.** G-32 can be closed on this ruling.

---

## 6. Priority 6 — Paper 3, and the four edits now unblocked

### 6.1 The claims table, checked against the packets

**50 IDs, C01–C50, no gaps. CONFIRMED.** I extracted every row identifier from
`f95742ae:papers/det4-blindness/CLAIMS.md` mechanically and sorted: `C01` through `C50`, 50 unique,
no duplicates, no missing number.

**Five stale rows: C23, C30, C35, C36, C37. CONFIRMED**, and each is self-marked in sequence —
`stale row 1 of 5` through `stale row 5 of 5` — so the count is checkable from the file itself
rather than from a claim about it. Each carries what it was, what it became, and the producer/
reviewer lineage for the change. Spot-checking two against the packets: C37's move from **OPEN with
single-point MEASURED evidence** to **PROVED** is supported by B23-03's hand proof plus B23-10's
independent re-derivation and a third exact rank on a disjoint seed — *"three method-disjoint
lineages"* — and the row **carries the caution that B23-03's own witness has rank 58, a special
member, never claimed as 64**. That is a producer keeping an inconvenient fact visible in the row
that could have hidden it. C36's move from **classification OPEN** to **PROVED** is supported by
B23-03 Thm 2.1, and the row records B23-10's **honest negative** that it did *not* replay the
theorem, `T3 ⊆ T2`, or `T1 ⊄ T2`. Both rows are labelled at the strength the packets support and
not above it.

**The distinction between stale and superseded — CONFIRMED, and it is a real distinction, not a
bookkeeping one.** Two further rows carry a replaced clause rather than a stale row:

- **C34**, marked `(superseded clause)`: the row's claim stands; one companion figure inside it —
  *"64 on a cubic through a plane"*, which was **one exact rank at one point, i.e. a floor** — is
  SUPERSEDED by C37 (corrigendum K3), which proves the **ceiling for every member**. The row is not
  stale because nothing about the row's own claim changed; a supporting figure was replaced by a
  stronger result.
- **C44**, marked `(scoped clause)`: the height-2000 claim is **SCOPED**, not withdrawn — false per
  coefficient, true under a common denominator, candidate height 2842 — with the original
  SUPERSEDED (K7).

**The distinction holds and is the right one: *stale* = the row's own label moved; *superseded* /
*scoped* = the row stands and an internal clause was replaced or narrowed.** Conflating them would
either overstate how much of the table moved or hide that a clause changed. I note for precision
that the brief describes both as "a superseded rather than a stale clause" while the file
distinguishes SUPERSEDED (C34) from SCOPED (C44); the count of two is right and the finer
distinction in the file is an improvement on the brief, not a divergence from it.

### 6.2 G-A1 is Question 6.5, and the right-way corner is scoped throughout — **CONFIRMED.** Method: INDEPENDENT derivation from the source

**The numbering derives correctly without compiling anything.** `\newtheorem{theorem}{Theorem}[section]`
with `proposition`, `lemma`, `question` and the rest all sharing the `theorem` counter. Section 6 is
`\section{The one right-way problem: the cubic factor}\label{sec:cubic}` (the sixth `\section`), and
its numbered environments run in source order:

```
lemma      lem:cubic          -> 6.1    (CLAIMS.md C34 says "Lemma 6.1")     ✓
proposition prop:intersection -> 6.2    (C35 says "Prop. 6.2")               ✓
theorem    thm:classify       -> 6.3    (C36 says "Thm. 6.3")                ✓
proposition prop:capplane     -> 6.4    (C37 says "Prop. 6.4")               ✓
question   q:boundary [G-A1]  -> 6.5                                          ✓
```

**Four independent cross-checks against `CLAIMS.md` all agree, so `q:boundary` is Question 6.5 and
G-A1 is the paper's named open question at 6.5.** Confirmed.

**The right-way corner is scoped to the determinant part at every occurrence. CONFIRMED —
five of five.** B23-10 required that the "right-way corner survives" sentence be scoped; it is, and
more thoroughly than the requirement:

| line | how it is scoped |
|---|---|
| 114 (intro) | *"the right-way corner survives on **that part**"*, immediately followed by *"Whether it survives on the boundary … is this paper's named open question"* |
| 197 (thesis/scope) | *"proved to survive … **\emph{on the determinant part of that intersection}**"*, plus *"not known to survive on the boundary"* |
| 647 (Table 1, row 13) | *"Its target is now known on **the determinant part** of `D45 ∩ P5` and unknown on the boundary (Question 6.5)"* |
| 836 (§6.1) | *"the right-way corner survives the enlargement of the intersection. **\emph{On the determinant part of it.}}**"* — set as its own emphasised sentence |
| 1004 (§9, open) | *"whether the right-way corner … holds on all of `D45 ∩ P5` or only on its **determinant part**"* |

**No unscoped occurrence exists.** The scoping is also load-bearing in a way worth recording: because
every claim is already restricted to the determinant part and the boundary is already named as open,
**Paper 3 is true whichever way G-A1 resolves.** That fact drives my §9 sequencing.

### 6.3 C50's boundary precision — **CONFIRMED by exact arithmetic.** Method: INDEPENDENT EVALUATOR (pilot 1 block C)

C50 carries: *"LMR's inequality is not strict at `n = m²/2` (`m` even), where one row is
nevertheless visible, so 'exactly the LMR range' is off at that one point; nothing turns on it at
`m = 3`."*

The visible rows are `2n+1 … m²+1`, so they exist iff `2n+1 ≤ m²+1`, i.e. `n ≤ m²/2`. At
`n = m²/2` exactly, the range collapses to the single row `m²+1`. Pilot 1 confirms for `m = 4, 6, 8`:

```
m=4:  n = 8,  rows 17..17,  count 1
m=6:  n = 18, rows 37..37,  count 1
m=8:  n = 32, rows 65..65,  count 1
```

**Exactly one row in every case. The precision is correct**, and the parenthetical "`m` even" is
correct too, since `m²/2` is an integer only for even `m`. **Confirmed.** The row's own statement
that nothing turns on it at `m = 3` is right — `9/2` is not an integer, so the boundary case does
not arise there.

**One further consistency check, unasked.** Pilot 1 block D: C35 records `Σ_Π` at 31 affine on the
cubic side and `T2 = {ℓ·C : C ∈ Σ_Π}` at 35 affine on the quartic side. The product construction
predicts `31 + 5 − 1 = 35`, since a linear form contributes 5 and the scaling `(ℓ, C) ↦ (cℓ, c^{-1}C)`
removes 1. **The predicted and recorded values agree**, which independently confirms both figures
*and* confirms that `T2` and `Σ_Π` are genuinely different objects in different spaces — the point
at issue in §7.2 below.

### 6.4 The four unblocked edits, each against the committed packet

The brief asks whether the committed packet supports the edit **as `GAPS.md` §E describes it**. I
read §E's four entries against the packets I verified in §§1–3. §E's own premise — that all four
were uncommitted when it was written — is now discharged: all four are committed at the commits the
brief pins, which is exactly what unblocks them.

**G-30 (B24-02) — SUPPORTED.** §E describes three things and all three are in the bytes. (i) The
`N = 5` pilot, one wrapped run, 0.194 s, exit 0, pre-registration hash written before
`import flint` — I verified the byte order in the script itself (§3.4), and the closed forms
`h_5`, `H`, `D` and the margins in pilot 1. (ii) The independent hand re-derivation of Astra
Thms 8.1, 8.2, Cor. 8.3. (iii) The G-15 sharpening: the statement C45 uses is **Thm 2.3.1**, not
Thm 1.0.1, and at the point of use the read-status was UNREAD. The edit §E names —
**C48 / row 1 becomes a PROVED-kill on elementary premises across `N = 5..8`, and K5 is
discharged** — is exactly what B24-02 §4.4 establishes and labels, with the premises enumerated
(*"No Kleiman. No Dimca, no Gulliksen–Negård, no depth sensitivity."*). **Supported, with one
wording carry**: §E repeats *"including three negative controls"*, which per §3.4 should read *one
control checked at three points*. Small, and it should not propagate into `CLAIMS.md`.

**G-31 (B24-02b) — SUPPORTED, and §E's description is the most careful of the four.** The fetch
hash matches the record's `cfc28275…` (I verified the report's own account of this, and the
record's manifest value is quoted in full, all 64 digits). The three confirmations are in the bytes.
Most importantly, **§E does not describe this as a formality** — it names *"three things that would
have to travel with it, and they are the reason this is not a formality"*: cite Thm 2.3.1 never
Thm 1.0.2 (with the concrete consequence, `(13,7,2⁵)` at degree 6, spelled out); carry `(★)` at
`ℓ(λ) = 7`, *"exactly at its boundary"*; and note that LMR's two example numbers are asserted
without printed proof so the record leans only on the proved floor. **All three are correct and all
three match my §3.** The edit — C45 becomes PROVED with the citation attached, G-15 discharged — is
supported, **subject to my §3.2 ruling that the label is `PROVED modulo (★)` and that `(★)`'s own
status is unsettled.**

**G-32 (B24-06) — SUPPORTED, and the edit is correctly *no* edit.** §E's prescribed change is
*"Nothing, deliberately"*: C11's label unchanged, a one-line pointer in the draft, and the
divergence recorded before either paper circulates. That matches the packet and it was the right
call (§5.3). **With my §5.3 ruling now on the record, G-32 can be closed and C11 relabelled
`PROVED modulo …` — but that is a Batch 25 edit made on *this* review's authority, not on B24-06's
and not on B24-03's.**

**G-36 (B24-05) — SUPPORTED AS TO SUBSTANCE, NOT AS TO ONE PHRASE.** The substance checks out
completely: D1 and D2 are PROVED and self-contained (§2.1, §2.2), D2′ is PROVED (§2.3), the
six-item disposal list is correct, and the item deserves its own claim ID next to C15 and C16.
**The phrase that does not check out is §E's own**: *"It is **of the same kind and scope** as C15
… and C16."* The packet claims only that D2′ *"excludes a class that goes through neither"* — a
claim about coverage. **§E upgrades a coverage claim into a kind claim, and the upgrade is not in
the packet.** Per §2.4, "same scope" is defensible and "same kind" is not: 1.3 and 1.4 are
mechanism exclusions, D2′ is a witness exclusion with an actionable escape route. **The edit should
go in with the packet's wording, not §E's, and with the witness named in the statement.**

---

## 7. Priority 7 — the integrator's record, and whether the handling was right

The integrator's record meets producer gates under G28; the question is the handling of three
self-reported items.

### 7.1 (a) The PART 14 brief asserted a B24-01 packet that does not exist — **handling PARTLY right; the disclosure is right, the consequence was not drawn.**

The disclosure is real and it is in the ledger. What was **not** done is to propagate the
consequence: `b24_12_ledger.md` §8.0c transcribes B24-01's outcome as *"all five cleared or
prepared"*, and carries forward two substantive claims — Paper 1 awaits one signature, LMR
Prop. 3.5.1 constructs `P_2` — **at full strength, from a relay, with no packet**. The second is a
prior-art finding against the programme's own paper and is given weight enough to generate a general
lesson (*"'cited' and 'read' have been different things on this record more often than anyone
assumed"*). **A disclosure that the packet is missing, followed by transcription of the packet's
claims as if it were not, leaves the record in the same state as if the disclosure had not been
made.**

**Ruling: disclosing was right and is to the integrator's credit; the handling is incomplete.** The
two claims must carry the producer-relay-only label of §4.2. Under G29 (§9.1) this could not recur:
the slot would have had to write a report or the batch would have had to record that it produced
none.

### 7.2 (b) `T2` written as `Σ_Π` — **the correction is right, and the integrator's reading of the untouched statement is CONFIRMED.** Method: READ + INDEPENDENT arithmetic

The error: `b23_12_ledger.md`'s table read `**T2** = Σ_Π`, carrying the quartic-side dimensions
(35 affine / 34 projective) onto the cubic-side locus (31 / 30). Corrected in place, booked as the
eleventh integrator error, found by B24-03.

**The correction is right.** `T2` and `Σ_Π` are different objects in different spaces, and pilot 1
block D confirms it dimensionally: `dim Σ_Π + 5 − 1 = 31 + 5 − 1 = 35 = dim T2` (affine). The two
figures are consistent precisely *because* the objects are different; had they been the same object
the arithmetic would not close.

**The integrator did not touch `deg f ≥ onset I(D35 ∪ Σ_Π)`, reading `D35` and `Σ_Π` as both
cubic-side, and asks me to confirm. CONFIRMED — the reading is correct and the statement rightly
stands as written.** I verified from the paper's own source rather than from the ledger's account.
`det4-blindness.tex` Lemma 6.1 (`lem:cubic`, claim C34) is titled **"restriction to the cubic
factor"**, derives `C ↦ f(ℓ·C)` as a nonzero element of `I(D_{35})_d` via
`ℓ·det_3 M = det_4 diag(ℓ, M)`, and then states the strengthened bound with the definition printed
inline:

```
deg f  >=  onset I( D_35 ∪ Σ_Π ),     Σ_Π := {quinary cubics containing a plane}.
```

**`Σ_Π` is defined in the displayed formula itself as a set of cubics**, and `D_35` is the
cubic-side determinantal locus whose onset is `δ_0`. Both live in `Sym³C⁵`. The union is a
subvariety of the cubic side and its ideal's onset bounds the degree of the restricted `f`.
**Writing `T2` there would have been a genuine error** — it would have placed a quartic-side object
inside a statement about the restriction to the cubic factor, and imported 35/34 where 31/30 belongs.
**The integrator's reading is right, the statement needed no change, and leaving it alone was
correct.**

I note in the integrator's favour that this is the harder half of the correction to get right: it
is easy to over-correct after finding an error and rewrite a neighbouring statement that was always
sound. Stopping at the boundary of the actual error, and asking for confirmation rather than
assuming, is the right handling.

### 7.3 (c) G9′ reported twice — **YES, G9′ needs a reporting clause as well as a use clause.**

The facts: B23-01 and B24-02b both wrote producer tool memories; **neither was used as an input to
anything**; the integrator flagged both and asked for a ruling.

**The use clause is working exactly as designed.** In both cases the memory was inadmissible, and in
both cases the conclusion did not depend on it — B24-02b's LMR citation trap is in the committed
bytes at §2.5 and at ledger rows .10 and .11, which the integrator read in the staged packet. **No
harm occurred either time.** That is the gate doing its job.

**But a use clause alone cannot detect the failure it is meant to prevent.** The specific risk is
not that a producer writes a memory; it is that a producer **reads one in a later slot and uses it
without knowing it is a memory** — at which point the input is invisible in the packet, carries no
hash, no read-status and no lineage, and the use clause has nothing to bite on because nobody knows
a use occurred. **A use clause is enforced at the moment of use by the very person least able to
notice it. A reporting clause is enforced at the moment of writing, when the act is visible.** Those
are different control points and only the second is observable by a reviewer.

The empirical case is now sufficient: **two batches running, two different slots, two producers.**
That is a pattern, not an incident, and both times it was caught by the integrator reading a relay
rather than by any gate.

**Ruling: G9′ gains a reporting clause. Proposed wording, for the record to adopt or amend:**

> **G9′ (amended).** A producer tool memory is not part of the record and is not an admissible
> input to any slot. **In addition: a slot that writes one must say so in its report, naming what
> was written, and must state that nothing in the slot depends on it.** An unreported memory is a
> gate defect even when unused.

The cost is one sentence per affected report. The benefit is that the reviewer can see the memory
exists and check the independence claim against the packet — which is exactly what the integrator
did by hand, twice, and which should not depend on an integrator happening to read a relay closely.

---

## 8. Priority 8 — the two threads

### 8.1 (a) The rational candidate and the two-number check — **I decline to certify the candidate real, and the check should NOT be priced as a Batch 25 item. It should be recorded as an opportunistic rider.**

The brief permits "not worth ruling on". I can do better than that, so I rule on the parts that are
rulable and say precisely which part is not.

**On whether the candidate is real: I decline to certify it, and the record's existing labels are
correct.** The evidence is a rational reconstruction agreeing at a second prime. That is *evidence*,
and reasonably strong evidence — but it is modular evidence, and §3.1 is the whole lesson of this
batch about modular evidence: **it bounds, it does not prove.** Certifying a `Q`-statement from
two-prime agreement is the same category error as taking a floor from a ceiling. The record's
labels — MEASURED candidate, `Q`-rank OPEN, height 2842 under a common denominator — are exactly
right and I change none of them. **Anyone who wants the `Q` statement must do the exact check;
nobody may assert it from the primes.**

**On pricing: no, and the reason is payoff, not cost.** The integrator's own assessment is the
decisive one and I adopt it: the upgrade *"would upgrade one label in a `D = −1` cell and change no
direction"*. The cell's sign is already known and negative; C44's cheap mechanisms are already
closed; the height-2000 tension is already scoped by B23-10 (K7). **A slot that spends itself to
convert MEASURED into PROVED in a cell whose direction is settled has bought a label.**

**But the asymmetry is worth recording, because it cuts the other way on cost.** The targeted check
is *two rational numbers* — exact arithmetic on integers of height ~3000, verifying a linear
relation over `Q`. That is **seconds of a wrapped pilot**, against the `≈10⁴`-evaluation re-run it
replaces. **Price is not the obstacle; payoff is.** So the correct disposition is neither "fund it"
nor "forget it":

**Ruling: do not schedule it. Record it as an opportunistic rider — if any Batch 25 slot is running
exact rational arithmetic in this neighbourhood for another reason, it may do the two-number check
in the same pilot and report the result in one line.** If it comes back positive, one label moves;
if negative, a candidate dies and that is worth marginally more. Neither outcome justifies a slot of
its own.

### 8.2 (b) The equivariance constraint on the C45 nullity — **YES, worth a Batch 25 half-slot, and for a better reason than the one offered.**

The suggestion: the C45 nullity is constrained by equivariance to a sum `Σ_λ (dim V_λ)·ν_λ`. Status
is exactly that of the `D`-module idea before B24-05: integrator speculation, group and
decomposition unverified, and the integrator says so explicitly so that no later reader takes it as
a finding. That disclosure is correct and is the right way to carry an unassessed idea.

**The integrator's own reason for it is the weaker one.** The ledger prices it as *"a second lineage
for a result that now has one solid one"*, off the critical path now the floor stands. On that
framing I would decline it: a second lineage for a settled result is a luxury.

**The better reason, which my §3.2 supplies: it targets `(★)`.** C45's floor is PROVED *modulo the
programme's own `(★)` reduction*, used at the included endpoint of its stated range, transporting an
external theorem across `N = 9 → 7`, and **`(★)`'s own label is not established by anything I
reviewed.** A record-internal constraint on the nullity would be the first route to the floor that
**does not pass through `(★)` or through LMR at all**. That is not a luxury — it is the difference
between "the programme's only positive result rests on an external theorem plus an internal
reduction at its boundary" and "it rests on an internal argument". **That is worth a half-slot.**

**It is also correctly sized as a half-slot, because it is cheap to close negatively.** The
integrator's outcome (c) — the map is not equivariant in the relevant sense, or the shape was
misread — should be reachable in a paragraph by anyone who writes down the group. Outcome (b) — the
constraint is vacuous in the measured range — likewise. Only outcome (a) needs real work, and
outcome (a) is the one worth having. **A question whose negative answer is a paragraph and whose
positive answer discharges a load-bearing premise is the ideal shape for a half-slot.**

I note without weighting it that the underlying idea is not implausible on its face: `I(D_n)` is
stable under the stabiliser of `det_n`, so a decomposition under that stabiliser is a real
structure, not an invented one. **I have not verified the group or the decomposition and I make no
finding — I am ruling only on whether it is worth the half-slot.** It is.

---

## 9. Priority 9 — Gates, and the Batch 25 slate

### 9.1 G29 — **ACCEPT, with two amendments.** The evidence for it is in this batch.

Proposed: *a slot's deliverable is a committed packet with a manifest; a slot producing only edits
still writes a short report binding what it changed and why.*

**Accept the principle. The case is B24-01 and it is decisive.** That slot produced six edited
paths, no report, no manifest, and the consequences are all four of the failure modes the gate
would prevent, simultaneously: two claims carried at full strength with nothing to check them
against (§4.2); a prior-art finding against the programme's own paper resting on a relayed sentence
(§4.2); a patch bound to a file hash that exists **nowhere in the branch's history** (§4.3); and an
integrator brief asserting a packet that does not exist (§7.1). **No other gate on the books catches
any of these.** G26 requires a claim to carry its packet and commit, but B24-01 made no *claims* in
a packet — it made edits, and the claims entered the record through a relay. That is the hole G29
closes.

**Amendment 1 — every hash a packet prints must resolve.** G29 as drafted would have required
B24-01 to write a report; it would not have caught `b911a151…`, a binding digest matching no
committed object. Proposed addition:

> **G29(b).** Every sha256 a packet prints must resolve to a committed object, or be explicitly
> labelled as naming an uncommitted state. A patch, diff or report that binds itself to an
> unresolvable digest is unbound, and what it says about the target cannot be verified.

**Amendment 2 — a brief may not assert a packet's existence.** The PART 14 failure was upstream of
the producer. Proposed addition:

> **G29(c).** A brief or ledger that relies on a slot's output cites that output's commit and
> manifest hash, or states that none exists. The existence of a packet is a checkable fact and is
> checked, not assumed.

**One thing I deliberately do not add.** G29 should **not** require an edits-only slot to produce a
full manifest — only a short report binding what changed, with before/after hashes. B24-03 is the
model: it produced paper edits plus `CLAIMS.md`, `GAPS.md`, `DIFF_NOTES.md` and no results manifest,
and nothing about it is unbound. **The gate should demand bindings, not ceremony**, or edits-only
slots will acquire empty manifests that bind nothing and the gate will have made the record longer
without making it checkable.

**All other gates stand: G1–G28, G5′, G9′ (amended per §7.3), G14′, G15′, G20′.** G9′ is the only
one I change.

### 9.2 The integrator's reading, disputed in one part

The integrator's view — the programme's value has migrated into the negative, and Batch 25 should be
mostly writing plus one live question — is in the ledger as **opinion, not finding**, and is offered
for dispute. **I agree with the conclusion and dispute one premise.**

**The premise I dispute: value has *not* only migrated into the negative in Batch 24.** Two genuine
positives were produced. **B24-02 made row 1 unconditional across the whole window `N = 5..8` on
elementary premises** — no Kleiman, no Dimca, no Gulliksen–Negård, no depth sensitivity — which
*discharged* B23-10's own required qualifier and corrigendum K5. That is a strengthening, not a
kill. **B24-02b closed C45**, which is the programme's only positive result, and closed it by
reading a source rather than by computing. Neither is a negative in any sense. What migrated into
the negative is the **candidate pipeline** (B24-05's two sub-candidates, B24-04's small-tail
regime), and that is a different thing from the record.

The distinction matters for Batch 25's framing: the programme is not in the position of "everything
we try dies, so let us write up the corpses". It is in the position of "the candidate pipeline is
exhausted, two results were strengthened, and one open question is live". **That is a better
position and the write-up should say so.**

**The conclusion I accept:** mostly writing, plus live questions. My slate follows.

### 9.3 What the record supports, in order, with prerequisites

**First — (b), the four unblocked Paper 3 edits.** Cheapest, highest certainty, and **fully
unblocked**: all four packets are committed at the commits this review pins, which is the exact
condition `GAPS.md` §E held them out for. I have verified each against its packet in §6.4. Paper 3
already compiles clean at 22 pages. **This is the programme's realisable value and it is four edits
away.** Carry my three corrections: G-36 goes in with the packet's wording and its witness named,
not §E's "same kind and scope" (§2.4, §6.4); G-31 carries `PROVED modulo (★)` (§3.2); G-30 drops
"three negative controls" for "one control at three points" (§3.4). **Prerequisite: none remaining.**
**And on my §5.3 ruling, C11 becomes `PROVED modulo …` and G-32 closes — a fifth edit, now unblocked
by this review.**

**Second — (a), Paper 2's repair, B2 first.** Highest severity in the batch: **a theorem that is
false as stated, in a paper, under "we prove" in its abstract** for the separate cap-theorem
matter. Nothing has circulated, which is the only reason this is not urgent. B2 first because the
repair is known, cheap, and preserves the conclusion (§5.1); then B3 (a gate one step too tight,
silently emptying the open region — §5.2); then B4 (the sign, not the interval); then B1, which
should be checked at Kadish–Landsberg rather than repaired from the record. **Prerequisite for B5:
B24-02b's LMR reading, which partly discharges it (§5.2) — so Paper 2's repair is cheaper than
B24-06 priced it.** **Beauville must be read to B24-02b's standard before the repair cites it**, one
reviewer-hour, no pilot. **Add to the list: the cap theorem's label in Theorem 7.1 and in the
abstract, per §5.3.**

**Third — (d), B24-04 Q2: large tail with small treewidth.** The best live mathematics on the
table, and B24-04 identifies it precisely: Lemma 2 is one-directional, so a cell with tail `≥ 900`
may still contain small-treewidth tableaux, and *"whether the separating cells forced by §2 contain
small-treewidth tableaux is open, is not priced by anything on record"*. **A negative is worth as
much as a positive**, which makes it the right shape for a slot. It is a question about fillings and
the record has never asked one. **Prerequisite: none** — §2's Theorem 1 is PROVED and supplies the
constraint the question is asked inside. Carry B24-04's own two warnings so they are not read into
the answer: a cheap evaluation does not shrink `N_S`, and BDI's generator count is a Kostka number,
a third quantity.

**Fourth — the equivariance half-slot (§8.2).** Targets `(★)`, which is the last unlabelled premise
under the programme's only positive result. Cheap to close negatively. **Prerequisite: none**, but
it is worth more if it follows the `(★)` label question below.

**Also in Batch 25, and small: settle `(★)`'s label.** Per §3.2, I could not establish whether the
programme's `(★)` reduction is PROVED or ADOPTED at `ℓ(λ) = 7`, because `s73` was not among my
pinned commits. **This is a reading task on a record-internal document, not research.** It is the
single most consequential unlabelled thing I found, because C45's status sentence depends on it.
**Flagged for B25-10 per the brief's instruction to say so rather than round it.**

**Fifth — (c), G-A1.** Should be done, but **is not a prerequisite of anything and should not gate
the papers.** The brief flags it as a risk to the paper, and it is: a positive answer costs the
right-way corner. **But §6.2 establishes that Paper 3 is honest whichever way it resolves** — every
occurrence is scoped to the determinant part and the boundary is already named as the paper's
principal open question at 6.5. **So the paper does not depend on the answer, and the risk is a risk
to the programme's ambitions, not to the paper's correctness.** That is precisely why it can wait,
and why it must not be quietly dropped: an open question named in a published paper is a commitment.
Note the packet's own pricing — three routes, none of them a pilot, since sampled degenerations are
only MEASURED.

**Not funded: (e) row 2 at `2 ≤ j ≤ N−4`.** `CLAIMS.md` C23 records this as **OPEN** and describes
it in its own words as *"producer B23-03 only and … a statement that nothing is known"*. A slot
would be starting from nothing, with no instrument identified and no negative worth having.

**Not funded: (f) the `s_rep = 0` candidate with `Y ↦ Yᵀ`.** Nothing in the packets I reviewed
raises it above the candidate pipeline that Batch 24 exhausted, and B24-05's D2′ is now a one-line
test that any such candidate must pass first. **Apply D2′ to it before funding anything.** If it
fails at a pure power, it is dead for the cost of a sentence — which is the whole point of having
D2′, and the best immediate demonstration of the corollary's value.

**Not (g).** "Nothing more" is not supported: (b) is four verified edits from shipping a paper, (a)
is a false theorem awaiting repair, and (d) is a live question with a valuable negative. There is
real work.

**No cell is nominated. No gap is claimed. No worker is requested.**

---

## 10. Honest negatives

Recorded as B20-10 through B23-10 recorded theirs, and as the brief requires.

1. **I did not replay B24-04's dynamic programme.** The `min N_S` table at `t = 4…24` is READ, not
   replayed. My independent work in pilot 1 block A operates **on** those six numbers — it verifies
   the constants, the convergence and the extrapolation — and would not detect an error in the
   dynamic programme that produced them. B24-04's own controls C1 (three values reproduced against
   B23-06 independently) and C2 (literal enumeration at two shapes) are the evidence there, and I
   accepted them on reading.
2. **I did not verify the `t = 18…24` rows are global minima**, and they are not claimed to be:
   B24-04 states plainly that only two shapes were evaluated there, so those rows are *"a minimum
   over the shapes evaluated, never a proved global minimum"*. **My extrapolation analysis inherits
   that limitation in full.** If a cheaper shape exists at large `t`, the fitted constant is too
   high and the price is lower than either of us says. This is the largest single uncertainty in my
   §1.3 ruling and I do not think it is small.
3. **I did not establish `(★)`'s label** (§3.2). `s73` is not among the pinned commits and I declined
   to rule on it from B24-02b's description. Flagged for B25-10.
4. **I did not read Kadish–Landsberg, Beauville, Kleiman, Dimca or Gulliksen–Negård.** B1 is
   accepted on B24-06's assessment; the cap theorem's three inputs are ruled on by *label*, not by
   reading. My §5.3 ruling is about which label is accurate given the dependency structure, and is
   not a judgement on whether the theorem is true.
5. **I did not replay B24-02's Astra re-derivation (Task 2)** or B24-05's two sub-candidate gates
   (§1.3, §1.4) beyond reading the three lemmas they rest on. My memory of the batch records both
   sub-candidates as killed; I verified the *instrument* that kills them (D2′) and not the kills.
6. **I did not verify B24-02b's fetch independently.** No network access was used in this slot. The
   PDF hash `cfc28275…` matching B23-06's record is B24-02b's report of its own download; I verified
   that the report's account is internally consistent and that the record's manifest value is quoted
   in full, not that the bytes were fetched.
7. **My §1.2 Richardson analysis assumes a `1/t` correction.** `c(t) = c_∞ − a/t` is the natural
   first correction and all six pairs agree to three digits, which is evidence the form is right
   over the fitted range. It is **not** evidence about `t = 900`, and I do not offer `c_∞ ≈ 0.0627`
   as a prediction there — only as a demonstration that `0.060` is not converged and that the drift
   runs upward.
8. **My pre-verdict on the 70-pattern count was wrong and `v2`'s was right** (§1.4). I asserted the
   count was pinned by nothing; the block targets are proved and `7+31+28+4 = 70` is a rank. I
   record this as the clearest case in this review of two pre-formed readings being better than one,
   and of my own being the weaker.
9. **I compiled nothing**, as instructed. The §6.2 numbering is derived from `\newtheorem`
   declarations and source order, which is sound for shared counters but is not a compiler.
10. **One pilot of three, and it is arithmetic.** Pilot 1 does exact rational arithmetic on numbers
    the packets printed. It is an independent evaluator of *inferences*, not of *measurements*. No
    measurement in any packet was re-measured by me.

---

## 11. Closing ledger

**All decisions are here.** Nothing is transcribed from §§1–10; where they differ, this governs.
Every row: label, method, and whether the verdict was pre-formed.

### 11.1 Priority 1 — B24-04

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 1.1 | **Theorem 1 (the tail theorem) is correct as stated and proved in the packet.** Every separating cell has tail `≥ D*` | **PROVED** | READ + independent hand re-derivation of every step | Pre-formed **CONDITIONAL** on C1/C2/C3 (`v3` §1.3); **all three met**; converts to PROVED |
| 1.2 | The factorisation holds for **weight vectors, not only monomials** — every basis monomial is divisible by `c_{ne_1}^{d-t}`, hence every element of the span | PROVED | independent re-derivation | pre-registered as the likeliest gap (C1); **not a gap** |
| 1.3 | `c_{n e_1} ∉ I(D_r^{det_n})` is **proved with two explicit witnesses**, not assumed. The omission I flagged is in the **brief's summary**, not the packet | PROVED | READ | pre-formed as "a named omission"; **omission is the brief's** |
| 1.4 | `D*` is un-indexed — a minimum over all separating `f` — so the descent cannot leak across weights | PROVED | READ | pre-registered risk (C3); **does not materialise** |
| 1.5 | Part (ii) is an **iff**; the corollary uses one direction. Irreducibility of `P_r` and `c_{ne_1}|_{P_r} ≠ 0` are needed **only for the unused direction**. Not a defect; the consumed hypothesis set is smaller than announced | — | independent re-derivation | partly pre-formed; my "inert hypothesis" guess was **wrong** — it earns its place in (ii) |
| 1.6 | **The brief's one-sentence summary of Theorem 1 must not be quoted in place of the theorem**: it invokes primality without the non-membership and does not say `D*` is un-indexed | — | READ | not pre-formed |
| 1.7 | The sizing `N_S ≈ 0.060·t⁴` is **a fit on `t = 12…24`**. All four printed constants reproduce exactly | **MEASURED** | INDEPENDENT EVALUATOR (pilot 1 A) | Pre-formed MEASURED-not-law; **confirmed** |
| 1.8 | **The constant has not converged.** `c(t)` rises monotonically across the whole fitted range; `c_∞ = 10409/165888 ≈ 0.062747` (Richardson, pair 12/24), within 0.4 % of `1/16` | MEASURED | INDEPENDENT EVALUATOR | not pre-formed |
| 1.9 | **The drift runs upward: `c_∞·900⁴ = 4.117×10¹⁰`, 4.6 % above the report's figure.** The report's number is conservative on its own fit's terms | MEASURED | INDEPENDENT EVALUATOR | not pre-formed |
| 1.10 | **The cited closed form does not carry the constant.** `1/((n−1)!n!) = 1/2880 = 0.000347` against the measured `0.060` — **ratio 172.9**. Read as the law it gives `2.28×10⁸` at `t = 900`, wrong by 173× and in the direction that makes the programme look reachable. It supports the **exponent only** and must be written that way | **CONDITIONAL** (exponent supported, constant not) | INDEPENDENT EVALUATOR | not pre-formed |
| 1.11 | **The `4×10¹⁰` figure is NOT independent of the sizing law.** It is `0.060·900⁴ = 3.9366×10¹⁰`, exact to every digit printed. No second route exists and the packet claims none | **EXTRAPOLATION** | INDEPENDENT EVALUATOR + READ | **Pre-formed and derived by hand before opening the packet** (`v3` §2.2). `v2` derived the same independently |
| 1.12 | **No circularity.** B24-04 does not present figure and law as corroborating each other | — | READ | pre-registered as a thing to check; **clean** |
| 1.13 | **The `EXTRAPOLATION` label alone is NOT sufficient. The fitted range `t = 12…24` and the fold-factor must be printed wherever the figure is.** B24-04 already does this correctly; **the risk is in the record's transcription, not the packet** | — | READ | Pre-formed "range must travel"; **the packet already complies** — my pre-verdict was wrong about the packet |
| 1.14 | **The record may use `4×10¹⁰` only as an order of magnitude, only carrying Conjecture 2, and never to two significant figures.** The unconditional statement is `min N_S ≥ 231`, **inside the programme's reach** | **CONDITIONAL** on Conjecture 2 (an expectation, not a theorem) | READ + INDEPENDENT EVALUATOR | Pre-formed NO-as-a-price; **refined to yes-in-this-form** |
| 1.15 | **"Supersede" is the wrong verb and the record should stop using it.** `10^150.4` was an **average** over all cells; `4×10¹⁰` is a conditional **minimum** over non-excluded cells — different statistics of different sets. `621` was never reduced by Theorem 1 either; it was already excluded by `D* ≥ 8`. **Neither of B23-06's numbers is refuted or superseded; both answer questions that are no longer the question** | **SUPERSEDED** label rejected; both **reclassified** | READ | Pre-formed as "is `10^150` wrong or merely larger?"; **answered differently than pre-formed — neither** |
| 1.16 | **Carry-forward item 6 amends to:** order-of-magnitude phrasing, the fitted range and fold, Conjecture 2 named, and the reclassification of 1.15 | — | — | ruling on the integrator's request |
| 1.17 | **Q3 stands: the 70-pattern basis is a seeded greedy selection, not canonical**, and the Missing Theorem is **bespoke** — it must be re-proved per cell | **CONFIRMED**; Missing Theorem **CONDITIONAL on the seeded basis** | READ | Pre-formed CONFIRM; **confirmed** |
| 1.18 | **The count 70 IS canonical; only the set is not.** The blocks have **proved targets** `7+31+28+4 = 70`, so 70 is a rank and seed-independent. **`v2` §Q1.4 had this right and my `v3` §2.3 had it wrong; I hold `v2`.** The repair direction follows: restate over the rank or a seed-independent property of the span and the bespokeness goes | CONFIRMED | READ | **My pre-verdict OVERTURNED; `v2`'s upheld** |
| 1.19 | **Theorem 1 does NOT inherit the bespokeness.** `tail = |λ̄|` is a function of the partition alone — no basis, no seed, no pattern | PROVED | READ | **The single most consequential thing I pre-registered to check** (`v3` §1.4); clean |

### 11.2 Priority 2 — B24-05

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 2.1 | **Lemma D1 is correct and proved from the Weyl algebra**, self-contained; classical in content, not claimed as novel | **PROVED** | READ + independent hand re-derivation | Pre-formed PROVED/classical; **confirmed** |
| 2.2 | **The convention in D1 is the standard `b(s)f^s ∈ D[s]f^{s+1}`**, stated explicitly, and the `(s+1)` factor self-certifies it. **D3's Cayley usage is the same convention and is arithmetically consistent** (`lct = 1`, `α̃ = 2`). **No convention error propagated into the `D`-module lineage** | PROVED | independent re-derivation | **Pre-registered the self-certification test** (`v3` §3.1); passes |
| 2.3 | **The integrator's self-booked Cayley error is over-harsh.** `(s+1)···(s+n)` and CSS's `s(s+1)···(s+n−1)` are **the same identity in two conventions** (`s → s+1`). The right label is *"convention not stated"*, not *"error"*. **An integrator that over-counts its own errors degrades the error count as an instrument** | **not an error** | independent re-derivation | not pre-formed |
| 2.4 | **Lemma D2(b) PROVED** — `X ↦ x_{11}I_n` is linear, `det_n` of it is `x_{11}^n`, `GL` dense in `End` | PROVED | independent re-derivation | Pre-formed PROVED; **confirmed** |
| 2.5 | **Lemma D2(a) PROVED, and "in the image" STRENGTHENS the claim** — `x_1^4` is in the image of the pencil parametrisation itself, witnessed by `A_1 = I_4` | PROVED | READ | Pre-formed **CONDITIONAL**, fearing it weakened; **OVERTURNED — it strengthens** |
| 2.6 | **Corollary D2′ PROVED**, and it follows from **D2 alone** | **PROVED** | READ + independent re-derivation | Pre-formed PROVED-from-D2-alone; **confirmed** |
| 2.7 | **D1 is NOT a premise of D2′** — it is a premise of one *application*. **The over-attribution is the brief's; the packet states the dependency correctly** | — | READ | **Pre-formed** (`v3` §3.3); confirmed, and the packet is clean |
| 2.8 | If D2′ enters Paper 3's body, **the word "closed" belongs in the hypothesis**, not only the conclusion | — | independent re-derivation | pre-formed |
| 2.9 | **Placement: JUSTIFIED AS TO SCOPE, NOT AS TO KIND.** Lemmas 1.3/1.4 are **mechanism** exclusions; D2′ is a **witness** exclusion resting on one point, silent on every property holding at `x^n`, and carrying an **actionable escape route** they do not. **`GAPS.md` §E's "of the same kind and scope" over-reads the packet, which claims only that D2′ "excludes a class that goes through neither"** | **PROVED**, placement **amended** | READ | Pre-formed **NARROWER**; **refined** — scope comparable, kind different |
| 2.10 | **D2′ takes its own claim ID beside C15/C16, with its witness named in the statement.** Wording offered in §2.4, not applied | — | — | ruling |

### 11.3 Priority 3 — C45, B24-02 → B24-02b

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 3.1 | **The ceiling/floor reasoning is correct.** `nullity_p ≥ nullity_Q = i_det`, so measurement gives a **ceiling** and **no number of primes can produce a floor** | **PROVED**, elementary | READ + independent re-derivation | Pre-formed PROVED; **confirmed** |
| 3.2 | **The converse direction is correctly used too**: `nullity_p = 0` forces `nullity_Q = 0`, so `i_per = 0` is genuinely proved over `Q`. Measurement alone gives only `0 ≤ D ≤ 1`; **the sign comes entirely from the LMR floor** | PROVED | READ | not pre-formed |
| 3.3 | **`(★)` at the boundary is SOUND.** The range is stated **closed** (`ℓ(λ) ≤ 7`); using a premise at an **included** endpoint is not an approximation. **I rule against reading `(★)`-at-the-boundary as a defect in itself** | **PROVED** (the boundary use) | READ | Pre-formed: sound iff range closed; **it is** |
| 3.4 | **The cell is at a double pinch with no margin** — `N ≥ k+3 = 7` with `r = 7`, and `ℓ(λ) = 7` against `ℓ(λ) ≤ 7`. Not an error, but any widening leaves the validated region immediately | — | READ | not pre-formed |
| 3.5 | **The load-bearing step is the `N = 9 → 7` transport, not the boundary** — and the brief's `(★)` names only one of the two approximations | **CONDITIONAL** | READ | **Pre-formed** (`v3` §4.2); confirmed |
| 3.6 | **B24-02b supplies a genuine external corroboration of the transport**: s73's `a = 6` at `C^7` by three engines against LMR's printed "six" at `C^9`. **Method-disjoint, and the only evidence in the chain that the transport behaves.** It corroborates the **ambient multiplicity**, not the ideal-copy count | MEASURED corroboration | READ | not pre-formed; **stronger than I expected** |
| 3.7 | **C45's floor is PROVED modulo `(★)` at `ℓ(λ) = 7`.** The citation is PRIMARY and correct; the boundary use is sound | **PROVED modulo `(★)`** | READ | refined from pre-formed CONDITIONAL |
| 3.8 | **`(★)`'s own label is NOT established by anything I reviewed** (`s73` is outside my pinned commits, and I declined to rule from a description). **Flagged for B25-10 — the single most consequential unlabelled thing I found.** If `(★)` is ADOPTED, the programme's only positive result rests on an adopted internal reduction as well as an external theorem, and the label must say so | **OPEN** | — | **flagged, not rounded**, per the brief |
| 3.9 | **The recommendation against taking `i_det = 1` from LMR is CORRECT and is ENDORSED.** The record takes the **proved floor** and measures the **ceiling** itself — the correct division, and already the record's | **ENDORSED** | READ | Pre-formed endorse; **confirmed** |
| 3.10 | **The positive result is robust to the weakest link in its own citation**: if "only one copy" were wrong, `i_det` could only be **larger**, and `D ≥ 1` still holds. A structural argument, correct, and worth more than the hygiene point | PROVED | READ | **not anticipated by me**; B24-02b's own |
| 3.11 | **The pre-registration hash was written before `import flint`. CONFIRMED FROM THE BYTES.** `dump()` at line 37 writes the prereg block; abort at 41–42; `import flint` at 44. Prereg file hashes to `b0b4b660…`, matching `sha256` and `expected`, `match: true`, `recorded_at_elapsed_s: 0.0`. **G25 satisfied** | **CERTIFIED** | READ of the script source | mechanical |
| 3.12 | **The three negative controls REPLAY exactly**: `D(7),D(8),D(9) = −17,−11,−2`, by hand and in exact rational arithmetic. `h_5`, `H` and `D` closed forms all verify | **REPLAY — confirmed** | REPLAY + INDEPENDENT EVALUATOR (pilot 1 B) | mechanical |
| 3.13 | **They are ONE control checked at three points, not three controls.** Three evaluations of one pre-registered quadratic; the informative fact is the root at `≈9.186`. **The report's "sharpest check available on the instrument" overstates** — it checks the derivation. **The real instrument check is uncounted in the same section**: `rank M_k(F_0) = dim S_k − H(k)` at `k = 3…7`, 5/5 | **MEASURED**, count corrected | **Pre-registered this exact test** (`v3` §4.4) | **pre-formed; confirmed** |
| 3.14 | **"`D(k) > 0` exactly for integer `k ≥ 10`" is false read unrestricted** — `D(0) = 25`, `D(1) = 10`. True on `k ≥ 3`, where `H` is defined. **Same defect as 1.10: a formula quoted without the range it inherits** | minor correction | INDEPENDENT EVALUATOR (pilot 1 B) | not pre-formed |
| 3.15 | **Neither 3.13 nor 3.14 disturbs B24-02's verdict.** The `N = 5` PASS, the coverage over `k`, the ties at `k = 3,4,5`, the margins `+19,+54,+89,+116`, and Theorem B24-02.1 all stand | **PROVED** (B24-02.1) | READ + REPLAY | — |

### 11.4 Priority 4 — B24-01

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 4.1 | **B24-01 has no packet. Confirmed from the committed tree**: no `results/b24_01/`, no report, no manifest at `bc7e62b7`. The six paths are **unbound** | **CONFIRMED** | INDEPENDENT check of the tree | mechanical |
| 4.2 | **"Paper 1 awaits one signature": the patch-pending state is CERTIFIED from bytes; the word "one" is PRODUCER-RELAY-ONLY** | split label | READ + independent check | ruling |
| 4.3 | **"LMR Prop. 3.5.1 constructs `P_2`": PRODUCER-RELAY-ONLY, and it should not be carried at any strength.** A prior-art finding against the programme's own paper, resting on a relayed sentence with no quote, no hash, no read-status. **B24-02b set the standard within this same batch and B24-01 does not meet it** | **PRODUCER-RELAY-ONLY** | READ | ruling |
| 4.4 | **A re-run producing a packet is required, and it is narrow**: bind the six paths with before/after hashes; state what was checked to reach "awaits one signature"; read LMR Prop. 3.5.1 to B24-02b's standard or withdraw the claim. **A half-slot** | — | — | ruling |
| 4.5 | **`ATTRIBUTION_PATCH.md` is NOT applied. CONFIRMED three ways**: original text present at lines 176 and 560; `\cite[Cor.~7.2]{BI}` occurs **0 times**; the patch self-labels PREPARED, NOT APPLIED | **CERTIFIED** | READ of committed bytes | mechanical |
| 4.6 | **The wording matches B23-10 §4.4 verbatim**, and meets all three qualitative requirements: **RELATED not equivalent** ✓, **one remark sentence** (optional, §4) ✓, **no novelty claim** ✓. Prop. 7.3 correctly dropped, with the right reason | **CONFIRMED** | READ + direct comparison against `239dd6e8` | mechanical |
| 4.7 | **The patch's binding hash `b911a151…` resolves to NOTHING.** I hashed **every** version of `paper/det3-conductor.tex` in `b23-05-paper1`'s history; the digest appears nowhere. Its "applies cleanly" assertion and its self-checks are unverifiable. **The patch is usable — the two target passages are intact at `bc7e62b7`, lines 176/560 against the stated 175–179/559–561 — but its binding is not** | **UNBOUND** | INDEPENDENT check over the branch history | **not pre-formed; the clearest single case for G29** |

### 11.5 Priority 5 — Paper 2 and the cap-theorem label

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 5.1 | **B2 CONFIRMED: Theorem 9.1 is false as stated.** `dim D^det_4 = 34` in `dim W_4 = 35` — **the paper's own Prop. 2.1** — so `I(D^det_4)` is principal and nonzero and `mult_det < a` at and above its generator. **A theorem whose proof proves something weaker than its statement is false as stated** | **REJECTED as stated** | READ + independent check | ruling |
| 5.2 | **The repair is on the record and the headline survives.** Restate as `blindness_slab.md` Theorem A's three clauses, citing `e` (`e ≥ 10` CERTIFIED, `e = 320112` ADOPTED, carried separately). `Δ ≤ 0` on the slab follows from Prop. 6.1 / `n4_gate_containment`, a **containment** and therefore degree-free | PROVED (the repair) | READ + independent check | ruling |
| 5.3 | **B2 is the highest-severity item in Batch 24** — a false theorem in a paper — and also cheap to fix | — | — | ruling |
| 5.4 | **B3 CONFIRMED**: the gate is `ℓ ≥ 5`, not `ℓ ≥ 6`, on the paper's **own** Thm 3.1 (`P_5 = R_5`) and on `n4_gate.md` / `PROVED.md`. **A gate one step too tight silently declares the 2,571-label open region empty** — the worst direction | **CONFIRMED** | READ | ruling |
| 5.5 | **B4 CONFIRMED**: `[−4,−2]` not `[−4,+1]`, CERTIFIED conditional on ADOPTED `dim N₁₃ = 73`. **The substantive change is the sign, not the interval.** B24-06's `[AUTHOR]` handling of the uncommitted `[−4,−3]` narrowing is **correct** — G26 applied against the producer's own interest | **CONFIRMED** | READ | ruling |
| 5.6 | **B1 ACCEPTED on B24-06's assessment, not independently verified.** Should be checked at Kadish–Landsberg, not repaired from the record | **ADOPTED** | READ | honest negative |
| 5.7 | **B5 CONFIRMED and PARTLY DISCHARGED** — a finding B24-06 could not make: **B24-02b read LMR and recorded PRIMARY** (§§1, 2.3, 3.1, 3.2). **Paper 2's repair is cheaper than B24-06 priced it.** Two things must travel: cite **Thm 2.3.1 never Thm 1.0.2** (halved and mutually inconsistent), and carry `(★)` | **partly discharged** | READ of both packets | **cross-packet finding** |
| 5.8 | **Beauville carries UNREAD at its points of use and must be read to B24-02b's standard before Paper 2's repair cites it** — one reviewer-hour, no pilot | **UNREAD** | — | ruling |
| 5.9 | **B24-03's refusal to re-label C11 was CORRECT**, and for the right reason: a writing slot re-labelling a theorem to match a sibling paper makes a ruling it has no authority for. **Recording the divergence before either paper circulates is the whole value** | **CONFIRMED** | READ | ruling |
| 5.10 | **The right label is `PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level) and Gulliksen–Negård (SECONDARY)` — the source wording, which neither paper currently carries.** Paper 2's flat "we prove" **drops the dependency and must be corrected before circulation**. C11's "ADOPTED modulo" **misdescribes provenance** — the theorem is the programme's own (session 40); its *inputs* are adopted — but errs conservatively. **This ruling is mine and nobody else's; G-32 closes on it** | **PROVED modulo (three named, ADOPTED)** | READ | **ruling reserved to this review** |

### 11.6 Priority 6 — Paper 3

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 6.1 | **Claims table: 50 IDs, C01–C50, no gaps. CONFIRMED** mechanically | **CONFIRMED** | INDEPENDENT extraction | mechanical |
| 6.2 | **Five stale rows — C23, C30, C35, C36, C37 — CONFIRMED**, each self-marked `stale row n of 5` so the count checks from the file. Spot-checked C36 and C37 against packets; **both labelled at the strength the packets support and not above**, and both carry their inconvenient facts (the rank-58 witness; B23-10's non-replay) in the row | **CONFIRMED** | READ | ruling |
| 6.3 | **The stale/superseded distinction is real and correct.** *Stale* = the row's own label moved; *superseded* (C34) / *scoped* (C44) = the row stands, an internal clause was replaced or narrowed. **Two such rows, as the brief says** — and the file's finer SUPERSEDED/SCOPED split is an improvement on the brief, not a divergence | **CONFIRMED** | READ | ruling |
| 6.4 | **G-A1 is Question 6.5. CONFIRMED by independent derivation** from `\newtheorem{...}[theorem]` shared counters and source order: 6.1 lemma, 6.2 prop, 6.3 thm, 6.4 prop, **6.5 question** — and all four numbered predecessors match `CLAIMS.md`'s C34/C35/C36/C37 | **CONFIRMED** | INDEPENDENT derivation; **nothing compiled** | mechanical |
| 6.5 | **The right-way corner is scoped to the determinant part at ALL FIVE occurrences** (lines 114, 197, 647, 836, 1004). **No unscoped occurrence exists.** B23-10's requirement is met and exceeded | **CONFIRMED** | READ | ruling |
| 6.6 | **Consequence: Paper 3 is true whichever way G-A1 resolves**, because every claim is already restricted and the boundary is already named as the principal open question. **This drives the §9.3 sequencing** | — | READ | ruling |
| 6.7 | **C50's precision CONFIRMED by exact arithmetic**: at `n = m²/2` (`m` even) the visible range collapses to exactly one row (`m = 4, 6, 8` → rows 17..17, 37..37, 65..65). LMR's inequality is **not strict** there | **PROVED** | INDEPENDENT EVALUATOR (pilot 1 C) | mechanical |
| 6.8 | **C35's dimensions independently corroborated**: `31 + 5 − 1 = 35` reproduces `dim T2` affine, confirming both figures **and** that `T2` and `Σ_Π` are different objects in different spaces | **CONFIRMED** | INDEPENDENT EVALUATOR (pilot 1 D) | unasked |
| 6.9 | **G-30 SUPPORTED.** All three reported items are in the bytes; the C48/row-1 edit is exactly what B24-02 §4.4 establishes, with premises enumerated. **Carry: "three negative controls" → "one control at three points"** (11.3.13) | **SUPPORTED** | READ + REPLAY | ruling |
| 6.10 | **G-31 SUPPORTED, and §E's description is the most careful of the four** — it explicitly refuses to call the edit a formality and names all three travelling conditions correctly. **Subject to 11.3.7–.8: the label is `PROVED modulo (★)`** | **SUPPORTED** | READ | ruling |
| 6.11 | **G-32 SUPPORTED, and the edit is correctly *no* edit.** With 11.5.10 now on the record, **G-32 closes and C11 becomes `PROVED modulo …` — a Batch 25 edit on this review's authority** | **SUPPORTED** | READ | ruling |
| 6.12 | **G-36 SUPPORTED AS TO SUBSTANCE, NOT AS TO ONE PHRASE.** D1, D2, D2′, the six-item list and the claim ID all check out. **`GAPS.md` §E's "of the same kind and scope" is §E's own upgrade of a coverage claim into a kind claim and is not in the packet** (11.2.9). **The edit goes in with the packet's wording and the witness named** | **SUPPORTED with amendment** | READ | ruling |

### 11.7 Priority 7 — the integrator's record

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 7.1 | **(a) Disclosing the phantom B24-01 packet was right and is to the integrator's credit; the handling is INCOMPLETE.** The claims were then transcribed at full strength anyway. **A disclosure not followed by a consequence leaves the record where it was.** Both claims take the producer-relay-only label of 11.4.2–.3 | **handling incomplete** | READ | ruling |
| 7.2 | **(b) The `T2` → `Σ_Π` correction is right**, and the two figures are consistent *because* the objects differ (`31 + 5 − 1 = 35`) | **CONFIRMED** | READ + INDEPENDENT arithmetic | ruling |
| 7.3 | **(b) The integrator's reading is CONFIRMED: `deg f ≥ onset I(D35 ∪ Σ_Π)` is entirely cubic-side and rightly stands untouched.** Verified from the paper's source, not the ledger: Lemma 6.1 is titled *"restriction to the cubic factor"* and **defines `Σ_Π := {quinary cubics containing a plane}` inline in the displayed formula**. Writing `T2` there would have been a genuine error. **Stopping at the boundary of the actual error, and asking rather than assuming, is the right handling** | **CONFIRMED** | READ of `det4-blindness.tex` + INDEPENDENT arithmetic | **the integrator's explicit request; confirmed** |
| 7.4 | **(c) YES — G9′ needs a reporting clause as well as a use clause.** **A use clause is enforced at the moment of use by the person least able to notice it; a reporting clause is enforced at the moment of writing, when the act is visible.** The risk is not writing a memory but *reading one in a later slot without knowing what it is*, at which point the use clause has nothing to bite on. **Two batches, two slots, two producers is a pattern**, and both were caught by an integrator reading a relay rather than by any gate. **Amended wording in §7.3** | **G9′ AMENDED** | READ | ruling |

### 11.8 Priority 8 — the two threads

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 8.1 | **I decline to certify the rational candidate real.** Two-prime agreement is evidence, not a `Q`-proof — **the same category error as taking a floor from a ceiling** (11.3.1). The record's MEASURED / `Q`-rank-OPEN / height-2842 labels are correct and I change none | **MEASURED**, `Q`-rank **OPEN** | READ | ruling |
| 8.2 | **Do NOT price the two-number check as a Batch 25 item.** Payoff, not cost, is the obstacle: it *"would upgrade one label in a `D = −1` cell and change no direction"* | **not funded** | READ | ruling |
| 8.3 | **Record it as an opportunistic rider.** The check is seconds of exact arithmetic on integers of height ~3000. **Price is not the obstacle.** Any Batch 25 slot already running exact rational arithmetic nearby may do it in the same pilot and report in one line | — | — | ruling |
| 8.4 | **(b) The equivariance constraint IS worth a Batch 25 half-slot — for a better reason than offered.** Not "a second lineage" but: **it is the first route to the C45 floor that passes through neither `(★)` nor LMR** (11.3.7–.8). **And it is correctly sized**: outcomes (b) and (c) are each a paragraph, outcome (a) discharges a load-bearing premise. **A question whose negative answer costs a paragraph and whose positive answer discharges a premise is the ideal half-slot** | **worth a half-slot** | READ | ruling |
| 8.5 | **I make no finding on the mathematics** of 8.4 — I did not verify the group or the decomposition, and I rule only on whether it earns the half-slot | **OPEN** | — | honest negative |

### 11.9 Priority 9 — gates and Batch 25

| # | ruling | label | method | pre-formed? |
|---|---|---|---|---|
| 9.1 | **G29 ACCEPTED in principle.** The case is B24-01, which produced **all four** failure modes at once: unbound claims, a relayed prior-art finding, a patch bound to a nonexistent digest, and a brief asserting a packet that does not exist. **No gate on the books catches any of them** — G26 needs a claim in a packet, and B24-01 made no packet | **ACCEPTED** | — | ruling |
| 9.2 | **G29(b) ADDED — every printed sha256 must resolve to a committed object, or be labelled as naming an uncommitted state.** G29 as drafted would not have caught `b911a151…` (11.4.7) | **ADDED** | — | ruling |
| 9.3 | **G29(c) ADDED — a brief or ledger may not assert a packet's existence; it cites the commit and manifest hash or states that none exists.** The PART 14 failure was upstream of the producer | **ADDED** | — | ruling |
| 9.4 | **G29 must NOT require a full manifest from an edits-only slot** — only a short report binding what changed, with before/after hashes. **B24-03 is the model.** The gate should demand bindings, not ceremony, or it will produce empty manifests and a longer record that is no more checkable | **scope limited** | — | ruling |
| 9.5 | **All other gates stand: G1–G28, G5′, G9′ (as amended at 11.7.4), G14′, G15′, G20′** | **STAND** | — | ruling |
| 9.6 | **The integrator's "value has migrated into the negative" is DISPUTED in its premise, accepted in its conclusion.** Batch 24 produced **two genuine positives** — B24-02 made row 1 unconditional across `N = 5..8` on elementary premises, discharging K5; B24-02b closed C45. **What is exhausted is the candidate pipeline, not the record**, and the write-up should say so | **DISPUTED in part** | READ | ruling, as invited |
| 9.7 | **FIRST: (b), the four Paper 3 edits.** Fully unblocked — all four packets committed at the pinned commits. **Prerequisite: none remaining.** Carry the three corrections at 11.6.9, .10, .12. **Plus a fifth edit unblocked by this review: C11 → `PROVED modulo …`, closing G-32** | **order: 1** | — | ruling |
| 9.8 | **SECOND: (a), Paper 2's repair, B2 first**, then B3, B4, B1-at-source. **Cheaper than B24-06 priced it** because B24-02b partly discharges B5 (11.5.7). **Add the cap-theorem label in Thm 7.1 and the abstract** (11.5.10). **Read Beauville first** (11.5.8) | **order: 2** | — | ruling |
| 9.9 | **THIRD: (d), B24-04 Q2 — large tail with small treewidth.** The best live mathematics on the table; **a negative is worth as much as a positive**. **Prerequisite: none** — Theorem 1 is PROVED and supplies the constraint. Carry B24-04's two warnings so they are not read into the answer | **order: 3** | — | ruling |
| 9.10 | **FOURTH: the equivariance half-slot** (11.8.4), **and — small, and a reading task, not research — settle `(★)`'s label** (11.3.8), which is the most consequential unlabelled thing in this review | **order: 4** | — | ruling |
| 9.11 | **FIFTH: (c), G-A1 — do it, but it gates NOTHING.** Per 11.6.6 the paper is honest either way, so the risk is to the programme's ambitions, not the paper's correctness. **That is why it can wait and why it must not be quietly dropped: an open question named in a published paper is a commitment.** None of its three routes is a pilot | **order: 5, not a prerequisite** | READ | ruling |
| 9.12 | **NOT FUNDED: (e) row 2 at `2 ≤ j ≤ N−4`.** `CLAIMS.md` C23 describes it in its own words as *"a statement that nothing is known"* — no instrument, and no negative worth having | **not funded** | READ | ruling |
| 9.13 | **NOT FUNDED: (f) the `s_rep = 0` candidate with `Y ↦ Yᵀ`. Apply D2′ to it first** — if it fails at a pure power it dies for the cost of a sentence, which is the best immediate demonstration of D2′'s value | **not funded pending a one-line test** | — | ruling |
| 9.14 | **(g) "nothing more" is NOT supported**: four verified edits ship a paper, a false theorem awaits repair, and one live question has a valuable negative | **rejected** | — | ruling |
| 9.15 | **No cell nominated. No gap claimed. No worker requested.** | — | — | limits observed |

### 11.10 Gate defect found in this slot

| # | ruling | label |
|---|---|---|
| 10.1 | **`negation missing for `b24_10_``.** `.gitignore:51` ignores `results/logs/*.pid`; negations run `!results/logs/b16_10_*.pid` … `!results/logs/b23_10_*.pid` and **stop at b23_10**. This slot's `b24_10_p1_arith.pid` is ignored; its `_resources.json` is not. Verified with `git check-ignore -v`. **I did not edit `.gitignore`** — one line is needed before this slot's receipts are staged | **REPORTED** |

---

## 12. Resources, receipts, manifest

**Pilots: 1 of 3.** `b24_10_p1_arith` — wrapped via `analysis/b15_bound.py`, `--seconds 60`,
`--memory-mb 512`, `PYTHONDONTWRITEBYTECODE=1`, `--name b24_10_p1_arith`, `--slot 10`.
Started `2026-09-20T17:00:41Z`, wall **0.0030 s** of 60 s, exit code **0**, job object enforced,
1 worker, 1 BLAS thread. **No cap was approached.** `Get-Process python*` returned nothing before
launch. Two pilots unspent. Exact rational arithmetic only; no floats in any comparison, no
randomness, no project code imported, no network.

| artefact | path |
|---|---|
| this report | `docs/b24_10_review.md` |
| pre-formed verdicts (mine) | `results/b24_10/preverdicts_formed_before_reading_v3.md` |
| pre-formed verdicts (prior session, bound, **not edited**) | `results/b24_10/preverdicts_formed_before_reading_v2.md` |
| dead fragment (bound, **not edited**) | `results/b24_10/preverdicts_formed_before_reading.md` |
| pilot source | `analysis/b24_10_p1_arith.py` |
| pilot output | `results/b24_10/p1_arith.json` |
| pilot receipts | `results/logs/b24_10_p1_arith.pid` (**ignored — see 11.10.1**), `results/logs/b24_10_p1_arith_resources.json` |
| seal script | `analysis/b24_10_seal.sh` |
| seal log | `results/b24_10/SEAL_LOG.txt` |
| manifest | `results/b24_10/MANIFEST.json` |

**Timestamps** are UTC with a `Z` throughout this report, except where a quoted ledger line is
marked local by its own source (the integrator's observation logs are local, UTC−4, and are quoted
as such).

**Nothing was edited that this slot did not create.** No sealed report, manifest, packet, paper
file or ledger was modified. `ATTRIBUTION_PATCH.md` was not applied. Nothing was compiled. Git was
read-only: no commit, no push, no fetch. HEAD at the end of the slot is
`239dd6e84417ab04914a8d84cca02ddf754bf1fb`, unchanged.
