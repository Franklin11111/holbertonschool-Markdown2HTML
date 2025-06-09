#!/usr/bin/python3
"""
This module is for converting markdown to html
"""
import sys
import os
def markdown2html(*args):
    # This function converts markdown to html
    num_args = len(args)
    print(num_args)
    filename = 'README.md'
    if num_args < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)

    if not os.path.exists(filename):
        print(f"Missing {filename}", file=sys.stderr)
        exit(1)
    else:
        print()
        exit(0)
print(__import__("markdown2html").__doc__)
if __name__ == "__main__":
    markdown2html('README.md', 'README.html')
