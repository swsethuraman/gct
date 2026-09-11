# Recovered Gram certificate

Original filename: gram_spherical.json. Original size: 7917718 bytes.
Original SHA-256: 28acff2c79d9172c683ab5dbe7dccca96b83cf0ceec6f7291875c6ec8024ab6e

Stored filename: gram_spherical.json.gz. Stored size: 2060580 bytes.
Stored SHA-256: 8b44c470c66f2904456ec90a6aee761f1015847e0585a89f73279cb1a2f1f150

The original JSON is not committed uncompressed because it exceeds 5 MB. The gzip retains exactly the original bytes. In an isolated replay copy of this artifacts directory run:

```python
import gzip
from pathlib import Path
p = Path("gram_spherical.json.gz")
Path("gram_spherical.json").write_bytes(gzip.decompress(p.read_bytes()))
```

Verify the decompressed SHA-256 above before replay. No numerical values were modified.
