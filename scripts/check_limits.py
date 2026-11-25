#!/usr/bin/env python3
"""Simple offline writing QA; no applicant data is transmitted.
Usage: python scripts/check_limits.py essay.txt --max-words 500
       python scripts/check_limits.py essay.txt --max-chars 4000
       python scripts/check_limits.py resume.txt --bullets
"""
import argparse
import pathlib
import re
import sys


def main():
    parser = argparse.ArgumentParser(description="Check English word/character limits and CV bullet density")
    parser.add_argument("file", type=pathlib.Path)
    parser.add_argument("--max-words", type=int)
    parser.add_argument("--max-chars", type=int)
    parser.add_argument("--bullets", action="store_true", help="Report bullet word counts and 32–40 target")
    a = parser.parse_args()
    s = a.file.read_text(encoding="utf-8")
    words = len(s.split())
    chars = len(s)
    print(f"Words (whitespace estimate): {words}")
    print(f"Characters incl spaces/newlines (Unicode code points): {chars}")
    print(f"Characters excl whitespace: {sum(not c.isspace() for c in s)}")
    failed = False
    if a.max_words is not None:
        failed |= words > a.max_words
        print(f"Word max {a.max_words}: {'FAIL' if words > a.max_words else 'PASS'}")
    if a.max_chars is not None:
        failed |= chars > a.max_chars
        print(f"Character max {a.max_chars}: {'FAIL' if chars > a.max_chars else 'PASS'}")
    if a.bullets:
        for line_no, line in enumerate(s.splitlines(), 1):
            if re.match(r"^\s*(?:[-*•]|\d+[.)])\s+", line):
                bullet = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s+", "", line)
                n = len(bullet.split())
                print(f"Line {line_no}: {n} words ({'target 32–40' if 32 <= n <= 40 else 'outside editorial target'})")
    if failed:
        print("A hard limit has been exceeded.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
