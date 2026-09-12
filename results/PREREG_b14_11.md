# B14-11 preregistration — exclusion audit and quartic shortlist

Date: 2026-09-12 UTC. board_numbering: batch14.
Actual model: gpt-6-astra (Codex); requested reasoning xhigh, not independently
introspectable. No other model or agent participates.
Branch: b14-11-astra. Frozen base: 9898e56941a7665f231873481dae956f08509995.
Base tree: cb688cd3fe454d638f3202e759e2eaa0c629739f.
Both HEAD and `git log -1 --format=%H batch14-base` match the base; the tag's
`%T` matches the tree. Initial working tree clean. No moving reference is used.

## Question, objects, instrument

Audit repository prose for an invalid BIP exclusion of ambient multiplicity-one
quartic labels. Enumerate distinct (n=4, delta, lambda), delta <= 8,
lambda a partition of 4 delta, 5 <= length(lambda) <= delta, lambda[0] >= delta,
a = [s_lambda] h_delta[h_4] > 0. Retain A1 unless a theorem or certificate
excludes it. Produce at most ten candidates with explicit exact filters and
costs; cost truncation is a funding decision, never a mathematical closure.

Use frozen census files as recorded inputs, with exact character scalar
products using banked `wk8_s30_pleth.pleth_p` and `chi` for recounts. Avoid
unbounded whole-ambient `amb` and do not use historical N_S/|Stab| as a bound
on n_chi. Use exact integer tail DP to size selected labels and independent
Weyl/weight enumeration controls where affordable. Every positive or zero
coefficient will be labelled by its actual verification. A frozen rank record
without a replayable certificate remains RECORDED, not newly proved.

Prove the quartic length bound directly: symmetrisation injects
Sym^delta(Sym^4 V) into (Sym^4 V)^tensor delta in characteristic zero;
successive Pieri horizontal 4-strips add at most one row each. Do not import
the cubic length theorem. Derive lambda[0] >= delta through the reducible
pullback and a horizontal delta-strip, which requires delta distinct columns.

Conventions: polynomial representation labels on the coefficient ring
Sym^delta(Sym^4 V), or dualise the underlying form space consistently;
partition order descending; unnormalised coefficient monomials; exact Z/Q
counts. For any stored matrix: rows are source vectors and columns are points,
values_are must be adjacent to data; relation columns K obey A^T K=0.
No evaluation matrix is planned. House primes 2147483647, 2147483629; rational
denominators must be prime units before modular comparison. Character sums
are reduced exactly over Q, and must be nonnegative integers.

## Decision table and falsifiers

* Missing required input, base mismatch, empty census or failed control: FAIL,
  never PASS. Missing optional historical certificates: RECORDED only.
* Actual length/containment or exact h_pad=0 predicate: exclusion in its stated
  domain; mere absence of a known equation or sampled deficiency: OPEN.
* Positive full minor: rank floor only. Complete interpolation needs all four
  stated conditions. No LMR update: a24=274, det=273, pad>=269, D in [-4,+1].
* A1 input with no valid exclusion must survive. Inject an occurrence rule,
  wrong ambient coefficient, empty input, duplicate key, invalid partition,
  wrong length/eligibility and a missing evidence input to exercise rejection.
* Check small plethysms by an independent route, including a zero coefficient,
  and reject at least one intentionally corrupted result per numerical control.
* Failure of the length proof or of a common Z/Q model stops that claim.

## Resources and stopping rules

Windows AMD64, Python 3.12.14, numpy 2.3.5; flint and psutil absent. No installs.
Exact stdlib arithmetic is sufficient for this combinatorial assignment; no
large exact linear algebra is scheduled. 20 logical CPUs, 33,752,997,888 bytes
physical RAM, 12,729,540,608 available at preflight; shared, not dedicated.
One calculation at a time, BLAS/OpenMP thread limits one. Each worker launched
with a PID log and parent-enforced timeout <= 300 seconds; per-worker memory
limit 1.5 GiB with Windows job/process accounting. Checkpoint per degree or
cell. At most 30 minutes aggregate heavy calculation, at most 120 seconds per
selected cost/count unless a committed addendum says otherwise.
If a complete fresh degree-eight census exceeds bounds, deliver the frozen
coverage reconciliation plus independently checked shortlist and exact partial
coverage; state the uncomputed labels. No unpriced giant expansion. Report
resource-ended calculations as such, not mathematical negatives.

## Already observed, expectations, provenance

Before registration only input reading, file searches, toolchain and host
inspection occurred. Observed stale BIP prose in n4_gate, easy_counts and later
summaries; observed that the inherited ledger lacks an occurrence predicate.
Also observed an overbroad arbitrary-weight-vector statement in BIP Lemma B;
will replace with a justified isotypic/highest-weight statement and a control.
The external BIP v3 PDF was read at arxiv.org/pdf/1604.06431: theorem 1.4 has
n>=m^25; its padding uses an existing matrix variable, unlike the independent
padding variable in this project. Neither input observation is a blind result.
Expectation: relabelling is incomplete; eligible A1 remain; no positive gap is
expected from a census. No new mathematical measurements have run.

Frozen input Git blob IDs (portable across line endings):

| path | blob |
|---|---|
| docs/dispatch/B14-11_packet.md | b8231c72c4e0ab507bf8cf0b892e6513e6f8d5fb |
| docs/batch14_board.md | 42e3da6b26c61a062c3534c1b6e9ebc2dd28cfdc |
| docs/PROVED.md | 68f2669eda3ceea9b677dbf85a113c6116eaf94d |
| docs/brief_wording.md | d906773e108e0d26dfed2f106db543152c698e0a |
| docs/batch14_reconciliation.md | 23faffc46b631fbd5a2f1a80b7dd2f318256e870 |
| docs/b14_claude_scratch_code.md | fbc558a87faf57acc91ea292eabdb5d93250ffeb |
| docs/bip_transfer.md | 13daab471a305579ee4bcb6d02ca45b334ee6e5d |
| docs/dip_transfer.md | 1822b9113bba48a44abe78bf191f997731ee7135 |
| docs/n4_gate.md | 00f825aab1502783582c4894afb8d3ad390e95e6 |
| results/integrate/inherited_exclusions.json | 02505480869719bdc333adcc41a50a3f1ed495ed |
| analysis/wk8_s30_pleth.py | cb0a9f7ff55d04e8ad276984b5cb00c633efb52c |
| analysis/wk9_s42_census.py | f68069805cc14f86b1a70f1175bb7ca3b65d6a13 |
| results/s42_census.json | c574fb6bb6e194af0eb8c0fcad8c8528068c2115 |
| results/s54_length5_census.json | 36a208ed2c461c219eb84e6c36597d9fc4b27ebf |

Delivery: intentional commits with actual model Co-Authored-By trailers;
report, replay scripts, exact artifacts, manifest, checker logs and named-ref
bundle against the captured base. No protected-file edits, pushes, integration
merge, other session worktree modifications or further automation.
