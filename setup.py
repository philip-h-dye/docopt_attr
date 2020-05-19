from setuptools import setup, find_packages
from setuptools.command.install import install

from src.version import __version__

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4).pprint

setup(
    name='docattr',
    version=__version__,
    description="docopt with options in attributes rather than dictionary elements",
    author='Philip H. Dye',
    author_email='philip@phd-solutions.com',
    packages=find_packages(exclude=['tests', 'src', 's', 'log']),
    url='https://github.com/philip-h-dye/docattr',
    requires=['docopt'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)

#
