#!/usr/bin/python3
""" This script converts markdown to HTML.
"""
import sys


def convert(markdownFile, htmlFile):
    """ Converts markdown to HTML.
    """
    try:
        with open(markdownFile, 'r') as r:
            with open(htmlFile, 'w') as w:
                for line in r:
                    if line.startswith('######'):
                        w.write('<h6>{}</h6>\n'.format(line[7:-1]))
                    elif line.startswith('#####'):
                        w.write('<h5>{}</h5>\n'.format(line[6:-1]))
                    elif line.startswith('####'):
                        w.write('<h4>{}</h4>\n'.format(line[5:-1]))
                    elif line.startswith('###'):
                        w.write('<h3>{}</h3>\n'.format(line[4:-1]))
                    elif line.startswith('##'):
                        w.write('<h2>{}</h2>\n'.format(line[3:-1]))
                    elif line.startswith('#'):
                        w.write('<h1>{}</h1>\n'.format(line[2:-1]))
                    else:
                        w.write(line)

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
