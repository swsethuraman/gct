"""Bounded portable assembly, verification and seal for the frozen audit."""
import hashlib
import json
import os
from pathlib import Path
import runpy
import time
import zipfile

OWN=Path(__file__).resolve().parents[1]
PACKAGE=OWN/"delivery/b16_11"
OUT=OWN/"results/b16_11"


def dump(p,v): p.write_text(json.dumps(v,indent=2)+"\n",encoding="utf-8")
def sha(data): return hashlib.sha256(data).hexdigest()


def main():
    if "CI73_DEADLINE" not in os.environ: raise RuntimeError("wrapper required")
    start=time.perf_counter()
    copies={
        "docs/b16_11_report.md":"REPORT.md",
        "docs/b16_11_receiver_spec.md":"RECEIVER_SPEC.md",
        "analysis/b16_11_test_receiver.py":"b16_11_test_receiver.py",
        "analysis/b16_11_finalize.py":"b16_11_finalize.py",
        "results/b16_11/integration_controls.json":"integration_controls.json",
        "results/b16_11/receiver_01.json":"first_receiver_receipt.json",
        "results/b16_11/process_exit.json":"process_exit_before_packaging.json",
    }
    for name in ("build_01","build_02","receiver_01","controls_01"):
        copies["results/logs/b16_11_"+name+"_resources.json"]="resources/b16_11_"+name+"_resources.json"
    for src,dst in copies.items():
        target=PACKAGE/dst
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes((OWN/src).read_bytes())
    ns=runpy.run_path(str(PACKAGE/"b16_11_receiver.py"),run_name="bounded_receiver")
    result=ns["verify"](PACKAGE,OWN.parents[2])
    result["receiver_source_sha256"]=sha((PACKAGE/"b16_11_receiver.py").read_bytes())
    dump(PACKAGE/"FINAL_RECEIVER_RESULT.json",result)
    (PACKAGE/"README.md").write_text(
        "# B16-11 frozen-launch receiver\n\n"
        "Read REPORT.md and RECEIVER_SPEC.md. INPUT_HASHES.json pins the108 semantic/audit input copies. "
        "DELIVERY_MANIFEST.json seals this filesystem delivery; no commit or common merged base is asserted. "
        "The B15 proofs and expensive calculations are inherited. This receiver verifies metadata, "
        "conditional arithmetic, and its own rejection controls only.\n\n"
        "From the assigned B15-11 worktree (choose fresh output names):\n\n"
        "```powershell\n"
        "& ./.venv/python.exe -B delivery/b16_11/b15_bound.py --slot 11 --name b16_11_receive_again "
        "--seconds 60 --memory-mb 512 delivery/b16_11/b16_11_receiver.py --package delivery/b16_11 "
        "--output results/b16_11/receive_again.json\n```\n\n"
        "Core b16_11_receiver.py and b15_bound.py are portable together with evidence/ and INPUT_HASHES.json. "
        "The test, build, Git and finalize scripts preserve provenance and use the original worktree layout; "
        "they are not the portable entry point. Another OS needs an equivalent enforced supervisor. "
        "No inherited producer code is executed.\n\n"
        "Final archive-generation resources and final process exit are sibling worktree artifacts "
        "results/logs/b16_11_finalize_02_resources.json and results/b16_11/process_exit.json. "
        "The archive contains completed build, receiver and integration-control receipts; it cannot "
        "contain the receipt written after its own creation.\n",encoding="utf-8")
    files=[]
    for p in sorted(PACKAGE.rglob("*")):
        if p.is_file() and p.relative_to(PACKAGE).as_posix() not in ("DELIVERY_MANIFEST.json","b16_11_receiver.zip"):
            data=p.read_bytes()
            files.append(dict(path=p.relative_to(PACKAGE).as_posix(),bytes=len(data),sha256=sha(data)))
    manifest=dict(schema="b16-11-delivery/1",status="FILESYSTEM_DELIVERY_NO_COMMIT_CLAIM",
        owner="B16-11",source_head="c40546038506fc6c7c4585dc32244a63376a91dc",
        files=files,mathematical_replays=0,heavy_lease_used=False,
        positive_claim_admitted=False,contents_bytes=sum(f["bytes"] for f in files))
    dump(PACKAGE/"DELIVERY_MANIFEST.json",manifest)
    # Re-read every sealed byte before archiving.
    for e in files:
        data=(PACKAGE/e["path"]).read_bytes()
        if len(data)!=e["bytes"] or sha(data)!=e["sha256"]: raise RuntimeError("seal mismatch")
    archive=PACKAGE/"b16_11_receiver.zip"
    with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for e in files: z.write(PACKAGE/e["path"],e["path"])
        z.write(PACKAGE/"DELIVERY_MANIFEST.json","DELIVERY_MANIFEST.json")
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None: raise RuntimeError("archive CRC failure")
        for e in files:
            if sha(z.read(e["path"]))!=e["sha256"]: raise RuntimeError("archive hash failure")
        extracted=OUT/("archive_control_"+str(os.getpid()))
        z.extractall(extracted)
    extracted_ns=runpy.run_path(str(extracted/"b16_11_receiver.py"),run_name="archive_receiver")
    extracted_result=extracted_ns["verify"](extracted)
    if extracted_result["payload_files"]!=result["payload_files"]:
        raise RuntimeError("archive receiver inventory changed")
    receipt=dict(status="PASS_PORTABLE_RECEIVER_SEAL_AND_ARCHIVE",sealed_files=len(files),
        payload_files=result["payload_files"],payload_bytes=result["payload_bytes"],
        zip_bytes=archive.stat().st_size,zip_sha256=sha(archive.read_bytes()),
        delivery_manifest_sha256=sha((PACKAGE/"DELIVERY_MANIFEST.json").read_bytes()),
        input_manifest_sha256=sha((PACKAGE/"INPUT_HASHES.json").read_bytes()),
        archive_extracted_receiver="PASS",seconds=time.perf_counter()-start)
    dump(OUT/"delivery_receipt.json",receipt)
    print(json.dumps(receipt))


if __name__=="__main__": main()
