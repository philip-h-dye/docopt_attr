# -*- coding: utf-8 -*-

import sys
import re

from docopt import docopt

from collections.abc import Mapping


class AttributeConfig(Mapping):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items() :
            setattr(self, key, value)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __str__(self):
        return ( "AttributeConfig(" +
                 ", ".join([ f'{k}={repr(v)}' for k,v in self.__dict__.items() ]) +
                 ")" )

    def __repr__(self):
        return self.__str__()


def docopt_attr(doc, argv=None, help=True, version=None, options_first=False):

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
            # print(f": -- {key:<16s} : {repr(value)}")
        if key.startswith('--') :
            key = key[2:]
            # print(f": -- {key:<16s} : {repr(value)}")
        if key.startswith('-') :
            key = key[1:]
            # print(f": -- {key:<16s} : {repr(value)}")
        key = key.replace('-', '_')

        # Replace any remaining non-identifier characters with underscore
        if not key.isidentifier() :
            key = re.sub(r'[^A-Za-z_]','_',key)
        if not key.isidentifier() :
            raise ValueError(f"Cleaned '{key}' is not an valid identifier.\n"
                             f"This occurred when converting '{original_key}'.\n"
                             f"This is a docopt_attr internal error.\n"
                             f"Please report this to the maintainer at github.")
        if key in clean :
            raise ValueError(f"Duplicate key '{key}' found converting '{original_key}' "
                             f"to an attribute.\nPlease adjust your docstring to resolve.")

        clean [ key ] = value

    return AttributeConfig(**clean)
        
docopt_attr.__doc__ = docopt_attr.__doc__.replace('<docopt-doc>', docopt.__doc__ )
