#!/usr/bin/env python
# coding: UTF-8

from setuptools import setup
import os
import shutil

__description__ = 'malware crawler'
__author__ = '@tkmru'
__version__ = '0.1.0'
__date__ = '2016/4/12'
__minimum_python_version__ = (2, 7, 11)
__maximum_python_version__ = (3, 5, 1)
__copyright__ = 'Copyright (c) @tkmru'
__license__ = 'THE BEER-WARE LICENSE'

if not os.path.exists('scripts'):
    os.makedirs('scripts')
shutil.copyfile('maruko.py', 'scripts/maruko')

with open('README.rst', 'r') as f:
    readme_file = f.read()

setup(
    name='maruko',
    version=__version__,
    author=__author__,
    author_email='i.am.tkmru@gmail.com',
    install_requires=['BeautifulSoup4', 'python-magic'],
    scripts=['scripts/maruko'],
    url='https://github.com/tkmru/maruko',
    license=__license__,
    keywords=['malware', 'crawler'],
    description=__description__,
    long_description=readme_file,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux'
        ]
)
