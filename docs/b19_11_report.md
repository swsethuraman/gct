# B19-11: reproducible delivery and batch-18 carry-forward

Batch 19, slot 11. 15 September 2026. Worktree `work/batch15_workers/B15-11`,
written in place. Model: Claude Fable 5.1 (as reported by the session). Status line
in section 9.

**Starting state (read-only, recorded before any write):**

    git rev-parse HEAD          18ff3d0c981926b8a2b158368aee9116ac8655d9
    git rev-parse HEAD^{tree}   808349e008616a223442141b92b30627ef041d21
    git status --porcelain      ?? results/logs/b15_11_runtime_native_20260913.pid
                                ?? results/logs/b15_11_runtime_native_20260913_resources.json
                                (two untracked files dated 13 September 2026, predating
                                this session; not touched)

Branch of this worktree (read from the worktree's `HEAD` file, no git command):
`b15-11-executable-memory`. The batch-19 byte-preservation rules for slot 11 are
present in `.gitattributes` (lines 18-24) and `.gitignore` (lines 78-79), so the
`B19_RULES.ps1` step has been run for this worktree.

## 0. Plain-terms summary

This slot makes batch 18's evidence portable and adds two rules to the delivery
contract. It changes no mathematics and accepts nothing: a hash proves a file is
unchanged, never that the claim inside it is true.

What this report delivers:

Section map: 1 frozen inputs; 2 literature inventory; 3 git and worktree state;
4 what the batch-18 certificates contain; 5 the replay and the vector packet;
6 the two contract rules; 7 labelled claims; 8 honest negatives; 9 next test and
status.

1. **A frozen input list** for the batch-19 first wave: every document the five
   first-wave prompts and the preamble tell a session to read, with byte size and
   SHA-256 as found on disk today (section 1).
2. **The nineteen explicit highest-weight vectors, with their monomial ordering.**
   The batch-18 sweep certificates in `B15-06/results/b18_06_sweep/` record each
   vector's size data (largest coefficient, nonzero count, weight-space dimension,
   shifted-target dimensions) and the exact values at the points used, but **not
   the vector itself and not the monomial ordering**; the sweep document says the
   vectors are "reproducible from the recorded seed and prime". So the ordering
   does not ship with the vector today. This slot regenerates each vector by the
   same construction, verifies it exactly over the integers, replays the recorded
   determinant and padding values at the recorded points, and writes vector plus
   ordering plus the new certificate fields to `results/b19_11/vectors/` (sections
   2-3). Whether that replay reproduced every recorded number is stated there, cell
   by cell.
3. **Two new rules in `docs/delivery_contract.md`** (section 4): a check whose
   subject can be empty ships the size of what it checked; fetched literature stays
   out of the delivery tree.
4. **A literature inventory** (section 5): every third-party paper or full-text
   copy found in the repository tree, with location, size, hash, and whether it is
   tracked, untracked or ignored. Nothing is deleted, untracked or rewritten.
5. **The actual git and worktree state** (section 6), read from the worktree
   pointers and the repository configuration files, plus the permitted
   `git status --porcelain`. No push, no publication, no commit.

What this report does not do: it does not commit anything, does not re-review any
batch-18 claim, and does not run any new mathematics beyond the replay of existing
certificates.

## 0.1 Conventions and inherited rules, with their justification

- **Hash function.** SHA-256 over the bytes on disk, CRLF included, because the
  batch-19 `.gitattributes` rules (`-text whitespace=cr-at-eol`) bind the bytes as
  written and the manifest values are meant to match them. ADOPTED from
  `B19_RULES.ps1`; the justification (batch 18 saw four CRLF files rewritten under
  `eol=lf`) is recorded in that script and holds here because the same rules are in
  force in this worktree.
- **Pilot envelope.** Any computation in this slot runs one process, one BLAS
  thread, through the unchanged inspected wrapper `analysis/b15_bound.py` with
  `--seconds 60 --memory-mb 512`. ADOPTED from the preamble. The replay in section
  3 needs at most 14 s and 80 MiB per cell by the batch-18 measurements
  (`b18_06_sweep.md` section 9), so the envelope is adequate; the largest cell is
  measured again here rather than assumed.
- **Vector conventions.** The replayed vectors use the sweep's own conventions
  verbatim: ordinary coefficients, `E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)`,
  five variables, degree five, weight-space basis enumerated by the sweep script's
  `weight_basis` in the order it produces. This slot does not re-derive or re-argue
  those conventions; it records the ordering they induce.
- **Normalisation of the vector.** Each cell has `a = 1`, and the sweep clears
  denominators and divides by the gcd after normalising the first nonzero
  coordinate to one, so the primitive integer vector with positive first nonzero
  coordinate is **unique** and independent of the random seed. PROVED from the
  sweep code (`exact_hwv`); this is why a replay must reproduce the vector exactly,
  not merely up to scalar, and why a mismatch would be a finding.

## 1. Frozen inputs for the first wave (MEASURED)

Every document a first-wave session is told to read was located and hashed as it
stood on disk at freeze time; the full list with sizes and 64-hex SHA-256 values
is `results/b19_11/input_freeze.json` (frozen 2026-09-16 03:1x UTC, i.e. the
evening of 15 September local time). Nothing was missing. Abbreviated:

| document | bytes | SHA-256 (first 16) |
|---|---:|---|
| `batch19_launch/B19_PREAMBLE.md` | 11,398 | `4286e2149d7f1368` |
| `batch19_launch/LAUNCH.md` | 3,672 | `3c93fe0839c12c20` |
| `batch19_launch/B19_RULES.ps1` | 3,441 | `6e5ba1876560856e` |
| `batch19_launch/B19-01.md` / `-02` / `-05` / `-10` / `-11` / `-12` | 2,848 / 2,672 / 2,157 / 2,518 / 2,418 / 2,135 | `afbe0addf513ad72` / `5562ba3232b5334d` / `56947494d17003ca` / `f7040f506ecee214` / `45634d93fdddc2aa` / `5489bbbca9dbe06d` |
| `BATCH19_PROPOSED_BOARD.md` | 20,381 | `d1690a3fe47224bf` |
| `BATCH18_REVIEW_AND_NEXT_ROADMAP.md` | 21,848 | `14d808168ba1335d` |
| `B15-02/docs/b18_02_report.md` (01 input) | 38,295 | `dca6de94e0746fcc` |
| `B15-02/docs/b18_02_review.md` (01 input) | 7,799 | `0d30ec90c1c4e13c` |
| `B15-08/docs/b17_08_report.md` (01 input) | 21,103 | `246c96c506ebb4e4` |
| `B15-01/docs/b18_01_report.md` (02 input) | 49,572 | `2ba3fc9c14182703` |
| `B15-10/docs/b18_10_review.md` (02 input) | 48,344 | `dc1cc655a95bcadb` |
| `B15-03/docs/b17_03_report.md` (02 input) | 20,187 | `bcb38b5f2682f69c` |
| `B15-01/docs/b17_01_report.md` (02 input) | 15,609 | `8812eeef2b454cfa` |
| `B15-12/docs/b18_12_ledger.md` (05, 12 input) | 38,365 | `a4520e2aab3a9d01` |
| `B15-12/docs/b18_12_review.md` (12 input) | 6,970 | `ebc39b2cb3388cfe` |
| `B15-06/docs/b18_06_sweep.md` (05 input) | 20,446 | `6ac744d6cb21cc64` |
| `B15-06/docs/b18_06_report.md` (05 input) | 37,667 | `6039299644b1e890` |
| `B15-05/docs/b18_05_report.md` (05 input) | 23,139 | `609796845ed5c875` |
| `B15-11/docs/delivery_contract.md` (before this slot's edit) | 10,686 | `669122416cc0f201` |
| `B15-06/analysis/b18_06_sweep.py` | 22,441 | `a75db90a57272388` |
| 24 sweep certificates `B15-06/results/b18_06_sweep/*.json` | 535 - 7,439 each | in the JSON |

The `b17_08_report.md` hash equals the one pinned by supplement04_08 in batch 17
(`246c96c5...`), and the sweep script hash equals the one quoted in
`b18_06_sweep.md` (`a75db90a...`): those two documents are byte-identical to what
their reviewers read. Every other entry is a fresh pin; it asserts only "this is
what the first wave read", never that the content is correct. Four of the
documents are CRLF on disk (`b18_06_sweep.md`, `b18_06_report.md`,
`b18_05_report.md`, `delivery_contract.md`, and all 24 certificates); the hashes
are over those bytes, as the batch-19 attribute rules intend.

## 2. Literature inventory (MEASURED; inventory only, nothing remediated)

Searched the whole `gct-gpt` tree (excluding `.git` and `.venv` directories) for
`.pdf`, `.djvu`, `.ps`, `.epub`, `.bib`, for directories named like
`literature`, `references`, `papers`, `arxiv`, `cache`, and for files carrying an
arXiv identifier. Tracking state was read with `git status --porcelain --ignored`
on the path, inside the worktree that owns it.

| location | file | bytes | SHA-256 (first 16) | state |
|---|---|---:|---|---|
| `B15-12/results/b15_12/sources/` | `bip_1604.06431v3.pdf` | 406,395 | `b6d54e77f9157...` | **tracked** (committed on `b15-12-padding-orbit-bounds`) |
| same | `blmw_0907.2850v2.pdf` | 346,907 | `70bb2af9d4cc5...` | **tracked** |
| same | `ip_1512.03798v2.pdf` | 333,521 | `683d3aa4d89dfe...` | **tracked** |
| same | `kl_1204.4693v1.pdf` | 150,290 | `599486883d141d...` | **tracked** |
| same | `bip_theorem.png`, `blmw_proposition.png`, `ip_appendix.png`, `kl_theorem.png` | 391 k - 485 k each | not hashed | untracked (page images of the papers) |
| `B15-01/results/b18_01/literature/` | `arXiv_2303.09028v3.pdf` (LLV) | 278,201 | `67b1701f761d43...` | untracked (whole directory) |
| same | `arXiv_1411.0777_latest.pdf` | 553,228 | `0741e2d2c60570...` | untracked |
| same | `llv_v3.txt`, `ss.txt` (full-text extractions) | 65,293 / 175,290 | not hashed | untracked |
| `Batch16/reviews/12/results/b15_12/sources/` | `kl_1204.4693v1.pdf` | 150,290 | `599486883d141d...` (same bytes as the B15-12 copy) | outside any git repository: `Batch16/` is a handover directory, not a worktree |
| `B15-01/results/b17_01/literature/` | (empty directory) | | | untracked, empty |

Full hashes are in `results/b19_11/literature_inventory.json`. The twenty
`results/ci73/cache` directories that the name search returned are computation
caches from batch 14/15, not literature, and are listed there only so the search
is reproducible.

**Conclusion of the inventory.** Four third-party PDFs (about 1.2 MB) are
committed in the B15-12 worktree's branch; two PDFs and two full-text copies
(about 1.07 MB) sit untracked in B15-01 and would be committed by any add list
that takes `results/b18_01/**` wholesale. Per the assignment, this slot lists them
and stops: nothing was deleted, moved, untracked or rewritten. The remediation and
its authorisation are the integrator's. The new contract rule in section 6 is
written so that a future delivery gate can flag these paths.

## 3. Git and worktree state, inspected (MEASURED, read-only)

Read from files (`.git` pointers, `HEAD`, `refs/`, `packed-refs`, `config`) plus
the permitted `git rev-parse` and `git status --porcelain`. No other git command.

- The parent directory `C:/Users/swami/Projects/gct-gpt` is **not** a git
  repository. The repository is `work/batch15/.git`; the twelve worktrees
  `work/batch15_workers/B15-01..12` are linked worktrees of it
  (`.git/worktrees/B15-NN`). `Claude_Handover_B15_B18/`, `Batch16/` and similar
  top-level directories are plain directories outside version control.
- Remote: `origin = https://github.com/swsethuraman/gct.git`. Remote-tracking
  refs exist for `main`, `integration/batch13`, `housekeeping/batch14-close`,
  `batch15-launch` and all twelve `b15-NN-*` branches. This is existing state; it
  is **not** an authorisation and nothing here pushes.
- Main worktree `work/batch15`: `HEAD = refs/heads/batch15-launch =
  01ba49b832a60c189c143981f3a7550f7157c18a`, equal to `origin/batch15-launch`;
  status shows one untracked directory `results/b15_integrator/`.
- Each linked worktree is checked out on its own `b15-NN-*` branch. For every
  worktree examined (01, 02, 05, 06, 10, 11, 12), `HEAD~1` equals the
  remote-tracking ref `origin/b15-NN-*` (loose ref, newer than the packed one), so
  each local head is **exactly one commit ahead of what was pushed**. That commit
  is, by the launch document's account, the batch-19 rules commit made by
  `B19_RULES.ps1`; this slot did not read the commit itself (that would need
  `git show`), so "rules commit" is ADOPTED from the launch document while "one
  commit ahead" is MEASURED. This is consistent with the integrator assessment's
  statement that batches 14-18 are published and the rules were added afterwards.

| worktree | branch | local HEAD | `HEAD~1` = `origin/<branch>` |
|---|---|---|---|
| B15-01 | `b15-01-ci159` | `03c8fb86` | `ea045cef` yes |
| B15-02 | `b15-02-a1-probes` | `ba1ec94a` | `33528da6` yes |
| B15-05 | `b15-05-tail21` | `ca3d6d80` | `8c4e45b4` yes |
| B15-06 | `b15-06-fresh-tails` | `42638d25` | `84a9a28d` yes |
| B15-10 | `b15-10-portable-witness` | `fce465ae` | `a1bd3478` yes |
| B15-11 | `b15-11-executable-memory` | `18ff3d0c` | `c301a32d` yes (packed ref; no loose ref for this branch) |
| B15-12 | `b15-12-padding-orbit-bounds` | `c0cd755b` | `5925557f` yes |

Worktrees 03, 04, 07, 08, 09 were not inspected beyond their `HEAD` files
(branches `b15-03-two-dimensional`, `b15-04-small-panel`,
`b15-07-projected-product`, `b15-08-new-brackets`, `b15-09-global-det`); their
packed remote refs differ from their local heads, presumably by the same rules
commit, NOT REACHED here.

- `FETCH_HEAD` and `ORIG_HEAD` are dated 12 September 2026; no fetch has happened
  since, and none was run by this slot.
- This worktree's own status before and after this slot's writes is in section 9.

## 4. What the batch-18 sweep certificates contain, and what they do not (MEASURED)

The 21 cell certificates `B15-06/results/b18_06_sweep/{S01..S19,R01,R02}.json`
(7.4 kB each) carry: `cell`, `lambda`, `d`, `a_weyl_alternant`, `lift_attempts`,
`primes_used`, `seed_used`, `hwv_max_abs`, `hwv_nonzeros`, `raising_target_dims`
(four integers), `weight_space_dim`, `exact_raising_residues_all_zero`, the three
determinant points (integer `4x4` arrays of 5-vectors `A`) and three padding
points (`l`, `N`) with the exact integer value at each, `m_det_floor`,
`m_pad_floor`, `status`, `D`, timings.

They do **not** carry the vector `W` itself, nor the ordering of the `K` basis
elements it is expressed in. `b18_06_sweep.md` claim 2 says so explicitly:
"certificates hold the vectors' size data; the vectors themselves are reproducible
from the recorded seed and prime". The ordering is defined only implicitly, by the
recursion order of `weight_basis` in `b18_06_sweep.py` over the recursion order of
`exps(5, 4)`. So as of the batch-18 delivery **the vector and its ordering ship
only as code plus a seed**: replayable, but not portable as data, and a change to
that script would silently change what "the vector" means. That is the gap
assignment item 2 asks about, and the answer is: **neither was recorded**.

Two things the certificates do get right and this slot did not need to add: the
target dimensions of the four raising operators are recorded per cell (so the
batch-18 verification is demonstrably non-vacuous on the dimension count), and the
points are recorded as integers, so the values can be recomputed without any
random number generator.

## 5. The replay and the vector packet (MEASURED, CERTIFIED)

**Why a computation was necessary.** The only way to ship the vectors with their
ordering is to regenerate them; the only way to confirm replayability "end to end"
is to recompute every recorded number from the recorded inputs. Both need the
sweep's construction to run once per cell. The batch-18 measurements put every
cell inside the standard envelope (at most 14.0 s and 80 MiB), so this was done as
21 bounded runs, one process each, through the unchanged wrapper.

**What ran.** `analysis/b19_11_vectors.py` (this worktree; hash in the manifest)
imports the **unmodified** `B15-06/analysis/b18_06_sweep.py` (SHA-256
`a75db90a...`, equal to the hash quoted in `b18_06_sweep.md`) and, per cell:

1. rebuilds `W` by `exact_hwv` with the script's own seeds and primes;
2. writes the ordering explicitly: the 70 degree-4 exponent vectors `MONS` in
   order, and the `K` basis elements as sorted 5-tuples of `MONS` indices in
   order, plus a SHA-256 of the fully expanded ordering; and writes `W` as a
   list of `K` integers;
3. verifies `W` exactly over `Z` with the four fields the new contract rule
   requires per operator: source weight `lambda`, target weight
   `lambda + e_i - e_(i+1)`, both dimensions, the operator's stored nonzero count,
   and an independent nontrivial action test (the operator applied to the first
   basis vector `e_0` and to the all-ones vector, nonzero counts recorded);
4. rebuilds each of the six recorded points from its integer data (no random
   numbers), evaluates `W` there exactly, and compares with the recorded value;
   compares `a`, `K`, `hwv_max_abs`, `hwv_nonzeros` and the four target
   dimensions with the recorded ones.

**Result: all 21 cells `REPLAYED_ALL_MATCH`.** Every recorded determinant and
padding value (126 values) was reproduced exactly; every recorded size datum
matched; every residue was zero; every operator was populated and acted
nontrivially on the test vectors. Per cell:

| cell | `lambda` | `K` | operator nonzero counts `E_12, E_23, E_34, E_45` | action on `e_0` (nonzeros) | points matched | packet bytes | wall s |
|---|---|---:|---|---|---|---:|---:|
| S01 | (11,4,2,2,1) | 705 | 1691, 1107, 1107, 705 | 2,2,1,1 | 6/6 | 51,787 | 2.3 |
| S02 | (10,5,3,1,1) | 774 | 2145, 1600, 774, 774 | 2,2,1,1 | 6/6 | 56,022 | 2.2 |
| S03 | (10,5,2,2,1) | 1008 | 2800, 1600, 1600, 1008 | 2,2,1,1 | 6/6 | 70,446 | 2.7 |
| S04 | (8,7,3,1,1) | 1091 | 3656, 2284, 1091, 1091 | 2,2,1,1 | 6/6 | 76,066 | 2.7 |
| S05 | (9,5,4,1,1) | 1215 | 3419, 2999, 1215, 1215 | 2,2,1,1 | 6/6 | 83,220 | 2.9 |
| S06 | (9,6,2,2,1) | 1275 | 3922, 2035, 2035, 1275 | 2,2,1,1 | 6/6 | 87,491 | 3.0 |
| S07 | (8,5,5,1,1) | 1610 | 4583, 4583, 1610, 1610 | 2,2,1,1 | 6/6 | 108,198 | 3.4 |
| S08 | (10,4,2,2,2) | 1761 | 4316, 2800, 2800, 2800 | 2,1,1,1 | 6/6 | 116,485 | 4.0 |
| S09 | (9,5,3,2,1) | 1860 | 5283, 3922, 2999, 1860 | 2,2,1,1 | 6/6 | 123,692 | 4.1 |
| S10 | (9,4,4,2,1) | 2123 | 5283, 5283, 3419, 2123 | 2,2,1,1 | 6/6 | 139,555 | 4.4 |
| S11 | (8,6,3,2,1) | 2261 | 7105, 4790, 3656, 2261 | 2,2,1,1 | 6/6 | 150,557 | 4.6 |
| S12 | (8,5,4,2,1) | 2825 | 8112, 7105, 4583, 2825 | 2,2,1,1 | 6/6 | 185,776 | 5.4 |
| S13 | (8,6,2,2,2) | 2972 | 9331, 4790, 4790, 4790 | 2,1,1,1 | 6/6 | 192,775 | 5.8 |
| S14 | (7,6,4,2,1) | 3260 | 10351, 8231, 5303, 3260 | 3,2,1,1 | 6/6 | 212,975 | 6.0 |
| S15 | (7,5,4,3,1) | 4807 | 14020, 12274, 10351, 4807 | 2,1,1,1 | 6/6 | 310,590 | 7.9 |
| S16 | (8,4,4,2,2) | 4988 | 12620, 12620, 8112, 8112 | 1,1,1,1 | 6/6 | 319,434 | 8.4 |
| S17 | (7,4,4,4,1) | 5490 | 14020, 14020, 14020, 5490 | 2,2,2,1 | 6/6 | 352,278 | 8.4 |
| S18 | (6,6,4,2,2) | 6869 | 22114, 17538, 11244, 11244 | 2,1,1,1 | 6/6 | 442,714 | 10.5 |
| S19 | (6,4,4,4,2) | 11640 | 30049, 30049, 30049, 19201 | 2,2,2,1 | 6/6 | 749,867 | 14.5 |
| R01 | (9,7,2,1,1) | 621 | 2035, 983, 621, 621 | 2,1,1,1 | 6/6 | 47,025 | 1.7 |
| R02 | (12,2,2,2,2) | 553 | 852, 852, 852, 852 | 1,1,1,1 | 6/6 | 42,592 | 1.7 |

Resource receipts `results/logs/b19_11_vec_*_resources.json`: 21 runs, all exit 0,
largest wall 14.56 s (S19), largest peak Job commitment 84,455,424 bytes (80.5
MiB), consistent with the batch-18 measurements. The packet
`results/b19_11/vectors/` totals 3.92 MB; the largest single file is 750 kB, under
the contract's 5 MB limit. `results/b19_11/replay_run_log.txt` holds the one-line
result per cell as printed.

**What the packet is.** For each cell, one JSON with: the conventions in words;
the sweep script and batch-18 certificate hashes it was built against; the
ordering (`MONS`, basis index tuples, expanded-ordering SHA-256, first and last
element expanded); `W`; the per-operator verification block; the replay block with
every recorded and recomputed value side by side. A reader with the JSON alone,
and no code, can evaluate `W` at any point and rebuild the raising operators.

**What the packet is not.** It is not a re-review of the sweep's inference. That
`a = 1`, that the points are actual restrictions of invertible substitutions, and
that a nonzero value closes the cell are batch-18 claims accepted in
`b18_06_sweep_review.md`; this slot recomputed `a` and the block ranks as part of
the replay because the sweep code does so, and found the same numbers, but it does
not re-argue them. A hash match, or a value match, says the certificate is
replayable, not that it is right.

## 6. The two contract rules (delivered)

Appended as section 11 of `docs/delivery_contract.md` in this worktree (the
document's own hash before the edit is in section 1; after, in the manifest):

- **11.1 Any check whose subject can be empty ships the size of what it checked.**
  Source and target weights, both dimensions, the operator's nonzero count, and an
  independent nontrivial action test with its nonzero count. A nonempty target
  space alone proves nothing. Extended to any check whose subject can be empty.
  Reference implementation: the per-operator block of `analysis/b19_11_vectors.py`.
- **11.2 Fetched literature stays out of the delivery tree.** Local cache outside
  `docs/`, `analysis/`, `results/`, `delivery/`; report identifier with version,
  URL, access date, theorem location, optional hash of the copy read; page images
  and text extractions count; committed literature is inventoried, never deleted
  or untracked by a worker.

The contract's older sections were not changed. The edit is a tracked change on
the worktree and is the integrator's to commit or not.

## 7. Claims, labelled

**MEASURED.** The input freeze (section 1); the literature inventory and each
file's tracking state (section 2); the repository, remote and worktree facts and
the "one commit ahead of origin" relation for seven worktrees (section 3); the
absence of `W` and of the ordering from the batch-18 certificates (section 4); the
21 replays with all 126 point values, all size data, all residues and all action
tests (section 5); the resource receipts.

**CERTIFIED.** The 21 vectors in `results/b19_11/vectors/`, each with its
ordering, exact annihilation by the four simple raising operators against
recorded target dimensions, populated operators (nonzero counts 553 to 30049) with
nontrivial action, and exact agreement with every recorded batch-18 value. These
are objects rechecked here; the mathematical inference drawn from them in batch 18
is not re-adjudicated.

**PROVED.** Only one small fact: with `a = 1`, the sweep's normalisation
(pivot to one, clear denominators, divide by gcd) makes `W` unique, so replay must
reproduce it exactly (section 0.1).

**ADOPTED.** All conventions of `b18_06_sweep.py`; the pilot envelope; the
CRLF-preserving hash convention; the launch document's account of the local
rules commits; the batch-18 review's acceptance of the sweep's inference.

**NOT REACHED.** Ancestry inspection for worktrees 03, 04, 07, 08, 09; the
content of the one unpushed commit per worktree; any remediation of literature;
any commit; the pending batch-18 closeout documents (`PROVED.md` for B15-B18, the
close document), which the launch note says are the integrator's; the B18-05
control repair, which is slot 05's.

## 8. Honest negatives

- **The vectors did not ship with their ordering in batch 18.** The certificates
  are replayable from code plus seed, and that replay succeeded here, but a
  certificate whose meaning depends on the recursion order of an unhashed helper
  function is not portable. This packet fixes the portability; it does not change
  the batch-18 claim.
- **Literature is committed.** Four PDFs on the B15-12 branch; two more plus two
  text extractions untracked in B15-01 and exposed to any wholesale add list.
  Listed, not touched.
- **"One commit ahead" is inferred to be the rules commit**, not read. Reading the
  commit needs a git command this slot may not run.
- **Nothing here is mathematical acceptance.** Matching hashes and matching values
  say the files are what they were and the computation replays; the direction of
  inference, the point validity and `a = 1` remain the sweep's and its review's.
- **The replay used the sweep's own code.** Independence of method was already
  supplied in batch 18 by the elimination cross-check on S01 and S12; this slot
  adds replay fidelity, not a third lineage.
- The 21 bounded runs are more than "one pilot"; they are the assignment's
  preservation step, each inside the envelope, and are declared in section 5.

## 9. One next sufficient test, and status

**Next test.** Have the integrator's delivery gate read one packet file, say
`results/b19_11/vectors/S19.json`, and, **without importing any project code**,
(i) rebuild the four raising operators from `MONS` and the basis index tuples,
(ii) confirm the recorded nonzero counts and target dimensions, (iii) apply them
to `W` and to `e_0`, and (iv) evaluate `W` at the first recorded determinant point
and match `33900369404217588856`. Price: a few hundred lines of independent code
and under a minute; if it passes, the packet is portable in the sense the board
asked for, and rule 11.1 has one worked example on both sides of the seam.

**Status.** COMPLETE as a delivery-and-inventory slot. No commit, no push, no
publication, no heavy lease, nothing deleted or untracked. Git commands run: the
two opening `rev-parse` calls, `git rev-parse HEAD~k` (k = 1..3) in seven
worktrees, and `git status --porcelain` (with `--ignored` on literature paths) as
permitted. Runs: 21 bounded processes through `analysis/b15_bound.py`, all exit 0,
largest 14.56 s and 80.5 MiB. Files written in this worktree:
`docs/b19_11_report.md`, `docs/delivery_contract.md` (section 11 appended),
`analysis/b19_11_vectors.py`, `results/b19_11/` (input freeze, literature
inventory, replay log, 21 vector packets, manifest), and the wrapper's
`results/logs/b19_11_vec_*` receipts and pid files. Final write footprint by
`git status --porcelain` and the manifest are recorded in section 9.1.

### 9.1 Final footprint and manifest

`git status --porcelain` after the last write, before this subsection was
appended:

     M docs/delivery_contract.md
    ?? analysis/b19_11_vectors.py
    ?? docs/b19_11_report.md
    ?? results/b19_11/
    ?? results/logs/b19_11_vec_{S01..S19,R01,R02}.pid            (21 files)
    ?? results/logs/b19_11_vec_{S01..S19,R01,R02}_resources.json (21 files)
    ?? results/logs/b15_11_runtime_native_20260913.pid            (pre-existing)
    ?? results/logs/b15_11_runtime_native_20260913_resources.json (pre-existing)

Exactly one tracked file modified (the contract, section 11 appended); everything
else new is under batch-19 slot-11 paths covered by the attribute rules. The
`.pid` files are written by the wrapper and are tracked by the batch-19 ignore
exception, per the contract's rule to ship them.

`results/b19_11/MANIFEST.json` lists 70 files with byte sizes and SHA-256:
this report as it stood before this subsection (26,071 bytes,
`284982d12ce026a7...`), `docs/delivery_contract.md` after the edit (13,393 bytes,
`dfc7b93a017db9a6...`), `analysis/b19_11_vectors.py` (9,972 bytes,
`aa8d3e95f155d9d5...`), the unchanged wrapper (`ca001081f49e0048...`, identical
to the B15-06 copy), the input freeze, the literature inventory, the replay log,
the 21 vector packets and the 42 receipts. The manifest excludes its own hash. It
binds bytes; it accepts nothing.
