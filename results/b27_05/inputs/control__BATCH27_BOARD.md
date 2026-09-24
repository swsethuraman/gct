# Batch 27 — board

Written by the integrator, 2026-09-23. It follows `BATCH26_CLOSE.md` (`c2a4a187…`). The user
approved the operating changes on 2026-09-23: producers commit to their own slot branches, a
bounded exact/symbolic compute allowance, ladders of questions within each slot, and review
folded into each wave. The user accepted all editorial patches.

**Aim:** more research and less process. There is one setup pass at the start and one merge pass
at close, and no per-slot delivery passes.

## Slots

| slot | lineage | question | depends on |
|---|---|---|---|
| **PART 25** | Claude Code (housekeeping) | Create 10 slot branches and worktrees, plus the attribute rule | — |
| **B27-01** | Astra | Where a separating witness can live: map, smooth `per₃`, degree window | PART 25 |
| **B27-02** | Astra | An unpaired or mixed-sign contraction, gated on an escape paragraph | PART 25 |
| **B27-03** | Claude | A25-10 reopening condition at a nonsymmetric `T′`: exact kernel at low degree | PART 25 (uses B27-01's `T*` if available) |
| **B27-04** | Claude | Editorial pass on Papers 1–3 (accepted edits) | PART 25 |
| **R27-K4** | Claude | Review of B26-10A §2.3 (general degree-4 extension) | PART 25 |
| **R27-01 / 02** | Claude | Review of B27-01 / B27-02 | that producer has pushed |
| **R27-03** | Astra | Review of B27-03 | B27-03 has pushed |
| **Close** | integrator + coordinator | I compile the papers and write the close; one merge pass; the coordinator seals | all above |

## Order

1. **PART 25** runs first, alone.
2. **Then all five at once:** B27-01, B27-02, B27-03, B27-04, R27-K4. Each uses its own worktree.
3. **As each producer pushes:** launch its reviewer.
4. **To me after each run:** send the final message. I verify the tip, blobs and manifest in one
   check per wave.

## Launch line

Every session uses the same line. Replace `<FILE>`, and for the R27-0N reviews add "Your slot is
R27-0N."

```
Read C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch27_launch/B27_COMMON.md, then C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch27_launch/<FILE>, and carry it out. The user authorizes this slot now. Do your own preflight; if anything does not match the brief, stop and report.
```

## Brief hashes (raw SHA-256)

| file | sha256 |
|---|---|
| `B27_COMMON.md` | `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee` |
| `HOUSEKEEPING_B27_PART25_SETUP.md` | `aeb41a4b62b84dcc873cd0b96a5416ac629abe038618a616fc8cf6ac23138a04` |
| `B27-01.md` | `ce5a7910fbc913fffd52924f1c98707d3970392fe979259bfb9e2931baf18b8b` |
| `B27-02.md` | `8dbb0a0d1bd56fd5a1c5995254cf6c200b3f45698635f3f3f3daf6cbd42635d5` |
| `B27-03.md` | `b48370b0c99f96e57d2ebe633cb8852877cbd78c8d90455fc4948ebb663e1579` |
| `B27-04.md` | `165f3a62706f406258cc3fac00084126deb59f046830b93dee963738268d20ea` |
| `R27-K4.md` | `59043481ae85a595db9b5187b927a5f21667f4464805795e69c9f98d5e967a27` |
| `R27-REVIEWS.md` | `916de53ab8c31c3d4242a84d8a894ce9ceecc75d76ef83dea8d4d87b3edddaa9` |

## Standing

- **Binding constraint:** "No five-row determinant equation is known to be nonzero on padding."
- **Programme decision:** "no construction ready."
- **Integrator suggestions:** 0 for 3. Every question above is typed, and producers choose their
  own methods.
