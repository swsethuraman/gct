# Proposed separate delivery — not executed

**UNCOMMITTED / NOT RELEASED.** Repository `C:/Users/swami/Projects/gct-gpt/work/batch15`, branch batch15-launch, unchanged starting HEAD eb53b97cf0904e2d54fdb7d101d83b024822811b. No prospective delivery commit is asserted.

PROPOSED_ADD_LIST.txt is the exact allowlist for a separately authorized delivery: only docs/a25_10_report.md and named results/a25_10 files. Do not recursively stage pre-existing results/b15_integrator/, producer files, papers, shared ledgers, unrelated outputs or downloaded PDFs. No mathematical analysis script was created.

Follow RUNBOOK and B24 delivery examples as procedures, not current authorization. Verify branch/HEAD/unrelated state and all manifest hashes, including the external manifest digest in SEAL_RECEIPT.json. Recheck current attributes and raw-versus-prospective-filtered blobs for every proposed file. The seal records this read-only comparison; core.autocrlf=true. Owned text is normalized to UTF-8/LF before hashing. No .gitattributes or .gitignore change was made. If filters would change reviewed bytes, stop that delivery and document the resolution before a new seal; never silently normalize another producer or rewrite a historical manifest.

After separate authorization, stage only the allowlist, verify the staged path set and bytes, and inspect the final diff. Preserve original receipts and seals. Record the actual delivery commit and manifest hash in a separate receipt, then re-read committed blobs to establish G29. Do not inject a later commit into this immutable research-time packet. Any push needs its own applicable authorization; neither commit nor push is performed here.

MANIFEST.json does not hash itself. SEAL_RECEIPT.json is a post-seal external digest/readback receipt, excluded from the manifest payload graph but explicitly on the add list; it does not hash itself. ADMIN_VERIFICATION.json records baseline state and pre-seal filter checks for fixed payloads. Generated manifest/receipt filter checks appear in SEAL_RECEIPT.json, with the receipt itself checked by the sealing process after its final write.

No A25-10 PID exists, so no ignore-negation change is required. The global-ignore read warning stays disclosed. No trust, ownership or Git-setting changes are proposed.

Suggested future commit subject: `A25-10: independently review six packets; no construction ready`. This is not an executed command.
