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
                text = r.read()
                textLines = text.splitlines()
                i = 0
                while i < len(textLines):
                    line = textLines[i]
                    if line == '':
                        i += 1
                        continue
                    if line.startswith('######'):
                        w.write('<h6>{}</h6>\n'.format(line[7:]))
                    elif line.startswith('#####'):
                        w.write('<h5>{}</h5>\n'.format(line[6:]))
                    elif line.startswith('####'):
                        w.write('<h4>{}</h4>\n'.format(line[5:]))
                    elif line.startswith('###'):
                        w.write('<h3>{}</h3>\n'.format(line[4:]))
                    elif line.startswith('##'):
                        w.write('<h2>{}</h2>\n'.format(line[3:]))
                    elif line.startswith('#'):
                        w.write('<h1>{}</h1>\n'.format(line[2:]))
                    elif line.startswith('-'):
                        listStr = ""
                        for j in range(i, len(textLines)):
                            if textLines[j].startswith('-'):
                                listStr += "<li>{}</li>\n".format(
                                    textLines[j][2:])
                            else:
                                break
                        w.write("<ul>\n{}</ul>\n".format(listStr))
                        i = j
                    else:
                        w.write(line)
                    i += 1

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
