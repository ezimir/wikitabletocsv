#!/usr/bin/env python



import argparse
import csv
import urllib2
import sys

from bs4 import BeautifulSoup


DEFAULT_CLASS_NAME = 'wikitable'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'url',
        help = 'Source of data. Expects to contain one or more <table> elements with specified class name.'
    )
    parser.add_argument(
        'dest',
        nargs = '?',
        type = argparse.FileType('w'),
        default = sys.stdout,
        help = 'The file to write output to. Omit or use \'-\' to write to stdout.'
    )
    parser.add_argument(
        '--class-name',
        dest = 'class_name',
        default = DEFAULT_CLASS_NAME,
        help = 'CSS class name for the tables to search for. (Without dot, just name.) (default: %(default)s)'
    )
    args = parser.parse_args()

    response = urllib2.urlopen(args.url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for table in soup.findAll('table', {'class': args.class_name}):
        if not data:
            headers = table.findAll('th')
            data.append([h.text.encode('utf8') for h in headers])

        rows = table.findAll('tr')
        for row in rows:
            columns = row.findAll('td')
            if columns:
                data.append([c.text.encode('utf8') for c in columns])

    with args.dest as csvfile:
        writer = csv.writer(csvfile)
        map(writer.writerow, data)


if __name__ == '__main__':
    main()

