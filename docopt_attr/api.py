# -*- coding: utf-8 -*-

import sys
import re

from docopt import docopt

from collections import UserDict


class AttributeConfig(UserDict):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items() :
            setattr(self, key, value)

    def __str__(self):
        s = ( "AttributeConfig(" +
                 ", ".join([ f'{k}={repr(v)}' for k,v in self.__dict__.items() ]) +
                 ")" )
        return s.replace('\n', '')

    def __repr__(self):
        return self.__str__()


def docopt_attr(doc, argv=None, help=True, version=None, options_first=False,
                _test_cleaned_not_identifier = False):

    """docopt with options in attributes rather than dictionary elements

           args['--verbose']  =>  args.verbose

           args['<file>']     =>  arg.file

       All else remains the same.  Attributes are single values or lists
       as appropriate.

       Original docopt args object args._docopt.

       <docopt-doc>
    """

    args = docopt(doc, argv, help, version, options_first)

    clean = { '_docopt' : args }

    for key in args :
        original_key = key
        value = args[key]
        if key.startswith('<') and key.endswith('>') :
            key = key[1:][:-1]
        key = key.replace('-', '_')
        # Replace any remaining non-identifier characters with underscore
        if not key.isidentifier() :
            key = re.sub(r'[^A-Za-z_]', '_', key)
        # Collapse multiple underscores into a single underscore
        while '__' in key:
            key = key.replace('__', '_')
        # Strip leading and trailing underscores
        if key.startswith('_') :
            key = key[1:]
        if key.endswith('_') :
            key = key[:-1]

        if key in clean:
            raise ValueError(f"Duplicate key '{key}' found converting '{original_key}' "
                             f"to an attribute.\nPlease adjust your docstring to resolve.")

        if not key.isidentifier() or _test_cleaned_not_identifier:
            raise ValueError(f"INTERNAL ERROR : Cleaned '{key}' is not an valid identifier.\n"
                             f"Occurred when converting '{original_key}'.\n"
                             f"Please report this to the maintainer at github.")

        clean [ key ] = value

    return AttributeConfig(**clean)
        
docopt_attr.__doc__ = docopt_attr.__doc__.replace('<docopt-doc>', docopt.__doc__ )
