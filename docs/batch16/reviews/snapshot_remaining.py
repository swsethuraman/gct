from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2]
for slot,name,key,base_delivery in [('01','MANIFEST.json','files',False),('09','delivery_manifest.json','outputs',False),('10','SHA256_MANIFEST.json','files',True),('11','DELIVERY_MANIFEST.json','files',True)]:
    w=ROOT/'work/batch15_workers'/('B15-'+slot);d=w/'delivery'/('b16_'+slot)
    out=ROOT/'Batch16/reviews'/slot;out.mkdir(exist_ok=True)
    m=json.loads((d/name).read_text(encoding='utf-8-sig'));checked=[]
    for f in m[key]:
        p=Path(f['path']); src=p if p.is_absolute() else (d if base_delivery else w)/p
        assert hashlib.sha256(src.read_bytes()).hexdigest()==f['sha256'].lower(),src
        rel=src.relative_to(d if base_delivery else w)
        dst=out/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        checked.append({'path':str(rel),'sha256':f['sha256']})
    if slot=='09': shutil.copytree(d/'inputs',out/'delivery/b16_09/inputs',dirs_exist_ok=True);shutil.copy2(d/'input_manifest.json',out/'delivery/b16_09/input_manifest.json')
    shutil.copy2(d/name,out/'ORIGINAL_DELIVERY_MANIFEST.json')
    # Portable receivers expect their own manifest filename as well.
    if base_delivery: shutil.copy2(d/name,out/name)
    (out/'SNAPSHOT_BINDING.json').write_text(json.dumps(checked,indent=2)+'\n')
    print(slot,len(checked),'hashes PASS')
