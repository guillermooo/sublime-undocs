Build Systems
=============

See `Build Systems <http://www.sublimetext.com/docs/build>`_.

.. warning::

    This topic is only valid for Sublime Text X.

define
    run command line utilities
    build stuff, test ??, launch external console progs (tidy)

options
    cmd
        Required. Command to be run. The executable must be on your ``PATH``.
    file_regex
        Captures build errors and extracts information to enable you to cycle
        through errors by pressing ``F4``. **EXPLAIN 4 FIELDS PCRE?**
    selector
        Determines in which scope the build system will be active.
    working_dir
        If set, the current directory is changed to point to this location
        before running ``cmd``.

variables:
    $file
    $file_dir
    $file_name
    $file_ext
    $basename
    $project_dir
    $project_name

Snippet formatting. **EXPLAIN AND REFER TO SNIPPETS**.

alternatives
    plugin, subprocess, exec command?

limitations
    no windowed programs
