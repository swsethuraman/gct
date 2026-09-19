# CLAIMS — *Why multiplicity obstructions are blind at five rows* (draft `det4-blindness.tex`)

Slot B23-04 (writing only; no computation). Worktree `work/batch15_workers/B23-04`, branch
`b23-04-paper3`, HEAD `82633a60893236fab4fbc317df416e1b8a349005`; `git status --porcelain` was
empty before the first write (recorded 2026-09-18).

**Check this table against the packets, not against the prose (G26).** Every numbered result in
the draft carries a bracketed ID `C01`–`C46` in its heading. Each ID has exactly one row here. A
result without a row is a defect.

**How to read a row.**
- **label** is the record's own label, copied. It is never upgraded. `CERTIFIED-modular` is never
  shortened to `CERTIFIED`, and `ADOPTED` never becomes `PROVED`.
- **source** names the packet and section, and **commit** is where those bytes are committed.
  Most packets are *not* on this branch. Read them with `git show <commit>:<path>`. Paths under
  `docs/` without a batch prefix, and everything under `docs/post_b19_20260917/`, are committed at
  `82633a60` (this branch's HEAD).
- **lineage** is `producer only`, `integrator` (the integrator review lineage only), or a reviewer
  slot with its method: READ, REPLAY, INDEPENDENT EVALUATOR, INDEPENDENT (hand).

Packet paths at their commits:

| short name | path | commit |
|---|---|---|
| B18-01 | `docs/b18_01_report.md` | `ea045cef` |
| B19-01 | `docs/b19_01_report.md` | `6b161513` |
| B19-02 | `docs/b19_02_report.md` | `75ddb900` |
| B19-12 | `docs/b19_12_ledger.md` | `f008ac39` |
| B20-01 | `docs/b20_01_report.md` | `878258f2` |
| B20-02, B20-02b | `docs/b20_02_report.md`, `docs/b20_02b_report.md` | `7de65d7c` |
| B20-10 | `docs/b20_10_review.md` | `6915ae6f` |
| B20-12 | `docs/b20_12_ledger.md` | `da803892` (later edits at `8b6be856`, `16f2392e`) |
| B21-01 | `docs/b21_01_report.md` | `d5e9d885` |
| B21-10 | `docs/b21_10_review.md` | `f7727cb7` |
| B21-12 | `docs/b21_12_ledger.md` | `8b6be856` |
| B22-01 | `docs/b22_01_report.md` | `53bdb31e` |
| B22-02 | `docs/b22_02_report.md` | `e22a41b1` |
| B22-10 | `docs/b22_10_review.md` | `2efb7aaf` |
| B22-12 | `docs/b22_12_ledger.md` | `16f2392e` (first version `bc93a2c5`) |
| GKZ | `docs/post_b19_20260917/claude_gkz_incidence_20260917/REPORT.md` and `scope_corrigendum/{CORRIGENDUM,REVISED_VERDICT,CLAIM_SCOPE_TABLE}.md` | `82633a60` |
| Astra | `docs/post_b19_20260917/astra_gkz_degenerations_20260917/REPORT.md` | `82633a60` |
| SingLoc | `docs/post_b19_20260917/claude_singular_locus_audit_20260916/REPORT.md` | `82633a60` |
| onset | `docs/onset_conjecture.md` | `82633a60` |
| obstr | `docs/obstruction_power.md` | `82633a60` |
| washout | `docs/washout_lemma.md` | `82633a60` |
| PROVED | `docs/PROVED.md` | `82633a60` |
| s73 | `docs/s73_report.md` | `82633a60` |
| stock11 | `docs/stocktake_batch11.md` | `82633a60` |
| plan11 | `docs/batch11_plan.md` | `82633a60` |
| corr13 | `docs/batch13_corrections.md` | `82633a60` |

## Unnumbered standing rule

| where | statement | label | source | commit | lineage |
|---|---|---|---|---|---|
| §1.2 | The four achievements (necessary source condition; coefficient equation; separation on padding; positive multiplicity gap) are distinct and never conflated. "No five-row determinant equation **known** to be nonzero on padding", never "none known". | standing rule | B20-12 §1; B22-02 §0; B22-01 §0; GKZ REVISED_VERDICT "Reconciliation" | `da803892`; `e22a41b1`; `53bdb31e`; `82633a60` | integrator rule, restated by every B20–B22 packet |

## Numbered results

| ID | draft | statement (short) | record label | source | commit | lineage |
|---|---|---|---|---|---|---|
| C01 | Prop. 2.1 | `dim D45 = 50` affine (`dim P(D45) = 49`); `dim P5 = 39` (affine, as recorded) | PROVED; certificate CERTIFIED | B18-01 Prop. 3.2; B19-12 F1; B22-10 pilot-2 sanity row (§7) | `ea045cef`; `f008ac39`; `2efb7aaf` | two lineages: B18 slot 10 (replay at two points) + integrator (own reimplementation). Affine convention of 39: see GAPS G-24 |
| C02 | Record 2.2 | `P5 = R135` at five rows; for `L >= 6`, `dim P_L = 10L − 5`, strictly inside all linear×cubic; a product evaluation above five variables is not a padding certificate | `P5 = R135` ADOPTED; the `L >= 6` part MEASURED and PROVED | B22-02 §0 (citing B18-10 §9); B19-12 F7 | `e22a41b1`; `f008ac39` | two lineages (B18 slot 10 + integrator). Convention of `10L−5` not stated at source (G-24) |
| C03 | Prop. 2.3 | `dim D35 = 29` affine (28 proj.); `dim{l·C : C ∈ D35} = 33` affine (32 proj.); the record's bare "32" is the projective count | dimensions CERTIFIED in the safe direction (S23); "slip corrected" (S24) | B22-10 §7, S23–S24 | `2efb7aaf` | reviewer B22-10 (INDEPENDENT EVALUATOR, pilot 2), correcting producer B22-02 |
| C04 | Lemma 2.4 | Deficit decomposition `mult_B − mult_A = [m_B − m_A] − [def_B − def_A]`; containment ⇒ surjection ⇒ `mult_A >= mult_B` | PROVED (producer's label; elementary) | obstr §1, Lemma 1 and (SUR) | `82633a60` | producer only (session 24); no reviewer row located (G-14) |
| C05 | Ruling 2.5 | G5′: `r > B` gives `D > 0`; the `a = 1` separation exception; one det evaluation closes a cell only when `a = 1` | ruling (G5′ ACCEPTED) | B20-10 §8, R22 | `6915ae6f` | reviewer B20-10 |
| C06 | Thm. 3.1 | A five-variable separator `h` with `deg h <= δ45 <= 4^49` exists; some five-row cell has a det equation failing on padding | PROVED, CONDITIONAL on refined Bézout (Fulton, SECONDARY) | B18-01 Thm. 3.5; B19-12 F2; B20-10 R14 | `ea045cef`; `f008ac39`; `6915ae6f` | two lineages (B18 slot 10 ACCEPTED; integrator ACCEPT conditional); B20-10: SECONDARY, CONDITIONAL stands |
| C07 | Remark 3.2 | `4^49` is an existence statement, not a budget; refined Bézout overshoots the four-variable truth (320112) by ~15 orders of magnitude | MEASURED | B19-12 F3 | `f008ac39` | two lineages (B18 slot 10 calibration; integrator) |
| C08 | Cor. 3.3 | `I(D45)_d = 0` for `d <= 5`; first five-variable equation has degree `>= 6`; bracket `6 <= d_5 <= 4^49` | PROVED, on premise 03-A (B17-03 Lemma 2) and LLV (PRIMARY) | B19-02 Cor. 8.1, §8.1; B20-10 §10 regime row, R13 | `75ddb900`; `6915ae6f` | producer B19-02; integrator review; B20-10 (READ; LLV confirmed from primary text) |
| C09 | Record 3.4 | The 22 non-rectangular degree-5 five-row cells are EXCLUDED at `D = 0` (`m_det = a = 1` by exact nonzero det evaluation; `m_pad >= 1` at an actual padding point) | EXCLUDED, integrator-accepted | B19-12 F10–F11, §4b; B20-10 R8 (family sentence) | `f008ac39`; `6915ae6f` | single review lineage (B18-06 producer + integrator review). B20-10 R8's method column (R6 + R7) covers only `(4^5)` (G-19) |
| C10 | Thm. 3.5 | `(5,(4^5))`: `m_det = 1`, `m_pad = 0`, `D = −1` | `m_det = 1` CERTIFIED (two lineages); `m_pad = 0` PROVED; `D = −1` PROVED/CERTIFIED | B20-10 R6–R8, §3.3, §10; B19-02 §8.1; B18-01 Prop. 8.4 | `6915ae6f`; `75ddb900`; `ea045cef` | producer B19-02 (exact values at 3 det points); reviewer B20-10 (INDEPENDENT EVALUATOR, ratio 192 at all three; padding leg re-derived) |
| C11 | Thm. 3.6 | Cap theorem: size-`cap(n) = 5n(n−1)²(7n−8)/12` minors of `M_{3n−5}` lie in `I(D_5^{det_n})`, not all zero; degree-300 `det_4` equations at `n = 4` | ADOPTED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), Gulliksen–Negård (SECONDARY). Source wording "proved modulo …, all adopted" | onset §0, Thm. 1; B22-12 §3 | `82633a60`; `16f2392e` | producer (session 40); the `n = 3` instance used in C34 re-derived by B22-10 S18 (Dimca Thm. 3.1 + general position) |
| C12 | Record 3.7 | `δ_0` = onset `I(D35)` (det3 quinary cubics), never `I(D45)`; `6 <= δ_0 <= 65` unconditionally, `8 <= δ_0 <= 65` given the batch-13 measured total-deficit identity | ADOPTED record-internal; source "paper 1" UNREAD per ledger | GKZ corrigendum C10; B22-12 §3 | `82633a60`; `16f2392e` | producer (corrigendum session); integrator ledger |
| C13 | Lemma 4.1 | Semicontinuity form: separation needs an l.s.c. statistic larger on padding or a u.s.c. statistic smaller on padding | PROVED (from definitions) | B22-02 §1.1, L1 | `e22a41b1` | producer only. B22-10 did not rule on §1.1 separately; it calls the step "padding more singular ⇒ larger Milnor algebra" at `N = 6..8` plausible and unproved (S19) |
| C14 | Lemma 4.2 | A polynomial nonzero at one point is nonzero on a dense open set | PROVED | B22-02 Lemma 1.2 (L2) | `e22a41b1` | producer B22-02; reviewer B22-10 S17 (READ) |
| C15 | Lemma 4.3 | Kernel covariants: polynomials in the `r × r` minors vanish where rank `< r`; instance `M_7`: 244 (padding) vs 299 (P2 pencil) | PROVED, scope caveat (kernel extracted via minors only); instance ranks CERTIFIED exact | B22-02 Lemma 1.3 (L3); B20-02 §7.3 | `e22a41b1`; `7de65d7c` | producer B22-02; reviewer B22-10 S17 (READ; caveat pre-formed) |
| C16 | Lemma 4.4 | `l·C` is `SL_5`-unstable: all positive-degree `SL_5`-invariants vanish on `P5`; `l`-divisibility of covariants; `GL_5`-covariants into cubics send `P5` into `D35` | PROVED (Hilbert–Mumford weight count; plethysm row bound UNREAD-CLASSICAL); (c) scoped to `GL_5`-covariants | B22-02 Lemma 1.4 (L4) | `e22a41b1` | producer B22-02; reviewer B22-10 S17 (READ, re-derived), §6 row 13 |
| C17 | Fact 4.5 | `Δ_{l·C} ≡ 0`, `Δ_F ≠ 0` generically on `D45`; ordinary `Disc(F)` vanishes on both | PROVED (Bertini UNREAD-CLASSICAL); `Disc(F)` trivial PROVED-kill / Excluded (theorem) | B22-02 Fact 1.7 (L7); B22-10 S20; GKZ CLAIM_SCOPE_TABLE row 1 | `e22a41b1`; `2efb7aaf`; `82633a60` | producer B22-02; reviewer B22-10 S17 (READ, re-derived), S20 |
| C18 | Thm. 4.6 | GKZ Theorem B (`N = 5`): `r_P5(k) <= r_D45(k)` ∀k; `J_k ⊆ I(D45) ∩ I(P5)`; scope = rank-threshold ideals, not individual minors of size `<= r_det(k)` | PROVED; Kleiman SECONDARY (`k >= 7`); exact P2 ranks (`k <= 6`); BH 1.5.12 UNREAD-CLASSICAL (fact proved by B21-10) | GKZ REPORT; corrigendum C1–C4; REVISED_VERDICT | `82633a60` | producer (GKZ session) + corrigendum; B20-10 R15, R21 (READ); B21-10 R16 (fact proved), R19 (profile replayed) |
| C19 | Thm. 4.7 | GKZ Theorem A (`N = 16`): `rank M_k(z per_3) <= rank M_k(det_4)` ∀k; `J_k ⊆ I(Y_det) ∩ I(Y_pad)`; same scope restriction | PROVED; Gulliksen–Negård SECONDARY; P1 certificates exact | GKZ REPORT §3.B; corrigendum C1 | `82633a60` | producer + corrigendum; B20-10 R15, R21 (READ) |
| C20 | Thm. 4.8 | B20-02 Thm. 6.4: in five variables, `r^{(j)}_{D45}(k) = ρ_j(k)` ∀ `j >= 2`, ∀k; rank-threshold ideals of higher differentials on `D45` are zero | PROVED CONDITIONAL on (T2) BH Cor. 2.1.4 (UNREAD-CLASSICAL); (T1) LIFTED by B21-10. Unconditional certificate `j = 2,3,4`, `k = 3..12` (exact `k <= 8`; single-prime floors `k = 9..12`) | B20-02 Thm. 6.4, L6–L7; B21-10 R12–R15, R19 | `7de65d7c`; `f7727cb7` | producer B20-02; reviewer B21-10 (Lemma 6.3 PROVED by INDEPENDENT hand + REPLAY; T1 lifted by INDEPENDENT proof). L7 certificate producer only |
| C21 | Cor. 4.9 | No `d_2` reversal in five variables: `rank d_j^{(k)}(F') <= ρ_j(k) = r^{(j)}_{D45}(k)`; padding-side data `146 < 150` at `k = 8` (exact), floors at `k = 9, 10` | PROVED given C20 (L8); "strictly more homology" sentence CONDITIONAL on the unlifted nonvanishing half of (T1); padding data CERTIFIED (`k = 8`) / MEASURED (`k = 9, 10`) | B20-02 Cor. 6.5, L8–L9; B21-10 R14 | `7de65d7c`; `f7727cb7` | producer only; B21-10 ruled on the condition only |
| C22 | Thm. 4.10 | `N = 16`, `d_2`: `k = 6`: 120/105; `k = 7`: 1904 (of 1920)/1650; `k = 8`: 15660/13490, `ρ_2(8) = 16320`; no reversal at `(16,2,7)`, `(16,2,8)`; size-1905 and size-15661 minor ideals in the common ideal | ranks CERTIFIED exact over `Q`; containments PROVED given ranks. Scope `j = 2`, `k = 6,7,8` only | GKZ corrigendum C5, C7 (P3); B20-02b L3–L5, §4 | `82633a60`; `7de65d7c` | producers (GKZ; B20-02b); B21-10 R19–R20 (sizes/homology consistency REPLAYED; scope READ; ranks not recomputed) |
| C23 | Ruling 4.11 | Rank-threshold kills PROVED for `d_1` at `N = 5, 16`, `d_j (j >= 2)` at `N = 5`, `j = 2, k = 7, 8` at `N = 16`; ASSESSED only at `N = 6, 7, 8` and for `j >= 3` / `k >= 9` at `N = 16`; Thm. 6.4's mechanism fails at `N = 6` | ruling; labels corrected | B22-10 §6, S19, S21; B22-12 §4 correction 1 | `2efb7aaf`; `16f2392e` | reviewer B22-10 (READ); integrator withdrew "any `d_j`" |
| C24 | Thm. 4.12 | Astra Thms. 8.1, 8.2, Cor. 8.3: `N_w = L_w C` on `M`; `rank(C,T,N) = rank(C,T)`; hypotheses; **verbatim scope limit quoted in the draft** | PROVED | Astra REPORT §1, §8; GKZ corrigendum C12 | `82633a60` | producer (Astra); recorded, not replayed (GKZ corrigendum); tabulated by B20-10 §10 (R21, READ). No reviewer re-derivation on record (G-23) |
| C25 | Thm. 4.13 | Counting criterion cannot fire below 320112 in the four-variable control; `r/A` rises at every computed degree, `n = 4, 5` (75.8 at `d = 12`) | bound PROVED (on LLV, PRIMARY); ratios MEASURED; five-variable extrapolation HEURISTIC (Claim 6.2) | B19-02 §§4–6; B20-10 §10 route row, R13 | `75ddb900`; `6915ae6f` | producer B19-02; integrator review; B20-10 (READ) |
| C26 | Thm. 4.14 | Silence theorem: `λ1+λ2+λ3 <= 2d` ⇒ forbidden part zero, `b = 0`, `B = min(a, s)`; band empty for `ℓ <= 5`, rectangle at `ℓ = 6` (`3 \| d`), band for `7 <= ℓ <= 16` | PROVED | B19-01 Thm. 4.1, Prop. 4.4 | `6b161513` | producer B19-01; integrator review; B20-10 finding S3 (READ) |
| C27 | Thm. 4.15 | Arc exactness refuted at `(6,(4^6))`: `a = 1, g = 13, s = 10, b = 0`; defect `>= 9`; length-`<= 5` form OPEN | PROVED, given the MEASURED `a, g, s` | B19-01 Thm. 5.1; B20-10 §10 route row | `6b161513`; `6915ae6f` | producer B19-01; integrator (recomputed `a, s`); B20-10 (READ; `s, g` not recomputed, honest negative 6) |
| C28 | Thm. 4.16 | `ρ_Z = 0` in every five-row cell (singular-pencil locus invisible); route-closing only | PROVED CONDITIONAL on C1 (EH statements PRIMARY, proofs unread) and C3 (Ballico 1995 UNREAD-SPECIALIST) | SingLoc Thm. 4.1; B20-10 R11–R12 | `82633a60`; `6915ae6f` | producer (singular-locus audit); reviewer B20-10 (READ, pre-formed) |
| C29 | Record 4.17 | Class 68 (20-nodal) vs 24 (`l·C`): l.s.c., drops on padding; dual dimension: hypersurfaces at `N = 5`, first bites at `N = 9`; LMR at `N = 16` | class: PROVED-kill given the two class values (Teissier SECONDARY/UNREAD, illustrative); dual dimension: PROVED-kill | B22-02 §1.3 rows 4–5, L9; B20-02 §4 | `e22a41b1`; `7de65d7c` | producer B22-02; reviewer B22-10 §6 rows 4–5 (READ, arithmetic checked) |
| C30 | Table 1 | The thirteen candidates with killing sentences and labels (rows 1–2 corrected); plus `Disc(F)`, Severi closure, two non-candidates; outcome (3) honest negative | per-row labels as in the table; gate met; outcome (3) confirmed | B22-02 §1.3, §5; B22-10 §6, S19–S21; B22-12 §8.2b, §8.4 | `e22a41b1`; `2efb7aaf`; `16f2392e` | producer B22-02; reviewer B22-10 (READ; rows 1–2 corrected, 3–13 affirmed; row 3's ">300" to read "conjecturally") |
| C31 | Lemma 5.1 | Window: rank-6 second fundamental form bound (right-way) and rank-36 catalecticant bound (reversed) both vacuous iff `N <= 8` | PROVED (self-contained; LMR UNREAD-SPECIALIST, not load-bearing) | B22-02 Lemma 1.5 (L5) | `e22a41b1` | producer B22-02; reviewer B22-10 S17 (INDEPENDENT hand: 6 and 36 replayed) |
| C32 | Record 5.2 | For `ℓ(λ) <= 5`, `m_pad = m_{R_ℓ}` (`D_k^{per_3} = Sym^3 C^k`, `k <= 5`); `per_3` does not appear below length 6 | PROVED | washout §0, Thm. 2; PROVED `washout_thm2`, `restriction_lemma` | `82633a60` | producer (session 37); re-derived by B13-07 (per PROVED.md) |
| C33 | Record 5.3 | `I(D_r^{per_3})_δ = 0` ∀r, `δ <= 8`; `m_pad = m_red` at every weight, degree `<= 8` | PROVED (reconciliation result) | PROVED `degree8_global` | `82633a60` | integrator reconciliation of several batch-13 producers; component counts reproduced by several sessions |
| C34 | Lemma 6.1 | Restriction to the cubic factor: separating `f` restricts to nonzero element of `I(D35)_d`; `d >= δ_0`; right-way clause: size-65 cap minors vanish on `D35`, nonzero at smooth cubics | containment/restriction PROVED; right-way clause CONDITIONAL on the cap theorem at `n = 3` (ADOPTED); `δ_0 >= 8` ADOPTED (given batch-13 identity) | B22-02 Lemma 1.6 (L6); B22-10 S18 | `e22a41b1`; `2efb7aaf` | producer B22-02; reviewer B22-10 (READ + INDEPENDENT hand; MEASURED ranks 64/64/65 at single points) |
| C35 | Prop. 6.2 | `D45 ∩ P5 ⊇ {l·C : C ∈ D35}`, strictly: `(2,1)`-compression matrix gives `l·C` for generically any cubic through a plane; dim `>= 35` vs exactly 33 (affine) | `⊇` PROVED; strictness PROVED (dims CERTIFIED safe direction) | B22-10 §7, S22–S23; B22-12 §3 | `2efb7aaf`; `16f2392e` | reviewer B22-10 (INDEPENDENT hand + INDEPENDENT EVALUATOR) |
| C36 | Record 6.3 | Two known families in `D45 ∩ P5`; classification OPEN; nothing more said | OPEN | B22-10 S25, honest negative 6; B22-12 §3 | `2efb7aaf`; `16f2392e` | reviewer B22-10; integrator. Slot B23-03 in flight (G-3) |
| C37 | Remark 6.4 | Separating `f` restricts to `I(D35 ∪ {cubics ⊃ plane})`; degree bound unaffected; vanishing of cap minors on the plane family OPEN (single-point MEASURED evidence only) | strengthening PROVED (S18); vanishing OPEN | B22-10 S18; B22-12 §4 correction 2 | `2efb7aaf`; `16f2392e` | reviewer B22-10; integrator (flagged observation). See G-17 |
| C38 | Record 7.1 | `(4^5)`: `a = 1`, `s = 5`; `q_3, q_7, e, n02` rank 4 over `Q`; fifth direction not found | `s = 5` as recorded in the corrected intake row; rank 4 CERTIFIED (arithmetic replayed); fifth direction OPEN | B20-10 §10 corrected row, R10; B20-12 §4 | `6915ae6f`; `da803892` | producer (routeA); reviewer B20-10 (REPLAY; no independent evaluator for any source vector) |
| C39 | Thm. 7.2 | `rank T = 3`: `C2, C4_{S1,S2}, C4_{S1,S4}` jointly independent on `M_(4^5)` (det 225843); "not established" line STRUCK | CERTIFIED, two lineages | B20-10 R9, §3.4; B20-12 §1, §8.4 | `6915ae6f`; `da803892` | producer (routeA); reviewer B20-10 (REPLAY, pilot 2) |
| C40 | Thm. 7.3 | Theorem A: reduction to `F_1` on the flag locus; 15 evaluations per functional; control passes with `det(g)^{-4}` | PROVED; control PASSES, corrected | B20-01 §4.2; B21-10 R2–R7 | `878258f2`; `f7727cb7` | producer B20-01; reviewer B21-10 (READ, re-derived, pre-formed; INDEPENDENT EVALUATOR for the control) |
| C41 | Thm. 7.4 | Prop. C (target = 70-dim `F^L_{-1}`); Theorem M (i)–(iv): typed patterns in and spanning `F^L_{-1}`, `F^L_{-2}`; 70 + 4 bases; 70 injective points over `Q` and `F_P`; det 132757, top minor 136525; `b_L(11) = 70`, `b_L(12) = 4` two lineages | Prop. C PROVED; Theorem M PROVED; certificate CERTIFIED (replayed); classical inputs UNREAD-CLASSICAL | B20-01 §4.4; B21-10 R8; B22-01 §2, B22-01.3–.8; B22-10 S2–S7 | `878258f2`; `f7727cb7`; `53bdb31e`; `2efb7aaf` | producer B22-01; reviewer B22-10 (READ + INDEPENDENT EVALUATOR for `b_L`; REPLAY of the certificate) |
| C42 | Thm. 7.5 | Five-row mixed-pairing identity holds mod `P = 524287` as a polynomial identity; `rank(C\|_U ⊗ F_P) = 2`; over `Q` OPEN (rank 3 not excluded; would require `P` to divide every 3×3 minor of the exact rows) | **CERTIFIED-modular** (identity); **OPEN** (`Q` form) | B22-01 §4.3, B22-01.14–.15; B22-10 S8, S10–S11 | `53bdb31e`; `2efb7aaf` | producer B22-01; reviewer B22-10 (REPLAY of decisive rows; span control vs original sources). Slot B23-01 in flight (G-1) |
| C43 | Thm. 7.6 | Prop. 7.1: `F_P` form `n̄ ∈ ker(C ⊗ F_P)`, `C2(n̄) = 0`, `C4(n̄) = 499917, 487898`; `Q` form: exact lift `n*` with `C4(n*) ≠ 0` | `F_P` form PROVED (values REPLAYED); `Q` form CONDITIONAL on `rank(C\|_U) = 2` over `Q` | B22-01 B22-01.16–.17; B22-10 S12–S13 | `53bdb31e`; `2efb7aaf` | producer B22-01; reviewer B22-10 (REPLAY, pilot 3; pencil values not recomputed) |
| C44 | Remark 7.7 | The example is a necessary source condition in a `D = −1` cell; cheap mechanisms closed: relabelling sign (conditional on height-2000 search), slice density (floor 55,440 = 792×), isotropic type | standing (B22-01.18); density PROVED-with-correction; isotropic type: mechanism closed, producer only | B22-01 §0; B21-10 R10; B21-01; B21-12 §8.4, §10; B20-12 §8.7 (C6) | `53bdb31e`; `f7727cb7`; `d5e9d885`; `8b6be856`; `da803892` | mixed: B21-10 reviewed the density floor; B21-01 producer only (five points, one prime); C6 producer only |
| C45 | Thm. 8.1 | `n = 3` unpadded ladder `(3δ−17, 7, 2^5)`: `a = 0,2,4,5` at `δ = 8..11`, `a = 6` for `δ >= 12`; `D = +1` ∀ `δ >= 12`, `D = 0` at 9–11; base rung `m_per = 6 > 5 = m_det` | PROVED (record: "a theorem, not a measurement"; Prop. S + Lemma L); rungs 12–16 MEASURED at two primes; `i_per = 0` proved over `Q`; base `i_det(12) >= 1` from LMR (read-status for this use not on record, G-15) | s73 §0, §4; stock11 §4; plan11 §1.1 | `82633a60` | producer (s73; P0-A, s62, s63 for the base rung); integrator stocktake (46/46 certificates PASS; `a` reproduced at `δ = 12..18, 20`). No independent reviewer slot |
| C46 | Record 8.2 | Padded `n = 3` control degenerate: `l·per_2` has five essential variables, `m_pad = 0` at seven-row weights, `i_pad = a`, padded gap −5 | PROVED | PROVED `n3_padded_seven_row`; corr13 §5 | `82633a60` | producer B13-11; integrator correction accepted |

## Cross-checks a reviewer should run

1. Every `\cid{Cnn}` in `det4-blindness.tex` appears once as a heading (46 IDs, `C01`–`C46`, no gaps).
   Checked statically by this slot. The draft was **not compiled** (GAPS P-1).
2. For each row, `git show <commit>:<path>` and search the cited section for the label word. The
   draft copies the label and never strengthens it.
3. Specific traps (G26 corollaries), each checked in the draft:
   - `CERTIFIED-modular` appears only for C42 and is never shortened.
   - `ADOPTED` for the cap theorem (C11) is never written `PROVED`, and the source's "proved
     modulo" wording is quoted as the source's own.
   - Every CONDITIONAL row carries its condition in the same provenance line: C06, C08, C20, C21,
     C28, C34, C43.
   - `(4^5)` at `d = 5` is `D = −1` (C10). `δ_0` is a cubic onset (C12). `rank T = 3` is
     CERTIFIED (C39).
   - Every dimension says affine or projective (C01, C03, C35; exceptions logged in G-24).
   - The rank-threshold kills are scoped to `N = 5` and the stated `N = 16` gradings (C18–C23, C30).
