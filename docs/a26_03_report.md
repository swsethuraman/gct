# A26-03 — contraction redesign: incremental producer report

UNCOMMITTED / PRODUCER ONLY. One candidate only; zero pilots and zero mathematical programs.

## Increment 1 — preflight and selected object (written 01:33:08 UTC)

Session opened 2026-09-23T01:29:21Z; first explicit UTC observation 01:29:37Z.
Own session metadata identifies gpt-6-astra / xhigh and task
01a0cbe1-b51e-7b00-b1f7-525b906c89fc, distinct from the notes' 01a0c159… lineage.
This is a fresh task, not the coordinator conversation.

Preflight passed: work/batch15 is on batch15-launch, HEAD
7464a2bd02c9740db55d15ac43571cca74acea5f exactly. Both output paths and analysis/a26_03_*
were absent. No applicable AGENTS.md or CLAUDE.md was found at the project/worktree
roots, ancestors checked, or under docs/results/analysis. Existing untracked paths:
docs/a26_02_review.md, results/a26_02/, results/a25_10/literature/,
results/b15_integrator/. They are left alone. Git warned that the global ignore file
was unreadable; no setting was changed. The stale held status in the administrative
ledger is superseded by the user's explicit launch and this slot's precedence rule.

Required SHA-256 bindings, each naming raw administrative working-copy bytes:

| File | SHA-256 |
|---|---|
| B26_COMMON.md | a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd |
| A26-03.md | d1a15deda8dd8af882dc2b77bd6c2d01934718027c884d38f8b8e4291cfc1991 |
| BATCH26_LIVE_LEDGER.md | 1ec1ff50dc397e8df4505e03902393fd95cd7974b1196468b66c4e5115c38a10 |

READ: the governing B26-02 audit at cdf6839cd81031d42e43dc640b08e2746a7ef22c.
Its committed LF manifest hashes to
02060eac5391002420d5bbc216da02543a3dec79899c05a835bc84b6951a0cb9;
all five listed payloads match their committed byte counts and SHA-256 values.

Selected redesign (hand definition): n=4, d=50, the K5,5 half-edge labels of the
audited base tableau. Replace the doubled height-two columns (a00,b00) and
(a02,b02) by two identical height-four columns (a00,b00,a02,b02). All other
columns stay as defined in the audited base. The new shape is (68,68,22,22,20).
No other redesign is being considered.

Preliminary hand result: at q0=sum_(c=0)^4 (x1+c x2+c^2 x3+c^3 x4+c^4 x5)^4,
f(q0+s B^2) is a quadratic polynomial in s with positive coefficients. Thus the
new contraction sees B^2. Retaining paired columns also gives f(Q^2)>0 for
Q=x1^2+...+x5^2, and Q^2 is an explicit 4-by-4 determinant. The final packet
will state the exact certificates and close under the one-failure stop rule.

No five-row determinant equation is known to be nonzero on padding.

## Increment 2 — final verdict and early stop (checkpoint 01:35:25 UTC)

**Registered outcome 3: REJECTION.** The one redesigned function is admissible,
nonzero and highest-weight, and sees B^2. It is strictly positive on a literal
determinant, so it fails the determinant-equation requirement. The first failure
closes the slot. No second pattern or family was attempted.

**Hand derivation, exact certificates:**

1. `results/a26_03/PROOF.md` section 1 fixes content 50 x 4, shape
   (68,68,22,22,20), every column, orientation and tensor normalization.
2. Section 2 specifies a rational ambient quartic q0 and exact finite sums
   C0,C1,C2 with f(q0+s B^2)=C0+C1 s+C2 s^2. Each coefficient has a proved
   strictly positive rational lower bound. In particular the dependence is
   quadratic, not only a column-level indication of visibility.
3. Section 3 specifies K_Q with det K_Q=Q^2, Q=x1^2+...+x5^2, in the normalized
   determinant chart. A finite positive fourth-moment identity and the elementary
   five-point grid lemma give f(Q^2)>=1/(3^50 12^250)>0. The finite sum is not
   enumerated. This is an exact structural nonvanishing certificate, not a sample.

**Padding status: unresolved for this redesign.** The old padding proof applies
to the old contraction. It cannot be inherited after the column merge. No
actual-padding nonvanishing or vanishing claim is made; the mandatory stop
after determinant rejection makes a further padding check unnecessary for this
registered outcome. No conclusion about f(p4)-f(D4) is made or used.

`results/a26_03/CHECKPOINT.md` records the four early-checkpoint items, the full
scope comparison and a priced hand-only plan. In particular, the single graph
component has 50 vertices: it is in B25-04's symbolic sub-D* family exactly if
50<D*. The record does not determine that inequality. We do not certify an
unconditional escape from that theorem or from every possible minor extraction.
The independent determinant rejection is decisive in either case. Application
3 retains its proved ceiling 245 and CERTIFIED-modular one-prime floor 299.

**Achievement level:** a visible, nonzero coefficient function and a rejection
certificate only. No new source condition, determinant coefficient equation,
separation on padding, positive multiplicity gap, geometric noncontainment or
asymptotic lower bound. A25-10's READ decision remains "no construction ready."

**Exact feasibility obstruction and reopening condition (hand derivation):**
retaining wholly paired columns in this quartic contraction gives a positive
sum on Q^2. Recovering visibility by this merge does not evade that obstruction.
Any separately authorized reopening must evade it and furnish separate visibility,
actual-padding and determinant certificates. No replacement candidate is nominated.

## Limitations and delivery

This is one n=4, d=50 redesign, not a conclusion about n=5 or arbitrary sums.
The certificate is producer-only and has no independent review. No graph
connectivity-to-irreducibility claim, independence claim, spectral comparison,
expansion argument, numerical replay or claim about all evaluation algorithms is
used. A26-01 is delivered but unreviewed and supplies no premise; the other
prohibited mathematical inputs are not used.

The packet contains this incremental report, PROOF.md, CHECKPOINT.md,
SOURCE_LEDGER.md, INPUT_BINDINGS.json, RESOURCE_RECEIPT.md, the administrative-only
ADMIN_SEAL.ps1, PROPOSED_DELIVERY_PATHS.txt and MANIFEST.json. The manifest binds
every payload's raw SHA-256 and byte count, excluding itself. The proposed
delivery list includes the manifest. All paths remain UNCOMMITTED / PRODUCER ONLY.

Resource receipt: zero pilots, zero mathematical programs, zero leases, zero
subagents and no Git mutation. UTC session origin 01:29:21, first explicit clock
01:29:37, mathematical stop / early checkpoint 01:35:25, all on 2026-09-23.
This is at most 6m04s through the mathematical stop, including administration;
there were no interruptions or time deductions. No 45-minute checkpoint became
due. Subsequent work was certificate transcription, source-scope reporting,
byte binding and packet verification. The final receipt records packet stop.

At 01:38:04 UTC, branch and HEAD still exactly matched preflight; status showed
only the four original untracked entries plus this report and results/a26_03/.
No existing file, sealed packet, ledger or Batch 25 record was edited.

No five-row determinant equation is known to be nonzero on padding.
