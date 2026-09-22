# Batch 25 exact-path delivery proposal — 2026-09-22

PROPOSAL ONLY — UNCOMMITTED / NOT RELEASED. No staging, commits, pushes, session launches, experiments, compiler runs, producer edits, or Git configuration changes were performed. This proposal updates the existing B25-12 live ledger under the userʼs direct coordinator instruction.

## Verified inventory

Eleven completed packets: 135 inventoried paths, of which 133 are proposed producer delivery paths and two are unchanged B25-03 bindings. All supplied payload hash/size checks pass. The JSON inventory binds raw SHA256, bytes, current filtered/raw Git object IDs, baseline content, ignore results, branch and HEAD. Full repository status snapshots also contain unrelated files; those are excluded from delivery.

Each path below is relative to the explicitly stated absolute worktree. This is an exact list, not a directory glob. ADD_EXACT_PATH includes both new files and tracked after-states. Configuration changes described later are additional proposed paths.

## A25_01

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15`
Branch: `batch15-launch`; baseline/current HEAD: `82633a60893236fab4fbc317df416e1b8a349005`.

Scoped one-frame no-go; producer-only.

Manifest: `results/a25_01/MANIFEST.json`; raw SHA256 `ceeaac27392742b3a79a44ec1d136dbdf6b9a6058e292f51bc0d052e7165e2ee`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `docs/a25_01_report.md` | 8176 | `76a231daea64473e39fd44acf8751e8dde4a3cf9ebc99958d4df96de42c05b10` | ADD_EXACT_PATH |
| `results/a25_01/audit_sources.ps1` | 2769 | `74bf6e518438623ea666bef23ec624e52aba3f80232d65c3e3c795bd41d1e6c3` | ADD_EXACT_PATH |
| `results/a25_01/CONSTRUCTION.md` | 2321 | `9909e2872dda0afd33ac90fea697c8c29afbceab1f91cf5dd1597f7e2c887d33` | ADD_EXACT_PATH |
| `results/a25_01/DELIVERY_NOTE.md` | 2318 | `875bfe4d71614d46675f555efee80e46caa6131a2efd0a9f636442a4b59d2fca` | ADD_EXACT_PATH |
| `results/a25_01/EXCLUSION_CHECK.md` | 2954 | `04a2350db3d34ca97e2366e0f8bf9ba2d8dd3cedce9d9db99b01e95b0ff8915a` | ADD_EXACT_PATH |
| `results/a25_01/INTAKE.md` | 2127 | `5da2acaa4a780d6ec94e5f88ca972f3690f306ca21fc9ca5c751b9fbeb73e98e` | ADD_EXACT_PATH |
| `results/a25_01/LIMITATIONS.md` | 2385 | `24c3b00095786182a2e910cab1c288ca5d6062c79fe423aa5d0814cd0ef1bb72` | ADD_EXACT_PATH |
| `results/a25_01/MANIFEST.json` | 19410 | `ceeaac27392742b3a79a44ec1d136dbdf6b9a6058e292f51bc0d052e7165e2ee` | ADD_EXACT_PATH |
| `results/a25_01/NEXT_CERTIFICATE.md` | 3694 | `dd85237ec37e9beeeb25faa5fd1d03279b7ed2548bf6d08255b5568031070686` | ADD_EXACT_PATH |
| `results/a25_01/PADDING_STATUS.md` | 1073 | `c763c088f57f897b7dbcdc4df63430093f51648cc2d3625b1411456f8a78118f` | ADD_EXACT_PATH |
| `results/a25_01/PROOFS.md` | 4931 | `1cda31dfd9cc9c5763547e053d803e4de10171eea2c5cdbba9c690243ac5d8d2` | ADD_EXACT_PATH |
| `results/a25_01/PROPOSED_ADD_LIST.txt` | 494 | `39d9be6cb78320feea4d2482afb04d8194b6bcf1ab8b6bd7899d36fc81209bb6` | ADD_EXACT_PATH |
| `results/a25_01/RESOURCE_RECEIPTS.md` | 1171 | `9e8ab56cff9969533bca02c2b0c5d5e05dd4e2435161ba3169bcc71adcc7c961` | ADD_EXACT_PATH |
| `results/a25_01/seal_packet.ps1` | 2508 | `4d49db33ca054e2107b1e82cce7ac43b68ff32b5c6201a1ce0afbf2e38d742da` | ADD_EXACT_PATH |
| `results/a25_01/SOURCE_BINDINGS.json` | 15649 | `344f7344ffde108804bc683b63c82d9255b1e9c1a012c0e5da0bbeb38c74b3a2` | ADD_EXACT_PATH |
| `results/a25_01/STATUS.md` | 1029 | `803d16eb681f46f6fde74b25e666ca8879fc30b813a965c18dddf1d077e61b3f` | ADD_EXACT_PATH |

## A25_02

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15`
Branch: `batch15-launch`; baseline/current HEAD: `82633a60893236fab4fbc317df416e1b8a349005`.

Typed criterion and scope analysis; producer-only.

Manifest: `results/a25_02/MANIFEST.json`; raw SHA256 `4c6d5fdc11ca4d30221d5d454cc29daf0af2de0db1bbafb3b14f4333cebbeedd`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `analysis/a25_02_admin.ps1` | 2203 | `45ab64a437035eb535b841b9acb111c7a11352c42030f05ab345d97f5ca9cc48` | ADD_EXACT_PATH |
| `analysis/a25_02_seal.ps1` | 5395 | `055d80f8f78b5d1e2b02ba1f640d5a967b487f4c1616c70d2099aa0783674865` | ADD_EXACT_PATH |
| `docs/a25_02_report.md` | 10077 | `fc291cb906bd5dc3fbdc41344d4586239b18cc388833858739f800321cbaeb53` | ADD_EXACT_PATH |
| `results/a25_02/ADD_LIST.txt` | 453 | `81436ee68d5c07025526dbecac0f8958910b76da3c937a1c47ad3235ff2c65d9` | ADD_EXACT_PATH |
| `results/a25_02/ADMIN_VERIFICATION.json` | 9093 | `660cebbd19092f4754ef6cee5e8aa5101e64dcef4f6e6c9d248adb9921fc291b` | ADD_EXACT_PATH |
| `results/a25_02/APPLICATIONS.md` | 7170 | `945cad8f537f475e93b898c3c2f5ba4e956005f2578ac76f8bed3e6c75b06c1b` | ADD_EXACT_PATH |
| `results/a25_02/DELIVERY_NOTE.md` | 2936 | `4d36167d5af80c27e0f818778f7e578737455728a28b15bfbc7ad8bf41d525d6` | ADD_EXACT_PATH |
| `results/a25_02/IMPLICATIONS.md` | 10420 | `0c20299840911459b86b2c22da584c020b27444c44c1eb44b418b3a9e0c8c137` | ADD_EXACT_PATH |
| `results/a25_02/INTAKE.md` | 3182 | `0362d78bef040f9ec95510841d73a9a82309e1e3b01bf1edc2390dec40c90872` | ADD_EXACT_PATH |
| `results/a25_02/LIMITATIONS.md` | 3247 | `195df737437d9ddded61d7e66ceaae4e1d4526e5a318484da18d45852e2ea583` | ADD_EXACT_PATH |
| `results/a25_02/MANIFEST.json` | 25631 | `4c6d5fdc11ca4d30221d5d454cc29daf0af2de0db1bbafb3b14f4333cebbeedd` | ADD_EXACT_PATH |
| `results/a25_02/RESOURCE_RECEIPTS.md` | 3049 | `200de91e3294bead2c4caa233576da8b48b914e4d566dbe1a84df9f8b36c3590` | ADD_EXACT_PATH |
| `results/a25_02/SCOPE_MATRIX.md` | 15437 | `bc07c5d1317796be3b84e357a6c4af1580a0c07a90fa8bbfb34fa5ec96f5e15d` | ADD_EXACT_PATH |
| `results/a25_02/SOURCE_BINDINGS.json` | 21368 | `ba5a1d006b149ad19be160ce7cf331aaaa4e112b692bf99d0f53b9bae0f9a2a5` | ADD_EXACT_PATH |
| `results/a25_02/SURVIVOR_SPEC.md` | 8764 | `c314e742cbb139cecfa16d5cdd0c8b6b05fa7f458dbc50ff8a888a4ac210d97e` | ADD_EXACT_PATH |

## A25_03

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15`
Branch: `batch15-launch`; baseline/current HEAD: `82633a60893236fab4fbc317df416e1b8a349005`.

COMPLETE per final STATUS/manifest: outcome (3), joint rank-29 projection no-go; independent review pending.

Manifest: `results/a25_03/MANIFEST.json`; raw SHA256 `52e23aeb5eeb78afb889d1986706b05209f945d4de53f3033a4a3c2996d79216`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `analysis/a25_03_admin.ps1` | 4184 | `31a61870bb859f1be0d55da58d1775bab23ecf94bbbf7dbf291b5d9694c5a2fe` | ADD_EXACT_PATH |
| `analysis/a25_03_seal.ps1` | 8592 | `7d74a1e884044eb1d973aa79a0da3dc421bdff1c1b19dcb5b87f34eb1d4a37ba` | ADD_EXACT_PATH |
| `docs/a25_03_report.md` | 8237 | `9d1e199aad51bc7c2f75fc5253db81cfd0fbbceb773c9b19d119c8ceaa68403d` | ADD_EXACT_PATH |
| `results/a25_03/ADD_LIST.txt` | 489 | `3cca7347f19382ad1d75ea756789079f0f03ef05dd56ed27bea3e2ff12f0860b` | ADD_EXACT_PATH |
| `results/a25_03/ADMIN_VERIFICATION.json` | 11857 | `9b8b59020f6eba24cc7507b2d5f3d0d1b763e20633953afb8fbedf1868fc2680` | ADD_EXACT_PATH |
| `results/a25_03/DELIVERY_NOTE.md` | 2031 | `08f7c18f0e58c90a18ca7dd50b36f94cde28a5b01e422ec71a6fb757c7ef9931` | ADD_EXACT_PATH |
| `results/a25_03/EXCLUSION_PADDING.md` | 6437 | `bc5839332617709b03f97cd0ac1049919d33750fa22032e317ebfe1cfb7de059` | ADD_EXACT_PATH |
| `results/a25_03/FRAMES.md` | 4965 | `6337f4b1a04c2dda6af9f5ed40cfd2d252d9e83ffc5cbb4a72ddaa16f02bb46e` | ADD_EXACT_PATH |
| `results/a25_03/INDEPENDENT_LEMMAS.md` | 3148 | `f61e47d597f324f772d1fe9ca3d0d4747f82af0fec07aabda2ac908c69202243` | ADD_EXACT_PATH |
| `results/a25_03/JACOBIAN_CERTIFICATE.json` | 1692 | `96a01c935ec302ef1bc628fa0b7c2202d89209ac42f02dfa6775ad7a792b0553` | ADD_EXACT_PATH |
| `results/a25_03/MANIFEST.json` | 5633 | `52e23aeb5eeb78afb889d1986706b05209f945d4de53f3033a4a3c2996d79216` | ADD_EXACT_PATH |
| `results/a25_03/PROOF.md` | 7616 | `71c1072976d89b4d29551e2c35b8473012639078b9fa1667d7b076387ae457c3` | ADD_EXACT_PATH |
| `results/a25_03/RESOURCES_NEXT.md` | 5649 | `b9bf1e718c7b6415050dc9df3734e723faee524ea5fc7c0f3cb842d5c9d91bd2` | ADD_EXACT_PATH |
| `results/a25_03/SOURCE_BINDINGS.json` | 21537 | `c67d06be1e3d2aef14b7cb03b5b7e55e80f6854acacad4ea7362691408697977` | ADD_EXACT_PATH |
| `results/a25_03/SOURCE_READS.md` | 5837 | `c979329f730d7c9a97f1c343bc44b61c582f92b7f4a9a63d211c387bbd99b73a` | ADD_EXACT_PATH |
| `results/a25_03/STATUS.md` | 2172 | `ee7649dc4108f7f4aafb2918b8ac40358ba4918f0a9f5b6a7578736023c1bed9` | ADD_EXACT_PATH |

## A25_04

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15`
Branch: `batch15-launch`; baseline/current HEAD: `82633a60893236fab4fbc317df416e1b8a349005`.

COMPLETE per STATUS: outcome (3), ten selected minors no-go; independent review pending.

Manifest: `results/a25_04/MANIFEST.json`; raw SHA256 `01e98e1dab11139c403cad6b3993c94bf54c0ddcb8072cfb6a81b37e5a58775f`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `analysis/a25_04_admin.ps1` | 4461 | `d84443e9300f2dbcb0600a08d3484ebae1b5150affbf49346d6c63043f9e4211` | ADD_EXACT_PATH |
| `analysis/a25_04_seal.ps1` | 6646 | `a3c24aa8cdbcd1612802f0f4aa3070eeb3122f94f6793f2b23010c5777ce9c83` | ADD_EXACT_PATH |
| `docs/a25_04_report.md` | 7716 | `f2444c33f3d11295a2e53abed279c82e7891b42fc9f4a9be41f2a7d2cb905651` | ADD_EXACT_PATH |
| `results/a25_04/ADD_LIST.txt` | 429 | `2543f220d8893d49ae614cb2f56e8218974ed79f813b15d24dc10b6b682d90a3` | ADD_EXACT_PATH |
| `results/a25_04/ADMIN_VERIFICATION.json` | 8885 | `05a746f2ecfc475b880913b8a37bd1f2dfe242866f1e58e90859a3335e8d6d0d` | ADD_EXACT_PATH |
| `results/a25_04/CONSTRUCTION_AND_PROOF.md` | 11621 | `a49f3ad79a86107cd4b28fd667581368f3500a2101f545649cf769f5ade6acfa` | ADD_EXACT_PATH |
| `results/a25_04/DELIVERY_NOTE.md` | 2215 | `5abfa282bb4dbd2a6be28b30d63357724d2cc7988cd1ac868100477c5618e524` | ADD_EXACT_PATH |
| `results/a25_04/EXCLUSION_AUDIT.md` | 5090 | `20dfdb1ea7924866cea7a9da003f37cb6cebe3b409bf9d77374f24eb0e0013f7` | ADD_EXACT_PATH |
| `results/a25_04/INTAKE.md` | 2282 | `2f42e159de42d5881dca7894d1fb96df1cccd4d2547f9675580821a0dc21de04` | ADD_EXACT_PATH |
| `results/a25_04/MANIFEST.json` | 4570 | `01e98e1dab11139c403cad6b3993c94bf54c0ddcb8072cfb6a81b37e5a58775f` | ADD_EXACT_PATH |
| `results/a25_04/RESOURCE_RECEIPTS.md` | 4206 | `36331e431db669de62b946aa18fa7d08730bb49ebfa4435623a3e52e713e2845` | ADD_EXACT_PATH |
| `results/a25_04/SOURCE_BINDINGS.json` | 23248 | `1e6a172803f06681c1b9095ced1e9726f791e800b16f30ce18f318c30585fbc8` | ADD_EXACT_PATH |
| `results/a25_04/SOURCE_READS.md` | 6274 | `cf0137301ec5d29ba90c553ea198e11efc01a950d57aa5a3628fca559be405f7` | ADD_EXACT_PATH |
| `results/a25_04/STATUS.md` | 2247 | `b678ebc58e41a1caadc2eb5bc51dde7aacb62a6781be742c1971232e51d81053` | ADD_EXACT_PATH |

## A25_05

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15`
Branch: `batch15-launch`; baseline/current HEAD: `82633a60893236fab4fbc317df416e1b8a349005`.

Outcome (3), structural reduction; containment/separation open. Overnight connectivity interruption attested by user; retain disclosure, no new timing gate.

Manifest: `results/a25_05/MANIFEST.json`; raw SHA256 `25989d1da8cd702737aa3a1e0442a318dd98ffe8b68dc63fa526c671269b198f`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `analysis/a25_05_admin.ps1` | 4462 | `da81d0494d2976ea607d6f01b65708ae0a298db3e2aff4d713f874d0b13c686a` | ADD_EXACT_PATH |
| `analysis/a25_05_seal.ps1` | 5270 | `267d1dba262ae30c863f3a0ab5b2b0c4ab5e68a278a13fdbc1e732f6a8f8fd60` | ADD_EXACT_PATH |
| `docs/a25_05_report.md` | 13118 | `c254bbf71e6f255558edc400a55b5973077f95b8172a66fd848952cfb3458671` | ADD_EXACT_PATH |
| `results/a25_05/ADD_LIST.txt` | 538 | `12308f9f5bb88242f6b46936148fddab2b0ee45cd2ea54d4c5e45cf1c871bf6c` | ADD_EXACT_PATH |
| `results/a25_05/ADMIN_VERIFICATION.json` | 4454 | `94ce066272ae825feeebaae4de3df41301bab2f585330aa84d2b9ef231cef651` | ADD_EXACT_PATH |
| `results/a25_05/DELIVERY_NOTE.md` | 2041 | `5868c38adbf19533422d6db4a99ea8fbd857c259090fd58aa4e40520a97b540c` | ADD_EXACT_PATH |
| `results/a25_05/FIVE_CENTER_REDUCTION.md` | 10415 | `02b3e7ab24c099a92c3ce08929f35fc201d120d5247dad2554f7c8305fc52542` | ADD_EXACT_PATH |
| `results/a25_05/MANIFEST_RECEIPT.json` | 388 | `594b27193bcf011dfde750129593d0557ec1fb75a7e7a14fca1c1429be522f98` | ADD_EXACT_PATH |
| `results/a25_05/MANIFEST.json` | 5697 | `25989d1da8cd702737aa3a1e0442a318dd98ffe8b68dc63fa526c671269b198f` | ADD_EXACT_PATH |
| `results/a25_05/NEXT_CERTIFICATE.md` | 7010 | `c81b303da3b064aef00c6d613a6da472d538f4581059568f63f8211664c6d0db` | ADD_EXACT_PATH |
| `results/a25_05/PADDING_FIBERS.md` | 7025 | `4705c54233427fa0a16984d0c25754221e854d7c52f8a07f0d192c0c10d11a80` | ADD_EXACT_PATH |
| `results/a25_05/PRIOR_CHECKS.md` | 4605 | `6e1c6f4de216fb8925721256cd692c0704058b2bed5b7afe5c900560973b9bb4` | ADD_EXACT_PATH |
| `results/a25_05/RESOURCE_RECEIPTS.md` | 3027 | `e8231a636ed0841e76c5bfd246cb75113f1b9c781f48e1923cafb0505c838139` | ADD_EXACT_PATH |
| `results/a25_05/SOURCE_BINDINGS.json` | 31965 | `3478807b50bad25f89948081726c71ea9b9f56122c750cbc286186f5b850a8fa` | ADD_EXACT_PATH |
| `results/a25_05/SOURCE_READS.md` | 6449 | `b835826d440d25cdc1e885e4d721040d3732d60b52cfb998f8c563ec3d2e4bc6` | ADD_EXACT_PATH |
| `results/a25_05/STATUS.md` | 3154 | `03e9039b8bcd4a4c74901f3020679be85637cb2fefd8da98634b9f62650336ab` | ADD_EXACT_PATH |
| `results/a25_05/STRUCTURAL_MAP.md` | 6739 | `eb810d497c9798ab388fffa698d9ce56bc304a2cbed6bc31397d1fd55ebc8124` | ADD_EXACT_PATH |

## B25_01

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B23-04`
Branch: `b23-04-paper3`; baseline/current HEAD: `f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c`.

Paper 3 five-edit after-state; clean compile reported on matching source; review pending.

Manifest: `results/b25_01/FILES.sha256`; raw SHA256 `9bfa9d00db597ebe9831e6c36009d34f46542a92ab0ec9b8f4f285fd8c34330d`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `docs/b25_01_report.md` | 11605 | `b791ceb32707cc91abd29111281ee2f9b08b216ce844fd3359c030d944b16483` | ADD_EXACT_PATH |
| `papers/det4-blindness/BIB.md` | 14356 | `55e3b24d10221957257fa68c451969b4a931cc64c5f5a970698c0d63b98f75ed` | ADD_EXACT_PATH |
| `papers/det4-blindness/CLAIMS.md` | 46003 | `ac1736518ec3cfa47194ac04164b1277ecfac31a0f3a30f773b6a2425fda89a9` | ADD_EXACT_PATH |
| `papers/det4-blindness/det4-blindness.tex` | 108327 | `19e616cfb445ec36d16b7526a0972b8f4be52c05a1cb10df8d33da653082ff49` | ADD_EXACT_PATH |
| `papers/det4-blindness/DIFF_NOTES.md` | 30641 | `a35b79c47ee4bd5909dabcc6fdeccbccd03bca589256580120527452387adc60` | ADD_EXACT_PATH |
| `papers/det4-blindness/GAPS.md` | 44076 | `a85518f23c87df80240bca3703357b49eb697fc4699b6b3d079360a6652f9a27` | ADD_EXACT_PATH |
| `results/b25_01/bindings.md` | 4342 | `0c261be86ef12b2eafc8391bf0a037fd53a553f4bc6eb47110defaf51ae78e80` | ADD_EXACT_PATH |
| `results/b25_01/FILES.sha256` | 644 | `9bfa9d00db597ebe9831e6c36009d34f46542a92ab0ec9b8f4f285fd8c34330d` | ADD_EXACT_PATH |
| `results/b25_01/num.py` | 538 | `523ceeab8f529221d00005ad853d02a6cc11719f01aa80101805501026cd006c` | ADD_EXACT_PATH |
| `results/b25_01/static_check.py` | 2247 | `4d5874b296193c4b4521d476994a0d2eef5ecd25c9020ef4c415fcac1162e48b` | ADD_EXACT_PATH |
| `results/b25_01/static_check.txt` | 2891 | `21aefe0c853df37d5b08b93d4cd89f8e15dd4c907579f9aa89806a77d0c8c4a8` | ADD_EXACT_PATH |
| `results/b25_01/STATUS.md` | 1118 | `209b040a4e64dea0917228b535191dc81b8d3958db51523985294401ab2a4016` | ADD_EXACT_PATH |

## B25_02

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B24-06`
Branch: `b24-06-paper2`; baseline/current HEAD: `0019b2e2359eeabe065dad4271b89f06e2553896`.

HOLD FOR PRE-DELIVERY REPAIR: Paper 2 line 653 compile error; outcome (2), mathematical readiness blockers remain.

Manifest: `results/b25_02/MANIFEST.json`; raw SHA256 `71c008fe10ed3496f1c10192e4ecce4ba8a1a746b2462cb998e99d564760b036`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `docs/b25_02_report.md` | 20364 | `0b976c69d629adcfd2fb7638dd9a09fb5664b8c6a542b282599935a462f1a25c` | ADD_EXACT_PATH |
| `paper/det4-onset.tex` | 71238 | `328b23350bf9dee438887403ed39d7fa8b51f52debb23304c9acae916285e6a3` | ADD_EXACT_PATH |
| `PAPER2_BLOCKERS.md` | 30489 | `dfbcd16537325f107c5f830166596a3a3624e1077ac325c0288487de8ffdf050` | ADD_EXACT_PATH |
| `PAPER2_CLAIMS.md` | 31773 | `6a2b525235cf22c24654084d7d1fc7c86b509748dfcfb80de3400a736c26f0a2` | ADD_EXACT_PATH |
| `PAPER2_GAPS.md` | 15883 | `4f86bcd45f2ca302243e28cd95d440516e3a5397b97290ab67f43bbf148dda55` | ADD_EXACT_PATH |
| `PAPER2_READINESS.md` | 5131 | `9de8d41fbbced72fbec3eac4b00aedede41338e26392c52e2a4f7351d8c2e097` | ADD_EXACT_PATH |
| `results/b25_02/det4-onset.diff` | 55486 | `00b37fbae05695bf5447aadb9bd4a5a8b80741d383442860ee63a3c4d650b8cd` | ADD_EXACT_PATH |
| `results/b25_02/MANIFEST.json` | 4634 | `71c008fe10ed3496f1c10192e4ecce4ba8a1a746b2462cb998e99d564760b036` | ADD_EXACT_PATH |
| `results/b25_02/mechanical_check_after.txt` | 1177 | `6bdc19814b5ba4cc372fefdbda8c906cf9e04d90df8dca8c8c52d08d04aa14dc` | ADD_EXACT_PATH |
| `results/b25_02/mechanical_check_before.txt` | 1245 | `6790b2eb6a060c385c0641bc0a2e6905c3b3246b8e68a640b3fad196df5abedb` | ADD_EXACT_PATH |
| `results/b25_02/SOURCE_READING.md` | 9851 | `64240338e4275decf3069507f45a123c99070bc9ba60927b7e450acbc98ef1b7` | ADD_EXACT_PATH |
| `results/b25_02/texnum.py` | 2169 | `7050d6adf663a4d17e45efc127ac6cc4f85b7974e38e041d33db84a4f0e27a4c` | ADD_EXACT_PATH |

## B25_03

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B23-05`
Branch: `b23-05-paper1`; baseline/current HEAD: `bc7e62b714632c20d2405e54030224a2549c242d`.

Paper 1 readiness withdrawal and proposed attribution patch; patch NOT applied; paper unchanged; reported clean unsigned compile.

Manifest: `results/b25_03/MANIFEST.json`; raw SHA256 `e476683e49221a24ff88f8702379ada3cb5ea8cf0c6e1cfc52ce56b3830e1607`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `ATTRIBUTION_PATCH.md` | 14528 | `4882be4b31000877a35636e61df195789002ef2cf91d59dfebab40650a678497` | ADD_EXACT_PATH |
| `CHANGES.md` | 30662 | `13572d1564c40612f32c78b1091f87c494faa05ae81a36936102ddb8a0f1bb58` | ADD_EXACT_PATH |
| `docs/b25_03_report.md` | 21964 | `fd1f0d93a23407f8f55f2d82ae342016a904c256573cba2be26262244087d01a` | ADD_EXACT_PATH |
| `GAPS.md` | 27371 | `b1b8d4c773a614d85610b63999959164291e05d42ca5fa3f96f6f7ce809a298d` | ADD_EXACT_PATH |
| `paper/det3-conductor.tex` | 116406 | `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445` | BIND_ONLY_UNCHANGED_CRLF_RENDERING |
| `READINESS.md` | 9662 | `9d82b251ead30b3e6b5634237b97b879365383a796c1db514447db87b5ee8470` | ADD_EXACT_PATH |
| `README.md` | 9892 | `5ba2586a7f312be99fb6f6e231e95461a17acdc2c1c3e0fccdfc4c8427eeb617` | BIND_ONLY_UNCHANGED_CRLF_RENDERING |
| `results/b25_03/attribution_patch_extracted.diff` | 2193 | `ea80adeb9b85cc3906bf03086cbc404e6e99cdf49086376290f13c14229734f5` | ADD_EXACT_PATH |
| `results/b25_03/lmr_prop351_quotes.md` | 5109 | `bb339cd4c3e9b064184f620e4b3318f54f11b56dbda058dd25208aca1e9913f5` | ADD_EXACT_PATH |
| `results/b25_03/MANIFEST.json` | 6273 | `e476683e49221a24ff88f8702379ada3cb5ea8cf0c6e1cfc52ce56b3830e1607` | ADD_EXACT_PATH |

## B25_04

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-02`
Branch: `b15-02-a1-probes`; baseline/current HEAD: `aafcbb692375f0a968881dbf18963a74d62ab557`.

Scoped component-family no-go; 2 wrapped pilots reported (first vacuous, second nonvacuous); review pending.

Manifest: `results/b25_04/MANIFEST.json`; raw SHA256 `a33ab4dd19d5507e569870971ff1d835813ab2cd5cef96c48afb5de6b473edd9`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `analysis/b25_04_p1_factor.py` | 4939 | `cee1d087c3b3c68366539738ddffab434a47319f57a9f041fd2532e05a5a76a5` | ADD_EXACT_PATH |
| `analysis/b25_04_p2_nonvacuous.py` | 2967 | `be3cb85bce4177a114e61d4b35d3c546b429d428666df51931cc0db847e8059f` | ADD_EXACT_PATH |
| `docs/b25_04_report.md` | 29850 | `f6e14afdd7da6b2c7b3df340cce5d3571af864f14240abf82f6331edd6129a47` | ADD_EXACT_PATH |
| `results/b25_04/lease_acquired_copy_p2.json` | 558 | `81cb2efa142d5360d9bea74cc81ac085b2df33909132c75be32f035b230fa8b1` | ADD_EXACT_PATH |
| `results/b25_04/lease_acquired_copy.json` | 549 | `c7705c3ddeecfca1d4897d72d65f1ec9b8e64a23f675bbd5bc5f56af1e1e0de9` | ADD_EXACT_PATH |
| `results/b25_04/MANIFEST.json` | 4009 | `a33ab4dd19d5507e569870971ff1d835813ab2cd5cef96c48afb5de6b473edd9` | ADD_EXACT_PATH |
| `results/b25_04/p1_factor.json` | 2505 | `cc6031c8ed9fe6a354e53676fc03e21426feae661fbbfa70e5581e2f1ed40ce5` | ADD_EXACT_PATH |
| `results/b25_04/p1_stdout.txt` | 561 | `a99d8cab50baaee75f5dfa9d60cafd57bc790ef0b3126556376126fcac697a9f` | ADD_EXACT_PATH |
| `results/b25_04/p2_nonvacuous.json` | 1858 | `385208957a660dd19772bb7a6251abdf473d71a503c60c07a2a75f5619356054` | ADD_EXACT_PATH |
| `results/b25_04/p2_stdout.txt` | 751 | `303a17b149b1270ba327f5937d10e713128d01aca21f4b98fecfc3462b8e31a0` | ADD_EXACT_PATH |
| `results/b25_04/PREREG_b25_04_p1.md` | 2889 | `101c086e9916f5280d78db5397c6ddbc889a13ebf0a1a11316e58688fbfb6516` | ADD_EXACT_PATH |
| `results/b25_04/PREREG_b25_04_p2.md` | 2125 | `d67ff53405d7e438e5c1cb42c0989e2e5488d0ece271e1701acb07407a8cf5a4` | ADD_EXACT_PATH |
| `results/b25_04/STATUS.md` | 654 | `7deb9bc123cd20705be6fa5fae553b3369cc13ab369909604069464542afab96` | ADD_EXACT_PATH |
| `results/b25_04/THEORY_GATE.md` | 3916 | `a86e41d65a40bd9c1e3e42e216d4b5db6aab605bad678a9d2e2b24644545518e` | ADD_EXACT_PATH |
| `results/logs/b25_04_p1_factor_resources.json` | 808 | `ac95ab0977fc7578eab3716aba3f2a5d4dbab22c2e82277b90873583ce210d1d` | ADD_EXACT_PATH |
| `results/logs/b25_04_p1_factor.pid` | 7 | `1e1c8c4b31ba6b4aba6046153d80f2f220ad825ddc6a436fb8ef3317dc7ab30d` | ADD_EXACT_PATH |
| `results/logs/b25_04_p2_nonvacuous_resources.json` | 809 | `058d9e3246dbaaf67f24f50163326528e39d77a29b083a620ea136cba6053e4e` | ADD_EXACT_PATH |
| `results/logs/b25_04_p2_nonvacuous.pid` | 7 | `cfb908fb2688eebf6479849a746a1d6a30b511c6a8fa888c76b5da97b0805920` | ADD_EXACT_PATH |

## B25_05

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-01`
Branch: `b15-01-ci159`; baseline/current HEAD: `5a97317e7e28753261cf6e8dcece180a0e71b718`.

Length restriction proof producer-only; equivariance no-go; B25-10 review required before C45 qualifier change.

Manifest: `results/b25_05/MANIFEST.json`; raw SHA256 `035ef6ead2033e64e847773efe7d0ddfb17108cf7d15d2b706cc424139c1a3fe`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `docs/b25_05_report.md` | 25204 | `38834c316c1b182e6acbe120b1608e3fb325c65e0f12790d0312e1c3a2373455` | ADD_EXACT_PATH |
| `results/b25_05/MANIFEST.json` | 5304 | `035ef6ead2033e64e847773efe7d0ddfb17108cf7d15d2b706cc424139c1a3fe` | ADD_EXACT_PATH |

## B25_06

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B23-03`
Branch: `b23-03-intersection`; baseline/current HEAD: `3bcad66601a586936ce5c76fdf72d9551700dab3`.

Partial boundary reduction, conditional premises named; G-A1 remains OPEN; review pending.

Manifest: `results/b25_06/MANIFEST.json`; raw SHA256 `88f5e8a7973d442f9d292d4c2268c1c515d349abcd1f432e8b94118c225bbedf`.

| Exact relative path | Bytes | Raw SHA256 | Action |
|---|---:|---|---|
| `docs/b25_06_report.md` | 21774 | `c2103a0aa3326cf622a026eff9ac8dc61bdb58b572fa7cb1279dee786b3091bb` | ADD_EXACT_PATH |
| `results/b25_06/MANIFEST.json` | 2811 | `88f5e8a7973d442f9d292d4c2268c1c515d349abcd1f432e8b94118c225bbedf` | ADD_EXACT_PATH |
| `results/b25_06/STATUS.md` | 583 | `0fefee013318d45602aa3e1be2dcaad5c5ded2dad81dc03699517addf965367e` | ADD_EXACT_PATH |

## Configuration changes proposed per branch

Append only the following negation on each slotʼs own branch, after the broad PID ignore rule. Include that branchʼs `.gitignore` in its delivery. These are proposed edits, not applied. Only B25-04 currently has PID receipts; the other five negations implement the userʼs requested coverage.

| Worktree (under repository root) | Exact config path | Line to append | Current config SHA256 |
|---|---|---|---|
| `work/batch15_workers/B23-04` | `.gitignore` | `!results/logs/b25_01_*.pid` | `3ecf799d1709f1626087409ce4336b5c86f38d008b00ffa79019000d83431f09` |
| `work/batch15_workers/B24-06` | `.gitignore` | `!results/logs/b25_02_*.pid` | `3ecf799d1709f1626087409ce4336b5c86f38d008b00ffa79019000d83431f09` |
| `work/batch15_workers/B23-05` | `.gitignore` | `!results/logs/b25_03_*.pid` | `3ecf799d1709f1626087409ce4336b5c86f38d008b00ffa79019000d83431f09` |
| `work/batch15_workers/B15-02` | `.gitignore` | `!results/logs/b25_04_*.pid` | `7202f3a3efaafb01251b2996114e21a7f78696ef56274fbed23a60cd23d0fcea` |
| `work/batch15_workers/B15-01` | `.gitignore` | `!results/logs/b25_05_*.pid` | `919a705ed54f1e5782ecd913db750db93eb9778517fab7e1a6af1d36d4625d4e` |
| `work/batch15_workers/B23-03` | `.gitignore` | `!results/logs/b25_06_*.pid` | `dfd428d3a4d64c03a35c8e5c3fc4b14bc9f52b1b511b2e4555b50cafe11ba2bc` |

For byte preservation, append these exact-path attributes to `.gitattributes` in the indicated worktree; include that `.gitattributes` in its delivery. Existing raw bytes and producer manifests must remain unchanged. `-text` disables line-ending conversion; `whitespace=cr-at-eol` prevents CRLF provenance bytes being treated as whitespace defects. No broad renormalization.

Worktree `C:/Users/swami/Projects/gct-gpt/work/batch15`; config `.gitattributes`; current raw SHA256 `cd3681ae2b30964a0afcc13c304e9c93f739508b63bb74f1b80cab146d264909`.

```gitattributes
results/a25_01/MANIFEST.json -text whitespace=cr-at-eol
results/a25_01/SOURCE_BINDINGS.json -text whitespace=cr-at-eol
docs/a25_02_report.md -text whitespace=cr-at-eol
results/a25_02/ADMIN_VERIFICATION.json -text whitespace=cr-at-eol
results/a25_02/INTAKE.md -text whitespace=cr-at-eol
results/a25_02/MANIFEST.json -text whitespace=cr-at-eol
results/a25_02/SOURCE_BINDINGS.json -text whitespace=cr-at-eol
results/a25_03/ADMIN_VERIFICATION.json -text whitespace=cr-at-eol
results/a25_03/MANIFEST.json -text whitespace=cr-at-eol
results/a25_03/SOURCE_BINDINGS.json -text whitespace=cr-at-eol
```

Worktree `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-02`; config `.gitattributes`; current raw SHA256 `5b492e285c98882b2c6e0af1c006b67ba2efd0ea994747c072f5245c4dedfb33`.

```gitattributes
results/b25_04/lease_acquired_copy_p2.json -text whitespace=cr-at-eol
results/b25_04/lease_acquired_copy.json -text whitespace=cr-at-eol
results/b25_04/p1_factor.json -text whitespace=cr-at-eol
results/b25_04/p1_stdout.txt -text whitespace=cr-at-eol
results/b25_04/p2_nonvacuous.json -text whitespace=cr-at-eol
results/b25_04/p2_stdout.txt -text whitespace=cr-at-eol
results/logs/b25_04_p1_factor_resources.json -text whitespace=cr-at-eol
results/logs/b25_04_p1_factor.pid -text whitespace=cr-at-eol
results/logs/b25_04_p2_nonvacuous_resources.json -text whitespace=cr-at-eol
results/logs/b25_04_p2_nonvacuous.pid -text whitespace=cr-at-eol
```

Worktree `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B23-04`; config `.gitattributes`; current raw SHA256 `b01531705d450fbadaa9e4a016de88c0b242f319d3a0378821fd39b8709fa937`.

```gitattributes
results/b25_01/static_check.txt -text whitespace=cr-at-eol
```

Worktree `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B24-06`; config `.gitattributes`; current raw SHA256 `9b8de18e38d856326c8cbec0e2823496f59c2d5f97c27c5723b89d124890d24d`.

```gitattributes
paper/det4-onset.tex -text whitespace=cr-at-eol
results/b25_02/mechanical_check_after.txt -text whitespace=cr-at-eol
results/b25_02/mechanical_check_before.txt -text whitespace=cr-at-eol
```

B25-03: do not stage the unchanged paper/det3-conductor.tex or README.md and do not change their attributes just to preserve a working-copy rendering. Their raw CRLF and committed LF hashes are separately bound. B25-05 and B25-06: current raw/filtered bytes agree; no new attributes are required by this observation. Recheck at actual delivery.

Coordinator branch: also propose `.gitattributes` additions `docs/b25_12_ledger.md -text whitespace=cr-at-eol` and `results/b25_12/** -text whitespace=cr-at-eol`, and include `.gitattributes`. No coordinator PID negation is needed because no pilot ran.

## Pre-delivery repair and evidence holds

D5 — B25-02: source line 653 contains an optional-argument citation inside the optional theorem title. The integrator reports two parser errors from this line. Brace the citation as `{\cite[Thm.~3.1]{Dimca13}}` or move the provenance outside the optional header while retaining the proved-modulo qualification. No repair has been applied in this intake. Recompile, inspect the log and rendering, and require zero errors. Preserve the present failed-build binding as history; record new after-state hashes, diff and build receipts in a separately identified repair supplement or versioned manifest. Refresh the exact delivery list for any newly created repair artifacts before authorization. Do not silently overwrite a sealed manifest or claim its old hash binds repaired bytes. The listed B25-02 packet is complete as a producer record, but release-ready delivery is held.

D6 — Three compiled-PDF digests in the integrator notes cannot be confirmed locally; build logs were not located either. Obtain matching artifacts or a new source-bound build receipt before claiming independently verified build evidence. Source hashes do match. Papers 1 and 3 have integrator-reported clean builds, not a coordinator build certification. Paper 2ʼs recovered PDF must not circulate.

D7 — Independent acceptance remains pending. B25-10 and A25-10 stay WAITING for committed, hash-bound inputs; no launch is authorized here. Extend A25-10ʼs original input scope explicitly to A25-03/04/05 before any later launch. Keep C45ʼs (star) qualifier until review accepts B25-05, and do not infer the quartic 16-to-9 transfer from the cubic proof. Paper 2ʼs B17-01 closure dependency and B14/B16 decisions remain open. Paper 1ʼs attribution patch is unapplied and readiness remains withdrawn. G-A1 remains open.

## Delivery procedure for a separately authorized future pass

1. Recheck each branch HEAD, file hashes and exact status against the inventory; any drift requires reconciliation. Preserve the current proposal as the intake snapshot.
2. Apply only the proposed per-branch config edits, then confirm both B25-04 PID files are no longer ignored. Do not force-add around the rule defect.
3. Stage only the explicitly enumerated paths after authorization. Verify staged blob content bytes, sizes and SHA256 against raw bindings; raw-versus-filtered equality is mandatory for delivered manifest-bound payloads. Inspect config diffs separately. Preserve before/after bindings for tracked papers.
4. Deliver A25-01/02 before dependent A25-03/04, and those before A25-05, or in one explicitly scoped main-worktree delivery. Pin each producerʼs actual delivery commit for cross-branch reviewers; do not merge or cherry-pick unrelated work. B25-01/02 retain existing qualifiers while B25-05 awaits review.
5. Record real commit IDs only after authorized delivery; then update review input bindings and the live ledger. None exist for these packets yet.

Exclude unrelated caches, old-session receipts, tool memory, other research continuations, all unlisted untracked files, and unavailable PDFs/logs. A directory-level add, add-all, or renormalization is outside this proposal.

## Coordinator exact delivery paths

Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12`; branch `b15-12-padding-orbit-bounds`; baseline HEAD `f55ed57f636e5ae6ea791f3238a66f9414008c90`.

The coordinator manifest hashes the following existing/new administrative artifacts, except itself; the proposed config edit is not yet hash-bound as an after-state.

- `docs/b25_12_ledger.md`
- `results/b25_12/TAKEOVER_RECEIPT_20260921T033154Z.md`
- `results/b25_12/intake_20260922.ps1`
- `results/b25_12/INTAKE_INVENTORY_20260922.json`
- `results/b25_12/finish_intake_20260922.ps1`
- `results/b25_12/NOTE_HASH_VERIFICATION_20260922.json`
- `results/b25_12/NOTE_HASH_VERIFICATION_20260922.md`
- `results/b25_12/DELIVERY_PROPOSAL_20260922.md`
- `results/b25_12/COORDINATOR_MANIFEST_20260922.json`
- `results/b25_12/integrator_notes/A25_INTEGRATOR_VERIFICATION_NOTE.md`
- `results/b25_12/integrator_notes/A25_05_INTEGRATOR_CHECK_NOTE.md`
- `results/b25_12/integrator_notes/B25_01_03_INTEGRATOR_COMPILE_NOTE.md`
- `results/b25_12/integrator_notes/B25_02_INTEGRATOR_COMPILE_NOTE.md`
- `results/b25_12/integrator_notes/a25_05_integrator_check.py`
- `.gitattributes` — proposed configuration edit only, not applied.