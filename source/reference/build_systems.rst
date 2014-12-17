=============
Build Systems
=============


Overview
========

Using build systems, you can run files
through external programs
without leaving Sublime Text,
and see the output they generate.

.. note::

    *Build* is used in a broad sense.
    A build system doesn't need to generate
    a compiled executable---it could simply
    format code, run an interpreter, etc.


Build System Basics
===================

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
in the form of a JSON object.
This file is used to specify
switches, options and environmental data.
Each ``.sublime-build`` file
is normally associated with a specific scope.

The file name is ignored by Sublime Text.


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
Often, it interacts
with an external program.
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
As we'll see further below,
this command can be overriden
by modifying the ``target`` option
in a ``.build-system`` file.


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


Meta Options in Build Systems
=============================

This is a list of standard options
that all build systems understand.
These options are used internally
by Sublime Text.
The ``target`` command does not
receive any of these options.

``target``
    Optional. A Sublime Text ``WindowCommand``.
    Defaults to ``exec`` (:file:`Packages/Default/exec.py`).
    This command receives
    all the target command arguments specified
    in the ``.sublime-build`` file (as ``**kwargs``).

    Used to override the default build system command.
    Note that
    if you choose
    to override the default command
    for build systems,
    you can add any number of extra options
    to the ``.sublime-build`` file.

``selector``
    Optional. Used when **Tools | Build System | Automatic**
    is set to ``true``.
    Sublime Text uses this scope selector
    to find the appropriate build system
    for the active view.

``windows``, ``osx`` and ``linux``
    Optional. Used to selectively apply options by OS.
    OS-specific values override defaults.
    Each of the listed items
    accepts a dictionary of options.

    See `Platform-specific Options`_.

``variants``
    Optional. A list of dictionaries of options.
    Variant names will appear in the Command Palette
    for easy access if the build system's selector
    matches for the active file.

    Using variants it's possible
    to specify multiple build system tasks
    in the same ``.sublime-build`` file.

    See Variants_.

``name``
    **Only valid inside a variant**.

    Identifies a build system task.
    If the ``name`` is *Run*,
    the variant will show up
    under **Tools | Build System**.
    Sublime Text will also automatically bind this
    task to :kbd:`Ctrl+Shift+B`.

    See Variants_.

.. _build-arbitrary-options:


Target Command Arguments
************************

Thanks to the ``target`` setting,
which overrides the default ``exec`` command
with any other command of your choice,
a build system may contain
any number of custom arguments
that the new ``target`` command accepts.


``exec`` Command Arguments
**************************

All the options below
are related to the ``exec`` command
(see also :ref:`Exec Command Reference <cmd-exec>`).
If you change the ``target`` command,
these options can no longer be relied on
(see `Target Command Arguments`_ for details).

``cmd``
    Required.

    Overriden by ``shell_cmd``.

    Array containing the command to run
    and its desired arguments.
    If you don't specify an absolute path,
    the external program
    will be searched in your :const:`PATH`.

    On Windows, GUIs are supressed.

    ``shell_cmd`` and ``cmd`` are mutually
    exclusive. ``shell_cmd`` has precedence
    over ``cmd``.

``shell_cmd``
    Optional.

    Overrides ``cmd`` if used.

    A string that specifies
    the command to be run
    and its arguments.

    It should help in getting right
    invocations involving complex uses
    of quotation marks.

    ``shell_cmd`` and ``cmd`` are mutually
    exclusive. ``shell_cmd`` has precedence
    over ``cmd``.

``file_regex``
    Optional.

    Regular expression (Perl-style)
    to capture error output of ``cmd``.
    See the next section for details.

``line_regex``
    Optional.

    If ``file_regex`` doesn't match
    on the current line,
    but ``line_regex`` exists,
    and it does match on the current line,
    then walk backwards through the buffer
    until a line matching ``file regex`` is found,
    and use these two matches
    to determine the file and line to go to.

``working_dir``
    Optional.

    Directory to change
    the current directory to
    before running ``cmd``.
    The original current directory
    is restored afterwards.

``encoding``
    Optional.

    Output encoding of ``cmd``.
    Must be a valid Python encoding.
    Defaults to ``UTF-8``.

``env``
    Optional.

    Dictionary of environment variables
    to be merged with the current process'
    before passing them to ``cmd``.

    Use this option, for example,
    to add or modify environment variables
    without modifying your system's settings.

    Environmental variables
    will be expanded.

``shell``
    Optional.

    If ``true``, ``cmd``
    will be run through the shell
    (``cmd.exe``, ``bash``...).

    If ```shell_cmd`` is used,
    this option has no effect.

``path``
    Optional.

    :const:`PATH` used
    by the ``cmd`` subprocess.

    Use this option
    to add directories to :const:`PATH`
    without having to modify
    your system's settings.

    Environmental variables
    will be expandend.

``syntax``
    Optional.

    If provided,
    it will be used to colorize
    the build system's output.


.. _build-capture-error-output:

Capturing Error Output with ``file_regex``
******************************************

The ``file_regex`` option
uses a Perl-style regular expression
to capture up to four fields of error information
from the build program's output, namely:
*filename*, *line number*, *column number* and *error message*.
Use groups in the pattern
to capture this information.
The *filename* field and
the *line number* field are required.

When error information is captured,
you can navigate to error instances
in your project's files with :kbd:`F4` and :kbd:`Shift+F4`.
If available, the captured *error message*
will be displayed in the status bar.


Platform-specific Options
*************************

The ``windows``, ``osx`` and ``linux`` elements
let you provide platform-specific data
in the build system.
Here's an example:

.. sourcecode:: javascript

    {
        "cmd": ["ant"],
        "file_regex": "^ *\\[javac\\] (.+):([0-9]+):() (.*)$",
        "working_dir": "${project_path:${folder}}",
        "selector": "source.java",

        "windows": {
            "cmd": ["ant.bat"]
        }
    }

In this case, ``ant`` will be executed
for every platform except Windows,
where ``ant.bat`` will be used instead.


Variants
********

Here's a contrived example
of a build system with variants:

.. sourcecode:: javascript

    {
        "selector": "source.python",
        "cmd": ["date"],

        "variants": [

            { "name": "List Python Files",
              "cmd": ["ls -l *.py"],
              "shell": true
            },

            { "name": "Word Count (current file)",
              "cmd": ["wc", "$file"]
            },

            { "name": "Run",
              "cmd": ["python", "-u", "$file"]
            }
        ]
    }


Given these settings,
:kbd:`Ctrl+B` would run the *date* command,
:kbd:`Crtl+Shift+B` would run the Python interpreter
and the remaining variants would appear
in the :ref:`Command Palette <ext-command-palette-overview>`
as :samp:`Build: {name}` whenever the build system was active.

.. _build-system-variables:

Build System Variables
----------------------

Build systems expand the following variables
in ``.sublime-build`` files:

====================== =====================================================================================
``$file_path``         The directory of the current file, e.g., *C:\\Files*.
``$file``              The full path to the current file, e.g., *C:\\Files\\Chapter1.txt*.
``$file_name``         The name portion of the current file, e.g., *Chapter1.txt*.
``$file_extension``    The extension portion of the current file, e.g., *txt*.
``$file_base_name``    The name-only portion of the current file, e.g., *Document*.
``$packages``          The full path to the *Packages* folder.
``$project``           The full path to the current project file.
``$project_path``      The directory of the current project file.
``$project_name``      The name portion of the current project file.
``$project_extension`` The extension portion of the current project file.
``$project_base_name`` The name-only portion of the current project file.
====================== =====================================================================================

Placeholders for Variables
**************************

Features found in snippets
can be used with these variables.
For example::

    ${project_name:Default}

This will emit the name of the current project
if there is one, otherwise ``Default``.

::

    ${file/\.php/\.txt/}

This will emit
the full path of the current file,
replacing *.php* with *.txt*.

.. seealso::

    :doc:`/extensibility/snippets`
        Documentation on snippet variables.


Running Build Systems
*********************

Select the desired build system
from **Tools | Build System**,
and then select **Tools | Build**.
Alternatively, you can use
the command palette or
the following key bindings:


===================  ========================
:kbd:`Ctrl+B`        Run default build task
:kbd:`F7`            Run default build task
:kbd:`Ctrl+Shift+B`  Run *Run* build task
:kbd:`Ctrl+Break`    Cancel build task
===================  ========================

See `Variants`_.


.. _troubleshooting-build-systems:

Troubleshooting Build Systems
*****************************

Build systems will look for executables
in your :const:`PATH`.
Therefore, your :const:`PATH`
variable must be correctly set.

On some operating systems,
the value of :const:`PATH`
may vary between terminal windows
and graphical applications.
Thus, depending how you start Sublime Text,
the build system may or may not work.

To solve this issue,
make sure you set the :const:`PATH`
so that graphical applications such as Sublime Text
can find it.
See the links below
for more information.

Alternatively, you can use the ``path`` option
in a ``.sublime-build`` file
to override the :const:`PATH` used to locate
the executable specified in ``cmd``.

.. seealso::

    `Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
        Search Microsoft knowledge base for this topic.

    `Setting environment variables in OSX <http://stackoverflow.com/q/135688/1670>`_
        StackOverflow topic.
