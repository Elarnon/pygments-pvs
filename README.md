Pygments PVS
============

Overview
--------

This packages provides a Pygments lexer for the PVS language. The
lexer is published as an entry point - once installed, Pygments should
use it automatically.

You can then use the ``pvs`` lexer with Pygments:

    $ pygmentize -l pvs mytheory.pvs

.. More about PVS: http://pvs.csl.sri.com/
.. Pygments documentation: http://pygments.org/docs/

Installation
------------

The preferred way to install pygments-pvs is by using pip. This can be
done by installing pygments-pvs from the PyPI repository, or directly
from the source. In both case, the commands install pygments-pvs for
the local user only - if you want to install it system-wide, simply
remove the `--user` flag and start the command as root (using `su` or
`sudo`).

Installing from the PyPI repository:

    $ pip install pygments-pvs --user

Installing directly from the git:

    $ git clone git://github.com/Elarnon/pygments-pvs.git
    $ cd pygments-pvs
    $ pip install . --user

To verify the installation, run

    $ pygmentize -L lexer | grep -i pvs
    * pvs:
        PVS (filenames *.pvs)

Using in LaTeX documents
------------------------

See the minted package at http://minted.googlecode.com
