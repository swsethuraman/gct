# B26-01: independent review of B17-01's general smooth-cubic claim

**REVIEWER ONLY. UNCOMMITTED.** Slot B26-01, Batch 26. Reviewer: Claude (Opus 5.5, 1M context).
This is a **same-lineage independent review**: B17-01 is also a Claude packet. It is not
cross-model replication. Zero pilots and zero mathematical programs were run.

## Verdict first

**Registered outcome 1: ACCEPT, at the whole headline.** For every smooth complex cubic
threefold `C ⊂ P^4` and every nonzero linear form `l`,

    lC ∉ D_{4,5} := closure{ det(x_0 B_0 + ... + x_4 B_4) : B_i ∈ Mat_4(C) }.

The supporting lemma is also accepted as stated: if `0 ≠ F ∈ D_{4,5}` is square-free, then
every irreducible component of `V(F) ⊂ P^4` is ruled.

Scope and qualifications:

- **Achievement level: geometric noncontainment only.** This is not a source condition, a
  coefficient equation, separation on padding, or a positive multiplicity gap. No determinant
  equation is exhibited. The binding constraint still reads exactly: "No five-row
  determinant equation is known to be nonzero on padding."
- **"Modulo classical facts".** The accepted proof depends on the primary statements read
  below, on my hand derivations, and on four textbook facts I did not re-read in this
  session. Those four are listed as UNREAD-CLASSICAL in §4.
- **Three precisions, none of which changes scope** (§3). The main one: B17-01 does not argue
  that the generic point of its test curve inherits the good-open-set properties. I supply
  that argument by hand.
- **Out of scope:** the explicit witness `s_5·C*` and its numerical certificate (claim (a)).
  They were not replayed and not re-reviewed; they keep their existing ADOPTED (narrow)
  status. The density premise `D_pad,5 = R_{1,3,5}` belongs to (a) and is also not reviewed.
- **What this verdict changes** (rule of 2026-09-22): it releases the scheduling gate only.
  A26-02 stays HELD until the user re-scopes it. The verdict does **not** close C1 or G-A1,
  and it does not license any paper to cite the general result. Those wait for the
  non-Claude confirmation in B26-10. B17-01 stays unreviewed on the record until this review
  is delivered and committed.

## 0. State, exposure, timeline

| event | UTC |
|---|---|
| start (brief hashes verified) | 2026-09-22T21:22:45Z |
| preflight complete | 21:22:45Z |
| primary sources read (Kollár–Smith, CTKM, Clemens–Griffiths, LLV) | 21:23–21:26Z |
| first certificate (premise table, §2) complete | 21:27:37Z |
| 45-minute checkpoint | not reached; I finished well before it |
| stop | see `results/b26_01/resource_receipt.json` |
| interruptions | none |

**Preflight.** Worktree `work/batch15_workers/B15-10`, branch `b15-10-portable-witness`, HEAD
`42e7f4ba45e8bd1fda529de9ce116f64e7ac6be1`, equal to the expected value.
`git status --porcelain` shows only the two pre-existing untracked files,
`results/logs/b15_10_runtime_native_20260913.pid` and `..._resources.json`. I left them alone.
Neither output path existed. There is no `AGENTS.md` or `CLAUDE.md` in the worktree.

**Brief bindings (raw working-copy bytes).** `B26_COMMON.md` `4550c48b…578509` and
`B26-01.md` `644e0578…27711` match. `BATCH26_LIVE_LEDGER.md` hashes to `748550d8…d133ac`, as
quoted at dispatch. Ledger line 24 and §"B26-01 authorization and preflight" record this
slot as AUTHORIZED. I did not edit the ledger.

**Remote containment (the brief's open limitation).**
`git -C work/batch15_workers/B15-01 branch -r --contains 01c49022` returns
`origin/b15-01-ci159`. That is a remote-tracking ref only: no fetch was made, so it shows what
was last fetched, not a live remote check.

**Inputs (every hash below names LF committed blob content from `git show`).**

| input | commit | SHA-256 | match |
|---|---|---|---|
| `docs/b17_01_report.md` | `01c49022` | `8812eeef…f6f2c0` | yes |
| `delivery/b17_01/MANIFEST.json` | `01c49022` | `cb971e20…cbcc2f` | yes |
| `docs/b25_10_review.md` | `42e7f4ba` | `0488ce1e90a6…589477e` | yes, against the brief's prefix `0488ce1e…` |
| input binding `B26_B17_01_INPUT_BINDING_20260922.json` (raw working copy) | uncommitted admin file | `2a674ee1…292587` | yes |

I also read B25-06's headline (`c740532b:docs/b25_06_report.md`, lines 1–40) and located
Paper 2's use (`79b68dcf:paper/det4-onset.tex`, lines 530–541: the one-witness
`s_5·C*` reading).

**Prior exposure, disclosed.** In this session I had not seen B17-01 or B25-10 before these
reads. The auto-memory index loaded at session start does not mention B17-01. The dispatch
prompt summarised only the preflight. I read B25-10 §4.3, which reports that the record reads
B17-01 narrowly and that B25-10 "did not audit B17-01". The same model lineage produced
B17-01. Neither B17-01's "PROVED/COMPLETE" label, nor the fact that this is a separate session,
nor model identity was used as evidence.

## 1. What is being reviewed

This review covers claim (b) only: the general geometric proof in B17-01, §"Proved lemma" and
§"Consequence". The argument runs as follows:

1. On a nonempty open set of 5-tuples `(B_i)`, the determinant quartic `X_B` is integral,
   normal and rational, via the incidence `Z_M = {M(x)u = 0}`.
2. Given `0 ≠ F ∈ D_{4,5}`, take the closure `Γ̄` of the graph of the determinant map. It
   surjects onto `P(D_{4,5})` because the projection is proper. Choose a curve through a
   point over `[F]` whose generic point lies over the good open set. Normalize it and localize
   to get a DVR `R` with residue field `C`.
3. `X = V(F_R) ⊂ P^4_R` is integral, S2 and R1, hence normal. For R1 at vertical points,
   square-freeness of `F` is used.
4. Apply Matsusaka's specialization of ruledness in the rational-generic-fibre form: every
   component of `V(F)` is ruled.
5. A smooth cubic threefold is not ruled, by Clemens–Griffiths, unirationality and
   Castelnuovo. Since `lC` is square-free with component `V(C)`, `lC ∉ D_{4,5}`.

**Closures.** The object is the full coefficient closure `D_{4,5}`. Step 2 reaches every
boundary point, including limits with no finite matrix limit, because matrices are needed
only over the fraction field `K`. So the statement is about `closure(image)` itself. It is not
a statement about `closure(B1 ∩ P)` or any intersection-first object. In that respect it is
stronger in scope than B25-06 Theorem 1, which covers only order-one limits in `B1 ∩ P5`.

## 2. First certificate: premise-by-premise table

Labels: **READ** (committed text), **PRIMARY** (source read by me; locator given),
**HAND** (my own derivation in this session), **UNREAD-CLASSICAL** (textbook fact not re-read),
**PROXY** (a quotation extracted by a fetch tool, not byte-read by me).

| # | step | theorem / source used | exact source statement | why hypotheses hold | quantifiers delivered | label |
|---|---|---|---|---|---|---|
| S1 | Generic `X_B` is integral with finite singular locus | Bertini for general linear sections; rank-≤2 locus of `4×4` matrices has codimension 4 | LLV: "A general linear determinantal quartic in ℙ⁴ is nodal, non-ℚ-factorial and rational"; "The generic element … is 20-nodal" | general `P^4 ⊂ P^15` meets a codimension-4 locus in finitely many points and is transverse to `Det` elsewhere. A hypersurface in `P^4` with finite singular locus is irreducible (two components meet in dimension ≥ 2) and normal (R1 + S2) | for a nonempty open set of closed points `B` | HAND + UNREAD-CLASSICAL (Bertini); LLV quote is PROXY and not load-bearing |
| S2 | Generic `X_B` is rational via incidence | B17-01 in-text argument | B17-01: kernel gives a unique `[u]` on the rank-3 locus; for general `u`, `N(u)x=0` is 4 equations in 5 unknowns | HAND check: let `Z'` be the closure of the graph `u ↦ x(u)` (4×4 signed minors of `N(u) = [B_0u…B_4u]`). `Z'` is irreducible of dimension 3 with image in `X`. If the image were finite, `Z'` would lie over finitely many points with kernels of dimension ≤ 1, a contradiction. So `Z'` dominates `X` and meets the rank-3 locus, where the fibre is one point. Char 0 gives birationality | same open set | READ + HAND |
| S3 | **Generic point of the test curve inherits S1–S2** (elided in B17-01) | closedness of the image of a projective morphism; nonvanishing of polynomials is open | — | HAND: the properties are open conditions on `B` in the scheme sense. (P1) `det ≢ 0` and geometrically irreducible: the complement of the image of the multiplication maps `P(Sym^a)×P(Sym^{4−a}) → P(Sym^4)`, `a = 1, 2`, which is closed. (P2) Some 4×4 minor of `N(u)` is `≢ 0` in `u`. (P3) The Jacobian of `u ↦ x(u)` has generic rank 4 (affine). (P4) Some 3×3 minor of `M(x(u))` is `≢ 0` in `u`. An open set containing one closed point of an irreducible curve's image contains that image's generic point `ξ`. At `ξ`, `u ↦ x(u)` is defined over `k(ξ) ⊂ K`, so `X_K` is **rational over K**, not only geometrically | at the generic point `ξ` of the chosen curve | HAND + UNREAD-CLASSICAL (properness ⇒ closed image) |
| S4 | A curve through a point over `[F]` whose generic point lies in the open set | curve-selection lemma in an irreducible variety | — | `Γ̄` is irreducible and the preimage of the good set is dense open in it | for **every** `0 ≠ F ∈ D_{4,5}` | UNREAD-CLASSICAL |
| S5 | DVR `R`: a localization of a finitely generated C-algebra, residue field `C` | normalization of a curve is finite | Kollár–Smith fn. 5: normalization "is finite for schemes … essentially of finite type over Z, or more generally for any excellent scheme" | a curve over C is of finite type | — | PRIMARY + READ |
| S6 | `X = V(F_R)` is integral and flat | Gauss / primitivity | — | HAND: `F_R mod t ≠ 0` and `C[x]` is a domain, so `t` is a nonzerodivisor on `R[x]/(F_R)`. Associated points are horizontal, and `X_K` is integral by S3 | — | READ + HAND |
| S7 | Vertical R1: `X` is regular at the generic point `p` of every component of `V(F)` | char 0; square-free `F` | — | HAND: `O_{X_0,p}` is Artinian and reduced (the factor has exponent 1), hence a field. So `m_p = (t)` with `t` a nonzerodivisor, and `O_{X,p}` is a DVR. This agrees with B17-01's partial-derivative phrasing | every component of `V(F)`, `F` square-free | READ + HAND |
| S8 | Horizontal R1 and S2 ⇒ `X` normal | hypersurface in regular `P^4_R` is CM; `X_K` normal by S1/S3 | — | as B17-01 says. **Not needed**: applying S9 to the normalization `X^ν` (finite by S5) avoids horizontal normality, since `X^ν → X` is an isomorphism at the points of S7 | — | READ + HAND |
| S9 | Special components are ruled | **Kollár–Smith Thm 5.3, weak form Rem. 5.3.1**, printed pp. 34–37 | "Let V be a discrete valuation ring that is a localization of a finitely generated algebra over a field or over the integers. … Let Z_S be a normal irreducible projective scheme over S = Spec V. If the generic fiber … is ruled over K, then each irreducible component of the special fiber is ruled over k." Rem 5.3.1: "we prove here only the following weak form …: If the general fiber above is rational, then the components of the special fiber are ruled." | `V = R` by S5. `Z_S = X` (or `X^ν`) is normal irreducible projective by S6–S8. The generic fibre is rational over `K` by S3, which is exactly the proved weak form. The proof (pp. 36–37) uses only the normalized graph, "isomorphism in codimension one", and Thm 5.4 | every irreducible component of the special fibre, reduced or not | PRIMARY |
| S10 | Exceptional divisors over regular `P^3_R` are ruled | **Kollár–Smith Thm 5.4** (Abhyankar) | "Let Y → X be a proper birational morphism of irreducible schemes, with Y normal and X regular. Then every exceptional divisor … is ruled over its image." Fn. 6: sufficient if X is "of finite type over a localization of a finitely generated algebra over a field or Z" | `X = P^3_R` is regular and of finite type over `R`; `Y` is the normalized graph | — | PRIMARY (statement and the lectures' proof sketch pp. 37–38; Abhyankar's original UNREAD) |
| S11 | "Ruled" means birational to `P^1 × T` | Kollár–Smith **Def. 4.2** | "A variety X is ruled if there exists a variety Y and a birational map Y × P^1 ⇢ X." | matches B17-01's usage ("not merely uniruled") | — | PRIMARY |
| S12 | Smooth cubic threefold irrational | **Clemens–Griffiths Thm 13.12**, Ann. Math. 95 (1972), printed p. 350 | "Let V be a non-singular cubic threefold. Then V is not birationally equivalent to P³." | complex setting throughout the paper | every smooth complex cubic threefold | PRIMARY |
| S13 | Smooth cubic threefold unirational | **Clemens–Griffiths App. B**, pp. 352–353 | "It was evidently known to Max Noether that the cubic threefold is unirational"; Fogarty construction from a line `L_0 ⊂ V`, "f is generically two-to-one" | needs a line on `V`. Every smooth cubic threefold contains lines (Fano surface of lines) | every smooth cubic threefold | PRIMARY (construction) + UNREAD-CLASSICAL (existence of lines) |
| S14 | Castelnuovo | **CTKM Thm 2.3**, arXiv math/0611777v1, p. 3 | "A unirational integral surface X over an algebraically closed field F of characteristic zero is rational" | `T` is a surface over C, dominated by `Y`, which is dominated by `P^3` | — | PRIMARY |
| S15 | Not ruled | hand from S12–S14 | — | if `Y ~ P^1 × T`, then `T` is unirational, hence rational, hence `Y` is rational, contradicting S12 | every smooth cubic threefold | HAND (agrees with B17-01) |
| S16 | `lC` square-free with component `V(C)` | smooth hypersurface in `P^4` is irreducible; `deg C = 3` so `l ∤ C` | — | — | every smooth `C`, every `l ≠ 0` | HAND |
| S17 | Conclusion `lC ∉ D_{4,5}` | S9 + S15 + S16 | — | the component `V(C)` would be ruled | **∀ smooth C, ∀ l ≠ 0** | HAND |

**Load-bearing audit, as the brief asks.**

- **Generic rationality.** Holds over `K`, not merely over `K̄` (S2, S3).
- **Passage to a DVR.** Correct (S4, S5).
- **Normality.** Correct as written. It is also avoidable via `X^ν` (S8).
- **Reduced special fibre.** Used only for vertical R1 (S7). Theorem 5.3 itself needs no
  reducedness.
- **Hypotheses of the specialization theorem.** Exactly met in the proved weak form (S9, S10).
- **Non-ruledness.** Correct (S12–S15).

No load-bearing step is false. No step is UNRESOLVED on account of an inaccessible source.

## 3. Precisions (non-blocking; for the record and any delivery pass)

1. **Elided step (S3).** B17-01 asserts that "on the generic fiber the matrix representation
   and the incidence birational maps are defined over K" and that horizontal normality
   "follows from that of the generic determinant hypersurface". It does not say why a
   non-closed point inherits properties proved for general closed points. §2, S3 supplies
   this with explicit open conditions (P1)–(P4). This is a presentation gap, not a
   mathematical one.
2. **Horizontal normality is dispensable (S8).** Applying Theorem 5.3 to the normalization
   makes the proof depend only on vertical R1 at the component of interest.
3. **Source status.** The lectures prove Theorem 5.3 only in the weak form of Remark 5.3.1.
   That is exactly the form B17-01 uses, and B17-01 says so. Leal–Lozano Huerta–Vite was
   seen only through a fetch-tool extraction (PROXY). It is not load-bearing, because S1–S2
   are established by hand. The "20-nodal" figure matches the degree of the rank-≤2 locus
   and is consistent with S1.

**Not claimed by this review:** anything about non-reduced points of `D_{4,5}`, the rank-≤2
classification (not imported), the boundary classification of B25-06, or any equation,
degree, or multiplicity.

## 4. Source and method ledger

| source | version / locator | how read | bytes |
|---|---|---|---|
| Kollár lectures by K. E. Smith, appendix J. Rosenberg, *Rational and non-rational algebraic varieties* | arXiv alg-geom/9707013v1, 15 Jul 1997; Def. 4.2 (Lecture 4), Thm 5.3, Rem 5.3.1, Thm 5.4, fns 4–6, pp. 34–38 | PRIMARY: fetched PDF, text extracted with `pdftotext -layout`, read by me | raw PDF SHA-256 `583f5d3fb5455c3f0e2be579bf1298b5783e9df30aaad15e4d5de2041ccc054d`, 545,094 B (fetched bytes; not archived in the repository) |
| Clemens–Griffiths, *The intermediate Jacobian of the cubic threefold* | Ann. Math. 95 (1972) 281–356 (JSTOR scan via IAS); Thm 13.12 p. 350, App. B pp. 352–353 | PRIMARY, same method | `6cfe96ecb81179ce2756cb114414d3db1eab46274665c96c582d7f42c7a60a60`, 4,531,144 B |
| Colliot-Thélène–Karpenko–Merkurjev, *Rational surfaces and canonical dimension of PGL6* | arXiv math/0611777v1; Thm 2.3 p. 3 | PRIMARY, same method | `d66b8049edfb5a8e30addd978f9e4aa7e6c4542f931e91ad0789c2a7bface232`, 215,114 B |
| Leal–Lozano Huerta–Vite | arXiv 2504.14461v1 (HTML), Introduction | PROXY (fetch-tool quotations; not byte-read) | not pinned |
| Matsusaka, Nagoya 31 (1968), Appendix §1; Abhyankar [Ab p. 336] | — | UNREAD (original sources; the lectures' statements were used) | — |
| UNREAD-CLASSICAL | Bertini for general linear sections (char 0); closed image of projective morphisms; curve selection in irreducible varieties; lines on smooth cubic threefolds | not re-read | — |
| B17-01 report, B25-10 §§0, 4.3, 7.1, 10, B25-06 lines 1–40, Paper 2 lines 530–541 | commits as in §0 | READ | LF blobs as in §0 |

Method: reading and hand derivation only. Administrative actions: SHA-256 hashing, `git show`,
`git branch -r --contains`, `git status`, `git check-attr`, `git config --get`, PDF-to-text
extraction for reading, and date stamps. **No mathematical program, symbolic test,
certificate replay, or pilot.** No lease was taken.

## 5. Limitations

- Same-lineage review. The brief routes non-Claude confirmation to B26-10.
- The PDFs were read as `pdftotext` extractions, which garble some symbols. Every quoted
  statement was checked against its surrounding text for sense. The fetched bytes are hashed
  above but not archived in the repository.
- Four textbook facts are UNREAD-CLASSICAL (§4). If a stricter standard is imposed, the
  verdict reads "ACCEPT modulo those four".
- Line endings: the payloads are written with LF. `core.autocrlf=true` holds in this
  worktree, and no `.gitattributes` rule covers `docs/b26_01*` or `results/b26_01/`. The
  manifest hashes name the **raw working-copy bytes as written**. A delivery pass should
  re-hash after staging or add a `-text` rule.

## 6. Resource receipt

Zero pilots, zero mathematical programs, zero subagents, zero commits, fetches or pushes.
There were no paper, ledger or sealed-file edits. Writes: this file and `results/b26_01/`
only. Clock times are in `results/b26_01/resource_receipt.json`.
