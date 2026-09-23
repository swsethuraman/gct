# B26-10C input bindings

Each SHA-256 is of `git show <commit>:<path>` output from `work/batch15_workers/B15-10`, i.e. the
committed blob. CR counts are given; a file with CR=0 has blob = raw working copy. The two
manifests with CRs are committed `-text`, so their blob equals the producer's raw bytes.

| commit | path | bytes | CR | sha256 |
|---|---|---:|---:|---|
| 7464a2bd02c9740db55d15ac43571cca74acea5f | docs/a26_01_report.md | 8754 | 0 | 747934648cdaee66749516b9cc0584ee4a07a8b0a5d1966d4eece4ba82e41635 |
| 7464a2bd02c9740db55d15ac43571cca74acea5f | results/a26_01/PROOF.md | 8928 | 0 | 479d644595df05fd00750d359aaef8cebc4e62ff8b75bcdb067eba033a4f48ed |
| 7464a2bd02c9740db55d15ac43571cca74acea5f | results/a26_01/EXCLUSIONS.md | 6370 | 0 | 834c058a245be1e022ea852753572bc26e2c8bbcb261330de854bf2e1de0da28 |
| 7464a2bd02c9740db55d15ac43571cca74acea5f | results/a26_01/VERIFICATION_COST.md | 5321 | 0 | 9d84ef794e3dc77c310d1f2a1c1e432155ebb19020e29f70eaddee63fbad9c23 |
| 7464a2bd02c9740db55d15ac43571cca74acea5f | results/a26_01/MANIFEST.json | 4590 | 119 | 983328d6464c544244e555d2f939ce6d5101294ef683bb86615515e03dc465f3 |
| f7967d17935d6256e7744f6457b45a3787b6940f | docs/a26_03_report.md | 7105 | 0 | 7ff59fe60b5ef3e246971a3b1d4b9f8319d191a4623e914b372a99677581b0e7 |
| f7967d17935d6256e7744f6457b45a3787b6940f | results/a26_03/PROOF.md | 9904 | 0 | ff9507bb97c1d6917aef652622b2669b1ecd0ac03e95950d224d302e60f121e3 |
| f7967d17935d6256e7744f6457b45a3787b6940f | results/a26_03/CHECKPOINT.md | 8890 | 0 | 29e0530692d87b7c5b951e23fcb7999db1394f32a28cfc9385cdfa16afcf3233 |
| f7967d17935d6256e7744f6457b45a3787b6940f | results/a26_03/MANIFEST.json | 1571 | 47 | 236987891ba16169b16148108df405f2a367cb707530455fc89fea3ad3470a46 |
| eb53b97cf0904e2d54fdb7d101d83b024822811b | results/a25_05/FIVE_CENTER_REDUCTION.md | 10415 | 0 | 02b3e7ab24c099a92c3ce08929f35fc201d120d5247dad2554f7c8305fc52542 |
| eb53b97cf0904e2d54fdb7d101d83b024822811b | results/a25_05/STRUCTURAL_MAP.md | 6739 | 0 | eb810d497c9798ab388fffa698d9ce56bc304a2cbed6bc31397d1fd55ebc8124 |
| eb53b97cf0904e2d54fdb7d101d83b024822811b | results/a25_05/PADDING_FIBERS.md | 7025 | 0 | 4705c54233427fa0a16984d0c25754221e854d7c52f8a07f0d192c0c10d11a80 |
| eb53b97cf0904e2d54fdb7d101d83b024822811b | docs/a25_05_report.md | 13118 | 0 | c254bbf71e6f255558edc400a55b5973077f95b8172a66fd848952cfb3458671 |
| 5007de860ba195100adc4f5a6cdebd3d344cadaa | docs/a25_02_report.md | 10077 | 1 | fc291cb906bd5dc3fbdc41344d4586239b18cc388833858739f800321cbaeb53 |
| 5007de860ba195100adc4f5a6cdebd3d344cadaa | results/a25_02/APPLICATIONS.md | 7170 | 0 | 945cad8f537f475e93b898c3c2f5ba4e956005f2578ac76f8bed3e6c75b06c1b |
| cdf6839cd81031d42e43dc640b08e2746a7ef22c | docs/b26_02_review.md | 17495 | 0 | 14de8f0f03f45b97ce7a82ca47801ae7d22e6a65d8c09fd1e68f847b36ec8bd0 |
| 92a7d054369a20854fd51685ee09ecb756344e8d | docs/b25_04_report.md | 29850 | 0 | f6e14afdd7da6b2c7b3df340cce5d3571af864f14240abf82f6331edd6129a47 |
| 9e12d7892734f6ec199da3b947e64f09704959d7 | results/b25_04/SCOPE_ERRATUM_20260922.md | 4202 | 0 | 9f59d31ba203457dd6ac2a0ab16ef1af0cc0ee8639d6c088c1b1e9bafd8070ed |
| e22a41b1787ff5e8a284433d5d7e0d2a6a2d35b8 | docs/b22_02_report.md | 26231 | 0 | b41e4265809a018750286d6eda416d62c4f4044b3fdb7cbac2cc51caf50593e4 |
| 82633a60893236fab4fbc317df416e1b8a349005 | docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/REVISED_VERDICT.md | 6857 | 0 | dfce2ec26c437335089509eda3bfce2c3595e2012f66f6186a4e6b81ae9710a4 |
| 81967ddeb68340f31762bc41d424379cdd57527c | docs/a25_04_report.md | 7716 | 0 | f2444c33f3d11295a2e53abed279c82e7891b42fc9f4a9be41f2a7d2cb905651 |
| 81967ddeb68340f31762bc41d424379cdd57527c | results/a25_04/CONSTRUCTION_AND_PROOF.md | 11621 | 0 | a49f3ad79a86107cd4b28fd667581368f3500a2101f545649cf769f5ade6acfa |

`docs/a25_02_report.md` contains one CR byte in its committed blob; only a READ of Application 3's
status line was taken from it.

Administrative (uncommitted, raw working-copy bytes, handover folder):

| file | sha256 |
|---|---|
| batch26_launch/B26_COMMON.md | a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd |
| batch26_launch/B26-10C.md | 0d5d4fcd85bb47180393ac2b5bedff547d394fbc1c6f604bb6e06353f756cc4b |
| BATCH26_LIVE_LEDGER.md | 8260cd3772c5208960b941d6243962e0e42012317f173dc48c68f28ac231de14 |
