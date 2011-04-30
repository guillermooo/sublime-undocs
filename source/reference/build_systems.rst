Build Systems
=============


Build systems run external programs to process your project's files and print
captured output to the output panel. Ultimately, they call ``subprocess.Popen``.


File Format
***********

Build systems use JSON. Here's an example build system:

.. sourcecode:: python

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }


Options
*******

``cmd``
    Array containing the command to run and its desired arguments.

    .. note::
        Under Windows, GUIs are supressed.

``file_regex``
    Optional. Regular expression to capture error output of ``cmd``.

``line_regex``
    If the ``file_regex`` doesn't match on the current line, but there's a
    ``line_regex`` specified, and it does match the current line, then walk
    backwards through the buffer until a line matching the file regex is found:
    use these two matches to determine the file and line to go to.

``selector``
    Optional. Used when **Tools | Build System | Automatic** is set to ``true``.
    Sublime Text uses this scope selector to find the appropriate build system
    for the active view.

``working_dir``
    Optional. Directory to change the current directory to before running ``cmd``.

``encoding``
    Optional. Output encoding of ``cmd``. Must be a valid python encoding. Defaults to ``utf-8``.

``target``
    Optional. Sublime Text command to run. Defaults to ``exec`` (``Packages/Default/exec.py``).

``env``
    Optional. Dictionary of environment variables to be merged with the current
    process' that will be passed to ``cmd``.

``shell``
    If ``true``, ``cmd`` will be run through the shell (``cmd.exe``, ``bash``…).

``path``
    This string will replace the current process' ``PATH`` before calling ``cmd``.
    The old ``PATH`` value will be restored after that.

Capturing Error Output with ``file_regex``
------------------------------------------

The ``file_regex`` option uses a Perl-style regular expression to capture up
to four fields of error information from the build program's output, namely:
*file name*, *line number*, *column number* and *error message*. Use
groups in the pattern to capture this information. The *file name* field and
the *line number* field are required.

When error information is captured, you can navigate to error instances in
your project's files with ``F4`` and ``SHIFT + F4``. If available, the captured
*error message* will be displayed in the status bar.

Platform-specific Options
-------------------------

``windows``, ``osx`` and ``linux`` are additional options which override any
build system options for the corresponding platform only. Here's an example::


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

In this case, ``ant.bat`` will be executed under Windows, while for the other
platforms ``ant`` will be used instead.


Variables
*********

====================== =====================================================================================
``$file``              The full path to the current file, e.g., ``C:\Files\Chapter1.txt``.
``$file_path``         The directory of the current file, e.g., ``C:\Files``.
``$file_name``         The name portion of the current file, e.g., ``Chapter1.txt``.
``$file_extension``    The extension portion of the current file, e.g., ``txt``.
``$file_base_name``    The name only portion of the current file, e.g., ``Document``.
``$packages``          The full path to the ``Packages`` folder. 
``$project``           The full path to the current project file.
``$project_path``      The directory of the current project file.
``$project_name``      The name portion of the current project file.
``$project_extension`` The extension portion of the current project file.
``$project_base_name`` The name only portion of the current project file.
====================== =====================================================================================

Variable Place Holders
----------------------

Snippet style formatting can be used with these variables, for example::

    ${project_name:Default}

This will emit the name of the current project if there is one, otherwise *Default*.

::

    ${file/\.php/\.txt/}

This will emit the full path of the current file, replacing *.php* with *.txt*.

Running Build Systems
*********************

Select **Tools | Build** in the Sublime Text menu or press ``F7``.


Troubleshooting Build Systems
*****************************

External programs used in build systems need to be in your ``PATH``. As a
quick test, you can try to run them from the command line first and see whether
they work. However, note that your shell's ``PATH`` variable might differ to
that seen by Sublime Text due to your shell's profile.

.. seealso::
	
	`Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
		Search Microsoft for this topic.
	