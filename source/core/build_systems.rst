Build Systems
=============

.. seealso::

   :doc:`Reference for build systems <../reference/build_systems>`
        Complete documentation on all available options, variables, etc.

Build systems provide a convenient way to pass arguments and environment
information to external programs. Use build systems if you need to run your
files through build programs like ``make``, command line utilities like
``tidy``, interpreters, etc.

.. note::
    The program you want to call from a build system must be in your ``PATH``.


File Format
***********

Like many other configuration files in Sublime Text, build systems use JSON.
Build systems have the extension ``sublime-build`` and must be located somewhere
under the ``Packages`` folder (e.g. ``Packages/User``).

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
    Required. This option contains the actual command line that will be executed;
    in this case::

        python -u /path/to/current/file.ext

``file_regex``
    A Perl-style regular expression to capture the external program's output and
    extract error information. This information is then used to help you move
    through errors with ``F4``.

``selector``
    If the **Tools | Build System | Automatic** option is set, this option's value
    will be used to determine whether the build system should be used for your file.

In addition to options, you can use variables in build systems too, like we've
done above with ``$file``, which expands to the full path of the file underlying
the active buffer.


Running Build Systems
*********************

Build systems can be run by pressing ``F7`` or from the menu
(**Tools | Build**).
