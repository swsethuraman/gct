"""Commit-message callback for the one-pass history rewrite.

Applied with git-filter-repo.  Four fixes, all message-level:

  1. strip the UTF-8 byte-order mark that Windows PowerShell's
     `Set-Content -Encoding utf8` prepended to two merge messages;
  2. correct `h_pad >= 19` to `h_pad >= 9` in the s47 merge message
     (19 is the first counterexample's value; 9 is the minimum over
     the five, and is what results/sixrow_record.md states);
  3. remove `Claude-Session:` trailer lines;
  4. remove any bare claude.ai URL line.

Everything else is left byte-identical.
"""

BOM = b"\xef\xbb\xbf"


def commit_callback(commit, metadata):
    msg = commit.message

    # 1. byte-order mark, anywhere it leads a line
    if msg.startswith(BOM):
        msg = msg[len(BOM):]
    msg = msg.replace(b"\n" + BOM, b"\n")

    # 2. the h_pad bound in the s47 merge message
    msg = msg.replace(b"h_pad >= 19", b"h_pad >= 9")

    # 3 + 4. session links
    out = []
    for line in msg.split(b"\n"):
        s = line.strip()
        if s.startswith(b"Claude-Session:"):
            continue
        if s.startswith(b"http") and b"claude.ai" in s:
            continue
        out.append(line)
    msg = b"\n".join(out)

    # collapse any trailing blank lines the removals left behind
    msg = msg.rstrip(b"\n") + b"\n"

    commit.message = msg
