# Integrator review — B14-10

**Verdict: ACCEPT.** Every count reproduces, all four witnesses recompute, and
the one thing it left open — the mechanism behind the 29 digest discrepancies —
falls out of its own data.

Branch `b14-10-astra`, head `018678d1`, 4 commits over `9898e569`. Model
**gpt-6-astra**. Bundle sha256/md5 and size as declared; evidence ZIP sha256 and
size as declared. Intake CLEAN. Pre-registration first.

## The four witnesses recompute

Their standalone stdlib verifier passes on all four from inside the ZIP. I then
recomputed each 8×8 integer determinant with `python-flint`:

| cell | my det == claimed | nonzero | both residues |
|---|---|---|---|
| `(7,5,5,2,2,1,1,1)` | **yes** | yes | match |
| `(7,6,3,3,2,1,1,1)` | **yes** | yes | match |
| `(8,5,3,2,2,2,1,1)` | **yes** | yes | match |
| `(9,4,2,2,2,2,2,1)` | **yes** | yes | match |

`mult_per3 = a = 1` and `i_per3 = 0` over ℚ then follow from the indexed top-cell
theorem plus that nonvanishing. The report is explicit that these add **no**
frontier closure — the cells already lie inside `degree8_global` — and that they
are replacements for eight absent files, not recovery of the original bytes.

## `peaked_quartic_ladders`, ambient half checked

Computed `a` on the house `a_weyl` for `λ = (4δ − 2(ℓ−1), 2^(ℓ−1))` at
`(ℓ,δ) = (2,2), (3,3), (4,4), (6,6), (2,5), (3,6), (5,5)`: **`a = 1` at every
one.** The `mult_det = 1` half rests on their rank-15 trace pairing on `sl₄`,
which is their proof; the ambient half is now independently checked.

## Its scanner replay reproduces mine exactly

23 reports, 0 missing, 13 cross-path, 1 explicitly absent — the same four numbers
my own `tools/integrate/scan_unstaged.py` prints. Independent confirmation of the
staging picture, from a session that rebuilt it rather than reading my output.

## The 29 mismatches: reproduced, then explained

Walking `results/s79_cert_manifest.json` against the working tree:

| | B14-10 | mine |
|---|---:|---:|
| listed | 2,066 | **2,066** |
| present | 1,229 | **1,229** |
| absent | 837 | **837** |
| present, MD5 matches | 1,200 | **1,200** |
| present, MD5 mismatches | 29 | **29** |

Every figure. And the mechanism they left unknown is visible in the same file.
The manifest's own `shipped` flags read 1200 true / 866 false, and the 29
present-despite-`shipped=false` files close the gap in **both** directions:

    1200 + 29 = 1229 present      866 − 29 = 837 absent

with the mismatching set **identical** to the present-but-unshipped set. So the
question the report leaves open — whether those 29 are semantically equivalent to
the historical payloads — is the wrong question. The manifest never claimed to
have shipped them. They are unshipped paths that something later wrote to, not
corrupted shipped files. Indexed as `s79_digest_discrepancies_identified`; the
`digest_discrepancies.json` queue can be closed rather than worked.

## Its framing is right for an evidence slot

- 699 results and 175 metadata are "conservative content/schema classifications,
  **not** 699 new mathematical proofs".
- The 1,116 `hybrid_kernel` records are recognised but **not** marked PASS — the
  native verifier checks record consistency, not the claimed ranks.
- It flags that all 1,116 carry the producer's **erroneous** `field_note` saying a
  modular kernel bounds `i` from below. Wrong direction, and the same error class
  this batch has been correcting all week. Flagging it in the register rather than
  silently rewriting banked data is the right call.
- 223 cell keys stay **OPEN by name** in `remaining_cell_keys.json` rather than
  being guessed. "None becomes a false closure."
- The 837 absences are characterised as recorded shipping-size exclusions against
  the manifest's actual 60,000-byte cut, and it distinguishes that from the
  producer script's 150,000-byte default, the 3,000,000-term expansion condition
  and the 4,500,000-byte deletion guard — four different mechanisms that a looser
  report would have conflated.

## Two failures preserved rather than hidden

The first inventory hit the enforced 1 GiB limit after 19.594 s expanding a
compressed basis; streaming payload hashes with a materialization ceiling fixed
it. The first bounded reconciliation failed in 0.047 s because `runpy` had not
added the script directory to `sys.path`. Neither produced a mathematical PASS,
and both are in the record.

## Defects

**`PROVED.md` section collision, fifth instance** — B14-10 also claimed F.
Resolved to J, after F, G, H and I.

Its own defect notes are fair: 874 is a historical list length while the
comparable fresh discovery gap is 907; the packet's three absence categories omit
B13-09's documented shipment-prefix case; and the banked s57 dimension expression
`15ℓ−30` needs a stabiliser qualification and fails at `ℓ = 2` — correctly noted
as **not** indexed or used rather than quietly relied on.
