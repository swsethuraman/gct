# B26-02 input bindings

Hash = SHA-256 of `git -C work/batch15_workers/B15-02 show <commit>:<path>` output, i.e. the
committed LF blob. For the three notes, DELIVERY_NOTE.md and MANIFEST.json there are zero CR bytes,
so blob = raw working-copy bytes. Brief prefixes all match.

| commit | path | bytes | sha256 (blob) |
|---|---|---|---|
| 0d6f5a8cc206e8703e3ebd9c0c45acb88adea0eb | results/b26_expander_input/CONSTRUCTION_AND_LIMITATIONS.md | 15629 | 51851ab57a42715647cd8304112957ce0f3e03842a7523d9d63238faf0fdd674 |
| same | results/b26_expander_input/PADDING_SURVIVAL.md | 10578 | e2053e46b92aa6edafbac27d83e53a1f8e97fabca3b49e8eac40ab589e276a2d |
| same | results/b26_expander_input/DETERMINANT_REJECTION.md | 8463 | 6a40317b5e7679997b499d2346790079db336b300e10c42a40e92320145d89f3 |
| same | results/b26_expander_input/DELIVERY_NOTE.md | 2889 | 9f99dfd99f0ae485935eca25c86c506efd584ac7d7d68dc2201921db9b768010 |
| same | results/b26_expander_input/MANIFEST.json | 1004 | 36b482b6993f490cf1edac0f74c43c6b4f602dd1ad01809a327411dfe0443c0a |
| 92a7d054369a20854fd51685ee09ecb756344e8d | docs/b25_04_report.md | 29850 | f6e14afdd7da6b2c7b3df340cce5d3571af864f14240abf82f6331edd6129a47 |
| same | results/b25_04/MANIFEST.json | — | a33ab4dd19d5507e569870971ff1d835813ab2cd5cef96c48afb5de6b473edd9 |
| 9e12d7892734f6ec199da3b947e64f09704959d7 | results/b25_04/SCOPE_ERRATUM_20260922.md | 4202 | 9f59d31ba203457dd6ac2a0ab16ef1af0cc0ee8639d6c088c1b1e9bafd8070ed |
| 7464a2bd02c9740db55d15ac43571cca74acea5f | docs/a26_01_report.md | 8754 | 747934648cdaee66749516b9cc0584ee4a07a8b0a5d1966d4eece4ba82e41635 |
| same | results/a26_01/PROOF.md | 8928 | 479d644595df05fd00750d359aaef8cebc4e62ff8b75bcdb067eba033a4f48ed |
| same | results/a26_01/MANIFEST.json | — | 983328d6464c544244e555d2f939ce6d5101294ef683bb86615515e03dc465f3 |
| ab4f527189bea14b5d146f9dc9d5b445844eaff3 | results/a25_10/NEXT_ACTION.md | 2571 | af774505871c8c58ba83bd7538aec8d019ff93d6ffd14f48bbeb3e3fcda79d69 |

Pre-pointer states: committed PADDING_SURVIVAL.md with lines 6-10 deleted hashes to
6bfebc9b913377664919bde1eaa9f652748745659016b31749b988dff5ec4ca4 (= note 3's citation; reproduced).
Note 1's cited 67d3d1ccfee0c6b1a3e3f1c3f909de2b37f0bdd988e850f506a5d34f5508a1d1 was NOT reproduced by
deleting its pointer paragraphs (variants 7-17, 7-18, 6-17, 13-18, 7-12 tried): UNREAD.

Administrative (uncommitted) raw hashes: B26_COMMON.md a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd;
B26-02.md 1ad6bd6a966c8a419d9cacfed26b1660cb3c3ff4d6d49f7c9f304733ec2d1fbe;
BATCH26_LIVE_LEDGER.md 9d24c37c5953c66583f199af3e8fc226e4feb9f7c70d412f2d4424594b47d2c8.
