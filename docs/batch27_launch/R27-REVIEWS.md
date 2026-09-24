# R27-01, R27-02, R27-03 — cross-lineage reviews, run as each producer lands

Read `B27_COMMON.md` first. Launch a review as soon as its producer has **pushed**. A review
reads the producer's committed tip, `git show <tip>:<path>`, and never the working copy.

**Setup:** each reviewer launches with the same one-line prompt, using `R27-REVIEWS.md` as the
brief, and adds one extra line: "Your slot is R27-0N."

| review | reviews | reviewer lineage | branch / worktree | ceiling |
|---|---|---|---|---|
| R27-01 | B27-01 (Astra) at the tip of `b27-01` | **Claude** | `b27-01r` / `work/batch27/b27-01r` | 60 min |
| R27-02 | B27-02 (Astra) at the tip of `b27-02` | **Claude** | `b27-02r` / `work/batch27/b27-02r` | 60 min |
| R27-03 | B27-03 (Claude) at the tip of `b27-03` | **Astra**, fresh session | `b27-03r` / `work/batch27/b27-03r` | 60 min |

Output paths are `docs/b27_0Nr_review.md` and `results/b27_0Nr/`.

## Method

1. **Bindings.** Record the producer tip SHA and its `MANIFEST.json` hash, and confirm that every
   payload matches.
2. **Claim check.** Take every rung's claim at the level the producer assigned it. Check each one
   by hand derivation, and **re-run every COMPUTED script** within your own allowance, recording
   whether each output hash matches.
3. **Scrutiny.**
   - Any claim of a coefficient equation that is nonzero on padding (B27-03 outcome 1, or B27-02
     outcomes 1–2) gets the heaviest scrutiny. That means exact kernel membership, the literal
     actual-padding point, and the evaluation re-derived by you.
   - Any geometric noncontainment claim (B27-01 1b) gets a smoothness certificate that you
     re-derive yourself.
4. **Verdicts.** For each claim: ACCEPT, REPAIR (with the smallest true statement), DEFER or
   REJECT.

**Prior exposure.** If you produced, or saw during production, the packet you are reviewing,
stop and report it.

Keep the achievement levels distinct. The binding constraint changes only through an accepted
coefficient equation, and even then only by the user's ruling.
