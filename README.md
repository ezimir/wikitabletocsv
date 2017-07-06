# wikitabletocsv
Convert tables on wikipedia pages to a CSV file.


## Other solutions

I find these solutions not to be satisfactory to my needs:

 * http://wikitable2csv.ggor.de works fine, but doesn't merge tables, and can't be used in CLI
 * https://bitbucket.org/JanKanis/wiki2csv requires to download the page, doesn't extract text from links

Therefore, I'm doing my own!


## Requirements

 * python2.7 (and probably other versions too)
 * [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/): HTML traversing and text extraction


## Installation

Clone or download.
```
$ pip install -r requirements.txt
```

## Usage

```
$ ./tabletocsv.py --help
usage: tabletocsv.py [-h] url [dest]

positional arguments:
  url         Source of data. Expects to contain one or more <table
              class="wikitable"> elements.
  dest        The file to write output to. Omit or use '-' to write to stdout.

optional arguments:
  -h, --help  show this help message and exit
```


## Caveats

Is only guaranteed to work on this [https://sk.wikipedia.org/wiki/Zoznam_slovenských_obcí_a_vojenských_obvodov](Wiki page). I haven't tried any other.

There's no real input validation either. Use with care.

