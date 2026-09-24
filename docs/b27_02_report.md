# B27-02: mixed signs escape the two squares, but not the determinant variety

**HAND — registered outcome 3: exact rejection of the one candidate.** The
candidate passes both prescribed determinant evaluations and is nonzero at
actual padding. Its universal determinant identity is nevertheless false at
an explicit third pencil. The packet includes that counterexample, rather
than leaving the determinant-side question open under outcome 1. It is not
a separator.

## Preflight and scope

**READ (administrative).** Fresh Astra task, no B27-01 work, no subagents or
messages to other tasks. Worktree `work/batch27/b27-02`, branch `b27-02`, initial
HEAD `6dea55ec926c1618cc60ad71209795528705bf61`, exactly the PART 25 setup
commit. Initial status was clean, with no untracked entries. All three output
patterns were absent. No applicable AGENTS.md was found. The brief and common
hashes match the board; no preflight mismatch occurred. A command-local Git
safe.directory setting was necessary for the sandbox account; no configuration
file was changed. The unreadable global ignore file produced a warning only.

**READ (raw administrative byte bindings).**

| file | SHA-256 |
|---|---|
| B27_COMMON.md | 891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee |
| B27-02.md | 8dbb0a0d1bd56fd5a1c5995254cf6c200b3f45698635f3f3daf6cbd42635d5 |
| BATCH27_BOARD.md | b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec |

**READ.** Mathematical premises were read from committed blobs: A26-03's
normalization and Q^2 pencil; B26-02's D4 and actual p4 substitution; B26-10C's
corrected reopening rule. Full commits, Git blob IDs, raw SHA-256 hashes, byte
counts and read scopes are in `results/b27_02/INPUT_BINDINGS.json`. Mathematical
hashes name exact committed blob payloads, excluding the Git object header,
with no line-ending transformation. **UNREAD:** external literature and any
uncommitted work by other slots; none is a premise.

## Ladder results

**HAND — 2a, pass (early checkpoint).** Both tableaux have content 10 x 4 and
shape (24,4,4,4,4). T1 consists of four columns (1,2,3,4,5), plus four singleton
columns for each label 6,...,10. T2 consists of two columns (1,2,3,4,5), two
columns (6,7,8,9,10), and two singleton columns for each label 1,...,10. Use
top-coordinate alternating tensors, the displayed orders and the symmetric
quartic convention q=sum q_ijkl*x_i*x_j*x_k*x_l, without extra factorials.
The exact candidate is f=f_T1-567 f_T2. Its signs are mixed. CHECKPOINT.md was
written before the 45-minute deadline; no feasibility stop was needed.

**HAND — evaluation notation.** Let a=q_1111, C_ij=q_11ij, H=120 det C, and F
be the contraction of five labels with four full height-five columns. Then
f=a^5 F-567 H^2. The hand proof in `results/b27_02/PROOF.md` derives
F(Q^2)=11200/9 by a seven-row cycle-type calculation, fixing the coefficient
567 without fitting sampled values.

**HAND, replayed COMPUTED — 2b, pass.** Put A=x1^2+x2^2,
B=x3^2+x4^2+x5^2, Q=A+B and q=p4=A(A+B). The exact endpoint values
f(q)=-175/9 and f(q+B^2/4)=0 prove that t -> f(q+t B^2) is nonconstant.
This establishes visibility of Sym^4(span(x3,x4,x5)) in the required sense.

**HAND, replayed COMPUTED — 2c, pass.** f(Q^2)=0 and f(D4)=0 for
D4=(A+B/2)^2. Both are literal normalized determinant points, with explicit
skew pencils in the proof. Because they differ by a diagonal change of
variables, they impose only one vanishing constraint on any fixed-weight
candidate. Passing these tests gives no universal ideal-membership conclusion.

**HAND, replayed COMPUTED — 2d, actual-padding nonvanishing; universal identity
rejected.** On entering 2d, b27-01 was still at its setup commit and had no
committed b27_01 outputs. The permitted fallback p4 is used. The proof replays
the ten linear substitutions exhibiting p4=z*per_3(Y), with Y nonsymmetric,
and gives f(p4)=-175/9. A universal identity would require f(det(sum x_i M_i))
to vanish identically in the 80 pencil parameters. It does not: the pencil

    [ x1   0    0     x3   ]
    [  0  x1    0     x4   ]
    [  0   0   x1     x5   ]
    [ x3  x4   x5   x1+x2  ]

has determinant E=x1^2(x1^2+x1*x2-B), x1 coefficient I4, and
f(E)=-175/256. This answers the precise determinant-side question negatively.
Since 2c passed, its replacement-candidate instruction was not triggered;
the terminal rung is complete and no second candidate was attempted.

**HAND — strengthened scoped obstruction.** The evaluations at Q^2 and E of
the two functions a^5F and H^2 form a matrix of determinant 4375/2916. Therefore
their entire two-dimensional span contains no nonzero determinant equation.
This says nothing about other mixed-sign combinations or other tableaux of
the same weight.

## Achievement level, verification and delivery

**HAND.** Achieved: a nonzero highest-weight coefficient function, mixed-sign
escape, exact visibility, and actual-padding nonvanishing, followed by exact
determinant rejection. No new source condition is asserted. No determinant
coefficient equation, separation on padding, positive multiplicity gap,
geometric noncontainment, or asymptotic lower bound is obtained. Nonvanishing
on padding alone does not establish any of those stronger achievements.

**COMPUTED.** Two exact sequential verification runs, followed by no search or
further mathematical runs. Run 2 replays the epsilon sum without run 1's
first-column symmetry reduction. Both match all claimed values. Resource
receipts bind commands, inputs, outputs, wall times and enforced Job Object
memory caps. Each used less than one second of mathematical wall time and
12 MiB of peak Job Object memory. Installed Python standard-library integers
and Fraction sufficed; SymPy was unavailable and nothing was installed.

**READ (administrative).** Only this slot's explicit output paths are delivered.
The manifest binds every payload's raw bytes and excludes itself. One commit
and a push to b27-02 are required, followed by ls-remote confirmation. The
final response supplies the resulting commit and manifest hash; no receipt
inside the commit claims knowledge of its own future commit SHA.

**READ — standing constraint:** No five-row determinant equation is known to be
nonzero on padding. A25-10's decision remains "no construction ready."
