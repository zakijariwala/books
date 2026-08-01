"""Per-chapter and total word count for manuscript/, checked against a budget.

Run: python scripts/wordcount.py --budget 20000 manuscript
"""
import argparse
import re
import sys
from pathlib import Path

CODE_FENCE = re.compile(r"```.*?```", re.DOTALL)
MERMAID_OR_HTML_TAG = re.compile(r"<[^>]+>")
MD_IMAGE_OR_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
MD_HEADING_MARKS = re.compile(r"^#+\s*", re.MULTILINE)


def word_count(text: str) -> int:
    text = CODE_FENCE.sub("", text)
    text = MERMAID_OR_HTML_TAG.sub("", text)
    text = MD_IMAGE_OR_LINK.sub(r"\1", text)
    text = MD_HEADING_MARKS.sub("", text)
    return len(text.split())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript_dir")
    parser.add_argument("--budget", type=int, default=20000)
    args = parser.parse_args()

    md_files = sorted(Path(args.manuscript_dir).glob("*.md"))
    total = 0
    for path in md_files:
        count = word_count(path.read_text(encoding="utf-8"))
        total += count
        print(f"{path.name:30s} {count:6d}")

    print("-" * 38)
    print(f"{'TOTAL':30s} {total:6d}")
    print(f"{'BUDGET':30s} {args.budget:6d}")
    remaining = args.budget - total
    if remaining < 0:
        print(f"OVER BUDGET by {-remaining} words")
        return 1
    print(f"remaining: {remaining} words")
    return 0


if __name__ == "__main__":
    sys.exit(main())
