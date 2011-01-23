Build Systems
=============

.. warning::

    This topic is a draft.

**The specifics of this topic target Sublime Text X.**

Build systems run external programs to process your project's files and show
captured output.

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

=============== ====================================================================================================
``cmd``         Array containing the command to run and its desired arguments.
``file_regex``  Regular expression to capture error output of ``cmd``.
``selector``    Used when **Tools | Build System | Automatic** is set for automatic discovery based on file's scope.
``working_dir`` Directory to change the current directory to before running ``cmd``.
``encoding``    Output encoding of ``cmd``. Must be a valid python encoding. Defaults to ``utf-8``.
=============== ====================================================================================================

Capturing Error Output with ``file_regex``
------------------------------------------

The ``file_regex`` option uses a Perl-style regular expression to capture up to
four fields of error information from the build program's standard streams, namely:
**file name**, **line number**, **column number** and **error message**. Use groups
in the pattern to capture this information.

When error information is captured, you can cycle through error instances in your
project's files with ``F4`` and ``SHIFT + F4``. The captured error message will
be shown in the status bar.


Variables
*********

====================== =====================================================================================
``$file``              The full path to the current file, e.g., ``C:\Files\Chapter1.txt``.
``$file_path``         The directory of the current file, e.g., ``C:\Files``.
``$file_name``         The name portion of the current file, e.g., ``Chapter1.txt``.
``$file_extension``    The extension portion of the current file, e.g., ``txt``.
``$file_base_name``    The name only portion of the current file, e.g., ``Document``.
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

Select **Tools | Build** in the Sublime Text X menu or press ``F7``.

Troubleshooting
***************

External programs used in build systems need to be in your ``PATH``. As a quick test, you
can try to run them from the command line first and see whether they work. However,
note that your shell's ``PATH`` variable might differ to that seen by Sublime Text X due
to your shell's profile.

At the moment (v. 20110123), new build systems require Sublime Text X to be restarted before
they can appear under **Tools | Build System**.
