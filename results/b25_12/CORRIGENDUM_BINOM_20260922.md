# Record-level corrigendum — `binom(77,8)`, 2026-09-22

Written by the housekeeping pass PART 17e (Claude Code, Claude Opus 5 (1M context)) for the B25-12
record. **No sealed packet is edited.** Every file named below stays byte-for-byte as committed. This
corrigendum is the record's correction, by reference.

## The correction

Three packets print `binom(77,8) = dim Sym^8(C^70) = 21,042,084,900`:

| packet | commit | location |
|---|---|---|
| B19-02 | `75ddb900a0b47b911c53f941885bac73b358eacb` | `docs/b19_02_report.md` L269, degree-eight row of the dimension table (`21042084900`) |
| B23-02 | `68866e6ddc4deb38ac1fa29ffc1294395178357a` | `docs/b23_02_report.md` L238, §1 elimination pricing, citing B19-02 §5 `A(8)` |
| A25-01 | `aca16c7531483163d392200baced8757fb8746ca` | `docs/a25_01_report.md` L38, §4, "as priced in B23-02" |

**The value is `21,042,072,975`**, 11,925 less. By the hand recurrence
`C(77,k) = C(77,k−1)(78−k)/k`, `k = 0..8`, the values are 1; 77; 2,926; 73,150; 1,353,275;
19,757,815; 237,093,780; 2,404,808,340; 21,042,072,975. That matches exact integer arithmetic.

**No conclusion changes.** One dense eight-byte vector of the corrected size is 168,336,583,800 bytes,
far beyond the 512 MiB cap, so every pricing argument that used the figure is unaffected.

## Authority

A25-10 `docs/a25_10_report.md` §"Decisive checks", at `ab4f527189bea14b5d146f9dc9d5b445844eaff3`:

> **The arithmetic correction is `binom(77,8) = 21,042,072,975`.** The printed 21,042,084,900 already
> occurs in B19-02 and was propagated through B23-02; A25-01 did not miscopy its source. A hand
> recurrence verifies the correction. A single eight-byte dense vector still costs 168,336,583,800
> bytes, leaving the cost assessment unchanged.

Detail: A25-10 `results/a25_10/REVIEW.md` §1, "Arithmetic provenance repair". A25-10 establishes the
checked chain B19-02 → B23-02 → A25-01. It does not assert where the error first appeared
historically.

## Related records

- A25-01's own erratum: `work/batch15:results/a25_01/ERRATUM_20260922.md` (PART 17d). A25-01's seal
  is preserved.
- This branch's ledger (`docs/b25_12_ledger.md`) and
  `results/b25_12/integrator_notes/A25_INTEGRATOR_VERIFICATION_NOTE.md` quote the wrong figure only as
  the finding to be checked. The ledger item that marks the attribution "OPEN for A25-10" is answered
  by A25-10: B23-02 printed the figure, inherited from B19-02, and A25-01 copied it correctly.
