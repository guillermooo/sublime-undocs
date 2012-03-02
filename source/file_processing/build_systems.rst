================================
Build Systems (Batch Processing)
================================

Build systems let you run your files through external programs like
:program:`make`, :program:`tidy`, interpreters, etc.

Executables called from build systems must be in your ``PATH``. For more
information about making sure the ``PATH`` seen by Sublime Text is set
correctly, see :ref:`troubleshooting-build-systems`.


File Format
===========

Build systems are JSON files and have the extension ``.sublime-build``.

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
    will automatically find the corresponding build system for the active file
    by matching ``selector`` to the file's scope.

In addition to options, you can also use some variables in build systems, like
we have done above with ``$file``, which expands to the the active buffer's
file name.


Where to Store Build Systems
============================

Build systems must be located somewhere under the ``Packages`` folder
(e. g. :file:`Packages/User`). Many packages include their own build systems.


Running Build Systems
=====================

Build systems can be run by pressing :kbd:`F7` or from **Tools | Build**.


.. seealso::

   :doc:`Reference for build systems <../reference/build_systems>`
        Complete documentation on all available options, variables, etc.
