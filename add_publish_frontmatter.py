#!/usr/bin/env python3
"""
Bulk-add `publish: true` to the frontmatter of every .md file in a folder.

- Skips files that already have a `publish:` field (won't duplicate/overwrite it).
- If a file has no frontmatter block, one is created.
- If a file already has frontmatter (--- ... ---), `publish: true` is inserted into it.

Usage:
    python add_publish_frontmatter.py "C:\\path\\to\\vault\\Writeups"

Add --dry-run to preview changes without writing anything.
"""

import sys
import re
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def process_file(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)

    if match:
        fm_body = match.group(1)
        if re.search(r"^publish:\s*", fm_body, re.MULTILINE):
            return "skipped (already has publish field)"
        new_fm_body = fm_body + "\npublish: true"
        new_text = text[:match.start(1)] + new_fm_body + text[match.end(1):]
    else:
        new_text = "---\npublish: true\n---\n\n" + text

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return "updated"

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_publish_frontmatter.py <folder> [--dry-run]")
        sys.exit(1)

    folder = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv

    if not folder.is_dir():
        print(f"Not a folder: {folder}")
        sys.exit(1)

    md_files = list(folder.rglob("*.md"))
    if not md_files:
        print("No .md files found.")
        return

    print(f"Found {len(md_files)} markdown files.{' (dry run, no changes will be written)' if dry_run else ''}\n")

    for f in md_files:
        result = process_file(f, dry_run)
        print(f"{result:40} {f}")

if __name__ == "__main__":
    main()
