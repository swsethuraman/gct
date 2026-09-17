# B20-10 — Independent adversarial review of the B19 and post-B19 record, and release gates for Phase 2

Slot 10, Batch 20, Phase 1 (run alone). Claude Code (Fable 5.1), 17 September 2026.
Worktree `work/batch15_workers/B15-10`, branch `b15-10-portable-witness`.

**Status: COMPLETE.** Closing ledger in §12; decisions are transcribed from §12 only.

## 0. Provenance, and what "independent" means in this document

Recorded before any write (read-only git only: `rev-parse`, `status --porcelain`, `log`, `show`, `ls-tree`, `grep`, `cat-file`; no commit, push, fetch, checkout, stash or history operation):

```
git rev-parse HEAD          5764e7ffc03439b7f34b912ff9ff984554c0884e
git rev-parse HEAD^{tree}   6d80f069ba4858389a5388e4584cf514c9a6ba71
git status --porcelain      ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
recorded at                 2026-09-17T18:20:37Z
```

Zero tracked changes, zero staged; the two untracked files are B15-era run residue, pre-existing. HEAD and tree equal the values in the brief and in `COMMIT_RECEIPTS.json`.

Every verdict below carries one of three method labels, as the brief requires:

- **INDEPENDENT EVALUATOR** — a value recomputed here by code that imports no project code and re-derives the object from its definition (pilot 1, §3.3).
- **REPLAY** — saved integers re-run through the stated arithmetic (pilot 2, §3.4; the hash checks of §2).
- **READ** — a proof or certificate read and judged; no arithmetic performed.

Verdicts formed **before** reading the deliverable's own defence are marked **[pre-formed]**; the pre-verdict text is preserved byte-for-byte in `results/b20_10/preverdicts_formed_before_reading.md` (written 18:22:21Z and 18:33:54Z, before `b19_01_report.md` §6 and before any packet governing document was opened). Items so formed: the Levi commutation argument (P2), the 10,505 count (P1), the singular-locus Theorem 4.1 (P3), the status a chat-only input can confer (P4), and refined Bézout (P5). Everything else was formed while reading.

Three subagents were used for **extraction only** (verbatim quotes with file and line, hashes of files on disk): one traced literature citations across the archive, one inventoried uncommitted inputs on disk, one extracted every scope-sensitive sentence in the archive under six headings (rank direction, padding model, source membership, global versus sampled, exhaustiveness, the `D = -1` wording). Their outputs are not verdicts; every quote I rely on in §4 and §7 I re-read myself in the committed text, and the judgements are mine. The scope extraction (647 lines) is preserved as `results/b20_10/extractions/scope_extraction.md`; the on-disk sweep as `results/b20_10/extractions/d5_sweep.txt`.

Committed bytes, not the working tree, were reviewed throughout: every document cited below was read from `git show <commit>:<path>` into a scratch copy, and the hash of each was checked against `COMMIT_RECEIPTS.json` (§2).

## 1. Plain terms

The record survives. Every claim I could test independently held; every claim I could replay replayed; and the corrigendum discipline of the post-B19 body is as good as the housekeeping says. What I found are four things the integrator lineage got wrong or left inconsistent, none of which changes a theorem:

1. **The claim ledger contradicts itself on the three transverse functionals.** `L24` says their joint rank on `M` is "NOT ESTABLISHED (2 or 3)"; `L21` says `rank T = 3` is PROVED. They are the same statement about the same three rows. The routeA packet's certificate `transverse_triple_rank3.json` is a nonzero `3x3` modular minor on three certified source vectors, which I replayed (det `225843`). **The three rows are jointly independent on `M`.** `L24` and the two "record corrections" that repeat it (PRE_AUDIT §4D, §7.5; `POST_B19_STOCKTAKE` §5, §9) are wrong and must not be carried into the board.
2. **D5 is overstated.** Of the six "chat-only" values, five are recomputed and stored in committed pilot outputs (`-12`: `p9_sixrow_replay.json`; `108`, `-14`, `3/896`: `c2_fivevar_order4.json`; `175/36`: `p3_c2_derivation.py` from the stored `322560`). Only `Ω det Q = 315/4` has no artifact, and it feeds an `a = 0` control that nothing consumes. The weakest reproducibility link is not where the housekeeping put it.
3. **`(4^5)` at `d = 5` is `D = -1` with two lineages now**, not one: my independent evaluator (no project code, the four-epsilon contraction realising the unique degree-five `SL5`-invariant) is nonzero at all three recorded determinant points with the same constant ratio `192` to the recorded values, and zero at all three recorded padding points; `m_pad = 0` I re-derived from the null cone. The B19-05 intake row is corrected in §10.
4. **The Levi commutation argument is proved, but B19-01's proof of the displayed expansion cites the wrong torus.** Theorem 6.2 restricts the `L`-invariant sum to `|mu| = d` by Proposition 3.1, which needs the diagonal tori of `SL(A) x SL(B)`; `L` does not contain them. The restriction holds anyway, by the scalar subtorus of `L` (two lines, §3.1), and the later `arc_target` packet §3.2 already supplies exactly that argument. Conclusion unchanged; the proof as written in B19-01 is incomplete.

The dependency chain is thinner than the record implies in one place and thicker in another. Thinner: Eisenbud–Harris enters the singular-locus closure theorem only through the shape classification in Lemma 3.3; the vanishing mechanism itself is a self-contained one-parameter-subgroup argument, and the theorem is a **route-closing** result — if the classification were wrong a closed route would reopen, no positive claim on the record would fail. Thicker: Bruns–Herzog 1.5.12 is cited inside the proof of Theorem B of the GKZ packet and appears in no literature list or manifest; it is an unlabelled load-bearing pointer. The Ballico 1995 addendum remains unread by anyone; I tried three routes to its text (§4.2) and record the failure.

Release gates for Phase 2 are in §9. The G5 generalisation is **accepted with four conditions**, the `a = 1` exception is stated, and nine further gates are added, each traceable to a defect on this record.

No cell is nominated. No gap is claimed. No producer computation was redone; two wrapped pilots ran, 1.15 s in total, no cap hit, no failure.

## 2. The committed-artifact dependency chain, verified

Script `results/b20_10/verify_layers.py`, output `results/b20_10/verify_layers_out.json` (REPLAY of hashes against git objects; 16 s).

**Batch 20 label.** `git log --all --oneline | grep -i -E 'b20|batch ?20'` returns three commits whose *hashes* contain the substring `b20` (`7bb7b20c`, `cb205601`, `b20b0603`) and nothing else; no ref, tag or subject carries the label. `for-each-ref` lists 54 refs (36 in `STATE_CAPTURE.json` plus the 18 remote-tracking refs the PART 7 fetch added, as `PUSH_REPORT.md` says). One untracked file carries the label: `B15-12/docs/b20_12_ledger.md`, the live Batch 20 ledger, untracked by instruction. **Label free; check closed.**

**Layer 0 — the nine commits.** All nine exist; for each, parent, tree and subject equal the receipt and the branch tip equals the commit. Per-path committed sha256: `244/244` archive paths at `82633a60` and `137/137` worker paths (`11 + 39 + 6 + 1 + 1 + 72 + 7`) equal `committed_sha256`. The archive receipt lists 246 staged paths but hashes 244; the two unhashed are the session-generated `RELOCATION_MAP.json` and `ARCHIVE_NOTE.md`, present in the tree (archive file count 246). Local tips of the five untouched branches equal the receipt. `housekeeping/batch14-close`, `integration/batch13`, `batch15-base`, `batch14-base` unchanged. `origin/*` differ from `refs_unchanged_by_this_session` **because of the later PART 7 push**: every `origin/<branch>` now equals the local tip and `origin/main` is `2816cdc7`, exactly as `PUSH_REPORT.md` records; the receipt's values are the pre-push state and are superseded by `PUSH_RECEIPTS.json`. **Layer 0 PASSES.**

**Layer 1 — sixteen packet manifests at `82633a60`.** 678 distinct 64-hex values across the sixteen manifests; **565 resolve to committed blobs**, exactly the number in the brief. The 49 distinct non-resolving values (113 occurrences) are classified by manifest key in `results/b20_10/unresolved_manifest_hashes_by_key.json`: 22 are worker-branch files (resolved at Layer 2/3 below or historical B15–B18 documents on other branches), 3 are literature PDFs (EH `6b10d8fe…`, Dimca `20b96f58…`, Segal `8c8d9d05…`), 5 are chat attachments (`e9130c38…`, `cd117721…`, `de741dea…`, `438aec6f…`, `f850f840…`), 1 is the interpreter `4d6f5f81…`, 1 the wrapper `ca001081…`, and the rest are handover documents, the Batch-17 census, batch-13 notes and `read_only_inputs_sha256_gct_original` pins. Nothing unexpected. **Layer 1 PASSES; D6 nesting confirmed** (the `scope_corrigendum` and `clarification_20260917` manifests carry their own files; the parents cannot list them).

**Layer 2 — the eleven worker files the packets pin.** All eleven committed blobs at the worker commits have sha256 values that occur verbatim in the archive text (`aa136106…`, `52a9e474…`, `e28bcc93…`, `26f66bc4…`, `16aa1626…`, `1af53479…`, `76e709ba…`, `5ac1a31f…`, `b998182a…`, `bec224ec…`, `d2d992d9…`). **PASSES.**

**Layer 3 — the B19 record.** All twelve listed prefixes match the committed blobs (`aa136106`, `33b154e6`, `52a9e474`, `e28bcc93`, `dc074191`, `8a321a18`, `30942342`, `c9604f9e`, `ee256f38` (LF blob), `63f002d4`, `129a7c2c`, `575b1cae`). The one B15-10 path in the housekeeping commit, `docs/b18_10_integrator_review.md`, hashes `036c1616…`. **PASSES.**

**Layer 4 — hash-only inputs.** All recoverable on this machine today, with matching hashes (subagent inventory, read-only; the interpreter and the LLV file I re-hashed myself): the Eisenbud–Harris scan `eh1988.pdf` (`6b10d8fea80396a7c833…`, 1,067,244 B) in a Claude session scratchpad under `%TEMP%`, with its 21 page images beside it; Segal (`8c8d9d058c878e77…`, two identical copies, one in `%TEMP%\astra_gkz_20260917_literature`); Dimca (`20b96f5830291574…`); the two transverse attachments `cd1177211fe4…` (`515d31fd…/pasted-text.txt`) and `e9130c3865a3…` (`43761221…/pasted-text.txt`) among the 34 files under `.codex/attachments`; the interpreter `B15-02/.venv/python.exe` (`4d6f5f81a4bca111…`, Python 3.12.10, an embedded distribution rather than a venv); the wrapper `b15_bound.py` (`ca001081…`); the LLV PDF `B15-01/results/b18_01/literature/arXiv_2303.09028v3.pdf` (`67b1701f761d4336…`, equal to B19-11's inventory) with its text extraction `llv_v3.txt` (§4.3). **Recoverable today; none of it is committed, and a scratchpad clean would remove the first five.** Three provenance facts surfaced: (i) the 21 page images carry no pinned hash anywhere, and the committed `checks/render_eh_pages.py` (`81fd16d9…`) matches neither of the two render scripts found beside them on disk (`render_eh.py`, `render_eh2.py`), so the images cannot be tied to the committed script; the transcription in the singular-locus report is tied to the PDF hash only. (ii) The pinned `ca001081…` for `b15_bound.py` is the hash of the CRLF working copy; the LF git blob is `1f73ad8d…` (the same class of fact `COMMIT_REPORT.md` §2 records for B19-11's manifest). (iii) `descent_followup_claude_20260916/REPORT.md` line 22 refers to "§A.4", a section that does not exist in the sealed report (the fourth-order witness is reviewed under E11 / P9); a dangling cross-reference, not a missing result.

**Layer 5 — D5.** Corrected in §5.

**Known non-resolutions, confirmed from committed bytes.** D1: `routeA_signfilter_20260917/results/s1_screen_arc.json` pins `candidates_selected.json` at `11df1d527b28cafd5a31…`; the committed file is at `certificates/candidates_selected.json` (not `results/`) and hashes `a69c6313f2d736b2040a…`; `s2_certify_n02_and_new.json` and `s3_full_forbidden_rows.json` pin `a69c6313…`. The 12-record version does not exist at `82633a60`. Confirmed.

## 3. The two deferred items

### 3.1 The Levi commutation argument (B19-01 §6, Proposition 6.1, Theorem 6.2) — [pre-formed]

**Pre-verdict (P2, before reading §6):** formal if `L` is defined as the subgroup preserving each graded piece of `W`; the only failure modes are (i) `b` not being the dimension of a projection of an `L`-stable space of `L`-invariants, (ii) "grading-preserving" meaning a parabolic rather than the centraliser, (iii) the branching expansion omitting components.

**Read against the proof.** Proposition 6.1 defines `L ⊆ H` as the subgroup preserving the three `gamma`-weight spaces and computes `L^0 = {x -> AxB : A = diag(alpha, A'), B = diag(beta, c A'^T), det A det B = 1}`. I re-derived it: preserving the first row forces `A e_1 ∝ e_1`; preserving `W_{+1}` (zero first row, symmetric lower block) forces `B`'s first row and column to `(beta, 0, 0, 0)` and the lower block map `E -> A' E B'` to commute with transposition, hence `B' = c A'^T`; the transposition coset preserves no weight space because it swaps `r` (weight `-1`) with `c` (weight `+1`). So `L` is connected, `L = L^0`, and the derivation is correct. Theorem 6.2's first two steps are then formal: `L` preserves each `(mu, kappa, tau)`-component, so the skew-degree projection is `L`-equivariant on all of `S_lambda W` (stronger than the negative-weight projection, which is all that is needed); `L ⊆ H` gives `M_lambda ⊆ (S_lambda W)^L`; hence `C(M_lambda) ⊆ ((S_lambda W)_{<0})^L` and `b <= dim((S_lambda W)_{<0})^L`. **PROVED.**

**One proof gap, conclusion unaffected.** The displayed expansion sums only over `|mu| = d` and justifies this by "Proposition 3.1 plus Proposition 6.1". Proposition 3.1 uses invariance under the diagonal tori of `SL(A)` and `SL(B)` (a 6-dimensional torus); the maximal torus of `L` is 5-dimensional and does not contain it. The restriction nevertheless holds for `L`-invariants: on the subtorus `{(alpha, beta, c) : alpha beta c^3 = 1, A' = I}` a component with adapted multidegree `(#a, #r, #v, #c, #S)` has character `alpha^{#a+#r} beta^{#a+#c} c^{#r+#v+#S}`, which is trivial iff `(#a+#r, #a+#c, #r+#v+#S) = m(1,1,3)`; with total degree `4d` this gives `4m = 4d`, so `|mu| = #a + #r = d`. This is exactly the argument `arc_target_dimension_followup` §3.2 gives ("`|mu| = 5` is automatic for `L`-invariants"). B19-01's proof of the expansion is therefore incomplete as written and complete on the record. **Label: PROVED; proof of the expansion line to be read from `arc_target` §3.2.**

**One wording precision, endorsed.** B19-01 Theorem 4.1 says the "forbidden part of `S_lambda W` is zero". Forbidden there means skew degree `> 2d` (Corollary 3.2), which is a statement about the whole Schur module and is correct. It must not be read as "the negative-`gamma`-weight part of `S_lambda W` is zero", which is false (components with `|tau| < |mu|` exist off the invariant source). `extension_descent` §1 makes this precision; I endorse it. `C = 0` on `M_lambda` in the band is unaffected.

**Independence of the bound from the count.** The screen `dim((S_lambda W)_{<0})^L` was evaluated once on the record, at `(5,(4^5))`: `b_L = 74` (`arc_target`, two formulations, PROVED), against the trivial ceiling `rank C <= 4`. So the one evaluated instance of the Levi screen is uninformative. B19-01 §6.3 step 2 (the `GL_3` invariant count) remains **NOT REACHED for any cell with `s - a` small enough for the screen to matter**, exactly as B19-01 says.

### 3.2 The 10,505-triple count (B19-01 §6.3) — [pre-formed]

**Pre-verdict (P1):** by hand, `p_4(7) = 11`; `p_3(15..21) = 27, 30, 33, 37, 40, 44, 48`; `p_9(6..0) = 11, 7, 5, 3, 2, 1, 1`; `sum = 297+210+165+111+80+44+48 = 955`; `11 x 955 = 10,505`.

**Replayed in pilot 1** (`counts`): `d7_p4 = 11`, `d7_inner_sum = 955`, `d7_crude_triples = 10505`; `d26_crude_triples = 424,193,140`, which is B19-01's "about `4.2·10^8`". **PROVED counts**, with the scope B19-01 gives them: they count raw `(mu, kappa, tau)` triples before the containment restrictions `mu, kappa, tau ⊆ lambda` and before Littlewood–Richardson vanishing (at `(5,(4^5))` only 9 of the raw triples survive), and they bound the size of an enumeration, not `b`.

### 3.3 Pilot 1 — the `(4^5)` cell by an independent evaluator (INDEPENDENT EVALUATOR)

`analysis/b20_10_p1_independent_invariant.py` (sha256 in `MANIFEST.json`), input the committed certificate `results/b19_02/rect_4_4_4_4_4.json` at `75ddb900` (sha256 `16aa1626…`, copied to `results/b20_10/inputs/`), run under `B15-02/analysis/b15_bound.py --seconds 60 --memory-mb 512` with the pinned interpreter: exit 0, wall 1.07 s, peak Job memory 12,963,840 B, receipt `results/b20_10/b20_10_p1_independent_invariant_resources.json`.

The unique (`a = 1`) degree-five `SL5`-invariant of quinary quartics is realised as the four-epsilon contraction `I(F) = sum_{tau,rho,pi} sgn(tau rho pi) prod_i T[i, tau(i), rho(i), pi(i)]` on the symmetric coefficient tensor. No project code is imported; the determinant points are expanded here by Leibniz from the certificate's `4x4x5` matrices; the padding points are `l · per_3(N)`.

| check | result |
|---|---|
| Fermat control `I(sum t_a x_a^4) = 24^5 prod t_a` | `5,733,089,280 = 5,733,089,280`, pass |
| generic 61-monomial control | nonzero |
| three recorded determinant points | independent values `-92426948831256103104`, `1311544807472918477568`, `855827308056012231552`, all nonzero; **ratio to the recorded values `192` at all three points** |
| three recorded padding points `l · per_3(N)` | `0, 0, 0` |

A constant ratio across three points ties this evaluator to B19-02's highest-weight vector up to scale, so it confirms both the vector and the recorded values without using either. Nonzero at an actual determinant point gives `m_det >= 1 = a`. **`m_det(5,(4^5)) = 1`: CERTIFIED, second lineage.**

`m_pad = 0` I re-derived (READ + own proof): `F = x_1 C` is in the `SL5` null cone (the one-parameter subgroup `x_1 -> t^4 x_1`, `x_i -> t^{-1} x_i` gives every monomial `x_1^{1+k} m_{3-k}` weight `1 + 5k >= 1`), and the `(4^5)` highest-weight vector is an `SL5`-invariant of positive degree, so it vanishes on `R135 = closure{l · C}`, which is `P_5` at five rows. This is B18-01 Proposition 8.4; the three zeros above are consistent with it and are not used as evidence. **`m_pad(5,(4^5)) = 0`: PROVED.** Hence **`D = m_pad - m_det = -1`: PROVED (padding leg) and CERTIFIED (determinant leg), two lineages.**

### 3.4 Pilot 2 — spot replay of three certificates (REPLAY)

`analysis/b20_10_p2_spot_replay_certificates.py`, inputs the three committed certificates copied to `results/b20_10/inputs/` (hashes `4ac3f896…`, `1f0da0af…`, `fce1a1a3…`), same wrapper: exit 0, wall 0.08 s, peak 12,693,504 B.

| certificate | replayed | result |
|---|---|---|
| `routeA/certificates/transverse_triple_rank3.json` | rebuild the `3x3` matrix `[C2; C4_{S1,S2}; C4_{S1,S4}]` on `(q3, q7, n02)` from the recorded pencil values and the displayed formulas; det mod `524287` | matrix equals the stored one; det `225843`; rank 3 |
| `routeA/certificates/independence_q3_q7_e_n02.json` | five `4x4` minors, rank | `426380, 191230, 255288, 485311, 35010`; rank 4 |
| `final_arc_diagnostic/results/f1_new_point_minor.json` | 14 x 3 forbidden matrix: rank; all `C(14,3) = 364` minors; residuals of `n02 - 265391 q3 - 275398 q7` | rank 2; 0 nonzero minors of 364; all residuals 0; degree-12 rows rank 1, degree-11 rows rank 2 |

Replay of saved arithmetic only; no source vector was evaluated.

## 4. The dependency chain, link by link

Labels: **PRIMARY** (the packet says it read the primary text and records a file and hash, and I could re-read the citation in the committed text), **SECONDARY** (quoted through a programme note, a survey or a previous report), **UNREAD/POINTER** (cited by name, never fetched). Load-bearing means a labelled claim on the record depends on it.

| dependency | where load-bearing | how consulted | label | exposure if wrong |
|---|---|---|---|---|
| Eisenbud–Harris 1988, Thms 1.1–1.2, Cors 1.3–1.4, rank formula, nondegeneracy | `claude_singular_locus_audit` Lemma 3.2(c) (Cor 1.4) and Lemma 3.3 (Thms 1.1, 1.2, Cor 1.3), hence Theorem 4.1 (C8, "conditional only on C1") | scan `eh1988.pdf` sha256 `6b10d8fea80396a7c833…`, 1,067,244 B, rendered to 21 page images, pp. 135–141 transcribed verbatim (REPORT §1.1); proofs in EH §3 **not** re-verified (C1) | **PRIMARY (statements), proofs unread** | a closed route (`rho_Z = 0`) would reopen; no cell closure or `D` value rests on it (§4.1) |
| Ballico 1995 addendum, Beitr. Algebra Geom. 36, 119–122 | C3 ("no later correction alters EH §1") | **not read by anyone**; EUDML record only. My three attempts (§4.2) also failed | **UNREAD** | same as above; mitigated by Atkinson 1983's independent proof (itself unread) and by the addendum's own record (§4.2) |
| Atkinson 1983 | corroborative only (singular-locus REPORT §1) | "Not fetched"; restated through Huang–Landsberg §4.1 | UNREAD/POINTER | none by the packet's own scoping |
| Huang–Landsberg arXiv:2306.14428v1 | "no result of this paper is load-bearing" | arXiv HTML read, not hashed | read, unhashed | none |
| Atkinson–Lloyd | definitional contrast only | through HL | SECONDARY | none |
| Domokos–Zubkov / Derksen–Weyman / Schofield–Van den Bergh (FFT for `SL4 x SL4` on `(Mat4)^5`) | singular-locus Lemma 3.1's semistability certificate (check 1); B19-02 §2 (declared non-load-bearing there) | "adopted exactly as in the B15-12 note" | **SECONDARY** | check 1's `G`-semistability of `X_0` would lose its certificate; Theorem 4.1 does not need it (Case 2 uses only that unstable tuples kill invariants, which is definitional) |
| Refined Bézout, Fulton Ex. 8.4.6 / Thm 12.3 | B18-01 Theorem E's upper end `d_5 <= 4^49` (B19-12 F2, H-Bez) | secondary quotation in `b18_01_review` §4; untouched by B19 and by every post-B19 packet (absent from the archive) | **SECONDARY** | the bracket's upper end `4^49` becomes unlabelled; the lower end `6` (B19-02 Cor 8.1) is independent of it; the number is never a budget |
| Gulliksen–Negard (via Bruns–Vetter) | GKZ Theorem A (`N = 16`), all `k` | "ADOPTED exactly as in `onset_conjecture.md` §2 (not re-fetched)" | **SECONDARY** | Theorem A's containment `J_k ⊆ I(Y_det) ∩ I(Y_pad)` in sixteen variables; Theorem B (five variables) does not use it |
| Kleiman transversality | GKZ Theorem B for `k >= 7`; batch-13 Jacobian cap | same secondary route | **SECONDARY** | Theorem B at `k >= 7`; `k <= 6` rests on P2's exact ranks |
| Bruns–Herzog Prop. 1.5.12 | GKZ Theorem B proof, part (iii) (regular sequence of general combinations) | cited by name inside the proof; **absent from the packet's literature list and manifest**, no label | **UNREAD/POINTER, unlabelled** | Theorem B part (iii) at `k >= 7`; a labelling defect in a packet that labels everything else |
| Dimca Thm 3.1, arXiv:1210.1795v4 | GKZ `k = 6` alternative and Remark 3.3 only; "not needed at `k >= 7`" | PDF sha256 `20b96f5830291574…`, 198,017 B, Theorem 3.1 read (VERIFIED-SOURCE) | **PRIMARY** | none (P2 certifies `k = 6` independently) |
| Segal arXiv:2412.14748v1 | GKZ packet and Astra: "a dependency map, not an invocation of unverified machinery" | PDF sha256 `8c8d9d058c878e77…`, 579,885 B, read in full by both packets | **PRIMARY** | none by both packets' scoping |
| HMSV Lemma 6.6 (`SO_4` reflection-odd invariants have exactly four odd parts) | `fiber_compatibility` rectangular blindness `D_{(4k)^5} = 0` | URL and printed page only; "pointer not fetched" (descent E16), result "re-derived" there | **UNREAD/POINTER**; the fact itself is the classical `O_n` branching rule (`S_alpha(C^n)` carries the determinant character of `O_n` iff `alpha` has exactly `n` odd parts), which I know independently | none in substance; the pointer should be replaced by a textbook citation or a two-line proof |
| LLV arXiv:2303.09028v3 | B19-02 Cor 4.3, Claim 6.1, Cor 8.1 (`I(D45)_d = 0` for `d <= 5`) | B19-02 report: secondary, CONDITIONAL; integrator (review §1, ledger §7e.3): "verified against the primary text" without naming a file or hash; **confirmed here** (§4.3) | **PRIMARY** (confirmed) | none now |

### 4.1 Eisenbud–Harris and the singular-locus closure theorem — [pre-formed]

**Pre-verdict (P3):** the vanishing on `Z` would be a null-cone / one-parameter-subgroup argument, with EH entering only through the description of which subspaces occur; a correction to EH §1 would change the *scope* of "every five-row cell" only through the identification of the semistable singular spans, not the vanishing on the spans as described.

**Read against the proof of Theorem 4.1.** Case 1 (dependent tuples) is Claim 4.2.2 of the B15-12 note, which uses only that every weight of `S_lambda(C^5)` with `l(lambda) = 5` has fifth coordinate `>= lambda_5 >= 1`. Case 2 (unstable tuples) is definitional. Case 3 uses Lemma 3.3 to place a `G`-semistable singular 5-dimensional span inside `Mt` up to bases and transpose, finds a column-only element by a dimension count (`5 > 4`), and kills `f` with the explicit one-parameter subgroup `g(tau) = (diag(1,1,1,1,tau^{-4+eps}), diag(tau,tau,tau,tau^{-3}), diag(tau^{-1},tau^{-1},tau^{-1},tau^{3}))`. I checked the exponents: the `S` block scales by `tau^0`, the `u` column by `tau^4`, the `t` entry by `tau^0`, the zero row by `tau^{-4}`, and the column-only fifth matrix by `tau^{eps}`; the limit exists; `f(g(tau) T) = tau^{-(4-eps) nu_5} f(T)` with `nu_5 >= 1` forces `f(T) = 0`; the reduction to weight vectors of a basis tuple is valid because the isotypic component is `GL5`-stable. **The mechanism is self-contained and correct.** EH enters exactly and only through Lemma 3.3 (and Lemma 3.2(c) via Corollary 1.4). The pre-verdict is confirmed.

**What rests on it.** Theorem 4.1 feeds the restriction bound `m_det <= min(a, s - rho_L + u_L)` (descent B1) with `L = Z`, `u_Z = 0`: it says `rho_Z = 0`, i.e. the bound reads `m_det <= s`, the trivial one. A positive `rho_Z` would *lower* a ceiling on `m_det`, i.e. would open a route. So Theorem 4.1 is a **route-closing** theorem. If EH §1 were corrected so that Lemma 3.3 failed, the consequence is that the singular-locus route is not closed, not that any positive claim on the record is false. No cell closure, no `D` value, no `I(D45)_d = 0` statement depends on it. **Exposure: a wrongly-closed route, nothing else.** The packet's own falsification criterion (a `G`-semistable 5-dimensional singular `4x4` space with no column-only or row-only element) and its proposed literature-free fix (a self-contained proof of Lemma 3.3 for `4x4` matrices) are the right ones. **Label: C8 PROVED conditional on C1 (primary statements) and C3 (unread); unchanged.**

### 4.2 Ballico 1995 — three attempts, all failed

I tried to read the addendum myself. (i) EMIS mirror of Beitr. Algebra Geom. 36(1): the index and the file `b36h1bal.ps.gz` both 301-redirect to zbMATH; the "PostScript" download is an HTML page (sha256 `7bc06934…`, 502,238 B). (ii) zbMATH Open API: the record exists (Zbl 0828.14009, MSC 14F05, 14N05, 15A03, 15A99; title *"Vector spaces of matrices of low rank and vector bundles on projective spaces: An addendum to a paper by Eisenbud and Harris"*), review text "unavailable due to conflicting licenses". (iii) EuDML doc 227256: metadata only, full-text links dead. **Not read. UNREAD stands.** Two secondary facts lower the risk without discharging it: the descent session's EUDML abstract reading that the addendum shows Atkinson's rank-`<= 3` characterisation *follows from* the EH results (a corroboration, not a correction), and the MSC placement (sheaves, projective techniques), consistent with the singular-locus packet's reading that the addendum concerns EH §§2, 4. The proper discharge is the literature-free Lemma 3.3; until then C3 stays open and every downstream use of Theorem 4.1 stays CONDITIONAL.

### 4.3 LLV — confirmed from the primary text on disk

`llv_v3.txt` (extraction of the PDF hashed `67b1701f…`, B19-11 inventory) contains, verbatim: "Theorem 2. The family of determinantal quartic surfaces consists of 5 prime divisors F1, . . . , F5" with "deg(F1) = 320112, deg(F2) = 136512, deg(F3) = 38475, … deg(F5) = 2508"; the abstract line "320, 2508, 136512, 38475 and 320112"; the table row "F1 (5,5,5,5) (6,6,6,6)"; "Corollary 3.1 (of Theorem 1). The linear determinantal surfaces of degree d form a family of dimension …"; "Proposition 1.1. Let (a, b) be an admissible pair. Then det(a, b) is irreducible". That is the integrator's chain, and I read it in the primary text. **The lift of CONDITIONAL on LLV is CONFIRMED; the five-component precision is CONFIRMED (`D44 = F1`, degree 320112; the others 320, 2508, 38475, 136512).** One record defect: neither the B19-02 review nor the B19-12 ledger names the file or hash it read; the only hash on the record is B19-11's inventory. Gate G14 (§9) closes this class.

### 4.4 Refined Bézout — [pre-formed]

**Pre-verdict (P5):** secondary; feeds only an estimate already discounted; no PROVED claim rests on it. **Confirmed:** absent from all eleven packets; in the B19 record only as B19-12's H-Bez ("remains a secondary quotation, untouched") and the F3 calibration. It labels the upper end of `6 <= d_5 <= 4^49` only. **SECONDARY; CONDITIONAL stands; nothing else moves.**

## 5. D5 — what status a claim can hold when its input is unrecoverable — [pre-formed]

**Pre-verdict (P4):** a claim whose only evidence is an unrecoverable input cannot be PROVED or CERTIFIED; if it is an inference from the value it is CONDITIONAL on an unverifiable premise and must not be consumed downstream.

**What is actually on disk, at `82633a60` (READ, `git grep`):**

| value | housekeeping says | committed artifact | status |
|---|---|---|---|
| `-12` (six-row fourth-order witness `C2(Q^2)`) | no script, JSON or manifest | `descent_followup_claude_20260916/pilots/p9_sixrow_replay.json`: `"C2_on_Q2_normalised": "-12"`, computed by `p9_sixrow_replay.py` line 52 | **recomputed and stored** (descent E11 VERIFIED, execution replay of the producer's evaluator) |
| `108`, `-14`, `3/896` (six-variable fourth-order constants) | chat attachments only | `claude_transverse_structure_20260916/checks/c2_fivevar_order4.json`: `"N_ratio_S2_over_S1": "108"`, `"A2_minus_108_A1": "-14"`, `"kappa_from_S1": "3/896"`, `"kappa_from_S2": "3/896"`, by `c2_fivevar_order4.py` (T7 VERIFIED) | **recomputed and stored** |
| `175/36` (cone-vertex contraction value) | no artifact | `descent_followup_claude_20260916/pilots/p3_c2_derivation.py` line 61 computes `H5_base_e95_convention_T_over_24` from the stored `322560` (`= 5!·322560/24^5`, E4 VERIFIED) | **recomputable from a committed value by a convention change** |
| `Ω det Q = 315/4` | no artifact | none | **chat-only** |

So five of the six "chat-only" values are on the record as recomputations, and the PRE_AUDIT sentence "Nothing on disk would reveal an error in any of them" is false for those five: an error in the attachment would show as a disagreement with the committed recomputation, which is how the descent session validated them. The housekeeping's A.0 sentence was about the *Astra* directories, and was correct there; it was generalised in the audit to the whole record, which is where it became wrong.

**Ruling.** (a) `Ω det Q = 315/4`: ADOPTED as the symmetric Cayley identity (a standard result), used only in the `a = 0` quadratic-square control E17, itself CONDITIONAL; nothing on the record consumes it; **status CONDITIONAL, unconsumed, no downgrade needed downstream**. (b) The five recomputed values: their status is that of the committed recomputation — VERIFIED (execution replay) for `-12`, VERIFIED for `108`, `-14`, `3/896` (T7), VERIFIED for `175/36` (E4) — and the attachments are no longer the evidence. (c) General rule, adopted as gate G9: **a value that exists only in a chat attachment is inadmissible as a premise of any PROVED or CERTIFIED claim; the claim is CONDITIONAL until the value is recomputed into a committed artifact.** D5 as a defect is reduced to one unconsumed constant.

## 6. Dispositions for D1–D9

| defect | confirmed from committed bytes? | what it does to claims | disposition |
|---|---|---|---|
| **D1** stale pin: `s1_screen_arc.json` pins `candidates_selected.json` `11df1d52…`; committed `certificates/candidates_selected.json` is `a69c6313…`; s2, s3 pin `a69c6313…` | yes (§2) | s1's screening output (which candidates the arc screen selected, and its statistics) is **MEASURED, not replayable**. Nothing certified rests on s1 alone: the independence certificate (L13), the sign-filter theorem (L20), `rank T = 3` (L21) and the forbidden matrix (L15) pin the 14-record file and their own inputs. | Record; do not repair. Downgrade every number sourced to s1 alone to REPORTED (non-replayable). Gate G10. |
| **D2** "36/36" | the verifier prints 30 PASS and no total (PRE_AUDIT measured) | none; the sentence is SUPERSEDED by the measured 30/30 | Gate G16: counts are emitted by the verifier, never typed. |
| **D3** `q_3`, `q_7` orderings in four scripts, no definition certificate | yes (scripts at `82633a60` carry the tuple) | L13, L15, L21, L25 are CERTIFIED **as computed by the committed scripts**: replayable from code, **not portable as data** — the class B19-11 caught for the batch-18 sweep. Validity unchanged; portability defective. | Hard prerequisite for any Phase 2 consumer of `q_3`, `q_7` (gate G8). Fix in a new directory in the `n02_definition.json` format with an ordering hash; never touch the sealed packet. |
| **D4** `.pyc` dropped into a sealed tree by a later import | excluded from the archive; all 14 manifest entries verify | none | Gate G11: `PYTHONDONTWRITEBYTECODE=1` (or `sys.dont_write_bytecode`) in every wrapper invocation that imports from a sealed tree. |
| **D5** chat-only inputs | corrected in §5: one constant, unconsumed | none | Gate G9. |
| **D6** child packets invisible to parent manifests | yes (§2, Layer 1) | none; both children self-manifest | Gate G12: new packets are siblings, never children, of a sealed tree. |
| **D7** parent GKZ REPORT lines 84 and 179 ("the only place … signs enter") | read: both are exhaustiveness claims of the C8 type | **SUPERSEDED**, withdrawn by type under C8; recorded by line here since C8 does not name them | Gate G15: a corrigendum names every withdrawn sentence by line. |
| **D8** missing receipts (two aborted check-2 starts; ImageMagick render; P1/P3/P5 unwrapped; failed first P7 overwritten) | disclosed in the packets | none: check 2 is "not used as evidence"; P1/P3's outputs (`s = 5`, `g = 6`, `a = 1`, `m_det = 1`) are all reproduced elsewhere on the record (B19-02, clarification, and pilot 1 here); the failed P7 is a cost fact, not a result | Gate G10: receipts are never overwritten (unique run names), aborted starts get receipts, unwrapped runs are labelled "no memory receipt". |
| **D9** `L` overloaded (jet line vs Levi); `det3-conductor.tex` vs `det-conductor.tex`; `delta_0` in a quartic title | read | none; wording | Gate G13: distinct symbols; corrigendum, not manifest edit. |

## 7. Scope, under pressure — what I checked and what I found

Method: READ of the governing documents (corrigenda first), with the four scope hazards of the brief in mind, followed by a judgement of every sentence the scope extraction surfaced (647 lines, all packets, six headings; `results/b20_10/extractions/scope_extraction.md`). Every sentence the extraction tagged as a possible hazard I re-read in context; the judgements below are mine.

**Rank directions.** The B19-05 intake's direction rules (§3 there) are correct and were applied correctly: a global ideal floor `q` gives `m_det <= a - q`, a *lower* bound on `D`, and excludes only with exactness (P-S57) or an evaluation floor; the intake reconciles B17-12 and B18-12 on exactly this point, and its reconciliation is right (B18-12's "floor, `m_det` unknown" together with its `D` column was direction-inconsistent). B19-02 Theorem 4.4 (`m_det <= s <= g`, `a > g => i_det >= a - g`) and Theorem 7.1 (a rank drop *below* the ceiling certifies nothing) are stated in the right directions. `rank T = 3` "as a value" is a floor (nonzero minor) meeting a trivial ceiling (three rows), correctly labelled. `rank C ∈ {2,3,4}` and `rank(C|U) ∈ {2,3}` are floor-plus-ceiling ranges, correctly labelled OPEN. **No rank used from the wrong side found in the governing documents.**

**The actual-padding model.** B19-02 §1 uses `P_5` throughout and "never evaluate[s] on a product above five variables"; `extension_descent` §5 states the five-variable identification explicitly before calling a nonzero `l · C` value a padding separation certificate; `claude_image_ceiling` §2.1 uses `Y_pad = R135` at five rows only; the intake's six-row row `(14,2^5)` uses the generic-product `T` as a *ceiling* only, which is the valid direction (`P_6` inside the generic-product variety). **Holds.**

**Source membership.** `q_3`, `q_7`, `n02` by construction (epsilon contractions with the full-`H` argument; `fiber_compatibility` and `extension_descent` give the argument in full); `e = H5 ∘ phi ∈ E ⊆ M` by `a = 1` plus the row-model identification (clarification L3, premises listed); the sampled-zero candidates `n05`, `n07`, `n09` and P6 index 10 are never promoted. **Holds.**

**Global versus sampled.** Correctly qualified everywhere I read: the degree-12 relation "sampled-true", `(265391, 275398)` residues "not a rational witness" (C3), the covariant identities "conditional on pattern-span injectivity; unconditionally at the general point", the 33 "identically vanishing" contractions withdrawn to "zero at the recorded points" (descent addendum A), `C2(n̄) ≡ 0 mod P` "proves nothing about `C2(n*)`". **Holds — with one inconsistency in the integrator's own ledger, which is the opposite error:**

**Finding S1 (integrator, not producer). `L24` is stale and contradicts `L21`.** The clarification packet, working with two source columns `(q_3, q_7)`, correctly said the triple `{C2, C4_{S1,S2}, C4_{S1,S4}}` could have rank 2 or 3 on `M` and that a two-column test cannot decide it. The routeA packet, later the same day, added the third certified column `n02` and recorded a nonzero `3x3` minor of integer evaluations (`transverse_triple_rank3.json`, det `225843` mod `524287`), which I replayed (§3.4). A nonzero modular minor on three vectors of `M` proves the three functionals linearly independent on `M` over `Q`. So **"the three transverse rows are jointly independent on `M`" is CERTIFIED**, and `L21` is right. `L24` ("NOT ESTABLISHED"), PRE_AUDIT §4D ("CONTRADICTED as stated") and §7.5, and `POST_B19_STOCKTAKE` §5 and §9 item 5 carry the pre-`routeA` state forward as a "record correction". The correction is itself wrong and must not enter the Batch 20 board. (What remains OPEN is different and correctly stated elsewhere: independence of the transverse conditions from the *arc* `C`, L26.)

**Finding S2. "Every"/"only" in the parent GKZ report.** D7's two lines are withdrawn (§6). Beyond them, the governing `REVISED_VERDICT.md` and `CORRIGENDUM.md` C1–C12 are scoped exactly; the assessed/unassessed range (C7) and the three statuses absent / excluded-by-theorem / not-funded (C8) are the right distinctions, and I found no surviving exhaustiveness claim in the governing text.

**Finding S3. The silence theorem's reach.** B19-01 §4.3 and the review's `3 | d` precision at `l = 6` are correct (recomputed by the integrator; the arithmetic `3·4d/5 = 2.4d > 2d` I checked). The theorem is about one arc; `extension_descent` §3 shows a globally necessary condition (`C2`, rank one) that the arc misses at `(6,(4^6))`, so "the arc is blind in the band" must never be read as "the boundary is silent in the band". Both documents say this; the stocktake says it; I confirm it.

**Finding S4. The intake's degree-six settled count.** B19-05 §2.5 lists four settled `d = 6` five-row cells; the B18-06 review's "three or four" is resolved as four there. Post-B19 adds `(8,4,4,4,4)` (`D <= 0`, descent B.9) and `(12,8,2,1,1)` (`i_det = 0`, extension_descent §6): six degree-six five-row cells now carry a cell-level bound (§10).

**What the full extraction added.** Across the six headings the archive's discipline holds: every rank used from the wrong side that the extraction flagged turned out, in context, to be a floor meeting a ceiling (`rank T = 3`, `rank C = 2` in the fibre cell, `dim span = 4`), a ceiling used to show a bound is weak (`u_L = m_pad` in the image-ceiling report), or a hypothetical withdrawn by a corrigendum (`b_L ∈ {2,3,4}` cases, AT C2). The "padding" object is `P_5 = R135 = {l·C}` in every five-variable statement and the genuine `closure(GL_16 · z per_3)` in every sixteen-variable statement; no packet evaluates on a general product above five variables and calls it padding (Astra says so explicitly at its line 285). Membership of every source vector is by construction or by the `a = 1` identification, with the sampled candidates never promoted. Five wording slips survive in non-governing text and are recorded here so they are not quoted forward; none changes a label:

- **W1** `clarification_20260917/SOURCE_HANDOFF.md` lines 76–78: "independent … **iff** the `4x5` matrix has modular rank 4" — the correct direction is stated in the same sentence ("a floor, valid over `Q`"); "iff" is wrong (modular rank 4 implies independence, not conversely).
- **W2** `routeA_signfilter_20260917/REPORT.md` lines 13–15: "so no `rank C >= 3` or `= 4` certificate **exists**" — should read "was found"; the packet's own ledger (line 277) and `CURRENT_DIAGNOSTIC_STATE` §2 state it correctly as OPEN.
- **W3** `direct_arc_relation_followup/REPORT.md` lines 163–164: "only degree-11 rows can contribute, so the minor must use at least two degree-11 rows" — true for minors drawn from the recorded points (where the degree-12 rows are rank 1), a prior for new points; the degree-12 rank-1 structure is SAMPLED (`CURRENT_DIAGNOSTIC_STATE` §4 says so; the same packet's line 143 calls it "a genuine structural fact about `B`", which overstates).
- **W4** `CURRENT_DIAGNOSTIC_STATE.md` line 121: "the paired families tried so far live in `span(q_3, q_7, e, n02)`" is unqualified; routeA lines 182–183 give it as MEASURED mod `P` for `m00`, `m01` only.
- **W5** `SOURCE_HANDOFF.md` lines 171–172: "if `b_L = 4`, Route A and Route B are the two exhaustive outcomes" — moot since `b_L = 74`, and "exhaustive" was never proved; AT C2 withdraws the parallel routeA paragraph but no corrigendum names this line.

Two further parent-GKZ sentences of the C8 type that C8 does not name by line, in addition to D7's lines 84 and 179: line 15 ("the one GKZ construction that produces determinant-specific information beyond 'singular'") and line 90 ("the only candidate that … admits a complete answer"). **Treated as withdrawn by type**, like D7.

## 8. Ruling on the G5 generalisation

**G5 as written (Batch 18).** A gap claim passes only with `B = min(a, s - b)` (`b` certified or 0) and an exhibited `(B+1)`-minor of highest-weight polynomials at actual padding points, same cell, same convention, minor rechecked; `U > B` alone is headroom; geometric separation is reported as such and never as `D > 0`.

**Proposal (roadmap correction 3).** Generalise to any certified `B` and `r > B`, including `B = a - q`; state the `a = 1` separation exception explicitly.

**Ruling: ACCEPTED, as G5′ below, with four conditions and the exception stated.** The logic is sound: any certified upper bound `B >= m_det` together with a certified padding floor `r <= m_pad` with `r > B` gives `m_pad >= r > B >= m_det`, i.e. `D > 0`. The arc's `B = min(a, s - b)` is one source of such a `B`; a certified global ideal floor `q` (equations proved to vanish on the whole closure `D45`, e.g. through `ker phi^*` as in B19-02 Lemma 3.1, or a proved transport) gives `B = a - q` and is another; a certified restriction bound `min(a, s - rho_L + u_L)` with `rho_L` a certified floor and `u_L` a certified ceiling (descent B1) is a third. The conditions:

1. **`B` must be unconditional.** A `B` that holds under an inherited premise (P-S57, a stable-tail carry, an uncomputed finite `T`) yields a gap claim labelled CONDITIONAL on that premise, which never passes as a release. Direction is checked per G3: a floor on `i_det` is a ceiling on `m_det` (usable as `B`); a floor on `m_det` (`r_det`) is never a `B`; a ceiling on `b` is never `b`.
2. **`r` must be a rank of evaluations at exhibited actual-padding points per G4**: at five rows an explicit `l · C` suffices because `P_5 = R135`; at `L >= 6` rows the points must be exhibited on `P_L` as `(z per_3) ∘ T`, and a rank on a general product bounds the wrong variety and is inadmissible. The rank is of the full `a`-dimensional highest-weight space (or of a certified subspace, with the subspace's own certificate), in the same cell and convention as `B`, and its nonvanishing minor is rechecked by the reviewer.
3. **A rank drop below `B` certifies nothing** (B19-02 §7.1); only `r > B` fires, and only a nonzero minor fires it. Sampled zeros never enter.
4. **Modular evidence enters in the safe direction only**: a nonzero minor mod `p` of integer evaluations is a floor over `Q`; a modular rank deficiency is not a ceiling. Single-prime evidence is admissible for a floor; it is never admissible for a value.

**The `a = 1` exception (stated).** When `a = 1`, `B ∈ {0, 1}` and a gap needs `B = 0`, `r = 1`: i.e. the unique highest-weight vector vanishes identically on `D45` (a *global* statement, `q = 1 = a`, which must be PROVED, never sampled) and is nonzero at one actual padding point. In that case geometric separation *is* `D = 1 > 0`, and G5's last sentence ("separation is never reported as `D > 0`") does not apply. For `a >= 2` one equation nonzero on padding gives only `i_det >= 1` and `m_pad >= 1`, never `D > 0`, and the sentence applies in full. Symmetrically (roadmap correction 4): one nonzero determinant evaluation closes a cell (`D <= 0`) only when `a = 1`; for `a >= 2` closure needs a full-rank evaluation matrix, `r_det = a`, or `r_det >= U`.

## 9. Release gates for Phase 2

G1–G4, G6, G7 stand as written in `b18_10_review.md` §7. G5 is replaced by G5′ (§8). Nine gates are added; each names the defect on this record that motivates it.

- **G5′ — Gap claim, generalised.** As §8, conditions 1–4 and the `a = 1` exception.
- **G8 — Portability as data (D3, B19-11).** Every vector, ordering, evaluation point and constant a certificate depends on ships *in* the certificate (or in a hashed definition file it pins), with an ordering hash. A certificate whose meaning depends on the recursion order of an unhashed script, or on a tuple hardcoded in a script, is "replayable from code", not CERTIFIED-portable, and Phase 2 may not consume it until it is. Concretely: `q3_definition.json` and `q7_definition.json` in the `n02_definition.json` format, in a new directory, before B20-01 starts.
- **G9 — Admissible inputs (D5).** A value present only in a chat attachment, a scratchpad, or a session transcript is inadmissible as a premise of a PROVED or CERTIFIED claim; the claim is CONDITIONAL until the value is recomputed into a committed artifact. Literature pinned by hash outside the tree is admissible only with the hash *and* a stated location that a reviewer can reach; if it cannot be reached at review time, the citation is UNREAD.
- **G10 — Receipts (D1, D8).** Run names are unique; a receipt is never overwritten; an aborted start, a cap hit and an unwrapped run each get a receipt or an explicit "no receipt" line in the resource table. Every input a pilot reads is pinned by hash *in the pilot's output*, and a pin that no longer resolves is disclosed as a provenance break at sealing, never repaired.
- **G11 — Sealed trees are inert (D4).** Any process that imports from a sealed packet runs with `PYTHONDONTWRITEBYTECODE=1`; a sealed directory is re-hashed at the end of any session that read it, and any new byte is reported.
- **G12 — Siblings, not children (D6).** A corrigendum, follow-up or clarification is a sibling directory with its own manifest that re-hashes every file of the packet it corrects; it is never created inside a sealed tree.
- **G13 — One symbol, one meaning (D9).** `L` (jet line) and `L` (Levi) may not coexist in one packet; `delta_0` is the det3 quinary-cubic onset and is not used for `D45`; a file is named identically in the manifest and the prose.
- **G14 — Literature labelled at the point of use (Bruns–Herzog, LLV).** Every external theorem that a proof step uses is listed in the packet's literature table and manifest with PRIMARY / SECONDARY / UNREAD and, if PRIMARY, a file name and hash; an UNREAD load-bearing citation makes the claim CONDITIONAL; a verification "against the primary text" names the file and hash it read.
- **G15 — Corrigenda govern and name lines (D7).** Later corrigenda govern; a sealed report is never edited; a withdrawal names every withdrawn sentence by line number, and "withdrawn by type" is not sufficient.
- **G16 — Counts are emitted, not typed (D2).** Any "N/N" in prose is copied from a verifier that prints the total.
- **G17 — Budget fit before launch (B20-02).** A pilot whose dense form exceeds 512 MiB (`D_8`: about 270 MB dense from `2176 x 15504`) is not launched under the default cap; either a sparse plan is pre-approved with its own priced receipt or the candidate is replaced. A cap hit is recorded as a cap hit and is not a mathematical statement.
- **G18 — Single-lineage claims are labelled (B19, post-B19).** Until a second lineage exists, a claim carries "integrator-accepted only" or "producer only"; this review supplies the second lineage for exactly the items in §12 and nothing else.

**Stop gates for Phase 2 (unchanged from the board, restated).** Stop a diagnostic slot when its three wrapped pilots (60 s / 512 MiB, 180 s total) are spent without the named identity certified or refuted; record PAUSED with reopening conditions. Do not describe a necessary-condition result as a gap; do not describe the absence of a gap as the programme's failure.

## 10. B19-05 intake delta

The sealed intake (`dc074191…`) is not edited. The rows below replace or extend it; labels are the intake's (CLOSED-U / CLOSED-P / CLOSED-Z / SCREEN / OPEN) plus **CLOSED-X** for a cell whose `D` is known exactly by two-sided evidence.

**Corrected row (§2.4 of the intake).**

| d | lambda | a | s | T | U | m_det | m_pad | D | closed by | label |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 5 | (4,4,4,4,4) | 1 | 5 | 0 | 0 | **1** | **0** | **-1** | `m_pad = 0`: B18-01 Prop 8.4 (null cone, PROVED; re-derived here); `m_det = 1`: B19-02 §8.1 exact integer at three determinant points, CERTIFIED, and independently CERTIFIED here (pilot 1, ratio 192 at all three points) | **CLOSED-X** |

The degree-five five-row family is fully determined: 22 cells at `D = 0`, one at `D = -1`. The uniform statement "`D <= 0`" (B18-06 review, intake §0 item 2, §2.4, §6 claim 4) is superseded.

**New rows (post-B19), §2.5 / §2.7 of the intake.**

| d | lambda | l | a | s | m_det | m_pad | D | argument | label |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 6 | (8,4,4,4,4) | 5 | 2 (MEASURED, `b18_12_ambient_table.py`) | unknown | `>= 1` | `<= 1` | `<= 0` | `h = c_(4,0,0,0,0)·H5` is a highest-weight vector nonzero on `D45` and zero on `R135` (descent §B.9; premises P1 MEASURED, P2 VERIFIED, P3 PROVED by Pieri) | CLOSED-U (`a` MEASURED, single lineage) |
| 6 | (12,8,2,1,1) | 5 | 1 (census, inherited) | 24 (inherited) | 1 | unknown | `<= 0` | exact 230-term highest-weight vector, zero raising residues over `Z`, nonzero at a determinant point (`extension_descent` §6, producer's own verifier; not replayed) | CLOSED-U (`a` inherited) |
| 6 | (4,4,4,4,4,4) | 6 | 1 | 10 | `<= 1`, unknown | unknown | unknown | band cell: `b = 0` (B19-01 Thm 4.1); arc admits nine dimensions that cannot extend; one detected by `C2` (`extension_descent`); `m_det` not computed | **OPEN** (named, not closed; no gap route through the arc) |
| 3 | (4,2,2,2,2) | 5 | 0 | 2 | — | — | — | ambient-empty mechanism diagnostic (`fiber_compatibility`) | not a cell; record only |

**Regime rows to add to §2.1.**

| regime | statement | argument | label |
|---|---|---|---|
| `l(lambda) = 5`, `d <= 5` | `I(D45)_d = 0`; first five-variable equation has degree `>= 6` | B19-02 Cor 8.1 on 03-A and LLV (LLV PRIMARY, confirmed here §4.3) | PROVED |
| `6 <= l(lambda) <= 10`, `lambda_1+lambda_2+lambda_3 <= 2d` | the boundary arc returns `b = 0`; `B = min(a, s)`; no gap certificate through this arc | B19-01 Thm 4.1 (PROVED; empty for `l <= 5`; `l = 6` only the rectangle `((2d/3)^6)` with `3 \| d`) | SCREEN (bounds no `D`) |

**Screens / routes to add to §2.6 (none bounds `D`; each retires a certificate route with the exact scope shown).**

| route | what it retired | exact scope (verbatim where it matters) | label |
|---|---|---|---|
| 1+3 restriction-to-reducible-pencils bound | as a gap route in every five-row cell with `d <= 6`; `d = 7` given batch-13's measured totals | `u_L = m_pad` whenever `I(D_5)_d = 0`; `d <= 5` producer-certified, `d = 6` certified per weight (the three residue units are length 6), `d = 7` MEASURED (80 uncertified units), `8 <= d < delta_0` open; "polynomials of degree below `delta_0` cannot tell determinantal products from arbitrary products" | PROVED (`d <= 6`) |
| 2+2 partial-transpose fibre family | rank increment over the arc on every `(4k)^5` | "`D_(4k)^5 = 0` on the entire full-stabilizer source"; "Other equal-quartic families are not ruled out"; the `K5` transverse map is a different map | PROVED (modulo the classical `O_4` odd-part rule, pointer unread) |
| Astra five-block weight family | any new source test from block-scalar weights in the fixed `(a, r, c, S, v)` decomposition | `N_w = L_w C` on `M`, `rank(C,T,N) = rank(C,T)`; needs characteristic zero and transposition invariance; "does not cover equations among allowed jets, descent between different parameter points of a limit fiber, special-locus cancellations followed by stronger normalization, anisotropic weights inside a block, or different matrix-coordinate bases" | PROVED |
| Cayley-complex rank-threshold family (`J_k`, first differential; `D_2` at `k = 6, 7`, `N = 16`) | as a source of separating equations | `J_k ⊆ I(Y_det) ∩ I(Y_pad)` for every `k`, `N = 5` and `N = 16`; does **not** cover a minor of size `<= r_det(k)` that happens to vanish on `Y_det`; does **not** establish `D = 0` anywhere; `d_2` at `k >= 8`, `d_j` for `j >= 3`, `d_2` for `N = 5` unassessed | PROVED (Thm A on Gulliksen–Negard SECONDARY; Thm B on Kleiman SECONDARY and Bruns–Herzog UNREAD at `k >= 7`) |
| singular-pencil locus `Z` | as a source of five-row constraints | `rho_Z = 0` in every five-row cell, by a `GL5 x G` one-parameter subgroup; conditional on EH §1 statements (PRIMARY) and on C3 (UNREAD) | PROVED CONDITIONAL (C1, C3) |
| B19-02 counting construction | as a source of the missing equation | cannot fire below degree 320112 in the four-variable control; `r/A` increasing at every computed degree in both `n = 4, 5` | PROVED (on LLV, now PRIMARY) |
| proportional-tops mechanism for `rank(C\|U) = 2` | refuted | `dim Cov = 4`, `N_top = 26`; exact rank 3 at 50 poised points; tangent rank 23 | PROVED |
| arc exactness as a general conjecture | refuted at `(6,(4^6))` | `a = 1, g = 13, s = 10, b = 0`; the length-`<= 5` form remains open | PROVED |

Nothing above nominates a cell; every open five-row cell in the intake still has `s >= a`, hence `B = a` and no headroom, and no cell has a certified `b`.

## 11. Honest negatives

1. **Ballico 1995 remains unread.** Three fetch routes failed (§4.2). C3 is open; every use of the singular-locus Theorem 4.1 stays CONDITIONAL. I did not attempt the literature-free proof of Lemma 3.3; that is producer work.
2. **The EH proofs (§3 of the paper) were not re-verified by anyone**, including me. C1 is PRIMARY at the statement level only.
3. **Layer 4 inputs are recoverable today but uncommitted**, and the EH page images cannot be tied to the committed render script (§2). A scratchpad clean would make the EH transcription unrepeatable from the record; the PDF hash and the public URL would remain.
4. **The scope extraction was performed by a subagent and judged by me**; my judgement covers every sentence it surfaced, not every sentence of every report, and the extraction itself is model output preserved as data.
5. **No independent evaluator was built for any source vector** (`q_3`, `q_7`, `n02`, `e`); pilot 2 is a replay of saved integers. The four-vector independence, the forbidden matrix and `rank T = 3` therefore have a second lineage at the level of "the certificate's arithmetic is right", not "the values are right".
6. **B19-01's `s = 10`, `g = 13` at `(4^6)` and B19-02's `r(d)` table were not recomputed here** (the integrator recomputed them; that lineage is unchanged).
7. **The Levi screen itself (B19-01 §6.3 step 2) is still not evaluated in any five-row cell where it could matter**; its one evaluation (`b_L = 74` at `(4^5)`) is uninformative.
8. **Bruns–Herzog 1.5.12 was not fetched** here either; I only established that it is load-bearing and unlabelled.
9. Nothing here bounds any `m_pad`, produces any `r`, nominates any cell, or claims any gap.

## 12. Closing ledger

Decisions are transcribed from this table only.

| id | statement | label | method | pre-formed? |
|---|---|---|---|---|
| R1 | Layers 0–3 of the committed-artifact chain verify: nine commits with recorded parent, tree, subject and tip; 244/244 + 137/137 path hashes; 565 manifest values resolve; eleven pins resolve; twelve B19 hashes match; local tips as receipted; `origin/*` as post-push; "Batch 20" label free | VERIFIED | REPLAY (hashes) | — |
| R2 | Levi commutation (B19-01 Prop 6.1, Thm 6.2): `C` is `L`-equivariant, `M_lambda ⊆ (S_lambda W)^L`, `b <= dim((S_lambda W)_{<0})^L`; `L` connected, no transposition component | **PROVED** | READ, re-derived | yes (P2) |
| R3 | B19-01's justification of the `|mu| = d` restriction in Thm 6.2's expansion cites Prop 3.1, whose torus `L` does not contain; the restriction holds by the scalar subtorus of `L` (`arc_target` §3.2) | proof gap, conclusion unchanged | READ | yes (P2) |
| R4 | B19-01 Thm 4.1's "forbidden part of `S_lambda W` is zero" means skew degree `> 2d`, not negative `gamma`-weight; `extension_descent`'s precision is endorsed | wording precision | READ | — |
| R5 | The 10,505 count at `d = 7` and the `4.2·10^8` (`424,193,140`) count at `d = 26` are correct raw-triple counts, before containment and LR vanishing; they bound an enumeration, not `b` | **PROVED counts** | INDEPENDENT (hand) + REPLAY (pilot 1) | yes (P1) |
| R6 | `(4^5)`, `d = 5`: `m_det = 1` | **CERTIFIED, two lineages** | INDEPENDENT EVALUATOR (pilot 1) | — |
| R7 | `(4^5)`, `d = 5`: `m_pad = 0` (null cone; B18-01 Prop 8.4) | **PROVED** | READ, re-derived; consistent with pilot 1 | — |
| R8 | `(4^5)`, `d = 5`: `D = -1`; the degree-five five-row family is 22 at `D = 0`, one at `D = -1`; the intake row is corrected (§10) | **PROVED / CERTIFIED** | R6 + R7 | — |
| R9 | The three transverse functionals `C2, C4_{S1,S2}, C4_{S1,S4}` are jointly linearly independent on `M_(4^5)` (`rank T = 3`); ledger `L24`, PRE_AUDIT §4D/§7.5 and the stocktake's "record correction" are wrong and superseded by `L21` | **CERTIFIED** | REPLAY (pilot 2, det 225843) + READ | — |
| R10 | Four source directions `q_3, q_7, e, n02` independent (rank 4 over `Q`); forbidden matrix rank 2 mod one prime with 0 of 364 nonzero `3x3` minors; `(265391, 275398)` residues of a sampled relation | **CERTIFIED (arithmetic replayed)**; relation SAMPLED | REPLAY (pilot 2) | — |
| R11 | Singular-locus Theorem 4.1 (`rho_Z = 0` in every five-row cell): mechanism self-contained; EH enters only through Lemma 3.3; a route-closing theorem, no positive claim rests on it | **PROVED CONDITIONAL on C1 (primary statements, proofs unread) and C3 (unread)**; exposure = a wrongly-closed route | READ | yes (P3) |
| R12 | Ballico 1995: unread by anyone; three fetch attempts here failed; secondary record indicates corroboration of Atkinson, not correction of EH §1 | **UNREAD**; C3 open | attempted | — |
| R13 | LLV arXiv:2303.09028v3: Theorem 2 (five prime divisors, `deg F1 = 320112`, others 136512, 38475, 2508, 320), Cor 3.1, table row `F1 (5,5,5,5)(6,6,6,6)`, Prop 1.1 read in the text extraction of the PDF hashed `67b1701f…` | **PRIMARY; CONDITIONAL lifted; five-component precision confirmed** | READ | — |
| R14 | Refined Bézout: secondary quotation; labels only the upper end `4^49`; untouched by B19 and post-B19 | **SECONDARY, CONDITIONAL stands** | READ | yes (P5) |
| R15 | Gulliksen–Negard, Kleiman: SECONDARY (via the onset note); Dimca, Segal: PRIMARY (hashed), not load-bearing; HMSV Lemma 6.6: POINTER, the fact is the classical `O_n` odd-part rule; Bruns–Herzog 1.5.12: **UNREAD and unlabelled load-bearing pointer** in GKZ Thm B(iii) | as stated | READ | — |
| R16 | D5: of the six values, five are recomputed in committed artifacts (`-12`; `108`, `-14`, `3/896`; `175/36`); only `Ω det Q = 315/4` is chat-only, and it is unconsumed | D5 reduced to one unconsumed constant; general rule = gate G9 | READ (`git grep`) | yes (P4, rule) |
| R17 | D1: confirmed; s1's outputs non-replayable; nothing certified rests on s1 alone | REPORTED (s1 only); no other label moves | REPLAY (hashes) | — |
| R18 | D3: `q_3`, `q_7` orderings exist only as code; L13/L15/L21/L25 replayable-from-code, not portable-as-data; hard prerequisite (G8) before Phase 2 consumes them | CERTIFIED (validity), portability defective | READ | — |
| R19 | D2, D4, D6, D7, D8, D9: no claim moves; dispositions and gates as §6 | recorded | READ | — |
| R20 | Scope hazards (rank direction, actual-padding model, source membership, global vs sampled) hold in every governing document read; one integrator inconsistency (R9) | holds | READ | — |
| R21 | New cell-level bounds since the intake: `(6,(8,4,4,4,4))` `D <= 0`; `(6,(12,8,2,1,1))` `i_det = 0`; `(6,(4^6))` named OPEN; eight routes retired with exact scope (§10) | as tabulated | READ | — |
| R22 | G5 generalisation: **ACCEPTED as G5′** with conditions 1–4 and the `a = 1` separation exception | ruling | — | — |
| R23 | Release gates G1–G4, G6, G7 stand; G5′ replaces G5; G8–G18 added (§9) | ruling | — | — |
| R24 | Two wrapped pilots run (1.07 s, 0.08 s; peaks 12.96 MB, 12.69 MB; exit 0, 0); no cap hit; no failure; no lease; no cell nominated; no gap claimed | MEASURED | — | — |
| R25 | Layer 4: EH scan, page images, Segal, Dimca, the two transverse attachments, the interpreter, the wrapper and the LLV PDF all present on disk with matching hashes; none committed; page images unpinned and not tied to the committed render script; `b15_bound.py` pinned as CRLF bytes (LF blob `1f73ad8d…`); descent REPORT line 22 cites a non-existent §A.4 | RECOVERABLE TODAY; three provenance notes | REPLAY (hashes) + READ | — |
| R26 | Wording slips W1–W5 (§7) and parent-GKZ lines 15, 90 recorded; none changes a label; not to be quoted forward | wording | READ | — |

**Status: COMPLETE.** Phase 2 may open on this report with G8 (the `q_3`/`q_7` definition certificates) as the one hard prerequisite for B20-01 and G17 as the one hard prerequisite for B20-02.

## 13. Resources, footprint and manifest

| run | wrapper | exit | wall | peak Job memory | receipt |
|---|---|---|---|---|---|
| `b20_10_p1_independent_invariant` | `B15-02/analysis/b15_bound.py --seconds 60 --memory-mb 512`, interpreter `B15-02/.venv/python.exe` 3.12.10 (`4d6f5f81…`), `job_object_enforced: true` | 0 | 1.07 s | 12,963,840 B | `results/b20_10/b20_10_p1_independent_invariant_resources.json` |
| `b20_10_p2_spot_replay_certificates` | same | 0 | 0.08 s | 12,693,504 B | `results/b20_10/b20_10_p2_spot_replay_certificates_resources.json` |
| `verify_layers.py` (hash replay) | unwrapped, read-only git | 0 | 16 s | not measured | `results/b20_10/verify_layers_out.json` |
| Ballico fetch attempts (3) | network, read-only | failed | — | — | §4.2; the HTML received in place of `b36h1bal.ps.gz` is not kept |

Two of three wrapped pilots used, 1.15 s of 180 s. No retry. No third pilot.

Write footprint (all new, nothing modified): `docs/b20_10_review.md`, `analysis/b20_10_p1_independent_invariant.py`, `analysis/b20_10_p2_spot_replay_certificates.py`, `results/b20_10/` (this manifest's file list), `results/logs/b20_10_p1_*`, `results/logs/b20_10_p2_*`. `results/b20_10/MANIFEST.json` binds every file with sha256; it was written after this document was finalised, and this document does not name its own hash.

No sealed report, manifest or packet was edited. No git command beyond `rev-parse`, `status --porcelain`, `log`, `show`, `ls-tree`, `grep`, `cat-file`, `for-each-ref` was run.
