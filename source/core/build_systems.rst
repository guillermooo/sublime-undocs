=============
Build Systems
=============

.. seealso::

   :doc:`Reference for build systems <../reference/build_systems>`
        Complete documentation on all available options, variables, etc.

Build systems provide a convenient way to supply arguments and environmental
information to external programs and run them. Use build systems if you need
to run your files through build programs like :program:`make`, command line
utilities like :program:`tidy`, interpreters, etc.

.. note::
    Executables called from build systems must be in your ``PATH``.


File Format
===========

Like many other configuration files in Sublime Text, build systems are JSON
files. Fittingly, they have the extension ``.sublime-build``.

Example
-------

Here's an example of a build system:

.. code-block:: js

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }

``cmd``
    Required. This option contains the actual command line to be executed::

        python -u /path/to/current/file.ext

``file_regex``
    A Perl-style regular expression to capture error information out of the
    external program's output. This information is then used to help you
    navigate through error instances with :kbd:`F4`.

``selector``
    If the **Tools | Build System | Automatic** option is set, Sublime Text
    will use this information to determine which build system is to be used for
    the active file.

In addition to options, you can use variables in build systems too, like we've
done above with ``$file``, which expands to the full path of the file
underlying the active buffer.


Where to Store Build Systems
============================

Build systems must be located somewhere under the ``Packages`` folder
(e. g. :file:`Packages/User`).


Running Build Systems
=====================

Build systems can be run by pressing :kbd:`F7` or from **Tools | Build**.
