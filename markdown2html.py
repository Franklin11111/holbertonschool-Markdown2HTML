#!/usr/bin/env python
"""
This module is for converting markdown to html
"""

import sys
import os
def markdown2html(markdown, output):
    # This function converts markdown to html

    # if num_args < 2:
    #     print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    filename = 'README.md'
    if not os.path.exists(filename):
        print(f"Missing {filename}", file=sys.stderr)
        exit(1)
    else:
        print()
        exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)

    print(__import__("markdown2html").__doc__)


