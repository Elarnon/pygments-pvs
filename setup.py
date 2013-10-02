from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'pygments-pvs',
    version = version,
    description = 'Pygments lexer for PVS source files',
    long_description = open('README.txt').read() + '\n' +
    open('CHANGES.txt').read(),
    # TODO classifiers = [
    # TODO keywords =
    author = 'Basile Clement',
    author_email = 'basile@clement.pm',
    # TODO url
    # TODO license
    py_modules = ['lexer'],
    zip_safe = True,
    install_requires = [
        'setuptools'
    ],
    entry_points = {
        'pygments.lexer': 'pvs=lexer:PVSLexer',
    },
)
