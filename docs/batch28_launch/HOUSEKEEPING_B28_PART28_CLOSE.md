# Batch 28 — PART 28: the close pass (merge, fast-forward, commit the close records)

**STATUS: READY.** Run this in a Claude Code session in **default permission mode**. It is the
only delivery pass at the close of Batch 28. It assesses no mathematics, and edits no packet,
paper, ledger or seal. The ceiling is 60 minutes. **It follows PART 26 exactly**
(`docs/batch27_launch/HOUSEKEEPING_B27_PART26_CLOSE.md` @ `96a8074d`) except where this file
differs.

Read `batch28_launch/B28_COMMON.md` for conventions. **In this pass only**, the Git prohibitions are
lifted for exactly:
- `git merge --no-ff` into `batch15-launch` (28a);
- fast-forward-only updates of two paper branches (28b);
- one content commit on `batch15-launch` (28c);
- `git merge --abort` after a conflict;
- fast-forward pushes (28d).

No `-f`, `-A`, `+refspec`, rebase, amend, reset, clean, checkout, or `.gitattributes` /
`.gitignore` edit. Run every Git command as `git -C <worktree>`.

## §0 — Author decisions (given 2026-09-28)

| item | decision |
|---|---|
| 28a — merge the four research and review branches into `batch15-launch` | **YES** |
| 28b — fast-forward the two paper base branches to B28-04's tips | **YES** |
| 28c — commit the close records on `batch15-launch` | **YES** |
| 28d — push the three updated branches, fast-forward only | **YES** |
| Coordinator's Batch 28 ledger | **NOT in this pass**; it goes in the first Batch 29 delivery pass |
| Slot branches `b28-*` | left as they are |

## Preflight

1. Record the raw SHA-256 of this file, of `B28_COMMON.md` and of `BATCH28_CLOSE.md`. The last
   must be `7429fb1f1245019fccd19d8d4f5fad9f00361992f1424baa3d6835d1bbf20c62`.
2. Run `git fetch`, then `ls-remote` every branch below. Everything must be level with origin.
3. `batch15-launch` must be at `96a8074d240033161302233672aed5980d84eccb`, and the paper bases
   at the tips in 28b. If a base has moved, stop the part that uses it.
4. For each slot branch:
   - its first-parent chain back to its setup commit must contain only the commits listed;
   - `git diff --name-only <setup>..<tip>` must list only that branch's slot output paths, as
     bound by the manifests below.

   If either fails, stop that row.
5. Use `work/batch15` for `batch15-launch`, as PART 26 did. It must show no tracked
   modifications.

## 28a — merge into `batch15-launch`, in this order

| # | branch | tip | setup | commits (setup → tip) |
|---|---|---|---|---|
| 1 | `b28-02` | `fd001ddb5cd8486d7f6fafb9002f6dbc94325187` | `9daf22c5` | `fd001ddb` |
| 2 | `b28-03` | `e0a8041ba7026cd7502a10a1eebf8a7d35491115` | `b0863403` | `e0a8041b` |
| 3 | `b28-01` | `467e8402478bca64923c0a1a852bd0efee331356` | `c0122f57` | `a1c3c3a6` → `5a3174cd` → `0f7af8b1` → `467e8402` |
| 4 | `b28-01r` | `1b9c2295ac8460186a838d91d003a4d519e6097a` | `ee354b57` | `8a86fec1` → `93db0679` → `ff62d929` → `1b9c2295` |

**Manifests to re-check at each tip** from committed blobs (`git show <tip>:<path>`), comparing
every payload's SHA-256 and bytes:

| path | raw hash |
|---|---|
| `results/b28_02/MANIFEST.json` | `eedb53739d63c22bcd0dfaceed11d547187ef788794c8226cd9d01570db031d1` |
| `results/b28_03/MANIFEST.json` | `ab09c3fdda92916c005aaf90a6cd836af22edef5ecd838c3c6833c72959e749e` |
| `results/b28_01/MANIFEST.json` | `420eb69ab49165338cfe9afab87f02ecb4ffc9d270b2fcc50ce2acb8172b934e` |
| `results/b28_01c/MANIFEST.json` | `93bb78e2f4bee90ec668c6c957689571052761860b5556d41bd67641f278254a` |
| `results/b28_01d/MANIFEST.json` | `2129631d0b9189c4bd21a6ebafb8b148ff49dfb94829d9ad6adda9eaf66d3d90` |
| `results/b28_01b/MANIFEST.json` | `9beba33cce900aed46940d25eacf535820c379385c2a3225d9f944541a45f314` |
| `results/b28_01r/MANIFEST.json` | `5ffcc018b5e5a29effb2e31dc3e4ac171b13a5e9d7ad63816a3dd250544eb8a6` |
| `results/b28_01rb/MANIFEST.json` | `5068e6cdabfb0d578bb5c1c5f3d02ba36f15542e5c3bcfba63cae5bd1266d4b4` |
| `results/b28_01rc/MANIFEST.json` | `66eb68fc311b475a9bdf6b92431646ec10cf3ed43061d89f6f3f78ad6ee45f99` |
| `results/b28_01rd/MANIFEST.json` | `76f41c381baa906c7fbb0ed4943b6eaf0f4bad773f792132a962932c50745bc4` |

**For each merge:**
- `git merge --no-ff --no-edit -m "Batch 28 close: merge <branch>" <branch>`.
- The setup commits each append the same three `b28` attribute lines, so they merge cleanly.
- **On any conflict:** `git merge --abort`, stop 28a at that row, and report.
- After each merge, confirm two parents, and that each `b28` attribute line appears exactly once.

## 28b — fast-forward the paper branches

| base | now | fast-forward to | manifest on the tip |
|---|---|---|---|
| `b24-06-paper2` | `f8326974…` | `b28-04-p2` @ `11e99b258b42465c3b7a9a415a211d4939bdca87` (setup `65060dea`) | `4036bea41f222e75f60a7fa6c72c24a01bdc5a7da222e861a3fe91f5e1d7a27e` |
| `b23-04-paper3` | `4c5a5450…` | `b28-04-p3` @ `181214bc1d7bab7b4d7fcd13e37fcde66802bd79` (setup `ff1d4772`) | `b653306a61c5e9ef99692d25ed39258d3ef562f3148d852f0ddffe5f39ffca91` |

Run `--ff-only` in the base's own clean worktree, or `git fetch . <src>:<dst>` with no `+`. A
non-fast-forward is a stop for that row. The integrator has already compiled both after-states
clean (16 and 24 pages).

## 28c — one content commit on `batch15-launch` (after 28a)

The source folder is `Claude_Handover_B15_B18\post_b19_housekeeping_20260917\`. Copy each file
byte for byte, then re-hash the copy. All of these sources are LF with 0 CR; stop if any is not.

| destination | source | raw SHA-256 |
|---|---|---|
| `docs/batch_closes/BATCH27_LIVE_LEDGER.md` | `BATCH27_LIVE_LEDGER.md` (the coordinator's seal) | `45a0a0ec20cf898c8d2f887c20ae48e95dc331cbfd262845d80b96001a709f8d` |
| `docs/batch_closes/BATCH28_CLOSE.md` | `BATCH28_CLOSE.md` | `7429fb1f1245019fccd19d8d4f5fad9f00361992f1424baa3d6835d1bbf20c62` |
| `docs/batch28_launch/B28_COMMON.md` | `batch28_launch/` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `docs/batch28_launch/BATCH28_BOARD.md` | same | `ba404fd0a2c9686e76701e9f3e84681b7806bca8d198d23127a8c46d77f149b6` |
| `docs/batch28_launch/HOUSEKEEPING_B28_PART27_SETUP.md` | same | `52c174ac2d7a028a9b06386036a3a2d97d701fdcf006c21a475b361369322cf2` |
| `docs/batch28_launch/HOUSEKEEPING_B28_PART28_CLOSE.md` | this file | record in the report |
| `docs/batch28_launch/B28-01a.md` | same | `3975e63fbf3873e01ea4f64a6bb43a1d009cdaa5d39ea0d37b09f624419307b5` |
| `docs/batch28_launch/B28-01b.md` | same | `66cd584e5e9726bb427da14d2dc768a6f342f59c6896287f0f23e9e4918b482f` |
| `docs/batch28_launch/B28-01c.md` | same | `d4c7909fa3fe13981562e34fe1f4160d01bc0ad55702feb536ae227305368b93` |
| `docs/batch28_launch/B28-01d.md` | same | `e26a0914ef65e63af7f14078151cc33bfc06453fde53740ca551d219b7c7b240` |
| `docs/batch28_launch/B28-02.md` | same | `ac957649f624f59e69e98f4ea6635f6849ea6c3ac2758dfffc81e4e65a201158` |
| `docs/batch28_launch/B28-03.md` | same | `57adf8a3937f01dfdebd46e2223b878b66c9b45932f36ca00f854e92cda2ef59` |
| `docs/batch28_launch/B28-04.md` | same | `8f2213af031198efa547aa889ab9c0af4a7964001999be64c4e690be8e6d637f` |
| `docs/batch28_launch/R28-01.md` | same | `57904854afc6be2e9c7385e6131eb4cc0a67b988e7d3dc3f8d069a9249b134ef` |
| `docs/batch28_launch/R28-01b.md` | same | `5952741b70b9370802c3bc897c1e6bc7af874046f4ff2d35717398220b6e1165` |
| `docs/batch28_launch/R28-01c.md` | same | `947405cefedc81b425263c356d318c506a1d5b2b3e4ee72e4ac1f1c85b2ddbdc` |
| `docs/batch28_launch/R28-01d.md` | same | `388da3404e8f1550858ef8976ed81fc15fa647053db4caae4d02ac98e6f17510` |
| `docs/batch28_launch/B27_04B_WORDING_DRAFT.md` | same (approved in full, 2026-09-28) | `5d8f40124402c298321450c7ab31c192276655e5767665ec50a29f6f09d38663` |

**Rules for 28c:**
- For every staged path, `git hash-object <p>` must equal `git hash-object --no-filters <p>`.
- No path may match `git check-ignore`.
- Stage by explicit path only.
- Make one commit:
  `Batch 28 close: Batch 27 sealed ledger, Batch 28 close, launch briefs and approved wording`.
- Afterwards, verify that every committed blob equals the raw bytes.

## 28d — push

- `git fetch` first. Each branch must be 0 behind.
- Push one at a time with `--no-force --no-tags`, fast-forward only: `batch15-launch`,
  `b24-06-paper2`, `b23-04-paper3`.
- Confirm each push with `ls-remote`.
- Do not push any `b28-*` branch.

## Stops, deliverables

- A stop in one part does not undo earlier parts. If 28a stops, do not run 28c.
- Write these to `Claude_Handover_B15_B18\post_b19_housekeeping_20260917\`:
  - `B28_PART28_CLOSE_RECEIPTS.json`, with merges and parents, fast-forward old→new, per-file
    blob/SHA-256/bytes for the content commit, and push logs;
  - `B28_PART28_CLOSE_REPORT.md`, at most 60 lines;
  - `PART28_MANIFEST.json`.
- Then stop. **No Batch 29 slot is launched by this pass.**
