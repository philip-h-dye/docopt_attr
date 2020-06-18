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
  -i             Ignore
"""

#------------------------------------------------------------------------------

import unittest

import sys

from docopt import docopt

from docopt_attr import docopt_attr

#------------------------------------------------------------------------------

class Test_Case ( unittest.TestCase ) :

    def setUp(self):
        argv = [ '--verbose', '--out=foobar', '-q', '-i', 'abc', 'foo', 'bar' ]
        self.args = docopt_attr(__doc__, argv.copy(), version='0.1.5', options_first=True )

    def test_000_doc ( self ) :
        self.assertIn ( "creates your command-line interface", docopt_attr.__doc__ )

    def test_001_boolean_option__verbose ( self ) :
        self.assertEqual ( self.args.verbose, True )

    def test_002_valued_option__out ( self ) :
        self.assertEqual ( self.args.out, 'foobar' )

    def test_003_boolean_option_short__quiet ( self ) :
        self.assertEqual ( self.args.quiet, True )

    def test_004_boolean_option_short_only__i ( self ) :
        self.assertEqual ( self.args.i, True )

    def test_005_value_list__file ( self ) :
        self.assertEqual ( self.args.file, [ 'abc', 'foo', 'bar' ] )

    def test_006_unspecified_boolean__no_show ( self ) :
        self.assertEqual ( self.args.no_show, False )

    def test_007_unspecified_boolean__debug ( self ) :
        self.assertEqual ( self.args.debug, False )

    def test_008_unspecified_boolean__version ( self ) :
        self.assertEqual ( self.args.version, False )

#------------------------------------------------------------------------------
