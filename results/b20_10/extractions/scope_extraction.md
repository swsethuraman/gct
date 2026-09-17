# Extraction report — post-B19 archive at 82633a60 (read-only; no files modified)

Conventions. `PB` = `docs/post_b19_20260917`. Line numbers are 1-based `cat -n` lines of `git show 82633a60:<path>`. Quotes are verbatim, trimmed with `…` to ≤ 350 chars; a `¦` inside a quote replaces a literal `|` (table cell). Tags are mine; no verdicts. Packet abbreviations: GKZ = `claude_gkz_incidence_20260917`; SC = its `scope_corrigendum`; IC = `claude_image_ceiling_20260916`; SL = `claude_singular_locus_audit_20260916`; TS = `claude_transverse_structure_20260916`; TF = `claude_transverse_structure_20260916_followup`; CL = `TF/clarification_20260917`; SV = `claude_source_vectors_20260917`; RA = `SV/routeA_signfilter_20260917`; AT = `SV/arc_target_dimension_followup`; DA = `SV/direct_arc_relation_followup`; FA = `SV/final_arc_diagnostic`; DF = `descent_followup_claude_20260916`; DFA = `descent_followup_claude_20260916_addendum`; ED = `extension_descent_20260916`; FC = `fiber_compatibility_20260916`; AS = `astra_gkz_degenerations_20260917`.

Governing documents read first: `PB/ARCHIVE_NOTE.md`; SC `CORRIGENDUM.md`, `REVISED_VERDICT.md`, `CLAIM_SCOPE_TABLE.md`; TF `CORRIGENDUM.md` (K1–K9); CL `CORRIGENDUM.md` (L1–L6), `STABILIZER.md`, `SOURCE_HANDOFF.md`; FA `CURRENT_DIAGNOSTIC_STATE.md`; AT `CORRIGENDUM.md` (C1–C4); DA `CORRIGENDUM.md` (C1–C3); DFA `CORRIGENDUM.md` (A–F). Then every REPORT.md, PREREG/PREFLIGHT/FEASIBILITY, section drafts, `b_L_tables.md`, and the TS `drafts/REPORT_body_draft.md`; grep passes over all `.json/.py/.ps1/.log` files for the listed patterns (only hits with prose content are listed).

---

## A. RANK DIRECTION (bounds stated from one side; places consumed from the other side)

| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/DF/REPORT.md@82633a60:86-88` | "A nonzero `4 x 4` minor of the stacked forbidden rows certifies `rank C >= 4`. Since the extendable line `H5 ∘ phi` lies in `ker C`, `rank C <= 4`; so `rank C = 4` and the old arc is exact in this cell." | floor+ceiling→value |
| `PB/DF/REPORT.md@82633a60:342-344` | "Rank of the six rows: **2**. So `rank C >= 2` over `Q` (characteristic-zero floor from a nonzero modular `2 x 2` minor of actual forbidden coefficients), and `C` is injective on `span(q_3, q_7)`: **no arc-kernel vector lies in the certified subspace.**" | floor-consumed-as-injectivity |
| `PB/DF/REPORT.md@82633a60:352-353` | "Needed `rank C >= 4`; certified `rank C >= 2`. Upper bound `rank C <= 4` holds (`E = span(H5 ∘ phi) subset ker C`, `m_det = 1`)." | floor-and-ceiling-stated |
| `PB/DF/REPORT.md@82633a60:236-241` | "So `m_det(6,(8,4^4)) >= 1`. … `h` vanishes on `R135 = closure{l·C}` by (P3), so `i_pad >= 1` and `m_pad <= a - 1 = 1`. Hence `D = m_pad - m_det <= 1 - 1 = 0`." | i_pad-floor-consumed-as-m_pad-ceiling |
| `PB/DF/REPORT.md@82633a60:210` | "`m_det <= min(a, s - rho_L + u_L)`. Any certified floor `rho_0 <= rho_L` and any certified ceiling `u_0 >= u_L` give a valid bound." | direction-stated |
| `PB/DF/REPORT.md@82633a60:211` | "With `u_0 = U`: `min(a, s - rho_0 + U) >= U >= r` for every padding floor `r`, since `rho_0 <= s` and `U <= a`. **This version can never yield a gap.**" | ceiling-U-used-as-floor-on-bound |
| `PB/DF/REPORT.md@82633a60:217` | "With `s = 10, a = 1, u_0 = 1` the clipped bound is `min(1, 11 - rho_0) = 1` for every `rho_0 <= 10`; sampled rank zero cannot prove `rho_L = 0`" | direction-stated |
| `PB/DF/REPORT.md@82633a60:135-136` | "**Increment.** `rank[C; C2] = 0 + 1`. One false survivor removed; clipped bound stays `min(1, 9) = 1`." | rank-sum |
| `PB/DF/REPORT.md@82633a60:347-348` | "`C2` row `(456851, 3402)`, rank 1; stacked `[C; C2]` rank 2. On this subspace the increment is zero, as it must be where `C` is already injective." | floor-consumed |
| `PB/DFA/CORRIGENDUM.md@82633a60:111-113` | "`2 <= rank C <= 4` (floor from a nonzero modular minor of actual forbidden coefficients at three symmetric-part-zero points on two certified vectors; ceiling from `E subset ker C`, `dim E = 1`);" | correctly-qualified |
| `PB/DFA/CORRIGENDUM.md@82633a60:70-73` | "A nonzero `C2(n)` on one globally certified survivor `n in ker C` proves a rank increment. A zero `C2(n)` on one such vector proves only that `C2` does not detect that vector; redundancy of `C2` relative to `C` requires `C2` to vanish on the whole certified kernel `ker C` (here of dimension `5 - rank C`)" | direction-stated |
| `PB/IC/REPORT.md@82633a60:17` | "**`u_L = m_pad` exactly.** The restriction bound then reads `m_det <= min(a, s - rho_L + m_pad) >= m_pad >= r` for every actual-padding floor `r`, whatever the source restriction rank `rho_L` is." | ceiling=value-consumed-as-floor |
| `PB/IC/REPORT.md@82633a60:67-71` | "`u_L = mult_lambda (R_L)_d <= … =: T_L(d, lambda)`: the **parameter-ring ceiling** … `u_L <= m_pad`, because `R_L` is a quotient of `R_pad` … `rho_L <= min(s, T^s_L)` … A certified floor `rho_0 <= rho_L` and a certified ceiling `u_0 >= u_L` are the safe substitutions; the exact `u_L` is what this note pins." | direction-stated |
| `PB/IC/REPORT.md@82633a60:83-89` | "`delta_L := m_pad - u_L >= 0` … `max( 0, sum_mu i_3(d, mu) - (T - m_pad) )  <=  delta_L  <=  sum_{mu : lambda/mu horizontal d-strip} i_3(d, mu)`." | two-sided |
| `PB/IC/REPORT.md@82633a60:95` | "If `I(D_5)_d = 0` then `u_L = m_pad` for every `lambda` … Then `min(a, s - rho_L + u_L) = min(a, s - rho_L + m_pad) >= m_pad >= r` for every actual-padding floor `r` and every `rho_L in [0, s]`: the 1+3 restriction bound cannot certify a gap in any cell of that degree." | ceiling-consumed-as-floor |
| `PB/IC/REPORT.md@82633a60:105-107` | "Hence `rho_L <= min(s, T^s_L)`. Whatever the target-side deficit `delta_L` is, a gap through the route needs `r  >  s - rho_L + u_L      <=>      rho_L  >  s - delta_L + (m_pad - r)`" | direction-stated |
| `PB/IC/REPORT.md@82633a60:146` | "Hence `m_det >= 1`, `i_pad >= 1`, `m_pad <= a - 1 = 1`, `D <= 0`. **Excluded.**" | i_pad-floor-consumed-as-m_pad-ceiling |
| `PB/IC/REPORT.md@82633a60:148` | "so `u_L <= m_pad <= 1 <= m_det` and no bound below `m_det` is available from any `rho_L`." | ceiling-chain |
| `PB/IC/REPORT.md@82633a60:93` | "`u_L <= min( a, m_pad, T(d, lambda) - sum_mu i_3(d, mu) )`, where any certified lower bound on `dim I(D_5)^{hw}_{d, mu}` may be substituted for `i_3` … (valid since `m_3 <= s_3`, the orbit bound for `det_3`)." | floor-on-i_3-consumed-as-ceiling-on-u_L |
| `PB/IC/REPORT.md@82633a60:125` | "`d <= 5`: `I(closure(GL_9 det_3))_d = 0` at every weight of every length; each weight a rank-attains-`a` certificate, two primes (**PRODUCER-CERTIFIED**, batch-13 …)" | modular-rank-floor-consumed-as-ideal-vanishing |
| `PB/IC/REPORT.md@82633a60:126` | "the total-deficit identity … left side measured by the batch-13 streamed algorithm, right side exact plethysm/branching, forces `mult = a` at every weight through `d = 7` (**MEASURED**: the paper says 'given the measured totals' …)" | measured-total-consumed-as-per-weight-equality |
| `PB/GKZ/REPORT.md@82633a60:17` | "the only `GL_16`-compatible content is lower bounds `m_det >= m_{in_Gamma(det_4)}` from face degenerations, which run against a gap." | floor-direction-stated |
| `PB/GKZ/REPORT.md@82633a60:86` | "The `GL_16`-compatible content reduces to `closure(GL . in_Gamma(det_4)) subset Y_det`, giving lower bounds `m_det(lambda, d) >= m_{in_Gamma}(lambda, d)` for every face; these can only kill cells, never open them." | floor-direction-stated |
| `PB/GKZ/REPORT.md@82633a60:179` | "the face degenerations `in_Gamma(det_4)` *are* inside the orbit closure … but that only yields `m_det >= m_{in_Gamma}`, the wrong direction for a gap." | floor-direction-stated |
| `PB/GKZ/REPORT.md@82633a60:15` | "for every Macaulay degree `k`, `rank M_k(z * per_3) <= rank M_k(det_4)`, so every Macaulay minor vanishing on the determinant orbit closure vanishes on the padded-permanent orbit closure. Its contribution to `D = m_pad - m_det` is zero in every cell." | rank-inequality-consumed-as-D-statement (narrowed SC C1/C4) |
| `PB/GKZ/REPORT.md@82633a60:164` | "for every cell `(d, lambda)`, `I_k(Y_det)_{d,lambda} subset I(Y_det)_{d,lambda} cap I(Y_pad)_{d,lambda}`, hence contributes equally to `i_det` and `i_pad` and contributes `0` to `D = i_det - i_pad`. There is no unproved transition on this path; the path ends in zero." | sign-convention-D=i_det−i_pad; narrowed-by-C4 |
| `PB/GKZ/REPORT.md@82633a60:200` | "Modular rank is a lower bound on the rational rank, so agreement with the exact formula is a consistency check, not a proof." | correctly-qualified |
| `PB/GKZ/REPORT.md@82633a60:145` | "by Lemma 3.1, `r_k(D45) >= r_k(F_0) = rho_k >= r_k(P5)`." | floor-at-point-consumed-as-max-on-closure |
| `PB/GKZ/REPORT.md@82633a60:149` | "For `k >= 7`: `sigma(k) <= 81 < 85 <= h(k)`, so `r_k(D45) >= dim S_k - 81 > dim S_k - h(k) >= r_k(P5)`." | two-sided-chain |
| `PB/GKZ/SC/CORRIGENDUM.md@82633a60:54` | "Then `D = i_det - i_pad = (i_det - i_common) - (i_pad - i_common)`. Every component of `(J_k)_d` of type `lambda` lies in the common ideal and so is counted in `i_common`; it supplies no separating equation and no advantage in the difference `D`. This does **not** prove `D = 0` in any cell" | correctly-qualified |
| `PB/TS/REPORT.md@82633a60:38-41` | "it bounds the number of conditions from above and locates the orders where they can live; a lower bound (a condition that is actually nonzero on the source) always needs one explicit source vector" | direction-stated |
| `PB/TS/REPORT.md@82633a60:273-274` | "inside one cell `j(M_lambda)` can be a proper subspace of `J_{<=4}`, and `dim j(M_lambda) <= min(s, dim J_{<=4})`. The rank of `j` on `M_lambda` is a global question (Tier C)." | ceiling-stated |
| `PB/TS/REPORT.md@82633a60:429-430` | "The space of such **E-free** conditions has dimension at most `dim J_{<=4} - 2`, i.e. **`1` for `r = 6` and `5` for `r = 5`**." | J*-dimension-read-as-rank (K2) |
| `PB/TS/REPORT.md@82633a60:436-438` | "The **rank actually realised** on `M_lambda` by all order-`<= 4` conditions at `K` is `dim j(M_lambda) - dim L` (with `L` replaced by `L_max` for E-free conditions), hence at most `min(dim J_{<=4}, s) - m_det` in case (b)." | dim(L_max)-substituted-for-dim(V∩L_max) (K1) |
| `PB/TS/REPORT.md@82633a60:461-462` | "Hence **at least `9 - 2 = 7` of the nine false survivors of `(6,(4^6))` are invisible to every jet condition of order `<= 4` at `K6`**, whatever carrier is built." | ceiling-consumed-as-floor-on-survivors (K7 retains) |
| `PB/TS/REPORT.md@82633a60:486-487` | "Realised rank: at most `s - m_det = 4` at `k = 1`. Whether the order-`<= 4` transverse conditions at `K5` reach rank 4 on `M_(4^5)` is exactly the **missing lemma** of §9." | ceiling-stated |
| `PB/TS/REPORT.md@82633a60:526-529` | "so `rank{C2, C4_{ij}} <= min(D, 5)` on the jet space, and `<= 4` on `M_(4^5)` (`E` is in every kernel). Hence at most **four** of the `D - 1` order-four identities can be independent, and adding directions beyond five is pointless." | ceiling-consumed-as-exhaustiveness |
| `PB/TS/REPORT.md@82633a60:573-578` | "`E subset ker C`, `dim E = 1`, so `rank C <= 4`, and `E` lies in the kernel of every transverse condition too, so `rank [C; T] <= 4` … `increment := rank [C; T] - rank C  in {0, 1, 2}  with  rank C in {2, 3, 4}`, and the increment is positive **iff** `rank C < 4` and some transverse condition does not vanish on `ker C`." | two-sided-stated |
| `PB/TS/REPORT.md@82633a60:602-605` | "Since `E` lies in every kernel, `rank <= s - m_det`, so `B >= m_det`, and `B < a` requires `m_det < a`, i.e. a determinant equation in the cell. In every cell touched here `m_det = a = 1`; **no transverse condition can lower the clipped bound below `a` there**, and none can anywhere unless an equation exists." | rank-ceiling-consumed-as-B-floor |
| `PB/TS/REPORT.md@82633a60:607-608` | "**`D > 0`** additionally needs a certified actual-padding rank floor `r > B`. Nothing here produces a padding floor" | direction-stated |
| `PB/TS/drafts/REPORT_body_draft.md@82633a60:387-390` | (same as TS 602-605) "`rank <= s - m_det`, so `B >= m_det`, and `B < a` requires `m_det < a` …" | duplicate-of-sealed |
| `PB/TF/CORRIGENDUM.md@82633a60:15-16` | "For the family annihilating `L_max` the correct quantity is `dim V − dim(V ∩ L_max)`; replacing `V ∩ L_max` by `L_max` presumes `L_max ⊆ V`, which is not proved (and need not hold)." | corrects-K1 |
| `PB/TF/CORRIGENDUM.md@82633a60:37-38` | "Also, '`dim J − 2`' is a dimension in `J^*`, not a rank on `M`; and a finite family of direction evaluations need not span the annihilator it sits in." | corrects-K2 |
| `PB/TF/CORRIGENDUM.md@82633a60:141` | "`C4_{S1,S2}` and `C4_{S1,S4}` are independent of `C2` over `Q` on `span(q_3, q_7)` (nonzero modular `2×2` minors `247396`, `197933`); hence `dim V − dim(V ∩ L_max) ≥ 2`, `dim V ≥ 3`." | floor-consumed-as-floor |
| `PB/TF/REPORT.md@82633a60:93-97` | "As `L ⊆ V ∩ L_max`: `rank F_free ≤ rank F_E`, with equality iff `V ∩ L_max = L`. … If `dim V = 5` (jet injectivity), `rank F_E = 4`; `rank F_free = 4` iff `V ∩ L_max = L`, and `= 3` iff `L_max ⊆ V`" | two-sided-stated |
| `PB/TF/REPORT.md@82633a60:114-116` | "Equivalently: `ker T = E` iff `rank T = 4` on `M` (because `dim M = 5` and `E ⊆ ker T`); a certified rank `4` of `T` on `M` therefore proves `ker j = 0`, the spanning, and (for E-free `T`) `V ∩ L_max = L` all at once" | floor=ceiling→kernel |
| `PB/TF/REPORT.md@82633a60:183-186` | "`dim V ≤ 3`, `dim L = 1` ⇒ `rank F_E ≤ 2`, `rank F_free ≤ 1` on `M_(4^6)`. At most two of the nine false directions are removable" | ceiling-stated |
| `PB/TF/REPORT.md@82633a60:249-254` | "(i) `rank F = 5` ⇒ `ker j = 0` … (iii) `rank F < 5` is inconclusive for injectivity unless the rank-one evaluations are shown to span … the OPEN spanning question of §3.3" | direction-stated |
| `PB/TF/REPORT.md@82633a60:314-317` | "`281079 ≠ 0` shows they are independent on `span(q_3, q_7)`, hence on `M`; but the rank of `{C2, C4_{S1,S2}, C4_{S1,S4}}` on `M` is only known to be `≥ 2`, the subspace having dimension two" | floor-stated (L2 reworded) |
| `PB/CL/CORRIGENDUM.md@82633a60:40-42` | "What two source columns cannot decide is whether the **three** rows … have total rank `2` or `3` on `M`; on the two known columns their rank is `2` (the maximum possible there), which is compatible with either. Consequently `rank F_free ≥ 2` and `dim V ≥ 3` (unchanged)." | correctly-qualified |
| `PB/CL/CORRIGENDUM.md@82633a60:70-73` | "a nonzero `4×4` minor of actual forbidden coefficient rows on columns `(q_3, q_7, q_a, q_b)` proves `rank C = 4` (with the known bound `rank C ≤ 4` from `E ⊆ ker C`, `dim E = 1`), hence `ker C = E` and every transverse condition is redundant with the arc. No complete basis is needed; S0 rows suffice for this floor." | floor+ceiling→value |
| `PB/CL/CORRIGENDUM.md@82633a60:80-84` | "or the observation that a sampled forbidden matrix of rank `b_L` on any set of source vectors makes the sample functionals injective on `C(M) = F_L`." | b_L-ceiling-used-as-target-value |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:7-8` | "`s = 5`, `g = 6`, `a = 1`, `m_det = 1`, `2 ≤ rank C ≤ 4`, no positive gap possible (`a = m_det`)." | two-sided-stated |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:76-78` | "A candidate `q_a` is independent of the known three iff the `4×5` matrix of `(q_3, q_7, e, q_a)` at the P6 points has modular rank `4` (a floor, valid over `Q`); with `q_b`, a nonzero `5×5` modular minor certifies a basis (`s = 5`)." | floor-consumed-as-'iff' |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:107-108` | "Rows: `p7_arc_S0.json: rows` (six rows, columns `(q_3, q_7)`), modular rank `2` ⇒ `rank C ≥ 2` over `Q` (sealed E6, PROVED floor)." | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:110-111` | "S0 rows are therefore valid for **rank floors** but a vector with vanishing S0-sampled forbidden rows is **not** thereby in `ker C`." | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:149-151` | "Since `rank C ≤ 4` (`E ⊆ ker C`, `dim E = 1`), this proves `rank C = 4`, `ker C = E`, and **every** globally necessary condition (`C2`, `C4`, anything) is redundant with the arc in this cell." | floor+ceiling→value |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:154-155` | "if the S0 rank on four vectors stays `3`, try general points with 13 nodes before concluding anything (S0 may under-count)." | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:163-166` | "`b_L := dim F_L` computable by branching … Then either (a) `rank_P R = b_L` — this forces `rank C = b_L`, `C(M) = F_L`, and the sample functionals are injective on `C(M)`, so a mod-`P` kernel vector of `R` is the reduction of an exact kernel vector of `C` (equal ranks over `Q` and mod `P`)" | b_L-ceiling-consumed-as-value |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:171-172` | "If `b_L ≤ 3` turns out true, `rank C ≤ 3 < 4` follows at once and a survivor exists; if `b_L = 4`, Route A and Route B are the two exhaustive outcomes." | ceiling-consumed-as-value; exhaustive |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:204` | "`rank C ≥ 2`, `rank C ≤ 4` ¦ PROVED (modular floor of actual forbidden rows; `E ⊆ ker C`)" | two-sided-stated |
| `PB/RA/REPORT.md@82633a60:13-15` | "every forbidden row tested — on the S0 slice at three points and, decisively, the full forbidden components at two general points — has rank 2 on `(q_3, q_7, n02)`, so no `rank C ≥ 3` or `= 4` certificate exists" | sampled-rank-read-as-absence-of-floor |
| `PB/RA/REPORT.md@82633a60:167-173` | "The `4×5` matrix … has modular rank **4**; nonzero `4×4` minors on point columns `{0,1,2,3}: 426380`, `{0,1,2,4}: 191230`, `{0,1,3,4}: 255288`, `{0,2,3,4}: 485311`, `{1,2,3,4}: 35010`. Since every entry is the reduction of an integer …, a nonzero modular minor proves rank 4 over `Q`." | floor-correctly-derived |
| `PB/RA/REPORT.md@82633a60:189-191` | "`3×3` determinant `225843 ≠ 0` mod `P`. Integer coefficients on integer evaluations, so the three globally necessary transverse functionals are linearly independent on `M` (rank exactly 3, the maximum for three rows)." | floor=row-count→value |
| `PB/RA/REPORT.md@82633a60:289-293` | "if `b_L = 2`, the four full-row functionals here already have rank `2 = b_L` on `C(M)`, so they are injective on `C(M) = F_L` and `n` is the reduction of an exact kernel vector — Outcome B follows … if `b_L = 3`, `rank C ≤ 3 < 4` and a survivor exists … if `b_L ≥ 4`, Route A remains possible" | b_L-ceiling-consumed-as-value (AT C2 withdraws as false) |
| `PB/AT/REPORT.md@82633a60:10-12` | "The grading-preserving Levi bound is `rank C ≤ b_L = 74` — PROVED, exact, by two independent formulations — and it is far too weak to decide anything: the known ceiling is `rank C ≤ 4` (`E ⊆ ker C`). No upper bound below 4 is obtained." | ceiling-stated |
| `PB/AT/REPORT.md@82633a60:32-34` | "If `rank C ≤ 2` were proved: `rank C = 2`, `dim ker C = 3 > 2 = dim ker T`, so `ker C ⊄ ker T` — an existence statement prior to any witness." | ceiling-consumed-hypothetically |
| `PB/AT/REPORT.md@82633a60:85-86` | "Therefore `C(M) ⊆ F^L` and `rank C ≤ b_L := dim F^L` (B19-01 Thm. 6.2). `C(M) = F^L` is not assumed anywhere." | correctly-qualified |
| `PB/AT/REPORT.md@82633a60:174-175` | "`b_L = 74 ≥ 2` is consistent with the certified floor (no convention conflict); it is also weaker than the trivial ceiling `4`, so the bound adds nothing to `rank C` (Case C)." | ceiling-stated |
| `PB/AT/REPORT.md@82633a60:232` | "**`C(M) ⊆ F''` and `rank C ≤ dim F'' ≤ b_L = 74`** (PROVED). `dim F''` is NOT computed here." | ceiling-stated |
| `PB/AT/REPORT.md@82633a60:247-249` | "The **sampled** kernel dimension `b''` satisfies `b'' ≥ dim F'' ≥ rank C` (sampling can only drop constraints), so it is a valid upper bound; over `F_P` it is again an upper bound (rank drops under reduction)." | sampled-kernel-dim-as-ceiling |
| `PB/AT/REPORT.md@82633a60:259-260` | "Proved upper bound on `rank C`: `74`, which is weaker than the known `rank C ≤ 4`. Proved lower bound: `2` (unchanged)." | two-sided-stated |
| `PB/AT/REPORT.md@82633a60:292-296` | "If it is 2: `rank C = 2`, `dim ker C = 3`, `ker C ⊄ ker T`, Proposition 7.1 applies … If it is 3: Case B (`rank C ≤ 3`, the arc does not isolate `E` …). If it is ≥ 4: the unipotent constraints are also insufficient and only exact arithmetic remains." | dim F''-ceiling-consumed-as-value |
| `PB/AT/CORRIGENDUM.md@82633a60:25-27` | "The paragraph is conditional on a value of `b_L` that is now known to be false (`b_L = 74`). The paragraph's logic was also stated for the global rank; the same conclusion in fact needs only `rank C¦_S = 2`" | corrects-RA-289 |
| `PB/AT/CORRIGENDUM.md@82633a60:31` | "`rank C¦_S = 2` is **not** proved; the Levi bound does not give it." | correctly-qualified |
| `PB/DA/REPORT.md@82633a60:123-124` | "as identities of functions they hold if evaluation at the point is injective on the span of the patterns, which is not certified: the rank 3 is a floor for that span's dimension" | correctly-qualified |
| `PB/DA/REPORT.md@82633a60:133-135` | "**Exact rank of the three restricted covariants: 3.** Since restriction to the dense-orbit slice is injective on this span (§B.5), `dim span(Φ_1^{(6)}, Φ_2^{(6)}, Φ_3^{(6)}) = 3` as functions" | floor+density→value |
| `PB/DA/REPORT.md@82633a60:205-207` | "the only characteristic-zero rank statements are floors (`r_top ≥ 3` from an exact nonzero rank on the slice, promoted to equality by the density argument on the span of the three covariants)." | correctly-qualified |
| `PB/FA/REPORT.md@82633a60:26-27` | "A nonzero `3×3` minor would prove `rank_Q(C¦_U) = 3` and `rank C ≥ 3` (Outcome A); zero minors prove no ceiling (Outcome B)." | correctly-qualified |
| `PB/FA/REPORT.md@82633a60:92` | "Proved intervals unchanged: `rank(C¦_U) ∈ {2, 3}`, `rank C ∈ {2, 3, 4}`, `rank T = 3` on `M` and on `U`." | two-sided-stated |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:32-37` | "`C` on `M` ¦ 2 (CERTIFIED, sealed E6) ¦ 4 (PROVED: `E ⊆ ker C`) ¦ `rank C ∈ {2,3,4}` OPEN … `T = (C2, C4_{S1,S2}, C4_{S1,S4})` on `M` and on `U` ¦ 3 (CERTIFIED, minor `225843`) ¦ 3 ¦ `rank T = 3`, `T¦_U` injective, PROVED … Levi target `F^L` ¦ — ¦ `b_L = 74` (PROVED, two formulations) ¦ uninformative" | two-sided-table |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:81-84` | "It is a valid ceiling for `rank C` but weaker than the trivial ceiling 4 … the refined target `F''` … is proved to contain `C(M)` but its dimension was never computed." | ceiling-stated |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:122-125` | "`rank C ≤ 2` proved (then `dim ker C = 3 > 2 = dim ker T`) … currently `rank(C,T) ≥ 3` (from `T` alone) and `≤ 4`." | two-sided-stated |
| `PB/ED/REPORT.md@82633a60:154-158` | "`rank [C;C2] = rank C + rank(C2 N_C)`. … Never add the individual ranks without checking the restriction to the first kernel. Modular minors of correctly defined rational/integral matrices certify characteristic-zero rank floors. Modular sampled zeros do not certify a rational identity or a rational kernel vector." | direction-stated |
| `PB/ED/REPORT.md@82633a60:206` | "For `a=1`, a nonzero determinant equation gives `m_det=0`; a padding nonzero gives `m_pad=1`, hence `D=1`. … A positive gap additionally requires `rank(T_pad)>rank(T_det)` in that same full ambient multiplicity space, or a certified determinant upper bound below an actual padding rank floor." | direction-stated |
| `PB/FC/REPORT.md@82633a60:106-112` | "The first two rows have determinant `61631 mod p`, nonzero. … this proves a characteristic-zero rank floor two. The source dimension is two; consequently `rank_Q C=2`, `ker C=0`, `rank_Q C2=1`, `rank_Q [C;C2]=2`. The rank increment is **zero**." | floor=dim→value |
| `PB/FC/REPORT.md@82633a60:152` | "An exact witness proves a positive increment; a nonzero modular minor of correctly defined rational matrices certifies a rank floor. Modular sampled zeros do not establish that a lifted vector belongs to the exact arc kernel. Likewise a lower bound on the stacked rank does not prove an increment over an old rank that is known only from below." | correctly-qualified |
| `PB/SL/REPORT.md@82633a60:227-228` | "Hence `rho_Z = 0` in every five-row cell, and the restriction bound of the B15-12 note … reads `m_det <= min(a, s)` on `L = Z`: the singular-pencil locus contributes nothing." | rank=0-consumed |

---

## B. PADDING MODEL (what "padding" is evaluated on)

| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/GKZ/REPORT.md@82633a60:48` | "`Y_det = closure(GL_N . det_4)` (for `N = 5`: `D45` … `dim 50`, ADOPTED B18-01), `Y_pad = closure(GL_N . z per_3)` (for `N = 5`: `P5 = R135 = { ell C }`, `dim 39`, ADOPTED B17-01/B18-01)." | P5=R135={ell C}; N=16 padded-with-idle |
| `PB/GKZ/REPORT.md@82633a60:15` | "**Result: rigorously blind to padding in every degree.** … Theorem A (sixteen variables …): for every Macaulay degree `k`, `rank M_k(z * per_3) <= rank M_k(det_4)`, so every Macaulay minor vanishing on the determinant orbit closure vanishes on the padded-permanent orbit closure." | 16-var padded form called "padding"; flag |
| `PB/GKZ/REPORT.md@82633a60:13` | "Applied to the Veronese this is the ordinary discriminant, which vanishes on `ell * C` products for the elementary reason in the brief." | general-product |
| `PB/GKZ/REPORT.md@82633a60:17` | "the padded permanent is not even in the family" | padded-form |
| `PB/GKZ/REPORT.md@82633a60:69` | "`rank Hess(z q) <= 9` on `{q = 0}` for every padded form, PROVED census 2.4" | padded-form |
| `PB/GKZ/REPORT.md@82633a60:78` | "Products and padded forms have a larger singular locus (codimension 2 against 4), so their Milnor algebra is larger in every degree … the mechanism then reads padding as 'more determinantal than the determinant'." | products-and-padded-forms-conflated |
| `PB/GKZ/REPORT.md@82633a60:90` | "**for every degree `k`, `r_k(Y_pad) <= r_k(Y_det)`, in `N = 5` and in `N = 16`**; if true, every Macaulay-minor determinant equation vanishes on padding and the route is closed" | "vanishes on padding" from Y_pad |
| `PB/GKZ/REPORT.md@82633a60:112` | "Coordinates: `x = (z, y_11..y_33, w_1..w_6)`, `F_pad = z per_3(y)`, `F_det = det_4(x)` in the same sixteen variables." | padded-with-6-idle-variables; flag |
| `PB/GKZ/REPORT.md@82633a60:118-120` | "*Padding side.* `d_z F_pad = per_3`, `d_{y_ij} F_pad = z p_ij` …, `d_w F_pad = 0`. … `r_k(z per_3) = … `" | 16-var-padded-called-"padding side" |
| `PB/GKZ/REPORT.md@82633a60:134` | "Theorem B (five variables …). For every `k >= 0`, `r_k(P5) <= r_k(D45)` … Consequently every Macaulay minor vanishing on `D45`, in every degree `k` … vanishes identically on `P5 = { ell C }` and hence on every actual five-variable padding restriction." | general-product ell·C labelled padding; flag (SC C2 narrows to J_k) |
| `PB/GKZ/REPORT.md@82633a60:138` | "*Padding side (PROVED, the argument of Proposition D).* For `F = ell C`, `d_i F = (d_i ell) C + ell d_i C in (ell, C)`, so `(J_F)_k subset (ell, C)_k` … the generic point of `P5` has `ell` not dividing `C`, so `r_k(P5) <= dim S_k - h(k)`" | general-product; flag |
| `PB/GKZ/REPORT.md@82633a60:143` | "pad UB:     16   39   80   146  245  386  579  835  1166" | general-product-bound called "pad UB" |
| `PB/GKZ/REPORT.md@82633a60:159` | "by Theorems A and B, `Y_pad subset Z_{k, r_k(Y_det)}` for every `k`, so the padding family is not an extraneous *component* of the Macaulay locus but is contained in it outright." | Y_pad |
| `PB/GKZ/REPORT.md@82633a60:164` | "Padding evaluation: identically zero on `Y_pad` (Theorems A, B; PROVED given the certificates)." | "padding evaluation" = Y_pad |
| `PB/GKZ/REPORT.md@82633a60:173` | "vanishes on the whole product family for an elementary reason? … **yes, and now proved in all degrees**: `J_{ell C} subset (ell, C)` (Theorems A, B)" | general-product; flag |
| `PB/GKZ/REPORT.md@82633a60:205` | "`F_prod = ell . C` with random integer `ell`, `C` (a point of `P5`); `F_padpt = x_1 . per_3(L x)`, `L in Mat_{9 x 5}(Z)` random (an actual padding restriction, a point of `P5`)" | both-called-P5; general product evaluated |
| `PB/GKZ/REPORT.md@82633a60:238-241` | "F_prod (ell C):    5   25   69  141  244  386  579 / F_padpt (x1 per3): 5   25   69  141  244  386  579 … both `P5` points stay at or below `padUB(k)` at every `k` (they equal it from `k = 8`, i.e. `(J_F)_k = (ell, C)_k` there)." | general-product-evaluation labelled certificate |
| `PB/GKZ/REPORT.md@82633a60:245-248` | "at `z per_3`: dim ker 15 (constant antisymmetric matrices on the six idle variables), rank 105. … (ii) they are blind: `rank D_7(z per_3) = 1650 <= 1904`, so all of them vanish on `closure(GL_16 . z per_3)`." | 16-var-padded-with-idle called "blind"; flag |
| `PB/GKZ/REPORT.md@82633a60:183` | "none is known to be nonzero on padding, and by Theorem B none of the Macaulay family ever is" | "on padding" = P5 |
| `PB/GKZ/pilots/p1_ambient_macaulay.py@82633a60:156` | "# z = x0, y[3a+b] = x[1 + 3a + b], w = x10..x15 idle" | idle-variables |
| `PB/GKZ/pilots/p2_quinary_macaulay.py@82633a60:4-5` | "integer product (a point of P5); F_padpt = x_1 * per_3(L x) with L a 9x5 integer matrix (an actual five-variable padding restriction, a point of P5)" | general-product=P5 |
| `PB/GKZ/pilots/p2_quinary_macaulay.json@82633a60:30` | "both P5 points obey padUB(k) for every k (else the (ell, C) argument is wrong)" | general-product |
| `PB/GKZ/SC/CORRIGENDUM.md@82633a60:22` | "`J_k  ⊆  I(Y_det) ∩ I(Y_pad)`      for every k,   Y_det = closure(GL_16 . det_4),  Y_pad = closure(GL_16 . z per_3)." | 16-var-padded |
| `PB/GKZ/SC/CORRIGENDUM.md@82633a60:34` | "`r_pad(k) <= r_det(k)` on `D45` versus `P5` (unchanged) … generate `J_7 ⊆ I(D45) ∩ I(P5)`, hence vanish on every actual five-variable padding restriction (points of `P5`)." | general-product-cone called padding; flag |
| `PB/GKZ/SC/CORRIGENDUM.md@82633a60:94` | "The ordinary discriminant … vanishes on the whole product family `{ ell C }` and on `Y_pad`: blind (elementary, `dF = C dl + l dC`)." | general-product |
| `PB/GKZ/SC/REVISED_VERDICT.md@82633a60:18` | "**Theorem B (five variables).** For every `k`, the maximal rank of `M_k` on the product cone `P5 = { ell C }` is at most its maximal rank on `D45`" | general-product cone |
| `PB/GKZ/SC/REVISED_VERDICT.md@82633a60:32` | "The ordinary discriminant vanishes on all products `ell C`: blind, elementary." | general-product |
| `PB/GKZ/SC/CLAIM_SCOPE_TABLE.md@82633a60:7` | "vanishes on every product `ell C`, hence on `P5` and on `Y_pad`; vanishes on `Y_det` (every determinantal quartic is singular)" | general-product |
| `PB/GKZ/SC/CLAIM_SCOPE_TABLE.md@82633a60:8` | "Macaulay rank-threshold ideals `J_k` …, five variables (`D45` vs `P5`) … padding side proved (`J_{ell C} ⊆ (ell, C)`)" | general-product called "padding side"; flag |
| `PB/IC/REPORT.md@82633a60:13` | "The closed image of the 1+3 locus is `Y_L = { l * C : l linear, C in D_5 }`, a closed cone inside the 39-dimensional padding cone `Y_pad = { l * C : C any cubic }`." | general-product-cone = padding cone |
| `PB/IC/REPORT.md@82633a60:17` | "**polynomials of degree below `delta_0` cannot tell determinantal products `l * C_det` from arbitrary products `l * C`.**" | general-product |
| `PB/IC/REPORT.md@82633a60:47` | "`Y_pad := m(V^* x Sym^3 V^*)`. … `Y_pad = R135` of B18-01, `dim Y_pad = 39` (ADOPTED, B18-01 Lemma 4.1). By the accepted five-variable identification, `m_pad(d, lambda) = mult_lambda C[Y_pad]_d` (ADOPTED, B17-08 (2), B18-01 01-A with B17-03 Lemma 2)." | m_pad defined on general-product cone; flag |
| `PB/IC/REPORT.md@82633a60:206` | "(The 2+2 locus has image `{ q_1 q_2 : rank q_i <= 4 }`, which is not of this form and is not contained in `Y_pad`; …)" | scope |
| `PB/DF/REPORT.md@82633a60:227-231` | "(P3) `H5` vanishes on all of `{l·C}` — **PROVED by Pieri**: … hence `T(5,(4^5)) = 0`, `U = 0` (B19-02 §8.1 records the same)." | general-product |
| `PB/DF/REPORT.md@82633a60:239-240` | "`h` vanishes on `R135 = closure{l·C}` by (P3), so `i_pad >= 1` and `m_pad <= a - 1 = 1`." | general-product vanishing → m_pad; flag |
| `PB/DF/REPORT.md@82633a60:219` | "For `pi(L_(2,2)) = closure{q_1 q_2}` no inclusion in `{l·C}` holds, so `U` does not bound `u_L` there; a separate ceiling is required." | scope |
| `PB/DF/REPORT.md@82633a60:24-25` | "the 2+2 partial-transpose family is provably blind on every even five-row rectangle." | "blind" (source-side family) |
| `PB/ED/REPORT.md@82633a60:200-204` | "**Five rows and padding.** … Test an extracted equation on `c_alpha(l C)=…`. The padding pullback has bidegree `(d,d)` in five linear coefficients and 35 cubic coefficients. By the accepted five-variable equality of the actual padding restriction closure with `R135`, a nonzero value on any `lC` is a legitimate padding separation certificate here. It is not an extrapolation to unrestricted cubic products in more variables." | general-product-nonzero = "padding separation certificate"; flag |
| `PB/ED/REPORT.md@82633a60:206` | "a padding nonzero gives `m_pad=1`, hence `D=1`." | consumes-B |
| `PB/ED/REPORT.md@82633a60:236` | "It does not rule out … the accepted noncontainment `R135 not subset D45`." | R135 |
| `PB/AS/REPORT.md@82633a60:37` | "Background, not premises of the redundancy proof: dim D45=50, dim P5=39, and P5=closure{linear times arbitrary cubic} only in five variables." | P5 = general product, five variables only |
| `PB/AS/REPORT.md@82633a60:285-286` | "A product ell*C already has d(ell*C)=C*dell+ell*dC and is singular along ell=C=0. - No claim about arbitrary cubic padding in six or more variables is made." | correctly-scoped |
| `PB/TS/REPORT.md@82633a60:607-608` | "**`D > 0`** additionally needs a certified actual-padding rank floor `r > B`. Nothing here produces a padding floor; the transverse programme is a determinant-side tool only." | "actual-padding" |
| `PB/SL/REPORT.md@82633a60:355` | "No `rho_Z`, no `m_det`, no `m_pad`, no `r`, no gap: the outcome is purely a closure." | scope |
| `75ddb900:docs/b19_02_report.md:471-473` | "The three padding values were all zero, which I use for **nothing**: a sampled zero proves nothing, and the inherited padding ceiling `U = 0` already gives `m_pad = 0` in this cell." | ceiling-U-consumed-as-value |

---

## C. SOURCE MEMBERSHIP (vector ∈ M_λ / M / U / E / ker C, with cited evidence)

| file@commit:line | verbatim quote | tag (evidence type) |
|---|---|---|
| `PB/TS/REPORT.md@82633a60:87-91` | "`M_lambda = (S_lambda W)^H` realised as polynomials `z(Y_1, ..., Y_r)` of `GL_r`-highest weight `lambda`; `phi(Y) = det(sum x_i Y_i)`; `A_{d,lambda}` = ambient highest-weight coefficient polynomials; `E_lambda = phi^* A_{d,lambda}`; `m_det = dim E_lambda`." | definition |
| `PB/TS/REPORT.md@82633a60:408-409` | "`j(E) = j_A(A_{d,lambda}) = L`, and `E subset M_lambda`, so `L subset j(M_lambda)`." | asserted-by-identification |
| `PB/ED/REPORT.md@82633a60:13-15` | "`E_lambda = phi_r^*(A_{d,lambda}) subset M_lambda`, … This follows from equivariance of coefficient pullback and the row-model/Peter-Weyl identification; it identifies positions of subspaces, not just their dimensions." | proof-sketch |
| `PB/ED/REPORT.md@82633a60:86-90` | "Simultaneous transpose interchanges `pi` and `rho`; `Q` is therefore fixed by the full stabilizer. Thus `Q in M_(2^6)`, … Its square `z_* := Q^2 in M_(4^6)` … The nonzero evaluations below also prove these are nonzero polynomials. By the silence calculation, `C(z_*)=0`." | by-construction + B19-01 theorem |
| `PB/ED/REPORT.md@82633a60:61-63` | "Suppose `q_1,...,q_s` are a certified basis of `M_lambda` and the `N x s` matrix `S_T=(q_i(Y^(j)))` has column rank `s`. Then evaluation is injective on the whole carrier. Since both `q` and `phi_r^*h` belong to this carrier, … Therefore `ker C2_T = E_lambda`." | conditional-on-basis |
| `PB/DF/REPORT.md@82633a60:77-81` | "Build five vectors `q_1..q_5 in M_(4^5)` as symmetrised epsilon contractions (membership by construction: four full five-wedges give type `(4^5)`; five row-epsilons and five column-epsilons give `(det A det B)^5`; symmetrisation gives transposition invariance)." | by-construction |
| `PB/DF/REPORT.md@82633a60:118-121` | "**`Q in M_(2^6)`, `Q^2 in M_(4^6)` (membership).** The epsilon-contraction argument … is correct. **VERIFIED (re-derived).**" | re-derived |
| `PB/DF/REPORT.md@82633a60:313-315` | "Certified: **two independent vectors `q_3, q_7 in M_(4^5)`** (slot lists in `pilots/p6_basis.json`, `pi`/`rho` fields; membership by construction; independence by the `2 x 5` value matrix of rank 2 mod `524287`, hence over `Q`). **Not certified:** a basis." | by-construction + modular rank |
| `PB/DF/REPORT.md@82633a60:353` | "Upper bound `rank C <= 4` holds (`E = span(H5 ∘ phi) subset ker C`, `m_det = 1`)." | E ⊆ ker C asserted (no citation here) |
| `PB/DF/REPORT.md@82633a60:459` | "E5 ¦ Two independent vectors `q_3, q_7 in M_(4^5)` ¦ CERTIFIED (membership by construction; `2 x 5` modular rank 2) ¦ `p6_basis.json`" | by-construction |
| `PB/DF/REPORT.md@82633a60:461` | "E7 ¦ `rank C <= 4` ¦ PROVED (`E subset ker C`, `dim E = m_det = 1`) ¦ §C.6" | E ⊆ ker C asserted |
| `PB/FC/REPORT.md@82633a60:84` | "The three row epsilons and three column epsilons give the factor `(det L det R)^3` … Transpose interchanges the ordered partitions, so the sum is invariant under the full stabilizer. Thus membership is proved directly, without ambient polynomials. A two-point evaluation determinant `418914 mod 524287` proves independence." | by-construction |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:24-25` | "Membership `q ∈ M`: four full five-wedges give `GL_5`-weight `(4^5)`; five `pi` and five `rho` epsilons give `(det A det B)^5`; symmetrisation gives transpose invariance (sealed §3 item 3)." | by-construction |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:33` | "### 2.1 `q_3` and `q_7` (full-`H` epsilon contractions; PROVED members of `M`)" | by-construction |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:50` | "### 2.2 `e = H5 ∘ phi` (the ambient generator; PROVED member of `E ⊆ M ∩ ker C`)" | PROVED-label |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:61-67` | "Certificates: `a = 1` by the Weyl alternant (sealed P1); the B19-02 rectangle certificate `…rect_4_4_4_4_4.json` …: a highest-weight vector of weight `(4^5)` …, exact raising residues zero …; by `a = 1` it is proportional to the alternant `H5`. Nonzeroness of `e`: `e(K5) = 322560` … `E ⊆ ker C`: B19-01 §5; checked here in the S0 convention (§4)." | certificate-files + B19-01 §5 + S0 sampled check |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:115` | "`e` at the S0 points is constant in `t` (checked exactly here), as `E ⊆ ker C` requires." | sampled-consistency |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:203` | "`q_3, q_7 ∈ M`; `e ∈ E ⊆ M ∩ ker C`; `q_3, q_7, e` independent ¦ PROVED (membership by construction / certificates; independence by the arc argument), plus modular rank 3" | PROVED-label |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:147-148` | "Find `q_a, q_b ∈ M` (contractions, membership by construction)" | by-construction |
| `PB/CL/CORRIGENDUM.md@82633a60:49-57` | "Let `e := H5 ∘ phi` … Premises, each verified: (i) `e ∈ E ⊆ M`: `H5` is the unique (up to scale) element of `A_{5,(4^5)}` (`a = 1`, Weyl alternant, sealed P1 and B19-02 `rect_4_4_4_4_4.json`), and `E = phi^*(A_{5,(4^5)}) ⊆ M` by the row-model identification (`extension_descent` conventions); (ii) `e ≠ 0`: `e(K5) = 322560` …; (iii) `e ∈ ker C`: `E ⊆ ker C` (B19-01 §5); in the implemented S0 convention this was checked exactly here: at each of the three sealed P7 symmetric-part-zero points, `e(a -> t a)` is **constant** for `t = 0..3`" | identification + B19-01 §5 + S0 sampled check |
| `PB/CL/CORRIGENDUM.md@82633a60:74-84` | "Construct `n ∈ ker C` and certify `C(n) = 0` **globally**, then show `T(n) ≠ 0`. Sampled zeros do not certify `n ∈ ker C`, for two separate reasons … (a) S0 rows see only the `#Sigma = 0` part … (b) even then, finitely many evaluations certify `C(n) = 0` only through an injectivity argument on the finite-dimensional space `F_L := ((S_lambda W)_{forbidden})^L ⊇ C(M)` (B19-01 Thm 6.2)" | membership-in-ker C-conditional |
| `PB/CL/STABILIZER.md@82633a60:12-15` | "Every `z in M = M_(4^5)` is a semi-invariant: `z(g.A.Y.B) = det(g)^4 det(A)^5 det(B)^5 z(Y),        z(Y^T) = z(Y).`" | definition |
| `PB/RA/REPORT.md@82633a60:50-51` | "`q_3, q_7 ∈ M` (contractions, membership by construction, B18-02 Prop. 2.2) ¦ PROVED / `e = H5 ∘ phi ∈ E ⊆ M ∩ ker C`, `e(K5) = 322560` ¦ PROVED" | by-construction / inherited |
| `PB/RA/REPORT.md@82633a60:90-93` | "**Membership.** Every candidate is a symmetrised contraction of the form (2.1) with four height-5 columns, five `pi` and five `rho` epsilon blocks: `GL_5`-weight `(4^5)`, `(det A det B)^5` semi-invariance and transpose invariance are by construction (B18-02 Prop. 2.2 (i)–(ii); the handoff §1 membership line). Membership does not depend on any evaluation." | by-construction |
| `PB/RA/REPORT.md@82633a60:135` | "n02 ¦ (02)(13) ¦ 53303, 478236, 468518 ¦ nonzero ¦ **outside `span(q_3, q_7, e)`**" | modular-residuals |
| `PB/RA/REPORT.md@82633a60:146-148` | "For n02 the three residuals are nonzero (`286028, 468669, 186556`), which **proves** (a nonzero modular rank of integer evaluations) that `n02 ∉ span(q_3, q_7, e)`: four independent source directions." | modular-nonzero→Q |
| `PB/RA/REPORT.md@82633a60:182-183` | "A six-value fit shows both [m00, m01] lie in `span(q_3, q_7, e, n02)` modulo `P` (two residual checks each; MEASURED, not proved)." | sampled-membership-in-span, qualified |
| `PB/RA/REPORT.md@82633a60:224-229` | "`n := n02 − 265391·q_3 − 275398·q_7   (coefficients modulo P; …)` vanishes on ten sampled forbidden functionals … **This is a sampled arc-kernel candidate, not a certified member of `ker C`** (CORRIGENDUM L4 / handoff §7 step 3 …). It is not promoted." | ker C membership not asserted |
| `PB/RA/REPORT.md@82633a60:241` | "`n02 ∈ M` (contraction, form (2.1)) ¦ PROVED (by construction)" | by-construction |
| `PB/RA/REPORT.md@82633a60:246` | "`n ∈ ker C` (survivor) ¦ SAMPLED ONLY (ten functionals, one prime); NOT certified" | correctly-qualified |
| `PB/RA/certificates/n02_definition.json@82633a60:3` | "Full-stabilizer source vector of M_(4^5): q = P_{pi,rho} + P_{rho,pi} (B18-02 Prop. 2.2 eq. (2.1)); membership by construction." | by-construction |
| `PB/RA/certificates/arc_rows_and_sampled_kernel_candidate.json@82633a60:395` | "SAMPLED ONLY: zero on 10 sampled forbidden functionals modulo one prime. NOT a certificate of n in ker C (SOURCE_HANDOFF section 7 Route B step 3; b_L not computed)." | correctly-qualified |
| `PB/AT/REPORT.md@82633a60:51-55` | "`M` is the space of polynomial functions on `W ⊗ C^5` of multidegree `(4^5)` that are `GL_5`-highest-weight vectors of weight `λ` and satisfy `z(AYB) = (det A det B)^5 z(Y)`, `z(Y^T) = z(Y)`. … On `H^0 = {(A,B): det A det B = 1}` every `z ∈ M` is an invariant function." | definition |
| `PB/AT/REPORT.md@82633a60:84-86` | "`L` preserves each `W_i` …; `C` is `L`-equivariant; `M ⊆ (S_λ W)^L` because `(det A det B)^5 = 1` on `L`. Therefore `C(M) ⊆ F^L` and `rank C ≤ b_L := dim F^L` (B19-01 Thm. 6.2). `C(M) = F^L` is not assumed anywhere." | C(M) ⊆ F^L proved; equality not assumed |
| `PB/AT/REPORT.md@82633a60:123-127` | "(3) that the *displayed modular candidate* `n̄ = n02 − 265391 q_3 − 275398 q_7 ∈ F_P ⊗ M` is the reduction of such an `n`. The residues are not a rational witness. Status after this session: (1) OPEN, (2) OPEN, (3) PROVED only conditionally on `rank C¦_S = 2` (Prop. 7.1)." | conditional |
| `PB/AT/REPORT.md@82633a60:227` | "For `z ∈ M`, `z∘τ = z` and the `#v`-graded pieces with `#r = #c` are `τ`-stable, so `z_{−2}∘τ = z_{−2}`, `z_{−1}∘τ = z_{−1}`: `C(M) ⊆ (F^L)^{τ}`." | proved-containment |
| `PB/AT/CORRIGENDUM.md@82633a60:44-45` | "(3) *Lifting of the displayed modular candidate*: PROVED **conditionally** on `rank C¦_S = 2` (REPORT.md Prop. 7.1); unconditionally the displayed `n̄` is a vector over `F_P` in the kernel of ten sampled functionals and nothing more." | conditional |
| `PB/DA/REPORT.md@82633a60:59-60` | "Each `X_H` is a quadratic `GL(A)×GL(B)`-covariant of the 5-wedge `D` (an element of `Cov = Hom(Sym²Λ⁵(A⊗B), Λ²A⊗Λ²B⊗det_A²det_B²)`; only the `Λ²⊗Λ²` part survives `B`)." | covariant-membership by construction |
| `PB/DA/REPORT.md@82633a60:122-124` | "Hence, exactly at this point, `q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)` (MEASURED-EXACT at one point; as identities of functions they hold if evaluation at the point is injective on the span of the patterns, which is not certified …)." | at-one-general-point; conditional |
| `PB/DA/REPORT.md@82633a60:97-98` | "so `G'·cone(V)` is dense in `S*` and **a linear combination of restricted covariants vanishing on `cone(V)` vanishes on `S*`**." | density argument |
| `PB/DA/CORRIGENDUM.md@82633a60:30-32` | "the exact structure `q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)` (exact at the general point) stand and are the new starting point." | "at the general point" |
| `PB/FA/REPORT.md@82633a60:24` | "`U = span_Q(q_3, q_7, n02)`, `dim U = 3` (certified)." | certified-span |
| `PB/FA/REPORT.md@82633a60:87-88` | "`e ∈ ker C` is the inherited global proof (B19-01 §5, restriction of a global polynomial), not a sampled zero." | inherited-proof |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:27-28` | "Membership of `q_3, q_7, n02` is by construction (B18-02 Prop. 2.2); `e ∈ E ⊆ ker C` by the global restriction argument (B19-01 §5). The fifth direction is NOT found. `U := span_Q(q_3, q_7, n02)`." | by-construction / inherited |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:53-55` | "Coordinates `q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)` hold exactly at one general point (exact integers); as identities of functions they need injectivity of evaluation on the pattern span, which is not certified (values have rank 3 there, `dim Cov = 4`)." | at-one-point; conditional |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:97-98,105-106` | "Let `Φ_1, Φ_2, Φ_3` be the two-column covariants with (at the general point) `q_3 = 2B(Φ_1,Φ_2)` … (as identities of functions, conditional on the pattern-span injectivity of §4; unconditionally at the general point)." | "at the general point" |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:119-121` | "two source directions beyond `span(q_3, q_7, e, n02)`... precisely, the fifth direction plus full rows …; the paired families tried so far live in `span(q_3, q_7, e, n02)`." | span-membership asserted (RA 182-183 says MEASURED mod P, not proved) |
| `PB/AS/REPORT.md@82633a60:59-63` | "let `M` be any finite source subspace of degree-4d polynomials on W^k such that `z(PYQ) = (det P det Q)^d z(Y)`, `z(Y^T)=z(Y)` … A specified highest-weight source M_lambda is such a subspace. … The argument therefore applies to the full M of the user's diagnostic, not just its four known vectors." | hypothesis-level |
| `PB/AS/REPORT.md@82633a60:65` | "Let E be its genuine coefficient subspace: z=H o phi … It is essential that polynomial descent is assumed only for E, not for arbitrary z in M." | assumption-scoped |
| `PB/AS/REPORT.md@82633a60:187` | "These components live in the ambient polynomial space; they need not separately belong to M." | correctly-qualified |
| `PB/SL/REPORT.md@82633a60:138-143` | "for `l(lambda) = 5` the full-`H` source `M_lambda` sits inside the `S_lambda`-isotypic component of `C[(Mat4)^5]^G`. That component is `GL5`-stable and is spanned by multihomogeneous functions whose multidegree … satisfies `nu_5 >= lambda_5 >= 1` … This is the B15-12 note's Claim 4.2.2, which stays PROVED" | containment-asserted (inherited) |
| `PB/SL/REPORT.md@82633a60:309-312` | "check 2 evaluated the two certified full-`H` vectors `q_3, q_7` of `M_(4^5)` … at four `GL5`-mixes of `X_0` … All eight values are zero, exactly as Theorem 4.1 predicts; they are **not** used as evidence, the theorem is." | inherited-membership |
| `PB/TF/REPORT.md@82633a60:130-134` | "`F_E = Ann(L) ∘ j`: uses the Hessian ratio of the ambient generator (`[t^4]/[t^0]` on `H5 ∘ phi`: `13/21` …), an **ambient-image datum adopted from the evaluation of `H5`**; these conditions are not independent of ambient-image information" | adopted-ambient-datum |
| `PB/TF/REPORT.md@82633a60:225-226` | "`z = s^8 z` there and **`[t^4] z(K5 + t S4) = 0` for every `z ∈ M`** — the E-using `S4` row is identically zero on `M` (observed on `q_3, q_7` and on `H5 ∘ phi`, §5.5)" | proved-for-all-M (torus) |

---

## D. GLOBAL vs SAMPLED (labels "global/identically/certified/PROVED" versus one-prime sampled evidence)

### D.1 The 14-functional forbidden matrix / sampled relation of n02
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/RA/REPORT.md@82633a60:151-154` | "The four S0 rows … have modular rank **2**; all 21 minors `4×4` containing `q_3, q_7` vanish. In particular n02's forbidden S0 components at points 0 and 1 lie in the span of those of `q_3, q_7` (MEASURED on the slice; see §5.2 for point 2)." | correctly-qualified |
| `PB/RA/REPORT.md@82633a60:175-179` | "The `6×3` S0 forbidden matrix on `(q_3, q_7, n02)` has rank **2**: on the slice, `n02`'s column equals `265391·q_3 + 275398·q_7` (mod `P`) in all six rows … this is the under-counting the handoff warned about, or a genuine arc dependence — decided in §5.3." | "decided in §5.3" over-reads |
| `PB/RA/REPORT.md@82633a60:220-222` | "Modular rank **2**. Moreover n02's column satisfies **exactly the same relation** as on the S0 slice: `n02 = 265391·q_3 + 275398·q_7` (mod `P`) in all four full rows (residuals `0, 0, 0, 0`) and in all six S0 rows." | sampled; "exactly" |
| `PB/RA/REPORT.md@82633a60:227-229,235` | "**This is a sampled arc-kernel candidate, not a certified member of `ker C`** … Without the global certificate nothing follows." | correctly-qualified |
| `PB/RA/REPORT.md@82633a60:279` | "Route B is not settled: the sampled survivor `n` has no global `C(n) = 0` certificate." | correctly-qualified |
| `PB/AT/REPORT.md@82633a60:284-286` | "The hypothesis `rank C¦_S = 2` is exactly what the ten recorded sampled functionals suggest and what neither the Levi bound nor any certificate proves" | correctly-qualified |
| `PB/DA/REPORT.md@82633a60:11-12` | "Everything recorded remains consistent with `rank C¦_U = 2` (the sampled relation and, newly, an exact rank-1 structure of the degree-12 rows)" | "exact rank-1 structure" from sampled rows; flag |
| `PB/DA/REPORT.md@82633a60:143-145` | "The recorded degree-12 rows are proportional at all five sampled points (exact rank 1 modulo `P`, constant ratios `101007`, `295818`): with independent tops, this says the pairing `B` restricted to the top space has (sampled) rank 1 — a genuine structural fact about `B`, not about the tops." | sampled→"genuine structural fact"; flag |
| `PB/DA/CORRIGENDUM.md@82633a60:19-22` | "New, exact, and consistent with the parent: the skew-degree-12 rows of `q_3, q_7, n02` are proportional at all five recorded points with constant ratios (… mod `P`), i.e. the degree-12 part of the sampled forbidden matrix has rank 1, not 2" | "exact" for sampled-mod-P; flag |
| `PB/FA/REPORT.md@82633a60:12-16` | "All four satisfy the recorded relation `n02 ≡ 265391 q_3 + 275398 q_7 (mod 524287)` exactly (residuals 0); the combined 14-row matrix has rank 2 and all 364 `3×3` minors vanish modulo `P`; the seven degree-12 rows have rank 1 with the constant ratios `101007, 295818`. These are additional sampled zeros and prove nothing about a ceiling; they are not promoted." | correctly-qualified |
| `PB/FA/REPORT.md@82633a60:78-79` | "The sampled relation now holds on 14 functionals at 5 general and 3 S0 points, all modulo one prime. This remains evidence only." | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:48-50` | "`n02 ≡ 265391 q_3 + 275398 q_7` on the forbidden components at **14 sampled functionals** …, modulo `P` only. The coefficients are residues; no small-height rational lift exists (bound 2000). Not a global identity." | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:51` | "Degree-12 rows: rank 1 at all seven recorded points with constant ratios `101007, 295818` (SAMPLED)." | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:108-110` | "The degree-12 equation is sampled-true (rank-1 rows); the degree-11 equation is the open 'mixed-pairing identity'. `rank(C¦_U) = 3` ⟺ some full-row `3×3` minor is nonzero (none found on 14 functionals)." | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:137-138` | "Cheap, but cannot prove rank 2, and after 14 concordant functionals the prior for rank 3 is low." | sampled-as-prior |

### D.2 The five 4×4 minors (426380, 191230, 255288, 485311, 35010)
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/RA/REPORT.md@82633a60:167-173` | "**Four independent source directions (CERTIFIED, characteristic-zero floor).** … nonzero `4×4` minors on point columns `{0,1,2,3}: 426380`, `{0,1,2,4}: 191230`, `{0,1,3,4}: 255288`, `{0,2,3,4}: 485311`, `{1,2,3,4}: 35010`. Since every entry is the reduction of an integer (contraction values; exact `e`), a nonzero modular minor proves rank 4 over `Q`." | correctly-qualified (floor) |
| `PB/RA/REPORT.md@82633a60:242` | "`q_3, q_7, e, n02` linearly independent; `dim span = 4` ¦ CERTIFIED (nonzero modular `4×4` minors of integer evaluations ⇒ over `Q`)" | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:16-17` | "Four independent directions (CERTIFIED: `4×5` matrix at the sealed P6 points, minors `426380, 191230, 255288, 485311, 35010`)" | correctly-qualified |
| `PB/AT/CORRIGENDUM.md@82633a60:55` | "`dim span(q_3, q_7, e, n02) = 4` (certified); `rank T = 3` on `M` (proved)" | certified/proved labels |
| `PB/AS/REPORT.md@82633a60:30` | "four independent source vectors q3,q7,n02,e; transverse rank 3, certified by minor 225843 modulo 524287. This supersedes the older handoff's rank-2-or-3 status." | certified-label |

### D.3 rank T = 3 (det 225843)
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/RA/REPORT.md@82633a60:185-192` | "**Transverse triple has rank 3 on `M` (PROVED).** … `3×3` determinant `225843 ≠ 0` mod `P`. Integer coefficients on integer evaluations, so the three globally necessary transverse functionals are linearly independent on `M` (rank exactly 3, the maximum for three rows). This closes the 'rank 2 or 3' question of CORRIGENDUM L2." | PROVED-from-modular-nonzero (floor=max) |
| `PB/RA/REPORT.md@82633a60:243` | "`{C2, C4_{S1,S2}, C4_{S1,S4}}` has rank 3 on `M` ¦ PROVED (nonzero modular `3×3` minor `225843`)" | PROVED-label |
| `PB/RA/certificates/transverse_triple_rank3.json@82633a60:2` | "The three globally necessary transverse functionals C2, C4_{S1,S2}, C4_{S1,S4} have rank 3 on M_(4^5) (nonzero 3x3 modular minor of integer evaluations on q3, q7, n02)" | certificate-claim |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:36,41` | "3 (CERTIFIED, minor `225843`) ¦ 3 ¦ `rank T = 3`, `T¦_U` injective, PROVED" / "`C2`, `C4_{S1,S2}`, `C4_{S1,S4}` vanish on `E` (globally necessary); pairwise and jointly independent on `M`." | PROVED/CERTIFIED labels |
| `PB/AT/REPORT.md@82633a60:32-33` | "Known (parent packet; PROVED/CERTIFIED over `Q`): `dim M = 5`, `dim E = 1`, `E ⊆ ker C`, `rank C ≥ 2`, `rank T = 3` for `T = (C2, C4_{S1,S2}, C4_{S1,S4})`." | labels |
| `PB/AS/PREREG.md@82633a60:24` | "The user-supplied updated status is rank T = 3 and 2 <= rank C <= 4." | inherited |
| `PB/FA/REPORT.md@82633a60:92` | "`rank T = 3` on `M` and on `U`." | unqualified-in-line (CERTIFIED elsewhere) |

### D.4 Pairwise minors 247396, 197933, 281079
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/TF/REPORT.md@82633a60:302-303` | "`2×2` minors mod `P`: `det[C2; C4_{S1,S2}] = 247396`, `det[C2; C4_{S1,S4}] = 197933`, `det[C4_{S1,S2}; C4_{S1,S4}] = 281079`; rank of the `3×2` matrix `= 2`." | data |
| `PB/TF/REPORT.md@82633a60:307-310` | "**Certified (characteristic zero).** `C2` and `C4_{S1,S2}` are linearly independent functionals on `M` (a nonzero minor of integer evaluations reduced modulo a prime is a nonzero integer minor); likewise `C2` and `C4_{S1,S4}`. Hence `rank F_free ≥ 2` on `M`, so `dim V − dim(V ∩ L_max) ≥ 2` and `dim V ≥ 3`." | correctly-qualified |
| `PB/TF/REPORT.md@82633a60:77-80` | "A nonzero modular `2×2` minor of `[C2; C4_*]` on columns `(q_3, q_7)` certifies independence of the two functionals over `Q` … Zero modular minors are inconclusive. Either way nothing follows for all of `M` or for `ker C`." | correctly-qualified |
| `PB/TF/REPORT.md@82633a60:373` | "F12 ¦ `C2` and `C4_{S1,S2}` (and `C2`, `C4_{S1,S4}`) independent over `Q` on `M`; `rank F_free ≥ 2`; `dim V ≥ 3`; T9' positive ¦ CERTIFIED (nonzero modular minors of integer evaluations)" | CERTIFIED-label |
| `PB/TF/CORRIGENDUM.md@82633a60:141-142` | "T9 ¦ NOT REACHED ¦ **PARTLY REACHED** … (nonzero modular `2×2` minors `247396`, `197933`) … T9' ¦ EXPECTED ¦ **PROVED a posteriori**: a nonzero minor with `C2` forces a nonzero `Phi_4`-component" | PROVED-from-modular |
| `PB/CL/CORRIGENDUM.md@82633a60:9-11` | "the nonzero minors `247396` and `197933` (follow-up §5.3) prove that fourth-order compatibility supplies functionals independent of `C2` on `M = M_(4^5)`; independence from the old arc `C` remains unresolved (`C` is injective on `span(q_3, q_7)`)." | "prove"-from-modular |
| `PB/CL/CORRIGENDUM.md@82633a60:37-39` | "*The nonzero modular minor `281079` of integer evaluations proves that `C4_{S1,S2}` and `C4_{S1,S4}` are linearly independent functionals on `span(q_3, q_7)`, hence on all of `M`. Likewise each of them is independent of `C2` on `M` (minors `247396`, `197933`)." | "proves"-from-modular |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:124-127` | "minors with `C2`: `247396`, `197933`; mutual `281079` — all nonzero mod `P` ⇒ pairwise independent over `Q` on `M`; the triple's rank on `M` is `2` or `3` (undecided)." | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:206` | "`C2`, `C4_{S1,S2}`, `C4_{S1,S4}` pairwise independent on `M` ¦ PROVED (nonzero modular minors of integer evaluations)" | PROVED-label |

### D.5 c2_three_rows_rank (475171)
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/CL/CORRIGENDUM.md@82633a60:59-62` | "*Proof of independence.* If `a q_3 + b q_7 + c e = 0`, apply `C`: … ∎ Numerical confirmation: the rows `(q_3, q_7, e)` at the five sealed P6 points have modular rank `3` (minor `475171` on columns `0,1,2`, `checks/c2_three_rows_rank.json`). **Corrected carrier count: `dim span(q_3, q_7, e) = 3`**" | proof + modular confirmation |
| `PB/CL/CORRIGENDUM.md@82633a60:92` | "new F14 ¦ `q_3, q_7, e` linearly independent (PROVED, and modular rank `3` at the P6 points); two further vectors complete the carrier" | PROVED-label |
| `PB/CL/CORRIGENDUM.md@82633a60:102-103` | "`checks/c2_three_rows_rank.py` → `c2_three_rows_rank.json` (plain arithmetic, no wrapper): rank `3`, minor `475171` mod `524287`." | data |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:73-75` | "`C` is injective on `span(q_3, q_7)` and `C e = 0`, `e ≠ 0` ⇒ `q_3, q_7, e` are linearly independent. Modular confirmation: rows `(q_3, q_7, e)` at the P6 points have rank `3`, minor `475171`" | proof + modular |
| `PB/CL/checks/c2_three_rows_rank.py@82633a60:3` | "three is a second, numerical certificate of the independence proved in CORRIGENDUM item K3." | (cites K3; L3 is the item) |

### D.6 b_L = 74
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/ARCHIVE_NOTE.md@82633a60:20` | "`b_L = 74` is proved in `arc_target_dimension_followup`" | proved-label |
| `PB/AT/REPORT.md@82633a60:10-11` | "The grading-preserving Levi bound is `rank C ≤ b_L = 74` — PROVED, exact, by two independent formulations" | exact-integer (LR/Kostka), not modular |
| `PB/AT/REPORT.md@82633a60:138,155` | "### 5.1 The exact count: `b_L = 74` (PROVED)" / "`b_L(11) = 70`, `b_L(12) = 4`, **`b_L = 74`**. Every LR coefficient was computed twice (alternant extraction in five variables; combinatorial LR rule) and asserted equal." | exact |
| `PB/AT/results/b_L_tables.md@82633a60:19,33` | "Totals: b_L(11) = 70, b_L(12) = 4, b_L = 74." / "Agreement with Formulation I: True." | exact |
| `PB/AT/CORRIGENDUM.md@82633a60:17-18` | "`b_L = dim F^L` is computed here with `L` connected, exactly as in B19-01 §6 (REPORT.md §2.3, §3.1): `b_L = 74`." | exact |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:37,80-81` | "`b_L = 74` (PROVED, two formulations) ¦ uninformative" / "`F^L` … has dimension 74 (70 from skew degree 11, 4 from 12)." | PROVED-label |
| `PB/AS/REPORT.md@82633a60:31` | "b_L=74, not a useful improvement on rank C<=4." | inherited |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:211` | "`b_L = dim F_L` ¦ NOT COMPUTED (recipe B19-01 §6)" | pre-dates 74 |

### D.7 Other "global / identically / PROVED / certified" versus sampled statements
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/DF/REPORT.md@82633a60:308,311` | "column-local (19 cyclic shifts) ¦ 19 at 7 points ¦ **all identically zero at the points**" / "priced random + pair-block … ¦ **all identically zero**; rank stays 2" | "identically" for sampled zeros (withdrawn DFA A) |
| `PB/DF/REPORT.md@82633a60:155-156` | "every cheap random contraction vanishes identically at five points." | unqualified (DFA A) |
| `PB/DF/REPORT.md@82633a60:412-413` | "The affordable contraction family has been exhausted twice (rank 2 both times, with 33 identically-vanishing candidates)" | unqualified (DFA A, B) |
| `PB/DF/REPORT.md@82633a60:464,509-510` | "E10 … 33 cheap candidates vanish identically, family rank 2" / "33 of 35 cheap candidates vanish identically at five points" | unqualified (DFA A) |
| `PB/DFA/CORRIGENDUM.md@82633a60:16-21` | "A zero value at finitely many integer points modulo one prime is not a global identity … *The listed candidates evaluated to zero at the recorded points modulo `p = 524287`. No global vanishing, and no upper bound on the span of the affordable contraction family, follows without additional proof.*" | corrects |
| `PB/DF/REPORT.md@82633a60:289-291` | "Therefore `C2(z) = 112 z(K5+S) - 7 z(K5+2S) - 177 z(K5)` vanishes on `E`: **directly checked, `112·798720 - 7·4623360 - 177·322560 = 0`.**" | exact-integer, global on E (dim 1) |
| `PB/DF/REPORT.md@82633a60:189-192` | "Arc `2 x 2` minor `61631 mod 524287` **PRODUCER-CERTIFIED**; the direction (nonzero modular minor of actual forbidden coefficient rows is a characteristic-zero floor) is correct." | correctly-qualified |
| `PB/DF/REPORT.md@82633a60:325-332` | "scaling `a -> t a` gives `q(t) = q_10 + t q_11 + t^2 q_12` … a fourth node `t = 3` was predicted exactly at all three points (**degree control passed**), which also re-confirms the skew-degree bound in this cell on these vectors." | sampled-consistency |
| `PB/DF/REPORT.md@82633a60:354-356` | "`C2` is nonzero on the source (rank 1 on the certified subspace) and vanishes on `E`, so it is a genuinely nonzero necessary condition" | correctly-qualified |
| `PB/DFA/FEASIBILITY.md@82633a60:62-67` | "`t = 0,1,2` determine the forbidden components and `t = 3` is a control node. **This holds for every such point, sparse or not** … Sparse arc points therefore yield valid rows of the forbidden matrix; … zero rows are not evidence of anything." | correctly-qualified |
| `PB/TS/REPORT.md@82633a60:119-122` | "the control that `C4` vanishes **exactly** on the ambient line `H5 o phi` (values of `H5` at `K5 + tS`, `t = 0, 1, 2`, independently recomputed …)" | exact-integer |
| `PB/TS/REPORT.md@82633a60:372-373` | "Each `C4_{S,S'}` is **globally necessary** on `M_(4^5)` (it vanishes on `E` by construction, and the vanishing on the ambient line is checked exactly)." | global-from-exact-generator (K3 wording) |
| `PB/TS/REPORT.md@82633a60:688` | "T8 ¦ explicit `C4_{S,S'}` integer conditions, globally necessary on `M_(4^5)` ¦ B ¦ PROVED (necessity) + VERIFIED (exact zero on `H5` line)" | PROVED-label |
| `PB/TF/CORRIGENDUM.md@82633a60:57-60` | "*Each `C4_{S,S'}` evaluates to zero **exactly on the ambient generator** `H5 ∘ phi` (integer arithmetic), hence on `E = C·(H5 ∘ phi)`; it is therefore globally necessary. Its full kernel on `M` is not determined by this*" | correctly-qualified |
| `PB/TF/REPORT.md@82633a60:333-336` | "Order-two rows in directions `S2`, `S4` are proportional to `C2` on `(q_3, q_7)` (minors `0`, consistent with the sealed Theorem 6.2, which predicts exact proportionality on all of `M`); the `S1` order-two row equals `C2/84` exactly. The vanishing of the `S4` order-four row on both certified vectors and on `H5` is the torus identity of §4.2, observed exactly." | theorem + sampled-consistency |
| `PB/TF/REPORT.md@82633a60:320` | "Exact dependence on the two vectors, had it occurred, would have proved nothing about `M`." | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:117` | "## 5. Transverse formulas (PROVED globally necessary; integer coefficients)" | PROVED-label (exact) |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:142-143` | "The runner is mod one prime; exact rational reconstruction would need several primes" | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:187-189` | "A zero value at finitely many points modulo one prime is **not** a global identity, and no bound on the span of any family was proved: **none of these families is shown exhausted.**" | correctly-qualified |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:205,209-210` | "`C2`, `C4_{S1,S2}`, `C4_{S1,S4}` globally necessary ¦ PROVED (vanish exactly on the generator `e`, hence on `E`)" / "zero-valued contraction candidates are identically zero; a family is exhausted ¦ NOT ESTABLISHED (sampled only) / S0 rows certify `ker C` membership ¦ FALSE in general" | correctly-qualified |
| `PB/RA/REPORT.md@82633a60:72-73` | "the 14 zero-valued ones include **13 with a sign obstruction** (identically zero, PROVED), and both nonzero ones … have no obstruction. One zero-valued candidate (P6 index 10) has no sign obstruction: its vanishing at the five points remains unexplained (MEASURED zero only)." | PROVED (sign theorem) vs MEASURED, qualified |
| `PB/RA/REPORT.md@82633a60:144-146` | "The '`= …`' entries are exact fits modulo `P` of the six values … to `alpha q_3 + beta q_7 + gamma e` …; they are MEASURED identities modulo one prime, not proofs." | correctly-qualified |
| `PB/RA/REPORT.md@82633a60:247-249` | "13 sign-obstructed P6 candidates and 19 P2 candidates vanish identically ¦ PROVED (automorphism sign) … n05, n07, n09 vanish identically ¦ NOT ESTABLISHED (zero at three sampled values only)" | correctly-qualified |
| `PB/RA/REPORT.md@82633a60:251` | "any global arc-kernel identity ¦ NOT PROVED" | correctly-qualified |
| `PB/AT/REPORT.md@82633a60:272-282` | "the determinant of `[φ_i(C q_j)]` is `104967 ≢ 0 mod P` … Since `C(n*) = 0`, … a `2×2` integer system with determinant `D ≢ 0 mod P`; its unique rational solution has denominators dividing `D` and reduces mod `P` to the unique solution of the reduced system, which is `(265391, 275398)` … `D·T(n*) … is an integer congruent to `D·T(n̄) mod P`, … both nonzero, so `T(n*) ≠ 0`. ∎" | conditional-lift (Prop 7.1) |
| `PB/AT/REPORT.md@82633a60:284` | "For `C2`, `C2(n̄) ≡ 0 mod P` proves nothing about `C2(n*)`." | correctly-qualified |
| `PB/DA/REPORT.md@82633a60:43-44` | "A nonzero `2×2` evaluation minor on `(Cq_3, Cq_7)` (`104967` at P7 point 0, `171205` at P6 point 0) fixes `(α, β)` uniquely **if** a global relation exists; it does not prove existence." | correctly-qualified |
| `PB/DA/REPORT.md@82633a60:61-62` | "**Verification (pilot 3, mod `P`):** the twelve half-tensors of `q_3, q_7, n02`, recombined through `B`, reproduce the sealed values at P6 point 0 exactly: `260975, 301718, 386346`." | one-point-mod-P verification of a PROVED factorization |
| `PB/DA/REPORT.md@82633a60:101` | "the 50 recorded points … are poised (evaluation matrix of rank 50), so vanishing at them is vanishing on `cone(V)`." | exact/poised |
| `PB/DA/REPORT.md@82633a60:109-110,130-132` | "evaluated modulo three primes (`524287, 599999, 599993`) and reconstructed exactly by CRT (a-priori bound …). Exact rank of the 18 vectors: **3**." / "CRT-exact (bound `331776·(120·2·2)² = 7.6·10¹⁰ < modulus/2`)" | multi-prime exact |
| `PB/DA/REPORT.md@82633a60:205-207` | "No modular zero is used as a characteristic-zero statement anywhere; the only characteristic-zero rank statements are floors" | correctly-qualified |
| `PB/DA/code/p3_covariant_relation.py@82633a60:11` | "among restricted covariants holds identically on S* iff it holds at the 50 poised slice points (exact integers)." | density-claim |
| `PB/FA/REPORT.md@82633a60:85-88` | "Degree assumption: `u = 14` predicted exactly … Corrupted relation: `(α+1, β)` fails on the rows. `e ∈ ker C` is the inherited global proof (B19-01 §5 …), not a sampled zero." | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:6-8` | "Labels: PROVED (characteristic-zero argument or exact integer computation), CERTIFIED (nonzero modular minor of integer evaluations ⇒ characteristic-zero floor), SAMPLED (finitely many evaluations modulo one prime; no ceiling), OPEN." | label-definitions |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:52` | "Zero-valued contraction candidates (n05, n07, n09; P8 family) are zero at sampled points only." | correctly-qualified |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:65-66` | "## 6. Covariant factorization (PROVED; verified exactly against sealed values)" | PROVED-label |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:86` | "## 8. Astra's five-block redundancy theorem (PROVED globally, `astra_gkz_degenerations_20260917`)" | PROVED-globally (symbolic) |
| `PB/AS/REPORT.md@82633a60:201` | "This is an explicitly defined linear map on polynomials, not a collection of sampled values." | correctly-qualified |
| `PB/AS/REPORT.md@82633a60:229` | "No component with nu<=2d can contribute, so this is the exact identity N_w=L_w C, not just an inclusion observed on samples." | correctly-qualified |
| `PB/AS/REPORT.md@82633a60:248` | "The statement is over characteristic zero on the complete M. It is not a restricted four-column rank assertion, a sampled-kernel claim, or a new rank measurement." | correctly-qualified |
| `PB/AS/REPORT.md@82633a60:303,305` | "These finite checks supplement, and do not replace, the all-degree proofs." / "No zero at finitely many points is promoted to a global identity." | correctly-qualified |
| `PB/AS/MANIFEST.json@82633a60:5` | "proved globally in REPORT.md sections 7-8, independently of finite pilot controls" | PROVED-globally (symbolic) |
| `PB/GKZ/REPORT.md@82633a60:225` | "`e_i = Delta^i Q(11) = 7582, 384540, …` all nonnegative … Hence `Q(k) = sum_{i<=13} e_i C(k-11, i) >= 0` for every integer `k >= 11`, and `r_pad(k) <= r_det(k)` for all `k`. **Theorem A is now PROVED** given Gulliksen-Negard (ADOPTED) and these certificates." | exact-integer certificate |
| `PB/GKZ/REPORT.md@82633a60:227` | "(c) MEASURED (mod `p`, lower bounds on the rational ranks): `rank M_3 = 16 / 10 / 16` and `rank M_4 = 226 / 155 / 256` … P3 then computed `rank_Q M_4 = 226` and `155` exactly, so (A1) at `k = 4` and (A2) at `k = 4` are also CERTIFIED directly." | correctly-qualified |
| `PB/GKZ/REPORT.md@82633a60:229` | "(d) MEASURED (second Koszul differential, mod `p`): `rank D_6 = 120 / 105 / 120` exact mod `p` …; Gram lower bounds `rank D_7 >= 1904 / 1650 / 1920`" | correctly-qualified |
| `PB/GKZ/REPORT.md@82633a60:241` | "**Theorem B is now PROVED** given Kleiman (ADOPTED) and these certificates. (At this pencil the modular caveat does not even arise: the ranks are rational.)" | exact |
| `PB/GKZ/REPORT.md@82633a60:248` | "CERTIFIED consequences (Lemma 3.1 applies verbatim to `D_k` …): (i) the second Koszul differential *does* yield determinant equations in sixteen variables, in degree `k = 7`: … nonzero degree-1905 polynomials in `I(closure GL_16 . det_4)` (nonzero because the sparse random control has full rank 1920)" | exact-over-Q |
| `PB/GKZ/REPORT.md@82633a60:69` | "`rank Hess(per_3) = 9` at a general point of `{per_3 = 0}`, census 2.2, MEASURED there, 40 of 40 clean draws" | correctly-qualified |
| `PB/IC/REPORT.md@82633a60:180` | "> `I(D_5)_6 = 0` is **PRODUCER-CERTIFIED per weight** (batch-13 certificates, identified here), no longer only 'given the measured totals'. Corollary 2.5 holds unconditionally at `d = 6`" | modular-rank-attains-a → vanishing |
| `PB/IC/REPORT.md@82633a60:236-238` | "L9 ¦ `I(D_5)_d = 0` for `d <= 5` ¦ PRODUCER-CERTIFIED (batch-13 rank-attains-`a` certificates, two primes; not replayed) … L11 ¦ `I(D_5)_7 = 0` ¦ MEASURED (batch-13 total-deficit identity; 80 uncertified ambient units of unknown length)" | labels |
| `PB/IC/REPORT.md@82633a60:256` | "The statement `I(D_5)_7 = 0` remains conditional on batch-13's measured totals; the negative is unconditional through `d = 6` and conditional at `d = 7`." | correctly-qualified |
| `PB/SL/REPORT.md@82633a60:262-263` | "This is why check 2 (section 6) *had* to return zeros for the certified `(4^5)` vectors on `X_0`: those zeros are now a theorem, not sampled evidence." | theorem-over-sampled |
| `PB/SL/REPORT.md@82633a60:330,355` | "all values `0`; controls passed … - INCONCLUSIVE as evidence, CONSISTENT with Theorem 4.1" / "(d) Check 2's zeros are consistent with, not evidence for, Theorem 4.1." | correctly-qualified |
| `PB/ED/REPORT.md@82633a60:196-197` | "Rationally reconstruct any modular candidate and check `A v=0` exactly. Merely observing `A v=0 mod p`, or testing extra random determinant points, is insufficient." | correctly-qualified |
| `PB/ED/REPORT.md@82633a60:192` | "Require `det S != 0`. A nonzero reduction modulo a suitable prime suffices to certify this rational nonzero." | correctly-qualified |
| `PB/ED/REPORT.md@82633a60:240` | "The new six-row mechanism is proved and numerically instantiated: `C2(Q^2)!=0` with `C(Q^2)=0`." | exact-integer |
| `PB/ED/PREFLIGHT.md@82633a60:8` | "Both are bounded diagnostics; sampled zero is never a global equation certificate." | correctly-qualified |
| `PB/FC/REPORT.md@82633a60:140` | "An independent modular tensor contraction agrees with its integer values, and a separate Lagrange interpolation implementation reproduces the arc rows obtained by the producer's Vandermonde solve." | verification |
| `PB/FC/PREFLIGHT.md@82633a60:7` | "Nonzero minors prove characteristic-zero rank floors. A sampled kernel is NOT certified as a characteristic-zero kernel." | correctly-qualified |
| `PB/TS/REPORT.md@82633a60:278-279` | "The sealed packet supplies the only Tier-C facts used: `C2 != 0` on `M_(4^5)` and `C_2(Q^2) = -12` on `M_(4^6)`." | inherited |
| `PB/CL/STABILIZER.md@82633a60:6-7` | "Everything below is PROVED unless labelled; the one MEASURED input is the commutant computation of the sealed Check 1 (`A_K5_commutant_dimension = 1`)." | labels |

---

## E. EXHAUSTIVENESS ("only / every / all / cannot / never / no … can") in REPORT.md files, with corrigendum coverage

### E.1 GKZ REPORT.md (covered by SC C1–C12 where noted)
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/GKZ/REPORT.md@82633a60:11` | "the GKZ toolbox contains exactly three things that act on a single quartic's coefficients, and none of them produces a determinant equation that is both new to the programme and nonzero on padding" | withdrawn-by-C8 |
| `:13` | "**Known; repackaged, not new.**" | narrowed-by-C9 |
| `:15` | "**Result: rigorously blind to padding in every degree.** … so every Macaulay minor vanishing on the determinant orbit closure vanishes on the padded-permanent orbit closure. Its contribution to `D = m_pad - m_det` is zero in every cell." | narrowed-by-C1/C4 |
| `:15` | "This is the one GKZ construction that produces determinant-specific information beyond 'singular'" | not-explicitly-covered ("the one") |
| `:17` | "the only `GL_16`-compatible content is lower bounds `m_det >= m_{in_Gamma(det_4)}` … **Rejected by the early tests of section 4**" | partly-C8(E)/C12 ("only" not addressed) |
| `:19` | "The recommendation (section 8) is to stop the GKZ route as a source of equations." | restated-by-C11 |
| `:62` | "So the Cayley method's non-determinantal output, restricted to `d_1`, is precisely the programme's Macaulay-minor family" | not-covered (definitional) |
| `:70` | "The Chow form of `Sing X_F` is not polynomial in `F`. **Nothing here is new to the programme.**" | narrowed-by-C9 |
| `:86` | "these can only kill cells, never open them. **Rejected** (section 4)." | not-explicitly-covered ("never") |
| `:90` | "Candidate 2 … It is the only candidate that (a) acts on `F` alone …, (b) is `GL_N`-equivariant by construction, (c) …, and (d) admits a complete answer with the tools at hand." | not-covered ("the only candidate") |
| `:90` | "if true, every Macaulay-minor determinant equation vanishes on padding and the route is closed; if false at some `k`, the size-`(r_k(Y_det)+1)` minors of `M_k` are determinant equations nonzero on padding." | narrowed-by-C1 |
| `:110` | "Consequently every minor of every Macaulay matrix `M_k` that vanishes on `closure(GL_16 . det_4)` vanishes on `closure(GL_16 . z per_3)`, in every degree and every `GL_16`-type, i.e. in every cell `(d, lambda)` of every length." | withdrawn/narrowed-by-C1 |
| `:134` | "Consequently every Macaulay minor vanishing on `D45`, in every degree `k` …, vanishes identically on `P5 = { ell C }` and hence on every actual five-variable padding restriction." | narrowed-by-C2 |
| `:159` | "The extraneous content is instead total: by Theorems A and B, `Y_pad subset Z_{k, r_k(Y_det)}` for every `k`" | not-explicitly-covered |
| `:159` | "any functional monotone in that quantity inherits the inequality (this is the record's own formulation …, now proved rather than measured at `N = 5` and extended to `N = 16`)." | not-covered |
| `:164` | "There is no unproved transition on this path; the path ends in zero." | narrowed-by-C4 |
| `:170` | "for `V = X_F`, no: it is LMR" | narrowed-by-C9 |
| `:173` | "**yes, and now proved in all degrees**: `J_{ell C} subset (ell, C)` (Theorems A, B)" | narrowed-by-C1/C2 |
| `:177` | "none: contribution to `D` is zero in every cell" | narrowed-by-C4 |
| `:179` | "candidate 3 is the only place signs enter, and it does not survive the invariance test." | not-covered ("only place") |
| `:183` | "none is known below `delta_0 >= 8`, none is known to be nonzero on padding, and by Theorem B none of the Macaulay family ever is." | withdrawn-in-part-by-C10 |
| `:188` | "They agree where they overlap: the cap is the first known equation at `k = 7`, degree 300, and it is blind." | corrected-by-C10 |
| `:266` | "coincides with the programme's Macaulay-minor / Jacobian-cap family and is rigorously blind to padding" | narrowed-by-C4 |
| `:268` | "Theorem A (all Macaulay degrees, sixteen variables, every cell of every length …), Theorem B (all Macaulay degrees, five variables …), … the classification of candidate 1 as LMR." | narrowed-by-C4/C9 |
| `:274` | "the *whole* complex, not just its first differential, is subject to the same wrong-way comparison" / "It adds no new determinant equation nonzero on padding, and it cannot: the three GKZ mechanisms are … The one GKZ object that separates in the right direction, the dual variety of `X_F`, is LMR" | withdrawn-by-C5/C8 |
| `:276` | "zero for the negative (it is proved); expanding any Macaulay or Koszul minor (degree 300, 227, 1905, ...) is out of scope and, by Theorems A-B, pointless for separation." | retained-in-C11 |
| `:278` | "a negative answer (not blind at `D_8`) would contradict the monotonicity that the Hilbert-function comparison makes overwhelmingly likely" / "for completeness only, since no separating equation can come from a wrong-way statistic" / "the census already shows the only right-way family" | withdrawn-by-C6/C11 |

### E.2 Astra REPORT.md (no corrigendum; SC C12 records "not broadened")
| `PB/AS/REPORT.md@82633a60:3` | "**Outcome C: this restricted family adds no forbidden-weight conditions beyond the existing arc.**" | proved-scope |
| `:7` | "This is a classification of initial forms for this restricted torus, not of actual paths up to every equivalence, and not of all determinant degenerations." | correctly-scoped |
| `:11-15` | "**on the full certified source M, every test constructed here factors through C**. … `ker(C,T,N) = ker(C,T), rank(C,T,N) = rank(C,T).` … The corresponding statement holds in every degree and polynomial source label, under the explicit hypotheses below." | proved (Thm 8.1-8.2) |
| `:17` | "It does not cover equations among allowed jets, descent between different parameter points of a limit fiber, special-locus cancellations …, anisotropic weights inside a block, or different matrix-coordinate bases. None of those are ruled out." | correctly-scoped |
| `:19` | "**Funding decision:** stop enumerating weights or coherent triangulations for this five-block family. No further computational certificate is needed" | decision |
| `:63` | "The argument therefore applies to the full M of the user's diagnostic, not just its four known vectors." | proved-scope |
| `:143` | "This is the complete finite initial-form classification of the chosen family: four vertices, four edges, one full face. … There remain infinitely many actual one-parameter weight paths." | complete-within-family |
| `:153` | "We do not claim that no such family could ever be realized by a different GL_16 map." | correctly-scoped |
| `:223` | "Theorem 8.1 (interval tests). For every permitted w there is an explicit linear map L_w … such that N_w=L_w C on M. Moreover the simultaneous kernel of all N_w is ker C." | proved |
| `:244-248` | "Corollary 8.3 … Any stack N of the interval or exact-support tests satisfies rank(C,T,N)=rank(C,T), ker(C,T,N)=ker(C,T). All rows of N lie in the row space of C." | proved |
| `:252` | "Nothing about the unknown fifth vector can change this." | proved-scope |
| `:274` | "**No unverified load-bearing external theorem remains in the selected result.**" | self-assessment |
| `:283` | "The candidate endpoint is not symmetry-equivalent to the old universal endpoint, but is an iterated face limit and adds no condition." | proved |
| `:322` | "Any future degeneration proposal must leave this block-scalar torus … give its own actual-orbit map, and price that new comparison separately." | decision |

### E.3 Image-ceiling REPORT.md (no corrigendum; ARCHIVE_NOTE:16 notes §0 item 4 says `d <= 5` vs proved `d <= 6`)
| `PB/IC/REPORT.md@82633a60:5` | "the restriction-to-reducible-pencils bound can never certify a gap there, for any source rank `rho_L`." | not-covered |
| `:17` | "The route cannot certify a gap in the proposed regime. … **polynomials of degree below `delta_0` cannot tell determinantal products `l * C_det` from arbitrary products `l * C`.**" | not-covered |
| `:22` | "Nothing short of an explicit low-degree equation of the six-nodal cubic threefolds revives the route." | not-covered |
| `:81` | "the restriction of `D_5` to a 4-plane is `D_4 = ` all cubic surfaces (Beauville …), … `I(D_5)` is concentrated at `ell(mu) = 5`" | adopted |
| `:95` | "the 1+3 restriction bound cannot certify a gap in any cell of that degree." | not-covered |
| `:109` | "By Corollary 2.5 the deficit is zero wherever `I(D_5)_d = 0`, so in that regime no value of `rho_L` helps." | not-covered |
| `:111` | "The stabilizer comparison `a_3 > s_3` is the only character-computable source of `i_3 > 0`; batch-13 measured that it never fires at length 5 through degree 10" | not-covered ("only") |
| `:142` | "In the programme's proposed regime … the route cannot improve the existing bound. This is the precise negative result requested." | not-covered |
| `:199` | "The only sharpening of the padding ceiling available through the 1+3 image is the Pieri transport of the ideal of the six-nodal cubic threefolds" | not-covered ("only") |
| `:200` | "A five-row cell `(d, lambda)` can carry a positive 1+3 deficit only if (i) `d >= delta_0` … and (ii) …" | not-covered |
| `:206` | "**the restriction-to-reducible-pencils bound cannot identify a structurally promising five-row cell, and cannot certify a gap, at any degree the programme can carry.** … for `Z = D_5` this is the whole story of the 1+3 locus." | not-covered |
| `:210` | "Everything on the record points the other way: `delta_0 >= 8` given the measured totals, `delta_0 = 65` conjectured, and the only known equations cost 65 (Jacobian cap) and 80 (discriminant)." | not-covered (GKZ C10 distinguishes det_3 δ_0) |
| `:218` | "A cell where `u_L < m_pad` at `d <= 6` would require `I(Y_L)_d != I(Y_pad)_d` …; with `I(D_5)_d = 0` this is impossible." | not-covered |
| `:222` | "Do not pursue the 1+3 restriction bound further in any degree the programme can carry; retire it as a gap route with this negative on file." | decision |

### E.4 Singular-locus REPORT.md (no corrigendum)
| `PB/SL/REPORT.md@82633a60:171-172` | "Hence the only tuples in `Z` that can carry a nonzero `G`-invariant are those whose span `X` is nondegenerate of generic rank exactly 3 and is not sub-compression." | proved (Lemmas 3.1-3.2) |
| `:211-213` | "H-EH … is **false**; `Mt` and `X_0` are explicit counterexamples" | proved |
| `:219` | "By Lemma 3.3 these are the only two shapes that occur." | conditional-on-EH (C1, C3) |
| `:224-228` | "**Theorem 4.1.** … Every element of the `S_lambda`-isotypic component … vanishes identically on `Z`. Hence `rho_Z = 0` in every five-row cell" | proved, "conditional only on C1" |
| `:264-266` | "The same argument with `m` matrices and `l(lambda) = m >= 5` gives `rho_Z = 0` in every cell with at least five rows in any `m`-variable model" | proved (Remark ii) |
| `:300-305` | "But under the group that matters for five-row functions the answer is **no**: for every 5-dimensional singular `G`-semistable `X` the tensor is `SL5 x G`-unstable" | proved |
| `:358-364` | "Theorem 4.1 shows every five-row full-`H` function vanishes on `Z`, so `Z` can never supply a five-row determinant constraint, in five or more variables. Nothing on `Z` can be 'certified nonzero in a named full-`H` cell' with five rows; the route is closed, not reopened." | proved-conditional-on-C1/C3 |
| `:343` | "C3 ¦ No later correction alters EH section 1 ¦ NOT VERIFIED" | residual |

### E.5 Transverse-structure REPORT.md (sealed; governed by TF K1–K9 and CL L1–L6)
| `PB/TS/REPORT.md@82633a60:34-36` | "that in five variables a **single** order-two condition exists …, that it is the verified `C2`, and that **every other order-two direction is redundant with it** (a theorem, §6.3)" | not-covered (Thm 6.2 stands) |
| `:42` | "No positive gap is claimed, and none is possible in any cell touched (§8)." | not-covered |
| `:47-49` | "six variables carry exactly one E-free condition through order four (the known one) and five variables carry one order-two condition (`C2`, unique in all directions) plus at most four further E-free order-four conditions." | narrowed-by-K2 (E-free redefined) |
| `:239-240` | "`r = 6`: `[t^2] z(K + tS) = z(K) alpha_2(S)` for **every** `z` and every symmetric `S` (`j_2(6) = 0`). … there is no order-two transverse datum at all in six variables." | not-covered (stands) |
| `:426-430` | "(a) Every globally necessary linear condition on `M_lambda` that is built from Taylor coefficients of order `<= 4` …, and without using knowledge of `A_{d,lambda}` beyond its covariance, factors through `j` and vanishes on `L_max`." | corrected-by-K2 |
| `:450-451` | "Order two: **no condition exists** for any `z`, any direction (Cor. 4.6.2). The attachment's silence claim is a theorem." | not-covered (stands) |
| `:452-455` | "there is **exactly one E-free condition** (up to scale), and it is the verified `C_2` … **No second pair of directions, no non-scalar symmetric direction, and no mixed jet can add an E-free condition of order `<= 4` at `K6`.**" | narrowed-by-K2/K7 |
| `:461-462` | "**at least `9 - 2 = 7` of the nine false survivors of `(6,(4^6))` are invisible to every jet condition of order `<= 4` at `K6`**, whatever carrier is built." | retained-by-K7 |
| `:469-479` | "there is **exactly one E-free order-two condition**, and it is `C2` … identically on `M_(4k)^5` … So the active session's `C2` is *the* order-two transverse test at `K5`, in every direction and for every `k`." | not-covered (Thm 6.2 stands) |
| `:480` | "**up to five E-free conditions in total**, one of them `C2`, hence **up to four genuinely new order-four conditions**" | narrowed-by-K2/K8(T12) |
| `:494` | "All five-row cells with `d <= 5` are excluded anyway (`D <= 0`), so the first non-rectangular candidates are at `d = 6`." | not-covered |
| `:524-529` | "jointly they have rank `<= 1`, whatever `D`. Adding order-two directions never adds rank. … Hence at most **four** of the `D - 1` order-four identities can be independent, and adding directions beyond five is pointless." | not-covered |
| `:570-572` | "`C = 0` on the source (B19-01 Thm 4.1), so every nonzero necessary functional acts nonzero on `ker C = M`. Independence is automatic" | not-covered |
| `:580-582` | "then `ker C = E`, and *every* necessary condition — `C2`, all `C4`, anything else — is redundant. A theorem of redundancy, not a witness." | not-covered |
| `:592-596` | "A **redundancy theorem** without computation is not available … Redundancy can only be established as in route 1, or by `T` vanishing on a certified spanning set of `ker C` (corrigendum D)." | not-covered ("only") |
| `:604-605` | "**no transverse condition can lower the clipped bound below `a` there**, and none can anywhere unless an equation exists." | not-covered |
| `:618-619` | "`N_5 = V(2w_1 + w_2)` of `Sp_4` (one order-two condition, `C2`, unique up to scale in all directions and all `k`; up to four further E-free conditions at order four)." | narrowed-by-K2 |
| `:641-642` | "if a nonzero `4 x 4` forbidden minor certifies `rank C = 4`: **outcome (2)** for every transverse condition, by the theorem `ker C = E` (redundant with the arc, whatever `rank T` is)" | not-covered |
| `:659-662` | "Equivalently, the source jet map `j : M_(4^5) -> J_{<=4} = C^7` is injective, i.e. the order-`<= 4` transverse conditions at `K5` have rank exactly `4` on the source and their common kernel is `E`." | corrected-by-K4 |
| `:664-666` | "If true, the transverse family alone certifies the determinant coordinate subspace in this cell, the arc is redundant with it, and 'independence from `C`' reduces to `rank C < 4`." | conflation-corrected-by-K4 |
| `:189,232-234` | "`N` is the unique `Stab^0`-stable complement" / "The finite parts of `Stab` … act trivially on `Sym^{even}(N^*)`, so these are the counts for the full stabilizer." | justified-by-K6, proof replaced by L1/STABILIZER |
| `:691-693,698` | "T10 ¦ six-row: no order-two condition; exactly one E-free order-`<=4` condition; `>= 7` survivors invisible … PROVED / T11 … PROVED / T12 … PROVED / T17 ¦ no transverse condition lowers `B` below `a` where `m_det = a`; no padding content ¦ PROVED" | T12 replaced-by-K8 |
| `PB/TS/drafts/REPORT_body_draft.md@82633a60:275-286,299-302,317,355-357,365-366,389-390,414` | duplicates of the sealed lines above (draft superseded per TS:726-727); e.g. `:414` "Either way no gap and no arc statement follows." | superseded-draft |

### E.6 Transverse follow-up REPORT.md (governed by CL L1–L6)
| `PB/TF/REPORT.md@82633a60:10-12` | "fourth-order compatibility certified independent of `C2` on the known source subspace; arc independence open" | stands |
| `:93-94` | "As `L ⊆ V ∩ L_max`: `rank F_free ≤ rank F_E`, with equality iff `V ∩ L_max = L`." | proved |
| `:114-116` | "a certified rank `4` of `T` on `M` therefore proves `ker j = 0`, the spanning, and (for E-free `T`) `V ∩ L_max = L` all at once, whereas `ker j = 0` by itself proves none of the spanning." | proved |
| `:122-125` | "**these evaluations need not span the five-dimensional `(Sym^4 N_5^*)^{Sp_4, *}`** — spanning is an OPEN finite question … Only general symmetric directions (degree up to `20` in `t`, eleven even nodes) can supply the rest." | not-covered ("Only") |
| `:171-172` | "`Stab_Gamma(K) = {…}` is a connected double cover of the connected group `G_r` …, hence connected: there are no further components inside `Gamma`." | corrected-by-L1 |
| `:225-229` | "**`[t^4] z(K5 + t S4) = 0` for every `z ∈ M`** — the E-using `S4` row is identically zero on `M` … proves `z = 0` there for every `z ∈ M`" | proved (torus) |
| `:243-244` | "the Kronecker description `M = (S_(4^5) W)^H`, `dim = 5`, offers no product structure (`M_(e^5) = 0` for `e < 4` since `5e` must be divisible by `4`)." | not-covered |
| `:256-257,347-349` | "Cost: the basis (three more certified vectors …)" / "which in practice needs a certified complete carrier (three more independent vectors)" | corrected-by-L3 (two) |
| `:314-317` | "the rank of `{C2, C4_{S1,S2}, C4_{S1,S4}}` on `M` is only known to be `≥ 2`" | reworded-by-L2 |
| `:349-351` | "or a rank-four forbidden minor (then `ker C = E` and every transverse condition is redundant with the arc, closing the question negatively)." | not-covered |

### E.7 Descent follow-up REPORT.md (governed by DFA CORRIGENDUM A–F)
| `PB/DF/REPORT.md@82633a60:24-25` | "the 2+2 partial-transpose family is provably blind on every even five-row rectangle." | not-covered (FC theorem) |
| `:33-34` | "No positive gap is claimed anywhere in this document, and none can be: every cell touched is a known no-gap cell." | not-covered |
| `:155-156` | "every cheap random contraction vanishes identically at five points." | corrected-by-A |
| `:179-180` | "no linear condition factoring through that family, of any jet order, sees the nine missing dimensions. Transverse information is required." | not-covered |
| `:195` | "**VERIFIED (re-derived): `D_(4k)^5 = 0` on the full source.**" | not-covered |
| `:211` | "**This version can never yield a gap.**" | not-covered (E19 PROVED) |
| `:217` | "The proposed `(4^6)` pilot **cannot improve the determinant bound** and is withdrawn." | not-covered |
| `:241-242` | "**The cell is excluded for a positive gap without any two-vector rank computation.**" | not-covered (E21) |
| `:308,311` | "**all identically zero at the points**" / "**all identically zero**; rank stays 2" | corrected-by-A |
| `:344` | "**no arc-kernel vector lies in the certified subspace.**" | not-covered |
| `:412-414` | "The affordable contraction family has been exhausted twice (rank 2 both times, with 33 identically-vanishing candidates); the next family needs `4^14`-entry intermediates (2 GiB) per contraction" | corrected-by-A/B |
| `:427-433` | "The rectangles are the only five-row cells where (i) the full-`H` source is `SL5`-invariant …; (iv) the `2+2` fibre family is provably blind, so any detection would be genuinely new information about the arc." | not-covered ("only") |
| `:438-441` | "Either a `4 x 4` forbidden minor (arc exact at `k = 1`: then no necessary condition, `C2` included, can add anything there …)" | scope-restricted-by-C |
| `:443-446` | "A nonzero `4 x 4` minor … kills the 'false survivor' hypothesis in this cell in one modular computation. Conversely `C2(n) = 0` on an exact kernel vector kills the transverse map as a detector in this cell (not in general)." | second-sentence-corrected-by-D |
| `:464,509-510` | "33 cheap candidates vanish identically, family rank 2" / "33 of 35 cheap candidates vanish identically at five points." | corrected-by-A |
| `:384-386` | "detected by two independent globally necessary conditions …, both replayed here." | corrected-by-E |

### E.8 Extension-descent REPORT.md (no corrigendum; reviewed in DF §A)
| `PB/ED/REPORT.md@82633a60:5` | "Its rank is exactly one, while the old map has rank zero. This removes a false survivor but leaves the clipped determinant bound equal to one." | proved |
| `:7` | "an exact determinant nonzero proves that this cell contains no determinant equation." | proved (a=1 inherited) |
| `:37` | "Consequently no source vector has a forbidden exponent at `d=6`." | proved (B19-01 Thm 4.1) |
| `:57` | "It is an identity on all matrix tuples. It is valid on singular tuples, on arbitrary frames, and on every function of the original affine closure. It needs no normality, no exhaustive chart cover, and no geometric conjecture." | proved |
| `:137-139` | "We have detected one of the nine missing dimensions, not certified that this one functional detects all nine. … no exhaustive minimality claim over all possible cells/tests is made." | correctly-scoped |
| `:166` | "The resulting map has rank nine exactly. Generic existence is proved above; that carrier/basis computation was not performed here." | conditional |
| `:184` | "Hence `h` vanishes on every actual determinant representation. Its zero set is closed, so it vanishes on `D45=closure(im phi)` … Conversely every equation of `D45` has this zero pullback." | proved |
| `:236` | "The cheap negative rules out **only this degree-six representation cell**." | correctly-scoped |
| `:242` | "In every already-certified cell with `ker C=E_lambda`, any globally necessary `C2` must vanish on `ker C`; it cannot add constraints there." | proved |
| `:244` | "The six-row success does not predict a degree, a partition, or `D>0` for five rows." | correctly-scoped |

### E.9 Fiber-compatibility REPORT.md (no corrigendum)
| `PB/FC/REPORT.md@82633a60:5` | "It also proves that this entire family is blind on every five-row rectangle `(4k)^5`. No positive five-row increment over the arc is claimed." | proved |
| `:45` | "The explicit nonzero below proves that our two tuples are not related by the full stabilizer. … it does not prove independence from `C`." | correctly-scoped |
| `:112` | "This is stronger than merely failing to find a witness: no globally necessary additional test can remove an arc survivor in this cell, because there are none." | proved (rank 2 = dim) |
| `:131-134` | "This proves `D_(4k)^5 = 0` on the entire full-stabilizer source, for every `k>=1`. The same complement argument proves blindness on even rectangles with more than four rows … Other equal-quartic families are not ruled out." | proved; scoped |
| `:144` | "This check rules out only that proposed multiplier, not products or cancellations in general." | correctly-scoped |

### E.10 Route A REPORT.md (governed by AT CORRIGENDUM C1–C4)
| `PB/RA/REPORT.md@82633a60:13-15` | "every forbidden row tested … has rank 2 on `(q_3, q_7, n02)`, so no `rank C ≥ 3` or `= 4` certificate exists" | stands (qualified) |
| `:65-66` | "Hence `sign(g) = −1` for one such `g` forces `P_{pi,rho} ≡ 0`. Likewise a `g` with `g(pi) = rho`, `g(rho) = pi` and sign `−1` forces `P_{pi,rho} + P_{rho,pi} ≡ 0`." | proved |
| `:75-78` | "The 19 P2 'column-local shift' candidates are all obstructed by the transposition case … So the previously unproductive families were mostly identically zero for a provable reason" | proved |
| `:152` | "all 21 minors `4×4` containing `q_3, q_7` vanish." | sampled |
| `:191-192` | "(rank exactly 3, the maximum for three rows). This closes the 'rank 2 or 3' question of CORRIGENDUM L2." | stands |
| `:277-278` | "Route A is not settled: no nonzero `4×4` (or `3×3`) forbidden minor exists on any tested columns, and the fifth source direction was not found within the cap." | stands |
| `:284-288` | "Compute `b_L = dim F_L` … with the three scalar conditions and the transposition component from `STABILIZER.md`" | corrected-by-AT-C1 |
| `:289-295` | "if `b_L = 2`, … Outcome B follows … if `b_L = 3`, `rank C ≤ 3 < 4` and a survivor exists … if `b_L ≥ 4`, Route A remains possible" | withdrawn-by-AT-C2 |
| `:224` | "`n := n02 − 265391·q_3 − 275398·q_7 (coefficients modulo P; no small-height rational lift found)`" | reworded-by-AT-C3 |

### E.11 Arc-target REPORT.md (governed by DA CORRIGENDUM C1)
| `PB/AT/REPORT.md@82633a60:10-13` | "it is far too weak to decide anything … No upper bound below 4 is obtained. Transverse independence from the arc is therefore NOT proved here, neither existentially nor by a witness." | stands |
| `:102-103` | "Hence **no element of `τH^0` preserves the grading; `L ⊆ H^0` is connected and the B19-01 count is an `L`-invariant count.**" | proved |
| `:112` | "the characters of `GL_3 × (C*)³` trivial on `L` are exactly the powers of `φ`" | proved |
| `:171-172,175` | "the Levi target does not track `C(M)`." / "so the bound adds nothing to `rank C` (Case C)." | stands |
| `:284-288` | "a proof needs `dim F'' = 2`, or a target of dimension 2 containing `C(S)`, or exact multi-prime evaluation of the forbidden components on a spanning set of `F^L` (priced in the parent as unaffordable)." | narrowed-by-DA-C1 (not the only route) |
| `:292-296` | "If it is ≥ 4: the unipotent constraints are also insufficient and only exact arithmetic remains." | narrowed-by-DA-C1 |

### E.12 Direct-arc REPORT.md (governed by DA CORRIGENDUM C2–C3)
| `PB/DA/REPORT.md@82633a60:17-18` | "(i) every same-pairing paired contraction factors as a symmetric pairing `B(X_H, X_{H'})` of two-column covariants" | proved |
| `:41` | "`(∗)` for some `(α,β)` ⟺ `rank_Q(C¦_U) = 2`" | proved |
| `:48-49` | "Route 2 … needs an explicit 74-vector basis and about 2 900 runner evaluations (≈ 22 min): not affordable" | priced |
| `:84-86` | "**no** isotypic component of `ν_1∧ν_2∧ν_3∧Z_1∧Z_2` vanishes for all `Z_1, Z_2 ∈ W'` … No covariant is forced to have vanishing top by this argument." | proved (exact) |
| `:134-135` | "**the tops are linearly independent; the proportional-tops mechanism is false.**" | proved (C3) |
| `:148-149` | "Nothing here excludes `rank C¦_U = 3` either: no new full-row functional was evaluated" | stands |
| `:153` | "Either of the following would finish the question:" | not-covered ("Either") |
| `:163-164` | "only degree-11 rows can contribute, so the minor must use at least two degree-11 rows. This is cheap per point but cannot prove `rank 2`." | rests-on-sampled-rank-1 (flag) |
| `:166` | "if all `3×3` minors remain zero the evidence is strengthened only, and route 1 is required." | not-covered ("required") |

### E.13 Final-arc REPORT.md and CURRENT_DIAGNOSTIC_STATE.md
| `PB/FA/REPORT.md@82633a60:28-29` | "any new row violating the relation would give a nonzero minor with two inherited rows." | stands |
| `:37-38` | "Accordingly no five-block weights were enumerated, no face degeneration sought, no alternative endpoint assumed independent." | scope |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:10` | "**The cell has `a = m_det = 1`. Nothing here is or can become a positive multiplicity obstruction.**" | stands |
| `:62-63` | "it is not a completeness statement (one recorded zero, P6 index 10, is unexplained)." | correctly-scoped |
| `:76` | "hence the 'proportional tops' mechanism for `rank(C¦_U) = 2` is refuted." | proved |
| `:92-93` | "Consequence: no more five-block weights, no stronger test from face degeneration in that family." | Astra-scope |
| `:121` | "the paired families tried so far live in `span(q_3, q_7, e, n02)`." | unqualified (RA:182-183 MEASURED mod P) |
| `:131-132` | "None of it is, or can be turned into, a multiplicity obstruction in this cell (`a = m_det = 1`); a positive gap would require a cell with `a > m_det`, which this cell is not." | stands |
| `:144-146` | "Reopening this diagnostic is justified only by (a) …, or (b) …, or (c) a cell with `a > m_det`" | decision ("only") |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:171-172` | "if `b_L = 4`, Route A and Route B are the two exhaustive outcomes." | superseded-by-b_L=74 (not explicitly withdrawn in CL; AT C2 covers RA only) |
| `PB/CL/STABILIZER.md@82633a60:84-85` | "No element with `epsilon = 1` outside the parametrisation exists (the Claim is an iff), and every `epsilon = tau` element is `tau'` times one of them; this exhausts `S`." | proved (one MEASURED commutant input) |

---

## F. `D = -1` / `D <= 0` / `(4^5)` / `m_pad = 0` / `m_det = 1` wording

### F.1 In the archive (82633a60)
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `PB/DF/REPORT.md@82633a60:239-242` | "`h` vanishes on `R135 = closure{l·C}` by (P3), so `i_pad >= 1` and `m_pad <= a - 1 = 1`. Hence `D = m_pad - m_det <= 1 - 1 = 0`. **The cell is excluded for a positive gap without any two-vector rank computation.**" | D<=0 at (8,4,4,4,4), d=6 |
| `PB/DF/REPORT.md@82633a60:475` | "E21 ¦ `(8,4,4,4,4)` at `d = 6` has `D <= 0` ¦ PROVED on (P1) MEASURED, (P2) VERIFIED, (P3) PROVED by Pieri" | D<=0 |
| `PB/DF/REPORT.md@82633a60:28-29` | "`d = 5`, `lambda = (4^5)`, `s = 5`, `a = 1`, `m_det = 1`." | m_det=1 |
| `PB/DF/REPORT.md@82633a60:64` | "Cell `d = 5`, `lambda = (4,4,4,4,4)`, conjugate heights `(5,5,5,5)`: four columns of height five, twenty slots." | (4,4,4,4,4) |
| `PB/DF/REPORT.md@82633a60:252` | "## C. The one authorized five-row diagnostic: `d = 5`, `lambda = (4,4,4,4,4)`" | (4,4,4,4,4) |
| `PB/DF/REPORT.md@82633a60:261` | "`m_det` ¦ 1 ¦ **1** ¦ `H5(det K5) = 322560 != 0` at the actual pencil `K5` (P3), independently of B19-02's three points" | m_det=1 |
| `PB/DF/REPORT.md@82633a60:399,456` | "In `(5,(4^5))`: `s = 5`, `g = 6`, `a = 1`, `m_det = 1` recomputed" / "E2 ¦ `m_det(5,(4^5)) = 1` ¦ VERIFIED independently (`H5(det K5) = 322560`) and PRODUCER-CERTIFIED (B19-02, reviewed)" | m_det=1 |
| `PB/DFA/CORRIGENDUM.md@82633a60:6,62,110` | "**INCONCLUSIVE on five-row arc exactness at `d = 5`, `lambda = (4^5)`.**" / "uses `s = 5` and `m_det = 1` of the present cell" / "`s = 5`, `g = 6`, `a = 1`, `m_det = 1` (P1, P3; controls passing);" | m_det=1 |
| `PB/DFA/FEASIBILITY.md@82633a60:1,167` | "# Sparse-evaluator feasibility at `d = 5`, `lambda = (4^5)` — one cell only" / "`a = m_det = 1`, `2 <= rank C <= 4`" | (4^5); m_det=1 |
| `PB/IC/REPORT.md@82633a60:146` | "Hence `m_det >= 1`, `i_pad >= 1`, `m_pad <= a - 1 = 1`, `D <= 0`. **Excluded.**" | D<=0 at (8,4,4,4,4) |
| `PB/IC/REPORT.md@82633a60:20` | "The `d = 6` cell `(8,4,4,4,4)` is excluded by the reviewed H5 multiplication argument before any consideration (section 4)" | excluded |
| `PB/IC/REPORT.md@82633a60:188` | "`d = 5` (6 of 23): `(9,7,2,1,1)`, `(8,7,3,1,1)`, `(7,7,4,1,1)`, `(7,4,4,4,1)`, `(6,4,4,4,2)`, `(4,4,4,4,4)`." | (4,4,4,4,4) inert-list |
| `PB/GKZ/REPORT.md@82633a60:15` | "Its contribution to `D = m_pad - m_det` is zero in every cell." | D-sign m_pad−m_det (C4) |
| `PB/GKZ/REPORT.md@82633a60:164` | "hence contributes equally to `i_det` and `i_pad` and contributes `0` to `D = i_det - i_pad`." | D-sign i_det−i_pad |
| `PB/GKZ/SC/CORRIGENDUM.md@82633a60:54,58` | "Then `D = i_det - i_pad = (i_det - i_common) - (i_pad - i_common)`. … This does **not** prove `D = 0` in any cell" / "No cell's `D` is asserted to be zero by this packet." | D not asserted |
| `PB/GKZ/SC/REVISED_VERDICT.md@82633a60:24` | "They do not show that `D = 0` in any cell" | D not asserted |
| `PB/TS/REPORT.md@82633a60:494` | "All five-row cells with `d <= 5` are excluded anyway (`D <= 0`), so the first non-rectangular candidates are at `d = 6`." | D<=0 (all d<=5) |
| `PB/TS/REPORT.md@82633a60:391,434,624` | "specific to `s = 5`, `m_det = 1` at `k = 1`." / "`2` for `r = 6` and `6` for `r = 5` when `a = m_det = 1`." / "Cell `(5, (4^5))`, `a = m_det = 1`, `s = 5`." | m_det=1 |
| `PB/TS/drafts/REPORT_body_draft.md@82633a60:317,215,259,408` | "All five-row cells with `d <= 5` are excluded anyway (`D <= 0`)" / "`s = 5`, `m_det = 1` at `k = 1`." / "`a = m_det = 1`." / "`(5, (4^5))`, `a = s_det = 1`, `s = 5`" | D<=0; note `s_det` typo in draft |
| `PB/TF/REPORT.md@82633a60:23-24,33` | "`E ⊆ M` the determinant coordinate subspace (dim `m_det = 1`, generator `H5 ∘ phi`)" / "This cell has `a = m_det = 1` and cannot yield a positive gap." | m_det=1 |
| `PB/TF/CORRIGENDUM.md@82633a60:5` | "Notation: `M = M_(4^5)`, `E ⊆ M` the determinant coordinate subspace" | (4^5) |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:7-8` | "Cell facts (all certified in the sealed packets): `s = 5`, `g = 6`, `a = 1`, `m_det = 1`, `2 ≤ rank C ≤ 4`, no positive gap possible (`a = m_det`)." | m_det=1 |
| `PB/CL/SOURCE_HANDOFF.md@82633a60:62` | "`work/batch15_workers/B15-02/results/b19_02/rect_4_4_4_4_4.json`" | rect_4_4_4_4_4 certificate |
| `PB/CL/CORRIGENDUM.md@82633a60:50-51` | "`H5` is the unique (up to scale) element of `A_{5,(4^5)}` (`a = 1`, Weyl alternant, sealed P1 and B19-02 `rect_4_4_4_4_4.json`)" | (4^5) |
| `PB/RA/REPORT.md@82633a60:1,21,49,297` | "# Source-vector experiment, cell `d = 5`, `lambda = (4^5)`" / "This cell has `a = m_det = 1` and cannot produce a positive multiplicity gap." / "`s = dim M = 5`, `g = 6`, `a = m_det = 1` ¦ PROVED (sealed)" / "**Reminder.** This cell has `a = m_det = 1`…" | m_det=1 |
| `PB/AT/REPORT.md@82633a60:27,51,261` | "**Standing reminder.** `a = m_det = 1` in this cell: no positive multiplicity gap is possible." / "`d = 5`, `λ = (4^5)`." / "Nothing here is a multiplicity obstruction (`a = m_det = 1`)." | m_det=1 |
| `PB/AT/CORRIGENDUM.md@82633a60:56` | "the standing reminder that `a = m_det = 1` and no positive multiplicity gap is possible in this cell." | m_det=1 |
| `PB/AT/results/b_L_tables.md@82633a60:3` | "Cell d = 5, lambda = (4^5). L = grading-preserving Levi." | (4^5) |
| `PB/DA/REPORT.md@82633a60:30` | "**Standing reminder.** `a = m_det = 1`: no positive multiplicity gap is possible in this cell." | m_det=1 |
| `PB/FA/REPORT.md@82633a60:20` | "**Standing reminder.** `a = m_det = 1`: no positive multiplicity gap is possible in this cell." | m_det=1 |
| `PB/FA/CURRENT_DIAGNOSTIC_STATE.md@82633a60:1,10,131-132` | "# Current diagnostic state — the `d = 5`, `λ = (4^5)` source-vector sequence" / "**The cell has `a = m_det = 1`. Nothing here is or can become a positive multiplicity obstruction.**" / "a positive gap would require a cell with `a > m_det`, which this cell is not." | m_det=1 |
| `PB/AS/REPORT.md@82633a60:67,294` | "In the diagnostic k=d=5, lambda=(4,4,4,4,4), dim M=5, E=span(e), e=H5 o phi, and a=m_det=1." / "4. Positive multiplicity gap: **not produced**; the diagnostic has a=m_det=1." | (4,4,4,4,4); m_det=1 |
| `PB/AS/PREREG.md@82633a60:24` | "The current five-row diagnostic has dim M = 5, E = span(e), and a = m_det = 1." | m_det=1 |
| `PB/ED/REPORT.md@82633a60:17` | "We prove the first cell's `m_det=1` afresh below by an exact ambient nonzero. The latest B19-02 report/review closes the degree-five rectangle and records `I(D45)_d=0` for all `d<=5`. That latest review, rather than the older '22 determined, one bounded' statement, is the input used here." | m_det=1 (six-row); (4^5) closure inherited |
| `PB/ED/REPORT.md@82633a60:116,226` | "it spans `A_{6,(4^6)}` and proves `m_det=1`." / "Therefore `m_det=1=a` and `I(D45)_{6,(12,8,2,1,1)}=0`." | m_det=1 (other cells) |
| `PB/ED/REPORT.md@82633a60:206` | "For `a=1`, a nonzero determinant equation gives `m_det=0`; a padding nonzero gives `m_pad=1`, hence `D=1`." | D=1 hypothetical |
| `PB/SL/REPORT.md@82633a60:262,309` | "the certified `(4^5)` vectors on `X_0`" / "the two certified full-`H` vectors `q_3, q_7` of `M_(4^5)`" | (4^5) |
| `PB/IC/REPORT.md@82633a60:26,249` | "the separate session testing a sparse evaluator for `(5,(4^5))`" / "The separate session's `(5,(4^5))` sparse-evaluator work was neither read nor touched." | (4^5) |
| (no occurrences) | The strings `D = -1`, `D=-1`, `m_pad = 0`, `m_pad=0` do **not** occur anywhere in the archive at 82633a60 (all files, case-insensitive). `D ≤ 0`/`D <= 0` occurs only in the lines listed above. | absent |

### F.2 In the worker commits
| file@commit:line | verbatim quote | tag |
|---|---|---|
| `docs/b19_02_report.md@75ddb900:443` | "points — and the rectangle `(4^5)` had `m_det` undetermined, its inherited exclusion" | (4^5) |
| `docs/b19_02_report.md@75ddb900:445` | "So `h` would have to live in `(4^5)`. **That cell is closed in §8.1 below.** ∎" | (4^5) |
| `docs/b19_02_report.md@75ddb900:459` | "raising operators `E_12, E_23, E_34, E_45` ¦ source weight `(4,4,4,4,4)` dim 19834, target weights `(5,3,4,4,4)` etc., each **target dim 17329, 51723 nonzero entries**" | (4,4,4,4,4) |
| `docs/b19_02_report.md@75ddb900:470-473` | "A nonzero exact integer value at an actual determinant point gives `m_det >= 1 = a`, hence `i_det = 0` in `(4^5)`. The three padding values were all zero, which I use for **nothing**: a sampled zero proves nothing, and the inherited padding ceiling `U = 0` already gives `m_pad = 0` in this cell." | m_det floor→value; U ceiling→m_pad=0 |
| `docs/b19_02_report.md@75ddb900:475` | "So Corollary 8.1 holds with no exception: **`I(D45)_d = 0` for all `d <= 5`.**" | consumes |
| `docs/b19_02_review.md@75ddb900:21` | "`a = 1` and `K = 19834` at `(4^5)` ¦ matches what I computed during the B18-01 review" | (4^5) |
| `docs/b19_02_review.md@75ddb900:39` | "## 2. The result: `(4^5)` is closed, and the family is now fully determined" | (4^5) |
| `docs/b19_02_review.md@75ddb900:41-42` | "`(4^5)` at `d = 5` was excluded by padding vanishing — `i_pad = 1 = a`, so `m_pad = 0` — with `m_det` unknown. §8.1 settles it:" | i_pad=a→m_pad=0 |
| `docs/b19_02_review.md@75ddb900:49` | "**fully determined: 22 cells at `D = 0`, one at `D = -1`.** That is the correct form for" | D=-1 |
| `docs/b19_02_review.md@75ddb900:51` | "yesterday — that `m_det` at `(4^5)` was knowable and unknown." | (4^5) |
| `docs/b19_02_review.md@75ddb900:98` | "`rect_cell_det_multiplicity` ¦ `(4^5)` at `d = 5` has `m_det = 1 = a`, by exact nonzero integer evaluation of the unique highest-weight vector (`K = 19834`) at three determinant points. With `m_pad = 0` from B18-01 Prop 8.4, **`D = -1`**. The degree-five five-row family is fully determined: 22 cells at `D = 0`, one at `D = -1` ¦ PROVED; `a` and `K` recomputed here" | D=-1; m_det=1; m_pad=0 |
| `docs/b19_02_review.md@75ddb900:108` | "1. State `D = -1` at `(4^5)` explicitly; the report stops at `i_det = 0`." | D=-1 |
| `docs/b18_06_sweep_review.md@0a236381:11-15` | "I first wrote that all 23 cells close at `D = 0` exactly. That is true of 22. The rectangle `(4^5)` is excluded by *padding vanishing* — B18-01 Prop 8.4 gives `i_pad = 1 = a`, hence `m_pad = 0` and `D <= 0` — and says nothing about `m_det`, which remains undetermined. The uniform statement across the family is `D <= 0`; `D = 0` holds in 22 of 23." | D<=0; m_pad=0 |
| `docs/b18_06_sweep_review.md@0a236381:36-38` | "The determinant evaluation alone gives `m_det = 1`, hence `i_det = 0`, hence `D <= 0`. The slot ran the padding evaluation too and got `m_pad = 1`, so `i_pad = 0` and **`D = 0` exactly** in all nineteen. Both legs are sampled *nonzeros*, the one direction that certifies." | m_det=1→D<=0 |
| `docs/b18_06_sweep_review.md@0a236381:98` | "**22 of them have `D = 0` exactly** … with `a = 1`, `m_det = 1` and `m_pad = 1`, so `i_det = i_pad = 0`. The 23rd, the rectangle `(4^5)`, has only `D <= 0`: it is excluded by padding vanishing (`i_pad = 1 = a`, so `m_pad = 0`), and **its determinant multiplicity `m_det` is undetermined**. The uniform statement across all 23 is `D <= 0`." | D<=0; m_pad=0 |
| `docs/b19_05_intake.md@e3aa25b4:37-38` | "with `D = 0` exactly in 26 of the 27 and `D <= 0` in the rectangle `(4^5)`. These are the only cells in the admissible range 5–10 closed" | D<=0 |
| `docs/b19_05_intake.md@e3aa25b4:81` | "**CLOSED-Z** : closed by `i_pad = a` (padding side vanishes), `D <= 0` with" | D<=0 |
| `docs/b19_05_intake.md@e3aa25b4:90-91` | "every `lambda` with `ell(lambda) <= 4`, every `d` ¦ `K_det ⊆ K_pad`, so `D <= 0` … every `lambda` with `ell(lambda) > 10`, every `d` ¦ `m_pad = 0`, so `D = -m_det <= 0`" | D<=0; m_pad=0 |
| `docs/b19_05_intake.md@e3aa25b4:189` | "(4,4,4,4,4) ¦ 1 ¦ 5 ¦ **0** ¦ **0** ¦ unknown ¦ **0** ¦ `<= 0` ¦ B18-01 Prop. 8.4 (null cone, `i_pad = 1 = a`), independently `T = 0` in the census ¦ CLOSED-Z" | D<=0 |
| `docs/b19_05_intake.md@e3aa25b4:265-266` | "*Padding vanishing* (`i_pad = a`): `m_pad = 0`, so `D = -m_det <= 0`. ✓ for `(4^5)` and for `ell > 10`." | m_pad=0; D<=0 |
| `docs/b19_05_intake.md@e3aa25b4:345` | "All 23 degree-five and 4 degree-six five-row cells are closed at cell level; 26 with `D = 0` exact, `(4^5)` with `D <= 0`" | D<=0 |
| `docs/b19_12_ledger.md@f008ac39:110` | "F11 ¦ … own wording corrected: 22 at `D = 0`, `(4^5)` at `D <= 0` only" | D<=0 |
| `docs/b19_12_ledger.md@f008ac39:130-132` | "22 at `D = 0` exactly (19 swept, …); the rectangle `(4^5)` at `D <= 0` only, by padding vanishing (`i_pad = 1 = a`, so `m_pad = 0`), its" | D<=0; m_pad=0 |
| `docs/b19_12_ledger.md@f008ac39:222` | "(4,4,4,4,4) ¦ 1 ¦ census (`s - a = 4`) ¦ **0** ¦ none ¦ 0 (`U = 0`: no gate) ¦ **<= 0** only; `m_det` undetermined ¦ padding vanishing, `m_pad = 0` (B18-01 Prop 8.4)" | D<=0; m_pad=0 |
| `docs/b19_12_ledger.md@f008ac39:258,269` | "Length at most 4: `D <= 0` in every degree (B17-03). Closed." / "Length above 10: `m_pad = 0` (B17-03). Closed." | D<=0; m_pad=0 |
| `docs/b19_12_ledger.md@f008ac39:369` | "(4,4,4,4,4,4) ¦ 6 ¦ 1 ¦ 10 ¦ 13 ¦ **unknown** … ¦ **0, PROVED by 01 (Thm 4.1)** ¦ `>= 10` if `U >= 1`; unreachable since `b = 0` ¦ unknown (`<= 1`) ¦ … ¦ **NOT A CANDIDATE by this arc**: `B = min(a, s - b) = 1 = a`; an `m_det`, `m_pad` computation would decide `D` but the arc cannot" | b=0 used as value (six-row) |
| `docs/b19_12_ledger.md@f008ac39:375` | "rectangle `(4^5)_5` had `m_pad = 0` by padding vanishing; whether the six-row" | m_pad=0 |
| `docs/b19_12_ledger.md@f008ac39:705-708` | "### 7e.4 §4b correction — the last degree-five cell is closed, and `D = -1` / §4b carried `(4,4,4,4,4)` as the one cell of the degree-five family with `m_det` **undetermined**, closed only at `D <= 0` by padding vanishing." | D=-1; D<=0 |
| `docs/b19_12_ledger.md@f008ac39:721-722` | "A nonzero exact integer at an actual determinant point gives `m_det >= 1 = a`, so `m_det = 1` and `i_det = 0`." | floor→value |
| `docs/b19_12_ledger.md@f008ac39:728` | "(4,4,4,4,4) ¦ 1 ¦ census (`s - a = 4`) ¦ 0 ¦ none ¦ 0 (`U = 0`: no gate) ¦ **0** ¦ **1** ¦ **−1** ¦ `m_pad = 0` by padding vanishing (B18-01 Prop 8.4); `m_det = 1` by B19-02 §8.1" | D=-1; m_pad=0; m_det=1 |
| `docs/b19_12_ledger.md@f008ac39:730-732` | "`D = -1` is the **integrator's arithmetic on the slot's measurement**: the report stops at `i_det = 0` and does not state `D`. Recorded with that attribution." | D=-1 attribution |
| `docs/b19_12_ledger.md@f008ac39:734-739` | "It is **fully determined: 22 cells at `D = 0` exactly, one at `D = -1`.** … The §2c item 2 wording ('the rectangle `(4^5)` at `D <= 0` only, its `m_det` undetermined') is superseded." | D=-1 |
| `docs/b19_12_ledger.md@f008ac39:741-743` | "Three padding values in that cell were sampled zero. The report uses them for nothing and so does this ledger: a sampled zero is not an identity, and `U = 0` already gives `m_pad = 0` (roadmap correction 5)." | U-ceiling→m_pad=0 |
| `docs/b19_12_ledger.md@f008ac39:814` | "`b19_02_rect.py`, the `(4^5)` cell, `K = 19834` ¦ 02 ¦ MEASURED ¦ 19.7 s, 123 MiB, exit 0 ¦ the computation that closed the degree-five family" | (4^5) |
| `docs/b19_12_ledger.md@f008ac39:880` | "`D = 0`, `(4^5)` at `D = -1` — and **`I(D45)_d = 0` for every `d <= 5`**," | D=-1 |
| `docs/b19_12_ledger.md@f008ac39:913` | "to find: `D <= 0` in every degree at length at most four, and `m_pad = 0`" | D<=0; m_pad=0 |
| `docs/b19_12_ledger.md@f008ac39:964-965` | "the `D = -1` arithmetic at `(4^5)`; the loose `K_A = 69` (7e.4), which carries nothing." | D=-1 |
| `docs/b19_12_ledger.md@f008ac39:1017-1022` | "`(4,4,4,4,4)` at `d = 5`: `a = 1` (in-script Weyl alternant), weight space 19834, … three exact nonzero values at determinant points. Hence `m_det = 1 = a`, `i_det = 0`. With the inherited `m_pad = 0`:" | m_det=1; m_pad=0 inherited |
| `docs/b19_12_ledger.md@f008ac39:1026` | "(4,4,4,4,4), `d = 5` ¦ 1 ¦ 5 ¦ 0 ¦ **1** (was unknown) ¦ 0 ¦ **= -1** (was `<= 0`) ¦ padding vanishing (B18-01) + determinant evaluation (B19-02 §8.1)" | D=-1 |
| `docs/b19_12_ledger.md@f008ac39:1028-1030` | "So, if slot 02's certificate stands review, every one of the 23 degree-five five-row cells has exact `D`: 22 at `D = 0` and one at `D = -1`; and Corollary 8.1 (conditional on LLV and 03-A) reads `I(D45)_d = 0` for all `d <= 5` with no exception." | D=-1 conditional |
| `docs/b19_12_ledger.md@f008ac39:1088` | "degree-five cell `(4^5)` closed with `D = -1` exactly, so the first" | D=-1 |
| `docs/b19_12_ledger.md@f008ac39:1107` | "Claim 6.1 of 02, or the `(4^5)` certificate — the decision is re-read from" | (4^5) |
| `docs/b19_12_ledger.md@f008ac39:1166` | "`(4^5)` at `D = -1` ¦ unreviewed ¦ integrator-accepted; `D = -1` is the integrator's arithmetic on the slot's measurement" | D=-1 unreviewed |

---

Coverage notes (extraction only, no verdicts): (1) `m_pad = 0` and `D = -1` never appear in the archive itself; the archive's `(4^5)` packets consistently write `a = m_det = 1` and "no positive gap possible", and the only `D <= 0` lines are the `(8,4,4,4,4)` exclusion (DF B.9, IC §4) and TS:494/draft:317 ("all five-row cells with d <= 5 … D <= 0"). (2) The "padding" object in GKZ Theorem B / SC C2 / CLAIM_SCOPE_TABLE row 2 / DF B.9 / IC §2.1 / ED §5 is the five-variable general-product cone `P5 = R135 = {ell·C}`; in GKZ Theorem A and P3 it is the sixteen-variable `z·per_3` with six idle `w` variables. (3) `b_L = 74` is an exact LR/Kostka integer count (not modular); the modular statements are the 4×4/3×3/2×2 minors (floors) and the 14-functional relation (sampled). (4) Items in E marked "not-covered" are `only/every/cannot` statements whose packet corrigendum does not name them; items marked "stands" are ones the corrigenda explicitly leave unchanged.