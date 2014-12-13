=============
Build Systems
=============

Overview
========

Using build systems, you can run files
through external programs
without leaving Sublime Text,
and see the output they generate.

Build systems consist of one
--or optionally three-- parts:

* Configuration data in JSON format (the *.sublime-build* file content)
* Optionally, a custom Sublime Text command driving the build process
* Optionally, an external executable file (script or binary file)

A *.sublime-build* file
contains configuration data
in the form of a JSON object.
This file is used to specify
switches, options and environment information
you want forwarded.

When you run a build action in Sublime Text
(usually, by pressing :kbd:`Ctrl+B`),
a Sublime Text command receives
this configuration data.
The command then does whatever it needs
to *build* the files.
Often, it interacts
with an external program.

By default, build systems will use
the ``exec`` command implemented by :file:`Packages/Default/exec.py`.
As we'll explain below, however,
this command can be overriden.

Finally, the external program
that processes the files
may be a custom shell script
or a well-known utility like ``make`` or ``tidy``.
=======
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


The Sublime Text Command Used in Build Systems
**********************************************

When you run
the default build action in Sublime Text
(:kbd:`Ctrl+B`),
a Sublime Text command receives
the configuration data
specified in the ``.sublime-build`` file.
The command then *builds* the files.
Often, it interacts
with an external program.
By default, the command
used in build systems is called ``excec``.


The ``target`` Option
---------------------

By default, build systems use
the ``exec`` command implemented by :file:`Packages/Default/exec.py`.
This command simply forwards configuration data
to an external program
and runs it asynchronously.
As we'll see further below,
this command can be overriden
by modifying the ``target`` option
in a ``.build-system`` file.


Interaction with External Programs
**********************************

A build system may interact
with an external program
to process files.
This program may be
a custom shell script
or a standard utility like ``make`` or ``tidy``.
Usually, this executable
receives paths to files or directories,
along with switches and options
that configure its behavior.

.. note::

    Build systems can but don't need to
    call external programs---a build system
    could be implemented entirely
    as a Sublime Text command.


Format
------

``.sublime-build`` files use JSON.
The file name is ignored by Sublime Text.


Example
-------

.. sourcecode:: javascript

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }


Predefined Options in Build Systems
***********************************

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
    **Only valid inside a variant** (see Variants_).

    Identifies variant build systems.
    If the ``name`` is *Run*,
    the variant will show up
    under the **Tools | Build System**.
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
    Required. Array containing the command to run
    and its desired arguments.
    If you don't specify an absolute path,
    the external program
    will be searched in your :const:`PATH`.

    On Windows, GUIs are supressed.

    ``shell_cmd`` and ``cmd`` are mutually
    exclusive. ``shell_cmd`` has precedence
    over ``cmd``.

``shell_cmd``
    Required. A string that specifies
    the command to be run
    and its arguments.

    It should help in getting right
    invocations involving complex uses
    of quotation marks.

    ``shell_cmd`` and ``cmd`` are mutually
    exclusive. ``shell_cmd`` has precedence
    over ``cmd``.

``file_regex``
    Optional. Regular expression (Perl-style)
    to capture error output of ``cmd``.
    See the next section for details.

``line_regex``
    Optional. If ``file_regex`` doesn't match
    on the current line,
    but ``line_regex`` exists,
    and it does match on the current line,
    then walk backwards through the buffer
    until a line matching ``file regex`` is found,
    and use these two matches
    to determine the file and line to go to.

``working_dir``
    Optional. Directory to change
    the current directory to
    before running ``cmd``.
    The original current directory
    is restored afterwards.

``encoding``
    Optional. Output encoding of ``cmd``.
    Must be a valid Python encoding.
    Defaults to ``UTF-8``.

``env``
    Optional. Dictionary of environment variables
    to be merged with the current process'
    before passing them to ``cmd``.

    Use this option, for example,
    to add or modify environment variables
    without modifying your system's settings.

``shell``
    Optional. If ``true``, ``cmd``
    will be run through the shell
    (``cmd.exe``, ``bash``...).

    If ```shell_cmd`` is used,
    this option has no effect.

``path``
    Optional. This string will replace
    the current process' :const:`PATH`
    before calling ``cmd``.

    Use this option
    to add directories to :const:`PATH`
    without having to modify
    your system's settings.

``syntax``
    Optional. If provided,
    it will be used to format
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
the following key bindings:


===================  ========================
:kbd:`Ctrl+B`        Run default build task
:kbd:`F7`            Run default build task
:kbd:`Ctrl+Shift+B`  Run *Run* build task
===================  ========================

See `Variants`_.


.. _troubleshooting-build-systems:

Troubleshooting Build Systems
*****************************

Build systems will look for executables
in your :const:`PATH`,
unless you specify an absolute path
to the executable.
Therefore, your :const:`PATH`
variable must be correctly set.

On some operating systems,
the value of :const:`PATH`
may vary between terminal windows and graphical applications.
Thus, in your build system,
even if the command you are using
works in the command line,
it may not work from Sublime Text.
This is due to user profiles in shells.

To solve this issue,
make sure you set the desired :const:`PATH`
so that graphical applications such as Sublime Text
can find it.
See the links below
for more information.

Alternatively, you can use the ``path`` key
in ``.sublime-build`` files
to override the :const:`PATH` used to locate
the executable specified in ``cmd``.
This new value for :const:`PATH`
will be in effect only
as long as your build system is running.
After that, the old :const:`PATH` will be restored.

.. seealso::

    `Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
        Search Microsoft knowledge base for this topic.

    `Setting environment variables in OSX <http://stackoverflow.com/q/135688/1670>`_
        StackOverflow topic.
