# Review of B14-11

**Slot:** B14-11, quartic exclusion audit and shortlist. Astra (`gpt-6-astra`), xhigh
requested, no subagents.
**Base:** `9898e569` / tree `cb688cd3`, the dispatch base, matched exactly.
**Delivered head:** `54effabc` / tree `ca060ddf`. Bundle 458,313 bytes,
md5 `4cb60ed3fdf396534cba9a5eda8bb2a4`, whole and `part00` byte-identical, both
sha256 sidecars `8b6d7663…`. `git bundle list-heads` gives one ref,
`refs/heads/b14-11-astra`. The four single-writer files are untouched.
**Verdict: ACCEPTED.** Merged at `1113a0ff`. Every load-bearing count was
reproduced here by a second route, and the whole census was recounted, not sampled.
One consequence the slot could not see changes its recommended next run.

## 1. What it claims, and what I checked with my own code

| claim | how I checked it | outcome |
|---|---|---|
| the region `n=4`, `delta<=8`, `5<=ell<=delta`, `lambda_1>=delta` has 4,198 labels | my own partition enumeration | identical label set, 4,198 |
| 2,734 of them have `a>0`, 667 have `a=1` (22/163/636/1913 and 22/92/203/350 by degree) | house `a_weyl` — Weyl alternation, weight-space DP at both primes, CRT — run over **all 4,198**, against B14-11's power-sum/Murnaghan–Nakayama route | **0 mismatches in 4,198**, 207 s; same per-degree split |
| `a>0 ⟹ ell(lambda) <= min(dim V, delta)` | `a_weyl` on every over-length label at `delta<=7` | 1,879 labels, all `a=0` |
| `mult_pad>0 ⟹ lambda_1 >= delta` | own horizontal-strip enumeration into `Sym^d V ⊗ Sym^d(Sym^3 V)` | 789 labels at `delta<=5`, no violation |
| 153 labels have exact `h_pad=0` | own strip enumeration + house **cubic** plethysm coefficients | 153/153 zero |
| the ten shortlist `h_pad` values 2,5,1,2,4,1,6,5,4,4 | same route | all ten exact |
| `n_chi = \|G\|^-1 Σ ε(g) Fix(g)` with `ε(g)=Π sign(g_b)^b` | re-derived: `P_ij = diag(1,-1)·n_ij`, and the Weyl representative acts trivially on a HWV of `SL_2`-weight `lambda_i-lambda_j=0`, so a transposition of equal parts `b` acts by `(-1)^b` | the character is right |
| the ten `N_S`, `\|G\|`, signed sums and `n_chi` | direct enumeration of each weight-`lambda` monomial basis, `Fix(g)` by elementwise comparison over **every** group element (so class sizes are checked, not assumed) | all ten exact; every shipped class representative's trace **and** sign agrees |
| controls `(3,3,1,1)_2 = 2`, wrong trivial character gives 4; `(14,2,2,2,2,2)_6 = 7508/171` | same route | both reproduce |
| power-sum denominators, quartic and cubic, `delta` 5–8 | own plethysm-to-power-sum expansion with `Fraction` | all eight values exact; `gcd` with both house primes is 1; the `delta=5` term count 241 also matches |
| 88 frozen input blobs | `git rev-parse` + sha256 against the base tree | 88/88 byte-identical |
| BIP v3 Theorem 1.4 assumes `n >= m^25`; Proposition 2.3 with `sharp` extending the first row | fetched arXiv:1604.06431v3 (2018-09-17, the version the manifest records) independently of the delivery | confirmed verbatim; at `(4,3)` the theorem needs `n >= 3^25 ≈ 8.5×10^11`, so it is silent |
| at `n=4` Prop. 2.3 yields `(4)_1` and `(6,2)_2`, at most two rows | re-derived from the quoted statement: `n>=k·ell`, `ell` even forces `k<=2`, `ell<=2`; `sharp` to `nk` boxes | exactly those two — **the same two partitions the house found in-house as the multipliers `u` and `q62`** |
| the old span lemma is false for arbitrary weight vectors | own evaluation: `c_(3,1)((x+y)^4) = 4` at a span-1 point, weight length 2; also `c_(2,1,1)((x+y+z)^4) = 12` | false as stated |
| the corrected isotypic/HWV form holds | the engine is `K_{lambda,mu}>0 ⟹ ell(mu) >= ell(lambda)`: the `s`-th partial sum of a shorter `mu` already exceeds `lambda`'s. Machine-checked on 1,818 `(lambda,mu)` pairs to `\|lambda\|=9` | holds; the conclusion of `bip_blind_at_n4` survives |
| `easy_counts`'s BIP sentence should read as ambient arithmetic | the house's own `docs/ambient_audit.md` §8 already said so and asked for the fix; `Sym^2(Sym^5)` has exactly three constituents `(10),(8,2),(6,4)` — recomputed | correction is right, and closes a house-recorded open item |

Nothing in the delivery claims a rank, an equation or a kernel, and `rank_or_equation_certificate_claimed` is `false` in `validation.json`. That matches what the
files contain. `h_pad>0` is used as an upper bound only, never as evidence of
`mult_pad>0`, and `n_chi` is labelled a carrier size throughout.

## 2. The one finding that changes the next run

**D1 (integrator-side, not a slot defect). Shortlist entry 1 is already closed.**
`peaked_quartic_ladders` — banked from B14-10, s57 Theorem P — gives
`a = mult_det = 1`, `i_det = 0` and hence `D <= 0` at every
`lambda = (4delta-2(ell-1), 2^(ell-1))` with `delta >= ell`. B14-11's top candidate
`(16,2,2,2,2,2,2)_7` is exactly that shape at `ell = delta = 7`. So is
`(18,2^7)_8` and `(20,2^6)_8` in its queue. Across the census the rule closes
**10 of the 2,734** positive labels, exactly the peaked shapes with `5<=ell<=delta<=8`.

That rule entered the repository *after* dispatch base `9898e569`, so B14-11 could
not have seen it, and its report correctly states that no concurrent session's
result was used. This is a cross-slot collision only the integrator can catch.

I did not take B14-10's word for it. The witness is a trace form on `sl4`: I rebuilt
the Gram matrix `tr(A_i A_j)` from the shipped basis with my own multiplication and
trace (identical to the banked values), and recomputed all 15 leading minors with
`python-flint`. At `ell = 7` the determinant is `-64`, nonzero, so `mult_det = a = 1`
at `(16,2^6)_7` and the closure is real.

**Consequence for the launch order.** Entry 1 needs no determinant evaluation. The
smallest open carrier is **entry 3, `(11,8,5,1,1,1,1)_7`, `n_chi = 1,576`**, then
entry 8 `(13,5,5,2,1,1,1)_7` at 10,923. The join is recorded in
`results/integrate/b14_11_ledger_join.json`.

**None of the 153 new exclusions was already closed** by the banked ledger: all 153
are net new. With them the ledger now closes 163 of the 2,734, leaving 2,571 open.

## 3. Defects in the delivery

**D2. The two new ledger predicates broke the consumer rather than being skipped.**
B14-11 appended `quartic_length_and_eligibility` and `quartic_pullback_zero` to
`inherited_exclusions.json` and wrote that "the old range-only `reconcile_cells.py`
deliberately skips these unfamiliar predicate shapes." It does not skip them. The
matcher's allow-list branch **raises** on an unrecognised key, and
`conclusions_for` raises even earlier — the entries carry no
`application_contract.conclusions_by_id` record — so after the merge *every* query
for *every* cell failed with `ValueError`. The instinct behind the warning was
right ("never treat an unrecognised predicate as all `n=4`"), but a fail-closed gate
that fails closed on the whole file is not a skip.

Fixed here rather than deferred: `exclusion_predicates.matches` now implements
`any_of`, `lambda_length_gt_delta`, `lambda_1_lt_delta` and `explicit_cell_keys`
(the last loading the named catalog and raising if it is absent, so a missing
certificate can never read as "no match"), and both ids have application contracts.
Tested in both directions — the shortlist cells do not fire the relational rule, all
153 explicit keys do fire, a cell satisfying neither branch does not, an unknown key
still raises, and a missing catalog still raises.

**D3. `results/b14_11/prose_changes.json` is right; `PROVED.md` table syntax was not.**
The `quartic_signed_burnside_size` row shipped `|G_lambda|` with unescaped pipes,
which splits one markdown cell into four. Repaired in the merge. Small, but this is
the citation index — it is read as a table.

**D4. "Resolved" overstates the padding-model finding.** `docs/bip_transfer.md` now
closes with "B14-11 resolved convention". What is established is that BIP pads with
`X11`, a variable already inside `per_m`, giving `m^2 = 9` essential variables against
this programme's independent-`x0` ten. What is *not* established is that
Kadish–Landsberg's `ell(lambda) <= 9` therefore fails to transfer: BIP itself calls
the distinction irrelevant and cites an appendix for it. So the `ell = 10` question
moves from "flagged, not claimed" to "identified, not imported" — still open, and
still worth one session. I have recorded it that way in `bip_blind_at_n4` rather than
as resolved.

**D5. Its LMR summary is stale, correctly so.** "LMR remains `a24=274`,
`mult_det=273`, `mult_pad>=269`, `D in [-4,+1]`" was true at `9898e569`. `lmr_D_upper`
has since put `i_pad(24) >= 3` and `D_LMR in [-4,-2]`. Not a defect — the slot was
required not to use concurrent results, and it did not — but readers of
`docs/b14_11_report.md` should take `PROVED.md` as the current statement. Recorded
here rather than by editing the delivered report.

**D6. The garbled `bundle_prerequisites`, a fourth time.** The manifest's
prerequisite field again carries the base commit's *subject line* captured alongside
the hash. Same shape as B14-04, B14-05 and B14-08. Harmless — `git bundle verify`
reports the prerequisite correctly — but it is now four of six Astra deliveries and
belongs in the batch-15 manifest template as a field that must be a bare hash.

## 4. Defects in my own material, found by this delivery

**My intake gate failed a clean delivery.** Check 8 scanned the whole new content of
every changed `.md`, so a slot that edits a historical document inherits that
document's wording debt. B14-11's prose audit tripped seven of these and **added not
one list word** — I verified added and removed lines separately before believing the
gate. Check 8 now scans added lines only and reports pre-existing hits as notes
naming them as integrator debt. `--selftest` gained the missing direction: a delivery
that edits a base document containing a list word must come back clean, alongside the
existing case that adds one and must be rejected. Both pass. This is the fourth
defect in this gate found by a delivery rather than by me, and the third of the same
species — a check that could only fail in one direction.

**Seven historical documents carry list words at the base:** `batch11_plan`,
`n4_gate`, `s24_obstruction`, `s25_race`, `screen_results`, `session_24b`,
`washout_threshold`. Recorded, not silently rewritten: they pre-date the wording
policy and editing them for vocabulary alone would obscure the audit trail.

**Two readings in my own `bip_transfer.md` are withdrawn, correctly.** The `chow6`
zero was recorded as a *second, independent* reason BIP's supply fails at `n=4`,
"that point has full support 6". A product of four linear forms has essential span at
most 4 whatever coordinates appear in it, so a six-row HWV must vanish there: the
zero is forced by the same lemma and is not independent evidence. And the
`4·3-3 = 9` dimension comparison does not hold as stated, since the support subspace
varies with the point. Neither carried the conclusion — Lemma B does — but both were
overstated, and `PROVED.md` now says so.

**`PROVED.md`'s own `bip_blind_at_n4` carried the false lemma.** "A weight vector of
weight `λ` vanishes at every point of span `< ℓ(λ)`" is false; `c_(3,1)` on `(x+y)^4`
is a two-line refutation. The isotypic form is the true one and is what the entry
needed. B14-11 repaired the row in place; I have extended it with the source check,
the two withdrawals and the open padding-model question.

## 5. What is now open

After this merge, of the 2,734 positive labels in the region: **163 closed**
(153 pullback-zero, 10 peaked ladder), **2,571 open**. The 866 labels B14-11 marks
`OPEN_IN_THIS_AUDIT` are open because it did not replay their certificates, which is
the honest state, not a downgrade.

The mathematical bottleneck is unchanged and correctly named: an `a=1` cell can
separate only by an occurrence obstruction, and nothing in the literature excludes
one at `(4,3)`, so these cells are open rather than closed. Closing one needs a
nonzero determinant-side HWV evaluation with a forced-zero control; vanishing on
samples leaves it open, since a sampled zero is a ceiling on the ideal dimension and
never a floor.

## 6. Batch-15 items added by this slot

1. The manifest template must specify `bundle_prerequisites` as a bare 40-hex string
   (D6, fourth occurrence).
2. A packet that appends to `inherited_exclusions.json` must require the
   `application_contract` entry in the same commit, and must state that the consumer
   fails closed by raising, so a new predicate shape is an integrator deliverable and
   not a skip (D2).
3. The board must tell each slot that the ledger may have advanced past its dispatch
   base, and that the integrator joins its OPEN set against the current ledger at
   intake — so a slot's own launch order is a proposal (D1).
