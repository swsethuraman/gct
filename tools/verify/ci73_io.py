"""Bounded UTF-8 JSON/gzip read, before parsing; duplicate keys are errors."""
import gzip,hashlib,json
from pathlib import Path

MAX_COMPRESSED=5_000_000
MAX_EXPANDED=16_000_000

def load(path):
    path=Path(path)
    if path.stat().st_size>MAX_COMPRESSED:raise ValueError('compressed/input size limit exceeded')
    opener=gzip.open if str(path).endswith('.gz') else open
    with opener(path,'rb') as stream:raw=stream.read(MAX_EXPANDED+1)
    if len(raw)>MAX_EXPANDED:raise ValueError('expanded size limit exceeded')
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise ValueError('duplicate JSON key: '+k)
            d[k]=v
        return d
    def constant(value):raise ValueError('nonfinite JSON value: '+value)
    return json.loads(raw.decode('utf-8-sig'),object_pairs_hook=pairs,parse_constant=constant)

def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()

def reference(path,root):
    p=Path(path)
    return {'path':p.relative_to(root).as_posix(),'canonical_sha256':digest(load(p))}

def read_reference(ref,root):
    if type(ref) is not dict or set(ref)!={'path','canonical_sha256'}:raise ValueError('invalid dependency reference')
    root=Path(root).resolve();path=(root/ref['path']).resolve()
    if not path.is_relative_to(root):raise ValueError('dependency escapes certificate directory')
    data=load(path)
    if digest(data)!=ref['canonical_sha256']:raise ValueError('dependency digest mismatch: '+ref['path'])
    return data
