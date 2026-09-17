# Renders the scanned Eisenbud-Harris PDF (CCITT G4 strips, no text layer) to page PNGs.
# Input: eh1988.pdf (SHA-256 6b10d8fe...) in the working directory; output: pages/pageNN.png.
# Standard library plus ImageMagick `magick` for the G4 decode. Read-only w.r.t. the project.
import re, zlib, struct, os, subprocess
data=open('eh1988.pdf','rb').read()
objs={}
for m in re.finditer(rb'(?:^|[\r\n])(\d+) 0 obj\r?\n?(.*?)endobj', data, re.S):
    objs[int(m.group(1))]=m.group(2)
print(len(objs),'objects')
def stream_of(body):
    i=body.find(b'stream')
    if i<0: return None
    j=i+6
    while body[j:j+1] in (b'\r',b'\n'): j+=1
    k=body.rfind(b'endstream')
    s=body[j:k]
    while s[-1:] in (b'\r',b'\n'): s=s[:-1]
    return s
def deref(b):
    m=re.fullmatch(rb'\s*(\d+) 0 R\s*',b)
    return objs[int(m.group(1))] if m else b
root=[n for n,b in objs.items() if re.search(rb'/Type\s*/Pages\b',b) and b'/Parent' not in b]
print('roots',root)
order=[]
def walk(n):
    b=objs[n]
    if re.search(rb'/Type\s*/Pages\b',b):
        for k in re.findall(rb'(\d+) 0 R', re.search(rb'/Kids\s*\[(.*?)\]',b,re.S).group(1)): walk(int(k))
    elif re.search(rb'/Type\s*/Page\b',b): order.append(n)
walk(root[0]); print('pages in order',len(order))
def tiff_g4(w,h,raw):
    tags=[(256,4,1,w),(257,4,1,h),(258,3,1,1),(259,3,1,4),(262,3,1,0),(273,4,1,0),(277,3,1,1),(278,4,1,h),(279,4,1,len(raw)),(293,4,1,0)]
    hdr_len=8+2+12*len(tags)+4
    out=bytearray(b'II*\x00'+struct.pack('<I',8)+struct.pack('<H',len(tags)))
    for t,typ,cnt,val in tags:
        if t==273: val=hdr_len
        if typ==3: out+=struct.pack('<HHIHH',t,typ,cnt,val,0)
        else: out+=struct.pack('<HHII',t,typ,cnt,val)
    out+=struct.pack('<I',0)+raw
    return bytes(out)
os.makedirs('pages',exist_ok=True)
for pi,pn in enumerate(order,1):
    b=objs[pn]
    r=re.search(rb'/Resources\s*(\d+) 0 R',b)
    res=objs[int(r.group(1))] if r else b
    xo=re.search(rb'/XObject\s*(<<[^>]*>>|\d+ 0 R)',res,re.S).group(1); xo=deref(xo)
    xmap={k.decode():int(v) for k,v in re.findall(rb'/(\w+)\s+(\d+) 0 R',xo)}
    contents=re.search(rb'/Contents\s*(\[.*?\]|\d+ 0 R)',b,re.S).group(1)
    contents=deref(contents)
    if b'stream' in contents: contents=re.search(rb'/Contents\s*(\d+ 0 R)',b).group(1)
    names=[]
    for c in re.findall(rb'(\d+) 0 R',contents):
        cs=stream_of(objs[int(c)])
        if cs is None: continue
        try: txt=zlib.decompress(cs)
        except Exception: txt=cs
        names+=re.findall(rb'/(\w+)\s+Do',txt)
    strips=[]
    for k,nm in enumerate(names):
        if nm.decode() not in xmap: continue
        ib=objs[xmap[nm.decode()]]
        w=int(re.search(rb'/Width\s*(\d+)',ib).group(1)); h=int(re.search(rb'/Height\s*(\d+)',ib).group(1))
        fn=f'pages/p{pi:02d}_{k:03d}.tif'
        open(fn,'wb').write(tiff_g4(w,h,stream_of(ib))); strips.append(fn)
    if strips:
        subprocess.run(['magick']+strips+['-append','-resize','60%',f'pages/page{pi:02d}.png'],check=True)
        for s in strips: os.remove(s)
    print(pi,len(names),'strips',end='; ')
