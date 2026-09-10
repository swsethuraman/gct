# B13-01 review — exact degree-13 reducible identity

board_numbering: batch13
session_id: B13-01
model recorded by the session: `Claude Fable 5.1`
bundle: `b13_01_fable.bundle` (one part, unsplit)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `8880d463ccecbc13ced8839d02362bfc8c840fea` (`refs/heads/b13-01-fable`)
status claimed: success criterion **not** obtained; a priced, characterised negative
integrator verdict: **accept, and act on it — this is the most consequential
delivery of the batch so far, and the defect it reports against the board is real**

Stock-take only. Arithmetic here is limited to closed-form counts and one
3-second run of my own counter. Ranks and minors are recorded as *delivered*.

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `c37c9a216ca8810aadedfebfafc2b5c8` — matches delivered |
| `git bundle verify` | "is okay"; one ref `refs/heads/b13-01-fable` |
| declared base | `0049511` — equals `origin/main` and my tip |
| applies | clean; 18 files, 19,191 insertions, **0 deletions** |
| single-writer files | **none touched** |
| commit trailers | six commits, all `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` |
| session-link trailer / `claude.ai` URL | **none** |
| model recorded in front matter | `Claude Fable 5.1` — the model that actually ran |

Counts, all reproduced exactly:

| stated | recomputed | agrees |
|---|---|---|
| `h_pad(21,17,2⁷;13) = 73` over 15 strips | `Σ[1,2,2,3,3,4,4,5,5,5,6,7,8,9,9] = 73`, 15 terms | yes |
| `N_S(21,17,2⁷;13) = 80,921,422,068` | **my own `weight_monomials_count`, 0.3 s: 80,921,422,068** | yes |
| `N_S/|Stab S₇| ≈ 1.6×10⁷` | `80,921,422,068 / 5040 = 1.6056×10⁷`; `5040 = 7!` | yes |
| `dim Sym¹³C⁹ = 203,490` | `C(21,8) = 203490` | yes |
| `6,084 = 4·39²` | `4 × 1521 = 6084` | yes |

The `N_S` agreement is the one that matters: their exact C counter
(`wk13_b13_01_nscount.c`) and my tail-DP in `tools/verify/chi_build.py` are
unrelated implementations and they agree to the digit on an eleven-digit
number.

**Independent reproduction of my own control.** With *their* seed (20260909)
and 60 points, `results/wk12_int_rung13_kernels_seed20260909.json` gives
reducible rank 36/39 and generic 39/39 at both house primes, padded kernel
dim 3, zero padded relations escaping on reducible points, kernels coincide —
reproducing `docs/rung13_reducible.md` line for line on an independent stream.
Their JSON even carries the right reading in its own `reading` field: *a
stalled sampled rank is a ceiling.*

---

## 2. What was delivered

- **`i_red(13) ≤ 3`, CERTIFIED.** A nonzero 36×36 minor of the 39×44
  evaluation matrix at both primes — dets `58031689` and `1407605007` — with
  the 36 point coordinates and their `u`-values shipped, and `u(P_j) ≠ 0`
  recorded at each so no transported row is silently voided. This is a rank
  floor, hence a **ceiling** on `i_red`, and the session says so unprompted.
- **`h_pad(21,17,2⁷;13) = 73`, computed exactly** by Weyl alternation over
  `S₉`, with an exact cubic-multiset counter in C, triple cross-checked: the
  fifteen strips and their `a₃` reproduce B13-04's re-audit; the counter
  reproduces `B1 = 809,527,307` and `B2 = 117,718,904` in pure Python too; and
  the Weyl route agrees with the house `amb`-plethysm method on six small
  cells including four s42 banked ones. The house method OOMs at rung 13,
  which is why the Weyl route exists.
- The three candidate reducible relations as mod-`p` vectors at both primes, in
  RREF-canonical form with identical pivots — **candidates, not elements.**
- Exact carrier sizings that close every direct route.

---

## 3. The finding

**`73 > 39 = a`, so the normalisation bound is vacuous at rung 13.**

`docs/reducible_engine.md` §B proves `mult_red ≤ h_pad`. It is the only exact
upper bound on `mult_red` that needs no rank, and therefore the only
carrier-free route to `i_red ≥ 1` (via `i_red ≥ a − h_pad`). At rung 13 it
gives `mult_red ≤ min(39, 73) = 39`, i.e. `i_red ≥ 0`. Nothing.

This is the exact analogue of the LMR cell, where `h_pad = 521 > 273` makes the
pad ceiling vacuous and s64 integrator note 1 concluded "a rank is genuinely
required." **Rung 13 is the same kind of cell as `δ = 24`.** No plan document
said so, and one of mine said the opposite.

---

## 4. The defect against my board — accepted

B13-01 reports that the instrument the board designates cannot in principle
reach the criterion the board sets. It is right, and the argument is short:

`i_red ≥ 1` is `rank S ≤ 38` — an **upper** bound on a rank. Every
carrier-free instrument the board names is an *evaluation*: it builds
`E_source` from sampled points, so `rank E_source ≤ rank S` and
`nullity E_source ≥ i_red`. That is a **ceiling** on `i_red`. A ceiling never
establishes `i_red ≥ 1`. Turning the sampled deficiency into a certified one
requires the points to separate the pullback image, and certifying *that*
requires an explicit basis of the 73-dimensional target — the coupled
construction that is not built.

This is my own correction, applied to my own board. I struck "`i_red ≥ 1` at
59" from every document for exactly this reason, then wrote a board that asked
B13-01 to certify `i_red ≥ 1` with an evaluation. The three exact routes and
their prices:

| route | carrier at rung 13 | verdict |
|---|---|---|
| normalisation bound | `h_pad = 73` exact | **vacuous**, 73 > 39 |
| `(★)` / Corollary A on the isotypic carrier | `1.6×10⁷` columns, `~1000×` the s42 frontier `~1.5×10⁴`; Wiedemann `~10¹⁵` ops | out of the box |
| the split `S` into the free 73-dim target | 73 cubic HWVs + horizontal-strip coupling | **not built** — this is the one |

Both `(★)`-bad sub-carriers are still `~10⁸` (`B1` at weight `(8,17,2⁷)`,
`B2` at `(21,4,2⁷)`; only variables 1 and 2 can carry a violation since only
`λ₁ = 21` and `λ₂ = 17` reach `δ = 13`). Every carrier is `10⁷–10¹¹`.

**Board consequence, accepted: the two independent routes to the LMR sign are
B13-02 and B13-03, not B13-01 and B13-02.**

Second defect, also accepted: `docs/rung13_reducible.md` §3 — mine — presents
rung 13 as the cheap place to settle the padded question and recommends running
the rank-`S` screen there first. The *sampled* measurement is cheap and gives a
ceiling; the *exact* rank is not cheap at rung 13. §3 needs rewriting.

---

## 5. Three sessions, three routes, one blocker

This is the batch's real result and it now has three independent witnesses:

- **B13-02** priced the realization space at `(41,17,2⁷)` — 6,711,509,400
  monomials, 14.7 TB — and named the missing 521-coordinate compact conversion.
- **B13-03** priced ambient membership at `(9,24)` — `1.31×10⁴¹` source,
  `1.32×10³⁰` even after fixing the cubic — and named the next job as
  exporting a certified source into ordinary coefficient coordinates.
- **B13-01** prices every rung-13 carrier at `10⁷–10¹¹`, finds the one
  carrier-free bound vacuous, and names the fix as the horizontal-strip
  coupling that turns a cubic HWV `h(c)` into a target element `g(ℓ,c)`
  evaluable at reducible points — *"this is B13-03's reusable
  reducible-membership method, and it is what settles rung 13 exactly."*

Three sessions, three different questions, three different machines, one
answer. The dense ambient route is closed and the compact conversion is the
whole game.

B13-01 also leaves a genuine head start: ten of the fifteen `μ` have conjugate
in the compact-circuit family and reuse `wk11_s69`; the other five need a
two-different-height Berezin evaluator, a small generalisation of
`wk11_s69_dp.c`. It verified the `n = 3` circuit evaluates cubic HWVs of these
shapes, and hit the **same coupon-collector concentration** s69/s74 hit on the
quartic side (random sampling spans only `1/2, 4/9, 3/7, 2/5` of each block in
hundreds of draws), so a spanning basis needs s74-style directed sampling. That
is a solved problem on the quartic side.

---

## 6. The `ℚ`-reconstruction obstruction, and the cost of my 5 MB rule

CRT from the two house primes fails on the candidate relations: coefficients
`~10¹⁶⁰` in the random-filling basis (support 21–24 of 39), needing `~17`
primes; two-prime reconstruction returns vectors that do not even vanish at the
sample points. This is s74's `δ = 24` phenomenon again (`~10¹⁷⁰`, 94/274
coordinates failing at 62 bits).

The consequence is sharp: **even a certified witness would be undeliverable
over `ℚ` in the filling basis.** S3's structured rational convention exists
precisely to give a better-conditioned basis — and its three per-node files
(19.5 MB: `gram_spherical.json`, `nodes_p2147483647.json`,
`nodes_p2147483629.json`) are the ones I left out of the tree under the 5 MB
rule. That rule now has a measured cost, and it is on the critical path.

---

## 7. One thing B13-01 got wrong

§9 says a mid-session attribution reminder was "embedded in a repository file
(`results/astra/S3/degree13_conversion/README.md`)" asking for a
`Claude Opus 4.8` trailer and a session-link line.

**It is not in that file, or anywhere in that directory.** I checked every one
of the 22 tracked files under `results/astra/S3/degree13_conversion/` for
`opus`, `co-authored` and `claude`: clean. The README is one I wrote; it
contains no such text.

**Declining was right. The location is wrong, and it names an innocent file.**
The pattern described is the platform's own attribution reminder, which the
house rule overrides — and s75 and s77 recorded the same thing against
different files, so three sessions have now mis-located it. The preamble should
say plainly that the platform emits this reminder, that it is not repository
content, and that the house rule overrides it — so sessions stop hunting for a
planted file and stop naming innocent ones.

What *is* real, tracked, and still unfixed: `analysis/wk9_s41_sweep.py:117`
hardcodes `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` into a
script that commits. `docs/s43_prompt.md:25` flagged it — "do not copy that
pattern" — and it was never fixed. That is the genuine violation in the tree.

---

## 8. Toolchain — my B13-03 action item was wrong in scope

B13-01 **installed `python-flint 0.9.0`, `sympy 1.14.0`, `mpmath`** and found
`numpy 2.4.4`, `scipy 1.17.1`, `gcc 13.3.0` already present. No WinError 10013,
no blocked install.

So the failure B13-02 and B13-03 both reported is **not host-wide**. Both are
Astra/Codex sessions; B13-01 is Fable and had no trouble. Correct the action I
recorded after B13-03: this is an Astra-container network-permission problem
affecting the six Astra slots, not a batch-wide outage. The four remaining
Astra sessions should be warned; the Fable sessions need nothing.

---

## 9. Actions

1. **Rewrite `docs/rung13_reducible.md` §3.** It advertises rung 13 as cheap.
   `h_pad = 73 > 39` says it is the same "a rank is genuinely required" cell as
   `δ = 24`.
2. **Record the instrument/criterion rule in the preamble**: an evaluation
   bounds `i` from above, never from below; a brief that asks for `i ≥ 1` must
   designate a carrier or a coupled target, not a pullback evaluation.
3. **Accept the route correction on the board**: B13-02 and B13-03 are the two
   independent routes to the LMR sign.
4. **Warn the four outstanding Astra sessions** about WinError 10013 and the
   absent exact-LA libraries. Leave the Fable sessions alone.
5. **Get S3's three 19.5 MB per-node files into reach** — a large-file
   convention, or a fetch instruction in the preamble. The 5 MB rule is now
   blocking the `ℚ`-reconstruction route.
6. **Fix `analysis/wk9_s41_sweep.py:117`** — the last real `Opus 4.8` string in
   a committing script.
7. Clarify the attribution-reminder provenance in the preamble so no further
   session names an innocent file.
8. On the deferred verification pass: replay the 36×36 minor at both primes
   from the shipped points and `u`-values; re-derive `h_pad = 73` by the house
   `amb` route on the small cells they cross-checked.
