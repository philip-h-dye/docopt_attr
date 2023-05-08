#!/usr/bin/env python

"""
usage: example [options] <file> ...

Do something for each <file>.

Optional arguments :
  -o, --out FILE Output file
  -n, --no-show  Do not print or log the command line.
  -q, --quiet    Quiet script meta output.
  -v, --verbose  Show additional details.
  -d, --debug    Show debugging details.
  -h, --help     Show this help message and exit.
  -V, --version  Show program version and exit.
  -i             Ignore
"""

import docopt_attr

from docopt_attr import docopt_attr

if __name__ == '__main__':
    arguments = docopt_attr(__doc__, version='0.1.0')
    for key, value in arguments.__dict__.items() :
        if not key.startswith('_') :
            print(f"arguments.{key:<16}  =  {value}")
