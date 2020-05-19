# -*- coding: utf-8 -*-

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

NOT YET IMPLEMENTED :
X -s, --silent   Silence STDOUT.  Output only to <log-file> (-q -n).
"""

#------------------------------------------------------------------------------

import unittest

import sys

from docopt import docopt

from docattr import docattr

#------------------------------------------------------------------------------

class Test_Case ( unittest.TestCase ) :

    def setUp ( self ) :
        argv = [ '--verbose', '--out=foobar', '-q', 'abc', 'foo', 'bar' ]
        self.args = docattr(__doc__, argv.copy(), version='0.1.5', options_first=True )

    def test_001_doc ( self ) :
        self.assertTrue ( len(docattr.__doc__) > 30 )

    def test_002_args ( self ) :

        self.assertEqual ( self.args.out		, 'foobar' )
        self.assertEqual ( self.args.no_show	, False )
        self.assertEqual ( self.args.quiet		, True )
        self.assertEqual ( self.args.verbose	, True )
        self.assertEqual ( self.args.debug		, False )
        self.assertEqual ( self.args.version	, False )
        self.assertEqual ( self.args.file		, [ 'abc', 'foo', 'bar' ] )

#------------------------------------------------------------------------------
