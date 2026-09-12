# Integrator review — B14-01

**Verdict: ACCEPT.** Delivery clean, every load-bearing claim independently
checked, and the session's one open question is closed by this review in the
direction it thought less likely to need work.

Branch `b14-01-mixed-brackets`, tip `cf68004c`, 6 commits over `9898e569`.
`md5 -c` OK on both the whole file and `part00`, which are byte-identical (a
genuine one-part delivery, as the report's first paragraph states). Intake gate
CLEAN. Pre-registration is the first commit.

## What I verified myself

| claim | how I checked it | result |
|---|---|---|
| rank 72 at both primes | rebuilt the 72×96 matrices from the shipped rows in `python-flint`, computed rank | **72 and 72** |
| `det = 462198740` / `1924539738` | recomputed both 72×72 minors from the shipped rows | **both match exactly** |
| minor columns are real primary points | 72 indices in range, ids match `primary[index]`, `u_symbols` match the point file 72/72 | **72/72** |
| `u(P_j) ≠ 0` on the minor | min `|u|` = 48 | **all nonzero** |
| 72 distinct members | hashed each filling | **72 of 72 distinct** |
| strip counts 15 and 27 | my own interlacing enumeration, and separately the session's closed form | **15 and 27, and the closed form generates exactly the same set** |
| blob contract | `P13`, `P14`, `s74/source.json` at the base tree | **all three match the board** |

The determinant and rank checks are arithmetic on the session's own numbers, and
I say so: they confirm the minor is what it claims to be, not that the rows are
correct evaluations. The independent-evaluator check is M5's job and the session
did it (a second Python DP, different state encoding, 4/4 at the real shape); I
did not write a third.

## The open question in §7 is closed — it is the span, not the count

The report leaves two live branches and declines to choose. The discriminator it
proposes — recount `a₃(μ,13)` for the five `μ₉ = 1` strips by the character
route — **was already banked before dispatch and I have now run the comparison.**
All fifteen channels agree between B13-01's Weyl alternation and Astra's
power-sum/Murnaghan–Nakayama route, partition by partition:

    (21,5,2^6,1) 1=1   (20,6,2^6,1) 2=2   (19,7,2^6,1) 3=3
    (18,8,2^6,1) 4=4   (17,9,2^6,1) 4=4        sum 14, exactly as predicted

and the other ten likewise, total 73 = 73. The five strips the session
identified as where a miscount is most plausible are among the five that agree
most cleanly.

**So `h_pad(21,17,2⁷;13) = 73` stands on two independent lineages, and the
remaining branch is the spanning one.** That is a finding about the instrument,
not about the arithmetic, and it carries to rung 14. It does not yet prove the
mixed brackets span only codimension 1 — 78,814 candidates in one 72-space is
strong evidence, not a proof — but the cheap alternative explanation is gone,
and slot 4 should not be asked to spend a run on it.

The session was right to decline the assertion and right about which branch was
less likely. It could have closed this itself: the character pilot and both
per-channel tables were in the tree it checked out.

## Defects reported, all confirmed, one magnitude wrong

1. **No dispatch message reached the session.** Confirmed, and it is mine: I
   wrote the launch messages after the packets and told the packet to rely on
   them. The substituted cross-check is sound and correctly labelled weaker.
2. **The packet's bundle command produces a bundle the repository's own gate
   rejects.** Confirmed, and the session's version is sharper than mine was.
   `check_delivery.py` not only rejects a `..HEAD` bundle, it prints the exact
   fix — so a session that follows the packet's own instruction to run the check
   before bundling is told how to correct the packet. That is how B14-01 got it
   right, and it is why its bundle carries the named ref.
3. **`results/b13_01_hpad.json` stores μ keys at inconsistent length.**
   Confirmed: ten blocks with 9 parts, five with 8. A literal-key join against a
   9-part enumeration gets 10 hits and 5 silent misses. **One correction: the
   lost five carry `a₃ = 9,9,8,6,5 = 37`, which is 51% of 73, not "a third".**
   The defect is worse than reported.
4. **B13-01 §6 points a successor at an evaluator this route does not need.**
   Accepted as stated; the mixed route on the full `λ'` keeps both tall columns
   at height 9 for all fifteen strips.
5. **The success criterion assumed the span rather than asking for it to be
   measured.** Accepted, and it is a fair criticism of my board text. "A nonzero
   73×73 minor" leaves a session that measures 72 with nowhere to put a real
   result. The board's own report rule says a characterised negative is a
   deliverable; the slot text should have matched it.

Its two self-reported defects (S3 deviating from its own pre-registration, and
the runner not checkpointing) are both reported against itself with the
consequence priced. The S3 deviation is the more interesting: the deviation ran
the *better* search, and the session found this by noticing three searches
plateauing together and then running what it had actually pre-registered.

## Controls

C1/C1d are the ones that matter, and C1d is the one the board asked for: eight
shapes of independently computable dimension 4–10, so it tests mixing between
independent basis directions rather than a single value. Every control was run
with a negative instance and none is reported as passing without it.

The C4 note is worth carrying into `PROVED.md`: dropping `α!` is a **diagonal
rescaling** of the cubic coefficient space, so it commutes with the torus and the
weight check cannot see it. A session testing a wrong normalisation only against
C2 gets a meaningless pass. C3, the raising check, is what rejects it.

The C1b episode — measured 0 against predicted 1, traced to undersampling at a
shape where ~9% of undirected fillings are nonzero — is reported because the
first number existed before the second. That is the right instinct.

## What is worth banking beyond the certificate

- **Mixed evaluation is 6× cheaper than the uniform quartic baseline** (0.029 s
  against 0.174 s), because low valence drops the open-2-column width from 3–4 to
  1–2. The arithmetic was never the cost; the search was.
- **Stratifying on the tall-column overlap `k` is worth ~4× in candidates per
  direction.** Any successor should stratify from the first draw.
- **Unconstrained sampling is a worse search, not a broader one**: 61,873
  unconstrained fillings gave rank 17 against 71 from 4,567 directed ones.
- **`dp_pack` with an arbitrary letter order exhausts a 2.5 GB bound at `h = 9`**,
  and a uniformly random order does the same. A low-width order is required.

## Not claimed, correctly

No `i_red`, no `i ≥ 1`, no `D`. The degree-14 stretch is NOT REACHED and the
report says explicitly that `D = −4` is therefore not reached, as the packet
requires. `dim N₁₃ ∈ {72, 73}` is the honest statement and it is the one made.
