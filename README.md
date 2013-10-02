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

The preferred way to install pygments-pvs is by using pip.

Global installation using pip (can require root privileges):

    $ pip install pygments-pvs

User installation using pip:

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
