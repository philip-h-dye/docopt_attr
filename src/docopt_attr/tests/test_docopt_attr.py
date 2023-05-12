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

  --non-identifier-char-%
"""

__version__ = '0.1.0'

import unittest

import sys

from docopt_attr import docopt_attr

#------------------------------------------------------------------------------

class Test_Good ( unittest.TestCase ) :

    def setUp(self):
        argv = [ '--verbose', '--out=foobar', '-q', '-i', 'abc', 'foo', 'bar' ]
        self.args = docopt_attr(__doc__, argv.copy())

    def test_str ( self ) :
        doc = "Usage: example [--foo] BAR"
        args = docopt_attr(doc, ['test'], version=__version__)
        expected = "AttributeConfig(_docopt={'--foo': False, 'BAR': 'test'}, foo=False, BAR='test')"
        self.assertEqual (str(args), expected)

    def test_repr ( self ) :
        doc = "Usage: example [--foo] BAR"
        args = docopt_attr(doc, ['test'], version=__version__)
        expected = "AttributeConfig(_docopt={'--foo': False, 'BAR': 'test'}, foo=False, BAR='test')"
        self.assertEqual (repr(args), expected)

    def test_doc ( self ) :
        self.assertIn ( "creates your command-line interface", docopt_attr.__doc__ )

    def test_boolean_option__verbose ( self ) :
        self.assertEqual ( self.args.verbose, True )

    def test_valued_option__out ( self ) :
        self.assertEqual ( self.args.out, 'foobar' )

    def test_boolean_option_short__quiet ( self ) :
        self.assertEqual ( self.args.quiet, True )

    def test_boolean_option_short_only__i ( self ) :
        self.assertEqual ( self.args.i, True )

    def test_value_list__file ( self ) :
        self.assertEqual ( self.args.file, [ 'abc', 'foo', 'bar' ] )

    def test_unspecified_boolean__no_show ( self ) :
        self.assertEqual ( self.args.no_show, False )

    def test_unspecified_boolean__debug ( self ) :
        self.assertEqual ( self.args.debug, False )

    def test_unspecified_boolean__version ( self ) :
        self.assertEqual ( self.args.version, False )

    def test_non_identifier_char ( self ) :
        self.assertEqual ( self.args.non_identifier_char, False )


class Test_Errors ( unittest.TestCase ) :

    def test_Duplicate_Key ( self ) :
        doc = "Usage: example [--foo_bar | --foo%bar ]"
        with self.assertRaises(ValueError):
            docopt_attr(doc, [])

    # As this situation which shouldn't be possible, we must force
    # it with a module flag.
    def test_Cleaned_Not_Idenifier_Error ( self ) :
        doc = "Usage: example --foo"
        # AttributeConfig.TEST_CLEANED_NOT_IDENTIFIER = True
        with self.assertRaises(ValueError):
            docopt_attr(doc, ['--foo'], _test_cleaned_not_identifier=True)
