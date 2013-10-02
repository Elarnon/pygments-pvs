#!/usr/bin/python

from setuptools import setup, find_packages
setup(
    name = 'pygments-pvs',
    version = '0.1',
    description = 'Pygments lexer for PVS source files',
    long_description = open('README.txt').read(),
    license = 'MIT',
    author = 'Basile Clement',
    author_email = 'basile@clement.pm',
    packages = find_packages(),
    zip_safe = True,
    install_requires = [
        'pygments'
    ],
    entry_points = {
        'pygments.lexers': 'pvs=pygments_pvs:PVSLexer',
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
