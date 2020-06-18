### docopt_attr

docopt with options as attributes rather than dictionary elements

A simple wrapper around docopt that maps the args dictionary elements to attributes.

Isn't arguments.file nicer than arguments['<file>'] ?

### Usage

Given example.py :

```
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
```

`example` executed thus :

```
% example --verbose --out=foobar -q -i abc foo bar
arguments.out               =  foobar
arguments.help              =  False
arguments.debug             =  False
arguments.i                 =  True
arguments.version           =  False
arguments.verbose           =  True
arguments.no_show           =  False
arguments.quiet             =  True
arguments.file              =  ['abc', 'foo', 'bar']

```
