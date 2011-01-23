Build Systems
=============

**The specifics of this topic target Sublime Text X.**

.. seealso::

   :doc:`Reference for build systems <../reference/build_systems>`
        Complete documentation on all available options, variables, etc.

If you need to run build programs like ``make``, command line utilities like
``tidy``, interpreters, etc., use **build systems**. Build systems provide a
convenient way to pass arguments to these programs and adjust other settings so
that you can run your entire project or selected files through them.

.. note::
    The programs you want to call from Sublime Text X via build systems must be
    in your ``PATH``.

File Format
***********

Like many other configuration files in Sublime Text X, build systems use JSON.
Build systems have the extension ``sublime-build`` and must be located somewhere
under the ``Packages`` folder.

Example
*******

Here's an example build system:

.. code-block:: js

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }

``cmd``
    Required. This option contains the actual command line that will be executed;
    in this case::

        python -u /path/to/current/file.ext

``file_regex``
    A Perl-style regular expression to capture the external program's output and
    extract error information. This information is then used to help you move
    through errors with ``F4``.

``selector``
    Determines de scope where the build system will be active.

In addition to options, you can use variables in build systems too, like we've
done above with ``$file``, which expands to the full path of the file underlying
the currently active buffer in Sublime Text X.

How to Run a Build System
*************************

Build systems can be run by pressing ``F7`` or always upon saving your file.
You can also run build systems from the menu if you go to **Tools | Build**.
