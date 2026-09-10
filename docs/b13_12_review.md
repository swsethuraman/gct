# B13-12 review — global five-variable closure and a universal rank-one support

board_numbering: batch13
session_id: B13-12
model recorded by the session: `gpt-6-astra`, reasoning effort `xhigh`
bundle: `b13_12_five_variable_closure.bundle` (one part, `part00` byte-identical)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `cd716bad1684923b57f033bf44027d559fa78ddc` (`b13-12`)
status claimed: formulation repaired; universal rank-one support and triangular
family proved; global containment open
integrator verdict: **accept and merge. It corrects a claimed equivalence in
s78 that was an inference in the wrong direction, and replaces it with a theorem
whose engine I verified in two lines.**

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 / sha256 | `8b03ac28…` / `06d51740…` — both match, whole and `part00` |
| `part00` vs whole | **byte-identical**; 89,619 B, matching the manifest |
| declared base | `0049511` — equals `origin/main` and my tip |
| `git bundle verify` | "is okay" |
| applies | clean; 33 files, 44,544 insertions, **0 deletions**; 5 commits |
| single-writer files | **none touched** |
| outside its own namespace | **none** |
| 5 MB rule | none close |
| `Claude-Session:` / `Co-Authored-By` | **neither** — the Astra pattern |
| pre-registration | present, and every planned computation finished under its launch bounds |

Delivery hygiene is among the batch's best: both digests for whole and part, an
`input_manifest.json` recording **both** worktree bytes and canonical git-blob
bytes for every input (so a CRLF difference cannot be mistaken for a content
difference), a `REPLAY.md` carrying the *expected check counts*, and per-run
PIDs, logs and resource records. The `.md5`/`.sha256` files also cover a
`b13_12_changed_files.zip` that was not uploaded — documented, not checkable here.

Every count reproduces: `dim Sym⁴C⁵ = 70`, `dim Sym³C⁵ = 35`, `P(W)` dim 34;
nonanchor counts `4, 10, 20, 35` summing to 69; `133 = 64 + 69` variables;
`540 = C(4,2)²·C(6,2)` and `560 = C(4,3)²·C(7,3)`; `625 = 5⁴` and `125 = 5³`;
fixed-factor preimage `16 − 4 = 12`.

---

## 2. The correction to s78 — an inference in the wrong direction

s78 claimed `W ⊆ D5` is **equivalent** to dominance of its restricted map `G`.
B13-12 shows the argument passes through an unjustified closure-to-actual-image
step. What actually holds is

    closure(G(S)) ⊆ Z ∩ {y_bad = 0},

and **equality is an additional statement** that irreducibility of `W` does not
supply. So `G` dominant still gives containment, but **failure of dominance does
not give noncontainment** — which is the direction s78 needed.

The refutation is two lines and I verified both:

- `(a,b) ↦ (u = a, v = ab)`. The image is `{u ≠ 0} ∪ {(0,0)}`, dense because the
  pullbacks of `uⁱvʲ` are `a^{i+j}b^j` with distinct exponents. **Its closure
  meets `u = 0` in the whole `v`-axis; the actual image meets `u = 0` only at the
  origin.** The closure's slice is strictly bigger.
- `(x(x−z)) : x^∞ = (x−z)`, which still contains `(0,0)` after `z = 0`; whereas
  imposing `z = 0` first gives `(x²) : x^∞ = (1)`. **Order matters: saturate
  first, restrict second.**

The session is careful about what this does and does not do: *"These controls
refute the inference, not the unproved equality for s78's particular map."* And
s78's reduction from 149 to 98 variables survives for the restricted
actual-image problem; only the claimed global equivalence and the dismissal of
the boundary fall.

**This is the batch's recurring theme in geometric form.** Five sessions found
checks that could not fail; this one found a *proof* that ran the implication
backwards — the same family as the reversed `rank_p ≤ rank_Q` note B13-11 caught
in `s63_n3control.json`.

---

## 3. The new theorem, and I verified its engine

**A nonzero projective rank-one support already has the whole determinant image
closure as its graph image.**

With `Y = {A₅ = 0, Aᵢ = aᵢE₁₄} ≅ P³ ⊂ P⁷⁹`, the claim is
`q(Γ|_Y) = P(D5)`. The engine is an arc: `w = (−1,0,0,1)`,
`g(t) = diag(t⁻¹,1,1,t)`, `Aᵢ(t) = t²·g(t)Cᵢg(t)⁻¹`, `A₅(t) = t²I`.

I checked both halves:

- **The exponent matrix `2 + w_row − w_col` reproduces exactly** —
  `[2,1,1,0] / [3,2,2,1] / [3,2,2,1] / [4,3,3,2]`. Every entry is `≥ 0`, so this
  is a *polynomial* arc, and the minimum `0` occurs **uniquely at entry (1,4)**,
  which is precisely what makes the limit `Nᵢ(0) = Cᵢ(1,4)·E₁₄` a nonzero
  rank-one pencil with `A₅(0) = 0`.
- **The identity holds**: `det(v A₅(t) + Σ sᵢAᵢ(t)) = t⁸ det(vI + Σ sᵢCᵢ)`,
  confirmed on sixteen random rational `(C, s, v, t)` cases exactly. It is
  immediate once seen — conjugation preserves the determinant and `det(t²M) =
  t⁸ det M` for `4×4` — which is the mark of the right construction.

So the projective target is **constant along the whole arc** while the source
degenerates into `Y`. The graph over `Y` is closed in `P⁷⁹ × P⁶⁹`, its projection
is closed, it contains a dense subset of `P(D5)` and is contained in it, so they
are equal.

**The consequence is the useful negative**: removing the affine zero pencil does
not make the remaining exceptional-image bounds independently easier, because a
*nonzero* rank-one support carries the identical problem. And the sharper point:
these arcs are changes of basis with constant target and first nonzero
determinant order **eight**, despite nonzero rank-one source limits — so **the
exceptional image of a parameter-space blowup must not be identified with the
target's closure-minus-actual-image boundary.** That retires the wording of that
identification in `docs/critic_rees_response.md`, and the session says so rather
than leaving it to be discovered.

The scope is honest too: *"This is not a claim that `Y` itself is a base
component, or that this component is an entire exceptional divisor."*

---

## 4. The subtlest thing in the report

§5 proves the simultaneously-triangularizable **family** image is closed with
fixed-factor chart dimension exactly **12**, by a clean finite-map argument: each
of the 16 diagonal coefficients is a root of the monic characteristic polynomial
of its `Bᵢ`, whose four coefficients are among the image coordinates, so the
map `A¹⁶ → A⁶⁹` is integral, hence finite, hence closed with dimension preserved;
`Π L_a(s) = 0` in a domain forces one whole `L_a = 0`, whose preimage is four
12-dimensional linear spaces.

Then it immediately notes what that does **not** give: *"`Y` in section 4 is
itself strictly triangular, but transverse arcs over it carry the whole
determinant closure."* — and `E₁₄` is indeed strictly upper triangular.

**So a family-image theorem and a graph-image theorem about the same support say
opposite-looking things, and the session explains exactly why they are
compatible: the family image is not the graph image.** That is precisely the
distinction s78 collapsed, it is stated as applying equally to s78's retained
28-dimensional common-kernel result, and it is the most valuable paragraph here.

---

## 5. The reduction that makes the job decidable

`W ⊆ D5 ⟺ J_W = (0)`, where `J_W` is the contraction `K = L ∩ A` restricted by
`y_bad = 0`. **No radical computation is needed for a zero-versus-nonzero
decision**, because a nonzero rational polynomial cannot vanish identically on
`A³⁴` over `ℂ`. 133 variables, 69 generators, 7,957 terms, maximal degree four —
and a built-in output control: `B = 0` gives the known point `v⁴`, so a unit
ideal would contradict it.

The certificate shape is specified precisely, and it is a real reduction of the
work: one explicit `F(y)` with `F(p(B)) = 0` as an exact rational identity and
`F(y_good, 0)` nonzero with a displayed coefficient **suffices without finishing
a Gröbner basis**. With the warning attached: *"Vanishing only on `G(S)` does not
suffice"* — the same error, guarded against in advance.

The compactification section gets the ordering right for the same reason as §2:
saturate the graph first, impose `y_bad = 0` or `z = 0` afterwards. On `z = 0`
all 69 `pᵢ(N) = 0`, i.e. every member of the pencil is nilpotent — **necessary
support equations, explicitly not a substitute for the saturated graph's scheme
structure.**

---

## 6. What it refuses to claim

Worth quoting, because the restraint is uniform:

- *"Global `R5` versus `D5` containment remains open."*
- *"The global elimination is supplied as an exact, uncompleted handoff, not a
  claimed theorem."*
- *"The Singular files are generated mathematical inputs, **not executed CAS
  scripts**."*
- *"**No missing import is interpreted as a mathematical result.**"* — the right
  response to a blocked toolchain, and the sentence I would put in the preamble.
- The S2 replay is labelled *"a replay of that instrument, not a newly
  independent proof of every S2 theorem."*
- LMR is carried forward unchanged: det 273, padded floor 269, `D = 1 −
  i_pad(24) ∈ [−4,+1]`, the `−4` not certified, `i_pad(24) = i_pad(23)` not
  promoted.

---

## 7. Two things for me

**A second staged-artefact gap.** `results/astra/S2/tangent_calibration.json` was
absent from the checkout; the session regenerated it by running S2's own
verifier and recorded the absence in `input_manifest.json`. **That is the second
time my staging has been caught short** — S3's degree-13 conversion was the
first. Two independent misses argue for a systematic pass: for every
`results/astra/S*/` report, check that every artefact it references is actually
in the tree.

**Sixth Astra session, sixth WinError 10013.** The split closes at **nine for
nine**: six Astra sessions blocked from installing exact-LA libraries, three
Claude-side sessions installing them without trouble. Not one Astra session
downgraded an exact computation to sampling because of it.

**Board defects**: the board names S2, the reviewed s78 and the batch-11
formulation as *collections* rather than exact filenames, so the session had to
resolve them by repository search and documents the resolution. And `main` is
absent from the prepared checkout — the same friction B13-06 and B13-11 reported,
now three times.

---

## 8. Actions

1. **Merge-ready** — no trailer surgery, no shared-code edits, nothing outside
   its namespace.
2. **Retire the exceptional-image wording in `docs/critic_rees_response.md`.**
   §4 shows the identification of a blowup's exceptional image with the target's
   closure-minus-actual-image boundary is wrong, with an explicit arc of
   determinant order eight over a nonzero rank-one limit.
3. **Correct `docs/s78_report.md`'s claimed equivalence** to the containment
   direction that actually holds, keeping its 149→98 reduction for the restricted
   problem.
4. **Record the family-image versus graph-image distinction** where s78's
   28-dimensional common-kernel result is quoted — it has the same limitation.
5. **Sweep every `results/astra/S*/` report for referenced-but-unstaged
   artefacts.** Two misses found by two sessions is a pattern.
6. **Fix the board's input naming** — name files, not collections — and make the
   preamble's clone check tolerate a frozen checkout with no `main` (third
   session to hit it).
7. If the global job is ever funded: one bounded 600 s pilot on
   `full_monic_Q.sing`, contraction **before** restriction, preserving the input
   and partial basis, with the `B = 0 → v⁴` control applied to any output.
8. On the deferred verification pass: re-run the 69 coefficient comparisons and
   the 70 triangular identities independently, and check the `t⁸` order claim
   symbolically rather than at sampled `t`.
