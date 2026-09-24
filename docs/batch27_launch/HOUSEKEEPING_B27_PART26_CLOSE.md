# Batch 27 — PART 26: the close pass (merge, fast-forward, commit the close records)

**STATUS: READY.** Run this in a Claude Code session in **default permission mode**. It is the
only delivery pass at the close of Batch 27. It assesses no mathematics and edits no packet,
paper, ledger or seal. The ceiling is 60 minutes.

Read `batch27_launch/B27_COMMON.md` for conventions.
- **In this pass only**, the Git prohibitions are lifted for exactly: `git merge --no-ff` into
  `batch15-launch` (26a), fast-forward-only updates of three paper branches (26b), one content
  commit on `batch15-launch` (26c), `git merge --abort` after a conflict, and fast-forward pushes
  (26d).
- Everything else in B27_COMMON's "Never" list still holds: no `-f`, `-A`, `+refspec`, rebase,
  amend, reset, clean, checkout, or `.gitattributes`/`.gitignore` edit.
- Run every Git command as `git -C <worktree>`.

## §0 — Author decisions (given 2026-09-23)

| item | decision |
|---|---|
| 26a — merge the seven research and review branches into `batch15-launch` | **YES** |
| 26b — fast-forward the three paper base branches to B27-04's tips | **YES** |
| 26c — commit the close records on `batch15-launch` | **YES** |
| 26d — push the four updated branches, fast-forward only | **YES** |
| Coordinator's Batch 27 ledger | **NOT in this pass**; it goes in the first Batch 28 delivery pass |
| Slot branches `b27-*` | left as they are; do not delete or move them |

## Preflight

1. Record the raw SHA-256 of this file, of `B27_COMMON.md` and of `BATCH27_CLOSE.md`. The last
   must be `0e55ca6bc2152a77c3e882a35395a2eaaf6cc128dd0cf5c6e63678da7678bd35`.
2. Run `git fetch`, then `ls-remote` every branch named below.
3. For each slot tip:
   - it must start with the prefix in the table;
   - its only parent must be its PART 25 setup commit;
   - `git diff --name-only <setup>..<tip>` must list only that slot's own output paths.

   If any check fails, stop that row.
4. **Base branches.**
   - `batch15-launch` must be at `f7967d17935d6256e7744f6457b45a3787b6940f`.
   - The three paper bases must be at their PART 25 tips.
   - If a base has moved, stop the part that uses it and report.
5. **Worktree for `batch15-launch`.**
   - Find it with `git worktree list --porcelain`. It must show no tracked modifications:
     `status --porcelain --untracked-files=no` must be empty.
   - If `batch15-launch` is not checked out anywhere, run
     `git worktree add work/batch27/b27-close batch15-launch`.
   - Leave untracked files alone.

## 26a — merge into `batch15-launch`, in this order

| # | branch | expected tip | setup parent | slot |
|---|---|---|---|---|
| 1 | `b27-k4r` | `53206b43…` | `f35dbb6c` | R27-K4 |
| 2 | `b27-01` | `01f78eb2…` | `6dea55ec` | B27-01 |
| 3 | `b27-01r` | `51f9d17eeae019a27e16b101d30c568df0e7d422` | `6dea55ec` | R27-01 |
| 4 | `b27-02` | `35eeff49…` | `6dea55ec` | B27-02 |
| 5 | `b27-02r` | `459c32fa54bcfb9c8f1e33a03c1a6ad7048953e7` | `fcff7eea` | R27-02 |
| 6 | `b27-03` | `7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19` | `fcff7eea` | B27-03 |
| 7 | `b27-03r` | `8f011f012d3d2f963cf69ea3c63cec08b4870bc1` | `fcff7eea` | R27-03 |

**Manifests to re-check at each tip,** by reading blobs with `git show <tip>:<path>` and comparing
every payload's SHA-256 and bytes:

| slot | manifest path | raw hash |
|---|---|---|
| R27-K4 | `results/b27_k4/MANIFEST.json` | `d63c535f…` |
| B27-01 | `results/b27_01/MANIFEST.json` | `580aa717efd424fd89619f8bde5dd16c4e1a7a5b902ad9629d6c5e9c882f3863` |
| R27-01 | `results/b27_01r/MANIFEST.json` | `5e1b039fb0d80a459384db980835ebb3647a200f81664088dd9f35bc7de3618b` |
| B27-02 | `results/b27_02/MANIFEST.json` | `bb55a4e5…` |
| R27-02 | `results/b27_02r/MANIFEST.json` | `a57995e5c996b09a70414414a71efff3943eb5f8c3e71cc058525495e93e13ca` |
| B27-03 | `results/b27_03/MANIFEST.json` | `463d9dfcc04a7782476f4854ef3714264227ee59fe21765ab9124e00cbcf2c0d` |
| R27-03 | `results/b27_03r/MANIFEST.json` | `62759639ea400454daf707cc61d8f022a86b92949b2013d10cad8a0ba9376f5a` |

Where a hash is given only as a prefix, record the full hash you find.

**For each merge:**
- Run `git merge --no-ff --no-edit -m "Batch 27 close: merge <branch> (<slot>)" <branch>`.
- Every setup commit appends the same three `.gitattributes` lines, so those hunks should merge
  cleanly.
- **On any conflict:** run `git merge --abort`, stop 26a at that row, and report. Do not resolve
  it by hand. Rows already merged stay merged.
- After each merge, confirm:
  - the merge commit has exactly two parents;
  - `.gitattributes` contains each of the three b27 lines exactly once.

## 26b — fast-forward the paper branches

| base branch | PART 25 tip | fast-forward to | manifest (on the tip) |
|---|---|---|---|
| `b23-05-paper1` | `af8468f3…` | `b27-04-p1` @ `d59ce77ae3937ef0d9c49eca2ea71ab607f69964` | `bcd6b425424a4f9c6a85eb7439fa39705e8dfe593e6f918023c129f1f9b9d43c` |
| `b24-06-paper2` | `721d54a2…` | `b27-04-p2` @ `f8326974a1454ac83a925860635e29bbfaf5d5c7` | `5130c98f6bf4872be0678a1f1ef276af2c40247dd449f8337ca69e8200f98ecb` |
| `b23-04-paper3` | `0a8029bb…` | `b27-04-p3` @ `4c5a54501bb046b236239fdbcff19556a317655c` | `2fc8a59182c53161e780b34b7498ecb4529b2a32f1e827f7bf35cf9d6e27615d` |

- The manifest path on each tip is `results/b27_04/MANIFEST.json`.
- **If the base is checked out in a worktree:** it must have no tracked modifications; then run
  `git -C <that worktree> merge --ff-only <b27-04-pN>`.
- **Otherwise:** run `git fetch . <b27-04-pN>:<base>`, with no `+`.
- A non-fast-forward is a stop for that row.

The integrator has already compiled all three after-states clean: 27, 16 and 24 pages, with 0
undefined references or citations.

## 26c — one content commit on `batch15-launch` (after 26a)

The source folder is `Claude_Handover_B15_B18\post_b19_housekeeping_20260917\`. Copy each file
byte-for-byte (for example with Python `shutil.copyfile`), then re-hash the copy.

| destination in the repo | source | raw SHA-256 |
|---|---|---|
| `docs/batch_closes/BATCH26_CLOSE.md` | `BATCH26_CLOSE.md` | `c2a4a187b503766ded4bf36f3a5b6c365269324b13b07ee6f2d82cdc42a3b5ef` |
| `docs/batch_closes/BATCH26_LIVE_LEDGER.md` | `BATCH26_LIVE_LEDGER.md` (the coordinator's seal) | `66b4869d8a39e103546ef947557f674d5eb729a724d08f59cef800c839adfdc7` |
| `docs/batch_closes/BATCH27_CLOSE.md` | `BATCH27_CLOSE.md` | `0e55ca6bc2152a77c3e882a35395a2eaaf6cc128dd0cf5c6e63678da7678bd35` |
| `docs/batch27_launch/B27_COMMON.md` | `batch27_launch/B27_COMMON.md` | `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee` |
| `docs/batch27_launch/BATCH27_BOARD.md` | same folder | `b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec` |
| `docs/batch27_launch/HOUSEKEEPING_B27_PART25_SETUP.md` | same folder | `aeb41a4b62b84dcc873cd0b96a5416ac629abe038618a616fc8cf6ac23138a04` |
| `docs/batch27_launch/HOUSEKEEPING_B27_PART26_CLOSE.md` | this file | record in the report |
| `docs/batch27_launch/B27-01.md` | same folder | `ce5a7910fbc913fffd52924f1c98707d3970392fe979259bfb9e2931baf18b8b` |
| `docs/batch27_launch/B27-02.md` | same folder | `8dbb0a0d1bd56fd5a1c5995254cf6c200b3f45698635f3f3f3daf6cbd42635d5` |
| `docs/batch27_launch/B27-03.md` | same folder | `b48370b0c99f96e57d2ebe633cb8852877cbd78c8d90455fc4948ebb663e1579` |
| `docs/batch27_launch/B27-04.md` | same folder | `165f3a62706f406258cc3fac00084126deb59f046830b93dee963738268d20ea` |
| `docs/batch27_launch/B27-05.md` | same folder | `1c2a37885816f19852436ded553fd44e18820458ab2fa91fe21a2a3d712f749e` |
| `docs/batch27_launch/B27-06.md` | same folder | `3f75ef35f7de580e28210627cc7ef70a63f54129b6240d83f92f8f5e11a0911a` |
| `docs/batch27_launch/R27-K4.md` | same folder | `59043481ae85a595db9b5187b927a5f21667f4464805795e69c9f98d5e967a27` |
| `docs/batch27_launch/R27-REVIEWS.md` | same folder | `916de53ab8c31c3d4242a84d8a894ce9ceecc75d76ef83dea8d4d87b3edddaa9` |
| `results/b27_05/**` | every file of `batch27_launch/b27_05_out/`, same relative paths | folder `MANIFEST.json` `325c1c817bce32e0f11fbd587bee16ea14ae3111c2ee56129fa7028571558a5c`, 39 payloads |
| `results/b27_06/**` | every file of `batch27_launch/b27_06_out/`, same relative paths, including `interrupted_delivery/` | folder `MANIFEST.json` `b713ca8b23c0ee430b663a04a74c68cdd99f3509f900a0ce7d73da0c3521cfce`, 129 payloads |

**Rules for 26c:**
1. **Hash checks.**
   - Every `docs/` source above must hash as listed and contain 0 CR bytes.
   - Every file in the two folders must match its folder manifest. The manifest file itself is
     the one exception: it is checked by its own raw hash.
   - Also copy any file in either folder that its manifest does not list, and name it in the
     report. There should be none apart from `MANIFEST.json`.
   - On any mismatch, stop 26c.
2. **Line endings.** Some files in `b27_05_out` and `b27_06_out` contain CRLF. The merged
   `.gitattributes` rule `results/b27_*/** -text whitespace=cr-at-eol` covers
   `results/b27_05/**` and `results/b27_06/**`. Confirm it with `git check-attr text` before
   staging.
3. **What Git will store.** For every staged path, `git hash-object <p>` must equal
   `git hash-object --no-filters <p>`. If any path differs, stop 26c.
4. **Ignores.** If `git check-ignore` matches any path, stop 26c and report it. Do not force-add
   and do not edit `.gitignore`.
5. **Size.** Stop if any file exceeds 5 MB. The largest expected is about 4.5 MB.
6. **Staging and commit.**
   - Stage by explicit path only. A generated path list is fine; no directory adds.
   - Make one commit:
     `Batch 27 close: Batch 26 close and sealed ledger, Batch 27 close, launch briefs, B27-05/06 outputs`.
   - After committing, verify that every committed blob equals the raw bytes.

## 26d — push

- Run `git fetch` first. Each branch must be 0 behind its remote.
- Push one branch at a time with `--no-force --no-tags`, fast-forward only:
  - `batch15-launch`
  - `b23-05-paper1`
  - `b24-06-paper2`
  - `b23-04-paper3`
- Confirm each push with `ls-remote`.
- Do not push any `b27-*` branch; they are already on the remote at their tips.

## Stops and partial delivery

- A stop in one part does not undo earlier parts.
- Deliver what completed, and state exactly which rows or parts stopped and why.
- If 26a stops, do not run 26c, because the attribute rule may be missing.

## Deliverables

Write these to `Claude_Handover_B15_B18\post_b19_housekeeping_20260917\`:

- `B27_PART26_CLOSE_RECEIPTS.json`, containing:
  - every merge commit and its parents;
  - the fast-forward old→new SHAs;
  - the content commit, with path, blob, SHA-256 and bytes for every committed file;
  - the push logs and `ls-remote` results.
- `B27_PART26_CLOSE_REPORT.md`, at most 60 lines.
- `PART26_MANIFEST.json`.

Then stop. **No Batch 28 slot is launched by this pass.** The coordinator's Batch 27 seal follows
separately.
