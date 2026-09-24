"""Administrative selection of existing records. No ranks computed or source code executed."""
import datetime, gzip, hashlib, io, json, pathlib, pickle, re, subprocess, zipfile, zlib
from pypdf import PdfReader
import numpy as np
OUT=pathlib.Path(__file__).resolve().parent
REPO=pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
TARGETS=((12,8,6,4,2),(14,10,6,4,2))
def git(*a): return subprocess.check_output(['git','-C',str(REPO),*a])
def sha(b): return hashlib.sha256(b).hexdigest()
def save(p,x): (OUT/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def walk(x,loc='$'):
    if isinstance(x,dict):
        for key in ('lam','lambda','tail','lam_close'):
            v=x.get(key)
            if isinstance(v,list) and (tuple(v) in TARGETS or (key=='tail' and tuple(v) in [t[1:] for t in TARGETS])):
                yield dict(locator=loc,record=x); break
        for k,v in x.items(): yield from walk(v,loc+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): yield from walk(v,loc+'/'+str(i))

selected=[]
for path in sorted((OUT/'inputs').glob('*')):
    if path.suffix not in ['.json','.jsonl','.gz']: continue
    data=path.read_bytes()
    parsed_data=gzip.decompress(data) if path.suffix=='.gz' else data
    if path.suffix=='.jsonl':
        found=[]
        for i,l in enumerate(parsed_data.splitlines(),1):
            if l.strip(): found.extend(walk(json.loads(l),f'line {i}'))
    else: found=list(walk(json.loads(parsed_data)))
    if found: selected.append(dict(snapshot=path.name,sha256=sha(data),matches=found))
save('TARGET_RECORD_EXCERPTS.json',selected)

class SafeUnpickler(pickle.Unpickler):
    def find_class(self,*a): raise ValueError('No executable pickle globals allowed')

review=[]
for row in json.loads((OUT/'RECORD_SEARCH_BINARY.json').read_text()):
    data=git('cat-file','blob',row['oid']); ent=dict(**row,sha256=sha(data)); path=row['path']
    if path.endswith('.pdf'):
        reader=PdfReader(io.BytesIO(data)); txt='\n'.join(p.extract_text() or '' for p in reader.pages)
        hits=[]
        for t in TARGETS:
            p=re.compile(r'(?<!\d)' + r'[\s,;_|:\[\]()]+'.join(map(str,t)) + r'(?!\d)')
            hits.extend(txt[max(0,m.start()-100):m.end()+100] for m in p.finditer(txt))
        ent.update(pages=len(reader.pages),text_sha256=sha(txt.encode()),target_hits=hits,
                   first_text=txt[:300],scope='text search only; no external mathematical premise adopted')
    elif path.endswith('.pkl'):
        obj=SafeUnpickler(io.BytesIO(data)).load()
        ent.update(container_type=type(obj).__name__,records=len(obj),target_matches=list(walk(obj)))
    elif path.endswith(('.npz','.npy')):
        f=np.load(io.BytesIO(data),allow_pickle=False)
        if isinstance(f,np.ndarray):
            ent['arrays']=[dict(name='array',shape=list(f.shape),dtype=str(f.dtype))]
        else:
            ent['arrays']=[]
            for n in f.files:
                try:
                    a=f[n]; detail=dict(name=n,shape=list(a.shape),dtype=str(a.dtype))
                    if n in ('lambda','lam','weight','n','delta','degree','n_chi','prime') and a.size<=20: detail['value']=a.tolist()
                    ent['arrays'].append(detail)
                except ValueError as e: ent['arrays'].append(dict(name=n,note=str(e)))
        ent['scope']='numeric sidecar; metadata/associated source required to identify its cell'
    elif path.endswith('.zip'):
        ent['scope']='text members searched in main scan; archive entries inventoried'
    else:
        ent['scope']='compiled code, image, or scratch data; associated textual source searched'
    review.append(ent)
save('BINARY_REVIEW.json',review)

errs=[]
for row in json.loads((OUT/'RECORD_SEARCH_ERRORS.json').read_text()):
    data=git('cat-file','blob',row['oid']); d=zlib.decompressobj(16+zlib.MAX_WBITS).decompress(data)
    errs.append(dict(**row,sha256=sha(data),decoded_bytes=len(d),prefix=d[:800].decode(errors='replace'),
                     note='Historical truncated gzip; available prefix searched; cell in filename is not a target'))
save('ARCHIVE_EXCEPTIONS.json',errs)
print('Selected source files:',len(selected),'binary objects reviewed:',len(review))
print('PDF hits:',[(r['path'],r['target_hits']) for r in review if 'target_hits' in r])
print('Pickle target records:',[(r['path'],len(r['target_matches'])) for r in review if 'target_matches' in r])
print('Archive exceptions:',errs)
