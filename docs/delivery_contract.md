# The delivery contract

For a worker session, and for whoever is briefing one. Batch 14 ran twelve slots;
this is what went wrong at the seams, ranked by how often it actually happened, and
what now catches each thing before it reaches the integrator.

**The one thing to take away.** Run this twice — once before you build the bundle,
once after, with the bundle and the manifest:

```
python3 tools/delivery/check_delivery.py --branch <your-branch> \
        --base "$(git log -1 --format=%H batch14-base)" --slot NN
# ... build the bundle ...
python3 tools/delivery/check_delivery.py --branch <your-branch> \
        --base "$(git log -1 --format=%H batch14-base)" --slot NN \
        --bundle <file> --manifest <file>
```

It now holds thirteen checks, which is the integrator's nine plus four the
integrator used to do by eye. `--selftest` runs nineteen cases: every check
rejected by a constructed bad input, next to two good deliveries that must come
back clean — including the awkward one, a session that edits a historical document
and adds nothing wrong to it.

The tag name and the batch prefix are parameters, `--base-tag` and `--batch`
(default `batch14-base` and `b14`). Pass them in the next batch: hardcoded, check 7
would degrade to a note and check 9 would find no slot number, and **both would
stop checking without saying so**.

---

## 1. The base — eleven of twelve sessions hit this

No dispatch message carrying the expected commit and tree reached **eleven of the
twelve** batch-14 sessions. The value had already been wrong three times before
that: stamped into the board header naming the commit *before* the one containing
it, twice; then `origin/main`, which can advance mid-run.

Resolve it yourself, from the tag, and know which command gives what:

```
git log -1 --format=%H batch14-base     # the COMMIT.  This is your base.
git log -1 --format=%T batch14-base     # its tree
git rev-parse batch14-base              # the annotated TAG OBJECT.  Not a base.
```

That third line is a real trap — an annotated tag's `rev-parse` returns the tag
object, and `4bda8a12` is not a commit. Record all three in your pre-registration.

**Check 7** fails if `--base` is not the commit the tag names.

## 2. The bundle — seven sessions hit this

The packet's own text said `git bundle create <file> batch14-base..HEAD`. That
produces a **HEAD-only** bundle, and a receiver doing
`git fetch <bundle> <branch>:<branch>` against it fails. The board's form is right:

```
git bundle create <file> <base>..<branch> <branch>
git bundle list-heads <file>     # must print refs/heads/<branch>, and only that
```

**Check 5** fails on a HEAD-only bundle, **check 8** on more than one ref or a
bundle whose prerequisite is not the base. Note that `git bundle verify` writes to
**stderr** — read both streams, or you will conclude every bundle is broken. That
mistake cost the integrator's own gate five wrongly-passing test cases.

## 3. The manifest — four of six Astra deliveries hit this

`bundle_prerequisites` kept arriving with the base commit's **subject line**
captured alongside the hash, because `git bundle verify` prints them on one line.
Capture only the hash.

**Check 13** requires every commit field to be bare 40-hex, `head` and `head_tree`
to match the branch as committed, and any checksum or byte count to match the
bundle as built. Regenerate the manifest **after** the last commit and **after**
building the bundle — a stale head is the second most common shape.

It reads named fields, so **it will tell you if it recognises none of yours** and
fail rather than reporting clean. That is deliberate: a manifest with different
field names was checked against nothing and passed, which is the same species of
defect this whole document is about. If your manifest uses other names, say so and
the gate will learn them — do not rename your manifest to satisfy a tool.

## 4. Pre-registration lands first, always

Everything committed before the pre-registration is exploratory and the integrator
reads it that way. **Check 9** fails if it is not the first commit in the range, and
if there is no report for the slot.

## 5. Direction of inference — the integrator checks this by hand and cannot automate it

This is where a delivery gets downgraded rather than rejected, so it is worth more
than the packaging:

- `rank_p ≤ rank_ℚ`. A **full** modular rank (rank = `a`) proves the rational
  statement — one prime is enough. A **deficient** modular rank proves only that the
  rank is at least what you measured: it is a **ceiling** on the ideal multiplicity
  and never a floor. A sampled zero never establishes `i ≥ 1`.
- An absent equation is not a proved absence. A positive upper bound proves nothing.
- If you write `i_pad = 3` anywhere, say in the same breath whether that is a value
  or a ceiling — and see §6, because the field name has to say it too.

Batch 14's twelve reports got this right almost everywhere. Where a claim was
withdrawn it was usually a *lemma's hypothesis*, not a number: an arbitrary-weight
vanishing statement that is true only for the isotypic component, a converse used
without its two positivity hypotheses, a clamp whose justification did not support
it. State the hypotheses you are using, not just the conclusion.

## 6. Field naming — four instances in four costumes, and every one misled a reader

| the field said | it actually was |
|---|---|
| `n_chi_lb`, a lower bound | not a bound — 135 of 222 values fell below it |
| `nchi_est`, an estimate | `ceil(N_S/\|Stab\|)`, a quotient the index forbids, in all 123 queue entries, with nothing naming the estimator. Two documents quoted it as a measurement |
| `i_pad`, `i_red` | ceilings, labelled correctly on a sibling field and nowhere on these |
| `signed_uniqueness_verified: true` | equally true at 1.38x margin and at 3e9 |

**The rule:** a field whose name asserts a property ships the quantity that property
is measured by. Ceilings get `_ub`, floors `_lb`, estimators name their estimator, a
boolean that summarises an inequality carries the margin too. `values_are` is the
house mechanism and it works — no file carrying one was ever misread.

## 7. The shared records

- **`docs/PROVED.md`.** Propose a section letter; expect the integrator to move it.
  Six slots collided in batch 14 and every one had chosen "F", which no worker could
  have avoided — you cannot see what a concurrent slot took. **Check 11** catches a
  self-collision and a malformed table row; escape every pipe inside a cell as `\|`,
  because `|G_lambda|` unescaped splits one cell into four.
- **`results/integrate/inherited_exclusions.json`.** Its consumer **fails closed**:
  an unrecognised predicate key *raises*, it does not skip. An entry appended without
  an `application_contract.conclusions_by_id` record, or using a shape the matcher
  does not implement, breaks every query for every cell. **Check 12** catches both.
  If you need a new predicate shape, implement it in
  `tools/integrate/exclusion_predicates.py` in the same delivery, or hand the shape
  to the integrator and say so plainly.
- **Never touch** `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`. Record errata against them in
  your own file, with frozen line numbers, as B14-11 did. **Check 3.**

## 8. Running, and not running

- Bound every long run with `timeout` and `ulimit -v`. Have the script write **its
  own** `os.getpid()` to `results/logs/<run>.pid` — a launcher records the wrapper's
  pid, not python's, and the recorded id then names nothing. End a run only by the
  recorded id.
- Ship the `.pid` files, not just the `.log` files.
- No push. Ever. Delivery is a bundle.
- No file over 5 MB. **Check 4.**
- No `claude.ai` URL in a commit trailer or in a delivered file. Writing *about* the
  rule is fine; **checks 1 and 2** distinguish a live link from a quoted placeholder,
  and the integrator's gate learned that distinction the hard way.
- The house wording list in `docs/brief_wording.md` §2 applies to what you **add**.
  Editing a historical document that already contains one of those words is fine and
  **check 10** will not fail you for it — it scans added lines only. That refinement
  exists because the integrator's gate failed a clean delivery on seven documents it
  had not touched.

## 9. What the integrator does with your delivery, so you can anticipate it

- **Every load-bearing number is recomputed on a second lineage.** Batch 14: the
  whole 4,198-label census re-run by Weyl alternation against a power-sum route; all
  153 exclusions recomputed; all ten Burnside sizes by direct enumeration; one 27
  million-monomial cell rebuilt from scratch on another host with the opposite
  `fo` setting. If a number cannot be reproduced, the entry is downgraded, not
  deleted — so make your route replayable and say what it was.
- **Your OPEN set is joined against the current ledger.** The ledger may have
  advanced past your dispatch base: B14-11's top shortlist entry was already closed
  by a rule banked after it dispatched. Your launch order is a proposal, and saying
  so costs you nothing.
- **Cited sources are read.** The BIP hypothesis, the proposition numbering, the
  version — checked against the paper. Cite the version.
- **Defects you report against the assignment are wanted and are acted on.** Batch
  14's most useful single finding came from a slot pointing out that the board had
  mispriced it, and the batch's own tooling carries five fixes that came from
  workers. Report them.

## 10. Where the fault actually lay in batch 14

Worth saying, because a checklist like this reads as though the sessions were the
problem. They were not. The recurring defects above are seam defects, and most of
the seams are the integrator's:

- the base was wrong three times before the tag settled it, and the dispatch message
  that was supposed to carry it never existed
- the packet shipped a bundle command that the delivery gate rejects
- four defects in the integrator's own intake gate, three of them the same species —
  a check that could only fail in one direction — the last of which **failed a clean
  delivery**
- a board that quoted a cost model its own index says not to quote, and sized a slot
  from a forbidden quotient
- two file references in an integrator review that were never written

Sessions found all of those. Keep doing it.

## 11. Two rules added in batch 19 (B19-11), from what batch 18 paid for

### 11.1 Any check whose subject can be empty ships the size of what it checked

A batch-18 prototype indexed its raising operators in the **source** weight space
instead of the shifted **target** space. The operators were therefore empty, every
"residual is zero" verification passed vacuously, and nothing in the output said so.
The error was caught only because the producer rebuilt the operators against the
correct target spaces and recorded their dimensions.

**The rule.** A certificate for any linear check — an operator annihilating a
vector, a kernel, a rank, a restriction — records, for each operator or map:

- the **source weight** and the **target weight** (or, outside weight spaces, the
  named source and target);
- **both dimensions**, source and target;
- the **operator's nonzero count** (entries, or terms, as stored);
- an **independent nontrivial action test**: the same operator applied to a fixed
  vector that is *not* expected to lie in the kernel, with the nonzero count of the
  result recorded. A zero here means the operator is empty or misindexed and the
  main check proved nothing.

A nonempty target space alone does not prove the operator was populated. A
"residual zero" without the four items above is a claim, not a certificate. The
same rule applies to any check whose subject can be empty: a filter that matched no
files, a census that enumerated no cells, a restriction to a subspace of dimension
zero. Ship the size.

Batch-19 reference implementation: `analysis/b19_11_vectors.py` in this worktree,
whose per-operator block records exactly these fields for the batch-18 sweep vectors.

### 11.2 Fetched literature stays out of the delivery tree

Third-party papers, their PDFs and full-text extractions are **not** delivered. Keep
them in a local reference cache outside every path an add list can take
(`docs/`, `analysis/`, `results/`, `delivery/`). In the report, record for each
source consulted:

- the identifier (arXiv number, DOI, or journal reference) **with its version**;
- the source URL and the **access date**;
- the **theorem, proposition, table or page** actually relied on;
- optionally, the SHA-256 of the copy you read, so a reader can confirm they have
  the same bytes.

Page images and text extractions are literature too. **Do not delete or untrack
literature already committed anywhere in the tree**: inventory it — path, size,
hash, tracked or untracked — and leave remediation to the integrator under separate
authorisation. Batch 19's inventory is in
`B15-11/results/b19_11/literature_inventory.json`.
