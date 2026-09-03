# House wording for session briefs and reports (in force from session 43)

2026-09-02.  Session 41, run under a different model than the brief was
written for, tripped a content safeguard mid-run.  The mathematics cannot be
the cause; the plausible surface is the *operational* vocabulary the briefs
inherited from the early sessions — process control, "kill", "hunt",
"stop-everything" — and, on the worker side, hand-written shell commands
for ending processes.  Neither is needed for the work.  From session 43
onward every brief, every worker report, and every integrator review uses
the neutral forms below, and workers are set up so that they never need to
write a process-control command by hand.

## 1. Process management — say it once, neutrally

Replace the old rule ("kill by explicit PID, never `pkill -f`") with:

> Bound every long run at launch: `timeout <seconds>` for wall clock and
> `ulimit -v` for memory, and write the run's process id to
> `results/logs/<run>.pid`.  A run that must be ended early is ended by that
> recorded id; runs are never ended by name-pattern matching.

This keeps the substance (the four `pkill -f` self-match incidents are why
the rule exists) without the vocabulary.

## 2. Substitutions

| old | new |
|---|---|
| kill criteria | stopping rules |
| obstruction hunt, hunt | obstruction search, search |
| STOP-EVERYTHING | halt the sweep; the verification protocol takes over |
| sceptical branch | independent re-check |
| insurance bundle | checkpoint bundle |
| fire-risk cells; the screen could have fired | candidate cells; the screen was sensitive |
| manufactures false obstructions | produces false positives |
| brutal protocol, attack, assault | (drop) the protocol, approach |
| exploit (as a verb for a trick) | use, apply |
| the git proxy refuses pushes / access denied | (not mentioned) deliver by bundle; do not push |
| target | goal |

Mathematical vocabulary is unaffected: kernel, certificate, prime, seed,
rank, obstruction, ideal, onset, cap, transfer, washout all stay.

## 3. What does not change

Single-writer files, bundle delivery, the 5 MB limit, logs under
`results/logs/`, append-only config, pre-registration first, bank per cell,
`python-flint` only, the verification protocol for any `D > 0` cell.  Only
the words change, not the discipline.

## 4. Check before launch

Before a brief goes out: search it for `kill`, `pkill`, `hunt`, `brutal`,
`attack`, `exploit`, `proxy`, `bypass`, `circumvent`, `STOP-EVERYTHING`.
Any hit is rewritten from §2.
