# Commit-message callback BODY for git-filter-repo.
#
# git-filter-repo's --commit-callback takes the *body* of the function, with
# `commit` and `metadata` already in scope -- not a `def`.  Three fixes, all
# message-level:
#
#   1. strip the UTF-8 byte-order mark that Windows PowerShell's
#      `Set-Content -Encoding utf8` prepended to two merge messages;
#   2. remove `Claude-Session:` trailer lines;
#   3. remove any bare claude.ai URL line.
#
# A third fix lived here until the batch-13 pass: `h_pad >= 19` -> `h_pad >= 9`
# in the s47 merge message.  It was a one-off content correction, it is complete,
# and the batch-13 run measured zero remaining targets, so it is retired.  The
# BOM strip stays: PowerShell can reintroduce one at any time.
#
# Everything else is left byte-identical.

_bom = b"\xef\xbb\xbf"
_msg = commit.message

if _msg.startswith(_bom):
    _msg = _msg[len(_bom):]
_msg = _msg.replace(b"\n" + _bom, b"\n")

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
