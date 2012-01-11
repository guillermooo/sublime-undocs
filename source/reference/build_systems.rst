Build Systems
=============

Build systems let you run your files through external programs and see the
output they generate within Sublime Text.

Build systems consist of two --or optionally three-- parts:

* configuration data in JSON format (the `.sublime-build` file contents)
* a Sublime Text command driving the build process
* optionally, an external executable file (script, binary file)

Essentially, ``.sublime-build`` files are configuration data for an external
program as well as for the Sublime Text command just mentioned. In them, you
specify the switches, options and environment information you want forwarded.

The Sublime Text command then receives the data stored in the `.sublime-build`
file. At this point, it can do whatever it needs to *build* the files. By
default, build systems will use the ``exec`` command, implemented in
``Packages/Default/exec.py``. As we'll explain below, you can override this
command.

Lastly, the external program may be a shell script you've created to process
your files, or a well-known utility like ``make`` or ``tidy``.

Note that build systems need not call any external program at all if there
isn't any reason to; you could implement a build system entirely in a
Sublime Text command. Similarly, build systems don't need to process any files;
they can simply be used to launch programs too, like a calculator.


File Format
***********

``.build-system`` files use JSON. Here's an example:

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
    specify an absolute path, the external program will be searched in your
    ``PATH``, one of your system's environmental variables.

    On Windows, GUIs are supressed.

``file_regex``
    Optional. Regular expression (Perl-style) to capture error output of
    ``cmd``. See the next section for details.

``line_regex``
    Optional. If ``file_regex`` doesn't match on the current line, but
    ``line_regex`` exists, and it does match on the current line, then
    walk backwards through the buffer until a line matching ``file regex`` is
    found, and use these two matches to determine the file and line to go to.

``selector``
    Optional. Used when **Tools | Build System | Automatic** is set to ``true``.
    Sublime Text uses this scope selector to find the appropriate build system
    for the active view.

``working_dir``
    Optional. Directory to change the current directory to before running ``cmd``.
    The original current directory is restored afterwards.

``encoding``
    Optional. Output encoding of ``cmd``. Must be a valid python encoding.
    Defaults to ``UTF-8``.

``target``
    Optional. Sublime Text command to run. Defaults to ``exec`` (``Packages/Default/exec.py``).
    This command receives the configuration data specified in the ``.build-system`` file.

    Used to override the default build system command. Note that if you choose
    to override the default command for build systems, you can add arbitrary
    variables in the ``.sublime-build`` file.

``env``
    Optional. Dictionary of environment variables to be merged with the current
    process' before passing them to ``cmd``.

    Use this element, for example, to add or modify environment variables
    without modifying your system's settings.

``shell``
    Optional. If ``true``, ``cmd`` will be run through the shell (``cmd.exe``, ``bash``\ …).

``path``
    Optional. This string will replace the current process' ``PATH`` before
    calling ``cmd``. The old ``PATH`` value will be restored after that.

    Use this option to add directories to ``PATH`` without having to modify
    your system's settings.

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

The ``windows``, ``osx`` and ``linux`` elements let you provide
platform-specific data in the build system. Here's an example::


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

Build systems expand the following variables in ``.sublime-build`` files:

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


.. _troubleshooting-build-systems:

Troubleshooting Build Systems
*****************************

Build systems will look for executables in your ``PATH``, unless you specify
an absolute path to the executable. Therefore, your ``PATH`` variable must be
correctly set.

On some operating systems, the value for ``PATH`` will vary from a terminal
window to a graphical application. Thus, even if the command you are using in
your build system works in the command line, it may not work from Sublime Text.
This is due to user profiles in shells.

To solve this issue, make sure you set the desired ``PATH`` so that graphical
applications such as Sublime Text can find it. See the links below for more
information.

Alternatively, you can use the ``path`` element in ``.sublime-build`` files
to override the ``PATH`` used to locate the executable specified in ``cmd``.
This new value for ``PATH`` will only be in effect for as long as your
build system is running. After that, the old ``PATH`` will be restored.

.. seealso::

    `Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
        Search Microsoft knowledge base for this topic.

    `Setting environment variables in OSX <http://stackoverflow.com/q/135688/1670>`_
        StackOverflow topic.
