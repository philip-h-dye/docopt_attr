"""

Prepend build/lib* directories to sys.path.

If environent variable CONFTEST_VERBOSE is defined and Pythonically
'True' (i.e. neither zero nor an empty string), also print the
paths prepended.

"""

import sys, os
from glob import glob
from pathlib import Path

here = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

here_is_symlink = here.is_symlink()

# Prevent duplicate tests due to symlinks as much as feasible
def pytest_ignore_collect(path, config):
    if here_is_symlink:
        return True
    if '/src/docopt_attr' not in str(path):
        return True

if not here_is_symlink:   
    libs = []
    for lib in glob('build/lib*'):
        lib = Path(lib.strip()).resolve()
        if not lib.is_dir():
            print(f"! NOT a directory '{lib}' ?")
        libs.append(sys.path[0])
        sys.path.insert(0, str(lib))

    _CONFTEST_VERBOSE = 'CONFTEST_VERBOSE'
    if _CONFTEST_VERBOSE in os.environ and os.environ[_CONFTEST_VERBOSE]:
        print(f"Prepended to sys.path :")
        for lib in libs:
            print(f"  {lib  = }")
        print()

