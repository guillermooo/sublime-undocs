=============
Build Systems
=============

Build systems let you run your files through external programs without leaving
Sublime Text, and see the output they generate.

Build systems consist of one --or optionally three-- parts:

* configuration data in JSON format (the *.sublime-build* file contents)
* optionally, a Sublime Text command driving the build process
* optionally, an external executable file (script, binary file)

Essentially, *.sublime-build* files are configuration data for an external
program, as well as for a Sublime Text command (just mentioned). In them, you
specify the switches, options and environment information you want forwarded.

The Sublime Text command then receives the data stored in the *.sublime-build*
file. At this point, it can do whatever it needs to do to *build* the files. By
default, build systems will use the ``exec`` command implemented by
:file:`Packages/Default/exec.py`. As explained below, you can override this
command.

Finally, the external program may be a shell script you've created to process
your files, or a well-known utility like ``make`` or ``tidy``. Usually, these
executable files will receive paths to files or directories, along with
switches and options to run with.

Note that build systems can but don't need to call external programs; a valid
build system could be implemented entirely in Python in a Sublime Text
command.


File Format
***********

*.build-system* files use JSON. Here's an example:

.. sourcecode:: javascript

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }


Options
*******

Build system-specific options
-----------------------------

These options are standard for all build systems.

``target``
    Optional. Sublime Text command to run. Defaults to ``exec``.
    (:file:`Packages/Default/exec.py`). This command receives the full
    configuration data specified in the *.build-system* file (as ``**kwargs``).

    Used to override the default build system command. Note that if you choose
    to override the default command for build systems, you can add arbitrary
    variables in the *.sublime-build* file.

``selector``
    Optional. Used when **Tools | Build System | Automatic** is set to ``true``.
    Sublime Text uses this scope selector to find the appropriate build system
    for the active view.

``windows``, ``osx`` and ``linux``
    Optional. Allow specification of OS-specific options which will override the
    default settings. These accept a dict of `Arbitrary options`_ each.

    See `Platform-specific Options`_.

``variants``
    Optional. A list of dictionaries of options to override the main build
    system's options. Variant names will appear in the Command Palette for easy
    access if the build system's selector matches for the active file.

    See Variants_.

``name``
    **Only valid inside a variant** (see ``variants``). Identifies variant
    build systems. If ``name`` is *Run*, the variant will show up under the
    **Tools | Build System** menu and be bound to :kbd:`Ctrl+Shift+B`.


.. _build-arbitrary-options:

Arbitrary options
-----------------

Due to the ``target`` setting a build system can contain literally any option
(key) that is not one of the options already listed above.

Please note that all the options below are from the default implementation of
``exec`` (see :ref:`exec command <cmd-exec>`). If you change the ``target`` option, these can no longer be relied on.

``cmd``
    Array containing the command to run and its desired arguments. If you don't
    specify an absolute path, the external program will be searched in your
    :const:`PATH`, one of your system's environmental variables.

    On Windows, GUIs are supressed.

``file_regex``
    Optional. Regular expression (Perl-style) to capture error output of
    ``cmd``. See the next section for details.

``line_regex``
    Optional. If ``file_regex`` doesn't match on the current line, but
    ``line_regex`` exists, and it does match on the current line, then
    walk backwards through the buffer until a line matching ``file regex`` is
    found, and use these two matches to determine the file and line to go to.

``working_dir``
    Optional. Directory to change the current directory to before running
    ``cmd``. The original current directory is restored afterwards.

``encoding``
    Optional. Output encoding of ``cmd``. Must be a valid python encoding.
    Defaults to ``utf-8``.

``env``
    Optional. Dictionary of environment variables to be merged with the current
    process' before passing them to ``cmd``.

    Use this element, for example, to add or modify environment variables
    without modifying your system's settings.

``shell``
    Optional. If ``true``, ``cmd`` will be run through the shell (``cmd.exe``, ``bash``\ ...).

``path``
    Optional. This string will replace the current process's :const:`PATH`
    before calling ``cmd``. The old :const:`PATH` value will be restored after
    that.

    Use this option to add directories to :const:`PATH` without having to modify
    your system's settings.


.. _build-capture-error-output:

Capturing Error Output with ``file_regex``
------------------------------------------

The ``file_regex`` option uses a Perl-style regular expression to capture up
to four fields of error information from the build program's output, namely:
*filename*, *line number*, *column number* and *error message*. Use
groups in the pattern to capture this information. The *filename* field and
the *line number* field are required.

When error information is captured, you can navigate to error instances in your
project's files with :kbd:`F4` and :kbd:`Shift+F4`. If available, the captured
*error message* will be displayed in the status bar.


Platform-specific Options
-------------------------

The ``windows``, ``osx`` and ``linux`` elements let you provide
platform-specific data in the build system. Here's an example:

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

In this case, ``ant`` will be executed for every platform except Windows,
where ``ant.bat`` will be used instead.


Variants
--------

Here's a contrived example of a build system with variants

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


Given these settings, :kbd:`Ctrl+B` would run the *date* command,
:kbd:`Crtl+Shift+B` would run the Python interpreter and the remaining variants
would appear in the :ref:`Command Palette <ext-command-palette-overview>` as
:samp:`Build: {name}` whenever the build system was active.


.. _build-system-variables:

Build System Variables
**********************

Build systems expand the following variables in *.sublime-build* files:

====================== =====================================================================================
``$file_path``         The directory of the current file, e. g., *C:\\Files*.
``$file``              The full path to the current file, e. g., *C:\\Files\\Chapter1.txt*.
``$file_name``         The name portion of the current file, e. g., *Chapter1.txt*.
``$file_extension``    The extension portion of the current file, e. g., *txt*.
``$file_base_name``    The name only portion of the current file, e. g., *Document*.
``$packages``          The full path to the *Packages* folder.
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

This will emit the name of the current project if there is one, otherwise
``Default``.

::

    ${file/\.php/\.txt/}

This will emit the full path of the current file, replacing *.php* with *.txt*.

.. seealso::

    :doc:`/extensibility/snippets`
        Documentation on snippets and their variable features.


Running Build Systems
*********************

Select the desired build system from **Tools | Build System**, and then select
**Tools | Build** or press :kbd:`F7`.


.. _troubleshooting-build-systems:


Troubleshooting Build Systems
*****************************

Build systems will look for executables in your :const:`PATH`, unless you
specify an absolute path to the executable. Therefore, your :const:`PATH`
variable must be correctly set.

On some operating systems, the value for :const:`PATH` will vary from a terminal
window to a graphical application. Thus, even if the command you are using in
your build system works in the command line, it may not work from Sublime Text.
This is due to user profiles in shells.

To solve this issue, make sure you set the desired :const:`PATH` so that
graphical applications such as Sublime Text can find it. See the links below for
more information.

Alternatively, you can use the ``path`` key in *.sublime-build* files to
override the :const:`PATH` used to locate the executable specified in ``cmd``.
This new value for :const:`PATH` will only be in effect for as long as your
build system is running. After that, the old :const:`PATH` will be restored.

.. seealso::

    `Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
        Search Microsoft knowledge base for this topic.

    `Setting environment variables in OSX <http://stackoverflow.com/q/135688/1670>`_
        StackOverflow topic.
