# PAPER2_GAPS — what Paper 2 needs that the record does not have, and errors found in the record

Slot B24-06, 2026-09-19/20. Assessment only; `paper/det4-onset.tex` unchanged.
HEAD `82633a60893236fab4fbc317df416e1b8a349005`, `git status --porcelain` empty.

Two kinds of entry, kept apart:

- **G-P2-nn** — a gap: the paper needs something the record does not carry, or carries only
  under a condition the paper would have to state.
- **E-nn** — an error or drift **in a committed packet**. Per G26 these go here and **not** into
  the paper's prose; they are for the record's own keeper, not for the draft.

---

## Part I — gaps (what the paper needs and the record lacks)

### G-P2-01 — the `r = 4` onset `e` is adopted, not certified, and Theorem 9.1 needs it

Theorem 9.1 (blocker B2) is true only below `e = onset I(D_4^{det_4})`. The record has
`e >= 10` **certified** (s33) and `e = 320112` **adopted** from LLV, never independently
confirmed: `docs/e4_hunt.md` L149, "**Adopted, not certified**: `e = 320112`. Two external
corroborations on the same source"; `docs/equation_census.md` L479 says the second corroboration
"is **not** an independent confirmation". So the paper can state Theorem 9.1 unconditionally
only for `δ <= 9`, and for `10 <= δ < 320112` it inherits an adopted literature value.
**Cost to close:** nothing computational is in reach — 320112 is far past any degree this
programme can touch. It stays ADOPTED, and the paper must say so.

### G-P2-02 — LMR's module statements are unverified at source

The three uses in §9 that are not Theorem 1.0.1 (blocker B5). Nothing on the record reads LMR
beyond `dcbar(perm_m) >= m²/2`. **Cost to close:** one literature read of a 16-page paper,
already a named blocker for Paper 1 (B23-05 blocker 5), so one read clears both.

### G-P2-03 — Beauville is unread, and is the likeliest place prior art is being re-proved

Blocker B6(a). Beauville, *Determinantal hypersurfaces*, Michigan Math. J. 48 (2000), has no
read-status anywhere on the record — it is absent from Paper 3's `BIB.md` entirely, in a
document whose whole purpose is read-status. Prop. 2.1, Thm 7.1 Step 2 and Thm 7.3 are in its
subject. **Cost to close:** one full read, labelled at the point of use per G14′.

### G-P2-04 — the boundary of `D45 ∩ P5` (B23-03's G-A1) is genuinely open

Remark 6.3's residual caveat, correctly located. A point of `D45 ∩ P5` outside `T1 ∪ T2` would
have to be a limit of determinants that is itself no determinant; nothing excludes such points,
and by the affine dimension inequality in `C^70` any component they form has dimension
`>= 50 + 39 − 70 = 19` aff (`B23-03/docs/b23_03_report.md` §2.6, @ `3bcad666`). B23-10's ruling:
"**G-A1 (the boundary) — genuinely open**". **Reopening condition, quoted:** a proof that
`D45°` is closed, or a description of the boundary meeting `P5`. B23-03: "No such statement is
on the record, and I have not attempted one." The B24-12 ledger §9 puts G-A1 in Batch 25.

### G-P2-05 — `N = 5` in the rank-threshold row still leans on Kleiman

The paper does not state the rank-threshold row, but a repair pass that imports B23-03 Thm 3.2
will meet this. Row 1 is a PROVED-kill at `N = 6, 7, 8` by B23-03 Thm 3.2 (elementary padding
ceiling, certified modular floors, monomial-Jacobian Hilbert functions, Newton certificate — no
Kleiman, Dimca, GN or depth sensitivity). **At `N = 5` it is by GKZ Theorem B on the record, and
B23-10 records that it "still leans on Kleiman for `k >= 7`", with the note that "one cheap
pilot would remove that".** So "PROVED-kill across `N = 5..8`" is true with an asterisk at
`N = 5`, and the asterisk must travel with it.

### G-P2-06 — the paper has no provenance apparatus

Paper 3 prints a label, a source, a commit and a lineage for every claim (`\prov{}` +
`BIB.md` by read-status). Paper 2 prints none, which is why every blocker in this slot had to
be found by hand. **Cost:** the apparatus exists and is one branch away; adopting it is a
mechanical pass over 24 numbered results plus the abstract.

### G-P2-07 — `mult_det = 5` at the `n = 3` control has no source-side lower bound of its own

§9's `Δ = +1` control needs `mult_det = 5` **exactly**. The paper's argument is: the measured
rank gives `>= 5`, and LMR gives `i_det >= 1`, hence `<= 5`. The upper half is G-P2-02 again.
The permanent half is clean and the paper says why (`rank_p <= rank_Q <= a` forces equality; no
finite-point caveat in that direction) — `docs/PROVED.md` `rank_floor`. The certificates on the
record for this cell are labelled **RECORDED** (`docs/artifacts.md` L92), the weakest of the
certificate labels, and the paper does not say so.

### G-P2-08 — no record statement supports "no obstruction below degree eight"

§9's map says "degree `>= 8`". What the record supports is the *determinant-side* reading:
`I(D_5^{det_4})` is empty through degree seven and on every **measured** cell at degree eight
(`docs/det_onset.md` §0.2 — "δ=8 is excluded only on the measured corner (27 of 435 cells), so
the onset could still be 8 on an unreached cell"). It does **not** support the reading that no
obstruction exists below degree eight: `Δ > 0` requires `i_det >= 1`, which is why the
determinant-side emptiness is the right lever, and that lever is MEASURED, not PROVED. The paper
calls the map "a proof".

### G-P2-09 — the `n = 5` anomaly's component claim carries a condition the paper drops

`docs/onset_conjecture.md` §0: `D_5^{det_n}` is a component of the `ν(n)`-nodal locus "at every
`n` **where the minor ideal is saturated in degree `n`** (measured at `n = 3..7`)", and §6 lists
"saturation of `J` in degree `n` (and hence §4(iii)) for `n >= 8`" under **Expectation**. §7.1
states the component claim without it.

### G-P2-10 — Thm 7.3's component half is unproved in the paper

`docs/onset_conjecture.md` §5 proves `W = P(D_5^{det_3})` and then gets the component claim from
§4(iii) at `n = 3` (`def_3(N) = 0`; the incidence variety is smooth at the determinantal point,
tangent space of dimension 28). The paper's sketch stops before that. Also unstated: whether the
six-nodal closure has **other** components with nodes in special position is "not decided here
and is not needed" (record's words).

### G-P2-11 — `n_χ` has no formula, and §8 needs one

Blocker B12(1). The record's position is that `n_χ` must be **computed**, by the signed Burnside
count `n_χ = |G_λ|^{-1} Σ_g ε(g) Fix(g)` with `ε(g) = Π sign(g_b)^b`
(`docs/PROVED.md` `quartic_signed_burnside_size`, PROVED + CERTIFIED, B14-11), and that
`N_S/|Stab|` bounds it in neither direction. §8 needs either the Burnside statement or no
estimate at all.

### G-P2-12 — the `682` six-row cells were reported before they were verified

`docs/s79_review.md` L132: "Part 2's 682 six-row cells, all three ideals empty | **reported**,
not verified — bundle incomplete". They were later corroborated — B13-07 L186, "all 682
determinant-full records agree with the board" — and B13-11 L67 fixes their label:
"**682 cells remain MEASURED**, regardless of old `exact`, `i_red`, or status". The paper cites
the count twice (§1, Q 10.2) without the label.

### G-P2-13 — "Data availability" points at a repository that does not carry this work

§ Data availability promises "All code, inputs, exact outputs and the full commit history …
at `https://github.com/swsethuraman/gct`". Two things the paper would have to be sure of before
submission: that the URL resolves publicly (not checked here — no network use in this slot), and
that the artefacts it names are actually **committed**. Several results Paper 2 leans on are
not: B23-03, B23-06, B23-10, B23-12 and B15-01 are uncommitted or on sibling branches
(§ "Reachability of sources" in `PAPER2_CLAIMS.md`), and Batch 17's own closeout records that
"research artifacts are filesystem deliveries, not new commits"
(`docs/batch17/STOCKTAKE.md` @ `82633a60`).

### G-P2-14 — no environment check on `\cite{Beau}`'s actual content

The paper attributes to Beauville the statement "cubics in five variables are not generally
`3×3` determinantal". The record **measures** that (Jacobian rank 29 of 35,
`docs/l5_containment.md` §3) and does not source it. Whether Beauville states it is unverified.
Folded into G-P2-03.

### G-P2-15 — Corollary C of the (★) theorem is not in the paper

`docs/reducible_ideal.md` §0 Corollary C: every `SL_r`-invariant of `r`-ary `n`-ics vanishes on
`X^{(k)}` as soon as `n < kr`. It is what makes `I_5` and `I_6` ideal members **by proof** rather
than by measurement (§4 Proposition, items 1–2), and §5 of the paper asserts the `I_5` fact
without it. Not a gap in the record — a gap in the paper's own chain.

### G-P2-16 — the 2026-09-17 stocktake could not be found

The document this slot was sent to check against is not on disk. Searched: the whole tree at
`82633a60` (`docs/`, `README.md`, `PROJECT_NOTES.md`), every sibling worktree's `docs/`, and
`work/` for the phrase "second author" and for stocktake files. What exists is
`docs/batch16/STOCKTAKE.md`, `docs/batch17/STOCKTAKE.md`, `docs/stocktake_batch9..13.md` and
`docs/post_b19_20260917/ARCHIVE_NOTE.md` — none of which describes Paper 2. The six candidate
defects were therefore checked **against the source**, not against the stocktake, and the
results are in `PAPER2_BLOCKERS.md` §0. **If the stocktake exists elsewhere, this slot has not
seen it and cannot say whether it contains further items.**

### G-P2-17 — the paper has never been compiled by anyone on the record

No LaTeX toolchain is installed in this environment, and B23-05 recorded the same for Paper 1.
No commit message or review on the record claims a successful compile of `det4-onset.tex`. The
mechanical checks (balance, labels, references, bibliography keys, theorem numbering) all pass;
a compile has not been attempted.

---

## Part II — errors and drift found in committed packets

Recorded here per G26. **None of these is a defect of the paper**, and none should be written
into the paper's prose as if it were the paper's finding.

### E-01 — `docs/equation_census.md` calls the determinantal quartic surfaces irreducible

L372–374: "determine that the determinantal quartic surfaces form an **irreducible divisor** of
degree **320112** in the `P^34` of quartic surfaces." The primary text says otherwise. B20-10
§4.3 read `llv_v3.txt` (extraction of the PDF hashed `67b1701f…`) and quotes verbatim:
"**Theorem 2. The family of determinantal quartic surfaces consists of 5 prime divisors
F1, …, F5**", with `deg(F1) = 320112`, `deg(F2) = 136512`, `deg(F3) = 38475`, … `deg(F5) = 2508`,
and `D44 = F1`. The **number** 320112 is confirmed and is the right one for `D_4^{det_4}`
(irreducible as the image of an irreducible variety, hence one component); the word
"irreducible" applied to *the family* is wrong. `docs/e4_hunt.md` L40 is careful — "this is
`D_4`" — and `docs/det_onset.md` L62 ("principal of degree `e = 320112`") is fine.
**Severity:** wording in one census row; nothing computed depends on it. The governing reading
is B20-10 §4.3 (uncommitted, `B15-10/docs/b20_10_review.md`).

### E-02 — the brief's `Sigma_Pi` dimensions are T2's

The brief for this slot says "`D45 ∩ P5` … B23-03 §2.4: `T1` 33 affine / 32 projective, `Σ_Π` 35
affine / 34 projective". B23-03 §2.4 says `T1` **33 aff / 32 proj** ✓ and `Sigma_Pi`
**31 aff / 30 proj**; **35 aff / 34 proj is `T2` = `{l·C : C ∈ Sigma_Pi}`**, not `Sigma_Pi`.
B23-10 §6.1's C35 row reads it correctly ("plane family … exactly 35 aff / 34 proj;
`Sigma_Pi` 31 aff / 30 proj"). This is a brief error, not a packet error, and is logged because
a repair slot working from the brief would import the wrong number — the exact failure mode
B23-05 hit on Paper 1.

### E-03 — the brief's "since Batch 14" is one batch generous

`paper/det4-onset.tex` was last touched at `a1bf7c00`, 2026-09-09, **434 commits** behind HEAD,
and the next commit after it is `3d978222` ("Batch 13 consolidated"). The draft therefore
predates the **dispatch of Batch 13**. Eleven batches of record have landed since, not nine.

### E-04 — `docs/PROVED.md` `lmr_ranks` and `lmr_D_upper` state two different intervals

`lmr_ranks` ends "`D = 1 − i_pad(24) ∈ [−4, +1]`" (CERTIFIED / ADOPTED, s74); two rows later
`lmr_D_upper` gives `D_LMR ∈ [−4, −2]` (CERTIFIED, batch 14). Both rows are correct at their own
date and the second governs, but the index reads as if the first were current — which is
plausibly how the paper's `[−4, +1]` survived. `docs/batch15/ACCEPTED_STATE.md` carries only
`[−4, −2]`, correctly. **Severity:** a superseded row not marked as superseded, in the file whose
preamble says "Read this before writing a brief and before starting work."

### E-05 — a chain of three intervals, only two of them committed

`[−4, +1]` (s74, `lmr_ranks`) → `[−4, −2]` (batch 14, `lmr_D_upper`, committed) → `[−4, −3]`
(`B15-01/docs/b15_01_report.md`, **uncommitted**, "with the banked premises and injective
multiplication by `u^10`"), with `D = −4` measured and never promoted
(`lmr_D_measured`: "a five-dimensional sampled kernel at 282 points bounds `i_pad <= 5` and
proves **nothing** downward"). A reader of the committed tree alone gets `[−4, −2]`. Recorded so
that a Batch 25 repair does not reach past what is committed.

### E-06 — B23-03 is not an ancestor of HEAD, and three of its consumers are uncommitted

`git merge-base --is-ancestor 3bcad666 HEAD` fails. Paper 3 (`ce43cdb7`) is likewise a sibling.
B23-06, B23-10 and B23-12 exist only as files in worktrees B15-02, B15-10 and B15-12. B23-10's
own hash (`8bbc8d9eaee69620…`) is bound by the B23-12 ledger §2.0b, so the chain is internally
consistent — but **none of it is reachable from the paper's own branch**, and Paper 2's
"Data availability" section promises otherwise (G-P2-13).

### E-07 — `docs/s79_review.md` marks the 682 cells "reported, not verified"

Recorded under G-P2-12. Not a defect now — B13-07 corroborated them and B13-11 set the label to
MEASURED — but the review row itself was never amended, so the file still reads as an open
verification failure.

---

## Part III — B25-02 updates (2026-09-22, UNCOMMITTED, producer-only)

Parts I–II above are unchanged. Status of the gaps after the B25-02 repair pass:

- G-P2-01 — unchanged: e = 320112 ADOPTED; LLV now read PRIMARY by B25-02 (Thm 2, Table 2, Cor. 4.1).
- G-P2-02 — closed for the paper's four uses (LMR PRIMARY); (★) remains (B25-05).
- G-P2-03, G-P2-14 — closed: Beauville v2 read PRIMARY; it states (1.9) and Cor. 6.4, both now cited; it does not contain Prop. 2.1, Thm 7.1 Step 2 or Thm 7.3.
- G-P2-04 — open (G-A1); the paper now says so and no longer calls Thm 6.2 unconditional.
- G-P2-06 — partly: a read-status paragraph added to §1 and labels at points of use; no `\prov` apparatus.
- G-P2-07 — superseded: C45 is PROVED modulo (★) (B24-10 §3.2); the paper says so.
- G-P2-08, G-P2-09, G-P2-10, G-P2-11, G-P2-12 — addressed in the TeX.
- G-P2-13 — open. G-P2-15 — not addressed (Cor. C not added). G-P2-16 — unchanged.
- G-P2-17 — still open: no toolchain on the B25-02 host either; mechanical checks pass.
- **G-P2-18 (new)** — Thm 6.2's closure statement is carried as ADOPTED from B17-01 (`01c49022`, B15-01), whose scope B23-03 §4 reads more narrowly than B17-01 states; needs review before the paper relies on it.
- **G-P2-19 (new)** — the n = 4 LMR transfer 16 → 9 is flagged in the paper as the analogue of (★); B25-05 should say whether (★) covers it.
- **E-08 (new, record)** — Paper 2's "Prop. C" of the companion does not exist in Paper 1 @ `bc7e62b7` (length reduction is Prop. 4.19 by source order).
