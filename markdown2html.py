#!/usr/bin/python3
import sys
import os
def markdown2html(*args):
    num_args = len(args) - 1
    filename = 'README.md'
    if num_args < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)

    if not os.path.exists(filename):
        print(f"Missing {filename}", file=sys.stderr)
        exit(1)
    else:
        print()
        exit(0)

if __name__ == "__main__":
    print(__import__("markdown2html").__doc__)
