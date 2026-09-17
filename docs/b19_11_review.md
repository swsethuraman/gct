# B19-11 review — the evidence packet, and what it found

Report: `work/batch15_workers/B15-11/docs/b19_11_report.md`. Started from `18ff3d0c`,
tree `808349e0`. Packet `results/b19_11/`, 70 files.

## Verdict

**ACCEPT.** It did the job and, more importantly, it found the thing it was sent to
look for. I ran its own §9 cross-seam test and the packet passes completely.

## 1. The cross-seam test, run here

§9 proposes: read one packet file, **import no project code**, rebuild the four raising
operators from `MONS` and the basis tuples, confirm the counts and dimensions, apply
them to `W` and `e_0`, and evaluate `W` at the first determinant point. I did exactly
that on `S19.json`, `lambda = (6,4,4,4,2)`, `K = 11640`.

| operator | target weight | target dim | claimed | nonzeros | claimed | `E(W) = 0` | `E(e_0)` nz | claimed |
|---|---|---:|---:|---:|---:|---|---:|---:|
| `E_1,2` | `(7,3,4,4,2)` | **8519** | 8519 | **30049** | 30049 | yes | 2 | 2 |
| `E_2,3` | `(6,5,3,4,2)` | **10174** | 10174 | **30049** | 30049 | yes | 2 | 2 |
| `E_3,4` | `(6,4,5,3,2)` | **10174** | 10174 | **30049** | 30049 | yes | 2 | 2 |
| `E_4,5` | `(6,4,4,5,1)` | **6545** | 6545 | **19201** | 19201 | yes | 1 | 1 |

Target dimensions came from my own weight-multiplicity table, which also returns
`M[lambda] = 11640 = K`. The vector is primitive with positive first nonzero, max
coefficient 82944, 11640 nonzeros — all as recorded. Every residue is exactly zero over
`Z`.

**And the value.** Evaluating `W` at the first recorded determinant point with my own
determinant code gives

```
33900369404217588856
```

matching the certificate and §9's target exactly.

So **rule 11.1 now has its worked example on both sides of the seam**, which is what §9
asked for. My rebuild used no project code for the operators, so it is also an
independent check of the operator structure and of the annihilation — not a third
lineage for the highest-weight construction itself, but it does close the part of the
gap the slot flags in its own honest negatives.

## 2. One gap in the packet, found by running the test

**The packet does not carry the evaluation points.** Step (iv) needed the batch-18
certificate `B15-06/results/b18_06_sweep/S19.json`, because the packet records the
*value* and not the *point*.

§5 says "A reader with the JSON alone, and no code, can evaluate `W` at any point and
rebuild the raising operators." That is true and it is not the same as replayable: a
reader with the JSON alone **cannot reproduce the recorded value**, which is the thing
replay means here. The packet pins the certificate by SHA-256, so the reference is
sound and nothing is unverifiable — but portability is two files, not one.

**Fix, and it is small.** Inline the six points into each packet. A determinant point is
a `4x4` array of 5-vectors, 80 integers; six points is under 500 integers against a
750 kB file. Then the claim in §5 is exactly true.

## 3. The defect it found, and whose it is

**The batch-18 vectors did not ship with their ordering.** The certificates carry size
data and values; the vector and the ordering exist only as code plus a seed, with the
ordering defined implicitly by the recursion order of an unhashed helper. A change to
that script would silently change what "the vector" means.

**That one is mine.** I reviewed the B18-06 sweep and accepted it. My review praised the
recorded shifted-weight target dimensions — correctly, that was the right instrument
against vacuous passes — but I never asked whether `W` itself shipped. I only thought to
ask when writing this slot's prompt, one batch later, and then I asked the slot rather
than checking myself. A certificate that is replayable-from-code but not
portable-as-data passed my gate.

The slot's fix is right: regenerate with the unmodified script, write vector plus
ordering plus an expanded-ordering hash, and replay every recorded number. 21 cells,
126 values, all matched.

## 4. Literature: the decision is now mine, and the options are narrow

The inventory is clean and it stopped where it was told to:

- **Four third-party PDFs, about 1.2 MB, are committed** on `b15-12-padding-orbit-bounds`
  under `results/b15_12/sources/` — BIP, BLMW, IP and KL. They predate Phase B, so they
  came in at the batch-15 frozen head, and they are now on the public remote.
- Two PDFs and two full-text extractions, about 1.07 MB, sit untracked in
  `B15-01/results/b18_01/literature/` — the ones I stripped from the add list on
  Monday. Still untracked, still one wholesale add list away.
- One copy in `Batch16/`, outside any repository.

**On the committed four, I want to be plain about what can and cannot be done.** They
are in the published history. Removing them from `HEAD` stops the working tree carrying
them but does not remove them from history, and rewriting history is forbidden by the
standing constraints and would in any case not affect what is already fetched. So the
realistic options are: leave them and record the decision, or add a deletion commit that
stops future checkouts carrying them while the history retains them. Neither is a
retraction. I would take the second and record it, but it is your call and it should be
made knowingly rather than by default.

The untracked four are easy: they stay untracked, and rule 11.2 now makes that a
contract term rather than my vigilance.

## 5. What else it got right

- **It labelled what it did not read.** "One commit ahead" is MEASURED; "that commit is
  the rules commit" is ADOPTED from the launch document, because reading it needs
  `git show`, which it may not run. Exactly the right split.
- **It declined to accept anything.** "A hash proves a file is unchanged, never that the
  claim inside it is true", and the packet "binds bytes; it accepts nothing."
- **It flagged its own lack of independence.** "The replay used the sweep's own code…
  this slot adds replay fidelity, not a third lineage." True, and it is the honest thing
  to say about a replay.
- **It found that four documents are CRLF on disk** and hashed the bytes as the batch-19
  attribute rules intend — the rule I had to repair on Monday, now being used correctly
  by a later slot.

## 6. What enters the index

| id | statement | status |
|---|---|---|
| `vectors_did_not_ship_with_ordering` | The batch-18 sweep certificates record each vector's size data and values but not the vector or its monomial ordering; the ordering was defined implicitly by an unhashed helper's recursion order. Replayable from code plus seed, not portable as data. A certificate whose meaning depends on unhashed code is not a certificate | RECORDED defect; integrator's, accepted at the B18-06 review |
| `b18_vectors_now_portable` | All 21 batch-18 vectors regenerated with the unmodified sweep script, written with explicit ordering and an expanded-ordering hash, verified exactly over `Z`, and replayed against all 126 recorded point values, all size data and all residues. 21/21 `REPLAYED_ALL_MATCH` | CERTIFIED; S19 independently rebuilt across the seam here |
| `packet_omits_the_points` | The vector packets carry values but not evaluation points, so a reader with one packet alone can evaluate `W` anywhere but cannot reproduce a recorded value. Inline the points | RECORDED, small |
| `literature_is_committed` | Four third-party PDFs (~1.2 MB) are committed on `b15-12-padding-orbit-bounds` and published; two PDFs and two extractions (~1.07 MB) are untracked in B15-01; one copy sits outside any repository. Inventoried, untouched | MEASURED |

## 7. Carry-forward

1. Inline the six points into each vector packet.
2. Decide the committed literature, knowing that neither option is a retraction.
3. The contract edit (§11 of `delivery_contract.md`) is the one tracked modification and
   is mine to commit — it will need the byte gate like everything else.
