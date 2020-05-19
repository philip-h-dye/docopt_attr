# -*- coding: utf-8 -*-

import sys

from docopt import docopt

#------------------------------------------------------------------------------

class AttributeConfig(object):
    def __init__(self, *args, **kwargs):
        # self.attr = [ ]
        for key, value in kwargs.items() :
            setattr(self, key, value)
            # self.attr.append(key)
    def __str__(self):
        return ( "AttributeConfig(" +
                 ", ".join([ f'{k}={repr(v)}' for k,v in self.__dict__.items() ]) +
                 ")" )

#------------------------------------------------------------------------------

def docattr(doc, argv=None, help=True, version=None, options_first=False):

    """docopt with options in attributes rather than dictionary elements

           args['--verbose']  =>  args.verbose

           args['<file>']     =>  arg.file

       All else remains the same.  Attributes are single values or lists
       as appropriate.

       <docopt-doc>
    """

    args = docopt(doc, argv, help, version, options_first)

    clean = { }
    # for key, value in args.items() :
    for key in args :
        value = args[key]
        if key.startswith('--') :
            key = key[2:]
            print(f": -- {key:<16s} : {repr(value)}")
        elif key.startswith('<') and key.endswith('>') :
            key = key[1:][:-1]
            print(f": -- {key:<16s} : {repr(value)}")
        else :
            raise ValueError("Unrecognized option name '{key}'")
        key = key.replace('-', '_')
        clean [ key ] = value
    #
    return AttributeConfig(**clean)
        
docattr.__doc__ = docattr.__doc__.replace('<docopt-doc>', docopt.__doc__ )

# ------------------------------------------------------------------------------
