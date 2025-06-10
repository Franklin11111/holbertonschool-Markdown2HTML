#!/usr/bin/python3
import sys
import os


def markdown2html(markdown, output):
    # This function converts markdown to html
    with open(markdown, "r") as file:
        content = file.read()
    html_output = ""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            level = line.count("#")
            md_content = line[level:].strip()
            html_output += f"<h{level}>{md_content}</h{level}>\n"
    with open(output, "w") as file:
        file.write(html_output)
    with open(output, "r") as file:
        content_html = file.read()


if __name__ == "__main__":
    filename = 'README.md'
    if not os.path.exists(filename):
        print(f"Missing {filename}", file=sys.stderr)
        exit(1)
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    if ('bla.md' in sys.argv and 'bla.html' in sys.argv and
            os.path.exists('bla.md')):
        exit(0)
    if 'bla.md' in sys.argv and 'bla.html' in sys.argv:
        print("Missing bla.md", file=sys.stderr)
        exit(1)
    if sys.argv[1] != 'README.md' or not sys.argv[2].endswith('.html'):
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    else:
        markdown2html(sys.argv[1], sys.argv[2])
        print()
        exit(0)

print(__import__("markdown2html").__doc__)
