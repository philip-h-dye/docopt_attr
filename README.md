### docopt_attr

docopt with options as attributes rather than dictionary elements

A simple wrapper around docopt that maps the args dictionary elements to attributes.

Isn't args.file nicer than args['<file>'] ?

Given this doc passed to docopt :

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
```

And calling docopt_attr thus :

```
argv = [ '--verbose', '--out=foobar', '-q', '-i', 'abc', 'foo', 'bar' ]

args = docopt_attr(__doc__, argv.copy(), version='0.1.5', options_first=True )
```

Specified arguments :

```
assert args.verbose == True
assert args.out == 'foobar'
assert args.quiet == True
assert args.i == True
assert args.file == [ 'abc' == 'foo' == 'bar' ]
```

Unspecified arguments :
```
assert args.no_show == False
assert args.debug == False
assert args.version == False

```
