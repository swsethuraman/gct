# Integrator review — B14-03

**Verdict: ACCEPT.** The verifier does what a verifier has to do: it passes the
positive control, rejects every negative fixture, and rejects a mutation I wrote
that its own suite does not contain. Its Lemma CI then sharpened the `D ≤ −2`
entry in two places, which is the slot earning its place twice over.

Branch `b14-03-astra`, head `d1ef799d`, 2 commits over `9898e569`. Model
**gpt-6-astra**, effort xhigh, recorded from local turn context. md5 OK on whole
and part00; sha256 `dc241485…` and size 67442 both match the manifest. Intake
gate CLEAN. Pre-registration is the first commit.

## Run here

| | result |
|---|---|
| standalone checker, positive control | **PASS** — source dim 2, target dim 1, rank 1, `i_red = 1` |
| its reported internals | 561 weight dim, 1056 raising rows, 1720 terms, minor **209952** — every figure as stated |
| `corrupted_entry_control.json` | exit 1, **FAIL** |
| `missing_input_control.json` | exit 1, **UNPARSEABLE** |
| `duplicate_key_control.json` | exit 1, **UNPARSEABLE** |
| `rational_control.json` | exit 0, **PASS** |
| **my own mutation:** claim `i_red = 2`, leave all arithmetic saying 1 | exit 1, **FAIL** |
| `verify.py` dispatch after merging into the tree | PASS 1, FAIL 0, UNPARSEABLE 0 |

The last row of the first block is the one I cared about. A verifier that
accepted a false claim sitting on correct arithmetic would be worth nothing.
This one rejects it.

## Lemma CI, and what it changes about `lmr_D_upper`

`docs/b14_03_complete_interpolation.md` §1 states CI with four hypotheses and
two clauses that bear directly on the `D` result. I have amended the entry.

**The dimension sandwich.** "It suffices initially to prove `dim N ≤ h`: the
`h`-member nonzero minor supplies the reverse inequality." My entry named
`dim N₁₃ = 73` as the single point of failure. What actually carries the weight
is the **upper** bound `dim N₁₃ ≤ 73` — the 73-minor gives `≥ 73` by itself. So
the exposure is that both the Weyl and character routes are *short*, not that
they disagree with each other. Narrower and more accurate.

**Source completeness.** "If sources only span a subspace, CI computes its
restriction kernel; identifying an ideal multiplicity requires completeness in
the intended `M`." This is a hypothesis I had checked but had not recorded *as*
a hypothesis. It is exactly why `a(21,17,2⁷;13) = 39` mattered: with B14-02's
nonzero generic 39-minor, the 39 rows are a basis of the ambient space, so
`i_red(13) = 3` is an ideal multiplicity and not an artefact of an incomplete
source. Both conditions are now written into `lmr_D_upper` as the two things
carrying it.

The D chain satisfies all four of CI's hypotheses as B14-03 states them:
`dim N₁₃ = 73` established independently of any sampled source rank (Weyl and
characters); 73 verified members (B14-01's 72 checked four ways, plus `φ(F₁₅)`
by equivariance); a nonzero 73-minor; and exact source arithmetic from B14-02.

Also worth keeping: **"Missing an input never weakens the verdict to PASS."**
That is the right default for a fail-closed checker and it is implemented —
three of the four negative fixtures are missing-input cases and all three
return UNPARSEABLE rather than PASS.

## Scope, stated correctly

The verifier implements the **`h = 1` profile only**, not a degree-13/14 bracket
engine, and the report says so without hedging. Its five-second ternary control
prices nothing about larger cells and the report refuses to infer a runtime.
The `NOT REACHED` on the legacy-corpus re-derivation is honest — flint and scipy
are absent on that host and no legacy arithmetic was changed.

The report still records LMR at `D ∈ [−4, +1]`. That was correct when written;
the joint B14-01 + B14-02 result landed after. Not a defect.

## Defects

Its own: the packet's checkout and HEAD-only bundle examples conflict with the
launch brief — **fourth session to report the bundle command**, and the launch
brief is what governed, correctly. The packet's flint/Linux commands needed the
Windows/exact-stdlib adaptation the brief authorises. And the legacy verifier's
eager flint/scipy imports would have prevented even this stdlib-only checker
from running; the lazy per-kind imports fix a real integration fault.

**Mine, found by this delivery:** my intake gate read every blob as text and
died with `UnicodeDecodeError` on `control.json.gz` — the first binary file any
session has shipped. A gate that crashes on a legitimate delivery is worse than
no gate. It now reads bytes, skips text checks on binaries and records that it
did; selftest still passes.
