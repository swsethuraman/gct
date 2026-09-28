# Batch 28 — board

Written by the integrator on 2026-09-24 and approved by the user. It follows `BATCH27_CLOSE.md`
(`0e55ca6b…`), which is committed at `96a8074d`. The Batch 27 operating model carries over:
- slot branches;
- one setup pass and one close pass;
- review folded into each wave;
- the bounded compute allowance (≤10 runs of ≤60 s and ≤512 MB each).

The only exception is B28-01, whose resources are set in §0 and in its brief.

## §0 — The user's decisions (2026-09-23/24)

| item | decision |
|---|---|
| Cell A (`(12,8,6,4,2)` at k=8) | **YES, Cell A only.** Cell B stays unrun. The run follows B27-06's `PREREGISTRATION.md` (`96a8074d:results/b27_06/`, folder `b713ca8b…`) |
| Host for B28-01 | The user's laptop, under WSL2 Ubuntu 24.04.5 with `.wslconfig` `memory=28GB`, `swap=8GB`. Verified: 27 GB total, 8 GB swap, 20 cores |
| Installs | **Allowed for B28-01 only, inside WSL only**: `build-essential`, NumPy/SciPy and `python-flint`. Every version recorded. Nothing installed on the Windows side |
| READ slot | **YES, in Batch 28** |
| B27-04b | **YES, in Batch 28.** The integrator drafts exact wording and the author approves it before B28-04 launches |
| R27-K4 any-degree lemma | Astra check, in Batch 28 |
| Image-bound research slot | **Not in Batch 28.** It waits until a producer names a rank-preserving contraction of the s56 Foulkes map and prices it |
| Coordinator's Batch 27 seal | Committed in the **Batch 28 close pass** (PART 28), so it does not block the start |

## Slots

| slot | lineage | question | depends on |
|---|---|---|---|
| **PART 27** | Claude Code (housekeeping) | Create 6 slot branches and worktrees, plus the `b28_*` attribute rule | — |
| **B28-01a** | Claude Code | Cell A **build and calibrate**: determinant-only driver, independent verifier, controls, the two recorded calibration cells, a repriced Cell A estimate. **Stops before the target** | PART 27 |
| **B28-02** | Astra | **READ**: (a) known methods for multiplicities in the generated subalgebra of left-right semi-invariants; (b) first-order boundary points of `det₄` orbit closures and class (iii) | PART 27 |
| **B28-03** | Astra | Cross-lineage check of R27-K4's any-degree lemma | PART 27 |
| **R28-01** | Astra, fresh session | Review of B28-01a's driver, verifier and calibration | 01a has pushed |
| **B28-01c** | Claude Code | Apply R28-01's repairs P1–P5 (stop paths, certificate checks, verifier time/memory in the gate, aggregate monotonic cap); add the failure-branch controls; refreeze. No Cell A | R28-01 (YES after repairs) |
| **R28-01b** | Astra | Re-review of B28-01c's repairs only | 01c has pushed |
| **B28-01d** | Claude Code | Fix the launch supervisor (P5a whole-group kill; P5b post-exit size and deadline checks). No Cell A | R28-01b (NO: P5 only) |
| **R28-01c** | Astra | Check P5a/P5b only | 01d has pushed |
| **B28-01b** | Claude Code | Cell A **measurement**, under the preregistration's gates and certificate rules | R28-01c says YES **and the user's go** |
| **R28-01d** | Astra | Cross-lineage check of B28-01b's FULL_RANK at Cell A: re-run the frozen verifier once (host sleep verified off) | B28-01b has pushed |
| **B28-04** | Claude Code | **B27-04b**: apply the six approved editorial items to Papers 2 and 3 exactly as worded | PART 27 **and the user's approval of the wording** |
| **Close** | integrator + coordinator | Integrator compiles the papers and writes the close; PART 28 merges and commits the Batch 27 and Batch 28 seals; the coordinator seals | all above |

B28-02 is READ-only and changes no record, so it needs no review. B28-03 is itself the
cross-lineage check. B28-04 applies author-approved wording, and the integrator compiles its
after-states.

**Achievement ceiling for Cell A.** A certified drop shows only that an equation **exists** in
that cell. Before the binding constraint could change, the equation must be exhibited exactly and
evaluated nonzero at a certified padding point, `T*` or `T′`. That would be separate, priced work.

## Order

1. **PART 27** runs first, alone.
2. **First wave, all at once:** B28-01a, B28-02, B28-03. Each uses its own worktree.
3. **As 01a pushes:** R28-01. **After R28-01 ACCEPTs and the user says go:** B28-01b.
4. **When the wording is approved:** B28-04. Its brief is written then.
5. Close.

## Launch line

Every session uses the same line; replace `<FILE>`.

```
Read C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch/B28_COMMON.md, then C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch/<FILE>, and carry it out. The user authorizes this slot now. Do your own preflight; if anything does not match the brief, stop and report.
```

## Brief hashes (raw SHA-256)

| file | sha256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `HOUSEKEEPING_B28_PART27_SETUP.md` | `52c174ac2d7a028a9b06386036a3a2d97d701fdcf006c21a475b361369322cf2` |
| `B28-01a.md` | `3975e63fbf3873e01ea4f64a6bb43a1d009cdaa5d39ea0d37b09f624419307b5` |
| `B28-02.md` | `ac957649f624f59e69e98f4ea6635f6849ea6c3ac2758dfffc81e4e65a201158` |
| `B28-03.md` | `57adf8a3937f01dfdebd46e2223b878b66c9b45932f36ca00f854e92cda2ef59` |
| `R28-01.md` | `57904854afc6be2e9c7385e6131eb4cc0a67b988e7d3dc3f8d069a9249b134ef` |

| `B28-01c.md` | `d4c7909fa3fe13981562e34fe1f4160d01bc0ad55702feb536ae227305368b93` |
| `R28-01b.md` | `5952741b70b9370802c3bc897c1e6bc7af874046f4ff2d35717398220b6e1165` |
| `B28-01d.md` | `e26a0914ef65e63af7f14078151cc33bfc06453fde53740ca551d219b7c7b240` |
| `R28-01c.md` | `947405cefedc81b425263c356d318c506a1d5b2b3e4ee72e4ac1f1c85b2ddbdc` |
| `B28-01b.md` | `66cd584e5e9726bb427da14d2dc768a6f342f59c6896287f0f23e9e4918b482f` |
| `R28-01d.md` | `388da3404e8f1550858ef8976ed81fc15fa647053db4caae4d02ac98e6f17510` |
| `B28-04.md` | `8f2213af031198efa547aa889ab9c0af4a7964001999be64c4e690be8e6d637f` |
| `B27_04B_WORDING_DRAFT.md` (approved in full by the author, 2026-09-28) | `5d8f40124402c298321450c7ab31c192276655e5767665ec50a29f6f09d38663` |

R28-01 (`8a86fec1`) returned **YES after repairs**; B28-01c implemented them and R28-01b (`93db0679`) accepted P1–P4 but returned **NO** on P5 (supervisor stop enforcement), which B28-01d (`0f7af8b1`) fixed and R28-01c (`ff62d929`) accepted: **B28-01b may launch: YES**, subject to the user's go. The B27-04b wording was approved in full on 2026-09-28; B28-04 applies it. R28-01 may re-run B28-01a's controls and one calibration cell under WSL (≤1 h, ≤8 GB, no installs), with the user's authorization given at launch.

## Standing

- **Binding constraint:** "No five-row determinant equation is known to be nonzero on padding."
- **Programme decision:** "no construction ready."
- **Certified padding test points:** `T*` and `T′`. `p₄` is retired.
- **Integrator suggestions:** 0 for 4. Every question above is typed, and producers choose their
  methods.
