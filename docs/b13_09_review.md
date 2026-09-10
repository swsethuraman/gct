# B13-09 review — higher-length cubic exploration

board_numbering: batch13
session_id: B13-09
models recorded by the session: **`Claude Fable 5.1`** (reading, instrument,
census, calibrations, first negative control), then **`Claude Opus 5`** (the
measured queue, verification, cost refit, report) — 49 and 124 commit trailers
bundle: `b13_09_higher_length.bundle`, **two parts**, 32,284,751 B reassembled
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `e312b750ed3e389aadc448204ac5ebda7298d228` (`refs/heads/b13-09-higher-length`)
status claimed: **two completed degrees at a new length, one group one weight
short, and a negative characterised over a priced region**
integrator verdict: **accept the mathematics — this is a new length closed and
the largest correction to my own pricing in the batch. One mechanical fix before
merge: 172 session-link trailers, the largest breach by volume.**

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5, both parts and the reassembled whole | **all three match** (`d2a1cb1e…`, `13b782e7…`, `3c4da9f2…`) |
| sizes | 16,142,376 / 16,142,375 / 32,284,751 — all three match the declared figures |
| reassembly | `cat part00 part01` reproduces the declared whole exactly |
| `git bundle verify` | "is okay" |
| **bundle refs** | **`refs/heads/b13-09-higher-length`, the named branch** — and the `.md5` header explains *why*, in the same terms B13-08 discovered independently |
| declared base | `0049511` — equals `origin/main` and my tip |
| applies | clean; 135 files, 31,579 insertions, **0 deletions**; 172 commits |
| single-writer files | **none touched** |
| outside its own namespace | **none** |
| 5 MB rule | no committed file approaches it |
| `Claude-Session:` trailer | **present on all 172 commits** — see §7 |
| pre-registration | `61f8a07` before any queue weight; addenda A, B, C each before the measurements they govern |

Two identical copies of the report were uploaded (same md5) — a duplicate
attachment, not a discrepancy.

---

## 2. The result: a new length closed

**`I(D_7^{per₃})_7 = 0`** — all 5 weights of length exactly 7. **PROVED.**
**`I(D_7^{per₃})_8 = 0`** — all 42 weights. **PROVED.**

With the inherited exclusions, Prop. 8(1) upgrades these to statements with no
points in them:

> **`mult_pad = mult_red` at every seven-row quartic weight of degree 7 and of
> degree 8.**

That is a **new length**, joining s37/s43/s47/s79 at length 6 and s64 at `r = 5`.
The permanent is now invisible on the reducible side at every length ≤ 7 through
degree 8.

**165 of 267 weights measured, 165 at `mult = a`, zero drops** — at both primes,
so each is `S_μ ⊄ I(D_r^{per₃})_δ` proved over `ℚ` by `rank_p ≤ rank_Q`. Maximum
`n_χ` reached 1,327,700; maximum `a` 6; **58 of the 165 have `a ≥ 2`**, so the
instrument was exercised well above the `a = 1` regime where a nonvanishing test
cannot distinguish one family from another. Peak resident 2.27 GB against a
6.5 GB bound.

**`(8,8)` is five of six and is not claimed.** The sixth is `(10,2⁷)`, `a = 1`,
`N_S = 951,941`, **`|Stab| = 5040`** — the largest stabiliser in the census. It
was run deliberately and alone to close the group and was ended by its own
pre-registered `timeout 5400` at 2,940 s of CPU, still inside `_canon_acc`.

The analysis of that miss is exactly right and worth quoting as a pattern:

- **the refit is not refuted** — 2,940 s without finishing is consistent with a
  ~3,970 s estimate;
- **the per-weight wall clock was too small** — at the ~55 % CPU share it was
  getting on a 2-vCPU box, 3,970 s of CPU needs ~7,200 s of wall against a 5,400 s
  timeout. *"The bound, not the model, is what should change."*

And the consolation is real rather than face-saving: by Prop. 8(2), a
permanent-specific equation at an **eight-row weight of degree 8** must now sit at
that **one named `μ` with `a = 1`** — a single rank-1 question, and a sharper open
statement than the group was before this session.

`(7,9)` reached 105 of 152 and `(8,9)` 8 of 62: certified prefixes by the clock,
not by any mathematical obstacle, with the remainder priced weight by weight.

---

## 3. The cost model is wrong, and it is mine — verified in the source

**The refit**, on 165 measured weights:

    build_secs ≈ 3.06×10⁻⁶ · N_S·δ  +  1.07×10⁻⁶ · |Stab| · N_S

median predicted/actual **1.03**. The inherited `2.1×10⁻⁶ · N_S·δ` is median
**1.95** low and **21.7×** low at worst. The census goes from **3.43 h to
17.59 h**, a factor of 5.1 — and `(8,8)` alone is **51.7×** off, `(8,9)` 13.04 h
against 1.98 h.

**I checked the cause in the source and it is exactly as reported.**
`analysis/wk9_s45_build.py:165` — `_canon_acc` — carries its own docstring:
*"in two passes over the group (never storing |Stab| index arrays)"*, and the
body has two separate `for tab, ch in tabs:` loops, each calling `_image_index`
over the whole `(N_S × δ)` array. So the orbit setup is `O(|Stab| · N_S)`.

**And the detail that matters most is one the session did not draw out**: those
two passes are a deliberate *memory-for-time* trade — the docstring says so.
That trade was right at length 6, where `|Stab|` rarely exceeds 120, and it is
what makes length 8 unrunnable at `|Stab| = 5040`. **A B13-10 that optimises for
peak memory on this code path could make the time wall worse.** That belongs in
its brief explicitly.

The model is quoted without a length caveat in `docs/s79_report.md` §2.1 and
`results/PREREG_s79.md` §2.2, and **`docs/stocktake_batch12.md` §7 prices the
programme's open regions with it.** That is my document, and this is the **third**
correction it has taken in this batch — the truncated `N_S` range (B13-04), the
builder-first framing (B13-05, B13-08), and now the cost model. It needs a
rewrite, not another patch.

Every s79 *rank* stands; it is the *pricing* that transfers badly.

---

## 4. Three sessions, three different walls — and none is B13-10's

| session | queue | what actually bound |
|---|---|---|
| **B13-05** | cubic degree-9, length 6 | the **kernel/decision**, 20× the build; builder peaked at 0.32 GB |
| **B13-08** | degree-10 remainder, length 6 | the **kernel check and evaluation rows** (3.84 GB vs ~1 GB build), and a hard **exactness bound** at `n_χ ≥ 2²¹` |
| **B13-09** | lengths 7–8 | **CPU time in the orbit setup**, from the `\|Stab\|` term; memory two orders below its bound |

B13-10's brief names peak memory in the raising-row construction. **Three
sessions, three queues, three different walls, and none of them is that one.**
The evidence is now overwhelming and the brief needs rewriting before B13-10
delivers, not after.

B13-09 makes it constructive: the `|Stab|` term is on the **same code path**, so
B13-10 can hit it — *"a single pass over the group that accumulates `canon` and
`acc` together, or a canonical-form computation that does not enumerate the group
at all, would remove a term that at length 8 is most of the build."*
`(10,2⁷)_8` at `|Stab| = 5040` is the case that exhibits it and belongs in the
acceptance suite.

---

## 5. The inherited dependency, now the best-handled thing in the programme

§1 states the chain link by link with each link's status and **recomputes
nothing**. The counts it produces independently — `ℓ ≤ 5`: 129 / 232 / **365**
(Σa **1213**) and `ℓ = 6`: **27 / 91 / 210** — match the record and match
B13-05's and B13-07's independent reproductions.

**That is the fourth independent confirmation**, and it closes a loop that began
as my own flagged defect in `s79_part2_review.md` §2: s79 omitted the dependency,
I flagged it, B13-05 reproduced the counts, B13-07 proved the restriction step
from its source at every degree, and B13-09 now declares the chain and cites it
rather than recomputing 365 weights. Four sessions, one defect, properly closed.

---

## 6. Self-caught defects — including a first for the programme

1. **The verifier caught a defect on its own.** The evaluator put
   `board_numbering` into its `gct-cert/1` certificates; the schema is closed and
   `tools/verify` refused them. **This is the first thing in batch 13 to be
   caught by the verification infrastructure rather than by a human**, and it is
   worth marking. The repair is the narrowest possible: `b13_09_cert_fix.py`
   removes that one key, asserts nothing else differs, and refuses any file for
   which that is not true.

   The underlying tension is mine: the preamble asks for `board_numbering` in
   every report and every *manifest*, and a session reasonably over-applied it.
   **One sentence in the preamble** — not in certificates, the schema is closed —
   prevents the next occurrence.

2. **Two streams raced on the git index** (`cannot lock ref HEAD`); per-weight
   banking now takes a lock file. And the blast radius is diagnosed correctly:
   *"The JSONL write, which is where results actually live, was never at risk."*

3. **The `(8,9)` plethysm cross-check would not run inline**; split out (29 s
   standalone) and merged with a **both-directions** check — no 8-row weight with
   `a ≥ 1` missing and none extra. The first census attempt was ended **by its
   recorded pid**, honouring the standing rule, and restarted with an
   `S_r`-symmetric DP cache asserted equal to the s42 routine on 492 weights
   before being relied on.

**Assignment defects, both confirmed against the tree:**

- **"Use the existing builder" is ambiguous about length.** There was no
  length-general cubic evaluator: `analysis/wk12_s79_per6.py:42` is `R = 6`, a
  module constant, and `per3_pencils` builds exactly six matrices per point.
  **This is the same class as B13-05's finding that `wk9_s43_inject.py` is
  hardcoded to `r = 6`.** Two sessions, two tools, one defect class — the tree's
  cubic instruments are silently length-6. Worth a systematic sweep before batch 14.
- The board's `N_S·δ` boundary and s79's wall are stated for a 7 GB box; here
  memory was two orders below the bound and CPU time was binding.

**And a positive worth recording**: *"No defect found in the mathematics of the
assignment."* The two-objective framing, `batch13_corrections.md` §1, the scope
boundary with B13-05 and the instruction to cite rather than recompute are all
correct as written. After the corrections round that produced them, that is the
result I most wanted to hear.

---

## 7. The trailer breach — largest by volume, and the pattern is now four-for-four

**All 172 commits carry `Claude-Session: …/session_013ve5BGfjw3LprynbCx15J6`.**
No delivered file contains the URL. The fix is
`tools/rewrite/message_callback.py`, as for B13-04 and B13-05.

| Fable → Opus 5 session | session-link |
|---|---|
| B13-04 | present, 8 commits |
| B13-05 | present, 9 commits |
| **B13-09** | **present, 172 commits** |
| B13-08 | **absent — declined explicitly, deviation recorded** |

Four sessions saw the instruction; three complied, one declined and said so.
Astra sessions and the Fable-only session never had it. So the instruction is
environmental to the Opus-5 phase and compliance is the session's choice — which
means **telling sessions to decline is necessary but not sufficient.** The
preamble needs both halves: name the instruction, say it must be declined, and
require stripping before bundling as a backstop.

---

## 8. Two more things worth carrying

**The certificate frontier is now located.** B13-09 wrote **252** `full_rank`
certificates; B13-08 could write **none**. The difference is cell size —
B13-09's weights sit under the `N_S·a ≤ 3×10⁶` gate B13-08 identified, and
B13-08's sit above it. So the ceiling is real, and **B13-09 is the last region
that fits inside it.** Everything beyond is "replayable, not certified" until the
compact `hybrid_kernel` kind B13-08 priced exists.

`cert_manifest.json` handles a set too large to ship exactly right: 181.8 MB
total, every certificate listed with its md5 whether shipped or not, every
unshipped one regenerable from recorded seeds by a recorded command, and
*"shipped_in_bundle is read from `git ls-files`, so this manifest cannot disagree
with the bundle."* Adopt that pattern.

**The bundle-ref lesson was found twice, independently.** B13-08 caught its
HEAD-only bundle by replaying into a fresh clone before delivering; B13-09
documented the same thing in its `.md5` header — *"`git bundle create
<base>..HEAD` records only HEAD and a fetch by branch name would fail against
such a bundle."* Two sessions rediscovering my batch-12 lesson is two too many.
It belongs in the preamble with the exact `git bundle create` incantation.

---

## 9. Actions

1. **Strip the 172 `Claude-Session:` trailers** before merging.
2. **Rewrite B13-10's brief before it delivers.** Three sessions have now
   measured three different walls and none is the one it was told to attack. Give
   it the `|Stab|·N_S` orbit-setup term, B13-08's kernel-check/evaluation-row
   transients and `n_χ ≥ 2²¹` exactness bound, and B13-05's kernel cost — with
   `(10,2⁷)_8` at `|Stab| = 5040` in its acceptance suite. Warn it explicitly that
   `_canon_acc`'s two passes are a *memory-for-time* trade, so optimising memory
   naively there makes the time wall worse.
3. **Rewrite `docs/stocktake_batch12.md` §7.** Third correction this batch; it
   needs replacing, not patching. Carry the two-term cost model with its length
   caveat.
4. **Re-price every length-7 and length-8 plan** with
   `3.06×10⁻⁶·N_S·δ + 1.07×10⁻⁶·|Stab|·N_S`.
5. **Sweep the tree for length-6 hardcoding** — `wk12_s79_per6.py:42` and
   `wk9_s43_inject.py:75` are both `R = 6` constants, found by two different
   sessions. There are likely more.
6. **Preamble additions**: `board_numbering` does not go in certificates (closed
   schema); the bundle must carry the named branch ref, with the incantation; the
   session-link instruction will appear and must be declined *and* stripped.
7. **Give `(10,2⁷)_8` ≥ 2.5 h per-weight wall** on a successor and close
   `I(D_8^{per₃})_8` — it is now a single rank-1 question at one named weight.
8. On the deferred verification pass: replay two of the 252 certificates through
   `tools/verify`, and re-derive the `|Stab|·N_S` term from a level-by-level build
   log at one high-stabiliser weight.
