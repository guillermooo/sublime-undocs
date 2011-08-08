Build Systems
=============

Build systems run external programs to process your files, and print their
output to the output panel. Ultimately, they call ``subprocess.Popen``.

Essentially, build systems are configuration data for an external program. In
them, you specify the switches, options and environment information you want
passed to the executable.

Optionally, you can override the default *middleman* between the configuration
data and the external program. For example, you could implement the build
system entirely in a Sublime Text plugin, without ever calling an external
program. You can do this because this *middleman* is simply a Sublime Text
plugin, implemented in ``Packages/Default/exec.py``.


File Format
***********

Build systems use JSON. Here's an example:

.. sourcecode:: python

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }


Options
*******

``cmd``
    Array containing the command to run and its desired arguments. If you don't
    specify an absolute path, the external program must be in your ``PATH``, one
    of your system's environmental variables.

    .. XXX Is this still true?
    .. note::
        Under Windows, GUIs are supressed.

.. XXX Cross-reference properly to next section.
``file_regex``
    Optional. Regular expression (Perl-style) to capture error output of
    ``cmd``. See next section for more details.

``line_regex``
    Optional. If ``file_regex`` doesn't match on the current line, but
    ``line_regex`` is specified, and it does match on the current line, then
    walk backwards through the buffer until a line matching ``file regex`` is
    found, and use these two matches to determine the file and line to go to.

``selector``
    Optional. Used when **Tools | Build System | Automatic** is set to ``true``.
    Sublime Text uses this scope selector to find the appropriate build system
    for the active view automatically.

``working_dir``
    Optional. Directory to change the current directory to before running ``cmd``.
    The original current directory is restored afterwards.

``encoding``
    Optional. Output encoding of ``cmd``. Must be a valid python encoding.
    Defaults to ``UTF-8``.

``target``
    Optional. Sublime Text command to run. Defaults to ``exec`` (``Packages/Default/exec.py``).
    It receives the configuration data specified in the ``.build-system`` file.

``env``
    Optional. Dictionary of environment variables to be merged with the current
    process' that will be passed to ``cmd``.

``shell``
    Optional. If ``true``, ``cmd`` will be run through the shell (``cmd.exe``, ``bash``\ …).

``path``
    Optional. This string will replace the current process' ``PATH`` before
    calling ``cmd``. The old ``PATH`` value will be restored after that. It's
    useful to add directories to ``PATH`` that you don't have or want in your
    regular ``PATH`` variable everywhere.

Capturing Error Output with ``file_regex``
------------------------------------------

The ``file_regex`` option uses a Perl-style regular expression to capture up
to four fields of error information from the build program's output, namely:
*file name*, *line number*, *column number* and *error message*. Use
groups in the pattern to capture this information. The *file name* field and
the *line number* field are required.

When error information is captured, you can navigate to error instances in
your project's files with ``F4`` and ``Shift+F4``. If available, the captured
*error message* will be displayed in the status bar.

Platform-specific Options
-------------------------

``windows``, ``osx`` and ``linux`` are additional options to provide
platform-specific data. Here's an example::


    {
        "cmd": ["ant"],
        "file_regex": "^ *\\[javac\\] (.+):([0-9]+):() (.*)$",
        "working_dir": "${project_path:${folder}}",
        "selector": "source.java",
    
        "windows":
        {
            "cmd": ["ant.bat"]
        }
    }

In this case, ``ant`` will be executed for every platform except Windows, where
``ant.bat`` will be used instead.


Variables
*********

Build systems expand the following variables:

====================== =====================================================================================
``$file``              The full path to the current file, e. g., ``C:\Files\Chapter1.txt``.
``$file_path``         The directory of the current file, e. g., ``C:\Files``.
``$file_name``         The name portion of the current file, e. g., ``Chapter1.txt``.
``$file_extension``    The extension portion of the current file, e. g., ``txt``.
``$file_base_name``    The name only portion of the current file, e. g., ``Document``.
``$packages``          The full path to the ``Packages`` folder. 
``$project``           The full path to the current project file.
``$project_path``      The directory of the current project file.
``$project_name``      The name portion of the current project file.
``$project_extension`` The extension portion of the current project file.
``$project_base_name`` The name only portion of the current project file.
====================== =====================================================================================

Place Holders for Variables
---------------------------

Features found in snippets can be used with these variables. For example::

    ${project_name:Default}

This will emit the name of the current project if there is one, otherwise *Default*.

::

    ${file/\.php/\.txt/}

This will emit the full path of the current file, replacing *.php* with *.txt*.

Running Build Systems
*********************

Select the desired build system from **Tools | Build System**, and then select
**Tools | Build** or press ``F7``.


Troubleshooting Build Systems
*****************************

External programs used in build systems need to be in your ``PATH``. As a
quick test, you can try to run them from the command line first and see whether
they work. Note, however, that your shell's ``PATH`` variable might differ to
that seen by Sublime Text due to your shell's profile. Remember that you can
use the ``path`` option in a ``.build-system`` file to add directories to
``PATH`` without changing your system's settings.

.. seealso::
	
	`Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
		Search Microsoft for this topic.
	