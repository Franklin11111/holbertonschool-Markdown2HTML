#!/usr/bin/python3
import sys
import os
def markdown2html(markdown, output):
    filename = 'README.md'
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    if not os.path.exists(filename):
        print(f"Missing {filename}", file=sys.stderr)
        exit(1)
    else:
        print()
        exit(0)

if __name__ == "__main__":
    print(__import__("markdown2html").__doc__)