# Batch-11 housekeeping — what was done

Run at the batch-11/12 boundary, with batch 12 specified in
`docs/batch12_plan.md`.

---

## 0. Not done, and it blocks batch 12

**The push.**  `origin/main` is at `226b4ef1`; local `main` is **65 commits
ahead**.  This is the third time it has been the top item and the first time it
has a measured cost:

- **s73** rebuilt the `n ∈ {3,4}` verifier extension that was already banked, and
  wrote a **second dialect of `sparse_nullity`**, because neither existed in its
  clone.
- **s71** could not find session 67's bundle and **re-implemented its widened
  monomial code and its initial-term certifier from the report**, and says the
  two implementations have never been compared.
- **s72** ran without the plan or the preamble.
- s73 also re-derived `i_per(12) = 0` on independent seeds — the one place the
  accident paid, and it is now a third confirmation of `mult_per = 6`.

Batch 12 does not go out until `git ls-remote origin refs/heads/main` returns the
commit containing `docs/batch12_plan.md`.  The preamble check is being changed to
key on the tree rather than on whether the worker feels blocked, and the
integrator now verifies the push before briefs go out (batch-12 plan §6).

---

## 1. All six batch-11 branches merged

s68, s69, s70, s71, s72, s73.  Two conflicts, both real:

**`.gitignore`** — trivial, both sides kept.  s71's addition of
`results/logs/*.pid` is adopted: the standing rule is to *record* a pid so a run
can be ended by id, not to commit it.

**`tools/verify`** — the substantial one, four files.  Session 73 branched from
`226b4ef1`, which predates the merge of session 67's format work, so its verifier
is a parallel evolution missing the declared field, `matrix_role`, `parse_field`,
`layer3` and the batch-10 relabelling of the 44 Gram certificates.  **Taking it
wholesale would have silently reverted all of that.**  The mainline verifier is
kept and only what the new sessions need is added.

---

## 2. The verifier, reconciled

**The unpadded family is `permanent_pencil`, appended.**  Session 73's naming and
ordering win, and the ordering matters more than the name: `FAMILIES` fixes the
fresh-point seed offsets (`seed + 1000·index`), so **inserting** the family in
the middle — as my first version did — shifts the offsets of `padded_permanent`,
`reducible` and `generic`, and a certificate's "fresh points of family X" would
then be drawn from a different stream than when it was written.  My regression
missed it because every certificate it touched used `det_pencil`, which is index
0 either way.  **Session 73 caught a latent defect of mine.**  My two
certificates were renamed.

**Both `sparse_nullity` dialects are accepted**, with no check weakened —
finite field, nonnegative nullity, substitution-data points and the
exhibit-your-kernel rule all still apply, each read off whichever dialect the
certificate uses, and every sub-key check either dialect imposes is imposed when
that key is present.  One deliberate **narrowing**: a certificate with
`variety: "none"` claims `nullity_p(E) = a`, and the verifier recomputes `a`
independently from the plethysm — a stronger check than exhibiting the vectors.
Session 73's four full-`E` records are of that shape.

**Two unreadable kinds registered.**  `split_rank` (s70) and `hybrid_kernel`
(s71) both declared `gct-cert/1` and neither could be parsed by any verifier —
both sessions said so.  Both are now registered as recipe-style kinds reporting
**`RECORDED`, not `PASS`**: cell, field and the internal consistency of every
claim are checked, and the ranks are not re-derived, because each needs the
cell's build.

**One of my own checks was wrong and fired on a correct certificate.**  I
asserted `n_χ·|Stab| ≥ N_S`.  It does not hold: the build *drops* `χ`-orbits
whose twisted sum vanishes identically, so `n_χ` can and does fall below
`N_S/|Stab|`.  Replaced by `n_χ ≤ N_S`, with the reason recorded in the code and
in `FORMAT.md`.

**Corpus status: 1 082 certificates, six kinds, all schema-valid; self-test
passes.**

---

## 3. The single-writer files

**`paper/det4-onset.tex`** — the `r = 5` status remark went from *four unbounded
loci* to *four numbers*, with s72's exact interior bound added: the interior
reparametrises through the `r = 4` base locus, so its dimension is a generic
Jacobian rank over irreducible families and therefore an **exact upper** bound,
`31 < 35`.  What is still not proved — completeness of the enumeration — is
stated as such.  The file compiles.

**`PROJECT_NOTES.md`** — the thread-2 status opens on a bottleneck that is gone,
with both small realisations and their measured sizes, the `D = +1` recorded as a
theorem, and a rewritten open list.  The roadmap carries batch 12 and leads with
the push.

**`docs/artifacts.md`** — the batch-11 corpus and what the merge reconciled.

---

## 4. Still outstanding

- **The push** (§0).
- **Unification, not validity.**  Two `sparse_nullity` dialects still coexist;
  `split_rank` and `hybrid_kernel` are recorded rather than re-derived; s67's and
  s71's certifiers have never been compared.  All three are session 78's
  (batch-12 plan, C5).
- **Batch 10's Sol memos** are still uncommitted; batch 11's report is committed
  (`docs/sol/sol_batch11_report.md`).  Fixable only if the memos still exist.
- **Sessions 63, 64 and 66 shipped no certificates** — recorded in batch 10 and
  unrepairable from here.  Batch 11 has no equivalent gap.
- **`B_δ` at `δ = 14, 16, 18`** was not finished; `B₁₂ = 31` and `B₂₄ = 2 168`
  are measured, and the DAG count is the number that decides the route.
