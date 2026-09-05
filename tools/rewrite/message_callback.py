# Commit-message callback BODY for git-filter-repo.
#
# git-filter-repo's --commit-callback takes the *body* of the function, with
# `commit` and `metadata` already in scope -- not a `def`.  Four fixes, all
# message-level:
#
#   1. strip the UTF-8 byte-order mark that Windows PowerShell's
#      `Set-Content -Encoding utf8` prepended to two merge messages;
#   2. correct `h_pad >= 19` to `h_pad >= 9` in the s47 merge message
#      (19 is the first counterexample's value; 9 is the minimum over the
#      five, and is what results/sixrow_record.md states);
#   3. remove `Claude-Session:` trailer lines;
#   4. remove any bare claude.ai URL line.
#
# Everything else is left byte-identical.

_bom = b"\xef\xbb\xbf"
_msg = commit.message

if _msg.startswith(_bom):
    _msg = _msg[len(_bom):]
_msg = _msg.replace(b"\n" + _bom, b"\n")

_msg = _msg.replace(b"h_pad >= 19", b"h_pad >= 9")

_keep = []
for _line in _msg.split(b"\n"):
    _s = _line.strip()
    if _s.startswith(b"Claude-Session:"):
        continue
    if _s.startswith(b"http") and b"claude.ai" in _s:
        continue
    _keep.append(_line)
_msg = b"\n".join(_keep).rstrip(b"\n") + b"\n"

commit.message = _msg
