#!/usr/bin/python3
""" This script converts markdown to HTML.
"""
import sys


def convert(markdownFile, htmlFile):
    """ Converts markdown to HTML.
    """
    try:
        with open(markdownFile, 'r') as f:
            markdown = f.read()
    except Exception:
        print("Missing {}".format(markdownFile), file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
