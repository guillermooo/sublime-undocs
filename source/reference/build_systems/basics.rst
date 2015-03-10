======================
Build System -- Basics
======================


Overview
========

Using build systems,
you can run files
through external programs
without leaving Sublime Text,
and see the output they generate.

.. note::

    *Build* is used in a broad sense.
    A build system doesn't need to generate
    a compiled executable---it could simply
    format code, run an interpreter, etc.


Parts of a Build System
=======================

Simple build systems
only require a ``.sublime-build`` file.
More advanced build systems
may optionally consist of up to three parts:

* a ``.sublime-build`` file (configuration data in JSON format)
* optionally, a custom Sublime Text command driving the build process
* optionally, an external executable file (script or binary file)


``.sublime-build`` Files
************************

A ``.sublime-build`` file
contains configuration data
as a JSON object.
This file is used to specify
switches, options and environmental data.
Each ``.sublime-build`` file
is normally associated
with a specific scope.

The file name represents the name
of the build system
and will be displayed
whenever you can select a build system.


Example
*******

.. sourcecode:: javascript

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }


The Sublime Text Command Used in A Build System
***********************************************

When you run
the default build task in Sublime Text
(:kbd:`Ctrl+B`),
a Sublime Text command receives
the configuration data
specified in the ``.sublime-build`` file.
This command then *builds* the files.
Often, it calls
an external program.
By default, the command
used in build systems is called ``exec``,
but it can be overriden.


Overriding the Default Command for Build Systems
------------------------------------------------

By default, build systems use
the ``exec`` command implemented by :file:`Packages/Default/exec.py`.
This command simply forwards configuration data
to an external program
and runs it asynchronously.

Using the ``target`` option
in a ``.build-system`` file,
it's possible to override
the ``exec`` command.
See :ref:`build-arbitrary-options` for details.


Calling External Programs
*************************

A build system may call
an external program
to process files.
The external program may be
a custom shell script,
a standard utility like ``make`` or ``tidy``, etc.
Usually, the external program
receives paths to files or directories,
along with switches and options
that configure its behavior.

.. note::

   Build systems can but don't need to
   call external programs---a build system
   could be implemented entirely
   as a Sublime Text command.
