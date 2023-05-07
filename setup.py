from setuptools import setup
from pathlib import Path
import re

pypi_name   = 'docopt-attr'
package     = pypi_name.replace('-', '_')
version     = re.search("^__version__\s*=\s*'(.*)'",
                        Path(f'{package}/__init__.py').read_text(),
                        re.M ).group(1)

setup (
    name = pypi_name,
    version = version,
    description = f'docopt with options as attributes rather than dictionary elements'
    author = 'Philip H. Dye',
    author_email = 'philip@acm.org',
    url = f'https://www.github.com/philip-d-dye/{pypi_name}',
    long_description = Path('README.txt').read_text(),
    packages = (pypi_name),
    license_files = ( 'LICENSE' ),
    install_requires = ( 'docopt',),
    tests_require=('pytest','pytest-runner'),
    entry_points = {
        'console_scripts': ( f'{command} = {package}:main',
                           ) },
)
