# Session 49 — foundations audit, and an independent two-layer verifier

Branch `s49-audit` off `eb8cecb`.  No new science: every item is a correction to
something committed, or verification infrastructure.  Pre-registration
`results/PREREG_s49.md` (committed **before any run**, fixing seed `20260905`
and every box and prime).  Delivery by git bundle; no push; commit trailers
carry `Co-Authored-By` only, no session link (standing rule).

Nothing in the s50–s55 batch should be trusted until measured against this
session's verifier (`tools/verify/`), which runs clean over every certificate on
record.

---

## 1. Corrections made

**2.1 — both six-row cap degrees were one too large.**  The smallest minor that
vanishes on `D_6^{det_4}` has size `(determinantal rank) + 1`, not `ρ_d` (the
*smooth* rank).  Recomputed from scratch at seed `20260905`
(`analysis/wk9_s49_cap.py ladder`, `results/logs/s49_cap_ladder.log`):

| `d` | `dim S_d` | `h_d` | `ρ_d` | GN `H_{S/J}(d)` | GN ceiling | det rank (both primes) | usable minor |
|---|---|---|---|---|---|---|---|
| 7 | 792 | 126 | 666 | 120 | 672 | **660** | **661** |
| 8 | 1287 | 90 | 1197 | 140 | **1147** | 1146 | 1148 (proved), 1147 (certified) |

- **Certified cap 661** (was 666): the determinantal rank at `d = 7` is 660, so
  the size-661 minors vanish.  Re-certified over `Q` at three fresh `±10^12`
  pencils by a size-**661** multimodular certificate
  (`analysis/wk9_s49_cap.py certify 7 661`, `results/logs/s49_certify661.log`:
  `rank_Q M_7 ≤ 660 < 661`, 3/3 pencils, ~1740 primes each), which supersedes
  s44's size-666 run.
- **Proved cap 1148** (was 1197): the Gulliksen–Négård ceiling proves
  `rank M_8 ≤ 1147` at every determinantal point, so the size-1148 minors vanish
  a priori.  (The measured rank at `d = 8` is 1146, giving a *certified* 1147;
  the *proved* bound is 1148 from the ceiling.)
- Corrected bracket: **`onset I(D_6^{det_4}) ≤ 661`** certified, `≤ 1148` proved.
  No lower bracket above the trivial one is established: `mult_det = a` at all
  193 measured cells through `δ = 9`, but the measured set is not exhaustive at
  any degree `≥ 7` (`results/sixrow_record.md`), so the earlier `9 ≤` is
  withdrawn as reach-only.
- Corrected in place: `docs/sixrow_cap.md` (headers, §0, §2, §4, §8, §10, §11)
  and `docs/sixrow_cap_closed.md`.  The `(5,7)` numbers there (`ρ_10 = 5880`,
  rank 5859, drop 21) are ranks and unchanged; a minor there would be size 5860.
- **Paper 1 `prop:jaccap` has no such slip** (checked, not edited): it states
  "for smooth `F` the rank is 65; for `F ∈ D_5` at most 64" and takes the
  **65×65** minors — that is already `(determinantal rank) + 1 = 64 + 1`, because
  the five-row drop is exactly one.  The slip is specific to the six-row case,
  where the drop is `C(6,5) = 6`.  Likewise paper 2's `cap(n)` is right for the
  `r = 5` family (drop 1), and the general `r = 6` cap is `ρ_{3n−5} − C(r,5) + 1`
  (`docs/sixrow_cap.md` §8).

**2.2 — the `r ≤ 4` proof of `R_r ⊆ D_r`, written out** (`docs/r4_containment.md`).
Block construction `ℓ·c = det_4 diag(ℓ, N)` (no hypothesis on `ℓ`), plus density
of `3×3`-determinantal cubics for `r ≤ 4` (measured dominant: Jacobian rank
`4,10,20` at `r = 2,3,4`, and `29 < 35` at `r = 5`; `analysis/wk9_s49_checks.py A`),
plus one closure limit that covers every special member (`c` singular,
non-reduced, `ℓ` a component, `ℓ = 0`) at once.  Tightness of
`9·4 − 16 = 20 = dim Sym^3 C^4` is respected: the only existence claim about an
individual cubic is for a *general* one, where the count earns it; every special
member is reached by a limit, never assumed general.

**2.4 — the Pieri transport step, with explicit maps** (`docs/pieri_transport.md`).
Proposition 8 of `docs/transfer_lemma.md` re-proved on multiplicity spaces:
`μ^*` induces an **injection** `U_P/U_R ↪ (Sym^δ V ⊗ I(D_r^{per_3})_δ)^{hw}_λ`,
giving `mult_red − mult_pad ≤` the Pieri sum, an *upper* bound on the erasure.
The direction used needs no surjectivity — the external audit's reading — and
`μ^*` is indeed not surjective (its image is the non-normal `C[R_r]`), which is
no obstacle.

**2.5 — proved vs measured.**
- **Proposition D** (`docs/excess_singularity.md`): the pad side of the
  separating inequality is a **proved** lower bound; the determinantal-corank
  side is **measured** (mod-`p` coranks at `d = 6,7,8` as upper bounds; GN value
  plus the **measured** `Q_d = 0` at `d ≥ 9`).  Relabelled "proved given the
  measured determinantal coranks" and **renamed to the Macaulay-minor mechanism
  specifically**.
- **Theorem C** (`docs/washout_threshold.md`, new `docs/washout_r3_uniform.md`):
  the counting threshold `r*(m) = 3` for `m ≥ 17` was already proved uniformly;
  the **density** at `r = 3` was only measured on a finite range.  Session 49
  supplies the **uniform argument** — a structured cyclic-bidiagonal point whose
  sub-permanents are `s_3`-homogeneous with binary factors the `τ`-orbit of one
  cyclic window product, and a **window lemma** (cyclic window products of length
  `j` span `Sym^j C^2`) **proved for all `m`** by a `q`-binomial non-vanishing.
  So `Φ_{m,3}` is dominant for every `m`: **`r = 3` density is now proved, not
  measured.**  `r = 4, 5` top-row density stays measured-on-range /
  expectation-beyond.  Corroboration: `analysis/wk9_s49_checks.py` B (full `r=3`
  Jacobian rank to `m=20`), C (window lemma to `m=40`), D (sub-permanent
  structure to `m=14`).
- **s48 washout-table corrections folded in / confirmed present**: `orbit(m) =
  2m − 2`, the `m = 2` `O(4)` stabiliser, and the deficit `6` (not 2) at
  `(m,r) = (3,6)` are all in `docs/washout_threshold.md` (§0, §2, §3) and its
  table; paper 2's `cor:washout` already carries `dim P_6 = 55 < 61` (deficit 6).

**2.6 — randomised-test provenance** (`docs/randomised_protocol.md`).  From the
git history: the s44 and s48 *protocols* were pre-registered before any
computation (`2e06e3f`, `902cccd`), but the concrete **seeds** were committed
*with the results* (`e50575a`, `ddb76cd`), not in a pre-run artifact — stated
plainly.  Not a real p-hacking risk (seeds are the session date / round
constants; the drop reproduces at every seed and both primes and is certified
over `Q`), and s49 fixes it going forward by banking seed `20260905` in
`PREREG_s49.md` *before* any run.  Seeds and introducing commits tabulated.

**2.3 / 2.9 wording.**  The `ℓ ≤ 5` exclusion was justified by washout in several
docs; corrected in `docs/session_39.md`, `docs/s39_review.md`,
`docs/longweight_hunt.md`, `docs/sixrow_frontier.md`,
`results/longweight_screen.md`: `ℓ ≥ 6` is where the permanent **enters**, not a
proof that no obstruction exists at `ℓ ≤ 5`; washout (`P_r = R_r`) makes any
`D > 0` there a *reducibility* statement and does not preclude it; `ℓ ≤ 4` is
closed by containment (proved), `ℓ = 5` only by measurement.  The
degeneracy-direction pre-check (§2.9) was already in `docs/brief_wording.md` §5;
its committed three-point test set and worked example are new this session
(`tools/verify/testset/`, `results/s49_degeneracy.md`).

## 2. The verifier (2.7) — the main deliverable

`tools/verify/` is a standalone two-layer checker sharing **no code** with the
worker pipeline (it re-implements forms, coefficients, raising operators, the
Weyl-alternation plethysm, and exact linear algebra from scratch; format in
`tools/verify/FORMAT.md`).  It refuses anything it cannot parse — unknown key,
missing key, wrong type, non-canonical term — as **UNPARSEABLE** with the reason,
and never guesses.

- **Layer 1 (syntactic):** rank over `Q` (exact, by a multimodular certificate),
  rank modulo every recorded prime and both house primes, a named minor's
  determinant over `Z`, a nullity-zero claim at its prime.  A `matrix_source`
  rebuilds the Macaulay matrix of a `det_4` pencil and requires any recorded
  matrix to match it.
- **Layer 2 (semantic) — the layer that matters:** the weight of every term
  equals `λ`; every simple raising operator annihilates the vector **over `Z`**
  (integer certs) or modulo the recorded prime (mod-`p` certs, reported as such
  and never promoted); `a` recomputed by an independent Weyl alternation; `(★)`
  support; and every evaluation point **rebuilt from its substitution data**
  (pad points really are `x_0·per_3` of the recorded linear forms, det pencils
  really are `det_4` of the recorded pencil), the vectors vanishing / not
  vanishing there as claimed, at recorded and fresh points.

Self-test passes on six hand-made certificates (a true invariant, a corrupted
one, an unknown-key one, a `299`-rank Macaulay matrix, a `300`-rank false claim,
a full-rank `mult=1` cell): `tools/verify/selftest.py`.

**Run over every certificate on record.**  All lifts and kernel vectors of
s42/s41/s43/s47 were converted to the declared format
(`analysis/wk9_s49_convert.py`, worker-side) and verified:

    50 certificates in results/certs/ : PASS 50, FAIL 0, UNPARSEABLE 0, ERROR 0
    + 1 d9 cell (15,9,9,1,1,1) too large to commit (4.97 MB) : PASS, verified from scratch

Report: `results/s49_verify_report.md`.  Every integer lift passes both layers
over `Z`; every mod-`p` kernel vector passes mod its prime and is labelled
mod-`p`.  Nothing on record fails a semantic check.

## 3. Items confirmed correct (checked, not changed)

- **Paper 1 `prop:jaccap`** — no cap-degree slip (§1 above).
- **The `d ≤ 6` no-drop floor** and the `ρ_d`, `h_d`, GN ceiling arithmetic of
  `docs/sixrow_cap.md` — reproduced exactly at a fresh seed.
- **"onset ≥ 10"** — the only such claim in the repository is the `r = 4`
  determinant onset `e ≥ 10`, which is a **correct exhaustive per-degree** lower
  bound (`D_4` is a hypersurface, its ideal is principal on an invariant, and
  every invariant degree `≤ 9` is either empty or measured non-vanishing;
  `docs/e4_hunt.md`).  It is not a reach-only bracket and is left as is.
- **"the occurrence route is empty"** — this phrase does not occur; the
  repository says the occurrence route is **silent** (the correct *measured*
  statement) and explicitly that it "does not bound the onset anywhere"
  (`results/occurrence_screen.md`).  No change needed.
- **"exact whenever it fires"** — the general claim is already **withdrawn** in
  `results/sixrow_record.md` (its own section, s47's refutation); the per-cell
  "fires, exact" column entries are accurate facts about individual cells, now
  guarded by an explicit note that they are not the refuted general rule.
- **The degeneracy pre-check** returns WRONG DIRECTION on its worked example
  (Proposition D): the padded permanent is at least as degenerate as the
  determinant at every degree, and the six-variable determinant coranks
  `(90,126,141,132,141)` reproduce s44's column exactly — an independent
  reproduction of the s44 Macaulay measurements (`results/s49_degeneracy.md`).

## 4. Items now open (or flagged for the integrator)

- **`R_5 ⊆ D_5` is open** — and is the correct statement of the length-5
  question.  What is *proved* is `R_5 ⊄ im Φ_5` (s32 Theorem 5: the generic
  `ℓ·c` is not a `4×4` linear determinant); `R_5 ⊆ D_5` asks whether every `ℓ·c`
  is a **limit** of `det_4` pencils, and nothing on record decides it.  Handed to
  session 54 (`docs/r4_containment.md` §3–4).  **This is not the failure
  case of the brief** — no obstruction was found to be excluded at `ℓ = 5` on
  bad grounds; the `ℓ = 5` cells were measured and gave `D ≤ 0`.  The only error
  was the *justification* (washout, not measurement), now fixed.
- **`docs/s43_review.md` does not exist** — the batch housekeeping and the s49
  brief §2.8 both reference it for the "exact whenever it fires" removal, but no
  such file is in the repository (nor in any commit).  The claim it was to carry
  is refuted and withdrawn in `results/sixrow_record.md`, so nothing is lost;
  flagging the dangling reference.
- **Three tracked files exceed the 5 MB limit** (pre-existing, from s36, not
  touched this session): `results/s36_cells/8_8_8_2_2_d7_pad_exactZ.txt`
  (12.5 MB), `…_pad_p2147483629_vec1.txt` (13.1 MB), `…_pad_p2147483647_vec1.txt`
  (13.0 MB).  Recommend the integrator gzip them (as s43 did) or drop them; I did
  not alter another session's committed measurement data.
  **Resolved at merge:** gzipped in place (about seventeen-fold, all three now
  under 0.75 MB), with `results/s36_cells/README.md` recording the format.  The
  uncompressed blobs are removed from history by the rewrite in
  `docs/history_rewrite.md`.  All 50 files this
  session commits are well under the limit (largest 3.5 MB).
- **`r = 4, 5` top-row washout density** (`4 ≤ m ≤ 16`) remains proved on the
  checked range only; the uniform argument this session gives is for `r = 3`.
- **The six-row syzygy gap** (`onset ≤ 661` proved vs certified) is unchanged:
  the six non-Koszul syzygies of `(4,6,7)` are still not in closed form (s44/s48).

## 5. Deliverables

    docs/s49_report.md                      this file
    results/PREREG_s49.md                   pre-registration (seed, boxes, primes) before any run
    tools/verify/                           the standalone two-layer verifier + FORMAT.md + selftest + testset
    results/certs/                          50 certificates in the declared format (all PASS)
    results/s49_verify_report.md            the verifier's run over results/certs/
    results/s49_degeneracy.md               the degeneracy pre-check worked example
    docs/r4_containment.md                  2.2 (r<=4 containment) + 2.3 (r=5 open)
    docs/pieri_transport.md                 2.4 (transport with explicit maps)
    docs/washout_r3_uniform.md              2.5 (uniform r=3 density for Theorem C)
    docs/randomised_protocol.md             2.6 (seed provenance)
    analysis/wk9_s49_cap.py                 2.1 (cap ladder + size-661 certificate)
    analysis/wk9_s49_checks.py              A/B/C/D exact checks
    analysis/wk9_s49_convert.py             record certificates -> declared format
    analysis/wk9_s49_run.sh                 bounded-run launcher (timeout, ulimit, pid)
    corrected in place: docs/sixrow_cap.md, docs/sixrow_cap_closed.md,
      docs/excess_singularity.md, docs/washout_threshold.md, docs/session_39.md,
      docs/s39_review.md, docs/longweight_hunt.md, docs/sixrow_frontier.md,
      results/longweight_screen.md, results/sixrow_record.md
