# b26_expander_input -- delivery note

**PRODUCER-ONLY input packet; not a numbered result; no acceptance implied.**

Delivered by Batch 26 PART 18a (housekeeping session, Claude Code, Claude Opus 5.5)
on 2026-09-22. The delivery session assessed no mathematics. Delivery is not review.

## Origin

Copied byte for byte from the project root (not a Git repository; the notes were
untracked everywhere before this commit):

    C:\Users\swami\Projects\gct-gpt\research_notes\20260921_expander_tableaux\

File names are unchanged. Hashes are raw SHA-256 of the bytes on disk. They were
re-hashed at delivery and match the discovery hashes in the Claude slate v1.

| # | file | bytes | raw SHA-256 |
|---|---|---|---|
| 1 | CONSTRUCTION_AND_LIMITATIONS.md | 15629 | 51851ab57a42715647cd8304112957ce0f3e03842a7523d9d63238faf0fdd674 |
| 2 | PADDING_SURVIVAL.md | 10578 | e2053e46b92aa6edafbac27d83e53a1f8e97fabca3b49e8eac40ab589e276a2d |
| 3 | DETERMINANT_REJECTION.md | 8463 | 6a40317b5e7679997b499d2346790079db336b300e10c42a40e92320145d89f3 |

Line endings: all three are LF only, ASCII, no BOM, so the Git blob equals the raw
bytes. No .gitattributes line was needed.

## Supersession order

1 -> 2 -> 3. Each later note supersedes the earlier open items it names, and
`DETERMINANT_REJECTION.md` supersedes the earlier membership-open remarks in
notes 1 and 2. Notes 1 and 2 carry follow-up pointers that say so. Per note 3 it does
not rule out arbitrary linear combinations. Notes 2 and 3 cite pre-pointer hashes
of their inputs (`67d3d1cc...` for note 1, `6bfebc9b...` for note 2). Those
earlier byte states are not in this packet, and this delivery did not verify them.

## Producing session and model

| note | producing session | model | created (UTC) |
|---|---|---|---|
| 1 | Codex Desktop session 01a0c159-bb84-7692-852a-cf00ffd05067 | gpt-6-astra | 2026-09-22T01:27:30Z |
| 2 | same session | gpt-6-astra | 2026-09-22T01:34:12Z |
| 3 | same session | gpt-6-astra | 2026-09-22T01:37:39Z |

Evidence, from bytes:
- Each note's header reads "Producer: Astra integrator, current task." The notes
  name no model.
- Rollout log `~/.codex/sessions/2026/09/20/rollout-2026-09-20T20-24-38-01a0c159-bb84-7692-852a-cf00ffd05067.jsonl`
  records an apply_patch "Add File" for each note at the times above, with
  turn_context model "gpt-6-astra". The 01:34:12Z and 01:37:39Z patches also update
  the earlier notes with their follow-up pointers.
- The file ctimes (01:27:32Z, 01:34:13Z, 01:37:41Z) and the common last mtime
  (01:37:4xZ) agree with those writes. Later log mentions do not coincide with
  any later file modification.
- No Claude session log in `~/.claude/projects` references these notes before this
  delivery session.

Lineage: **Astra (non-Claude)**.

## Excluded

No mathematical edits, acceptance labels or reformatting. Nothing else from
`research_notes/` is delivered.
