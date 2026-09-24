# R27-03 resource receipt

Eight mathematical runs, sequential: seven exact producer replays plus one independent verification. No installs or searches. All commands and input/output/log hashes are in the corresponding runN_receipt.json.

Runtime: installed Python 3.12.10, SymPy 1.14.0, NumPy 2.4.6. The bundled runtime lacked SymPy and was used only for administrative byte binding.

Each mathematical child waited for its supervisor to assign a Windows Job Object, then received the start token. The supervisor enforced 60 seconds wall time and a 512 MiB committed job-memory cap, queried PeakJobMemoryUsed, and recorded it. Every measured peak was also below the stricter decimal 512 MB threshold. OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 were set. No mathematical runs overlapped.

| Run | Script suffix | Wall seconds | Peak job bytes | Raw output equals producer | Mathematical JSON equals producer |
|---|---|---:|---:|---|---|
| 1 | witness | 1.296181 | 70569984 | no | yes, ignoring only wall_s |
| 2 | kernel | 6.052240 | 57876480 | no | yes, ignoring only wall_s |
| 3 | kernel2 | 40.877088 | 130031616 | no | yes, ignoring only wall_s |
| 4 | dims | 1.117925 | 40992768 | no | yes, ignoring only wall_s |
| 5 | rays | 30.509023 | 88084480 | no | yes, ignoring only wall_s |
| 6 | deg4 | 26.725291 | 191000576 | no | yes, ignoring only wall_s |
| 7 | ray2 | 38.937249 | 85925888 | no | yes, ignoring only wall_s |
| 8 | independent | 1.233822 | 70844416 | not applicable | independent certificate |

Raw output SHA-256 values (hashes name the exact files on disk, with no normalization):

| Run | Reviewer output SHA-256 | Producer output SHA-256 |
|---|---|---|
| 1 | `d822d23e4bbb29a6c18a78114bef3c4d6b1412b1b38bb511d9f06671d0d1af0d` | `132616f48f90150f24de0cda27fab118db22408c9e62d828fdd1fbcc884142a9` |
| 2 | `af62d22bb885adc97f31db47061378a21199f38ad1968f0b0101e7bdf3f1a565` | `53faa7c20f94dcd03bd6a79dee1a34358916c5f5dca23fc1ba3462c5ee3918f9` |
| 3 | `90a5580d50bcc32d948d59787bddee555b06f9267dbf1c683d11b85bf369b751` | `b8142414ce319ec3843ed49d95b31b9c818415b91dcfbbbe171461a4a99a10ef` |
| 4 | `5fc4f886539d59f7de2572acc924a711b3de7e084599cae11b47bfc8bd73b9e9` | `f73e4616269b7fb810ec15eb8d7ab26af61780adc6e2b9c5d626850ee2572c09` |
| 5 | `bcb0230fc1be48f046add9b307d8f77f9aeec49529e4769c24ae2aa18116ff87` | `784606b0fb8b06d93b4c478fa8d594ce8f668b1f1201a92480aaabafca7fc9e9` |
| 6 | `c804f4db651d571b0fa465a28c83b4eb09893f30bdb3d9018c755444d6801c16` | `4668d2bf59dd3356a25787b3205cc01045d1299b2b3902d0a8d82c2c0eb9e03a` |
| 7 | `5c7bb944b0e6b9aa9816140326166976cfc3c888f150f176c5111be588367349` | `e2d567f2c0384a8b6a73c78c8600371cd0395a0456a410b73ac43e24a1087232` |
| 8 | `6ae5b902a55e11e843bde8cd816623429c2551693abd0cf0fce9581f38415a64` | `not applicable` |

The mathematical comparison parses both JSON files and recursively removes only dictionary keys exactly named wall_s. Every other value, key and list order agrees on all seven replays. Raw output hashes do not agree; timing fields prevent byte-identical reexecution. No changed source code or frozen clock was used to force a match.

Runs 1–7 executed the manager version preserved byte-for-byte as analysis/b27_03r_manage_replays.py, SHA-256 4c72adb9e85290095ef83ca7ef5426e12582d5b2bd7ad2ec7629ac64d28df0db. The final analysis/b27_03r_manage.py adds support for independent run 8 without changing the seven replay algorithms. Producer code was extracted with git show and executed from isolated temporary analysis directories with its original filenames and imports. Delivered source copies are under analysis/b27_03r_source_*. The library is recorded as an input even for the witness and dimension jobs that do not import it.

Independent run 8 imports no producer mathematics. Its premise is the committed witness JSON. It expands the permanent via sparse integer polynomial multiplication, independently forms gradient Macaulay matrices and nonzero minors, checks prime moduli by exhaustive trial division, verifies the two previously approximate stable-degree dimensions, and checks the stated degree-five combinatorial price. Matrix hashes in independent_run8.json name UTF-8 bytes of json.dumps(matrix,separators=(",",":")), without a trailing newline.

Administrative Python, PowerShell and Git operations only located installed runtimes, copied/read files, hashed and compared bytes, generated receipts/manifests or managed this branch. These are not mathematical runs. The two initial interpreter/import probes found no usable sandbox-PATH Python/SymPy; they did not run mathematical scripts.

First recorded clock after intake: 2026-09-23 04:11:29 UTC. All mathematical runs finished before 2026-09-23 04:18:41 UTC. Initial intake was not separately timestamped. Packet generation UTC: 2026-09-23T04:21:49.652564+00:00.

No follow-up computation, installation, subagent/session, task message, publication or automatic continuation was launched.
